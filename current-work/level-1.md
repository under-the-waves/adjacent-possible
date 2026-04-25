---
layout: default
title: "Current Work – Level 1: Awareness"
life_area_slug: current-work
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

<h1>Current Work: Level 1</h1>

<p class="l1-subtitle">Understand what current work means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Current Work Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why current work matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your current work dominates your waking life. The average person spends roughly <a href="https://www.gettysburg.edu/news/stories?id=79db7b34-630c-4f49-ad32-4ab9ea48e72b" target="_blank">90,000 hours</a> at work over a lifetime – more time than almost any other single activity.</p>

<p>Yet most people underperform relative to their potential. The average worker is genuinely productive for just <a href="https://www.vouchercloud.com/resources/office-worker-productivity" target="_blank">2 hours and 53 minutes</a> of an 8-hour day. Only <a href="https://www.gallup.com/workplace/349484/state-of-the-global-workplace.aspx" target="_blank">21% of employees globally</a> are actively engaged, and 45% report working primarily for pay rather than purpose.</p>

<p>The gap between typical and exceptional is enormous. Top performers in complex roles are up to <a href="https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights" target="_blank">800% more productive</a> than average, with the top 5% producing 26% of total output. Flow states – which occupy roughly 5% of working hours for the average person – can nearly double productivity when increased.</p>

<p>Small improvements compound dramatically. Moving from disengaged to engaged, from reactive to intentional, or from competent to skilled can transform both your output and your experience of work.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about current work</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach their working lives for different reasons. This site scores every current work intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Rewards</h3>
<p>The tangible returns you receive for your work – compensation, recognition, status, and career advancement. People who lean towards this value ensure their work delivers fair returns for the effort invested, and actively manage their compensation trajectory.</p>

<h3>Competence</h3>
<p>Skill and effectiveness at performing your role's core responsibilities. Technical proficiency, consistent quality of output, and the ability to handle increasing complexity. People who lean towards this value focus on mastering the craft of their work and continuously raising their standard.</p>

<h3>Engagement</h3>
<p>Psychological investment, motivation, and meaning found in daily work. Experiencing flow states, feeling intrinsically motivated, and finding genuine interest in problems. People who lean towards this value seek roles and tasks that align with their strengths and actively shape their work to be absorbing.</p>

<h3>Balance</h3>
<p>Maintaining sustainable boundaries between work and the rest of life. Manageable hours, predictable schedules, the ability to disconnect, and ensuring work does not crowd out health, relationships, or personal interests. People who lean towards this value protect their non-work life as a deliberate choice.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each current work value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Rewards &ndash; Level 5</div>
    <p><a href="https://www.crunchbase.com/person/stewart-butterfield" target="_blank">Stewart Butterfield</a> co-founded Flickr and Slack, both of which emerged from failed video game projects. He sold Flickr to Yahoo for an estimated $25 million and built Slack into a company valued at $27.7 billion when Salesforce acquired it in 2021. His career demonstrates how exceptional rewards follow from building things people genuinely need.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Competence &ndash; Level 5</div>
    <p><a href="https://jvns.ca/" target="_blank">Julia Evans</a> is a software engineer known for explaining complex systems concepts with unusual clarity. Her zines, blog posts, and tools have become widely used learning resources across the industry. She exemplifies competence that goes beyond performing a role well – she advances how others understand and practise their craft.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Engagement &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/John_Carmack" target="_blank">John Carmack</a> has spent decades working at the frontier of real-time graphics and virtual reality, from Doom to Oculus. He is known for sustained, deep focus – often working 60+ hour weeks by choice – and has described programming as the activity he would do regardless of compensation. His engagement is inseparable from his identity.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Balance &ndash; Level 5</div>
    <p><a href="https://basecamp.com/about/jason-fried" target="_blank">Jason Fried</a>, co-founder of Basecamp, built a profitable technology company while publicly advocating for 40-hour weeks, no meetings on certain days, and company-wide sabbaticals. He has sustained high performance over two decades while deliberately protecting personal time, and his writing on work-life integration has influenced how thousands of companies operate.</p>
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
<h4>Rewards</h4>

<div class="assess-input-group" id="ig-comp-market">
    <span class="assess-label">How does your total compensation compare to the market rate for your role and experience level?</span>
    <span class="assess-hint">Check Glassdoor, Levels.fyi, or industry salary surveys for your role and location.</span>
    <select id="a-comp-market" onchange="handleAssessInput('a-comp-market')">
        <option value="">Select...</option>
        <option value="dont-know">I don't know &ndash; I haven't checked</option>
        <option value="well-below">Well below market &ndash; significantly underpaid</option>
        <option value="somewhat-below">Somewhat below &ndash; noticeable gap</option>
        <option value="at-market">At market &ndash; roughly what I'd expect</option>
        <option value="above-market">Above market &ndash; paid more than the typical rate</option>
    </select> <span class="assess-percentile-hint" id="pct-comp-market"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-comp-market" onchange="handleSkip('a-comp-market')"><label for="skip-comp-market">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-last-raise">
    <span class="assess-label">When did you last receive a pay rise or promotion?</span>
    <span class="assess-hint">Check your employment records or payslips.</span>
    <select id="a-last-raise" onchange="handleAssessInput('a-last-raise')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; no raise since I started this role</option>
        <option value="over-two-years">Over two years ago</option>
        <option value="one-to-two-years">One to two years ago</option>
        <option value="within-a-year">Within the past year</option>
        <option value="recently">Recently &ndash; within the past six months</option>
    </select> <span class="assess-percentile-hint" id="pct-last-raise"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-last-raise" onchange="handleSkip('a-last-raise')"><label for="skip-last-raise">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-recognition">
    <span class="assess-label">How often are your contributions recognised by your manager or organisation?</span>
    <span class="assess-hint">Think about the last 6 months &ndash; have you received specific, positive feedback on your work?</span>
    <select id="a-recognition" onchange="handleAssessInput('a-recognition')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; my work goes unacknowledged</option>
        <option value="rarely">Rarely &ndash; once or twice in the past year</option>
        <option value="occasionally">Occasionally &ndash; every few months</option>
        <option value="regularly">Regularly &ndash; monthly or more</option>
        <option value="frequently">Frequently &ndash; consistent, specific recognition</option>
    </select> <span class="assess-percentile-hint" id="pct-recognition"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-recognition" onchange="handleSkip('a-recognition')"><label for="skip-recognition">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Competence</h4>

<div class="assess-input-group" id="ig-performance">
    <span class="assess-label">How would you describe your current performance level?</span>
    <span class="assess-hint">If you don't have formal reviews, consider what feedback you've received informally.</span>
    <select id="a-performance" onchange="handleAssessInput('a-performance')">
        <option value="">Select...</option>
        <option value="struggling">Struggling &ndash; I'm underperforming and I know it</option>
        <option value="developing">Developing &ndash; I'm learning but not yet fully effective</option>
        <option value="meeting">Meeting expectations &ndash; solid, reliable performance</option>
        <option value="exceeding">Exceeding expectations &ndash; consistently strong</option>
        <option value="exceptional">Exceptional &ndash; top performer in my team or organisation</option>
    </select> <span class="assess-percentile-hint" id="pct-performance"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-performance" onchange="handleSkip('a-performance')"><label for="skip-performance">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-skills-gap">
    <span class="assess-label">Can you identify the skills that would most improve your effectiveness in your current role?</span>
    <span class="assess-hint">Think about where you struggle, where you spend the most time, or where mistakes happen.</span>
    <select id="a-skills-gap" onchange="handleAssessInput('a-skills-gap')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I haven't thought about it</option>
        <option value="vaguely">Vaguely &ndash; I have a general sense but nothing specific</option>
        <option value="one-or-two">One or two &ndash; I know my biggest gap</option>
        <option value="clearly">Clearly &ndash; I can name 2 &ndash; 3 specific skills</option>
        <option value="detailed">Detailed &ndash; I have a prioritised development plan</option>
    </select> <span class="assess-percentile-hint" id="pct-skills-gap"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-skills-gap" onchange="handleSkip('a-skills-gap')"><label for="skip-skills-gap">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-output">
    <span class="assess-label">How does your output compare to peers in a similar role?</span>
    <span class="assess-hint">Consider speed, quality, and the complexity of work you handle relative to others.</span>
    <select id="a-output" onchange="handleAssessInput('a-output')">
        <option value="">Select...</option>
        <option value="dont-know">I don't know &ndash; I have no basis for comparison</option>
        <option value="below">Below average &ndash; others seem more productive</option>
        <option value="average">Average &ndash; roughly comparable to peers</option>
        <option value="above">Above average &ndash; I produce more or better work</option>
        <option value="top">Top of peer group &ndash; consistently outperforming</option>
    </select> <span class="assess-percentile-hint" id="pct-output"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-output" onchange="handleSkip('a-output')"><label for="skip-output">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Engagement</h4>

<div class="assess-input-group" id="ig-flow">
    <span class="assess-label">How much of your working day do you spend in genuine focus or flow?</span>
    <span class="assess-hint">Estimate the percentage of your day where you are deeply absorbed in meaningful work.</span>
    <select id="a-flow" onchange="handleAssessInput('a-flow')">
        <option value="">Select...</option>
        <option value="almost-none">Almost none &ndash; less than 10% of my day</option>
        <option value="little">A little &ndash; roughly 10 &ndash; 25%</option>
        <option value="moderate">Moderate &ndash; around 25 &ndash; 50%</option>
        <option value="substantial">Substantial &ndash; around 50 &ndash; 75%</option>
        <option value="most">Most of my day &ndash; 75%+</option>
    </select> <span class="assess-percentile-hint" id="pct-flow"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-flow" onchange="handleSkip('a-flow')"><label for="skip-flow">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-motivation">
    <span class="assess-label">What primarily motivates you in your current work?</span>
    <span class="assess-hint">Would you do this work if the pay were lower? Do you look forward to the tasks themselves?</span>
    <select id="a-motivation" onchange="handleAssessInput('a-motivation')">
        <option value="">Select...</option>
        <option value="neither">Neither intrinsic nor extrinsic &ndash; I feel unmotivated</option>
        <option value="external-only">External rewards only &ndash; pay and status</option>
        <option value="mostly-external">Mostly external &ndash; but some aspects are interesting</option>
        <option value="mostly-intrinsic">Mostly intrinsic &ndash; I enjoy the work itself</option>
        <option value="deeply-intrinsic">Deeply intrinsic &ndash; I'd do this work even without external rewards</option>
    </select> <span class="assess-percentile-hint" id="pct-motivation"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-motivation" onchange="handleSkip('a-motivation')"><label for="skip-motivation">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-meaning">
    <span class="assess-label">Does your work feel meaningful to you?</span>
    <span class="assess-hint">Meaning can come from the work itself, its impact, the people, or the learning it provides.</span>
    <select id="a-meaning" onchange="handleAssessInput('a-meaning')">
        <option value="">Select...</option>
        <option value="meaningless">Meaningless &ndash; I can't see any purpose in what I do</option>
        <option value="mostly-not">Mostly not &ndash; occasional glimpses of meaning</option>
        <option value="somewhat">Somewhat &ndash; parts of it feel meaningful</option>
        <option value="mostly-yes">Mostly yes &ndash; I can see how my work matters</option>
        <option value="deeply">Deeply meaningful &ndash; my work is a core source of purpose</option>
    </select> <span class="assess-percentile-hint" id="pct-meaning"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-meaning" onchange="handleSkip('a-meaning')"><label for="skip-meaning">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Balance</h4>

<div class="assess-input-group" id="ig-hours">
    <span class="assess-label">How many hours do you actually work in a typical week?</span>
    <span class="assess-hint">Track a normal week honestly &ndash; include evening email, weekend work, and commuting time.</span>
    <select id="a-hours" onchange="handleAssessInput('a-hours')">
        <option value="">Select...</option>
        <option value="under-35">Under 35 hours</option>
        <option value="35-to-40">35 &ndash; 40 hours</option>
        <option value="40-to-45">40 &ndash; 45 hours</option>
        <option value="45-to-55">45 &ndash; 55 hours</option>
        <option value="over-55">Over 55 hours</option>
    </select> <span class="assess-percentile-hint" id="pct-hours"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-hours" onchange="handleSkip('a-hours')"><label for="skip-hours">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-disconnect">
    <span class="assess-label">Can you fully disconnect from work in evenings and weekends?</span>
    <span class="assess-hint">Consider whether you check messages out of habit, obligation, or genuine need.</span>
    <select id="a-disconnect" onchange="handleAssessInput('a-disconnect')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I'm always on call or checking</option>
        <option value="rarely">Rarely &ndash; I disconnect occasionally but usually can't</option>
        <option value="sometimes">Sometimes &ndash; depends on the week</option>
        <option value="mostly">Mostly &ndash; I disconnect most evenings and weekends</option>
        <option value="fully">Fully &ndash; I have clear boundaries and maintain them</option>
    </select> <span class="assess-percentile-hint" id="pct-disconnect"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-disconnect" onchange="handleSkip('a-disconnect')"><label for="skip-disconnect">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-crowding">
    <span class="assess-label">Is work currently crowding out health, relationships, or personal interests?</span>
    <span class="assess-hint">Think about the last month &ndash; has work prevented you from exercising, seeing friends, or pursuing hobbies?</span>
    <select id="a-crowding" onchange="handleAssessInput('a-crowding')">
        <option value="">Select...</option>
        <option value="severely">Severely &ndash; work dominates everything else</option>
        <option value="significantly">Significantly &ndash; multiple important areas are suffering</option>
        <option value="somewhat">Somewhat &ndash; one or two areas are affected</option>
        <option value="minimally">Minimally &ndash; I maintain most non-work activities</option>
        <option value="not-at-all">Not at all &ndash; work fits comfortably alongside everything else</option>
    </select> <span class="assess-percentile-hint" id="pct-crowding"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-crowding" onchange="handleSkip('a-crowding')"><label for="skip-crowding">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-rewards">
        <span class="assess-summary-label">Rewards</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-rewards" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-rewards">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-competence">
        <span class="assess-summary-label">Competence</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-competence" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-competence">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-engagement">
        <span class="assess-summary-label">Engagement</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-engagement" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-engagement">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-balance">
        <span class="assess-summary-label">Balance</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-balance" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-balance">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on work engagement, compensation, and work-life balance among adults. Some items in this area are not scored.</p>
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

<p>You now understand why current work matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about rewards, competence, engagement, and balance. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/current-work/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Current Work Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Current Work. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/current-work/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'current-work';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-comp-market', 'a-last-raise', 'a-recognition',
        'a-performance', 'a-skills-gap', 'a-output',
        'a-flow', 'a-motivation', 'a-meaning',
        'a-hours', 'a-disconnect', 'a-crowding'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: ~21% of employees globally are engaged (Gallup),
    // average productive hours ~2h53m/day, ~45% work primarily for pay.
    var THRESHOLDS = {
        'a-comp-market': [
            // ~40% don't know their market rate; being above market is uncommon
            {v:'dont-know',p:20},{v:'well-below',p:15},{v:'somewhat-below',p:35},{v:'at-market',p:60},{v:'above-market',p:85}
        ],
        'a-last-raise': [
            // Median time between raises ~18 months; recent raise within 6 months is top quartile
            {v:'never',p:10},{v:'over-two-years',p:25},{v:'one-to-two-years',p:50},{v:'within-a-year',p:72},{v:'recently',p:90}
        ],
        'a-recognition': [
            // ~65% of employees say they don't receive enough recognition (Gallup)
            {v:'never',p:10},{v:'rarely',p:30},{v:'occasionally',p:55},{v:'regularly',p:78},{v:'frequently',p:93}
        ],
        'a-performance': [
            // Self-reported; most rate themselves as meeting expectations
            {v:'struggling',p:8},{v:'developing',p:25},{v:'meeting',p:50},{v:'exceeding',p:78},{v:'exceptional',p:95}
        ],
        'a-skills-gap': [
            // Most people have not done deliberate skills gap analysis
            {v:'no',p:15},{v:'vaguely',p:35},{v:'one-or-two',p:55},{v:'clearly',p:78},{v:'detailed',p:95}
        ],
        'a-output': [
            // Many people have no basis for comparison; top of peer group is rare
            {v:'dont-know',p:20},{v:'below',p:15},{v:'average',p:50},{v:'above',p:78},{v:'top',p:95}
        ],
        'a-flow': [
            // Average worker is genuinely productive ~36% of the day; 75%+ is very rare
            {v:'almost-none',p:10},{v:'little',p:30},{v:'moderate',p:55},{v:'substantial',p:80},{v:'most',p:95}
        ],
        'a-motivation': [
            // ~45% work primarily for pay; deeply intrinsic motivation is uncommon
            {v:'neither',p:5},{v:'external-only',p:20},{v:'mostly-external',p:45},{v:'mostly-intrinsic',p:75},{v:'deeply-intrinsic',p:95}
        ],
        'a-meaning': [
            // ~40% of workers find their work meaningful; deeply meaningful is rare
            {v:'meaningless',p:8},{v:'mostly-not',p:25},{v:'somewhat',p:50},{v:'mostly-yes',p:75},{v:'deeply',p:95}
        ],
        'a-hours': [
            // Balance is inverse: fewer hours = better balance. ~40h is median for full-time.
            {v:'over-55',p:8},{v:'45-to-55',p:25},{v:'40-to-45',p:50},{v:'35-to-40',p:75},{v:'under-35',p:92}
        ],
        'a-disconnect': [
            // ~60% check work email outside hours; fully disconnecting is uncommon
            {v:'never',p:8},{v:'rarely',p:25},{v:'sometimes',p:50},{v:'mostly',p:75},{v:'fully',p:93}
        ],
        'a-crowding': [
            // Work-life conflict is widespread; no crowding at all is uncommon
            {v:'severely',p:8},{v:'significantly',p:25},{v:'somewhat',p:50},{v:'minimally',p:75},{v:'not-at-all',p:93}
        ]
    };

    var VALUE_ITEMS = {
        rewards: ['a-comp-market', 'a-last-raise', 'a-recognition'],
        competence: ['a-performance', 'a-skills-gap', 'a-output'],
        engagement: ['a-flow', 'a-motivation', 'a-meaning'],
        balance: ['a-hours', 'a-disconnect', 'a-crowding']
    };

    // All current-work items are scorable
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

        if (firstIncomplete) { openStep(firstIncomplete); }
    }

    function openStep(step) {
        STEPS.forEach(function(s) {
            var el = document.getElementById('step-' + s);
            if (el) el.classList.remove('open');
        });
        var target = document.getElementById('step-' + step);
        if (target) {
            target.classList.add('open');
            setTimeout(function() { target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 100);
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
        ['rewards', 'competence', 'engagement', 'balance'].forEach(function(vk) {
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
        ['rewards', 'competence', 'engagement', 'balance'].forEach(function(vk) {
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
