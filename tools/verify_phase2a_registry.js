#!/usr/bin/env node
'use strict';

const fs = require('fs');
const vm = require('vm');
const path = require('path');

const root = '/home/ubuntu/north-phase2a';
const sandbox = { window: {} };
vm.createContext(sandbox);
vm.runInContext(fs.readFileSync(path.join(root, 'assets/product-studio-config.js'), 'utf8'), sandbox, { filename: 'product-studio-config.js' });
const studio = sandbox.window.NORTH_PRODUCT_STUDIO;
const expectedSlugs = [
  '1-3-5-execution-planner', 'decision-clarity-toolkit', 'focus-recovery-program',
  'weekly-compass-journal', 'financial-clarity-kit', 'north-foundation-collection',
  'find-your-north-book', 'north-90-day-direction-sprint', 'north-90-day-direction-book',
  'north-money-foundations', 'family-money-meeting-system', 'adult-money-foundations',
  'north-picks', 'north-physical-planners', 'north-original-audio'
];
const products = studio.catalog();
const failures = [];
function check(condition, message) { if (!condition) failures.push(message); }

check(products.length === expectedSlugs.length, `Expected ${expectedSlugs.length} roadmap records; found ${products.length}`);
for (const slug of expectedSlugs) check(products.some((product) => product.slug === slug), `Missing roadmap slug: ${slug}`);
for (const product of products) {
  const policy = studio.renderPolicy(product);
  check(studio.productStatuses.includes(product.status), `${product.slug}: unsupported status ${product.status}`);
  check(studio.safePublicStates.includes(product.safePublicState), `${product.slug}: unsupported safe state ${product.safePublicState}`);
  check(!policy.eligible, `${product.slug}: incorrectly eligible for sale`);
  check(!policy.allowPrice && !policy.allowSavingsClaim && !policy.allowPurchaseCTA && !policy.allowCheckout && !policy.allowDeliveryPromise && !policy.allowAppEntitlement, `${product.slug}: commercial rendering flag enabled`);
  check(policy.displayPrice === null, `${product.slug}: displayed a price`);
  check(Array.isArray(product.blockers) && product.blockers.length > 0, `${product.slug}: missing release blockers`);
  check(product.localeReadiness && Object.keys(product.localeReadiness).length === studio.localeRegistry.verifiedMobileAppLocales.length, `${product.slug}: locale-readiness path incomplete`);
}
check(studio.localeRegistry.sourceLocale === 'en', 'English is not the canonical source locale');
check(studio.localeRegistry.verifiedMobileAppLocales.length === 14, 'Verified app locale count is not 14');
check(studio.localeRegistry.locales.find((locale) => locale.code === 'ar')?.rtl === true, 'Arabic RTL review flag is missing');

const htmlFiles = fs.readdirSync(root).filter((file) => file.endsWith('.html'));
for (const file of ['library.html', 'library-resources.html', 'library-programs.html', 'library-books.html', 'library-item.html']) {
  const text = fs.readFileSync(path.join(root, file), 'utf8');
  check(text.includes('/assets/product-studio-config.js'), `${file}: missing product registry loader`);
  check(text.includes('/assets/product-studio.js'), `${file}: missing product studio loader`);
}
const studioPage = fs.readFileSync(path.join(root, 'internal/studio-control.html'), 'utf8');
check(studioPage.includes('noindex,nofollow,noarchive'), 'Internal dashboard is missing no-index directive');
const accessGuard = fs.readFileSync(path.join(root, 'internal/.htaccess'), 'utf8');
check(/Require all denied|Deny from all/.test(accessGuard), 'Internal dashboard has no shared-hosting access guard');

const result = {
  branch: 'north-web-phase2a-product-studio',
  source_baseline: 'e7e81968127f8f7ef7e76c09475312ebda68477b',
  product_record_count: products.length,
  verified_mobile_app_locale_count: studio.localeRegistry.verifiedMobileAppLocales.length,
  commercial_eligible_record_count: products.filter((product) => studio.renderPolicy(product).eligible).length,
  result: failures.length ? 'FAIL' : 'PASS',
  failures
};
fs.mkdirSync(path.join(root, 'evidence'), { recursive: true });
fs.writeFileSync(path.join(root, 'evidence/phase2a-registry-verification.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify(result, null, 2));
process.exit(failures.length ? 1 : 0);
