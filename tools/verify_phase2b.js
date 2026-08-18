#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const root = '/home/ubuntu/north-phase2b';
const report = { phase: '2B', timestamp: new Date().toISOString(), checks: [], passed: 0, failed: 0 };
function check(id, pass, detail) { report.checks.push({ id, pass, detail }); pass ? report.passed++ : report.failed++; }
function file(rel) { return fs.readFileSync(path.join(root, rel), 'utf8'); }
function exists(rel) { return fs.existsSync(path.join(root, rel)); }
function words(rel) { return file(rel).trim().split(/\s+/).filter(Boolean).length; }
try {
  const context = { window: {}, Object, String, Array, Boolean, Number, console };
  vm.createContext(context);
  vm.runInContext(file('assets/product-studio-config.js'), context);
  const studio = context.window.NORTH_PRODUCT_STUDIO;
  const records = studio.catalog().filter((item) => item.reviewDraft);
  check('registry_has_three_release_a_review_records', records.length === 3, `${records.length} review records found`);
  check('registry_phase_is_private_phase_2b', studio.phase === 'phase-2b-private-founder-review', studio.phase);
  for (const record of records) {
    const policy = studio.renderPolicy(record);
    check(`${record.slug}_sale_gate_locked`, record.saleGateLocked === true, `saleGateLocked=${record.saleGateLocked}`);
    check(`${record.slug}_render_policy_is_not_eligible`, policy.eligible === false && !policy.allowPrice && !policy.allowPurchaseCTA && !policy.allowCheckout && !policy.allowDeliveryPromise, JSON.stringify(policy));
    check(`${record.slug}_review_state_is_private`, record.publicVisibility === false && record.safePublicState === 'private_preview', `${record.publicVisibility}/${record.safePublicState}`);
    check(`${record.slug}_complete_draft_metadata`, record.reviewDraft.contentCompletionPercent === 100 && record.reviewDraft.founderApprovalStatus === 'pending_founder_review', JSON.stringify(record.reviewDraft));
    const sourceRel = `${record.reviewDraft.sourcePackage}/01-draft-content.md`;
    const overviewRel = `${record.reviewDraft.sourcePackage}/00-package-overview.md`;
    const exportRel = record.reviewDraft.reviewExport;
    check(`${record.slug}_editable_source_exists`, exists(sourceRel) && exists(overviewRel), `${sourceRel}; ${overviewRel}`);
    check(`${record.slug}_source_is_substantive`, words(sourceRel) >= 1800, `${words(sourceRel)} words`);
    check(`${record.slug}_private_export_exists`, exists(exportRel), exportRel);
    const exportText = file(exportRel);
    check(`${record.slug}_export_is_marked_not_for_sale`, /Founder review draft[^<]{0,50}not for sale/i.test(exportText), 'draft notice present');
    check(`${record.slug}_export_has_no_customer_price_or_checkout`, !/\$17|\$19|\$27|checkout|buy now|add to cart|purchase/i.test(exportText), 'no customer commerce text');
    for (const format of ['US-Letter', 'A4']) {
      const printRel = `internal/print-review/release-a/${record.reviewDraft.artifactStem}_${format}_PRINT-REVIEW-NOT-FOR-SALE.pdf`;
      check(`${record.slug}_${format}_print_review_exists`, exists(printRel) && fs.statSync(path.join(root, printRel)).size > 10000, printRel);
    }
  }
  const dashboard = file('internal/founder-review.html');
  check('dashboard_has_noindex', /noindex,nofollow,noarchive/.test(dashboard), 'robots directive');
  check('dashboard_has_no_form_submission', !/<form\b|action=|method=/i.test(dashboard), 'no form');
  const guard = file('internal/.htaccess');
  check('internal_folder_has_access_guard', /Require all denied|Deny from all/i.test(guard), 'Apache deny rule');
  const finder = file('assets/founder-review.js');
  check('review_notes_are_disabled_and_noncollecting', /textarea disabled/.test(finder) && /does not save, transmit, or collect notes/i.test(finder), 'disabled note placeholder');
  check('no_external_review_assets', !/https?:\/\//.test(finder), 'no remote URLs in review renderer');
} catch (error) {
  check('verification_runtime', false, String(error.stack || error));
}
report.status = report.failed ? 'FAIL' : 'PASS';
fs.mkdirSync(path.join(root, 'evidence'), { recursive: true });
fs.writeFileSync(path.join(root, 'evidence/phase2b-verification.json'), JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));
process.exit(report.failed ? 1 : 0);
