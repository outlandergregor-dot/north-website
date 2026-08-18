# NORTH Phase 2C — Canonical Localization Readiness System

> **Status:** Governance and static-route readiness only. This document does not authorize any translated product, checkout, delivery, support, legal, or public language release.

## Canonical locale registry

| Locale | Navigation and layout route | Website language | Product-content language | Checkout language | Delivery language | Support language | Legal / policy language | Release position |
|---|---|---|---|---|---|---|---|---|
| English (`en`) | Complete source route | Complete English source | Founder-review English only; no customer product release | Not enabled | Not enabled | Not release-ready | Not release-ready | Source language |
| Portuguese (Brazil) (`pt-BR`) | Governed route with translated navigation | Pending human review | Not released | Not enabled | Not enabled | Not release-ready | Not release-ready | First human-review queue |
| Spanish (Latin America) (`es-419`) | Governed route with translated navigation | Pending human review | Not released | Not enabled | Not enabled | Not release-ready | Not release-ready | Second human-review queue |
| French (`fr`) | Governed route with translated navigation | Pending human review | Not released | Not enabled | Not enabled | Not release-ready | Not release-ready | Later queue |
| German (`de`) | Governed route with translated navigation | Pending human review | Not released | Not enabled | Not enabled | Not release-ready | Not release-ready | Later queue |
| Italian (`it`) | Governed route with translated navigation | Pending human review | Not released | Not enabled | Not enabled | Not release-ready | Not release-ready | Later queue |
| Japanese (`ja`) | Governed route with translated navigation | Pending human review | Not released | Not enabled | Not enabled | Not release-ready | Not release-ready | Later queue |
| Korean (`ko`) | Governed route with translated navigation | Pending human review | Not released | Not enabled | Not enabled | Not release-ready | Not release-ready | Later queue |
| Chinese, Simplified (`zh-Hans`) | Governed route with translated navigation | Pending human review | Not released | Not enabled | Not enabled | Not release-ready | Not release-ready | Later queue |
| Chinese, Traditional (`zh-Hant`) | Governed route with translated navigation | Pending human review | Not released | Not enabled | Not enabled | Not release-ready | Not release-ready | Later queue |
| Arabic (`ar`) | Governed RTL route; Phase 2C RTL layout QA completed | Pending human review | Not released | Not enabled | Not enabled | Not release-ready | Not release-ready | Later queue; requires repeat RTL QA on final content |
| Russian (`ru`) | Governed route with translated navigation | Pending human review | Not released | Not enabled | Not enabled | Not release-ready | Not release-ready | Later queue |
| Polish (`pl`) | Governed route with translated navigation | Pending human review | Not released | Not enabled | Not enabled | Not release-ready | Not release-ready | Later queue |
| Dutch (`nl`) | Governed route with translated navigation | Pending human review | Not released | Not enabled | Not enabled | Not release-ready | Not release-ready | Later queue |

## Release invariant

A locale is **not product-available** unless all six layers are released for that product and locale: website language, product-content language, checkout language, delivery language, support language, and legal / policy language. This invariant applies even where a static locale route exists or navigation labels have been translated.

> **No machine translation becomes final paid-product content.** Translation routes are a governed review surface. Final public product language requires human translation, human review, founder approval, and the required delivery, support, and legal/policy preparation.

## Controlled sequence

Portuguese (Brazil) is first in the future human-review queue, followed by Spanish (Latin America). Each subsequent mobile-app locale is reviewed one at a time. Arabic requires a separate final RTL visual and interaction QA pass after its real human-reviewed website and product content exists.

## Static candidate behavior

Every non-English route has a visible native-language notice explaining that it is prepared for human review and that complete website and product content remains English until release. Navigation labels and layout direction are localized. Product overviews expose the six readiness fields and have no price, checkout, download, delivery, waitlist, or customer-product source.
