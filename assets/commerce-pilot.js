(function(window,document){
  'use strict';
  const P=Object.freeze({
    state:'FOUNDER_REVIEW', commerceEnabled:false, merchantProduct:null, checkoutUrl:null, deliveryEnabled:false,
    title:'1-3-5 Execution Planner', subtitle:'Two weeks. One clear direction.',
    includes:[
      'Complete 14-day English planner rhythm',
      'Two weekly reset / review pages',
      'Final two-week continuation plan',
      'Fictional worked example',
      'US Letter and A4 private print proofs',
      'Editable English master for founder review'
    ],
    options:[
      {name:'Core Digital Edition',price:'$19 USD',note:'Founder-selected first pilot candidate. English PDFs only; no merchant, checkout, payment, delivery, or public price is configured.'},
      {name:'Planner + Editable Source',price:'Deferred',note:'Future founder decision only. Editable source is excluded from the first Core Digital purchaser bundle pending demand, licensing, support, and format-compatibility evidence.'}
    ],
    readiness:{
      website:'English product page complete for review',
      product:'English master and private print proofs complete for review',
      checkout:'Not designed as an active customer flow',
      delivery:'No customer delivery configured',
      support:'Draft policy only; no operating support promise',
      legal:'Drafts require qualified legal review'
    },
    visuals:[
      {src:'/assets/product-presentation/web/planner-morning-desk-illustrative.webp',alt:'Illustrative calm morning desk scene for the NORTH 1-3-5 Execution Planner.',label:'Morning orientation'},
      {src:'/assets/product-presentation/web/planner-weekly-reset-illustrative.webp',alt:'Illustrative weekly reset desk scene for the NORTH 1-3-5 Execution Planner.',label:'Weekly reset'},
      {src:'/assets/product-presentation/web/planner-two-week-rhythm-illustrative.webp',alt:'Illustrative digital product presentation for beginning a two-week Planner rhythm.',label:'Two-week rhythm'},
      {src:'/assets/product-presentation/web/planner-weekly-review-illustrative.webp',alt:'Illustrative digital product presentation for a Planner weekly review.',label:'Weekly review'}
    ],
    dependencies:[
      'Founder approval of final content, cover, previews, and option to test',
      'Qualified legal review of license, support/refund, privacy, consumer and tax disclosures',
      'Merchant selection and approved merchant-product setup',
      'Approved pricing, tax treatment, refund configuration, and buyer jurisdiction plan',
      'Secure delivery method, download-expiry/re-delivery procedure, and buyer-access test',
      'Transactional confirmation content, support inbox, escalation process, and analytics/privacy review',
      'Accessibility review of tagged/screen-fillable PDFs and human-reviewed language plan'
    ]
  });

  const e=(v)=>String(v).replace(/[&<>"']/g,(c)=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]));
  const illustrativeLabel='Illustrative digital product mockup — not a physical product photograph.';

  function render(){
    const app=document.getElementById('commercePilotApp');
    if(!app)return;
    app.innerHTML=`
      <div class="commerce-pilot">
        <div class="pilot-banner">Founder review draft — not for sale · checkout, payment, delivery, and download disabled</div>
        <header class="pilot-header">
          <div class="pilot-shell">
            <div class="pilot-brand"><img src="/assets/brand/north-compass-official-512.png" width="28" height="28" alt="Official NORTH compass icon">NORTH</div>
            <a href="/library/item?product=1-3-5-execution-planner">View public-safe Library overview →</a>
          </div>
        </header>
        <main>
          <section class="pilot-hero">
            <div class="pilot-shell pilot-grid">
              <div class="pilot-hero-copy">
                <p class="pilot-eyebrow">Release A / Private product presentation / English source</p>
                <h1>${e(P.title)}</h1>
                <p class="pilot-lead">${e(P.subtitle)} A calm, two-week planning system for making one meaningful priority, three supports, and five useful small wins visible without turning your day into a verdict.</p>
                <p class="pilot-hero-status"><strong>Private review only.</strong> This page shows the founder-ready content direction and visual system. No product can be purchased, paid for, received, or downloaded.</p>
              </div>
              <figure class="pilot-hero-media">
                <img src="/assets/product-presentation/web/planner-hero-illustrative.webp" width="2200" height="1228" alt="Illustrative digital product mockup of the NORTH 1-3-5 Execution Planner on a warm refined desk." fetchpriority="high">
                <figcaption><span>${illustrativeLabel}</span> The actual offer under review is a digital Planner; this image communicates visual direction only.</figcaption>
              </figure>
            </div>
          </section>

          <section class="pilot-section">
            <div class="pilot-shell">
              <div class="pilot-heading">
                <p class="pilot-eyebrow">Future English package</p>
                <h2>Complete source. Clear boundaries. Still private.</h2>
                <p>The Planner content, visual direction, print-review files, policy drafts, and future commerce path are ready for founder inspection. No person can purchase, pay for, receive, or download this package.</p>
              </div>
              <div class="pilot-columns">${P.includes.map((x,i)=>`<article class="pilot-card"><h3>${String(i+1).padStart(2,'0')} · Included for review</h3><p>${e(x)}</p></article>`).join('')}</div>
            </div>
          </section>

          <section class="pilot-section alt">
            <div class="pilot-shell">
              <div class="pilot-heading">
                <p class="pilot-eyebrow">Real Planner-page detail</p>
                <h2>Designed to make the next useful step visible.</h2>
                <p>These are actual private Planner-page details. They are the only source used to represent the Planner’s real content structure and writable fields.</p>
              </div>
              <div class="pilot-preview-grid">
                <figure><img src="/assets/product-visuals/execution-planner-open-spread.png" alt="Actual Planner detail showing blank priority and reflection structures"><figcaption>Actual Planner-page detail — private review source.</figcaption></figure>
                <figure><img src="/assets/product-visuals/execution-planner-detail.png" alt="Actual Planner detail showing blank writable fields"><figcaption>Actual Planner-page detail — private review source.</figcaption></figure>
              </div>
            </div>
          </section>

          <section class="pilot-section presentation-section">
            <div class="pilot-shell">
              <div class="pilot-heading">
                <p class="pilot-eyebrow">Premium visual presentation</p>
                <h2>Quiet structure for a useful rhythm.</h2>
                <p>This editorial sequence is deliberately separate from real page evidence. It is designed to express focus, recovery, and review without inventing a physical product, a customer outcome, or a feature.</p>
              </div>
              <div class="pilot-presentation-grid">
                ${P.visuals.map((visual,index)=>`<figure class="pilot-presentation-card pilot-presentation-card-${index+1}"><img src="${visual.src}" alt="${e(visual.alt)}" loading="lazy" width="1600" height="893"><figcaption><strong>${e(visual.label)}</strong><span>${illustrativeLabel}</span></figcaption></figure>`).join('')}
              </div>
              <p class="pilot-disclosure">All generated imagery on this page is clearly labeled as illustrative. No image is a representation of an actual downloadable page, shipped product, customer, testimonial, purchase flow, or result.</p>
            </div>
          </section>

          <section class="pilot-section">
            <div class="pilot-shell">
              <div class="pilot-heading"><p class="pilot-eyebrow">What the planner contains</p><h2>A humane two-week rhythm.</h2></div>
              <ul class="pilot-list">
                <li>Start Here guidance that makes the 1-3-5 method clear in under ten minutes.</li>
                <li>One two-week intention page with boundaries, evidence, and a first visible action.</li>
                <li>Fourteen distinct daily pages, each with a Big Thing, three supporting tasks, five small wins, realistic focus block, obstacle response, and short reflection.</li>
                <li>Two reset/review pages plus a final continuation plan that use evidence rather than a score.</li>
                <li>A fictional operational example showing a bounded documentation-reset cycle.</li>
              </ul>
            </div>
          </section>

          <section class="pilot-section alt">
            <div class="pilot-shell">
              <div class="pilot-heading"><p class="pilot-eyebrow">Future commercial architecture</p><h2>Mapped, but intentionally inactive.</h2><p>The future flow is documented so the founder can evaluate it before any merchant setup. These are not checkout buttons or customer actions.</p></div>
              <div class="inactive-architecture">
                <article class="architecture-step"><span>01 · FUTURE</span><h3>Product page</h3><p>Final content, price, language, license, and policy disclosure only after approval.</p></article>
                <article class="architecture-step"><span>02 · FUTURE</span><h3>Checkout</h3><p>Merchant-hosted payment only after merchant, tax, policy, and consumer-rights review.</p></article>
                <article class="architecture-step"><span>03 · FUTURE</span><h3>Confirmation</h3><p>Transaction details, support path, and delivery instructions only after operational test.</p></article>
                <article class="architecture-step"><span>04 · FUTURE</span><h3>Delivery</h3><p>Secure buyer access and re-delivery process only after privacy and fulfillment approval.</p></article>
              </div>
            </div>
          </section>

          <section class="pilot-section">
            <div class="pilot-shell">
              <div class="pilot-heading"><p class="pilot-eyebrow">Proposed options — founder decision only</p><h2>Choose the pilot shape before the merchant.</h2><p>These are proposed prices for evaluation, not displayed publicly and not connected to payment, checkout, or a product listing.</p></div>
              <div class="pilot-pricing">${P.options.map(o=>`<article class="price-option"><h3>${e(o.name)}</h3><div class="price">${e(o.price)}</div><small>${e(o.note)}</small><button class="pilot-button-disabled" disabled aria-disabled="true">Pending founder approval — no checkout</button></article>`).join('')}</div>
            </div>
          </section>

          <section class="pilot-section alt">
            <div class="pilot-shell">
              <div class="pilot-heading"><p class="pilot-eyebrow">Customer-readiness status</p><h2>Each layer must be real before it can be sold.</h2></div>
              <table class="readiness-table"><thead><tr><th>Layer</th><th>Phase 2F status</th></tr></thead><tbody>${Object.entries(P.readiness).map(([k,v])=>`<tr><td>${e(k.charAt(0).toUpperCase()+k.slice(1))}</td><td>${e(v)}</td></tr>`).join('')}</tbody></table>
            </div>
          </section>

          <section class="pilot-section">
            <div class="pilot-shell"><div class="gate-panel"><strong>Sale gate remains closed.</strong><p>Commerce is disabled in the product configuration. There is no merchant product, checkout URL, payment connection, customer account, order confirmation, delivery link, email capture, or customer download. The next step is founder approval of the product and pilot structure—not activation.</p></div></div>
          </section>
        </main>
        <footer class="pilot-footer"><div class="pilot-shell">Private Phase 2F product-presentation review. <a href="/library">Return to the NORTH Library</a></div></footer>
      </div>`;
  }
  window.NORTH_COMMERCE_PILOT=Object.freeze({product:P,render});
})(window,document);
