---
layout: default
title: "Investing – Level 1: Awareness"
life_area_slug: investing
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

<h1>Investing: Level 1</h1>

<p class="l1-subtitle">Understand what investing means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Investing Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why investing matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Investing is one of the few financial decisions where time does most of the work for you. A portfolio growing at 7% annually (the long-run average for global equities after inflation) doubles roughly every ten years. Someone who invests $500 a month starting at 25 would have over $1 million by 55 &ndash; and more than half of that total comes from returns on returns, not from the money they put in.</p>

<p>Most people who invest still underperform. <a href="https://www.dalbar.com/QAIB/Index" target="_blank">DALBAR's annual studies</a> consistently show that the average equity fund investor trails the S&amp;P 500 by 3 &ndash; 5% annually over 20-year periods. The gap comes from behavioural mistakes &ndash; buying after gains and selling after losses &ndash; rather than poor fund selection. Basic discipline and a long time horizon put you ahead of the majority.</p>

<p>Professional management seldom helps. The <a href="https://www.spglobal.com/spdji/en/research-insights/spiva/" target="_blank">SPIVA scorecard</a> shows that 94% of actively managed domestic equity funds underperform their benchmark over 20 years. Low-cost index funds, which require almost no expertise to use, tend to beat most professionals over long periods. This makes investing unusual among skills: a simple, passive approach is genuinely difficult to improve upon.</p>

<p>Financial literacy remains surprisingly rare. Research by <a href="https://www.nber.org/papers/w17107" target="_blank">Lusardi and Mitchell</a> found that only 43% of adults worldwide can correctly answer three basic questions about compound interest, inflation, and diversification. Even foundational knowledge &ndash; understanding what you own and why &ndash; represents a meaningful advantage.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about investing</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People invest for different reasons. This site scores every investing intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Growth</h3>
<p>Maximising the long-term increase in your invested wealth. People who lean towards this value focus on compounding, appropriate asset allocation, and consistent contributions over decades. They tend to accept short-term volatility in exchange for higher expected returns, and they measure success by the total value of their portfolio over time.</p>

<h3>Safety</h3>
<p>Protecting your capital from catastrophic loss. People who lean towards this value prioritise diversification, position sizing, and resilient portfolio construction. They want to avoid scenarios where a single bad bet, market crash, or economic shift could wipe out years of progress. They measure success by how well their portfolio holds up in the worst periods.</p>

<h3>Simplicity</h3>
<p>Keeping your investment approach straightforward and low-maintenance. People who lean towards this value want a system they can set up once and sustain for decades without active management, frequent trading, or specialist knowledge. They measure success by how little time and attention their investments require while still delivering reasonable returns.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each investing value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Growth &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Warren_Buffett" target="_blank">Warren Buffett</a> compounded Berkshire Hathaway's book value at roughly 20% annually for over 58 years, turning an initial investment in a struggling textile company into one of the world's largest conglomerates. His approach relies on buying businesses with durable competitive advantages and holding them indefinitely. That rate of compounding, sustained over that duration, appears to be without precedent in public markets.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Safety &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Ray_Dalio" target="_blank">Ray Dalio</a> built Bridgewater Associates into the world's largest hedge fund, managing over $150 billion at its peak. His All Weather portfolio strategy, designed in the 1990s, allocates across asset classes to perform acceptably in any economic regime &ndash; growth, recession, rising inflation, or falling inflation. The approach has likely influenced a generation of institutional and retail portfolio construction, and variations of it are now widely used by individual investors.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Simplicity &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/John_C._Bogle" target="_blank">John C. Bogle</a> founded Vanguard in 1975 and launched the first retail index fund the following year. He spent decades arguing that most investors would do better with a low-cost, broadly diversified index fund than with any actively managed alternative &ndash; a claim that subsequent data has strongly supported. By the time of his death in 2019, index funds held trillions of dollars and had become the default recommendation for most individual investors.</p>
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
<h4>Growth</h4>

<div class="assess-input-group" id="ig-annual-return">
    <span class="assess-label">What was your approximate annual investment return last year (%)?</span>
    <span class="assess-hint">Check your brokerage, ISA, or pension provider dashboard for a total return figure. A rough number is fine.</span>
    <input type="number" id="a-annual-return" min="-50" max="100" step="0.5" placeholder="e.g. 7" onchange="handleAssessInput('a-annual-return')"> % <span class="assess-percentile-hint" id="pct-annual-return"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-annual-return" onchange="handleSkip('a-annual-return')"><label for="skip-annual-return">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-behaviour-gap">
    <span class="assess-label">How does your actual return compare to the funds you hold?</span>
    <span class="assess-hint">The behaviour gap is the difference between a fund's return and what investors in it actually earn, caused by buying high and selling low. If you're not sure, that's normal &ndash; most people have never checked.</span>
    <select id="a-behaviour-gap" onchange="handleAssessInput('a-behaviour-gap')">
        <option value="">Select...</option>
        <option value="0">I have no idea</option>
        <option value="1">I think I've underperformed my funds significantly (5%+ gap)</option>
        <option value="2">I've probably underperformed by a moderate amount (3 &ndash; 5% gap)</option>
        <option value="3">Roughly in line with my funds (1 &ndash; 3% gap)</option>
        <option value="4">Very close to or matching my funds' returns (&lt;1% gap)</option>
    </select> <span class="assess-percentile-hint" id="pct-behaviour-gap"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-behaviour-gap" onchange="handleSkip('a-behaviour-gap')"><label for="skip-behaviour-gap">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-financial-literacy">
    <span class="assess-label">How many of the three standard financial literacy questions can you answer correctly?</span>
    <span class="assess-hint">The <a href="https://www.nber.org/papers/w17107" target="_blank">Lusardi &amp; Mitchell</a> questions cover compound interest, inflation, and diversification. If you haven't taken the test, try answering: (1) If you had &pound;100 in savings at 2% interest, how much after 5 years? (2) If inflation is 1% and savings earn 2%, can you buy more/less/same after a year? (3) Is a single company stock usually safer than a fund?</span>
    <select id="a-financial-literacy" onchange="handleAssessInput('a-financial-literacy')">
        <option value="">Select...</option>
        <option value="0">0 out of 3</option>
        <option value="1">1 out of 3</option>
        <option value="2">2 out of 3</option>
        <option value="3">3 out of 3</option>
    </select> <span class="assess-percentile-hint" id="pct-financial-literacy"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-financial-literacy" onchange="handleSkip('a-financial-literacy')"><label for="skip-financial-literacy">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-savings-rate">
    <span class="assess-label">What percentage of your income do you invest each month?</span>
    <span class="assess-hint">Include pension contributions, ISAs, brokerage accounts, and any other investment vehicles. Employer match counts too.</span>
    <input type="number" id="a-savings-rate" min="0" max="100" step="1" placeholder="e.g. 15" onchange="handleAssessInput('a-savings-rate')"> % <span class="assess-percentile-hint" id="pct-savings-rate"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-savings-rate" onchange="handleSkip('a-savings-rate')"><label for="skip-savings-rate">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Safety</h4>

<div class="assess-input-group" id="ig-diversification">
    <span class="assess-label">How diversified is your portfolio across asset classes?</span>
    <span class="assess-hint">Consider whether you hold a mix of equities, bonds, property, cash, and whether your equity holdings span multiple geographies.</span>
    <select id="a-diversification" onchange="handleAssessInput('a-diversification')">
        <option value="">Select...</option>
        <option value="0">Everything in one asset class or a single holding</option>
        <option value="1">Mostly one asset class with a little diversification</option>
        <option value="2">Spread across 2 &ndash; 3 asset classes</option>
        <option value="3">Broadly diversified across asset classes, geographies, and sectors</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-diversification" onchange="handleSkip('a-diversification')"><label for="skip-diversification">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-largest-position">
    <span class="assess-label">What percentage of your portfolio is in your single largest holding?</span>
    <span class="assess-hint">Include employer shares, property investments, and individual stock positions. If you hold one global index fund, that counts as one holding.</span>
    <select id="a-largest-position" onchange="handleAssessInput('a-largest-position')">
        <option value="">Select...</option>
        <option value="0">Over 80%</option>
        <option value="1">50 &ndash; 80%</option>
        <option value="2">25 &ndash; 50%</option>
        <option value="3">10 &ndash; 25%</option>
        <option value="4">Under 10%</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-largest-position" onchange="handleSkip('a-largest-position')"><label for="skip-largest-position">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-emergency-fund">
    <span class="assess-label">How many months of expenses could you cover without selling investments?</span>
    <span class="assess-hint">Count cash savings and easily accessible funds that are separate from your investment portfolio.</span>
    <select id="a-emergency-fund" onchange="handleAssessInput('a-emergency-fund')">
        <option value="">Select...</option>
        <option value="0">Less than 1 month</option>
        <option value="1">1 &ndash; 2 months</option>
        <option value="2">3 &ndash; 5 months</option>
        <option value="3">6 &ndash; 12 months</option>
        <option value="4">More than 12 months</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-emergency-fund" onchange="handleSkip('a-emergency-fund')"><label for="skip-emergency-fund">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Simplicity</h4>

<div class="assess-input-group" id="ig-time-spent">
    <span class="assess-label">How much time do you spend on your investments each month?</span>
    <span class="assess-hint">Include research, trading, checking prices, reading financial news, and rebalancing.</span>
    <select id="a-time-spent" onchange="handleAssessInput('a-time-spent')">
        <option value="">Select...</option>
        <option value="0">I don't track or manage my investments at all</option>
        <option value="1">Less than 30 minutes</option>
        <option value="2">30 minutes to 2 hours</option>
        <option value="3">2 &ndash; 5 hours</option>
        <option value="4">More than 5 hours</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-time-spent" onchange="handleSkip('a-time-spent')"><label for="skip-time-spent">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-fees">
    <span class="assess-label">What are your total annual investment fees (% of portfolio)?</span>
    <span class="assess-hint">Include platform fees, fund charges (OCF/TER), and any adviser fees. Many providers list a combined figure on your account summary.</span>
    <select id="a-fees" onchange="handleAssessInput('a-fees')">
        <option value="">Select...</option>
        <option value="0">I have no idea</option>
        <option value="1">Over 1.5%</option>
        <option value="2">1.0 &ndash; 1.5%</option>
        <option value="3">0.5 &ndash; 1.0%</option>
        <option value="4">0.2 &ndash; 0.5%</option>
        <option value="5">Under 0.2%</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-fees" onchange="handleSkip('a-fees')"><label for="skip-fees">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-auto-contributions">
    <span class="assess-label">Are your investment contributions automated?</span>
    <span class="assess-hint">Check if you have a standing order or direct debit set up for regular investments.</span>
    <select id="a-auto-contributions" onchange="handleAssessInput('a-auto-contributions')">
        <option value="">Select...</option>
        <option value="0">No &ndash; I invest manually and irregularly</option>
        <option value="1">Partly &ndash; some contributions are automated, some manual</option>
        <option value="2">Yes &ndash; all contributions are fully automated</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-auto-contributions" onchange="handleSkip('a-auto-contributions')"><label for="skip-auto-contributions">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-growth">
        <span class="assess-summary-label">Growth</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-growth" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-growth">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published research on investor behaviour and financial literacy. Safety and Simplicity are recorded for your awareness but not scored, as the available data does not support reliable percentile estimates.</p>
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

<p>You now understand why investing matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about growth, safety, and simplicity. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/investing/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Investing Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Investing. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/investing/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'investing';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-annual-return', 'a-behaviour-gap', 'a-financial-literacy', 'a-savings-rate',
        'a-diversification', 'a-largest-position', 'a-emergency-fund',
        'a-time-spent', 'a-fees', 'a-auto-contributions'
    ];

    // Scoring thresholds: [{value, percentile}, ...] sorted by value ascending
    // For dropdowns, value is a string matching the option value
    var THRESHOLDS = {
        'a-annual-return': [
            {v:-10,p:5},{v:0,p:20},{v:4,p:40},{v:7,p:55},{v:10,p:70},{v:15,p:85},{v:20,p:92},{v:30,p:98}
        ],
        'a-behaviour-gap': [
            {v:'0',p:15},{v:'1',p:30},{v:'2',p:50},{v:'3',p:75},{v:'4',p:90}
        ],
        'a-financial-literacy': [
            {v:'0',p:10},{v:'1',p:30},{v:'2',p:55},{v:'3',p:80}
        ],
        'a-savings-rate': [
            {v:0,p:10},{v:5,p:30},{v:10,p:50},{v:15,p:65},{v:20,p:75},{v:30,p:85},{v:50,p:95}
        ]
    };

    var VALUE_ITEMS = {
        growth: ['a-annual-return', 'a-behaviour-gap', 'a-financial-literacy', 'a-savings-rate']
    };

    // Safety and simplicity items are recorded but not scored (insufficient population data for percentiles)
    var UNSCORED_ITEMS = [
        'a-diversification', 'a-largest-position', 'a-emergency-fund',
        'a-time-spent', 'a-fees', 'a-auto-contributions'
    ];

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
        if (UNSCORED_ITEMS.indexOf(itemId) !== -1) return; // no hints for unscored items
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
        ['growth'].forEach(function(vk) {
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
        ['growth'].forEach(function(vk) {
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
