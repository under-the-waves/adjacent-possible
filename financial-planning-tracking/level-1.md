---
layout: default
title: "Financial Planning and Tracking – Level 1: Awareness"
life_area_slug: financial-planning-tracking
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

<h1>Financial Planning and Tracking: Level 1</h1>

<p class="l1-subtitle">Understand what financial planning means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Financial Planning Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why financial planning and tracking matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Financial planning and tracking form the foundation for virtually every other financial decision you make. The evidence for their impact is broad and consistent.</p>

<p>People with a written financial plan report <a href="https://fpsb.org/about-financial-planning/the-value-of-financial-planning/" target="_blank">38% improved financial wellbeing</a>, 37% greater financial confidence, and 36% better understanding of financial matters. Over half say financial planning has positively affected their mental health and family life.</p>

<p>Yet most people operate without systematic tracking. <a href="https://www.thepennyhoarder.com/budgeting/budgeting-statistics/" target="_blank">55% of Americans</a> do not use any form of budget, and most who claim to budget are simply reviewing bank statements after the fact. Only <a href="https://www.schwab.com/learn/story/modern-wealth-survey" target="_blank">36% have a written financial plan</a>, despite widespread recognition that planning works.</p>

<p>The psychological benefits extend well beyond money management. Having a clear picture of your finances reduces the mental burden of constant uncertainty &ndash; 74% of Americans report stress over personal finances, but those with financial plans report significantly lower anxiety. Tracking also improves cognitive performance by providing clear information for decisions, reducing the errors that come from guessing or estimating.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about financial planning</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach financial planning for different reasons. This site scores every financial planning intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Accuracy & Control</h3>
<p>Having precise, reliable financial information and clear oversight of money flows. People who lean towards this value want comprehensive data and tight control over their financial picture, enabling informed decisions based on complete information. They track every category, reconcile accounts, and know exactly where money goes.</p>

<h3>Simplicity & Convenience</h3>
<p>Making financial management effortless and low-friction. People who lean towards this value want good financial outcomes without having to think about money regularly. They prefer automated systems, minimal time investment, and approaches that work in the background with occasional check-ins.</p>

<h3>Insight & Optimisation</h3>
<p>Using financial data to make better decisions and identify opportunities. People who lean towards this value enjoy the analytical side &ndash; trend analysis, finding inefficiencies, and turning tracking data into actionable improvements that compound over time.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each financial planning value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Accuracy & Control &ndash; Level 5</div>
    <p><a href="https://www.youneedabudget.com/the-four-rules/" target="_blank">Jesse Mecham</a> founded YNAB (You Need A Budget) in 2004 after developing a meticulous envelope-based budgeting system as a newly married university student. He built it into a company used by millions of people worldwide, all grounded in the principle that every pound should be assigned a specific purpose before it is spent. His personal financial tracking system accounts for every transaction across all accounts in real time, and his methodology has demonstrably changed the financial behaviour of hundreds of thousands of users.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Simplicity & Convenience &ndash; Level 5</div>
    <p><a href="https://jlcollinsnh.com/about/" target="_blank">JL Collins</a> spent decades refining his personal finances into the simplest possible system &ndash; a single index fund, automated contributions, and minimal ongoing management. His approach, documented in <em>The Simple Path to Wealth</em>, deliberately rejects complexity in favour of systems that require almost no maintenance while delivering strong long-term outcomes. He manages his own portfolio in under an hour per year.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Insight & Optimisation &ndash; Level 5</div>
    <p><a href="https://www.madfientist.com/about/" target="_blank">Brandon Ganch</a> (the Mad Fientist) built detailed analytical models of his own finances, systematically optimising tax strategies, account structures, and spending patterns. His spreadsheets and calculators, published freely online, helped him retire at 34 by identifying and eliminating financial inefficiencies that most people never notice. He treats personal finance as an engineering problem, quantifying the impact of every decision.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to look up.</p>

<div class="assess-group">
<h4>Accuracy &amp; Control</h4>

<div class="assess-input-group" id="ig-net-worth-freq">
    <span class="assess-label">How often do you check or update your net worth?</span>
    <span class="assess-hint">Include savings, investments, property, pensions, and any outstanding loans, credit cards, or mortgages.</span>
    <select id="a-net-worth-freq" onchange="handleAssessInput('a-net-worth-freq')">
        <option value="">Select...</option>
        <option value="0">Never &ndash; I don't track my net worth</option>
        <option value="1">Rarely &ndash; once or twice a year at most</option>
        <option value="2">Quarterly &ndash; every few months</option>
        <option value="3">Monthly &ndash; I update it each month</option>
        <option value="4">Weekly or more &ndash; I check it regularly</option>
    </select> <span class="assess-percentile-hint" id="pct-net-worth-freq"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-net-worth-freq" onchange="handleSkip('a-net-worth-freq')"><label for="skip-net-worth-freq">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-budget-accuracy">
    <span class="assess-label">How close is your budget or spending plan to what you actually spend?</span>
    <span class="assess-hint">If you don't use a budget, select the first option.</span>
    <select id="a-budget-accuracy" onchange="handleAssessInput('a-budget-accuracy')">
        <option value="">Select...</option>
        <option value="0">I don't have a budget or spending plan</option>
        <option value="1">I have one but rarely check it against actual spending</option>
        <option value="2">Roughly in the right area &ndash; within 20% of actual spending</option>
        <option value="3">Fairly close &ndash; within 10% of actual spending</option>
        <option value="4">Very accurate &ndash; within 5% of actual spending</option>
    </select> <span class="assess-percentile-hint" id="pct-budget-accuracy"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-budget-accuracy" onchange="handleSkip('a-budget-accuracy')"><label for="skip-budget-accuracy">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-expense-tracking">
    <span class="assess-label">How do you track your expenses?</span>
    <span class="assess-hint">Choose the option that best describes your current approach.</span>
    <select id="a-expense-tracking" onchange="handleAssessInput('a-expense-tracking')">
        <option value="">Select...</option>
        <option value="0">I don't track expenses at all</option>
        <option value="1">I occasionally review bank statements after the fact</option>
        <option value="2">I use a simple system &ndash; spreadsheet, notebook, or basic app</option>
        <option value="3">I use a dedicated budgeting app or detailed spreadsheet with categories</option>
        <option value="4">I track every transaction in real time across all accounts</option>
    </select> <span class="assess-percentile-hint" id="pct-expense-tracking"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-expense-tracking" onchange="handleSkip('a-expense-tracking')"><label for="skip-expense-tracking">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Simplicity &amp; Convenience</h4>

<div class="assess-input-group" id="ig-automation-level">
    <span class="assess-label">What proportion of your regular payments and savings are automated?</span>
    <span class="assess-hint">Include standing orders, direct debits, automatic transfers to savings, and pension contributions.</span>
    <select id="a-automation-level" onchange="handleAssessInput('a-automation-level')">
        <option value="">Select...</option>
        <option value="0">None or very few &ndash; I handle most things manually</option>
        <option value="1">Some &ndash; a few direct debits but most transfers are manual</option>
        <option value="2">About half &ndash; bills are automated but savings and investments are manual</option>
        <option value="3">Most &ndash; bills, savings, and investments are all automated</option>
        <option value="4">Nearly everything &ndash; my finances run on autopilot with rare manual intervention</option>
    </select> <span class="assess-percentile-hint" id="pct-automation-level"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-automation-level" onchange="handleSkip('a-automation-level')"><label for="skip-automation-level">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-time-on-finances">
    <span class="assess-label">How much time do you spend managing your finances each month?</span>
    <span class="assess-hint">Include bill-paying, budgeting, checking accounts, and any financial admin.</span>
    <select id="a-time-on-finances" onchange="handleAssessInput('a-time-on-finances')">
        <option value="">Select...</option>
        <option value="0">No time &ndash; I don't actively manage my finances</option>
        <option value="1">Under 30 minutes</option>
        <option value="2">30 minutes to 1 hour</option>
        <option value="3">1 to 3 hours</option>
        <option value="4">More than 3 hours</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-time-on-finances" onchange="handleSkip('a-time-on-finances')"><label for="skip-time-on-finances">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-tracking-system">
    <span class="assess-label">What system do you currently use to manage your finances?</span>
    <span class="assess-hint">This could be a spreadsheet, an app, a notebook, or nothing at all.</span>
    <select id="a-tracking-system" onchange="handleAssessInput('a-tracking-system')">
        <option value="">Select...</option>
        <option value="none">Nothing &ndash; I don't use any system</option>
        <option value="mental">Mental tracking &ndash; I keep a rough picture in my head</option>
        <option value="paper">Paper &ndash; notebook or printed statements</option>
        <option value="spreadsheet">Spreadsheet &ndash; Excel, Google Sheets, or similar</option>
        <option value="basic-app">Basic app &ndash; bank app or simple budgeting tool</option>
        <option value="dedicated-app">Dedicated app &ndash; YNAB, Monarch, or similar</option>
        <option value="custom">Custom system &ndash; personal dashboard or integrated toolset</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-tracking-system" onchange="handleSkip('a-tracking-system')"><label for="skip-tracking-system">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Insight &amp; Optimisation</h4>

<div class="assess-input-group" id="ig-financial-goals">
    <span class="assess-label">How specific are your financial goals?</span>
    <span class="assess-hint">Examples of specific goals: "Save &pound;10,000 by December 2027" or "Pay off credit card by March 2026."</span>
    <select id="a-financial-goals" onchange="handleAssessInput('a-financial-goals')">
        <option value="">Select...</option>
        <option value="0">I don't have any financial goals</option>
        <option value="1">I have vague goals &ndash; "save more" or "pay off debt"</option>
        <option value="2">I have one or two specific goals with target amounts</option>
        <option value="3">I have specific goals with amounts and target dates</option>
        <option value="4">I have documented goals with amounts, dates, and a written plan to reach them</option>
    </select> <span class="assess-percentile-hint" id="pct-financial-goals"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-financial-goals" onchange="handleSkip('a-financial-goals')"><label for="skip-financial-goals">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-spending-trends">
    <span class="assess-label">Do you know whether your total spending has been going up, down, or staying flat over the past 6 months?</span>
    <span class="assess-hint">Even a rough sense counts &ndash; you don't need exact figures.</span>
    <select id="a-spending-trends" onchange="handleAssessInput('a-spending-trends')">
        <option value="">Select...</option>
        <option value="no-idea">No idea</option>
        <option value="rough">Rough sense &ndash; I know the general direction</option>
        <option value="clear">Clear picture &ndash; I could estimate the change</option>
        <option value="precise">Precise &ndash; I track this and know the numbers</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-spending-trends" onchange="handleSkip('a-spending-trends')"><label for="skip-spending-trends">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-written-plan">
    <span class="assess-label">Do you have a written financial plan?</span>
    <span class="assess-hint">A written plan covers income, expenses, savings targets, and investment strategy in a single document or system.</span>
    <select id="a-written-plan" onchange="handleAssessInput('a-written-plan')">
        <option value="">Select...</option>
        <option value="0">No written plan</option>
        <option value="1">Partial plan &ndash; some notes but nothing comprehensive</option>
        <option value="2">Basic written plan covering budget and savings goals</option>
        <option value="3">Comprehensive plan covering budget, savings, investments, and timeline</option>
        <option value="4">Detailed plan with regular reviews, scenario analysis, and professional input</option>
    </select> <span class="assess-percentile-hint" id="pct-written-plan"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-written-plan" onchange="handleSkip('a-written-plan')"><label for="skip-written-plan">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-accuracy">
        <span class="assess-summary-label">Accuracy &amp; Control</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-accuracy" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-accuracy">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-insight">
        <span class="assess-summary-label">Insight &amp; Optimisation</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-insight" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-insight">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published survey data for American adults. Simplicity &amp; Convenience items are recorded for your awareness but not scored, as time spent on finances is context-dependent and the available data does not support reliable percentile estimates.</p>
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

<p>You now understand why financial planning matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about accuracy and control, simplicity and convenience, and insight and optimisation. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/financial-planning-tracking/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Financial Planning Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Financial Planning and Tracking. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/financial-planning-tracking/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'financial-planning-tracking';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-net-worth-freq', 'a-budget-accuracy', 'a-expense-tracking',
        'a-automation-level', 'a-time-on-finances', 'a-tracking-system',
        'a-financial-goals', 'a-spending-trends', 'a-written-plan'
    ];

    // Scoring thresholds: [{v, p}, ...] sorted by value ascending
    // Based on published survey data for American adults
    var THRESHOLDS = {
        'a-net-worth-freq': [
            // ~60% of Americans don't track net worth at all; quarterly+ is well above median
            {v:'0',p:20},{v:'1',p:40},{v:'2',p:65},{v:'3',p:82},{v:'4',p:95}
        ],
        'a-budget-accuracy': [
            // 55% don't budget; of those who do, most are rough estimates
            {v:'0',p:15},{v:'1',p:35},{v:'2',p:55},{v:'3',p:75},{v:'4',p:92}
        ],
        'a-expense-tracking': [
            // Only 45% use any systematic approach; real-time tracking is rare
            {v:'0',p:15},{v:'1',p:35},{v:'2',p:55},{v:'3',p:78},{v:'4',p:95}
        ],
        'a-automation-level': [
            // Most people automate some bills; full automation is uncommon
            {v:'0',p:15},{v:'1',p:35},{v:'2',p:55},{v:'3',p:78},{v:'4',p:93}
        ],
        'a-financial-goals': [
            // Fewer than 20% achieve their financial goals; documented plans are rare
            {v:'0',p:15},{v:'1',p:35},{v:'2',p:55},{v:'3',p:75},{v:'4',p:92}
        ],
        'a-written-plan': [
            // Only 36% of Americans have a written financial plan
            {v:'0',p:20},{v:'1',p:40},{v:'2',p:64},{v:'3',p:82},{v:'4',p:95}
        ]
    };

    var VALUE_ITEMS = {
        accuracy: ['a-net-worth-freq', 'a-budget-accuracy', 'a-expense-tracking'],
        insight: ['a-financial-goals', 'a-written-plan']
    };

    // Simplicity items + spending-trends are recorded but not scored
    var UNSCORED_ITEMS = ['a-time-on-finances', 'a-tracking-system', 'a-spending-trends'];

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
        // All financial planning items use string keys (dropdowns)
        for (var i = 0; i < thresholds.length; i++) {
            if (thresholds[i].v === String(value)) return thresholds[i].p;
        }
        return null;
    }

    function getItemPercentile(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return null;

        if (!THRESHOLDS[itemId]) return null;

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

    function updateInputGroupState(itemId) {
        var group = document.getElementById('ig-' + itemId.replace('a-', ''));
        if (group) group.classList.toggle('answered', isItemAnswered(itemId));
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['accuracy', 'insight'].forEach(function(vk) {
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
        ['accuracy', 'insight'].forEach(function(vk) {
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
        }
        updatePercentileHint(itemId);
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessSummary();
        updateAssessCompletion();
    };

    // Override completeStep to also save scores
    var _origCompleteStep = window.completeStep;
    window.completeStep = function(step) {
        if (step === 'assess') saveScores();
        _origCompleteStep(step);
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
