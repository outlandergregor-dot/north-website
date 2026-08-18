# Future Opt-In Sharing System — Phase 2E Specification

> **Roadmap only. No social integration, tracking, share-card generation, account connection, auto-posting, or public sharing feature is built in Phase 2E.**

## Purpose

Future sharing can help people celebrate intentional action without exposing the private data that makes NORTH useful. The system must create a voluntary, editable preview and require an explicit final user action before any share leaves NORTH.

## Candidate share artifacts

| Asset | Safe default content | Prohibited default content |
|---|---|---|
| My Big Thing card | User-approved short title or generic “My Big Thing” statement | Captain memory, journal body, detailed task list, calendar information, voice transcript |
| Weekly reset completion card | Generic completion milestone and selected non-sensitive theme | Reflection text, habit history, private priorities, health details |
| 1-3-5 planning cover | Non-sensitive title or a generic planning-session cover | Individual tasks, work/client names, private next steps |
| Focus-session milestone | Duration category or generic milestone the user approves | Focus content, location, app data, calendar or identity details |
| NORTH journey progress card | Non-sensitive self-selected progress phrase | Financial information, routines/history, journal text, personal identifiers |

## Required interaction flow

```text
User requests share
  → NORTH creates local preview with conservative defaults
  → user reviews and optionally edits / removes content
  → user selects destination
  → user explicitly confirms share
  → platform-native handoff occurs
```

No auto-posting, queued posting, background sharing, destination connection, or silent data export is allowed. A user must be able to cancel at the preview stage. NORTH attribution and a link can be included only after founder approval and must never displace the user’s privacy choices.

## Privacy and launch gates

1. Share payload starts with no Captain memory, journal text, voice transcripts, financial information, private tasks, calendar details, or identifiers.
2. Every field entering a card is visibly previewed and editable before the user’s final confirmation.
3. No social account connection, share analytics, referral attribution, or affiliate tracking is added until separately approved.
4. The system needs threat-model, consent, retention, platform-policy, accessibility, and localization review before implementation.
5. Any share event must use data minimization, documented purpose limitation, and a founder-approved privacy notice.
