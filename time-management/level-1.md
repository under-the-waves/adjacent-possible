---
layout: default
title: "Time Management – Level 1: Awareness"
life_area_slug: time-management
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
.assess-input-group input[type="number"] {
    width: 100px;
    padding: 6px 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 0.95em;
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

<h1>Time Management: Level 1</h1>

<p class="l1-subtitle">Understand what time management means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Time Management Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why time management matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Time is the one resource you cannot earn more of. How you allocate it determines almost everything about the shape of your life &ndash; your career progress, your relationships, your health, and your sense of control.</p>

<p>A <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7799745/" target="_blank">meta-analysis of 158 studies</a> (n = 53,957) found that effective time management enhances life satisfaction more than job performance &ndash; the effect on life satisfaction was 72% stronger than on job satisfaction. Time management is not primarily a work skill; it is a life skill.</p>

<p>Research shows that <a href="https://www.timewatch.com/blog/time-management-statistics/" target="_blank">91% of people</a> who implement structured time management practices report reduced stress, and 94% report increased productivity. People who feel in control of their time report significantly better work-life balance, lower feelings of overload, and <a href="https://journals.sagepub.com/doi/full/10.1177/2158244018824506" target="_blank">less tension</a> than their peers.</p>

<p>Yet only 18% of people have any formal time management system, and just 5% use structured approaches like time blocking. Even basic practices place you well ahead of most people.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about time management</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People manage their time for different reasons. This site scores every time management intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Productivity & Achievement</h3>
<p>Maximising output and accomplishing meaningful goals efficiently. Getting more done in less time, meeting deadlines consistently, and making tangible progress on important projects. People who lean towards this value focus on systems and techniques that measurably increase their productive capacity.</p>

<h3>Balance & Wellbeing</h3>
<p>Creating sustainable rhythms that support long-term effectiveness while maintaining personal wellbeing. Managing energy levels, preventing burnout, maintaining boundaries between work and personal time, and ensuring time for rest and relationships. People who lean towards this value seek approaches that enhance both performance and life satisfaction.</p>

<h3>Flexibility & Responsiveness</h3>
<p>Maintaining the ability to adapt to changing priorities and unexpected demands while staying effective. Handling interruptions gracefully, pivoting between tasks smoothly, and remaining productive despite uncertainty. People who lean towards this value want systems that work across different contexts and can accommodate life's unpredictability.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each time management value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Productivity & Achievement &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Elon_Musk" target="_blank">Elon Musk</a> runs multiple companies simultaneously by scheduling his day in five-minute blocks and batching similar tasks together. Whatever one thinks of his other attributes, his time management output is verifiable: he has sustained CEO-level involvement across Tesla, SpaceX, and other ventures for over a decade. His system appears to be built around extreme scheduling discipline rather than delegation.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Balance & Wellbeing &ndash; Level 5</div>
    <p><a href="https://www.sarahknightbooks.com/" target="_blank">Sarah Knight</a> left a high-pressure publishing career in New York to redesign her life around sustainable work rhythms. She went on to write multiple bestselling books about prioritisation and boundary-setting while living in the Dominican Republic, maintaining what she describes as a deliberately structured schedule that protects time for relationships, rest, and enjoyment. Her work focuses specifically on the intersection of productivity and personal wellbeing.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Flexibility & Responsiveness &ndash; Level 5</div>
    <p><a href="https://www.oliverburkeman.com/" target="_blank">Oliver Burkeman</a> spent years as a productivity journalist before writing <em>Four Thousand Weeks</em>, a book that reframes time management around embracing finitude rather than maximising output. He maintains a writing career, family life, and speaking schedule while openly practising a flexible approach to planning that accommodates uncertainty. His system explicitly rejects rigid scheduling in favour of adaptable structures that work across changing circumstances.</p>
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
<h4>Productivity &amp; Achievement</h4>

<div class="assess-input-group" id="ig-focused-hours">
    <span class="assess-label">How many hours of focused, productive work do you complete on a typical work day?</span>
    <span class="assess-hint">Count only time spent on meaningful tasks with genuine concentration &ndash; not meetings, email, or distracted browsing.</span>
    <input type="number" id="a-focused-hours" min="0" max="16" step="0.5" placeholder="e.g. 4" onchange="handleAssessInput('a-focused-hours')"> <span class="assess-percentile-hint" id="pct-focused-hours"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-focused-hours" onchange="handleSkip('a-focused-hours')"><label for="skip-focused-hours">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-task-completion">
    <span class="assess-label">What percentage of your planned tasks do you actually complete in a typical week?</span>
    <span class="assess-hint">Think about last week &ndash; how much of what you intended to do actually got done?</span>
    <select id="a-task-completion" onchange="handleAssessInput('a-task-completion')">
        <option value="">Select...</option>
        <option value="0">Less than 30%</option>
        <option value="1">30 &ndash; 50%</option>
        <option value="2">50 &ndash; 70%</option>
        <option value="3">70 &ndash; 85%</option>
        <option value="4">85 &ndash; 95%</option>
        <option value="5">95%+</option>
    </select> <span class="assess-percentile-hint" id="pct-task-completion"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-task-completion" onchange="handleSkip('a-task-completion')"><label for="skip-task-completion">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-task-system">
    <span class="assess-label">What kind of system do you use to capture and organise tasks?</span>
    <span class="assess-hint">To-do list, calendar, app, notebook, or nothing at all?</span>
    <select id="a-task-system" onchange="handleAssessInput('a-task-system')">
        <option value="">Select...</option>
        <option value="0">No system &ndash; I keep things in my head</option>
        <option value="1">Informal &ndash; occasional notes or lists, not consistent</option>
        <option value="2">Basic &ndash; a consistent to-do list or notebook</option>
        <option value="3">Structured &ndash; a dedicated app or planner with regular reviews</option>
        <option value="4">Advanced &ndash; an integrated system (e.g. time blocking, weekly reviews, task prioritisation)</option>
    </select> <span class="assess-percentile-hint" id="pct-task-system"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-task-system" onchange="handleSkip('a-task-system')"><label for="skip-task-system">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Balance &amp; Wellbeing</h4>

<div class="assess-input-group" id="ig-boundaries">
    <span class="assess-label">How clear are the boundaries between your work time and personal time?</span>
    <span class="assess-hint">Do you have a defined end to your work day, or does work bleed into evenings and weekends?</span>
    <select id="a-boundaries" onchange="handleAssessInput('a-boundaries')">
        <option value="">Select...</option>
        <option value="0">No boundaries &ndash; work and personal time blur together completely</option>
        <option value="1">Weak &ndash; I have a rough idea when to stop but regularly work beyond it</option>
        <option value="2">Moderate &ndash; I usually stop on time but make exceptions several times a week</option>
        <option value="3">Clear &ndash; I have defined hours and stick to them most days</option>
        <option value="4">Strong &ndash; firm boundaries that I protect consistently, with rare exceptions</option>
    </select> <span class="assess-percentile-hint" id="pct-boundaries"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-boundaries" onchange="handleSkip('a-boundaries')"><label for="skip-boundaries">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-breaks">
    <span class="assess-label">How do you manage breaks during focused work?</span>
    <span class="assess-hint">Do you take regular breaks, or do you work until you are exhausted?</span>
    <select id="a-breaks" onchange="handleAssessInput('a-breaks')">
        <option value="">Select...</option>
        <option value="0">No breaks &ndash; I work until I run out of energy or get distracted</option>
        <option value="1">Occasional &ndash; I take breaks when I remember or feel tired</option>
        <option value="2">Fairly regular &ndash; I usually take a break every couple of hours</option>
        <option value="3">Deliberate &ndash; I schedule breaks at set intervals (e.g. Pomodoro, 90-minute blocks)</option>
    </select> <span class="assess-percentile-hint" id="pct-breaks"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-breaks" onchange="handleSkip('a-breaks')"><label for="skip-breaks">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-protected">
    <span class="assess-label">Do you have protected time for relationships, health, and personal interests?</span>
    <span class="assess-hint">Is time for these things scheduled, or do they only happen when work permits?</span>
    <select id="a-protected" onchange="handleAssessInput('a-protected')">
        <option value="">Select...</option>
        <option value="0">No &ndash; personal time only happens if work allows it</option>
        <option value="1">Sometimes &ndash; I try to make time but it is often squeezed out</option>
        <option value="2">Usually &ndash; I have regular personal time most weeks</option>
        <option value="3">Always &ndash; I have scheduled, protected blocks for personal priorities</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-protected" onchange="handleSkip('a-protected')"><label for="skip-protected">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Flexibility &amp; Responsiveness</h4>

<div class="assess-input-group" id="ig-interruptions">
    <span class="assess-label">How well do you handle interruptions during focused work?</span>
    <span class="assess-hint">Think about what happens when someone messages you or an urgent request arrives mid-task.</span>
    <select id="a-interruptions" onchange="handleAssessInput('a-interruptions')">
        <option value="">Select...</option>
        <option value="0">Poorly &ndash; an interruption derails my whole session</option>
        <option value="1">Inconsistently &ndash; sometimes I recover quickly, sometimes I lose the thread</option>
        <option value="2">Fairly well &ndash; I can note the interruption and return to my task within a few minutes</option>
        <option value="3">Well &ndash; I have a system for capturing interruptions and resuming without losing focus</option>
    </select> <span class="assess-percentile-hint" id="pct-interruptions"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-interruptions" onchange="handleSkip('a-interruptions')"><label for="skip-interruptions">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-reprioritise">
    <span class="assess-label">How do you respond when priorities shift mid-week?</span>
    <span class="assess-hint">Do you adjust your plan, or do you try to do everything and end up overwhelmed?</span>
    <select id="a-reprioritise" onchange="handleAssessInput('a-reprioritise')">
        <option value="">Select...</option>
        <option value="0">I try to do everything and usually feel overwhelmed</option>
        <option value="1">I drop things reactively, without a clear process for deciding what gives</option>
        <option value="2">I reprioritise deliberately, though it takes effort</option>
        <option value="3">I reprioritise smoothly &ndash; I have a clear process for adjusting plans</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-reprioritise" onchange="handleSkip('a-reprioritise')"><label for="skip-reprioritise">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-contexts">
    <span class="assess-label">Does your time management approach work across different contexts?</span>
    <span class="assess-hint">Does your system travel with you (work, home, travel), or does it only work at your desk?</span>
    <select id="a-contexts" onchange="handleAssessInput('a-contexts')">
        <option value="">Select...</option>
        <option value="0">It only works in one context &ndash; I have no system outside that setting</option>
        <option value="1">It mostly works in one context but partially transfers to others</option>
        <option value="2">It works across most contexts with some adaptation</option>
        <option value="3">It works reliably in any context I find myself in</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-contexts" onchange="handleSkip('a-contexts')"><label for="skip-contexts">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-productivity">
        <span class="assess-summary-label">Productivity &amp; Achievement</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-productivity" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-productivity">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-balance">
        <span class="assess-summary-label">Balance &amp; Wellbeing</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-balance" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-balance">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published research on time management practices among working adults. Flexibility &amp; Responsiveness items are recorded for your awareness but not scored, as the available data does not support reliable percentile estimates.</p>
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

<p>You now understand why time management matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about productivity and achievement, balance and wellbeing, and flexibility and responsiveness. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/time-management/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Time Management Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Time Management. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/time-management/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'time-management';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-focused-hours', 'a-task-completion', 'a-task-system',
        'a-boundaries', 'a-breaks', 'a-protected',
        'a-interruptions', 'a-reprioritise', 'a-contexts'
    ];

    // Scoring thresholds: [{value, percentile}, ...] sorted by value ascending
    // Sources: time management research, productivity studies, workplace surveys
    var THRESHOLDS = {
        'a-focused-hours': [
            {v:0,p:5},{v:1,p:15},{v:2,p:30},{v:3,p:50},{v:4,p:70},{v:5,p:82},{v:6,p:90},{v:8,p:96}
        ],
        'a-task-completion': [
            {v:'0',p:10},{v:'1',p:25},{v:'2',p:45},{v:'3',p:65},{v:'4',p:82},{v:'5',p:95}
        ],
        'a-task-system': [
            {v:'0',p:15},{v:'1',p:35},{v:'2',p:55},{v:'3',p:78},{v:'4',p:93}
        ],
        'a-boundaries': [
            {v:'0',p:15},{v:'1',p:35},{v:'2',p:55},{v:'3',p:75},{v:'4',p:92}
        ],
        'a-breaks': [
            {v:'0',p:20},{v:'1',p:40},{v:'2',p:65},{v:'3',p:88}
        ],
        'a-interruptions': [
            {v:'0',p:15},{v:'1',p:40},{v:'2',p:65},{v:'3',p:88}
        ]
    };

    var VALUE_ITEMS = {
        productivity: ['a-focused-hours', 'a-task-completion', 'a-task-system'],
        balance: ['a-boundaries', 'a-breaks']
    };

    // Flexibility items and some balance items are recorded but not scored
    // (insufficient population data for reliable percentile estimates)
    var UNSCORED_ITEMS = ['a-protected', 'a-reprioritise', 'a-contexts'];

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
        var num = parseFloat(value);
        // Check if thresholds use string keys (dropdowns)
        if (typeof thresholds[0].v === 'string') {
            for (var i = 0; i < thresholds.length; i++) {
                if (thresholds[i].v === String(value)) return thresholds[i].p;
            }
            return null;
        }
        // Numeric interpolation
        if (num <= thresholds[0].v) return thresholds[0].p;
        if (num >= thresholds[thresholds.length - 1].v) return thresholds[thresholds.length - 1].p;
        for (var i = 0; i < thresholds.length - 1; i++) {
            if (num >= thresholds[i].v && num <= thresholds[i + 1].v) {
                var t = (num - thresholds[i].v) / (thresholds[i + 1].v - thresholds[i].v);
                return Math.round(thresholds[i].p + t * (thresholds[i + 1].p - thresholds[i].p));
            }
        }
        return null;
    }

    function getItemPercentile(itemId) {
        if (UNSCORED_ITEMS.indexOf(itemId) !== -1) return null;
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return null;
        if (!THRESHOLDS[itemId]) return null;

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

    function isItemAnswered(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return true;

        var el = document.getElementById(itemId);
        return el && el.value !== '' && el.value !== null;
    }

    function updatePercentileHint(itemId) {
        if (UNSCORED_ITEMS.indexOf(itemId) !== -1) return; // no hints for unscored items
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

    function updateInputGroupState(itemId) {
        var group = document.getElementById('ig-' + itemId.replace('a-', ''));
        if (group) group.classList.toggle('answered', isItemAnswered(itemId));
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['productivity', 'balance'].forEach(function(vk) {
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
        ['productivity', 'balance'].forEach(function(vk) {
            scores[vk] = computeValuePercentile(vk);
        });
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-scores') || {};
            all[AREA] = scores;
            APStorage.save('ap-level1-scores', all);
        }
    }

    function updateAssessCompletion() {
        var allAnswered = ASSESS_IDS.every(function(id) { return isItemAnswered(id); });
        var btn = document.getElementById('assessBtn');
        if (btn) {
            btn.disabled = !allAnswered;
            btn.textContent = allAnswered ? 'All done \u2013 continue' : 'Answer all items to continue';
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
            if (skipBox.checked && input.type === 'number') input.value = '';
        }
        updatePercentileHint(itemId);
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessSummary();
        updateAssessCompletion();
    };

    // Override completeStep to also save scores
    var _origCompleteStep = window.completeStep;
    window.completeStep = function(step) {
        if (step === 'assess') saveScores();
        _origCompleteStep(step);
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
