---
layout: default
title: "Ethics – Level 1: Awareness"
life_area_slug: ethics
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

<h1>Ethics: Level 1</h1>

<p class="l1-subtitle">Understand what ethics means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Ethics Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why ethics matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Most people absorb their moral frameworks from family, culture, and religion without examining them closely. That inherited toolkit may work well enough for routine situations, but it tends to break down when decisions get genuinely difficult &ndash; when values conflict, when the stakes are high, or when social pressure pulls against what you believe is right.</p>

<p>Developing your ethical thinking deliberately has measurable effects. <a href="https://psycnet.apa.org/record/2004-16788-000" target="_blank">Peterson and Seligman (2004)</a> found that character strengths including integrity and fairness are among the strongest predictors of life satisfaction across cultures. People with clearer moral frameworks also tend to experience less <a href="https://www.swarthmore.edu/SocSci/bschwar1/Sci.Amer.pdf" target="_blank">decision paralysis</a> when facing complex choices, likely because they have stable criteria for evaluating options.</p>

<p>There is a practical dimension too. Consistent ethical behaviour builds social trust over time. <a href="https://www.bowlingalone.com/" target="_blank">Putnam (2000)</a> found that communities with higher levels of moral trust have better social and economic outcomes. On an individual level, the people others turn to for advice in difficult situations are almost always those whose integrity has been tested and held.</p>

<p>Ethics also intersects with nearly every other area of life &ndash; how you manage money, how you treat colleagues, how you raise children, what career you choose. Strengthening your ethical framework may be one of the broadest-impact investments available.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about ethics</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue ethical development for different reasons. This site scores every ethics intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Philosophical Depth</h3>
<p>Comprehensive understanding of ethical theories, moral philosophy, and rigorous reasoning about complex moral questions. Studying major frameworks like utilitarianism, deontology, and virtue ethics, understanding their historical development and contemporary applications, and developing analytical skills for moral reasoning. People who lean towards this value seek deep engagement with ethics as an intellectual discipline.</p>

<h3>Practical Guidance</h3>
<p>Clear, actionable ethical frameworks that provide reliable guidance for daily decisions and life choices. Developing decision-making processes for common moral dilemmas, creating personal principles that can be applied consistently across different contexts, and translating abstract moral insights into concrete behavioural guidelines. People who lean towards this value focus on ethics that actually helps them navigate real-world situations with confidence.</p>

<h3>Moral Integrity</h3>
<p>Living according to your ethical convictions consistently, even when it requires personal sacrifice, social awkwardness, or going against popular opinion. Developing the courage to act on moral principles when it's difficult, maintaining consistency between private beliefs and public behaviour, and building character traits that support ethical action under pressure. People who lean towards this value focus on closing the gap between knowing what's right and actually doing it.</p>

<h3>Community Ethics &amp; Belonging</h3>
<p>Understanding and fulfilling your moral obligations within your communities, families, and relationships whilst contributing to collective moral flourishing. Aligning with the ethical expectations of groups you value belonging to, understanding your moral duties to others based on your roles and relationships, and seeing ethics as fundamentally about service to others. People who lean towards this value focus on how their ethical choices strengthen their communities.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each ethics value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Philosophical Depth &ndash; Level 5</div>
    <p><a href="https://www.utilitarianism.net/utilitarian-thinker/peter-singer" target="_blank">Peter Singer</a> has spent over five decades developing and refining utilitarian arguments on animal welfare, global poverty, and effective altruism. His 1975 book <em>Animal Liberation</em> provided the philosophical foundation for the modern animal rights movement. He has consistently revised his positions in response to counter-arguments &ndash; a rarity among public intellectuals &ndash; and his practical ethics framework is taught in most university philosophy programmes worldwide.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Practical Guidance &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Bryan_Stevenson" target="_blank">Bryan Stevenson</a> founded the Equal Justice Initiative in 1989 and has since won relief for over 140 wrongly condemned prisoners on death row. His ethical framework &ndash; centred on proximity to suffering as a prerequisite for moral understanding &ndash; translates directly into legal strategy, organisational decisions, and public advocacy. His approach has been adopted by law schools, public defenders' offices, and criminal justice organisations across the United States.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Moral Integrity &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Dietrich_Bonhoeffer" target="_blank">Dietrich Bonhoeffer</a> was a German theologian who returned to Nazi Germany from the safety of the United States in 1939 because he believed he could not participate in rebuilding German moral life after the war if he had not shared the trials of his countrymen. He joined the resistance, was arrested in 1943, and was executed in April 1945. His theological writings on the cost of moral conviction, composed largely in prison, continue to influence ethical thought eight decades later.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Community Ethics &amp; Belonging &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Ela_Bhatt" target="_blank">Ela Bhatt</a> founded the Self-Employed Women's Association (SEWA) in India in 1972, building it into a union of over 2 million members. She developed ethical frameworks for economic cooperation rooted in Gandhian principles and applied them at scale, creating banking, insurance, and housing cooperatives that transformed the lives of some of the poorest women in the world. Her model of community-centred ethics has been replicated across dozens of countries.</p>
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
<h4>Philosophical Depth</h4>

<div class="assess-input-group" id="ig-frameworks">
    <span class="assess-label">How many ethical frameworks can you name and explain?</span>
    <span class="assess-hint">E.g. utilitarianism, deontology, virtue ethics, care ethics.</span>
    <select id="a-frameworks" onchange="handleAssessInput('a-frameworks')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I couldn't name one</option>
        <option value="heard">I've heard the names but couldn't explain any</option>
        <option value="one">I could explain one in basic terms</option>
        <option value="several">I could explain two or three clearly</option>
        <option value="many">I could explain four or more and compare their strengths</option>
    </select> <span class="assess-percentile-hint" id="pct-frameworks"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-frameworks" onchange="handleSkip('a-frameworks')"><label for="skip-frameworks">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-reasoning">
    <span class="assess-label">How do you tend to judge whether an action is right or wrong?</span>
    <span class="assess-hint">There's no right answer &ndash; this is about noticing your default approach.</span>
    <select id="a-reasoning" onchange="handleAssessInput('a-reasoning')">
        <option value="">Select...</option>
        <option value="unsure">I haven't really thought about it</option>
        <option value="gut">Mostly gut feeling &ndash; I just know</option>
        <option value="outcomes">Mainly by the outcomes &ndash; did it cause harm or good?</option>
        <option value="intentions">Mainly by the intentions &ndash; was the person trying to do right?</option>
        <option value="mixed">A conscious mix of several standards depending on the situation</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-reasoning" onchange="handleSkip('a-reasoning')"><label for="skip-reasoning">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-dilemma">
    <span class="assess-label">How recently have you faced a genuine moral dilemma where two principles pulled in different directions?</span>
    <span class="assess-hint">A time you had to choose between competing values, not just a hard decision.</span>
    <select id="a-dilemma" onchange="handleAssessInput('a-dilemma')">
        <option value="">Select...</option>
        <option value="never">I can't recall one</option>
        <option value="distant">Years ago, and I don't remember my reasoning well</option>
        <option value="moderate">Within the past year or two</option>
        <option value="recent">Within the past few months, and I can describe how I reasoned through it</option>
        <option value="frequent">I notice these regularly and have a process for working through them</option>
    </select> <span class="assess-percentile-hint" id="pct-dilemma"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-dilemma" onchange="handleSkip('a-dilemma')"><label for="skip-dilemma">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Practical Guidance</h4>

<div class="assess-input-group" id="ig-principles">
    <span class="assess-label">How clearly could you state your core moral principles?</span>
    <span class="assess-hint">The rules or commitments you try to follow in daily life.</span>
    <select id="a-principles" onchange="handleAssessInput('a-principles')">
        <option value="">Select...</option>
        <option value="none">I don't think I have any explicit ones</option>
        <option value="vague">I have a vague sense but couldn't articulate them</option>
        <option value="some">I could name a few but haven't thought them through carefully</option>
        <option value="clear">I have a clear set I could write down</option>
        <option value="tested">I have explicit principles I've tested and refined over time</option>
    </select> <span class="assess-percentile-hint" id="pct-principles"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-principles" onchange="handleSkip('a-principles')"><label for="skip-principles">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-consistency">
    <span class="assess-label">How consistently do you apply your moral principles across different contexts?</span>
    <span class="assess-hint">For example, whether you hold yourself to the same standards you hold others to.</span>
    <select id="a-consistency" onchange="handleAssessInput('a-consistency')">
        <option value="">Select...</option>
        <option value="inconsistent">Very inconsistently &ndash; my standards shift a lot depending on who's involved</option>
        <option value="somewhat">Somewhat &ndash; I notice double standards in myself fairly often</option>
        <option value="mostly">Mostly consistent, with occasional exceptions I'm aware of</option>
        <option value="very">Very consistent &ndash; I actively work to apply the same standards everywhere</option>
    </select> <span class="assess-percentile-hint" id="pct-consistency"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-consistency" onchange="handleSkip('a-consistency')"><label for="skip-consistency">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-blindspots">
    <span class="assess-label">Can you identify areas where your moral decision-making feels unclear or where you suspect you have a blind spot?</span>
    <span class="assess-hint">Common examples: spending habits, environmental impact, how you treat people you'll never see again.</span>
    <select id="a-blindspots" onchange="handleAssessInput('a-blindspots')">
        <option value="">Select...</option>
        <option value="unaware">I haven't thought about this</option>
        <option value="maybe">I suspect I have blind spots but can't name them</option>
        <option value="one">I can identify one area where I'm unsure</option>
        <option value="several">I can identify several and have thought about why</option>
        <option value="active">I actively look for blind spots and have strategies to address them</option>
    </select> <span class="assess-percentile-hint" id="pct-blindspots"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-blindspots" onchange="handleSkip('a-blindspots')"><label for="skip-blindspots">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Moral Integrity</h4>

<div class="assess-input-group" id="ig-gap">
    <span class="assess-label">How large is the gap between what you believe is right and how you actually behave?</span>
    <span class="assess-hint">Most people have some gap here. The point is to see it clearly.</span>
    <select id="a-gap" onchange="handleAssessInput('a-gap')">
        <option value="">Select...</option>
        <option value="havent-looked">I haven't really looked at this honestly</option>
        <option value="large">Large &ndash; I regularly act against what I believe is right</option>
        <option value="moderate">Moderate &ndash; I notice the gap in some areas</option>
        <option value="small">Small &ndash; I live according to my values most of the time</option>
        <option value="minimal">Minimal &ndash; I've deliberately closed this gap over time</option>
    </select> <span class="assess-percentile-hint" id="pct-gap"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-gap" onchange="handleSkip('a-gap')"><label for="skip-gap">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-courage">
    <span class="assess-label">How often do you act on moral convictions when it costs you something?</span>
    <span class="assess-hint">Social disapproval, financial cost, inconvenience, or awkwardness all count.</span>
    <select id="a-courage" onchange="handleAssessInput('a-courage')">
        <option value="">Select...</option>
        <option value="rarely">Rarely &ndash; I tend to avoid situations where it would cost me</option>
        <option value="sometimes">Sometimes &ndash; when the cost is low</option>
        <option value="often">Often &ndash; I'll speak up or act even when it's uncomfortable</option>
        <option value="consistently">Consistently &ndash; I've accepted significant costs for my principles</option>
    </select> <span class="assess-percentile-hint" id="pct-courage"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-courage" onchange="handleSkip('a-courage')"><label for="skip-courage">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-pressure">
    <span class="assess-label">How much does social pressure affect your moral choices?</span>
    <span class="assess-hint">Do you tend to go along with the group, or hold your ground?</span>
    <select id="a-pressure" onchange="handleAssessInput('a-pressure')">
        <option value="">Select...</option>
        <option value="strong">Strongly &ndash; I usually go along with the group</option>
        <option value="moderate">Moderately &ndash; I'll conform on smaller things but hold firm on big ones</option>
        <option value="low">Low &ndash; I hold my ground on most things regardless of social cost</option>
        <option value="very-low">Very low &ndash; I've consciously developed resistance to social pressure</option>
    </select> <span class="assess-percentile-hint" id="pct-pressure"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-pressure" onchange="handleSkip('a-pressure')"><label for="skip-pressure">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Community Ethics &amp; Belonging</h4>

<div class="assess-input-group" id="ig-obligations">
    <span class="assess-label">How clearly have you thought about your moral obligations to the communities you belong to?</span>
    <span class="assess-hint">Family, friends, workplace, neighbourhood, religious community, or broader society.</span>
    <select id="a-obligations" onchange="handleAssessInput('a-obligations')">
        <option value="">Select...</option>
        <option value="not-considered">I haven't really thought about this</option>
        <option value="vague">I have a vague sense but nothing specific</option>
        <option value="some">I've thought about obligations to one or two communities</option>
        <option value="clear">I have a clear sense of my obligations across several communities</option>
        <option value="active">I've thought this through carefully and actively fulfil specific commitments</option>
    </select> <span class="assess-percentile-hint" id="pct-obligations"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-obligations" onchange="handleSkip('a-obligations')"><label for="skip-obligations">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-impact">
    <span class="assess-label">How aware are you of how your ethical choices affect the people around you?</span>
    <span class="assess-hint">Both the direct effects and the example you set.</span>
    <select id="a-impact" onchange="handleAssessInput('a-impact')">
        <option value="">Select...</option>
        <option value="unaware">I don't think about this much</option>
        <option value="sometimes">I sometimes notice the effects after the fact</option>
        <option value="aware">I'm generally aware of the direct effects on others</option>
        <option value="very-aware">I consider both direct effects and the broader example I'm setting</option>
    </select> <span class="assess-percentile-hint" id="pct-impact"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-impact" onchange="handleSkip('a-impact')"><label for="skip-impact">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-contribute">
    <span class="assess-label">Do you actively contribute to the moral health of your communities, or mostly follow existing norms?</span>
    <span class="assess-hint">Do you raise ethical concerns, mediate disputes, or set standards &ndash; or leave that to others?</span>
    <select id="a-contribute" onchange="handleAssessInput('a-contribute')">
        <option value="">Select...</option>
        <option value="follow">Mostly follow &ndash; I go along with established norms</option>
        <option value="occasionally">Occasionally &ndash; I'll speak up if something feels clearly wrong</option>
        <option value="regularly">Regularly &ndash; I raise concerns and try to set a good example</option>
        <option value="actively">Actively &ndash; I take on a visible role in shaping my communities' ethical standards</option>
    </select> <span class="assess-percentile-hint" id="pct-contribute"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-contribute" onchange="handleSkip('a-contribute')"><label for="skip-contribute">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-philosophical">
        <span class="assess-summary-label">Philosophical Depth</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-philosophical" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-philosophical">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-practical">
        <span class="assess-summary-label">Practical Guidance</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-practical" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-practical">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-integrity">
        <span class="assess-summary-label">Moral Integrity</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-integrity" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-integrity">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-community">
        <span class="assess-summary-label">Community Ethics</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-community" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-community">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published data on ethical literacy, moral reasoning, prosocial behaviour, and community engagement. Unscored items (default moral reasoning style) are excluded from calculations.</p>
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

<p>You now understand why ethics matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about philosophical depth, practical guidance, moral integrity, and community ethics. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/ethics/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Ethics Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Ethics. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/ethics/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'ethics';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-frameworks', 'a-reasoning', 'a-dilemma',
        'a-principles', 'a-consistency', 'a-blindspots',
        'a-gap', 'a-courage', 'a-pressure',
        'a-obligations', 'a-impact', 'a-contribute'
    ];

    var THRESHOLDS = {
        'a-frameworks': [
            // ~70% cannot name any ethical framework; explaining four+ is ~5%
            {v:'none',p:10},{v:'heard',p:28},{v:'one',p:50},{v:'several',p:78},{v:'many',p:97}
        ],
        'a-dilemma': [
            // ~35% can't recall a moral dilemma; frequent recognition with process is ~8%
            {v:'never',p:10},{v:'distant',p:30},{v:'moderate',p:55},{v:'recent',p:78},{v:'frequent',p:95}
        ],
        'a-principles': [
            // ~40% have no explicit moral principles; tested and refined is ~8%
            {v:'none',p:10},{v:'vague',p:28},{v:'some',p:50},{v:'clear',p:78},{v:'tested',p:95}
        ],
        'a-consistency': [
            // ~35% are very inconsistent; actively working to apply same standards is ~15%
            {v:'inconsistent',p:10},{v:'somewhat',p:32},{v:'mostly',p:62},{v:'very',p:92}
        ],
        'a-blindspots': [
            // ~45% haven't thought about ethical blind spots; active strategies is ~8%
            {v:'unaware',p:10},{v:'maybe',p:28},{v:'one',p:50},{v:'several',p:78},{v:'active',p:95}
        ],
        'a-gap': [
            // ~30% haven't looked honestly at belief-behaviour gap; deliberately closed is ~10%
            {v:'havent-looked',p:10},{v:'large',p:25},{v:'moderate',p:48},{v:'small',p:75},{v:'minimal',p:93}
        ],
        'a-courage': [
            // ~35% rarely act on convictions at cost; consistent significant cost is ~10%
            {v:'rarely',p:12},{v:'sometimes',p:38},{v:'often',p:68},{v:'consistently',p:93}
        ],
        'a-pressure': [
            // ~30% strongly conform; consciously developed resistance is ~12%
            {v:'strong',p:10},{v:'moderate',p:38},{v:'low',p:70},{v:'very-low',p:93}
        ],
        'a-obligations': [
            // ~40% haven't considered community obligations; careful active fulfilment is ~10%
            {v:'not-considered',p:10},{v:'vague',p:28},{v:'some',p:50},{v:'clear',p:78},{v:'active',p:95}
        ],
        'a-impact': [
            // ~35% don't think about ethical ripple effects; considering broader example is ~15%
            {v:'unaware',p:10},{v:'sometimes',p:32},{v:'aware',p:60},{v:'very-aware',p:92}
        ],
        'a-contribute': [
            // ~45% mostly follow existing norms; visible active role is ~8%
            {v:'follow',p:12},{v:'occasionally',p:38},{v:'regularly',p:70},{v:'actively',p:95}
        ]
    };

    var VALUE_ITEMS = {
        philosophical: ['a-frameworks', 'a-dilemma'],
        practical: ['a-principles', 'a-consistency', 'a-blindspots'],
        integrity: ['a-gap', 'a-courage', 'a-pressure'],
        community: ['a-obligations', 'a-impact', 'a-contribute']
    };

    var UNSCORED_ITEMS = ['a-reasoning'];

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
        ['philosophical', 'practical', 'integrity', 'community'].forEach(function(vk) {
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
        ['philosophical', 'practical', 'integrity', 'community'].forEach(function(vk) {
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
