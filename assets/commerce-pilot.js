(function (window, document) {
  'use strict';

  const P = Object.freeze({
    state: 'FOUNDER_REVIEW',
    commerceEnabled: false,
    merchantProduct: null,
    checkoutUrl: null,
    deliveryEnabled: false,
    title: 'NORTH 1-3-5 Execution Planner',
    version: 'Core Digital Edition candidate · v1.0 · English source',
    subtitle: 'Two weeks. One clear direction.',
    proofPages: [
      { src: '/assets/product-proof/planner-start-here-us-letter.png', label: 'Start Here', alt: 'Actual US Letter Planner proof page showing the 1-3-5 method and under-ten-minutes use guidance.', detail: 'Method, scope boundary, and a practical first use.' },
      { src: '/assets/product-proof/planner-two-week-intention-us-letter.png', label: 'Two-Week Intention', alt: 'Actual US Letter Planner proof page showing cycle dates, an outcome, boundaries, evidence, and a starting point.', detail: 'One real way the two-week cycle begins.' },
      { src: '/assets/product-proof/planner-daily-page-us-letter.png', label: 'Day 1 daily page', alt: 'Actual US Letter Planner proof page showing One Big Thing, three medium tasks, five small wins, and a realistic focus block.', detail: 'The actual daily 1-3-5 field structure.' },
      { src: '/assets/product-proof/planner-final-review-us-letter.png', label: 'Final review and continuation', alt: 'Actual US Letter Planner proof page showing whole-cycle reflection and a next starting point.', detail: 'A real final review and continuation page.' }
    ],
    received: [
      { title: 'Start Here method', text: 'A short orientation explaining the 1-3-5 rhythm and a source-supported way to begin in under ten minutes.' },
      { title: 'One Two-Week Intention', text: 'A cycle page for an outcome, realistic boundaries, evidence, and a first visible action.' },
      { title: 'Fourteen daily pages', text: 'Each day uses a Big Thing, three supporting actions, five small wins, a focus block, obstacle response, and reflection.' },
      { title: 'Two reset / review pages', text: 'The source includes two weekly reset and review pages for looking at what is helping, creating friction, or worth carrying forward.' },
      { title: 'Continuation plan', text: 'A final review helps identify what to continue, change, leave behind, and begin next.' },
      { title: 'Fictional worked example', text: 'One clearly labelled example shows a bounded documentation-reset cycle; it is not a customer outcome or case study.' }
    ],
    useSteps: [
      'Read the two-week intention before selecting today’s work.',
      'Name one Big Thing with a visible definition of done.',
      'Add no more than three supporting actions and up to five smaller wins.',
      'Reserve one realistic focus block, name a likely obstacle, and choose one usable response.',
      'Write one sentence of evidence and leave tomorrow a clearer starting point.'
    ],
    dependencies: [
      'Founder approval of final buyer-visible files, proof sequence, visual direction, and offer decision.',
      'Qualified legal review of personal-use license, support/refund, privacy, seller, and consumer disclosures.',
      'Final purchaser-file readability, print, tagged-PDF, and any later fillable-field accessibility QA.',
      'Merchant-of-record, tax, payment, delivery, re-delivery, confirmation, and support operating decisions.',
      'Controlled end-to-end test before any customer order, receipt, delivery, or access is allowed.',
      'Separate human review of every non-English product edition before a locale can be called available.'
    ]
  });

  const e = (value) => String(value).replace(/[&<>"']/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' }[char]));
  const actualProofLabel = 'Actual Planner-page proof — private founder-review source.';
  const illustrativeLabel = 'Illustrative digital product mockup — not a physical product photograph.';

  function proofCard(page) {
    return `<figure class="proof-card"><div class="proof-image-frame"><img src="${page.src}" alt="${e(page.alt)}" loading="lazy" width="1275" height="1650"></div><figcaption><strong>${e(page.label)}</strong><span>${e(page.detail)}</span><em>${actualProofLabel}</em></figcaption></figure>`;
  }

  function render() {
    const app = document.getElementById('commercePilotApp');
    if (!app) return;

    app.innerHTML = `
      <div class="commerce-pilot">
        <div class="pilot-banner">Founder review only · no checkout, payment, delivery, download, email capture, or public price</div>
        <header class="pilot-header">
          <div class="pilot-shell pilot-header-inner">
            <a class="pilot-brand" href="/" aria-label="NORTH private candidate home"><img src="/assets/brand/north-compass-official-512.png" width="28" height="28" alt="Official NORTH compass icon"><span>NORTH</span></a>
            <nav class="pilot-private-nav" aria-label="Private founder review navigation"><a href="/library/item?product=1-3-5-execution-planner">Public-safe Library overview <span aria-hidden="true">→</span></a><a href="/internal/phase2g-product-truth.html">Product truth &amp; launch gates <span aria-hidden="true">→</span></a></nav>
          </div>
        </header>
        <main id="main-content">
          <section class="pilot-hero" aria-labelledby="planner-title">
            <div class="pilot-shell pilot-hero-grid">
              <div class="pilot-hero-copy">
                <p class="pilot-eyebrow">Release A / flagship proof product / English source</p>
                <h1 id="planner-title">${e(P.title)}</h1>
                <p class="pilot-lead">${e(P.subtitle)} A private, self-guided two-week planning rhythm for one meaningful priority, three supporting actions, and five small wins.</p>
                <p class="pilot-version">${e(P.version)}</p>
                <div class="pilot-hero-status"><strong>Private founder-review candidate.</strong><span>No person can purchase, pay for, receive, download, or request this Planner from this page.</span></div>
              </div>
              <figure class="hero-proof-card">
                <img src="/assets/product-proof/planner-daily-page-us-letter.png" alt="Actual US Letter Planner proof page showing One Big Thing, three medium tasks, five small wins, and a realistic focus block." fetchpriority="high" width="1275" height="1650">
                <figcaption><strong>Real daily-page proof</strong><span>${actualProofLabel}</span></figcaption>
              </figure>
            </div>
          </section>

          <section class="pilot-section proof-intro" aria-labelledby="what-receive-title">
            <div class="pilot-shell">
              <div class="pilot-heading proof-heading"><div><p class="pilot-eyebrow">What you receive — future English bundle</p><h2 id="what-receive-title">A defined digital product, not a promise in a box.</h2></div><p>The proposed Core Digital Edition is a digital PDF bundle only. It is not a hardcover, shipped kit, app subscription, course, coaching service, or editable-template license.</p></div>
              <div class="buyer-facts" role="list">
                <article role="listitem"><strong>Language</strong><span>English private candidate only</span></article>
                <article role="listitem"><strong>Proposed formats</strong><span>US Letter PDF and A4 PDF</span></article>
                <article role="listitem"><strong>Private proof</strong><span>31-page US Letter and 27-page A4 review proofs</span></article>
                <article role="listitem"><strong>Editable source</strong><span>Retained privately; not part of the proposed buyer bundle</span></article>
              </div>
              <div class="receive-grid">${P.received.map((item, index) => `<article class="receive-card"><span>${String(index + 1).padStart(2, '0')}</span><h3>${e(item.title)}</h3><p>${e(item.text)}</p></article>`).join('')}</div>
            </div>
          </section>

          <section class="pilot-section alt proof-section" aria-labelledby="inside-title">
            <div class="pilot-shell">
              <div class="pilot-heading"><p class="pilot-eyebrow">Real product evidence</p><h2 id="inside-title">See what is inside from the actual Planner source.</h2><p>These are direct exports from the approved private US Letter proof. They are used to show actual structure and readability; they are not customer download links.</p></div>
              <div class="proof-grid">${P.proofPages.map(proofCard).join('')}</div>
            </div>
          </section>

          <section class="pilot-section" aria-labelledby="use-title">
            <div class="pilot-shell two-column-callout">
              <div class="pilot-heading"><p class="pilot-eyebrow">How it is used</p><h2 id="use-title">A useful start in under ten minutes.</h2><p>The real Start Here page explains a bounded way to begin. It is planning guidance, not a guarantee or professional advice.</p></div>
              <ol class="use-steps">${P.useSteps.map((step, index) => `<li><span>${String(index + 1).padStart(2, '0')}</span><p>${e(step)}</p></li>`).join('')}</ol>
            </div>
          </section>

          <section class="pilot-section alt print-section" aria-labelledby="print-title">
            <div class="pilot-shell print-grid">
              <div class="pilot-heading"><p class="pilot-eyebrow">Print proof</p><h2 id="print-title">US Letter and A4 evidence exists for review.</h2><p>Two private proof files exist: a 31-page US Letter PDF and a 27-page A4 PDF. They are review evidence, not customer delivery files, and they do not establish a tagged or fillable purchaser PDF.</p><div class="proof-boundary"><strong>Current accessibility boundary</strong><span>The current proofs are not tagged and have no PDF form fields. Tagged-PDF, assistive-technology, print, and any future fillable-field QA remain release blockers.</span></div></div>
              <figure class="a4-proof-card"><img src="/assets/product-proof/planner-start-here-a4.png" alt="Actual A4 private print-proof page showing the Start Here method and product boundary." loading="lazy" width="1240" height="1754"><figcaption><strong>Actual A4 private print-proof page</strong><span>Not a customer delivery file.</span></figcaption></figure>
            </div>
          </section>

          <section class="pilot-section boundaries-section" aria-labelledby="boundary-title">
            <div class="pilot-shell boundary-grid">
              <div><p class="pilot-eyebrow">Boundaries</p><h2 id="boundary-title">A self-guided planning tool, with clear limits.</h2></div>
              <div class="boundary-copy"><p>For adults who want a short, repeatable planning and reflection structure. It can stand alone on paper or screen; no app account is required by the current source.</p><p>It is not medical, mental-health, clinical, financial, tax, legal, investment, employment, or other individualized professional advice. It does not diagnose, treat, or guarantee a result.</p><p>Personal-use licensing, support, refund, privacy, consumer, and seller language remain draft material pending qualified review.</p></div>
            </div>
          </section>

          <section class="pilot-section editorial-section" aria-labelledby="editorial-title">
            <div class="pilot-shell editorial-grid">
              <div class="pilot-heading"><p class="pilot-eyebrow">Editorial atmosphere</p><h2 id="editorial-title">One calm visual, clearly separated from proof.</h2><p>Presentation imagery can express the NORTH mood, but it cannot prove a shipped object, a buyer result, a page, or a feature.</p></div>
              <figure class="editorial-figure"><img src="/assets/product-presentation/web/planner-hero-illustrative.webp" alt="Illustrative digital product mockup of the NORTH 1-3-5 Execution Planner on a warm refined desk." loading="lazy" width="2200" height="1228"><figcaption><strong>${illustrativeLabel}</strong><span>The actual product proof appears in the PDF-page sections above.</span></figcaption></figure>
            </div>
          </section>

          <section class="pilot-section alt" aria-labelledby="readiness-title">
            <div class="pilot-shell">
              <div class="pilot-heading"><p class="pilot-eyebrow">Release gate</p><h2 id="readiness-title">What must be real before any sale is considered.</h2><p>The future operating path is documented for founder evaluation. It is not an active customer journey.</p></div>
              <div class="gate-list">${P.dependencies.map((dependency, index) => `<article><span>${String(index + 1).padStart(2, '0')}</span><p>${e(dependency)}</p></article>`).join('')}</div>
              <div class="gate-panel"><strong>Commerce remains disabled.</strong><p>There is no merchant product, checkout URL, payment connection, customer account, order confirmation, delivery link, email capture, public price, customer download, affiliate link, or tracking integration on this private candidate.</p></div>
            </div>
          </section>
        </main>
        <footer class="pilot-footer"><div class="pilot-shell">Private Phase 2G flagship buyer-proof review. <a href="/library">Return to the NORTH Library</a></div></footer>
      </div>`;
  }

  window.NORTH_COMMERCE_PILOT = Object.freeze({ product: P, render });
})(window, document);
