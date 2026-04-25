---
layout: default
title: "Rationality – Level 1: Awareness"
life_area_slug: rationality
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

<h1>Rationality: Level 1</h1>

<p class="l1-subtitle">Understand what rationality means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Rationality Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why rationality matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>The quality of your thinking shapes nearly every outcome in your life. Career choices, financial decisions, relationships, health habits &ndash; all of these depend on how well you reason under uncertainty, how accurately you model the world, and how reliably you can identify the best course of action.</p>

<p>Most people overestimate the accuracy of their beliefs and the quality of their decisions. Research on <a href="https://www.sciencedirect.com/science/article/pii/S0010028516300421" target="_blank">calibration</a> consistently shows that people's confidence in their judgements tends to exceed their actual accuracy. This gap between perceived and real reasoning ability is one of the most robust findings in psychology.</p>

<p>The good news is that reasoning skills are trainable. Studies from the <a href="https://goodjudgment.com/resources/the-good-judgment-project/" target="_blank">Good Judgment Project</a> found that relatively brief training in probabilistic thinking and bias recognition improved forecasting accuracy by around 30%. Participants who practised structured reasoning outperformed professional intelligence analysts with access to classified information.</p>

<p>Rationality also serves as a multiplier for other life areas. Better reasoning about nutrition evidence helps you eat well. Clearer thinking about financial risk helps you invest wisely. More accurate models of other people help you build stronger relationships. Few skills compound across as many domains.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about rationality</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People develop their thinking for different reasons. This site scores every rationality intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Accurate Beliefs</h3>
<p>Developing more accurate beliefs about how the world actually works. Better calibration (your confidence matching actual accuracy), making more accurate forecasts and predictions, updating appropriately when presented with new evidence, and building superior mental models and heuristics for navigating complexity. People who lean towards this value focus on the outcomes of thinking &ndash; actually having true beliefs and understanding reality correctly, even when the truth is inconvenient or uncomfortable.</p>

<h3>Effective Decision-Making</h3>
<p>Using clear thinking to achieve your actual goals across all life domains. Avoiding costly mistakes from cognitive biases, developing systematic approaches to complex choices, improving your track record of successful outcomes, and building effective models and heuristics for practical decision-making. People who lean towards this value see rationality as a practical toolkit for getting what they want more reliably and avoiding expensive errors in judgement.</p>

<h3>Intellectual Honesty</h3>
<p>Maintaining truthful reasoning processes and admitting uncertainty appropriately. Changing your mind when evidence warrants it, acknowledging the limits of your knowledge, following arguments where they lead even when conclusions are personally uncomfortable, and recognising when your reasoning is motivated by comfort rather than truth. People who lean towards this value focus on the process of thinking &ndash; maintaining genuine truth-seeking as important in itself, regardless of whether it leads to immediately better outcomes.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each rationality value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Accurate Beliefs &ndash; Level 5</div>
    <p><a href="https://www.gjopen.com/" target="_blank">The top superforecasters</a> from the Good Judgment Project consistently outperformed professional intelligence analysts by 30% or more, despite having no access to classified information. These individuals &ndash; ordinary people with no special credentials &ndash; achieved this through disciplined calibration, granular probability estimates, and systematic belief updating. Over four years of geopolitical forecasting tournaments funded by IARPA, the best of them maintained Brier scores that placed them in the top fraction of a percent of all participants.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Effective Decision-Making &ndash; Level 5</div>
    <p><a href="https://fs.blog/annie-duke/" target="_blank">Annie Duke</a> was one of the top female poker players in history, winning a World Series of Poker bracelet and over $4 million in tournament earnings. She later applied the same structured decision-making frameworks &ndash; expected value calculations, separating decision quality from outcome quality, pre-mortems &ndash; to advising organisations and writing on decision science. Her track record spans thousands of high-stakes decisions under genuine uncertainty, with verifiable outcomes.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Intellectual Honesty &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Douglas_Hofstadter" target="_blank">Douglas Hofstadter</a> has spent decades publicly grappling with questions about consciousness, cognition, and artificial intelligence, consistently revising his positions as evidence and arguments demanded. Despite his strong initial scepticism about AI systems replicating aspects of human thought, he has openly acknowledged being shaken by recent developments and has discussed the discomfort of confronting evidence that challenges his life's work. This willingness to sit with uncertainty on questions central to his identity is unusual among prominent intellectuals.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to reflect on.</p>

<div class="assess-group">
<h4>Accurate Beliefs</h4>

<div class="assess-input-group" id="ig-calibration">
    <span class="assess-label">How well calibrated is your confidence?</span>
    <span class="assess-hint">When you say 'I'm 90% sure', are you actually right about 90% of the time? Most people are right considerably less often than their confidence suggests.</span>
    <select id="a-calibration" onchange="handleAssessInput('a-calibration')">
        <option value="">Select...</option>
        <option value="no-idea">No idea &ndash; I've never thought about this</option>
        <option value="overconfident">Probably overconfident &ndash; I suspect I'm wrong more often than I think</option>
        <option value="somewhat">Somewhat calibrated &ndash; I notice when I'm uncertain but don't track it</option>
        <option value="good">Good &ndash; I'm usually aware of how confident I should be</option>
        <option value="tracked">I've tested my calibration and it's reasonably accurate</option>
    </select> <span class="assess-percentile-hint" id="pct-calibration"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-calibration" onchange="handleSkip('a-calibration')"><label for="skip-calibration">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-predictions">
    <span class="assess-label">How recently can you recall a prediction you made and whether it turned out to be accurate?</span>
    <span class="assess-hint">This could be about work, politics, sports, relationships &ndash; any forward-looking claim you made.</span>
    <select id="a-predictions" onchange="handleAssessInput('a-predictions')">
        <option value="">Select...</option>
        <option value="cant-recall">I can't recall any specific predictions</option>
        <option value="vague">I have a vague sense but couldn't cite a specific example</option>
        <option value="one">I can recall one recent prediction and its outcome</option>
        <option value="several">I can recall several and I have a sense of my accuracy</option>
        <option value="tracked">I track predictions systematically and know my hit rate</option>
    </select> <span class="assess-percentile-hint" id="pct-predictions"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-predictions" onchange="handleSkip('a-predictions')"><label for="skip-predictions">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-updating">
    <span class="assess-label">How recently have you changed a belief based on new evidence?</span>
    <span class="assess-hint">This could be about anything &ndash; a factual claim, an opinion about a person, a view on how something works.</span>
    <select id="a-updating" onchange="handleAssessInput('a-updating')">
        <option value="">Select...</option>
        <option value="cant-recall">I can't recall changing a belief</option>
        <option value="years">Years ago &ndash; my views have been stable for a long time</option>
        <option value="past-year">Within the past year</option>
        <option value="recently">Within the past few months</option>
        <option value="regularly">I update beliefs regularly and can give multiple recent examples</option>
    </select> <span class="assess-percentile-hint" id="pct-updating"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-updating" onchange="handleSkip('a-updating')"><label for="skip-updating">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Effective Decision-Making</h4>

<div class="assess-input-group" id="ig-past-decisions">
    <span class="assess-label">How sound was your decision-making process for a recent significant decision?</span>
    <span class="assess-hint">Think about how you made the decision, not just whether it worked out. Good processes sometimes produce bad outcomes and vice versa.</span>
    <select id="a-past-decisions" onchange="handleAssessInput('a-past-decisions')">
        <option value="">Select...</option>
        <option value="no-process">No process &ndash; I went with my gut or defaulted to the easiest option</option>
        <option value="informal">Informal &ndash; I thought about it but without any structure</option>
        <option value="some-structure">Some structure &ndash; I considered pros and cons or sought advice</option>
        <option value="systematic">Systematic &ndash; I used a deliberate framework and considered alternatives</option>
        <option value="rigorous">Rigorous &ndash; I used multiple frameworks, sought disconfirming evidence, and stress-tested my reasoning</option>
    </select> <span class="assess-percentile-hint" id="pct-past-decisions"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-past-decisions" onchange="handleSkip('a-past-decisions')"><label for="skip-past-decisions">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-frameworks">
    <span class="assess-label">Do you use any structured approach when facing important decisions?</span>
    <span class="assess-hint">Pros/cons lists, decision matrices, seeking outside views, pre-mortems, expected value calculations &ndash; or nothing systematic at all.</span>
    <select id="a-frameworks" onchange="handleAssessInput('a-frameworks')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I don't use any structured approach</option>
        <option value="basic">Basic &ndash; I sometimes make a pros/cons list</option>
        <option value="moderate">Moderate &ndash; I have a few tools I use for bigger decisions</option>
        <option value="strong">Strong &ndash; I have a reliable toolkit I apply consistently</option>
        <option value="advanced">Advanced &ndash; I use multiple frameworks and adapt them to the decision type</option>
    </select> <span class="assess-percentile-hint" id="pct-frameworks"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-frameworks" onchange="handleSkip('a-frameworks')"><label for="skip-frameworks">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-biases">
    <span class="assess-label">How many cognitive biases can you name that have likely affected your decisions?</span>
    <span class="assess-hint">Sunk cost fallacy, confirmation bias, anchoring, status quo bias &ndash; or perhaps you're not sure what these terms mean yet.</span>
    <select id="a-biases" onchange="handleAssessInput('a-biases')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I'm not familiar with cognitive biases</option>
        <option value="heard">I've heard the terms but couldn't explain them</option>
        <option value="one-two">I can name one or two and recall them affecting me</option>
        <option value="several">I can name several and I watch for them actively</option>
        <option value="systematic">I have systematic strategies to counteract my most common biases</option>
    </select> <span class="assess-percentile-hint" id="pct-biases"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-biases" onchange="handleSkip('a-biases')"><label for="skip-biases">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Intellectual Honesty</h4>

<div class="assess-input-group" id="ig-motivated">
    <span class="assess-label">How aware are you of beliefs you might hold because they're comforting rather than because the evidence supports them?</span>
    <span class="assess-hint">Politics, religion, career choices, relationships &ndash; areas where being wrong would be personally costly or uncomfortable.</span>
    <select id="a-motivated" onchange="handleAssessInput('a-motivated')">
        <option value="">Select...</option>
        <option value="unaware">Unaware &ndash; I haven't thought about this</option>
        <option value="suspect">I suspect it's happening but can't identify where</option>
        <option value="one-area">I can identify one or two areas where my reasoning may be motivated</option>
        <option value="several">I can identify several and I actively work to counteract it</option>
        <option value="vigilant">I'm vigilant about this and regularly test my beliefs for motivated reasoning</option>
    </select> <span class="assess-percentile-hint" id="pct-motivated"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-motivated" onchange="handleSkip('a-motivated')"><label for="skip-motivated">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-disagreement">
    <span class="assess-label">How do you typically react when someone disagrees with you on something you care about?</span>
    <span class="assess-hint">Do you get defensive? Curious? Dismissive? Do you engage with their actual argument or focus on finding flaws?</span>
    <select id="a-disagreement" onchange="handleAssessInput('a-disagreement')">
        <option value="">Select...</option>
        <option value="defensive">Defensive &ndash; I feel attacked and push back</option>
        <option value="dismissive">Dismissive &ndash; I tend to discount the other person's view</option>
        <option value="mixed">Mixed &ndash; sometimes curious, sometimes defensive depending on the topic</option>
        <option value="curious">Usually curious &ndash; I try to understand their reasoning</option>
        <option value="actively-seeking">I actively seek out disagreement because it helps me think better</option>
    </select> <span class="assess-percentile-hint" id="pct-disagreement"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-disagreement" onchange="handleSkip('a-disagreement')"><label for="skip-disagreement">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-uncertainty">
    <span class="assess-label">How comfortable are you saying 'I don't know' on important questions?</span>
    <span class="assess-hint">This is harder than it sounds. Most people have opinions on most topics, even when the evidence is genuinely unclear.</span>
    <select id="a-uncertainty" onchange="handleAssessInput('a-uncertainty')">
        <option value="">Select...</option>
        <option value="uncomfortable">Very uncomfortable &ndash; I feel I should have an opinion on everything</option>
        <option value="reluctant">Reluctant &ndash; I'll offer a view even when I'm not sure</option>
        <option value="sometimes">Sometimes comfortable &ndash; depends on the topic and audience</option>
        <option value="comfortable">Comfortable &ndash; I can identify several important questions where I'm genuinely unsure</option>
        <option value="natural">Natural &ndash; I default to uncertainty and require evidence before forming views</option>
    </select> <span class="assess-percentile-hint" id="pct-uncertainty"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-uncertainty" onchange="handleSkip('a-uncertainty')"><label for="skip-uncertainty">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-beliefs">
        <span class="assess-summary-label">Accurate Beliefs</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-beliefs" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-beliefs">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-decisions">
        <span class="assess-summary-label">Effective Decision-Making</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-decisions" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-decisions">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-honesty">
        <span class="assess-summary-label">Intellectual Honesty</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-honesty" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-honesty">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published data on calibration practices, decision-making habits, cognitive bias awareness, and intellectual humility research. All items in this area are scored.</p>
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

<p>You now understand why rationality matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about accurate beliefs, effective decision-making, and intellectual honesty. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/rationality/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Rationality Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Rationality. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/rationality/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'rationality';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-calibration', 'a-predictions', 'a-updating',
        'a-past-decisions', 'a-frameworks', 'a-biases',
        'a-motivated', 'a-disagreement', 'a-uncertainty'
    ];

    var THRESHOLDS = {
        'a-calibration': [
            // ~80% have never thought about calibration; tested and accurate is ~3%
            {v:'no-idea',p:10},{v:'overconfident',p:30},{v:'somewhat',p:55},{v:'good',p:78},{v:'tracked',p:97}
        ],
        'a-predictions': [
            // ~60% can't recall specific predictions; systematic tracking is ~2%
            {v:'cant-recall',p:10},{v:'vague',p:30},{v:'one',p:55},{v:'several',p:78},{v:'tracked',p:97}
        ],
        'a-updating': [
            // ~30% can't recall changing a belief; regular updating with examples is ~10%
            {v:'cant-recall',p:8},{v:'years',p:25},{v:'past-year',p:50},{v:'recently',p:75},{v:'regularly',p:95}
        ],
        'a-past-decisions': [
            // ~45% use no process for decisions; rigorous multi-framework approach is ~5%
            {v:'no-process',p:10},{v:'informal',p:32},{v:'some-structure',p:55},{v:'systematic',p:80},{v:'rigorous',p:97}
        ],
        'a-frameworks': [
            // ~55% use no structured approach; advanced multi-framework use is ~5%
            {v:'none',p:10},{v:'basic',p:32},{v:'moderate',p:55},{v:'strong',p:80},{v:'advanced',p:97}
        ],
        'a-biases': [
            // ~40% are unfamiliar with cognitive biases; systematic countermeasures is ~5%
            {v:'none',p:10},{v:'heard',p:30},{v:'one-two',p:55},{v:'several',p:78},{v:'systematic',p:97}
        ],
        'a-motivated': [
            // ~50% are unaware of motivated reasoning; vigilant testing is ~5%
            {v:'unaware',p:10},{v:'suspect',p:30},{v:'one-area',p:55},{v:'several',p:78},{v:'vigilant',p:97}
        ],
        'a-disagreement': [
            // ~35% react defensively; actively seeking disagreement is ~8%
            {v:'defensive',p:8},{v:'dismissive',p:22},{v:'mixed',p:48},{v:'curious',p:75},{v:'actively-seeking',p:95}
        ],
        'a-uncertainty': [
            // ~40% are uncomfortable with "I don't know"; defaulting to uncertainty is ~8%
            {v:'uncomfortable',p:8},{v:'reluctant',p:25},{v:'sometimes',p:50},{v:'comfortable',p:78},{v:'natural',p:95}
        ]
    };

    var VALUE_ITEMS = {
        beliefs: ['a-calibration', 'a-predictions', 'a-updating'],
        decisions: ['a-past-decisions', 'a-frameworks', 'a-biases'],
        honesty: ['a-motivated', 'a-disagreement', 'a-uncertainty']
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
        ['beliefs', 'decisions', 'honesty'].forEach(function(vk) {
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
        ['beliefs', 'decisions', 'honesty'].forEach(function(vk) {
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
