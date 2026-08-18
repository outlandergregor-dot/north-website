/* NORTH Phase 2A private Product Studio registry.
 * Internal planning data only. It intentionally renders no commercial action for this phase.
 */
(function (window) {
  'use strict';

  const PRODUCT_STATUSES = Object.freeze(['concept', 'in_production', 'review_required', 'approved_for_sale', 'retired']);
  const SAFE_PUBLIC_STATES = Object.freeze(['hidden', 'private_preview', 'coming_soon', 'approved_for_sale']);
  const LOCALE_CODES = Object.freeze(['en', 'pt-BR', 'es-419', 'fr', 'de', 'it', 'ja', 'ko', 'zh-Hans', 'zh-Hant', 'ar', 'ru', 'pl', 'nl']);

  const localeRegistry = Object.freeze({
    sourceLocale: 'en',
    verifiedMobileAppLocales: LOCALE_CODES,
    locales: [
      { code: 'en', name: 'English', rtl: false, candidateOrder: 0, state: 'source', requirements: ['source copy approved'] },
      { code: 'pt-BR', name: 'Brazilian Portuguese', rtl: false, candidateOrder: 1, state: 'candidate_after_english', requirements: ['human page review', 'human asset review', 'checkout review', 'delivery review', 'support review', 'legal review'] },
      { code: 'es-419', name: 'Latin-American Spanish', rtl: false, candidateOrder: 2, state: 'candidate_after_english', requirements: ['human page review', 'human asset review', 'checkout review', 'delivery review', 'support review', 'legal review'] },
      { code: 'fr', name: 'French', rtl: false, candidateOrder: null, state: 'not_released', requirements: ['full locale path complete'] },
      { code: 'de', name: 'German', rtl: false, candidateOrder: null, state: 'not_released', requirements: ['full locale path complete'] },
      { code: 'it', name: 'Italian', rtl: false, candidateOrder: null, state: 'not_released', requirements: ['full locale path complete'] },
      { code: 'ja', name: 'Japanese', rtl: false, candidateOrder: null, state: 'not_released', requirements: ['full locale path complete'] },
      { code: 'ko', name: 'Korean', rtl: false, candidateOrder: null, state: 'not_released', requirements: ['full locale path complete'] },
      { code: 'zh-Hans', name: 'Chinese (Simplified)', rtl: false, candidateOrder: null, state: 'not_released', requirements: ['full locale path complete'] },
      { code: 'zh-Hant', name: 'Chinese (Traditional)', rtl: false, candidateOrder: null, state: 'not_released', requirements: ['full locale path complete'] },
      { code: 'ar', name: 'Arabic', rtl: true, candidateOrder: null, state: 'not_released', requirements: ['full locale path complete', 'RTL visual QA'] },
      { code: 'ru', name: 'Russian', rtl: false, candidateOrder: null, state: 'not_released', requirements: ['full locale path complete'] },
      { code: 'pl', name: 'Polish', rtl: false, candidateOrder: null, state: 'not_released', requirements: ['full locale path complete'] },
      { code: 'nl', name: 'Dutch', rtl: false, candidateOrder: null, state: 'not_released', requirements: ['full locale path complete'] }
    ]
  });

  const localeReadiness = () => Object.fromEntries(localeRegistry.locales.map((locale) => [locale.code, {
    page: locale.code === 'en' ? 'source_ready' : 'not_released',
    checkout: 'not_released',
    delivery: 'not_released',
    asset: 'not_released',
    support: 'not_released',
    legal: 'not_released',
    humanReview: locale.code === 'en' ? 'source_owner_required' : 'required'
  }]));

  const defaultReleaseControl = (state, blockers, owner) => ({
    safePublicState: state,
    publicVisibility: false,
    releaseDate: null,
    blockers,
    nextOwner: owner,
    supportOwner: 'Founder + support owner to be named',
    refundPolicyStatus: 'not_started',
    deliveryStatus: 'not_started',
    checkoutStatus: 'prohibited_phase_2a',
    assetManifestComplete: false,
    contentComplete: false,
    supportReady: false,
    policyReady: false,
    complianceComplete: false
  });

  const product = (data) => Object.freeze({
    currency: 'USD',
    bundleMembership: [],
    sampleAvailability: 'internal_draft_only',
    deliverables: [],
    compliance: { moneyEducation: false, ageRestricted: false, affiliateDisclosure: false, licensedContent: false, physicalFulfillment: false },
    localeReadiness: localeReadiness(),
    ...data
  });

  const products = Object.freeze({
    'execution-planner-14': product({
      id: 'north.release-a.execution-planner-14', category: 'resources', releaseFamily: 'Release A', slug: '1-3-5-execution-planner',
      title: '1-3-5 Execution Planner', status: 'review_required', proposedPrice: 19,
      outcome: 'Build a repeatable 14-day rhythm around one meaningful priority, three supporting actions, and five small wins.',
      audience: 'Adults who want a practical, bounded planning rhythm after trying the free 1-3-5 Daily Page.',
      notFor: 'Not for project management, medical/mental-health treatment, or a promise of productivity outcomes.',
      deliverables: ['Fillable 14-day planner — US Letter', 'Fillable 14-day planner — A4', 'Printable 14-day planner — US Letter', 'Printable 14-day planner — A4', 'Concise method guide'],
      reviewDraft: { version: 'v1.0', artifactStem: 'execution-planner', lastUpdated: '2026-08-18', sourcePackage: 'internal/commerce-pilot/execution-planner-v1', reviewExport: 'internal/commerce-pilot/execution-planner-v1/private-review/execution-planner-customer-review.html', contentCompletionPercent: 100, coverArtStatus: 'private_visuals_complete_pending_founder_approval', rightsStatus: 'original_text_and_phase2d_visual_assets_pending_brand_legal_review', accessibilityChecklistStatus: 'print_proofs_complete_pending_tagged_fillable_pdf_qa', founderApprovalStatus: 'pending_founder_commerce_pilot_review', expertReviewRequired: false, expertReviewStatus: 'not_required_if_non_regulated_scope_remains', reviewNotes: 'Founder to review final master, visual direction, print proofs, policy drafts, pricing options, and inactive delivery architecture.', draftAssetInventory: ['Editable customer-ready English master', 'Private premium HTML product review', 'US Letter private print proof', 'A4 private print proof', 'Four original preview assets', 'Personal-use license draft', 'Support and refund information draft'] },
      commercePilot: { enabled: false, merchant: null, merchantProductId: null, checkoutUrl: null, confirmation: 'designed_not_active', delivery: 'designed_not_active', pricingOptions: ['$19 core digital planner', '$29 planner plus editable source', '$14 launch promotion'], publicSaleApproved: false },
      editionAvailability: Object.freeze({
        en: { productContent: 'private_release_candidate', checkout: 'not_enabled', delivery: 'not_enabled', support: 'draft_only', legalPolicy: 'draft_pending_review', publicOffer: false },
        'pt-BR': { productContent: 'not_available_human_translation_required', checkout: 'not_enabled', delivery: 'not_enabled', support: 'not_available', legalPolicy: 'not_available', publicOffer: false },
        'es-419': { productContent: 'not_available_human_translation_required', checkout: 'not_enabled', delivery: 'not_enabled', support: 'not_available', legalPolicy: 'not_available', publicOffer: false },
        ar: { productContent: 'rtl_route_only_no_product_edition', checkout: 'not_enabled', delivery: 'not_enabled', support: 'not_available', legalPolicy: 'not_available', publicOffer: false },
        default: { productContent: 'not_available', checkout: 'not_enabled', delivery: 'not_enabled', support: 'not_available', legalPolicy: 'not_available', publicOffer: false }
      }),
      saleGateLocked: true,
      ...defaultReleaseControl('private_preview', ['Founder approval of final product and pilot option', 'attorney review of license/support/refund/consumer disclosures', 'tagged and fillable PDF accessibility QA', 'merchant selection and merchant-of-record setup', 'approved price/tax/refund configuration', 'secure delivery and re-delivery test', 'transactional confirmation and support inbox test', 'explicit written commerce activation approval'], 'Founder + legal reviewer + product operations')
    }),
    'decision-clarity-toolkit': product({
      id: 'north.release-a.decision-clarity-toolkit', category: 'resources', releaseFamily: 'Release A', slug: 'decision-clarity-toolkit',
      title: 'Decision Clarity Toolkit', status: 'in_production', proposedPrice: 19,
      outcome: 'Move a meaningful decision from vague pressure to a documented next choice and trade-off.',
      audience: 'Adults facing a meaningful personal or professional decision who want a structured reflection process.',
      notFor: 'Not for legal, medical, financial, investment, tax, or other professional advice.',
      deliverables: ['Decision Filter', 'Trade-off Map', 'Pre-mortem', 'Captain’s Brief', 'Plain-language instructions'],
      reviewDraft: { version: 'v0.1', artifactStem: 'decision-clarity-toolkit', lastUpdated: '2026-08-18', sourcePackage: 'internal/review-drafts/release-a/decision-clarity-toolkit-v0.1', reviewExport: 'internal/review-exports/release-a/decision-clarity-toolkit-review.html', contentCompletionPercent: 100, coverArtStatus: 'not_started', rightsStatus: 'original_text_only_no_external_visuals', accessibilityChecklistStatus: 'drafted_pending_layout_qa', founderApprovalStatus: 'pending_founder_review', expertReviewRequired: false, expertReviewStatus: 'not_required_if_non_regulated_scope_remains', reviewNotes: 'Founder to review examples, reflection boundaries, and one-page Captain’s Brief.', draftAssetInventory: ['Editable product brief', 'Editable 20-page source manuscript', 'Private HTML review export', 'Print and accessibility checklist'] },
      saleGateLocked: true,
      ...defaultReleaseControl('private_preview', ['Founder content approval', 'final layouts', 'claim boundary review', 'accessible-form QA if implemented', 'delivery system', 'support owner', 'refund policy', 'merchant-of-record approval'], 'Founder + ChatGPT')
    }),
    'focus-recovery-program': product({
      id: 'north.release-a.focus-recovery-program', category: 'programs', releaseFamily: 'Release A', slug: 'focus-recovery-program',
      title: 'Focus Recovery Program', status: 'in_production', proposedPrice: 27,
      outcome: 'Complete a seven-day practical reset that establishes one clearer priority and a workable daily focus rhythm.',
      audience: 'Adults who want a defined short reset around priorities and attention.',
      notFor: 'Not for clinical treatment, burnout treatment, therapy, crisis support, or guaranteed performance results.',
      deliverables: ['Seven short daily lessons/actions', 'Seven daily mission sheets', 'Reset workbook', 'Weekly reflection', 'Completion plan'],
      reviewDraft: { version: 'v0.1', artifactStem: 'focus-recovery-program', lastUpdated: '2026-08-18', sourcePackage: 'internal/review-drafts/release-a/focus-recovery-program-v0.1', reviewExport: 'internal/review-exports/release-a/focus-recovery-program-review.html', contentCompletionPercent: 100, coverArtStatus: 'not_started', rightsStatus: 'original_text_only_no_external_visuals', accessibilityChecklistStatus: 'drafted_pending_layout_qa', founderApprovalStatus: 'pending_founder_review', expertReviewRequired: false, expertReviewStatus: 'not_required_if_non_clinical_boundary_remains', reviewNotes: 'Founder to review every day for practical usefulness and non-clinical language.', draftAssetInventory: ['Editable product brief', 'Editable 22-page source manuscript', 'Private HTML review export', 'Print and accessibility checklist'] },
      saleGateLocked: true,
      ...defaultReleaseControl('private_preview', ['Founder curriculum approval', 'non-clinical claim boundary review', 'final layouts', 'accessible-form QA if implemented', 'delivery system', 'support owner', 'refund policy', 'merchant-of-record approval'], 'Founder + ChatGPT')
    }),
    'weekly-compass-journal': product({
      id: 'north.release-b.weekly-compass-journal', category: 'resources', releaseFamily: 'Release B', slug: 'weekly-compass-journal',
      title: 'Weekly Compass Journal', status: 'concept', proposedPrice: 27,
      outcome: 'Sustain a weekly reset practice across a full year of intentional reviews.',
      audience: 'Adults who want a longer-form weekly reflection practice after validating the free preview.',
      notFor: 'Not for therapy, diagnosis, or guaranteed habit outcomes.',
      deliverables: ['52 weekly resets', 'Wins and lessons prompts', 'Energy reflection', 'Quarterly review'],
      ...defaultReleaseControl('hidden', ['Original journal framework', 'all 52 weekly pages', 'editorial review', 'final formats', 'validated buyer need'], 'Founder + ChatGPT')
    }),
    'financial-clarity-kit': product({
      id: 'north.release-b.financial-clarity-kit', category: 'resources', releaseFamily: 'Release B', slug: 'financial-clarity-kit',
      title: 'Financial Clarity Kit', status: 'review_required', proposedPrice: 27,
      outcome: 'Organize a household money conversation and recurring review without individualized recommendations.',
      audience: 'Adults seeking general money organization and household conversation prompts.',
      notFor: 'Not for individualized financial, tax, investment, credit, lending, insurance, legal, or debt advice.',
      deliverables: ['Cash-flow organizer', 'Safe Number worksheet', 'Monthly review', 'Household conversation sheets'],
      compliance: { moneyEducation: true, ageRestricted: false, affiliateDisclosure: false, licensedContent: false, physicalFulfillment: false },
      ...defaultReleaseControl('hidden', ['Qualified financial-professional review', 'legal review', 'original curriculum', 'safe scope language', 'delivery system', 'support and refund policy'], 'Qualified financial reviewer + legal reviewer')
    }),
    'north-foundation-collection': product({
      id: 'north.release-b.north-foundation-collection', category: 'collections', releaseFamily: 'Release B', slug: 'north-foundation-collection',
      title: 'NORTH Foundation Collection', status: 'concept', proposedPrice: 77,
      outcome: 'Bring four fully validated NORTH practices into one coherent collection.',
      audience: 'Adults who want the complete validated foundation set after each component is available independently.',
      notFor: 'Not available until every named product is complete and approved for sale.',
      bundleMembership: ['focus-recovery-program', 'financial-clarity-kit', 'execution-planner-14', 'weekly-compass-journal'],
      deliverables: ['Focus Recovery Program', 'Financial Clarity Kit', '1-3-5 Execution Planner', 'Weekly Compass Journal'],
      ...defaultReleaseControl('hidden', ['All four member products approved for sale', 'bundle support policy', 'delivery test', 'merchant approval'], 'Founder + product operations')
    }),
    'find-your-north-book': product({
      id: 'north.release-c.find-your-north-book', category: 'books', releaseFamily: 'Release C', slug: 'find-your-north-book',
      title: 'Find Your North', status: 'concept', proposedPrice: null,
      outcome: 'Introduce the NORTH life operating system through a real authored long-form work.',
      audience: 'Readers who prefer a durable, long-form introduction to the NORTH method.',
      notFor: 'Not a low-content journal, AI-generated filler, preorder, or unpublished manuscript.',
      deliverables: ['Authored manuscript', 'Professional edit', 'Rights-cleared cover and interior', 'Final ebook format', 'Later paperback/audio assessment'],
      ...defaultReleaseControl('hidden', ['Founder-authored manuscript', 'editing', 'rights review', 'cover/interior', 'final formats'], 'Founder + editor + rights reviewer')
    }),
    'north-90-day-direction-sprint': product({
      id: 'north.release-c.north-90-day-direction-sprint', category: 'programs', releaseFamily: 'Release C', slug: 'north-90-day-direction-sprint',
      title: 'NORTH 90-Day Direction Sprint', status: 'concept', proposedPrice: null,
      outcome: 'Complete a guided 90-day direction cycle with a defined rhythm and next-cycle plan.',
      audience: 'Adults ready for a longer, fully developed and supported direction program.',
      notFor: 'Not a coaching substitute, unbuilt curriculum, or promise of personal transformation.',
      deliverables: ['Complete curriculum', 'Direction workbook', 'Completion journey', 'Support path'],
      ...defaultReleaseControl('hidden', ['Original curriculum', 'workbook', 'buyer feedback', 'support design', 'delivery path'], 'Founder + ChatGPT')
    }),
    'north-90-day-direction-book': product({
      id: 'north.release-c.north-90-day-direction-book', category: 'books', releaseFamily: 'Release C', slug: 'north-90-day-direction-book',
      title: 'The NORTH 90-Day Direction Book', status: 'concept', proposedPrice: null,
      outcome: 'Use a validated direction workbook after the related Sprint content and buyer feedback prove the need.',
      audience: 'Participants seeking a durable workbook after a validated NORTH Direction Sprint.',
      notFor: 'Not available before Sprint content, user feedback, and final workbook validation.',
      deliverables: ['Digital workbook', 'Later physical edition assessment'],
      ...defaultReleaseControl('hidden', ['Validated Sprint', 'buyer feedback', 'original workbook', 'print QA'], 'Founder + ChatGPT')
    }),
    'north-money-foundations': product({
      id: 'north.release-d.north-money-foundations', category: 'programs', releaseFamily: 'Release D', slug: 'north-money-foundations',
      title: 'NORTH Money Foundations', status: 'review_required', proposedPrice: null,
      outcome: 'Offer general adult money-organization education only after qualified expert review.',
      audience: 'Adults seeking general money organization education.',
      notFor: 'Not individual financial, investment, tax, credit, debt, lending, insurance, or legal advice.',
      deliverables: ['Reviewed general-education curriculum', 'Scope disclosures', 'Support and escalation path'],
      compliance: { moneyEducation: true, ageRestricted: true, affiliateDisclosure: false, licensedContent: false, physicalFulfillment: false },
      ...defaultReleaseControl('hidden', ['Qualified financial-professional review', 'legal review', 'adult-only policy', 'curriculum', 'support path'], 'Qualified financial reviewer + legal reviewer')
    }),
    'family-money-meeting-system': product({
      id: 'north.release-d.family-money-meeting-system', category: 'resources', releaseFamily: 'Release D', slug: 'family-money-meeting-system',
      title: 'Family Money Meeting System', status: 'concept', proposedPrice: null,
      outcome: 'Provide family conversation structure only after Money Foundations feedback proves the need.',
      audience: 'Adult couples or families seeking general household conversation structure.',
      notFor: 'Not advice, conflict mediation, family therapy, or a substitute for a qualified professional.',
      deliverables: ['Conversation structure', 'Meeting sheets', 'Scope and safety language'],
      compliance: { moneyEducation: true, ageRestricted: true, affiliateDisclosure: false, licensedContent: false, physicalFulfillment: false },
      ...defaultReleaseControl('hidden', ['Money Foundations feedback', 'qualified review', 'legal review', 'adult-use policy'], 'Founder + qualified reviewers')
    }),
    'adult-money-foundations': product({
      id: 'north.release-d.adult-money-foundations', category: 'programs', releaseFamily: 'Release D', slug: 'adult-money-foundations',
      title: 'Adult Money Foundations', status: 'review_required', proposedPrice: null,
      outcome: 'Provide age-appropriate general money education for adults ages 18–25 only after separate review.',
      audience: 'Adults ages 18–25 seeking general money-organization education.',
      notFor: 'Not for ages 16–17, personalized advice, or financial-product recommendations.',
      deliverables: ['Separate adult curriculum', 'Privacy review', 'Age-aware purchase policy'],
      compliance: { moneyEducation: true, ageRestricted: true, affiliateDisclosure: false, licensedContent: false, physicalFulfillment: false },
      ...defaultReleaseControl('hidden', ['Qualified financial-professional review', 'legal/privacy review', 'age policy', 'adult-only purchase flow'], 'Qualified financial reviewer + legal reviewer')
    }),
    'north-picks': product({
      id: 'north.later.north-picks', category: 'recommendations', releaseFamily: 'Later only', slug: 'north-picks',
      title: 'NORTH Picks', status: 'concept', proposedPrice: null,
      outcome: 'Curate a small disclosed editorial shelf only after a reviewable recommendation standard exists.',
      audience: 'Adults looking for carefully explained optional reading or focus-tool recommendations.',
      notFor: 'Not finance, crypto, lending, credit-repair, debt-relief, untested wellness, or undisclosed affiliate promotion.',
      deliverables: ['Editorial selection policy', 'Disclosure pattern', '10–15 justified recommendations'],
      compliance: { moneyEducation: false, ageRestricted: false, affiliateDisclosure: true, licensedContent: true, physicalFulfillment: false },
      ...defaultReleaseControl('hidden', ['Editorial policy', 'rights/disclosure review', 'approved disclosed links'], 'Founder + legal reviewer')
    }),
    'north-physical-planners': product({
      id: 'north.later.north-physical-planners', category: 'physical', releaseFamily: 'Later only', slug: 'north-physical-planners',
      title: 'NORTH Physical Planners & Desk Systems', status: 'concept', proposedPrice: null,
      outcome: 'Extend validated digital practices into physical formats only after fulfillment economics are proven.',
      audience: 'Customers who have validated a need for a premium physical companion.',
      notFor: 'Not available before digital conversion and fulfillment economics are proven.',
      deliverables: ['Physical planner concept', 'Desk system concept', 'Fulfillment model'],
      compliance: { moneyEducation: false, ageRestricted: false, affiliateDisclosure: false, licensedContent: false, physicalFulfillment: true },
      ...defaultReleaseControl('hidden', ['Digital validation', 'fulfillment economics', 'vendor review', 'support policy'], 'Founder + operations')
    }),
    'north-original-audio': product({
      id: 'north.later.north-original-audio', category: 'audio', releaseFamily: 'Later only', slug: 'north-original-audio',
      title: 'NORTH Original Audio', status: 'concept', proposedPrice: null,
      outcome: 'Offer original audio only after rights, production, localization, and wellness-claim review are complete.',
      audience: 'Adults seeking optional original NORTH audio once the production path is validated.',
      notFor: 'Not a wellness treatment, rights-uncleared audio, or unreviewed translated content.',
      deliverables: ['Original audio concept', 'Rights review', 'Production plan', 'Localization plan'],
      compliance: { moneyEducation: false, ageRestricted: false, affiliateDisclosure: false, licensedContent: true, physicalFulfillment: false },
      ...defaultReleaseControl('hidden', ['Rights review', 'production plan', 'localization review', 'wellness-claim review'], 'Founder + rights reviewer')
    })
  });

  function readiness(productRecord) {
    const required = [
      productRecord.status === 'approved_for_sale',
      productRecord.assetManifestComplete,
      productRecord.contentComplete,
      productRecord.deliveryStatus === 'ready',
      productRecord.supportReady,
      productRecord.policyReady,
      productRecord.complianceComplete,
      productRecord.checkoutStatus === 'approved_separate_phase',
      productRecord.publicVisibility === true
    ];
    return required.every(Boolean);
  }

  function renderPolicy(productRecord) {
    const eligible = readiness(productRecord);
    return Object.freeze({
      eligible,
      displayState: eligible ? 'approved_for_sale' : productRecord.safePublicState,
      allowPrice: eligible,
      allowSavingsClaim: eligible,
      allowPurchaseCTA: eligible,
      allowCheckout: eligible,
      allowDeliveryPromise: eligible,
      allowAppEntitlement: eligible,
      displayPrice: eligible ? `$${productRecord.proposedPrice}` : null
    });
  }

  function catalog() { return Object.values(products); }

  window.NORTH_PRODUCT_STUDIO = Object.freeze({
    phase: 'phase-2b-private-founder-review',
    productStatuses: PRODUCT_STATUSES,
    safePublicStates: SAFE_PUBLIC_STATES,
    localeRegistry,
    products,
    catalog,
    readiness,
    renderPolicy
  });
})(window);
