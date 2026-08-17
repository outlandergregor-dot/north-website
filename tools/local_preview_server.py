#!/usr/bin/env python3
"""Temporary local static preview server for visual QA; not a production service."""
from __future__ import annotations

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
import os

ROOT = Path(__file__).resolve().parents[1]
ROUTES = {
    "/library": "/library.html",
    "/library/free-tools": "/library-free-tools.html",
    "/library/resources": "/library-resources.html",
    "/library/programs": "/library-programs.html",
    "/library/books": "/library-books.html",
    "/library/item": "/library-item.html",
}


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        destination = ROUTES.get(parsed.path)
        if destination:
            self.path = destination + (f"?{parsed.query}" if parsed.query else "")
        return super().do_GET()

    def log_message(self, fmt: str, *args: object) -> None:
        print(fmt % args)


if __name__ == "__main__":
    os.chdir(ROOT)
    server = ThreadingHTTPServer(("0.0.0.0", 4173), Handler)
    print("Preview server listening on http://0.0.0.0:4173")
    server.serve_forever()
