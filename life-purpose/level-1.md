---
layout: default
title: "Life Purpose – Level 1: Awareness"
life_area_slug: life-purpose
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

<h1>Life Purpose: Level 1</h1>

<p class="l1-subtitle">Understand what life purpose means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Life Purpose Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why life purpose matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Having a clear sense of purpose is one of the strongest predictors of psychological wellbeing across cultures and age groups. The evidence connects purpose to outcomes in health, resilience, and overall life satisfaction.</p>

<p>People with a well-defined sense of purpose show <a href="https://psycnet.apa.org/record/2016-17273-001" target="_blank">roughly 40% greater resilience</a> during major life stressors, recovering more quickly from setbacks and maintaining perspective during difficulties. They also tend to score <a href="https://psycnet.apa.org/record/2009-05474-001" target="_blank">25 &ndash; 30% higher</a> on life satisfaction measures and report lower rates of depression and anxiety.</p>

<p>Purpose also affects physical health. A <a href="https://journals.sagepub.com/doi/10.1177/0956797619831612" target="_blank">meta-analysis of over 136,000 participants</a> found that having a strong sense of purpose was associated with reduced all-cause mortality. The mechanism likely involves better health behaviours, lower chronic stress, and stronger social connections &ndash; all of which tend to follow from purposeful living.</p>

<p>Perhaps most practically, purpose improves the quality of everyday decisions. When you know what matters to you, it becomes easier to evaluate opportunities, say no to distractions, and commit to long-term projects without constant second-guessing.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about life purpose</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People develop life purpose for different reasons. This site scores every life purpose intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Clarity &amp; Direction</h3>
<p>Having a clear sense of what you want to achieve and why it matters to you personally. Understanding your core motivations, having frameworks for major life decisions, and feeling confident about your chosen path. People who lean towards this value focus on reducing existential confusion, developing coherent long-term vision, and maintaining certainty about their direction even when circumstances change.</p>

<h3>Meaning &amp; Fulfilment</h3>
<p>The degree to which your life purpose provides deep satisfaction, emotional resonance, and a sense that your existence matters. Feeling that your goals are personally meaningful rather than externally imposed, experiencing regular fulfilment from working towards your purpose, and having a sense that your life has significance. People who lean towards this value seek purposes that genuinely inspire and motivate them.</p>

<h3>Integration &amp; Coherence</h3>
<p>How well your life purpose connects with and organises other aspects of your life &ndash; career, relationships, daily activities, and personal growth. Having a purpose that provides a unifying framework for life decisions, reduces internal conflict between different life domains, and creates synergy between various activities. People who lean towards this value want their purpose to serve as an organising principle that makes their whole life more coherent.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each life purpose value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Clarity &amp; Direction &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Greta_Thunberg" target="_blank">Greta Thunberg</a> identified climate activism as her purpose at age 15 and has maintained that direction with unusual consistency. She started by sitting alone outside the Swedish parliament in 2018 and sustained the commitment through global fame, intense criticism, and political pressure. Her clarity of purpose &ndash; and her refusal to be deflected from it &ndash; has been documented extensively in interviews, speeches, and her own writing.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Meaning &amp; Fulfilment &ndash; Level 5</div>
    <p><a href="https://www.nobelprize.org/prizes/peace/2014/satyarthi/biographical/" target="_blank">Kailash Satyarthi</a> has worked to end child labour since the early 1980s, directly participating in the rescue of over 80,000 children from forced labour. He continued this work for decades before receiving the Nobel Peace Prize in 2014, sustaining motivation through legal battles, physical attacks, and the deaths of colleagues. His purpose appears to have been the primary organising force of his adult life.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Integration &amp; Coherence &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Yo-Yo_Ma" target="_blank">Yo-Yo Ma</a> has spent over 50 years as a cellist, but his career consistently reflects a broader purpose &ndash; using music to build connection across cultures. His Silk Road Ensemble brings together musicians from dozens of countries, his community concerts take place in settings from prisons to refugee camps, and his public statements frame music as a tool for empathy. His concert schedule, teaching, and advocacy all appear to serve a single coherent vision rather than separate professional tracks.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes of reflection.</p>

<div class="assess-group">
<h4>Clarity &amp; Direction</h4>

<div class="assess-input-group" id="ig-articulate-purpose">
    <span class="assess-label">Could you articulate what you want your life to be about in one or two sentences?</span>
    <span class="assess-hint">This doesn't need to be polished &ndash; even a rough attempt counts.</span>
    <select id="a-articulate-purpose" onchange="handleAssessInput('a-articulate-purpose')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I have no idea how I'd answer this</option>
        <option value="fragments">I have fragments but couldn't form a coherent statement</option>
        <option value="rough">I could give a rough answer but it would feel vague</option>
        <option value="clear">I have a fairly clear answer I could state confidently</option>
        <option value="tested">I have a well-tested statement that has guided real decisions</option>
    </select> <span class="assess-percentile-hint" id="pct-articulate-purpose"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-articulate-purpose" onchange="handleSkip('a-articulate-purpose')"><label for="skip-articulate-purpose">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-decision-framework">
    <span class="assess-label">How do you tend to make major life decisions?</span>
    <span class="assess-hint">Think about your last major decision &ndash; moving, changing jobs, starting or ending a relationship.</span>
    <select id="a-decision-framework" onchange="handleAssessInput('a-decision-framework')">
        <option value="">Select...</option>
        <option value="default">I mostly go with whatever happens or what others expect</option>
        <option value="feeling">I decide based on what feels right in the moment</option>
        <option value="informal">I weigh pros and cons informally but don't have a system</option>
        <option value="framework">I have a framework I consciously use (values, priorities, criteria)</option>
        <option value="integrated">I have a well-developed system that connects decisions to my broader purpose</option>
    </select> <span class="assess-percentile-hint" id="pct-decision-framework"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-decision-framework" onchange="handleSkip('a-decision-framework')"><label for="skip-decision-framework">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-direction-confidence">
    <span class="assess-label">How confident do you feel about your current life direction?</span>
    <span class="assess-hint">There's no right answer here. The point is noticing where you stand.</span>
    <select id="a-direction-confidence" onchange="handleAssessInput('a-direction-confidence')">
        <option value="">Select...</option>
        <option value="adrift">Adrift &ndash; I don't feel like I'm heading anywhere in particular</option>
        <option value="uncertain">Uncertain &ndash; I have some ideas but they don't feel solid</option>
        <option value="mixed">Mixed &ndash; some areas feel on track, others don't</option>
        <option value="mostly-confident">Mostly confident &ndash; I feel broadly on the right path</option>
        <option value="very-confident">Very confident &ndash; I know where I'm going and why</option>
    </select> <span class="assess-percentile-hint" id="pct-direction-confidence"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-direction-confidence" onchange="handleSkip('a-direction-confidence')"><label for="skip-direction-confidence">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Meaning &amp; Fulfilment</h4>

<div class="assess-input-group" id="ig-fulfilment-sources">
    <span class="assess-label">How well can you identify the activities or contexts that give you the deepest sense of fulfilment?</span>
    <span class="assess-hint">These might be professional, personal, creative, or relational. Think about when you feel most alive.</span>
    <select id="a-fulfilment-sources" onchange="handleAssessInput('a-fulfilment-sources')">
        <option value="">Select...</option>
        <option value="unclear">I'm not sure what fulfils me</option>
        <option value="vague">I have a vague sense but couldn't name specifics</option>
        <option value="some">I can name a few things but I'm not sure they're the deepest ones</option>
        <option value="clear">I know clearly what fulfils me and I seek it out</option>
        <option value="organised">I've organised my life around my sources of fulfilment</option>
    </select> <span class="assess-percentile-hint" id="pct-fulfilment-sources"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-fulfilment-sources" onchange="handleSkip('a-fulfilment-sources')"><label for="skip-fulfilment-sources">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-meaning-vs-external">
    <span class="assess-label">How much of your current motivation comes from your own sense of meaning versus external expectations?</span>
    <span class="assess-hint">External expectations include family pressure, social norms, or what seems impressive to others.</span>
    <select id="a-meaning-vs-external" onchange="handleAssessInput('a-meaning-vs-external')">
        <option value="">Select...</option>
        <option value="mostly-external">Mostly external &ndash; I'm pursuing what others expect of me</option>
        <option value="mixed-external">More external than internal &ndash; I haven't separated the two clearly</option>
        <option value="balanced">Roughly balanced &ndash; some goals are mine, some are inherited</option>
        <option value="mostly-internal">Mostly internal &ndash; my goals feel personally meaningful</option>
        <option value="fully-internal">Fully internal &ndash; I've consciously chosen my goals and they feel deeply mine</option>
    </select> <span class="assess-percentile-hint" id="pct-meaning-vs-external"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-meaning-vs-external" onchange="handleSkip('a-meaning-vs-external')"><label for="skip-meaning-vs-external">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-setback-motivation">
    <span class="assess-label">How does your motivation respond during setbacks or difficult periods?</span>
    <span class="assess-hint">Do you push through, lose interest, pivot, or go numb? All are common patterns worth noticing.</span>
    <select id="a-setback-motivation" onchange="handleAssessInput('a-setback-motivation')">
        <option value="">Select...</option>
        <option value="collapse">It collapses &ndash; I lose direction and energy</option>
        <option value="dips">It dips significantly and takes a long time to recover</option>
        <option value="wobbles">It wobbles but I eventually get back on track</option>
        <option value="holds">It mostly holds &ndash; setbacks slow me down but don't derail me</option>
        <option value="strengthens">It strengthens &ndash; difficulties tend to clarify what matters</option>
    </select> <span class="assess-percentile-hint" id="pct-setback-motivation"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-setback-motivation" onchange="handleSkip('a-setback-motivation')"><label for="skip-setback-motivation">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Integration &amp; Coherence</h4>

<div class="assess-input-group" id="ig-values-alignment">
    <span class="assess-label">How well do your daily activities align with what you say matters to you?</span>
    <span class="assess-hint">Compare how you spend a typical week with what you'd list as your top priorities.</span>
    <select id="a-values-alignment" onchange="handleAssessInput('a-values-alignment')">
        <option value="">Select...</option>
        <option value="poor">Poorly &ndash; my time goes to things that don't reflect my priorities</option>
        <option value="somewhat">Somewhat &ndash; there's overlap but a lot of drift</option>
        <option value="moderate">Moderately &ndash; my priorities show up in my schedule but not consistently</option>
        <option value="well">Well &ndash; most of my time reflects what I care about</option>
        <option value="very-well">Very well &ndash; I've deliberately structured my life around my priorities</option>
    </select> <span class="assess-percentile-hint" id="pct-values-alignment"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-values-alignment" onchange="handleSkip('a-values-alignment')"><label for="skip-values-alignment">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-domain-conflict">
    <span class="assess-label">How well do different areas of your life (work, relationships, personal projects) support each other?</span>
    <span class="assess-hint">Conflict between domains is extremely common &ndash; the point is noticing the pattern.</span>
    <select id="a-domain-conflict" onchange="handleAssessInput('a-domain-conflict')">
        <option value="">Select...</option>
        <option value="competing">Actively competing &ndash; gains in one area come at the expense of others</option>
        <option value="tension">Some tension &ndash; I feel pulled in different directions regularly</option>
        <option value="coexisting">Coexisting &ndash; they don't conflict much but don't reinforce each other either</option>
        <option value="supportive">Mostly supportive &ndash; progress in one area tends to help others</option>
        <option value="integrated">Well integrated &ndash; my life areas form a coherent whole</option>
    </select> <span class="assess-percentile-hint" id="pct-domain-conflict"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-domain-conflict" onchange="handleSkip('a-domain-conflict')"><label for="skip-domain-conflict">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-purpose-decisions">
    <span class="assess-label">Have you ever made a significant life decision based on purpose or values rather than convenience, money, or default expectations?</span>
    <span class="assess-hint">This could be a career change, a move, ending something comfortable, or starting something risky.</span>
    <select id="a-purpose-decisions" onchange="handleAssessInput('a-purpose-decisions')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; my major decisions have been driven by practical considerations</option>
        <option value="once">Once &ndash; I can think of a single example</option>
        <option value="occasionally">Occasionally &ndash; a few times in my life</option>
        <option value="regularly">Regularly &ndash; purpose is a major factor in most big decisions</option>
        <option value="consistently">Consistently &ndash; purpose is the primary driver of my life direction</option>
    </select> <span class="assess-percentile-hint" id="pct-purpose-decisions"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-purpose-decisions" onchange="handleSkip('a-purpose-decisions')"><label for="skip-purpose-decisions">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-clarity">
        <span class="assess-summary-label">Clarity &amp; Direction</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-clarity" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-clarity">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-meaning">
        <span class="assess-summary-label">Meaning &amp; Fulfilment</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-meaning" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-meaning">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-integration">
        <span class="assess-summary-label">Integration &amp; Coherence</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-integration" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-integration">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published research on purpose, meaning, and life direction among adults. All items in this area are scored.</p>
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

<p>You now understand why life purpose matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about clarity and direction, meaning and fulfilment, and integration and coherence. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/life-purpose/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Life Purpose Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Life Purpose. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/life-purpose/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'life-purpose';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-articulate-purpose', 'a-decision-framework', 'a-direction-confidence',
        'a-fulfilment-sources', 'a-meaning-vs-external', 'a-setback-motivation',
        'a-values-alignment', 'a-domain-conflict', 'a-purpose-decisions'
    ];

    var UNSCORED_ITEMS = [];

    var THRESHOLDS = {
        'a-articulate-purpose': [
            {v:'no',p:10},{v:'fragments',p:30},{v:'rough',p:52},{v:'clear',p:78},{v:'tested',p:95}
        ],
        'a-decision-framework': [
            {v:'default',p:10},{v:'feeling',p:28},{v:'informal',p:52},{v:'framework',p:80},{v:'integrated',p:95}
        ],
        'a-direction-confidence': [
            {v:'adrift',p:8},{v:'uncertain',p:25},{v:'mixed',p:50},{v:'mostly-confident',p:75},{v:'very-confident',p:93}
        ],
        'a-fulfilment-sources': [
            {v:'unclear',p:8},{v:'vague',p:25},{v:'some',p:50},{v:'clear',p:78},{v:'organised',p:95}
        ],
        'a-meaning-vs-external': [
            {v:'mostly-external',p:8},{v:'mixed-external',p:25},{v:'balanced',p:48},{v:'mostly-internal',p:72},{v:'fully-internal',p:93}
        ],
        'a-setback-motivation': [
            {v:'collapse',p:8},{v:'dips',p:25},{v:'wobbles',p:50},{v:'holds',p:75},{v:'strengthens',p:94}
        ],
        'a-values-alignment': [
            {v:'poor',p:8},{v:'somewhat',p:28},{v:'moderate',p:50},{v:'well',p:78},{v:'very-well',p:95}
        ],
        'a-domain-conflict': [
            {v:'competing',p:8},{v:'tension',p:28},{v:'coexisting',p:50},{v:'supportive',p:75},{v:'integrated',p:95}
        ],
        'a-purpose-decisions': [
            {v:'never',p:10},{v:'once',p:28},{v:'occasionally',p:50},{v:'regularly',p:78},{v:'consistently',p:95}
        ],
    };

    var VALUE_ITEMS = {
        clarity: ['a-articulate-purpose', 'a-decision-framework', 'a-direction-confidence'],
        meaning: ['a-fulfilment-sources', 'a-meaning-vs-external', 'a-setback-motivation'],
        integration: ['a-values-alignment', 'a-domain-conflict', 'a-purpose-decisions'],
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
        hintEl.textContent = pct !== null ? '~' + ordinalSuffix(pct) + ' percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['clarity', 'meaning', 'integration'].forEach(function(vk) {
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
        ['clarity', 'meaning', 'integration'].forEach(function(vk) {
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
