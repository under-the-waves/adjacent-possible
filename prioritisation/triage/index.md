---
layout: default
title: Triage Screen
permalink: /prioritisation/triage/
---

<style>
body .main-content {
    max-width: none !important;
    padding: 1rem !important;
}

.triage-container {
    max-width: 760px;
    margin: 0 auto;
    padding: 20px;
    font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: #333;
}

.triage-results-container {
    max-width: 880px;
}

.triage-header h1 {
    font-weight: normal;
    color: #000;
    margin-bottom: 8px;
}

.triage-header p.lede {
    color: #555;
    margin-bottom: 24px;
}

.btn-primary {
    background: #155799;
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 12px 22px;
    font-size: 1em;
    cursor: pointer;
    font-weight: 600;
}
.btn-primary:hover { background: #0f4373; }
.btn-primary:disabled { background: #bdbdbd; cursor: not-allowed; }

.btn-secondary {
    background: #fff;
    color: #155799;
    border: 1px solid #155799;
    border-radius: 6px;
    padding: 10px 18px;
    font-size: 0.9em;
    cursor: pointer;
    font-weight: 600;
    text-decoration: none;
    display: inline-block;
}
.btn-secondary:hover { background: #f0f6fc; }

.btn-link {
    background: none;
    border: none;
    color: #155799;
    cursor: pointer;
    text-decoration: underline;
    padding: 4px 8px;
    font-size: 0.9em;
}

.prior-banner {
    background: #f5f5f5;
    border-left: 4px solid #888;
    border-radius: 4px;
    padding: 12px 16px;
    margin-bottom: 24px;
    font-size: 0.9em;
}
.prior-banner .actions {
    margin-top: 8px;
}

.start-row {
    margin-top: 24px;
}
.start-row .meta {
    color: #888;
    font-size: 0.85em;
    margin-top: 10px;
}

/* ── Survey ── */

.progress-bar-container { margin-bottom: 24px; }
.progress-bar-outer {
    height: 8px;
    background: #e0e0e0;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 6px;
}
.progress-bar-fill {
    height: 100%;
    background: #155799;
    border-radius: 4px;
    transition: width 0.3s ease;
}
.progress-info {
    display: flex;
    justify-content: space-between;
    font-size: 0.8em;
    color: #666;
}

.question-card {
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.q-section {
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.75em;
    color: #888;
    font-weight: 600;
    margin-bottom: 8px;
}
.q-text {
    font-size: 1.05em;
    color: #222;
    margin-bottom: 18px;
    line-height: 1.4;
}
.q-options { display: flex; flex-direction: column; gap: 6px; }
.radio-option {
    display: flex;
    align-items: center;
    padding: 11px 14px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.12s;
    font-size: 0.95em;
    background: #fff;
}
.radio-option:hover { border-color: #155799; background: #f7fbff; }
.radio-option input[type="radio"] {
    margin-right: 10px;
    accent-color: #155799;
}
.radio-option.selected { border-color: #155799; background: #e3f2fd; }

.nav-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 8px;
}

/* ── Results ── */

.results-header { margin-bottom: 20px; }
.results-header h1 { font-weight: normal; color: #000; margin-bottom: 4px; }
.results-header p.lede { color: #555; margin: 0; }

.tier-section {
    margin-top: 36px;
}
.tier-section > h2 {
    font-size: 1.25em;
    font-weight: 600;
    color: #222;
    margin-bottom: 14px;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 6px;
}
.tier-section > p.tier-intro {
    color: #555;
    font-size: 0.95em;
    margin-bottom: 18px;
}

.triage-card {
    border: 2px solid #f57c00;
    background: #fff8e1;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 16px;
}
.triage-card.acute {
    border-color: #c62828;
    background: #ffebee;
}
.triage-card h3 {
    font-size: 1.05em;
    color: #222;
    margin-top: 0;
    margin-bottom: 10px;
}
.triage-card .body { font-size: 0.95em; color: #333; line-height: 1.5; }
.triage-card .first-step {
    margin-top: 10px;
    font-size: 0.95em;
    color: #333;
}
.triage-card .resources {
    margin-top: 14px;
    padding-top: 12px;
    border-top: 1px solid rgba(0,0,0,0.08);
    font-size: 0.9em;
}
.triage-card .resources ul { margin: 4px 0 0; padding-left: 20px; }
.triage-card .resources li { margin-bottom: 4px; }

.fundamentals-card {
    border: 1px solid #e0e0e0;
    background: #fff;
    border-radius: 8px;
    padding: 18px 20px;
    margin-bottom: 14px;
}
.fundamentals-card.start-here { border-left: 4px solid #155799; }
.fundamentals-card h3 {
    font-size: 1.05em;
    color: #222;
    margin-top: 0;
    margin-bottom: 4px;
}
.fundamentals-card .pretitle {
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.72em;
    color: #155799;
    font-weight: 600;
    margin-bottom: 4px;
}
.fundamentals-card.start-here .pretitle { color: #155799; }
.fundamentals-card .body {
    font-size: 0.93em;
    color: #444;
    line-height: 1.5;
    margin-bottom: 10px;
}
.fundamentals-card .links {
    font-size: 0.88em;
}
.fundamentals-card .links a { margin-right: 12px; }

.everything-else {
    background: #f8f9fa;
    border-radius: 8px;
    padding: 16px 20px;
    margin-top: 24px;
    font-size: 0.95em;
    color: #444;
}

.pre-fundamentals-cta {
    background: #e3f2fd;
    border-left: 4px solid #155799;
    border-radius: 4px;
    padding: 12px 16px;
    margin-bottom: 16px;
    font-size: 0.92em;
    color: #333;
    line-height: 1.5;
}
.pre-fundamentals-cta a { font-weight: 600; }

.all-clear {
    background: #f0f7f0;
    border-left: 4px solid #28a745;
    border-radius: 4px;
    padding: 16px 20px;
    color: #333;
}
.all-clear h3 { margin-top: 0; margin-bottom: 8px; color: #1d6f30; font-size: 1.05em; }
.all-clear p { margin: 0 0 8px 0; font-size: 0.94em; line-height: 1.5; }
.all-clear p:last-child { margin-bottom: 0; }

.fundamentals-card .figure {
    font-weight: 600;
    color: #222;
    margin-bottom: 8px;
    font-size: 0.95em;
}

.results-footer {
    margin-top: 30px;
    padding-top: 16px;
    border-top: 1px solid #e0e0e0;
    text-align: center;
}

.hidden { display: none; }

@media (max-width: 600px) {
    .triage-container { padding: 12px; }
    .question-card { padding: 18px; }
    .triage-card { padding: 16px; }
    .fundamentals-card { padding: 14px 16px; }
}
</style>

<div class="triage-container" id="triageRoot">

  <!-- Landing view -->
  <div id="viewLanding">
    <div class="triage-header">
      <h1>Triage screen</h1>
      <p class="lede">A short screen that surfaces serious issues worth attending to before broader optimisation work. About five minutes, ten short questions.</p>
    </div>

    <div id="priorBanner" class="prior-banner hidden">
      <div id="priorBannerText"></div>
      <div class="actions">
        <button class="btn-secondary" onclick="viewResults()">View results</button>
        <button class="btn-link" onclick="startSurvey()">Retake</button>
      </div>
    </div>

    <p>The screen uses validated short forms (PHQ-2 for depression, GAD-2 for anxiety, the Hunger Vital Sign for food insecurity) plus single behavioural items for safety, financial distress, substance use, and carer strain. Where something flags, you will see the issue named plainly, a recommended first step, and links to professional resources. The site does first-step orientation and signposting, not treatment.</p>

    <p>Your responses stay on this device unless you sign in, in which case they sync across devices via your account. They are not shared.</p>

    <div class="start-row">
      <button class="btn-primary" onclick="startSurvey()">Start the screen</button>
      <div class="meta">10 questions, about five minutes.</div>
    </div>
  </div>

  <!-- Survey view -->
  <div id="viewSurvey" class="hidden">
    <div class="progress-bar-container">
      <div class="progress-bar-outer"><div class="progress-bar-fill" id="progressFill"></div></div>
      <div class="progress-info">
        <span id="progressText">Question 1 of 10</span>
        <button class="btn-link" onclick="exitSurvey()" style="padding:0;">Exit</button>
      </div>
    </div>
    <div id="questionMount"></div>
    <div class="nav-row">
      <button class="btn-secondary" id="backBtn" onclick="goBack()">Back</button>
      <button class="btn-primary" id="nextBtn" onclick="goNext()" disabled>Next</button>
    </div>
  </div>

  <!-- Results view -->
  <div id="viewResults" class="hidden triage-results-container">
    <div class="results-header">
      <h1>Your results</h1>
      <p class="lede" id="resultsLede"></p>
    </div>
    <div id="tier1Mount"></div>
    <div id="tier2Mount"></div>
    <div id="tier3Mount"></div>
    <div class="results-footer">
      <button class="btn-link" onclick="startSurvey()">Retake the screen</button>
    </div>
  </div>

</div>

<script>
// ────────────────────────────────────────────────────────────────────────────
// Data
// ────────────────────────────────────────────────────────────────────────────

var SCALE_PHQ = [
    { label: 'Not at all', value: 0 },
    { label: 'Several days', value: 1 },
    { label: 'More than half the days', value: 2 },
    { label: 'Nearly every day', value: 3 }
];

var SCALE_HUNGER = [
    { label: 'Often true', value: 'often' },
    { label: 'Sometimes true', value: 'sometimes' },
    { label: 'Never true', value: 'never' }
];

var SCALE_YN_PNR = [
    { label: 'Yes', value: 'yes' },
    { label: 'No', value: 'no' },
    { label: 'Prefer not to say', value: 'pns' }
];

var SCALE_YN = [
    { label: 'Yes', value: 'yes' },
    { label: 'No', value: 'no' }
];

var SCALE_YN_NA = [
    { label: 'Yes', value: 'yes' },
    { label: 'No', value: 'no' },
    { label: 'Not applicable', value: 'na' }
];

var QUESTIONS = [
    { id: 'phq2_1', section: 'Mood',     text: 'Over the last two weeks, how often have you been bothered by little interest or pleasure in doing things?', options: SCALE_PHQ },
    { id: 'phq2_2', section: 'Mood',     text: 'Over the last two weeks, how often have you been bothered by feeling down, depressed, or hopeless?',         options: SCALE_PHQ },
    { id: 'gad2_1', section: 'Anxiety',  text: 'Over the last two weeks, how often have you been bothered by feeling nervous, anxious, or on edge?',         options: SCALE_PHQ },
    { id: 'gad2_2', section: 'Anxiety',  text: 'Over the last two weeks, how often have you been bothered by not being able to stop or control worrying?',   options: SCALE_PHQ },
    { id: 'safety',    section: 'Safety',    text: 'In the last twelve months, has anyone made you feel physically unsafe – including a partner, family member, or someone in your home?', options: SCALE_YN_PNR },
    { id: 'financial', section: 'Financial', text: 'In the last three months, have you had trouble paying for rent, mortgage, or essential bills, or worried about losing your housing?', options: SCALE_YN },
    { id: 'substance', section: 'Substance use', text: 'In the last twelve months, have you used alcohol, prescription medication, or other drugs in ways that caused problems for you, or more than you wanted to?', options: SCALE_YN_PNR },
    { id: 'hunger_1', section: 'Food', text: 'Within the past twelve months, were you worried that your food would run out before you had money to buy more?', options: SCALE_HUNGER },
    { id: 'hunger_2', section: 'Food', text: 'Within the past twelve months, did the food you bought just not last and you did not have money to get more?', options: SCALE_HUNGER },
    { id: 'carer',    section: 'Caring responsibilities', text: 'Are you the main person responsible for the care of a child, adult, or dependent with high needs, with little or no respite?', options: SCALE_YN_NA }
];

var CONDITIONAL_PHQ9_9 = {
    id: 'phq9_9',
    section: 'Follow-up',
    text: 'Over the last two weeks, how often have you had thoughts that you would be better off dead, or of hurting yourself in some way?',
    options: SCALE_PHQ
};

// ────────────────────────────────────────────────────────────────────────────
// Flag content
// ────────────────────────────────────────────────────────────────────────────

var FLAG_CONTENT = {
    suicidal: {
        acute: true,
        title: 'If you are having thoughts of self-harm, please reach out now.',
        body: 'Your responses indicated some thoughts of being better off dead or hurting yourself. These thoughts are common alongside depression and they pass with the right support. Talking to a trained listener now is the most important first step.',
        firstStep: '',
        resources: [
            { label: 'United States – call or text 988', href: 'https://988lifeline.org/' },
            { label: 'United Kingdom and Ireland – Samaritans, 116 123 (24 hours, free)', href: 'https://www.samaritans.org/' },
            { label: 'Australia – Lifeline, 13 11 14', href: 'https://www.lifeline.org.au/' },
            { label: 'Other countries – findahelpline.com', href: 'https://findahelpline.com/' }
        ]
    },
    depression: {
        title: function(level) {
            return 'Your responses suggest ' + (level === 'moderate' ? 'moderate or higher' : 'mild') + ' symptoms of depression.';
        },
        body: 'A PHQ-2 score of 3 or more is the validated threshold at which a fuller depression assessment is warranted. Depression is among the most treatable mental health conditions, with strong evidence for therapy (cognitive behavioural therapy or behavioural activation) and medication.',
        firstStep: 'A reasonable first step is to take the longer PHQ-9 to get a clearer picture, then book a GP or primary care appointment.',
        resources: [
            { label: 'PHQ-9 self-screen and scoring (free)', href: 'https://www.phqscreeners.com/' },
            { label: 'NHS Talking Therapies – self-referral (UK)', href: 'https://www.nhs.uk/mental-health/talking-therapies-medicine-treatments/talking-therapies-and-counselling/nhs-talking-therapies/' },
            { label: 'Psychology Today therapist directory (US)', href: 'https://www.psychologytoday.com/us/therapists' }
        ]
    },
    anxiety: {
        title: function(level) {
            return 'Your responses suggest ' + (level === 'moderate' ? 'moderate or higher' : 'mild') + ' symptoms of anxiety.';
        },
        body: 'A GAD-2 score of 3 or more is the validated threshold at which a fuller anxiety assessment is warranted. Cognitive behavioural therapy is the best-evidenced treatment for generalised anxiety, panic, and social anxiety; some forms also respond well to medication.',
        firstStep: 'A reasonable first step is to take the longer GAD-7 to get a clearer picture, then book a GP or primary care appointment.',
        resources: [
            { label: 'GAD-7 self-screen and scoring (free)', href: 'https://www.phqscreeners.com/' },
            { label: 'NHS Talking Therapies – self-referral (UK)', href: 'https://www.nhs.uk/mental-health/talking-therapies-medicine-treatments/talking-therapies-and-counselling/nhs-talking-therapies/' },
            { label: 'Psychology Today therapist directory (US)', href: 'https://www.psychologytoday.com/us/therapists' }
        ]
    },
    safety: {
        title: 'You indicated that someone has made you feel physically unsafe.',
        body: 'Safety planning matters before any other kind of self-improvement work. The services below are free and confidential. They can help you think through your situation and options without committing you to any specific course of action.',
        firstStep: 'A reasonable first step is to talk to a trained adviser, who can help you understand what support is available where you are.',
        resources: [
            { label: 'United States – National Domestic Violence Hotline, 1-800-799-7233', href: 'https://www.thehotline.org/' },
            { label: 'United Kingdom – Refuge, 0808 2000 247 (24 hours, free)', href: 'https://www.refuge.org.uk/' },
            { label: 'Other countries – findahelpline.com', href: 'https://findahelpline.com/' }
        ]
    },
    financial: {
        title: 'You indicated trouble paying essential bills or worry about losing your housing.',
        body: 'Financial scarcity has measurable effects on cognitive bandwidth and decision-making (Mani et al. 2013, Science). The framework recommends addressing acute financial distress before broader optimisation work. Free debt-counselling charities exist in most countries and tend to negotiate better outcomes than handling creditors alone.',
        firstStep: 'A reasonable first step is contacting a free debt advice service before missing a payment, since options narrow once defaults start.',
        resources: [
            { label: 'United Kingdom – StepChange, 0800 138 1111', href: 'https://www.stepchange.org/' },
            { label: 'United States – National Foundation for Credit Counseling, 1-800-388-2227', href: 'https://www.nfcc.org/' },
            { label: 'United States – call 211 for local assistance programmes', href: 'https://www.211.org/' }
        ]
    },
    substance: {
        title: 'You indicated using alcohol, medication, or other drugs in ways that caused problems.',
        body: 'Self-screening with the longer AUDIT (alcohol) or DAST-10 (drugs) tools gives a clearer picture of severity. For most people the most useful first conversation is with a GP, who can discuss options privately and connect you to specialist services if useful.',
        firstStep: 'A reasonable first step is taking the relevant self-screen and, if it confirms a concern, a GP appointment.',
        resources: [
            { label: 'United Kingdom – Drinkaware (alcohol education and self-assessment)', href: 'https://www.drinkaware.co.uk/' },
            { label: 'United States – SAMHSA helpline 1-800-662-4357 (24 hours, free, confidential)', href: 'https://findtreatment.gov/' },
            { label: 'Other countries – findahelpline.com', href: 'https://findahelpline.com/' }
        ]
    },
    food: {
        title: 'You indicated worry about food running out or food not lasting.',
        body: 'Food insecurity has measurable effects on physical and mental health independent of overall income (Hager et al. 2010). Local food banks operate independently of any benefits process and can usually be accessed quickly.',
        firstStep: 'A reasonable first step is locating a nearby food bank and, separately, checking whether you are eligible for benefits or assistance you are not currently claiming.',
        resources: [
            { label: 'United Kingdom – Trussell food bank network', href: 'https://www.trussell.org.uk/' },
            { label: 'United States – Feeding America food bank locator', href: 'https://www.feedingamerica.org/find-your-local-foodbank' },
            { label: 'United States – call 211 for local food assistance', href: 'https://www.211.org/' }
        ]
    },
    carer: {
        title: 'You indicated that you are the main carer for someone with high needs and have little or no respite.',
        body: 'This is one of the situations the framework recognises as not always solvable. Carer strain affects what "starting with sleep" or "starting with exercise" even mean. The most useful first step is usually connecting with a service that knows the local respite, financial, and emotional support options.',
        firstStep: 'A reasonable first step is reaching out to a carer support organisation in your country, who can help map the support that exists for your situation.',
        resources: [
            { label: 'United Kingdom – Carers UK', href: 'https://www.carersuk.org/' },
            { label: 'United States – Family Caregiver Alliance', href: 'https://www.caregiver.org/' }
        ]
    }
};

// ────────────────────────────────────────────────────────────────────────────
// Fundamentals content (Tier 2)
// ────────────────────────────────────────────────────────────────────────────

var BASE = '{{ site.baseurl }}';

var FUNDAMENTALS = [
    {
        id: 'sleep',
        title: 'Sleep',
        body: 'Sleeping fewer than six hours per night on a regular basis is associated with measurable effects on cognition, mood, metabolism, and immune function (Walker 2017; Cappuccio et al. 2010). Sleep is one of the highest-leverage areas because gains here propagate to almost everything else.',
        links: [
            { label: 'Read the Sleep guide', href: BASE + '/sleep/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#sleep' }
        ]
    },
    {
        id: 'mental-health',
        title: 'Mental health and wellbeing',
        body: 'Sub-clinical wellbeing impairment – feeling flat, low energy, or chronically stressed without meeting depression or anxiety thresholds – tends to undermine progress in every other area. The validated WHO-5 Wellbeing Index is a five-item check that takes a minute to complete.',
        links: [
            { label: 'Read the Mental Health guide', href: BASE + '/mental-health/' },
            { label: 'Read the Mindfulness guide', href: BASE + '/mindfulness/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#mental-health-sub-clinical' }
        ]
    },
    {
        id: 'finances',
        title: 'Foundational finances',
        body: 'A modest emergency buffer (around $1,000 or one month of essentials) and the absence of high-interest revolving debt are the upstream financial fundamentals. Chronic financial worry imposes a measurable cognitive load (Mani et al. 2013); this layer addresses that. Investment and broader financial optimisation come later.',
        links: [
            { label: 'Read the Saving guide', href: BASE + '/saving/' },
            { label: 'Read the Financial Planning guide', href: BASE + '/financial-planning-tracking/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#foundational-finances' }
        ]
    },
    {
        id: 'social',
        title: 'Key relationships and social connection',
        body: 'Loneliness and social isolation have mortality effects comparable in magnitude to smoking 15 cigarettes per day (Holt-Lunstad et al. 2015). The threshold worth flagging is fewer than weekly meaningful contact with people you feel close to, or persistent feelings of isolation on the UCLA-3 short scale.',
        links: [
            { label: 'Read the Friendship guide', href: BASE + '/friendship/' },
            { label: 'Read the Romantic Relationships guide', href: BASE + '/romantic-relationships/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#key-relationships-and-social-connection' }
        ]
    },
    {
        id: 'activity',
        title: 'Physical activity and nutrition',
        body: 'The largest absolute mortality gains from physical activity come from going from zero to roughly 60 minutes per week of anything that raises your heart rate. The largest gains from diet come from the first two-to-three daily servings of vegetables or fruit. Fundamentals here means being above the inactive baseline; hitting an optimal target is a separate, smaller-gain question.',
        links: [
            { label: 'Read the Fitness guide', href: BASE + '/fitness/' },
            { label: 'Read the Nutrition guide', href: BASE + '/nutrition/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#physical-activity-and-nutrition' }
        ]
    }
];

// ────────────────────────────────────────────────────────────────────────────
// Personalised fundamentals (Phase 2)
// ────────────────────────────────────────────────────────────────────────────

var PERSONALISED_FUND_ORDER = ['wellbeing', 'sleep', 'finances', 'social', 'activity'];

var PERSONALISED_FUND = {
    wellbeing: {
        title: 'Mental health and wellbeing',
        body: 'Sub-clinical wellbeing impairment tends to undermine progress in every other area; the Mental Health guide covers self-administered options, evidence, and what to expect at each level. Mindfulness practice is one of the best-evidenced contributors and lives in its own guide.',
        links: [
            { label: 'Read the Mental Health guide', href: BASE + '/mental-health/' },
            { label: 'Read the Mindfulness guide', href: BASE + '/mindfulness/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#mental-health-sub-clinical' }
        ]
    },
    sleep: {
        title: 'Sleep',
        body: 'Below 6 hours, mortality and cognitive harm rise sharply (Cappuccio et al. 2010). Sleep is one of the highest-leverage areas because gains here propagate to almost every other domain, and the Sleep guide covers the full set of evidence-based options.',
        links: [
            { label: 'Read the Sleep guide', href: BASE + '/sleep/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#sleep' }
        ]
    },
    finances: {
        title: 'Foundational finances',
        body: 'Chronic financial worry imposes a measurable cognitive load (Mani et al. 2013). Building a small emergency buffer and reducing high-interest revolving debt is the upstream financial fundamentals work; the Saving and Financial Planning guides cover the methods and expected timelines.',
        links: [
            { label: 'Read the Saving guide', href: BASE + '/saving/' },
            { label: 'Read the Financial Planning guide', href: BASE + '/financial-planning-tracking/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#foundational-finances' }
        ]
    },
    social: {
        title: 'Key relationships and social connection',
        body: 'Loneliness and social isolation have mortality effects comparable to smoking 15 cigarettes per day (Holt-Lunstad et al. 2015). The Friendship and Romantic Relationships guides cover what works at each level.',
        links: [
            { label: 'Read the Friendship guide', href: BASE + '/friendship/' },
            { label: 'Read the Romantic Relationships guide', href: BASE + '/romantic-relationships/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#key-relationships-and-social-connection' }
        ]
    },
    activity: {
        title: 'Physical activity and nutrition',
        body: 'The largest absolute mortality gains come from going from zero to roughly 60 minutes of moderate activity per week, and from the first two-to-three daily servings of vegetables or fruit. The Fitness and Nutrition guides cover what works and how to start.',
        links: [
            { label: 'Read the Fitness guide', href: BASE + '/fitness/' },
            { label: 'Read the Nutrition guide', href: BASE + '/nutrition/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#physical-activity-and-nutrition' }
        ]
    }
};

function getFundamentalsFigure(flag, responses) {
    if (!responses) responses = {};
    var bits;
    switch (flag) {
        case 'wellbeing':
            var who5 = ['who5_1','who5_2','who5_3','who5_4','who5_5']
                .reduce(function(s, k) { return s + (typeof responses[k] === 'number' ? responses[k] : 0); }, 0);
            return 'You scored ' + (who5 * 4) + '% on the WHO-5, below the 52% threshold for poor wellbeing.';
        case 'sleep':
            var sleepLabel = responses.sleep_hours === 'under5' ? 'under 5 hours' : '5 to 6 hours';
            return 'You reported sleeping ' + sleepLabel + ' on a typical work night.';
        case 'finances':
            bits = [];
            if (responses.emergency === 'no') bits.push('you could not cover a $400 unexpected expense from cash or savings');
            if (responses.high_interest_debt === 'yes') bits.push('you are carrying interest-bearing consumer debt');
            return bits.length ? 'You reported that ' + bits.join(' and ') + '.' : '';
        case 'social':
            var ucla = ['ucla_1','ucla_2','ucla_3']
                .reduce(function(s, k) { return s + (typeof responses[k] === 'number' ? responses[k] : 0); }, 0);
            bits = [];
            if (ucla >= 6) bits.push('you scored ' + ucla + ' on the UCLA-3 loneliness items (cutoff at 6)');
            if (responses.contact_freq === 'monthly') bits.push('you reported monthly meaningful contact with people you feel close to');
            else if (responses.contact_freq === 'less') bits.push('you reported less than monthly meaningful contact with people you feel close to');
            return bits.length ? 'You reported that ' + bits.join(' and ') + '.' : '';
        case 'activity':
            bits = [];
            if (responses.activity_min === '0') bits.push('no moderate-to-vigorous activity in a typical week');
            else if (responses.activity_min === 'under60') bits.push('under 60 minutes of moderate-to-vigorous activity per week');
            if (responses.veg_servings === '0-1') bits.push('0 to 1 daily servings of vegetables or fruit');
            else if (responses.veg_servings === '2') bits.push('2 daily servings of vegetables or fruit');
            return bits.length ? 'You reported ' + bits.join(' and ') + '.' : '';
    }
    return '';
}

function renderPersonalisedFundCard(flag, responses, isFirst) {
    var c = PERSONALISED_FUND[flag];
    if (!c) return '';
    var classes = 'fundamentals-card' + (isFirst ? ' start-here' : '');
    var pretitle = isFirst ? 'We would suggest starting here' : 'Also worth addressing';
    var figure = getFundamentalsFigure(flag, responses);
    var html = '<div class="' + classes + '">';
    html += '<div class="pretitle">' + escapeHtml(pretitle) + '</div>';
    html += '<h3>' + escapeHtml(c.title) + '</h3>';
    if (figure) html += '<div class="figure">' + escapeHtml(figure) + '</div>';
    html += '<div class="body">' + escapeHtml(c.body) + '</div>';
    if (c.links && c.links.length) {
        html += '<div class="links">';
        c.links.forEach(function(l) {
            html += '<a href="' + l.href + '">' + escapeHtml(l.label) + '</a>';
        });
        html += '</div>';
    }
    html += '</div>';
    return html;
}

// ────────────────────────────────────────────────────────────────────────────
// State and storage
// ────────────────────────────────────────────────────────────────────────────

var STORAGE_RESPONSES = 'ap-triage-responses';
var STORAGE_FLAGS     = 'ap-triage-flags';
var STORAGE_DONE_AT   = 'ap-triage-completed-at';

var FUND_RESPONSES = 'ap-fundamentals-responses';
var FUND_FLAGS     = 'ap-fundamentals-flags';
var FUND_DONE_AT   = 'ap-fundamentals-completed-at';

var answers = {};
var index = 0;
var currentList = [];

function saveAnswers() { window.APStorage.save(STORAGE_RESPONSES, answers); }
function loadAnswers() { return window.APStorage.load(STORAGE_RESPONSES) || {}; }
function saveFlags(f)  { window.APStorage.save(STORAGE_FLAGS, f); }
function saveDoneAt()  { window.APStorage.save(STORAGE_DONE_AT, new Date().toISOString()); }
function loadDoneAt()  { return window.APStorage.load(STORAGE_DONE_AT); }

// ────────────────────────────────────────────────────────────────────────────
// Flag computation
// ────────────────────────────────────────────────────────────────────────────

function computeFlags(a) {
    var flags = {};
    var phq = (a.phq2_1 || 0) + (a.phq2_2 || 0);
    if (phq >= 3) flags.depression = phq >= 4 ? 'moderate' : 'mild';
    if ((a.phq9_9 || 0) >= 1) flags.suicidal = true;

    var gad = (a.gad2_1 || 0) + (a.gad2_2 || 0);
    if (gad >= 3) flags.anxiety = gad >= 4 ? 'moderate' : 'mild';

    if (a.safety === 'yes')    flags.safety = true;
    if (a.financial === 'yes') flags.financial = true;
    if (a.substance === 'yes') flags.substance = true;

    var hungerHit = function(v) { return v === 'often' || v === 'sometimes'; };
    if (hungerHit(a.hunger_1) || hungerHit(a.hunger_2)) flags.food = true;

    if (a.carer === 'yes') flags.carer = true;
    return flags;
}

function phqIsPositive(a) { return ((a.phq2_1 || 0) + (a.phq2_2 || 0)) >= 3; }

// ────────────────────────────────────────────────────────────────────────────
// View switching
// ────────────────────────────────────────────────────────────────────────────

function showView(name) {
    ['Landing', 'Survey', 'Results'].forEach(function(v) {
        document.getElementById('view' + v).classList.toggle('hidden', v !== name);
    });
    window.scrollTo({ top: 0, behavior: 'instant' });
}

// ────────────────────────────────────────────────────────────────────────────
// Landing
// ────────────────────────────────────────────────────────────────────────────

function renderLanding() {
    var doneAt = loadDoneAt();
    var banner = document.getElementById('priorBanner');
    if (doneAt) {
        var dateStr;
        try {
            dateStr = new Intl.DateTimeFormat('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }).format(new Date(doneAt));
        } catch (e) { dateStr = doneAt.split('T')[0]; }
        document.getElementById('priorBannerText').textContent = 'You took this screen on ' + dateStr + '.';
        banner.classList.remove('hidden');
    } else {
        banner.classList.add('hidden');
    }
    showView('Landing');
}

// ────────────────────────────────────────────────────────────────────────────
// Survey
// ────────────────────────────────────────────────────────────────────────────

function startSurvey() {
    answers = {};
    index = 0;
    currentList = QUESTIONS.slice();
    renderQuestion();
    showView('Survey');
}

function buildList() {
    // Conditional injection: PHQ-9 item 9 if PHQ-2 sum >= 3
    var list = QUESTIONS.slice();
    if (phqIsPositive(answers)) list.push(CONDITIONAL_PHQ9_9);
    return list;
}

function renderQuestion() {
    currentList = buildList();
    if (index >= currentList.length) {
        finishSurvey();
        return;
    }
    var q = currentList[index];
    var total = currentList.length;
    document.getElementById('progressText').textContent = 'Question ' + (index + 1) + ' of ' + total;
    document.getElementById('progressFill').style.width = ((index) / total * 100) + '%';

    var html = '<div class="question-card">';
    html += '<div class="q-section">' + escapeHtml(q.section) + '</div>';
    html += '<div class="q-text">' + escapeHtml(q.text) + '</div>';
    html += '<div class="q-options">';
    var current = answers[q.id];
    q.options.forEach(function(opt, i) {
        var checked = (current !== undefined && current === opt.value) ? 'checked' : '';
        var sel     = (current !== undefined && current === opt.value) ? ' selected' : '';
        var optId   = 'opt_' + q.id + '_' + i;
        html += '<label class="radio-option' + sel + '" for="' + optId + '">';
        html += '<input type="radio" name="opt_' + q.id + '" id="' + optId + '" value="' + i + '" ' + checked + ' onchange="onAnswer(\'' + q.id + '\', ' + i + ')">';
        html += '<span>' + escapeHtml(opt.label) + '</span>';
        html += '</label>';
    });
    html += '</div></div>';
    document.getElementById('questionMount').innerHTML = html;

    document.getElementById('backBtn').disabled = (index === 0);
    document.getElementById('nextBtn').disabled = (current === undefined);
    document.getElementById('nextBtn').textContent = (index === currentList.length - 1) ? 'Finish' : 'Next';
}

function onAnswer(qid, optIndex) {
    var q = currentList.find(function(x) { return x.id === qid; });
    if (!q) return;
    answers[qid] = q.options[optIndex].value;
    saveAnswers();
    // Update visual selection without full rerender
    var labels = document.querySelectorAll('label.radio-option');
    labels.forEach(function(l) { l.classList.remove('selected'); });
    var picked = document.getElementById('opt_' + qid + '_' + optIndex);
    if (picked && picked.parentNode) picked.parentNode.classList.add('selected');
    document.getElementById('nextBtn').disabled = false;
}

function goNext() {
    index += 1;
    renderQuestion();
}

function goBack() {
    if (index === 0) return;
    index -= 1;
    renderQuestion();
}

function exitSurvey() {
    saveAnswers();
    renderLanding();
}

function finishSurvey() {
    var flags = computeFlags(answers);
    saveFlags(flags);
    saveDoneAt();
    renderResults(flags);
    showView('Results');
}

function viewResults() {
    answers = loadAnswers();
    var flags = window.APStorage.load(STORAGE_FLAGS) || computeFlags(answers);
    renderResults(flags);
    showView('Results');
}

// ────────────────────────────────────────────────────────────────────────────
// Results rendering
// ────────────────────────────────────────────────────────────────────────────

var FLAG_ORDER = ['suicidal', 'safety', 'depression', 'anxiety', 'substance', 'financial', 'food', 'carer'];

function renderResults(flags) {
    flags = flags || {};
    var triggered = FLAG_ORDER.filter(function(k) { return flags[k]; });
    var lede;
    if (triggered.length === 0) {
        lede = 'No areas surfaced from the triage screen.';
    } else if (triggered.length === 1) {
        lede = 'The triage screen surfaced one area worth attending to before broader optimisation work.';
    } else {
        lede = 'The triage screen surfaced ' + triggered.length + ' areas worth attending to before broader optimisation work.';
    }
    document.getElementById('resultsLede').textContent = lede;

    // Tier 1
    var t1 = document.getElementById('tier1Mount');
    if (triggered.length === 0) {
        t1.innerHTML = '';
    } else {
        var html = '<div class="tier-section"><h2>Worth attending to first</h2>';
        triggered.forEach(function(k) {
            html += renderFlagCard(k, flags[k]);
        });
        html += '</div>';
        t1.innerHTML = html;
    }

    // Tier 2 – branches on whether the user has done the fundamentals screen
    var fundFlags     = window.APStorage.load(FUND_FLAGS);
    var fundResponses = window.APStorage.load(FUND_RESPONSES) || {};
    var fundDoneAt    = window.APStorage.load(FUND_DONE_AT);

    var t2html = '<div class="tier-section">';
    t2html += '<h2>The five fundamentals</h2>';

    if (!fundDoneAt) {
        // Generic five cards plus pre-fundamentals CTA
        t2html += '<div class="pre-fundamentals-cta">';
        t2html += '<strong>Want personalised fundamentals?</strong> The cards below are the universal default order. A 5-minute screen (14 questions) reorders and filters them based on your situation. ';
        t2html += '<a href="' + BASE + '/prioritisation/fundamentals/">Take the fundamentals screen →</a>';
        t2html += '</div>';
        t2html += '<p class="tier-intro">Five upstream areas where evidence supports broad cross-domain effects. Working through them in this default order is a sensible plan if you are not sure where to begin.</p>';
        FUNDAMENTALS.forEach(function(card, i) {
            t2html += renderFundamentalsCard(card, i === 0);
        });
    } else {
        var triggeredFund = PERSONALISED_FUND_ORDER.filter(function(k) { return fundFlags && fundFlags[k]; });
        if (triggeredFund.length === 0) {
            t2html += '<div class="all-clear">';
            t2html += '<h3>Your fundamentals look in good shape.</h3>';
            t2html += '<p>You cleared the cutoffs on sleep, wellbeing, foundational finances, social connection, and physical activity. The next step in this section is cross-area prioritisation across the remaining ~50 life areas (Phase 3, in development).</p>';
            t2html += '<p>For now, <a href="' + BASE + '/life-areas/">browse all life areas</a> and pick what looks most relevant to you.</p>';
            t2html += '</div>';
        } else {
            t2html += '<p class="tier-intro">Based on your fundamentals screen, ' + (triggeredFund.length === 1 ? 'one area was' : triggeredFund.length + ' areas were') + ' below the cutoff worth flagging.</p>';
            triggeredFund.forEach(function(flag, i) {
                t2html += renderPersonalisedFundCard(flag, fundResponses, i === 0);
            });
        }
    }

    t2html += '</div>';
    document.getElementById('tier2Mount').innerHTML = t2html;

    // Tier 3
    document.getElementById('tier3Mount').innerHTML =
        '<div class="everything-else">If you would rather work on something else, browse <a href="' + BASE + '/life-areas/">all 52 life areas</a>. The recommendation above is a default, not a gate.</div>';
}

function renderFlagCard(key, val) {
    var c = FLAG_CONTENT[key];
    if (!c) return '';
    var titleText = (typeof c.title === 'function') ? c.title(val) : c.title;
    var classes = 'triage-card' + (c.acute ? ' acute' : '');
    var html = '<div class="' + classes + '">';
    html += '<h3>' + escapeHtml(titleText) + '</h3>';
    html += '<div class="body">' + escapeHtml(c.body) + '</div>';
    if (c.firstStep) html += '<div class="first-step">' + escapeHtml(c.firstStep) + '</div>';
    if (c.resources && c.resources.length) {
        html += '<div class="resources"><strong>Resources</strong><ul>';
        c.resources.forEach(function(r) {
            html += '<li><a href="' + r.href + '" target="_blank" rel="noopener">' + escapeHtml(r.label) + '</a></li>';
        });
        html += '</ul></div>';
    }
    html += '</div>';
    return html;
}

function renderFundamentalsCard(card, isFirst) {
    var classes = 'fundamentals-card' + (isFirst ? ' start-here' : '');
    var pretitle = isFirst ? 'We would suggest starting here' : 'Also worth addressing';
    var html = '<div class="' + classes + '">';
    html += '<div class="pretitle">' + escapeHtml(pretitle) + '</div>';
    html += '<h3>' + escapeHtml(card.title) + '</h3>';
    html += '<div class="body">' + escapeHtml(card.body) + '</div>';
    if (card.links && card.links.length) {
        html += '<div class="links">';
        card.links.forEach(function(l) {
            html += '<a href="' + l.href + '">' + escapeHtml(l.label) + '</a>';
        });
        html += '</div>';
    }
    html += '</div>';
    return html;
}

// ────────────────────────────────────────────────────────────────────────────
// Utilities
// ────────────────────────────────────────────────────────────────────────────

function escapeHtml(s) {
    if (s === undefined || s === null) return '';
    return String(s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

// React to cross-device sync arriving after page load
window.addEventListener('ap-storage-sync', function() {
    if (!document.getElementById('viewLanding').classList.contains('hidden')) {
        renderLanding();
    }
});

// Init
document.addEventListener('DOMContentLoaded', function() {
    answers = loadAnswers();
    var hash = window.location.hash;
    var hasAnyFlags = window.APStorage.load(STORAGE_FLAGS) || window.APStorage.load(FUND_FLAGS);
    if (hash === '#results' && hasAnyFlags) {
        viewResults();
    } else {
        renderLanding();
    }
});
</script>
