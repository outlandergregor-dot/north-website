# NORTH Web Phase 2G — Baseline Source Audit

**Branch:** `north-web-phase2g-product-truth`
**Baseline commit:** `0153eef8080034c4ec5d68c8cbc87d9ef37f2704`
**Scope:** Source-controlled audit completed before Phase 2G implementation.
**Public release status:** No deployment, payment, checkout, delivery, email capture, tracking, or public price activation is authorized.

> **Source-of-truth rule:** Source-controlled website code and approved original product files govern claims. Canva, Higgsfield, and similar outputs are presentation assets only. They are never proof of a physical product, included file, customer outcome, or sales readiness.

## Audit Scope and Findings

| Audit area | Source inspected | Current finding | Phase 2G control |
|---|---|---|---|
| Public/private route system | `assets/public-site.js`, static route wrappers, `internal/commerce-pilot.html` | Public route framework covers Homepage, Library, Resources, Programs, Books, Money Education, Free Tools, and public-safe product overviews. The private Planner review route is separately rendered. | Preserve route and 14-locale architecture; upgrade only the private candidate experience and public-safe information architecture. |
| Product registry | `assets/product-studio-config.js` | The Planner is `review_required` and sale-gated; Decision Clarity and Focus Recovery remain private review/in-production; all other families are non-selling roadmap concepts. | Add exact status/gate documents and remove any weaker wording. |
| Flagship buyer files | `internal/commerce-pilot/execution-planner-v1/**` | Real English editable master and private US Letter/A4 print-review PDFs exist. Current proof PDFs are **not tagged** and contain **no form fields**. US Letter has 31 pages; A4 has 27 pages. | Buyer-facing proof must be based on real PDF exports, but no claim of tagged, accessible, fillable, or customer-deliverable files is permitted. |
| Planner content | `01-execution-planner-customer-master.md` | The master documents Start Here, a two-week intention, fourteen daily pages, two weekly reset/review pages, final continuation guidance, and a fictional example. | Use only these proven contents in the buyer-proof sequence. |
| Planner presentation images | `assets/product-visuals/*.png` and `assets/product-presentation/web/*.webp` | Existing open-spread/detail images are physical hardcover-style renders; Phase 2F hero/gallery assets are explicitly illustrative generated atmosphere. | Quarantine physical-looking visuals from primary proof. If retained, use the persistent illustrative label. Replace primary proof with exported real PDF pages. |
| Locale system | `assets/locale-system.js`, `assets/public-site.js`, product registry | Fourteen mobile-app locales, `pt-BR` and `es-419` priority queue, Arabic route with RTL metadata, canonical/hreflang creation. English is the only complete source/product language. | Maintain structure; show availability truthfully and preserve Arabic RTL QA. |
| Closed commerce state | `assets/product-studio-config.js`, `assets/public-catalog.js`, `assets/commerce-pilot.js` | Merchant, checkout URL, payment, delivery, customer account, email capture, and customer download are absent/inactive. Private proposed-price references exist only in founder-review context. | Retain all gates; Phase 2G documents readiness only. |
| Accessibility/motion baseline | `assets/public-site.css`, Planner print proof | Skip link, visible focus styling, responsive rules, RTL direction rules, and reduced-motion rule exist. PDF tagging and assistive-tech proof remain open blockers. | Extend QA; do not claim PDF accessibility completion. |

## Source-Controlled Proof Files Selected for Flagship Review

| File | Proof use | Claim boundary |
|---|---|---|
| `NORTH_1-3-5_Execution_Planner_US-Letter_PRIVATE-REVIEW.pdf` page 5 | Start Here / under-ten-minutes method | Private founder-review proof only; not a customer download. |
| Same US Letter PDF, page 7 | Two-Week Intention page | Shows real field structure; does not prove fillable accessibility. |
| Same US Letter PDF, page 9 | Day 1 daily planning page | Shows One Big Thing, three tasks, five small wins, focus block, and real field layout. |
| Same US Letter PDF, page 28 | Final Two-Week Review and Continuation Plan | Shows final review and continuation field structure. |
| Same US Letter PDF, page 31 | Product-use/accessibility notes | QA evidence only; explicitly records remaining tagged-PDF, assistive-technology, and printer-proof blockers. |
| `NORTH_1-3-5_Execution_Planner_A4_PRIVATE-REVIEW.pdf` | A4 proof file exists with 27 pages | Print-preview evidence only; not an approved customer delivery file. |

## Corrective Decisions Required by the Addendum

1. The old `execution-planner-open-spread.png` and `execution-planner-detail.png` must no longer be described as **actual Planner-page detail**. They depict physical bound-book objects and will be quarantined as illustrative, or removed from primary proof.
2. The flagship product page will become a buyer-proof flow: **what it is → what is inside → how it is used in under ten minutes → real source-controlled page proof → actual print-proof evidence → boundaries → release blockers**.
3. The Planner will be described as a **private English founder-review candidate**. Its future proposed bundle is digital PDFs only; the editable source remains private and is not represented as a buyer entitlement.
4. No product, language, format, accessibility feature, or operational capability is called “ready” unless a real source file and completed release gate prove it.

## Audit Conclusion

The source baseline is strong enough to build a credible private proof experience, but it is not sales-ready. The highest-priority Phase 2G correction is to replace physical-looking Planner imagery as the main proof surface with legible exports from the actual private PDF evidence. The second is to consolidate product status, asset truth, claim approvals, and language availability into one explicit governance system.
