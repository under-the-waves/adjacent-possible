---
layout: default
title: "Personality – Level 1: Awareness"
life_area_slug: personality
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

<h1>Personality: Level 1</h1>

<p class="l1-subtitle">Understand what personality means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Personality Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why personality matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your personality shapes nearly every interaction you have – how you approach work, navigate relationships, handle stress, and make decisions. Understanding and intentionally developing your personality is one of the most foundational investments you can make.</p>

<p>Research on personality–environment fit shows that people who choose careers, relationships, and lifestyles aligned with their traits report <a href="https://psycnet.apa.org/record/2005-07426-005" target="_blank">significantly higher life satisfaction</a> and effectiveness. Getting this alignment wrong leads to chronic friction that accumulates across years.</p>

<p>Personality is also more malleable than most people assume. A <a href="https://www.pnas.org/doi/10.1073/pnas.2017548118" target="_blank">2021 meta-analysis</a> found that targeted personality interventions produce meaningful changes, with effect sizes of 0.34 – 0.73 across different traits. People can and do become more emotionally stable, more conscientious, more socially confident, and more open to experience through deliberate practice.</p>

<p>Few other investments touch as many areas of life simultaneously. Your personality influences how you exercise, eat, sleep, communicate, manage money, build relationships, and pursue goals. Small shifts in core traits ripple outward across all of these domains.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about personality</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach personality development for different reasons. This site scores every personality intervention across two core values. Later, you'll set your own weighting across these two values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Personality Alignment</h3>
<p>Working with your natural personality patterns rather than against them. Understanding your Big Five trait profile, attachment style, cognitive preferences, and motivational patterns, then designing your life, environment, career choices, and daily approaches to leverage your psychological makeup. People who lean towards this value focus on choosing situations that naturally suit their traits and building systems that work with their psychological nature.</p>

<h3>Personality Growth</h3>
<p>Actively working to develop and modify your personality characteristics beyond your baseline tendencies. Deliberately building confidence, emotional stability, social effectiveness, conscientiousness, openness, or other traits through targeted interventions and sustained practice. People who lean towards this value focus on expanding their psychological capabilities and pushing beyond their comfort zones, even when change does not come naturally.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each personality value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Personality Alignment &ndash; Level 5</div>
    <p><a href="https://gretchenrubin.com/about/" target="_blank">Gretchen Rubin</a> spent years systematically studying how personality tendencies shape habits, happiness, and daily life. She developed the Four Tendencies framework from this research and restructured her career, relationships, and routines around her findings. Her work demonstrates what it looks like to build an entire life architecture around deep personality self-knowledge.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Personality Growth &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Eleanor_Roosevelt" target="_blank">Eleanor Roosevelt</a> was by her own account painfully shy and insecure as a young woman. Over several decades she deliberately pushed herself into public speaking, political advocacy, and diplomatic work, eventually becoming one of the most prominent public figures of the 20th century. She chaired the UN committee that drafted the Universal Declaration of Human Rights and maintained a syndicated newspaper column for 27 years. Her transformation from a reserved, self-doubting young woman into a confident global leader appears to have been largely intentional.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to look up or reflect on.</p>

<div class="assess-group">
<h4>Personality Alignment</h4>

<div class="assess-input-group" id="ig-big-five">
    <span class="assess-label">Have you completed a Big Five personality assessment?</span>
    <span class="assess-hint">Free options include the IPIP-NEO or the Big Five Inventory. Look for openness, conscientiousness, extraversion, agreeableness, and neuroticism scores.</span>
    <select id="a-big-five" onchange="handleAssessInput('a-big-five')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I have never taken one</option>
        <option value="vaguely">Vaguely &ndash; I took one years ago but do not remember the results</option>
        <option value="informal">Informal &ndash; I have a rough sense from a quick online quiz</option>
        <option value="yes">Yes &ndash; I know my approximate trait profile</option>
        <option value="detailed">Yes &ndash; I have detailed results I can refer to</option>
    </select> <span class="assess-percentile-hint" id="pct-big-five"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-big-five" onchange="handleSkip('a-big-five')"><label for="skip-big-five">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-attachment">
    <span class="assess-label">How well do you understand your attachment style in close relationships?</span>
    <span class="assess-hint">Secure, anxious, avoidant, or disorganised. You can take a short online questionnaire or reflect on recurring relationship patterns.</span>
    <select id="a-attachment" onchange="handleAssessInput('a-attachment')">
        <option value="">Select...</option>
        <option value="unaware">Unaware &ndash; I have not thought about this</option>
        <option value="vague">Vague &ndash; I have heard the terms but am not sure which applies</option>
        <option value="approximate">Approximate &ndash; I have a general sense of my pattern</option>
        <option value="clear">Clear &ndash; I know my attachment style and can see it in my relationships</option>
    </select> <span class="assess-percentile-hint" id="pct-attachment"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-attachment" onchange="handleSkip('a-attachment')"><label for="skip-attachment">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-fit">
    <span class="assess-label">How well does your current life fit your personality?</span>
    <span class="assess-hint">Think about work, relationships, and living situation. Do you feel energised or drained by your daily routines?</span>
    <select id="a-fit" onchange="handleAssessInput('a-fit')">
        <option value="">Select...</option>
        <option value="poor">Poor &ndash; most of my daily life works against my natural tendencies</option>
        <option value="mixed">Mixed &ndash; some areas suit me, others do not</option>
        <option value="mostly-good">Mostly good &ndash; my life generally fits my personality</option>
        <option value="excellent">Excellent &ndash; I have deliberately built my life around my traits</option>
    </select> <span class="assess-percentile-hint" id="pct-fit"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-fit" onchange="handleSkip('a-fit')"><label for="skip-fit">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Personality Growth</h4>

<div class="assess-input-group" id="ig-strength">
    <span class="assess-label">How many personality traits can you name that help you in daily life?</span>
    <span class="assess-hint">These might be things like emotional resilience, curiosity, discipline, warmth, or adaptability.</span>
    <select id="a-strength" onchange="handleAssessInput('a-strength')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I have not thought about my strengths in these terms</option>
        <option value="one">One &ndash; I can name one but struggle with more</option>
        <option value="two-three">Two or three &ndash; I have a reasonable sense of my strengths</option>
        <option value="many">Several &ndash; I know my personality strengths well</option>
    </select> <span class="assess-percentile-hint" id="pct-strength"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-strength" onchange="handleSkip('a-strength')"><label for="skip-strength">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-limitation">
    <span class="assess-label">How many personality traits can you name that hinder you or create recurring problems?</span>
    <span class="assess-hint">For example, conflict avoidance, impulsiveness, rigidity, social anxiety, or low frustration tolerance.</span>
    <select id="a-limitation" onchange="handleAssessInput('a-limitation')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I have not thought about my limitations in these terms</option>
        <option value="one">One &ndash; I can name one but struggle with more</option>
        <option value="two-three">Two or three &ndash; I have a reasonable sense of my limitations</option>
        <option value="many">Several &ndash; I know my personality limitations well</option>
    </select> <span class="assess-percentile-hint" id="pct-limitation"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-limitation" onchange="handleSkip('a-limitation')"><label for="skip-limitation">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-change">
    <span class="assess-label">Have you thought about whether to work with your current traits or actively try to change them?</span>
    <span class="assess-hint">There is no right answer. Some traits are worth adapting around; others are worth developing. The key is having considered the question.</span>
    <select id="a-change" onchange="handleAssessInput('a-change')">
        <option value="">Select...</option>
        <option value="not-considered">Not considered &ndash; I have not thought about this</option>
        <option value="vaguely">Vaguely &ndash; I have thought about it in passing</option>
        <option value="considered">Considered &ndash; I have a view on which traits to accept and which to develop</option>
        <option value="actively-working">Actively working on it &ndash; I am deliberately trying to change specific traits</option>
    </select> <span class="assess-percentile-hint" id="pct-change"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-change" onchange="handleSkip('a-change')"><label for="skip-change">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-alignment">
        <span class="assess-summary-label">Personality Alignment</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-alignment" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-alignment">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-growth">
        <span class="assess-summary-label">Personality Growth</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-growth" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-growth">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published data on personality assessment uptake, self-knowledge, and personal development practices. All items in this area are scored.</p>
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

<p>You now understand why personality matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about personality alignment and personality growth. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/personality/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Personality Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Personality. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/personality/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'personality';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-big-five', 'a-attachment', 'a-fit',
        'a-strength', 'a-limitation', 'a-change'
    ];

    var THRESHOLDS = {
        'a-big-five': [
            // ~75% have never taken a Big Five assessment; detailed results is ~8%
            {v:'no',p:12},{v:'vaguely',p:30},{v:'informal',p:50},{v:'yes',p:75},{v:'detailed',p:93}
        ],
        'a-attachment': [
            // ~65% are unaware of their attachment style; clear understanding is ~15%
            {v:'unaware',p:12},{v:'vague',p:35},{v:'approximate',p:62},{v:'clear',p:90}
        ],
        'a-fit': [
            // ~30% report poor personality-life fit; deliberately built life around traits is ~10%
            {v:'poor',p:12},{v:'mixed',p:38},{v:'mostly-good',p:68},{v:'excellent',p:93}
        ],
        'a-strength': [
            // ~40% cannot name any personality strengths; knowing several well is ~20%
            {v:'none',p:12},{v:'one',p:35},{v:'two-three',p:62},{v:'many',p:90}
        ],
        'a-limitation': [
            // ~50% have not thought about personality limitations; knowing several is ~18%
            {v:'none',p:12},{v:'one',p:35},{v:'two-three',p:65},{v:'many',p:92}
        ],
        'a-change': [
            // ~55% have not considered whether to adapt or change traits; actively working is ~12%
            {v:'not-considered',p:12},{v:'vaguely',p:35},{v:'considered',p:65},{v:'actively-working',p:92}
        ]
    };

    var VALUE_ITEMS = {
        alignment: ['a-big-five', 'a-attachment', 'a-fit'],
        growth: ['a-strength', 'a-limitation', 'a-change']
    };

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
        hintEl.textContent = pct !== null ? '~' + pct + 'th percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['alignment', 'growth'].forEach(function(vk) {
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
        ['alignment', 'growth'].forEach(function(vk) {
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
