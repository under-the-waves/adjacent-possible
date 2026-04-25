---
layout: default
title: "Self-Awareness – Level 1: Awareness"
life_area_slug: self-awareness
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

<h1>Self-Awareness: Level 1</h1>

<p class="l1-subtitle">Understand what self-awareness means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Self-Awareness Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why self-awareness matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Self-awareness &ndash; the ability to see yourself clearly, understand your emotions and motivations, and recognise how others experience you &ndash; is one of the strongest predictors of personal and professional effectiveness. Yet most people significantly overestimate how well they know themselves.</p>

<p>Organisational psychologist <a href="https://hbr.org/2018/01/what-self-awareness-really-is-and-how-to-cultivate-it" target="_blank">Tasha Eurich's research</a> found that while 95% of people believe they are self-aware, only about 10 &ndash; 15% meet the criteria when tested. This gap between perceived and actual self-knowledge affects decision-making, relationships, and emotional regulation in ways that are difficult to detect from the inside.</p>

<p>People with higher self-awareness tend to be <a href="https://doi.org/10.1016/j.leaqua.2010.03.009" target="_blank">more effective leaders</a>, form stronger relationships, and experience greater psychological wellbeing. They are also better at recognising their own biases, which leads to more accurate judgements in both personal and professional contexts.</p>

<p>Self-awareness has two distinct components: internal self-awareness (understanding your own values, reactions, and impact on others) and external self-awareness (understanding how other people actually perceive you). People who score high on one do not necessarily score high on the other, which means developing both requires different approaches.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about self-awareness</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People develop self-awareness through different approaches. This site scores every self-awareness intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Psychological</h3>
<p>Understanding yourself through analysis of mental patterns, triggers, and unconscious processes. People who lean towards this value tend to explore their emotional reactions, examine recurring thought patterns, and seek to understand why they respond to situations the way they do. This might involve therapy, journalling, personality assessments, or studying psychology.</p>

<h3>Contemplative/Somatic</h3>
<p>Awareness through meditation, mindfulness, body sensations, and embodied presence. People who lean towards this value develop the ability to observe their moment-to-moment experience without judgement. They tend to notice physical signals &ndash; tension, fatigue, gut feelings &ndash; as sources of self-knowledge, and may practise sitting meditation, body scanning, or breathwork.</p>

<h3>Relational</h3>
<p>Understanding yourself through social feedback, interpersonal patterns, and how you show up with others. People who lean towards this value recognise that other people often see things about them that they cannot see themselves. They actively seek honest feedback, pay attention to recurring dynamics in their relationships, and use interactions as a mirror.</p>

<h3>Experiential</h3>
<p>Self-discovery through trying new experiences, challenges, and active personal development. People who lean towards this value learn about themselves by doing &ndash; taking on unfamiliar situations, travelling, changing roles, or pushing personal boundaries. They treat life as a series of experiments that reveal who they are.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each self-awareness value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Psychological &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Carl_Jung" target="_blank">Carl Jung</a> pioneered analytical psychology and the concept of individuation &ndash; a lifelong process of integrating conscious and unconscious aspects of the psyche. He spent decades systematically analysing his own dreams, fantasies, and emotional reactions, documenting the process in his <em>Red Book</em>. His personal self-exploration became the foundation for widely used frameworks including psychological types and the concept of the shadow.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Contemplative/Somatic &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Thich_Nhat_Hanh" target="_blank">Thich Nhat Hanh</a> was a Vietnamese Zen Buddhist monk who maintained a daily mindfulness practice for over 60 years. He developed the concept of "engaged Buddhism", applying contemplative awareness to social action, and founded the Plum Village monastic community in France. His teaching emphasised awareness of breathing, walking, and ordinary daily activities as a path to deep self-knowledge.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Relational &ndash; Level 5</div>
    <p><a href="https://brenebrown.com/" target="_blank">Bren&eacute; Brown</a> has described in detail how her own research into vulnerability forced a personal reckoning &ndash; she sought therapy, confronted her patterns of emotional armour, and began deliberately practising the vulnerability she studied. Her 2010 TED talk, one of the most viewed of all time, was itself an act of public relational exposure. She appears to actively solicit feedback from colleagues, family, and audiences about how she comes across, and has spoken openly about the gap between how she sees herself and how others experience her.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Experiential &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Viktor_Frankl" target="_blank">Viktor Frankl</a> was an Austrian psychiatrist who survived three years in Nazi concentration camps, including Auschwitz. He drew on this direct experience of extreme suffering to develop logotherapy, a therapeutic approach built on the idea that meaning can be found in any circumstances. His book <em>Man's Search for Meaning</em> documented how lived experience &ndash; including the most harrowing kind &ndash; can become a source of profound self-understanding.</p>
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

<div class="assess-group">
<h4>Psychological</h4>

<div class="assess-input-group" id="ig-triggers">
    <span class="assess-label">How many situations can you name that reliably trigger a strong emotional reaction in you?</span>
    <span class="assess-hint">Think about recurring patterns at work, in relationships, or in daily life &ndash; anger, anxiety, defensiveness.</span>
    <select id="a-triggers" onchange="handleAssessInput('a-triggers')">
        <option value="">Select&hellip;</option>
        <option value="0">None &ndash; I haven't identified any</option>
        <option value="1">One &ndash; I know one clear trigger</option>
        <option value="2-3">Two or three &ndash; I can name a few</option>
        <option value="4+">Four or more &ndash; I've mapped my triggers in detail</option>
    </select> <span class="assess-percentile-hint" id="pct-triggers"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-triggers" onchange="handleSkip('a-triggers')"><label for="skip-triggers">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-coping">
    <span class="assess-label">What is your default coping mechanism when you are stressed?</span>
    <span class="assess-hint">Consider what you tend to do automatically, not what you think you should do.</span>
    <select id="a-coping" onchange="handleAssessInput('a-coping')">
        <option value="">Select&hellip;</option>
        <option value="avoidance">Avoidance or procrastination</option>
        <option value="overwork">Over-working or staying busy</option>
        <option value="withdrawal">Withdrawal or isolation</option>
        <option value="rumination">Rumination or overthinking</option>
        <option value="healthy">Healthy strategies (exercise, talking, journalling)</option>
        <option value="unsure">I'm not sure what I do</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-coping" onchange="handleSkip('a-coping')"><label for="skip-coping">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-values-conflict">
    <span class="assess-label">How often do your actions conflict with your stated values?</span>
    <span class="assess-hint">The gap between what we say we value and what we actually do is one of the most useful things to notice.</span>
    <select id="a-values-conflict" onchange="handleAssessInput('a-values-conflict')">
        <option value="">Select&hellip;</option>
        <option value="frequently">Frequently &ndash; most weeks</option>
        <option value="sometimes">Sometimes &ndash; a few times a month</option>
        <option value="rarely">Rarely &ndash; I can think of occasional examples</option>
        <option value="almost-never">Almost never &ndash; my actions and values are well aligned</option>
        <option value="unsure">I haven't thought about this before</option>
    </select> <span class="assess-percentile-hint" id="pct-values-conflict"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-values-conflict" onchange="handleSkip('a-values-conflict')"><label for="skip-values-conflict">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Contemplative/Somatic</h4>

<div class="assess-input-group" id="ig-body-signals">
    <span class="assess-label">How well can you identify where in your body you feel stress or anxiety?</span>
    <span class="assess-hint">Pause for a moment and scan from head to toe. Notice what's there right now.</span>
    <select id="a-body-signals" onchange="handleAssessInput('a-body-signals')">
        <option value="">Select&hellip;</option>
        <option value="no-awareness">I don't notice any physical sensations linked to stress</option>
        <option value="vague">I get a vague sense but can't pinpoint locations</option>
        <option value="one-area">I know one area (e.g. shoulders, stomach, jaw)</option>
        <option value="multiple">I can identify several specific areas and what each signals</option>
    </select> <span class="assess-percentile-hint" id="pct-body-signals"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-body-signals" onchange="handleSkip('a-body-signals')"><label for="skip-body-signals">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-attention">
    <span class="assess-label">How long can you sustain focused attention on a single task before your mind wanders?</span>
    <span class="assess-hint">Think about reading, working, or listening. Even a rough estimate counts.</span>
    <select id="a-attention" onchange="handleAssessInput('a-attention')">
        <option value="">Select&hellip;</option>
        <option value="under-5">Under 5 minutes</option>
        <option value="5-15">5 &ndash; 15 minutes</option>
        <option value="15-30">15 &ndash; 30 minutes</option>
        <option value="30-60">30 &ndash; 60 minutes</option>
        <option value="60+">More than an hour</option>
    </select> <span class="assess-percentile-hint" id="pct-attention"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-attention" onchange="handleSkip('a-attention')"><label for="skip-attention">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-meditation">
    <span class="assess-label">Do you have a meditation or mindfulness practice?</span>
    <span class="assess-hint">This includes formal meditation, breathing exercises, or any deliberate present-moment awareness practice.</span>
    <select id="a-meditation" onchange="handleAssessInput('a-meditation')">
        <option value="">Select&hellip;</option>
        <option value="none">No practice at all</option>
        <option value="occasional">Occasional &ndash; a few times a month or less</option>
        <option value="regular">Regular &ndash; a few times a week</option>
        <option value="daily">Daily or near-daily practice</option>
    </select> <span class="assess-percentile-hint" id="pct-meditation"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-meditation" onchange="handleSkip('a-meditation')"><label for="skip-meditation">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Relational</h4>

<div class="assess-input-group" id="ig-feedback">
    <span class="assess-label">When did someone last give you honest, critical feedback?</span>
    <span class="assess-hint">If you can't remember any, that itself is useful information.</span>
    <select id="a-feedback" onchange="handleAssessInput('a-feedback')">
        <option value="">Select&hellip;</option>
        <option value="never">I can't recall ever receiving honest critical feedback</option>
        <option value="over-year">More than a year ago</option>
        <option value="past-year">Within the past year</option>
        <option value="past-month">Within the past month</option>
        <option value="regularly">I receive it regularly</option>
    </select> <span class="assess-percentile-hint" id="pct-feedback"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-feedback" onchange="handleSkip('a-feedback')"><label for="skip-feedback">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-perception">
    <span class="assess-label">How well do you know how others perceive your strengths and weaknesses?</span>
    <span class="assess-hint">If you're unsure, consider asking someone you trust.</span>
    <select id="a-perception" onchange="handleAssessInput('a-perception')">
        <option value="">Select&hellip;</option>
        <option value="no-idea">No idea &ndash; I've never asked or thought about it</option>
        <option value="vague">Vague sense &ndash; I could guess but I'm not confident</option>
        <option value="partial">Partial &ndash; I know what a few people think</option>
        <option value="clear">Clear picture &ndash; I've had direct conversations about this</option>
    </select> <span class="assess-percentile-hint" id="pct-perception"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-perception" onchange="handleSkip('a-perception')"><label for="skip-perception">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-conflict">
    <span class="assess-label">What is your typical pattern in conflict?</span>
    <span class="assess-hint">Think about the last two or three disagreements you were involved in.</span>
    <select id="a-conflict" onchange="handleAssessInput('a-conflict')">
        <option value="">Select&hellip;</option>
        <option value="avoid">I tend to avoid or sidestep conflict</option>
        <option value="accommodate">I become overly accommodating or give in</option>
        <option value="go-quiet">I go quiet or shut down</option>
        <option value="escalate">I escalate or become defensive</option>
        <option value="engage">I engage directly and try to resolve it</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-conflict" onchange="handleSkip('a-conflict')"><label for="skip-conflict">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Experiential</h4>

<div class="assess-input-group" id="ig-comfort-zone">
    <span class="assess-label">When were you last outside your comfort zone?</span>
    <span class="assess-hint">This could be a new job, a difficult conversation, travel, or any unfamiliar challenge.</span>
    <select id="a-comfort-zone" onchange="handleAssessInput('a-comfort-zone')">
        <option value="">Select&hellip;</option>
        <option value="cant-recall">I can't recall a recent example</option>
        <option value="over-year">More than a year ago</option>
        <option value="past-year">Within the past year</option>
        <option value="past-month">Within the past month</option>
        <option value="currently">I'm outside my comfort zone right now</option>
    </select> <span class="assess-percentile-hint" id="pct-comfort-zone"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-comfort-zone" onchange="handleSkip('a-comfort-zone')"><label for="skip-comfort-zone">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-change">
    <span class="assess-label">How much has your self-understanding changed in the past five years?</span>
    <span class="assess-hint">Something you once believed about yourself that you no longer think is true, or vice versa.</span>
    <select id="a-change" onchange="handleAssessInput('a-change')">
        <option value="">Select&hellip;</option>
        <option value="unchanged">Largely unchanged &ndash; I see myself the same way</option>
        <option value="minor">Minor shifts &ndash; small adjustments to my self-image</option>
        <option value="significant">Significant change &ndash; I've revised a core belief about myself</option>
        <option value="major">Major transformation &ndash; I see myself very differently now</option>
    </select> <span class="assess-percentile-hint" id="pct-change"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-change" onchange="handleSkip('a-change')"><label for="skip-change">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-experiment">
    <span class="assess-label">Can you name something you haven't tried that you suspect would teach you about yourself?</span>
    <span class="assess-hint">A new skill, a different social context, solo travel, a creative pursuit &ndash; anything unfamiliar.</span>
    <select id="a-experiment" onchange="handleAssessInput('a-experiment')">
        <option value="">Select&hellip;</option>
        <option value="nothing">Nothing comes to mind</option>
        <option value="vague-idea">I have a vague idea but haven't articulated it</option>
        <option value="specific">I can name something specific</option>
        <option value="several">I have several ideas I'd like to try</option>
    </select> <span class="assess-percentile-hint" id="pct-experiment"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-experiment" onchange="handleSkip('a-experiment')"><label for="skip-experiment">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-psychological">
        <span class="assess-summary-label">Psychological</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-psychological" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-psychological">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-contemplative">
        <span class="assess-summary-label">Contemplative/Somatic</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-contemplative" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-contemplative">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-relational">
        <span class="assess-summary-label">Relational</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-relational" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-relational">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-experiential">
        <span class="assess-summary-label">Experiential</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-experiential" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-experiential">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published data on self-knowledge, mindfulness practice, feedback-seeking behaviour, and personal growth. Unscored items (coping style, conflict pattern) are excluded because they describe style rather than level.</p>
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

<p>You now understand why self-awareness matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about psychological understanding, contemplative awareness, relational feedback, and experiential learning. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/self-awareness/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Self-Awareness Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Self-Awareness. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/self-awareness/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'self-awareness';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-triggers', 'a-coping', 'a-values-conflict',
        'a-body-signals', 'a-attention', 'a-meditation',
        'a-feedback', 'a-perception', 'a-conflict',
        'a-comfort-zone', 'a-change', 'a-experiment'
    ];

    var THRESHOLDS = {
        'a-triggers': [
            // ~55% haven't identified any emotional triggers; detailed mapping is ~10%
            {v:'0',p:12},{v:'1',p:35},{v:'2-3',p:65},{v:'4+',p:93}
        ],
        'a-values-conflict': [
            // ~30% notice frequent conflicts; well-aligned is ~15%
            {v:'frequently',p:10},{v:'sometimes',p:35},{v:'rarely',p:65},{v:'almost-never',p:92}
        ],
        'a-body-signals': [
            // ~40% have no body-stress awareness; identifying multiple specific areas is ~12%
            {v:'no-awareness',p:10},{v:'vague',p:32},{v:'one-area',p:60},{v:'multiple',p:92}
        ],
        'a-attention': [
            // Average sustained attention is ~8-12 minutes; 60+ minutes is ~10%
            {v:'under-5',p:8},{v:'5-15',p:30},{v:'15-30',p:55},{v:'30-60',p:78},{v:'60+',p:95}
        ],
        'a-meditation': [
            // ~85% have no meditation practice; daily practice is ~5%
            {v:'none',p:12},{v:'occasional',p:45},{v:'regular',p:78},{v:'daily',p:97}
        ],
        'a-feedback': [
            // ~40% can't recall receiving honest critical feedback; regular receipt is ~10%
            {v:'never',p:8},{v:'over-year',p:25},{v:'past-year',p:50},{v:'past-month',p:78},{v:'regularly',p:95}
        ],
        'a-perception': [
            // ~35% have no idea how others perceive them; clear picture from direct conversations is ~15%
            {v:'no-idea',p:10},{v:'vague',p:32},{v:'partial',p:60},{v:'clear',p:92}
        ],
        'a-comfort-zone': [
            // ~30% can't recall a recent example; currently outside comfort zone is ~15%
            {v:'cant-recall',p:8},{v:'over-year',p:25},{v:'past-year',p:50},{v:'past-month',p:78},{v:'currently',p:95}
        ],
        'a-change': [
            // ~25% report largely unchanged self-understanding; major transformation is ~12%
            {v:'unchanged',p:10},{v:'minor',p:35},{v:'significant',p:68},{v:'major',p:93}
        ],
        'a-experiment': [
            // ~30% can't think of anything; having several ideas is ~18%
            {v:'nothing',p:10},{v:'vague-idea',p:35},{v:'specific',p:65},{v:'several',p:92}
        ]
    };

    var VALUE_ITEMS = {
        psychological: ['a-triggers', 'a-values-conflict'],
        contemplative: ['a-body-signals', 'a-attention', 'a-meditation'],
        relational: ['a-feedback', 'a-perception'],
        experiential: ['a-comfort-zone', 'a-change', 'a-experiment']
    };

    var UNSCORED_ITEMS = ['a-coping', 'a-conflict'];

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
        hintEl.textContent = pct !== null ? 'roughly ' + ordinalSuffix(Math.round(pct / 10) * 10) + ' percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['psychological', 'contemplative', 'relational', 'experiential'].forEach(function(vk) {
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
        ['psychological', 'contemplative', 'relational', 'experiential'].forEach(function(vk) {
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
