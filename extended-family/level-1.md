---
layout: default
title: "Extended Family – Level 1: Awareness"
life_area_slug: extended-family
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

<h1>Extended Family: Level 1</h1>

<p class="l1-subtitle">Understand what extended family means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Extended Family Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why extended family matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Extended family relationships &ndash; grandparents, aunts, uncles, cousins, in-laws &ndash; are among the longest-lasting connections most people have. Unlike friendships, they typically span generations and persist across geographic moves, career changes, and life transitions.</p>

<p>Research consistently shows that better family relationships are associated with <a href="https://www.sciencedirect.com/science/article/pii/S2212657017301204" target="_blank">reduced psychological distress, greater life satisfaction, and stronger resilience</a>. Close relationships with extended family specifically decrease symptoms of anxiety and depression.</p>

<p>Yet geographic mobility has made sustained contact harder. <a href="https://www.pewresearch.org/short-reads/2022/05/18/more-than-half-of-americans-live-within-an-hour-of-extended-family/" target="_blank">Pew Research (2022)</a> found that while 55% of adults live within an hour of some extended family, 20% live near none at all &ndash; and those with higher education are least likely to live close. The quality of family ties, not merely their existence, predicts wellbeing benefits across the lifespan.</p>

<p>Extended family also provides practical support networks &ndash; childcare, eldercare, financial help in emergencies &ndash; that are difficult to replicate through other relationships. Losing these connections often means losing a safety net that took generations to build.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about extended family</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People invest in extended family for different reasons. This site scores every extended family intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Harmony</h3>
<p>Maintaining peaceful, low-conflict relationships across the extended family. Navigating differences respectfully, managing family tensions proactively, finding common ground, and ensuring family gatherings are pleasant rather than stressful. People who prioritise this value invest in diplomacy and conflict prevention.</p>

<h3>Closeness</h3>
<p>Maintaining emotionally meaningful relationships with extended family across geographic and generational boundaries. Regular contact, shared experiences, genuine conversations, and investing time in relationships that might otherwise atrophy. People who prioritise this value actively seek deeper involvement with their extended family.</p>

<h3>Balance</h3>
<p>Maintaining healthy boundaries with extended family so these relationships enhance rather than constrain your life. The ability to set limits without guilt, make decisions independently, and ensure family obligations remain sustainable. People who prioritise this value protect their autonomy while staying connected.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each extended family value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Harmony &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Desmond_Tutu" target="_blank">Desmond Tutu</a> built his life around reconciliation &ndash; first within South Africa's fractured communities and consistently within his own large, multi-generational family. He and his wife Leah maintained warm relationships across an extended network of children, grandchildren, and in-laws spanning multiple countries and decades, navigating political, cultural, and generational differences without fracturing family cohesion.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Closeness &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Dolly_Parton" target="_blank">Dolly Parton</a> grew up as one of twelve children in rural Tennessee and has maintained close, emotionally substantive relationships across her extended family of dozens of nieces, nephews, and their children throughout a six-decade career. She funded the Imagination Library partly to connect with family literacy needs, employs several relatives, and consistently describes her extended family as her primary source of meaning.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Balance &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Michelle_Obama" target="_blank">Michelle Obama</a> has written and spoken extensively about maintaining close ties with her extended family on Chicago's South Side while setting clear boundaries around her own family's needs &ndash; first during her legal career, then through eight years in the White House. She managed to stay deeply connected to her roots without allowing family expectations to override her personal and professional decisions.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to think through.</p>

<div class="assess-group">
<h4>Harmony</h4>

<div class="assess-input-group" id="ig-conflict-map">
    <span class="assess-label">How many extended family relationships are currently strained or a source of tension?</span>
    <span class="assess-hint">Think about unresolved disagreements, people who avoid each other, or topics that reliably cause arguments.</span>
    <select id="a-conflict-map" onchange="handleAssessInput('a-conflict-map')">
        <option value="">Select...</option>
        <option value="many">Many &ndash; there are several ongoing tensions or feuds</option>
        <option value="a-few">A few &ndash; two or three relationships are strained</option>
        <option value="one">One &ndash; there is one main source of tension</option>
        <option value="none">None &ndash; my extended family relationships are largely peaceful</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-conflict-map" onchange="handleSkip('a-conflict-map')"><label for="skip-conflict-map">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-gatherings">
    <span class="assess-label">How do you find extended family gatherings?</span>
    <span class="assess-hint">Consider holidays, weddings, funerals, and other family events over the past few years.</span>
    <select id="a-gatherings" onchange="handleAssessInput('a-gatherings')">
        <option value="">Select...</option>
        <option value="stressful">Stressful &ndash; I dread them or find them exhausting</option>
        <option value="mixed">Mixed &ndash; some are fine, others are difficult</option>
        <option value="neutral">Neutral &ndash; neither particularly enjoyable nor stressful</option>
        <option value="pleasant">Pleasant &ndash; I generally enjoy them</option>
        <option value="very-pleasant">Very pleasant &ndash; I look forward to them</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-gatherings" onchange="handleSkip('a-gatherings')"><label for="skip-gatherings">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-navigate">
    <span class="assess-label">How well do you handle disagreements with extended family?</span>
    <span class="assess-hint">Do you tend to avoid conflict, escalate it, or navigate it constructively?</span>
    <select id="a-navigate" onchange="handleAssessInput('a-navigate')">
        <option value="">Select...</option>
        <option value="avoid">Avoid &ndash; I stay silent or withdraw rather than engage</option>
        <option value="escalate">Escalate &ndash; disagreements tend to become arguments</option>
        <option value="clumsy">Clumsy &ndash; I try to address things but it often goes badly</option>
        <option value="reasonable">Reasonable &ndash; I can usually navigate disagreements without damage</option>
        <option value="skilled">Skilled &ndash; I handle family tensions constructively and calmly</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-navigate" onchange="handleSkip('a-navigate')"><label for="skip-navigate">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Closeness</h4>

<div class="assess-input-group" id="ig-contact-freq">
    <span class="assess-label">How often do you have meaningful contact with extended family members?</span>
    <span class="assess-hint">Count conversations that go beyond logistics &ndash; genuine exchanges about each other's lives, feelings, or experiences.</span>
    <select id="a-contact-freq" onchange="handleAssessInput('a-contact-freq')">
        <option value="">Select...</option>
        <option value="rarely">Rarely &ndash; a few times a year at most</option>
        <option value="occasionally">Occasionally &ndash; every couple of months</option>
        <option value="monthly">Monthly &ndash; roughly once a month</option>
        <option value="fortnightly">Fortnightly &ndash; every couple of weeks</option>
        <option value="weekly">Weekly or more &ndash; regular meaningful contact</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-contact-freq" onchange="handleSkip('a-contact-freq')"><label for="skip-contact-freq">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-depth">
    <span class="assess-label">How many extended family relationships have genuine emotional depth?</span>
    <span class="assess-hint">Who would you call in a crisis? Who really knows what is going on in your life?</span>
    <select id="a-depth" onchange="handleAssessInput('a-depth')">
        <option value="">Select...</option>
        <option value="none">None &ndash; all my extended family relationships are surface-level</option>
        <option value="one">One &ndash; there is one person I am genuinely close to</option>
        <option value="a-few">A few &ndash; two or three relationships have real depth</option>
        <option value="several">Several &ndash; I have meaningful connections across my extended family</option>
        <option value="many">Many &ndash; I am emotionally close to most of my extended family</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-depth" onchange="handleSkip('a-depth')"><label for="skip-depth">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-generations">
    <span class="assess-label">Do you have meaningful relationships across different generations of your extended family?</span>
    <span class="assess-hint">Grandparents, older aunts and uncles, younger cousins, nieces and nephews &ndash; or only your own generation.</span>
    <select id="a-generations" onchange="handleAssessInput('a-generations')">
        <option value="">Select...</option>
        <option value="own-only">Own generation only &ndash; I mainly connect with cousins my age</option>
        <option value="one-other">One other generation &ndash; I am close to older or younger relatives, but not both</option>
        <option value="some-across">Some across generations &ndash; I have a few connections in different age groups</option>
        <option value="strong-across">Strong across generations &ndash; I have meaningful relationships spanning multiple generations</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-generations" onchange="handleSkip('a-generations')"><label for="skip-generations">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Balance</h4>

<div class="assess-input-group" id="ig-boundaries">
    <span class="assess-label">Are extended family expectations constraining your choices?</span>
    <span class="assess-hint">Where you live, how you spend holidays, career decisions, parenting approaches, or lifestyle choices.</span>
    <select id="a-boundaries" onchange="handleAssessInput('a-boundaries')">
        <option value="">Select...</option>
        <option value="heavily">Heavily &ndash; family expectations significantly limit my decisions</option>
        <option value="somewhat">Somewhat &ndash; there are a few areas where family pressure affects my choices</option>
        <option value="slightly">Slightly &ndash; minor influence but I mostly decide independently</option>
        <option value="not-at-all">Not at all &ndash; I make my own choices without family pressure</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-boundaries" onchange="handleSkip('a-boundaries')"><label for="skip-boundaries">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-guilt">
    <span class="assess-label">How much guilt do you feel when you decline family requests or set limits?</span>
    <span class="assess-hint">Can you say no to a family gathering or request without anxiety? Or does guilt drive your decisions?</span>
    <select id="a-guilt" onchange="handleAssessInput('a-guilt')">
        <option value="">Select...</option>
        <option value="overwhelming">Overwhelming &ndash; guilt makes it very hard to say no</option>
        <option value="significant">Significant &ndash; I feel strong guilt that often sways my decisions</option>
        <option value="moderate">Moderate &ndash; I feel guilt but can usually act on my own judgement</option>
        <option value="mild">Mild &ndash; some discomfort but it does not change my decisions</option>
        <option value="minimal">Minimal &ndash; I can set limits without significant guilt</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-guilt" onchange="handleSkip('a-guilt')"><label for="skip-guilt">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-sustainable">
    <span class="assess-label">Does your current level of family obligation feel sustainable?</span>
    <span class="assess-hint">Are you energised by family involvement, or does it feel like a drain you cannot reduce?</span>
    <select id="a-sustainable" onchange="handleAssessInput('a-sustainable')">
        <option value="">Select...</option>
        <option value="unsustainable">Unsustainable &ndash; I feel overwhelmed by family obligations</option>
        <option value="heavy">Heavy &ndash; it is manageable but takes more than I would like</option>
        <option value="balanced">Balanced &ndash; the level of involvement feels about right</option>
        <option value="light">Light &ndash; I have room for more family involvement if I wanted</option>
        <option value="energising">Energising &ndash; family involvement adds to my life rather than draining it</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-sustainable" onchange="handleSkip('a-sustainable')"><label for="skip-sustainable">I know but prefer not to say</label></div>
</div>
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

<p>You now understand why extended family matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about harmony, closeness, and balance. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/extended-family/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Extended Family Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Extended Family. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/extended-family/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'extended-family';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-conflict-map', 'a-gatherings', 'a-navigate',
        'a-contact-freq', 'a-depth', 'a-generations',
        'a-boundaries', 'a-guilt', 'a-sustainable'
    ];

    // All extended-family items are qualitative and unscored (no reliable percentile data)
    var UNSCORED_ITEMS = ASSESS_IDS.slice();

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
        // All extended-family items are unscored; save null for each value
        var scores = {
            harmony: null,
            closeness: null,
            balance: null
        };
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-scores') || {};
            all[AREA] = scores;
            APStorage.save('ap-level1-scores', all);
        }
    }

    // --- Event handlers ---

    window.handleAssessInput = function(itemId) {
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessRecorded();
        updateAssessCompletion();
    };

    window.handleSkip = function(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        var input = document.getElementById(itemId);
        if (skipBox && input) {
            input.disabled = skipBox.checked;
            if (skipBox.checked && input.tagName === 'SELECT') input.value = '';
        }
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessRecorded();
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

            updateInputGroupState(id);
        });

        updateAssessRecorded();
        updateAssessCompletion();
    }

    document.addEventListener('DOMContentLoaded', function() {
        restoreAssessment();
        updateUI();
    });
})();
</script>
