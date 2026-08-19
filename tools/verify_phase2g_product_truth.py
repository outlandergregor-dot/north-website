#!/usr/bin/env python3
"""Static acceptance checks for the NORTH Phase 2G private product-truth pilot."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path('/home/ubuntu/north-phase2g-product-truth')
EVIDENCE = ROOT / 'evidence' / 'phase2g-verification-output.json'

checks: list[dict[str, object]] = []


def check(check_id: str, title: str, passed: bool, detail: str) -> None:
    checks.append({'id': check_id, 'title': title, 'passed': bool(passed), 'detail': detail})


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')


def git_output(*args: str) -> str:
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True).strip()


branch = git_output('branch', '--show-current')
check('branch', 'Isolated Phase 2G branch', branch == 'north-web-phase2g-product-truth', f'Current branch: {branch}')

required_docs = [
    'docs/NORTH_PHASE2G_SOURCE_AUDIT.md',
    'docs/NORTH_PRODUCT_STATUS_AND_LAUNCH_GATES.md',
    'docs/NORTH_ASSET_AND_CLAIM_REGISTER.md',
    'docs/NORTH_PREMIUM_VISUAL_SYSTEM.md',
    'docs/NORTH_135_EXECUTION_PLANNER_BUYER_READINESS.md',
    'docs/NORTH_PRODUCT_LOCALIZATION_RELEASE_PLAN.md',
    'docs/NORTH_FUTURE_COMMERCE_READINESS_PLAN.md',
    'docs/NORTH_PHASE2H_FOUNDER_RECOMMENDATION.md',
]
check('required_docs', 'Required Phase 2G governance documents', all((ROOT / path).is_file() for path in required_docs), f'{sum((ROOT / path).is_file() for path in required_docs)}/{len(required_docs)} documents exist')

pilot = text('assets/commerce-pilot.js')
public_site = text('assets/public-site.js')
public_catalog = text('assets/public-catalog.js')
locale = text('assets/locale-system.js')
public_css = text('assets/public-site.css')
pilot_css = text('assets/commerce-pilot.css')
asset_register = text('docs/NORTH_ASSET_AND_CLAIM_REGISTER.md')

proof_assets = [
    'assets/product-proof/planner-start-here-us-letter.png',
    'assets/product-proof/planner-two-week-intention-us-letter.png',
    'assets/product-proof/planner-daily-page-us-letter.png',
    'assets/product-proof/planner-final-review-us-letter.png',
    'assets/product-proof/planner-start-here-a4.png',
]
check('proof_files', 'Five source-controlled real Planner proof exports', all((ROOT / path).is_file() and (ROOT / path).stat().st_size > 10000 for path in proof_assets), 'All required source-PDF exports exist and are nonempty')
check('actual_proof_sequence', 'Flagship proof sequence uses real PDF exports', all(path.replace('assets/', '/') in pilot for path in proof_assets[:4]), 'Start Here, intention, daily, and final-review proof cards are referenced')
check('proof_label', 'Actual product proof has a persistent private-source label', 'Actual Planner-page proof — private founder-review source.' in pilot, 'Actual proof label is present in private renderer')
check('illustrative_label', 'Generated editorial visual has digital-only disclosure', 'Illustrative digital product mockup — not a physical product photograph.' in pilot, 'Persistent illustrative disclosure is present')
check('no_physical_mockup_primary_proof', 'Physical-looking mockups are removed from primary proof renderer', 'assets/product-visuals/execution-planner-open-spread.png' not in pilot and 'assets/product-visuals/execution-planner-detail.png' not in pilot, 'Old physical-looking visual paths are not referenced by the private proof page')
check('digital_only', 'Future bundle is explicitly digital-only', 'digital PDF bundle only' in pilot and 'not a hardcover, shipped kit' in pilot, 'Private buyer copy sets the digital-versus-physical boundary')
check('no_fillable_claim', 'No unsupported fillable claim is made', 'fillable purchaser PDF' in pilot and 'do not establish a tagged or fillable purchaser PDF' in pilot, 'Renderer states fillable capability is not established')
check('no_accessibility_completion_claim', 'No unsupported PDF accessibility completion claim is made', 'current proofs are not tagged and have no PDF form fields' in pilot, 'Renderer states current proof-file limits')

pdf_us = ROOT / 'internal/commerce-pilot/execution-planner-v1/print-review/NORTH_1-3-5_Execution_Planner_US-Letter_PRIVATE-REVIEW.pdf'
pdf_a4 = ROOT / 'internal/commerce-pilot/execution-planner-v1/print-review/NORTH_1-3-5_Execution_Planner_A4_PRIVATE-REVIEW.pdf'
info_us = subprocess.check_output(['pdfinfo', str(pdf_us)], text=True)
info_a4 = subprocess.check_output(['pdfinfo', str(pdf_a4)], text=True)
check('print_proof_metadata', 'Actual print proof metadata remains truthful', 'Pages:           31' in info_us and 'Page size:       612 x 792 pts (letter)' in info_us and 'Pages:           27' in info_a4 and 'Page size:       595.276 x 841.89 pts (A4)' in info_a4, 'US Letter = 31 pages; A4 = 27 pages')
check('pdf_status', 'Current PDF limitations are documented', 'Tagged:          no' in info_us and 'Form:            none' in info_us and 'Tagged:          no' in info_a4 and 'Form:            none' in info_a4, 'Both private proof PDFs are untagged and non-form PDFs')

for key, value in (('commerceEnabled', 'false'), ('merchantProduct', 'null'), ('checkoutUrl', 'null'), ('deliveryEnabled', 'false')):
    expected = f'{key}: {value}'
    check(f'closed_{key}', f'Closed commerce configuration: {expected}', expected in pilot, f'{expected} is explicitly retained')
forbidden_endpoints = ('stripe.com', 'gumroad.com', 'shopify.com', 'checkout.stripe', 'google-analytics', 'googletagmanager.com', 'gtag(')
check('no_commerce_integrations', 'No payment, merchant, or tracking integration endpoints', not any(token in (pilot + public_site + public_catalog).lower() for token in forbidden_endpoints), 'No prohibited payment or tracking endpoint found')
check('no_public_price', 'No public price appears in the public catalog or public renderer', '$19' not in public_catalog and '$19' not in public_site, 'Founder-only price is not placed on public candidate routes')
check('asset_register', 'Asset-and-claim register documents approved, illustrative, and quarantined visual status', all(fragment in asset_register for fragment in ('Quarantined from primary proof', 'Approved private proof', 'Illustrative digital product mockup')), 'Asset register contains required approval and disclosure controls')
check('product_truth_route', 'Private product-truth and launch-gate route exists', (ROOT / 'internal/phase2g-product-truth.html').is_file() and '/internal/phase2g-product-truth.html' in pilot, 'Private governance page is present and linked from private review')

expected_locales = ['en', 'pt-BR', 'es-419', 'fr', 'de', 'it', 'ja', 'ko', 'zh-Hans', 'zh-Hant', 'ar', 'ru', 'pl', 'nl']
check('locale_registry', 'All 14 verified mobile-app locales remain in source registry', all(f"locale('{code}'" in locale for code in expected_locales), f'{len(expected_locales)} expected locale codes found')
check('arabic_rtl', 'Arabic retains RTL metadata and QA state', "locale('ar'" in locale and "dir: 'rtl'" in locale and 'requiresRtlQA: true' in locale, 'Arabic route remains declared RTL with QA requirement')
check('canonical_hreflang', 'Canonical and hreflang creation remains intact', 'canonical.href' in public_site and "link.hreflang=item.code" in public_site and "hreflang='x-default'" in public_site, 'Canonical, all-locale hreflang, and x-default logic remain')
check('language_availability_copy', 'Locale architecture does not imply localized product availability', 'English private founder-review candidate only; no customer product-language release.' in public_catalog and 'governed_route_pending_human_review' in locale, 'Product-language and route-readiness states remain distinct')
check('focus_and_skip', 'Visible focus and skip-link controls remain', '.skip-link:focus' in public_css and ':focus-visible' in public_css and ':focus-visible' in pilot_css, 'Public and private styles include focus treatments')
check('reduced_motion', 'Reduced-motion controls remain on public and private styles', '@media (prefers-reduced-motion:reduce)' in public_css and '@media(prefers-reduced-motion:reduce)' in pilot_css, 'Both style systems declare reduced-motion behavior')
check('responsive_390', '390px mobile rule exists on public and private styles', '@media (max-width:390px)' in public_css and '@media(max-width:390px)' in pilot_css, 'Public and private mobile rules are present')
check('image_budget', 'Proof and hero delivery assets satisfy private page size budget', all((ROOT / path).stat().st_size < 400000 for path in proof_assets) and (ROOT / 'assets/product-presentation/web/planner-hero-illustrative.webp').stat().st_size < 800000, 'Proof PNGs < 400KB each; optimized hero WebP < 800KB')

result = {'phase': 'Phase 2G', 'passed': all(item['passed'] for item in checks), 'checks': checks, 'passed_count': sum(item['passed'] for item in checks), 'total_count': len(checks)}
EVIDENCE.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
raise SystemExit(0 if result['passed'] else 1)
