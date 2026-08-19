# NORTH Premium Visual System

**Phase:** 2G private candidate
**Purpose:** Keep the website and NORTH mobile-app expression visibly one brand while prioritizing product truth, accessibility, calm utility, and mobile clarity.

> **Design position:** NORTH is adult, quiet, directional, and useful. It is not a generic productivity template, a mockup gallery, a physical-goods storefront, or a motivational-hype brand.

## 1. Foundation Tokens

| Token | Value | Use |
|---|---:|---|
| `--north-midnight` | `#071A2D` | Primary navigation, dark hero fields, trusted editorial depth |
| `--north-horizon` | `#102B45` | Secondary dark surface and layered depth |
| `--north-ivory` | `#F7F3EB` | Primary warm reading surface |
| `--north-paper` | `#FFFDF8` | Elevated quiet content/card surface |
| `--north-gold` | `#C8A96B` | Controlled accent, rule, focus indicator, status detail; never the only meaning carrier |
| `--north-ink` | `#172738` | Primary text on light surfaces |
| `--north-muted` | `#5E6970` | Secondary explanatory text |
| `--north-line` | `rgba(23,39,56,.16)` | Rules, proof frames, quiet separation |
| `--north-review` | `#956D23` | Founder-review status only; paired with text |
| `--north-available` | `#276E63` | Current public free-tool availability only; paired with text |

The palette is intentionally constrained: midnight navy, warm ivory, and controlled gold form the core visual language. Natural paper, walnut, or daylight atmosphere can appear only in labeled supporting imagery; it cannot replace proof of a digital product.

## 2. Typography and Editorial Hierarchy

| Level | Treatment | Intended job |
|---|---|---|
| Display `H1` | Editorial serif, 3rem–6.5rem responsive, tight tracking | Directional page promise; one per page |
| Section `H2` | Editorial serif, 2rem–4.2rem responsive | Section hierarchy; calm reading cadence |
| Section `H3` | Editorial serif, 1.2rem–1.7rem | Product-proof card or content substructure |
| Eyebrow | Sans-serif, uppercase, 0.72rem, generous tracking, gold | Quiet route/status context |
| Body | Inter/system sans-serif, 0.94rem–1.28rem | Straightforward product facts and boundaries |
| Proof label | Sans-serif, 0.74rem–0.84rem, high contrast | Clarifies actual proof versus illustrative material |

Use no more than one display serif and one body sans-serif. Product facts should read plainly before the editorial tone is noticed.

## 3. Grid, Spacing, Card, and Button Rules

The system uses a 4px spacing grid, with the working sequence `4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96`. Page shells cap at 1180px and preserve a minimum 16px side inset on small screens. Desktop proof layouts may use a 12-column grid; mobile collapses to one column before readability suffers.

Cards are flat-to-lightly-elevated paper surfaces, usually with 1px lines and one consistent 12px or 14px radius. Avoid exaggerated shadows, glass effects, decorative badges, or card stacks that compete with product proof. Buttons may be navy/gold primary, outlined ivory secondary, or disabled review state. A button must never simulate checkout unless a real approved checkout exists.

## 4. Icon and Symbol Rules

The supplied official NORTH compass is the sole brand anchor. No generated compass, alternate mark, decorative logo, or fake app icon can stand in for it. The compass may appear as a meaningful linked brand mark or as decorative art with `aria-hidden="true"`; it must not be announced redundantly.

Use text-first status labels. Any dot, star, arrow, or icon is supplementary and never carries availability, approval, or safety meaning alone.

## 5. Product Image and Buyer-Proof Rules

| Image type | Primary job | Allowed use | Required label |
|---|---|---|---|
| Actual PDF export | Prove the real digital product | Primary proof: Start Here, intention, daily page, weekly/final review, print-format evidence | `Actual Planner-page proof — private founder-review source.` |
| Actual A4/US Letter proof | Prove format evidence | Print-format comparison | `Actual [format] private print-proof page — not a customer delivery file.` |
| Approved generated visual | Editorial atmosphere only | One hero and one or two secondary supporting scenes | `Illustrative digital product mockup — not a physical product photograph.` |
| Physical-looking mockup | Atmosphere only; never proof | Only if needed and clearly subordinate to real proof | Same illustrative digital-product disclosure |
| Placeholder / unrelated asset | None | Prohibited | Remove or quarantine |

Do not show several near-identical notebook images. A buyer-proof flow should sequence **what it is → what is inside → how it is used → real page evidence → print evidence → boundaries → release status**. Generated imagery must never suggest a hardcover shipment, boxed kit, real buyer result, or unlisted app feature.

## 6. Motion and Interaction

Motion is short and purposeful: a 160–220ms hover/focus transition or a single entry reveal is sufficient. Do not use autoplay, parallax, scrolling gimmicks, looped decoration, or animation that interrupts reading.

All animated and smooth-scroll behavior must respect `prefers-reduced-motion: reduce`. In that mode, transitions and reveals are removed and scrolling returns to normal. Every link, form control, disabled action, card, menu button, and language selector receives a visible focus indicator with sufficient contrast.

## 7. Accessibility and Mobile-First Rules

1. Use semantic landmarks, one `h1`, ordered heading hierarchy, descriptive navigation labels, a visible-on-focus skip link, and native controls wherever practical.
2. Product proof images require source-specific alt text. Illustrative imagery must say that it is illustrative and not physical product proof. Decorative marks use empty alt text.
3. Text must be readable at 390px without horizontal scrolling, clipped disclosure labels, hidden focus, or a two-column proof layout that becomes too narrow.
4. Tables must have headers, and any dense product matrix must become scrollable or stack intentionally on mobile.
5. Arabic routes set `dir="rtl"`, right-align body copy where appropriate, reverse directional layout intentionally, and retain logical source order and focus sequence.
6. The color gold can accent a label or focus ring but cannot be the sole presentation of status, warning, availability, or required action.

## 8. Route Application

| Private candidate surface | Required expression |
|---|---|
| Homepage | Premium brand system, current-state honesty, App Store and Free Tools only as public actions |
| Library | Clear availability/status labels; no roadmap product presented as a current offer |
| Programs / product overview | Information architecture and founder-review state; no buy/download flow |
| 1-3-5 Planner private page | Real buyer proof first; labeled illustrative art secondary; truthful delivery/accessibility boundaries |
| Free Tools | Simple browser-local utility UI, clear data/privacy language, no account/capture/commerce decoration |
| Product roadmap | A status/gate matrix, not product-card theater or a fake catalog |

This system is a Phase 2G private-candidate standard. It does not itself approve product release, public launch, or commerce activation.
