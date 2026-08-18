#!/usr/bin/env python3
from pathlib import Path
import markdown
from weasyprint import HTML

ROOT = Path('/home/ubuntu/north-phase2d')
PKG = ROOT / 'internal/commerce-pilot/execution-planner-v1'
SOURCE = PKG / 'editable-source/01-execution-planner-customer-master.md'
ASSET_REL = '../../assets/product-visuals/execution-planner-cover-art.png'
OUT_HTML = PKG / 'private-review/execution-planner-customer-review.html'
OUT_US = PKG / 'print-review/NORTH_1-3-5_Execution_Planner_US-Letter_PRIVATE-REVIEW.pdf'
OUT_A4 = PKG / 'print-review/NORTH_1-3-5_Execution_Planner_A4_PRIVATE-REVIEW.pdf'

CSS = '''
:root{--navy:#071a2d;--gold:#c8a96b;--ivory:#f7f3eb;--ink:#162434;--muted:#6d7780}
*{box-sizing:border-box} body{font-family:Arial,Helvetica,sans-serif;line-height:1.48;color:var(--ink);margin:0;background:#fff;font-size:10.5pt} .draft{background:#151f2d;color:#fff;padding:8pt 12pt;font-size:8.5pt;letter-spacing:.07em;text-transform:uppercase}.cover{min-height:10.8in;display:flex;align-items:flex-end;padding:52pt;background:linear-gradient(90deg,rgba(4,14,26,.94),rgba(4,14,26,.28)),url("''' + ASSET_REL + '''") center/cover;color:white;page-break-after:always}.cover .eyebrow{font-size:10pt;letter-spacing:.18em;color:#d8c08f;font-weight:700}.cover h1{font-family:Georgia,serif;font-size:34pt;line-height:1.02;margin:12pt 0;max-width:360pt}.cover p{font-size:13pt;max-width:290pt;margin:0}.cover .edition{margin-top:34pt;font-size:9pt;letter-spacing:.08em;text-transform:uppercase}.document{padding:40pt 44pt 52pt;max-width:700pt;margin:auto}.document h1{font-family:Georgia,serif;font-size:24pt;color:var(--navy);border-bottom:2pt solid var(--gold);padding-bottom:8pt;margin-top:30pt;page-break-before:always}.document h1:first-child{page-break-before:auto}.document h2{font-size:16pt;color:var(--navy);margin-top:22pt}.document h3{font-size:12pt;color:#283b50;margin-top:16pt}.document p,.document li{orphans:3;widows:3}.document blockquote{border-left:3pt solid var(--gold);margin:14pt 0;padding:6pt 13pt;background:#fcfaf5;color:#3f4e5e}.document table{border-collapse:collapse;width:100%;margin:14pt 0;font-size:9.2pt}.document th,.document td{border:1px solid #cfd5db;padding:7pt;text-align:left;vertical-align:top}.document th{background:#edf0f2;color:var(--navy)}.document hr{border:0;border-top:1pt solid #d6d9dc;margin:24pt 0}.footer-note{margin-top:28pt;color:var(--muted);font-size:8pt}@page{size:LETTER;margin:0.55in;@bottom-center{content:"NORTH 1-3-5 Execution Planner — Founder review draft — not for sale";font-size:8pt;color:#68717b}}@media screen{body{background:#e6e8ea}.review-shell{max-width:790px;margin:28px auto;background:#fff;box-shadow:0 8px 30px rgba(0,0,0,.16)}.cover{min-height:820px}.document{padding:52px}}@media print{.review-shell{box-shadow:none}.cover{min-height:9.8in}.document{padding:0}.draft{margin:-.55in -.55in .25in}.cover{margin:-.55in;min-height:10.8in;padding:52pt}}
'''

def build_html():
    md = SOURCE.read_text(encoding='utf-8')
    content = markdown.markdown(md, extensions=['tables','fenced_code','sane_lists'])
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow,noarchive"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NORTH 1-3-5 Execution Planner — Private Review</title><style>{CSS}</style></head><body><main class="review-shell"><div class="draft">Founder review draft — not for sale — no customer delivery</div><section class="cover"><div><div class="eyebrow">NORTH</div><h1>1-3-5<br>Execution Planner</h1><p>Two weeks. One clear direction.</p><div class="edition">English customer-ready master v1.0 · private review</div></div></section><article class="document">{content}<p class="footer-note">Private founder-review edition. Customer delivery, payment, checkout, pricing, download, email, and public release remain disabled.</p></article></main></body></html>'''

if __name__ == '__main__':
    (PKG/'private-review').mkdir(exist_ok=True)
    OUT_HTML.write_text(build_html(),encoding='utf-8')
    HTML(filename=str(OUT_HTML),base_url=str(PKG)).write_pdf(str(OUT_US))
    letter = OUT_US.read_bytes()
    # Render A4 from the same fully editable source with only the page geometry changed.
    a4_html = build_html().replace('@page{size:LETTER;', '@page{size:A4;')
    tmp = PKG/'private-review/_a4_render.html'
    tmp.write_text(a4_html,encoding='utf-8')
    HTML(filename=str(tmp),base_url=str(PKG)).write_pdf(str(OUT_A4))
    tmp.unlink(missing_ok=True)
    print(OUT_HTML)
    print(OUT_US)
    print(OUT_A4)
