#!/usr/bin/env python3
"""Authenticated, no-store private review server for the Phase 2G worktree only."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlsplit
import base64
import os

ROOT = Path('/home/ubuntu/north-phase2g-product-truth')
USER = 'northfounder'
PASSWORD = os.environ['NORTH_PHASE2G_PREVIEW_PASSWORD']
PORT = int(os.environ.get('NORTH_PHASE2G_PREVIEW_PORT', '4193'))
TOKEN = 'Basic ' + base64.b64encode(f'{USER}:{PASSWORD}'.encode()).decode()
LOCALES = {'en', 'pt-BR', 'es-419', 'fr', 'de', 'it', 'ja', 'ko', 'zh-Hans', 'zh-Hant', 'ar', 'ru', 'pl', 'nl'}
ROUTES = {
    '/': '/internal/commerce-pilot.html',
    '/library': '/library.html',
    '/library/resources': '/library-resources.html',
    '/library/programs': '/library-programs.html',
    '/library/books': '/library-books.html',
    '/library/money-education': '/library-money-education.html',
    '/library/free-tools': '/library-free-tools.html',
    '/library/item': '/library-item.html',
    '/about': '/about.html',
}


def fallback_route(path: str) -> str | None:
    if path in ROUTES:
        return ROUTES[path]
    parts = [part for part in path.split('/') if part]
    if parts and parts[0] in LOCALES:
        suffix = '/' + '/'.join(parts[1:]) if len(parts) > 1 else '/'
        return ROUTES.get(suffix)
    return None


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.headers.get('Authorization') != TOKEN:
            self.send_response(401)
            self.send_header('WWW-Authenticate', 'Basic realm="NORTH Phase 2G Founder Review"')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Robots-Tag', 'noindex, nofollow, noarchive')
            self.end_headers()
            return
        parsed = urlsplit(self.path)
        mapped = fallback_route(parsed.path.rstrip('/') or '/')
        if mapped:
            self.path = mapped + (f'?{parsed.query}' if parsed.query else '')
        return super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('X-Robots-Tag', 'noindex, nofollow, noarchive')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        super().end_headers()


ThreadingHTTPServer(('0.0.0.0', PORT), Handler).serve_forever()
