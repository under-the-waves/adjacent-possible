---
layout: default
title: "Housework – Level 1: Awareness"
life_area_slug: housework
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

<h1>Housework: Level 1</h1>

<p class="l1-subtitle">Understand what housework means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Housework Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why housework matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your home environment shapes your health, stress levels, and cognitive performance more than most people realise. The evidence runs deeper than tidiness preferences.</p>

<p>Physical clutter competes for your attention and degrades your ability to focus and process information, according to research from the <a href="https://doi.org/10.1523/JNEUROSCI.5587-09.2011" target="_blank">Princeton Neuroscience Institute</a>. A <a href="https://pubmed.ncbi.nlm.nih.gov/19934011/" target="_blank">UCLA study</a> of 32 dual-income families found that those who described their homes as cluttered had flatter cortisol slopes throughout the day &ndash; a physiological marker of chronic stress.</p>

<p>On the health side, an <a href="https://news.iu.edu/stories/2015/08/iub/releases/24-housework-physical-activity.html" target="_blank">Indiana University study</a> found that house cleanliness was a stronger predictor of physical health than neighbourhood walkability. Indoor air quality, mould, and allergen exposure have measurable effects on respiratory health and sleep quality.</p>

<p>Research published in <a href="https://doi.org/10.1073/pnas.1706541114" target="_blank">PNAS</a> found that spending money to buy back time &ndash; including outsourcing household tasks &ndash; produced greater life satisfaction than spending on material goods, regardless of income level. How you manage your home is one of the most underrated levers for daily quality of life.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about housework</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People care about housework for different reasons. This site scores every housework intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Health & Hygiene</h3>
<p>Housework that protects physical health by reducing illness, allergens, pests, mould, and toxins. Cleaning protocols, air quality management, and maintenance practices that eliminate health hazards. People who lean towards this value focus on evidence-based cleaning frequencies and methods that have the greatest impact on health outcomes.</p>

<h3>Order</h3>
<p>The mental calm and cognitive ease that comes from an organised, uncluttered living space. Knowing where everything is, having systems that maintain themselves, and not feeling overwhelmed by mess. People who lean towards this value focus on organisational systems, decluttering, and routines that keep the home orderly without constant effort.</p>

<h3>Aesthetics</h3>
<p>The visual appeal and sensory pleasure derived from your living space. Design choices, visual harmony, and personalised spaces that reflect your taste and feel inviting. People who lean towards this value focus on creating environments that are pleasing to be in, not just tidy or functional.</p>

<h3>Environmental Impact</h3>
<p>The ecological footprint of home management practices. Sustainable cleaning methods, waste reduction, and considerate resource use. People who lean towards this value focus on eco-friendly products, minimal consumption, and practices that reduce environmental harm.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each housework value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Health & Hygiene &ndash; Level 5</div>
    <p><a href="https://www.youtube.com/@CleanMySpace" target="_blank">Melissa Maker</a> runs a cleaning company and has spent over a decade documenting evidence-based cleaning methods across hundreds of videos and a bestselling book. She appears to maintain clinical-grade hygiene standards in her own home, with systematic protocols for air quality, surface sanitisation, and allergen management that go well beyond standard domestic cleaning.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Order &ndash; Level 5</div>
    <p><a href="https://konmari.com/" target="_blank">Marie Kondo</a> developed the KonMari method and has reportedly maintained a highly organised living environment since childhood. Her approach &ndash; keeping only items that serve a purpose or bring satisfaction, with every object having a designated place &ndash; seems to produce homes that stay orderly with minimal ongoing effort. Clients who complete her full process report sustained results years later.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Aesthetics &ndash; Level 5</div>
    <p><a href="https://www.instagram.com/mikiashdesign/" target="_blank">Mike Mikish</a> is known for transforming everyday living spaces into multi-sensory environments with cohesive colour palettes, layered lighting, and curated objects. His own home appears to function as a gallery-quality space where every material, finish, and decorative element is chosen with intention &ndash; the kind of residential environment that could feature in a design publication.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Environmental Impact &ndash; Level 5</div>
    <p><a href="https://www.goingzerowaste.com/" target="_blank">Kathryn Kellogg</a> reportedly fits two years of landfill waste into a single jar while maintaining a clean, functional home. She uses exclusively non-toxic, biodegradable cleaning products &ndash; many homemade &ndash; and has eliminated single-use items from her household. Her approach demonstrates that near-zero-waste home management is achievable without sacrificing cleanliness or comfort.</p>
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
<h4>Health &amp; Hygiene</h4>

<div class="assess-input-group" id="ig-clean-freq">
    <span class="assess-label">How often do you clean your kitchen and bathroom surfaces?</span>
    <span class="assess-hint">Countertops, sinks, taps, toilet, and shower or bath.</span>
    <select id="a-clean-freq" onchange="handleAssessInput('a-clean-freq')">
        <option value="">Select...</option>
        <option value="rarely">Rarely &ndash; only when visibly dirty</option>
        <option value="monthly">Monthly or so</option>
        <option value="fortnightly">Fortnightly</option>
        <option value="weekly">Weekly</option>
        <option value="multiple">Multiple times a week or daily</option>
    </select> <span class="assess-percentile-hint" id="pct-clean-freq"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-clean-freq" onchange="handleSkip('a-clean-freq')"><label for="skip-clean-freq">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-fridge-temp">
    <span class="assess-label">Is your fridge at or below 5&deg;C?</span>
    <span class="assess-hint">Check the built-in display, or place a thermometer inside for a few hours.</span>
    <select id="a-fridge-temp" onchange="handleAssessInput('a-fridge-temp')">
        <option value="">Select...</option>
        <option value="dont-know">I don't know</option>
        <option value="probably-not">Probably not &ndash; I've never checked</option>
        <option value="think-so">I think so but I'm not certain</option>
        <option value="yes-checked">Yes &ndash; I've checked and it's correct</option>
        <option value="monitored">Yes &ndash; I monitor it regularly</option>
    </select> <span class="assess-percentile-hint" id="pct-fridge-temp"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-fridge-temp" onchange="handleSkip('a-fridge-temp')"><label for="skip-fridge-temp">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-mould">
    <span class="assess-label">Do you have any visible mould, damp, or persistent condensation in your home?</span>
    <span class="assess-hint">Check bathroom grout, window seals, behind furniture on external walls, and under sinks.</span>
    <select id="a-mould" onchange="handleAssessInput('a-mould')">
        <option value="">Select...</option>
        <option value="significant">Significant &ndash; visible mould in multiple areas</option>
        <option value="some">Some &ndash; one or two problem areas</option>
        <option value="minor">Minor &ndash; occasional condensation but no mould</option>
        <option value="none">None &ndash; I've checked and it's clear</option>
        <option value="prevented">Prevented &ndash; I take active steps to manage moisture and ventilation</option>
    </select> <span class="assess-percentile-hint" id="pct-mould"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-mould" onchange="handleSkip('a-mould')"><label for="skip-mould">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Order</h4>

<div class="assess-input-group" id="ig-clutter">
    <span class="assess-label">How would you describe the clutter level in your home?</span>
    <span class="assess-hint">Walk through each room and note surfaces, floors, and storage areas.</span>
    <select id="a-clutter" onchange="handleAssessInput('a-clutter')">
        <option value="">Select...</option>
        <option value="overwhelming">Overwhelming &ndash; clutter in most rooms</option>
        <option value="significant">Significant &ndash; several problem areas</option>
        <option value="moderate">Moderate &ndash; a few cluttered spots but mostly manageable</option>
        <option value="minimal">Minimal &ndash; surfaces are mostly clear</option>
        <option value="none">None &ndash; everything has a place and is in it</option>
    </select> <span class="assess-percentile-hint" id="pct-clutter"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-clutter" onchange="handleSkip('a-clutter')"><label for="skip-clutter">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-find-items">
    <span class="assess-label">How quickly can you find commonly needed items?</span>
    <span class="assess-hint">Keys, scissors, chargers, documents &ndash; do you regularly spend time searching?</span>
    <select id="a-find-items" onchange="handleAssessInput('a-find-items')">
        <option value="">Select...</option>
        <option value="frequent-search">Frequent searching &ndash; I lose things regularly</option>
        <option value="sometimes">Sometimes &ndash; I search for things a few times a week</option>
        <option value="usually-fine">Usually fine &ndash; I can find most things fairly quickly</option>
        <option value="rarely-search">Rarely search &ndash; nearly everything has a place</option>
        <option value="instantly">Instantly &ndash; I know exactly where everything is</option>
    </select> <span class="assess-percentile-hint" id="pct-find-items"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-find-items" onchange="handleSkip('a-find-items')"><label for="skip-find-items">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-tidy-routine">
    <span class="assess-label">Do you have a regular tidying routine or schedule?</span>
    <span class="assess-hint">Specific tasks on specific days vs cleaning when things get messy.</span>
    <select id="a-tidy-routine" onchange="handleAssessInput('a-tidy-routine')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I clean only when it gets bad</option>
        <option value="reactive">Reactive &ndash; I clean when I notice mess</option>
        <option value="loose">Loose routine &ndash; I have some regular habits but nothing fixed</option>
        <option value="weekly">Weekly schedule &ndash; specific tasks on specific days</option>
        <option value="daily">Daily routine &ndash; regular tidying is built into my day</option>
    </select> <span class="assess-percentile-hint" id="pct-tidy-routine"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-tidy-routine" onchange="handleSkip('a-tidy-routine')"><label for="skip-tidy-routine">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Aesthetics</h4>

<div class="assess-input-group" id="ig-visual-appeal">
    <span class="assess-label">How do you feel about the visual appearance of your living spaces?</span>
    <span class="assess-hint">Do furnishings reflect your taste or are they inherited defaults?</span>
    <select id="a-visual-appeal" onchange="handleAssessInput('a-visual-appeal')">
        <option value="">Select...</option>
        <option value="neglected">Neglected &ndash; most rooms feel uninviting</option>
        <option value="mixed">Mixed &ndash; some rooms are fine, others I avoid</option>
        <option value="acceptable">Acceptable &ndash; it's fine but doesn't reflect my taste</option>
        <option value="pleasant">Pleasant &ndash; most rooms look the way I want them to</option>
        <option value="curated">Curated &ndash; I've deliberately designed my spaces to suit me</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-visual-appeal" onchange="handleSkip('a-visual-appeal')"><label for="skip-visual-appeal">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-lighting">
    <span class="assess-label">Does the lighting in your main living spaces suit their function?</span>
    <span class="assess-hint">Bright enough for tasks? Warm enough for relaxation?</span>
    <select id="a-lighting" onchange="handleAssessInput('a-lighting')">
        <option value="">Select...</option>
        <option value="poor">Poor &ndash; too bright, too dim, or wrong colour temperature</option>
        <option value="default">Default &ndash; whatever was already there</option>
        <option value="partly">Partly &ndash; some rooms are well-lit, others aren't</option>
        <option value="good">Good &ndash; I've chosen lighting that works for each room</option>
        <option value="excellent">Excellent &ndash; I have layered lighting suited to different uses</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-lighting" onchange="handleSkip('a-lighting')"><label for="skip-lighting">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-sensory">
    <span class="assess-label">How does your home smell, sound, and feel when you walk in?</span>
    <span class="assess-hint">Think about what a visitor would notice.</span>
    <select id="a-sensory" onchange="handleAssessInput('a-sensory')">
        <option value="">Select...</option>
        <option value="unpleasant">Unpleasant &ndash; there are smells, noise, or discomfort I've got used to</option>
        <option value="neutral">Neutral &ndash; nothing noticeable either way</option>
        <option value="mostly-pleasant">Mostly pleasant &ndash; no problems, but I haven't given it thought</option>
        <option value="inviting">Inviting &ndash; I've addressed the main sensory elements</option>
        <option value="considered">Considered &ndash; I've deliberately shaped the sensory experience</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-sensory" onchange="handleSkip('a-sensory')"><label for="skip-sensory">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Environmental Impact</h4>

<div class="assess-input-group" id="ig-waste">
    <span class="assess-label">How much household waste do you generate per week?</span>
    <span class="assess-hint">Count your bin bags or check how often your bins are full.</span>
    <select id="a-waste" onchange="handleAssessInput('a-waste')">
        <option value="">Select...</option>
        <option value="dont-know">I don't know</option>
        <option value="high">High &ndash; multiple full bags with minimal recycling</option>
        <option value="average">Average &ndash; typical amount with some recycling</option>
        <option value="low">Low &ndash; I recycle most things and generate little waste</option>
        <option value="minimal">Minimal &ndash; I actively minimise waste and compost</option>
    </select> <span class="assess-percentile-hint" id="pct-waste"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-waste" onchange="handleSkip('a-waste')"><label for="skip-waste">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-products">
    <span class="assess-label">Are any of your cleaning products eco-friendly or plant-based?</span>
    <span class="assess-hint">Check labels for biodegradable, plant-based, or eco-certified claims.</span>
    <select id="a-products" onchange="handleAssessInput('a-products')">
        <option value="">Select...</option>
        <option value="dont-know">I don't know &ndash; I've never checked</option>
        <option value="none">None &ndash; I use conventional products</option>
        <option value="a-few">A few &ndash; I've switched one or two</option>
        <option value="mostly">Mostly &ndash; the majority are eco-friendly</option>
        <option value="all">All &ndash; I use exclusively eco-friendly products</option>
    </select> <span class="assess-percentile-hint" id="pct-products"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-products" onchange="handleSkip('a-products')"><label for="skip-products">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-wash-temp">
    <span class="assess-label">What temperature do you typically wash your clothes at?</span>
    <span class="assess-hint">90% of the energy used in washing goes to heating water.</span>
    <select id="a-wash-temp" onchange="handleAssessInput('a-wash-temp')">
        <option value="">Select...</option>
        <option value="dont-know">I don't know</option>
        <option value="hot">Hot &ndash; 60&deg;C or above for most loads</option>
        <option value="warm">Warm &ndash; 40&deg;C for most loads</option>
        <option value="cool">Cool &ndash; 30&deg;C for most loads</option>
        <option value="cold">Cold &ndash; 20&deg;C or below for most loads</option>
    </select> <span class="assess-percentile-hint" id="pct-wash-temp"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-wash-temp" onchange="handleSkip('a-wash-temp')"><label for="skip-wash-temp">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-health">
        <span class="assess-summary-label">Health &amp; Hygiene</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-health" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-health">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-order">
        <span class="assess-summary-label">Order</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-order" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-order">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-environmental">
        <span class="assess-summary-label">Environmental Impact</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-environmental" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-environmental">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on household practices among adults. Aesthetics items are recorded for your awareness but not scored, as the available data does not support reliable percentile estimates.</p>
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

<p>You now understand why housework matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about health and hygiene, order, aesthetics, and environmental impact. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/housework/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Housework Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Housework. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/housework/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'housework';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-clean-freq', 'a-fridge-temp', 'a-mould',
        'a-clutter', 'a-find-items', 'a-tidy-routine',
        'a-visual-appeal', 'a-lighting', 'a-sensory',
        'a-waste', 'a-products', 'a-wash-temp'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: ~30% clean weekly, ~60% never check fridge temp,
    // ~25% have visible mould, ~54% feel overwhelmed by clutter.
    var THRESHOLDS = {
        'a-clean-freq': [
            // ~20% clean rarely, ~30% weekly, <10% daily
            {v:'rarely',p:10},{v:'monthly',p:25},{v:'fortnightly',p:45},{v:'weekly',p:65},{v:'multiple',p:90}
        ],
        'a-fridge-temp': [
            // ~60% have never checked; regularly monitoring is very rare
            {v:'dont-know',p:10},{v:'probably-not',p:25},{v:'think-so',p:50},{v:'yes-checked',p:75},{v:'monitored',p:95}
        ],
        'a-mould': [
            // ~25% of UK homes have visible mould; active prevention is uncommon
            {v:'significant',p:10},{v:'some',p:30},{v:'minor',p:55},{v:'none',p:75},{v:'prevented',p:95}
        ],
        'a-clutter': [
            // ~54% report feeling overwhelmed by clutter; fully organised is rare
            {v:'overwhelming',p:10},{v:'significant',p:25},{v:'moderate',p:50},{v:'minimal',p:75},{v:'none',p:95}
        ],
        'a-find-items': [
            // Average person spends 8.5 min/day searching; instant retrieval is very rare
            {v:'frequent-search',p:10},{v:'sometimes',p:30},{v:'usually-fine',p:55},{v:'rarely-search',p:78},{v:'instantly',p:95}
        ],
        'a-tidy-routine': [
            // ~70% have no cleaning schedule; daily built-in routines are rare
            {v:'none',p:10},{v:'reactive',p:30},{v:'loose',p:50},{v:'weekly',p:75},{v:'daily',p:93}
        ],
        'a-waste': [
            // ~45% recycle regularly; active waste minimisation with composting is rare
            {v:'dont-know',p:10},{v:'high',p:20},{v:'average',p:45},{v:'low',p:72},{v:'minimal',p:93}
        ],
        'a-products': [
            // ~20% use any eco-friendly cleaning products; all-eco is very rare
            {v:'dont-know',p:10},{v:'none',p:25},{v:'a-few',p:50},{v:'mostly',p:78},{v:'all',p:95}
        ],
        'a-wash-temp': [
            // ~60% wash at 40C; cold washing is uncommon
            {v:'dont-know',p:15},{v:'hot',p:20},{v:'warm',p:45},{v:'cool',p:72},{v:'cold',p:93}
        ]
    };

    var VALUE_ITEMS = {
        health: ['a-clean-freq', 'a-fridge-temp', 'a-mould'],
        order: ['a-clutter', 'a-find-items', 'a-tidy-routine'],
        environmental: ['a-waste', 'a-products', 'a-wash-temp']
    };

    // Aesthetics items are recorded but not scored (insufficient population data)
    var UNSCORED_ITEMS = ['a-visual-appeal', 'a-lighting', 'a-sensory'];

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

    function ordinalSuffix(n) {
        var s = ['th','st','nd','rd'];
        var v = n % 100;
        return n + (s[(v-20)%10] || s[v] || s[0]);
    }
    function interpolatePercentile(value, thresholds) {
        // All housework items use string keys (dropdowns)
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
        hintEl.textContent = pct !== null ? '~' + ordinalSuffix(pct) + ' percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['health', 'order', 'environmental'].forEach(function(vk) {
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
        ['health', 'order', 'environmental'].forEach(function(vk) {
            scores[vk] = computeValuePercentile(vk);
        });
        scores.aesthetics = null; // unscored
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

    document.addEventListener('DOMContentLoaded', function() { restoreAssessment(); updateUI(); });
})();
</script>
