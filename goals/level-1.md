---
layout: default
title: "Goals – Level 1: Awareness"
life_area_slug: goals
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

<h1>Goals: Level 1</h1>

<p class="l1-subtitle">Understand what goal-setting means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Goals Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why goals matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Goal-setting is one of the most validated interventions in behavioural science. <a href="https://psycnet.apa.org/record/2002-15790-003" target="_blank">Locke and Latham's research</a> across over 1,000 studies shows that specific, challenging goals improve outcomes by 10 – 25% compared to vague intentions or "do your best" instructions.</p>

<p>Yet the gap between knowing goals work and actually achieving them is enormous. <a href="https://news.scranton.edu/articles/2021/01/fac-norcross-stories.shtml" target="_blank">92% of goal-setters</a> never reach their goals, and 80% of New Year's resolutions are abandoned by February.</p>

<p>The difference is almost entirely about practice, not willpower. <a href="https://scholar.dominican.edu/psychology-faculty-conference-presentations/3/" target="_blank">Writing goals down</a> increases achievement by 42%. <a href="https://psycnet.apa.org/record/2015-52587-001" target="_blank">Monitoring progress weekly</a> significantly promotes attainment across a wide range of domains. Simple, well-evidenced practices dramatically shift the odds &ndash; but only about a third of goal-setters use any of them.</p>

<p>Goal-setting also shapes your sense of direction and meaning. People with clear goals report higher life satisfaction, greater sense of purpose, and more resilience when facing setbacks.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about goals</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach goal-setting for different reasons. This site scores every goals intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Follow-through</h3>
<p>Consistently completing what you set out to do &ndash; turning goals from intentions into accomplished outcomes. Maintaining momentum, tracking progress, building accountability, and developing the discipline to keep working when motivation fades. People who lean towards this value measure success by completion rate.</p>

<h3>Clarity</h3>
<p>Defining goals with enough precision that you know exactly what success looks like and can tell whether you are on track. Specific, measurable targets, clear deadlines, and unambiguous criteria for completion. People who lean towards this value believe that vague goals produce vague results.</p>

<h3>Adaptability</h3>
<p>Maintaining the ability to change course, adjust timelines, reprioritise, or abandon goals as new information emerges. Treating goals as hypotheses, running regular reviews, and developing the skill of strategic retreat without emotional cost. People who lean towards this value believe that adapting intelligently is more important than persisting stubbornly.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each goals value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Follow-through &ndash; Level 5</div>
    <p><a href="https://www.chrisclear.com/" target="_blank">Chris Nikic</a> became the first person with Down syndrome to complete an Ironman triathlon in 2020, at age 21. He trained for over a year using a system he calls "1% better every day" &ndash; small, trackable daily improvements toward an audacious goal. He has since completed multiple Ironmans and a marathon, each time following the same methodical, incremental approach to follow-through across multi-month timescales.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Clarity &ndash; Level 5</div>
    <p><a href="https://www.samuelthomasdavies.com/" target="_blank">Samuel Thomas Davies</a> is a behavioural scientist and author who publicly documents his goal-setting methodology, including specific measurable targets, weekly progress reviews, and annual retrospectives published in detail. His system treats goal clarity as a discipline &ndash; every goal has explicit success criteria, a deadline, and a tracking mechanism. He has maintained this practice consistently for over a decade.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Adaptability &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Sara_Blakely" target="_blank">Sara Blakely</a> spent two years developing Spanx while working full-time as a door-to-door fax machine salesperson. When her initial patent strategy failed, she rewrote the patent herself. When major retailers rejected her, she demonstrated the product in person at Neiman Marcus. She has spoken about treating each setback as information rather than failure, adjusting her approach without abandoning the goal. Spanx reached $400 million in revenue with no outside funding.</p>
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
<h4>Follow-through</h4>

<div class="assess-input-group" id="ig-current-goals">
    <span class="assess-label">How many goals are you currently working towards?</span>
    <span class="assess-hint">Specific things you are actively pursuing right now &ndash; not aspirations or wishes.</span>
    <select id="a-current-goals" onchange="handleAssessInput('a-current-goals')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I don't have any defined goals right now</option>
        <option value="vague">Vague &ndash; I have a general sense of direction but nothing specific</option>
        <option value="one-two">One or two &ndash; a couple of goals I'm focused on</option>
        <option value="several">Several &ndash; 3 &ndash; 5 goals across different areas</option>
        <option value="many">Many &ndash; 6+ goals I'm actively pursuing</option>
    </select> <span class="assess-percentile-hint" id="pct-current-goals"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-current-goals" onchange="handleSkip('a-current-goals')"><label for="skip-current-goals">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-completion-rate">
    <span class="assess-label">Of the goals you set in the past year, how many did you actually complete?</span>
    <span class="assess-hint">Even a rough estimate is useful &ndash; 'most,' 'about half,' or 'almost none' all count.</span>
    <select id="a-completion-rate" onchange="handleAssessInput('a-completion-rate')">
        <option value="">Select...</option>
        <option value="almost-none">Almost none &ndash; I rarely finish what I start</option>
        <option value="few">A few &ndash; maybe one or two out of several</option>
        <option value="about-half">About half &ndash; a mixed record</option>
        <option value="most">Most &ndash; I complete the majority of goals I set</option>
        <option value="nearly-all">Nearly all &ndash; I consistently follow through</option>
    </select> <span class="assess-percentile-hint" id="pct-completion-rate"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-completion-rate" onchange="handleSkip('a-completion-rate')"><label for="skip-completion-rate">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-tracking">
    <span class="assess-label">Do you track progress on your goals in any systematic way?</span>
    <span class="assess-hint">A spreadsheet, journal, app, or regular review &ndash; or nothing at all.</span>
    <select id="a-tracking" onchange="handleAssessInput('a-tracking')">
        <option value="">Select...</option>
        <option value="no-tracking">No &ndash; I don't track progress at all</option>
        <option value="mental">Mental only &ndash; I keep a rough sense in my head</option>
        <option value="occasional">Occasional &ndash; I check in now and then but not regularly</option>
        <option value="regular">Regular &ndash; I review progress weekly or monthly</option>
        <option value="systematic">Systematic &ndash; detailed tracking with regular reviews</option>
    </select> <span class="assess-percentile-hint" id="pct-tracking"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-tracking" onchange="handleSkip('a-tracking')"><label for="skip-tracking">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Clarity</h4>

<div class="assess-input-group" id="ig-written">
    <span class="assess-label">Are your goals written down anywhere?</span>
    <span class="assess-hint">Written goals are 42% more likely to be achieved than unwritten ones.</span>
    <select id="a-written" onchange="handleAssessInput('a-written')">
        <option value="">Select...</option>
        <option value="no">No &ndash; they exist only in my head</option>
        <option value="some">Some &ndash; a few are written but most aren't</option>
        <option value="scattered">Scattered &ndash; written in various places with no system</option>
        <option value="mostly">Mostly &ndash; most are written in a central place</option>
        <option value="all">All &ndash; every goal is written down and accessible</option>
    </select> <span class="assess-percentile-hint" id="pct-written"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-written" onchange="handleSkip('a-written')"><label for="skip-written">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-measurable">
    <span class="assess-label">For each of your current goals, do you know exactly what 'done' looks like?</span>
    <span class="assess-hint">Could someone else look at the goal and tell you whether you've achieved it?</span>
    <select id="a-measurable" onchange="handleAssessInput('a-measurable')">
        <option value="">Select...</option>
        <option value="no">No &ndash; my goals are vague intentions</option>
        <option value="few">For a few &ndash; one or two have clear endpoints</option>
        <option value="some">For some &ndash; roughly half have clear success criteria</option>
        <option value="most">For most &ndash; the majority have measurable outcomes</option>
        <option value="all">For all &ndash; every goal has a specific, measurable definition of done</option>
    </select> <span class="assess-percentile-hint" id="pct-measurable"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-measurable" onchange="handleSkip('a-measurable')"><label for="skip-measurable">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-deadlines">
    <span class="assess-label">Do your goals have deadlines attached?</span>
    <span class="assess-hint">A specific date, not 'someday' or 'when I get round to it.'</span>
    <select id="a-deadlines" onchange="handleAssessInput('a-deadlines')">
        <option value="">Select...</option>
        <option value="none">None &ndash; no deadlines on any goals</option>
        <option value="few">A few &ndash; one or two have dates</option>
        <option value="some">Some &ndash; roughly half have deadlines</option>
        <option value="most">Most &ndash; the majority have target dates</option>
        <option value="all">All &ndash; every goal has a specific deadline</option>
    </select> <span class="assess-percentile-hint" id="pct-deadlines"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-deadlines" onchange="handleSkip('a-deadlines')"><label for="skip-deadlines">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Adaptability</h4>

<div class="assess-input-group" id="ig-abandoned">
    <span class="assess-label">When you've stopped pursuing a goal in the past, was it a deliberate decision or did you just drift away?</span>
    <span class="assess-hint">There is an important difference between strategic retreat and quiet abandonment.</span>
    <select id="a-abandoned" onchange="handleAssessInput('a-abandoned')">
        <option value="">Select...</option>
        <option value="always-drift">Always drift &ndash; goals just fade without a conscious decision</option>
        <option value="mostly-drift">Mostly drift &ndash; occasionally deliberate but usually not</option>
        <option value="mixed">Mixed &ndash; about half deliberate, half drift</option>
        <option value="mostly-deliberate">Mostly deliberate &ndash; I usually make a conscious choice to stop</option>
        <option value="always-deliberate">Always deliberate &ndash; I formally retire goals I no longer pursue</option>
    </select> <span class="assess-percentile-hint" id="pct-abandoned"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-abandoned" onchange="handleSkip('a-abandoned')"><label for="skip-abandoned">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-review">
    <span class="assess-label">Do you have any regular process for reviewing and adjusting your goals?</span>
    <span class="assess-hint">Weekly, monthly, quarterly &ndash; or never.</span>
    <select id="a-review" onchange="handleAssessInput('a-review')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I set goals and don't revisit them</option>
        <option value="rarely">Rarely &ndash; only when something forces me to</option>
        <option value="quarterly">Quarterly &ndash; a few times a year</option>
        <option value="monthly">Monthly &ndash; regular monthly review</option>
        <option value="weekly">Weekly &ndash; goals are reviewed every week</option>
    </select> <span class="assess-percentile-hint" id="pct-review"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-review" onchange="handleSkip('a-review')"><label for="skip-review">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-sunk-cost">
    <span class="assess-label">Do you tend to persist with goals that are no longer worth pursuing because of time already invested?</span>
    <span class="assess-hint">Sunk-cost bias is one of the most common obstacles to intelligent goal management.</span>
    <select id="a-sunk-cost" onchange="handleAssessInput('a-sunk-cost')">
        <option value="">Select...</option>
        <option value="strongly">Strongly &ndash; I find it very hard to abandon goals I've invested in</option>
        <option value="somewhat">Somewhat &ndash; I notice this tendency in myself</option>
        <option value="occasionally">Occasionally &ndash; it happens but I can usually recognise it</option>
        <option value="rarely">Rarely &ndash; I'm generally good at cutting losses</option>
        <option value="never">Never &ndash; I evaluate goals purely on future value</option>
    </select> <span class="assess-percentile-hint" id="pct-sunk-cost"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-sunk-cost" onchange="handleSkip('a-sunk-cost')"><label for="skip-sunk-cost">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-follow_through">
        <span class="assess-summary-label">Follow-through</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-follow_through" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-follow_through">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-clarity">
        <span class="assess-summary-label">Clarity</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-clarity" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-clarity">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-adaptability">
        <span class="assess-summary-label">Adaptability</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-adaptability" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-adaptability">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on goal-setting behaviour among adults. All items in this area are scored.</p>
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

<p>You now understand why goals matter, what different people get out of goal-setting, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about follow-through, clarity, and adaptability. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/goals/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Goals Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Goals. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/goals/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'goals';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-current-goals', 'a-completion-rate', 'a-tracking',
        'a-written', 'a-measurable', 'a-deadlines',
        'a-abandoned', 'a-review', 'a-sunk-cost'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: ~92% of goal-setters fail, ~33% write goals down,
    // ~15% track progress regularly, ~8% do weekly reviews.
    var THRESHOLDS = {
        'a-current-goals': [
            // ~50% of adults have no defined goals; having several specific goals is uncommon
            {v:'none',p:15},{v:'vague',p:35},{v:'one-two',p:55},{v:'several',p:75},{v:'many',p:90}
        ],
        'a-completion-rate': [
            // 92% never reach their goals; completing most is rare
            {v:'almost-none',p:10},{v:'few',p:30},{v:'about-half',p:55},{v:'most',p:80},{v:'nearly-all',p:95}
        ],
        'a-tracking': [
            // ~15% of people track progress systematically; ~70% do nothing
            {v:'no-tracking',p:15},{v:'mental',p:35},{v:'occasional',p:55},{v:'regular',p:78},{v:'systematic',p:95}
        ],
        'a-written': [
            // ~33% write goals down; writing all goals in a system is very rare
            {v:'no',p:20},{v:'some',p:40},{v:'scattered',p:55},{v:'mostly',p:75},{v:'all',p:92}
        ],
        'a-measurable': [
            // Most people set vague goals; having specific success criteria for all is rare
            {v:'no',p:15},{v:'few',p:35},{v:'some',p:55},{v:'most',p:78},{v:'all',p:95}
        ],
        'a-deadlines': [
            // Few people attach deadlines to all goals; most have none or vague timelines
            {v:'none',p:15},{v:'few',p:35},{v:'some',p:55},{v:'most',p:78},{v:'all',p:93}
        ],
        'a-abandoned': [
            // Most people drift away from goals unconsciously; deliberate retirement is rare
            {v:'always-drift',p:10},{v:'mostly-drift',p:30},{v:'mixed',p:55},{v:'mostly-deliberate',p:78},{v:'always-deliberate',p:95}
        ],
        'a-review': [
            // ~8% review goals weekly; most never formally revisit
            {v:'never',p:15},{v:'rarely',p:35},{v:'quarterly',p:60},{v:'monthly',p:80},{v:'weekly',p:95}
        ],
        'a-sunk-cost': [
            // Sunk-cost bias affects most people; evaluating purely on future value is very uncommon
            {v:'strongly',p:10},{v:'somewhat',p:30},{v:'occasionally',p:55},{v:'rarely',p:78},{v:'never',p:95}
        ]
    };

    var VALUE_ITEMS = {
        follow_through: ['a-current-goals', 'a-completion-rate', 'a-tracking'],
        clarity: ['a-written', 'a-measurable', 'a-deadlines'],
        adaptability: ['a-abandoned', 'a-review', 'a-sunk-cost']
    };

    // All goals items are scorable
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
        // All goals items use string keys (dropdowns)
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
        hintEl.textContent = pct !== null ? '~' + ordinalSuffix(pct) + ' percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['follow_through', 'clarity', 'adaptability'].forEach(function(vk) {
            var pct = computeValuePercentile(vk);
            var barEl = document.getElementById('bar-' + vk);
            var valEl = document.getElementById('val-' + vk);
            if (barEl && valEl) {
                if (pct !== null) {
                    barEl.style.width = pct + '%';
                    valEl.textContent = ordinalSuffix(pct);
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
            if (!skipped) {
                var el = document.getElementById(id);
                if (el && el.value !== '') value = el.value;
            }
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
        ['follow_through', 'clarity', 'adaptability'].forEach(function(vk) {
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
