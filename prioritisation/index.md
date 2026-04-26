---
layout: default
title: Prioritisation
permalink: /prioritisation/
---

<style>
.research-box {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 24px 0;
    background: #fafafa;
}
.research-box summary {
    cursor: pointer;
    font-size: 0.95em;
    color: #333;
    padding: 4px 0;
}
.research-box summary strong { color: #155799; }
.research-box[open] summary {
    margin-bottom: 12px;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 12px;
}
.research-box ul { margin-bottom: 0; }
.in-development {
    color: #888;
    font-size: 0.85em;
    font-style: italic;
}

/* ── Phase 3 view container ── */
.ph3-view { max-width: 880px; margin: 0 auto; }
.hidden { display: none; }

/* CTAs and buttons */
.ph3-cta {
    margin: 32px 0;
    padding: 24px 28px;
    background: #f0f7ff;
    border-left: 4px solid #155799;
    border-radius: 6px;
}
.ph3-cta h2 { margin-top: 0; }
.ph3-cta .meta { color: #666; font-size: 0.9em; margin-top: 8px; }

.ph3-btn-primary {
    background: #155799;
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 12px 22px;
    font-size: 1em;
    cursor: pointer;
    font-weight: 600;
    margin-right: 8px;
    margin-top: 12px;
}
.ph3-btn-primary:hover { background: #0f4373; }
.ph3-btn-primary:disabled { background: #bdbdbd; cursor: not-allowed; }
.ph3-btn-secondary {
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
    margin-top: 12px;
}
.ph3-btn-secondary:hover { background: #f0f6fc; }
.ph3-btn-link {
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
    margin-top: 16px;
    font-size: 0.9em;
}

/* Progress */
.ph3-progress {
    margin-bottom: 20px;
}
.ph3-progress-outer {
    height: 8px;
    background: #e0e0e0;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 6px;
}
.ph3-progress-fill {
    height: 100%;
    background: #155799;
    border-radius: 4px;
    transition: width 0.3s ease;
}
.ph3-progress-info {
    display: flex;
    justify-content: space-between;
    font-size: 0.8em;
    color: #666;
}

/* PVQ + demographic shared card style */
.ph3-card {
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.ph3-card .q-section {
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.75em;
    color: #888;
    font-weight: 600;
    margin-bottom: 8px;
}
.ph3-card .q-text {
    font-size: 1.05em;
    color: #222;
    margin-bottom: 18px;
    line-height: 1.5;
}
.ph3-card .q-prompt {
    font-size: 0.85em;
    color: #666;
    margin-bottom: 12px;
    font-style: italic;
}

.ph3-radio {
    display: flex;
    align-items: center;
    padding: 11px 14px;
    margin-bottom: 6px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.12s;
    font-size: 0.95em;
    background: #fff;
}
.ph3-radio:hover { border-color: #155799; background: #f7fbff; }
.ph3-radio input[type="radio"] { margin-right: 10px; accent-color: #155799; }
.ph3-radio.selected { border-color: #155799; background: #e3f2fd; }

.ph3-input {
    padding: 10px 12px;
    border: 1px solid #c0c0c0;
    border-radius: 6px;
    font-size: 1em;
    width: 200px;
}

.ph3-nav-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 16px;
}

/* Constraint area list */
.ph3-constraint-header {
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.ph3-constraint-header h3 { margin-top: 0; margin-bottom: 8px; font-size: 1.15em; }
.ph3-constraint-header .help {
    color: #555;
    font-size: 0.9em;
    margin-bottom: 0;
}

.ph3-pillar {
    margin-bottom: 24px;
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    overflow: hidden;
}
.ph3-pillar-header {
    background: #f8f9fa;
    padding: 10px 16px;
    font-weight: 600;
    font-size: 0.95em;
    color: #222;
    border-bottom: 1px solid #e0e0e0;
}

.ph3-area-row {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 12px;
    align-items: center;
    padding: 10px 16px;
    border-bottom: 1px solid #f0f0f0;
}
.ph3-area-row:last-child { border-bottom: none; }
.ph3-area-info { min-width: 0; }
.ph3-area-name {
    font-weight: 600;
    color: #222;
    font-size: 0.95em;
}
.ph3-area-desc {
    color: #666;
    font-size: 0.82em;
    line-height: 1.35;
    margin-top: 2px;
}
.ph3-rate-buttons {
    display: flex;
    gap: 4px;
}
.ph3-rate-btn {
    width: 32px;
    height: 32px;
    border: 1px solid #d0d0d0;
    background: #fff;
    color: #666;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.9em;
    font-weight: 600;
    transition: all 0.1s;
}
.ph3-rate-btn:hover { border-color: #155799; color: #155799; }
.ph3-rate-btn.active {
    background: #155799;
    color: #fff;
    border-color: #155799;
}
.ph3-rate-btn.zero.active {
    background: #888;
    border-color: #888;
}

/* Results */
.ph3-binding-card {
    border: 2px solid #155799;
    background: #f0f7ff;
    border-radius: 12px;
    padding: 24px 28px;
    margin-bottom: 20px;
}
.ph3-binding-card .pretitle {
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.75em;
    color: #155799;
    font-weight: 600;
    margin-bottom: 6px;
}
.ph3-binding-card h2 {
    margin-top: 0;
    margin-bottom: 12px;
    font-size: 1.5em;
    color: #000;
}
.ph3-binding-card .reason {
    color: #444;
    font-size: 0.95em;
    line-height: 1.5;
    margin-bottom: 16px;
}
.ph3-binding-card .links a {
    margin-right: 14px;
    font-weight: 600;
}

.ph3-successor {
    border: 1px solid #e0e0e0;
    background: #fff;
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 12px;
}
.ph3-successor .pretitle {
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.7em;
    color: #888;
    font-weight: 600;
    margin-bottom: 4px;
}
.ph3-successor h3 {
    margin: 0 0 6px 0;
    font-size: 1.05em;
    color: #222;
}
.ph3-successor .reason {
    color: #555;
    font-size: 0.88em;
    margin-bottom: 8px;
}
.ph3-successor .links a {
    font-size: 0.88em;
    margin-right: 10px;
}

.ph3-override {
    margin-top: 32px;
    padding-top: 20px;
    border-top: 1px solid #e0e0e0;
}
.ph3-override h3 { font-size: 1.05em; margin-bottom: 8px; }
.ph3-override-list {
    margin-top: 12px;
    max-height: 480px;
    overflow-y: auto;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    padding: 8px;
    background: #fafafa;
}
.ph3-override-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 6px 10px;
    border-bottom: 1px solid #ececec;
    font-size: 0.9em;
}
.ph3-override-row:last-child { border-bottom: none; }
.ph3-override-row .pin-btn {
    background: none;
    border: 1px solid #155799;
    color: #155799;
    border-radius: 4px;
    padding: 3px 10px;
    font-size: 0.82em;
    cursor: pointer;
}
.ph3-override-row.pinned { background: #e3f2fd; }

.ph3-balanced {
    background: #f0f7f0;
    border-left: 4px solid #28a745;
    border-radius: 4px;
    padding: 18px 22px;
    margin-bottom: 20px;
}
.ph3-balanced h2 { margin-top: 0; color: #1d6f30; font-size: 1.2em; }

@media (max-width: 600px) {
    .ph3-area-row {
        grid-template-columns: 1fr;
        gap: 8px;
    }
    .ph3-rate-buttons { justify-content: flex-start; }
}
</style>

<div id="viewOverview" class="ph3-view" markdown="1">

# Prioritisation

The framework covers around fifty life areas across five pillars. This section helps you decide which to work on first.

It is distinct from [Quick Wins]({{ site.baseurl }}/prioritisation/quick-wins/) <span class="in-development">(in development)</span>, which surfaces high-impact, low-effort actions for momentum, and from intervention-level scoring, which prioritises *within* an area. Choosing areas and choosing interventions are different problems and we treat them separately.

## What we recommend, and why

We recommend addressing fundamentals before pursuing goal-directed areas, because the evidence suggests gains here compound into everything else. You can override this if your situation differs.

That's the headline. The system is non-prescriptive. It offers a recommended default order based on what tends to enable flourishing, but you are free to ignore the recommendation and work on any area you choose. The value is the considered judgement – here is what we think and why – not gatekeeping. Wherever you see a recommendation in this section, the path to "show me everything else instead" is one click away.

The one exception is triage. Where a response indicates a serious mental health, safety, or material issue, we surface it with weight. Acute issues warrant clear pointing to evidence-based first steps and professional resources. That recommendation is still not a gate – the rest of the site remains accessible – but it does not read as one option among many.

<details class="research-box">
<summary><strong>Where the prioritisation research stands</strong> – how we decide what to recommend first, and why this is genuinely an open question</summary>

There is no unified academic framework for prioritising across all areas of personal life. The closest analogues each capture part of the picture.

- **Maslow's hierarchy** (1943) is widely cited but empirically weak. [Tay and Diener (2011)](https://psycnet.apa.org/doi/10.1037/a0023779) showed across 123 countries that needs are pursued in parallel, not sequence. We do not use it as a model.
- **Theory of Constraints** (Goldratt, 1984), drawn from operations management, holds that a system's output is gated by its weakest critical link. Applied to life, this means identifying and addressing the binding constraint before optimising elsewhere.
- **Self-Determination Theory** ([Deci and Ryan, 2000](https://selfdeterminationtheory.org/)) identifies three core psychological needs – autonomy, competence, and relatedness – alongside physical needs. Better supported than Maslow.
- **The Wheel of Life**, a coaching tool, asks you to self-rate eight to ten areas and work on the lowest. Intuitive but limited by poor self-assessment.
- **ITN** (Importance, Tractability, Neglectedness), developed by effective altruists for cause selection, adapts reasonably to personal areas.
- **Hedonic adaptation research** ([Lyubomirsky and others](https://lyubomirskylab.com/)) shows that relationships, autonomy, meaning, and mastery produce lasting wellbeing returns. Income beyond roughly $75,000–100,000 household and most possessions adapt away ([Killingsworth, 2021](https://www.pnas.org/doi/10.1073/pnas.2016976118)).

This site combines these into a three-stage approach: triage acute issues, recommend fundamentals where you have significant gaps, then prioritise across remaining areas. The values input draws on Schwartz's [theory of basic human values](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/) (validated across 80+ countries) and the constraint identification draws on Theory of Constraints. This is a reasoned synthesis, not a validated single framework, and we will update it as the literature develops.

</details>

## The three-stage approach

**Stage 1 – Triage.** A short ten-question screen surfaces serious issues that warrant attention before general optimisation content is useful: significant depression or anxiety symptoms, immediate safety concerns, financial or housing distress, substance use, food insecurity, and acute carer strain. Where something flags, the result names the issue plainly, points to an evidence-based first step, and signposts professional resources. The site does first-step orientation and signposting, not treatment.

**Stage 2 – Fundamentals.** Five upstream areas have evidence of broad cross-domain effects: sleep, mental health, foundational finances, key relationships and social connection, and physical activity and nutrition. Where you have a significant gap in one of these, we recommend starting there. An optional five-minute screen personalises which fundamentals are surfaced based on validated short-form measures (WHO-5 for wellbeing, UCLA-3 for loneliness, plus single behavioural items). Each cutoff is documented with the underlying evidence in the [fundamentals cutoffs reference]({{ site.baseurl }}/methodology/fundamentals-cutoffs/).

**Stage 3 – Find your focus area.** Once fundamentals are addressed, or you have chosen to skip them, the system identifies a single binding life area to focus on next. This is based on what you value (the validated 21-item Schwartz Portrait Values Questionnaire) combined with where you currently feel constrained across the framework's 52 life areas. Output is one focus area with a stated reason, plus two named successors. About 12 minutes.

</div>

<div id="ph3CtaContainer" class="ph3-view" markdown="1">
<div class="ph3-cta" markdown="0">
<h2>Find your focus area</h2>
<p>A 12-minute screen that combines what you value (Schwartz PVQ-21, 21 items) with where you currently feel most constrained across the 52 life areas. Surfaces one binding focus area, plus two successors. Designed to be taken after the <a href="{{ site.baseurl }}/prioritisation/triage/">triage</a> and <a href="{{ site.baseurl }}/prioritisation/fundamentals/">fundamentals</a> screens, but works on its own.</p>
<button class="ph3-btn-primary" onclick="ph3Start()">Start</button>
<div class="meta">21 values items + 4 constraint pages, about 12 minutes.</div>
<div id="ph3PriorBanner" class="prior-banner hidden">
<div id="ph3PriorBannerText"></div>
<button class="ph3-btn-link" onclick="ph3ViewResults()" style="padding-left:0;">View your results</button>
</div>
</div>

## Where else to go in this section

[Take the triage screen]({{ site.baseurl }}/prioritisation/triage/) – about five minutes; surfaces issues worth attending to before broader optimisation.

[Personalise your fundamentals]({{ site.baseurl }}/prioritisation/fundamentals/) – about five more minutes; reorders and filters the fundamentals layer of your results based on a 14-question screen.

[Take the level assessment]({{ site.baseurl }}/prioritisation/dashboard/) – assesses your current level across all life areas.

[Browse all life areas]({{ site.baseurl }}/life-areas/) – if you already know what you want to work on.
</div>

<div id="viewDemographics" class="ph3-view hidden">
  <div class="ph3-progress">
    <div class="ph3-progress-outer"><div class="ph3-progress-fill" style="width:5%"></div></div>
    <div class="ph3-progress-info">
      <span>Step 1 of 4 – about you</span>
      <button class="ph3-btn-link" onclick="ph3ExitToOverview()" style="padding:0;">Exit</button>
    </div>
  </div>
  <div class="ph3-card">
    <div class="q-section">About you</div>
    <div class="q-prompt">This helps us present the values items in a form that fits you.</div>
    <p style="margin: 0 0 10px 0; font-weight: 600;">Your age</p>
    <input type="number" id="demoAge" min="13" max="120" class="ph3-input" placeholder="e.g. 35">
    <p style="margin: 18px 0 10px 0; font-weight: 600;">Your gender (used to match pronouns in the values items)</p>
    <div id="demoGenderOptions"></div>
  </div>
  <div class="ph3-nav-row">
    <button class="ph3-btn-secondary" onclick="ph3ExitToOverview()">Back</button>
    <button class="ph3-btn-primary" id="demoNext" onclick="ph3GoToPvq()" disabled>Continue</button>
  </div>
</div>

<div id="viewPvq" class="ph3-view hidden">
  <div class="ph3-progress">
    <div class="ph3-progress-outer"><div class="ph3-progress-fill" id="pvqProgressFill"></div></div>
    <div class="ph3-progress-info">
      <span id="pvqProgressText">Step 2 of 4 – values, item 1 of 21</span>
      <button class="ph3-btn-link" onclick="ph3ExitToOverview()" style="padding:0;">Exit</button>
    </div>
  </div>
  <div id="pvqMount"></div>
  <div class="ph3-nav-row">
    <button class="ph3-btn-secondary" id="pvqBack" onclick="ph3PvqBack()">Back</button>
    <button class="ph3-btn-primary" id="pvqNext" onclick="ph3PvqNext()" disabled>Next</button>
  </div>
</div>

<div id="viewConstraints" class="ph3-view hidden">
  <div class="ph3-progress">
    <div class="ph3-progress-outer"><div class="ph3-progress-fill" id="conProgressFill"></div></div>
    <div class="ph3-progress-info">
      <span id="conProgressText">Step 3 of 4 – constraints, page 1 of 4</span>
      <button class="ph3-btn-link" onclick="ph3ExitToOverview()" style="padding:0;">Exit</button>
    </div>
  </div>
  <div id="conMount"></div>
  <div class="ph3-nav-row">
    <button class="ph3-btn-secondary" id="conBack" onclick="ph3ConBack()">Back</button>
    <button class="ph3-btn-primary" id="conNext" onclick="ph3ConNext()">Next</button>
  </div>
</div>

<div id="viewResults" class="ph3-view hidden">
  <h1 style="margin-bottom: 6px;">Your focus area</h1>
  <p style="color: #555; margin-top: 0;">Computed from your values (Schwartz PVQ-21) and the four constraint signals.</p>
  <div id="resultsMount"></div>
  <div style="margin-top: 30px; padding-top: 16px; border-top: 1px solid #e0e0e0; text-align: center;">
    <button class="ph3-btn-link" onclick="ph3Start()">Retake</button>
    <button class="ph3-btn-link" onclick="ph3ExitToOverview()">Back to overview</button>
  </div>
</div>

<script>
// ────────────────────────────────────────────────────────────────────────────
// Data dumped from Liquid at build time
// ────────────────────────────────────────────────────────────────────────────

var PVQ = {{ site.data.pvq21 | jsonify }};
var AREA_VALUES = {{ site.data["area-value-mapping"] | jsonify }};

var LIFE_AREAS = [
{% assign sorted_areas = site.data.life_areas | sort %}
{% for area in sorted_areas %}{% assign d = area[1] %}  { slug: {{ area[0] | jsonify }}, name: {{ d.name | jsonify }}, pillar: {{ d.pillar | jsonify }}, domain: {{ d.domain | jsonify }}, desc: {{ d.survey_description | jsonify }} }{% unless forloop.last %},{% endunless %}
{% endfor %}];

var PILLAR_ORDER = ['Expand Your Awareness', 'Look After Yourself', 'Connect with Others', 'Organise Your Life', 'Create & Contribute'];

var BASE = '{{ site.baseurl }}';

// ────────────────────────────────────────────────────────────────────────────
// Schwartz value friendly labels
// ────────────────────────────────────────────────────────────────────────────

var VALUE_LABELS = {
    'self-direction': 'independence and creativity',
    'power': 'status and resources',
    'universalism': 'fairness and the wider world',
    'achievement': 'success and recognition',
    'security': 'stability and safety',
    'stimulation': 'variety and excitement',
    'conformity': 'following expectations',
    'hedonism': 'pleasure and enjoyment',
    'benevolence': 'caring for those close to you',
    'tradition': 'continuity and cultural belonging'
};

// ────────────────────────────────────────────────────────────────────────────
// Constraint questions
// ────────────────────────────────────────────────────────────────────────────

var CONSTRAINT_QUESTIONS = [
    {
        id: 'cost',
        title: 'Disproportionate cost',
        question: 'Which areas of your life feel like they are absorbing more time, energy, or money than they are returning to you?',
        help: 'Leave at 0 anything that does not apply. Use 1–3 to indicate how strongly the area is over-costing you (1 = a bit, 2 = quite a lot, 3 = a major drain).'
    },
    {
        id: 'upside',
        title: 'Counterfactual upside',
        question: 'If one or two areas dramatically improved, where would the gains feel most transformative?',
        help: 'Use 1–3 for areas where improvement would meaningfully change your life (1 = noticeable, 2 = significant, 3 = transformative).'
    },
    {
        id: 'friction',
        title: 'Current friction',
        question: 'Where in your life do you most often feel stuck, frustrated, or held back?',
        help: 'Use 1–3 for areas that frustrate you (1 = occasional, 2 = frequent, 3 = constant).'
    },
    {
        id: 'underinvest',
        title: 'Underinvestment',
        question: 'Where do you feel you are putting in less than the area deserves, given how much it matters to you?',
        help: 'Use 1–3 for areas that you are neglecting relative to their importance (1 = a little, 2 = significantly, 3 = severely).'
    }
];

var CONSTRAINT_LABELS = {
    cost: 'is costing more than it returns',
    upside: 'would unlock big improvements',
    friction: 'is currently the most frustrating',
    underinvest: 'is under-attended given how much it matters'
};

// ────────────────────────────────────────────────────────────────────────────
// Storage
// ────────────────────────────────────────────────────────────────────────────

var KEY_DEMO   = 'ap-prioritisation-demographics';
var KEY_PVQ    = 'ap-prioritisation-pvq';
var KEY_CON    = 'ap-prioritisation-constraints';
var KEY_FLAGS  = 'ap-prioritisation-flags';
var KEY_DONE   = 'ap-prioritisation-completed-at';

function load(k) { return window.APStorage.load(k); }
function save(k, v) { window.APStorage.save(k, v); }

// ────────────────────────────────────────────────────────────────────────────
// State
// ────────────────────────────────────────────────────────────────────────────

var demographics = { age: null, gender: null };
var pvqAnswers = {};
var pvqIndex = 0;
var constraintAnswers = { cost: {}, upside: {}, friction: {}, underinvest: {} };
var constraintPage = 0;

// ────────────────────────────────────────────────────────────────────────────
// View switching
// ────────────────────────────────────────────────────────────────────────────

function showView(name) {
    var ids = ['Overview', 'Demographics', 'Pvq', 'Constraints', 'Results'];
    ids.forEach(function(v) {
        var el = document.getElementById('view' + v);
        if (el) el.classList.toggle('hidden', v !== name);
    });
    var ctaContainer = document.getElementById('ph3CtaContainer');
    if (ctaContainer) ctaContainer.classList.toggle('hidden', name !== 'Overview');
    window.scrollTo(0, 0);
}

// ────────────────────────────────────────────────────────────────────────────
// Overview
// ────────────────────────────────────────────────────────────────────────────

function ph3RenderOverview() {
    var doneAt = load(KEY_DONE);
    var banner = document.getElementById('ph3PriorBanner');
    if (doneAt) {
        var dateStr;
        try {
            dateStr = new Intl.DateTimeFormat('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }).format(new Date(doneAt));
        } catch (e) { dateStr = doneAt.split('T')[0]; }
        document.getElementById('ph3PriorBannerText').textContent = 'You completed this on ' + dateStr + '.';
        banner.classList.remove('hidden');
    } else {
        banner.classList.add('hidden');
    }
    showView('Overview');
}

function ph3ExitToOverview() {
    ph3RenderOverview();
}

function ph3Start() {
    demographics = { age: null, gender: null };
    pvqAnswers = {};
    pvqIndex = 0;
    constraintAnswers = { cost: {}, upside: {}, friction: {}, underinvest: {} };
    constraintPage = 0;
    ph3RenderDemographics();
    showView('Demographics');
}

function ph3ViewResults() {
    var savedDemo = load(KEY_DEMO);
    var savedPvq  = load(KEY_PVQ);
    var savedCon  = load(KEY_CON);
    if (!savedDemo || !savedPvq || !savedCon) {
        ph3Start();
        return;
    }
    demographics = savedDemo;
    pvqAnswers = savedPvq;
    constraintAnswers = savedCon;
    ph3RenderResults();
    showView('Results');
}

// ────────────────────────────────────────────────────────────────────────────
// Demographics
// ────────────────────────────────────────────────────────────────────────────

function ph3RenderDemographics() {
    var ageInput = document.getElementById('demoAge');
    if (demographics.age) ageInput.value = demographics.age;
    ageInput.oninput = ph3ValidateDemo;

    var genderHtml = '';
    var opts = [
        { value: 'male', label: 'Male' },
        { value: 'female', label: 'Female' },
        { value: 'they', label: 'Non-binary' },
        { value: 'they', label: 'Prefer not to say' }
    ];
    opts.forEach(function(o, i) {
        var id = 'demoGender_' + i;
        var checked = demographics.gender === o.value && demographics.genderLabel === o.label ? 'checked' : '';
        var sel = checked ? ' selected' : '';
        genderHtml += '<label class="ph3-radio' + sel + '" for="' + id + '">';
        genderHtml += '<input type="radio" name="demoGender" id="' + id + '" value="' + o.value + '" data-label="' + o.label + '" ' + checked + ' onchange="ph3SetGender(\'' + o.value + '\', \'' + o.label + '\')">';
        genderHtml += '<span>' + o.label + '</span>';
        genderHtml += '</label>';
    });
    document.getElementById('demoGenderOptions').innerHTML = genderHtml;
    ph3ValidateDemo();
}

function ph3SetGender(v, label) {
    demographics.gender = v;
    demographics.genderLabel = label;
    var radios = document.querySelectorAll('label.ph3-radio');
    radios.forEach(function(r) { r.classList.remove('selected'); });
    var picked = document.querySelector('input[name="demoGender"][data-label="' + label + '"]');
    if (picked && picked.parentNode) picked.parentNode.classList.add('selected');
    ph3ValidateDemo();
}

function ph3ValidateDemo() {
    var ageVal = parseInt(document.getElementById('demoAge').value, 10);
    if (!isNaN(ageVal) && ageVal >= 13 && ageVal <= 120) demographics.age = ageVal;
    var ok = demographics.age && demographics.gender;
    document.getElementById('demoNext').disabled = !ok;
}

function ph3GoToPvq() {
    save(KEY_DEMO, demographics);
    pvqIndex = 0;
    ph3RenderPvq();
    showView('Pvq');
}

// ────────────────────────────────────────────────────────────────────────────
// PVQ
// ────────────────────────────────────────────────────────────────────────────

function ph3RenderPvq() {
    var item = PVQ.items[pvqIndex];
    var portrait = item[demographics.gender] || item.male;
    var total = PVQ.items.length;
    document.getElementById('pvqProgressText').textContent = 'Step 2 of 4 – values, item ' + (pvqIndex + 1) + ' of ' + total;
    document.getElementById('pvqProgressFill').style.width = (5 + 45 * pvqIndex / total) + '%';

    var html = '<div class="ph3-card">';
    html += '<div class="q-section">' + escapeHtml(PVQ.intro) + '</div>';
    html += '<div class="q-text">' + escapeHtml(portrait) + '</div>';
    html += '<div class="q-prompt"><strong>' + escapeHtml(PVQ.prompt) + '</strong></div>';
    var current = pvqAnswers[item.id];
    PVQ.scale.forEach(function(s, i) {
        var checked = (current === s.value) ? 'checked' : '';
        var sel     = (current === s.value) ? ' selected' : '';
        var optId = 'pvqOpt_' + i;
        html += '<label class="ph3-radio' + sel + '" for="' + optId + '">';
        html += '<input type="radio" name="pvqOpt" id="' + optId + '" value="' + s.value + '" ' + checked + ' onchange="ph3PvqAnswer(' + s.value + ')">';
        html += '<span>' + escapeHtml(s.label) + '</span>';
        html += '</label>';
    });
    html += '</div>';
    document.getElementById('pvqMount').innerHTML = html;

    document.getElementById('pvqBack').disabled = (pvqIndex === 0);
    document.getElementById('pvqNext').disabled = (current === undefined);
    document.getElementById('pvqNext').textContent = (pvqIndex === total - 1) ? 'Next: constraints' : 'Next';
}

function ph3PvqAnswer(value) {
    var item = PVQ.items[pvqIndex];
    pvqAnswers[item.id] = value;
    save(KEY_PVQ, pvqAnswers);
    var labels = document.querySelectorAll('#pvqMount label.ph3-radio');
    labels.forEach(function(l) { l.classList.remove('selected'); });
    var picked = document.querySelector('input[name="pvqOpt"][value="' + value + '"]');
    if (picked && picked.parentNode) picked.parentNode.classList.add('selected');
    document.getElementById('pvqNext').disabled = false;
}

function ph3PvqNext() {
    if (pvqIndex < PVQ.items.length - 1) {
        pvqIndex += 1;
        ph3RenderPvq();
    } else {
        ph3RenderConstraints();
        showView('Constraints');
    }
}

function ph3PvqBack() {
    if (pvqIndex > 0) { pvqIndex -= 1; ph3RenderPvq(); }
    else { ph3RenderDemographics(); showView('Demographics'); }
}

// ────────────────────────────────────────────────────────────────────────────
// Constraints
// ────────────────────────────────────────────────────────────────────────────

function areasByPillar() {
    var byPillar = {};
    LIFE_AREAS.forEach(function(a) {
        if (!byPillar[a.pillar]) byPillar[a.pillar] = [];
        byPillar[a.pillar].push(a);
    });
    return byPillar;
}

function ph3RenderConstraints() {
    var q = CONSTRAINT_QUESTIONS[constraintPage];
    var totalPages = CONSTRAINT_QUESTIONS.length;
    document.getElementById('conProgressText').textContent = 'Step 3 of 4 – constraints, page ' + (constraintPage + 1) + ' of ' + totalPages;
    document.getElementById('conProgressFill').style.width = (50 + 40 * constraintPage / totalPages) + '%';

    var html = '<div class="ph3-constraint-header">';
    html += '<h3>' + escapeHtml(q.title) + '</h3>';
    html += '<p style="margin: 0 0 8px 0;"><strong>' + escapeHtml(q.question) + '</strong></p>';
    html += '<p class="help">' + escapeHtml(q.help) + '</p>';
    html += '</div>';

    var byPillar = areasByPillar();
    PILLAR_ORDER.forEach(function(pillar) {
        var areas = byPillar[pillar] || [];
        if (!areas.length) return;
        html += '<div class="ph3-pillar">';
        html += '<div class="ph3-pillar-header">' + escapeHtml(pillar) + '</div>';
        areas.forEach(function(a) {
            var current = constraintAnswers[q.id][a.slug] || 0;
            html += '<div class="ph3-area-row">';
            html += '<div class="ph3-area-info">';
            html += '<div class="ph3-area-name">' + escapeHtml(a.name) + '</div>';
            html += '<div class="ph3-area-desc">' + escapeHtml(a.desc) + '</div>';
            html += '</div>';
            html += '<div class="ph3-rate-buttons">';
            for (var i = 0; i <= 3; i++) {
                var cls = 'ph3-rate-btn' + (i === 0 ? ' zero' : '') + (current === i ? ' active' : '');
                html += '<button type="button" class="' + cls + '" data-area="' + a.slug + '" data-rating="' + i + '" onclick="ph3SetRating(\'' + q.id + '\', \'' + a.slug + '\', ' + i + ')">' + i + '</button>';
            }
            html += '</div></div>';
        });
        html += '</div>';
    });

    document.getElementById('conMount').innerHTML = html;

    document.getElementById('conBack').disabled = false;
    document.getElementById('conNext').textContent = (constraintPage === totalPages - 1) ? 'See results' : 'Next';
}

function ph3SetRating(questionId, areaSlug, rating) {
    if (rating === 0) {
        delete constraintAnswers[questionId][areaSlug];
    } else {
        constraintAnswers[questionId][areaSlug] = rating;
    }
    save(KEY_CON, constraintAnswers);
    // Update the visual state of just this row's buttons
    var btns = document.querySelectorAll('.ph3-rate-btn[data-area="' + areaSlug + '"]');
    btns.forEach(function(b) {
        var r = parseInt(b.getAttribute('data-rating'), 10);
        b.classList.toggle('active', r === rating);
    });
}

function ph3ConNext() {
    if (constraintPage < CONSTRAINT_QUESTIONS.length - 1) {
        constraintPage += 1;
        ph3RenderConstraints();
        window.scrollTo(0, 0);
    } else {
        ph3FinishConstraints();
    }
}

function ph3ConBack() {
    if (constraintPage > 0) {
        constraintPage -= 1;
        ph3RenderConstraints();
        window.scrollTo(0, 0);
    } else {
        pvqIndex = PVQ.items.length - 1;
        ph3RenderPvq();
        showView('Pvq');
    }
}

function ph3FinishConstraints() {
    var ranked = ph3ComputeScores();
    var flags = ph3DetermineFlags(ranked);
    save(KEY_FLAGS, flags);
    save(KEY_DONE, new Date().toISOString());
    ph3RenderResults();
    showView('Results');
}

// ────────────────────────────────────────────────────────────────────────────
// Scoring
// ────────────────────────────────────────────────────────────────────────────

function pvqScoreForValue(valueKey) {
    var ids = PVQ.items_by_value[valueKey] || [];
    if (!ids.length) return 0;
    var sum = 0, count = 0;
    ids.forEach(function(id) {
        var v = pvqAnswers[id];
        if (typeof v === 'number') { sum += v; count += 1; }
    });
    return count ? sum / count : 0;
}

function importanceForArea(slug) {
    var values = (AREA_VALUES[slug] && AREA_VALUES[slug].values) || [];
    var total = 0;
    values.forEach(function(v) { total += pvqScoreForValue(v); });
    return total;
}

function constraintForArea(slug) {
    var total = 0;
    CONSTRAINT_QUESTIONS.forEach(function(q) {
        total += (constraintAnswers[q.id][slug] || 0);
    });
    return total;
}

function ph3ComputeScores() {
    var ranked = LIFE_AREAS.map(function(a) {
        var imp = importanceForArea(a.slug);
        var con = constraintForArea(a.slug);
        return {
            slug: a.slug,
            name: a.name,
            pillar: a.pillar,
            domain: a.domain,
            importance: imp,
            constraint: con,
            score: imp * con
        };
    });
    ranked.sort(function(a, b) { return b.score - a.score; });
    return ranked;
}

function ph3DetermineFlags(ranked) {
    var prevFlags = load(KEY_FLAGS) || {};
    var top = ranked[0];
    var balanced = false;

    if (!top || top.score === 0) {
        balanced = true;
    } else {
        var t1 = ranked[0].score;
        var t3 = ranked[2] ? ranked[2].score : 0;
        if (t3 > 0 && (t1 - t3) / t1 < 0.10) balanced = true;
    }

    return {
        binding: top ? top.slug : null,
        successors: [ranked[1] ? ranked[1].slug : null, ranked[2] ? ranked[2].slug : null].filter(Boolean),
        balanced: balanced,
        pinned: prevFlags.pinned || null,
        ranked: ranked.slice(0, 52).map(function(r) {
            return { slug: r.slug, score: Math.round(r.score * 10) / 10, importance: Math.round(r.importance * 10) / 10, constraint: r.constraint };
        })
    };
}

// ────────────────────────────────────────────────────────────────────────────
// Results
// ────────────────────────────────────────────────────────────────────────────

function findArea(slug) {
    for (var i = 0; i < LIFE_AREAS.length; i++) if (LIFE_AREAS[i].slug === slug) return LIFE_AREAS[i];
    return null;
}

function reasonForArea(slug) {
    // Identify the user's top values that this area matches
    var areaValues = (AREA_VALUES[slug] && AREA_VALUES[slug].values) || [];
    var valuesScored = areaValues.map(function(v) { return { v: v, score: pvqScoreForValue(v) }; })
                                  .sort(function(a, b) { return b.score - a.score; });
    var topValues = valuesScored.filter(function(x) { return x.score >= 4 }).slice(0, 2);

    // Identify the user's strongest constraint signal for this area
    var topConstraint = null, topConstraintRating = 0;
    CONSTRAINT_QUESTIONS.forEach(function(q) {
        var r = constraintAnswers[q.id][slug] || 0;
        if (r > topConstraintRating) { topConstraintRating = r; topConstraint = q.id; }
    });

    var parts = [];
    if (topValues.length) {
        var labels = topValues.map(function(x) { return VALUE_LABELS[x.v]; });
        parts.push('it matches ' + (labels.length === 1 ? 'your value of ' + labels[0] : 'your values of ' + labels.join(' and ')));
    }
    if (topConstraint) {
        parts.push('it ' + CONSTRAINT_LABELS[topConstraint]);
    }
    if (!parts.length) return 'It scored highest on the combined values and constraint signals.';
    return 'Surfaced because ' + parts.join(', and ') + '.';
}

function ph3RenderResults() {
    var flags = load(KEY_FLAGS) || ph3DetermineFlags(ph3ComputeScores());
    var html = '';

    if (flags.balanced && !flags.pinned) {
        html += '<div class="ph3-balanced">';
        html += '<h2>Your priorities look balanced.</h2>';
        html += '<p>No single area stood out as clearly more constraining than the others. The top three by score are below. Pick whichever feels most relevant to start with – any of them is a defensible choice.</p>';
        html += '</div>';
        var topThree = [flags.binding].concat(flags.successors).filter(Boolean);
        topThree.forEach(function(slug) { html += renderSuccessor(slug); });
    } else {
        var bindingSlug = flags.pinned || flags.binding;
        if (bindingSlug) html += renderBinding(bindingSlug, flags.pinned ? flags.binding : null);
        flags.successors.forEach(function(slug) {
            if (slug !== bindingSlug) html += renderSuccessor(slug);
        });
        if (flags.pinned && flags.binding && flags.binding !== flags.pinned) {
            // Show the originally computed binding as a successor
            html += renderSuccessor(flags.binding);
        }
    }

    // Override section
    html += '<div class="ph3-override">';
    html += '<h3>Pick a different focus area</h3>';
    html += '<p style="font-size: 0.9em; color: #555;">All 52 areas ranked by combined score. Click a row to pin that as your focus area instead.</p>';
    html += '<div class="ph3-override-list">';
    flags.ranked.forEach(function(r) {
        var area = findArea(r.slug);
        if (!area) return;
        var pinned = (flags.pinned === r.slug);
        html += '<div class="ph3-override-row' + (pinned ? ' pinned' : '') + '">';
        html += '<span><strong>' + escapeHtml(area.name) + '</strong> <span style="color:#888; font-size: 0.85em;">' + escapeHtml(area.pillar) + '</span></span>';
        html += '<span style="color:#888; font-size: 0.85em; margin-left: auto; margin-right: 12px;">score ' + r.score + '</span>';
        html += '<button class="pin-btn" onclick="ph3Pin(\'' + r.slug + '\')">' + (pinned ? 'Pinned' : 'Pin') + '</button>';
        html += '</div>';
    });
    html += '</div>';
    if (flags.pinned) html += '<p style="margin-top: 10px;"><button class="ph3-btn-link" onclick="ph3Unpin()" style="padding-left: 0;">Clear pin</button></p>';
    html += '</div>';

    document.getElementById('resultsMount').innerHTML = html;
}

function renderBinding(slug, computedBindingIfDifferent) {
    var area = findArea(slug);
    if (!area) return '';
    var html = '<div class="ph3-binding-card">';
    html += '<div class="pretitle">' + (computedBindingIfDifferent ? 'You pinned' : 'Your focus area') + '</div>';
    html += '<h2>' + escapeHtml(area.name) + '</h2>';
    html += '<div class="reason">' + escapeHtml(reasonForArea(slug)) + '</div>';
    html += '<div class="reason"><em>' + escapeHtml(area.desc) + '</em></div>';
    html += '<div class="links"><a href="' + BASE + '/' + area.slug + '/">Read the ' + escapeHtml(area.name) + ' guide</a></div>';
    html += '</div>';
    return html;
}

function renderSuccessor(slug) {
    var area = findArea(slug);
    if (!area) return '';
    var html = '<div class="ph3-successor">';
    html += '<div class="pretitle">Next likely focus once this one clears</div>';
    html += '<h3>' + escapeHtml(area.name) + '</h3>';
    html += '<div class="reason">' + escapeHtml(reasonForArea(slug)) + '</div>';
    html += '<div class="links"><a href="' + BASE + '/' + area.slug + '/">Read the ' + escapeHtml(area.name) + ' guide</a></div>';
    html += '</div>';
    return html;
}

function ph3Pin(slug) {
    var flags = load(KEY_FLAGS) || {};
    flags.pinned = slug;
    save(KEY_FLAGS, flags);
    ph3RenderResults();
    window.scrollTo(0, 0);
}

function ph3Unpin() {
    var flags = load(KEY_FLAGS) || {};
    flags.pinned = null;
    save(KEY_FLAGS, flags);
    ph3RenderResults();
    window.scrollTo(0, 0);
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

window.addEventListener('ap-storage-sync', function() {
    if (!document.getElementById('viewOverview').classList.contains('hidden')) {
        ph3RenderOverview();
    }
});

document.addEventListener('DOMContentLoaded', function() {
    ph3RenderOverview();
});
</script>
