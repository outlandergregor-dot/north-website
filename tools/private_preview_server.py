#!/usr/bin/env python3
"""Temporary password-protected local preview server for founder review only; not production hosting."""
from __future__ import annotations

import base64
import hmac
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
USERNAME = os.environ.get('NORTH_PREVIEW_USER', 'northfounder')
PASSWORD = os.environ.get('NORTH_PREVIEW_PASSWORD')
if not PASSWORD:
    raise SystemExit('NORTH_PREVIEW_PASSWORD must be set')
ROUTES = {
    '/library': '/library.html',
    '/library/free-tools': '/library-free-tools.html',
    '/library/resources': '/library-resources.html',
    '/library/programs': '/library-programs.html',
    '/library/books': '/library-books.html',
    '/library/item': '/library-item.html',
}

class Handler(SimpleHTTPRequestHandler):
    def _authorized(self) -> bool:
        header = self.headers.get('Authorization', '')
        expected = 'Basic ' + base64.b64encode(f'{USERNAME}:{PASSWORD}'.encode()).decode()
        return hmac.compare_digest(header, expected)

    def _challenge(self) -> None:
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="NORTH Phase 2A Private Preview"')
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()

    def do_GET(self) -> None:  # noqa: N802
        if not self._authorized():
            self._challenge()
            return
        parsed = urlparse(self.path)
        destination = ROUTES.get(parsed.path)
        if destination:
            self.path = destination + (f'?{parsed.query}' if parsed.query else '')
        return super().do_GET()

    def end_headers(self) -> None:
        self.send_header('X-Robots-Tag', 'noindex, nofollow, noarchive')
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def log_message(self, fmt: str, *args: object) -> None:
        print(fmt % args)

if __name__ == '__main__':
    os.chdir(ROOT)
    print('Private preview listening on http://0.0.0.0:4174')
    ThreadingHTTPServer(('0.0.0.0', 4174), Handler).serve_forever()
