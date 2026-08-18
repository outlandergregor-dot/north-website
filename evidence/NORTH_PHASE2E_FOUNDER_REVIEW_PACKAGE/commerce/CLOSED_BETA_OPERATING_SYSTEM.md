# NORTH Phase 2E — Closed-Beta Commerce Operating System

> **Architecture specification only. It enables no merchant, checkout, payment, public price, delivery, customer account, email capture, tracking, or customer download.**

## Target future flow

```text
NORTH product page
  → merchant-hosted checkout
  → merchant payment confirmation
  → verified signed payment event / webhook
  → purchase record and receipt
  → secure, versioned PDF delivery
  → support / refund handling
  → operational reporting
```

NORTH must not collect, transmit, or store payment-card data. A future merchant should host payment collection. NORTH must not create a delivery entitlement from a browser redirect or unverified client-side “success” state; delivery can occur only after a server-side or controlled back-office verification of a signed merchant payment event.

## Required data records

| Record | Minimum fields | Phase 2E state |
|---|---|---|
| Product | product ID, SKU, title, edition, version, locale, currency, price, sale-gate state | Schema defined; inactive |
| Delivery asset | file name, product/version, locale, checksum, format, access state, retired/replaced status | Schema defined; private release-candidate files only |
| Purchase | purchase ID, merchant transaction reference, product ID, state, currency, timestamps, refund state | Schema defined; no records collected |
| Consent | consent type, captured-at timestamp, notice version, channel, withdrawal state | Schema defined; no consent collected |
| Fulfillment | delivery status, delivery timestamp, re-delivery state, support case reference, failure reason | Schema defined; no fulfillment configured |
| Support / refund | request ID, category, state, timestamps, outcome, policy version | Schema defined; no support or refund system active |
| Merchant tax / receipt | merchant reference, receipt ID, tax responsibility metadata, invoice/receipt availability | Schema defined; no merchant configured |

## Product candidate record

```json
{
  "product_id": "north.execution-planner.core-digital.en",
  "sku": "NORTH-PLN-135-CORE-EN-001",
  "edition": "Core Digital Edition",
  "version": "1.0",
  "locale": "en",
  "proposed_price": {"amount": 19, "currency": "USD", "public": false},
  "sale_gate": "closed",
  "files": [
    {"name": "NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-US-Letter.pdf", "format": "PDF", "status": "private-release-candidate"},
    {"name": "NORTH_1-3-5_Execution_Planner_Core-Digital-v1.0_EN-A4.pdf", "format": "PDF", "status": "private-release-candidate"}
  ]
}
```

## Future confirmation and delivery control

1. Receive a merchant event only through an authenticated, signature-verified integration.
2. Verify event type, merchant transaction reference, paid state, product ID, price/currency, and idempotency before a purchase state change.
3. Create an immutable internal purchase record. No delivery link should be created from the browser alone.
4. Associate the delivery record with the exact approved file version and checksum.
5. Send or display a receipt and delivery path only through the chosen merchant/fulfillment system after operations testing.
6. Support re-delivery, refunds, disputes, and revocations through documented operational roles, not manual improvisation.
7. Log only the minimum data necessary to operate, support, and meet legal/policy obligations; define retention and deletion rules before activation.

## Future measurement plan — not enabled

| Event | Purpose | Minimum non-sensitive attributes | Pilot signal |
|---|---|---|---|
| `product_page_view` | Validate product-page clarity | product ID, locale, page version, anonymous session state if approved | Visitor comprehension only; no profile construction |
| `checkout_started` | Identify checkout friction | product ID, merchant checkout version, locale | Conversion path health |
| `purchase_succeeded` | Confirm reliable transaction record | product ID, transaction reference, currency, receipt state | Successful paid order count |
| `delivery_succeeded` | Confirm fulfillment | product version, delivery method, delivery status | Successful delivery rate |
| `support_requested` | Measure burden and confusion | category, product version, response state | Support rate and recurring issues |
| `refund_requested` / `refund_completed` | Monitor policy and product fit | reason category, policy version, outcome state | Refund rate and outcome time |
| `feedback_submitted` | Gather optional direct feedback | product version, explicit consent, selected questions | Qualitative clarity / usefulness signal |

No analytics pixel, profiling, tracking script, automated email, or event collector is enabled in Phase 2E. Any later measurement implementation requires separate privacy review, data-minimization design, and founder approval.

## Founder closed-beta report template

| Metric / review | Target interpretation | Owner | Phase 2E state |
|---|---|---|---|
| Successful verified payment-to-delivery path | Every test transaction produces the correct versioned file and receipt | Commerce operator | Not tested; no merchant |
| Delivery failures | Investigate every failed / duplicate / inaccessible delivery | Commerce operator | No deliveries |
| Support burden | Categorize questions before scaling; do not optimize for volume first | Support owner | No support channel live |
| Refund rate and reasons | Treat as a product/policy signal, not merely a loss metric | Founder + support owner | No sales/refunds |
| Direct feedback | Seek consented, specific feedback on clarity, format, print, and expectations | Founder | No collection enabled |
| Product / policy revisions | Version every change and test compatibility | Founder + product owner | Draft process only |

## Privacy, legal, and operating dependencies

| Dependency | Required before commerce activation |
|---|---|
| Legal / policy | Qualified review of license, refund/support path, privacy, consumer disclosures, seller entity and jurisdictional obligations |
| Merchant | Founder selection, account eligibility, documented terms review, product configuration, tax/receipt and payout confirmation |
| Security | Signed payment-event/webhook verification, secret handling, access control, delivery-link and re-delivery policy |
| Data | Data map, minimization, retention, deletion/access request process and operator roles |
| Operations | Named support/refund owner, escalation process, response expectation, incident / access-failure playbook |
| QA | Test product, receipt, delivery, re-delivery, refund, support and failure cases end to end |
| Localization | Human-reviewed content, product page, PDFs, print proofs, support/refund/policy copy for each language before that edition is offered |
