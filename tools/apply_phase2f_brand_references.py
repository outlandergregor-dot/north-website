#!/usr/bin/env python3
from pathlib import Path
root=Path('/home/ubuntu/north-phase2f')
old='/assets/icons/favicon.png'
new='/assets/brand/favicon/north-compass-32.png'
changed=[]
for path in root.rglob('*.html'):
    if any(part in {'internal','evidence','release-candidate'} for part in path.parts):
        continue
    value=path.read_text(encoding='utf-8')
    updated=value.replace(old,new)
    if updated!=value:
        path.write_text(updated,encoding='utf-8')
        changed.append(str(path.relative_to(root)))
# Canonical source-generator must retain the official brand reference for future route regeneration.
generator=root/'tools/generate_phase2c_public_pages.py'
value=generator.read_text(encoding='utf-8')
updated=value.replace(old,new)
if updated!=value:
    generator.write_text(updated,encoding='utf-8')
    changed.append(str(generator.relative_to(root)))
print('\n'.join(changed))
