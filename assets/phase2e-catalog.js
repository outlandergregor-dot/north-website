/* NORTH Phase 2E governed catalog. Internal planning only; never exposes commercial actions. */
window.NORTHPhase2ECatalog = {
  schemaVersion: '2E.1',
  status: 'private-founder-roadmap',
  pilot: {
    productId: 'north.execution-planner.core-digital.en',
    sku: 'NORTH-PLN-135-CORE-EN-001',
    name: '1-3-5 Execution Planner — Core Digital Edition',
    proposedPrice: '$19 USD',
    salesLanguage: 'en',
    saleGate: 'closed',
    availability: 'private founder release candidate only'
  },
  northMethod: [
    'Safe Number', 'Big Thing', '1-3-5 execution', 'weekly reflection',
    'routines', 'recovery', 'growth'
  ],
  releaseRules: {
    noPublicAvailabilityWithout: ['human-reviewed product content', 'human-reviewed product page', 'approved policy/support/refund copy', 'legal review', 'accessibility and print QA', 'founder approval'],
    financeBoundary: 'General educational information only. Never personalized financial, tax, investment, debt, legal, income, or credit advice.',
    salesGate: 'No merchant, payment, checkout, public pricing, delivery, affiliate, email capture, tracking, or product download is enabled in Phase 2E.'
  },
  localePolicy: {
    activeProductEdition: 'English private candidate only',
    firstHumanReviewQueue: ['pt-BR', 'es-419'],
    governedRoutes: ['en','pt-BR','es-419','fr','de','it','ja','ko','zh-Hans','zh-Hant','ar','ru','pl','nl'],
    arabic: 'RTL route readiness only; no customer product edition until full Arabic content and asset QA.'
  },
  families: [
    {
      id: 'financial-clarity', name: 'Financial Clarity', pillar: 'Financial clarity and household stability',
      educationOnly: true,
      products: [
        {id:'safe-number-starter-kit', name:'Safe Number Starter Kit', priority:2, stage:'roadmap', audience:'Adults and households seeking a calmer starting point for money organization.', promise:'A general-education planning kit for identifying a personal household stability number and next money conversation.', method:['Safe Number','weekly reflection','growth'], boundary:'General educational information only; no individualized financial, tax, investment, debt, income, or legal guidance.', dependencies:['qualified legal and policy review','content review for financial education boundaries','localized policy review before release']},
        {id:'family-money-meeting-kit', name:'Family Money Meeting Kit', priority:7, stage:'roadmap', audience:'Households that want a structured recurring conversation about priorities and shared administration.', promise:'A household conversation kit for planning, listening, and documenting next steps without prescribing money decisions.', method:['Safe Number','Big Thing','weekly reflection','routines'], boundary:'General educational information only; not financial, tax, investment, debt, legal, or income advice.', dependencies:['qualified legal and policy review','household-safety and accessibility review','human-review of all customer-facing locales']},
        {id:'paycheck-to-priority-planner', name:'Paycheck-to-Priority Planner', priority:12, stage:'roadmap', audience:'Adults who want an educational way to connect income timing with household priorities.', promise:'A general planning structure for deciding what to review at each pay cycle.', method:['Safe Number','Big Thing','1-3-5 execution','routines'], boundary:'Education only; no budgeting recommendation, debt strategy, investment, tax, or income outcome claim.', dependencies:['qualified legal and policy review','financial-content specialist review','consumer-policy review']},
        {id:'financial-calm-workbook', name:'Financial Calm Workbook', priority:13, stage:'roadmap', audience:'Adults who want prompts for reducing avoidance around household money administration.', promise:'A reflective educational workbook for values, conversations, documentation, and next steps.', method:['Safe Number','recovery','weekly reflection','growth'], boundary:'Education only; does not provide therapy, financial, legal, tax, investment, debt, or income advice.', dependencies:['qualified legal and policy review','clinical-claims review','financial-content specialist review']}
      ]
    },
    {
      id: 'routine-reset', name: 'Routine Reset', pillar: 'Routines, discipline, and life organization', educationOnly: false,
      products: [
        {id:'21-day-routine-reset', name:'21-Day Routine Reset', priority:10, stage:'roadmap', audience:'Adults rebuilding simple, sustainable daily rhythms.', promise:'A guided 21-day practice for choosing and reviewing small routines.', method:['routines','weekly reflection','recovery','growth'], boundary:'Not medical or mental-health treatment; no guaranteed behavior change.', dependencies:['full curriculum','accessibility QA','customer support policy']},
        {id:'morning-evening-ritual-cards', name:'Morning and Evening Ritual Cards', priority:11, stage:'roadmap', audience:'Adults who prefer small visual prompts for opening and closing a day.', promise:'A flexible card set for personal reflection, intentional starts, and gentle closeouts.', method:['routines','Big Thing','recovery'], boundary:'Not a clinical treatment or productivity guarantee.', dependencies:['card production specification','rights-cleared visual system','print and accessibility QA']},
        {id:'life-admin-reset', name:'Life Admin Reset', priority:14, stage:'roadmap', audience:'Adults organizing recurring personal administration without turning it into a punitive system.', promise:'A planning kit for identifying administration categories and scheduling bounded next steps.', method:['Big Thing','1-3-5 execution','routines','weekly reflection'], boundary:'Not legal, tax, financial, medical, or professional advice.', dependencies:['scope taxonomy','legal/tax disclaimer review','accessibility QA']},
        {id:'weekly-reset-kit', name:'Weekly Reset Kit', priority:1, stage:'post-pilot candidate', audience:'People who want a light digital companion without duplicating the Planner’s value.', promise:'A compact weekly reflection and reset companion built around review, routines, and a next Big Thing.', method:['weekly reflection','Big Thing','routines','growth'], boundary:'No guaranteed outcomes; must be materially distinct from the Planner.', dependencies:['proven Planner demand','non-duplication review','product bundle definition','founder approval']}
      ]
    },
    {
      id: 'focus-execution', name: 'Focus and Execution', pillar: 'Focus, execution, and recovery from overwhelm', educationOnly: false,
      products: [
        {id:'execution-planner', name:'1-3-5 Execution Planner', priority:0, stage:'private pilot candidate', audience:'Adults seeking a bounded two-week planning rhythm.', promise:'One meaningful priority, three supports, and five useful small wins made visible over two weeks.', method:['Big Thing','1-3-5 execution','weekly reflection','recovery'], boundary:'No productivity, health, income, or transformation guarantee.', dependencies:['Phase 2E founder approval','legal and policy review','merchant test','controlled beta']},
        {id:'focus-recovery-protocol', name:'Focus Recovery Protocol', priority:5, stage:'founder review', audience:'Adults who want a non-clinical routine for returning to a manageable next step.', promise:'A structured recovery practice for interruption, overwhelm, and restarting.', method:['recovery','Big Thing','1-3-5 execution','routines'], boundary:'Non-clinical; not mental-health treatment, diagnosis, crisis support, or medical advice.', dependencies:['founder content approval','non-clinical claims review','accessibility QA']},
        {id:'deep-work-sprint-kit', name:'Deep Work Sprint Kit', priority:15, stage:'roadmap', audience:'Adults planning a bounded distraction-reduced work session.', promise:'A preparation, focus-session, recovery, and review kit for a deliberate work block.', method:['Big Thing','1-3-5 execution','recovery','weekly reflection'], boundary:'No productivity or income outcome guarantee.', dependencies:['curriculum design','duplicate-value review','accessibility QA']},
        {id:'distraction-reset-toolkit', name:'Distraction Reset Toolkit', priority:16, stage:'roadmap', audience:'Adults reflecting on environmental and behavioral distractions.', promise:'A practical reset toolkit for naming interruptions and choosing a next useful action.', method:['recovery','routines','1-3-5 execution'], boundary:'Not a clinical treatment or diagnosis.', dependencies:['content review','non-clinical claims review','accessibility QA']}
      ]
    },
    {
      id: 'direction-motivation', name: 'Direction and Motivation', pillar: 'Motivation, goals, decision-making, and personal direction', educationOnly: false,
      products: [
        {id:'decision-clarity-toolkit', name:'Decision Clarity Toolkit', priority:4, stage:'founder review', audience:'Adults making a bounded personal or professional decision.', promise:'A structured prompt set for separating facts, values, trade-offs, and next steps.', method:['Big Thing','weekly reflection','growth'], boundary:'Not legal, financial, medical, or professional advice; no promised decision outcome.', dependencies:['founder content approval','scenario and claims review','accessibility QA']},
        {id:'30-day-north-journey', name:'30-Day NORTH Journey', priority:17, stage:'roadmap', audience:'Adults who want a paced exploration of direction and routine.', promise:'A 30-day guided practice that connects reflection, Big Things, routines, and growth.', method:['Big Thing','routines','weekly reflection','growth'], boundary:'No guaranteed transformation or clinical claim.', dependencies:['complete curriculum','engagement design','accessibility QA']},
        {id:'momentum-journal', name:'Momentum Journal', priority:18, stage:'roadmap', audience:'Adults who want a reflective record of small forward movement.', promise:'A journal structure that captures wins, evidence, obstacles, and next steps.', method:['weekly reflection','recovery','growth'], boundary:'Not therapy or mental-health treatment.', dependencies:['journal manuscript','editorial review','print and accessibility QA']},
        {id:'purpose-goals-compass', name:'Purpose and Goals Compass', priority:19, stage:'roadmap', audience:'Adults exploring values, personal direction, and actionable goals.', promise:'A guided compass for translating values into bounded goals and weekly actions.', method:['Big Thing','weekly reflection','growth'], boundary:'No guarantee of purpose discovery, income outcome, or life transformation.', dependencies:['content framework','claims review','accessibility QA']}
      ]
    },
    {
      id: 'authority-education', name: 'Authority and Education', pillar: 'NORTH Method authority, life skills, and education', educationOnly: false,
      products: [
        {id:'north-method-book-audio', name:'The NORTH Method e-book / audiobook', priority:6, stage:'roadmap', audience:'Adults who want a first-party long-form explanation of the NORTH Method.', promise:'An original, founder-authored explanation of NORTH principles, practices, and examples.', method:['Safe Number','Big Thing','1-3-5 execution','weekly reflection','routines','recovery','growth'], boundary:'First-party authored content only; no copied, resold, PLR, or unlicensed material.', dependencies:['original manuscript','editing','rights review','audiobook production','accessibility and format QA']},
        {id:'financial-foundations-families', name:'Financial Foundations for Families', priority:9, stage:'roadmap', audience:'Families seeking general educational discussion and planning materials.', promise:'A general-education family resource for shared priorities, documentation, and calm conversations.', method:['Safe Number','weekly reflection','routines','growth'], boundary:'General educational information only; not individualized financial, tax, investment, debt, legal, or income advice.', dependencies:['qualified legal and policy review','financial-content specialist review','family/privacy review']},
        {id:'north-launch-kit-16-25', name:'NORTH Launch Kit for ages 16–25', priority:8, stage:'roadmap', audience:'Young people and families considering life skills, habit building, career readiness, and planning.', promise:'A life-skills and planning resource built with age-appropriate privacy and safeguarding controls.', method:['Big Thing','1-3-5 execution','routines','growth'], boundary:'No financial, legal, medical, tax, investment, or income advice; age/privacy review required.', dependencies:['age-appropriateness review','privacy and safeguarding review','guardian/consent policy decision','accessibility QA']},
        {id:'north-for-founders', name:'NORTH for Founders', priority:20, stage:'roadmap', audience:'Founders seeking an educational system for personal direction, routines, and weekly reflection.', promise:'A founder-focused adaptation of the NORTH Method for bounded personal operating-system practice.', method:['Big Thing','1-3-5 execution','weekly reflection','routines','recovery','growth'], boundary:'Not business, legal, financial, tax, or investment advice; no growth or revenue claim.', dependencies:['positioning review','professional-claims review','founder approval']}
      ]
    }
  ]
};
