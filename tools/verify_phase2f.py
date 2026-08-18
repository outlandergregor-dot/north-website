#!/usr/bin/env python3
from pathlib import Path
import json,re,subprocess
ROOT=Path('/home/ubuntu/north-phase2f')
checks=[]
def add(name,ok,evidence=''):checks.append({'check':name,'passed':bool(ok),'evidence':evidence})
def content(p): return (ROOT/p).read_text(encoding='utf-8')
def yes(p): return (ROOT/p).exists()

# Foundation/recoverability
head=subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'],text=True).strip()
tag=subprocess.check_output(['git','-C',str(ROOT),'rev-parse','north-web-phase2e-approved'],text=True).strip()
add('phase2e_tag_preserved',bool(tag),'north-web-phase2e-approved')
add('isolated_phase2f_branch',subprocess.check_output(['git','-C',str(ROOT),'branch','--show-current'],text=True).strip()=='north-web-phase2f-precommerce-validation','branch name')

# Brand assets and visible shell integration
for p in ['assets/brand/north-compass-official-512.png','assets/brand/favicon/north-compass-16.png','assets/brand/favicon/north-compass-32.png','assets/brand/favicon/north-compass-180.png','assets/brand/favicon/north-compass-192.png','internal/design-system/phase2f-premium-visual-system.md']:
 add('brand_'+Path(p).name,yes(p),p)
public=content('assets/public-site.js'); css=content('assets/public-site.css'); pilot=content('assets/commerce-pilot.js')
add('official_logo_public_shell',public.count('/assets/brand/north-compass-official-512.png')>=4,'header/footer/hero/about')
add('official_logo_private_planner','/assets/brand/north-compass-official-512.png' in pilot,'private Planner')
add('premium_tokens',all(x in css for x in ['--north-midnight','--north-gold','--north-ivory']),'navy/ivory/gold tokens')

# Audit and decision materials
for p in ['evidence/phase2f-planner-audit.json','internal/commerce-readiness/phase2f-planner-version-and-qa.md','internal/commerce-readiness/phase2f-pilot-decision-package.md','evidence/phase2f-visual-qa.md']:
 add('material_'+Path(p).name,yes(p),p)
audit=json.loads(content('evidence/phase2f-planner-audit.json'))
add('planner_audit_passed',audit['passed']==audit['total'],f"{audit['passed']}/{audit['total']}")
add('product_decision_not_ready_for_activation','not ready for payment activation' in content('internal/commerce-readiness/phase2f-planner-version-and-qa.md').lower(),'explicit activation boundary')
add('pilot_price_private_only','$19 USD' in content('internal/commerce-readiness/phase2f-pilot-decision-package.md') and 'not public price' in content('internal/commerce-readiness/phase2f-pilot-decision-package.md'),'founder decision only')

# Localization and roadmap
config=content('assets/product-studio-config.js')
add('all_14_locale_structures',all(yes(f'{x}/index.html') for x in ['pt-BR','es-419','fr','de','it','ja','ko','zh-Hans','zh-Hant','ar','ru','pl','nl']),'13 locale folders plus English root')
add('arabic_rtl_preserved',"'ar'" in config and 'rtl_route_only_no_product_edition' in config,'Arabic controls')
package=content('internal/commerce-readiness/phase2f-pilot-decision-package.md')
for term in ['Safe Number Starter Kit','Weekly Reset Kit','Focus Recovery Protocol','Decision Clarity Toolkit','Family Money Meeting Kit']:
 add('priority_'+term.lower().replace(' ','_').replace('-','_'),term in package,term)
add('finance_education_boundary','never individualized financial advice' in package and 'qualified legal/policy review required' in package,'financial safety boundary')

# No operation / no customer data / no merchant scripts
scan_files=['index.html','library.html','library-free-tools.html','assets/public-site.js','assets/commerce-pilot.js','internal/commerce-pilot.html','internal/phase2e-roadmap.html','internal/phase2e-operations.html']
scan='\n'.join(content(p) for p in scan_files if yes(p)).lower()
add('no_payment_provider_scripts',not re.search(r'<script[^>]+(stripe|paypal|gumroad|shopify|lemonsqueezy)',scan),'no payment scripts')
add('no_active_checkout_urls',not re.search(r'https?://[^\s"\']*(checkout|gumroad|stripe|paypal|lemonsqueezy|shopify)',scan),'no active merchant URLs')
add('no_customer_forms',not re.search(r'<form\b',scan),'no customer forms')
add('closed_commerce_config','commerceEnabled:false' in pilot and 'checkoutUrl:null' in pilot and 'deliveryEnabled:false' in pilot,'private renderer gates')

out={'phase':'2F','head':head,'phase2e_tag':tag,'passed':sum(c['passed'] for c in checks),'total':len(checks),'checks':checks}
(ROOT/'evidence').mkdir(exist_ok=True)
(ROOT/'evidence/phase2f-verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed']==out['total'] else 1)
