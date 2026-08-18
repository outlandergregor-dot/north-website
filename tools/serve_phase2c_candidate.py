#!/usr/bin/env python3
"""Local clean-route simulator for the exported Phase 2C static candidate only."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
import os

ROOT = Path('/home/ubuntu/north-phase2c/release-candidate/NORTH_PHASE2C_STATIC_RELEASE_CANDIDATE/website')
LOCALES = {'pt-BR','es-419','fr','de','it','ja','ko','zh-Hans','zh-Hant','ar','ru','pl','nl'}
ENGLISH = {'/':'/index.html','/library':'/library/index.html','/library/free-tools':'/library/free-tools/index.html','/library/resources':'/library/resources/index.html','/library/programs':'/library/programs/index.html','/library/books':'/library/books/index.html','/library/money-education':'/library/money-education/index.html','/library/item':'/library/item/index.html','/about':'/about/index.html'}

def destination(path: str):
    if path in ENGLISH: return ENGLISH[path]
    bits = [bit for bit in path.split('/') if bit]
    if bits and bits[0] in LOCALES:
        code, rest = bits[0], '/' + '/'.join(bits[1:])
        suffix = {'/':'index.html','/library':'library/index.html','/library/free-tools':'library/free-tools/index.html','/library/resources':'library/resources/index.html','/library/programs':'library/programs/index.html','/library/books':'library/books/index.html','/library/money-education':'library/money-education/index.html','/library/item':'library/item/index.html','/about':'about/index.html'}.get(rest or '/')
        return f'/{code}/{suffix}' if suffix else None
    return None
class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('X-Robots-Tag','noindex, nofollow, noarchive')
        super().end_headers()
    def do_GET(self):
        parsed = urlparse(self.path); mapped = destination(parsed.path)
        if mapped: self.path = mapped + (f'?{parsed.query}' if parsed.query else '')
        return super().do_GET()
if __name__ == '__main__':
    os.chdir(ROOT)
    ThreadingHTTPServer(('0.0.0.0',4182),Handler).serve_forever()
