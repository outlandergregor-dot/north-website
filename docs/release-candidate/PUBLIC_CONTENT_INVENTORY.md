# NORTH Phase 2C — Public Content Inventory and Route Model

> **Candidate status:** Private static release candidate. Not deployed, not for sale, and not a public launch authorization.

## Public experience classification

| Experience | Public state | Visitor action allowed in Phase 2C | Explicit exclusion |
|---|---|---|---|
| NORTH App | Available now | Verified App Store destination | No rating, trial, subscription, download, or language claim |
| Find Your North Snapshot | Available now | Open functional browser-local tool | No data transmission or coaching claim |
| 1-3-5 Daily Page | Available now | Open functional browser-local tool | No account, download, or completion claim |
| Weekly Compass Preview | Available now | Open functional browser-local tool | No paid journal, waitlist, or product claim |
| Safe Number Starter Sheet | Available now | Open functional browser-local tool | No individualized financial guidance or recommendation |
| 1-3-5 Execution Planner | In founder review | Read public-safe overview only | No price, purchase, sample download, delivery date, or private draft link |
| Decision Clarity Toolkit | In founder review | Read public-safe overview only | No price, purchase, private decision worksheet, or advice claim |
| Focus Recovery Program | In founder review | Read public-safe overview only | No enrollment, treatment, clinical, or outcome claim |
| Programs | Planned after review | Read high-level architecture | No course catalog, curriculum, enrollment, or waitlist |
| Books & Authority | Planned after review | Read high-level direction | No book cover, authoring claim, preorder, audio, or storefront |
| Money Education | In development | Read tightly governed architecture | No product, individual financial content, minors flow, financial guidance, or affiliate link |
| NORTH Picks / Physical | Planned after review | Read high-level direction only | No recommendation, affiliate, inventory, shipping, or product card |

## Public route model

| Route | Purpose | Data source | Allowed public actions |
|---|---|---|---|
| `/` | Premium NORTH landing page | `NORTH_PUBLIC_CATALOG` + verified app link | App Store, Free Tools, Library |
| `/library` | Editorial Library hub | Public catalog | Free Tools, Release A overview links |
| `/library/resources` | Free Tools directory | Public catalog + verified tool anchors | Use free tool |
| `/library/programs` | Release A context and future-program architecture | Public catalog | Release A overview links; Free Tools |
| `/library/books` | Future book / authority direction | Public catalog | Library; App Store |
| `/library/money-education` | Tightly governed future architecture | Public catalog | Free Tools; App Store |
| `/library/item?product=<slug>` | Reusable public-safe Release A overview | Public catalog allowlist | Free Tools; App Store |
| `/about` | Concise brand story using source-approved brand context | Static approved copy | Library; App Store |
| `/privacy`, `/terms` | Existing approved legal pages only | Existing legal files | No data capture or new legal claim |

## Copy and data rules

The public pages receive no values from `proposedPrice`, `reviewDraft`, source-package paths, internal export paths, internal asset lists, founder notes, passwords, private dashboard routes, commerce controls, support workflows, refund status, or merchant data. The public catalog is generated from the canonical product registry through a field allowlist and is checked to ensure these values do not appear in the release candidate.

English is the only public website source language in this candidate. The mobile app’s wider locale registry is not presented as website or product translation availability. The public brand statement is organizational and educational; it does not claim legal, medical, mental-health, investment, tax, credit, lending, insurance, or individualized financial advice.

## Public Release A overview shape

Each overview may show the intended outcome, audience, not-for boundary, time commitment, format intent, one small non-downloadable framework sample, and the exact state **“In founder review.”** Each overview routes the visitor only to Free Tools or the verified App Store destination. No release date, waitlist, download, purchase, refund, discount, bundle, order, or private-source control may render.
