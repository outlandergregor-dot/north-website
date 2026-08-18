#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re, subprocess

ROOT=Path('/home/ubuntu/north-phase2f')
SOURCE=ROOT/'internal/commerce-pilot/execution-planner-v1/editable-source/01-execution-planner-customer-master.md'
PDFS={
 'us_letter':ROOT/'internal/commerce-readiness/core-digital-bundle-candidate/NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-US-Letter_private-release-candidate.pdf',
 'a4':ROOT/'internal/commerce-readiness/core-digital-bundle-candidate/NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-A4_private-release-candidate.pdf'
}
checks=[]
def check(name,condition,evidence): checks.append({'check':name,'passed':bool(condition),'evidence':evidence})
body=SOURCE.read_text(encoding='utf-8')
days=len(re.findall(r'^## Day \d+',body,re.M))
weekly=len(re.findall(r'^# Week (?:One|Two) Reset / Review',body,re.M))
continuation=bool(re.search(r'^# Final Two-Week Review and Continuation Plan',body,re.M))
fictional=bool(re.search(r'^# Fictional Worked Example',body,re.M))
writable=len(re.findall(r'_{8,}',body))
check('editable_source_present',SOURCE.exists(),str(SOURCE.relative_to(ROOT)))
check('exactly_14_daily_sections',days==14,f'{days} Day headings')
check('exactly_2_weekly_reviews',weekly==2,f'{weekly} weekly reset/review headings')
check('continuation_plan_present',continuation,'Final Two-Week Review and Continuation Plan')
check('fictional_example_labeled',fictional,'Fictional Worked Example heading')
check('writable_field_cues',writable>=70,f'{writable} underscore field cues')
boundary_terms = ['not legal, medical, mental-health, financial, tax', 'does not diagnose, treat, or guarantee an outcome']
check('non_guarantee_boundary', all(x in body.lower() for x in boundary_terms), 'reviewed scope boundary language')

pdf_records={}
for name,path in PDFS.items():
    exists=path.exists(); check(f'{name}_exists',exists,str(path.relative_to(ROOT)))
    if not exists: continue
    info=subprocess.check_output(['pdfinfo',str(path)],text=True)
    pages=int(re.search(r'Pages:\s+(\d+)',info).group(1))
    page_size=re.search(r'Page size:\s+(.+)',info).group(1).strip()
    text_out=subprocess.check_output(['pdftotext',str(path),'-'],text=True,errors='replace')
    text_len=len(re.sub(r'\s+',' ',text_out).strip())
    sha=hashlib.sha256(path.read_bytes()).hexdigest()
    expected='612 x 792' if name=='us_letter' else '595.276 x 841.89'
    check(f'{name}_page_geometry',expected in page_size,page_size)
    check(f'{name}_page_count',pages>=20,f'{pages} pages')
    check(f'{name}_text_extractable',text_len>5000,f'{text_len} normalized text characters')
    check(f'{name}_private_marker','Private release candidate' in text_out or 'Private Release Candidate' in text_out,'private candidate marking')
    pdf_records[name]={'file':path.name,'pages':pages,'page_size':page_size,'normalized_text_characters':text_len,'sha256':sha}

report={'phase':'2F','source_revision':'0b5667b48adfa6708b75e0b5863845d43ce0f581','source':{'file':SOURCE.name,'sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'daily_sections':days,'weekly_reviews':weekly,'writable_field_cues':writable},'pdfs':pdf_records,'passed':sum(c['passed'] for c in checks),'total':len(checks),'checks':checks}
(ROOT/'evidence').mkdir(exist_ok=True)
(ROOT/'evidence/phase2f-planner-audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
raise SystemExit(0 if report['passed']==report['total'] else 1)
