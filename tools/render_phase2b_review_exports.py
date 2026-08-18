#!/usr/bin/env python3
"""Render editable Phase 2B founder-review Markdown into private HTML review exports only."""
from __future__ import annotations

from pathlib import Path
import markdown

ROOT = Path('/home/ubuntu/north-phase2b')
DRAFTS = {
    'execution-planner': ('1-3-5 Execution Planner', 'execution-planner-v0.1', '01-draft-content.md'),
    'decision-clarity-toolkit': ('Decision Clarity Toolkit', 'decision-clarity-toolkit-v0.1', '01-draft-content.md'),
    'focus-recovery-program': ('Focus Recovery Program', 'focus-recovery-program-v0.1', '01-draft-content.md'),
}

STYLE = '''
:root { --navy:#071b29; --ink:#122b3a; --gold:#c9a655; --blue:#799aad; --paper:#f6f4ed; --line:#d7d3c7; }
* { box-sizing:border-box; }
body { margin:0; color:var(--ink); background:var(--paper); font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif; line-height:1.6; }
header { background:var(--navy); color:#f9f6ec; padding:42px max(24px,calc((100vw - 920px)/2)); border-bottom:3px solid var(--gold); }
header .eyebrow { color:#e2c87b; text-transform:uppercase; letter-spacing:.13em; font-size:.72rem; font-weight:800; }
header h1 { color:#f9f6ec; font:400 clamp(2.5rem,6vw,4.8rem)/.98 Georgia,serif; letter-spacing:-.04em; margin:12px 0; }
header p { max-width:680px; color:#c5d6df; margin:0; }
.notice { display:inline-block; border:1px solid #e2c87b; color:#f4df9f; padding:7px 11px; margin-top:20px; font-size:.72rem; font-weight:800; text-transform:uppercase; letter-spacing:.08em; }
main { width:min(100% - 40px,920px); margin:0 auto; background:#fffdf8; padding:56px clamp(24px,6vw,72px) 86px; min-height:100vh; }
h1,h2,h3 { font-family:Georgia,serif; line-height:1.1; color:var(--ink); }
main h1 { font-size:2.5rem; border-top:3px solid var(--gold); padding-top:24px; margin-top:50px; }
main h2 { font-size:1.72rem; margin-top:40px; border-top:1px solid var(--line); padding-top:24px; }
main h3 { font-size:1.15rem; margin-top:26px; }
p,li { font-size:1rem; }
blockquote { margin:28px 0; padding:18px 22px; border-left:3px solid var(--gold); background:#fff8e6; color:#3c4d56; }
table { width:100%; border-collapse:collapse; margin:22px 0; font-size:.9rem; }
th { background:#edf2f4; text-align:left; font-size:.74rem; text-transform:uppercase; letter-spacing:.06em; }
th,td { border:1px solid var(--line); padding:12px; vertical-align:top; }
hr { border:0; border-top:1px solid var(--line); margin:48px 0; }
input[type=checkbox] { width:1rem; height:1rem; accent-color:var(--gold); }
@media print { @page { size: auto; margin: .55in; } header { background:#fff !important; color:#000 !important; padding:0 0 24px; border-color:#000; } header p, header .eyebrow { color:#000 !important; } .notice { color:#000; border-color:#000; } body { background:#fff; } main { width:100%; padding:0; } h1,h2 { break-after:avoid; } table { break-inside:avoid; } }
@media (max-width:480px) { main { width:100%; padding:36px 20px 60px; } header { padding:30px 20px; } th,td { padding:9px; overflow-wrap:anywhere; } table { font-size:.78rem; } }
'''

for slug, (title, folder, content_file) in DRAFTS.items():
    package = ROOT / 'internal/review-drafts/release-a' / folder
    source = (package / content_file).read_text(encoding='utf-8')
    source = source.replace('> **Founder review draft — not for sale**', '')
    rendered = markdown.markdown(source, extensions=['tables', 'fenced_code', 'sane_lists'])
    document = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex,nofollow,noarchive"><title>{title} — Founder Review Draft</title><style>{STYLE}</style></head>
<body><header><div class="eyebrow">NORTH Release A / Private product review</div><h1>{title}</h1><p>Editable-source review export. This is a working founder-review draft, not a customer file or available product.</p><div class="notice">Founder review draft — not for sale</div></header><main>{rendered}</main></body></html>'''
    output = ROOT / 'internal/review-exports/release-a' / f'{slug}-review.html'
    output.write_text(document, encoding='utf-8')
    print(output)
