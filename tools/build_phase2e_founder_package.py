#!/usr/bin/env python3
from pathlib import Path
import shutil, zipfile, hashlib, json

ROOT=Path('/home/ubuntu/north-phase2e')
OUT=ROOT/'evidence/NORTH_PHASE2E_FOUNDER_REVIEW_PACKAGE'
ZIP=ROOT/'evidence/NORTH_PHASE2E_FOUNDER_REVIEW_PACKAGE.zip'
FILES={
 'README.md':'evidence/PHASE2E_ACCEPTANCE_RECORD.md',
 'planner/CORE_DIGITAL_RELEASE_SPEC.md':'internal/commerce-readiness/execution-planner-core-digital-release-spec.md',
 'planner/EDITABLE_ENGLISH_MASTER.md':'internal/commerce-pilot/execution-planner-v1/editable-source/01-execution-planner-customer-master.md',
 'planner/NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-US-Letter_private-release-candidate.pdf':'internal/commerce-readiness/core-digital-bundle-candidate/NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-US-Letter_private-release-candidate.pdf',
 'planner/NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-A4_private-release-candidate.pdf':'internal/commerce-readiness/core-digital-bundle-candidate/NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-A4_private-release-candidate.pdf',
 'planner/PERSONAL_USE_LICENSE_DRAFT.md':'internal/commerce-pilot/execution-planner-v1/policy-drafts/01-personal-use-license-draft.md',
 'planner/SUPPORT_REFUND_DRAFT.md':'internal/commerce-pilot/execution-planner-v1/policy-drafts/02-support-and-refund-information-draft.md',
 'planner/assets/execution-planner-cover-art.png':'assets/product-visuals/execution-planner-cover-art.png',
 'planner/assets/execution-planner-open-spread.png':'assets/product-visuals/execution-planner-open-spread.png',
 'planner/assets/execution-planner-desk-kit.png':'assets/product-visuals/execution-planner-desk-kit.png',
 'planner/assets/execution-planner-detail.png':'assets/product-visuals/execution-planner-detail.png',
 'commerce/NEUTRAL_MERCHANT_COMPARISON.md':'internal/commerce-readiness/neutral-merchant-comparison.md',
 'commerce/OFFICIAL_MERCHANT_RESEARCH.md':'internal/commerce-readiness/official-merchant-research.md',
 'commerce/CLOSED_BETA_OPERATING_SYSTEM.md':'internal/commerce-readiness/closed-beta-commerce-operating-system.md',
 'commerce/FUTURE_OPT_IN_SHARING_SPEC.md':'internal/commerce-readiness/future-opt-in-sharing-spec.md',
 'catalog/GOVERNED_CATALOG_ROADMAP.md':'internal/commerce-readiness/phase2e-catalog-governance.md',
 'catalog/phase2e-catalog.js':'assets/phase2e-catalog.js',
 'catalog/PLANNER_LOCALE_AVAILABILITY_RECORD.txt':'assets/product-studio-config.js',
 'evidence/PHASE2E_ACCEPTANCE_RECORD.md':'evidence/PHASE2E_ACCEPTANCE_RECORD.md',
 'evidence/PHASE2E_PRIVATE_PREVIEW_RECORD.md':'evidence/PHASE2E_PRIVATE_PREVIEW_RECORD.md',
 'evidence/phase2e-verification.json':'evidence/phase2e-verification.json',
 'evidence/phase2e-browser-qa.txt':'evidence/phase2e-browser-qa.txt',
 'evidence/phase2e-visual-qa.md':'evidence/phase2e-visual-qa.md',
 'evidence/screenshots/planner-private-phase2e-desktop.webp':'evidence/planner-private-phase2e-desktop.webp',
 'evidence/screenshots/planner-private-phase2e-mobile.png':'evidence/screenshots/phase2e-planner-mobile.png',
 'evidence/screenshots/roadmap-private-desktop.png':'evidence/screenshots/phase2e-roadmap-desktop.png',
 'evidence/screenshots/operations-private-mobile.png':'evidence/screenshots/phase2e-operations-mobile.png'
}
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)
manifest=[]
for target,source in FILES.items():
    src=ROOT/source
    if not src.exists(): raise FileNotFoundError(src)
    dst=OUT/target; dst.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(src,dst)
    manifest.append({'path':target,'bytes':dst.stat().st_size,'sha256':hashlib.sha256(dst.read_bytes()).hexdigest()})
(OUT/'MANIFEST.json').write_text(json.dumps({'phase':'2E','private_only':True,'files':manifest},indent=2)+'\n',encoding='utf-8')
if ZIP.exists(): ZIP.unlink()
with zipfile.ZipFile(ZIP,'w',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(OUT.rglob('*')):
        if f.is_file(): z.write(f,f.relative_to(OUT.parent))
print(ZIP)
print(hashlib.sha256(ZIP.read_bytes()).hexdigest())
