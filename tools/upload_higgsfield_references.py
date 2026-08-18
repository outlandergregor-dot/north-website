#!/usr/bin/env python3
import json
from pathlib import Path
import requests

ROOT=Path('/home/ubuntu/north-phase2f-presentation')
RESULT=Path('/home/ubuntu/.mcp/tool-results/2026-08-18_22-53-57.861726706_higgsfield_media_upload_272d0ce2.json')
records=json.loads(RESULT.read_text())['structuredContent']['uploads']
paths={
 'north-compass-official-512.png': ROOT/'assets/brand/north-compass-official-512.png',
 'execution-planner-cover-art.png': ROOT/'assets/product-visuals/execution-planner-cover-art.png',
 'planner-page-07.png': ROOT/'assets/product-presentation/references/planner-page-07.png',
 'planner-page-08.png': ROOT/'assets/product-presentation/references/planner-page-08.png',
}
out=[]
for record in records:
    name=record['instructions'].split('@',1)[1].split(" '",1)[0]
    path=paths[name]
    response=requests.put(record['upload_url'],data=path.read_bytes(),headers={'Content-Type':record['content_type']},timeout=90)
    response.raise_for_status()
    out.append({'label':name,'media_id':record['media_id'],'url':record['url'],'source_path':str(path.relative_to(ROOT))})
manifest=ROOT/'internal/product-presentation/higgsfield-reference-media.json'
manifest.write_text(json.dumps({'purpose':'Phase 2F documented Planner presentation references','uploads':out},indent=2)+'\n')
print(json.dumps(out,indent=2))
