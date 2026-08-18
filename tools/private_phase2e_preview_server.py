#!/usr/bin/env python3
"""Temporary founder-review server; not a production host or deployment tool."""
from base64 import b64decode
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
import os

ROOT=Path(__file__).resolve().parents[1]
PASSWORD_FILE=ROOT/'.phase2e-preview-password'
USER='northfounder'

class Handler(SimpleHTTPRequestHandler):
    def authorized(self):
        auth=self.headers.get('Authorization','')
        if not auth.startswith('Basic '): return False
        try:
            value=b64decode(auth.split(' ',1)[1]).decode('utf-8')
        except Exception: return False
        return value==f'{USER}:{PASSWORD_FILE.read_text(encoding="utf-8").strip()}'
    def challenge(self):
        self.send_response(401); self.send_header('WWW-Authenticate','Basic realm="NORTH Phase 2E Founder Review"'); self.send_header('Cache-Control','no-store'); self.end_headers()
    def do_GET(self):
        if not self.authorized(): return self.challenge()
        parsed=urlparse(self.path)
        if parsed.path=='/': self.path='/internal/commerce-pilot.html'
        return super().do_GET()
    def end_headers(self):
        self.send_header('X-Robots-Tag','noindex, nofollow, noarchive')
        self.send_header('Cache-Control','no-store, private')
        super().end_headers()

if __name__=='__main__':
    os.chdir(ROOT)
    ThreadingHTTPServer(('0.0.0.0',4188),Handler).serve_forever()
