# Phase 2G Performance and Image-Size Audit

**Scope:** Authenticated private 1-3-5 Planner buyer-proof route.
**Method:** Source-controlled delivery-size inventory, static image-budget verification, and browser visual QA.

| Resource | Delivery size | Delivery role | Control |
|---|---:|---|---|
| `assets/commerce-pilot.css` | 10,915 B | Private page styling | Source-controlled; responsive and reduced-motion rules included |
| `assets/commerce-pilot.js` | 13,388 B | Private renderer | Source-controlled; no commerce SDK or tracking endpoint |
| Start Here US Letter proof PNG | 264,412 B | Actual page proof | Lazy-loaded in the proof grid |
| Two-Week Intention US Letter proof PNG | 116,681 B | Actual page proof | Lazy-loaded in the proof grid |
| Daily Page US Letter proof PNG | 126,329 B | Hero and proof evidence | Hero instance receives priority; grid instance lazy-loads |
| Final Review US Letter proof PNG | 94,957 B | Actual page proof | Lazy-loaded in the proof grid |
| Start Here A4 proof PNG | 39,584 B | Actual print-format evidence | Lazy-loaded |
| Illustrative editorial WebP | 485,800 B | Supporting atmosphere only | Lazy-loaded; present once; persistent illustrative label |
| **Total key source files** | **1,152,066 B** | CSS, renderer, five proof exports, one editorial WebP | Private-review budget; excludes browser caching/compression effects |

## Findings

The actual-page proof exports are all below the Phase 2G per-asset budget of 400 KB. The optimized editorial WebP is below the 800 KB budget and appears once, after real proof. The static verifier passed the size controls and confirms that the old physical-looking image pair is not referenced by the flagship proof renderer.

No payment, merchant, affiliate, or analytics endpoint is present in the audited private/public renderer source. Generated imagery is not used as the first or only product evidence. The four lower proof cards and the secondary editorial image use native lazy loading; the hero uses one actual Planner page as priority content.

**Performance conclusion:** The private candidate uses a restrained asset set appropriate for review. Production performance remains a future deployment-stage concern and must be re-tested against the selected real host/CDN before any public release.
