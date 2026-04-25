---
layout: default
title: "Networks – Level 1: Awareness"
life_area_slug: networks
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

<h1>Networks: Level 1</h1>

<p class="l1-subtitle">Understand what professional networks mean, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Networks Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why networks matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Professional networks are one of the strongest predictors of career outcomes. An estimated <a href="https://www.apollotechnical.com/networking-statistics/" target="_blank">85% of jobs are filled through networking</a>, and 70% are never publicly posted. Referral candidates are <a href="https://www.zippia.com/advice/networking-statistics/" target="_blank">four times more likely</a> to receive an interview and are hired up to 70% faster.</p>

<p>The information advantage is equally important. A landmark MIT study using LinkedIn data found that <a href="https://www.science.org/doi/10.1126/science.abl4476" target="_blank">moderately weak ties</a> – casual acquaintances rather than close contacts – had the greatest impact on job mobility, because they connect you to networks that do not overlap with your own.</p>

<p>Despite 80% of professionals considering networking important, most people network reactively – reaching out only when they need something. Deliberate, sustained network building is uncommon and disproportionately rewarded. The difference between a passive and an active networker compounds over years into dramatically different career trajectories.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about networks</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People build professional networks for different reasons. This site scores every networks intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Depth</h3>
<p>The quality and strength of key professional relationships – trusted advisors, mentors, collaborators, and allies who genuinely understand your work and advocate for you. People who lean towards this value cultivate a smaller number of high-value relationships, investing time in deepening trust and providing genuine value.</p>

<h3>Breadth</h3>
<p>The range and diversity of your professional network – connections across different industries, roles, seniority levels, and backgrounds. People who lean towards this value actively expand their circle, maintain weak ties, and ensure their network provides access to diverse information and opportunities.</p>

<h3>Relevance</h3>
<p>Ensuring your network connections are aligned with your current and future professional direction. People who lean towards this value regularly evaluate whether their network serves their goals, prune connections that no longer add value, and deliberately build relationships in areas where they are heading.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each networks value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Depth &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Esther_Dyson" target="_blank">Esther Dyson</a> has maintained deep professional relationships with technology founders, investors, and policymakers for over 40 years. She was an early investor in Flickr, del.icio.us, and 23andMe, in each case building on years of genuine relationships with the founders. She is known for maintaining a small number of close professional ties that she invests in deeply over decades rather than collecting contacts.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Breadth &ndash; Level 5</div>
    <p><a href="https://rfreedman.org/" target="_blank">Reid Hoffman</a> co-founded LinkedIn and built a professional network spanning technology, venture capital, politics, media, and academia. He is known for connecting people across industries and geographies, and his network routinely surfaces emerging opportunities, talent, and ideas before they become widely known. His book <em>The Start-up of You</em> codified his approach to network building.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Relevance &ndash; Level 5</div>
    <p><a href="https://www.ycombinator.com/people/michael-seibel" target="_blank">Michael Seibel</a>, CEO of Y Combinator, has built a network that evolves in precise alignment with his professional direction. As he moved from founding Justin.tv (later Twitch) to leading YC, his network shifted from media and gaming to early-stage startups, ensuring that his connections anticipate where he is heading and proactively surface relevant founders and opportunities.</p>
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
<h4>Depth</h4>

<div class="assess-input-group" id="ig-strong-ties">
    <span class="assess-label">How many professional contacts would actively recommend or advocate for you if asked?</span>
    <span class="assess-hint">Think about who would take a phone call from a hiring manager on your behalf.</span>
    <select id="a-strong-ties" onchange="handleAssessInput('a-strong-ties')"><option value="">Select...</option><option value="none">None &ndash; I can't think of anyone</option><option value="one-or-two">One or two people</option><option value="three-to-five">Three to five people</option><option value="six-to-ten">Six to ten people</option><option value="more-than-ten">More than ten people</option></select> <span class="assess-percentile-hint" id="pct-strong-ties"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-strong-ties" onchange="handleSkip('a-strong-ties')"><label for="skip-strong-ties">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-mentor-sponsor">
    <span class="assess-label">Do you currently have a mentor or sponsor in your professional life?</span>
    <span class="assess-hint">A mentor gives advice; a sponsor advocates for you in rooms you're not in. Both count.</span>
    <select id="a-mentor-sponsor" onchange="handleAssessInput('a-mentor-sponsor')"><option value="">Select...</option><option value="no">No &ndash; neither</option><option value="informal">Informal &ndash; someone I occasionally turn to</option><option value="mentor">Mentor &ndash; regular guidance from someone senior</option><option value="sponsor">Sponsor &ndash; someone who actively opens doors for me</option><option value="both">Both &ndash; I have a mentor and a sponsor</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-mentor-sponsor" onchange="handleSkip('a-mentor-sponsor')"><label for="skip-mentor-sponsor">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-reciprocity">
    <span class="assess-label">How much value do you offer to your strongest professional relationships?</span>
    <span class="assess-hint">Introductions, expertise, feedback, emotional support &ndash; value flows both ways.</span>
    <select id="a-reciprocity" onchange="handleAssessInput('a-reciprocity')"><option value="">Select...</option><option value="very-little">Very little &ndash; I mostly receive without giving back</option><option value="some">Some &ndash; I help when asked but don't proactively offer</option><option value="balanced">Balanced &ndash; roughly equal give and take</option><option value="generous">Generous &ndash; I actively look for ways to help my contacts</option><option value="systematic">Systematic &ndash; I deliberately invest in my key relationships</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-reciprocity" onchange="handleSkip('a-reciprocity')"><label for="skip-reciprocity">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Breadth</h4>

<div class="assess-input-group" id="ig-network-size">
    <span class="assess-label">How large is your professional network and how many contexts does it span?</span>
    <span class="assess-hint">Count separate professional contexts: current work, previous roles, industry groups, alumni networks, conferences.</span>
    <select id="a-network-size" onchange="handleAssessInput('a-network-size')"><option value="">Select...</option><option value="very-small">Very small &ndash; essentially just my current colleagues</option><option value="small">Small &ndash; current and one previous workplace</option><option value="moderate">Moderate &ndash; 2 &ndash; 3 professional contexts</option><option value="broad">Broad &ndash; 4 &ndash; 5 contexts across different settings</option><option value="extensive">Extensive &ndash; 6+ contexts spanning multiple industries or sectors</option></select> <span class="assess-percentile-hint" id="pct-network-size"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-network-size" onchange="handleSkip('a-network-size')"><label for="skip-network-size">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-diversity">
    <span class="assess-label">Is your network concentrated in one industry or does it span multiple areas?</span>
    <span class="assess-hint">Check your LinkedIn connections by industry &ndash; are 90% in the same field?</span>
    <select id="a-diversity" onchange="handleAssessInput('a-diversity')"><option value="">Select...</option><option value="single-industry">Single industry &ndash; almost everyone is in my current field</option><option value="mostly-one">Mostly one &ndash; a few contacts in adjacent fields</option><option value="two-to-three">Two to three industries or sectors</option><option value="diverse">Diverse &ndash; connections across several different fields</option><option value="very-diverse">Very diverse &ndash; broad network spanning many industries and backgrounds</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-diversity" onchange="handleSkip('a-diversity')"><label for="skip-diversity">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-new-connections">
    <span class="assess-label">How often do you make meaningful new professional connections?</span>
    <span class="assess-hint">Count the last 6 months &ndash; how many new people have you had a substantive conversation with?</span>
    <select id="a-new-connections" onchange="handleAssessInput('a-new-connections')"><option value="">Select...</option><option value="never">Never &ndash; I haven't made a new professional connection in months</option><option value="rarely">Rarely &ndash; one or two in the past 6 months</option><option value="occasionally">Occasionally &ndash; roughly one per month</option><option value="regularly">Regularly &ndash; several per month</option><option value="frequently">Frequently &ndash; I actively build new connections every week</option></select> <span class="assess-percentile-hint" id="pct-new-connections"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-new-connections" onchange="handleSkip('a-new-connections')"><label for="skip-new-connections">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Relevance</h4>

<div class="assess-input-group" id="ig-alignment">
    <span class="assess-label">Are your current network connections aligned with where your career is heading?</span>
    <span class="assess-hint">Are most of your strong connections in areas relevant to your future, or mainly from your past?</span>
    <select id="a-alignment" onchange="handleAssessInput('a-alignment')"><option value="">Select...</option><option value="past-focused">Past-focused &ndash; almost all connections are from previous roles</option><option value="mostly-past">Mostly past &ndash; a few connections relevant to my future direction</option><option value="mixed">Mixed &ndash; roughly half past, half future-relevant</option><option value="mostly-aligned">Mostly aligned &ndash; the majority are in relevant areas</option><option value="strategically-aligned">Strategically aligned &ndash; I've deliberately built connections in my target direction</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-alignment" onchange="handleSkip('a-alignment')"><label for="skip-alignment">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-gaps">
    <span class="assess-label">Can you identify the industries, roles, or seniority levels where you lack connections but would benefit from them?</span>
    <span class="assess-hint">Think about your career goals &ndash; who would you need to know to reach them?</span>
    <select id="a-gaps" onchange="handleAssessInput('a-gaps')"><option value="">Select...</option><option value="no">No &ndash; I haven't thought about network gaps</option><option value="vaguely">Vaguely &ndash; I know I need more connections but not where specifically</option><option value="some">Some &ndash; I can identify one or two gaps</option><option value="clearly">Clearly &ndash; I know exactly which areas I need to build</option><option value="mapped">Mapped &ndash; I have a specific plan for filling network gaps</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-gaps" onchange="handleSkip('a-gaps')"><label for="skip-gaps">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-maintenance">
    <span class="assess-label">How actively do you maintain your existing professional relationships?</span>
    <span class="assess-hint">When did you last reach out to a former colleague or professional contact without needing something?</span>
    <select id="a-maintenance" onchange="handleAssessInput('a-maintenance')"><option value="">Select...</option><option value="not-at-all">Not at all &ndash; I only reconnect when I need something</option><option value="passively">Passively &ndash; I respond when contacted but don't initiate</option><option value="occasionally">Occasionally &ndash; I reach out to a few people now and then</option><option value="regularly">Regularly &ndash; I proactively maintain key relationships</option><option value="systematically">Systematically &ndash; I have a regular cadence for staying in touch</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-maintenance" onchange="handleSkip('a-maintenance')"><label for="skip-maintenance">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-depth">
        <span class="assess-summary-label">Depth</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-depth" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-depth">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-breadth">
        <span class="assess-summary-label">Breadth</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-breadth" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-breadth">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-relevance">
        <span class="assess-summary-label">Relevance</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-relevance" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-relevance">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on professional networking behaviour among adults. Items without reliable population benchmarks are not scored.</p>
</div>

<div class="assess-recorded" id="assessRecorded">Your answers have been recorded.</div>

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

<p>You now understand why networks matter, what different people get out of them, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about depth, breadth, and relevance. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/networks/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Networks Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Networks. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/networks/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'networks';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-strong-ties', 'a-mentor-sponsor', 'a-reciprocity',
        'a-network-size', 'a-diversity', 'a-new-connections',
        'a-alignment', 'a-gaps', 'a-maintenance'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: most professionals have 1 – 2 advocates at most;
    // median LinkedIn network spans 2 – 3 contexts; deliberate new-connection
    // building is rare (~80% network reactively).
    var THRESHOLDS = {
        'a-strong-ties': [
            // Most professionals lack active advocates; 10+ is exceptional
            {v:'none',p:10},{v:'one-or-two',p:30},{v:'three-to-five',p:55},{v:'six-to-ten',p:78},{v:'more-than-ten',p:95}
        ],
        'a-network-size': [
            // Most people draw professional contacts from 1 – 2 settings; 6+ is rare
            {v:'very-small',p:12},{v:'small',p:30},{v:'moderate',p:52},{v:'broad',p:75},{v:'extensive',p:93}
        ],
        'a-new-connections': [
            // ~80% network reactively; weekly deliberate connection-building is very uncommon
            {v:'never',p:10},{v:'rarely',p:30},{v:'occasionally',p:55},{v:'regularly',p:78},{v:'frequently',p:95}
        ]
    };

    var VALUE_ITEMS = {
        depth: ['a-strong-ties'],
        breadth: ['a-network-size', 'a-new-connections'],
        relevance: []
    };

    // Items without reliable population benchmarks
    var UNSCORED_ITEMS = [
        'a-mentor-sponsor', 'a-reciprocity', 'a-diversity',
        'a-alignment', 'a-gaps', 'a-maintenance'
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
            setTimeout(function() { openStep(STEPS[idx + 1]); }, 300);
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
        if (!THRESHOLDS[itemId]) return null;
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
        if (!items || items.length === 0) return null;
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
        ['depth', 'breadth', 'relevance'].forEach(function(vk) {
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
        ['depth', 'breadth', 'relevance'].forEach(function(vk) {
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
