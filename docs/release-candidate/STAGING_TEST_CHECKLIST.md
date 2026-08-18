# NORTH Phase 2C — Staging Test Checklist

> Use only after founder-authorized staging on a temporary subdomain. This checklist is not production approval.

## Route and refresh checks

| Route family | Expected result |
|---|---|
| `/`, `/library`, `/library/resources`, `/library/programs`, `/library/books`, `/library/money-education`, `/about` | HTTP success, premium public shell, App Store/Free Tools only as active public actions |
| `/library/free-tools` | Four browser-local tools load; Snapshot, clear/reset, total calculation, and print controls function without transmitting entered content |
| `/library/item?product=1-3-5-execution-planner` and the other two Release A slugs | Public-safe overview; **In founder review** state; six language readiness fields; no price, checkout, download, delivery, preorder, waitlist, or private link |
| `/pt-BR/`, `/es-419/`, `/ar/` | Governed locale route with translated navigation, visible human-review notice, and no claim of product-language release |
| `/ar/` | Right-to-left header, notice, hero, cards, and mobile layout have no clipping or reversed action order |
| Every listed route | Direct visit and page refresh remain on the intended route under `.htaccess` rules |

## Product and claims checks

The four Free Tools are the only browser-first public actions. The verified App Store destination is the only external product action. The candidate must not show prices, carts, checkout, payment buttons, purchase language, delivery promises, subscriptions, bundles, discounts, refunds, waitlists, email forms, affiliate disclosures or links, book listings, course enrollment, or private founder-review materials.

## Locale governance checks

Check that the selector contains exactly 14 verified mobile-app locales: English, Portuguese (Brazil), Spanish (Latin America), French, German, Italian, Japanese, Korean, Chinese (Simplified), Chinese (Traditional), Arabic, Russian, Polish, and Dutch. English is the complete source language. Portuguese (Brazil) and Spanish (Latin America) are the first future human-review queue; no non-English product language is declared available.

## Accessibility and responsive checks

At 390px and desktop width, verify visible keyboard focus, readable selector labels, no page-level horizontal overflow, usable menu controls, adequate contrast, correct heading order, and a clear focus return path. At a browser-equivalent 200% zoom, verify that header controls, Release A readiness fields, and Arabic RTL content reflow without hidden controls.

## Candidate indexing safeguard checks

While staging, `robots.txt` must disallow all crawlers and `.htaccess` must retain the `X-Robots-Tag: noindex, nofollow, noarchive` header where the host supports `mod_headers`. These files must remain until a future written public-launch authorization.
