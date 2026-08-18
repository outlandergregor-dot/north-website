#!/usr/bin/env python3
from pathlib import Path
import markdown
from weasyprint import HTML

ROOT = Path('/home/ubuntu/north-phase2e')
SOURCE = ROOT / 'internal/commerce-pilot/execution-planner-v1/editable-source/01-execution-planner-customer-master.md'
OUT = ROOT / 'internal/commerce-readiness/core-digital-bundle-candidate'
ASSET = '../../assets/product-visuals/execution-planner-cover-art.png'

CSS = '''
:root{--navy:#071a2d;--gold:#c8a96b;--ink:#162434;--muted:#6d7780}
*{box-sizing:border-box}body{margin:0;background:#fff;color:var(--ink);font-family:Arial,Helvetica,sans-serif;font-size:10.4pt;line-height:1.48}.gate{background:#151f2d;color:white;padding:8pt 12pt;font-size:8.2pt;font-weight:700;letter-spacing:.07em;text-transform:uppercase}.cover{min-height:10.8in;display:flex;align-items:flex-end;padding:52pt;background:linear-gradient(90deg,rgba(4,14,26,.95),rgba(4,14,26,.28)),url("''' + ASSET + '''") center/cover;color:#fff;page-break-after:always}.eyebrow{font-size:10pt;letter-spacing:.18em;color:#d8c08f;font-weight:700}.cover h1{font-family:Georgia,serif;font-size:35pt;line-height:1.02;margin:12pt 0;max-width:360pt}.cover p{font-size:13pt;max-width:300pt;margin:0}.edition{margin-top:34pt;font-size:9pt;letter-spacing:.08em;text-transform:uppercase}.document{padding:40pt 44pt 52pt;max-width:700pt;margin:auto}.document h1{font-family:Georgia,serif;font-size:24pt;color:var(--navy);border-bottom:2pt solid var(--gold);padding-bottom:8pt;margin-top:30pt;page-break-before:always}.document h1:first-child{page-break-before:auto}.document h2{font-size:16pt;color:var(--navy);margin-top:22pt}.document h3{font-size:12pt;color:#283b50;margin-top:16pt}.document blockquote{border-left:3pt solid var(--gold);margin:14pt 0;padding:6pt 13pt;background:#fcfaf5;color:#3f4e5e}.document table{border-collapse:collapse;width:100%;margin:14pt 0;font-size:9.2pt}.document th,.document td{border:1px solid #cfd5db;padding:7pt;text-align:left;vertical-align:top}.document th{background:#edf0f2;color:var(--navy)}.release-note{margin-top:28pt;color:var(--muted);font-size:8pt}@page{size:LETTER;margin:.55in;@bottom-center{content:"NORTH 1-3-5 Execution Planner — Core Digital Edition v1.0 — Private release candidate";font-size:8pt;color:#68717b}}@media screen{body{background:#e6e8ea}.bundle-shell{max-width:790px;margin:28px auto;background:#fff;box-shadow:0 8px 30px rgba(0,0,0,.16)}.cover{min-height:820px}.document{padding:52px}}@media print{.bundle-shell{box-shadow:none}.cover{min-height:9.8in}.document{padding:0}.gate{margin:-.55in -.55in .25in}.cover{margin:-.55in;min-height:10.8in;padding:52pt}}
'''

def html():
    content = markdown.markdown(SOURCE.read_text(encoding='utf-8'), extensions=['tables','fenced_code','sane_lists'])
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow,noarchive"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NORTH 1-3-5 Execution Planner — Core Digital Edition v1.0</title><style>{CSS}</style></head><body><main class="bundle-shell"><div class="gate">Private release candidate — founder approval, legal review, merchant test, and customer delivery activation still required</div><section class="cover"><div><div class="eyebrow">NORTH</div><h1>1-3-5<br>Execution Planner</h1><p>Two weeks. One clear direction.</p><div class="edition">Core Digital Edition v1.0 · English · $19 founder pilot candidate</div></div></section><article class="document">{content}<p class="release-note">Private Core Digital Edition release candidate. No sale, payment, customer delivery, or public download is enabled. This file is provided only for founder, legal, accessibility, print, and merchant-readiness review.</p></article></main></body></html>'''

if __name__ == '__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    review = OUT / 'NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN_private-release-candidate.html'
    review.write_text(html(),encoding='utf-8')
    letter = OUT / 'NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-US-Letter_private-release-candidate.pdf'
    a4 = OUT / 'NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-A4_private-release-candidate.pdf'
    HTML(filename=str(review),base_url=str(OUT)).write_pdf(str(letter))
    temp = OUT / '_a4.html'
    temp.write_text(html().replace('@page{size:LETTER;', '@page{size:A4;'),encoding='utf-8')
    HTML(filename=str(temp),base_url=str(OUT)).write_pdf(str(a4))
    temp.unlink(missing_ok=True)
    print(review)
    print(letter)
    print(a4)
