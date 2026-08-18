#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
root=Path('/home/ubuntu/north-phase2f')
source=Image.open(root/'assets/brand/north-compass-official-512.png').convert('RGBA')
out=root/'assets/brand/favicon'
out.mkdir(parents=True,exist_ok=True)
for size in [16,32,48,180,192,512]:
    image=source.resize((size,size),Image.Resampling.LANCZOS)
    image.save(out/f'north-compass-{size}.png',optimize=True)
source.save(out/'north-compass-512.png',optimize=True)
