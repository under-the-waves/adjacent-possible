---
layout: default
title: Prioritisation
permalink: /prioritisation/
---

<style>
.prio { max-width: 880px; margin: 0 auto; }
.hidden { display: none; }

/* Buttons */
.btn-primary {
    background: #155799; color: #fff; border: none;
    border-radius: 6px; padding: 12px 22px; font-size: 1em;
    cursor: pointer; font-weight: 600;
}
.btn-primary:hover { background: #0f4373; }
.btn-primary:disabled { background: #bdbdbd; cursor: not-allowed; }
.btn-secondary {
    background: #fff; color: #155799;
    border: 1px solid #155799; border-radius: 6px;
    padding: 10px 18px; font-size: 0.9em;
    cursor: pointer; font-weight: 600;
    text-decoration: none; display: inline-block;
}
.btn-secondary:hover { background: #f0f6fc; }
.btn-link {
    background: none; border: none; color: #155799;
    cursor: pointer; text-decoration: underline;
    padding: 4px 8px; font-size: 0.9em;
}

/* Stage roadmap on landing */
.stage-list { margin: 28px 0; }
.stage-row {
    display: grid;
    grid-template-columns: 28px 1fr auto;
    gap: 14px; align-items: start;
    padding: 14px 0;
    border-bottom: 1px solid #e8e8e8;
}
.stage-row:last-child { border-bottom: none; }
.stage-num {
    background: #155799; color: #fff;
    width: 26px; height: 26px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.85em; font-weight: 600;
}
.stage-title { font-weight: 600; color: #222; margin-bottom: 4px; }
.stage-desc { color: #555; font-size: 0.92em; line-height: 1.45; }
.stage-meta { color: #888; font-size: 0.82em; margin-top: 4px; }
.stage-skip {
    background: none; border: none;
    color: #155799; font-size: 0.85em;
    text-decoration: underline; cursor: pointer;
    padding: 4px 0; white-space: nowrap;
}

.start-row { margin-top: 20px; display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }
.start-row .meta { color: #888; font-size: 0.85em; }

.prior-banner {
    background: #f5f5f5; border-left: 4px solid #888;
    border-radius: 4px; padding: 12px 16px;
    margin: 16px 0; font-size: 0.9em;
}
.prior-banner .actions { margin-top: 8px; }

/* Progress bar */
.progress-bar { margin-bottom: 24px; }
.progress-outer {
    height: 8px; background: #e0e0e0;
    border-radius: 4px; overflow: hidden;
    margin-bottom: 6px;
}
.progress-fill {
    height: 100%; background: #155799;
    border-radius: 4px; transition: width 0.3s ease;
}
.progress-info {
    display: flex; justify-content: space-between;
    font-size: 0.8em; color: #666;
}

/* Question card */
.q-card {
    background: #fff; border: 1px solid #e0e0e0;
    border-radius: 12px; padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.q-section {
    text-transform: uppercase; letter-spacing: 0.5px;
    font-size: 0.75em; color: #888;
    font-weight: 600; margin-bottom: 8px;
}
.q-text {
    font-size: 1.05em; color: #222;
    margin-bottom: 18px; line-height: 1.5;
}
.q-prompt {
    font-size: 0.85em; color: #666;
    margin-bottom: 12px; font-style: italic;
}
.radio-option {
    display: flex; align-items: center;
    padding: 11px 14px; margin-bottom: 6px;
    border: 1px solid #e0e0e0; border-radius: 8px;
    cursor: pointer; transition: all 0.12s;
    font-size: 0.95em; background: #fff;
}
.radio-option:hover { border-color: #155799; background: #f7fbff; }
.radio-option input[type="radio"] { margin-right: 10px; accent-color: #155799; }
.radio-option.selected { border-color: #155799; background: #e3f2fd; }

.input-text {
    padding: 10px 12px; border: 1px solid #c0c0c0;
    border-radius: 6px; font-size: 1em; width: 200px;
}

.nav-row {
    display: flex; justify-content: space-between;
    align-items: center; margin-top: 16px;
}

/* Result cards */
.flag-card {
    border: 2px solid #f57c00; background: #fff8e1;
    border-radius: 8px; padding: 20px; margin-bottom: 16px;
}
.flag-card.acute { border-color: #c62828; background: #ffebee; }
.flag-card h3 {
    font-size: 1.05em; color: #222;
    margin-top: 0; margin-bottom: 10px;
}
.flag-card .body { font-size: 0.95em; color: #333; line-height: 1.5; }
.flag-card .first-step { margin-top: 10px; font-size: 0.95em; color: #333; }
.flag-card .resources {
    margin-top: 14px; padding-top: 12px;
    border-top: 1px solid rgba(0,0,0,0.08);
    font-size: 0.9em;
}
.flag-card .resources ul { margin: 4px 0 0; padding-left: 20px; }
.flag-card .resources li { margin-bottom: 4px; }

.fund-card {
    border: 1px solid #e0e0e0; background: #fff;
    border-radius: 8px; padding: 18px 20px;
    margin-bottom: 14px;
}
.fund-card.start-here { border-left: 4px solid #155799; }
.fund-card h3 { font-size: 1.05em; color: #222; margin: 0 0 4px; }
.fund-card .pretitle {
    text-transform: uppercase; letter-spacing: 0.5px;
    font-size: 0.72em; color: #155799;
    font-weight: 600; margin-bottom: 4px;
}
.fund-card .figure {
    font-weight: 600; color: #222;
    margin-bottom: 8px; font-size: 0.95em;
}
.fund-card .body { font-size: 0.93em; color: #444; line-height: 1.5; margin-bottom: 10px; }
.fund-card .links { font-size: 0.88em; }
.fund-card .links a { margin-right: 12px; }

.section-h {
    font-size: 1.25em; font-weight: 600; color: #222;
    margin: 36px 0 14px;
    border-bottom: 1px solid #e0e0e0; padding-bottom: 6px;
}

.all-clear {
    background: #f0f7f0; border-left: 4px solid #28a745;
    border-radius: 4px; padding: 16px 20px; color: #333;
}
.all-clear h3 { margin: 0 0 8px; color: #1d6f30; font-size: 1.05em; }
.all-clear p { margin: 0 0 8px; font-size: 0.94em; line-height: 1.5; }
.all-clear p:last-child { margin-bottom: 0; }

.results-lede { color: #555; margin-bottom: 18px; }

.stage-actions {
    margin-top: 24px; padding-top: 18px;
    border-top: 1px solid #e0e0e0;
    display: flex; gap: 10px; flex-wrap: wrap; align-items: center;
}

.everything-else {
    background: #f8f9fa; border-radius: 8px;
    padding: 16px 20px; margin-top: 24px;
    font-size: 0.95em; color: #444;
}

/* Focus area constraint UI */
.con-header {
    background: #fff; border: 1px solid #e0e0e0;
    border-radius: 12px; padding: 20px 24px;
    margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.con-header h3 { margin: 0 0 8px; font-size: 1.15em; }
.con-header .help { color: #555; font-size: 0.9em; margin: 0; }
.pillar-block {
    margin-bottom: 24px; background: #fff;
    border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden;
}
.pillar-head {
    background: #f8f9fa; padding: 10px 16px;
    font-weight: 600; font-size: 0.95em; color: #222;
    border-bottom: 1px solid #e0e0e0;
}
.area-row {
    display: grid; grid-template-columns: 1fr auto;
    gap: 12px; align-items: center;
    padding: 10px 16px; border-bottom: 1px solid #f0f0f0;
}
.area-row:last-child { border-bottom: none; }
.area-name { font-weight: 600; color: #222; font-size: 0.95em; }
.area-desc { color: #666; font-size: 0.82em; line-height: 1.35; margin-top: 2px; }
.rate-buttons { display: flex; gap: 4px; }
.rate-btn {
    width: 32px; height: 32px;
    border: 1px solid #d0d0d0; background: #fff;
    color: #666; border-radius: 4px;
    cursor: pointer; font-size: 0.9em; font-weight: 600;
    transition: all 0.1s;
}
.rate-btn:hover { border-color: #155799; color: #155799; }
.rate-btn.active { background: #155799; color: #fff; border-color: #155799; }
.rate-btn.zero.active { background: #888; border-color: #888; }

.binding-card {
    border: 2px solid #155799; background: #f0f7ff;
    border-radius: 12px; padding: 24px 28px;
    margin-bottom: 20px;
}
.binding-card .pretitle {
    text-transform: uppercase; letter-spacing: 0.5px;
    font-size: 0.75em; color: #155799;
    font-weight: 600; margin-bottom: 6px;
}
.binding-card h2 {
    margin: 0 0 12px; font-size: 1.5em; color: #000;
}
.binding-card .reason { color: #444; font-size: 0.95em; line-height: 1.5; margin-bottom: 12px; }
.binding-card .links a { margin-right: 14px; font-weight: 600; }

.successor {
    border: 1px solid #e0e0e0; background: #fff;
    border-radius: 8px; padding: 16px 20px; margin-bottom: 12px;
}
.successor .pretitle {
    text-transform: uppercase; letter-spacing: 0.5px;
    font-size: 0.7em; color: #888;
    font-weight: 600; margin-bottom: 4px;
}
.successor h3 { margin: 0 0 6px; font-size: 1.05em; color: #222; }
.successor .reason { color: #555; font-size: 0.88em; margin-bottom: 8px; }
.successor .links a { font-size: 0.88em; margin-right: 10px; }

.balanced-card {
    background: #f0f7f0; border-left: 4px solid #28a745;
    border-radius: 4px; padding: 18px 22px; margin-bottom: 20px;
}
.balanced-card h2 { margin: 0; color: #1d6f30; font-size: 1.2em; }

.override {
    margin-top: 32px; padding-top: 20px;
    border-top: 1px solid #e0e0e0;
}
.override h3 { font-size: 1.05em; margin-bottom: 8px; }
.override-list {
    margin-top: 12px; max-height: 480px; overflow-y: auto;
    border: 1px solid #e0e0e0; border-radius: 6px;
    padding: 8px; background: #fafafa;
}
.override-row {
    display: flex; justify-content: space-between; align-items: center;
    padding: 6px 10px; border-bottom: 1px solid #ececec;
    font-size: 0.9em;
}
.override-row:last-child { border-bottom: none; }
.override-row .pin-btn {
    background: none; border: 1px solid #155799;
    color: #155799; border-radius: 4px;
    padding: 3px 10px; font-size: 0.82em; cursor: pointer;
}
.override-row.pinned { background: #e3f2fd; }

@media (max-width: 600px) {
    .area-row { grid-template-columns: 1fr; gap: 8px; }
    .rate-buttons { justify-content: flex-start; }
    .stage-row { grid-template-columns: 28px 1fr; }
    .stage-skip { grid-column: 2; margin-top: 6px; }
}
</style>

<div class="prio">

<!-- ────────────────────────────────────────────────────────────────────── -->
<!-- LANDING                                                                  -->
<!-- ────────────────────────────────────────────────────────────────────── -->
<div id="viewLanding">

# Prioritisation

The framework covers around fifty life areas across five pillars. This screen helps you decide which to work on first.

It runs through three stages. You can take all three (about 22 minutes total), or skip ahead to the one you want.

<div class="stage-list">
  <div class="stage-row">
    <div class="stage-num">1</div>
    <div>
      <div class="stage-title">Triage</div>
      <div class="stage-desc">Surfaces serious issues that warrant attention before broader optimisation: significant depression or anxiety symptoms, immediate safety concerns, financial or housing distress, substance use, food insecurity, acute carer strain.</div>
      <div class="stage-meta">10 questions, about 5 minutes</div>
    </div>
    <button class="stage-skip" onclick="skipTo('triage')">Start triage</button>
  </div>
  <div class="stage-row">
    <div class="stage-num">2</div>
    <div>
      <div class="stage-title">Fundamentals</div>
      <div class="stage-desc">Checks five upstream areas with broad cross-domain effects: sleep, mental wellbeing, foundational finances, social connection, physical activity and nutrition. Significant gaps here tend to undermine progress everywhere else.</div>
      <div class="stage-meta">14 questions, about 5 minutes</div>
    </div>
    <button class="stage-skip" onclick="skipTo('fund')">Skip to fundamentals</button>
  </div>
  <div class="stage-row">
    <div class="stage-num">3</div>
    <div>
      <div class="stage-title">Focus area</div>
      <div class="stage-desc">Identifies a single binding life area to focus on next, based on what you value (Schwartz PVQ-21) and where you currently feel constrained across the 52 life areas. Output is one focus area with a stated reason, plus two named successors.</div>
      <div class="stage-meta">21 values items + 4 constraint pages, about 12 minutes</div>
    </div>
    <button class="stage-skip" onclick="skipTo('focus')">Skip to focus area</button>
  </div>
</div>

<div id="priorBanner" class="prior-banner hidden">
  <div id="priorBannerText"></div>
  <div class="actions">
    <button class="btn-secondary" onclick="viewSummary()">View results</button>
    <button class="btn-link" onclick="restartAll()">Start over</button>
  </div>
</div>

<div class="start-row">
  <button class="btn-primary" onclick="skipTo('triage')">Start the screen</button>
  <span class="meta">Your responses stay on this device unless you sign in, in which case they sync via your account.</span>
</div>

## Where this fits with the rest of the site

[Quick Wins](#) – high-impact, low-effort actions for momentum (in development).

[Level assessment]({{ site.baseurl }}/prioritisation/dashboard/) – assesses your current level across all life areas.

[Browse all life areas]({{ site.baseurl }}/life-areas/) – if you already know what you want to work on.

<details>
<summary><strong>Where the prioritisation research stands</strong></summary>

There is no single validated academic framework for prioritising across all of personal life. The closest analogues each capture part of the picture.

- **Maslow's hierarchy** (1943) is widely cited but empirically weak. [Tay and Diener (2011)](https://psycnet.apa.org/doi/10.1037/a0023779) showed across 123 countries that needs are pursued in parallel, not sequence. Not used here.
- **Theory of Constraints** (Goldratt, 1984), drawn from operations management, holds that a system's output is gated by its weakest critical link. Applied to life, this means identifying and addressing the binding constraint before optimising elsewhere.
- **Self-Determination Theory** ([Deci and Ryan, 2000](https://selfdeterminationtheory.org/)) identifies three core psychological needs – autonomy, competence, and relatedness – alongside physical needs. Better supported than Maslow.
- **The Wheel of Life**, a coaching tool, asks you to self-rate eight to ten areas and work on the lowest. Intuitive but limited by poor self-assessment.
- **ITN** (Importance, Tractability, Neglectedness), developed by effective altruists for cause selection, adapts reasonably to personal areas.
- **Hedonic adaptation research** ([Lyubomirsky and others](https://lyubomirskylab.com/)) shows that relationships, autonomy, meaning, and mastery produce lasting wellbeing returns. Income beyond roughly $75,000–100,000 household and most possessions adapt away ([Killingsworth, 2021](https://www.pnas.org/doi/10.1073/pnas.2016976118)).

This screen combines these into the three-stage approach above: triage acute issues first, then fundamentals where there are significant gaps, then prioritise across remaining areas. The values input draws on [Schwartz's theory of basic human values](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/) (validated across 80+ countries); the constraint identification draws on Theory of Constraints.

</details>

</div>

<!-- ────────────────────────────────────────────────────────────────────── -->
<!-- TRIAGE QUESTIONS                                                         -->
<!-- ────────────────────────────────────────────────────────────────────── -->
<div id="viewTriageQ" class="hidden">
  <div class="progress-bar">
    <div class="progress-outer"><div class="progress-fill" id="triageProgressFill"></div></div>
    <div class="progress-info">
      <span id="triageProgressText">Triage – question 1 of 10</span>
      <button class="btn-link" onclick="exitToLanding()" style="padding:0;">Exit</button>
    </div>
  </div>
  <div id="triageMount"></div>
  <div class="nav-row">
    <button class="btn-secondary" id="triageBack" onclick="triageBack()">Back</button>
    <button class="btn-primary" id="triageNext" onclick="triageNext()" disabled>Next</button>
  </div>
</div>

<!-- ────────────────────────────────────────────────────────────────────── -->
<!-- TRIAGE RESULTS                                                           -->
<!-- ────────────────────────────────────────────────────────────────────── -->
<div id="viewTriageR" class="hidden">
  <h1 style="margin-bottom: 6px;">Triage results</h1>
  <p class="results-lede" id="triageResultsLede"></p>
  <div id="triageResultsMount"></div>
  <div class="stage-actions">
    <button class="btn-primary" onclick="skipTo('fund')">Continue to fundamentals</button>
    <button class="btn-secondary" onclick="skipTo('focus')">Skip to focus area</button>
    <button class="btn-link" onclick="exitToLanding()">Exit</button>
  </div>
</div>

<!-- ────────────────────────────────────────────────────────────────────── -->
<!-- FUNDAMENTALS QUESTIONS                                                   -->
<!-- ────────────────────────────────────────────────────────────────────── -->
<div id="viewFundQ" class="hidden">
  <div class="progress-bar">
    <div class="progress-outer"><div class="progress-fill" id="fundProgressFill"></div></div>
    <div class="progress-info">
      <span id="fundProgressText">Fundamentals – question 1 of 14</span>
      <button class="btn-link" onclick="exitToLanding()" style="padding:0;">Exit</button>
    </div>
  </div>
  <div id="fundMount"></div>
  <div class="nav-row">
    <button class="btn-secondary" id="fundBack" onclick="fundBack()">Back</button>
    <button class="btn-primary" id="fundNext" onclick="fundNext()" disabled>Next</button>
  </div>
</div>

<!-- ────────────────────────────────────────────────────────────────────── -->
<!-- FUNDAMENTALS RESULTS                                                     -->
<!-- ────────────────────────────────────────────────────────────────────── -->
<div id="viewFundR" class="hidden">
  <h1 style="margin-bottom: 6px;">Fundamentals results</h1>
  <p class="results-lede" id="fundResultsLede"></p>
  <div id="fundResultsMount"></div>
  <div class="stage-actions">
    <button class="btn-primary" onclick="skipTo('focus')">Continue to focus area</button>
    <button class="btn-link" onclick="exitToLanding()">Exit</button>
  </div>
</div>

<!-- ────────────────────────────────────────────────────────────────────── -->
<!-- FOCUS AREA – DEMOGRAPHICS                                                -->
<!-- ────────────────────────────────────────────────────────────────────── -->
<div id="viewFocusDemo" class="hidden">
  <div class="progress-bar">
    <div class="progress-outer"><div class="progress-fill" style="width:5%"></div></div>
    <div class="progress-info">
      <span>Focus area – step 1 of 4</span>
      <button class="btn-link" onclick="exitToLanding()" style="padding:0;">Exit</button>
    </div>
  </div>
  <div class="q-card">
    <div class="q-section">About you</div>
    <div class="q-prompt">Used to match pronouns in the values items.</div>
    <p style="margin: 0 0 10px; font-weight: 600;">Your age</p>
    <input type="number" id="demoAge" min="13" max="120" class="input-text" placeholder="e.g. 35">
    <p style="margin: 18px 0 10px; font-weight: 600;">Your gender</p>
    <div id="demoGenderOptions"></div>
  </div>
  <div class="nav-row">
    <button class="btn-secondary" onclick="exitToLanding()">Back</button>
    <button class="btn-primary" id="demoNext" onclick="goToPvq()" disabled>Continue</button>
  </div>
</div>

<!-- ────────────────────────────────────────────────────────────────────── -->
<!-- FOCUS AREA – PVQ                                                         -->
<!-- ────────────────────────────────────────────────────────────────────── -->
<div id="viewFocusPvq" class="hidden">
  <div class="progress-bar">
    <div class="progress-outer"><div class="progress-fill" id="pvqProgressFill"></div></div>
    <div class="progress-info">
      <span id="pvqProgressText">Focus area – step 2 of 4 – values, item 1 of 21</span>
      <button class="btn-link" onclick="exitToLanding()" style="padding:0;">Exit</button>
    </div>
  </div>
  <div id="pvqMount"></div>
  <div class="nav-row">
    <button class="btn-secondary" id="pvqBack" onclick="pvqBack()">Back</button>
    <button class="btn-primary" id="pvqNext" onclick="pvqNext()" disabled>Next</button>
  </div>
</div>

<!-- ────────────────────────────────────────────────────────────────────── -->
<!-- FOCUS AREA – CONSTRAINTS                                                 -->
<!-- ────────────────────────────────────────────────────────────────────── -->
<div id="viewFocusCon" class="hidden">
  <div class="progress-bar">
    <div class="progress-outer"><div class="progress-fill" id="conProgressFill"></div></div>
    <div class="progress-info">
      <span id="conProgressText">Focus area – step 3 of 4 – constraints, page 1 of 4</span>
      <button class="btn-link" onclick="exitToLanding()" style="padding:0;">Exit</button>
    </div>
  </div>
  <div id="conMount"></div>
  <div class="nav-row">
    <button class="btn-secondary" id="conBack" onclick="conBack()">Back</button>
    <button class="btn-primary" id="conNext" onclick="conNext()">Next</button>
  </div>
</div>

<!-- ────────────────────────────────────────────────────────────────────── -->
<!-- FOCUS AREA RESULTS                                                       -->
<!-- ────────────────────────────────────────────────────────────────────── -->
<div id="viewFocusR" class="hidden">
  <h1 style="margin-bottom: 6px;">Your focus area</h1>
  <p class="results-lede">Computed from your values (Schwartz PVQ-21) and the four constraint signals.</p>
  <div id="focusResultsMount"></div>
  <div class="stage-actions">
    <button class="btn-primary" onclick="viewSummary()">See full summary</button>
    <button class="btn-link" onclick="exitToLanding()">Exit</button>
  </div>
</div>

<!-- ────────────────────────────────────────────────────────────────────── -->
<!-- COMBINED SUMMARY                                                         -->
<!-- ────────────────────────────────────────────────────────────────────── -->
<div id="viewSummary" class="hidden">
  <h1>Your prioritisation summary</h1>
  <p class="results-lede" id="summaryLede"></p>
  <div id="summaryMount"></div>
  <div class="stage-actions">
    <button class="btn-secondary" onclick="restartAll()">Retake the whole screen</button>
    <button class="btn-link" onclick="exitToLanding()">Back to overview</button>
  </div>
</div>

</div>

<script>
// ════════════════════════════════════════════════════════════════════════
// DATA
// ════════════════════════════════════════════════════════════════════════

var PVQ = {{ site.data.pvq21 | jsonify }};
var AREA_VALUES = {{ site.data["area-value-mapping"] | jsonify }};

var LIFE_AREAS = [
{% assign sorted_areas = site.data.life_areas | sort %}
{% for area in sorted_areas %}{% assign d = area[1] %}  { slug: {{ area[0] | jsonify }}, name: {{ d.name | jsonify }}, pillar: {{ d.pillar | jsonify }}, domain: {{ d.domain | jsonify }}, desc: {{ d.survey_description | jsonify }} }{% unless forloop.last %},{% endunless %}
{% endfor %}];

var PILLAR_ORDER = ['Expand Your Awareness', 'Look After Yourself', 'Connect with Others', 'Organise Your Life', 'Create & Contribute'];
var BASE = '{{ site.baseurl }}';

// ════════════════════════════════════════════════════════════════════════
// TRIAGE – question definitions and flag content
// ════════════════════════════════════════════════════════════════════════

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

var TRIAGE_Q = [
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

var TRIAGE_PHQ9_9 = {
    id: 'phq9_9',
    section: 'Follow-up',
    text: 'Over the last two weeks, how often have you had thoughts that you would be better off dead, or of hurting yourself in some way?',
    options: SCALE_PHQ
};

// Triage flag content. Each card includes hyperlinked, briefly-explained
// supporting evidence directly in the body where relevant.
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
        title: function(level) { return 'Your responses suggest ' + (level === 'moderate' ? 'moderate or higher' : 'mild') + ' symptoms of depression.'; },
        body: 'A PHQ-2 score of 3 or more is the validated cutoff at which a fuller depression assessment is warranted (<a href="https://pubmed.ncbi.nlm.nih.gov/14583691/" target="_blank" rel="noopener">Kroenke, Spitzer & Williams, 2003</a>, on a sample of 6,000 adults). Depression is among the most treatable mental health conditions, with strong evidence for cognitive behavioural therapy, behavioural activation, and medication.',
        firstStep: 'A reasonable first step is taking the longer PHQ-9 to get a clearer picture, then booking a GP or primary care appointment.',
        resources: [
            { label: 'PHQ-9 self-screen and scoring (free)', href: 'https://www.phqscreeners.com/' },
            { label: 'NHS Talking Therapies – self-referral (UK)', href: 'https://www.nhs.uk/mental-health/talking-therapies-medicine-treatments/talking-therapies-and-counselling/nhs-talking-therapies/' },
            { label: 'Psychology Today therapist directory (US)', href: 'https://www.psychologytoday.com/us/therapists' }
        ]
    },
    anxiety: {
        title: function(level) { return 'Your responses suggest ' + (level === 'moderate' ? 'moderate or higher' : 'mild') + ' symptoms of anxiety.'; },
        body: 'A GAD-2 score of 3 or more is the validated cutoff at which a fuller anxiety assessment is warranted (<a href="https://pubmed.ncbi.nlm.nih.gov/17339617/" target="_blank" rel="noopener">Kroenke et al., 2007</a>). Cognitive behavioural therapy is the best-evidenced treatment for generalised anxiety, panic, and social anxiety; some forms also respond well to medication.',
        firstStep: 'A reasonable first step is taking the longer GAD-7 to get a clearer picture, then booking a GP or primary care appointment.',
        resources: [
            { label: 'GAD-7 self-screen and scoring (free)', href: 'https://www.phqscreeners.com/' },
            { label: 'NHS Talking Therapies – self-referral (UK)', href: 'https://www.nhs.uk/mental-health/talking-therapies-medicine-treatments/talking-therapies-and-counselling/nhs-talking-therapies/' },
            { label: 'Psychology Today therapist directory (US)', href: 'https://www.psychologytoday.com/us/therapists' }
        ]
    },
    safety: {
        title: 'You indicated that someone has made you feel physically unsafe.',
        body: 'Safety planning matters before any other kind of self-improvement work. The services below are free and confidential. They can help you think through your situation and options without committing you to any specific course of action.',
        firstStep: 'A reasonable first step is talking to a trained adviser, who can help you understand what support is available where you are.',
        resources: [
            { label: 'United States – National Domestic Violence Hotline, 1-800-799-7233', href: 'https://www.thehotline.org/' },
            { label: 'United Kingdom – Refuge, 0808 2000 247 (24 hours, free)', href: 'https://www.refuge.org.uk/' },
            { label: 'Other countries – findahelpline.com', href: 'https://findahelpline.com/' }
        ]
    },
    financial: {
        title: 'You indicated trouble paying essential bills or worry about losing your housing.',
        body: 'Financial scarcity has measurable effects on cognitive bandwidth and decision-making (<a href="https://www.science.org/doi/10.1126/science.1238041" target="_blank" rel="noopener">Mani, Mullainathan, Shafir & Zhao, 2013</a>, in <em>Science</em>: scarcity reduced cognitive function in their experimental conditions by an effect size equivalent to roughly 13 IQ points). Free debt-counselling charities exist in most countries and tend to negotiate better outcomes than handling creditors alone.',
        firstStep: 'A reasonable first step is contacting a free debt advice service before missing a payment, since options narrow once defaults start.',
        resources: [
            { label: 'United Kingdom – StepChange, 0800 138 1111', href: 'https://www.stepchange.org/' },
            { label: 'United States – National Foundation for Credit Counseling, 1-800-388-2227', href: 'https://www.nfcc.org/' },
            { label: 'United States – call 211 for local assistance programmes', href: 'https://www.211.org/' }
        ]
    },
    substance: {
        title: 'You indicated using alcohol, medication, or other drugs in ways that caused problems.',
        body: 'Self-screening with the longer <a href="https://auditscreen.org/" target="_blank" rel="noopener">AUDIT (alcohol)</a> or DAST-10 (drugs) tools gives a clearer picture of severity. For most people the most useful first conversation is with a GP, who can discuss options privately and connect you to specialist services.',
        firstStep: 'A reasonable first step is taking the relevant self-screen and, if it confirms a concern, a GP appointment.',
        resources: [
            { label: 'United Kingdom – Drinkaware (alcohol education and self-assessment)', href: 'https://www.drinkaware.co.uk/' },
            { label: 'United States – SAMHSA helpline 1-800-662-4357 (24 hours, free, confidential)', href: 'https://findtreatment.gov/' },
            { label: 'Other countries – findahelpline.com', href: 'https://findahelpline.com/' }
        ]
    },
    food: {
        title: 'You indicated worry about food running out or food not lasting.',
        body: 'Food insecurity has measurable effects on physical and mental health independent of overall income (<a href="https://pubmed.ncbi.nlm.nih.gov/20595453/" target="_blank" rel="noopener">Hager et al., 2010</a>, validating the two-item Hunger Vital Sign in 30,000 households). Local food banks operate independently of any benefits process and can usually be accessed quickly.',
        firstStep: 'A reasonable first step is locating a nearby food bank and, separately, checking whether you are eligible for benefits or assistance you are not currently claiming.',
        resources: [
            { label: 'United Kingdom – Trussell food bank network', href: 'https://www.trussell.org.uk/' },
            { label: 'United States – Feeding America food bank locator', href: 'https://www.feedingamerica.org/find-your-local-foodbank' },
            { label: 'United States – call 211 for local food assistance', href: 'https://www.211.org/' }
        ]
    },
    carer: {
        title: 'You indicated being the main carer for someone with high needs and having little or no respite.',
        body: 'Carer strain is one situation that broad self-improvement advice often does not address well. It affects what "starting with sleep" or "starting with exercise" even mean. The most useful first step is usually connecting with a service that knows the local respite, financial, and emotional support options.',
        firstStep: 'A reasonable first step is reaching out to a carer support organisation in your country, which can help map the support that exists for your situation.',
        resources: [
            { label: 'United Kingdom – Carers UK', href: 'https://www.carersuk.org/' },
            { label: 'United States – Family Caregiver Alliance', href: 'https://www.caregiver.org/' }
        ]
    }
};
var FLAG_ORDER = ['suicidal', 'safety', 'depression', 'anxiety', 'substance', 'financial', 'food', 'carer'];

// ════════════════════════════════════════════════════════════════════════
// FUNDAMENTALS – question definitions and content
// ════════════════════════════════════════════════════════════════════════

var SCALE_WHO5 = [
    { label: 'At no time', value: 0 },
    { label: 'Some of the time', value: 1 },
    { label: 'Less than half of the time', value: 2 },
    { label: 'More than half of the time', value: 3 },
    { label: 'Most of the time', value: 4 },
    { label: 'All of the time', value: 5 }
];
var SCALE_UCLA3 = [
    { label: 'Hardly ever', value: 1 },
    { label: 'Some of the time', value: 2 },
    { label: 'Often', value: 3 }
];
var SCALE_SLEEP = [
    { label: 'Under 5 hours', value: 'under5' },
    { label: '5 to 6 hours', value: '5-6' },
    { label: '6 to 7 hours', value: '6-7' },
    { label: '7 to 8 hours', value: '7-8' },
    { label: '8 hours or more', value: '8plus' }
];
var SCALE_CONTACT = [
    { label: 'Daily', value: 'daily' },
    { label: 'Weekly', value: 'weekly' },
    { label: 'Monthly', value: 'monthly' },
    { label: 'Less than monthly', value: 'less' }
];
var SCALE_ACTIVITY = [
    { label: 'None', value: '0' },
    { label: 'Under 60 minutes', value: 'under60' },
    { label: '60 to 150 minutes', value: '60-150' },
    { label: '150 to 300 minutes', value: '150-300' },
    { label: 'Over 300 minutes', value: 'over300' }
];
var SCALE_VEG = [
    { label: '0 to 1 servings', value: '0-1' },
    { label: '2 servings', value: '2' },
    { label: '3 to 4 servings', value: '3-4' },
    { label: '5 or more servings', value: '5plus' }
];

var WHO5_LEAD = 'Over the last two weeks, ';
var FUND_Q = [
    { id: 'who5_1', section: 'Wellbeing',  text: WHO5_LEAD + 'I have felt cheerful and in good spirits.',                       options: SCALE_WHO5 },
    { id: 'who5_2', section: 'Wellbeing',  text: WHO5_LEAD + 'I have felt calm and relaxed.',                                   options: SCALE_WHO5 },
    { id: 'who5_3', section: 'Wellbeing',  text: WHO5_LEAD + 'I have felt active and vigorous.',                                options: SCALE_WHO5 },
    { id: 'who5_4', section: 'Wellbeing',  text: WHO5_LEAD + 'I woke up feeling fresh and rested.',                             options: SCALE_WHO5 },
    { id: 'who5_5', section: 'Wellbeing',  text: WHO5_LEAD + 'My daily life has been filled with things that interest me.',    options: SCALE_WHO5 },
    { id: 'sleep_hours',        section: 'Sleep',     text: 'On a typical work night, roughly how many hours of sleep do you get?', options: SCALE_SLEEP },
    { id: 'emergency',          section: 'Finances',  text: 'If you had an unexpected $400 expense, could you cover it from cash or savings without borrowing?', options: SCALE_YN },
    { id: 'high_interest_debt', section: 'Finances',  text: 'Are you currently carrying balances on credit cards, payday loans, or overdrafts that charge interest?', options: SCALE_YN },
    { id: 'ucla_1', section: 'Social connection', text: 'How often do you feel that you lack companionship?', options: SCALE_UCLA3 },
    { id: 'ucla_2', section: 'Social connection', text: 'How often do you feel left out?',                    options: SCALE_UCLA3 },
    { id: 'ucla_3', section: 'Social connection', text: 'How often do you feel isolated from others?',        options: SCALE_UCLA3 },
    { id: 'contact_freq', section: 'Social connection', text: 'How often do you have meaningful contact with close friends or family (in person, by phone, or video)?', options: SCALE_CONTACT },
    { id: 'activity_min', section: 'Activity', text: 'In a typical week, roughly how many minutes of activity that raises your heart rate noticeably do you do? (Brisk walking, cycling, sport, gym, manual work all count.)', options: SCALE_ACTIVITY },
    { id: 'veg_servings', section: 'Nutrition', text: 'On a typical day, how many servings of vegetables or fruit do you eat? (One serving is roughly a fist-sized portion.)', options: SCALE_VEG }
];

// Personalised fundamentals cards. Each contains a brief, hyperlinked
// explanation of the supporting evidence rather than a bare citation.
var FUND_ORDER = ['wellbeing', 'sleep', 'finances', 'social', 'activity'];
var FUND_CONTENT = {
    wellbeing: {
        title: 'Mental health and wellbeing',
        body: 'A WHO-5 score below 13 (52%) is the validated cutoff for poor wellbeing (<a href="https://pubmed.ncbi.nlm.nih.gov/25831962/" target="_blank" rel="noopener">Topp et al., 2015</a>, systematic review of 213 studies). Sub-clinical wellbeing impairment tends to undermine progress in every other area before it shows up as clinical depression or anxiety.',
        links: [
            { label: 'Read the Mental Health guide', href: BASE + '/mental-health/' },
            { label: 'Read the Mindfulness guide', href: BASE + '/mindfulness/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#mental-health-sub-clinical' }
        ]
    },
    sleep: {
        title: 'Sleep',
        body: 'Below 6 hours per night, all-cause mortality, cognitive harm, and metabolic risk rise sharply (<a href="https://pubmed.ncbi.nlm.nih.gov/20469800/" target="_blank" rel="noopener">Cappuccio et al., 2010</a>, meta-analysis of 16 prospective cohorts covering 1.4 million participants). Sleep is the highest-leverage fundamental because gains here propagate to almost every other domain.',
        links: [
            { label: 'Read the Sleep guide', href: BASE + '/sleep/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#sleep' }
        ]
    },
    finances: {
        title: 'Foundational finances',
        body: 'Chronic financial worry imposes a measurable cognitive load – roughly 13 IQ points in experimental conditions (<a href="https://www.science.org/doi/10.1126/science.1238041" target="_blank" rel="noopener">Mani et al., 2013</a>, in <em>Science</em>). Recommending career, productivity, or relationship interventions to someone under acute financial pressure tends to fail because the underlying scarcity is the binding constraint on bandwidth.',
        links: [
            { label: 'Read the Saving guide', href: BASE + '/saving/' },
            { label: 'Read the Financial Planning guide', href: BASE + '/financial-planning-tracking/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#foundational-finances' }
        ]
    },
    social: {
        title: 'Key relationships and social connection',
        body: 'Loneliness and social isolation have mortality effects comparable to smoking 15 cigarettes per day (<a href="https://journals.sagepub.com/doi/10.1177/1745691614568352" target="_blank" rel="noopener">Holt-Lunstad et al., 2015</a>, meta-analysis of 70 studies covering 3.4 million participants). The cutoff flags either persistent loneliness on the UCLA-3 short scale or less-than-weekly meaningful contact.',
        links: [
            { label: 'Read the Friendship guide', href: BASE + '/friendship/' },
            { label: 'Read the Relationship Quality guide', href: BASE + '/relationship-quality/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#key-relationships-and-social-connection' }
        ]
    },
    activity: {
        title: 'Physical activity and nutrition',
        body: 'The largest absolute mortality gains come from going from zero to roughly 60 minutes of moderate activity per week (<a href="https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(12)61031-9/fulltext" target="_blank" rel="noopener">Lee et al., 2012</a>, <em>Lancet</em>), and from the first two-to-three daily servings of vegetables or fruit (<a href="https://academic.oup.com/ije/article/46/3/1029/3039477" target="_blank" rel="noopener">Aune et al., 2017</a>). Hitting an optimal target is a separate, smaller-gain question.',
        links: [
            { label: 'Read the Fitness guide', href: BASE + '/fitness/' },
            { label: 'Read the Nutrition guide', href: BASE + '/nutrition/' },
            { label: 'Why this cutoff', href: BASE + '/methodology/fundamentals-cutoffs/#physical-activity-and-nutrition' }
        ]
    }
};

// ════════════════════════════════════════════════════════════════════════
// FOCUS AREA – constraint definitions and labels
// ════════════════════════════════════════════════════════════════════════

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

// ════════════════════════════════════════════════════════════════════════
// STORAGE KEYS
// ════════════════════════════════════════════════════════════════════════

var KEY_TRIAGE_RESP = 'ap-triage-responses';
var KEY_TRIAGE_FLAGS = 'ap-triage-flags';
var KEY_TRIAGE_DONE = 'ap-triage-completed-at';
var KEY_FUND_RESP = 'ap-fundamentals-responses';
var KEY_FUND_FLAGS = 'ap-fundamentals-flags';
var KEY_FUND_DONE = 'ap-fundamentals-completed-at';
var KEY_DEMO = 'ap-prioritisation-demographics';
var KEY_PVQ = 'ap-prioritisation-pvq';
var KEY_CON = 'ap-prioritisation-constraints';
var KEY_FOCUS_FLAGS = 'ap-prioritisation-flags';
var KEY_FOCUS_DONE = 'ap-prioritisation-completed-at';

function load(k) { return window.APStorage.load(k); }
function save(k, v) { window.APStorage.save(k, v); }

// ════════════════════════════════════════════════════════════════════════
// STATE
// ════════════════════════════════════════════════════════════════════════

var triageAnswers = {}, triageIdx = 0;
var fundAnswers = {}, fundIdx = 0;
var demographics = { age: null, gender: null };
var pvqAnswers = {}, pvqIdx = 0;
var constraintAnswers = { cost: {}, upside: {}, friction: {}, underinvest: {} };
var conPage = 0;

// ════════════════════════════════════════════════════════════════════════
// VIEW SWITCHING
// ════════════════════════════════════════════════════════════════════════

var ALL_VIEWS = ['Landing', 'TriageQ', 'TriageR', 'FundQ', 'FundR', 'FocusDemo', 'FocusPvq', 'FocusCon', 'FocusR', 'Summary'];

function showView(name) {
    ALL_VIEWS.forEach(function(v) {
        var el = document.getElementById('view' + v);
        if (el) el.classList.toggle('hidden', v !== name);
    });
    window.scrollTo(0, 0);
}

function exitToLanding() { renderLanding(); }

function restartAll() {
    if (!confirm('This will clear your previous responses to all three stages. Continue?')) return;
    [KEY_TRIAGE_RESP, KEY_TRIAGE_FLAGS, KEY_TRIAGE_DONE,
     KEY_FUND_RESP, KEY_FUND_FLAGS, KEY_FUND_DONE,
     KEY_DEMO, KEY_PVQ, KEY_CON, KEY_FOCUS_FLAGS, KEY_FOCUS_DONE].forEach(function(k) {
        save(k, null);
    });
    triageAnswers = {}; triageIdx = 0;
    fundAnswers = {}; fundIdx = 0;
    demographics = { age: null, gender: null };
    pvqAnswers = {}; pvqIdx = 0;
    constraintAnswers = { cost: {}, upside: {}, friction: {}, underinvest: {} };
    conPage = 0;
    skipTo('triage');
}

function skipTo(stage) {
    if (stage === 'triage') {
        triageAnswers = {};
        triageIdx = 0;
        renderTriageQ();
        showView('TriageQ');
    } else if (stage === 'fund') {
        fundAnswers = {};
        fundIdx = 0;
        renderFundQ();
        showView('FundQ');
    } else if (stage === 'focus') {
        demographics = load(KEY_DEMO) || { age: null, gender: null };
        pvqAnswers = {};
        pvqIdx = 0;
        constraintAnswers = { cost: {}, upside: {}, friction: {}, underinvest: {} };
        conPage = 0;
        renderDemographics();
        showView('FocusDemo');
    }
}

// ════════════════════════════════════════════════════════════════════════
// LANDING
// ════════════════════════════════════════════════════════════════════════

function renderLanding() {
    var triageDone = load(KEY_TRIAGE_DONE);
    var fundDone = load(KEY_FUND_DONE);
    var focusDone = load(KEY_FOCUS_DONE);
    var anyDone = triageDone || fundDone || focusDone;
    var banner = document.getElementById('priorBanner');
    if (anyDone) {
        var bits = [];
        if (triageDone) bits.push('triage');
        if (fundDone) bits.push('fundamentals');
        if (focusDone) bits.push('focus area');
        var lastDate = [triageDone, fundDone, focusDone].filter(Boolean).sort().pop();
        var dateStr;
        try { dateStr = new Intl.DateTimeFormat('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }).format(new Date(lastDate)); }
        catch (e) { dateStr = lastDate.split('T')[0]; }
        var label = bits.length === 1 ? bits[0] : bits.length === 2 ? bits.join(' and ') : bits.slice(0, -1).join(', ') + ', and ' + bits[bits.length - 1];
        document.getElementById('priorBannerText').textContent = 'You have completed ' + label + ' (most recent: ' + dateStr + ').';
        banner.classList.remove('hidden');
    } else {
        banner.classList.add('hidden');
    }
    showView('Landing');
}

// ════════════════════════════════════════════════════════════════════════
// TRIAGE
// ════════════════════════════════════════════════════════════════════════

function triagePhqPositive(a) { return ((a.phq2_1 || 0) + (a.phq2_2 || 0)) >= 3; }

function triageList() {
    var l = TRIAGE_Q.slice();
    if (triagePhqPositive(triageAnswers)) l.push(TRIAGE_PHQ9_9);
    return l;
}

function renderTriageQ() {
    var list = triageList();
    if (triageIdx >= list.length) { finishTriage(); return; }
    var q = list[triageIdx];
    var total = list.length;
    document.getElementById('triageProgressText').textContent = 'Triage – question ' + (triageIdx + 1) + ' of ' + total;
    document.getElementById('triageProgressFill').style.width = (triageIdx / total * 100) + '%';

    var html = '<div class="q-card">';
    html += '<div class="q-section">' + escapeHtml(q.section) + '</div>';
    html += '<div class="q-text">' + escapeHtml(q.text) + '</div>';
    html += '<div>';
    var current = triageAnswers[q.id];
    q.options.forEach(function(opt, i) {
        var checked = (current !== undefined && current === opt.value) ? 'checked' : '';
        var sel = (current !== undefined && current === opt.value) ? ' selected' : '';
        var optId = 'tri_' + q.id + '_' + i;
        html += '<label class="radio-option' + sel + '" for="' + optId + '">';
        html += '<input type="radio" name="tri_' + q.id + '" id="' + optId + '" value="' + i + '" ' + checked + ' onchange="onTriageAnswer(\'' + q.id + '\', ' + i + ')">';
        html += '<span>' + escapeHtml(opt.label) + '</span></label>';
    });
    html += '</div></div>';
    document.getElementById('triageMount').innerHTML = html;

    document.getElementById('triageBack').disabled = (triageIdx === 0);
    document.getElementById('triageNext').disabled = (current === undefined);
    document.getElementById('triageNext').textContent = (triageIdx === list.length - 1) ? 'See triage results' : 'Next';
}

function onTriageAnswer(qid, i) {
    var list = triageList();
    var q = list.find(function(x) { return x.id === qid; });
    if (!q) return;
    triageAnswers[qid] = q.options[i].value;
    save(KEY_TRIAGE_RESP, triageAnswers);
    var labels = document.querySelectorAll('#triageMount label.radio-option');
    labels.forEach(function(l) { l.classList.remove('selected'); });
    var picked = document.getElementById('tri_' + qid + '_' + i);
    if (picked && picked.parentNode) picked.parentNode.classList.add('selected');
    document.getElementById('triageNext').disabled = false;
}

function triageNext() { triageIdx += 1; renderTriageQ(); }
function triageBack() {
    if (triageIdx === 0) { exitToLanding(); return; }
    triageIdx -= 1;
    renderTriageQ();
}

function computeTriageFlags(a) {
    var f = {};
    var phq = (a.phq2_1 || 0) + (a.phq2_2 || 0);
    if (phq >= 3) f.depression = phq >= 4 ? 'moderate' : 'mild';
    if ((a.phq9_9 || 0) >= 1) f.suicidal = true;
    var gad = (a.gad2_1 || 0) + (a.gad2_2 || 0);
    if (gad >= 3) f.anxiety = gad >= 4 ? 'moderate' : 'mild';
    if (a.safety === 'yes') f.safety = true;
    if (a.financial === 'yes') f.financial = true;
    if (a.substance === 'yes') f.substance = true;
    var hh = function(v) { return v === 'often' || v === 'sometimes'; };
    if (hh(a.hunger_1) || hh(a.hunger_2)) f.food = true;
    if (a.carer === 'yes') f.carer = true;
    return f;
}

function finishTriage() {
    var flags = computeTriageFlags(triageAnswers);
    save(KEY_TRIAGE_FLAGS, flags);
    save(KEY_TRIAGE_DONE, new Date().toISOString());
    renderTriageR(flags);
    showView('TriageR');
}

function renderTriageR(flags) {
    flags = flags || load(KEY_TRIAGE_FLAGS) || {};
    var triggered = FLAG_ORDER.filter(function(k) { return flags[k]; });
    var lede;
    if (triggered.length === 0) {
        lede = 'No areas surfaced from the triage screen.';
    } else if (triggered.length === 1) {
        lede = 'The triage screen surfaced one area worth attending to before broader optimisation work.';
    } else {
        lede = 'The triage screen surfaced ' + triggered.length + ' areas worth attending to before broader optimisation work.';
    }
    document.getElementById('triageResultsLede').textContent = lede;

    var html = '';
    if (triggered.length === 0) {
        html += '<div class="all-clear"><h3>Nothing flagged.</h3><p>The triage screen did not surface any acute issues. Continue to fundamentals when ready.</p></div>';
    } else {
        triggered.forEach(function(k) { html += renderFlagCard(k, flags[k]); });
    }
    document.getElementById('triageResultsMount').innerHTML = html;
}

function renderFlagCard(key, val) {
    var c = FLAG_CONTENT[key];
    if (!c) return '';
    var titleText = (typeof c.title === 'function') ? c.title(val) : c.title;
    var classes = 'flag-card' + (c.acute ? ' acute' : '');
    var html = '<div class="' + classes + '">';
    html += '<h3>' + escapeHtml(titleText) + '</h3>';
    html += '<div class="body">' + c.body + '</div>';
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

// ════════════════════════════════════════════════════════════════════════
// FUNDAMENTALS
// ════════════════════════════════════════════════════════════════════════

function renderFundQ() {
    if (fundIdx >= FUND_Q.length) { finishFund(); return; }
    var q = FUND_Q[fundIdx];
    var total = FUND_Q.length;
    document.getElementById('fundProgressText').textContent = 'Fundamentals – question ' + (fundIdx + 1) + ' of ' + total;
    document.getElementById('fundProgressFill').style.width = (fundIdx / total * 100) + '%';

    var html = '<div class="q-card">';
    html += '<div class="q-section">' + escapeHtml(q.section) + '</div>';
    html += '<div class="q-text">' + escapeHtml(q.text) + '</div>';
    html += '<div>';
    var current = fundAnswers[q.id];
    q.options.forEach(function(opt, i) {
        var checked = (current !== undefined && current === opt.value) ? 'checked' : '';
        var sel = (current !== undefined && current === opt.value) ? ' selected' : '';
        var optId = 'fund_' + q.id + '_' + i;
        html += '<label class="radio-option' + sel + '" for="' + optId + '">';
        html += '<input type="radio" name="fund_' + q.id + '" id="' + optId + '" value="' + i + '" ' + checked + ' onchange="onFundAnswer(\'' + q.id + '\', ' + i + ')">';
        html += '<span>' + escapeHtml(opt.label) + '</span></label>';
    });
    html += '</div></div>';
    document.getElementById('fundMount').innerHTML = html;

    document.getElementById('fundBack').disabled = (fundIdx === 0);
    document.getElementById('fundNext').disabled = (current === undefined);
    document.getElementById('fundNext').textContent = (fundIdx === FUND_Q.length - 1) ? 'See fundamentals results' : 'Next';
}

function onFundAnswer(qid, i) {
    var q = FUND_Q.find(function(x) { return x.id === qid; });
    if (!q) return;
    fundAnswers[qid] = q.options[i].value;
    save(KEY_FUND_RESP, fundAnswers);
    var labels = document.querySelectorAll('#fundMount label.radio-option');
    labels.forEach(function(l) { l.classList.remove('selected'); });
    var picked = document.getElementById('fund_' + qid + '_' + i);
    if (picked && picked.parentNode) picked.parentNode.classList.add('selected');
    document.getElementById('fundNext').disabled = false;
}

function fundNext() { fundIdx += 1; renderFundQ(); }
function fundBack() {
    if (fundIdx === 0) { exitToLanding(); return; }
    fundIdx -= 1;
    renderFundQ();
}

function computeFundFlags(a) {
    var f = {};
    if (a.sleep_hours === 'under5' || a.sleep_hours === '5-6') f.sleep = true;
    var who5 = ['who5_1','who5_2','who5_3','who5_4','who5_5'].reduce(function(s, k) { return s + (typeof a[k] === 'number' ? a[k] : 0); }, 0);
    if (who5 <= 13) f.wellbeing = true;
    if (a.emergency === 'no' || a.high_interest_debt === 'yes') f.finances = true;
    var ucla = ['ucla_1','ucla_2','ucla_3'].reduce(function(s, k) { return s + (typeof a[k] === 'number' ? a[k] : 0); }, 0);
    if (ucla >= 6 || a.contact_freq === 'monthly' || a.contact_freq === 'less') f.social = true;
    if (a.activity_min === '0' || a.activity_min === 'under60' || a.veg_servings === '0-1' || a.veg_servings === '2') f.activity = true;
    return f;
}

function finishFund() {
    var flags = computeFundFlags(fundAnswers);
    save(KEY_FUND_FLAGS, flags);
    save(KEY_FUND_DONE, new Date().toISOString());
    renderFundR(flags);
    showView('FundR');
}

function fundFigure(flag, r) {
    r = r || {};
    var bits;
    switch (flag) {
        case 'wellbeing':
            var who5 = ['who5_1','who5_2','who5_3','who5_4','who5_5'].reduce(function(s, k) { return s + (typeof r[k] === 'number' ? r[k] : 0); }, 0);
            return 'You scored ' + (who5 * 4) + '% on the WHO-5, below the 52% threshold for poor wellbeing.';
        case 'sleep':
            var lbl = r.sleep_hours === 'under5' ? 'under 5 hours' : '5 to 6 hours';
            return 'You reported sleeping ' + lbl + ' on a typical work night.';
        case 'finances':
            bits = [];
            if (r.emergency === 'no') bits.push('you could not cover a $400 unexpected expense from cash or savings');
            if (r.high_interest_debt === 'yes') bits.push('you are carrying interest-bearing consumer debt');
            return bits.length ? 'You reported that ' + bits.join(' and ') + '.' : '';
        case 'social':
            var ucla = ['ucla_1','ucla_2','ucla_3'].reduce(function(s, k) { return s + (typeof r[k] === 'number' ? r[k] : 0); }, 0);
            bits = [];
            if (ucla >= 6) bits.push('you scored ' + ucla + ' on the UCLA-3 loneliness items (cutoff at 6)');
            if (r.contact_freq === 'monthly') bits.push('you reported monthly meaningful contact with people you feel close to');
            else if (r.contact_freq === 'less') bits.push('you reported less than monthly meaningful contact with people you feel close to');
            return bits.length ? 'You reported that ' + bits.join(' and ') + '.' : '';
        case 'activity':
            bits = [];
            if (r.activity_min === '0') bits.push('no moderate-to-vigorous activity in a typical week');
            else if (r.activity_min === 'under60') bits.push('under 60 minutes of moderate-to-vigorous activity per week');
            if (r.veg_servings === '0-1') bits.push('0 to 1 daily servings of vegetables or fruit');
            else if (r.veg_servings === '2') bits.push('2 daily servings of vegetables or fruit');
            return bits.length ? 'You reported ' + bits.join(' and ') + '.' : '';
    }
    return '';
}

function renderFundR(flags) {
    flags = flags || load(KEY_FUND_FLAGS) || {};
    var responses = load(KEY_FUND_RESP) || fundAnswers;
    var triggered = FUND_ORDER.filter(function(k) { return flags[k]; });
    var lede;
    if (triggered.length === 0) {
        lede = 'Your fundamentals look in good shape – no cutoffs flagged.';
    } else {
        lede = 'Based on your responses, ' + (triggered.length === 1 ? 'one area was' : triggered.length + ' areas were') + ' below the cutoff worth flagging.';
    }
    document.getElementById('fundResultsLede').textContent = lede;

    var html = '';
    if (triggered.length === 0) {
        html += '<div class="all-clear"><h3>All five fundamentals cleared.</h3><p>Sleep, wellbeing, foundational finances, social connection, and physical activity all came back above the cutoffs. Continue to the focus area stage to identify which of the remaining 50 life areas to work on next.</p></div>';
    } else {
        triggered.forEach(function(flag, i) { html += renderFundCard(flag, responses, i === 0); });
    }
    document.getElementById('fundResultsMount').innerHTML = html;
}

function renderFundCard(flag, responses, isFirst) {
    var c = FUND_CONTENT[flag];
    if (!c) return '';
    var classes = 'fund-card' + (isFirst ? ' start-here' : '');
    var pretitle = isFirst ? 'Suggested starting point' : 'Also worth addressing';
    var figure = fundFigure(flag, responses);
    var html = '<div class="' + classes + '">';
    html += '<div class="pretitle">' + escapeHtml(pretitle) + '</div>';
    html += '<h3>' + escapeHtml(c.title) + '</h3>';
    if (figure) html += '<div class="figure">' + escapeHtml(figure) + '</div>';
    html += '<div class="body">' + c.body + '</div>';
    if (c.links && c.links.length) {
        html += '<div class="links">';
        c.links.forEach(function(l) { html += '<a href="' + l.href + '">' + escapeHtml(l.label) + '</a>'; });
        html += '</div>';
    }
    html += '</div>';
    return html;
}

// ════════════════════════════════════════════════════════════════════════
// FOCUS AREA – DEMOGRAPHICS
// ════════════════════════════════════════════════════════════════════════

function renderDemographics() {
    var ageInput = document.getElementById('demoAge');
    if (demographics.age) ageInput.value = demographics.age;
    ageInput.oninput = validateDemo;

    var html = '';
    var opts = [
        { value: 'male', label: 'Male' },
        { value: 'female', label: 'Female' },
        { value: 'they', label: 'Non-binary' },
        { value: 'they', label: 'Prefer not to say' }
    ];
    opts.forEach(function(o, i) {
        var id = 'demoG_' + i;
        var checked = demographics.gender === o.value && demographics.genderLabel === o.label ? 'checked' : '';
        var sel = checked ? ' selected' : '';
        html += '<label class="radio-option' + sel + '" for="' + id + '">';
        html += '<input type="radio" name="demoG" id="' + id + '" value="' + o.value + '" data-label="' + o.label + '" ' + checked + ' onchange="setGender(\'' + o.value + '\', \'' + o.label + '\')">';
        html += '<span>' + o.label + '</span></label>';
    });
    document.getElementById('demoGenderOptions').innerHTML = html;
    validateDemo();
}

function setGender(v, lbl) {
    demographics.gender = v;
    demographics.genderLabel = lbl;
    var rs = document.querySelectorAll('label.radio-option');
    rs.forEach(function(r) { r.classList.remove('selected'); });
    var picked = document.querySelector('input[name="demoG"][data-label="' + lbl + '"]');
    if (picked && picked.parentNode) picked.parentNode.classList.add('selected');
    validateDemo();
}

function validateDemo() {
    var ageVal = parseInt(document.getElementById('demoAge').value, 10);
    if (!isNaN(ageVal) && ageVal >= 13 && ageVal <= 120) demographics.age = ageVal;
    var ok = demographics.age && demographics.gender;
    document.getElementById('demoNext').disabled = !ok;
}

function goToPvq() {
    save(KEY_DEMO, demographics);
    pvqIdx = 0;
    renderPvq();
    showView('FocusPvq');
}

// ════════════════════════════════════════════════════════════════════════
// FOCUS AREA – PVQ
// ════════════════════════════════════════════════════════════════════════

function renderPvq() {
    var item = PVQ.items[pvqIdx];
    var portrait = item[demographics.gender] || item.male;
    var total = PVQ.items.length;
    document.getElementById('pvqProgressText').textContent = 'Focus area – step 2 of 4 – values, item ' + (pvqIdx + 1) + ' of ' + total;
    document.getElementById('pvqProgressFill').style.width = (5 + 45 * pvqIdx / total) + '%';

    var html = '<div class="q-card">';
    html += '<div class="q-section">' + escapeHtml(PVQ.intro) + '</div>';
    html += '<div class="q-text">' + escapeHtml(portrait) + '</div>';
    html += '<div class="q-prompt"><strong>' + escapeHtml(PVQ.prompt) + '</strong></div>';
    var current = pvqAnswers[item.id];
    PVQ.scale.forEach(function(s, i) {
        var checked = (current === s.value) ? 'checked' : '';
        var sel = (current === s.value) ? ' selected' : '';
        var optId = 'pvqOpt_' + i;
        html += '<label class="radio-option' + sel + '" for="' + optId + '">';
        html += '<input type="radio" name="pvqOpt" id="' + optId + '" value="' + s.value + '" ' + checked + ' onchange="onPvqAnswer(' + s.value + ')">';
        html += '<span>' + escapeHtml(s.label) + '</span></label>';
    });
    html += '</div>';
    document.getElementById('pvqMount').innerHTML = html;

    document.getElementById('pvqBack').disabled = (pvqIdx === 0);
    document.getElementById('pvqNext').disabled = (current === undefined);
    document.getElementById('pvqNext').textContent = (pvqIdx === total - 1) ? 'Next: constraints' : 'Next';
}

function onPvqAnswer(value) {
    var item = PVQ.items[pvqIdx];
    pvqAnswers[item.id] = value;
    save(KEY_PVQ, pvqAnswers);
    var labels = document.querySelectorAll('#pvqMount label.radio-option');
    labels.forEach(function(l) { l.classList.remove('selected'); });
    var picked = document.querySelector('input[name="pvqOpt"][value="' + value + '"]');
    if (picked && picked.parentNode) picked.parentNode.classList.add('selected');
    document.getElementById('pvqNext').disabled = false;
}

function pvqNext() {
    if (pvqIdx < PVQ.items.length - 1) { pvqIdx += 1; renderPvq(); }
    else { renderConstraints(); showView('FocusCon'); }
}
function pvqBack() {
    if (pvqIdx > 0) { pvqIdx -= 1; renderPvq(); }
    else { renderDemographics(); showView('FocusDemo'); }
}

// ════════════════════════════════════════════════════════════════════════
// FOCUS AREA – CONSTRAINTS
// ════════════════════════════════════════════════════════════════════════

function areasByPillar() {
    var byP = {};
    LIFE_AREAS.forEach(function(a) {
        if (!byP[a.pillar]) byP[a.pillar] = [];
        byP[a.pillar].push(a);
    });
    return byP;
}

function renderConstraints() {
    var q = CONSTRAINT_QUESTIONS[conPage];
    var totalP = CONSTRAINT_QUESTIONS.length;
    document.getElementById('conProgressText').textContent = 'Focus area – step 3 of 4 – constraints, page ' + (conPage + 1) + ' of ' + totalP;
    document.getElementById('conProgressFill').style.width = (50 + 40 * conPage / totalP) + '%';

    var html = '<div class="con-header">';
    html += '<h3>' + escapeHtml(q.title) + '</h3>';
    html += '<p style="margin: 0 0 8px;"><strong>' + escapeHtml(q.question) + '</strong></p>';
    html += '<p class="help">' + escapeHtml(q.help) + '</p></div>';

    var byP = areasByPillar();
    PILLAR_ORDER.forEach(function(pillar) {
        var areas = byP[pillar] || [];
        if (!areas.length) return;
        html += '<div class="pillar-block"><div class="pillar-head">' + escapeHtml(pillar) + '</div>';
        areas.forEach(function(a) {
            var current = constraintAnswers[q.id][a.slug] || 0;
            html += '<div class="area-row"><div>';
            html += '<div class="area-name">' + escapeHtml(a.name) + '</div>';
            html += '<div class="area-desc">' + escapeHtml(a.desc) + '</div></div>';
            html += '<div class="rate-buttons">';
            for (var i = 0; i <= 3; i++) {
                var cls = 'rate-btn' + (i === 0 ? ' zero' : '') + (current === i ? ' active' : '');
                html += '<button type="button" class="' + cls + '" data-area="' + a.slug + '" data-rating="' + i + '" onclick="setRating(\'' + q.id + '\', \'' + a.slug + '\', ' + i + ')">' + i + '</button>';
            }
            html += '</div></div>';
        });
        html += '</div>';
    });
    document.getElementById('conMount').innerHTML = html;

    document.getElementById('conBack').disabled = false;
    document.getElementById('conNext').textContent = (conPage === totalP - 1) ? 'See focus area' : 'Next';
}

function setRating(qid, slug, r) {
    if (r === 0) delete constraintAnswers[qid][slug];
    else constraintAnswers[qid][slug] = r;
    save(KEY_CON, constraintAnswers);
    var btns = document.querySelectorAll('.rate-btn[data-area="' + slug + '"]');
    btns.forEach(function(b) {
        var rr = parseInt(b.getAttribute('data-rating'), 10);
        b.classList.toggle('active', rr === r);
    });
}

function conNext() {
    if (conPage < CONSTRAINT_QUESTIONS.length - 1) {
        conPage += 1;
        renderConstraints();
        window.scrollTo(0, 0);
    } else {
        finishFocus();
    }
}
function conBack() {
    if (conPage > 0) {
        conPage -= 1;
        renderConstraints();
        window.scrollTo(0, 0);
    } else {
        pvqIdx = PVQ.items.length - 1;
        renderPvq();
        showView('FocusPvq');
    }
}

function finishFocus() {
    var ranked = computeFocusScores();
    var flags = determineFocusFlags(ranked);
    save(KEY_FOCUS_FLAGS, flags);
    save(KEY_FOCUS_DONE, new Date().toISOString());
    renderFocusR();
    showView('FocusR');
}

// ════════════════════════════════════════════════════════════════════════
// FOCUS AREA – SCORING
// ════════════════════════════════════════════════════════════════════════

function pvqScoreForValue(vk) {
    var ids = PVQ.items_by_value[vk] || [];
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
    var t = 0;
    values.forEach(function(v) { t += pvqScoreForValue(v); });
    return t;
}

function constraintForArea(slug) {
    var t = 0;
    CONSTRAINT_QUESTIONS.forEach(function(q) { t += (constraintAnswers[q.id][slug] || 0); });
    return t;
}

function computeFocusScores() {
    var ranked = LIFE_AREAS.map(function(a) {
        var imp = importanceForArea(a.slug);
        var con = constraintForArea(a.slug);
        return { slug: a.slug, name: a.name, pillar: a.pillar, domain: a.domain, importance: imp, constraint: con, score: imp * con };
    });
    ranked.sort(function(a, b) { return b.score - a.score; });
    return ranked;
}

function determineFocusFlags(ranked) {
    var prev = load(KEY_FOCUS_FLAGS) || {};
    var top = ranked[0];
    var balanced = false;
    if (!top || top.score === 0) balanced = true;
    else {
        var t1 = ranked[0].score;
        var t3 = ranked[2] ? ranked[2].score : 0;
        if (t3 > 0 && (t1 - t3) / t1 < 0.10) balanced = true;
    }
    return {
        binding: top ? top.slug : null,
        successors: [ranked[1] ? ranked[1].slug : null, ranked[2] ? ranked[2].slug : null].filter(Boolean),
        balanced: balanced,
        pinned: prev.pinned || null,
        ranked: ranked.slice(0, 52).map(function(r) {
            return { slug: r.slug, score: Math.round(r.score * 10) / 10, importance: Math.round(r.importance * 10) / 10, constraint: r.constraint };
        })
    };
}

function findArea(slug) {
    for (var i = 0; i < LIFE_AREAS.length; i++) if (LIFE_AREAS[i].slug === slug) return LIFE_AREAS[i];
    return null;
}

function reasonForArea(slug) {
    var areaValues = (AREA_VALUES[slug] && AREA_VALUES[slug].values) || [];
    var scored = areaValues.map(function(v) { return { v: v, score: pvqScoreForValue(v) }; })
                            .sort(function(a, b) { return b.score - a.score; });
    var topV = scored.filter(function(x) { return x.score >= 4; }).slice(0, 2);
    var topC = null, topR = 0;
    CONSTRAINT_QUESTIONS.forEach(function(q) {
        var r = constraintAnswers[q.id][slug] || 0;
        if (r > topR) { topR = r; topC = q.id; }
    });
    var parts = [];
    if (topV.length) {
        var labels = topV.map(function(x) { return VALUE_LABELS[x.v]; });
        parts.push('it matches ' + (labels.length === 1 ? 'your value of ' + labels[0] : 'your values of ' + labels.join(' and ')));
    }
    if (topC) parts.push('it ' + CONSTRAINT_LABELS[topC]);
    if (!parts.length) return 'It scored highest on the combined values and constraint signals.';
    return 'Surfaced because ' + parts.join(', and ') + '.';
}

function renderFocusR() {
    var flags = load(KEY_FOCUS_FLAGS) || determineFocusFlags(computeFocusScores());
    var html = '';
    if (flags.balanced && !flags.pinned) {
        html += '<div class="balanced-card"><h2>Your priorities look balanced.</h2></div>';
        html += '<p>No single area stood out as clearly more constraining than the others. The top three by score are below. Pick whichever feels most relevant to start with – any of them is a defensible choice.</p>';
        var top3 = [flags.binding].concat(flags.successors).filter(Boolean);
        top3.forEach(function(slug) { html += renderSuccessor(slug); });
    } else {
        var bindingSlug = flags.pinned || flags.binding;
        if (bindingSlug) html += renderBinding(bindingSlug, flags.pinned ? flags.binding : null);
        flags.successors.forEach(function(slug) { if (slug !== bindingSlug) html += renderSuccessor(slug); });
        if (flags.pinned && flags.binding && flags.binding !== flags.pinned) html += renderSuccessor(flags.binding);
    }

    html += '<div class="override">';
    html += '<h3>Pick a different focus area</h3>';
    html += '<p style="font-size: 0.9em; color: #555;">All 52 areas ranked by combined score. Click a row to pin that as your focus area instead.</p>';
    html += '<div class="override-list">';
    flags.ranked.forEach(function(r) {
        var area = findArea(r.slug);
        if (!area) return;
        var pinned = (flags.pinned === r.slug);
        html += '<div class="override-row' + (pinned ? ' pinned' : '') + '">';
        html += '<span><strong>' + escapeHtml(area.name) + '</strong> <span style="color:#888; font-size: 0.85em;">' + escapeHtml(area.pillar) + '</span></span>';
        html += '<span style="color:#888; font-size: 0.85em; margin-left: auto; margin-right: 12px;">score ' + r.score + '</span>';
        html += '<button class="pin-btn" onclick="pinFocus(\'' + r.slug + '\')">' + (pinned ? 'Pinned' : 'Pin') + '</button>';
        html += '</div>';
    });
    html += '</div>';
    if (flags.pinned) html += '<p style="margin-top: 10px;"><button class="btn-link" onclick="unpinFocus()" style="padding-left: 0;">Clear pin</button></p>';
    html += '</div>';
    document.getElementById('focusResultsMount').innerHTML = html;
}

function renderBinding(slug, computed) {
    var a = findArea(slug);
    if (!a) return '';
    var html = '<div class="binding-card">';
    html += '<div class="pretitle">' + (computed ? 'You pinned' : 'Your focus area') + '</div>';
    html += '<h2>' + escapeHtml(a.name) + '</h2>';
    html += '<div class="reason">' + escapeHtml(reasonForArea(slug)) + '</div>';
    html += '<div class="reason"><em>' + escapeHtml(a.desc) + '</em></div>';
    html += '<div class="links"><a href="' + BASE + '/' + a.slug + '/">Read the ' + escapeHtml(a.name) + ' guide</a></div>';
    html += '</div>';
    return html;
}

function renderSuccessor(slug) {
    var a = findArea(slug);
    if (!a) return '';
    var html = '<div class="successor">';
    html += '<div class="pretitle">Next likely focus once this one clears</div>';
    html += '<h3>' + escapeHtml(a.name) + '</h3>';
    html += '<div class="reason">' + escapeHtml(reasonForArea(slug)) + '</div>';
    html += '<div class="links"><a href="' + BASE + '/' + a.slug + '/">Read the ' + escapeHtml(a.name) + ' guide</a></div>';
    html += '</div>';
    return html;
}

function pinFocus(slug) {
    var f = load(KEY_FOCUS_FLAGS) || {};
    f.pinned = slug;
    save(KEY_FOCUS_FLAGS, f);
    renderFocusR();
    window.scrollTo(0, 0);
}
function unpinFocus() {
    var f = load(KEY_FOCUS_FLAGS) || {};
    f.pinned = null;
    save(KEY_FOCUS_FLAGS, f);
    renderFocusR();
    window.scrollTo(0, 0);
}

// ════════════════════════════════════════════════════════════════════════
// COMBINED SUMMARY
// ════════════════════════════════════════════════════════════════════════

function viewSummary() {
    var triageDone = load(KEY_TRIAGE_DONE);
    var fundDone = load(KEY_FUND_DONE);
    var focusDone = load(KEY_FOCUS_DONE);

    if (!triageDone && !fundDone && !focusDone) {
        skipTo('triage');
        return;
    }

    triageAnswers = load(KEY_TRIAGE_RESP) || {};
    fundAnswers = load(KEY_FUND_RESP) || {};
    demographics = load(KEY_DEMO) || demographics;
    pvqAnswers = load(KEY_PVQ) || {};
    constraintAnswers = load(KEY_CON) || constraintAnswers;

    var stages = [];
    if (triageDone) stages.push('triage');
    if (fundDone) stages.push('fundamentals');
    if (focusDone) stages.push('focus area');
    var lede = 'Combined results from ' + (stages.length === 1 ? stages[0] : stages.length === 2 ? stages.join(' and ') : stages.slice(0, -1).join(', ') + ', and ' + stages[stages.length - 1]) + '.';
    document.getElementById('summaryLede').textContent = lede;

    var html = '';

    if (triageDone) {
        var tFlags = load(KEY_TRIAGE_FLAGS) || {};
        var tTriggered = FLAG_ORDER.filter(function(k) { return tFlags[k]; });
        html += '<h2 class="section-h">Triage</h2>';
        if (tTriggered.length === 0) {
            html += '<div class="all-clear"><h3>Nothing flagged.</h3></div>';
        } else {
            tTriggered.forEach(function(k) { html += renderFlagCard(k, tFlags[k]); });
        }
    }

    if (fundDone) {
        var fFlags = load(KEY_FUND_FLAGS) || {};
        var fTriggered = FUND_ORDER.filter(function(k) { return fFlags[k]; });
        html += '<h2 class="section-h">Fundamentals</h2>';
        if (fTriggered.length === 0) {
            html += '<div class="all-clear"><h3>All five fundamentals cleared.</h3></div>';
        } else {
            fTriggered.forEach(function(flag, i) { html += renderFundCard(flag, fundAnswers, i === 0); });
        }
    }

    if (focusDone) {
        var foFlags = load(KEY_FOCUS_FLAGS) || {};
        html += '<h2 class="section-h">Focus area</h2>';
        var bindingSlug = foFlags.pinned || foFlags.binding;
        if (foFlags.balanced && !foFlags.pinned) {
            html += '<div class="balanced-card"><h2>Your priorities look balanced.</h2></div>';
            var top3 = [foFlags.binding].concat(foFlags.successors || []).filter(Boolean);
            top3.forEach(function(slug) { html += renderSuccessor(slug); });
        } else {
            if (bindingSlug) html += renderBinding(bindingSlug, foFlags.pinned ? foFlags.binding : null);
            (foFlags.successors || []).forEach(function(slug) {
                if (slug !== bindingSlug) html += renderSuccessor(slug);
            });
        }
    }

    var missing = [];
    if (!triageDone) missing.push({ label: 'triage', stage: 'triage' });
    if (!fundDone) missing.push({ label: 'fundamentals', stage: 'fund' });
    if (!focusDone) missing.push({ label: 'focus area', stage: 'focus' });
    if (missing.length) {
        html += '<div class="everything-else"><strong>Stages not yet taken:</strong> ';
        html += missing.map(function(m) {
            return '<a href="#" onclick="skipTo(\'' + m.stage + '\'); return false;">' + m.label + '</a>';
        }).join(' &middot; ');
        html += '</div>';
    }

    document.getElementById('summaryMount').innerHTML = html;
    showView('Summary');
}

// ════════════════════════════════════════════════════════════════════════
// UTILITIES
// ════════════════════════════════════════════════════════════════════════

function escapeHtml(s) {
    if (s === undefined || s === null) return '';
    return String(s)
        .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;').replace(/'/g, '&#039;');
}

window.addEventListener('ap-storage-sync', function() {
    if (!document.getElementById('viewLanding').classList.contains('hidden')) {
        renderLanding();
    }
});

document.addEventListener('DOMContentLoaded', function() {
    triageAnswers = load(KEY_TRIAGE_RESP) || {};
    fundAnswers = load(KEY_FUND_RESP) || {};
    demographics = load(KEY_DEMO) || demographics;
    pvqAnswers = load(KEY_PVQ) || {};
    constraintAnswers = load(KEY_CON) || constraintAnswers;

    var hash = window.location.hash;
    if (hash === '#summary') {
        viewSummary();
    } else if (hash === '#triage') {
        skipTo('triage');
    } else if (hash === '#fundamentals' || hash === '#fund') {
        skipTo('fund');
    } else if (hash === '#focus') {
        skipTo('focus');
    } else {
        renderLanding();
    }
});
</script>
