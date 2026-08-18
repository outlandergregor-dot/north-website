#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path('/home/ubuntu/north-phase2f-presentation')
EXPECTED_BRANCH = 'north-web-phase2f-product-presentation-pilot'
assets = [
    'planner-hero-illustrative',
    'planner-morning-desk-illustrative',
    'planner-weekly-reset-illustrative',
    'planner-two-week-rhythm-illustrative',
    'planner-weekly-review-illustrative',
    'social-calm-direction-illustrative',
    'social-method-illustrative',
    'story-reel-cover-illustrative',
]
checks = []

def check(name, condition, detail):
    checks.append({'name': name, 'pass': bool(condition), 'detail': detail})

branch = subprocess.check_output(['git', '-C', str(ROOT), 'branch', '--show-current'], text=True).strip()
check('Correct isolated branch', branch == EXPECTED_BRANCH, branch)

manifest_path = ROOT / 'internal/product-presentation/phase2f-visual-asset-inventory.json'
manifest = json.loads(manifest_path.read_text())
manifest_assets = manifest.get('assets', [])
check('Eight recorded source assets', len(manifest_assets) == 8, f'{len(manifest_assets)} assets in manifest')
check('All source files exist', all((ROOT / item['file']).is_file() for item in manifest_assets), 'Source PNG presence')
check('All manifest disclosures are truthful', all('Illustrative' in item.get('disclosure', '') and 'physical product' in item.get('disclosure', '') for item in manifest_assets), 'Illustrative and physical-product limitation recorded')
check('All original asset hashes match manifest', all(hashlib.sha256((ROOT / item['file']).read_bytes()).hexdigest() == item.get('sha256') for item in manifest_assets), 'SHA-256 provenance verification')
check('All optimized web assets exist', all((ROOT / 'assets/product-presentation/web' / f'{name}.webp').is_file() for name in assets), 'Responsive WebP delivery copies')

js = (ROOT / 'assets/commerce-pilot.js').read_text()
css = (ROOT / 'assets/commerce-pilot.css').read_text()
html = (ROOT / 'internal/commerce-pilot.html').read_text()
server = (ROOT / 'tools/private_phase2f_presentation_preview_server.py').read_text()

check('Hero uses optimized illustrative asset', '/assets/product-presentation/web/planner-hero-illustrative.webp' in js, 'Hero asset reference')
check('Gallery includes all four illustrative presentation cards', all(f'/assets/product-presentation/web/{name}.webp' in js for name in assets[1:5]), 'Four supporting image references')
check('Required hero disclosure exists', 'Illustrative digital product mockup — not a physical product photograph.' in js, 'Exact required disclosure')
check('Actual-page and illustrative evidence are separated', 'Real Planner-page detail' in js and 'Premium visual presentation' in js, 'Separate named sections')
check('Official compass remains the page brand anchor', '/assets/brand/north-compass-official-512.png' in js, 'Official supplied asset reference')
check('Commerce is disabled in configuration', "commerceEnabled:false" in js and "deliveryEnabled:false" in js and 'merchantProduct:null' in js and 'checkoutUrl:null' in js, 'Inactive configuration values')
check('No active checkout URL', 'https://checkout' not in js and 'gumroad.com' not in js and 'stripe.com' not in js, 'No merchant endpoint in renderer')
check('No email capture form added', '<input' not in js.lower() and '<form' not in js.lower(), 'No collection surface in renderer')
check('Private route retains noindex', 'noindex' in html.lower() and 'nofollow' in html.lower(), 'Route metadata')
check('Responsive gallery rules exist', '@media(max-width:800px)' in css and '.pilot-presentation-grid{grid-template-columns:1fr' in css, 'Mobile single-column gallery')
check('Preview server confines root to current worktree', "ROOT = Path('/home/ubuntu/north-phase2f-presentation')" in server and "'4192'" in server, 'Isolated root and port default')
check('Preview server sends private headers', 'noindex, nofollow, noarchive' in server and 'no-store' in server and 'WWW-Authenticate' in server, 'Authenticated no-cache noindex policy')

passed = sum(item['pass'] for item in checks)
report = {
    'phase': '2F Premium Product Presentation Pilot',
    'branch': branch,
    'passed': passed,
    'total': len(checks),
    'status': 'PASS' if passed == len(checks) else 'FAIL',
    'checks': checks,
}
out = ROOT / 'evidence/phase2f-product-presentation-verification.json'
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
sys.exit(0 if report['status'] == 'PASS' else 1)
