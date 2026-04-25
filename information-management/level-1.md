---
layout: default
title: "Information Management – Level 1: Awareness"
life_area_slug: information-management
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

<h1>Information Management: Level 1</h1>

<p class="l1-subtitle">Understand what information management is, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Information Management Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why information management matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Most of what you read, hear, and learn disappears within weeks. Research on the <a href="https://en.wikipedia.org/wiki/Forgetting_curve" target="_blank">forgetting curve</a> consistently shows that people lose 70 &ndash; 80% of newly learned information within days unless they take active steps to retain it. For most people, the books they read last year might as well not have been read at all.</p>

<p>The cost goes beyond wasted reading time. Without a reliable way to capture and retrieve information, you end up re-researching the same questions, losing track of useful sources, and making decisions based on whatever happens to be in your head at the time. Surveys of knowledge workers suggest they spend <a href="https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-social-economy" target="_blank">15 &ndash; 30% of their working hours</a> searching for information they have encountered before.</p>

<p>Good information management compounds over time. Each piece of well-organised knowledge makes future learning easier, because you have more existing context to connect new ideas to. People who maintain effective personal knowledge systems tend to develop richer mental models, spot patterns across domains more readily, and make better-informed decisions.</p>

<p>The good news is that even simple, consistent practices &ndash; a reliable place to capture notes, a workable way to find them again &ndash; put you well ahead of most people. You do not need a sophisticated system to see substantial benefits.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about information management</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People manage information for different reasons. This site scores every information management intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Information Retention</h3>
<p>Capturing and preserving valuable insights, ideas, and knowledge from various sources without losing them over time. Comprehensive coverage &ndash; the more you retain, the more valuable your knowledge base becomes. People who lean towards this value focus on broad capture across many sources and contexts, and measure success by how little slips through the cracks.</p>

<h3>Retrieval Efficiency</h3>
<p>Finding the right information quickly when you need it. Having relevant knowledge accessible at decision points is what makes information management valuable for real-world outcomes. People who lean towards this value focus on search capabilities, organisation schemes, and fast access &ndash; and judge their system by how quickly it surfaces what they need.</p>

<h3>Insight Generation</h3>
<p>Connecting ideas across sources to generate new understanding, identify patterns, and develop original thinking. People who lean towards this value focus on systems that help them see relationships between concepts and build coherent mental models. They want their notes to produce ideas they would not have had otherwise.</p>

<h3>System Simplicity</h3>
<p>Preferring approaches that minimise ongoing cognitive overhead and maintenance burden, whether through minimal analogue systems (notebooks, index cards) or highly automated digital setups. People who lean towards this value want their information system to support their thinking without becoming a project unto itself.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each information management value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Information Retention &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Niklas_Luhmann" target="_blank">Niklas Luhmann</a> was a German sociologist who maintained a Zettelkasten (slip-box) of roughly 90,000 index cards over three decades. Each card captured a single idea with cross-references to related cards, allowing him to preserve and connect insights across his entire reading life. He published over 70 books and 400 articles, and attributed much of his productivity to the system's ability to retain and surface ideas that would otherwise have been forgotten. The archive is now <a href="https://niklas-luhmann-archiv.de/bestand/zettelkasten/zettel/ZK_1_NB_1_1_V" target="_blank">digitised and publicly accessible</a>.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Retrieval Efficiency &ndash; Level 5</div>
    <p><a href="https://www.gwern.net/About" target="_blank">Gwern Branwen</a> maintains an extensive personal website covering statistics, psychology, technology, and philosophy, with a sophisticated tagging and cross-linking system. His pages are heavily annotated with sources, and he has described his workflow for rapidly locating prior research across thousands of notes and references. The site functions as a public demonstration of a retrieval system that makes years of accumulated knowledge accessible within seconds.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Insight Generation &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Vannevar_Bush" target="_blank">Vannevar Bush</a> was a scientist and engineer who directed the U.S. Office of Scientific Research and Development during the Second World War. His 1945 essay <a href="https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/" target="_blank">"As We May Think"</a> described the Memex, a hypothetical device for storing and cross-referencing personal knowledge &ndash; effectively anticipating hypertext and personal knowledge management systems decades before they existed. Bush's ability to synthesise insights across electrical engineering, analogue computing, and library science into a coherent vision exemplifies cross-domain insight generation at an exceptional level.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">System Simplicity &ndash; Level 5</div>
    <p><a href="https://rfrfrfr.substack.com/" target="_blank">Robert Greene</a> has described a consistent, low-tech research system he has used across all of his books, including <em>The 48 Laws of Power</em> and <em>Mastery</em>. He reads widely, writes notes on index cards with thematic labels, and sorts them into categories by hand. The system involves no specialised software and has remained essentially unchanged for over 25 years, yet it has supported the synthesis of hundreds of sources per book. Its longevity and simplicity, given the volume of material it handles, make it a strong example of sustainable system design.</p>
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
<h4>Information Retention</h4>

<div class="assess-input-group" id="ig-capture-method">
    <span class="assess-label">Do you have a consistent method for capturing notes from what you read, watch, or hear?</span>
    <span class="assess-hint">A notebook, an app, marginalia, or nothing at all.</span>
    <select id="a-capture-method" onchange="handleAssessInput('a-capture-method')">
        <option value="">Select...</option>
        <option value="nothing">Nothing &ndash; I don't capture information</option>
        <option value="occasional">Occasional &ndash; I sometimes jot things down but inconsistently</option>
        <option value="one-method">One method &ndash; I have a go-to tool I use fairly often</option>
        <option value="consistent">Consistent &ndash; I reliably capture from most sources</option>
        <option value="systematic">Systematic &ndash; I have a structured capture process I follow for everything</option>
    </select> <span class="assess-percentile-hint" id="pct-capture-method"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-capture-method" onchange="handleSkip('a-capture-method')"><label for="skip-capture-method">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-retention-rate">
    <span class="assess-label">How much do you retain from books or articles you read more than a month ago?</span>
    <span class="assess-hint">Pick something you read recently and try to recall the key points.</span>
    <select id="a-retention-rate" onchange="handleAssessInput('a-retention-rate')">
        <option value="">Select...</option>
        <option value="almost-nothing">Almost nothing &ndash; can barely recall reading it</option>
        <option value="title-only">Title and topic only</option>
        <option value="main-points">Main points &ndash; I remember the core argument</option>
        <option value="good-detail">Good detail &ndash; I can summarise and recall key evidence</option>
        <option value="thorough">Thorough &ndash; I can discuss it in depth weeks later</option>
    </select> <span class="assess-percentile-hint" id="pct-retention-rate"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-retention-rate" onchange="handleSkip('a-retention-rate')"><label for="skip-retention-rate">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-capture-sources">
    <span class="assess-label">From which information sources do you actually capture notes?</span>
    <span class="assess-hint">Books, podcasts, conversations, meetings, articles, courses.</span>
    <select id="a-capture-sources" onchange="handleAssessInput('a-capture-sources')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I don't take notes from any source</option>
        <option value="one-type">One type &ndash; I only capture from one kind of source</option>
        <option value="a-few">A few types &ndash; I capture from two or three source types</option>
        <option value="most">Most &ndash; I capture from most sources I encounter</option>
        <option value="comprehensive">Comprehensive &ndash; I have a capture habit for every source type</option>
    </select> <span class="assess-percentile-hint" id="pct-capture-sources"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-capture-sources" onchange="handleSkip('a-capture-sources')"><label for="skip-capture-sources">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Retrieval Efficiency</h4>

<div class="assess-input-group" id="ig-find-speed">
    <span class="assess-label">How long does it take you to find a specific piece of information you've saved before?</span>
    <span class="assess-hint">Think of something you noted down in the past few months.</span>
    <select id="a-find-speed" onchange="handleAssessInput('a-find-speed')">
        <option value="">Select...</option>
        <option value="cant-find">I usually can't find it</option>
        <option value="long-search">Long search &ndash; takes more than 10 minutes</option>
        <option value="moderate">Moderate &ndash; a few minutes of searching</option>
        <option value="quick">Quick &ndash; under a minute</option>
        <option value="instant">Instant &ndash; I know exactly where everything is</option>
    </select> <span class="assess-percentile-hint" id="pct-find-speed"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-find-speed" onchange="handleSkip('a-find-speed')"><label for="skip-find-speed">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-organisation">
    <span class="assess-label">How are your notes and files currently organised?</span>
    <span class="assess-hint">Folders, tags, chronological order, search-only, scattered across multiple apps.</span>
    <select id="a-organisation" onchange="handleAssessInput('a-organisation')">
        <option value="">Select...</option>
        <option value="chaotic">Chaotic &ndash; no organisation, scattered everywhere</option>
        <option value="minimal">Minimal &ndash; a few broad folders but mostly unsorted</option>
        <option value="basic">Basic &ndash; a folder structure I mostly follow</option>
        <option value="structured">Structured &ndash; consistent organisation with folders and/or tags</option>
        <option value="optimised">Optimised &ndash; a well-maintained system I can navigate confidently</option>
    </select> <span class="assess-percentile-hint" id="pct-organisation"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-organisation" onchange="handleSkip('a-organisation')"><label for="skip-organisation">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-reresearch">
    <span class="assess-label">How often do you end up re-researching something you know you've looked into before?</span>
    <span class="assess-hint">Recipes, product comparisons, technical solutions, factual questions.</span>
    <select id="a-reresearch" onchange="handleAssessInput('a-reresearch')">
        <option value="">Select...</option>
        <option value="constantly">Constantly &ndash; I re-research things every week</option>
        <option value="often">Often &ndash; several times a month</option>
        <option value="sometimes">Sometimes &ndash; a few times a month</option>
        <option value="rarely">Rarely &ndash; once a month or less</option>
        <option value="almost-never">Almost never &ndash; I can usually find my previous research</option>
    </select> <span class="assess-percentile-hint" id="pct-reresearch"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-reresearch" onchange="handleSkip('a-reresearch')"><label for="skip-reresearch">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Insight Generation</h4>

<div class="assess-input-group" id="ig-connections">
    <span class="assess-label">How often do you connect ideas from different sources to produce new insights?</span>
    <span class="assess-hint">A conversation that clicked with something you read, or two articles that illuminated each other.</span>
    <select id="a-connections" onchange="handleAssessInput('a-connections')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I consume information but don't connect it</option>
        <option value="rarely">Rarely &ndash; it happens by accident occasionally</option>
        <option value="sometimes">Sometimes &ndash; I notice connections a few times a month</option>
        <option value="regularly">Regularly &ndash; I actively look for connections</option>
        <option value="systematically">Systematically &ndash; my system is designed to surface connections</option>
    </select> <span class="assess-percentile-hint" id="pct-connections"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-connections" onchange="handleSkip('a-connections')"><label for="skip-connections">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-review-habit">
    <span class="assess-label">How regularly do you review or revisit your notes?</span>
    <span class="assess-hint">Do you ever go back to old notes?</span>
    <select id="a-review-habit" onchange="handleAssessInput('a-review-habit')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; notes sit untouched after writing</option>
        <option value="rarely">Rarely &ndash; only when I happen across them</option>
        <option value="occasionally">Occasionally &ndash; every few months</option>
        <option value="regularly">Regularly &ndash; weekly or fortnightly</option>
        <option value="daily">Daily &ndash; review is part of my routine</option>
    </select> <span class="assess-percentile-hint" id="pct-review-habit"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-review-habit" onchange="handleSkip('a-review-habit')"><label for="skip-review-habit">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-synthesis">
    <span class="assess-label">Does your current system help you think, or is it purely for storage?</span>
    <span class="assess-hint">Some systems generate ideas; others just hold them.</span>
    <select id="a-synthesis" onchange="handleAssessInput('a-synthesis')">
        <option value="">Select...</option>
        <option value="no-system">I don't have a system</option>
        <option value="storage-only">Storage only &ndash; it holds information but doesn't help me think</option>
        <option value="occasional">Occasionally helps &ndash; I sometimes find useful things while browsing</option>
        <option value="supports-thinking">Supports thinking &ndash; it regularly surfaces relevant material</option>
        <option value="thinking-tool">Thinking tool &ndash; it actively generates new ideas and connections</option>
    </select> <span class="assess-percentile-hint" id="pct-synthesis"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-synthesis" onchange="handleSkip('a-synthesis')"><label for="skip-synthesis">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>System Simplicity</h4>

<div class="assess-input-group" id="ig-maintenance">
    <span class="assess-label">How much time do you spend maintaining your information system each week?</span>
    <span class="assess-hint">Filing, tagging, reorganising, migrating between tools.</span>
    <select id="a-maintenance" onchange="handleAssessInput('a-maintenance')">
        <option value="">Select...</option>
        <option value="no-system">I don't have a system to maintain</option>
        <option value="excessive">Excessive &ndash; more than 2 hours per week</option>
        <option value="moderate">Moderate &ndash; 1&ndash;2 hours per week</option>
        <option value="light">Light &ndash; under 30 minutes per week</option>
        <option value="minimal">Minimal &ndash; the system mostly maintains itself</option>
    </select> <span class="assess-percentile-hint" id="pct-maintenance"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-maintenance" onchange="handleSkip('a-maintenance')"><label for="skip-maintenance">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-abandoned">
    <span class="assess-label">How many information management tools or systems have you tried and abandoned?</span>
    <span class="assess-hint">Apps, notebooks, methods &ndash; anything you started with good intentions and stopped using.</span>
    <select id="a-abandoned" onchange="handleAssessInput('a-abandoned')">
        <option value="">Select...</option>
        <option value="many">Many &ndash; five or more</option>
        <option value="several">Several &ndash; three or four</option>
        <option value="a-couple">A couple &ndash; one or two</option>
        <option value="one-stable">One stable system &ndash; I've stuck with my current approach</option>
        <option value="never-tried">I've never tried to set one up</option>
    </select> <span class="assess-percentile-hint" id="pct-abandoned"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-abandoned" onchange="handleSkip('a-abandoned')"><label for="skip-abandoned">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-friction">
    <span class="assess-label">Does your current approach feel sustainable or does it create friction you tend to avoid?</span>
    <span class="assess-hint">Do you skip capturing things because the process feels like too much effort?</span>
    <select id="a-friction" onchange="handleAssessInput('a-friction')">
        <option value="">Select...</option>
        <option value="high-friction">High friction &ndash; I avoid using it because it's too much effort</option>
        <option value="some-friction">Some friction &ndash; I use it but it often feels like a chore</option>
        <option value="neutral">Neutral &ndash; it's fine but not seamless</option>
        <option value="low-friction">Low friction &ndash; it's easy enough that I use it consistently</option>
        <option value="effortless">Effortless &ndash; capturing and organising feels natural</option>
    </select> <span class="assess-percentile-hint" id="pct-friction"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-friction" onchange="handleSkip('a-friction')"><label for="skip-friction">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-retention">
        <span class="assess-summary-label">Information Retention</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-retention" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-retention">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-retrieval">
        <span class="assess-summary-label">Retrieval Efficiency</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-retrieval" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-retrieval">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-insight">
        <span class="assess-summary-label">Insight Generation</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-insight" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-insight">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-simplicity">
        <span class="assess-summary-label">System Simplicity</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-simplicity" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-simplicity">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published data on personal knowledge management practices among adults. All items in this area are scored.</p>
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

<p>You now understand why information management matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about information retention, retrieval efficiency, insight generation, and system simplicity. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/information-management/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Information Management Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Information Management. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/information-management/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'information-management';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-capture-method',
        'a-retention-rate',
        'a-capture-sources',
        'a-find-speed',
        'a-organisation',
        'a-reresearch',
        'a-connections',
        'a-review-habit',
        'a-synthesis',
        'a-maintenance',
        'a-abandoned',
        'a-friction'
    ];

    var THRESHOLDS = {
        'a-capture-method': [
            // Most people don't capture information systematically; a structured process is very rare
            {v:'nothing',p:15},{v:'occasional',p:35},{v:'one-method',p:55},{v:'consistent',p:78},{v:'systematic',p:95}
        ],
        'a-retention-rate': [
            // Most people retain very little from what they read; thorough recall is rare
            {v:'almost-nothing',p:10},{v:'title-only',p:30},{v:'main-points',p:55},{v:'good-detail',p:78},{v:'thorough',p:95}
        ],
        'a-capture-sources': [
            // Most people capture from zero or one source type; comprehensive capture is very rare
            {v:'none',p:10},{v:'one-type',p:30},{v:'a-few',p:55},{v:'most',p:78},{v:'comprehensive',p:95}
        ],
        'a-find-speed': [
            // Most people struggle to find saved information; instant retrieval is rare
            {v:'cant-find',p:10},{v:'long-search',p:25},{v:'moderate',p:50},{v:'quick',p:78},{v:'instant',p:95}
        ],
        'a-organisation': [
            // Most people's files are minimally organised; an optimised system is rare
            {v:'chaotic',p:10},{v:'minimal',p:25},{v:'basic',p:50},{v:'structured',p:78},{v:'optimised',p:95}
        ],
        'a-reresearch': [
            // Most people frequently re-research things; almost never doing so is uncommon
            {v:'constantly',p:10},{v:'often',p:25},{v:'sometimes',p:50},{v:'rarely',p:78},{v:'almost-never',p:95}
        ],
        'a-connections': [
            // Most people consume information without connecting it; systematic connection is rare
            {v:'never',p:10},{v:'rarely',p:25},{v:'sometimes',p:50},{v:'regularly',p:78},{v:'systematically',p:95}
        ],
        'a-review-habit': [
            // Most people never revisit their notes; daily review is very rare
            {v:'never',p:10},{v:'rarely',p:30},{v:'occasionally',p:50},{v:'regularly',p:78},{v:'daily',p:95}
        ],
        'a-synthesis': [
            // Most people's systems are storage-only; a thinking tool is very rare
            {v:'no-system',p:10},{v:'storage-only',p:25},{v:'occasional',p:50},{v:'supports-thinking',p:78},{v:'thinking-tool',p:95}
        ],
        'a-maintenance': [
            // Having no system or excessive maintenance are both common; minimal self-maintaining is rare
            {v:'no-system',p:15},{v:'excessive',p:25},{v:'moderate',p:50},{v:'light',p:78},{v:'minimal',p:95}
        ],
        'a-abandoned': [
            // Most people have tried and abandoned several tools; one stable system is uncommon
            {v:'many',p:10},{v:'several',p:25},{v:'a-couple',p:50},{v:'one-stable',p:80},{v:'never-tried',p:20}
        ],
        'a-friction': [
            // Most people find information capture effortful; effortless flow is rare
            {v:'high-friction',p:10},{v:'some-friction',p:25},{v:'neutral',p:50},{v:'low-friction',p:78},{v:'effortless',p:95}
        ]
    };

    var VALUE_ITEMS = {
        retention: ['a-capture-method', 'a-retention-rate', 'a-capture-sources'],
        retrieval: ['a-find-speed', 'a-organisation', 'a-reresearch'],
        insight: ['a-connections', 'a-review-habit', 'a-synthesis'],
        simplicity: ['a-maintenance', 'a-abandoned', 'a-friction']
    };

    // All information-management items are scorable
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
        ['retention', 'retrieval', 'insight', 'simplicity'].forEach(function(vk) {
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
        ['retention', 'retrieval', 'insight', 'simplicity'].forEach(function(vk) {
            scores[vk] = computeValuePercentile(vk);
        });
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-scores') || {};
            all[AREA] = scores;
            APStorage.save('ap-level1-scores', all);
        }
    }

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
