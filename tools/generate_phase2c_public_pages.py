#!/usr/bin/env python3
from pathlib import Path

ROOT = Path('/home/ubuntu/north-phase2c')
HEAD = '''<!doctype html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="index,follow">
  <meta name="color-scheme" content="light">
  <meta name="theme-color" content="#061824">
  <meta name="description" content="NORTH is a calm system for clarity, priorities, decisions, and consistent daily action. Explore the app, Free Tools, and the public NORTH Library.">
  <link rel="icon" href="/assets/icons/favicon.png">
  <link rel="stylesheet" href="/assets/public-site.css">
  <title>{title}</title>
</head>
<body data-page="{page}">
  <div id="publicApp"></div>
  <script src="/assets/locale-system.js"></script>
  <script src="/assets/public-catalog.js"></script>
  <script src="/assets/public-site.js"></script>
  <script>window.NORTH_PUBLIC_SITE.render();</script>
</body>
</html>
'''
PAGES = {
    'index.html': ('home', 'NORTH — A calm system for clarity and daily action'),
    'library.html': ('library', 'NORTH Library — Practical support for a clearer next move'),
    'library-resources.html': ('resources', 'Free Tools — NORTH Library'),
    'library-programs.html': ('programs', 'Programs — NORTH Library'),
    'library-books.html': ('books', 'Books & Authority — NORTH Library'),
    'library-money-education.html': ('money', 'Money Education — NORTH Library'),
    'library-item.html': ('item', 'Release A Overview — NORTH Library'),
    'about.html': ('about', 'About NORTH')
}
LOCALES = ['pt-BR','es-419','fr','de','it','ja','ko','zh-Hans','zh-Hant','ar','ru','pl','nl']
LOCALE_ROUTES = {
    'index.html': 'index.html',
    'library.html': 'library/index.html',
    'library-resources.html': 'library/resources/index.html',
    'library-programs.html': 'library/programs/index.html',
    'library-books.html': 'library/books/index.html',
    'library-money-education.html': 'library/money-education/index.html',
    'library-item.html': 'library/item/index.html',
    'about.html': 'about/index.html',
    'library-free-tools.html': 'library/free-tools/index.html'
}
for dest, (page, title) in PAGES.items():
    (ROOT / dest).write_text(HEAD.format(page=page, title=title), encoding='utf-8')
for locale in LOCALES:
    for source, relative in LOCALE_ROUTES.items():
        output = ROOT / locale / relative
        output.parent.mkdir(parents=True, exist_ok=True)
        if source == 'library-free-tools.html':
            template = (ROOT / source).read_text(encoding='utf-8').replace('<html lang="en">', f'<html lang="{locale}">')
            output.write_text(template, encoding='utf-8')
        else:
            page, title = PAGES[source]
            output.write_text(HEAD.format(page=page, title=f'{title} — {locale}'), encoding='utf-8')
print(f'Generated {len(PAGES)} English pages and {len(LOCALES) * len(LOCALE_ROUTES)} locale route files.')
