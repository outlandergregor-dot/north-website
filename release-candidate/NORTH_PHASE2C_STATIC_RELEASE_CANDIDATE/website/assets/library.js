(function (window, document) {
  'use strict';

  const NORTH = window.NORTH_CONFIG;
  const LOCALES = window.NORTH_LOCALES;
  if (!NORTH) throw new Error('NORTH_CONFIG must load before library.js');
  if (!LOCALES) throw new Error('NORTH_LOCALES must load before library.js');

  const esc = (value) => String(value).replace(/[&<>'"]/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#039;', '"': '&quot;' }[char]));
  const productList = () => Object.values(NORTH.products);
  const base = (path) => path;

  function northTrack(eventName, properties) {
    if (!NORTH.analytics.allowedEvents.includes(eventName)) return;
    const safeProperties = Object.assign({ language: NORTH.publicWebLanguage }, properties || {});
    if (typeof window.gtag === 'function') window.gtag('event', eventName, safeProperties);
  }

  function trackAppStore(source) {
    northTrack('app_store_click', { source: source || 'library', route: window.location.pathname });
  }

  function activeLocale() {
    const first = window.location.pathname.split('/').filter(Boolean)[0];
    return LOCALES.byCode[first] ? first : 'en';
  }
  function canonicalPath() {
    const bits = window.location.pathname.split('/').filter(Boolean);
    if (LOCALES.byCode[bits[0]]) bits.shift();
    return '/' + bits.join('/') || '/';
  }
  function localeHref(code) {
    const path = canonicalPath();
    return code === 'en' ? path : `/${code}${path}`;
  }
  function localeSelector() {
    const current = activeLocale();
    return `<label class="locale-label" for="libraryLocale">Language</label><select id="libraryLocale" class="library-locale-select" aria-label="Language">${LOCALES.locales.map((item) => `<option value="${esc(item.code)}"${item.code === current ? ' selected' : ''}>${esc(item.nativeName)}</option>`).join('')}</select>`;
  }
  function header(active) {
    return `
      <header class="site-header">
        <div class="library-shell header-inner">
          <a class="brand" href="/" aria-label="NORTH home"><span class="brand-mark" aria-hidden="true">✦</span><span>NORTH</span></a>
          <nav class="header-nav" aria-label="Primary navigation">
            <a href="/"${active === 'home' ? ' aria-current="page"' : ''}>App</a>
            <a href="/library"${active === 'library' ? ' aria-current="page"' : ''}>Library</a>
            <a href="/library/free-tools"${active === 'free-tools' ? ' aria-current="page"' : ''}>Free tools</a>
            ${localeSelector()}
            <a class="app-link" href="${NORTH.brand.appStoreUrl}" target="_blank" rel="noopener" data-app-store-source="library-header">App Store ↗</a>
          </nav>
        </div>
      </header>`;
  }

  function footer() {
    return `
      <footer class="library-footer">
        <div class="library-shell footer-inner">
          <p>© 2026 NORTH. English web release.</p>
          <nav class="footer-links" aria-label="Footer navigation">
            <a href="/library">Library</a>
            <a href="/about">About NORTH</a>
            <a href="/library/free-tools">Free tools</a>
          </nav>
        </div>
      </footer>`;
  }

  function productCard(product) {
    const isAvailable = product.availability === 'available';
    const statusText = isAvailable ? 'Available now' : 'Coming soon';
    const href = isAvailable || ['1-3-5-execution-planner', '7-day-focus-recovery'].includes(product.slug)
      ? `/library/item?product=${encodeURIComponent(product.slug)}`
      : null;
    const content = `
      <span class="status ${isAvailable ? 'available' : 'coming-soon'}">${statusText}</span>
      <h3>${esc(product.title)}</h3>
      <p>${esc(product.summary)}</p>
      ${href ? `<span class="card-link">${isAvailable ? 'Open tool →' : 'View scope →'}</span>` : '<span class="not-available">Not available in Phase 1</span>'}`;
    if (!href) return `<article class="product-card" aria-label="${esc(product.title)} — coming soon">${content}</article>`;
    return `<a class="product-card" href="${href}" data-product-interest="${esc(product.slug)}">${content}</a>`;
  }

  function localeReleaseNotice() {
    const current = activeLocale();
    if (current === 'en') return '';
    const item = LOCALES.byCode[current];
    return `<section class="library-locale-notice" aria-label="Language release notice"><div class="library-shell"><strong>${esc(item.nativeName)}</strong><span>${esc(item.labels.notice)}</span><a href="${canonicalPath()}">View English source</a></div></section>`;
  }
  function mountLayout(active, content) {
    const currentLocale = LOCALES.byCode[activeLocale()] || LOCALES.byCode.en;
    document.documentElement.lang = currentLocale.code;
    document.documentElement.dir = currentLocale.dir;
    const root = document.getElementById('libraryApp');
    root.innerHTML = header(active) + localeReleaseNotice() + content + footer();
    const localeSelect = document.getElementById('libraryLocale');
    if (localeSelect) localeSelect.addEventListener('change', (event) => window.location.assign(localeHref(event.target.value)));
    document.querySelectorAll('[data-app-store-source]').forEach((link) => {
      link.addEventListener('click', () => trackAppStore(link.dataset.appStoreSource));
    });
    document.querySelectorAll('[data-product-interest]').forEach((link) => {
      link.addEventListener('click', () => northTrack('product_interest', { product_slug: link.dataset.productInterest, availability: NORTH.products[link.dataset.productInterest].availability }));
    });
  }

  function renderIndex() {
    const categories = [
      ['free-tools', 'Free Tools', 'Start with one clear next step.', '✦'],
      ['resources', 'Resources', 'Practical tools you can use today.', '◇'],
      ['programs', 'Programs', 'Guided resets with a defined finish line.', '↗'],
      ['books', 'Books & Audio', 'The NORTH method in a durable format.', '○']
    ];
    mountLayout('library', `
      <main>
        <section class="hero"><div class="library-shell hero-grid">
          <div><span class="eyebrow">NORTH Library</span><h1>Useful tools.<br><em>Clear direction.</em></h1><p class="lead">A focused collection of practical resources for planning, reflection, and intentional progress—built to stand on their own, with or without the NORTH app.</p><div class="inline-actions"><a class="button" href="/library/free-tools" data-category="free-tools">Start with a free tool</a><a class="button secondary" href="/">Explore the app</a></div></div>
          <aside class="hero-note"><strong>Phase 1 release</strong><p>Free tools are available now in English. Paid resources and programs are clearly marked as coming soon until their completed assets, delivery, support, and policy requirements are ready.</p></aside>
        </div></section>
        <section class="section alt"><div class="library-shell"><div class="section-header"><span class="eyebrow">Start here</span><h2>Choose the kind of support you need today.</h2></div><div class="category-grid">${categories.map(([slug, title, text, symbol]) => `<a class="category-card" href="/library/${slug}" data-category="${slug}"><span class="card-symbol" aria-hidden="true">${symbol}</span><h3>${title}</h3><p>${text}</p><span class="card-link">Explore ${title} →</span></a>`).join('')}</div></div></section>
        <section class="section paper"><div class="library-shell"><div class="section-header"><span class="eyebrow">Available now</span><h2>Start privately, in your browser.</h2><p>No account, email, purchase, or data upload is required for these first four tools.</p></div><div class="product-grid">${productList().filter((item) => item.category === 'free-tools').map(productCard).join('')}</div></div></section>
      </main>`);
    northTrack('library_view', { route: '/library', category: 'all' });
    document.querySelectorAll('[data-category]').forEach((link) => link.addEventListener('click', () => northTrack('library_category_select', { category: link.dataset.category, route: '/library' })));
  }

  function renderCategory(category, pageTitle, pageText) {
    const items = productList().filter((item) => item.category === category);
    mountLayout(category, `
      <main><section class="hero"><div class="library-shell hero-grid"><div><span class="eyebrow">NORTH Library</span><h1>${esc(pageTitle)}</h1><p class="lead">${esc(pageText)}</p></div><aside class="hero-note"><strong>Availability rule</strong><p>Only complete tools are available. A planned item does not show a price, checkout, preorder, or urgency message.</p></aside></div></section>
      <section class="section alt"><div class="library-shell"><div class="product-grid">${items.map(productCard).join('')}</div></div></section></main>`);
    northTrack('library_view', { route: window.location.pathname, category: category });
  }

  function dailyRows(prefix, count, label) {
    return Array.from({ length: count }, (_, index) => `<div class="task-row"><span class="number">${index + 1}</span><input class="text-input" id="${prefix}-${index + 1}" aria-label="${label} ${index + 1}" placeholder="${label} ${index + 1}"></div>`).join('');
  }

  function renderFreeTools() {
    mountLayout('free-tools', `
      <main><section class="hero"><div class="library-shell hero-grid"><div><span class="eyebrow">Free tools</span><h1>One clear next step.</h1><p class="lead">Private, browser-local tools to help you decide where to begin, plan a day, review a week, or organize the essentials you want to see.</p></div><aside class="hero-note"><strong>Your inputs stay local</strong><p>These Phase 1 tools do not send reflection text or financial figures to NORTH or analytics. Print only if you choose to.</p></aside></div></section>
      <section class="section paper"><div class="library-shell"><div class="tool-stack">
        <article class="tool" id="snapshot"><div class="tool-header"><div><span class="eyebrow">2-minute check-in</span><h2>Find Your North Snapshot</h2><p>Which area deserves your attention first? Choose one private starting point, then get a practical next move.</p></div></div>
          <form id="snapshotForm"><fieldset><legend>What feels most pressing right now?</legend><div class="choice-grid">
            <label class="choice"><input type="radio" name="north-area" value="focus"><span class="choice-mark">1</span><span><strong>Focus</strong><br>Too much competing for attention.</span></label>
            <label class="choice"><input type="radio" name="north-area" value="direction"><span class="choice-mark">2</span><span><strong>Direction</strong><br>Not sure what matters most next.</span></label>
            <label class="choice"><input type="radio" name="north-area" value="money"><span class="choice-mark">3</span><span><strong>Money organization</strong><br>Want a calmer picture of the essentials.</span></label>
            <label class="choice"><input type="radio" name="north-area" value="routine"><span class="choice-mark">4</span><span><strong>Routine</strong><br>Need a more intentional rhythm.</span></label>
          </div></fieldset><div class="tool-controls"><button class="button" type="submit">Show my next step</button></div></form><div class="tool-result" id="snapshotResult" aria-live="polite"></div>
        </article>
        <article class="tool" id="daily-page"><div class="tool-header"><div><span class="eyebrow">Daily planning</span><h2>1-3-5 Daily Page</h2><p>Make today smaller: one priority, three supporting tasks, and five quick wins.</p></div></div>
          <div class="planner-grid print-target" id="dailyPrint"><div class="planner-block"><h3>One Big Thing</h3><input class="text-input" aria-label="One Big Thing" placeholder="The one task that would make today meaningful"></div><div class="planner-block"><h3>Three supporting tasks</h3>${dailyRows('medium', 3, 'Supporting task')}</div><div class="planner-block"><h3>Five quick wins</h3>${dailyRows('quick', 5, 'Quick win')}</div></div>
          <div class="tool-controls"><button class="button print" type="button" data-print-target="dailyPrint">Print my Daily Page</button><button class="button secondary" type="button" data-clear-target="daily-page">Clear my Daily Page</button><a class="button secondary" href="/library/free-tools#daily-page">Stay with the Daily Page</a></div>
        </article>
        <article class="tool" id="weekly-compass"><div class="tool-header"><div><span class="eyebrow">Weekly reset</span><h2>Weekly Compass Preview</h2><p>A quiet ten-minute pause for noting what worked, what felt difficult, and what you want to bring into the next week.</p></div></div>
          <div class="reflection-grid print-target" id="compassPrint"><div><label for="compass-win">One thing that moved forward</label><textarea class="text-area" id="compass-win" placeholder="A win, a lesson, or a moment worth noticing"></textarea></div><div><label for="compass-friction">One source of friction</label><textarea class="text-area" id="compass-friction" placeholder="What made the week harder than it needed to be?"></textarea></div><div><label for="compass-next">One intention for next week</label><textarea class="text-area" id="compass-next" placeholder="A simple direction—not a promise of perfection"></textarea></div></div>
          <div class="tool-controls"><button class="button print" type="button" data-print-target="compassPrint">Print my Weekly Compass</button><button class="button secondary" type="button" data-clear-target="weekly-compass">Clear my Weekly Compass</button><a class="button secondary" href="/library/free-tools#weekly-compass">Stay with the Weekly Compass</a></div>
        </article>
        <article class="tool" id="safe-number"><div class="tool-header"><div><span class="eyebrow">Money organization</span><h2>Safe Number Starter Sheet</h2><p>Make a private list of recurring essentials you want to review. The total is only the sum of figures you enter—it is not advice, a forecast, or a recommendation.</p></div></div>
          <div class="notice money"><strong>General education and organization only.</strong> This sheet does not provide financial, tax, investment, credit, lending, insurance, legal, or debt advice. For advice tailored to you, speak with a qualified professional.</div>
          <div class="expense-grid print-target" id="safeNumberPrint" style="margin-top:18px;">${['Housing', 'Utilities', 'Food', 'Transportation', 'Health', 'Insurance', 'Debt minimums', 'Other essentials'].map((item) => `<div class="expense-row"><label for="expense-${item.toLowerCase().replace(/[^a-z]+/g, '-')}">${item}</label><input class="money-input expense-input" id="expense-${item.toLowerCase().replace(/[^a-z]+/g, '-')}" inputmode="decimal" type="number" min="0" step="0.01" placeholder="0.00" aria-label="${item} monthly amount"></div>`).join('')}</div>
          <div class="total-box"><span>Entered monthly total</span><strong id="expenseTotal">$0.00</strong></div><div class="tool-controls"><button class="button print" type="button" data-print-target="safeNumberPrint">Print my Starter Sheet</button><button class="button secondary" type="button" data-clear-target="safe-number">Clear my Starter Sheet</button><a class="button secondary" href="/library/free-tools#safe-number">Stay with the Starter Sheet</a></div>
        </article>
      </div></div></section></main>`);

    northTrack('library_view', { route: '/library/free-tools', category: 'free-tools' });
    let started = new Set();
    document.querySelectorAll('.tool input, .tool textarea').forEach((input) => input.addEventListener('focus', (event) => {
      const tool = event.target.closest('.tool');
      if (!tool || started.has(tool.id)) return;
      started.add(tool.id);
      northTrack('free_tool_start', { tool_slug: tool.id, route: '/library/free-tools' });
    }, { once: false }));

    const snapshotForm = document.getElementById('snapshotForm');
    snapshotForm.addEventListener('submit', (event) => {
      event.preventDefault();
      const selection = document.querySelector('input[name="north-area"]:checked');
      const result = document.getElementById('snapshotResult');
      if (!selection) { result.innerHTML = '<p><strong>Choose one area first.</strong> Your selection stays in this browser session.</p>'; result.classList.add('show'); return; }
      const paths = {
        focus: ['Start smaller: choose one Big Thing, then use the 1-3-5 Daily Page to protect attention around it.', '/library/free-tools#daily-page', 'Open the Daily Page'],
        direction: ['Give yourself a short weekly pause. Use the Weekly Compass Preview to name what is moving and what matters next.', '/library/free-tools#weekly-compass', 'Open the Weekly Compass'],
        money: ['Begin by organizing the essentials you want to see. The Safe Number Starter Sheet is private and educational—not advice.', '/library/free-tools#safe-number', 'Open the Starter Sheet'],
        routine: ['Use one day as a reset. The 1-3-5 Daily Page gives you a realistic structure without trying to rebuild everything at once.', '/library/free-tools#daily-page', 'Open the Daily Page']
      };
      const [copy, href, label] = paths[selection.value];
      result.innerHTML = `<p><strong>Your next step</strong></p><p>${copy}</p><div class="tool-controls"><a class="button secondary" href="${href}" data-recommendation="${selection.value}">${label}</a><button class="button secondary" type="button" data-snapshot-reset>Start again</button></div>`;
      result.classList.add('show');
      northTrack('free_tool_complete', { tool_slug: 'find-your-north-snapshot', route: '/library/free-tools' });
      result.querySelector('[data-recommendation]').addEventListener('click', () => northTrack('free_tool_recommendation', { tool_slug: 'find-your-north-snapshot', recommendation_slug: selection.value }));
      result.querySelector('[data-snapshot-reset]').addEventListener('click', () => {
        snapshotForm.reset();
        result.classList.remove('show');
        result.replaceChildren();
        snapshotForm.querySelector('input[name="north-area"]').focus();
      });
    });

    document.querySelectorAll('[data-print-target]').forEach((button) => button.addEventListener('click', () => {
      document.querySelectorAll('.tool').forEach((tool) => tool.classList.remove('print-target'));
      button.closest('.tool').classList.add('print-target');
      const toolSlug = button.closest('.tool').id;
      northTrack('free_tool_complete', { tool_slug: toolSlug, route: '/library/free-tools' });
      window.print();
    }));
    document.querySelectorAll('[data-clear-target]').forEach((button) => button.addEventListener('click', () => {
      const tool = document.getElementById(button.dataset.clearTarget);
      tool.querySelectorAll('input, textarea').forEach((field) => {
        field.value = '';
        field.dispatchEvent(new Event('input', { bubbles: true }));
      });
      const firstField = tool.querySelector('input, textarea');
      if (firstField) firstField.focus();
    }));
    document.querySelectorAll('.expense-input').forEach((input) => input.addEventListener('input', () => {
      const total = Array.from(document.querySelectorAll('.expense-input')).reduce((sum, item) => sum + (Number.parseFloat(item.value) || 0), 0);
      document.getElementById('expenseTotal').textContent = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(total);
    }));
  }

  function renderItem() {
    const slug = new URLSearchParams(window.location.search).get('product');
    const product = NORTH.products[slug];
    if (!product) {
      mountLayout('library', `<main class="template"><div class="library-shell"><p class="breadcrumb"><a href="/library">Library</a> / Item</p><h1>That Library item is not available.</h1><p class="lead">Return to the Library to choose an available free tool.</p><a class="button" href="/library">Return to Library</a></div></main>`);
      return;
    }
    const available = product.availability === 'available';
    const preview = available
      ? `<div class="preview-panel"><strong>Preview</strong><p>This is an honest preview of the live experience. Open the browser-local tool to use it—no account, email, or purchase required.</p><a class="button secondary" href="${product.action.href}">${esc(product.action.label)}</a></div>`
      : `<div class="preview-panel"><strong>Not available in this candidate</strong><p>This public candidate includes only the verified Free Tools and public-safe Release A overview routes.</p></div>`;
    const availability = available && product.action
      ? `<a class="button" href="${product.action.href}" data-tool-start="${esc(product.slug)}">${esc(product.action.label)}</a>`
      : `<span class="button muted" aria-disabled="true">Not available in Phase 1</span>`;
    mountLayout('library', `
      <main class="template"><div class="library-shell"><p class="breadcrumb"><a href="/library">Library</a> / <a href="/library/${product.category}">${esc(product.category.replace('-', ' '))}</a> / ${esc(product.title)}</p><div class="template-grid"><div class="template-main"><span class="eyebrow">${esc(product.type)} · ${available ? 'Available now' : 'Coming soon'}</span><h1>${esc(product.outcome)}</h1><p class="summary">${esc(product.summary)}</p>
        <section class="template-section"><div class="detail-pair"><article class="detail-card"><h3>For</h3><p>${esc(product.audience)}</p></article><article class="detail-card"><h3>Not for</h3><p>${esc(product.notFor)}</p></article></div></section>
        <section class="template-section"><h2>What is included</h2><ul class="content-list">${product.contents.map((item) => `<li>${esc(item)}</li>`).join('')}</ul></section>
        <section class="template-section"><h2>Access and time</h2><div class="detail-pair"><article class="detail-card"><h3>Access</h3><p>${esc(product.access)}</p></article><article class="detail-card"><h3>Time</h3><p>${esc(product.time)}</p></article></div></section>
        <section class="template-section">${preview}</section>
        ${product.moneyEducation ? '<section class="template-section"><div class="notice money"><strong>Scope notice.</strong> This is a general education and organization tool only. It is not individualized financial, tax, investment, credit, lending, insurance, legal, or debt advice.</div></section>' : ''}
        <section class="template-section faq"><h2>Questions</h2>${product.faq.map(([question, answer]) => `<details><summary>${esc(question)}</summary><p>${esc(answer)}</p></details>`).join('')}</section>
        ${product.appCTA ? `<section class="template-section"><h2>Use NORTH daily</h2><p class="lead">The app is optional. If you want a daily implementation layer after using this tool, explore NORTH on the App Store.</p><a class="button secondary" href="${NORTH.brand.appStoreUrl}" target="_blank" rel="noopener" data-app-store-source="product-${esc(product.slug)}">View NORTH on the App Store ↗</a></section>` : ''}
      </div><aside class="template-aside"><span class="status ${available ? 'available' : 'coming-soon'}">${available ? 'Available now' : 'Coming soon'}</span><h2>${esc(product.title)}</h2><p>${available ? 'Use this browser-local tool now. It is free and does not require a checkout.' : 'This item is not available for purchase, preorder, delivery, or waitlist enrollment.'}</p>${availability}</aside></div></div></main>`);
    northTrack('product_page_view', { product_slug: product.slug, availability: product.availability });
    document.querySelectorAll('[data-tool-start]').forEach((link) => link.addEventListener('click', () => northTrack('free_tool_start', { tool_slug: link.dataset.toolStart, route: window.location.pathname })));
  }

  window.NORTH_LIBRARY = {
    renderIndex,
    renderCategory,
    renderFreeTools,
    renderItem,
    northTrack,
    trackAppStore
  };
})(window, document);
