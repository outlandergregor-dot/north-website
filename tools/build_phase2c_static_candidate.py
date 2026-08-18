#!/usr/bin/env python3
"""Build the offline, public-safe NORTH Phase 2C static release candidate. No deploy action."""
from __future__ import annotations
from pathlib import Path
import hashlib
import json
import shutil
import zipfile

ROOT = Path('/home/ubuntu/north-phase2c')
OUT = ROOT / 'release-candidate' / 'NORTH_PHASE2C_STATIC_RELEASE_CANDIDATE'
WEB = OUT / 'website'
LOCALES = ['pt-BR','es-419','fr','de','it','ja','ko','zh-Hans','zh-Hant','ar','ru','pl','nl']

PUBLIC_ROOT = ['index.html','library.html','library-resources.html','library-programs.html','library-books.html','library-money-education.html','library-item.html','about.html','library-free-tools.html']
PUBLIC_ASSETS = ['public-site.css','public-site.js','public-catalog.js','locale-system.js','free-tools-config.js','library.js','library.css']

HTACCESS = '''# NORTH Phase 2C static release candidate — Apache / Namecheap shared hosting.
# Candidate safety: no deployment has occurred. Keep the noindex header until founder-approved public launch.
DirectoryIndex index.html
Options -Indexes
RewriteEngine On

# Preserve direct files, directories, and static assets.
RewriteCond %{REQUEST_FILENAME} -f [OR]
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^ - [L]

# Canonical English clean routes.
RewriteRule ^$ index.html [L]
RewriteRule ^library/?$ library/index.html [L]
RewriteRule ^library/free-tools/?$ library/free-tools/index.html [L]
RewriteRule ^library/resources/?$ library/resources/index.html [L]
RewriteRule ^library/programs/?$ library/programs/index.html [L]
RewriteRule ^library/books/?$ library/books/index.html [L]
RewriteRule ^library/money-education/?$ library/money-education/index.html [L]
RewriteRule ^library/item/?$ library/item/index.html [QSA,L]
RewriteRule ^about/?$ about/index.html [L]

# Locale-aware governed routes. The 13 non-English routes are not product-language releases.
RewriteRule ^(pt-BR|es-419|fr|de|it|ja|ko|zh-Hans|zh-Hant|ar|ru|pl|nl)/?$ $1/index.html [L]
RewriteRule ^(pt-BR|es-419|fr|de|it|ja|ko|zh-Hans|zh-Hant|ar|ru|pl|nl)/library/?$ $1/library/index.html [L]
RewriteRule ^(pt-BR|es-419|fr|de|it|ja|ko|zh-Hans|zh-Hant|ar|ru|pl|nl)/library/free-tools/?$ $1/library/free-tools/index.html [L]
RewriteRule ^(pt-BR|es-419|fr|de|it|ja|ko|zh-Hans|zh-Hant|ar|ru|pl|nl)/library/resources/?$ $1/library/resources/index.html [L]
RewriteRule ^(pt-BR|es-419|fr|de|it|ja|ko|zh-Hans|zh-Hant|ar|ru|pl|nl)/library/programs/?$ $1/library/programs/index.html [L]
RewriteRule ^(pt-BR|es-419|fr|de|it|ja|ko|zh-Hans|zh-Hant|ar|ru|pl|nl)/library/books/?$ $1/library/books/index.html [L]
RewriteRule ^(pt-BR|es-419|fr|de|it|ja|ko|zh-Hans|zh-Hant|ar|ru|pl|nl)/library/money-education/?$ $1/library/money-education/index.html [L]
RewriteRule ^(pt-BR|es-419|fr|de|it|ja|ko|zh-Hans|zh-Hant|ar|ru|pl|nl)/library/item/?$ $1/library/item/index.html [QSA,L]
RewriteRule ^(pt-BR|es-419|fr|de|it|ja|ko|zh-Hans|zh-Hant|ar|ru|pl|nl)/about/?$ $1/about/index.html [L]

# Candidate-only search indexing safeguard. Remove only after separate founder approval for public launch.
<IfModule mod_headers.c>
  Header always set X-Robots-Tag "noindex, nofollow, noarchive"
</IfModule>
'''

ROBOTS = '''# NORTH Phase 2C static release candidate. Do not index before founder-approved public launch.
User-agent: *
Disallow: /
'''

def copy_file(relative: str, target: Path | None = None) -> None:
    source = ROOT / relative
    destination = target or WEB / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)

def page_target(source: str) -> Path:
    mapping = {
        'index.html':'index.html','library.html':'library/index.html','library-free-tools.html':'library/free-tools/index.html',
        'library-resources.html':'library/resources/index.html','library-programs.html':'library/programs/index.html','library-books.html':'library/books/index.html',
        'library-money-education.html':'library/money-education/index.html','library-item.html':'library/item/index.html','about.html':'about/index.html'
    }
    return WEB / mapping[source]

def sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(65536), b''):
            digest.update(block)
    return digest.hexdigest()

if OUT.exists(): shutil.rmtree(OUT)
WEB.mkdir(parents=True)
for source in PUBLIC_ROOT:
    copy_file(source, page_target(source))
for asset in PUBLIC_ASSETS:
    copy_file(f'assets/{asset}')
for icon in ['assets/icons/favicon.png','assets/icons/north-icon.png']:
    if (ROOT / icon).exists(): copy_file(icon)
for code in LOCALES:
    for path in (ROOT / code).rglob('*'):
        if path.is_file():
            relative = path.relative_to(ROOT)
            copy_file(str(relative))
(WEB / '.htaccess').write_text(HTACCESS, encoding='utf-8')
(WEB / 'robots.txt').write_text(ROBOTS, encoding='utf-8')
for document in (ROOT / 'docs' / 'release-candidate').glob('*.md'):
    shutil.copy2(document, OUT / document.name)

manifest = []
for item in sorted(WEB.rglob('*')):
    if item.is_file():
        manifest.append({'path': str(item.relative_to(WEB)), 'bytes': item.stat().st_size, 'sha256': sha(item)})
(OUT / 'STATIC_RELEASE_MANIFEST.json').write_text(json.dumps({'phase':'2c','scope':'public-static-candidate-only','files':manifest}, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'website_files':len(manifest), 'website_bytes':sum(item['bytes'] for item in manifest)}, indent=2))
