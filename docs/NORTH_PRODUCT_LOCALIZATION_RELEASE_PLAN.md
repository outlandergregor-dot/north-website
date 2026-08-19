# NORTH Product Localization Release Plan

**Phase:** 2G private founder review
**Global availability statement:** The 14-locale website architecture is maintained for interface, route, canonical, hreflang, and future-review readiness. It is **not** evidence that a product edition, buyer support, checkout, delivery, or legal copy is available in every language.

## Release Policy

1. **English is Phase A.** The current 1-3-5 Execution Planner is an English private founder-review candidate only.
2. **Portuguese (Brazil) and Spanish (Latin America) are next candidates.** Work cannot begin as an approved paid release until each product source, preview, checkout instruction, delivery path, support flow, and legal/policy copy receives human-quality review.
3. **Arabic is RTL-readiness only.** The route, selector state, canonical/hreflang plan, and visual QA are maintained, but Arabic product content is not available until professional language review and RTL product QA are complete.
4. **All other locales remain future queue.** A translated navigation label, locale route, or English fallback does not make a product localized.
5. **No raw machine translation is accepted as final paid-product content.** Human review is required for all six release layers: website, product content, checkout, delivery, support, and legal/policy.

## Availability Matrix

| Locale | Website route / navigation | Product-content availability | Checkout / delivery / support / legal availability | Release state | Required next work |
|---|---|---|---|---|---|
| English (`en`) | Complete source route | English private founder-review candidate only | All commercial layers inactive or draft-only | **Phase A source** | Founder approval; product/legal/accessibility/merchant/delivery gates |
| Portuguese (Brazil) (`pt-BR`) | Governed route; translated navigation pending human review | Not available | Not available | **Next candidate #1** | Human page/product/asset/checkout/delivery/support/legal review after English validation |
| Spanish (Latin America) (`es-419`) | Governed route; translated navigation pending human review | Not available | Not available | **Next candidate #2** | Human page/product/asset/checkout/delivery/support/legal review after Portuguese/English decision |
| French (`fr`) | Governed route | Not available | Not available | Future queue | Full six-layer localization path and human QA |
| German (`de`) | Governed route | Not available | Not available | Future queue | Full six-layer localization path and human QA |
| Italian (`it`) | Governed route | Not available | Not available | Future queue | Full six-layer localization path and human QA |
| Japanese (`ja`) | Governed route | Not available | Not available | Future queue | Full six-layer localization path and human QA |
| Korean (`ko`) | Governed route | Not available | Not available | Future queue | Full six-layer localization path and human QA |
| Chinese Simplified (`zh-Hans`) | Governed route | Not available | Not available | Future queue | Full six-layer localization path and human QA |
| Chinese Traditional (`zh-Hant`) | Governed route | Not available | Not available | Future queue | Full six-layer localization path and human QA |
| Arabic (`ar`) | Governed RTL route | RTL route only; no product edition | Not available | **RTL readiness only** | RTL page/product visual QA; professional translation and legal/support review |
| Russian (`ru`) | Governed route | Not available | Not available | Future queue | Full six-layer localization path and human QA |
| Polish (`pl`) | Governed route | Not available | Not available | Future queue | Full six-layer localization path and human QA |
| Dutch (`nl`) | Governed route | Not available | Not available | Future queue | Full six-layer localization path and human QA |

## Per-Product Locale Release Checklist

A product may not move from **not available** to **available** in a locale until each item is complete and recorded:

| Layer | Required evidence |
|---|---|
| Website language | Human-reviewed page copy, navigation, metadata, canonical/hreflang, alt text, accessibility labels, and locale-specific QA |
| Product-content language | Human-reviewed original product file, page numbering, proofreading, cultural/context review, and format QA |
| Checkout language | Approved merchant instructions, price/tax disclosure, payment flow, receipts, and customer-rights language |
| Delivery language | Localized access instructions, file naming, re-delivery procedure, and support escalation |
| Support language | Staffed support response path, support expectation, accessible contact method, and escalation procedure |
| Legal / policy language | Qualified legal review of localized license, refund, privacy, consumer rights, and relevant jurisdictional disclosure |

## Locale Selector Requirements

1. Keep all 14 verified mobile-app locale options available in the selector because they represent governed interface routes.
2. Every non-English selection must display an explicit notice that English remains the complete source/product language until human review and release.
3. The selector, route, canonical, and hreflang link must not use phrases such as “available worldwide in 14 languages,” “translated product,” “download in your language,” or similar availability claims.
4. Arabic must set `lang="ar"` and `dir="rtl"`, preserve keyboard order, and pass visual/mobile QA before it can be described as RTL-ready.
5. Product cards, product overviews, and private buyer-proof pages must keep the product language state separate from website interface state.

## Evidence and Ownership

| Control | Owner before any localized sale |
|---|---|
| Source product approval | Founder |
| Translation and human quality review | Qualified native-language reviewer |
| RTL review where relevant | Product designer + qualified reviewer |
| Legal/policy local review | Qualified legal reviewer |
| Merchant, delivery, support configuration | Product operations |
| Release decision | Founder in writing |

**Phase 2G decision:** No locale product release is approved. This plan preserves readiness without representing availability.
