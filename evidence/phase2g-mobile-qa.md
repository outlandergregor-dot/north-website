# Phase 2G Mobile QA — 390 × 844

**Route:** Authenticated private `/internal/commerce-pilot.html`
**Viewport:** 390 × 844
**Evidence:** `evidence/screenshots/mobile-private-proof-390x844.png`

| Check | Result | Evidence |
|---|---|---|
| Horizontal overflow | **Pass** | Browser automation reported `pageWidth: 390`, `viewportWidth: 390`, and `hasHorizontalOverflow: false`. |
| Buyer-proof content | **Pass** | Four real proof cards rendered; actual-proof label was present five times, including the hero proof. |
| Illustrative control | **Pass** | The required illustrative digital-product disclosure was present exactly once on the supporting editorial image. |
| Keyboard focus | **Pass** | Private navigation link received focus with a solid 3px outline. |
| Reduced motion | **Pass** | Browser media emulation reported `prefers-reduced-motion: reduce` as active; private CSS removes animation/transition behavior. |
| Header / nav readability | **Pass** | Founder-review banner, official compass mark, Library overview link, and Product Truth link stack cleanly above the hero. |
| Mobile hierarchy | **Pass** | The small-screen view shows status first, a readable Planner headline, private-only boundary, and the real PDF proof page—without a physical-product mockup leading the experience. |

**Authentication test note:** External-proxy Basic Auth was rejected by the browser-automation service despite working in the interactive private preview. The final local authenticated navigation alternative returned the expected Planner page title, proof card count, disclosure count, and screenshot. The browser service retained a stale `401` status field from the earlier external proxy state; content-level assertions and the saved mobile screenshot confirm the authenticated local page rendered successfully.

## Arabic RTL Route QA

| Check | Result | Finding |
|---|---|---|
| Arabic selector state and navigation labels | **Pass** | The Arabic route uses Arabic navigation labels and exposes the 14-language selector. |
| RTL layout direction | **Pass for route readiness** | The header, navigation order, language notice, hero alignment, and card grid render in right-to-left orientation without visible clipping or overlap in the 390px/desktop browser inspection. |
| Availability truth | **Pass** | The Arabic notice states that the full website and product content remains English until launch/review. The page makes no Arabic product, delivery, checkout, support, or legal availability promise. |
| English source content | **Expected unreleased state** | The main page copy remains English by design because Arabic is governed route/RTL readiness only, not an approved localized website or product edition. It is not an approved locale and must not be released without human content, product, policy, support, and legal review. |

**QA status:** Arabic is structurally RTL-ready for the current private candidate, while Arabic content availability remains **not released**.

## Tablet QA — 768 × 1024

| Check | Result | Evidence |
|---|---|---|
| Intermediate layout | **Pass** | `evidence/screenshots/tablet-private-proof-768x1024.png` shows the proof-page hero in a balanced two-column layout, with the real daily-page proof fully legible. |
| Header and founder-review boundary | **Pass** | The private-only banner, official mark, private navigation, and no-commerce language remain visible and unclipped. |
| Buyer-proof hierarchy | **Pass** | Real PDF proof remains the hero visual; the digital-only package boundary and content facts begin directly below it. |
| Horizontal clipping | **Pass by visual inspection** | No clipped nav, heading, proof card, or content panel is visible in the captured 768px rendering. |

**Automation limitation:** The separate browser-automation service intermittently lost Basic Auth after viewport changes. An independent local Chromium capture using the same authenticated private server completed the tablet rendering and provides the preserved visual evidence. No product or hosting environment was changed.

## Public Candidate Accessibility and Locale QA

| Check | Result | Evidence |
|---|---|---|
| Skip link | **Pass** | The English Library accessibility tree exposes `Skip to content` linked to `#main-content`. |
| Navigation label | **Pass** | The primary public navigation exposes `aria-label="Primary navigation"`. |
| Language selector label | **Pass** | The Library selector exposes `aria-label="Language"`; Arabic route exposes its Arabic equivalent. |
| Product/roadmap card status text | **Pass** | Resource, Programs, Books, and Money cards expose status words in visible text, not color alone. |
| English canonical / hreflang | **Pass** | English Library canonical is `https://www.yournorth.app/library`; 15 alternates are present: 14 locale codes plus `x-default`. |
| Arabic canonical / hreflang | **Pass** | Arabic Library canonical is `https://www.yournorth.app/ar/library`; 15 alternates are present and the document uses `lang="ar"` / `dir="rtl"`. |
| Cross-route selector behavior | **Pass** | Selecting Portuguese (Brazil) from English Library moved to `/pt-BR/library` and displayed the human-review/English-source notice. |
| False language availability | **Pass** | Portuguese route states the complete site and product content remains English until release; no translated product, checkout, delivery, support, or legal availability is claimed. |

The locale framework is therefore functionally intact for private candidate review. Non-English routes remain governed interface/translation-review routes, not product-language releases.
