#!/usr/bin/env python3
from pathlib import Path
import json, re, subprocess, hashlib

ROOT=Path('/home/ubuntu/north-phase2e')
results=[]
def check(name, ok, detail=''):
    results.append({'check':name,'passed':bool(ok),'detail':detail})
def text(path): return (ROOT/path).read_text(encoding='utf-8')
def exists(path): return (ROOT/path).exists()

# Locked pilot artifacts
master='internal/commerce-pilot/execution-planner-v1/editable-source/01-execution-planner-customer-master.md'
check('editable_english_master',exists(master),master)
if exists(master):
    body=text(master)
    check('fourteen_daily_pages',len(re.findall(r'## Day \d+',body))==14,f'{len(re.findall(r"## Day \\d+",body))} daily headings')
    weekly_sections = len(re.findall(r'# Week (?:One|Two) Reset / Review', body))
    check('two_weekly_reviews', weekly_sections == 2, f'{weekly_sections} weekly reset/review sections')
    check('fictional_example',bool(re.search(r'fictional',body,re.I)),'fictional boundary')

# Core bundle candidates and print proof
bundle=ROOT/'internal/commerce-readiness/core-digital-bundle-candidate'
letter=bundle/'NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-US-Letter_private-release-candidate.pdf'
a4=bundle/'NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-A4_private-release-candidate.pdf'
for label,path,token in [('core_bundle_html',bundle/'NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN_private-release-candidate.html','Core Digital Edition v1.0'),('core_us_letter_pdf',letter,''),('core_a4_pdf',a4,'')]:
    check(label,path.exists(),str(path.relative_to(ROOT)))
    if path.suffix=='.html' and path.exists(): check('core_bundle_private_boundary', 'Private release candidate' in path.read_text(encoding='utf-8'),'private boundary text')
for label,path,expected in [('letter_geometry',letter,'612 x 792'),('a4_geometry',a4,'595.276 x 841.89')]:
    if path.exists():
        output=subprocess.check_output(['pdfinfo',str(path)],text=True)
        check(label,expected in output,output.split('Page size:')[-1].splitlines()[0].strip())
    else: check(label,False,'file missing')

# Required phase docs
required=[
 'internal/commerce-readiness/execution-planner-core-digital-release-spec.md',
 'internal/commerce-readiness/official-merchant-research.md',
 'internal/commerce-readiness/neutral-merchant-comparison.md',
 'internal/commerce-readiness/closed-beta-commerce-operating-system.md',
 'internal/commerce-readiness/phase2e-catalog-governance.md',
 'internal/commerce-readiness/future-opt-in-sharing-spec.md',
 'assets/phase2e-catalog.js','assets/phase2e-roadmap.js','assets/phase2e-roadmap.css','assets/phase2e-operations.js',
 'internal/phase2e-roadmap.html','internal/phase2e-operations.html'
]
for p in required: check('artifact_'+Path(p).name,exists(p),p)

# Catalog correctness and controlled commercial state
catalog=text('assets/phase2e-catalog.js')
for family in ['Financial Clarity','Routine Reset','Focus and Execution','Direction and Motivation','Authority and Education']:
    check('family_'+family.lower().replace(' ','_').replace('and',''),family in catalog,family)
brief_count = len(re.findall(r"\{id:'", catalog))
check('catalog_20_future_product_briefs', brief_count == 20, f'{brief_count} product briefs')
check('north_method_seven_elements',all(x in catalog for x in ['Safe Number','Big Thing','1-3-5 execution','weekly reflection','routines','recovery','growth']),'all method elements')
check('finance_general_education_boundary','General educational information only' in catalog,'financial boundary')
check('pilot_only_core_19',"proposedPrice: '$19 USD'" in catalog and 'Planner + Editable Source' not in catalog,'pilot specification')
check('catalog_sale_gate_closed',"saleGate: 'closed'" in catalog and 'No merchant, payment, checkout, public pricing' in catalog,'closed sale gate')

config=text('assets/product-studio-config.js')
check('planner_commerce_disabled','commercePilot: { enabled: false' in config,'commercePilot false')
check('planner_merchant_null','merchant: null' in config and 'checkoutUrl: null' in config,'merchant and checkout null')
check('locale_availability_fields',all(x in config for x in ['editionAvailability','pt-BR','es-419','rtl_route_only_no_product_edition','publicOffer: false']),'edition availability fields')
locale_match = re.search(r"LOCALE_CODES = Object\.freeze\(\[(.*?)\]\)", config, re.S)
locale_codes = re.findall(r"'([^']+)'", locale_match.group(1)) if locale_match else []
check('exact_14_locales', len(locale_codes) == 14 and len(set(locale_codes)) == 14, f'{len(locale_codes)} unique locale codes')

# No operation / customer intake in internal routes
for p in ['internal/commerce-pilot.html','internal/phase2e-roadmap.html','internal/phase2e-operations.html']:
    source=text(p)
    check('no_form_'+Path(p).stem,'<form' not in source.lower(),p)
    check('no_payment_script_'+Path(p).stem,not re.search(r'stripe|paypal|gumroad|lemonsqueezy|shopify',source,re.I),p)

# Preserve public foundation files
for p in ['index.html','library.html','library-free-tools.html','library-resources.html','library-programs.html','library-books.html','library-money-education.html','library-item.html','about.html','assets/locale-system.js','assets/public-site.js','assets/public-site.css']:
    check('foundation_'+p.replace('/','_'),exists(p),p)
for locale in ['pt-BR','es-419','fr','de','it','ja','ko','zh-Hans','zh-Hant','ar','ru','pl','nl']:
    check('locale_route_'+locale,exists(f'{locale}/index.html'),locale)

# Explicit no deployment configuration change
check('no_namecheap_or_vercel_deploy_config',not exists('phase2e-deploy.json') and not exists('vercel-phase2e.json'),'no deployment config')

out={'phase':'2E','passed':sum(r['passed'] for r in results),'total':len(results),'checks':results}
(ROOT/'evidence').mkdir(exist_ok=True)
(ROOT/'evidence/phase2e-verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed']==out['total'] else 1)
