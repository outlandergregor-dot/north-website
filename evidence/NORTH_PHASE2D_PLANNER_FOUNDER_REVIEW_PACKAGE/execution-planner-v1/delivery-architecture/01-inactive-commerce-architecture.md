# NORTH 1-3-5 Execution Planner — Inactive Commerce Architecture v1.0

> **Founder review only — no merchant, payment, checkout, confirmation, customer account, email, or delivery system is active.**

## Design objective

The future commerce path must preserve the NORTH website as the single storefront and product ecosystem. It must not create a detached product site, opaque reseller page, or a checkout that claims language, support, delivery, refund, or accessibility features that are not ready.

## Future journey, not an active flow

| Future stage | Required future behavior | Current Phase 2D state |
|---|---|---|
| NORTH Library overview | Presents a truthful product status, exact included files, language readiness, customer policy summary, and price only after approval | Product remains founder review; no price shown publicly |
| Product page | Shows final approved English content, previews, accessibility format details, license, refund terms, support contact, and disclosure | Private founder-review page only |
| Merchant checkout | Uses one approved merchant-of-record with payment, tax, consumer-rights, privacy, fraud, and jurisdictional configuration | No merchant selected or connected |
| Order confirmation | Confirms the buyer, order reference, version, purchased files, support channel, and delivery process | Designed only; no confirmation message or email exists |
| Secure delivery | Gives only the verified purchaser authorized access to final files, with documented re-delivery and expiry rules | No delivery service, customer record, or link exists |
| Support and refund | Routes verified order questions to an approved support owner and applies approved policy / mandatory consumer rights | Draft policy only; no live support operation |

## Commerce control model

The canonical registry must continue to enforce the following fields before any purchasing control can render:

```text
status = approved_for_sale
saleGateLocked = false
commercePilot.enabled = true
commercePilot.merchantProductId = configured
commercePilot.checkoutUrl = approved secure URL
checkoutStatus = approved_separate_phase
deliveryStatus = ready
assetManifestComplete = true
contentComplete = true
supportReady = true
policyReady = true
complianceComplete = true
publicVisibility = true
explicitFounderCommerceApproval = recorded
```

If any field is absent, false, unapproved, stale, or contradictory, the website must show the safe non-commercial state and never render price, payment, order, download, access, delivery, or entitlement behavior.

## Required pre-activation sequence

1. Founder approves the exact product master, cover, previews, file bundle, option, and intended audience.
2. A qualified attorney reviews the contracting entity, license, refund language, consumer-rights disclosures, privacy, tax / jurisdiction statements, and customer communications.
3. The founder chooses the merchant platform and merchant-of-record model. The platform must support the required payment, tax, refund, privacy, customer-access, and digital-delivery policies.
4. The product is configured in a non-public merchant test mode with the approved price, product description, policy links, permitted territories, and file bundle.
5. A full test order verifies payment, tax / receipt behavior, confirmation, buyer identity association, delivery, re-delivery, refund path, and support escalation. No live buyer is used before the founder authorizes a controlled pilot.
6. The live product page is updated only after every declared customer-facing layer is real, human-reviewed, and approved in the language offered.

## Explicit exclusions

This Phase 2D architecture does not activate Shopify, Gumroad, Stripe, PayPal, any payment system, any merchant product, any API key, any webhook, any checkout UI, any email capture, any transactional email, any customer download, any account entitlement, any affiliate system, or any public deployment. It is a reviewable operating design only.
