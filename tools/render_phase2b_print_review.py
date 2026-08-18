#!/usr/bin/env python3
"""Create internal print-review PDFs only; these are not customer delivery files."""
from pathlib import Path
from weasyprint import HTML, CSS

ROOT = Path('/home/ubuntu/north-phase2b')
EXPORTS = {
    'execution-planner': ROOT / 'internal/review-exports/release-a/execution-planner-review.html',
    'decision-clarity-toolkit': ROOT / 'internal/review-exports/release-a/decision-clarity-toolkit-review.html',
    'focus-recovery-program': ROOT / 'internal/review-exports/release-a/focus-recovery-program-review.html',
}
OUT = ROOT / 'internal/print-review/release-a'
OUT.mkdir(parents=True, exist_ok=True)
for slug, source in EXPORTS.items():
    html = source.read_text(encoding='utf-8').replace('</body>', '<div style="position:fixed;bottom:0;right:0;font-size:8pt;color:#555">Founder review draft — print review only — not for sale</div></body>')
    for size, label in [('Letter', 'US-Letter'), ('A4', 'A4')]:
        css = CSS(string=f'@page {{ size: {size}; margin: 0.55in; }}')
        output = OUT / f'{slug}_{label}_PRINT-REVIEW-NOT-FOR-SALE.pdf'
        HTML(string=html, base_url=str(source.parent)).write_pdf(output, stylesheets=[css])
        print(output)
