#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

ROOT = Path('/home/ubuntu/north-phase2f-presentation')
SOURCE = ROOT / 'assets/product-presentation/higgsfield'
OUTPUT = ROOT / 'assets/product-presentation/web'
OUTPUT.mkdir(parents=True, exist_ok=True)
# Preserve each composition; only downscale the longest edge and convert for private web preview delivery.
SPECS = {
    'planner-hero-illustrative.png': 2200,
    'planner-morning-desk-illustrative.png': 1600,
    'planner-weekly-reset-illustrative.png': 1600,
    'planner-two-week-rhythm-illustrative.png': 1600,
    'planner-weekly-review-illustrative.png': 1600,
    'social-calm-direction-illustrative.png': 1200,
    'social-method-illustrative.png': 1200,
    'story-reel-cover-illustrative.png': 1200,
}
for name, max_edge in SPECS.items():
    src = SOURCE / name
    image = Image.open(src).convert('RGB')
    width, height = image.size
    scale = min(1.0, max_edge / max(width, height))
    target = (round(width * scale), round(height * scale))
    if target != image.size:
        image = image.resize(target, Image.Resampling.LANCZOS)
    dest = OUTPUT / f'{src.stem}.webp'
    image.save(dest, 'WEBP', quality=84, method=6)
    print(f'{name} -> {dest.name}: {width}x{height} => {target[0]}x{target[1]}, {dest.stat().st_size} bytes')
