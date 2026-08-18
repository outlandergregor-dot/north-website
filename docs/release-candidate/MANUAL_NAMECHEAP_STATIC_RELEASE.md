# NORTH Phase 2C — Manual Namecheap Static Release Handoff

> **Release status:** Private static release candidate only. This document does **not** authorize upload, extraction, DNS edits, nameserver changes, redirects, Vercel changes, or public launch.

## Package contents

The ZIP contains a `website/` directory. Its contents—not the parent `website` folder—belong in the confirmed public document root when and only when the founder authorizes a manual release. The directory includes `index.html`, public assets, 14 locale route folders, `robots.txt`, and `.htaccess` clean-route rules.

The package intentionally excludes every `internal/` route, Founder Review artifact, editable source package, print-review export, private password, private registry field, checkout path, payment component, delivery artifact, Gumroad configuration, email-capture form, affiliate component, and deployment configuration.

## Required pre-upload confirmation

Before a future upload, confirm in the Namecheap/cPanel account that the target domain is the intended production domain and identify its **current document root**. Do not change the Nameservers, Host Records, CNAME records, domain redirects, email forwarding, or HTTPS settings merely to upload this candidate. Preserve the current website files as a named archive before replacement.

| Check | Required evidence before any future upload |
|---|---|
| Domain target | Screenshot or written confirmation of the exact domain and document root |
| Rollback | Dated ZIP backup of all current document-root files and a note of the prior version |
| Candidate integrity | ZIP SHA-256 matches `STATIC_RELEASE_MANIFEST.json` and the release record |
| Scope | Founder confirms this candidate remains noindex until a separate public-launch decision |
| Hosting behavior | Apache `.htaccess` is supported by the intended cPanel/shared-hosting plan |

## Future staging sequence

Use a temporary staging subdomain only after explicit approval. Upload the ZIP through cPanel File Manager, extract it outside the public root if possible, and point the staging document root to the extracted **contents of `website/`**. Do not point the domain at the parent package folder; doing so will produce nested paths and broken clean routes.

Keep the included `robots.txt` and `.htaccess` unchanged during staging. They intentionally prevent indexing through both a `Disallow: /` file and an `X-Robots-Tag: noindex, nofollow, noarchive` response header where Apache headers are available.

## Future production sequence

Do not perform this sequence unless the founder gives a written production decision.

1. Create and verify the rollback archive of the current document root.
2. Upload the approved Phase 2C ZIP to cPanel File Manager without changing DNS, nameservers, or redirects.
3. Extract to a temporary folder and move the **contents of `website/`** into the confirmed document root.
4. Confirm that `.htaccess` is present and readable; do not rename it.
5. Verify HTTPS at the existing canonical host. Do not buy, replace, or remove any certificate as part of this candidate upload.
6. Test `/`, `/library`, `/library/free-tools`, `/library/resources`, `/library/programs`, `/library/books`, `/library/money-education`, `/library/item?product=1-3-5-execution-planner`, `/about`, `/pt-BR/`, `/es-419/`, and `/ar/` with refreshes.
7. Verify that every Release A overview states **In founder review** and has no price, checkout, delivery, download, preorder, waitlist, or private link.
8. Verify only the App Store and verified Free Tools are public actions.
9. Retain `noindex` protection until a later written public-launch authorization.

## Rollback procedure

If any route, browser-local tool, layout, asset, HTTPS behavior, or claims check fails, immediately restore the named pre-release archive into the same document root. Confirm the old site renders on the canonical host, then stop and record the exact failed route or asset. Do not attempt a DNS, nameserver, redirect, or Vercel workaround.
