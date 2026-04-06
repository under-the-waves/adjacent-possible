---
layout: default
title: "Housing – Level 1: Awareness"
life_area_slug: housing
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

/* Assessment checklist */
.assess-group { margin-bottom: 20px; }
.assess-group h4 { margin: 0 0 10px 0; }
.assess-item {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 10px 14px;
    margin-bottom: 6px;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    cursor: pointer;
    transition: border-color 0.2s, background 0.2s;
    font-size: 0.93em;
    line-height: 1.4;
}
.assess-item:hover { border-color: #155799; background: #f0f4ff; }
.assess-item.checked { border-color: #28a745; background: #f0f7f0; }
.assess-item input[type="checkbox"] {
    margin-top: 2px;
    flex-shrink: 0;
    accent-color: #28a745;
}
.assess-item label { cursor: pointer; flex: 1; }
.assess-hint {
    font-size: 0.85em;
    color: #888;
    margin-top: 2px;
}

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
.assess-recorded {
    background: #f0f7f0;
    border: 2px solid #28a745;
    border-radius: 8px;
    padding: 16px 20px;
    margin-top: 24px;
    text-align: center;
    font-size: 0.95em;
    color: #1a6b2a;
    display: none;
}
.assess-recorded.visible { display: block; }

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

<h1>Housing: Level 1</h1>

<p class="l1-subtitle">Understand what housing means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Housing Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why housing matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Housing is the single largest expense most people face, and its effects extend well beyond the financial. Where and how you live shapes your physical health, mental health, relationships, and daily quality of life.</p>

<p>Research published in the <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9914515/" target="_blank">Journal of Housing and the Built Environment</a> found that households spending more than 30% of income on housing report significantly lower life satisfaction. Nearly <a href="https://www.census.gov/newsroom/press-releases/2024/renter-households-cost-burdened-race.html" target="_blank">half of renters</a> (49.7%) and 23.7% of homeowners exceed this threshold.</p>

<p>The effects go well beyond cost. Housing quality is linked to <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12333583/" target="_blank">material hardship, lower cognitive achievement for children, higher maternal stress, and strained social and familial relationships</a>. Poor housing conditions &ndash; damp, cold, overcrowding, noise &ndash; are associated with respiratory illness, sleep disruption, and chronic stress.</p>

<p>Location matters too. Commute time is one of the strongest predictors of daily wellbeing, with research in <a href="https://link.springer.com/article/10.1007/s11116-019-09983-9" target="_blank">Transportation</a> showing that longer commutes are associated with lower life satisfaction, less sleep, and reduced time for exercise and social connection. Your housing situation is the foundation on which other life areas rest.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about housing</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People make housing decisions for different reasons. This site scores every housing intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Comfort</h3>
<p>The physical quality of your living environment &ndash; space, light, temperature, noise levels, maintenance condition, and overall pleasantness. Having enough room for your activities, a well-functioning home that does not create daily friction, and an environment that supports rest and productivity. People who lean towards this value invest in the quality of their living space.</p>

<h3>Affordability</h3>
<p>Keeping housing costs at a sustainable level that preserves financial flexibility for other life goals. Mortgage or rent payments, utilities, maintenance, insurance, and taxes remaining below burdensome thresholds. People who lean towards this value make housing decisions that protect their broader financial health.</p>

<h3>Location</h3>
<p>Proximity to work, social connections, amenities, nature, and the quality of the surrounding neighbourhood. Commute time, access to services, safety, community character, and the fit between your lifestyle needs and what the location provides. People who lean towards this value choose where to live based on how the location supports their daily life.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each housing value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Comfort &ndash; Level 5</div>
    <p><a href="https://www.christophlowell.com/" target="_blank">Christopher Lowell</a> is an interior designer who has spent decades demonstrating how to create exceptionally comfortable living environments without excessive budgets. His approach centres on spatial flow, natural light maximisation, and designing rooms around daily rhythms. His own homes have consistently reflected these principles &ndash; purpose-designed spaces for work, rest, and socialising with no deferred maintenance or unresolved friction points.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Affordability &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Jay_Shafer" target="_blank">Jay Shafer</a> pioneered the tiny house movement by designing and living in homes under 10 square metres. He founded the Tumbleweed Tiny House Company and has lived in his own small-footprint houses since the late 1990s, consistently keeping his housing costs to a fraction of the national average. His approach demonstrates that deliberate downsizing can free up both money and time without sacrificing comfort.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Location &ndash; Level 5</div>
    <p><a href="https://www.strongtowns.org/charles-marohn" target="_blank">Charles Marohn</a> is an urban planner and author who has written extensively about what makes neighbourhoods work. He lives in a walkable small-town setting that he chose specifically for its combination of community connection, access to daily needs, natural environment, and manageable scale &ndash; a deliberate alignment between location and lifestyle priorities that he has maintained for decades.</p>
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

<div class="assess-privacy">Your answers are stored only on your device and are never sent to our servers. Only your estimated percentile scores (single numbers, not your answers) may be synced if you create an account.</div>

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to reflect on.</p>

<div class="assess-group">
<h4>Comfort</h4>

<div class="assess-input-group" id="ig-space">
    <span class="assess-label">How well do your rooms serve their intended purpose?</span>
    <span class="assess-hint">Bedroom, workspace, kitchen, shared living areas &ndash; are any too small, too dark, or poorly laid out?</span>
    <select id="a-space" onchange="handleAssessInput('a-space')">
        <option value="">Select...</option>
        <option value="poorly">Poorly &ndash; multiple rooms don't work well</option>
        <option value="some-issues">Some issues &ndash; one or two rooms need improvement</option>
        <option value="adequate">Adequate &ndash; they work but aren't ideal</option>
        <option value="well">Well &ndash; most rooms suit their purpose</option>
        <option value="excellent">Excellent &ndash; every room is well-suited to its function</option>
    </select> <span class="assess-percentile-hint" id="pct-space"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-space" onchange="handleSkip('a-space')"><label for="skip-space">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-temperature">
    <span class="assess-label">Does your home stay at a comfortable temperature year-round?</span>
    <span class="assess-hint">Draughts, insulation, rooms that are consistently too hot or cold.</span>
    <select id="a-temperature" onchange="handleAssessInput('a-temperature')">
        <option value="">Select...</option>
        <option value="poor">Poor &ndash; uncomfortable in multiple seasons</option>
        <option value="some-problems">Some problems &ndash; draughty or inconsistent</option>
        <option value="mostly-ok">Mostly OK &ndash; comfortable most of the time</option>
        <option value="good">Good &ndash; comfortable year-round with reasonable costs</option>
        <option value="excellent">Excellent &ndash; well-insulated and efficiently heated/cooled</option>
    </select> <span class="assess-percentile-hint" id="pct-temperature"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-temperature" onchange="handleSkip('a-temperature')"><label for="skip-temperature">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-maintenance">
    <span class="assess-label">How many maintenance issues have you been putting off?</span>
    <span class="assess-hint">Leaking taps, broken fixtures, peeling paint, appliances that don't work properly.</span>
    <select id="a-maintenance" onchange="handleAssessInput('a-maintenance')">
        <option value="">Select...</option>
        <option value="many">Many &ndash; five or more things need fixing</option>
        <option value="several">Several &ndash; three or four issues</option>
        <option value="a-couple">A couple &ndash; one or two minor things</option>
        <option value="none">None &ndash; everything is in working order</option>
        <option value="proactive">Proactive &ndash; I fix things promptly and do preventive maintenance</option>
    </select> <span class="assess-percentile-hint" id="pct-maintenance"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-maintenance" onchange="handleSkip('a-maintenance')"><label for="skip-maintenance">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Affordability</h4>

<div class="assess-input-group" id="ig-cost-ratio">
    <span class="assess-label">What are your total housing costs as a percentage of your gross income?</span>
    <span class="assess-hint">Rent or mortgage, council tax, utilities, insurance, and regular maintenance. The standard threshold is 30%.</span>
    <select id="a-cost-ratio" onchange="handleAssessInput('a-cost-ratio')">
        <option value="">Select...</option>
        <option value="over-50">Over 50%</option>
        <option value="40-50">40&ndash;50%</option>
        <option value="30-40">30&ndash;40%</option>
        <option value="20-30">20&ndash;30%</option>
        <option value="under-20">Under 20%</option>
    </select> <span class="assess-percentile-hint" id="pct-cost-ratio"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-cost-ratio" onchange="handleSkip('a-cost-ratio')"><label for="skip-cost-ratio">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-buffer">
    <span class="assess-label">Could you cover an unexpected housing cost of &pound;1,000&ndash;&pound;3,000?</span>
    <span class="assess-hint">A broken boiler, roof repair, or sudden rent increase.</span>
    <select id="a-buffer" onchange="handleAssessInput('a-buffer')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I'd need to borrow or go without</option>
        <option value="with-difficulty">With difficulty &ndash; it would mean cutting other essentials</option>
        <option value="stretch">A stretch &ndash; manageable but uncomfortable</option>
        <option value="yes">Yes &ndash; I have savings I could use</option>
        <option value="easily">Easily &ndash; I have a dedicated emergency fund</option>
    </select> <span class="assess-percentile-hint" id="pct-buffer"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-buffer" onchange="handleSkip('a-buffer')"><label for="skip-buffer">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-equity">
    <span class="assess-label">Is your current housing situation building long-term financial value?</span>
    <span class="assess-hint">Homeowners: mortgage principal payments. Renters: flexibility and lower commitment.</span>
    <select id="a-equity" onchange="handleAssessInput('a-equity')">
        <option value="">Select...</option>
        <option value="losing-value">Losing value &ndash; my housing costs are higher than they need to be with no return</option>
        <option value="no-equity">No equity &ndash; renting with no plan for ownership</option>
        <option value="neutral">Neutral &ndash; renting suits my situation for now</option>
        <option value="building">Building &ndash; paying down a mortgage or making value-adding improvements</option>
        <option value="strong">Strong &ndash; significant equity growth or very efficient housing costs</option>
    </select> <span class="assess-percentile-hint" id="pct-equity"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-equity" onchange="handleSkip('a-equity')"><label for="skip-equity">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Location</h4>

<div class="assess-input-group" id="ig-commute">
    <span class="assess-label">What is your actual door-to-door commute time on a typical day?</span>
    <span class="assess-hint">Include walking to transport, waiting, and any transfers. If you work from home, consider travel to a workplace or clients.</span>
    <select id="a-commute" onchange="handleAssessInput('a-commute')">
        <option value="">Select...</option>
        <option value="over-60">Over 60 minutes each way</option>
        <option value="40-60">40&ndash;60 minutes each way</option>
        <option value="20-40">20&ndash;40 minutes each way</option>
        <option value="under-20">Under 20 minutes each way</option>
        <option value="wfh">I work from home or within walking distance</option>
    </select> <span class="assess-percentile-hint" id="pct-commute"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-commute" onchange="handleSkip('a-commute')"><label for="skip-commute">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-amenities">
    <span class="assess-label">How far are you from the amenities you use most?</span>
    <span class="assess-hint">Grocery shops, healthcare, green space, and social venues.</span>
    <select id="a-amenities" onchange="handleAssessInput('a-amenities')">
        <option value="">Select...</option>
        <option value="far">Far &ndash; most things require a significant drive</option>
        <option value="moderate">Moderate &ndash; some things are nearby, others require effort</option>
        <option value="reasonable">Reasonable &ndash; most things within 10&ndash;15 minutes</option>
        <option value="close">Close &ndash; most amenities within walking or short cycling distance</option>
        <option value="everything-nearby">Everything nearby &ndash; all key amenities within a few minutes</option>
    </select> <span class="assess-percentile-hint" id="pct-amenities"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-amenities" onchange="handleSkip('a-amenities')"><label for="skip-amenities">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-neighbourhood">
    <span class="assess-label">Does your neighbourhood feel safe, well-connected, and suited to your lifestyle?</span>
    <span class="assess-hint">Noise, safety, community character, whether the area supports the life you want.</span>
    <select id="a-neighbourhood" onchange="handleAssessInput('a-neighbourhood')">
        <option value="">Select...</option>
        <option value="poor-fit">Poor fit &ndash; it doesn't suit me at all</option>
        <option value="some-issues">Some issues &ndash; one or two significant problems</option>
        <option value="adequate">Adequate &ndash; it's fine but not ideal</option>
        <option value="good">Good &ndash; I like it and feel comfortable here</option>
        <option value="excellent">Excellent &ndash; it suits my lifestyle perfectly</option>
    </select> <span class="assess-percentile-hint" id="pct-neighbourhood"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-neighbourhood" onchange="handleSkip('a-neighbourhood')"><label for="skip-neighbourhood">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-comfort">
        <span class="assess-summary-label">Comfort</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-comfort" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-comfort">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-affordability">
        <span class="assess-summary-label">Affordability</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-affordability" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-affordability">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-location">
        <span class="assess-summary-label">Location</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-location" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-location">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on housing affordability, quality, and location satisfaction among adults. All items in this area are scored.</p>
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

<p>You now understand why housing matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about comfort, affordability, and location. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/housing/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Housing Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Housing. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/housing/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'housing';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-space', 'a-temperature', 'a-maintenance',
        'a-cost-ratio', 'a-buffer', 'a-equity',
        'a-commute', 'a-amenities', 'a-neighbourhood'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: ~50% of renters spend >30% on housing (Census),
    // ~24% of homeowners are cost-burdened, median commute ~27 minutes.
    var THRESHOLDS = {
        'a-space': [
            // Most people report at least adequate space; excellent is uncommon
            {v:'poorly',p:10},{v:'some-issues',p:30},{v:'adequate',p:50},{v:'well',p:75},{v:'excellent',p:93}
        ],
        'a-temperature': [
            // ~25% of homes have significant temperature issues; excellent insulation is rare
            {v:'poor',p:10},{v:'some-problems',p:30},{v:'mostly-ok',p:55},{v:'good',p:78},{v:'excellent',p:95}
        ],
        'a-maintenance': [
            // Most homes have 1-2 deferred issues; proactive maintenance is uncommon
            {v:'many',p:10},{v:'several',p:28},{v:'a-couple',p:55},{v:'none',p:78},{v:'proactive',p:95}
        ],
        'a-cost-ratio': [
            // ~50% of renters and ~24% of owners spend >30%; under 20% is uncommon
            {v:'over-50',p:8},{v:'40-50',p:20},{v:'30-40',p:42},{v:'20-30',p:70},{v:'under-20',p:92}
        ],
        'a-buffer': [
            // ~40% couldn't cover a $400 emergency (US Fed); dedicated fund is uncommon
            {v:'no',p:10},{v:'with-difficulty',p:28},{v:'stretch',p:48},{v:'yes',p:72},{v:'easily',p:92}
        ],
        'a-equity': [
            // ~36% of households own outright or have significant equity; strong growth is top quartile
            {v:'losing-value',p:8},{v:'no-equity',p:25},{v:'neutral',p:45},{v:'building',p:72},{v:'strong',p:92}
        ],
        'a-commute': [
            // Median commute ~27 min; WFH/walking distance is increasingly common but still minority
            {v:'over-60',p:8},{v:'40-60',p:25},{v:'20-40',p:50},{v:'under-20',p:75},{v:'wfh',p:92}
        ],
        'a-amenities': [
            // Varies hugely by urban/rural; everything walkable is urban privilege
            {v:'far',p:10},{v:'moderate',p:30},{v:'reasonable',p:55},{v:'close',p:78},{v:'everything-nearby',p:95}
        ],
        'a-neighbourhood': [
            // Most people rate their neighbourhood as adequate or better; excellent fit is uncommon
            {v:'poor-fit',p:8},{v:'some-issues',p:25},{v:'adequate',p:48},{v:'good',p:75},{v:'excellent',p:95}
        ]
    };

    var VALUE_ITEMS = {
        comfort: ['a-space', 'a-temperature', 'a-maintenance'],
        affordability: ['a-cost-ratio', 'a-buffer', 'a-equity'],
        location: ['a-commute', 'a-amenities', 'a-neighbourhood']
    };

    // All housing items are scorable
    var UNSCORED_ITEMS = [];

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

    function interpolatePercentile(value, thresholds) {
        if (typeof thresholds[0].v === 'string') {
            for (var i = 0; i < thresholds.length; i++) {
                if (thresholds[i].v === String(value)) return thresholds[i].p;
            }
            return null;
        }
        return null;
    }

    function getItemPercentile(itemId) {
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

    function updatePercentileHint(itemId) {
        if (UNSCORED_ITEMS.indexOf(itemId) !== -1) return;
        var hintEl = document.getElementById('pct-' + itemId.replace('a-', ''));
        if (!hintEl) return;
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) {
            hintEl.textContent = 'Skipped';
            return;
        }
        var pct = getItemPercentile(itemId);
        hintEl.textContent = pct !== null ? '~' + pct + 'th percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['comfort', 'affordability', 'location'].forEach(function(vk) {
            var pct = computeValuePercentile(vk);
            var barEl = document.getElementById('bar-' + vk);
            var valEl = document.getElementById('val-' + vk);
            if (barEl && valEl) {
                if (pct !== null) {
                    barEl.style.width = pct + '%';
                    valEl.textContent = pct + 'th';
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

    // --- Assessment helpers ---

    function isItemAnswered(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return true;
        var el = document.getElementById(itemId);
        return el && el.value !== '' && el.value !== null;
    }

    function updateInputGroupState(itemId) {
        var group = document.getElementById('ig-' + itemId.replace('a-', ''));
        if (group) group.classList.toggle('answered', isItemAnswered(itemId));
    }

    function updateAssessCompletion() {
        var allAnswered = ASSESS_IDS.every(function(id) { return isItemAnswered(id); });
        var btn = document.getElementById('assessBtn');
        if (btn) {
            btn.disabled = !allAnswered;
            btn.textContent = allAnswered ? 'All done \u2013 continue' : 'Answer all items to continue';
        }
    }

    function saveAnswers() {
        var answers = {};
        ASSESS_IDS.forEach(function(id) {
            var skipBox = document.getElementById('skip-' + id.replace('a-', ''));
            var skipped = skipBox && skipBox.checked;
            var value = null;
            if (!skipped) { var el = document.getElementById(id); if (el && el.value !== '') value = el.value; }
            answers[id] = { value: value, skipped: skipped };
        });
        var allAnswers = {};
        try { allAnswers = JSON.parse(localStorage.getItem('ap-level1-answers')) || {}; } catch(e) {}
        allAnswers[AREA] = answers;
        localStorage.setItem('ap-level1-answers', JSON.stringify(allAnswers));
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
        ['comfort', 'affordability', 'location'].forEach(function(vk) {
            scores[vk] = computeValuePercentile(vk);
        });
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-scores') || {};
            all[AREA] = scores;
            APStorage.save('ap-level1-scores', all);
        }
    }

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
        }
        updatePercentileHint(itemId);
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessSummary();
        updateAssessCompletion();
    };

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
