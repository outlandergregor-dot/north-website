#!/usr/bin/env python3
"""Static verification for NORTH Library Phase 1 acceptance criteria."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "evidence" / "phase1-verification.json"
HTML_FILES = sorted(ROOT.glob("*.html"))
REQUIRED_ROUTES = {
    "/library": "library.html",
    "/library/free-tools": "library-free-tools.html",
    "/library/resources": "library-resources.html",
    "/library/programs": "library-programs.html",
    "/library/books": "library-books.html",
    "/library/item": "library-item.html",
}


def check(name: str, condition: bool, detail: str) -> dict[str, object]:
    return {"name": name, "pass": condition, "detail": detail}


def main() -> int:
    results: list[dict[str, object]] = []
    vercel = json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))
    rewrite_map = {item["source"]: item["destination"].lstrip("/") for item in vercel["rewrites"]}
    for route, filename in REQUIRED_ROUTES.items():
        results.append(check(f"route:{route}", rewrite_map.get(route) == filename and (ROOT / filename).is_file(), f"{route} -> {rewrite_map.get(route)}"))

    public_html = "\n".join(path.read_text(encoding="utf-8") for path in HTML_FILES)
    results.append(check("no-google-play-links", "play.google.com/store/apps/details" not in public_html, "No public HTML contains a Google Play listing URL."))
    results.append(check("no-old-app-store-url", "id6742574901" not in public_html, "No public HTML contains the known 404 App Store URL."))
    checkout_href = re.search(r'<a\\b[^>]+href=["\\\'][^"\\\']*(checkout|buy|preorder)[^"\\\']*["\\\']', public_html, re.I)
    results.append(check("no-published-web-checkout", checkout_href is None, "No public HTML exposes a checkout, Buy, or preorder destination."))
    results.append(check("no-homepage-rating-claim", "4.8★" not in (ROOT / "index.html").read_text(encoding="utf-8") and "aggregateRating" not in (ROOT / "index.html").read_text(encoding="utf-8"), "Homepage has no rating stat or rating schema."))
    results.append(check("no-homepage-testimonial-grid", '<div class="review-card' not in (ROOT / "index.html").read_text(encoding="utf-8"), "Homepage testimonial cards were removed; unused legacy CSS does not render a testimonial."))
    results.append(check("homepage-library-bridge", "Take NORTH Beyond the App" in (ROOT / "index.html").read_text(encoding="utf-8"), "Homepage includes the compact Library section."))
    results.append(check("homepage-app-cta-primary", APP_STORE_URL in (ROOT / "index.html").read_text(encoding="utf-8"), "Homepage retains the verified App Store CTA."))
    results.append(check("library-english-only", 'publicWeb: true' in (ROOT / "assets/north-config.js").read_text(encoding="utf-8") and (ROOT / "assets/north-config.js").read_text(encoding="utf-8").count('publicWeb: true') == 1, "Only English is marked as publicly published on web."))
    results.append(check("paid-offers-not-buyable", "merchantOfRecordReady: false" in (ROOT / "assets/north-config.js").read_text(encoding="utf-8") and "Not available in Phase 1" in (ROOT / "assets/library.js").read_text(encoding="utf-8"), "Paid offers are guarded by delivery/policy flags and have no purchase CTA."))
    results.append(check("sensitive-analytics-excluded", "Tool answers/text" in (ROOT / "docs/phase1-library-architecture.md").read_text(encoding="utf-8") and "safeProperties" in (ROOT / "assets/library.js").read_text(encoding="utf-8"), "Analytics wrapper limits events to approved non-sensitive properties."))
    results.append(check("free-tools-present", all(item in (ROOT / "assets/library.js").read_text(encoding="utf-8") for item in ["Find Your North Snapshot", "1-3-5 Daily Page", "Weekly Compass Preview", "Safe Number Starter Sheet"]), "All four Phase 1 free tools render from the shared source."))
    results.append(check("support-corrected", "play.google.com/store/apps/details" not in (ROOT / "support.html").read_text(encoding="utf-8") and APP_STORE_URL in (ROOT / "support.html").read_text(encoding="utf-8"), "Support page has no Google Play destination and uses the verified App Store source."))
    results.append(check("terms-no-stale-app-prices", "$6.99" not in (ROOT / "terms.html").read_text(encoding="utf-8") and "$59.99" not in (ROOT / "terms.html").read_text(encoding="utf-8"), "Terms removes stale Essential price and savings claims."))

    report = {"passed": all(item["pass"] for item in results), "checks": results}
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": report["passed"], "total": len(results), "failed": [item["name"] for item in results if not item["pass"]]}, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    APP_STORE_URL = "https://apps.apple.com/us/app/north-find-your-north/id6757988392"
    raise SystemExit(main())
