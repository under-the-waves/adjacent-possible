---
layout: default
title: "Saving – Level 1: Awareness"
life_area_slug: saving
---

<style>
.l1-container { max-width: 800px; margin: 0 auto; }
.l1-subtitle { text-align: center; color: #666; margin-bottom: 24px; font-size: 1.05em; }

/* Progress bar */
.l1-progress { margin-bottom: 32px; }
.l1-progress-bar {
    display: flex;
    gap: 4px;
    margin-bottom: 8px;
}
.l1-progress-segment {
    flex: 1;
    height: 6px;
    background: #e0e0e0;
    border-radius: 3px;
    transition: background 0.3s;
}
.l1-progress-segment.done { background: #28a745; }
.l1-progress-segment.active { background: #155799; }
.l1-progress-label {
    text-align: center;
    font-size: 0.85em;
    color: #888;
}

/* Step sections */
.l1-step {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    margin-bottom: 20px;
    overflow: hidden;
    transition: border-color 0.3s;
}
.l1-step.active { border-color: #155799; }
.l1-step.done { border-color: #28a745; }

.l1-step-header {
    display: flex;
    align-items: center;
    padding: 16px 20px;
    cursor: pointer;
    background: #f8f9fa;
    user-select: none;
    transition: background 0.2s;
}
.l1-step-header:hover { background: #f0f0f0; }

.l1-step-number {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    font-size: 0.9em;
    margin-right: 14px;
    flex-shrink: 0;
    background: #e0e0e0;
    color: #666;
    transition: background 0.3s, color 0.3s;
}
.l1-step.active .l1-step-number { background: #155799; color: white; }
.l1-step.done .l1-step-number { background: #28a745; color: white; }

.l1-step-title {
    font-weight: 600;
    font-size: 1.05em;
    flex: 1;
}

.l1-step-check {
    font-size: 1.2em;
    color: #28a745;
    display: none;
}
.l1-step.done .l1-step-check { display: block; }

.l1-step-expand {
    font-size: 0.8em;
    color: #888;
    margin-left: 8px;
    transition: transform 0.2s;
}
.l1-step.open .l1-step-expand { transform: rotate(180deg); }

.l1-step-body {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease;
}
.l1-step.open .l1-step-body { max-height: 3000px; }

.l1-step-content {
    padding: 0 20px 20px 20px;
    line-height: 1.6;
}
.l1-step-content p { margin: 0 0 12px 0; }
.l1-step-content h3 { margin: 16px 0 8px 0; font-size: 1em; }

.l1-mark-done {
    display: inline-block;
    padding: 10px 24px;
    background: #155799;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.95em;
    font-weight: 600;
    margin-top: 12px;
    transition: background 0.2s;
}
.l1-mark-done:hover { background: #0d47a1; }
.l1-mark-done:disabled { background: #ccc; cursor: default; }

/* Exemplar cards */
.exemplar-card {
    background: #f8f9fa;
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 12px;
    border-left: 4px solid #155799;
}
.exemplar-card h4 { margin: 0 0 4px 0; font-size: 1em; }
.exemplar-card .exemplar-value { font-size: 0.85em; color: #155799; font-weight: 600; margin-bottom: 6px; }
.exemplar-card p { margin: 0 0 6px 0; font-size: 0.93em; color: #444; }

/* Assessment inputs */
.assess-privacy {
    background: #f0f4ff;
    border-left: 4px solid #155799;
    border-radius: 6px;
    padding: 14px 18px;
    margin-bottom: 24px;
    font-size: 0.9em;
    color: #333;
    line-height: 1.5;
}
.assess-group { margin-bottom: 24px; }
.assess-group h4 { margin: 0 0 12px 0; }
.assess-input-group {
    padding: 14px 18px;
    margin-bottom: 10px;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    font-size: 0.93em;
    line-height: 1.4;
    transition: border-color 0.2s;
}
.assess-input-group.answered { border-color: #28a745; background: #f9fdf9; }
.assess-input-group .assess-label {
    display: block;
    font-weight: 500;
    margin-bottom: 6px;
}
.assess-input-group .assess-hint {
    font-size: 0.85em;
    color: #888;
    margin-bottom: 8px;
}
.assess-input-group input[type="number"] {
    width: 100px;
    padding: 6px 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 0.95em;
}
.assess-input-group select {
    padding: 6px 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 0.95em;
    max-width: 100%;
}
.assess-skip {
    display: flex;
    align-items: center;
    gap: 6px;
    margin-top: 8px;
    font-size: 0.85em;
    color: #888;
}
.assess-skip input[type="checkbox"] {
    accent-color: #888;
}
.assess-percentile-hint {
    display: inline-block;
    margin-left: 12px;
    font-size: 0.85em;
    color: #888;
    font-style: italic;
}
.assess-summary {
    background: #f8f9fa;
    border: 2px solid #155799;
    border-radius: 8px;
    padding: 20px 24px;
    margin-top: 24px;
    display: none;
}
.assess-summary.visible { display: block; }
.assess-summary h4 { margin: 0 0 14px 0; color: #155799; }
.assess-summary-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 10px;
    font-size: 0.93em;
}
.assess-summary-label { flex: 0 0 200px; font-weight: 500; }
.assess-summary-bar {
    flex: 1;
    height: 8px;
    background: #e0e0e0;
    border-radius: 4px;
    overflow: hidden;
}
.assess-summary-fill {
    height: 100%;
    background: #28a745;
    border-radius: 4px;
    transition: width 0.4s;
}
.assess-summary-value {
    flex: 0 0 60px;
    text-align: right;
    font-weight: 600;
    color: #155799;
}
.assess-summary-text {
    font-size: 0.88em;
    color: #555;
    margin-top: 2px;
}
@media (max-width: 600px) {
    .assess-summary-label { flex: 0 0 120px; }
}

/* Completion */
.l1-complete {
    text-align: center;
    padding: 32px 20px;
    background: #f0f7f0;
    border: 2px solid #28a745;
    border-radius: 8px;
    margin-top: 24px;
    display: none;
}
.l1-complete.visible { display: block; }
.l1-complete h2 { color: #1a6b2a; margin: 0 0 12px 0; }
.l1-complete p { margin: 0 0 16px 0; }
.l1-complete .btn-cta {
    display: inline-block;
    padding: 12px 28px;
    background: #28a745;
    color: white;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
    font-size: 1.05em;
    transition: background 0.2s;
}
.l1-complete .btn-cta:hover { background: #218838; }
</style>

<div class="l1-container">

<h1>Saving: Level 1</h1>

<p class="l1-subtitle">Understand what saving means, what's possible, and where you stand. About 15 minutes.</p>

<div class="l1-progress">
    <div class="l1-progress-bar">
        <div class="l1-progress-segment" id="prog-1"></div>
        <div class="l1-progress-segment" id="prog-2"></div>
        <div class="l1-progress-segment" id="prog-3"></div>
        <div class="l1-progress-segment" id="prog-4"></div>
        <div class="l1-progress-segment" id="prog-5"></div>
    </div>
    <div class="l1-progress-label" id="progressLabel">Step 1 of 5</div>
</div>

<!-- Step 1: Why Saving Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why saving matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Saving is the single most foundational financial behaviour. The evidence for its impact on wellbeing is strong and consistent.</p>

<p><a href="https://corporate.vanguard.com/content/corporatesite/us/en/corp/articles/emergency-savings-financial-wellbeing.html" target="_blank">Emergency savings are the strongest predictor</a> of overall financial wellbeing &ndash; stronger than income level, debt-to-income ratio, or investment portfolio size. Having even a modest emergency fund significantly reduces financial stress and improves decision-making across all other financial domains.</p>

<p>Yet most people have dangerously thin buffers. <a href="https://www.bankrate.com/banking/savings/emergency-savings-report/" target="_blank">24 – 27% of adults</a> have no emergency savings at all, and only 27 – 28% have six or more months of expenses saved. The <a href="https://fred.stlouisfed.org/series/PSAVERT" target="_blank">national savings rate</a> hovers between 3 – 5%, and the <a href="https://www.bls.gov/cex/tables.htm" target="_blank">bottom 40% of earners</a> have negative savings rates.</p>

<p>The psychological cost is substantial. People without emergency savings spend an average of 7.3 hours per week worrying about finances &ndash; nearly double the rate of those with even a modest buffer. Saving creates genuine choice: a financial buffer turns forced reactions into deliberate decisions, giving you the freedom to leave a bad job, seize an opportunity, or weather a crisis without going into debt.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about saving</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People save for different reasons. This site scores every saving intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Security</h3>
<p>Building and maintaining a financial buffer against unexpected expenses and income disruption. People who lean towards this value focus on emergency funds, insurance, and ensuring their reserves can absorb shocks without resorting to debt. They prioritise stability and protection from downside scenarios.</p>

<h3>Lifestyle</h3>
<p>Saving toward specific lifestyle goals &ndash; holidays, experiences, purchases, and planned upgrades to quality of life. People who lean towards this value see saving as a tool for living better, not just surviving emergencies. They balance present enjoyment with future security and maintain targeted savings accounts for near-term goals.</p>

<h3>Growth</h3>
<p>Accumulating wealth over time through consistently high savings rates. People who lean towards this value focus on the long-term trajectory of their wealth &ndash; steadily increasing net worth, maximising the rate at which savings compound, and sustaining saving discipline across years and decades.</p>

<button class="l1-mark-done" onclick="completeStep('values')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 3: What's Achievable -->
<div class="l1-step" id="step-achievable" data-step="achievable">
    <div class="l1-step-header" onclick="toggleStep('achievable')">
        <div class="l1-step-number">3</div>
        <div class="l1-step-title">What's achievable</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each saving value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Security &ndash; Level 5</div>
    <p><a href="https://www.mrmoneymustache.com/about/" target="_blank">Pete Adeney</a> (Mr. Money Mustache) retired at 30 after saving aggressively on a moderate software engineering salary. He accumulated enough invested assets to cover his family's living expenses indefinitely without earned income, achieving complete financial security through disciplined saving and frugal living. His detailed public accounting of household expenses demonstrates sustained annual spending well below the median, funded entirely by investment returns.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Lifestyle &ndash; Level 5</div>
    <p><a href="https://affordanything.com/about/" target="_blank">Paula Pant</a> built a savings system designed explicitly around lifestyle goals. She saved enough to buy multiple rental properties in her 20s, then used the income to fund extended international travel and eventual full financial independence. Her approach treats saving as the mechanism for buying freedom and experiences, maintaining full liquidity and access to capital at all times while funding a deliberately chosen lifestyle.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Growth &ndash; Level 5</div>
    <p><a href="https://earlyretirementextreme.com/about" target="_blank">Jacob Lund Fisker</a> (Early Retirement Extreme) sustained a savings rate above 75% for five years on a postdoctoral researcher's salary, accumulating 25 times his annual expenses and reaching full financial independence by age 33. His meticulous documentation of the process shows how extreme savings rates compress the timeline to financial independence from decades to years.</p>
</div>

<button class="l1-mark-done" onclick="completeStep('achievable')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 4: Where You Are -->
<div class="l1-step" id="step-assess" data-step="assess">
    <div class="l1-step-header" onclick="toggleStep('assess')">
        <div class="l1-step-number">4</div>
        <div class="l1-step-title">Where you are now</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<div class="assess-privacy">Your answers are stored only on your device and are never sent to our servers. Only your estimated percentile scores (single numbers, not your answers) may be synced if you create an account. Percentile estimates are approximate – they position you roughly relative to the general population based on your self-report, but could easily be off by 10–15 points.</div>

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to look up.</p>

<div class="assess-group">
<h4>Security</h4>

<div class="assess-input-group" id="ig-monthly-essentials">
    <span class="assess-label">What are your monthly essential expenses?</span>
    <span class="assess-hint">Add up your non-negotiable outgoings: housing, food, utilities, and transport. Exclude discretionary spending like dining out or subscriptions.</span>
    <input type="number" id="a-monthly-essentials" min="0" max="20000" step="50" placeholder="e.g. 1500" onchange="handleAssessInput('a-monthly-essentials')"> <span class="assess-percentile-hint" id="pct-monthly-essentials"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-monthly-essentials" onchange="handleSkip('a-monthly-essentials')"><label for="skip-monthly-essentials">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-buffer-months">
    <span class="assess-label">How many months of essential expenses do you hold in accessible savings?</span>
    <span class="assess-hint">Divide your accessible savings by your monthly essential expenses. Only count money you could access within a week.</span>
    <input type="number" id="a-buffer-months" min="0" max="120" step="0.5" placeholder="e.g. 3" onchange="handleAssessInput('a-buffer-months')"> <span class="assess-percentile-hint" id="pct-buffer-months"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-buffer-months" onchange="handleSkip('a-buffer-months')"><label for="skip-buffer-months">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-income-disruption">
    <span class="assess-label">What would happen to your finances if you lost your income for three months?</span>
    <span class="assess-hint">Consider savings, benefits, notice periods, and any other safety nets you have.</span>
    <select id="a-income-disruption" onchange="handleAssessInput('a-income-disruption')">
        <option value="">Select...</option>
        <option value="0">I would go into debt or miss essential payments</option>
        <option value="1">I would need to cut back significantly but could manage</option>
        <option value="2">I could cover essentials from savings without major lifestyle changes</option>
        <option value="3">I could maintain my full lifestyle from savings alone</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-income-disruption" onchange="handleSkip('a-income-disruption')"><label for="skip-income-disruption">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Lifestyle</h4>

<div class="assess-input-group" id="ig-liquidity-profile">
    <span class="assess-label">What proportion of your savings is instantly accessible versus locked away?</span>
    <span class="assess-hint">Consider how much you could access within 24 hours versus what is locked in pensions, notice accounts, or other restricted vehicles.</span>
    <select id="a-liquidity-profile" onchange="handleAssessInput('a-liquidity-profile')">
        <option value="">Select...</option>
        <option value="0">I don't know</option>
        <option value="1">Most is locked away &ndash; less than 25% is instantly accessible</option>
        <option value="2">Roughly half is accessible</option>
        <option value="3">Most is accessible &ndash; 75%+ available within 24 hours</option>
        <option value="4">Nearly all is accessible &ndash; 90%+ available within 24 hours</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-liquidity-profile" onchange="handleSkip('a-liquidity-profile')"><label for="skip-liquidity-profile">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-specific-goals">
    <span class="assess-label">Are you currently saving toward any specific goals, and if so, how much progress have you made?</span>
    <span class="assess-hint">Examples: a holiday, a deposit on a house, a car, or a particular experience.</span>
    <select id="a-specific-goals" onchange="handleAssessInput('a-specific-goals')">
        <option value="">Select...</option>
        <option value="0">No specific saving goals</option>
        <option value="1">I have goals in mind but haven't started saving for them</option>
        <option value="2">I'm actively saving toward at least one specific goal</option>
        <option value="3">I'm making strong progress &ndash; over halfway to my primary goal</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-specific-goals" onchange="handleSkip('a-specific-goals')"><label for="skip-specific-goals">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-enjoyment-tradeoffs">
    <span class="assess-label">Does your current saving rate feel sustainable, or does it come at the cost of things you value?</span>
    <span class="assess-hint">Are you saving comfortably, or does it feel like a constant sacrifice?</span>
    <select id="a-enjoyment-tradeoffs" onchange="handleAssessInput('a-enjoyment-tradeoffs')">
        <option value="">Select...</option>
        <option value="0">I'm not saving at all</option>
        <option value="1">Saving feels like a constant sacrifice</option>
        <option value="2">Saving requires effort but feels manageable</option>
        <option value="3">Saving feels comfortable and sustainable</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-enjoyment-tradeoffs" onchange="handleSkip('a-enjoyment-tradeoffs')"><label for="skip-enjoyment-tradeoffs">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Growth</h4>

<div class="assess-input-group" id="ig-savings-rate">
    <span class="assess-label">What percentage of your income do you save each month?</span>
    <span class="assess-hint">Divide your monthly savings by your monthly take-home pay. Include pension contributions if you wish.</span>
    <input type="number" id="a-savings-rate" min="0" max="100" step="1" placeholder="e.g. 15" onchange="handleAssessInput('a-savings-rate')"> <span class="assess-percentile-hint" id="pct-savings-rate"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-savings-rate" onchange="handleSkip('a-savings-rate')"><label for="skip-savings-rate">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-total-saved">
    <span class="assess-label">What is your total savings balance across all accounts?</span>
    <span class="assess-hint">Include current account buffers, savings accounts, ISAs, and any other liquid assets. Exclude pensions and property.</span>
    <input type="number" id="a-total-saved" min="0" max="10000000" step="500" placeholder="e.g. 25000" onchange="handleAssessInput('a-total-saved')"> <span class="assess-percentile-hint" id="pct-total-saved"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-total-saved" onchange="handleSkip('a-total-saved')"><label for="skip-total-saved">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-savings-trend">
    <span class="assess-label">Have your total savings been growing, shrinking, or staying flat over the past 6 months?</span>
    <span class="assess-hint">Even a rough sense counts &ndash; you don't need exact figures.</span>
    <select id="a-savings-trend" onchange="handleAssessInput('a-savings-trend')">
        <option value="">Select...</option>
        <option value="0">Shrinking</option>
        <option value="1">Staying roughly flat</option>
        <option value="2">Growing slowly</option>
        <option value="3">Growing steadily</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-savings-trend" onchange="handleSkip('a-savings-trend')"><label for="skip-savings-trend">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-security">
        <span class="assess-summary-label">Security</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-security" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-security">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-growth">
        <span class="assess-summary-label">Growth</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-growth" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-growth">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data for American and British adults. Lifestyle items are recorded for your awareness but not scored, as the available data does not support reliable percentile estimates.</p>
</div>

<button class="l1-mark-done" id="assessBtn" onclick="completeStep('assess')" disabled>Answer all items to continue</button>

        </div>
    </div>
</div>

<!-- Step 5: Set Values & See Interventions -->
<div class="l1-step" id="step-interventions" data-step="interventions">
    <div class="l1-step-header" onclick="toggleStep('interventions')">
        <div class="l1-step-number">5</div>
        <div class="l1-step-title">Set your values and see your interventions</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>You now understand why saving matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about security, lifestyle, and growth. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/saving/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Saving Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Saving. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/saving/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'saving';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-monthly-essentials', 'a-buffer-months', 'a-income-disruption',
        'a-liquidity-profile', 'a-specific-goals', 'a-enjoyment-tradeoffs',
        'a-savings-rate', 'a-total-saved', 'a-savings-trend'
    ];

    // Scoring thresholds: [{value, percentile}, ...] sorted by value ascending
    // Sources:
    //   buffer-months: Bankrate Emergency Savings Report (24-27% have 0; 46% have 3+; 27% have 6+)
    //   savings-rate: FRED PSAVERT (national avg 3-5%); BLS Consumer Expenditure Survey
    //   total-saved: Federal Reserve Survey of Consumer Finances (median liquid savings ~$8,000)
    var THRESHOLDS = {
        'a-monthly-essentials': null, // unscored -- context variable, no population ranking
        'a-buffer-months': [
            {v:0,p:10},{v:1,p:30},{v:3,p:50},{v:6,p:73},{v:12,p:92},{v:24,p:97},{v:60,p:99}
        ],
        'a-income-disruption': [
            {v:'0',p:20},{v:'1',p:45},{v:'2',p:72},{v:'3',p:92}
        ],
        'a-liquidity-profile': null, // unscored
        'a-specific-goals': null, // unscored
        'a-enjoyment-tradeoffs': null, // unscored
        'a-savings-rate': [
            {v:0,p:15},{v:3,p:35},{v:5,p:45},{v:10,p:60},{v:15,p:75},{v:20,p:82},{v:30,p:90},{v:40,p:95},{v:60,p:99}
        ],
        'a-total-saved': [
            {v:0,p:10},{v:1000,p:25},{v:5000,p:40},{v:10000,p:55},{v:25000,p:70},{v:50000,p:80},{v:100000,p:88},{v:250000,p:95},{v:500000,p:98}
        ],
        'a-savings-trend': [
            {v:'0',p:20},{v:'1',p:40},{v:'2',p:65},{v:'3',p:85}
        ]
    };

    var VALUE_ITEMS = {
        security: ['a-buffer-months', 'a-income-disruption'],
        growth: ['a-savings-rate', 'a-total-saved', 'a-savings-trend']
    };

    // Lifestyle items are recorded but not scored (insufficient population data for percentile estimates)
    var UNSCORED_ITEMS = ['a-monthly-essentials', 'a-liquidity-profile', 'a-specific-goals', 'a-enjoyment-tradeoffs'];

    function loadProgress() {
        if (typeof APStorage === 'undefined') return {};
        var all = APStorage.load('ap-level1-progress') || {};
        return all[AREA] || {};
    }

    function saveProgress(progress) {
        if (typeof APStorage === 'undefined') return;
        var all = APStorage.load('ap-level1-progress') || {};
        all[AREA] = progress;
        APStorage.save('ap-level1-progress', all);
    }

    function updateUI() {
        var progress = loadProgress();
        var doneCount = 0;
        var firstIncomplete = null;

        STEPS.forEach(function(step, i) {
            var el = document.getElementById('step-' + step);
            var seg = document.getElementById('prog-' + (i + 1));
            if (!el || !seg) return;

            if (progress[step]) {
                el.classList.add('done');
                el.classList.remove('active');
                seg.className = 'l1-progress-segment done';
                doneCount++;
            } else if (!firstIncomplete) {
                firstIncomplete = step;
                el.classList.add('active');
                el.classList.remove('done');
                seg.className = 'l1-progress-segment active';
            } else {
                el.classList.remove('active', 'done');
                seg.className = 'l1-progress-segment';
            }
        });

        var label = document.getElementById('progressLabel');
        if (doneCount >= STEPS.length) {
            if (label) label.textContent = 'All steps complete';
            var banner = document.getElementById('completeBanner');
            if (banner) banner.classList.add('visible');
        } else {
            if (label) label.textContent = 'Step ' + (doneCount + 1) + ' of ' + STEPS.length;
        }

        // Auto-open the first incomplete step
        if (firstIncomplete) {
            openStep(firstIncomplete);
        }
    }

    function openStep(step) {
        STEPS.forEach(function(s) {
            var el = document.getElementById('step-' + s);
            if (el) el.classList.remove('open');
        });
        var target = document.getElementById('step-' + step);
        if (target) {
            target.classList.add('open');
            setTimeout(function() {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100);
        }
    }

    window.toggleStep = function(step) {
        var el = document.getElementById('step-' + step);
        if (el) el.classList.toggle('open');
    };

    window.completeStep = function(step) {
        if (step === 'assess') saveScores();
        var progress = loadProgress();
        progress[step] = true;
        saveProgress(progress);
        updateUI();

        var idx = STEPS.indexOf(step);
        if (idx >= 0 && idx < STEPS.length - 1) {
            var next = STEPS[idx + 1];
            setTimeout(function() { openStep(next); }, 300);
        }
    };

    // --- Scoring functions ---

    function ordinalSuffix(n) {
        var s = ['th','st','nd','rd'];
        var v = n % 100;
        return n + (s[(v-20)%10] || s[v] || s[0]);
    }
    function interpolatePercentile(value, thresholds) {
        var num = parseFloat(value);
        // Check if thresholds use string keys (dropdowns)
        if (typeof thresholds[0].v === 'string') {
            for (var i = 0; i < thresholds.length; i++) {
                if (thresholds[i].v === String(value)) return thresholds[i].p;
            }
            return null;
        }
        // Check if inverted (first threshold has higher value than last)
        var inverted = thresholds[0].v > thresholds[thresholds.length - 1].v;
        if (inverted) {
            if (num >= thresholds[0].v) return thresholds[0].p;
            if (num <= thresholds[thresholds.length - 1].v) return thresholds[thresholds.length - 1].p;
            for (var i = 0; i < thresholds.length - 1; i++) {
                if (num <= thresholds[i].v && num >= thresholds[i + 1].v) {
                    var t = (thresholds[i].v - num) / (thresholds[i].v - thresholds[i + 1].v);
                    return Math.round(thresholds[i].p + t * (thresholds[i + 1].p - thresholds[i].p));
                }
            }
        } else {
            if (num <= thresholds[0].v) return thresholds[0].p;
            if (num >= thresholds[thresholds.length - 1].v) return thresholds[thresholds.length - 1].p;
            for (var i = 0; i < thresholds.length - 1; i++) {
                if (num >= thresholds[i].v && num <= thresholds[i + 1].v) {
                    var t = (num - thresholds[i].v) / (thresholds[i + 1].v - thresholds[i].v);
                    return Math.round(thresholds[i].p + t * (thresholds[i + 1].p - thresholds[i].p));
                }
            }
        }
        return null;
    }

    function getItemPercentile(itemId) {
        if (THRESHOLDS[itemId] === null) return null; // unscored item
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return null;

        var el = document.getElementById(itemId);
        if (!el) return null;
        var val = el.value;
        if (val === '' || val === null) return null;
        return interpolatePercentile(val, THRESHOLDS[itemId]);
    }

    function computeValuePercentile(valueKey) {
        var items = VALUE_ITEMS[valueKey];
        var total = 0, count = 0;
        items.forEach(function(id) {
            var pct = getItemPercentile(id);
            if (pct !== null) { total += pct; count++; }
        });
        return count > 0 ? Math.round(total / count) : null;
    }

    function isItemAnswered(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return true;

        var el = document.getElementById(itemId);
        return el && el.value !== '' && el.value !== null;
    }

    function updatePercentileHint(itemId) {
        if (UNSCORED_ITEMS.indexOf(itemId) !== -1) return; // no hints for unscored items
        if (THRESHOLDS[itemId] === null) return;
        var hintEl = document.getElementById('pct-' + itemId.replace('a-', ''));
        if (!hintEl) return;
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) {
            hintEl.textContent = 'Skipped';
            return;
        }
        var pct = getItemPercentile(itemId);
        hintEl.textContent = pct !== null ? 'roughly ' + ordinalSuffix(Math.round(pct / 10) * 10) + ' percentile' : '';
    }

    function updateInputGroupState(itemId) {
        var group = document.getElementById('ig-' + itemId.replace('a-', ''));
        if (group) group.classList.toggle('answered', isItemAnswered(itemId));
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['security', 'growth'].forEach(function(vk) {
            var pct = computeValuePercentile(vk);
            var barEl = document.getElementById('bar-' + vk);
            var valEl = document.getElementById('val-' + vk);
            if (barEl && valEl) {
                if (pct !== null) {
                    barEl.style.width = pct + '%';
                    valEl.textContent = ordinalSuffix(Math.round(pct / 10) * 10);
                    anyAnswered = true;
                } else {
                    barEl.style.width = '0%';
                    valEl.innerHTML = '&ndash;';
                }
            }
        });
        var summary = document.getElementById('assessSummary');
        if (summary) summary.classList.toggle('visible', anyAnswered);
    }

    function saveAnswers() {
        var answers = {};
        ASSESS_IDS.forEach(function(id) {
            var skipBox = document.getElementById('skip-' + id.replace('a-', ''));
            var skipped = skipBox && skipBox.checked;
            var value = null;

            if (!skipped) {
                var el = document.getElementById(id);
                if (el && el.value !== '') value = el.value;
            }
            answers[id] = { value: value, skipped: skipped };
        });
        // Save raw answers directly to localStorage (NOT via APStorage)
        var allAnswers = {};
        try { allAnswers = JSON.parse(localStorage.getItem('ap-level1-answers')) || {}; } catch(e) {}
        allAnswers[AREA] = answers;
        localStorage.setItem('ap-level1-answers', JSON.stringify(allAnswers));

        // Save booleans to ap-level1-assess for backward compat (via APStorage, syncs to Clerk)
        var checklist = {};
        ASSESS_IDS.forEach(function(id) { checklist[id] = isItemAnswered(id); });
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-assess') || {};
            all[AREA] = checklist;
            APStorage.save('ap-level1-assess', all);
        }
    }

    function saveScores() {
        var scores = {};
        ['security', 'growth'].forEach(function(vk) {
            scores[vk] = computeValuePercentile(vk);
        });
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-scores') || {};
            all[AREA] = scores;
            APStorage.save('ap-level1-scores', all);
        }
    }

    function updateAssessCompletion() {
        var allAnswered = ASSESS_IDS.every(function(id) { return isItemAnswered(id); });
        var btn = document.getElementById('assessBtn');
        if (btn) {
            btn.disabled = !allAnswered;
            btn.textContent = allAnswered ? 'All done \u2013 continue' : 'Answer all items to continue';
        }
    }

    // --- Event handlers ---

    window.handleAssessInput = function(itemId) {
        updatePercentileHint(itemId);
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessSummary();
        updateAssessCompletion();
    };

    window.handleSkip = function(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        var input = document.getElementById(itemId);
        if (skipBox && input) {
            input.disabled = skipBox.checked;
            if (skipBox.checked && input.tagName === 'SELECT') input.value = '';
            if (skipBox.checked && input.type === 'number') input.value = '';
        }
        updatePercentileHint(itemId);
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessSummary();
        updateAssessCompletion();
    };

    // --- Restore saved answers ---

    function restoreAssessment() {
        var allAnswers = {};
        try { allAnswers = JSON.parse(localStorage.getItem('ap-level1-answers')) || {}; } catch(e) {}
        var answers = allAnswers[AREA];
        if (!answers) return;

        ASSESS_IDS.forEach(function(id) {
            var item = answers[id];
            if (!item) return;

            if (item.skipped) {
                var skipBox = document.getElementById('skip-' + id.replace('a-', ''));
                if (skipBox) {
                    skipBox.checked = true;
                    var input = document.getElementById(id);
                    if (input) input.disabled = true;
                }
            } else if (item.value !== null) {
                var el = document.getElementById(id);
                if (el) el.value = item.value;
            }

            updatePercentileHint(id);
            updateInputGroupState(id);
        });

        updateAssessSummary();
        updateAssessCompletion();
    }

    document.addEventListener('DOMContentLoaded', function() {
        restoreAssessment();
        updateUI();
    });
})();
</script>
