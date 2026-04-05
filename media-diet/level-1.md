---
layout: default
title: "Media Diet – Level 1: Awareness"
life_area_slug: media-diet
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

<h1>Media Diet: Level 1</h1>

<p class="l1-subtitle">Understand what a media diet is, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Media Diet Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why your media diet matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>The information you consume shapes how you understand the world, the decisions you make, and the quality of your thinking. Yet most people's information intake is determined largely by algorithms and habit rather than deliberate choice.</p>

<p>The average knowledge worker checks email <a href="https://hbr.org/2019/01/how-to-spend-way-less-time-on-email-every-day" target="_blank">every six minutes</a> and spends a substantial portion of the day processing fragmented information. Research suggests that this reactive consumption pattern <a href="https://www.sciencedirect.com/science/article/abs/pii/S0747563217305216" target="_blank">increases anxiety</a> and reduces the capacity for sustained attention, without proportionally improving understanding.</p>

<p>People who intentionally curate their information sources tend to develop more accurate mental models, make better predictions, and experience less cognitive fatigue. Philip Tetlock's research on <a href="https://press.princeton.edu/books/hardcover/9780691175904/superforecasting" target="_blank">superforecasters</a> found that the best predictors consume information from diverse, high-quality sources and actively seek out viewpoints that challenge their assumptions.</p>

<p>A well-constructed media diet also compounds over time. The sources you choose today shape the frameworks you use to interpret new information for years. Few other habits have such a broad and lasting influence on your intellectual development.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about media diet</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People curate their information consumption for different reasons. This site scores every media diet intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Information Quality & Depth</h3>
<p>The accuracy, nuance, and intellectual rigour of consumed information. Prioritising books over articles, primary sources over summaries, expert analysis over hot takes, and comprehensive coverage over fragmented updates. People who lean towards this value invest time in fewer, higher-quality sources that provide deep understanding.</p>

<h3>Actionable Relevance</h3>
<p>How directly the information supports decision-making and practical outcomes in your life. Career-relevant developments, investment insights, health discoveries, and information that changes behaviour or choices. Those who lean towards this value curate their consumption around information with clear utility for their specific circumstances and goals.</p>

<h3>Breadth & Discovery</h3>
<p>Exposure to diverse perspectives, unexpected insights, and information outside your existing knowledge areas. Following curiosity into unfamiliar domains, consuming content from different cultural perspectives, and maintaining intellectual openness to ideas that might reshape your thinking. People who lean towards this value deliberately seek out information that challenges assumptions and expands mental models.</p>

<h3>Cognitive Efficiency</h3>
<p>Optimising the retention-to-effort ratio and minimising cognitive overhead from information consumption. Choosing formats that match your processing style, avoiding redundant coverage, and consuming information at optimal timing and frequency. Those who lean towards this value focus on maximum informational value with minimal mental fatigue or wasted attention.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each media diet value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Information Quality & Depth &ndash; Level 5</div>
    <p><a href="https://tylercowen.com/" target="_blank">Tyler Cowen</a> is an economics professor at George Mason University who reads roughly 50 &ndash; 80 books per year across economics, history, fiction, science, and philosophy. He maintains <a href="https://marginalrevolution.com/" target="_blank">Marginal Revolution</a>, where he has published daily posts synthesising academic papers, policy documents, and primary sources for over twenty years. His reading method &ndash; skimming aggressively, abandoning books quickly, and focusing retention on what changes his thinking &ndash; reflects an unusually disciplined approach to information quality.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Actionable Relevance &ndash; Level 5</div>
    <p><a href="https://patrickcollison.com/" target="_blank">Patrick Collison</a>, co-founder of Stripe, maintains a public bookshelf and has spoken extensively about how his reading directly informs business and policy decisions. His information diet spans economic history, infrastructure development, and scientific progress, and he has described specific cases where insights from these domains shaped Stripe's strategy. His reading appears tightly integrated with his decision-making rather than pursued as a separate activity.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Breadth & Discovery &ndash; Level 5</div>
    <p><a href="https://www.mariapopova.com/" target="_blank">Maria Popova</a> created <a href="https://www.themarginalian.org/" target="_blank">The Marginalian</a> (formerly Brain Pickings), where she has published daily essays connecting ideas across philosophy, science, art, literature, and psychology for over fifteen years. Her work draws on sources spanning centuries and disciplines, and she reads in multiple languages. The site is a public record of an exceptionally broad and sustained information diet.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Cognitive Efficiency &ndash; Level 5</div>
    <p><a href="https://calnewport.com/" target="_blank">Cal Newport</a> is a computer science professor at Georgetown who has written extensively about attention management and deep work. He does not use social media, limits his news consumption to a small number of curated sources, and has described specific systems for batching information processing and protecting cognitive resources. His academic output &ndash; multiple books and a consistent research programme &ndash; suggests these practices translate into measurable productivity.</p>
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
<h4>Information Quality &amp; Depth</h4>

<div class="assess-input-group" id="ig-source-types">
    <span class="assess-label">What proportion of your information comes from long-form sources versus short-form?</span>
    <span class="assess-hint">Long-form: books, in-depth articles, documentaries. Short-form: social media, news headlines, notifications.</span>
    <select id="a-source-types" onchange="handleAssessInput('a-source-types')">
        <option value="">Select...</option>
        <option value="almost-all-short">Almost all short-form</option>
        <option value="mostly-short">Mostly short-form with occasional long-form</option>
        <option value="roughly-even">Roughly even</option>
        <option value="mostly-long">Mostly long-form with occasional short-form</option>
        <option value="almost-all-long">Almost all long-form</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-source-types" onchange="handleSkip('a-source-types')"><label for="skip-source-types">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-books-read">
    <span class="assess-label">How many non-fiction books did you read in the past year?</span>
    <span class="assess-hint">Include audiobooks if you use them.</span>
    <select id="a-books-read" onchange="handleAssessInput('a-books-read')">
        <option value="">Select...</option>
        <option value="zero">Zero</option>
        <option value="1-3">1&ndash;3</option>
        <option value="4-10">4&ndash;10</option>
        <option value="11-20">11&ndash;20</option>
        <option value="over-20">Over 20</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-books-read" onchange="handleSkip('a-books-read')"><label for="skip-books-read">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-primary-sources">
    <span class="assess-label">How often do you read primary sources rather than summaries or commentary?</span>
    <span class="assess-hint">Academic papers, original reports, legislation, company filings.</span>
    <select id="a-primary-sources" onchange="handleAssessInput('a-primary-sources')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I always rely on summaries</option>
        <option value="rarely">Rarely &ndash; once or twice in the past year</option>
        <option value="sometimes">Sometimes &ndash; for topics I care deeply about</option>
        <option value="regularly">Regularly &ndash; multiple times a month</option>
        <option value="routinely">Routinely &ndash; primary sources are my default</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-primary-sources" onchange="handleSkip('a-primary-sources')"><label for="skip-primary-sources">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Actionable Relevance</h4>

<div class="assess-input-group" id="ig-decision-influence">
    <span class="assess-label">How often has something you read or listened to directly influenced a decision in the past year?</span>
    <span class="assess-hint">Career moves, financial choices, health changes, relationship approaches.</span>
    <select id="a-decision-influence" onchange="handleAssessInput('a-decision-influence')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I can't think of an example</option>
        <option value="once">Once &ndash; a single clear instance</option>
        <option value="a-few">A few times</option>
        <option value="regularly">Regularly &ndash; my consumption frequently informs decisions</option>
        <option value="consistently">Consistently &ndash; most of what I consume is chosen for its decision relevance</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-decision-influence" onchange="handleSkip('a-decision-influence')"><label for="skip-decision-influence">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-goal-alignment">
    <span class="assess-label">How well do your current information sources align with your actual goals and priorities?</span>
    <span class="assess-hint">Compare what you consume most with what you're trying to achieve.</span>
    <select id="a-goal-alignment" onchange="handleAssessInput('a-goal-alignment')">
        <option value="">Select...</option>
        <option value="no-alignment">No alignment &ndash; I haven't thought about this</option>
        <option value="poor">Poor &ndash; most of what I consume is unrelated to my goals</option>
        <option value="partial">Partial &ndash; some sources are relevant, many aren't</option>
        <option value="good">Good &ndash; most of my consumption supports my priorities</option>
        <option value="deliberate">Deliberate &ndash; I've curated my sources specifically around my goals</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-goal-alignment" onchange="handleSkip('a-goal-alignment')"><label for="skip-goal-alignment">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-noise-ratio">
    <span class="assess-label">How much of your weekly information consumption has no practical application to your life?</span>
    <span class="assess-hint">Content that's interesting but doesn't inform any decision or skill.</span>
    <select id="a-noise-ratio" onchange="handleAssessInput('a-noise-ratio')">
        <option value="">Select...</option>
        <option value="almost-all">Almost all &ndash; very little of what I consume is useful</option>
        <option value="most">Most &ndash; I consume a lot of noise</option>
        <option value="about-half">About half</option>
        <option value="some">Some &ndash; most of what I consume serves a purpose</option>
        <option value="very-little">Very little &ndash; my consumption is tightly curated</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-noise-ratio" onchange="handleSkip('a-noise-ratio')"><label for="skip-noise-ratio">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Breadth &amp; Discovery</h4>

<div class="assess-input-group" id="ig-echo-chamber">
    <span class="assess-label">How diverse are the perspectives across your regular information sources?</span>
    <span class="assess-hint">Think about the range of political, cultural, and intellectual viewpoints.</span>
    <select id="a-echo-chamber" onchange="handleAssessInput('a-echo-chamber')">
        <option value="">Select...</option>
        <option value="very-narrow">Very narrow &ndash; all my sources share similar views</option>
        <option value="somewhat-narrow">Somewhat narrow &ndash; mostly one perspective with rare exceptions</option>
        <option value="moderate">Moderate &ndash; some diversity but within a limited range</option>
        <option value="broad">Broad &ndash; I regularly encounter different perspectives</option>
        <option value="deliberately-diverse">Deliberately diverse &ndash; I actively seek out opposing or unfamiliar viewpoints</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-echo-chamber" onchange="handleSkip('a-echo-chamber')"><label for="skip-echo-chamber">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-unfamiliar-topics">
    <span class="assess-label">When did you last deliberately explore a topic you knew nothing about?</span>
    <span class="assess-hint">Something you chose out of curiosity, not something recommended by an algorithm.</span>
    <select id="a-unfamiliar-topics" onchange="handleAssessInput('a-unfamiliar-topics')">
        <option value="">Select...</option>
        <option value="cant-recall">Can't recall</option>
        <option value="months-ago">Months ago</option>
        <option value="weeks-ago">Weeks ago</option>
        <option value="this-week">This week</option>
        <option value="constantly">Constantly &ndash; I regularly explore unfamiliar topics</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-unfamiliar-topics" onchange="handleSkip('a-unfamiliar-topics')"><label for="skip-unfamiliar-topics">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-international">
    <span class="assess-label">How often do you consume information from sources based outside your own country?</span>
    <span class="assess-hint">News outlets, commentators, or publications from other regions.</span>
    <select id="a-international" onchange="handleAssessInput('a-international')">
        <option value="">Select...</option>
        <option value="never">Never</option>
        <option value="rarely">Rarely &ndash; once or twice a year</option>
        <option value="sometimes">Sometimes &ndash; monthly</option>
        <option value="regularly">Regularly &ndash; weekly</option>
        <option value="daily">Daily &ndash; international sources are a core part of my diet</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-international" onchange="handleSkip('a-international')"><label for="skip-international">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Cognitive Efficiency</h4>

<div class="assess-input-group" id="ig-time-spent">
    <span class="assess-label">How many hours per day do you spend consuming news, social media, and informational content?</span>
    <span class="assess-hint">Screen time data on your phone can help here.</span>
    <select id="a-time-spent" onchange="handleAssessInput('a-time-spent')">
        <option value="">Select...</option>
        <option value="over-6">Over 6 hours</option>
        <option value="4-6">4&ndash;6 hours</option>
        <option value="2-4">2&ndash;4 hours</option>
        <option value="1-2">1&ndash;2 hours</option>
        <option value="under-1">Under 1 hour</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-time-spent" onchange="handleSkip('a-time-spent')"><label for="skip-time-spent">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-retention">
    <span class="assess-label">Could you summarise the most important thing you read last week?</span>
    <span class="assess-hint">Try it now. If nothing comes to mind, that's useful information.</span>
    <select id="a-retention" onchange="handleAssessInput('a-retention')">
        <option value="">Select...</option>
        <option value="nothing">Nothing comes to mind</option>
        <option value="vague">Vague topic only &ndash; I remember the subject but no detail</option>
        <option value="general">General summary &ndash; I can describe the main point</option>
        <option value="clear">Clear summary &ndash; I can explain the argument and key evidence</option>
        <option value="detailed">Detailed &ndash; I could discuss it with someone knowledgeable</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-retention" onchange="handleSkip('a-retention')"><label for="skip-retention">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-overload">
    <span class="assess-label">Do you regularly experience information overload or anxiety about keeping up?</span>
    <span class="assess-hint">A sense of falling behind, compulsive checking, or fatigue from too much input.</span>
    <select id="a-overload" onchange="handleAssessInput('a-overload')">
        <option value="">Select...</option>
        <option value="severe">Severe &ndash; I feel overwhelmed daily</option>
        <option value="frequent">Frequent &ndash; several times a week</option>
        <option value="occasional">Occasional &ndash; it happens but I manage it</option>
        <option value="rare">Rare &ndash; I seldom feel overloaded</option>
        <option value="none">None &ndash; I feel in control of my information intake</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-overload" onchange="handleSkip('a-overload')"><label for="skip-overload">I know but prefer not to say</label></div>
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

<p>You now understand why your media diet matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about information quality, actionable relevance, breadth, and cognitive efficiency. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/media-diet/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Media Diet Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Media Diet. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/media-diet/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'media-diet';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-source-types', 'a-books-read', 'a-primary-sources',
        'a-decision-influence', 'a-goal-alignment', 'a-noise-ratio',
        'a-echo-chamber', 'a-unfamiliar-topics', 'a-international',
        'a-time-spent', 'a-retention', 'a-overload'
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
            quality: null,
            relevance: null,
            breadth: null,
            efficiency: null
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
