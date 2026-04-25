---
layout: default
title: "Mental Health – Level 1: Awareness"
life_area_slug: mental-health
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

<h1>Mental Health: Level 1</h1>

<p class="l1-subtitle">Understand what mental health means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Mental Health Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why mental health matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Mental health shapes how you think, feel, and act in daily life. It influences your decision-making, your relationships, your physical health, and your capacity to handle stress. The effects are measurable and far-reaching.</p>

<p>Depression increases <a href="https://www.verywellmind.com/the-mental-and-physical-health-connection-7255857" target="_blank">cardiovascular disease risk by 20 &ndash; 40%</a>, whilst chronic physical conditions raise depression risk in turn. About <a href="https://www.cdc.gov/social-connectedness/risk-factors/index.html" target="_blank">1 in 3 adults</a> report feeling lonely, and loneliness is linked to increased risks of heart disease, stroke, and premature mortality.</p>

<p>The workplace effects are substantial: the <a href="https://www.who.int/teams/mental-health-and-substance-use/promotion-prevention/mental-health-in-the-workplace" target="_blank">WHO estimates</a> that 12 billion working days are lost annually to depression and anxiety, costing the global economy $1 trillion per year. And <a href="https://www.hhs.gov/surgeongeneral/reports-and-publications/workplace-well-being/index.html" target="_blank">76% of workers</a> report experiencing mental health symptoms, with 84% saying workplace conditions contributed.</p>

<p>The good news is that mental health responds to intervention. Evidence-based therapies, self-management practices, and lifestyle changes all produce measurable improvements &ndash; and many of the highest-impact approaches are accessible without specialist referral.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about mental health</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach mental health for different reasons. This site scores every mental health intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Professional Treatment & Support</h3>
<p>Working with qualified mental health professionals and building strong support networks. Therapy, counselling, medication when appropriate, and leveraging relationships for mental health support. People who lean towards this value focus on expert guidance and community-based approaches to mental wellness.</p>

<h3>Self-Management & Independence</h3>
<p>Developing personal skills and practices to manage your own mental health independently. Mindfulness, journalling, exercise, and other self-directed interventions that build internal capabilities. People who lean towards this value focus on self-reliance and building their own emotional toolkit.</p>

<h3>Integration & Holistic Approach</h3>
<p>Viewing mental health as interconnected with all other life areas and addressing it through lifestyle, relationships, purpose, and environment. People who lean towards this value see mental wellness as emerging from overall life balance and meaning, and would pursue it even if they had no specific symptoms to address.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each mental health value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Professional Treatment & Support &ndash; Level 5</div>
    <p><a href="https://www.stephenfry.com/" target="_blank">Stephen Fry</a> has spoken and written extensively about living with bipolar disorder over several decades, including periods of hospitalisation and suicidal ideation. He has maintained ongoing professional treatment throughout, and his documentary <em>The Secret Life of the Manic Depressive</em> documented his relationship with psychiatry in detail. He appears to use professional support as a sustained foundation for functioning at a high level across multiple careers.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Self-Management & Independence &ndash; Level 5</div>
    <p><a href="https://www.thetoolsbook.com/phil-stutz.html" target="_blank">Phil Stutz</a>, the psychotherapist featured in the Netflix documentary <em>Stutz</em>, has managed Parkinson's disease, chronic pain, and depression throughout his career using a structured set of self-directed practices he developed over decades. His approach centres on daily internal exercises &ndash; visualisation, body awareness, and emotional regulation routines &ndash; which he reportedly practises himself, making him an unusually visible example of a practitioner who lives his own methods.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Integration & Holistic Approach &ndash; Level 5</div>
    <p><a href="https://johannhari.com/" target="_blank">Johann Hari</a>, after researching and writing <em>Lost Connections</em>, restructured his own life around the social and environmental contributors to depression he had identified &ndash; changing his work patterns, investing in community, and redesigning his daily routines around connection and purpose. He has discussed publicly how these lifestyle changes, alongside professional treatment, produced more lasting improvements than medication alone had done for him.</p>
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

<div class="assess-group">
<h4>Professional Treatment &amp; Support</h4>

<div class="assess-input-group" id="ig-prof-access">
    <span class="assess-label">How easily could you access professional mental health support if you needed it?</span>
    <span class="assess-hint">GP referral, local counselling service, employee assistance programme, or a specific therapist.</span>
    <select id="a-prof-access" onchange="handleAssessInput('a-prof-access')">
        <option value="">Select&hellip;</option>
        <option value="no-idea">No idea &ndash; I wouldn't know where to start</option>
        <option value="vague">Vague sense &ndash; I could probably find something but haven't looked</option>
        <option value="one-option">I know at least one specific service I could contact</option>
        <option value="multiple">I know multiple options and have used at least one before</option>
    </select> <span class="assess-percentile-hint" id="pct-prof-access"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-prof-access" onchange="handleSkip('a-prof-access')"><label for="skip-prof-access">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-prof-history">
    <span class="assess-label">What is your history with professional mental health support?</span>
    <span class="assess-hint">All honest answers are useful here &ndash; there is no right or wrong history.</span>
    <select id="a-prof-history" onchange="handleAssessInput('a-prof-history')">
        <option value="">Select&hellip;</option>
        <option value="never">Never tried it</option>
        <option value="tried-once">Tried it once but didn't continue</option>
        <option value="past-use">Used it in the past and found it helpful</option>
        <option value="past-mixed">Used it in the past with mixed results</option>
        <option value="current">Currently receiving professional support</option>
    </select> <span class="assess-percentile-hint" id="pct-prof-history"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-prof-history" onchange="handleSkip('a-prof-history')"><label for="skip-prof-history">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-prof-network">
    <span class="assess-label">Do you have someone you trust enough to discuss mental health concerns with honestly?</span>
    <span class="assess-hint">A friend, partner, family member, or colleague &ndash; someone you would actually talk to, not just theoretically could.</span>
    <select id="a-prof-network" onchange="handleAssessInput('a-prof-network')">
        <option value="">Select&hellip;</option>
        <option value="no-one">No &ndash; nobody I'd feel comfortable talking to</option>
        <option value="maybe-one">Maybe &ndash; one person, but I'm not sure I'd actually do it</option>
        <option value="one">Yes &ndash; one person I trust and would talk to</option>
        <option value="several">Yes &ndash; several people I could turn to</option>
    </select> <span class="assess-percentile-hint" id="pct-prof-network"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-prof-network" onchange="handleSkip('a-prof-network')"><label for="skip-prof-network">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Self-Management &amp; Independence</h4>

<div class="assess-input-group" id="ig-self-triggers">
    <span class="assess-label">How many of your most common stress triggers can you name and describe your typical response to?</span>
    <span class="assess-hint">Work deadlines, conflict, financial pressure, loneliness &ndash; and whether you withdraw, ruminate, exercise, talk to someone, etc.</span>
    <select id="a-self-triggers" onchange="handleAssessInput('a-self-triggers')">
        <option value="">Select&hellip;</option>
        <option value="none">None &ndash; I haven't mapped my stress triggers</option>
        <option value="1">One &ndash; I know my biggest trigger</option>
        <option value="2-3">Two or three &ndash; I can describe triggers and responses</option>
        <option value="4+">Four or more &ndash; I've mapped this in detail</option>
    </select> <span class="assess-percentile-hint" id="pct-self-triggers"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-self-triggers" onchange="handleSkip('a-self-triggers')"><label for="skip-self-triggers">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-self-techniques">
    <span class="assess-label">Do you use any deliberate stress management techniques, and do they help?</span>
    <span class="assess-hint">Meditation, exercise, journalling, breathing exercises, talking it through &ndash; or nothing structured at all.</span>
    <select id="a-self-techniques" onchange="handleAssessInput('a-self-techniques')">
        <option value="">Select&hellip;</option>
        <option value="none">None &ndash; I don't use any structured techniques</option>
        <option value="some-unsure">Some &ndash; but I'm not sure if they help</option>
        <option value="some-helpful">Some &ndash; and they noticeably help</option>
        <option value="toolkit">A well-practised toolkit that I use regularly and reliably</option>
    </select> <span class="assess-percentile-hint" id="pct-self-techniques"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-self-techniques" onchange="handleSkip('a-self-techniques')"><label for="skip-self-techniques">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-self-emotions">
    <span class="assess-label">How precisely can you identify what you're feeling during a difficult moment?</span>
    <span class="assess-hint">Anxious, frustrated, overwhelmed, lonely, ashamed, bored &ndash; the ability to name emotions accurately is a core self-management skill.</span>
    <select id="a-self-emotions" onchange="handleAssessInput('a-self-emotions')">
        <option value="">Select&hellip;</option>
        <option value="generic">Generic only &ndash; "bad," "stressed," or "fine"</option>
        <option value="broad">Broad categories &ndash; I can tell angry from sad from anxious</option>
        <option value="specific">Specific &ndash; I can usually pinpoint the exact emotion</option>
        <option value="nuanced">Nuanced &ndash; I can identify layered or mixed emotions in the moment</option>
    </select> <span class="assess-percentile-hint" id="pct-self-emotions"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-self-emotions" onchange="handleSkip('a-self-emotions')"><label for="skip-self-emotions">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Integration &amp; Holistic Approach</h4>

<div class="assess-input-group" id="ig-int-sleep">
    <span class="assess-label">How clearly do you see the link between your sleep quality and your mood the next day?</span>
    <span class="assess-hint">Better after good sleep, worse after poor sleep, or genuinely unsure &ndash; all count as long as you've thought about it.</span>
    <select id="a-int-sleep" onchange="handleAssessInput('a-int-sleep')">
        <option value="">Select&hellip;</option>
        <option value="no-link">I haven't noticed a link</option>
        <option value="vague">Vague &ndash; I suspect sleep matters but haven't tracked it</option>
        <option value="clear">Clear &ndash; I can reliably predict my mood based on sleep</option>
        <option value="detailed">Detailed &ndash; I know how much sleep I need and what disrupts it</option>
    </select> <span class="assess-percentile-hint" id="pct-int-sleep"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-int-sleep" onchange="handleSkip('a-int-sleep')"><label for="skip-int-sleep">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-int-exercise">
    <span class="assess-label">Does regular exercise noticeably change how you feel mentally?</span>
    <span class="assess-hint">A 20-minute walk, a gym session, a run &ndash; or you've noticed no mental health effect from exercise. Either answer is useful.</span>
    <select id="a-int-exercise" onchange="handleAssessInput('a-int-exercise')">
        <option value="">Select&hellip;</option>
        <option value="no-effect">No noticeable effect</option>
        <option value="slight">Slight &ndash; I feel a bit better but it's subtle</option>
        <option value="noticeable">Noticeable &ndash; exercise clearly improves my mood</option>
        <option value="essential">Essential &ndash; my mental health deteriorates without it</option>
        <option value="unsure">Unsure &ndash; I haven't exercised enough to tell</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-int-exercise" onchange="handleSkip('a-int-exercise')"><label for="skip-int-exercise">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-int-social">
    <span class="assess-label">How well do you know which relationships or social situations improve your mental state and which drain it?</span>
    <span class="assess-hint">Specific people, group sizes, types of interaction &ndash; knowing your social energy patterns.</span>
    <select id="a-int-social" onchange="handleAssessInput('a-int-social')">
        <option value="">Select&hellip;</option>
        <option value="no-idea">No idea &ndash; I haven't thought about this</option>
        <option value="vague">Vague sense &ndash; some people drain me but I couldn't list who or why</option>
        <option value="partial">Partial &ndash; I know some specific people and situations</option>
        <option value="clear">Clear map &ndash; I know my social energy patterns well</option>
    </select> <span class="assess-percentile-hint" id="pct-int-social"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-int-social" onchange="handleSkip('a-int-social')"><label for="skip-int-social">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-professional">
        <span class="assess-summary-label">Professional Treatment &amp; Support</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-professional" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-professional">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-self_management">
        <span class="assess-summary-label">Self-Management &amp; Independence</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-self_management" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-self_management">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-integration">
        <span class="assess-summary-label">Integration &amp; Holistic Approach</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-integration" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-integration">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on mental health engagement among adults. Items without a clear ordinal scale are left unscored.</p>
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

<p>You now understand why mental health matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about professional support, self-management, and holistic integration. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/mental-health/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Mental Health Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Mental Health. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/mental-health/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'mental-health';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-prof-access', 'a-prof-history', 'a-prof-network',
        'a-self-triggers', 'a-self-techniques', 'a-self-emotions',
        'a-int-sleep', 'a-int-exercise', 'a-int-social'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: ~46% of UK adults with MH problems receive treatment (McManus et al., 2016),
    // ~25% use structured self-management techniques, ~20% have mapped stress triggers in detail.
    var THRESHOLDS = {
        'a-prof-access': [
            // ~40% wouldn't know where to start; knowing multiple options and having used one is uncommon
            {v:'no-idea',p:15},{v:'vague',p:40},{v:'one-option',p:65},{v:'multiple',p:88}
        ],
        'a-prof-history': [
            // ~54% of adults have never accessed MH support; current engagement is relatively uncommon
            {v:'never',p:20},{v:'tried-once',p:40},{v:'past-mixed',p:55},{v:'past-use',p:72},{v:'current',p:90}
        ],
        'a-prof-network': [
            // ~33% report having no one they'd discuss MH with; several trusted people is uncommon
            {v:'no-one',p:12},{v:'maybe-one',p:35},{v:'one',p:60},{v:'several',p:85}
        ],
        'a-self-triggers': [
            // Most people haven't systematically mapped their stress triggers
            {v:'none',p:15},{v:'1',p:40},{v:'2-3',p:65},{v:'4+',p:90}
        ],
        'a-self-techniques': [
            // ~25% use any structured stress management; a reliable toolkit is rare
            {v:'none',p:18},{v:'some-unsure',p:42},{v:'some-helpful',p:68},{v:'toolkit',p:92}
        ],
        'a-self-emotions': [
            // Most people use broad or generic labels; nuanced emotional granularity is uncommon
            {v:'generic',p:15},{v:'broad',p:40},{v:'specific',p:70},{v:'nuanced',p:92}
        ],
        'a-int-sleep': [
            // Most people have a vague sense; detailed self-knowledge of sleep-mood links is uncommon
            {v:'no-link',p:12},{v:'vague',p:38},{v:'clear',p:68},{v:'detailed',p:90}
        ],
        'a-int-social': [
            // Few people have mapped their social energy patterns in detail
            {v:'no-idea',p:12},{v:'vague',p:35},{v:'partial',p:62},{v:'clear',p:90}
        ]
    };

    var VALUE_ITEMS = {
        professional: ['a-prof-access', 'a-prof-history', 'a-prof-network'],
        self_management: ['a-self-triggers', 'a-self-techniques', 'a-self-emotions'],
        integration: ['a-int-sleep', 'a-int-social']
    };

    // Items without a clear ordinal scale (categorical choices)
    var UNSCORED_ITEMS = ['a-int-exercise'];

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
        if (UNSCORED_ITEMS.indexOf(itemId) !== -1) return null;
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return null;
        var el = document.getElementById(itemId);
        if (!el) return null;
        var val = el.value;
        if (val === '' || val === null) return null;
        if (!THRESHOLDS[itemId]) return null;
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
        ['professional', 'self_management', 'integration'].forEach(function(vk) {
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
        ['professional', 'self_management', 'integration'].forEach(function(vk) {
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
