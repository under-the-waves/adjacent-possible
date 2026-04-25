---
layout: default
title: "Consumptive Leisure – Level 1: Awareness"
life_area_slug: consumptive-leisure
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

<h1>Consumptive Leisure: Level 1</h1>

<p class="l1-subtitle">Understand what consumptive leisure means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Consumptive Leisure Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why consumptive leisure matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>The average adult spends <a href="https://www.bls.gov/news.release/atus.nr0.htm" target="_blank">over 5 hours per day</a> on leisure activities, and the majority of that time goes to media consumption &ndash; watching, reading, listening, and browsing. How you spend those hours has a substantial effect on your mood, energy, knowledge, and overall quality of life.</p>

<p>Research consistently shows that not all leisure consumption is equal. A <a href="https://link.springer.com/article/10.1007/s12529-024-10307-0" target="_blank">longitudinal study</a> found that different types of screen-based leisure &ndash; social media, news, video, gaming &ndash; have distinct effects on 24 parameters of wellbeing. Some consumption restores and enriches; some merely fills time; some actively depletes.</p>

<p>The good news is that curating your consumptive leisure is one of the most accessible quality-of-life upgrades available. It requires no special equipment, no major life changes, and no money. It requires only awareness of what you currently consume, what effects it has on you, and what you might choose differently.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about consumptive leisure</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People consume media for different reasons. This site scores every consumptive leisure intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Restoration</h3>
<p>Using leisure consumption to genuinely recover from work and stress. Activities that leave you feeling recharged rather than drained. People who lean towards this value are deliberate about choosing media that provides genuine mental rest, and avoid consumption patterns that feel easy but leave them more depleted than before.</p>

<h3>Enrichment</h3>
<p>Consuming media and content that expands your knowledge, perspectives, and capabilities. Reading non-fiction, watching documentaries, listening to educational podcasts, and engaging with challenging art. People who lean towards this value seek to grow through their leisure and retain what they learn.</p>

<h3>Enjoyment</h3>
<p>The direct pleasure and satisfaction derived from leisure activities. Following curiosity, allowing yourself pure entertainment without guilt, and choosing what genuinely delights you rather than what feels productive. People who lean towards this value recognise that joy is a legitimate end in itself.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each consumptive leisure value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Restoration &ndash; Level 5</div>
    <p><a href="https://www.nytimes.com/by/jenny-odell" target="_blank">Jenny Odell</a> is an artist and author whose book <em>How to Do Nothing</em> became a bestseller on the art of resisting the attention economy. She practises and teaches deliberate disengagement from productivity-driven media consumption, using birdwatching, deep observation, and curated reading as restorative practices. Her work demonstrates mastery of using consumptive leisure for genuine recovery rather than mere distraction.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Enrichment &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Susan_Sontag" target="_blank">Susan Sontag</a> was one of the 20th century's most voracious and deliberate consumers of culture &ndash; film, literature, philosophy, theatre, and visual art. Her journals, published posthumously, reveal someone who treated cultural consumption as a serious practice, maintaining detailed reading lists and viewing schedules from her teenage years until her death in 2004. Her critical essays consistently drew connections across domains in ways that reflected genuinely deep engagement with what she consumed.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Enjoyment &ndash; Level 5</div>
    <p><a href="https://letterboxd.com/about/" target="_blank">Matthew Buchanan</a> co-founded Letterboxd, a social platform for film lovers with over 15 million members. His deep, lifelong love of cinema &ndash; not just watching films but savouring, discussing, and curating them &ndash; led him to build a platform that helps millions of others develop their own relationship with film. He exemplifies how genuine enjoyment of a consumptive medium can become a defining source of meaning.</p>
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
<h4>Restoration</h4>

<div class="assess-input-group" id="ig-energy-after">
    <span class="assess-label">Which of your regular leisure activities leave you genuinely recharged versus drained?</span>
    <span class="assess-hint">Think about how you feel after an hour of scrolling versus an hour of reading, for example.</span>
    <select id="a-energy-after" onchange="handleAssessInput('a-energy-after')"><option value="">Select...</option><option value="mostly-drained">Mostly drained &ndash; most of my leisure leaves me sluggish</option><option value="mixed-negative">Mixed &ndash; more draining activities than recharging ones</option><option value="balanced">Balanced &ndash; roughly equal recharging and draining</option><option value="mixed-positive">Mixed &ndash; more recharging activities than draining ones</option><option value="mostly-recharged">Mostly recharged &ndash; my leisure consistently restores my energy</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-energy-after" onchange="handleSkip('a-energy-after')"><label for="skip-energy-after">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-screen-time">
    <span class="assess-label">How much screen time do you spend per day on leisure activities?</span>
    <span class="assess-hint">Check your phone's screen time report or estimate from your typical evening routine.</span>
    <select id="a-screen-time" onchange="handleAssessInput('a-screen-time')"><option value="">Select...</option><option value="over-6">Over 6 hours per day</option><option value="4-to-6">4 &ndash; 6 hours per day</option><option value="2-to-4">2 &ndash; 4 hours per day</option><option value="1-to-2">1 &ndash; 2 hours per day</option><option value="under-1">Under 1 hour per day</option></select> <span class="assess-percentile-hint" id="pct-screen-time"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-screen-time" onchange="handleSkip('a-screen-time')"><label for="skip-screen-time">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-wind-down">
    <span class="assess-label">Do you have a deliberate wind-down routine, or do you default to whatever is easiest when tired?</span>
    <span class="assess-hint">Defaulting is common &ndash; the question is whether you're aware of the pattern.</span>
    <select id="a-wind-down" onchange="handleAssessInput('a-wind-down')"><option value="">Select...</option><option value="always-default">Always default &ndash; I reach for my phone or TV without thinking</option><option value="mostly-default">Mostly default &ndash; I occasionally make a deliberate choice</option><option value="sometimes">Sometimes deliberate &ndash; about half the time I choose intentionally</option><option value="mostly-deliberate">Mostly deliberate &ndash; I usually choose how to wind down</option><option value="always-deliberate">Always deliberate &ndash; I have a consistent, intentional routine</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-wind-down" onchange="handleSkip('a-wind-down')"><label for="skip-wind-down">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Enrichment</h4>

<div class="assess-input-group" id="ig-learning-proportion">
    <span class="assess-label">What proportion of your leisure consumption teaches you something valuable?</span>
    <span class="assess-hint">Books, podcasts, documentaries, articles &ndash; versus passive scrolling, background television, etc.</span>
    <select id="a-learning-proportion" onchange="handleAssessInput('a-learning-proportion')"><option value="">Select...</option><option value="almost-none">Almost none &ndash; my leisure is purely passive</option><option value="small">Small &ndash; under 20%</option><option value="moderate">Moderate &ndash; roughly 20 &ndash; 40%</option><option value="substantial">Substantial &ndash; roughly 40 &ndash; 60%</option><option value="majority">Majority &ndash; over 60% of my leisure has a learning element</option></select> <span class="assess-percentile-hint" id="pct-learning-proportion"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-learning-proportion" onchange="handleSkip('a-learning-proportion')"><label for="skip-learning-proportion">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-books-per-year">
    <span class="assess-label">How many books did you finish in the past year?</span>
    <span class="assess-hint">Include audiobooks and e-books. A rough number is fine.</span>
    <select id="a-books-per-year" onchange="handleAssessInput('a-books-per-year')"><option value="">Select...</option><option value="none">None</option><option value="1-to-3">1 &ndash; 3 books</option><option value="4-to-8">4 &ndash; 8 books</option><option value="9-to-15">9 &ndash; 15 books</option><option value="over-15">Over 15 books</option></select> <span class="assess-percentile-hint" id="pct-books-per-year"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-books-per-year" onchange="handleSkip('a-books-per-year')"><label for="skip-books-per-year">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-retention">
    <span class="assess-label">Can you recall and explain the main ideas from something you consumed recently?</span>
    <span class="assess-hint">If you can't, that's useful information &ndash; it suggests consumption without retention.</span>
    <select id="a-retention" onchange="handleAssessInput('a-retention')"><option value="">Select...</option><option value="no">No &ndash; I struggle to recall details from anything recent</option><option value="vaguely">Vaguely &ndash; I remember the gist but not the substance</option><option value="one-thing">One thing &ndash; I can explain one book, podcast, or documentary well</option><option value="several">Several &ndash; I retain ideas from multiple recent sources</option><option value="consistently">Consistently &ndash; I have a system for retaining what I consume</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-retention" onchange="handleSkip('a-retention')"><label for="skip-retention">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Enjoyment</h4>

<div class="assess-input-group" id="ig-genuine-pleasure">
    <span class="assess-label">Can you name 3 &ndash; 5 media sources you reliably enjoy?</span>
    <span class="assess-hint">Sources you actively look forward to, not just whatever appears in your feed.</span>
    <select id="a-genuine-pleasure" onchange="handleAssessInput('a-genuine-pleasure')"><option value="">Select...</option><option value="no">No &ndash; I mostly consume whatever the algorithm serves me</option><option value="one-or-two">One or two &ndash; a couple of favourites</option><option value="three-to-five">Three to five &ndash; a solid set of reliable sources</option><option value="many">Many &ndash; a curated collection across different media</option><option value="extensive">Extensive &ndash; a rich, diverse media diet I've built deliberately</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-genuine-pleasure" onchange="handleSkip('a-genuine-pleasure')"><label for="skip-genuine-pleasure">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-wasted-time">
    <span class="assess-label">How much of your leisure time do you spend on things you don't actually enjoy?</span>
    <span class="assess-hint">Scrolling out of boredom, watching shows you've lost interest in, checking feeds reflexively.</span>
    <select id="a-wasted-time" onchange="handleAssessInput('a-wasted-time')"><option value="">Select...</option><option value="most">Most of it &ndash; I spend more time on habitual consumption than genuine pleasure</option><option value="a-lot">A lot &ndash; roughly half my leisure feels wasted</option><option value="some">Some &ndash; a noticeable but manageable amount</option><option value="a-little">A little &ndash; occasional mindless browsing but mostly intentional</option><option value="almost-none">Almost none &ndash; nearly all my leisure is genuinely chosen</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-wasted-time" onchange="handleSkip('a-wasted-time')"><label for="skip-wasted-time">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-guilt-free">
    <span class="assess-label">Can you enjoy pure entertainment without guilt?</span>
    <span class="assess-hint">Some people struggle to watch a film without feeling they're wasting time.</span>
    <select id="a-guilt-free" onchange="handleAssessInput('a-guilt-free')"><option value="">Select...</option><option value="never">Never &ndash; I always feel I should be doing something productive</option><option value="rarely">Rarely &ndash; guilt creeps in most of the time</option><option value="sometimes">Sometimes &ndash; depends on how busy I am</option><option value="mostly">Mostly &ndash; I can usually relax without guilt</option><option value="always">Always &ndash; I fully embrace leisure time without guilt</option></select>
    <div class="assess-skip"><input type="checkbox" id="skip-guilt-free" onchange="handleSkip('a-guilt-free')"><label for="skip-guilt-free">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-restoration">
        <span class="assess-summary-label">Restoration</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-restoration" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-restoration">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-enrichment">
        <span class="assess-summary-label">Enrichment</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-enrichment" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-enrichment">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on leisure screen time, reading habits, and learning behaviour among adults. Items without reliable population data are not scored.</p>
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

<p>You now understand why consumptive leisure matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about restoration, enrichment, and enjoyment. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/consumptive-leisure/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Consumptive Leisure Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Consumptive Leisure. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/consumptive-leisure/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'consumptive-leisure';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-energy-after', 'a-screen-time', 'a-wind-down',
        'a-learning-proportion', 'a-books-per-year', 'a-retention',
        'a-genuine-pleasure', 'a-wasted-time', 'a-guilt-free'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: average leisure screen time is ~5 hrs/day,
    // ~24% of adults read zero books, most leisure consumption is passive.
    var THRESHOLDS = {
        'a-screen-time': [
            // Average leisure screen time is ~5 hrs/day; under 1 hr is very unusual
            {v:'over-6',p:5},{v:'4-to-6',p:20},{v:'2-to-4',p:50},{v:'1-to-2',p:78},{v:'under-1',p:95}
        ],
        'a-learning-proportion': [
            // Most people's leisure is purely passive; over 60% learning-oriented is very rare
            {v:'almost-none',p:10},{v:'small',p:30},{v:'moderate',p:55},{v:'substantial',p:78},{v:'majority',p:95}
        ],
        'a-books-per-year': [
            // ~24% read zero books; median is ~4; over 15 is top few percent
            {v:'none',p:12},{v:'1-to-3',p:35},{v:'4-to-8',p:58},{v:'9-to-15',p:80},{v:'over-15',p:95}
        ]
    };

    var VALUE_ITEMS = {
        restoration: ['a-screen-time'],
        enrichment: ['a-learning-proportion', 'a-books-per-year']
    };

    // Items without reliable population data for percentile scoring
    var UNSCORED_ITEMS = [
        'a-energy-after', 'a-wind-down',
        'a-retention',
        'a-genuine-pleasure', 'a-wasted-time', 'a-guilt-free'
    ];

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
        for (var i = 0; i < thresholds.length; i++) {
            if (thresholds[i].v === String(value)) return thresholds[i].p;
        }
        return null;
    }

    function getItemPercentile(itemId) {
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
        ['restoration', 'enrichment'].forEach(function(vk) {
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
        ['restoration', 'enrichment'].forEach(function(vk) {
            scores[vk] = computeValuePercentile(vk);
        });
        scores.enjoyment = null;
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
        updatePercentileHint(itemId);
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessSummary();
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
            updatePercentileHint(id);
            updateInputGroupState(id);
        });

        updateAssessSummary();
        updateAssessRecorded();
        updateAssessCompletion();
    }

    document.addEventListener('DOMContentLoaded', function() {
        restoreAssessment();
        updateUI();
    });
})();
</script>
