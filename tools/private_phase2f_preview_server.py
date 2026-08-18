#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import base64,os
ROOT=Path('/home/ubuntu/north-phase2f')
USER='northfounder'
PASSWORD=os.environ['NORTH_PHASE2F_PREVIEW_PASSWORD']
TOKEN='Basic '+base64.b64encode(f'{USER}:{PASSWORD}'.encode()).decode()
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs): super().__init__(*args,directory=str(ROOT),**kwargs)
    def do_GET(self):
        if self.headers.get('Authorization')!=TOKEN:
            self.send_response(401); self.send_header('WWW-Authenticate','Basic realm="NORTH Phase 2F Founder Review"'); self.send_header('Cache-Control','no-store'); self.end_headers(); return
        if self.path in {'/','/?'}: self.path='/internal/commerce-pilot.html'
        return super().do_GET()
    def end_headers(self):
        self.send_header('Cache-Control','no-store'); self.send_header('X-Robots-Tag','noindex, nofollow, noarchive'); super().end_headers()
ThreadingHTTPServer(('0.0.0.0',4190),Handler).serve_forever()
