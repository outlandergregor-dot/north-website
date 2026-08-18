#!/usr/bin/env python3
"""Temporary local static preview server for Phase 2C QA only; not production hosting."""
from __future__ import annotations

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
import os

ROOT = Path(__file__).resolve().parents[1]
LOCALES = {'en', 'pt-BR', 'es-419', 'fr', 'de', 'it', 'ja', 'ko', 'zh-Hans', 'zh-Hant', 'ar', 'ru', 'pl', 'nl'}
ROUTES = {
    '/': '/index.html', '/library': '/library.html', '/library/free-tools': '/library-free-tools.html',
    '/library/resources': '/library-resources.html', '/library/programs': '/library-programs.html',
    '/library/books': '/library-books.html', '/library/money-education': '/library-money-education.html',
    '/library/item': '/library-item.html', '/about': '/about.html'
}

def localized_destination(path: str) -> str | None:
    parts = [bit for bit in path.split('/') if bit]
    if not parts or parts[0] not in LOCALES or parts[0] == 'en':
        return None
    code, rest = parts[0], '/' + '/'.join(parts[1:])
    suffix = {
        '/': 'index.html', '/library': 'library/index.html', '/library/free-tools': 'library/free-tools/index.html',
        '/library/resources': 'library/resources/index.html', '/library/programs': 'library/programs/index.html',
        '/library/books': 'library/books/index.html', '/library/money-education': 'library/money-education/index.html',
        '/library/item': 'library/item/index.html', '/about': 'about/index.html'
    }.get(rest or '/')
    return f'/{code}/{suffix}' if suffix else None

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        destination = ROUTES.get(parsed.path) or localized_destination(parsed.path)
        if destination:
            self.path = destination + (f'?{parsed.query}' if parsed.query else '')
        return super().do_GET()

    def log_message(self, fmt: str, *args: object) -> None:
        print(fmt % args)

if __name__ == '__main__':
    os.chdir(ROOT)
    server = ThreadingHTTPServer(('0.0.0.0', 4173), Handler)
    print('Preview server listening on http://0.0.0.0:4173')
    server.serve_forever()
