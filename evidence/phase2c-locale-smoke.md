# Phase 2C Locale Smoke Test — Interim Record

| Route | Result | Verified behavior |
|---|---|---|
| `/` | Pass | Premium public landing page renders. Public actions are limited to the verified App Store destination, Free Tools, Library navigation, and public-safe Release A overviews. Release A cards show **In founder review** and expose no price, checkout, download, delivery, preorder, waitlist, or private-draft path. |
| `/pt-BR/` | Pass | The physical governed Portuguese (Brazil) route renders; the selector labels Home, Library, Free Tools, and Language in Portuguese. A visible Portuguese notice states that human review is pending and that complete website/product content remains English until release. Content links retain the `/pt-BR/` route prefix. |

## Interim localization conclusion

The localization system correctly distinguishes **translated navigation and layout readiness** from **complete customer/product language availability**. Portuguese (Brazil) is present as the first governed human-review route; it is not represented as a released product-content, checkout, delivery, support, legal, or policy language.

## Follow-up QA still required

Arabic RTL route, selector routing, route refreshes, hreflang/canonical DOM tags, Free Tools locale route notice, high-zoom/mobile behavior, and strict public safety scan.

| `/ar/` | Pass | The Arabic route sets right-to-left document/layout direction. The header order, translated Arabic navigation labels, native-language selector label, Arabic review notice, hero alignment, and action layout were visually checked. The English source body remains visibly bounded by the Arabic human-review notice. |
| `/ar/library/free-tools` | Pass | The physical Arabic Free Tools route renders the verified English browser-local tools, a visible Arabic governed-language notice, a language selector, and an English-source link. No translated product availability, checkout, delivery, product-content, support, or legal-language release is claimed. |

## RTL follow-up conclusion

Arabic has **RTL layout readiness verified for this Phase 2C static candidate only**. Arabic is not a complete customer/product release language. A future Arabic release remains blocked until human review is complete for website copy, product content, checkout instructions, delivery, support, legal/policy language, and any required print/PDF materials.

## Public Release A overview DOM check

The Decision Clarity Toolkit public overview rendered with a canonical URL of `https://www.yournorth.app/library/item?product=decision-clarity-toolkit`, the 14 required locale alternates plus `x-default`, no commercial controls, and no private `internal/` or founder-review references. The six readiness labels are visually present. Browser DOM text normalizes the visually uppercase labels to uppercase, so the automated acceptance test records their normalized uppercase forms rather than mixed-case source text.

## Exported static candidate visual QA

| Candidate route | View | Result |
|---|---|---|
| `http://localhost:4182/` | Desktop | The exported package renders the premium homepage correctly with a clear dark editorial hero, App Store and Free Tools as the only active primary actions, available Free Tools, founder-review Release A cards, and clearly bounded future ecosystem areas. |
| `http://localhost:4182/ar/library/item?product=decision-clarity-toolkit` | Desktop RTL | The exported Arabic route maintains RTL header and page ordering, preserves the Arabic human-review notice, keeps English product source clearly visible as not released in Arabic, shows all six language-readiness fields, and presents no commercial, delivery, download, preorder, waitlist, or private-review action. |
