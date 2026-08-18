# NORTH Product Registry Schema — Phase 2A

> **Canonical implementation:** `assets/product-studio-config.js`
> **Audience:** Internal founder, production, reviewer, and future commerce operations only.

## Record schema

Each roadmap offer is represented by one stable record in the canonical Product Studio registry.

| Field | Purpose | Required for release control |
|---|---|---:|
| `id` | Stable internal identifier | Yes |
| `slug` | Stable URL/data key | Yes |
| `category`, `releaseFamily`, `title` | Editorial organisation | Yes |
| `outcome`, `audience`, `notFor` | Honest product position and boundary | Yes |
| `status` | `concept`, `in_production`, `review_required`, `approved_for_sale`, or `retired` | Yes |
| `proposedPrice`, `currency` | Internal planning information only | Yes, but never public unless fully eligible |
| `bundleMembership` | Exact bundle composition | Yes where applicable |
| `deliverables` | Required customer asset manifest | Yes |
| `sampleAvailability` | Draft versus approved sample state | Yes |
| `supportOwner`, `refundPolicyStatus`, `deliveryStatus`, `checkoutStatus` | Operational readiness | Yes |
| `compliance` | Money education, age, affiliate, licensed-content, and physical-fulfillment flags | Yes |
| `localeReadiness` | Page, checkout, delivery, asset, support, legal, and human-review state per verified app locale | Yes |
| `safePublicState`, `publicVisibility`, `releaseDate` | Controlled presentation state | Yes |
| `blockers`, `nextOwner` | Release-control accountability | Yes |

## Non-negotiable render invariant

`renderPolicy(productRecord)` calculates a product’s commercial eligibility. The renderer permits price, savings claim, purchase CTA, checkout, delivery promise, or app entitlement **only when every condition below is true**:

1. `status === 'approved_for_sale'`;
2. final asset manifest is complete;
3. original content is complete;
4. delivery is `ready`;
5. support is ready;
6. policy is ready;
7. compliance is complete;
8. a separate approved checkout/merchant phase exists; and
9. the founder has set public visibility to `true`.

No Phase 2A record satisfies that invariant. Therefore every product page renders a governed state, blockers, and a **Not available in this phase** control rather than a price, checkout, delivery, savings, or entitlement action.

## Locale invariant

English is the source locale. The canonical locale registry uses only the verified mobile-app list: English, Brazilian Portuguese, Latin-American Spanish, French, German, Italian, Japanese, Korean, Chinese (Simplified), Chinese (Traditional), Arabic, Russian, Polish, and Dutch. A locale cannot be called released for a product unless its real page, checkout, delivery, asset, support, and legal path have human review. Arabic adds RTL visual QA.

## Record population coverage

The registry contains one record for every offer named in the Phase 2A roadmap: all Release A, B, C, D, and later-only offers. Internal pricing is stored only for the three Release A offers and the specified Release B offers; it is never rendered in the private preview because no record is eligible for commercial presentation.
