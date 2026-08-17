/* NORTH Phase 1 public content registry.
 * This is the only source of truth for Library product state, delivery readiness,
 * public language availability, verified app link, and anonymous analytics events.
 */
(function (window) {
  'use strict';

  const APP_STORE_URL = 'https://apps.apple.com/us/app/north-find-your-north/id6757988392';

  const languageRegistry = [
    { code: 'en', name: 'English', publicWeb: true, productDelivery: true, rtl: false },
    { code: 'pt-BR', name: 'Brazilian Portuguese', publicWeb: false, productDelivery: false, rtl: false },
    { code: 'es-419', name: 'Latin-American Spanish', publicWeb: false, productDelivery: false, rtl: false },
    { code: 'fr', name: 'French', publicWeb: false, productDelivery: false, rtl: false },
    { code: 'de', name: 'German', publicWeb: false, productDelivery: false, rtl: false },
    { code: 'it', name: 'Italian', publicWeb: false, productDelivery: false, rtl: false },
    { code: 'ja', name: 'Japanese', publicWeb: false, productDelivery: false, rtl: false },
    { code: 'ko', name: 'Korean', publicWeb: false, productDelivery: false, rtl: false },
    { code: 'zh-Hans', name: 'Chinese (Simplified)', publicWeb: false, productDelivery: false, rtl: false },
    { code: 'zh-Hant', name: 'Chinese (Traditional)', publicWeb: false, productDelivery: false, rtl: false },
    { code: 'ar', name: 'Arabic', publicWeb: false, productDelivery: false, rtl: true },
    { code: 'ru', name: 'Russian', publicWeb: false, productDelivery: false, rtl: false },
    { code: 'pl', name: 'Polish', publicWeb: false, productDelivery: false, rtl: false },
    { code: 'nl', name: 'Dutch', publicWeb: false, productDelivery: false, rtl: false }
  ];

  const products = {
    'find-your-north-snapshot': {
      slug: 'find-your-north-snapshot',
      title: 'Find Your North Snapshot',
      category: 'free-tools',
      type: 'Free tool',
      availability: 'available',
      outcome: 'Identify one place to begin, without trying to solve everything at once.',
      summary: 'A short private check-in that helps you name the NORTH area that feels most pressing right now.',
      audience: 'For anyone who wants a clearer first step around focus, direction, money organization, or routine.',
      notFor: 'Not for crisis support, diagnosis, or personalized financial, medical, legal, or mental-health advice.',
      contents: ['Four private starting-point choices', 'One concise next-step prompt', 'A relevant free-tool or app path'],
      access: 'Use in any modern browser. Your choice stays in the current browser session.',
      time: 'About 2 minutes',
      action: { label: 'Start the snapshot', href: '/library/free-tools#snapshot', type: 'start' },
      faq: [
        ['Does NORTH receive my answer?', 'No. This Phase 1 tool keeps your choice in the current browser session and does not send your reflection to NORTH.'],
        ['Is this a diagnosis or coaching session?', 'No. It is a simple reflection prompt designed to help you choose a practical next step.'],
        ['Where can I get support?', 'For website questions, email hello@yournorth.app. For urgent mental-health support, contact a qualified local professional or emergency service.']
      ],
      appCTA: true,
      moneyEducation: false
    },
    '1-3-5-daily-page': {
      slug: '1-3-5-daily-page',
      title: '1-3-5 Daily Page',
      category: 'free-tools',
      type: 'Free tool',
      availability: 'available',
      outcome: 'Turn a busy day into one meaningful priority, three supporting tasks, and five small wins.',
      summary: 'A printable one-day planning page built around the NORTH 1-3-5 framework.',
      audience: 'For people who want a simple structure for planning one day at a time.',
      notFor: 'Not for project management, calendar scheduling, or a guarantee that every task will be completed.',
      contents: ['One Big Thing field', 'Three supporting task fields', 'Five quick-win fields', 'Local print layout'],
      access: 'Use and print from any modern browser. Your entries remain in your browser.',
      time: 'About 5 minutes',
      action: { label: 'Use the Daily Page', href: '/library/free-tools#daily-page', type: 'start' },
      faq: [
        ['Is there a download?', 'The page is ready to print from your browser. No account or email is required.'],
        ['Where is my plan stored?', 'It stays in your current browser page unless you choose to print it. Refreshing the page clears the entries.'],
        ['Is there a refund?', 'This is a free browser tool, so no purchase or refund applies.']
      ],
      appCTA: true,
      moneyEducation: false
    },
    'weekly-compass-preview': {
      slug: 'weekly-compass-preview',
      title: 'Weekly Compass Preview',
      category: 'free-tools',
      type: 'Free tool',
      availability: 'available',
      outcome: 'Make space for a ten-minute review before you set the next week in motion.',
      summary: 'A private weekly reflection page with practical questions for noticing progress, friction, and one intentional next move.',
      audience: 'For people who want a lightweight weekly reset without committing to a longer journal.',
      notFor: 'Not for therapy, performance scoring, or a promise of personal transformation.',
      contents: ['Three reflection prompts', 'One next-week intention field', 'Local print layout'],
      access: 'Use and print from any modern browser. Your writing remains in your browser.',
      time: 'About 10 minutes',
      action: { label: 'Open the Preview', href: '/library/free-tools#weekly-compass', type: 'start' },
      faq: [
        ['Does NORTH store my reflection?', 'No. Your reflection is not transmitted by this Phase 1 website tool.'],
        ['Can I use it every week?', 'Yes. You can return whenever you want a simple review structure.'],
        ['Is there a paid journal?', 'A longer Weekly Compass Journal is planned, but it is not available or for sale in Phase 1.']
      ],
      appCTA: true,
      moneyEducation: false
    },
    'safe-number-starter-sheet': {
      slug: 'safe-number-starter-sheet',
      title: 'Safe Number Starter Sheet',
      category: 'free-tools',
      type: 'Free tool',
      availability: 'available',
      outcome: 'Create a clear private list of essential monthly expenses and a basic monthly target.',
      summary: 'A browser-local organization sheet for seeing the household essentials you want to review—not a recommendation or financial plan.',
      audience: 'For adults who want a simple starting place to organize essential expenses.',
      notFor: 'Not for individualized financial, tax, investment, lending, credit, insurance, legal, or debt advice.',
      contents: ['Essential-expense categories', 'Optional monthly values', 'Local total for your own review', 'Plain-language scope reminder'],
      access: 'Use and print from any modern browser. Figures stay in your browser and are never sent in analytics.',
      time: 'About 10 minutes',
      action: { label: 'Open the Starter Sheet', href: '/library/free-tools#safe-number', type: 'start' },
      faq: [
        ['Does this tell me what I should spend or save?', 'No. It only helps organize the numbers you choose to enter.'],
        ['Does NORTH receive my figures?', 'No. This Phase 1 tool does not transmit entered financial values.'],
        ['Who should I contact for advice?', 'For advice tailored to your circumstances, speak with a qualified financial, tax, legal, or other relevant professional.']
      ],
      appCTA: true,
      moneyEducation: true
    },
    '1-3-5-execution-planner': {
      slug: '1-3-5-execution-planner',
      title: '1-3-5 Execution Planner',
      category: 'resources',
      type: 'Resource',
      availability: 'coming_soon',
      outcome: 'A structured 14-day planning companion is being prepared.',
      summary: 'Planned materials include a fillable/printable planner, a 14-day execution guide, and instructions.',
      audience: 'For people who want a longer planning structure after trying the free Daily Page.',
      notFor: 'Not currently available for purchase, delivery, or preorder.',
      contents: ['Fillable/printable planner — planned', '14-day execution guide — planned', 'Instructions — planned'],
      access: 'Not available. No completed delivery asset is connected to this website.',
      time: 'Planned 14-day use',
      action: null,
      faq: [
        ['Can I buy this now?', 'No. This item is not available for purchase, preorder, or delivery.'],
        ['What is included?', 'The planned contents are listed here for clarity only. NORTH will publish a final, exact list when the asset and delivery are complete.'],
        ['What can I use today?', 'Use the free 1-3-5 Daily Page instead.']
      ],
      appCTA: false,
      moneyEducation: false,
      purchaseRequirements: { completedAsset: false, deliveryReady: false, supportReady: false, refundPolicyReady: false, merchantOfRecordReady: false }
    },
    'decision-clarity-toolkit': {
      slug: 'decision-clarity-toolkit',
      title: 'Decision Clarity Toolkit',
      category: 'resources',
      type: 'Resource',
      availability: 'coming_soon',
      outcome: 'A practical set of decision prompts is being prepared.',
      summary: 'Planned materials include a NORTH Decision Filter, trade-off map, pre-mortem, and Captain’s Brief.',
      audience: 'For people facing a decision and seeking a structured reflection framework.',
      notFor: 'Not currently available for purchase, delivery, or preorder.',
      contents: ['Decision Filter — planned', 'Trade-off map — planned', 'Pre-mortem — planned', 'Captain’s Brief — planned'],
      access: 'Not available in Phase 1.',
      time: 'Not yet published',
      action: null,
      faq: [['Can I access it now?', 'No. This planned resource is not available or for sale in Phase 1.']],
      appCTA: false,
      moneyEducation: false
    },
    'weekly-compass-journal': {
      slug: 'weekly-compass-journal',
      title: 'Weekly Compass Journal',
      category: 'resources',
      type: 'Resource',
      availability: 'coming_soon',
      outcome: 'A longer weekly review journal is being prepared.',
      summary: 'The planned journal will include 52 weekly review/reset pages and progress reflections.',
      audience: 'For people who have tried the free Weekly Compass Preview and want a longer format later.',
      notFor: 'Not currently available for purchase, delivery, or preorder.',
      contents: ['52 weekly review/reset pages — planned', 'Progress reflections — planned'],
      access: 'Not available in Phase 1.',
      time: 'Not yet published',
      action: null,
      faq: [['Can I access it now?', 'No. Use the free Weekly Compass Preview while this planned journal remains unavailable.']],
      appCTA: false,
      moneyEducation: false
    },
    '7-day-focus-recovery': {
      slug: '7-day-focus-recovery',
      title: '7-Day Focus Recovery',
      category: 'programs',
      type: 'Program',
      availability: 'coming_soon',
      outcome: 'A seven-day focus reset is being prepared.',
      summary: 'The planned program is intended to help participants establish one clear priority and a usable focus rhythm.',
      audience: 'For people who want a defined, short reset once the final program is ready.',
      notFor: 'Not currently available for purchase, delivery, or preorder. It is not clinical care or treatment.',
      contents: ['Seven guided days — planned', 'Priority and focus-rhythm exercises — planned', 'Final curriculum and delivery materials — not yet complete'],
      access: 'Not available. No completed curriculum or delivery system is connected to this website.',
      time: 'Planned seven days',
      action: null,
      faq: [
        ['Can I enroll now?', 'No. This program is not yet available, for sale, or in preorder.'],
        ['What can I do now?', 'Start with the free Find Your North Snapshot or 1-3-5 Daily Page.']
      ],
      appCTA: false,
      moneyEducation: false,
      purchaseRequirements: { completedAsset: false, deliveryReady: false, supportReady: false, refundPolicyReady: false, merchantOfRecordReady: false }
    },
    'north-90-day-direction-sprint': {
      slug: 'north-90-day-direction-sprint',
      title: 'NORTH 90-Day Direction Sprint',
      category: 'programs',
      type: 'Program',
      availability: 'coming_soon',
      outcome: 'A longer guided direction program is planned for a future phase.',
      summary: 'The planned outcome is one chosen 90-day direction, a weekly rhythm, evidence of wins, and a next-cycle plan.',
      audience: 'For people who want a longer guided program after it has been fully developed and validated.',
      notFor: 'Not available in Phase 1.',
      contents: ['Program curriculum — planned', 'Weekly rhythm — planned', 'Next-cycle plan — planned'],
      access: 'Not available in Phase 1.',
      time: 'Planned 90 days',
      action: null,
      faq: [['Can I enroll now?', 'No. This planned program is not available or for sale in Phase 1.']],
      appCTA: false,
      moneyEducation: false
    },
    'find-your-north-book': {
      slug: 'find-your-north-book',
      title: 'Find Your North',
      category: 'books',
      type: 'Book & audio',
      availability: 'coming_soon',
      outcome: 'A durable book format for the NORTH method is planned.',
      summary: 'The planned book will introduce the 1-3-5 life operating system in ebook, print, and audio formats after completion.',
      audience: 'For people who prefer a long-form introduction to the NORTH method.',
      notFor: 'Not available for preorder, purchase, or waitlist enrollment in Phase 1.',
      contents: ['Ebook — planned', 'Paperback — planned', 'Audiobook — planned'],
      access: 'Not available in Phase 1.',
      time: 'Not yet published',
      action: null,
      faq: [['Can I preorder or join a waitlist?', 'No. Phase 1 does not collect book preorders or waitlist details.']],
      appCTA: false,
      moneyEducation: false
    }
  };

  const analytics = {
    allowedEvents: [
      'library_view',
      'library_category_select',
      'free_tool_start',
      'free_tool_complete',
      'free_tool_recommendation',
      'product_page_view',
      'product_interest',
      'app_store_click'
    ],
    disabledEvents: [
      'checkout_start',
      'purchase',
      'refund',
      'course_start',
      'course_complete',
      'affiliate_click',
      'referral_revenue',
      'product_to_app_trial',
      'trial_to_paid'
    ]
  };

  function isPurchasable(product) {
    const req = product && product.purchaseRequirements;
    return Boolean(
      product && product.availability === 'available' && req &&
      req.completedAsset && req.deliveryReady && req.supportReady &&
      req.refundPolicyReady && req.merchantOfRecordReady
    );
  }

  window.NORTH_CONFIG = Object.freeze({
    phase: 'phase-1',
    publicWebLanguage: 'en',
    brand: { name: 'NORTH', supportEmail: 'hello@yournorth.app', appStoreUrl: APP_STORE_URL },
    languageRegistry,
    products,
    analytics,
    isPurchasable
  });
})(window);
