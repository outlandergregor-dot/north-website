#!/usr/bin/env python3
"""Removes the X profile link that failed the Phase 1 public-link audit."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(
    r'\s*<a\s+href="https://x\.com/yournorthapp"[^>]*>.*?</a>',
    flags=re.IGNORECASE | re.DOTALL,
)

for path in ROOT.glob("*.html"):
    content = path.read_text(encoding="utf-8")
    updated, count = PATTERN.subn("", content)
    if count:
        path.write_text(updated, encoding="utf-8")
        print(f"Removed {count} X link(s) from {path.name}")
