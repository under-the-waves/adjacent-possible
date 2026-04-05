---
layout: default
title: "Learning Methods – Level 1: Awareness"
life_area_slug: learning-methods
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

/* Assessment checklist */
.assess-group { margin-bottom: 20px; }
.assess-group h4 { margin: 0 0 10px 0; }
.assess-item {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 10px 14px;
    margin-bottom: 6px;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    cursor: pointer;
    transition: border-color 0.2s, background 0.2s;
    font-size: 0.93em;
    line-height: 1.4;
}
.assess-item:hover { border-color: #155799; background: #f0f4ff; }
.assess-item.checked { border-color: #28a745; background: #f0f7f0; }
.assess-item input[type="checkbox"] {
    margin-top: 2px;
    flex-shrink: 0;
    accent-color: #28a745;
}
.assess-item label { cursor: pointer; flex: 1; }
.assess-hint {
    font-size: 0.85em;
    color: #888;
    margin-top: 2px;
}

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

<h1>Learning Methods: Level 1</h1>

<p class="l1-subtitle">Understand what learning methods means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Learning Methods Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why learning methods matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>How you learn determines how quickly you grow in every other area of life. The techniques you use to study, practise, and retain information are a force multiplier: improve them once, and the benefits compound across everything you do.</p>

<p>The evidence for better methods is unusually clear. Spaced practice &ndash; spreading study sessions over time &ndash; produces <a href="https://link.springer.com/article/10.3758/s13421-010-0035-2" target="_blank">roughly double the long-term retention</a> of cramming, yet over 80% of people rate cramming as equally or more effective. Active recall &ndash; testing yourself rather than rereading &ndash; is <a href="https://www.science.org/doi/10.1126/science.1199327" target="_blank">one of the most effective study techniques</a> known, but most learners default to passive methods like highlighting and rereading.</p>

<p>The gap between typical and effective methods is large enough that switching techniques alone &ndash; without spending more time &ndash; can dramatically improve outcomes. Few other investments offer this kind of return: you don't need to work harder, just differently.</p>

<p>Beyond efficiency, learning how to learn well builds confidence, reduces the anxiety of tackling unfamiliar subjects, and makes it possible to adapt as the knowledge and skills the world demands continue to shift.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about learning methods</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue better learning methods for different reasons. This site scores every learning methods intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Efficiency & Speed</h3>
<p>Maximising learning outcomes per unit of time invested. People who lean towards this value focus on methods with proven time-to-competency ratios and systematic approaches that eliminate wasted effort. They want to learn more in less time.</p>

<h3>Depth & Mastery</h3>
<p>Achieving deep, transferable understanding rather than surface-level knowledge. People who lean towards this value prefer methods that sacrifice speed for comprehensive understanding and lasting expertise. They want to build robust mental models that enable creative application across contexts.</p>

<h3>Enjoyment & Motivation</h3>
<p>Learning approaches that maintain engagement and intrinsic motivation over time. People who lean towards this value choose techniques they can maintain consistently because they find the process inherently satisfying. They would keep learning even without external pressure.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each learning methods value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Efficiency & Speed &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Scott_Young_(author)" target="_blank">Scott Young</a> completed MIT's four-year computer science curriculum in 12 months using structured self-study, then learned four languages in a year by living in each country and applying targeted immersion techniques. His approach centres on identifying the highest-leverage study methods for each domain and eliminating low-return activity.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Depth & Mastery &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Josh_Waitzkin" target="_blank">Josh Waitzkin</a> became a national chess champion as a child, then switched to tai chi push hands and won a world championship in that discipline too. His book <em>The Art of Learning</em> describes a deliberate practice methodology built around identifying and internalising core principles deeply enough to transfer them across unrelated domains.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Enjoyment & Motivation &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Richard_Feynman" target="_blank">Richard Feynman</a> maintained a lifelong habit of learning for its own sake &ndash; picking locks, studying biology, learning to draw, playing bongo drums, and deciphering Mayan hieroglyphs alongside his physics work. He sustained deep curiosity across dozens of fields for over 40 years, driven almost entirely by the pleasure of figuring things out.</p>
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
<h4>Efficiency &amp; Speed</h4>

<div class="assess-input-group" id="ig-study-methods">
    <span class="assess-label">Which study techniques do you use regularly?</span>
    <span class="assess-hint">Rereading, highlighting, flashcards, practice problems, summarising, teaching someone else.</span>
    <select id="a-study-methods" onchange="handleAssessInput('a-study-methods')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I don't use any deliberate techniques</option>
        <option value="passive">Passive only &ndash; rereading or highlighting</option>
        <option value="one-active">One active method &ndash; e.g. flashcards or practice problems</option>
        <option value="several">Several methods &ndash; I mix techniques depending on the material</option>
        <option value="evidence-based">Evidence-based selection &ndash; I choose techniques based on what research shows works</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-study-methods" onchange="handleSkip('a-study-methods')"><label for="skip-study-methods">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-spacing">
    <span class="assess-label">How do you typically spread your learning over time?</span>
    <span class="assess-hint">Spread over multiple sessions or concentrated into one sitting?</span>
    <select id="a-spacing" onchange="handleAssessInput('a-spacing')">
        <option value="">Select...</option>
        <option value="all-at-once">All at once &ndash; I cram or binge-learn in a single session</option>
        <option value="mostly-crammed">Mostly crammed &ndash; occasional spacing but usually last-minute</option>
        <option value="mixed">Mixed &ndash; I space some things but not deliberately</option>
        <option value="mostly-spaced">Mostly spaced &ndash; I usually revisit material across days</option>
        <option value="deliberately-spaced">Deliberately spaced &ndash; I plan review intervals in advance</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-spacing" onchange="handleSkip('a-spacing')"><label for="skip-spacing">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-time-spent">
    <span class="assess-label">How many hours per week do you spend intentionally learning something new?</span>
    <span class="assess-hint">Count structured study, courses, deliberate practice &ndash; not passive consumption.</span>
    <select id="a-time-spent" onchange="handleAssessInput('a-time-spent')">
        <option value="">Select...</option>
        <option value="zero">Zero &ndash; I don't set aside time for learning</option>
        <option value="under-1">Under 1 hour</option>
        <option value="1-3">1&ndash;3 hours</option>
        <option value="3-7">3&ndash;7 hours</option>
        <option value="over-7">Over 7 hours</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-time-spent" onchange="handleSkip('a-time-spent')"><label for="skip-time-spent">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Depth &amp; Mastery</h4>

<div class="assess-input-group" id="ig-feedback">
    <span class="assess-label">How regularly do you seek feedback on your learning or practice?</span>
    <span class="assess-hint">A teacher, mentor, test scores, recording yourself, or any way of checking understanding.</span>
    <select id="a-feedback" onchange="handleAssessInput('a-feedback')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I don't get feedback on my learning</option>
        <option value="rarely">Rarely &ndash; only when feedback is forced on me</option>
        <option value="sometimes">Sometimes &ndash; I seek it out occasionally</option>
        <option value="regularly">Regularly &ndash; I have a consistent feedback source</option>
        <option value="systematically">Systematically &ndash; feedback is built into my learning process</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-feedback" onchange="handleSkip('a-feedback')"><label for="skip-feedback">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-connections">
    <span class="assess-label">Do you connect new information to what you already know?</span>
    <span class="assess-hint">When you learn something, do you naturally think about how it relates to other things you know?</span>
    <select id="a-connections" onchange="handleAssessInput('a-connections')">
        <option value="">Select...</option>
        <option value="rarely">Rarely &ndash; I treat new topics as isolated</option>
        <option value="sometimes">Sometimes &ndash; I notice obvious connections</option>
        <option value="often">Often &ndash; I regularly link new knowledge to existing understanding</option>
        <option value="actively">Actively &ndash; I deliberately look for connections and analogies</option>
        <option value="systematically">Systematically &ndash; I have a process for integrating new knowledge</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-connections" onchange="handleSkip('a-connections')"><label for="skip-connections">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-weakness">
    <span class="assess-label">Do you actively work on specific weaknesses in any skill area?</span>
    <span class="assess-hint">Deliberate practice means targeting what you find difficult, not repeating what you're comfortable with.</span>
    <select id="a-weakness" onchange="handleAssessInput('a-weakness')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I practise what I'm already comfortable with</option>
        <option value="aware">Aware &ndash; I know my weaknesses but don't target them</option>
        <option value="sometimes">Sometimes &ndash; I occasionally focus on weak areas</option>
        <option value="regularly">Regularly &ndash; I make a point of practising difficult things</option>
        <option value="systematically">Systematically &ndash; I identify and target weaknesses as a core part of practice</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-weakness" onchange="handleSkip('a-weakness')"><label for="skip-weakness">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Enjoyment &amp; Motivation</h4>

<div class="assess-input-group" id="ig-enjoy-learning">
    <span class="assess-label">Which types of learning do you find energising versus draining?</span>
    <span class="assess-hint">Reading vs doing, solo vs group, structured vs exploratory, short bursts vs long sessions.</span>
    <select id="a-enjoy-learning" onchange="handleAssessInput('a-enjoy-learning')">
        <option value="">Select...</option>
        <option value="draining">Most learning feels draining</option>
        <option value="mixed">Mixed &ndash; I haven't identified clear preferences</option>
        <option value="some-preferences">Some preferences &ndash; I know a few things I enjoy</option>
        <option value="clear-preferences">Clear preferences &ndash; I know what works for me and seek it out</option>
        <option value="optimised">Optimised &ndash; I've structured my learning around what energises me</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-enjoy-learning" onchange="handleSkip('a-enjoy-learning')"><label for="skip-enjoy-learning">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-consistency">
    <span class="assess-label">Can you sustain a learning routine for more than a few weeks?</span>
    <span class="assess-hint">Think about past attempts to learn something. Did you keep going, or did motivation fade?</span>
    <select id="a-consistency" onchange="handleAssessInput('a-consistency')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I always lose motivation quickly</option>
        <option value="rarely">Rarely &ndash; I've sustained it once or twice</option>
        <option value="sometimes">Sometimes &ndash; it depends on the subject</option>
        <option value="usually">Usually &ndash; I can maintain routines for months</option>
        <option value="always">Always &ndash; I have long-running learning habits</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-consistency" onchange="handleSkip('a-consistency')"><label for="skip-consistency">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-curiosity">
    <span class="assess-label">When did you last explore a topic out of pure curiosity?</span>
    <span class="assess-hint">Something you learned because you wanted to, not because you had to.</span>
    <select id="a-curiosity" onchange="handleAssessInput('a-curiosity')">
        <option value="">Select...</option>
        <option value="cant-recall">Can't recall &ndash; it's been a very long time</option>
        <option value="months-ago">Months ago</option>
        <option value="weeks-ago">Weeks ago</option>
        <option value="this-week">This week</option>
        <option value="today">Today or yesterday &ndash; I explore new topics constantly</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-curiosity" onchange="handleSkip('a-curiosity')"><label for="skip-curiosity">I know but prefer not to say</label></div>
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

<p>You now understand why learning methods matter, what different people get out of them, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about efficiency and speed, depth and mastery, and enjoyment and motivation. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/learning-methods/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Learning Methods Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Learning Methods. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/learning-methods/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'learning-methods';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-study-methods', 'a-spacing', 'a-time-spent',
        'a-feedback', 'a-connections', 'a-weakness',
        'a-enjoy-learning', 'a-consistency', 'a-curiosity'
    ];

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
        var scores = {
            efficiency: null,
            depth: null,
            enjoyment: null
        };
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-scores') || {};
            all[AREA] = scores;
            APStorage.save('ap-level1-scores', all);
        }
    }

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
