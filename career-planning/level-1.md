---
layout: default
title: "Career Planning – Level 1: Awareness"
life_area_slug: career-planning
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

<h1>Career Planning: Level 1</h1>

<p class="l1-subtitle">Understand what career planning means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Career Planning Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why career planning matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Most people do not plan their careers. Half of workers view their job as <a href="https://www.pewresearch.org/social-trends/2024/07/24/how-americans-view-their-jobs/" target="_blank">'just a job'</a> rather than a career or calling, and career progression is largely reactive – taking the next obvious step rather than choosing a deliberate direction.</p>

<p>The returns to planning are large. Only <a href="https://mentorcliq.com/mentoring-resources/mentoring-statistics" target="_blank">37% of professionals</a> have a mentor, yet those who do are five times more likely to be promoted. An estimated <a href="https://www.linkedin.com/pulse/new-survey-reveals-85-all-jobs-filled-via-networking-lou-adler/" target="_blank">85% of jobs</a> are filled through networking rather than formal applications, making deliberate relationship-building one of the highest-return career investments.</p>

<p>Skills are expiring faster than ever. The World Economic Forum projects that <a href="https://www.weforum.org/publications/the-future-of-jobs-report-2025/" target="_blank">39% of core skills</a> required for existing jobs will change by 2030, making passive career management increasingly dangerous.</p>

<p>Most people also lack the financial runway to take strategic risks – <a href="https://www.bankrate.com/banking/savings/emergency-savings-report/" target="_blank">59% cannot cover</a> more than three months of expenses. Career planning builds the clarity, positioning, and resilience needed to navigate an increasingly volatile professional landscape.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about career planning</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People plan their careers for different reasons. This site scores every career planning intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Clarity</h3>
<p>Having a clear, informed understanding of where your career is heading and why. Articulating a career thesis, understanding industry trajectories, and regularly revisiting your direction. People who lean towards this value invest in reflection and research rather than defaulting to the next obvious step.</p>

<h3>Advancement</h3>
<p>Progressing toward higher levels of responsibility, compensation, and influence. Building skills beyond your current role, pursuing promotions, developing your professional reputation, and ensuring your trajectory moves upward. People who lean towards this value treat career progression as an active project.</p>

<h3>Security</h3>
<p>Protecting yourself against career disruption through financial runway, transferable skills, and professional optionality. Maintaining multiple income capabilities, building financial buffers, and developing skills that are valuable across industries. People who lean towards this value build careers that are robust to disruption.</p>

<h3>Meaning</h3>
<p>Finding genuine purpose and significance in your professional life – work that aligns with your values and contributes to something you care about. Choosing roles based on mission fit, seeking work that feels inherently worthwhile, and ensuring your career contributes to your sense of identity. People who lean towards this value make career decisions based on purpose, not just advancement.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each career planning value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Clarity &ndash; Level 5</div>
    <p><a href="https://80000hours.org/about/#702" target="_blank">Benjamin Todd</a> co-founded 80,000 Hours, an organisation dedicated to helping people find careers that do the most good. He has spent over a decade researching career strategy and impact, developing frameworks for career decision-making that have influenced thousands of professionals. His career is itself a multi-decade thesis on how to choose professional direction deliberately.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Advancement &ndash; Level 5</div>
    <p><a href="https://www.linkedin.com/in/indranooyi/" target="_blank">Indra Nooyi</a> moved from India to the United States for graduate school and rose to become CEO of PepsiCo, a position she held for 12 years. She navigated multiple industries and geographies, building skills and reputation at each stage. Her trajectory from management consultant to Fortune 50 CEO exemplifies deliberate, sustained career advancement over decades.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Security &ndash; Level 5</div>
    <p><a href="https://tferriss.com/about/" target="_blank">Tim Ferriss</a> built a career structure that is genuinely antifragile – spanning bestselling books, a top-ranked podcast, angel investing, and public speaking. He has navigated multiple career transitions and income streams, ensuring that no single disruption could threaten his professional standing. His approach to career design emphasises optionality and redundancy.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Meaning &ndash; Level 5</div>
    <p><a href="https://paulgraham.com/bio.html" target="_blank">Paul Graham</a> co-founded Y Combinator after careers as a programmer, writer, and painter. His professional choices have consistently reflected a personal philosophy about what kind of work matters – from writing influential essays on startups and technology to funding early-stage founders. His career legacy is inseparable from his intellectual convictions.</p>
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
<h4>Clarity</h4>

<div class="assess-input-group" id="ig-direction">
    <span class="assess-label">Can you describe where you want your career to be in three years?</span>
    <span class="assess-hint">If you can't, that's useful information &ndash; it tells you clarity is a priority.</span>
    <select id="a-direction" onchange="handleAssessInput('a-direction')"><option value="">Select...</option><option value="no-idea">No idea &ndash; I haven't thought about it</option><option value="vague">Vague &ndash; a general sense but nothing specific</option><option value="rough-direction">Rough direction &ndash; I know the field or type of role</option><option value="clear">Clear &ndash; I can describe a specific target</option><option value="detailed">Detailed &ndash; specific role, organisation type, and timeline</option></select> <span class="assess-percentile-hint" id="pct-direction"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-direction" onchange="handleSkip('a-direction')"><label for="skip-direction">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-industry">
    <span class="assess-label">How well do you understand the major trends shaping your industry?</span>
    <span class="assess-hint">Consider AI, regulation, market shifts, and emerging roles in your field.</span>
    <select id="a-industry" onchange="handleAssessInput('a-industry')"><option value="">Select...</option><option value="not-at-all">Not at all &ndash; I haven't looked into it</option><option value="surface">Surface level &ndash; I've seen headlines</option><option value="moderate">Moderate &ndash; I have a reasonable understanding</option><option value="good">Good &ndash; I actively follow industry developments</option><option value="deep">Deep &ndash; I could brief someone on the key trends and their implications</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-industry" onchange="handleSkip('a-industry')"><label for="skip-industry">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-written-plan">
    <span class="assess-label">Do you have a written career plan or direction document?</span>
    <span class="assess-hint">This could be a document, a note on your phone, or a structured journal entry.</span>
    <select id="a-written-plan" onchange="handleAssessInput('a-written-plan')"><option value="">Select...</option><option value="no">No &ndash; nothing written</option><option value="mental-only">Mental only &ndash; I have ideas but haven't written them down</option><option value="rough-notes">Rough notes &ndash; scattered thoughts in various places</option><option value="basic-plan">Basic plan &ndash; a simple document with key goals</option><option value="detailed-plan">Detailed plan &ndash; structured document with milestones and timelines</option></select> <span class="assess-percentile-hint" id="pct-written-plan"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-written-plan" onchange="handleSkip('a-written-plan')"><label for="skip-written-plan">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Advancement</h4>

<div class="assess-input-group" id="ig-skills-beyond">
    <span class="assess-label">Are you currently developing skills beyond what your current role requires?</span>
    <span class="assess-hint">Think about courses, side projects, or deliberate practice in adjacent areas.</span>
    <select id="a-skills-beyond" onchange="handleAssessInput('a-skills-beyond')"><option value="">Select...</option><option value="no">No &ndash; I'm only using existing skills</option><option value="thinking-about-it">Thinking about it &ndash; I know I should but haven't started</option><option value="dabbling">Dabbling &ndash; occasional, unstructured learning</option><option value="actively">Actively &ndash; regular investment in one or two new skills</option><option value="systematically">Systematically &ndash; structured development plan with clear targets</option></select> <span class="assess-percentile-hint" id="pct-skills-beyond"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-skills-beyond" onchange="handleSkip('a-skills-beyond')"><label for="skip-skills-beyond">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-mentor">
    <span class="assess-label">Do you have a mentor or sponsor who is actively helping your career?</span>
    <span class="assess-hint">A mentor gives advice; a sponsor advocates for you in rooms you're not in.</span>
    <select id="a-mentor" onchange="handleAssessInput('a-mentor')"><option value="">Select...</option><option value="no">No &ndash; neither a mentor nor a sponsor</option><option value="informal">Informal &ndash; someone I occasionally ask for advice</option><option value="mentor">Mentor &ndash; someone who regularly guides my development</option><option value="sponsor">Sponsor &ndash; someone who actively advocates for me</option><option value="both">Both &ndash; I have a mentor and a sponsor</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-mentor" onchange="handleSkip('a-mentor')"><label for="skip-mentor">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-reputation">
    <span class="assess-label">Do you know what you are known for professionally?</span>
    <span class="assess-hint">If you're unsure, ask two or three colleagues what they see as your distinctive contribution.</span>
    <select id="a-reputation" onchange="handleAssessInput('a-reputation')"><option value="">Select...</option><option value="no-idea">No idea &ndash; I haven't asked or thought about it</option><option value="vague">Vague &ndash; a general sense but not specific</option><option value="one-thing">One thing &ndash; I know my main strength</option><option value="clear">Clear &ndash; I can articulate my professional brand</option><option value="deliberate">Deliberate &ndash; I've consciously built a specific reputation</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-reputation" onchange="handleSkip('a-reputation')"><label for="skip-reputation">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Security</h4>

<div class="assess-input-group" id="ig-runway">
    <span class="assess-label">How many months of expenses could you cover if you lost your income tomorrow?</span>
    <span class="assess-hint">Check your savings and liquid assets against your monthly expenses.</span>
    <select id="a-runway" onchange="handleAssessInput('a-runway')"><option value="">Select...</option><option value="zero">Zero &ndash; I'd be in trouble immediately</option><option value="one-to-two">One to two months</option><option value="three-to-five">Three to five months</option><option value="six-to-twelve">Six to twelve months</option><option value="over-twelve">Over twelve months</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-runway" onchange="handleSkip('a-runway')"><label for="skip-runway">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-transferable">
    <span class="assess-label">Can you name five skills you have that would be valuable in a different industry?</span>
    <span class="assess-hint">Think beyond technical skills &ndash; communication, project management, analysis, writing, leadership.</span>
    <select id="a-transferable" onchange="handleAssessInput('a-transferable')"><option value="">Select...</option><option value="no">No &ndash; my skills feel very role-specific</option><option value="one-or-two">One or two &ndash; I can think of a couple</option><option value="three-or-four">Three or four &ndash; several transferable skills</option><option value="five">Five &ndash; I can name them clearly</option><option value="more-than-five">More than five &ndash; I have a broad, portable skill set</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-transferable" onchange="handleSkip('a-transferable')"><label for="skip-transferable">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-cv-ready">
    <span class="assess-label">Is your CV up to date and ready to use?</span>
    <span class="assess-hint">Check when you last updated it. If it's more than 6 months old, it probably needs work.</span>
    <select id="a-cv-ready" onchange="handleAssessInput('a-cv-ready')"><option value="">Select...</option><option value="no-cv">No CV &ndash; I don't have one</option><option value="very-outdated">Very outdated &ndash; more than a year old</option><option value="somewhat-outdated">Somewhat outdated &ndash; 6 &ndash; 12 months old</option><option value="mostly-current">Mostly current &ndash; updated in the last 6 months</option><option value="ready">Ready &ndash; I could apply for a job this week</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-cv-ready" onchange="handleSkip('a-cv-ready')"><label for="skip-cv-ready">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Meaning</h4>

<div class="assess-input-group" id="ig-values-align">
    <span class="assess-label">Does your current role deliver the kind of meaning that matters to you?</span>
    <span class="assess-hint">Meaning can come from impact, learning, autonomy, community, or creative expression.</span>
    <select id="a-values-align" onchange="handleAssessInput('a-values-align')"><option value="">Select...</option><option value="not-at-all">Not at all &ndash; I feel disconnected from any purpose</option><option value="rarely">Rarely &ndash; occasional moments of meaning</option><option value="somewhat">Somewhat &ndash; some aspects are meaningful</option><option value="mostly">Mostly &ndash; my work generally aligns with what I care about</option><option value="deeply">Deeply &ndash; this role is a strong fit for my values</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-values-align" onchange="handleSkip('a-values-align')"><label for="skip-values-align">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-purpose">
    <span class="assess-label">Does your career contribute to something you genuinely care about?</span>
    <span class="assess-hint">This isn't about grand missions &ndash; even feeling that your work helps real people counts.</span>
    <select id="a-purpose" onchange="handleAssessInput('a-purpose')"><option value="">Select...</option><option value="no">No &ndash; I can't connect my work to anything I care about</option><option value="indirectly">Indirectly &ndash; there's a tenuous link if I squint</option><option value="somewhat">Somewhat &ndash; parts of it contribute to something meaningful</option><option value="mostly">Mostly &ndash; I can see a clear connection</option><option value="absolutely">Absolutely &ndash; my career is a direct expression of my values</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-purpose" onchange="handleSkip('a-purpose')"><label for="skip-purpose">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-tradeoffs">
    <span class="assess-label">What would you change about your career if money were not a constraint?</span>
    <span class="assess-hint">The gap between this answer and your current path reveals how much meaning you are trading away.</span>
    <select id="a-tradeoffs" onchange="handleAssessInput('a-tradeoffs')"><option value="">Select...</option><option value="everything">Everything &ndash; I'd pursue something completely different</option><option value="major-changes">Major changes &ndash; different field or role entirely</option><option value="some-changes">Some changes &ndash; same field but different focus or structure</option><option value="minor-tweaks">Minor tweaks &ndash; largely the same with small adjustments</option><option value="nothing">Nothing &ndash; I'm already doing what I'd choose to do</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-tradeoffs" onchange="handleSkip('a-tradeoffs')"><label for="skip-tradeoffs">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-clarity">
        <span class="assess-summary-label">Clarity</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-clarity" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-clarity">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-advancement">
        <span class="assess-summary-label">Advancement</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-advancement" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-advancement">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-security">
        <span class="assess-summary-label">Security</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-security" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-security">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-meaning">
        <span class="assess-summary-label">Meaning</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-meaning" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-meaning">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on career planning behaviour among adults. Items without reliable population benchmarks are not scored.</p>
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

<p>You now understand why career planning matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about clarity, advancement, security, and meaning. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/career-planning/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Career Planning Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Career Planning. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/career-planning/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'career-planning';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-direction', 'a-industry', 'a-written-plan',
        'a-skills-beyond', 'a-mentor', 'a-reputation',
        'a-runway', 'a-transferable', 'a-cv-ready',
        'a-values-align', 'a-purpose', 'a-tradeoffs'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: ~50% of workers view their job as "just a job";
    // only ~20% have a written career plan; ~37% have a mentor;
    // systematic skill development beyond current role is uncommon.
    var THRESHOLDS = {
        'a-direction': [
            // Most people lack a specific career direction; detailed 3-year plans are rare
            {v:'no-idea',p:10},{v:'vague',p:30},{v:'rough-direction',p:52},{v:'clear',p:75},{v:'detailed',p:93}
        ],
        'a-written-plan': [
            // ~80% have no written career plan; detailed structured plans are very rare
            {v:'no',p:15},{v:'mental-only',p:35},{v:'rough-notes',p:55},{v:'basic-plan',p:78},{v:'detailed-plan',p:95}
        ],
        'a-skills-beyond': [
            // Most professionals do not invest in skills beyond their current role
            {v:'no',p:12},{v:'thinking-about-it',p:30},{v:'dabbling',p:52},{v:'actively',p:75},{v:'systematically',p:93}
        ]
    };

    var VALUE_ITEMS = {
        clarity: ['a-direction', 'a-written-plan'],
        advancement: ['a-skills-beyond'],
        security: [],
        meaning: []
    };

    // Items without reliable population benchmarks
    var UNSCORED_ITEMS = [
        'a-industry', 'a-mentor', 'a-reputation',
        'a-runway', 'a-transferable', 'a-cv-ready',
        'a-values-align', 'a-purpose', 'a-tradeoffs'
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
        hintEl.textContent = pct !== null ? '~' + pct + 'th percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['clarity', 'advancement', 'security', 'meaning'].forEach(function(vk) {
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
        ['clarity', 'advancement', 'security', 'meaning'].forEach(function(vk) {
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
