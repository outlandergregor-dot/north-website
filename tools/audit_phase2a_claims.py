#!/usr/bin/env python3
"""Static copy, claim, and public-action audit for NORTH Phase 2A private Product Studio."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path('/home/ubuntu/north-phase2a')
PUBLIC_FILES = [
    ROOT / 'library.html', ROOT / 'library-resources.html', ROOT / 'library-programs.html',
    ROOT / 'library-books.html', ROOT / 'library-item.html', ROOT / 'assets/product-studio.js',
    ROOT / 'assets/product-studio-config.js', ROOT / 'assets/product-studio.css'
]
TEXT = '\n'.join(path.read_text(encoding='utf-8', errors='replace') for path in PUBLIC_FILES)

checks = {
    'public_commerce_destination': r'href=["\'][^"\']*(?:checkout|cart|payment|gumroad|stripe|paypal)[^"\']*',
    'public_email_capture_form': r'<form[^>]*(?:email|newsletter|subscribe|mailchimp)',
    'public_google_play_destination': r'href=["\'][^"\']*(?:play\.google|googleplay)[^"\']*',
    'fake_testimonial_or_social_proof': r'\b(?:testimonial|bestseller|rated\s+[0-9]|reviews?\s+from|customers\s+love)\b',
    'urgency_or_savings_claim': r'\b(?:limited\s+time|save\s+\$|sale\s+ends|only\s+today|discount)\b',
    'unsupported_language_scale_claim': r'\b(?:14\s+languages|available\s+in\s+14|all\s+languages)\b',
}
hits = {name: re.findall(pattern, TEXT, flags=re.IGNORECASE) for name, pattern in checks.items()}
hits = {name: found for name, found in hits.items() if found}

product_config = (ROOT / 'assets/product-studio-config.js').read_text(encoding='utf-8')
approved_statuses = len(re.findall(r"status:\s*'approved_for_sale'", product_config))
public_visibilities = len(re.findall(r'publicVisibility:\s*true', product_config))

# Money language is allowed only as an explicit no-advice/review boundary in the studio.
money_boundary_markers = [
    'Not for legal, medical, financial, investment, tax, or other professional advice.',
    'qualified financial-professional and legal review',
    'does not provide individual advice'
]
money_boundary_missing = [marker for marker in money_boundary_markers if marker.lower() not in TEXT.lower()]

result = {
    'branch': 'north-web-phase2a-product-studio',
    'source_baseline': 'e7e81968127f8f7ef7e76c09475312ebda68477b',
    'files_scanned': [path.relative_to(ROOT).as_posix() for path in PUBLIC_FILES],
    'prohibited_claim_or_action_hits': hits,
    'registry_approved_for_sale_status_literal_count': approved_statuses,
    'registry_public_visibility_true_count': public_visibilities,
    'money_boundary_markers_missing': money_boundary_missing,
    'result': 'PASS' if not hits and approved_statuses == 0 and public_visibilities == 0 and not money_boundary_missing else 'FAIL'
}
(ROOT / 'evidence').mkdir(exist_ok=True)
(ROOT / 'evidence/phase2a-claims-audit.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
