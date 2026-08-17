#!/usr/bin/env python3
"""Read-only external-link verifier for NORTH's public-trust preflight."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import json
import sys
import time
import urllib.request
import urllib.error

ROOT = Path(__file__).resolve().parents[1]
FILES = ["index.html", "support.html", "privacy.html", "terms.html"]
OUTPUT = ROOT / "evidence" / "link-audit.json"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.urls: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for name, value in attrs:
            if name == "href" and value and value.startswith(("http://", "https://")):
                self.urls.add(value)


def check(url: str) -> dict[str, object]:
    request = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": "Mozilla/5.0 (compatible; NORTH-Trust-Preflight/1.0)"},
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return {"url": url, "status": response.status, "final_url": response.url, "method": "HEAD"}
    except urllib.error.HTTPError as error:
        if error.code in {403, 405, 429}:
            get_request = urllib.request.Request(
                url,
                method="GET",
                headers={"User-Agent": "Mozilla/5.0 (compatible; NORTH-Trust-Preflight/1.0)"},
            )
            try:
                with urllib.request.urlopen(get_request, timeout=20) as response:
                    return {"url": url, "status": response.status, "final_url": response.url, "method": "GET"}
            except Exception as get_error:  # noqa: BLE001
                return {"url": url, "status": getattr(get_error, "code", None), "error": str(get_error), "method": "GET"}
        return {"url": url, "status": error.code, "error": str(error), "method": "HEAD"}
    except Exception as error:  # noqa: BLE001
        return {"url": url, "status": None, "error": str(error), "method": "HEAD"}


def main() -> int:
    urls: set[str] = set()
    for filename in FILES:
        parser = LinkParser()
        parser.feed((ROOT / filename).read_text(encoding="utf-8"))
        urls.update(parser.urls)

    results = []
    for url in sorted(urls):
        print(f"Checking {url}", file=sys.stderr)
        results.append(check(url))
        time.sleep(0.15)

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    failed = [result for result in results if not isinstance(result.get("status"), int) or int(result["status"]) >= 400]
    print(json.dumps({"checked": len(results), "failed": len(failed), "output": str(OUTPUT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
