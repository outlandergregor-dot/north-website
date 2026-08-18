#!/usr/bin/env python3
from pathlib import Path
import json,requests,hashlib
ROOT=Path('/home/ubuntu/north-phase2f-presentation')
OUT=ROOT/'assets/product-presentation/higgsfield'
OUT.mkdir(parents=True,exist_ok=True)
assets=[
 (1,'planner-hero-illustrative.png','671fbd8b-ada7-4d3b-985e-b10f600c9912','https://d8j0ntlcm91z4.cloudfront.net/user_38UVjehqX6cPedpN0VbHItSSCU8/hf_20260818_225608_671fbd8b-ada7-4d3b-985e-b10f600c9912.png','Website hero','Illustrative digital product mockup of the NORTH 1-3-5 Execution Planner on a warm refined desk.'),
 (2,'planner-morning-desk-illustrative.png','eb8f2ee1-b9b7-4450-8a5f-0b51aafbbb99','https://d8j0ntlcm91z4.cloudfront.net/user_38UVjehqX6cPedpN0VbHItSSCU8/hf_20260818_225608_eb8f2ee1-b9b7-4450-8a5f-0b51aafbbb99.png','Product detail sequence','Illustrative calm morning desk scene for the NORTH 1-3-5 Execution Planner.'),
 (3,'planner-weekly-reset-illustrative.png','a921b09c-5a4b-4574-9b84-d232b818e63d','https://d8j0ntlcm91z4.cloudfront.net/user_38UVjehqX6cPedpN0VbHItSSCU8/hf_20260818_225608_a921b09c-5a4b-4574-9b84-d232b818e63d.png','Product detail sequence','Illustrative weekly reset desk scene for the NORTH 1-3-5 Execution Planner.'),
 (4,'planner-two-week-rhythm-illustrative.png','6318def5-61c0-4540-a5d2-28520a2bb6e2','https://d8j0ntlcm91z4.cloudfront.net/user_38UVjehqX6cPedpN0VbHItSSCU8/hf_20260818_225608_6318def5-61c0-4540-a5d2-28520a2bb6e2.png','Two-week rhythm section','Illustrative digital product presentation for starting a two-week Planner rhythm.'),
 (5,'planner-weekly-review-illustrative.png','b2637a2e-c6e2-48d8-9c7f-3421f4428a9c','https://d8j0ntlcm91z4.cloudfront.net/user_38UVjehqX6cPedpN0VbHItSSCU8/hf_20260818_225608_b2637a2e-c6e2-48d8-9c7f-3421f4428a9c.png','Weekly review section','Illustrative digital product presentation for a Planner weekly review.'),
 (6,'social-calm-direction-illustrative.png','fb0fe8f4-c638-48ab-9dae-e7f424309fcf','https://d8j0ntlcm91z4.cloudfront.net/user_38UVjehqX6cPedpN0VbHItSSCU8/hf_20260818_225608_fb0fe8f4-c638-48ab-9dae-e7f424309fcf.png','Instagram portrait','Illustrative portrait product presentation for the NORTH 1-3-5 Execution Planner.'),
 (7,'social-method-illustrative.png','4db32c1b-1f5d-4f2b-a41d-ddd9aa140b3a','https://d8j0ntlcm91z4.cloudfront.net/user_38UVjehqX6cPedpN0VbHItSSCU8/hf_20260818_225608_4db32c1b-1f5d-4f2b-a41d-ddd9aa140b3a.png','Instagram portrait','Illustrative product presentation inspired by the 1-3-5 method.'),
 (8,'story-reel-cover-illustrative.png','95836871-6a9e-44e8-be6c-ececc7ff3fbf','https://d8j0ntlcm91z4.cloudfront.net/user_38UVjehqX6cPedpN0VbHItSSCU8/hf_20260818_225608_95836871-6a9e-44e8-be6c-ececc7ff3fbf.png','Story or Reel cover','Illustrative vertical product presentation for the NORTH 1-3-5 Execution Planner.'),
]
rows=[]
for index,name,job,url,use,alt in assets:
 data=requests.get(url,timeout=120).content
 p=OUT/name;p.write_bytes(data)
 rows.append({'id':f'P{index:02d}','file':str(p.relative_to(ROOT)),'higgsfield_job_id':job,'source':'Higgsfield marketing_studio_image using official NORTH compass and existing Planner cover references','prompt_file':'internal/product-presentation/higgsfield-image-batch.json','intended_usage':use,'disclosure':'Illustrative AI-assisted digital product presentation; not a physical product photograph; no planner page content is claimed from this image.','alt_text':alt,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
manifest=ROOT/'internal/product-presentation/phase2f-visual-asset-inventory.json'
manifest.write_text(json.dumps({'phase':'2F Premium Product Presentation Pilot','assets':rows},indent=2)+'\n')
print(json.dumps(rows,indent=2))
