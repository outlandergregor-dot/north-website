#!/usr/bin/env python3
"""Adds a cache-busting revision to the shared Phase 1.5 Library script."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for path in sorted(ROOT.glob("library*.html")):
    content = path.read_text(encoding="utf-8")
    updated = content.replace('src="/assets/library.js"', 'src="/assets/library.js?v=phase15-clear-reset"')
    if updated == content:
        raise SystemExit(f"Expected shared Library script tag not found in {path.name}")
    path.write_text(updated, encoding="utf-8")
    print(f"Updated {path.name}")
