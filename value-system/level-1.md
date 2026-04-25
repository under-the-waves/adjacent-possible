---
layout: default
title: "Value System – Level 1: Awareness"
life_area_slug: value-system
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

<h1>Value System: Level 1</h1>

<p class="l1-subtitle">Understand what a value system is, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Value System Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why your value system matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Most people operate from values they absorbed in childhood &ndash; from family, religion, peer groups, and culture &ndash; without ever examining whether those values are genuinely theirs. Research on <a href="https://www.britannica.com/science/Lawrence-Kohlbergs-stages-of-moral-development" target="_blank">moral development</a> suggests only 10 &ndash; 15% of adults reason from consciously examined principles rather than social convention.</p>

<p>The practical cost of unexamined values is substantial. People without clear priorities tend to experience more <a href="https://www.apa.org/news/press/releases/stress" target="_blank">decision fatigue</a>, more regret after major choices, and a persistent sense that they are living someone else's life. Clarifying your values does not guarantee good outcomes, but it does mean your decisions reflect what you actually care about rather than what you were told to care about.</p>

<p>Values work also affects how you handle pressure. Studies on <a href="https://doi.org/10.1177/0146167211436733" target="_blank">self-affirmation theory</a> show that people who can articulate their core values are measurably more resilient under stress, less defensive when receiving critical feedback, and better able to maintain their priorities when circumstances shift.</p>

<p>Perhaps most importantly, a clear value system gives you a basis for saying no. Without one, you tend to default to whatever is most urgent, most socially rewarded, or most comfortable &ndash; none of which reliably track what matters most.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about a value system</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People do values work for different reasons. This site scores every value system intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Practical Decision-Making</h3>
<p>Having a values framework that actively improves daily choices and major life decisions. People who lean towards this value want clear guidance that reduces decision fatigue and increases confidence in choices. They treat values as stable inputs to efficient decision processes &ndash; tools for resource allocation, career moves, and life direction.</p>

<h3>Comprehensive Insight</h3>
<p>Deep understanding of your authentic values, including recognising inherited versus genuine values, understanding value hierarchies and trade-offs, and knowing when enough is enough for different values. People who lean towards this value focus on thorough discovery and analysis &ndash; achieving clarity about what truly matters and why.</p>

<h3>Authentic Expression</h3>
<p>The courage to live in alignment with your discovered values even when they conflict with social expectations, family pressure, or external incentives. People who lean towards this value prioritise congruence between inner beliefs and outer behaviour &ndash; being true to themselves over efficiency or social approval.</p>

<h3>Values Evolution</h3>
<p>Viewing values as potentially changeable and being open to intentional value development through new experiences, reflection, and life transitions. People who lean towards this value treat values work as ongoing growth rather than one-time discovery, regularly reassessing whether current values still serve them.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each value system value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Practical Decision-Making &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Charlie_Munger" target="_blank">Charlie Munger</a> built his investment career around a set of explicit mental models and decision-making principles that he maintained for over 60 years. He kept a checklist of cognitive biases to guard against, publicly turned down investments that violated his principles regardless of profit potential, and repeatedly described his approach as "invert, always invert" &ndash; testing every decision against what could go wrong. His partnership with Warren Buffett appears to have been grounded in shared values more than shared strategy.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Comprehensive Insight &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Derek_Parfit" target="_blank">Derek Parfit</a> spent his career at Oxford examining the foundations of ethics and personal identity. His book <em>Reasons and Persons</em> (1984) systematically dismantled common assumptions about self-interest, rationality, and what makes a life go well. Colleagues consistently described him as someone whose philosophical conclusions visibly shaped his daily conduct &ndash; he lived with unusual frugality, gave away a large share of his income, and appeared to treat the examined life as a genuine practice rather than an academic exercise.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Authentic Expression &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Václav_Havel" target="_blank">V&aacute;clav Havel</a> spent two decades as a dissident playwright in communist Czechoslovakia, repeatedly imprisoned for writing and speaking according to his values. His 1978 essay "The Power of the Powerless" argued that living authentically &ndash; refusing to participate in official lies &ndash; was itself a political act. When the regime fell in 1989, he became president, applying the same principles to governance. His consistency between private conviction and public action across dramatically different circumstances is well documented.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Values Evolution &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Mahatma_Gandhi" target="_blank">Mahatma Gandhi</a> revised his values publicly and repeatedly over a 50-year period. He started as a conventional lawyer seeking acceptance within the British Empire, adopted nonviolent resistance after experiences in South Africa, and later evolved his views on caste, religion, and economic organisation as his understanding deepened. His autobiography, <em>The Story of My Experiments with Truth</em>, frames his life explicitly as a process of testing and revising values through lived experience.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know straight away, others might take a few minutes of honest reflection.</p>

<div class="assess-group">
<h4>Practical Decision-Making</h4>

<div class="assess-input-group" id="ig-core-values">
    <span class="assess-label">How many of your core values could you name right now?</span>
    <span class="assess-hint">These might include things like honesty, autonomy, compassion, achievement, security, creativity, or fairness.</span>
    <select id="a-core-values" onchange="handleAssessInput('a-core-values')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I haven't thought about this</option>
        <option value="vague">I have a vague sense but couldn't name specifics</option>
        <option value="one-two">I could name one or two</option>
        <option value="three-five">I could name three to five with confidence</option>
        <option value="ranked">I could name and rank them in order of importance</option>
    </select> <span class="assess-percentile-hint" id="pct-core-values"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-core-values" onchange="handleSkip('a-core-values')"><label for="skip-core-values">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-recent-decision">
    <span class="assess-label">How recently did you consciously consider your values when making a major decision?</span>
    <span class="assess-hint">A career move, relationship choice, large purchase, or life change where you weighed what mattered most.</span>
    <select id="a-recent-decision" onchange="handleAssessInput('a-recent-decision')">
        <option value="">Select...</option>
        <option value="never">I don't think I've ever done this consciously</option>
        <option value="years">Several years ago</option>
        <option value="past-year">Within the past year</option>
        <option value="recent">Within the past few months</option>
        <option value="routine">I do this routinely for important decisions</option>
    </select> <span class="assess-percentile-hint" id="pct-recent-decision"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-recent-decision" onchange="handleSkip('a-recent-decision')"><label for="skip-recent-decision">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-decision-regret">
    <span class="assess-label">How do you typically feel after important decisions?</span>
    <span class="assess-hint">Persistent regret often signals a gap between choices and underlying values.</span>
    <select id="a-decision-regret" onchange="handleAssessInput('a-decision-regret')">
        <option value="">Select...</option>
        <option value="frequent-regret">Frequently regretful &ndash; I often wish I'd chosen differently</option>
        <option value="some-regret">Some regret &ndash; a nagging sense I didn't choose well</option>
        <option value="uncertain">Uncertain &ndash; I second-guess myself but it fades</option>
        <option value="mostly-confident">Mostly confident &ndash; I generally feel good about my choices</option>
        <option value="very-confident">Very confident &ndash; my decisions feel aligned with what matters to me</option>
    </select> <span class="assess-percentile-hint" id="pct-decision-regret"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-decision-regret" onchange="handleSkip('a-decision-regret')"><label for="skip-decision-regret">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Comprehensive Insight</h4>

<div class="assess-input-group" id="ig-inherited">
    <span class="assess-label">How much have you examined which of your values came from family or culture versus which you've consciously chosen?</span>
    <span class="assess-hint">Consider religious beliefs, attitudes to money, views on success, or political leanings you grew up with.</span>
    <select id="a-inherited" onchange="handleAssessInput('a-inherited')">
        <option value="">Select...</option>
        <option value="not-considered">I haven't thought about this</option>
        <option value="aware">I'm aware some values are inherited but haven't examined which</option>
        <option value="partially">I've examined some areas (e.g. religion or politics) but not others</option>
        <option value="thorough">I've done a thorough review and can distinguish inherited from chosen</option>
        <option value="ongoing">I revisit this regularly as part of ongoing self-examination</option>
    </select> <span class="assess-percentile-hint" id="pct-inherited"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-inherited" onchange="handleSkip('a-inherited')"><label for="skip-inherited">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-conflict">
    <span class="assess-label">Can you identify situations where two of your values conflict with each other?</span>
    <span class="assess-hint">For example, valuing both ambition and work-life balance, or both honesty and kindness.</span>
    <select id="a-conflict" onchange="handleAssessInput('a-conflict')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I haven't noticed any conflicts</option>
        <option value="maybe">I suspect there are conflicts but can't name them</option>
        <option value="one">I can identify one clear conflict</option>
        <option value="several">I can identify several and I've thought about how to manage them</option>
        <option value="resolved">I've developed explicit rules for how to handle my recurring value conflicts</option>
    </select> <span class="assess-percentile-hint" id="pct-conflict"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-conflict" onchange="handleSkip('a-conflict')"><label for="skip-conflict">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-enough">
    <span class="assess-label">Do you have a sense of "enough" for any of your values &ndash; a point where pursuing it further stops adding to your wellbeing?</span>
    <span class="assess-hint">For instance, knowing how much financial security is enough, or how much achievement satisfies you.</span>
    <select id="a-enough" onchange="handleAssessInput('a-enough')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I haven't thought about limits on any of my values</option>
        <option value="vague">I have a vague sense for one or two values but nothing specific</option>
        <option value="one">I have a clear "enough" point for at least one value</option>
        <option value="several">I have clear limits for several values and they guide my decisions</option>
    </select> <span class="assess-percentile-hint" id="pct-enough"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-enough" onchange="handleSkip('a-enough')"><label for="skip-enough">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Authentic Expression</h4>

<div class="assess-input-group" id="ig-social-pressure">
    <span class="assess-label">How often do you act against your values because of social pressure or fear of judgement?</span>
    <span class="assess-hint">Times you went along with something you disagreed with, or stayed silent when you wanted to speak up.</span>
    <select id="a-social-pressure" onchange="handleAssessInput('a-social-pressure')">
        <option value="">Select...</option>
        <option value="often">Often &ndash; I regularly compromise my values to fit in</option>
        <option value="sometimes">Sometimes &ndash; I notice it happening in certain contexts</option>
        <option value="rarely">Rarely &ndash; I mostly hold my ground but occasionally bend</option>
        <option value="almost-never">Almost never &ndash; I've consciously developed the habit of living by my values</option>
    </select> <span class="assess-percentile-hint" id="pct-social-pressure"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-social-pressure" onchange="handleSkip('a-social-pressure')"><label for="skip-social-pressure">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-alignment">
    <span class="assess-label">How well does your daily life align with your stated values?</span>
    <span class="assess-hint">Consider how you spend your time, money, and energy. Do those patterns reflect what you say matters?</span>
    <select id="a-alignment" onchange="handleAssessInput('a-alignment')">
        <option value="">Select...</option>
        <option value="poor">Poorly &ndash; there's a big gap between what I say and what I do</option>
        <option value="somewhat">Somewhat &ndash; some areas align, others clearly don't</option>
        <option value="mostly">Mostly &ndash; my life broadly reflects my values with some exceptions</option>
        <option value="well">Well &ndash; I've deliberately structured my life around my values</option>
    </select> <span class="assess-percentile-hint" id="pct-alignment"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-alignment" onchange="handleSkip('a-alignment')"><label for="skip-alignment">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Values Evolution</h4>

<div class="assess-input-group" id="ig-changed">
    <span class="assess-label">Has at least one of your values changed significantly since your early adulthood?</span>
    <span class="assess-hint">Something you used to prioritise that you no longer do, or vice versa.</span>
    <select id="a-changed" onchange="handleAssessInput('a-changed')">
        <option value="">Select...</option>
        <option value="no">No &ndash; my values have stayed the same as far as I can tell</option>
        <option value="maybe">Maybe &ndash; I think some have shifted but I'm not sure which</option>
        <option value="yes-one">Yes &ndash; I can identify one clear change</option>
        <option value="yes-several">Yes &ndash; several values have changed and I understand why</option>
        <option value="intentional">Yes &ndash; I've intentionally revised my values based on experience and reflection</option>
    </select> <span class="assess-percentile-hint" id="pct-changed"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-changed" onchange="handleSkip('a-changed')"><label for="skip-changed">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-practical">
        <span class="assess-summary-label">Practical Decision-Making</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-practical" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-practical">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-insight">
        <span class="assess-summary-label">Comprehensive Insight</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-insight" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-insight">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-authentic">
        <span class="assess-summary-label">Authentic Expression</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-authentic" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-authentic">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-evolution">
        <span class="assess-summary-label">Values Evolution</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-evolution" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-evolution">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published research on values articulation, moral development, and self-examination among adults. All items in this area are scored.</p>
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

<p>You now understand why a value system matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about practical decision-making, comprehensive insight, authentic expression, and values evolution. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/value-system/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Value System Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Value System. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/value-system/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'value-system';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-core-values', 'a-recent-decision', 'a-decision-regret',
        'a-inherited', 'a-conflict', 'a-enough',
        'a-social-pressure', 'a-alignment',
        'a-changed'
    ];

    var UNSCORED_ITEMS = [];

    var THRESHOLDS = {
        'a-core-values': [
            {v:'none',p:8},{v:'vague',p:25},{v:'one-two',p:48},{v:'three-five',p:78},{v:'ranked',p:95}
        ],
        'a-recent-decision': [
            {v:'never',p:10},{v:'years',p:28},{v:'past-year',p:50},{v:'recent',p:75},{v:'routine',p:95}
        ],
        'a-decision-regret': [
            {v:'frequent-regret',p:8},{v:'some-regret',p:25},{v:'uncertain',p:48},{v:'mostly-confident',p:75},{v:'very-confident',p:95}
        ],
        'a-inherited': [
            {v:'not-considered',p:8},{v:'aware',p:25},{v:'partially',p:50},{v:'thorough',p:80},{v:'ongoing',p:95}
        ],
        'a-conflict': [
            {v:'no',p:10},{v:'maybe',p:28},{v:'one',p:50},{v:'several',p:78},{v:'resolved',p:95}
        ],
        'a-enough': [
            {v:'no',p:10},{v:'vague',p:32},{v:'one',p:58},{v:'several',p:92}
        ],
        'a-social-pressure': [
            {v:'often',p:10},{v:'sometimes',p:32},{v:'rarely',p:62},{v:'almost-never',p:92}
        ],
        'a-alignment': [
            {v:'poor',p:8},{v:'somewhat',p:30},{v:'mostly',p:58},{v:'well',p:92}
        ],
        'a-changed': [
            {v:'no',p:10},{v:'maybe',p:28},{v:'yes-one',p:48},{v:'yes-several',p:75},{v:'intentional',p:95}
        ],
    };

    var VALUE_ITEMS = {
        practical: ['a-core-values', 'a-recent-decision', 'a-decision-regret'],
        insight: ['a-inherited', 'a-conflict', 'a-enough'],
        authentic: ['a-social-pressure', 'a-alignment'],
        evolution: ['a-changed'],
    };

    // --- Scoring functions ---

    function ordinalSuffix(n) {
        var s = ['th','st','nd','rd'];
        var v = n % 100;
        return n + (s[(v-20)%10] || s[v] || s[0]);
    }
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
        hintEl.textContent = pct !== null ? 'roughly ' + ordinalSuffix(Math.round(pct / 10) * 10) + ' percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['practical', 'insight', 'authentic', 'evolution'].forEach(function(vk) {
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
        ['practical', 'insight', 'authentic', 'evolution'].forEach(function(vk) {
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
