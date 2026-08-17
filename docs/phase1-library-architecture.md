# NORTH Library — Phase 1 Architecture

**Status:** Approved for implementation under the NORTH Master Web Funnel & Product Monetization Brief.  
**Launch language:** English only.  
**Commerce state:** No live web checkout, no payment processor, no affiliate/resale links, no subscriptions, and no new mobile-app capability.

## Architecture principle

The NORTH Library is a calm editorial extension of the app, not a generic storefront. The homepage keeps its primary job—driving a verified app download. The Library gives visitors one practical next step, lets them use free browser-local tools, and clearly separates what is available now from work that is not yet ready.

All product availability, launch language, delivery readiness, pricing visibility, disclosures, and analytics-event names will come from `assets/north-config.js`. Page templates will never hardcode a Buy button or price. A CTA can be purchase-oriented only when `completedAsset`, `deliveryReady`, `supportReady`, `refundPolicyReady`, and `merchantOfRecordReady` are all true. Phase 1 sets every paid item to `coming_soon`, so no paid offer can render a price or checkout CTA.

## Route map

| Public route | Static implementation | Phase 1 role |
|---|---|---|
| `/library` | `library.html` | Curated English index for Free Tools, Resources, Programs, and Books & Audio. |
| `/library/free-tools` | `library-free-tools.html` | Browser-local North Snapshot, 1-3-5 Daily Page, Weekly Compass Preview, and Safe Number Starter Sheet. |
| `/library/resources` | `library-resources.html` | Resource catalog with one free planner path and non-purchasable future cards. |
| `/library/programs` | `library-programs.html` | Programs catalog; 7-Day Focus Recovery is clearly coming soon. |
| `/library/books` | `library-books.html` | Waitlist-free coming-soon catalogue. No price, form, preorder, or checkout. |
| `/library/item` | `library-item.html?product=<slug>` | Reusable product-page template for allowed Phase 1 detail pages. |

The Vercel rewrite configuration will translate clean URLs into these static files. `/north-picks` is intentionally absent from Phase 1.

## Canonical language registry

| Field | Value |
|---|---|
| Public web language in Phase 1 | `en` / English |
| Product delivery languages in Phase 1 | English only |
| Non-English web rendering | Not published |
| Arabic / RTL release | Not published; requires human-quality localization and RTL visual review |
| App language data | Stored as internal availability metadata only; never rendered as an available Library/product translation |

No Library page, product page, delivery claim, or purchase state may claim 14-language availability. The website will remove unverified language badges, alternate-language URLs, language strips, and 14-language marketing claims from the homepage and support/legal surfaces covered by the preflight.

## Phase 1 catalog state

| Product | Type | Status | Route / detail page | Available action | Reason |
|---|---|---|---|---|---|
| Find Your North Snapshot | Free tool | `available` | `/library/free-tools` and `/library/item?product=find-your-north-snapshot` | Start in browser | Completed as a browser-local guided snapshot. |
| 1-3-5 Daily Page | Free tool | `available` | `/library/free-tools` and `/library/item?product=1-3-5-daily-page` | Use and print locally | Completed as a browser-local planning page. |
| Weekly Compass Preview | Free tool | `available` | `/library/free-tools` | Use and print locally | Completed as a browser-local reflection tool. |
| Safe Number Starter Sheet | Free tool | `available` | `/library/free-tools` | Use and print locally | General organization only; no advice, promise, or data transmission. |
| 1-3-5 Execution Planner | Resource | `coming_soon` | `/library/item?product=1-3-5-execution-planner` | View scope only | Final asset and delivery are absent from the repository. |
| Decision Clarity Toolkit | Resource | `coming_soon` | `/library/resources` | None | Not a Phase 1 completed asset. |
| Financial Clarity Kit | Resource | `not_releasing` | Not linked | None | Requires professional/legal review; outside Phase 1 launch. |
| Weekly Compass Journal | Resource | `coming_soon` | `/library/resources` | None | Not a Phase 1 completed asset. |
| 7-Day Focus Recovery | Program | `coming_soon` | `/library/item?product=7-day-focus-recovery` | View scope only | Final curriculum/assets and delivery are absent from the repository. |
| NORTH 90-Day Direction Sprint | Program | `coming_soon` | `/library/programs` | None | Not a Phase 1 completed asset. |
| Money programs | Program | `not_releasing` | Not linked | None | Professional/legal/privacy review required; excluded by brief. |
| Find Your North | Book / audio | `coming_soon` | `/library/books` | None | Waitlist/checkout excluded from Phase 1. |

## Reusable product-page template contract

The `library-item.html` template must resolve its content entirely from the canonical registry and render these content blocks in the listed order:

| Template block | Requirement |
|---|---|
| Outcome-led hero | States the practical result without promising a personal outcome. |
| Audience and exclusions | Includes a clear **For** and **Not for** statement. |
| Exact contents | Names each file, exercise, browser interaction, or access term. |
| Time and access | Gives expected effort and device/access conditions. |
| Preview | Provides an honest in-page sample or direct tool preview. |
| Availability CTA | Offers `Start`, `Use`, or `Print` only for available free tools; shows non-actionable coming-soon copy for incomplete paid offers. |
| Financial-scope note | Shown when `moneyEducation` is true; states general education and organization only, not financial advice. |
| FAQ | Covers delivery/access, refund applicability, and support without inventing commercial policies. |
| Optional app CTA | Appears beneath the product experience and only links to the verified App Store page. |

All controls must have a visible keyboard focus state, a 44px minimum tap target, semantic labels, readable contrast, and no carousel/interaction that depends on a pointer device.

## Free-tool interaction design

| Tool | Inputs | Result | Privacy rule | Recommended next step |
|---|---|---|---|---|
| Find Your North Snapshot | One priority-area choice and one optional reflection | A private next-step prompt and route to a relevant free tool/app page | Inputs stay in memory in the current browser session; no server request or analytics payload carries text. | The matching free tool or verified App Store link. |
| 1-3-5 Daily Page | One Big Thing, three medium tasks, five quick wins | A printable one-page daily plan | Inputs remain in the browser; printing is user initiated. | App Store link after the plan. |
| Weekly Compass Preview | Structured reflection prompts | A printable weekly reflection | Inputs remain in the browser; no reflection content enters analytics. | App Store link after reflection. |
| Safe Number Starter Sheet | Essential-expense labels and optional values | A private organization sheet and a plain-language scope note | No calculation promises; all entries remain browser-local and are not collected. | Financial Clarity Kit is not promoted in Phase 1; the app CTA remains optional. |

## Privacy-aware event map

The existing Google Analytics implementation will use one small `northTrack` wrapper. It sends only event names and approved non-sensitive metadata. It does **not** send text input, task content, reflection content, expense values, Safe Number figures, email addresses, device identifiers, or any answers that could be sensitive.

| Event name | Trigger | Allowed properties | Explicitly excluded |
|---|---|---|---|
| `library_view` | A Library page loads | `route`, `category`, `language` | User content, financial data |
| `library_category_select` | A category card/link is selected | `category`, `route` | User content |
| `free_tool_start` | A free tool begins | `tool_slug`, `route` | Tool answers/text |
| `free_tool_complete` | A free tool reaches result/print state | `tool_slug`, `route` | Tool answers/text, values |
| `free_tool_recommendation` | Snapshot result presents a path | `tool_slug`, `recommendation_slug` | User selection text |
| `product_page_view` | An item template loads | `product_slug`, `availability` | User content |
| `product_interest` | A coming-soon card is opened | `product_slug`, `availability` | Email, waitlist data |
| `app_store_click` | Verified App Store link is selected | `source`, `route` | User content |

Events for checkout start, purchase, refund, course start/completion, affiliate click, referral revenue, and product-to-app conversion are registered in the analytics schema as **disabled** until a future approved phase supplies a merchant of record, completed asset, delivery, support, and privacy-safe implementation.

## Homepage and public-trust changes

The homepage will receive one compact section immediately after “How It Works” titled **Take NORTH Beyond the App**. It will use the brief’s four exact card categories and link to `/library`; it will not display products, pricing, product grids, testimonials, discounts, or purchase CTAs. The app download CTA remains primary in the hero, navigation, and mobile sticky CTA.

The same implementation removes the preflight’s unsupported app-rating/testimonial section, all non-verified Google Play links, stale pricing/trial claims, unverified language claims, misleading newsletter capture behavior, and unsupported “perfect day”/financial-freedom promises from the homepage and support/legal surfaces being corrected in this phase.

## Out-of-scope enforcement

No route or registry item will expose: a checkout URL, Buy label, price for an unavailable item, waitlist form, affiliate link, book sale, subscription, app-billing bypass, personal financial advice, referral program, or user-data collection beyond the existing anonymous analytics event wrapper.
