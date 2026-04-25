---
layout: default
title: "Communication – Level 1: Awareness"
life_area_slug: communication
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

<h1>Communication: Level 1</h1>

<p class="l1-subtitle">Understand what communication means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Communication Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why communication matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Communication is the medium through which almost everything in your life happens. Every relationship, every collaboration, every negotiation, and every conflict runs on it. Improving how you communicate has an unusually broad impact because it touches so many domains at once.</p>

<p>The evidence for its importance is consistent across contexts. Employers rank communication as the <a href="https://www.naceweb.org/talent-acquisition/candidate-selection/key-attributes-employers-want-to-see-on-students-resumes/" target="_blank">most sought-after skill</a> in job candidates across industries. People with strong interpersonal skills experience <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4968942/" target="_blank">less loneliness</a> and build deeper social networks. An estimated <a href="https://haiilo.com/blog/top-internal-communication-statistics/" target="_blank">86% of workplace failures</a> are attributed to poor communication or collaboration.</p>

<p>Communication is also unusually trainable. Unlike personality traits, which are relatively stable, specific communication skills – listening, structuring arguments, managing conflict, reading a room – respond well to deliberate practice. Small improvements compound quickly because you use these skills dozens of times a day.</p>

<p>Roughly 75% of people experience public speaking anxiety, and fewer than 5% communicate assertively in everyday situations. This means that even moderate competence puts you well above the median.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about communication</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People develop their communication for different reasons. This site scores every communication intervention across four core values. Later, you'll set your own weighting across these values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Influence</h3>
<p>The ability to persuade others, drive decisions, and create change through your communication. People who lean towards this value focus on strategic messaging, understanding what motivates different audiences, and developing the credibility and presence needed to shape outcomes.</p>

<h3>Connection</h3>
<p>Building genuine relationships, emotional intimacy, and mutual understanding through communication. People who lean towards this value focus on listening deeply, sharing vulnerably, and creating the emotional safety that allows relationships to flourish over time.</p>

<h3>Performance</h3>
<p>Excelling in high-stakes or formal communication situations – public speaking, presentations, job interviews, media appearances. People who lean towards this value develop skills specifically for moments when communication performance directly impacts important outcomes.</p>

<h3>Conflict Navigation</h3>
<p>Handling disagreements, difficult conversations, and interpersonal tensions constructively while maintaining relationships. People who lean towards this value become comfortable with necessary tension and develop frameworks for working through differences without damaging bonds.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each communication value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Influence &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/William_Ury" target="_blank">William Ury</a> co-founded the Harvard Program on Negotiation and co-authored <em>Getting to Yes</em>, one of the most widely read books on negotiation. He has mediated conflicts between corporations, governments, and ethnic groups on five continents, and his frameworks for principled negotiation have shaped how millions of people approach persuasion and deal-making.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Connection &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Terry_Gross" target="_blank">Terry Gross</a> has hosted <em>Fresh Air</em> on NPR since 1975, conducting thousands of interviews across nearly five decades. She is widely regarded as one of the most skilled interviewers alive – guests routinely disclose things to her they have never shared publicly, citing her deep listening and genuine curiosity as the reason.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Performance &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Hans_Rosling" target="_blank">Hans Rosling</a> was a Swedish physician and statistician whose TED talks have been viewed over 35 million times. He used animated data visualisations and physical props to make global health statistics compelling and memorable. His presentations consistently changed audience beliefs about world poverty and development &ndash; measurably, as he tested audiences before and after. He maintained this level of public communication for over a decade until his death in 2017.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Conflict Navigation &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/George_J._Mitchell" target="_blank">George Mitchell</a> chaired the Northern Ireland peace negotiations that produced the 1998 Good Friday Agreement, ending three decades of sectarian violence. Participants on all sides credited his patience, impartiality, and skill at finding common ground in situations where others saw none. He later served as US special envoy for Middle East peace.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to reflect on.</p>

<div class="assess-group">
<h4>Influence</h4>

<div class="assess-input-group" id="ig-persuade">
    <span class="assess-label">How often do your attempts to persuade someone actually work?</span>
    <span class="assess-hint">Think about meetings, negotiations, requests, or arguments where you wanted someone to change their mind or take action.</span>
    <select id="a-persuade" onchange="handleAssessInput('a-persuade')">
        <option value="">Select...</option>
        <option value="rarely">Rarely &ndash; most attempts fall flat</option>
        <option value="sometimes">Sometimes &ndash; it works when conditions are right</option>
        <option value="often">Often &ndash; I can usually bring people round</option>
        <option value="consistently">Consistently &ndash; persuasion is a strength of mine</option>
    </select> <span class="assess-percentile-hint" id="pct-persuade"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-persuade" onchange="handleSkip('a-persuade')"><label for="skip-persuade">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-ideas-adopted">
    <span class="assess-label">How often are your ideas adopted in group discussions?</span>
    <span class="assess-hint">Do people generally act on your suggestions, or do your points tend to get talked over?</span>
    <select id="a-ideas-adopted" onchange="handleAssessInput('a-ideas-adopted')">
        <option value="">Select...</option>
        <option value="rarely">Rarely &ndash; my points tend to get overlooked</option>
        <option value="sometimes">Sometimes &ndash; depends on the group and the topic</option>
        <option value="often">Often &ndash; people usually take my suggestions seriously</option>
        <option value="consistently">Consistently &ndash; I regularly shape group decisions</option>
    </select> <span class="assess-percentile-hint" id="pct-ideas-adopted"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-ideas-adopted" onchange="handleSkip('a-ideas-adopted')"><label for="skip-ideas-adopted">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-audience">
    <span class="assess-label">How much do you adjust your communication depending on who you are talking to?</span>
    <span class="assess-hint">Do you speak differently to your manager, your friends, and a stranger? Or roughly the same way?</span>
    <select id="a-audience" onchange="handleAssessInput('a-audience')">
        <option value="">Select...</option>
        <option value="not-at-all">Not at all &ndash; I communicate the same way with everyone</option>
        <option value="slightly">Slightly &ndash; minor adjustments in formality</option>
        <option value="moderately">Moderately &ndash; I adapt tone and detail for different audiences</option>
        <option value="significantly">Significantly &ndash; I consciously tailor my approach each time</option>
    </select> <span class="assess-percentile-hint" id="pct-audience"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-audience" onchange="handleSkip('a-audience')"><label for="skip-audience">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Connection</h4>

<div class="assess-input-group" id="ig-deep-conv">
    <span class="assess-label">How often do you have conversations that go beyond small talk in a typical week?</span>
    <span class="assess-hint">Conversations where you discuss something personal, meaningful, or emotionally honest.</span>
    <select id="a-deep-conv" onchange="handleAssessInput('a-deep-conv')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; my conversations stay surface-level</option>
        <option value="rarely">Rarely &ndash; maybe once a fortnight</option>
        <option value="weekly">A few times a week</option>
        <option value="daily">Most days &ndash; deep conversation is a regular part of my life</option>
    </select> <span class="assess-percentile-hint" id="pct-deep-conv"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-deep-conv" onchange="handleSkip('a-deep-conv')"><label for="skip-deep-conv">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-listening">
    <span class="assess-label">How would you rate your listening skills?</span>
    <span class="assess-hint">Do people seek you out to talk through problems? Do you remember details from past conversations?</span>
    <select id="a-listening" onchange="handleAssessInput('a-listening')">
        <option value="">Select...</option>
        <option value="poor">Poor &ndash; I often zone out or wait for my turn to speak</option>
        <option value="average">Average &ndash; I listen but sometimes miss the point</option>
        <option value="good">Good &ndash; people generally feel heard when talking to me</option>
        <option value="excellent">Excellent &ndash; people regularly seek me out because I listen well</option>
    </select> <span class="assess-percentile-hint" id="pct-listening"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-listening" onchange="handleSkip('a-listening')"><label for="skip-listening">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-vulnerable">
    <span class="assess-label">How comfortable are you sharing personal feelings or admitting uncertainty?</span>
    <span class="assess-hint">Can you say "I don't know" or "I'm struggling with this" to people you trust?</span>
    <select id="a-vulnerable" onchange="handleAssessInput('a-vulnerable')">
        <option value="">Select...</option>
        <option value="very-uncomfortable">Very uncomfortable &ndash; I almost never share personal feelings</option>
        <option value="uncomfortable">Uncomfortable &ndash; I can manage it but it feels forced</option>
        <option value="somewhat-comfortable">Somewhat comfortable &ndash; with close friends, yes</option>
        <option value="comfortable">Comfortable &ndash; I can be open with most people I trust</option>
        <option value="very-comfortable">Very comfortable &ndash; vulnerability comes naturally to me</option>
    </select> <span class="assess-percentile-hint" id="pct-vulnerable"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-vulnerable" onchange="handleSkip('a-vulnerable')"><label for="skip-vulnerable">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Performance</h4>

<div class="assess-input-group" id="ig-public-speaking">
    <span class="assess-label">How comfortable are you speaking in front of a group?</span>
    <span class="assess-hint">Could you give a five-minute presentation to 10 people tomorrow? Would anxiety interfere?</span>
    <select id="a-public-speaking" onchange="handleAssessInput('a-public-speaking')">
        <option value="">Select...</option>
        <option value="avoidant">Avoidant &ndash; I would do almost anything to get out of it</option>
        <option value="anxious">Anxious &ndash; I could do it but would be very nervous</option>
        <option value="manageable">Manageable &ndash; some nerves but I can get through it</option>
        <option value="comfortable">Comfortable &ndash; I feel fairly at ease presenting</option>
        <option value="confident">Confident &ndash; I enjoy public speaking</option>
    </select> <span class="assess-percentile-hint" id="pct-public-speaking"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-public-speaking" onchange="handleSkip('a-public-speaking')"><label for="skip-public-speaking">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-writing">
    <span class="assess-label">How clearly do you write when it matters?</span>
    <span class="assess-hint">Emails, reports, or messages to people you do not know well. Do people ask you to clarify, or do they usually understand first time?</span>
    <select id="a-writing" onchange="handleAssessInput('a-writing')">
        <option value="">Select...</option>
        <option value="unclear">Unclear &ndash; people regularly misunderstand or ask for clarification</option>
        <option value="passable">Passable &ndash; gets the point across but not always cleanly</option>
        <option value="clear">Clear &ndash; people usually understand first time</option>
        <option value="strong">Strong &ndash; I write well and receive positive feedback</option>
        <option value="excellent">Excellent &ndash; writing is one of my strongest communication skills</option>
    </select> <span class="assess-percentile-hint" id="pct-writing"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-writing" onchange="handleSkip('a-writing')"><label for="skip-writing">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Conflict Navigation</h4>

<div class="assess-input-group" id="ig-conflict-pattern">
    <span class="assess-label">What is your default response to difficult conversations?</span>
    <span class="assess-hint">Think about the last time you disagreed with someone. Did you raise it, let it go, or escalate?</span>
    <select id="a-conflict-pattern" onchange="handleAssessInput('a-conflict-pattern')">
        <option value="">Select...</option>
        <option value="avoid">Avoid &ndash; I almost always let things go rather than raise them</option>
        <option value="passive">Passive &ndash; I hint at the problem but rarely address it directly</option>
        <option value="mixed">Mixed &ndash; sometimes I raise it, sometimes I let it go</option>
        <option value="direct">Direct &ndash; I usually raise issues calmly and clearly</option>
        <option value="aggressive">Aggressive &ndash; I tend to confront or escalate</option>
    </select> <span class="assess-percentile-hint" id="pct-conflict-pattern"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-conflict-pattern" onchange="handleSkip('a-conflict-pattern')"><label for="skip-conflict-pattern">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-apologise">
    <span class="assess-label">How easy do you find it to apologise when you are wrong?</span>
    <span class="assess-hint">Can you say "I was wrong about that" without it feeling like a threat to your identity?</span>
    <select id="a-apologise" onchange="handleAssessInput('a-apologise')">
        <option value="">Select...</option>
        <option value="very-hard">Very hard &ndash; I almost never apologise</option>
        <option value="hard">Hard &ndash; I can do it but it takes a lot of effort</option>
        <option value="moderate">Moderate &ndash; it depends on the situation</option>
        <option value="easy">Easy &ndash; I can apologise without much difficulty</option>
        <option value="natural">Natural &ndash; apologising when I am wrong comes easily</option>
    </select> <span class="assess-percentile-hint" id="pct-apologise"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-apologise" onchange="handleSkip('a-apologise')"><label for="skip-apologise">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-influence">
        <span class="assess-summary-label">Influence</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-influence" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-influence">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-connection">
        <span class="assess-summary-label">Connection</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-connection" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-connection">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-performance">
        <span class="assess-summary-label">Performance</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-performance" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-performance">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-conflict">
        <span class="assess-summary-label">Conflict Navigation</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-conflict" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-conflict">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on communication behaviours among adults. All items in this area are scored.</p>
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

<p>You now understand why communication matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about influence, connection, performance, and conflict navigation. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/communication/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Communication Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Communication. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/communication/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'communication';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-persuade', 'a-ideas-adopted', 'a-audience',
        'a-deep-conv', 'a-listening', 'a-vulnerable',
        'a-public-speaking', 'a-writing',
        'a-conflict-pattern', 'a-apologise'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: ~75% have public speaking anxiety, <5% communicate
    // assertively, most people rarely adjust communication style for audience.
    var THRESHOLDS = {
        'a-persuade': [
            // Most people are ineffective persuaders; consistent success is rare
            {v:'rarely',p:15},{v:'sometimes',p:40},{v:'often',p:70},{v:'consistently',p:92}
        ],
        'a-ideas-adopted': [
            // Most people's ideas get overlooked in groups; consistently shaping decisions is rare
            {v:'rarely',p:15},{v:'sometimes',p:40},{v:'often',p:70},{v:'consistently',p:92}
        ],
        'a-audience': [
            // Most people communicate roughly the same way regardless of audience
            {v:'not-at-all',p:10},{v:'slightly',p:35},{v:'moderately',p:62},{v:'significantly',p:90}
        ],
        'a-deep-conv': [
            // Most conversations stay surface-level; daily deep conversation is rare
            {v:'never',p:10},{v:'rarely',p:30},{v:'weekly',p:62},{v:'daily',p:90}
        ],
        'a-listening': [
            // Most people self-rate as average listeners; being sought out for listening is uncommon
            {v:'poor',p:10},{v:'average',p:35},{v:'good',p:65},{v:'excellent',p:92}
        ],
        'a-vulnerable': [
            // Most people are uncomfortable with vulnerability; it coming naturally is rare
            {v:'very-uncomfortable',p:10},{v:'uncomfortable',p:25},{v:'somewhat-comfortable',p:50},{v:'comfortable',p:75},{v:'very-comfortable',p:93}
        ],
        'a-public-speaking': [
            // ~75% have public speaking anxiety; enjoying it is uncommon
            {v:'avoidant',p:10},{v:'anxious',p:30},{v:'manageable',p:55},{v:'comfortable',p:78},{v:'confident',p:95}
        ],
        'a-writing': [
            // Most people's writing is passable; strong or excellent is uncommon
            {v:'unclear',p:10},{v:'passable',p:30},{v:'clear',p:55},{v:'strong',p:78},{v:'excellent',p:95}
        ],
        'a-conflict-pattern': [
            // Most people avoid or are passive; direct calm addressing is uncommon
            // Note: 'aggressive' is not better than 'direct' -- it maps lower
            {v:'avoid',p:10},{v:'passive',p:25},{v:'mixed',p:45},{v:'direct',p:85},{v:'aggressive',p:20}
        ],
        'a-apologise': [
            // Most people find apologising hard; it coming naturally is rare
            {v:'very-hard',p:10},{v:'hard',p:25},{v:'moderate',p:50},{v:'easy',p:75},{v:'natural',p:93}
        ]
    };

    var VALUE_ITEMS = {
        influence: ['a-persuade', 'a-ideas-adopted', 'a-audience'],
        connection: ['a-deep-conv', 'a-listening', 'a-vulnerable'],
        performance: ['a-public-speaking', 'a-writing'],
        conflict: ['a-conflict-pattern', 'a-apologise']
    };

    // All communication items are scorable
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
        // All communication items use string keys (dropdowns)
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
        hintEl.textContent = pct !== null ? 'roughly ' + ordinalSuffix(Math.round(pct / 10) * 10) + ' percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['influence', 'connection', 'performance', 'conflict'].forEach(function(vk) {
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
        ['influence', 'connection', 'performance', 'conflict'].forEach(function(vk) {
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
