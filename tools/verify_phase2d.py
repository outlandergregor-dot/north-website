#!/usr/bin/env python3
from pathlib import Path
import json, re, subprocess

ROOT=Path('/home/ubuntu/north-phase2d')
PKG=ROOT/'internal/commerce-pilot/execution-planner-v1'
checks=[]
def check(name, ok, detail): checks.append({'check':name,'passed':bool(ok),'detail':detail})

def exists(rel): return (ROOT/rel).exists()
source=(PKG/'editable-source/01-execution-planner-customer-master.md').read_text(encoding='utf-8')
check('editable_customer_master', len(source)>28000, f'{len(source)} characters')
check('fourteen_distinct_daily_pages', len(re.findall(r'^## Day \d+ —',source,re.M))==14, f"{len(re.findall(r'^## Day \d+ —',source,re.M))} daily pages")
check('two_week_reviews', all(term in source for term in ['# Week One Reset / Review','# Week Two Reset / Review','# Final Two-Week Review and Continuation Plan']), 'weekly and final review sections present')
check('fictional_example_labelled', 'This is a fictional workflow example.' in source, 'fictional example boundary present')
for rel in ['00-product-package-specification.md','03-product-quality-checklist.md','policy-drafts/01-personal-use-license-draft.md','policy-drafts/02-support-and-refund-information-draft.md','delivery-architecture/01-inactive-commerce-architecture.md','delivery-architecture/02-pricing-and-packaging-options.md','private-review/execution-planner-customer-review.html','print-review/NORTH_1-3-5_Execution_Planner_US-Letter_PRIVATE-REVIEW.pdf','print-review/NORTH_1-3-5_Execution_Planner_A4_PRIVATE-REVIEW.pdf']:
    check(f'package_artifact_{rel}',(PKG/rel).exists(),rel)
for rel in ['assets/product-visuals/execution-planner-cover-art.png','assets/product-visuals/execution-planner-open-spread.png','assets/product-visuals/execution-planner-desk-kit.png','assets/product-visuals/execution-planner-detail.png']:
    check(f'visual_asset_{Path(rel).name}',exists(rel),rel)
for name,expected in [('US Letter', '612 x 792'),('A4','595.276 x 841.89')]:
    pdf=PKG/'print-review'/f"NORTH_1-3-5_Execution_Planner_{'US-Letter' if name=='US Letter' else 'A4'}_PRIVATE-REVIEW.pdf"
    info=subprocess.check_output(['pdfinfo',str(pdf)],text=True)
    pages=re.search(r'Pages:\s+(\d+)',info).group(1)
    check(f'print_proof_{name}',int(pages)>=20 and expected in info,f'{pages} pages; expected geometry {expected}')
config=(ROOT/'assets/product-studio-config.js').read_text(encoding='utf-8')
check('commerce_disabled','commercePilot: { enabled: false' in config,'inactive commercePilot metadata present')
check('merchant_null','merchant: null' in config and 'checkoutUrl: null' in config,'no merchant or checkout URL configured')
check('planner_sale_gate_locked',"'execution-planner-14'" in config and 'saleGateLocked: true' in config,'Planner sale gate locked')
check('other_release_a_preserved', all(x in config for x in ['decision-clarity-toolkit','focus-recovery-program']), 'other products remain in registry')
internal=(ROOT/'internal/commerce-pilot.html').read_text(encoding='utf-8')
check('private_pilot_route','noindex,nofollow,noarchive' in internal and 'commerce-pilot.js' in internal,'private page metadata and renderer loaded')
for rel in ['index.html','library.html','library-free-tools.html','library-resources.html','library-programs.html','library-books.html','library-money-education.html','library-item.html','about.html','assets/locale-system.js','assets/public-site.js','assets/public-site.css']:
    check(f'phase2c_preserved_{rel}',exists(rel),rel)
locales=['pt-BR','es-419','fr','de','it','ja','ko','zh-Hans','zh-Hant','ar','ru','pl','nl']
for locale in locales: check(f'locale_preserved_{locale}',(ROOT/locale/'index.html').exists(),f'{locale}/index.html')
report={'phase':'2D','passed':sum(c['passed'] for c in checks),'total':len(checks),'checks':checks}
(ROOT/'evidence').mkdir(exist_ok=True)
(ROOT/'evidence/phase2d-verification.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
if report['passed']!=report['total']: raise SystemExit(1)
