# Neutral Merchant Comparison — Phase 2E Founder Decision

> **Research and architecture only. No provider is selected, connected, configured, or recommended for activation in Phase 2E.** This document is not legal, tax, or payment-processing advice. Verify current terms, eligibility, product rules, geography, fees, tax responsibilities, implementation behavior, and counsel advice before choosing any provider.

## Decision context

The immediate candidate is one English-only $19 digital PDF Planner. NORTH’s own website remains the long-term storefront and product ecosystem, while any eventual merchant should host checkout and use verified payment events before delivery. NORTH must not accept or store payment-card data.

| Criterion | Merchant-of-record marketplace pattern | Direct-store pattern |
|---|---|---|
| Seller of record and indirect-tax workflow | May shift defined transaction responsibilities to the merchant of record, subject to terms and eligibility. | Generally remains with the storefront merchant, who must configure applicable tax and operational controls. |
| Checkout and payment | Merchant-hosted checkout may reduce direct payment-card handling. | Platform checkout and payment integrations require configuration and testing. |
| Delivery and receipt | May provide a delivery/receipt layer subject to provider behavior and setup. | Requires a tested delivery app/workflow and receipt/customer communication design. |
| Brand and storefront control | Product can remain integrated into NORTH’s website but checkout and some buyer experience may be merchant-led. | More control over storefront and buyer flow, with more implementation and operating burden. |
| Tax, policies, and support | Responsibility allocation must be reviewed in current provider terms; it is not eliminated. | Requires internal tax/policy operations and professional review in relevant jurisdictions. |
| Future multi-language / multi-currency | Must be validated against current supported countries, languages, currencies, payment methods, and product rules. | Must be designed, configured, tested, and maintained by the merchant. |
| Pilot fit | Potentially lower operational surface for a single digital-PDF pilot, pending due diligence. | Potentially stronger long-term ecosystem fit, but higher early configuration and compliance burden. |

## Candidate classes for founder review

| Candidate | Publicly described model | Relevant strengths to validate | Constraints to validate before any selection |
|---|---|---|---|
| Gumroad | Its terms describe a reseller / merchant-of-record service for eligible digital products sold through its service. | Digital-product resale model, product delivery facilitation, invoicing/refund/chargeback support described in its terms, and optional affiliate program. | Current eligibility, territory support, seller obligations, pricing control, support process, buyer experience, product/content policy, export availability, data responsibilities, and affiliate rules. |
| Lemon Squeezy | Its documentation says it acts as merchant of record and describes payment, sales-tax, refunds, chargebacks, and PCI responsibilities. | Merchant-of-record posture, hosted checkout, receipts/order operations, and future multilingual/multi-currency suitability to validate. | Current seller-country and product eligibility, digital-PDF workflow, payout availability, payment methods by buyer region, refunds/support split, data export, API/webhook design, fees, and brand control. |
| Shopify + approved digital-delivery stack | Shopify documents digital-product tax configuration as a merchant storefront concern. | High storefront control and potentially deep NORTH-site integration for a later ecosystem. | Merchant tax obligations, digital-delivery application, secure file access, receipt/refund workflow, buyer data minimization, app costs, webhook verification, international tax setup, and operational support burden. |

## Official-source signals

Lemon Squeezy describes a merchant of record as the legal entity selling to the customer and says that role handles payments, sales tax, refunds, chargebacks, and PCI responsibility.[1] Gumroad’s terms describe a reseller / merchant-of-record structure for eligible digital products, including delivery facilitation and first-tier post-sale support for invoices, refunds, chargebacks, disputes, and payment reconciliation within its service.[2] Shopify’s digital-product tax documentation makes clear that jurisdiction-specific obligations can apply and directs merchants to local tax expertise for consequential tax treatment.[3]

> These source descriptions do **not** determine the right provider for NORTH. They establish why provider responsibility, actual geography, current terms, legal/policy obligations, and implementation testing must be reviewed before selection.

## Founder scorecard for a future non-public test

| Dimension | Weight | Required evidence before a decision |
|---|---:|---|
| Merchant / tax responsibility clarity | 20% | Current written terms, seller role, tax treatment and professional review |
| Digital-PDF delivery reliability | 15% | Non-public end-to-end test, checksum/version controls, re-delivery procedure |
| Buyer payments and worldwide support | 15% | Verified target-country/payment-method coverage, seller eligibility and payout confirmation |
| Refund / chargeback / support workflow | 15% | Policy fit, operational owner, documented escalation and test records |
| Data minimization and export | 10% | Data map, retention, export, deletion and access-control review |
| NORTH storefront integration | 10% | No public activation; staged design and signed-event/webhook plan |
| Multi-language / currency future fit | 10% | Documented support and test plan; English pilot remains the only candidate edition |
| Affiliate / sharing compatibility | 5% | Deferred until founder approval; disclosure and privacy design only |

## Selection and activation gates

No provider can be selected, connected, or activated until the founder approves the product, policy drafts, data handling, target market, operating owner, merchant test plan, and a provider decision. Any chosen provider must then be tested with a non-public product, test payment environment where available, signed payment-event verification, receipt, secure delivery, re-delivery, support/refund path, and failure handling before a customer-facing sale.

## References

[1]: https://docs.lemonsqueezy.com/help/payments/merchant-of-record "Lemon Squeezy — Merchant of Record"
[2]: https://gumroad.com/terms "Gumroad Terms of Service"
[3]: https://help.shopify.com/en/manual/taxes/tax-on-digital-products "Shopify Help — Digital Product Taxes"
