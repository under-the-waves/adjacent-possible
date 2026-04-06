---
layout: default
title: "Relationship Status – Level 1: Awareness"
life_area_slug: relationship-status
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

<h1>Relationship Status: Level 1</h1>

<p class="l1-subtitle">Understand what relationship status means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Relationship Status Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why relationship status matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your relationship status &ndash; whether you are single, dating, or in a committed partnership &ndash; is one of the most consequential aspects of your life. But the quality of your decisions around it matters far more than the status itself.</p>

<p>A <a href="https://www.pnas.org/doi/10.1073/pnas.1917036117" target="_blank">machine-learning analysis</a> of 43 longitudinal couple studies (11,196 couples) found that relationship-specific perceptions at the outset &ndash; perceived commitment, appreciation, sexual satisfaction &ndash; predicted relationship quality far more than individual traits or partner characteristics. In other words, who you choose matters more than how hard you try to make it work afterwards.</p>

<p>At the same time, <a href="https://psycnet.apa.org/record/2013-36062-001" target="_blank">research on fear of being single</a> shows it consistently predicts settling for less responsive and less attractive partners, greater dependence in unsatisfying relationships, and lower selectivity during dating &ndash; even after controlling for attachment anxiety. Many people stay in relationships far longer than they should because leaving feels harder than staying.</p>

<p>And being single is not the deficit it is often assumed to be. <a href="https://journals.sagepub.com/doi/10.1177/02654075231197728" target="_blank">Comparative research</a> finds that singles and couples have overlapping ranges of happiness, and that the strongest predictors of life satisfaction for single people are the same as for everyone: strong friendships, high self-esteem, and low stress.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about relationship status</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach relationship status for different reasons. This site scores every relationship-status intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Partner Selection</h3>
<p>Choosing well: understanding what you genuinely need in a partner vs. what you think you want. Evaluating compatibility effectively, recognising red flags early, and avoiding common selection biases like prioritising excitement over stability. People who lean towards this value invest in self-knowledge and dating skills before committing.</p>

<h3>Meeting New Partners</h3>
<p>Actively creating opportunities to meet potential romantic partners rather than relying on chance. Expanding social circles, using dating platforms effectively, developing first-impression skills, and maintaining a steady pipeline of new connections. People who lean towards this value invest in the practical process of meeting compatible people rather than waiting for it to happen.</p>

<h3>Independence</h3>
<p>Being comfortable and fulfilled without a romantic partner. Building a rich single life, resisting social pressure to couple up, and knowing when being single is the right choice. People who lean towards this value ensure their happiness does not depend on relationship status.</p>

<h3>Transition Navigation</h3>
<p>Managing romantic transitions gracefully &ndash; entering relationships deliberately, leaving when needed, and processing breakups constructively. People who lean towards this value develop emotional resilience and decision-making skills around relationship changes, recovering quickly and extracting lessons rather than repeating patterns.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each relationship-status value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Partner Selection &ndash; Level 5</div>
    <p><a href="https://www.obamalibrary.gov/obamas/michelle-obama" target="_blank">Michelle Robinson</a> has spoken extensively about her deliberate approach to choosing a partner. When she met Barack Obama, she was his mentor at a law firm and initially resisted dating him. She assessed their compatibility across values, ambition, and family orientation over months before committing. In interviews and in her memoir <em>Becoming</em>, she describes evaluating whether he would be a genuine partner in domestic life and parenting &ndash; not just a charismatic match &ndash; and negotiating expectations before marriage. The result was a partnership that has weathered extraordinary public pressure for over 30 years.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Meeting New Partners &ndash; Level 5</div>
    <p><a href="https://amywebb.io/" target="_blank">Amy Webb</a>, a futurist and author, describes in her book <em>Data, a Love Story</em> how she reverse-engineered online dating after years of unsuccessful approaches. She created detailed profiles of who she was looking for, analysed what made profiles successful, systematically tested different approaches, and expanded her search beyond her usual social circles. The method was unconventional but effective &ndash; she met her husband through the optimised process and has been married since 2008. Her approach demonstrates what treating partner search as a skill to be refined, rather than a matter of luck, can achieve.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Independence &ndash; Level 5</div>
    <p><a href="https://dfranceschi.medium.com/" target="_blank">Diane Franceschi</a>, a retired NYPD detective, spent decades living alone by choice while building one of the most distinguished investigative careers in the department's history. She has spoken and written about constructing a rich life around deep friendships, professional purpose, and personal interests without treating singleness as a gap to fill. Her life demonstrates that relationship status can be fully decoupled from identity and fulfilment.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Transition Navigation &ndash; Level 5</div>
    <p><a href="https://terrycrews.com/" target="_blank">Terry Crews</a> and his wife Rebecca separated after he disclosed a pornography addiction that had damaged their marriage. Rather than letting the relationship end in acrimony or pretending nothing was wrong, Crews publicly took responsibility, entered intensive therapy, and the couple spent over a year in structured separation before reconciling. His account of that period &ndash; in his book <em>Manhood</em> and in interviews &ndash; describes navigating the transition with unusual emotional honesty, minimal blame, and genuine self-examination.</p>
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
<h4>Partner Selection</h4>

<div class="assess-input-group" id="ig-past-patterns">
    <span class="assess-label">How well can you identify your own partner-selection patterns?</span>
    <span class="assess-hint">Think about your last two or three relationships or significant interests. What drew you in?</span>
    <select id="a-past-patterns" onchange="handleAssessInput('a-past-patterns')">
        <option value="">Select...</option>
        <option value="no-awareness">No awareness &ndash; have not thought about my patterns</option>
        <option value="vague">Vague sense &ndash; can see some repeating themes but not clearly</option>
        <option value="partial">Partial &ndash; know what attracts me but unsure which choices led to good or poor outcomes</option>
        <option value="clear">Clear &ndash; can name my patterns and which ones served me well</option>
        <option value="detailed">Detailed &ndash; understand my patterns, their origins, and how to adjust</option>
    </select> <span class="assess-percentile-hint" id="pct-past-patterns"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-past-patterns" onchange="handleSkip('a-past-patterns')"><label for="skip-past-patterns">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-needs-vs-wants">
    <span class="assess-label">How well can you distinguish between what you need in a partner and what you find initially exciting?</span>
    <span class="assess-hint">For example, shared values vs. physical type, or emotional availability vs. social status.</span>
    <select id="a-needs-vs-wants" onchange="handleAssessInput('a-needs-vs-wants')">
        <option value="">Select...</option>
        <option value="no-distinction">No distinction &ndash; have not separated the two</option>
        <option value="starting">Starting to &ndash; beginning to notice the difference</option>
        <option value="moderate">Moderate &ndash; can list some genuine needs but still get pulled by excitement</option>
        <option value="clear">Clear &ndash; know my core needs and can separate them from surface attraction</option>
        <option value="tested">Tested &ndash; have applied this distinction in real decisions and it holds up</option>
    </select> <span class="assess-percentile-hint" id="pct-needs-vs-wants"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-needs-vs-wants" onchange="handleSkip('a-needs-vs-wants')"><label for="skip-needs-vs-wants">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-red-flags">
    <span class="assess-label">How well do you recognise red flags you have previously overlooked in partners?</span>
    <span class="assess-hint">Common ones include inconsistency, contempt, unwillingness to compromise, or misaligned life goals.</span>
    <select id="a-red-flags" onchange="handleAssessInput('a-red-flags')">
        <option value="">Select...</option>
        <option value="blind">Blind to them &ndash; tend to see the best in people regardless</option>
        <option value="retrospective">Retrospective only &ndash; recognise them after the fact</option>
        <option value="sometimes">Sometimes &ndash; spot some in the moment but miss others</option>
        <option value="usually">Usually &ndash; catch most red flags early</option>
        <option value="reliably">Reliably &ndash; can identify and act on red flags consistently</option>
    </select> <span class="assess-percentile-hint" id="pct-red-flags"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-red-flags" onchange="handleSkip('a-red-flags')"><label for="skip-red-flags">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Meeting New Partners</h4>

<div class="assess-input-group" id="ig-search-proactivity">
    <span class="assess-label">How active is your current approach to meeting potential partners?</span>
    <span class="assess-hint">Are you on dating apps, expanding your social circles, asking friends for introductions, or mainly hoping to meet someone organically?</span>
    <select id="a-search-proactivity" onchange="handleAssessInput('a-search-proactivity')">
        <option value="">Select...</option>
        <option value="passive">Passive &ndash; entirely relying on chance</option>
        <option value="single-channel">Single channel &ndash; one method (e.g. one dating app) without much effort</option>
        <option value="moderate">Moderate &ndash; a couple of methods with some consistency</option>
        <option value="active">Active &ndash; multiple deliberate methods used regularly</option>
        <option value="systematic">Systematic &ndash; structured approach across several channels with regular review</option>
    </select> <span class="assess-percentile-hint" id="pct-search-proactivity"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-search-proactivity" onchange="handleSkip('a-search-proactivity')"><label for="skip-search-proactivity">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-search-effectiveness">
    <span class="assess-label">Which of your methods for meeting people are actually generating compatible matches?</span>
    <span class="assess-hint">Think about where your best dates or connections have come from vs. where you spend the most time searching.</span>
    <select id="a-search-effectiveness" onchange="handleAssessInput('a-search-effectiveness')">
        <option value="">Select...</option>
        <option value="no-idea">No idea &ndash; have not tracked what works</option>
        <option value="nothing-works">Nothing working &ndash; no method is generating compatible matches</option>
        <option value="one-works">One works &ndash; one method produces decent results, others do not</option>
        <option value="several-work">Several work &ndash; a few methods reliably produce compatible matches</option>
        <option value="optimised">Optimised &ndash; know exactly which channels work and focus effort there</option>
    </select> <span class="assess-percentile-hint" id="pct-search-effectiveness"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-search-effectiveness" onchange="handleSkip('a-search-effectiveness')"><label for="skip-search-effectiveness">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-search-barriers">
    <span class="assess-label">What is your main barrier to meeting new partners?</span>
    <span class="assess-hint">Is it a volume problem (not meeting enough people), a conversion problem (meeting people but not generating interest), or an avoidance problem?</span>
    <select id="a-search-barriers" onchange="handleAssessInput('a-search-barriers')">
        <option value="">Select...</option>
        <option value="avoidance">Avoidance &ndash; I am not really trying</option>
        <option value="volume">Volume &ndash; not meeting enough new people</option>
        <option value="conversion">Conversion &ndash; meeting people but not generating mutual interest</option>
        <option value="selectivity">Selectivity &ndash; meeting people but few meet my standards</option>
        <option value="no-major-barrier">No major barrier &ndash; my search process is working reasonably well</option>
    </select> <span class="assess-percentile-hint" id="pct-search-barriers"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-search-barriers" onchange="handleSkip('a-search-barriers')"><label for="skip-search-barriers">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Independence</h4>

<div class="assess-input-group" id="ig-single-comfort">
    <span class="assess-label">How comfortable are you being single?</span>
    <span class="assess-hint">Consider whether you feel pressure from yourself, family, or society to be in a relationship.</span>
    <select id="a-single-comfort" onchange="handleAssessInput('a-single-comfort')">
        <option value="">Select...</option>
        <option value="very-uncomfortable">Very uncomfortable &ndash; being single feels like a serious problem</option>
        <option value="uncomfortable">Uncomfortable &ndash; strong internal or external pressure to couple up</option>
        <option value="mixed">Mixed &ndash; some discomfort but managing</option>
        <option value="comfortable">Comfortable &ndash; genuinely fine being single</option>
        <option value="thriving">Thriving &ndash; single life feels like a deliberate, fulfilling choice</option>
    </select> <span class="assess-percentile-hint" id="pct-single-comfort"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-single-comfort" onchange="handleSkip('a-single-comfort')"><label for="skip-single-comfort">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-solo-fulfilment">
    <span class="assess-label">How fulfilling is your daily life independently of your relationship status?</span>
    <span class="assess-hint">Would your life feel meaningfully emptier without a partner, or roughly the same?</span>
    <select id="a-solo-fulfilment" onchange="handleAssessInput('a-solo-fulfilment')">
        <option value="">Select...</option>
        <option value="empty">Empty &ndash; life feels hollow without a partner</option>
        <option value="lacking">Lacking &ndash; noticeably less fulfilling when single</option>
        <option value="adequate">Adequate &ndash; fine but could be better</option>
        <option value="fulfilling">Fulfilling &ndash; rich friendships, hobbies, and purpose regardless of status</option>
        <option value="deeply-fulfilling">Deeply fulfilling &ndash; a partner would add to an already complete life</option>
    </select> <span class="assess-percentile-hint" id="pct-solo-fulfilment"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-solo-fulfilment" onchange="handleSkip('a-solo-fulfilment')"><label for="skip-solo-fulfilment">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-fear-single">
    <span class="assess-label">How much does fear of being alone drive your relationship decisions?</span>
    <span class="assess-hint">Have you ever stayed in or entered a relationship primarily because being single felt worse?</span>
    <select id="a-fear-single" onchange="handleAssessInput('a-fear-single')">
        <option value="">Select...</option>
        <option value="primary-driver">Primary driver &ndash; fear of being alone is my main motivation</option>
        <option value="significant">Significant &ndash; has kept me in relationships I should have left</option>
        <option value="some-influence">Some influence &ndash; aware it plays a role but not the main factor</option>
        <option value="minor">Minor &ndash; rarely affects my decisions</option>
        <option value="not-a-factor">Not a factor &ndash; my decisions are based on genuine desire and compatibility</option>
    </select> <span class="assess-percentile-hint" id="pct-fear-single"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-fear-single" onchange="handleSkip('a-fear-single')"><label for="skip-fear-single">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Transition Navigation</h4>

<div class="assess-input-group" id="ig-breakup-speed">
    <span class="assess-label">How long do you typically stay in a relationship after recognising it is not working?</span>
    <span class="assess-hint">Weeks, months, or years? Some people leave quickly; others stay for years past the point of knowing.</span>
    <select id="a-breakup-speed" onchange="handleAssessInput('a-breakup-speed')">
        <option value="">Select...</option>
        <option value="years">Years &ndash; tend to stay long past the point of knowing</option>
        <option value="many-months">Many months &ndash; take a long time to act on what I know</option>
        <option value="few-months">A few months &ndash; some delay but eventually act</option>
        <option value="weeks">Weeks &ndash; act fairly quickly once I am sure</option>
        <option value="promptly">Promptly &ndash; address it as soon as the pattern is clear</option>
    </select> <span class="assess-percentile-hint" id="pct-breakup-speed"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-breakup-speed" onchange="handleSkip('a-breakup-speed')"><label for="skip-breakup-speed">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-recovery-time">
    <span class="assess-label">How long does it typically take you to recover emotionally from a breakup?</span>
    <span class="assess-hint">Research suggests most people return to baseline within about three months, but individual variation is large.</span>
    <select id="a-recovery-time" onchange="handleAssessInput('a-recovery-time')">
        <option value="">Select...</option>
        <option value="over-a-year">Over a year &ndash; takes a very long time to move on</option>
        <option value="6-12-months">6 &ndash; 12 months &ndash; a significant recovery period</option>
        <option value="3-6-months">3 &ndash; 6 months &ndash; roughly average</option>
        <option value="1-3-months">1 &ndash; 3 months &ndash; recover relatively quickly</option>
        <option value="under-a-month">Under a month &ndash; bounce back fast</option>
    </select> <span class="assess-percentile-hint" id="pct-recovery-time"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-recovery-time" onchange="handleSkip('a-recovery-time')"><label for="skip-recovery-time">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-transition-patterns">
    <span class="assess-label">What is your typical post-breakup pattern?</span>
    <span class="assess-hint">Think about your last significant breakup. What did you actually do in the weeks that followed?</span>
    <select id="a-transition-patterns" onchange="handleAssessInput('a-transition-patterns')">
        <option value="">Select...</option>
        <option value="rumination">Rumination &ndash; replay events and struggle to let go</option>
        <option value="rebound">Rebound &ndash; jump into a new relationship quickly</option>
        <option value="avoidance">Avoidance &ndash; suppress feelings and distract myself</option>
        <option value="mixed-processing">Mixed processing &ndash; some constructive reflection alongside difficult patches</option>
        <option value="constructive">Constructive &ndash; process emotions, extract lessons, and move forward deliberately</option>
    </select> <span class="assess-percentile-hint" id="pct-transition-patterns"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-transition-patterns" onchange="handleSkip('a-transition-patterns')"><label for="skip-transition-patterns">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-partnerSelection">
        <span class="assess-summary-label">Partner Selection</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-partnerSelection" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-partnerSelection">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-meetingPartners">
        <span class="assess-summary-label">Meeting Partners</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-meetingPartners" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-meetingPartners">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-independence">
        <span class="assess-summary-label">Independence</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-independence" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-independence">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-transitionNavigation">
        <span class="assess-summary-label">Transition Navigation</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-transitionNavigation" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-transitionNavigation">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published research on dating behaviour, relationship transitions, and single-life satisfaction among adults. All items in this area are scored.</p>
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

<p>You now understand why relationship status matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about partner selection, independence, and transition navigation. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/relationship-status/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Relationship Status Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Relationship Status. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/relationship-status/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'relationship-status';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-past-patterns', 'a-needs-vs-wants', 'a-red-flags',
        'a-search-proactivity', 'a-search-effectiveness', 'a-search-barriers',
        'a-single-comfort', 'a-solo-fulfilment', 'a-fear-single',
        'a-breakup-speed', 'a-recovery-time', 'a-transition-patterns'
    ];

    var UNSCORED_ITEMS = [];

    var THRESHOLDS = {
        'a-past-patterns': [
            {v:'no-awareness',p:8},{v:'vague',p:25},{v:'partial',p:50},{v:'clear',p:78},{v:'detailed',p:95}
        ],
        'a-needs-vs-wants': [
            {v:'no-distinction',p:8},{v:'starting',p:28},{v:'moderate',p:50},{v:'clear',p:78},{v:'tested',p:95}
        ],
        'a-red-flags': [
            {v:'blind',p:8},{v:'retrospective',p:28},{v:'sometimes',p:50},{v:'usually',p:78},{v:'reliably',p:95}
        ],
        'a-search-proactivity': [
            {v:'passive',p:10},{v:'single-channel',p:30},{v:'moderate',p:52},{v:'active',p:78},{v:'systematic',p:95}
        ],
        'a-search-effectiveness': [
            {v:'no-idea',p:10},{v:'nothing-works',p:20},{v:'one-works',p:45},{v:'several-work',p:75},{v:'optimised',p:95}
        ],
        'a-search-barriers': [
            {v:'avoidance',p:8},{v:'volume',p:28},{v:'conversion',p:48},{v:'selectivity',p:68},{v:'no-major-barrier',p:90}
        ],
        'a-single-comfort': [
            {v:'very-uncomfortable',p:8},{v:'uncomfortable',p:25},{v:'mixed',p:48},{v:'comfortable',p:72},{v:'thriving',p:93}
        ],
        'a-solo-fulfilment': [
            {v:'empty',p:8},{v:'lacking',p:25},{v:'adequate',p:48},{v:'fulfilling',p:75},{v:'deeply-fulfilling',p:95}
        ],
        'a-fear-single': [
            {v:'primary-driver',p:8},{v:'significant',p:25},{v:'some-influence',p:48},{v:'minor',p:72},{v:'not-a-factor',p:93}
        ],
        'a-breakup-speed': [
            {v:'years',p:8},{v:'many-months',p:25},{v:'few-months',p:50},{v:'weeks',p:78},{v:'promptly',p:95}
        ],
        'a-recovery-time': [
            {v:'over-a-year',p:10},{v:'6-12-months',p:30},{v:'3-6-months',p:50},{v:'1-3-months',p:75},{v:'under-a-month',p:93}
        ],
        'a-transition-patterns': [
            {v:'rumination',p:10},{v:'rebound',p:20},{v:'avoidance',p:30},{v:'mixed-processing',p:55},{v:'constructive',p:90}
        ],
    };

    var VALUE_ITEMS = {
        partnerSelection: ['a-past-patterns', 'a-needs-vs-wants', 'a-red-flags'],
        meetingPartners: ['a-search-proactivity', 'a-search-effectiveness', 'a-search-barriers'],
        independence: ['a-single-comfort', 'a-solo-fulfilment', 'a-fear-single'],
        transitionNavigation: ['a-breakup-speed', 'a-recovery-time', 'a-transition-patterns'],
    };

    // --- Scoring functions ---

    function interpolatePercentile(value, thresholds) {
        for (var i = 0; i < thresholds.length; i++) {
            if (thresholds[i].v === String(value)) return thresholds[i].p;
        }
        return null;
    }

    function getItemPercentile(itemId) {
        if (UNSCORED_ITEMS.indexOf(itemId) !== -1) return null;
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
        ['partnerSelection', 'meetingPartners', 'independence', 'transitionNavigation'].forEach(function(vk) {
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

    function updateAssessRecorded() {
        var allAnswered = ASSESS_IDS.every(function(id) { return isItemAnswered(id); });
        var recorded = document.getElementById('assessRecorded');
        if (recorded) recorded.classList.toggle('visible', allAnswered);
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
        ['partnerSelection', 'meetingPartners', 'independence', 'transitionNavigation'].forEach(function(vk) {
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
