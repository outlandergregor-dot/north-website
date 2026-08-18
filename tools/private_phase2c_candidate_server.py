#!/usr/bin/env python3
"""Password-protected local review server for the exported Phase 2C static candidate only."""
from __future__ import annotations
from base64 import b64decode
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
import hmac
import os

ROOT = Path('/home/ubuntu/north-phase2c/release-candidate/NORTH_PHASE2C_STATIC_RELEASE_CANDIDATE/website')
PASSWORD_FILE = Path('/home/ubuntu/north-phase2c/.phase2c-preview-password')
USER = 'northfounder'
LOCALES = {'pt-BR','es-419','fr','de','it','ja','ko','zh-Hans','zh-Hant','ar','ru','pl','nl'}
ENGLISH = {'/':'/index.html','/library':'/library/index.html','/library/free-tools':'/library/free-tools/index.html','/library/resources':'/library/resources/index.html','/library/programs':'/library/programs/index.html','/library/books':'/library/books/index.html','/library/money-education':'/library/money-education/index.html','/library/item':'/library/item/index.html','/about':'/about/index.html'}

def destination(path: str):
    if path in ENGLISH: return ENGLISH[path]
    bits = [bit for bit in path.split('/') if bit]
    if bits and bits[0] in LOCALES:
        code, rest = bits[0], '/' + '/'.join(bits[1:])
        target = {'/':'index.html','/library':'library/index.html','/library/free-tools':'library/free-tools/index.html','/library/resources':'library/resources/index.html','/library/programs':'library/programs/index.html','/library/books':'library/books/index.html','/library/money-education':'library/money-education/index.html','/library/item':'library/item/index.html','/about':'about/index.html'}.get(rest or '/')
        return f'/{code}/{target}' if target else None
    return None

def authorized(header: str | None):
    if not header or not header.startswith('Basic '): return False
    try: decoded = b64decode(header[6:]).decode('utf-8')
    except Exception: return False
    expected = f'{USER}:{PASSWORD_FILE.read_text(encoding="utf-8").strip()}'
    return hmac.compare_digest(decoded, expected)

class Handler(SimpleHTTPRequestHandler):
    def do_authhead(self):
        self.send_response(401); self.send_header('WWW-Authenticate','Basic realm="NORTH Phase 2C Founder Review"'); self.send_header('Cache-Control','no-store'); self.end_headers()
    def do_GET(self):
        if not authorized(self.headers.get('Authorization')): return self.do_authhead()
        parsed = urlparse(self.path); mapped = destination(parsed.path)
        if mapped: self.path = mapped + (f'?{parsed.query}' if parsed.query else '')
        return super().do_GET()
    def end_headers(self):
        self.send_header('X-Robots-Tag','noindex, nofollow, noarchive')
        self.send_header('Cache-Control','no-store')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(ROOT)
    ThreadingHTTPServer(('0.0.0.0',4184),Handler).serve_forever()
