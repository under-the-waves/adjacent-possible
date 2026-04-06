---
layout: default
title: "Organisation – Level 1: Awareness"
life_area_slug: organisation
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

<h1>Organisation: Level 1</h1>

<p class="l1-subtitle">Understand what organisation means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Organisation Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why organisation matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Organisation is the invisible infrastructure behind reliability and clarity. When it works, you barely notice it. When it fails, the costs are constant and compounding.</p>

<p>The average person spends <a href="https://www.prnewswire.com/news-releases/lost-and-found-the-average-american-spends-25-days-each-year-looking-for-lost-items-collectively-costing-us-households-27-billion-annually-in-replacement-costs-300449305.html" target="_blank">8.5 minutes per day</a> searching for misplaced items, and knowledge workers lose <a href="https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-social-economy" target="_blank">1.8 &ndash; 2.5 hours per day</a> hunting for information they need. That is roughly a quarter of the working day spent on retrieval rather than productive work.</p>

<p><a href="https://blog.idonethis.com/how-to-master-the-art-of-to-do-lists/" target="_blank">41% of to-do list items</a> are never completed, and <a href="https://www.unitedhealthgroup.com/newsroom/2022/2022-07-20-optum-consumer-survey-better-tools-for-finding-care.html" target="_blank">52% of people</a> missed a healthcare appointment in the past year &ndash; a third of them simply because they forgot. <a href="https://www.acuitytraining.co.uk/news-tips/time-management-statistics-research/" target="_blank">82% of people</a> have no formal time management system at all.</p>

<p>The baseline is so low that even modest improvements in capture, filing, and review place you well above the majority. Organisation is one of the rare areas where the gap between average and competent is enormous, and the effort required to close it is relatively small.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about organisation</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue organisation for different reasons. This site scores every organisation intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Tracking</h3>
<p>Capturing and monitoring all commitments, tasks, and information so nothing falls through the cracks. Maintaining a trusted system for recording what needs doing, reviewing progress regularly, and ensuring everything important is visible and accounted for. People who prioritise this value invest in comprehensive capture and review systems.</p>

<h3>Order</h3>
<p>Maintaining structured, predictable systems for physical and digital environments. Consistent filing, clear storage systems, labelled locations for everything, and routines that keep spaces and information organised. People who prioritise this value believe that external order supports internal clarity.</p>

<h3>Speed</h3>
<p>Minimising the time spent on organisational overhead so you can move quickly from intention to action. Rapid processing of incoming tasks, fast retrieval of information, and systems designed for throughput over perfection. People who prioritise this value accept occasional missed details in exchange for getting more done.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each organisation value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Tracking &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/David_Allen_(author)" target="_blank">David Allen</a> developed Getting Things Done (GTD), one of the most widely adopted personal productivity systems in the world. His methodology centres on comprehensive capture and regular review of all commitments, and he has practised and refined it for over 30 years. His concept of "mind like water" &ndash; a state of zero open loops in your head &ndash; has become the benchmark for what thoroughness in personal organisation looks like.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Order &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Martha_Stewart" target="_blank">Martha Stewart</a> built a media empire around the systematic organisation of domestic life. Her approach to household management treats every domain &ndash; from kitchen storage to seasonal maintenance schedules &ndash; as a system to be designed, documented, and maintained. She has practised and publicly demonstrated this level of domestic order for over 40 years across multiple homes.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Speed &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Tiago_Forte" target="_blank">Tiago Forte</a> developed the "Building a Second Brain" methodology for organising digital information and projects. He practises what he teaches &ndash; maintaining a personal knowledge management system that he uses daily to run a company, write, and teach. His approach prioritises speed of retrieval over comprehensiveness, and he has refined it through over a decade of personal use.</p>
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
<h4>Tracking</h4>

<div class="assess-input-group" id="ig-capture-system">
    <span class="assess-label">Do you have a single, trusted place where you capture all incoming tasks and commitments?</span>
    <span class="assess-hint">This could be an app, a notebook, a whiteboard &ndash; anything you consistently use to record what needs doing.</span>
    <select id="a-capture-system" onchange="handleAssessInput('a-capture-system')">
        <option value="">Select...</option>
        <option value="none">No &ndash; I rely on memory</option>
        <option value="scattered">Scattered &ndash; I capture things in multiple places with no consistency</option>
        <option value="partial">Partial &ndash; I have a main place but often forget to use it</option>
        <option value="consistent">Consistent &ndash; one trusted place I use most of the time</option>
        <option value="comprehensive">Comprehensive &ndash; everything goes into one system reliably</option>
    </select> <span class="assess-percentile-hint" id="pct-capture-system"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-capture-system" onchange="handleSkip('a-capture-system')"><label for="skip-capture-system">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-review-frequency">
    <span class="assess-label">How often do you review your outstanding tasks and commitments?</span>
    <span class="assess-hint">Think about whether you have a regular review habit or rely on memory.</span>
    <select id="a-review-frequency" onchange="handleAssessInput('a-review-frequency')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I rely on memory or react as things come up</option>
        <option value="rarely">Rarely &ndash; only when I feel overwhelmed</option>
        <option value="monthly">Monthly &ndash; rough check-in once a month or so</option>
        <option value="weekly">Weekly &ndash; regular weekly review</option>
        <option value="daily">Daily &ndash; I review my commitments every day</option>
    </select> <span class="assess-percentile-hint" id="pct-review-frequency"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-review-frequency" onchange="handleSkip('a-review-frequency')"><label for="skip-review-frequency">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-missed-commitments">
    <span class="assess-label">How many commitments did you drop or forget in the past month?</span>
    <span class="assess-hint">Missed appointments, forgotten promises, overdue tasks, unanswered messages you meant to reply to.</span>
    <select id="a-missed-commitments" onchange="handleAssessInput('a-missed-commitments')">
        <option value="">Select...</option>
        <option value="many">Many &ndash; I regularly forget things or miss deadlines</option>
        <option value="several">Several &ndash; a few significant ones I can recall</option>
        <option value="occasional">Occasional &ndash; one or two minor things</option>
        <option value="rare">Rare &ndash; almost nothing slipped through</option>
        <option value="none">None &ndash; I kept every commitment</option>
    </select> <span class="assess-percentile-hint" id="pct-missed-commitments"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-missed-commitments" onchange="handleSkip('a-missed-commitments')"><label for="skip-missed-commitments">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Order</h4>

<div class="assess-input-group" id="ig-physical-spaces">
    <span class="assess-label">Do your main physical spaces (desk, kitchen, bedroom) have a designated place for every item?</span>
    <span class="assess-hint">Could you tell someone exactly where everything belongs? Or do things accumulate on surfaces?</span>
    <select id="a-physical-spaces" onchange="handleAssessInput('a-physical-spaces')">
        <option value="">Select...</option>
        <option value="chaotic">Chaotic &ndash; things end up wherever they land</option>
        <option value="mostly-messy">Mostly messy &ndash; a few things have homes but most don't</option>
        <option value="mixed">Mixed &ndash; some spaces are organised, others aren't</option>
        <option value="mostly-ordered">Mostly ordered &ndash; most items have a place and I use it</option>
        <option value="fully-ordered">Fully ordered &ndash; everything has a home and I maintain it</option>
    </select> <span class="assess-percentile-hint" id="pct-physical-spaces"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-physical-spaces" onchange="handleSkip('a-physical-spaces')"><label for="skip-physical-spaces">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-digital-files">
    <span class="assess-label">Can you find any digital file you need within 60 seconds?</span>
    <span class="assess-hint">Think about documents, photos, receipts, passwords. Do you have a filing system or do you rely on search?</span>
    <select id="a-digital-files" onchange="handleAssessInput('a-digital-files')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I often can't find what I need</option>
        <option value="sometimes">Sometimes &ndash; depends on the file type</option>
        <option value="search-dependent">Search-dependent &ndash; I can usually find things but only via search</option>
        <option value="mostly">Mostly &ndash; I have a system that works for most things</option>
        <option value="always">Always &ndash; structured filing system with fast, reliable retrieval</option>
    </select> <span class="assess-percentile-hint" id="pct-digital-files"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-digital-files" onchange="handleSkip('a-digital-files')"><label for="skip-digital-files">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-clutter">
    <span class="assess-label">How overwhelmed do you feel by clutter in your home or workspace?</span>
    <span class="assess-hint">54% of people report feeling overwhelmed by clutter. Be honest about whether this applies to you.</span>
    <select id="a-clutter" onchange="handleAssessInput('a-clutter')">
        <option value="">Select...</option>
        <option value="very">Very overwhelmed &ndash; clutter is a constant source of stress</option>
        <option value="somewhat">Somewhat overwhelmed &ndash; it bothers me but I can function</option>
        <option value="neutral">Neutral &ndash; I notice it occasionally but it doesn't bother me much</option>
        <option value="low">Low &ndash; my spaces are reasonably tidy</option>
        <option value="none">Not at all &ndash; my spaces are consistently clear and organised</option>
    </select> <span class="assess-percentile-hint" id="pct-clutter"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-clutter" onchange="handleSkip('a-clutter')"><label for="skip-clutter">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Speed</h4>

<div class="assess-input-group" id="ig-search-time">
    <span class="assess-label">How much time do you spend each day searching for things you've misplaced?</span>
    <span class="assess-hint">Keys, wallet, phone, documents, tools. The average is about 8.5 minutes per day.</span>
    <select id="a-search-time" onchange="handleAssessInput('a-search-time')">
        <option value="">Select...</option>
        <option value="a-lot">A lot &ndash; 15+ minutes daily</option>
        <option value="above-average">Above average &ndash; around 10 &ndash; 15 minutes</option>
        <option value="average">Average &ndash; roughly 5 &ndash; 10 minutes</option>
        <option value="below-average">Below average &ndash; a few minutes at most</option>
        <option value="almost-none">Almost none &ndash; I rarely misplace things</option>
    </select> <span class="assess-percentile-hint" id="pct-search-time"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-search-time" onchange="handleSkip('a-search-time')"><label for="skip-search-time">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-inbox-processing">
    <span class="assess-label">How quickly do you typically process new tasks and messages that come in?</span>
    <span class="assess-hint">Same day? Same week? Do some sit unprocessed for weeks? Think about email, post, and verbal requests.</span>
    <select id="a-inbox-processing" onchange="handleAssessInput('a-inbox-processing')">
        <option value="">Select...</option>
        <option value="weeks">Weeks &ndash; things often sit unprocessed for a long time</option>
        <option value="several-days">Several days &ndash; I get to most things within a week</option>
        <option value="next-day">Next day &ndash; usually processed within 24 &ndash; 48 hours</option>
        <option value="same-day">Same day &ndash; I process most things the day they arrive</option>
        <option value="immediately">Immediately &ndash; I have a system that processes inputs as they arrive</option>
    </select> <span class="assess-percentile-hint" id="pct-inbox-processing"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-inbox-processing" onchange="handleSkip('a-inbox-processing')"><label for="skip-inbox-processing">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-system-count">
    <span class="assess-label">How many tools and systems do you currently use to stay organised?</span>
    <span class="assess-hint">Apps, notebooks, calendars, reminders, filing systems. Is it 1 &ndash; 2 core tools, or a scattered collection?</span>
    <select id="a-system-count" onchange="handleAssessInput('a-system-count')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I don't use any organisational tools</option>
        <option value="scattered">Scattered &ndash; many tools but no coherent system</option>
        <option value="several">Several &ndash; 3 &ndash; 5 tools that partially overlap</option>
        <option value="focused">Focused &ndash; 2 &ndash; 3 tools that work well together</option>
        <option value="integrated">Integrated &ndash; 1 &ndash; 2 core tools that cover everything I need</option>
    </select> <span class="assess-percentile-hint" id="pct-system-count"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-system-count" onchange="handleSkip('a-system-count')"><label for="skip-system-count">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-tracking">
        <span class="assess-summary-label">Tracking</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-tracking" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-tracking">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-order">
        <span class="assess-summary-label">Order</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-order" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-order">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-speed">
        <span class="assess-summary-label">Speed</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-speed" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-speed">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on organisational behaviour among adults. All items in this area are scored.</p>
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

<p>You now understand why organisation matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about tracking, order, and speed. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/organisation/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Organisation Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Organisation. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/organisation/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'organisation';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-capture-system', 'a-review-frequency', 'a-missed-commitments',
        'a-physical-spaces', 'a-digital-files', 'a-clutter',
        'a-search-time', 'a-inbox-processing', 'a-system-count'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: ~82% have no time management system, ~41% of to-do
    // items never completed, average 8.5 min/day searching for misplaced items.
    var THRESHOLDS = {
        'a-capture-system': [
            // ~82% have no formal system; comprehensive capture is very rare
            {v:'none',p:10},{v:'scattered',p:25},{v:'partial',p:45},{v:'consistent',p:72},{v:'comprehensive',p:93}
        ],
        'a-review-frequency': [
            // ~8% review weekly; most never formally revisit commitments
            {v:'never',p:10},{v:'rarely',p:30},{v:'monthly',p:55},{v:'weekly',p:80},{v:'daily',p:95}
        ],
        'a-missed-commitments': [
            // Most people drop several commitments per month; keeping all is very rare
            {v:'many',p:10},{v:'several',p:30},{v:'occasional',p:55},{v:'rare',p:78},{v:'none',p:95}
        ],
        'a-physical-spaces': [
            // ~54% feel overwhelmed by clutter; fully ordered spaces are rare
            {v:'chaotic',p:10},{v:'mostly-messy',p:25},{v:'mixed',p:50},{v:'mostly-ordered',p:75},{v:'fully-ordered',p:95}
        ],
        'a-digital-files': [
            // Most people rely on search or cannot find files reliably
            {v:'no',p:10},{v:'sometimes',p:30},{v:'search-dependent',p:50},{v:'mostly',p:75},{v:'always',p:95}
        ],
        'a-clutter': [
            // ~54% report feeling overwhelmed by clutter
            {v:'very',p:10},{v:'somewhat',p:30},{v:'neutral',p:50},{v:'low',p:75},{v:'none',p:95}
        ],
        'a-search-time': [
            // Average 8.5 min/day; rarely misplacing things is uncommon
            {v:'a-lot',p:10},{v:'above-average',p:25},{v:'average',p:45},{v:'below-average',p:72},{v:'almost-none',p:93}
        ],
        'a-inbox-processing': [
            // Most people process within days; immediate systematic processing is rare
            {v:'weeks',p:10},{v:'several-days',p:30},{v:'next-day',p:55},{v:'same-day',p:78},{v:'immediately',p:95}
        ],
        'a-system-count': [
            // Most people use scattered tools or none; an integrated 1-2 tool system is rare
            {v:'none',p:10},{v:'scattered',p:25},{v:'several',p:45},{v:'focused',p:75},{v:'integrated',p:93}
        ]
    };

    var VALUE_ITEMS = {
        tracking: ['a-capture-system', 'a-review-frequency', 'a-missed-commitments'],
        order: ['a-physical-spaces', 'a-digital-files', 'a-clutter'],
        speed: ['a-search-time', 'a-inbox-processing', 'a-system-count']
    };

    // All organisation items are scorable
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

    function interpolatePercentile(value, thresholds) {
        // All organisation items use string keys (dropdowns)
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
        ['tracking', 'order', 'speed'].forEach(function(vk) {
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
        ['tracking', 'order', 'speed'].forEach(function(vk) {
            scores[vk] = computeValuePercentile(vk);
        });
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-scores') || {};
            all[AREA] = scores;
            APStorage.save('ap-level1-scores', all);
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
