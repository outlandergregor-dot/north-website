# NORTH Web Phase 2G — Product Truth, Buyer Proof, and Premium Visual Control

**Branch:** `north-web-phase2g-product-truth`
**Baseline:** `0153eef8080034c4ec5d68c8cbc87d9ef37f2704` from the approved Phase 2F product-presentation pilot
**Release state:** Private founder review only
**Deployment / commerce state:** No deployment, hosting change, checkout, payment, delivery, email capture, tracking, affiliate, social integration, or public price activation.

> **Phase 2G outcome:** NORTH now has a private flagship buyer-proof experience rooted in the actual Planner source and PDFs. Generated or physical-looking visuals no longer function as product proof. The 1-3-5 Execution Planner remains an English private founder-review candidate, not a sale-ready offer.

## Acceptance Summary

| Requirement | Result | Evidence |
|---|---|---|
| New isolated branch from Phase 2F baseline | **Pass** | `north-web-phase2g-product-truth`; baseline recorded in `docs/NORTH_PHASE2G_SOURCE_AUDIT.md` |
| Source/product/asset/claim/route/locale audit before implementation | **Pass** | `docs/NORTH_PHASE2G_SOURCE_AUDIT.md`; `evidence/phase2g-visual-audit-notes.md` |
| Product status and launch gates with required four columns | **Pass** | `docs/NORTH_PRODUCT_STATUS_AND_LAUNCH_GATES.md` |
| Source-of-truth asset and claim register | **Pass** | `docs/NORTH_ASSET_AND_CLAIM_REGISTER.md` |
| Flagship buyer proof based on real Planner files | **Pass** | Five direct PDF exports in `assets/product-proof/`; four used as main proof sequence |
| Digital-versus-physical truthfulness | **Pass** | Private page states digital-PDF-only status; one editorial image has persistent illustrative disclosure |
| No physical-looking mockup as primary proof | **Pass** | Old `assets/product-visuals/*.png` paths removed from private proof renderer and quarantined in register |
| Premium shared visual system | **Pass** | `docs/NORTH_PREMIUM_VISUAL_SYSTEM.md`; navy/ivory/gold/compass, editorial hierarchy, motion/mobile rules |
| 14-locale / Arabic RTL governance | **Pass** | `docs/NORTH_PRODUCT_LOCALIZATION_RELEASE_PLAN.md`; runtime canonical/hreflang/RTL checks |
| Future commerce readiness, planning only | **Pass** | `docs/NORTH_FUTURE_COMMERCE_READINESS_PLAN.md` |
| Static acceptance suite | **Pass — 28/28** | `evidence/phase2g-verification-output.json` |
| Desktop, tablet, 390px mobile QA | **Pass with one tooling note** | Screenshots and `evidence/phase2g-desktop-private-preview-notes.md`; `evidence/phase2g-mobile-qa.md` |
| Keyboard, focus, labels, reduced motion | **Pass** | Mobile focus test; public route DOM audit; CSS/static acceptance checks |
| Performance/image-size audit | **Pass for private-review budget** | `evidence/phase2g-performance-audit.md` |
| No commerce, deployment, customer-data, or tracking activation | **Pass** | Source config, static verifier, and private-preview header audit |

## Flagship Buyer-Proof Correction

The prior private product page used two physical hardcover-style visuals under the heading “actual Planner-page detail.” The Phase 2G audit rejected that treatment. The updated private page now follows this order:

1. The actual US Letter daily-page export appears in the hero.
2. “What you receive” names only facts shown in approved Planner source files.
3. Four readable real source-page exports prove Start Here, Two-Week Intention, a daily page, and final review/continuation.
4. The A4 source export proves that a private A4 print-review file exists.
5. The private page states that current proof PDFs are untagged and contain no PDF form fields.
6. A single secondary editorial image remains only after the real proof, labeled **“Illustrative digital product mockup — not a physical product photograph.”**

This provides a premium presentation without implying a hardcover shipment, desk kit, buyer outcome, fillable file, accessibility completion, delivery, or sales availability.

## QA Evidence

| Evidence item | Result |
|---|---|
| Desktop flagship private-proof screenshot | `evidence/screenshots/desktop-private-proof-hero.webp` |
| Mobile flagship private-proof screenshot | `evidence/screenshots/mobile-private-proof-390x844.png` |
| Tablet flagship private-proof screenshot | `evidence/screenshots/tablet-private-proof-768x1024.png` |
| 390px browser metrics | 390px page width, no horizontal overflow, 4 real proof cards, 5 actual-proof labels, 1 illustrative label, visible 3px focus outline, reduced-motion media active |
| Arabic route runtime metadata | `lang="ar"`, `dir="rtl"`, Arabic canonical, 14 locales plus `x-default` hreflang |
| English route runtime metadata | English canonical, labeled primary navigation, labeled selector, visible skip link, 14 locales plus `x-default` hreflang |
| Portuguese selector test | English Library selector moved to `/pt-BR/library` and displayed a human-review/English-source notice |
| Private preview protection | Authenticated `200` returns no-store/noindex/nosniff/no-referrer; unauthenticated request returns `401` with Basic Auth challenge |

## Closed Controls Confirmed

| Control | State |
|---|---|
| Merchant product / checkout URL / payment | Disabled / null |
| Customer delivery / download / order confirmation | Disabled / absent |
| Email capture / customer accounts | Absent |
| Public price | Absent from public candidate routes |
| Affiliate / social integrations / tracking endpoints | Absent from audited renderers |
| Namecheap / DNS / Vercel / production deployment | Untouched |
| Product translations | No product-language release; English source only |
| Financial products or advice | No sale/product release; money material remains general future-education architecture only |

## Open Blockers

1. Founder approval of final English buyer-visible files, proof sequencing, visual art direction, proposed bundle contents, and product offer decision.
2. Qualified legal review of license, support/refund, privacy, seller identity, consumer disclosures, and applicable jurisdictional obligations.
3. Final purchaser-file accessibility and print QA. Current proof PDFs are untagged and contain no PDF form fields.
4. Merchant-of-record, tax, payment, receipt, delivery, re-delivery, support, and incident-operation decisions.
5. Controlled end-to-end test after future systems are separately authorized and configured.
6. Human review of every non-English product edition before any locale can be called product-ready.

## Founder Decision List

1. **Approve, revise, or reject** the real PDF-proof-first flagship page.
2. **Approve, revise, or reject** one labeled editorial atmosphere image after the proof sequence.
3. **Confirm** that the proposed first offer remains English digital PDFs only, with editable source excluded from the buyer bundle.
4. **Choose** whether Phase 2H may prepare final buyer files and review packets without activating a merchant, price, checkout, or delivery.
5. **Confirm** that Portuguese (Brazil), Spanish (Latin America), and Arabic remain future human-review/RTL candidates only.
6. **Authorize or defer** legal, accessibility, and operations preparation. These preparations do not authorize commerce or a public release.

## Recommended Next Step

The exact narrow Phase 2H recommendation is in `docs/NORTH_PHASE2H_FOUNDER_RECOMMENDATION.md`. It is a **flagship approval and buyer-file finalization gate only**, not commerce activation or a public launch.

**Stop gate:** Written founder approval is required before Phase 2H or any merchant, payment, delivery, public-price, deployment, or localization-release work begins.
