/* NORTH Phase 2A private Product Studio renderer.
 * This renderer is deliberately non-commercial: it uses only governed registry states.
 */
(function (window, document) {
  'use strict';

  const STUDIO = window.NORTH_PRODUCT_STUDIO;
  if (!STUDIO) throw new Error('NORTH_PRODUCT_STUDIO must load before product-studio.js');

  const esc = (value) => String(value ?? '').replace(/[&<>'"]/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#039;', '"': '&quot;' }[char]));
  const catalog = () => STUDIO.catalog();
  const label = (value) => ({ concept: 'Concept', in_production: 'In production', review_required: 'Expert review required', approved_for_sale: 'Approved for sale', retired: 'Retired' }[value] || value);
  const categoryTitle = (category) => ({ resources: 'Resources', programs: 'Programs', books: 'Books & authority', collections: 'Collections', recommendations: 'NORTH Picks', physical: 'Physical systems', audio: 'Original audio' }[category] || category);

  function shell(active, content, options) {
    const internal = options && options.internal;
    const nav = internal
      ? '<span class="studio-lock" aria-label="Internal review only">Internal review</span>'
      : `<nav class="studio-nav" aria-label="Primary navigation"><a href="/" ${active === 'app' ? 'aria-current="page"' : ''}>App</a><a href="/library" ${active === 'library' ? 'aria-current="page"' : ''}>Library</a><a href="/library/resources" ${active === 'resources' ? 'aria-current="page"' : ''}>Resources</a><a href="/library/programs" ${active === 'programs' ? 'aria-current="page"' : ''}>Programs</a><a href="/library/books" ${active === 'books' ? 'aria-current="page"' : ''}>Books</a><a class="studio-app-link" href="https://apps.apple.com/us/app/north-find-your-north/id6757988392" target="_blank" rel="noopener">App Store ↗</a></nav>`;
    document.getElementById('libraryApp').innerHTML = `
      <header class="studio-header"><div class="studio-shell studio-header-inner"><a class="studio-brand" href="/library" aria-label="NORTH Library"><span aria-hidden="true">✦</span><span>NORTH</span><em>Library</em></a>${nav}</div></header>
      ${content}
      <footer class="studio-footer"><div class="studio-shell"><p>© 2026 NORTH. English source release.</p><p>${internal ? 'Internal product operations view. Not for public release.' : 'Product concepts are shown only with their honest development state.'}</p></div></footer>`;
  }

  function productCard(item) {
    const policy = STUDIO.renderPolicy(item);
    const state = policy.displayState;
    const href = `/library/item?product=${encodeURIComponent(item.slug)}`;
    const copy = state === 'private_preview' ? 'View production brief →' : state === 'hidden' ? 'View concept brief →' : 'View release state →';
    return `<a class="studio-product-card" href="${href}" data-product="${esc(item.slug)}"><div class="studio-card-top"><span class="studio-status ${esc(item.status)}">${esc(label(item.status))}</span><span class="studio-release">${esc(item.releaseFamily)}</span></div><h3>${esc(item.title)}</h3><p>${esc(item.outcome)}</p><div class="studio-card-bottom"><span>${copy}</span><span aria-hidden="true">→</span></div></a>`;
  }

  function libraryIndex() {
    const releaseA = catalog().filter((item) => item.releaseFamily === 'Release A');
    const counts = [
      ['resources', 'Resources', 'Practical tools with a defined outcome.', '01'],
      ['programs', 'Programs', 'Guided resets with a clear finish line.', '02'],
      ['books', 'Books & authority', 'A durable editorial foundation, built responsibly.', '03']
    ];
    shell('library', `<main>
      <section class="studio-hero"><div class="studio-shell studio-hero-grid"><div><p class="studio-eyebrow">NORTH Library</p><h1>Clarity is a practice.<br><em>Build the next one.</em></h1><p class="studio-lead">A calm, editorial place for practical NORTH tools, programs, and future authority work. The app remains your daily implementation layer; the Library is the deeper work beside it.</p><div class="studio-actions"><a class="studio-button" href="/library/free-tools">Use a free tool</a><a class="studio-button secondary" href="/">Explore the app</a></div></div><aside class="studio-hero-note"><span>Product Studio preview</span><strong>Release A is in production.</strong><p>Concepts are visible here only as governed development records. Nothing is sold, preordered, or delivered in this private phase.</p></aside></div></section>
      <section class="studio-section studio-paper"><div class="studio-shell"><div class="studio-section-head"><p class="studio-eyebrow">Release A</p><h2>Three practical outcomes, built before they are offered.</h2><p>Each product is designed to stand alone without requiring the NORTH app. The app is a helpful daily next step, never a hidden requirement.</p></div><div class="studio-product-grid">${releaseA.map(productCard).join('')}</div></div></section>
      <section class="studio-section"><div class="studio-shell"><div class="studio-section-head"><p class="studio-eyebrow">The Library</p><h2>Choose the kind of work you need.</h2></div><div class="studio-category-grid">${counts.map(([slug, title, text, number]) => `<a href="/library/${slug}" class="studio-category"><span>${number}</span><h3>${title}</h3><p>${text}</p><strong>Explore →</strong></a>`).join('')}</div></div></section>
      <section class="studio-section studio-quiet"><div class="studio-shell studio-split"><div><p class="studio-eyebrow">Free, today</p><h2>Start privately in your browser.</h2><p>The current free tools remain browser-local. No account, email, upload, or purchase is required.</p></div><a class="studio-text-link" href="/library/free-tools">Open Free Tools <span>→</span></a></div></section>
    </main>`);
  }

  function category(category, title, description) {
    const records = catalog().filter((item) => item.category === category);
    shell(category, `<main><section class="studio-hero compact"><div class="studio-shell studio-hero-grid"><div><p class="studio-eyebrow">NORTH Library</p><h1>${esc(title)}</h1><p class="studio-lead">${esc(description)}</p></div><aside class="studio-hero-note"><span>Release control</span><strong>Honest availability, always.</strong><p>Every record carries its actual content, review, delivery, support, policy, and locale state. Unfinished work never becomes a purchase path.</p></aside></div></section><section class="studio-section studio-paper"><div class="studio-shell"><div class="studio-product-grid">${records.map(productCard).join('') || '<p class="studio-empty">No production records are planned for this category yet.</p>'}</div></div></section></main>`);
  }

  function productPage() {
    const slug = new URLSearchParams(window.location.search).get('product');
    const item = catalog().find((record) => record.slug === slug);
    if (!item) { shell('library', `<main class="studio-template"><div class="studio-shell"><p class="studio-eyebrow">Library record</p><h1>That record is not available.</h1><p class="studio-lead">Return to the Library to explore the active product roadmap.</p><a class="studio-button" href="/library">Return to Library</a></div></main>`); return; }
    const policy = STUDIO.renderPolicy(item);
    const locale = item.localeReadiness.en;
    shell(item.category, `<main class="studio-template"><div class="studio-shell"><p class="studio-breadcrumb"><a href="/library">Library</a> / <a href="/library/${esc(item.category)}">${esc(categoryTitle(item.category))}</a> / ${esc(item.title)}</p><div class="studio-detail-grid"><article><div class="studio-card-top"><span class="studio-status ${esc(item.status)}">${esc(label(item.status))}</span><span class="studio-release">${esc(item.releaseFamily)}</span></div><h1>${esc(item.outcome)}</h1><p class="studio-lead">${esc(item.title)} is an internal ${esc(item.status.replace('_', ' '))} record. It is not listed as available for purchase, preorder, delivery, or entitlement in Phase 2A.</p><div class="studio-detail-pairs"><section><h2>For</h2><p>${esc(item.audience)}</p></section><section><h2>Not for</h2><p>${esc(item.notFor)}</p></section></div><section class="studio-detail-section"><p class="studio-eyebrow">Planned deliverables</p><h2>What must exist before release</h2><ul>${item.deliverables.map((value) => `<li>${esc(value)}</li>`).join('')}</ul></section><section class="studio-detail-section"><p class="studio-eyebrow">Release gate</p><h2>What blocks a sale today</h2><ul>${item.blockers.map((value) => `<li>${esc(value)}</li>`).join('')}</ul></section>${item.compliance.moneyEducation ? '<section class="studio-compliance"><strong>Money education boundary.</strong><p>This internal concept cannot be released without qualified financial-professional and legal review. It does not provide individual advice or collect personal financial data.</p></section>' : ''}</article><aside class="studio-detail-aside"><p class="studio-eyebrow">Readiness</p><dl><div><dt>Safe state</dt><dd>${esc(policy.displayState.replace('_', ' '))}</dd></div><div><dt>Content</dt><dd>${item.contentComplete ? 'Complete' : 'Not complete'}</dd></div><div><dt>Delivery</dt><dd>${esc(item.deliveryStatus.replace('_', ' '))}</dd></div><div><dt>Support</dt><dd>${item.supportReady ? 'Ready' : 'Not ready'}</dd></div><div><dt>Policy</dt><dd>${esc(item.refundPolicyStatus.replace('_', ' '))}</dd></div><div><dt>English page</dt><dd>${esc(locale.page.replace('_', ' '))}</dd></div></dl><div class="studio-blocked-action"><span>Phase 2A release control</span><strong>Not available in this phase</strong><p>Price, savings, checkout, delivery promise, and app entitlement remain disabled until every required gate is complete.</p></div></aside></div></div></main>`);
  }

  function readinessDashboard() {
    const rows = catalog().map((item) => {
      const policy = STUDIO.renderPolicy(item);
      return `<tr><td data-label="Offer"><strong>${esc(item.title)}</strong><span>${esc(item.releaseFamily)}</span></td><td data-label="Status"><span class="studio-status ${esc(item.status)}">${esc(label(item.status))}</span></td><td data-label="Content">${item.contentComplete ? 'Complete' : 'Open'}</td><td data-label="Review">${item.compliance.moneyEducation ? 'Expert + legal' : item.compliance.licensedContent ? 'Rights review' : 'Not started'}</td><td data-label="Safe state">${esc(item.safePublicState.replace('_', ' '))}</td><td data-label="Next owner">${esc(item.nextOwner)}</td><td data-label="Release gate">${policy.eligible ? 'Approved' : `${item.blockers.length} blockers`}</td></tr>`;
    }).join('');
    const localeRows = STUDIO.localeRegistry.locales.map((locale) => `<tr><td data-label="Locale">${esc(locale.name)}</td><td data-label="State">${esc(locale.state.replaceAll('_', ' '))}</td><td data-label="RTL QA">${locale.rtl ? 'Required' : 'Not required'}</td><td data-label="Requirements">${esc(locale.requirements.join(' · '))}</td></tr>`).join('');
    shell('internal', `<main class="studio-dashboard"><div class="studio-shell"><div class="studio-dashboard-head"><div><p class="studio-eyebrow">NORTH Product Studio</p><h1>Release control dashboard</h1><p>Internal decision support only. No customer data, credentials, unpublished product files, checkout configuration, or launch controls are exposed here.</p></div><span class="studio-lock">Private Phase 2A</span></div><section class="studio-metric-grid"><article><strong>${catalog().length}</strong><span>roadmap records</span></article><article><strong>${catalog().filter((item) => item.status === 'in_production').length}</strong><span>in production</span></article><article><strong>${catalog().filter((item) => item.status === 'review_required').length}</strong><span>review required</span></article><article><strong>0</strong><span>approved for sale</span></article></section><section class="studio-dashboard-table"><div class="studio-section-head"><p class="studio-eyebrow">Offer readiness</p><h2>Every offer remains governed by its actual work.</h2></div><div class="studio-table-wrap"><table><thead><tr><th>Offer</th><th>Status</th><th>Content</th><th>Review</th><th>Safe public state</th><th>Next owner</th><th>Release gate</th></tr></thead><tbody>${rows}</tbody></table></div></section><section class="studio-dashboard-table"><div class="studio-section-head"><p class="studio-eyebrow">Localization readiness</p><h2>English is the source; release requires the whole path.</h2></div><div class="studio-table-wrap"><table><thead><tr><th>Locale</th><th>State</th><th>RTL QA</th><th>Requirements</th></tr></thead><tbody>${localeRows}</tbody></table></div></section></div></main>`, { internal: true });
  }

  window.NORTH_PRODUCT_STUDIO_VIEW = Object.freeze({ libraryIndex, category, productPage, readinessDashboard });
})(window, document);
