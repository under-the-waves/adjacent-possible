---
layout: default
title: "Community Contribution – Level 1: Awareness"
life_area_slug: community-contribution
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

<h1>Community Contribution: Level 1</h1>

<p class="l1-subtitle">Understand what community contribution means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Community Contribution Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why community contribution matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Community contribution &ndash; volunteering, neighbourhood involvement, and civic participation &ndash; produces measurable benefits for both the community and the contributor. A <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3890753/" target="_blank">meta-analysis of volunteering research</a> found that volunteers have lower rates of depression, higher life satisfaction, and a 22% reduction in mortality risk compared to non-volunteers.</p>

<p>The threshold for significant health benefits appears to be roughly <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3890753/" target="_blank">100 hours per year</a> &ndash; about 2 hours per week. Those who volunteer 200+ hours annually show a 40% reduction in hypertension risk. These findings hold after controlling for pre-existing health and socioeconomic status, suggesting a genuine causal relationship.</p>

<p>Beyond individual benefits, community contribution builds social capital &ndash; the networks of trust and reciprocity that make communities function. In an era where only <a href="https://americorps.gov/about/our-impact/volunteering-civic-life" target="_blank">23% of adults</a> formally volunteer, and neighbourhood social ties have weakened considerably, deliberate local involvement is both increasingly valuable and increasingly rare.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about community contribution</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People contribute to their communities for different reasons. This site scores every community contribution intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Impact</h3>
<p>Making a measurable, tangible difference in your community through your contributions. Choosing high-leverage volunteer activities, leading projects that produce real outcomes, and evaluating whether your community work is actually improving things rather than just filling time. People who lean towards this value focus on results.</p>

<h3>Belonging</h3>
<p>Feeling genuinely connected to and part of your local community through shared participation. Knowing your neighbours, being recognised as a community member, participating in local traditions, and experiencing the sense of home that comes from mutual investment. People who lean towards this value see community contribution as building their own roots.</p>

<h3>Fulfilment</h3>
<p>The personal satisfaction and meaning derived from contributing to community life. Volunteering in ways that energise you, finding purpose in service, and ensuring community work is a source of joy rather than obligation. People who lean towards this value seek contributions that nourish them as well as the community.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each community contribution value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Impact &ndash; Level 5</div>
    <p><a href="https://www.habitat.org/about/history" target="_blank">Millard Fuller</a> co-founded Habitat for Humanity in 1976, which has since built or repaired over 800,000 homes worldwide, providing shelter for more than 4 million people. He pioneered the "economics of Jesus" model &ndash; no-interest mortgage loans funded by donations and volunteer labour &ndash; proving that community-led housing construction could be scaled globally. His measurable impact on housing security transformed the volunteer construction sector.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Belonging &ndash; Level 5</div>
    <p><a href="https://www.incredibleedible.org.uk/what-we-do/" target="_blank">Pam Warhurst</a> co-founded Incredible Edible Todmorden in 2008, transforming unused public spaces in a small West Yorkshire town into community food-growing plots. The initiative spread to over 100 groups worldwide. By inviting anyone to plant, tend, and harvest food in shared spaces, she turned food growing into a vehicle for neighbourhood connection, making Todmorden measurably more cohesive according to local surveys.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Fulfilment &ndash; Level 5</div>
    <p><a href="https://www.maggiescentres.org/about-us/how-maggies-started/" target="_blank">Maggie Keswick Jencks</a> was diagnosed with cancer in 1988 and spent her remaining years designing a new model of cancer care based on her own experience of what patients need &ndash; not just treatment but warmth, information, and human connection. The first Maggie's Centre opened in Edinburgh in 1996, and there are now over 20 centres across the UK. She described the work as the most meaningful thing she had ever done.</p>
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
<h4>Impact</h4>

<div class="assess-input-group" id="ig-volunteer-hours">
    <span class="assess-label">How many hours per month do you spend on community activities or volunteering?</span>
    <span class="assess-hint">Include formal volunteering, informal helping, neighbourhood activities, and civic participation.</span>
    <select id="a-volunteer-hours" onchange="handleAssessInput('a-volunteer-hours')"><option value="">Select...</option><option value="none">None</option><option value="1-to-3">1 &ndash; 3 hours per month</option><option value="4-to-8">4 &ndash; 8 hours per month</option><option value="9-to-16">9 &ndash; 16 hours per month</option><option value="over-16">Over 16 hours per month</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-volunteer-hours" onchange="handleSkip('a-volunteer-hours')"><label for="skip-volunteer-hours">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-local-orgs">
    <span class="assess-label">How many community organisations or volunteer opportunities can you name in your area?</span>
    <span class="assess-hint">Food banks, neighbourhood associations, school boards, environmental groups, sports clubs, etc.</span>
    <select id="a-local-orgs" onchange="handleAssessInput('a-local-orgs')"><option value="">Select...</option><option value="none">None &ndash; I'm not aware of any</option><option value="one-or-two">One or two</option><option value="three-to-five">Three to five</option><option value="six-to-ten">Six to ten</option><option value="many">Many &ndash; I'm well connected to local organisations</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-local-orgs" onchange="handleSkip('a-local-orgs')"><label for="skip-local-orgs">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-skills-match">
    <span class="assess-label">Do your community contributions leverage your professional skills?</span>
    <span class="assess-hint">Skills-based volunteering &ndash; using your expertise for a cause &ndash; tends to produce significantly more impact per hour.</span>
    <select id="a-skills-match" onchange="handleAssessInput('a-skills-match')"><option value="">Select...</option><option value="no-contributions">I don't currently contribute</option><option value="generic">Generic &ndash; I do tasks anyone could do</option><option value="some-overlap">Some overlap &ndash; occasionally I use my skills</option><option value="often">Often &ndash; my skills are regularly relevant</option><option value="deliberately">Deliberately &ndash; I seek out contributions that leverage my expertise</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-skills-match" onchange="handleSkip('a-skills-match')"><label for="skip-skills-match">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Belonging</h4>

<div class="assess-input-group" id="ig-neighbours">
    <span class="assess-label">Do you know your immediate neighbours by name?</span>
    <span class="assess-hint">On both sides and across the road, if applicable. Only 26% of adults know most of their neighbours.</span>
    <select id="a-neighbours" onchange="handleAssessInput('a-neighbours')"><option value="">Select...</option><option value="none">None &ndash; I don't know any neighbours</option><option value="one-or-two">One or two &ndash; a couple of names</option><option value="some">Some &ndash; I know a few by name</option><option value="most">Most &ndash; I know nearly all my immediate neighbours</option><option value="all">All &ndash; I know all my neighbours and we interact regularly</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-neighbours" onchange="handleSkip('a-neighbours')"><label for="skip-neighbours">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-local-events">
    <span class="assess-label">Do you attend any regular community events, meetings, or gatherings?</span>
    <span class="assess-hint">Parish council meetings, community markets, neighbourhood clean-ups, local festivals, etc.</span>
    <select id="a-local-events" onchange="handleAssessInput('a-local-events')"><option value="">Select...</option><option value="never">Never &ndash; I don't attend community events</option><option value="rarely">Rarely &ndash; once or twice a year at most</option><option value="occasionally">Occasionally &ndash; a few times a year</option><option value="regularly">Regularly &ndash; monthly or more</option><option value="frequently">Frequently &ndash; weekly involvement in community activities</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-local-events" onchange="handleSkip('a-local-events')"><label for="skip-local-events">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-rootedness">
    <span class="assess-label">How rooted do you feel in your local area?</span>
    <span class="assess-hint">Rootedness is partly about time spent in a place, but mostly about relationships and shared investment.</span>
    <select id="a-rootedness" onchange="handleAssessInput('a-rootedness')"><option value="">Select...</option><option value="transient">Transient &ndash; this is just where I happen to live</option><option value="settling">Settling in &ndash; I'm getting to know the area</option><option value="somewhat-rooted">Somewhat rooted &ndash; I feel some connection</option><option value="rooted">Rooted &ndash; this feels like home</option><option value="deeply-rooted">Deeply rooted &ndash; strong relationships and shared history here</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-rootedness" onchange="handleSkip('a-rootedness')"><label for="skip-rootedness">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Fulfilment</h4>

<div class="assess-input-group" id="ig-enjoy-volunteering">
    <span class="assess-label">Does your current community involvement energise you or drain you?</span>
    <span class="assess-hint">Some people volunteer out of guilt or obligation. Others genuinely look forward to it. Both are common.</span>
    <select id="a-enjoy-volunteering" onchange="handleAssessInput('a-enjoy-volunteering')"><option value="">Select...</option><option value="no-involvement">No involvement &ndash; I don't currently participate</option><option value="draining">Draining &ndash; it feels like an obligation</option><option value="neutral">Neutral &ndash; neither energising nor draining</option><option value="energising">Energising &ndash; I generally look forward to it</option><option value="deeply-energising">Deeply energising &ndash; it's a highlight of my week</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-enjoy-volunteering" onchange="handleSkip('a-enjoy-volunteering')"><label for="skip-enjoy-volunteering">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-purpose">
    <span class="assess-label">Is contributing to your community an important part of your identity?</span>
    <span class="assess-hint">There's no wrong answer &ndash; the question is whether you've reflected on it.</span>
    <select id="a-purpose" onchange="handleAssessInput('a-purpose')"><option value="">Select...</option><option value="not-at-all">Not at all &ndash; I rarely think about it</option><option value="peripherally">Peripherally &ndash; it's something I do occasionally</option><option value="somewhat">Somewhat &ndash; it matters but isn't central</option><option value="important">Important &ndash; it's a significant part of how I see myself</option><option value="core">Core &ndash; community contribution is fundamental to my identity</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-purpose" onchange="handleSkip('a-purpose')"><label for="skip-purpose">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-barriers">
    <span class="assess-label">What is the main barrier to greater community involvement in your life?</span>
    <span class="assess-hint">Time, energy, social anxiety, not knowing where to start, feeling like an outsider &ndash; all are common.</span>
    <select id="a-barriers" onchange="handleAssessInput('a-barriers')"><option value="">Select...</option><option value="no-interest">No interest &ndash; I don't want more community involvement</option><option value="time">Time &ndash; too busy with work and other commitments</option><option value="social-barriers">Social barriers &ndash; anxiety, feeling like an outsider, or not knowing anyone</option><option value="logistics">Logistics &ndash; I don't know where to start or what's available</option><option value="none">None &ndash; I'm already as involved as I want to be</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-barriers" onchange="handleSkip('a-barriers')"><label for="skip-barriers">I know but prefer not to say</label></div>
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

<p>You now understand why community contribution matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about impact, belonging, and fulfilment. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/community-contribution/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Community Contribution Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Community Contribution. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/community-contribution/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'community-contribution';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-volunteer-hours', 'a-local-orgs', 'a-skills-match',
        'a-neighbours', 'a-local-events', 'a-rootedness',
        'a-enjoy-volunteering', 'a-purpose', 'a-barriers'
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
    function saveScores() { var scores = { impact: null, belonging: null, fulfilment: null }; if (typeof APStorage !== 'undefined') { var all = APStorage.load('ap-level1-scores') || {}; all[AREA] = scores; APStorage.save('ap-level1-scores', all); } }
    window.handleAssessInput = function(itemId) { updateInputGroupState(itemId); saveAnswers(); updateAssessRecorded(); updateAssessCompletion(); };
    window.handleSkip = function(itemId) { var skipBox = document.getElementById('skip-' + itemId.replace('a-', '')); var input = document.getElementById(itemId); if (skipBox && input) { input.disabled = skipBox.checked; if (skipBox.checked && input.tagName === 'SELECT') input.value = ''; } updateInputGroupState(itemId); saveAnswers(); updateAssessRecorded(); updateAssessCompletion(); };
    function restoreAssessment() { var allAnswers = {}; try { allAnswers = JSON.parse(localStorage.getItem('ap-level1-answers')) || {}; } catch(e) {} var answers = allAnswers[AREA]; if (!answers) return; ASSESS_IDS.forEach(function(id) { var item = answers[id]; if (!item) return; if (item.skipped) { var skipBox = document.getElementById('skip-' + id.replace('a-', '')); if (skipBox) { skipBox.checked = true; var input = document.getElementById(id); if (input) input.disabled = true; } } else if (item.value !== null) { var el = document.getElementById(id); if (el) el.value = item.value; } updateInputGroupState(id); }); updateAssessRecorded(); updateAssessCompletion(); }
    document.addEventListener('DOMContentLoaded', function() { restoreAssessment(); updateUI(); });
})();
</script>
