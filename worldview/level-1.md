---
layout: default
title: "Worldview – Level 1: Awareness"
life_area_slug: worldview
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

<h1>Worldview: Level 1</h1>

<p class="l1-subtitle">Understand what worldview means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Worldview Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why worldview matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your worldview &ndash; the collection of mental models, beliefs, and frameworks you use to interpret what happens around you &ndash; shapes nearly every significant decision you make. It determines which opportunities you notice, which risks you take seriously, and how well you predict what comes next.</p>

<p>Research on <a href="https://www.hup.harvard.edu/books/9780674975866" target="_blank">superforecasting</a> found that the best predictors share a common trait: they draw on broad, well-integrated knowledge rather than deep expertise in a single domain. People with well-developed worldviews were roughly <a href="https://goodjudgment.com/resources/the-superforecasters/" target="_blank">30% more accurate</a> at predicting geopolitical and economic events than intelligence analysts with access to classified information.</p>

<p>The practical consequences are substantial. Understanding basic economics helps you evaluate career decisions and financial choices. Knowing how political systems function lets you anticipate policy changes that affect your life. Familiarity with psychology helps you recognise when you are being manipulated &ndash; or when you are fooling yourself. A <a href="https://journals.sagepub.com/doi/10.1177/0956797611421206" target="_blank">2012 study</a> found that people with greater knowledge of how the world works were significantly less susceptible to conspiracy theories and misinformation.</p>

<p>Perhaps most importantly, a coherent worldview provides psychological grounding. People with well-examined beliefs about human nature, progress, and their place in the broader story tend to cope better with uncertainty and report greater life satisfaction. Your worldview is not just an intellectual exercise &ndash; it is the operating system your mind runs on.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about worldview</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People develop their worldviews for different reasons. This site scores every worldview intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Breadth</h3>
<p>Developing understanding across multiple domains that shape how the world works &ndash; history, economics, psychology, politics, culture, and technology. People who lean towards this value focus on seeing connections between different fields and avoiding the blind spots that come from narrow knowledge. They tend to favour comprehensive coverage over deep specialisation.</p>

<h3>Depth</h3>
<p>Building sophisticated, nuanced understanding within specific domains rather than surface-level familiarity. People who lean towards this value focus on mastering fewer areas thoroughly, understanding complex theories, and analysing subtle distinctions. They would rather know two subjects well enough to teach them than know ten subjects well enough to discuss them at a dinner party.</p>

<h3>Utility</h3>
<p>A worldview that enhances real-world decision-making, prediction, and practical navigation of complex situations. People who lean towards this value focus on understanding how systems actually work &ndash; not how they are supposed to work &ndash; and they tend to prioritise frameworks that improve their ability to achieve goals and avoid common mistakes.</p>

<h3>Meaning</h3>
<p>Developing understanding that provides psychological grounding, moral framework, and sense of purpose. People who lean towards this value focus on building coherent narratives about human nature, progress, and their place in the larger story. They want a worldview that offers stability and direction during uncertainty, not just analytical power.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each worldview value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Breadth &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Vaclav_Smil" target="_blank">Vaclav Smil</a> has published over 40 books spanning energy, food production, environmental change, economics, demographics, and technical innovation. His writing regularly integrates data from half a dozen disciplines in a single argument. Bill Gates has called him his favourite author, largely because Smil's analyses draw on a range of domains that few specialists can match. He holds no public office and runs no institute &ndash; the breadth of his published work is itself the evidence.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Depth &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/David_Deutsch" target="_blank">David Deutsch</a> is a physicist at Oxford who developed the quantum theory of computation and has written two books &ndash; <em>The Fabric of Reality</em> and <em>The Beginning of Infinity</em> &ndash; that attempt to unify physics, epistemology, evolution, and computation into a single explanatory framework. His work demonstrates an unusual depth of engagement with fundamental questions across multiple disciplines, sustained over several decades.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Utility &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Philip_Tetlock" target="_blank">Philip Tetlock</a> spent over 20 years tracking the accuracy of expert predictions and demonstrated that most experts performed barely better than chance. He then developed the Good Judgment Project, which identified ordinary people whose forecasting accuracy consistently exceeded that of intelligence analysts. His work on superforecasting has been adopted by intelligence agencies and investment firms as a practical framework for decision-making under uncertainty.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Meaning &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Wendell_Berry" target="_blank">Wendell Berry</a> has spent over 60 years farming, writing, and teaching from the same small farm in Henry County, Kentucky. His novels, essays, and poetry articulate a worldview built around land stewardship, community, and the limits of industrial progress &ndash; and he has lived according to those principles consistently, farming without a tractor for decades and refusing to own a computer. His worldview appears to be genuinely load-bearing in his daily decisions rather than a theoretical position.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to think through.</p>

<div class="assess-group">
<h4>Breadth</h4>

<div class="assess-input-group" id="ig-domains-map">
    <span class="assess-label">How many of the major domains that shape how the world works could you discuss competently?</span>
    <span class="assess-hint">Consider history, economics, psychology, politics, science, technology, philosophy, and culture.</span>
    <select id="a-domains-map" onchange="handleAssessInput('a-domains-map')">
        <option value="">Select...</option>
        <option value="one-two">One or two &ndash; I have deep gaps in most areas</option>
        <option value="few">A few &ndash; I'm comfortable in some but largely ignorant in others</option>
        <option value="several">Several &ndash; I have working knowledge across most major domains</option>
        <option value="most">Most &ndash; I could hold a substantive conversation in nearly all of them</option>
        <option value="integrated">Most, and I actively connect insights across domains</option>
    </select> <span class="assess-percentile-hint" id="pct-domains-map"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-domains-map" onchange="handleSkip('a-domains-map')"><label for="skip-domains-map">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-cross-domain">
    <span class="assess-label">How often does knowledge from one domain help you understand something in a completely different domain?</span>
    <span class="assess-hint">For example, understanding psychology helped you interpret a political event, or knowledge of history informed a business decision.</span>
    <select id="a-cross-domain" onchange="handleAssessInput('a-cross-domain')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I can't think of an example</option>
        <option value="rarely">Rarely &ndash; it's happened once or twice</option>
        <option value="sometimes">Sometimes &ndash; I notice connections occasionally</option>
        <option value="often">Often &ndash; I regularly draw on one field to understand another</option>
        <option value="constantly">Constantly &ndash; cross-domain thinking is how I naturally process information</option>
    </select> <span class="assess-percentile-hint" id="pct-cross-domain"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-cross-domain" onchange="handleSkip('a-cross-domain')"><label for="skip-cross-domain">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-blind-spots">
    <span class="assess-label">How many major knowledge gaps have you identified in your understanding of the world?</span>
    <span class="assess-hint">Be honest &ndash; most people have significant gaps in economics, statistics, or geopolitics even if they follow the news.</span>
    <select id="a-blind-spots" onchange="handleAssessInput('a-blind-spots')">
        <option value="">Select...</option>
        <option value="unaware">I haven't really thought about my gaps</option>
        <option value="vague">I know there are gaps but can't name specific domains</option>
        <option value="one-two">I can name one or two specific areas where I'm weak</option>
        <option value="several">I can name several and I know which ones matter most</option>
        <option value="mapped">I've mapped my gaps systematically and I'm working on the most important ones</option>
    </select> <span class="assess-percentile-hint" id="pct-blind-spots"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-blind-spots" onchange="handleSkip('a-blind-spots')"><label for="skip-blind-spots">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Depth</h4>

<div class="assess-input-group" id="ig-deep-area">
    <span class="assess-label">In how many areas does your knowledge go beyond surface-level familiarity to understanding underlying principles?</span>
    <span class="assess-hint">Could you explain why something works, not just that it does? Could you teach it to someone else?</span>
    <select id="a-deep-area" onchange="handleAssessInput('a-deep-area')">
        <option value="">Select...</option>
        <option value="none">None &ndash; my knowledge is mostly surface-level</option>
        <option value="one">One area &ndash; I have genuine depth in a single subject</option>
        <option value="two-three">Two or three &ndash; I understand principles in a few domains</option>
        <option value="several">Several &ndash; I have deep knowledge across multiple fields</option>
        <option value="many">Many &ndash; I could teach several subjects at an advanced level</option>
    </select> <span class="assess-percentile-hint" id="pct-deep-area"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-deep-area" onchange="handleSkip('a-deep-area')"><label for="skip-deep-area">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-assumption-check">
    <span class="assess-label">How rigorously have you tested your understanding in subjects you consider yourself knowledgeable about?</span>
    <span class="assess-hint">Have you read serious books or taken courses, or is your knowledge mostly from articles and conversation?</span>
    <select id="a-assumption-check" onchange="handleAssessInput('a-assumption-check')">
        <option value="">Select...</option>
        <option value="untested">Untested &ndash; my knowledge is mostly from casual sources</option>
        <option value="light">Lightly tested &ndash; I've read a book or two in my main interest areas</option>
        <option value="moderate">Moderately tested &ndash; I've studied formally or read extensively in some areas</option>
        <option value="rigorous">Rigorously tested &ndash; I've sought out challenges to my understanding</option>
        <option value="ongoing">Continuously tested &ndash; I regularly expose my views to informed criticism</option>
    </select> <span class="assess-percentile-hint" id="pct-assumption-check"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-assumption-check" onchange="handleSkip('a-assumption-check')"><label for="skip-assumption-check">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-nuance">
    <span class="assess-label">How well can you articulate the strongest arguments against your own views?</span>
    <span class="assess-hint">If you can't steelman the opposition, your understanding may be shallower than it feels.</span>
    <select id="a-nuance" onchange="handleAssessInput('a-nuance')">
        <option value="">Select...</option>
        <option value="cant">I can't do this for any of my views</option>
        <option value="weak">I can do it weakly &ndash; I know the other side exists but can't present it fairly</option>
        <option value="one-topic">I can do it well for one or two topics</option>
        <option value="several">I can do it for several important topics</option>
        <option value="habit">It's a habit &ndash; I routinely test my views by arguing the other side</option>
    </select> <span class="assess-percentile-hint" id="pct-nuance"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-nuance" onchange="handleSkip('a-nuance')"><label for="skip-nuance">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Utility</h4>

<div class="assess-input-group" id="ig-decision-quality">
    <span class="assess-label">How often does your understanding of how systems work lead to better real-world decisions?</span>
    <span class="assess-hint">A career choice, financial decision, or navigating an institutional process, for instance.</span>
    <select id="a-decision-quality" onchange="handleAssessInput('a-decision-quality')">
        <option value="">Select...</option>
        <option value="rarely">Rarely &ndash; I can't point to clear examples</option>
        <option value="occasionally">Occasionally &ndash; once or twice in the past year</option>
        <option value="sometimes">Sometimes &ndash; several times a year</option>
        <option value="often">Often &ndash; my understanding regularly gives me an edge</option>
        <option value="consistently">Consistently &ndash; systems thinking is central to how I make decisions</option>
    </select> <span class="assess-percentile-hint" id="pct-decision-quality"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-decision-quality" onchange="handleSkip('a-decision-quality')"><label for="skip-decision-quality">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-manipulation">
    <span class="assess-label">How reliably can you identify manipulation tactics in advertising, politics, or social situations?</span>
    <span class="assess-hint">Think about dark patterns online, rhetorical tricks in news coverage, or high-pressure sales tactics.</span>
    <select id="a-manipulation" onchange="handleAssessInput('a-manipulation')">
        <option value="">Select...</option>
        <option value="poorly">Poorly &ndash; I probably miss most of them</option>
        <option value="sometimes">Sometimes &ndash; I catch the obvious ones</option>
        <option value="usually">Usually &ndash; I spot most common tactics</option>
        <option value="well">Well &ndash; I can name the specific technique being used</option>
        <option value="very-well">Very well &ndash; I notice subtle manipulation and can explain the mechanism</option>
    </select> <span class="assess-percentile-hint" id="pct-manipulation"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-manipulation" onchange="handleSkip('a-manipulation')"><label for="skip-manipulation">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-prediction">
    <span class="assess-label">How accurate are your predictions about events?</span>
    <span class="assess-hint">Most people overestimate their predictive accuracy. Have you ever tracked your predictions?</span>
    <select id="a-prediction" onchange="handleAssessInput('a-prediction')">
        <option value="">Select...</option>
        <option value="no-idea">No idea &ndash; I've never tracked or thought about this</option>
        <option value="poor">Probably poor &ndash; I suspect I'm wrong more than I think</option>
        <option value="average">Average &ndash; I'm right sometimes but not reliably</option>
        <option value="above-average">Above average &ndash; I have some evidence my predictions are decent</option>
        <option value="tracked">I've tracked predictions and my calibration is good</option>
    </select> <span class="assess-percentile-hint" id="pct-prediction"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-prediction" onchange="handleSkip('a-prediction')"><label for="skip-prediction">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Meaning</h4>

<div class="assess-input-group" id="ig-purpose">
    <span class="assess-label">Does your worldview give you a sense of purpose and direction?</span>
    <span class="assess-hint">Do you have a framework for deciding what matters, or do you mostly react to whatever feels urgent?</span>
    <select id="a-purpose" onchange="handleAssessInput('a-purpose')">
        <option value="">Select...</option>
        <option value="adrift">No &ndash; I feel adrift on larger questions</option>
        <option value="fragmented">Somewhat &ndash; I have fragments but no coherent picture</option>
        <option value="developing">Developing &ndash; I'm working towards a framework but it's incomplete</option>
        <option value="solid">Yes &ndash; I have a solid sense of what matters and why</option>
        <option value="tested">Yes, and it's been tested by difficult circumstances</option>
    </select> <span class="assess-percentile-hint" id="pct-purpose"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-purpose" onchange="handleSkip('a-purpose')"><label for="skip-purpose">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-resilience">
    <span class="assess-label">How well does your worldview hold up during difficult periods?</span>
    <span class="assess-hint">Think about the last time something went seriously wrong. Did your understanding of the world help you cope?</span>
    <select id="a-resilience" onchange="handleAssessInput('a-resilience')">
        <option value="">Select...</option>
        <option value="crumbles">It crumbles &ndash; difficulty makes me question everything</option>
        <option value="shaken">It gets shaken &ndash; I lose confidence in my framework</option>
        <option value="holds">It mostly holds &ndash; I wobble but return to my beliefs</option>
        <option value="stable">It's stable &ndash; my worldview provides genuine comfort during hardship</option>
        <option value="strengthened">It's strengthened by difficulty &ndash; hard times deepen my understanding</option>
    </select> <span class="assess-percentile-hint" id="pct-resilience"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-resilience" onchange="handleSkip('a-resilience')"><label for="skip-resilience">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-moral-framework">
    <span class="assess-label">How clearly can you articulate the moral principles that guide your major decisions?</span>
    <span class="assess-hint">Not everyone has a formal ethical system, but most people have implicit rules. Can you name yours?</span>
    <select id="a-moral-framework" onchange="handleAssessInput('a-moral-framework')">
        <option value="">Select...</option>
        <option value="none">I can't articulate any guiding principles</option>
        <option value="vague">I have a vague sense but couldn't write them down</option>
        <option value="some">I could name a few principles but I'm not sure where they come from</option>
        <option value="clear">I have clear principles and I know their origins</option>
        <option value="examined">I have well-examined principles I've tested and refined over time</option>
    </select> <span class="assess-percentile-hint" id="pct-moral-framework"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-moral-framework" onchange="handleSkip('a-moral-framework')"><label for="skip-moral-framework">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-breadth">
        <span class="assess-summary-label">Breadth</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-breadth" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-breadth">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-depth">
        <span class="assess-summary-label">Depth</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-depth" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-depth">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-utility">
        <span class="assess-summary-label">Utility</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-utility" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-utility">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-meaning">
        <span class="assess-summary-label">Meaning</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-meaning" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-meaning">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published data on knowledge breadth, critical thinking, prediction accuracy, and meaning-making. All items in this area are scored.</p>
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

<p>You now understand why worldview matters, what different people get out of developing theirs, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about breadth, depth, utility, and meaning. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/worldview/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Worldview Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Worldview. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/worldview/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'worldview';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-domains-map', 'a-cross-domain', 'a-blind-spots',
        'a-deep-area', 'a-assumption-check', 'a-nuance',
        'a-decision-quality', 'a-manipulation', 'a-prediction',
        'a-purpose', 'a-resilience', 'a-moral-framework'
    ];

    var THRESHOLDS = {
        'a-domains-map': [
            // ~50% have deep gaps in most domains; integrated cross-domain knowledge is ~5%
            {v:'one-two',p:10},{v:'few',p:30},{v:'several',p:55},{v:'most',p:80},{v:'integrated',p:97}
        ],
        'a-cross-domain': [
            // ~30% never notice cross-domain connections; constant cross-domain thinking is ~8%
            {v:'never',p:8},{v:'rarely',p:25},{v:'sometimes',p:50},{v:'often',p:78},{v:'constantly',p:95}
        ],
        'a-blind-spots': [
            // ~40% haven't thought about knowledge gaps; systematic mapping is ~5%
            {v:'unaware',p:10},{v:'vague',p:28},{v:'one-two',p:52},{v:'several',p:78},{v:'mapped',p:97}
        ],
        'a-deep-area': [
            // ~30% have only surface-level knowledge; teaching many subjects at advanced level is ~5%
            {v:'none',p:10},{v:'one',p:30},{v:'two-three',p:55},{v:'several',p:80},{v:'many',p:97}
        ],
        'a-assumption-check': [
            // ~40% have untested knowledge; continuously exposing views to criticism is ~5%
            {v:'untested',p:10},{v:'light',p:30},{v:'moderate',p:55},{v:'rigorous',p:80},{v:'ongoing',p:97}
        ],
        'a-nuance': [
            // ~35% can't steelman any of their views; habitual steelmanning is ~5%
            {v:'cant',p:8},{v:'weak',p:25},{v:'one-topic',p:50},{v:'several',p:78},{v:'habit',p:97}
        ],
        'a-decision-quality': [
            // ~30% rarely see worldview improving decisions; consistent systems thinking is ~8%
            {v:'rarely',p:10},{v:'occasionally',p:30},{v:'sometimes',p:55},{v:'often',p:78},{v:'consistently',p:95}
        ],
        'a-manipulation': [
            // ~25% miss most manipulation tactics; noticing subtle mechanisms is ~10%
            {v:'poorly',p:8},{v:'sometimes',p:28},{v:'usually',p:52},{v:'well',p:78},{v:'very-well',p:95}
        ],
        'a-prediction': [
            // ~55% have never tracked predictions; tracked with good calibration is ~3%
            {v:'no-idea',p:10},{v:'poor',p:30},{v:'average',p:52},{v:'above-average',p:78},{v:'tracked',p:97}
        ],
        'a-purpose': [
            // ~25% feel adrift; tested framework surviving difficulty is ~12%
            {v:'adrift',p:8},{v:'fragmented',p:25},{v:'developing',p:50},{v:'solid',p:78},{v:'tested',p:95}
        ],
        'a-resilience': [
            // ~20% find worldview crumbles under stress; strengthened by difficulty is ~12%
            {v:'crumbles',p:8},{v:'shaken',p:25},{v:'holds',p:50},{v:'stable',p:78},{v:'strengthened',p:95}
        ],
        'a-moral-framework': [
            // ~30% can't articulate any guiding principles; well-examined and refined is ~8%
            {v:'none',p:8},{v:'vague',p:25},{v:'some',p:50},{v:'clear',p:78},{v:'examined',p:95}
        ]
    };

    var VALUE_ITEMS = {
        breadth: ['a-domains-map', 'a-cross-domain', 'a-blind-spots'],
        depth: ['a-deep-area', 'a-assumption-check', 'a-nuance'],
        utility: ['a-decision-quality', 'a-manipulation', 'a-prediction'],
        meaning: ['a-purpose', 'a-resilience', 'a-moral-framework']
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
        ['breadth', 'depth', 'utility', 'meaning'].forEach(function(vk) {
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
        ['breadth', 'depth', 'utility', 'meaning'].forEach(function(vk) {
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
