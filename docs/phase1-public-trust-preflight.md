# NORTH Phase 1 — Public-Trust Preflight

**Status:** Completed before Phase 1 Library work.  
**Audit date:** 2026-08-17.  
**Scope:** The current NORTH homepage, support page, legal pages, app-store links, and the new Library/product surfaces required by the approved Phase 1 brief. This record does not authorize checkout, products that lack final delivery assets, affiliate links, financial products, or changes to the native app.

## Verified public facts used for corrections

| Fact | Verified source | Phase 1 decision |
|---|---|---|
| The live iOS listing is **NORTH - AI Life Planner**, version **1.1.2**, and currently displays **5.0 from 1 rating**. | [App Store listing][1] | Remove all version and rating-count claims from the website instead of publishing a rapidly stale rating claim. |
| The listing is marked **Only for iPhone** and its visible compatibility section names Apple platforms. | [App Store listing][1] | Keep the live website’s download CTA focused on the verified App Store listing. Remove Google Play CTAs until an active listing is verified. |
| The App Store describes the app in 14 languages, but its language metadata shows English; the existing website has conflicting 14-language lists. | [App Store listing][1] | The Phase 1 website and Library launch in **English only**. A single registry records other app-language entries as unpublished for web. Do not expose them as product-language availability. |
| The current iOS listing visibly offers Essential and Prime in-app purchases, while the old web prices conflict with the listing. | [App Store listing][1] | Remove all web subscription prices, saving claims, and web trial-duration promises. Reference the applicable app-store purchase screen for current app terms. |
| The current Google Play URLs embedded in the website return 404. | [Link-audit evidence][2] | Remove all Google Play CTAs and links. Do not substitute a guessed package URL. |
| The old Apple URL ending in `id6742574901` returns 404. | [Link-audit evidence][2] | Replace it with the verified iOS listing URL ending in `id6757988392`. |

## Issues found and Phase 1 correction record

| ID | Surface | Issue | Risk | Phase 1 correction |
|---|---|---|---|---|
| PT-01 | Homepage | It exposes a `4.8★` App Store rating and `1000` rating count in both visual and structured-data claims. | Invented or stale social proof. | Remove the rating section, rating stat, rating schema, and unverified testimonials. |
| PT-02 | Homepage, support, legal, SEO pages | Google Play links point to unavailable package IDs. | Broken platform CTA. | Remove every Google Play link; route all current app-download CTAs to the verified App Store URL. |
| PT-03 | Homepage, support, legal | The website claims iOS and Android availability although Google Play is not verified live. | Unverified platform-availability claim. | State only iPhone/App Store availability where a platform claim is needed. |
| PT-04 | Homepage, support, legal | Language claims conflict with each other and the public app listing. | Unsupported localization claim. | Launch website and Library in English only; centralize all language metadata in `assets/north-config.js`; do not display unpublished languages. |
| PT-05 | Homepage, support, terms | Trial length and subscription prices vary by page and conflict with visible App Store purchase information. | Material billing inconsistency. | Remove exact web price, savings, and trial claims. Use factual app-store billing/cancellation language only. |
| PT-06 | Homepage | `Captain AI plans your perfect day` and financial-freedom results appear in marketing copy. | Unsupported outcome promise. | Reframe as planning prompts, focus support, and money organization; make no outcome guarantee. |
| PT-07 | Homepage | Six named App Store testimonials lack evidence of verification and permission. | Invented testimonial risk. | Remove the testimonial grid. Do not replace it with new testimonials in Phase 1. |
| PT-08 | Support | The support page contains unverified tracks, driving mode, calendar, voice, price, refund-window, and Android claims. | Product/claims mismatch. | Replace with conservative, source-verified guidance and the verified App Store link; remove details that have no verified source. |
| PT-09 | Terms | The terms specify a 14-day trial, stale prices, savings claims, Android billing, and a 48-hour refund window. | Legal/billing inconsistency. | Remove stale commercial terms; explain that purchases are handled by the store and direct iOS refund requests to Apple. Terms should receive legal review before any web paid-product checkout. |
| PT-10 | Privacy | The page contains specific integrations, security standards, language counts, data practices, and response/retention commitments that were not verified as part of this web preflight. | Legal/privacy exposure. | Leave operational policy claims for a separate legal/privacy review; correct broken support link labels and prevent the Library from collecting reflection or financial contents. |
| PT-11 | Newsletter | The form only writes emails to browser local storage and presents a success state as though a subscription exists. | Misleading data collection and unsupported delivery claim. | Disable the capture form and replace it with an explicit unavailable/coming-soon notice until a consented provider and privacy flow are configured. |
| PT-12 | Library/product work | No completed asset or delivery system exists in the website repository for the $17 planner or $27 program. | False availability/checkout risk. | Model both paid offers as non-purchasable coming soon cards without price, checkout, urgency, or delivery promises. |

## Phase 1 safeguards to implement

The Phase 1 build will use `assets/north-config.js` as the single public content registry. It will store the language registry, product status, price visibility, delivery readiness, disclosure requirements, verified app link, and analytics-event names. The rendering layer must show a purchase CTA only when all delivery and policy fields are explicitly true. No Phase 1 paid item meets that condition.

The Library will launch in English only. Free tools will work entirely in the visitor’s browser; their sensitive reflection and money-organization inputs will not be sent to analytics or a server. Analytics will measure page and journey events only, such as tool start/completion and category selection.

> **Implementation boundary:** The preflight supports a Library that helps users organize and reflect. It does not permit financial advice, individual recommendations, checkout, subscriptions, course sales, resale, affiliate commerce, or new mobile-app features.

## Sources

[1]: https://apps.apple.com/us/app/north-find-your-north/id6757988392 "NORTH - AI Life Planner — App Store"
[2]: ../evidence/link-audit.json "NORTH public-link audit, 2026-08-17"
