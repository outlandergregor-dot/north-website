#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,shutil,zipfile
ROOT=Path('/home/ubuntu/north-phase2f')
OUT=ROOT/'evidence'/'NORTH_PHASE2F_FOUNDER_DECISION_PACKET'
ZIP=ROOT/'evidence'/'NORTH_PHASE2F_FOUNDER_DECISION_PACKET.zip'
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)
files=[
 'evidence/PHASE2F_ACCEPTANCE_RECORD.md','evidence/PHASE2F_PRIVATE_PREVIEW_RECORD.md','evidence/phase2f-planner-audit.json','evidence/phase2f-verification.json','evidence/phase2f-browser-qa.txt','evidence/phase2f-visual-qa.md','evidence/screenshots/phase2f-home-premium-desktop.webp',
 'internal/design-system/phase2f-premium-visual-system.md','internal/commerce-readiness/phase2f-planner-version-and-qa.md','internal/commerce-readiness/phase2f-pilot-decision-package.md',
 'internal/commerce-pilot/execution-planner-v1/editable-source/01-execution-planner-customer-master.md',
 'internal/commerce-readiness/core-digital-bundle-candidate/NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-US-Letter_private-release-candidate.pdf',
 'internal/commerce-readiness/core-digital-bundle-candidate/NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-A4_private-release-candidate.pdf',
 'assets/brand/north-compass-official-512.png','assets/brand/favicon/north-compass-32.png',
 'assets/product-visuals/execution-planner-cover-art.png','assets/product-visuals/execution-planner-open-spread.png','assets/product-visuals/execution-planner-desk-kit.png','assets/product-visuals/execution-planner-detail.png'
]
manifest=[]
for relative in files:
 src=ROOT/relative
 if not src.exists(): raise FileNotFoundError(relative)
 dest=OUT/relative; dest.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dest)
 manifest.append({'file':relative,'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'bytes':src.stat().st_size})
(OUT/'MANIFEST.json').write_text(json.dumps({'phase':'2F','scope':'Private founder validation only; no commerce activation','files':manifest},indent=2)+'\n',encoding='utf-8')
if ZIP.exists(): ZIP.unlink()
with zipfile.ZipFile(ZIP,'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(OUT.rglob('*')):
  if p.is_file(): z.write(p,p.relative_to(OUT.parent))
with zipfile.ZipFile(ZIP) as z: bad=z.testzip()
if bad: raise RuntimeError(bad)
print(json.dumps({'zip':str(ZIP),'sha256':hashlib.sha256(ZIP.read_bytes()).hexdigest(),'files':len(manifest)},indent=2))
