#!/usr/bin/env python3
"""Apply the private Phase 2A Product Studio renderer to approved Library routes only."""
from __future__ import annotations

import re
from pathlib import Path

root = Path("/home/ubuntu/north-phase2a")
pages = {
    "library-resources.html": "window.NORTH_PRODUCT_STUDIO_VIEW.category('resources', 'Practical resources.', 'Useful standalone tools deserve a real outcome, a clear production plan, and honest availability.');",
    "library-programs.html": "window.NORTH_PRODUCT_STUDIO_VIEW.category('programs', 'Guided programs.', 'Defined outcomes, bounded time commitments, and no clinical or treatment claims.');",
    "library-books.html": "window.NORTH_PRODUCT_STUDIO_VIEW.category('books', 'Books & authority.', 'A durable NORTH editorial foundation—shown as concept work until a real manuscript and final formats exist.');",
    "library-item.html": "window.NORTH_PRODUCT_STUDIO_VIEW.productPage();",
}

for filename, renderer in pages.items():
    path = root / filename
    text = path.read_text(encoding="utf-8")
    text = text.replace('  <link rel="stylesheet" href="/assets/library.css">', '  <link rel="stylesheet" href="/assets/library.css">\n  <link rel="stylesheet" href="/assets/product-studio.css">', 1)
    old = re.compile(r'  <script src="/assets/north-config\.js"></script>\n  <script src="/assets/library\.js[^\n]*"></script>\n  <script>.*?</script>', re.DOTALL)
    new = '\n'.join([
        '  <script src="/assets/north-config.js"></script>',
        '  <script src="/assets/product-studio-config.js"></script>',
        '  <script src="/assets/product-studio.js"></script>',
        f'  <script>{renderer}</script>',
    ])
    text, count = old.subn(new, text, count=1)
    if count != 1:
        raise SystemExit(f"Could not replace renderer in {filename}")
    path.write_text(text, encoding="utf-8")
    print(f"Updated {filename}")
