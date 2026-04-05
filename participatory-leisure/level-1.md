---
layout: default
title: "Participatory Leisure – Level 1: Awareness"
life_area_slug: participatory-leisure
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

<h1>Participatory Leisure: Level 1</h1>

<p class="l1-subtitle">Understand what participatory leisure means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Participatory Leisure Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why participatory leisure matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Participatory leisure &ndash; activities you actively engage in for enjoyment rather than passive consumption &ndash; is one of the strongest predictors of life satisfaction. A <a href="https://www.nature.com/articles/s41591-023-02506-1" target="_blank">2023 study across 16 countries</a> found that people who engage in hobbies report higher life satisfaction, better self-rated health, and fewer depressive symptoms, with effects comparable in magnitude to being employed.</p>

<p>The benefits extend well beyond mood. Active leisure builds skills that transfer to other areas of life, creates social bonds that outlast workplace relationships, and provides a sense of identity and accomplishment independent of career status. Research in the <a href="https://www.nejm.org/doi/full/10.1056/NEJMoa022252" target="_blank">New England Journal of Medicine</a> found that adults who maintained diverse leisure interests showed significantly better cognitive function as they aged.</p>

<p>Perhaps most importantly, participatory leisure provides something that consumptive leisure often cannot: the experience of <a href="https://www.researchgate.net/publication/232501960_Flow_The_Psychology_of_Optimal_Experience" target="_blank">flow</a> &ndash; deep, absorbed engagement that is intrinsically rewarding and reliably produces lasting satisfaction rather than the fleeting pleasure of passive entertainment.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about participatory leisure</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue active leisure for different reasons. This site scores every participatory leisure intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Social Connection</h3>
<p>Building relationships and experiencing community through shared leisure activities. Developing friendships, feeling belonging to groups, and gaining emotional support through leisure pursuits. People who lean towards this value focus on activities that bring them together with others and create meaningful social bonds through shared interests.</p>

<h3>Achievement & Mastery</h3>
<p>Developing skills, accomplishing goals, and experiencing personal growth through leisure pursuits. Both the satisfaction of improving capabilities and the confidence that comes from competence. People who lean towards this value seek activities that provide measurable progress and the deep satisfaction of developing expertise.</p>

<h3>Adventure & Exploration</h3>
<p>Seeking novelty, challenge, and transformative experiences through leisure. Expanding comfort zones, discovering new activities, and pursuing memorable adventures that provide lasting personal meaning. People who lean towards this value pick activities that offer excitement and broaden their perspective on life.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each participatory leisure value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Social Connection &ndash; Level 5</div>
    <p><a href="https://www.parkrun.com/about/" target="_blank">Paul Sinton-Hewitt</a> founded parkrun in 2004 as a free, weekly 5 km community running event in a London park with 13 runners. By 2025 it had grown to over 2,500 events in 22 countries with more than 10 million registered participants. He built one of the largest leisure-based communities in the world, centred entirely on inclusive social connection through a shared activity.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Achievement & Mastery &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Simone_Biles" target="_blank">Simone Biles</a> began gymnastics at age 6 and has won 37 World Championship and Olympic medals, making her the most decorated gymnast in history. She has four skills named after her &ndash; moves so difficult that no one else had performed them in competition. She exemplifies the outer reaches of skill mastery through a leisure pursuit that became a vocation.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Adventure & Exploration &ndash; Level 5</div>
    <p><a href="https://www.alastairhumphreys.com/" target="_blank">Alastair Humphreys</a> cycled around the world over four years, rowed the Atlantic, and walked across southern India. He then coined the concept of "microadventures" &ndash; overnight outdoor adventures accessible to anyone with a sleeping bag and a free evening &ndash; making adventure a regular practice rather than an occasional expedition. He was named a National Geographic Adventurer of the Year in 2012.</p>
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
<h4>Social Connection</h4>

<div class="assess-input-group" id="ig-leisure-friends">
    <span class="assess-label">How many people do you regularly do leisure activities with?</span>
    <span class="assess-hint">Think about hobbies, sports, creative pursuits, or group activities &ndash; not just socialising over food or drinks.</span>
    <select id="a-leisure-friends" onchange="handleAssessInput('a-leisure-friends')"><option value="">Select...</option><option value="none">None &ndash; my leisure activities are all solo</option><option value="one">One &ndash; I have one regular activity partner</option><option value="two-to-three">Two to three people</option><option value="four-to-six">Four to six people</option><option value="many">Many &ndash; I regularly do activities with a broad group</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-leisure-friends" onchange="handleSkip('a-leisure-friends')"><label for="skip-leisure-friends">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-group-membership">
    <span class="assess-label">Do you belong to any clubs, groups, or communities organised around a shared activity?</span>
    <span class="assess-hint">Sports teams, book clubs, choirs, gaming groups, craft circles, volunteer organisations, etc.</span>
    <select id="a-group-membership" onchange="handleAssessInput('a-group-membership')"><option value="">Select...</option><option value="none">None &ndash; I'm not a member of any groups</option><option value="lapsed">Lapsed &ndash; I used to be but stopped attending</option><option value="one">One &ndash; I belong to one group</option><option value="two-to-three">Two to three groups</option><option value="several">Several &ndash; four or more active memberships</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-group-membership" onchange="handleSkip('a-group-membership')"><label for="skip-group-membership">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-social-satisfaction">
    <span class="assess-label">Do your leisure activities provide enough social connection?</span>
    <span class="assess-hint">Some people prefer solo pursuits and feel fine; others want more social leisure but haven't found it.</span>
    <select id="a-social-satisfaction" onchange="handleAssessInput('a-social-satisfaction')"><option value="">Select...</option><option value="isolated">Isolated &ndash; I want more social leisure but don't have it</option><option value="somewhat-lacking">Somewhat lacking &ndash; I'd like more social activities</option><option value="adequate">Adequate &ndash; I get enough but could benefit from more</option><option value="good">Good &ndash; my leisure provides solid social connection</option><option value="excellent">Excellent &ndash; rich social life through shared activities</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-social-satisfaction" onchange="handleSkip('a-social-satisfaction')"><label for="skip-social-satisfaction">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Achievement &amp; Mastery</h4>

<div class="assess-input-group" id="ig-skill-level">
    <span class="assess-label">Do you have at least one leisure activity where you've developed meaningful skill over time?</span>
    <span class="assess-hint">Musical instruments, a sport, a craft, cooking, gardening, a game &ndash; anything where you've noticeably improved.</span>
    <select id="a-skill-level" onchange="handleAssessInput('a-skill-level')"><option value="">Select...</option><option value="no">No &ndash; I haven't stuck with anything long enough</option><option value="beginner">Beginner &ndash; I'm learning something but still very early</option><option value="intermediate">Intermediate &ndash; noticeable improvement in one activity</option><option value="skilled">Skilled &ndash; genuine competence in one or two activities</option><option value="expert">Expert &ndash; high-level skill in at least one leisure pursuit</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-skill-level" onchange="handleSkip('a-skill-level')"><label for="skip-skill-level">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-consistency">
    <span class="assess-label">Do you tend to stick with activities long enough to develop real competence?</span>
    <span class="assess-hint">There's no wrong answer &ndash; some people are natural specialists, others natural explorers.</span>
    <select id="a-consistency" onchange="handleAssessInput('a-consistency')"><option value="">Select...</option><option value="always-move-on">Always move on &ndash; I try things and quickly lose interest</option><option value="mostly-explore">Mostly explore &ndash; I prefer variety over depth</option><option value="mixed">Mixed &ndash; some things I've stuck with, others I've dropped</option><option value="mostly-persist">Mostly persist &ndash; I tend to commit for months or years</option><option value="deep-commitment">Deep commitment &ndash; I stay with activities for years or decades</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-consistency" onchange="handleSkip('a-consistency')"><label for="skip-consistency">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-progress">
    <span class="assess-label">Are you currently improving at any leisure activity?</span>
    <span class="assess-hint">Improvement might mean better scores, harder pieces, more complex projects, or feedback from others.</span>
    <select id="a-progress" onchange="handleAssessInput('a-progress')"><option value="">Select...</option><option value="not-applicable">Not applicable &ndash; I don't have skill-based leisure activities</option><option value="plateaued">Plateaued &ndash; I haven't improved in a while</option><option value="not-tracking">Not tracking &ndash; I'm not sure whether I'm improving</option><option value="slowly">Slowly &ndash; gradual improvement over time</option><option value="actively">Actively improving &ndash; noticeable progress with deliberate practice</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-progress" onchange="handleSkip('a-progress')"><label for="skip-progress">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Adventure &amp; Exploration</h4>

<div class="assess-input-group" id="ig-new-activities">
    <span class="assess-label">How many genuinely new leisure activities have you tried in the past year?</span>
    <span class="assess-hint">Count anything genuinely new to you &ndash; a new sport, creative medium, game, or outdoor activity.</span>
    <select id="a-new-activities" onchange="handleAssessInput('a-new-activities')"><option value="">Select...</option><option value="none">None &ndash; I've stuck with the same activities</option><option value="one">One &ndash; I tried one new thing</option><option value="two-to-three">Two to three new activities</option><option value="four-to-five">Four to five new activities</option><option value="many">Many &ndash; six or more new activities</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-new-activities" onchange="handleSkip('a-new-activities')"><label for="skip-new-activities">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-comfort-zone">
    <span class="assess-label">How often do you push beyond your leisure comfort zone?</span>
    <span class="assess-hint">Public performance, physical risk, unfamiliar social settings, creative vulnerability &ndash; where does discomfort start?</span>
    <select id="a-comfort-zone" onchange="handleAssessInput('a-comfort-zone')"><option value="">Select...</option><option value="never">Never &ndash; I stay firmly within familiar activities</option><option value="rarely">Rarely &ndash; maybe once a year</option><option value="occasionally">Occasionally &ndash; a few times a year</option><option value="regularly">Regularly &ndash; I seek out mild discomfort monthly</option><option value="frequently">Frequently &ndash; I actively pursue new and challenging experiences</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-comfort-zone" onchange="handleSkip('a-comfort-zone')"><label for="skip-comfort-zone">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-memorable">
    <span class="assess-label">How many genuinely memorable leisure experiences have you had in the past year?</span>
    <span class="assess-hint">Experiences that stand out from routine &ndash; not just pleasant evenings, but moments that mattered.</span>
    <select id="a-memorable" onchange="handleAssessInput('a-memorable')"><option value="">Select...</option><option value="none">None &ndash; the past year blends together</option><option value="one">One &ndash; a single standout experience</option><option value="two-to-three">Two to three memorable experiences</option><option value="several">Several &ndash; regular memorable moments</option><option value="many">Many &ndash; rich with experiences I'll remember for years</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-memorable" onchange="handleSkip('a-memorable')"><label for="skip-memorable">I know but prefer not to say</label></div>
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

<p>You now understand why participatory leisure matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about social connection, achievement and mastery, and adventure and exploration. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/participatory-leisure/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Participatory Leisure Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Participatory Leisure. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/participatory-leisure/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'participatory-leisure';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-leisure-friends', 'a-group-membership', 'a-social-satisfaction',
        'a-skill-level', 'a-consistency', 'a-progress',
        'a-new-activities', 'a-comfort-zone', 'a-memorable'
    ];
    var UNSCORED_ITEMS = ASSESS_IDS.slice();

    function loadProgress() { if (typeof APStorage === 'undefined') return {}; var all = APStorage.load('ap-level1-progress') || {}; return all[AREA] || {}; }
    function saveProgress(progress) { if (typeof APStorage === 'undefined') return; var all = APStorage.load('ap-level1-progress') || {}; all[AREA] = progress; APStorage.save('ap-level1-progress', all); }
    function updateUI() { var progress = loadProgress(); var doneCount = 0; var firstIncomplete = null; STEPS.forEach(function(step, i) { var el = document.getElementById('step-' + step); var seg = document.getElementById('prog-' + (i + 1)); if (!el || !seg) return; if (progress[step]) { el.classList.add('done'); el.classList.remove('active'); seg.className = 'l1-progress-segment done'; doneCount++; } else if (!firstIncomplete) { firstIncomplete = step; el.classList.add('active'); el.classList.remove('done'); seg.className = 'l1-progress-segment active'; } else { el.classList.remove('active', 'done'); seg.className = 'l1-progress-segment'; } }); var label = document.getElementById('progressLabel'); if (doneCount >= STEPS.length) { if (label) label.textContent = 'All steps complete'; var banner = document.getElementById('completeBanner'); if (banner) banner.classList.add('visible'); } else { if (label) label.textContent = 'Step ' + (doneCount + 1) + ' of ' + STEPS.length; } if (firstIncomplete) { openStep(firstIncomplete); } }
    function openStep(step) { STEPS.forEach(function(s) { var el = document.getElementById('step-' + s); if (el) el.classList.remove('open'); }); var target = document.getElementById('step-' + step); if (target) { target.classList.add('open'); setTimeout(function() { target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 100); } }
    window.toggleStep = function(step) { var el = document.getElementById('step-' + step); if (el) el.classList.toggle('open'); };
    window.completeStep = function(step) { if (step === 'assess') saveScores(); var progress = loadProgress(); progress[step] = true; saveProgress(progress); updateUI(); var idx = STEPS.indexOf(step); if (idx >= 0 && idx < STEPS.length - 1) { setTimeout(function() { openStep(STEPS[idx + 1]); }, 300); } };
    function isItemAnswered(itemId) { var skipBox = document.getElementById('skip-' + itemId.replace('a-', '')); if (skipBox && skipBox.checked) return true; var el = document.getElementById(itemId); return el && el.value !== '' && el.value !== null; }
    function updateInputGroupState(itemId) { var group = document.getElementById('ig-' + itemId.replace('a-', '')); if (group) group.classList.toggle('answered', isItemAnswered(itemId)); }
    function updateAssessRecorded() { var allAnswered = ASSESS_IDS.every(function(id) { return isItemAnswered(id); }); var recorded = document.getElementById('assessRecorded'); if (recorded) recorded.classList.toggle('visible', allAnswered); }
    function updateAssessCompletion() { var allAnswered = ASSESS_IDS.every(function(id) { return isItemAnswered(id); }); var btn = document.getElementById('assessBtn'); if (btn) { btn.disabled = !allAnswered; btn.textContent = allAnswered ? 'All done \u2013 continue' : 'Answer all items to continue'; } }
    function saveAnswers() { var answers = {}; ASSESS_IDS.forEach(function(id) { var skipBox = document.getElementById('skip-' + id.replace('a-', '')); var skipped = skipBox && skipBox.checked; var value = null; if (!skipped) { var el = document.getElementById(id); if (el && el.value !== '') value = el.value; } answers[id] = { value: value, skipped: skipped }; }); var allAnswers = {}; try { allAnswers = JSON.parse(localStorage.getItem('ap-level1-answers')) || {}; } catch(e) {} allAnswers[AREA] = answers; localStorage.setItem('ap-level1-answers', JSON.stringify(allAnswers)); var checklist = {}; ASSESS_IDS.forEach(function(id) { checklist[id] = isItemAnswered(id); }); if (typeof APStorage !== 'undefined') { var all = APStorage.load('ap-level1-assess') || {}; all[AREA] = checklist; APStorage.save('ap-level1-assess', all); } }
    function saveScores() { var scores = { social: null, mastery: null, adventure: null }; if (typeof APStorage !== 'undefined') { var all = APStorage.load('ap-level1-scores') || {}; all[AREA] = scores; APStorage.save('ap-level1-scores', all); } }
    window.handleAssessInput = function(itemId) { updateInputGroupState(itemId); saveAnswers(); updateAssessRecorded(); updateAssessCompletion(); };
    window.handleSkip = function(itemId) { var skipBox = document.getElementById('skip-' + itemId.replace('a-', '')); var input = document.getElementById(itemId); if (skipBox && input) { input.disabled = skipBox.checked; if (skipBox.checked && input.tagName === 'SELECT') input.value = ''; } updateInputGroupState(itemId); saveAnswers(); updateAssessRecorded(); updateAssessCompletion(); };
    function restoreAssessment() { var allAnswers = {}; try { allAnswers = JSON.parse(localStorage.getItem('ap-level1-answers')) || {}; } catch(e) {} var answers = allAnswers[AREA]; if (!answers) return; ASSESS_IDS.forEach(function(id) { var item = answers[id]; if (!item) return; if (item.skipped) { var skipBox = document.getElementById('skip-' + id.replace('a-', '')); if (skipBox) { skipBox.checked = true; var input = document.getElementById(id); if (input) input.disabled = true; } } else if (item.value !== null) { var el = document.getElementById(id); if (el) el.value = item.value; } updateInputGroupState(id); }); updateAssessRecorded(); updateAssessCompletion(); }
    document.addEventListener('DOMContentLoaded', function() { restoreAssessment(); updateUI(); });
})();
</script>
