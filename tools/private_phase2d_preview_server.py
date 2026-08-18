#!/usr/bin/env python3
"""Temporary Phase 2D founder-review server. Never use for production hosting."""
from base64 import b64decode
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os

ROOT = Path('/home/ubuntu/north-phase2d')
USER = 'northfounder'
PASSWORD = Path('/home/ubuntu/north-phase2d/.phase2d-preview-password').read_text(encoding='utf-8').strip()
EXPECTED = 'Basic ' + __import__('base64').b64encode(f'{USER}:{PASSWORD}'.encode()).decode()

class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = path.split('?',1)[0].split('#',1)[0]
        if path == '/': path = '/internal/commerce-pilot.html'
        return str(ROOT / path.lstrip('/'))
    def _authorized(self): return self.headers.get('Authorization') == EXPECTED
    def _deny(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="NORTH Phase 2D Founder Review"')
        self.send_header('Cache-Control','no-store, private')
        self.send_header('X-Robots-Tag','noindex, nofollow, noarchive')
        self.end_headers()
    def do_GET(self):
        if not self._authorized(): return self._deny()
        return super().do_GET()
    def do_HEAD(self):
        if not self._authorized(): return self._deny()
        return super().do_HEAD()
    def end_headers(self):
        self.send_header('Cache-Control','no-store, private')
        self.send_header('X-Robots-Tag','noindex, nofollow, noarchive')
        super().end_headers()

if __name__=='__main__':
    os.chdir(ROOT)
    ThreadingHTTPServer(('0.0.0.0',4186),Handler).serve_forever()
