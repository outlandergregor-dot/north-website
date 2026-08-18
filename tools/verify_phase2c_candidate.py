#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json
import re

ROOT = Path('/home/ubuntu/north-phase2c')
CANDIDATE = ROOT / 'release-candidate' / 'NORTH_PHASE2C_STATIC_RELEASE_CANDIDATE'
WEB = CANDIDATE / 'website'
LOCALES = ['pt-BR','es-419','fr','de','it','ja','ko','zh-Hans','zh-Hant','ar','ru','pl','nl']
EXPECTED = ['index.html','library/index.html','library/free-tools/index.html','library/resources/index.html','library/programs/index.html','library/books/index.html','library/money-education/index.html','library/item/index.html','about/index.html']
results = []
def check(name, condition, detail=''):
    results.append({'check':name, 'passed':bool(condition), 'detail':detail})

check('candidate_directory', WEB.exists(), str(WEB))
check('no_internal_directory', not (WEB/'internal').exists(), 'Internal founder-review paths must never be included.')
for item in EXPECTED:
    check(f'english_{item}', (WEB/item).is_file(), item)
for code in LOCALES:
    for item in EXPECTED:
        check(f'locale_{code}_{item}', (WEB/code/item).is_file(), f'{code}/{item}')
check('locale_directory_count', len([code for code in LOCALES if (WEB/code).is_dir()]) == 13, '13 non-English directories plus canonical English root equals 14 governed locales.')
check('free_tools_config_only', (WEB/'assets/free-tools-config.js').is_file() and not (WEB/'assets/north-config.js').exists(), 'Public candidate carries only minimal verified Free Tools configuration.')
public_catalog = (WEB/'assets/public-catalog.js').read_text(encoding='utf-8')
for field in ['websiteLanguage','productContentLanguage','checkoutLanguage','deliveryLanguage','supportLanguage','legalPolicyLanguage']:
    check(f'language_readiness_{field}', public_catalog.count(field) == 3, 'One explicit field for each Release A product.')
for forbidden in ['proposedPrice','reviewExport','sourcePackage','checkoutStatus','merchant','northfounder','Gumroad','purchaseRequirements','priceCurrency','refundPolicy']:
    corpus = '\n'.join(path.read_text(encoding='utf-8', errors='ignore') for path in WEB.rglob('*') if path.is_file() and path.suffix in {'.html','.js','.css','.txt','.htaccess'})
    check(f'private_term_absent_{forbidden}', forbidden.lower() not in corpus.lower(), forbidden)
for forbidden_action in ['Buy now','Add to cart','Start trial','Join waitlist','Subscribe now','Enter email','Preorder now']:
    check(f'forbidden_action_absent_{forbidden_action}', forbidden_action.lower() not in corpus.lower(), forbidden_action)
check('no_email_input', not re.search(r'<input[^>]+(?:type=["\']email["\']|name=["\'][^"\']*email)', corpus, re.I), 'No email capture field.')
payment_integration = re.search(r'https?://[^\s\"\']*(?:stripe|paypal|gumroad)|<script[^>]+(?:stripe|paypal|gumroad)|<form[^>]+(?:checkout|payment)|window\.Stripe|data-(?:checkout|payment)', corpus, re.I)
check('no_payment_form', not payment_integration, 'No payment or checkout integration; the required checkout-language readiness labels are allowed.')
htaccess = (WEB/'.htaccess').read_text(encoding='utf-8')
check('apache_routes', 'RewriteEngine On' in htaccess and 'library/free-tools' in htaccess and 'zh-Hant' in htaccess, 'Clean English and locale rewrites are included.')
robots = (WEB/'robots.txt').read_text(encoding='utf-8')
check('candidate_noindex', 'Disallow: /' in robots and 'noindex, nofollow, noarchive' in htaccess, 'Candidate indexing safeguards retained.')
check('manual_handoff', (CANDIDATE/'MANUAL_NAMECHEAP_STATIC_RELEASE.md').is_file(), 'Manual Namecheap document included.')
check('staging_checklist', (CANDIDATE/'STAGING_TEST_CHECKLIST.md').is_file(), 'Staging checklist included.')
check('localization_record', (CANDIDATE/'LOCALIZATION_READINESS.md').is_file(), '14-locale governance record included.')
passed = sum(item['passed'] for item in results)
report = {'total':len(results),'passed':passed,'failed':len(results)-passed,'checks':results}
(ROOT/'evidence'/'phase2c-static-verification.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'total':report['total'], 'passed':report['passed'], 'failed':report['failed']}, indent=2))
if report['failed']:
    raise SystemExit(1)
