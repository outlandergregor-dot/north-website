# NORTH Phase 2B — Private Preview Record

> **Review status:** Founder review draft — not for sale.  
> **Environment:** Temporary authenticated preview; not production hosting.

## Preview controls

| Control | Verified state |
|---|---|
| Access model | HTTP Basic authentication; unauthenticated GET returned `401` |
| Authenticated review route | Returned `200` for `/internal/founder-review` only with the temporary credential |
| Robots directive | `X-Robots-Tag: noindex, nofollow, noarchive` |
| Cache directive | `Cache-Control: no-store` |
| Production impact | None. No Namecheap, DNS, Vercel, or production hosting change was made. |
| Commercial impact | None. The preview contains no checkout, payment, delivery, entitlement, email capture, or customer access. |
| Credential storage | Temporary credential is excluded from Git; it is conveyed to the founder only in the task handoff. |

## Private review entry point

The founder entry route is `/internal/founder-review`. It contains links to the three draft detail pages and actual private HTML review exports. All review material is marked “Founder review draft — not for sale.”

## Expected preview lifecycle

The preview is temporary and access-controlled. It is intended only for founder review during this task session and may stop when the temporary environment ends. The durable evidence and editable sources are committed on the isolated branch and attached in the evidence archive.
