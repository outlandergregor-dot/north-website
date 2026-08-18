#!/usr/bin/env node
/* Build a public-only catalog from canonical registries. Never copy private review paths, pricing, or release-control internals. */
const fs = require('fs');
const vm = require('vm');
const path = require('path');
const root = '/home/ubuntu/north-phase2c';
function load(rel, key) {
  const ctx = { window: {}, Object, String, Array, Boolean, Number, console };
  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(root, rel), 'utf8'), ctx);
  return ctx.window[key];
}
const studio = load('assets/product-studio-config.js', 'NORTH_PRODUCT_STUDIO');
const north = load('assets/north-config.js', 'NORTH_CONFIG');
const appStoreUrl = north.appStoreUrl || north.APP_STORE_URL || 'https://apps.apple.com/us/app/north-find-your-north/id6757988392';
const freeTools = Object.values(north.products || {}).filter((item) => item.category === 'free-tools' && item.availability === 'available').map((item) => ({
  slug: item.slug, title: item.title, outcome: item.outcome, summary: item.summary, time: item.time, href: item.action && item.action.href, state: 'available'
}));
const allowedReleaseA = new Set(['1-3-5-execution-planner', 'decision-clarity-toolkit', 'focus-recovery-program']);
const releaseA = studio.catalog().filter((item) => allowedReleaseA.has(item.slug)).map((item) => ({
  slug: item.slug,
  title: item.title,
  category: item.category,
  outcome: item.outcome,
  audience: item.audience,
  notFor: item.notFor,
  formatIntent: item.deliverables.map((line) => line.replace(/—.*$/, '').trim()),
  timeCommitment: item.slug === '1-3-5-execution-planner' ? 'Designed around a 14-day rhythm' : item.slug === 'focus-recovery-program' ? 'Designed around seven short days' : 'Designed for a considered self-guided decision session',
  state: 'in_founder_review',
  overviewHref: `/library/item?product=${encodeURIComponent(item.slug)}`,
  sample: item.slug === '1-3-5-execution-planner' ? ['One meaningful priority', 'Three supporting actions', 'Five small wins'] : item.slug === 'decision-clarity-toolkit' ? ['Decision context', 'Trade-off reflection', 'A clear next choice'] : ['One focus priority', 'A bounded daily action', 'A useful next-day rhythm'],
  languageReadiness: {
    websiteLanguage: 'English complete source; 13 governed locale routes pending human review.',
    productContentLanguage: 'English founder review draft only; no customer product-language release.',
    checkoutLanguage: 'Not enabled.',
    deliveryLanguage: 'Not enabled.',
    supportLanguage: 'Not release-ready.',
    legalPolicyLanguage: 'Not release-ready.'
  }
}));
const futureArchitecture = [
  { key: 'programs', title: 'Programs', state: 'planned_after_review', summary: 'Later guided learning experiences will be considered only after complete curricula, support design, and founder approval.' },
  { key: 'books', title: 'Books & Authority', state: 'planned_after_review', summary: 'Original NORTH books and audio are planned directions, not current publications or storefront items.' },
  { key: 'money', title: 'Money Education', state: 'in_development', summary: 'A later general adult money-organization education architecture is under review. It will never replace individualized professional advice.' },
  { key: 'picks', title: 'NORTH Picks & Physical', state: 'planned_after_review', summary: 'Recommendations and physical goods are later concepts. No affiliate links, product listings, or fulfillment are active.' }
];
const payload = {
  phase: 'phase-2c-static-candidate',
  sourceLanguage: 'en',
  appStoreUrl,
  freeTools,
  releaseA,
  futureArchitecture,
  availabilityCopy: {
    available: 'Available now',
    in_founder_review: 'In founder review',
    in_development: 'In development',
    planned_after_review: 'Planned after review'
  },
  safeguards: { saleEligibility: false, hasCheckout: false, hasPayment: false, hasEmailCapture: false, hasDelivery: false, hasTranslations: false }
};
const output = `(function (window) { 'use strict'; window.NORTH_PUBLIC_CATALOG = Object.freeze(${JSON.stringify(payload, null, 2)}); })(window);\n`;
fs.writeFileSync(path.join(root, 'assets/public-catalog.js'), output);
console.log(JSON.stringify({ freeTools: freeTools.length, releaseA: releaseA.length, phase: payload.phase }, null, 2));
