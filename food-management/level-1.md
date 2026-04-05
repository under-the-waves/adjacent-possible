---
layout: default
title: "Food Management – Level 1: Awareness"
life_area_slug: food-management
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

<h1>Food Management: Level 1</h1>

<p class="l1-subtitle">Understand what food management involves, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Food Management Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why food management matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Getting food on the table is one of the most repetitive and cognitively demanding tasks in daily life. Most adults make it happen every day without thinking of it as a skill &ndash; but the gap between someone who manages food well and someone who doesn't shows up in stress levels, wasted money, and diet quality.</p>

<p>A <a href="https://dentsu-ho.com/en/articles/9478" target="_blank">Dentsu survey</a> found that deciding what to cook is now rated as more burdensome than the actual cooking or cleanup, with the percentage of daily cooks who find cooking troublesome rising from 45.7% to 55.6% between 2022 and 2024. Separately, 77% of people report being too exhausted to cook after work.</p>

<p>The <a href="https://pubmed.ncbi.nlm.nih.gov/24462490/" target="_blank">most cited academic framework for food literacy</a> (Vidgen &amp; Gallegos, 2014) identifies four domains: planning and managing, selecting, preparing, and eating. Higher food literacy is associated with better diet quality, lower food waste, and reduced stress around food provision.</p>

<p>Food management is distinct from nutrition. Nutrition concerns <em>what</em> you eat; food management concerns <em>how you get it</em>. A well-run food system reduces daily decision fatigue, minimises waste, and ensures your nutritional goals are actually achievable in practice.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about food management</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach food management for different reasons. This site scores every food management intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Competence</h3>
<p>Reliably getting good food on the table through whatever combination of methods works for you. Planning, sourcing, preparation skill, food safety, adaptability, and the ability to make do with what's available. People who prioritise this value focus on building a dependable food provision system &ndash; whether that involves cooking from scratch, meal kits, takeaway, or any combination &ndash; that consistently delivers meals meeting their needs.</p>

<h3>Craft</h3>
<p>Satisfaction and creative expression derived from the process of preparing food. Skill development, mastery of techniques, culinary exploration, and the meditative or therapeutic aspects of cooking. Those who prioritise this value treat food preparation as a rewarding activity in its own right, investing in developing skills and finding genuine pleasure in the process.</p>

<h3>Waste Reduction</h3>
<p>Minimising the food that gets thrown away through better management practices. Stock management, use-up routines, storage skills, purchasing discipline, and creative use of leftovers. Those who prioritise this value focus on the operational side of waste prevention &ndash; planning purchases carefully, storing food properly, and building habits that ensure food gets eaten.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each food management value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Competence &ndash; Level 5</div>
    <p><a href="https://www.instagram.com/maboroshikitchen/" target="_blank">Samin Nosrat</a>, author of <em>Salt, Fat, Acid, Heat</em>, learned to cook professionally at Chez Panisse and then spent years teaching home cooks to develop reliable instincts. She appears to plan, shop, and cook with the kind of fluency where improvising a meal from whatever is in the fridge is effortless. Her public cooking demonstrates consistent adaptability across cuisines, seasons, and available ingredients.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Craft &ndash; Level 5</div>
    <p><a href="https://www.binging-with-babish.com/" target="_blank">Andrew Rea</a> (Babish Culinary Universe) taught himself to cook as an adult and has spent over a decade documenting his progression from basic techniques to advanced pastry, fermentation, and multi-day projects. His channel catalogues thousands of hours of deliberate skill development, and he regularly attempts dishes well outside his comfort zone on camera.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Waste Reduction &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Bea_Johnson" target="_blank">Bea Johnson</a> fits her family of four's entire annual non-recyclable waste into a single quart-sized jar. Her food management system &ndash; buying in bulk, composting, planning meals around what needs using up &ndash; is central to how she achieves this. She has maintained the practice since 2008 and documented it in her book <em>Zero Waste Home</em>.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to look up or test.</p>

<div class="assess-group">
<h4>Competence</h4>

<div class="assess-input-group" id="ig-meals-cooked">
    <span class="assess-label">How many meals per week do you prepare at home?</span>
    <span class="assess-hint">Count breakfasts, lunches, and dinners separately. Include meal kits and reheated batch-cooked meals as home-prepared.</span>
    <input type="number" id="a-meals-cooked" min="0" max="21" step="1" placeholder="e.g. 14" onchange="handleAssessInput('a-meals-cooked')"> <span class="assess-percentile-hint" id="pct-meals-cooked"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-meals-cooked" onchange="handleSkip('a-meals-cooked')"><label for="skip-meals-cooked">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-planning-method">
    <span class="assess-label">How often do you plan meals in advance?</span>
    <span class="assess-hint">Weekly plan, daily improvisation, rotating set of staples, or something else entirely.</span>
    <select id="a-planning-method" onchange="handleAssessInput('a-planning-method')">
        <option value="">Select...</option>
        <option value="0">Never &ndash; I decide at the last minute each time</option>
        <option value="1">Occasionally &ndash; I plan a day or two ahead sometimes</option>
        <option value="2">Regularly &ndash; I plan most meals a few days ahead</option>
        <option value="3">Consistently &ndash; I plan the full week in advance</option>
        <option value="4">Systematically &ndash; I plan, batch, and rotate meals on a regular cycle</option>
    </select> <span class="assess-percentile-hint" id="pct-planning-method"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-planning-method" onchange="handleSkip('a-planning-method')"><label for="skip-planning-method">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-fallback">
    <span class="assess-label">What do you do when your usual food plan breaks down?</span>
    <span class="assess-hint">Unexpected guests, empty fridge, no energy to cook. Reliable fallback options might include a go-to takeaway, freezer meals, or a 10-minute storecupboard recipe.</span>
    <select id="a-fallback" onchange="handleAssessInput('a-fallback')">
        <option value="">Select...</option>
        <option value="0">I don't have a fallback &ndash; I skip meals or panic</option>
        <option value="1">I order takeaway or grab something convenient</option>
        <option value="2">I have one or two go-to quick meals I can make</option>
        <option value="3">I have several reliable fallbacks and rarely feel stuck</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-fallback" onchange="handleSkip('a-fallback')"><label for="skip-fallback">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Craft</h4>

<div class="assess-input-group" id="ig-technique-count">
    <span class="assess-label">Roughly how many cooking techniques can you execute confidently?</span>
    <span class="assess-hint">Count only methods you use without needing to look up the basics each time &ndash; e.g. roasting, stir-frying, braising, baking, poaching.</span>
    <select id="a-technique-count" onchange="handleAssessInput('a-technique-count')">
        <option value="">Select...</option>
        <option value="0">None &ndash; I don't really cook</option>
        <option value="1">1 &ndash; 2 techniques</option>
        <option value="2">3 &ndash; 5 techniques</option>
        <option value="3">6 &ndash; 10 techniques</option>
        <option value="4">More than 10 techniques</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-technique-count" onchange="handleSkip('a-technique-count')"><label for="skip-technique-count">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-new-recipes">
    <span class="assess-label">How often do you try a new recipe or technique?</span>
    <span class="assess-hint">This is about frequency, not success rate. Attempting and failing counts.</span>
    <select id="a-new-recipes" onchange="handleAssessInput('a-new-recipes')">
        <option value="">Select...</option>
        <option value="0">Never or almost never</option>
        <option value="1">A few times a year</option>
        <option value="2">Monthly</option>
        <option value="3">Weekly or more</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-new-recipes" onchange="handleSkip('a-new-recipes')"><label for="skip-new-recipes">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-enjoy-cooking">
    <span class="assess-label">How do you feel about the process of cooking?</span>
    <span class="assess-hint">There is no right answer. Knowing your honest reaction helps you choose the right interventions.</span>
    <select id="a-enjoy-cooking" onchange="handleAssessInput('a-enjoy-cooking')">
        <option value="">Select...</option>
        <option value="0">I actively dislike it</option>
        <option value="1">I tolerate it as a necessary chore</option>
        <option value="2">I'm neutral &ndash; it depends on the day</option>
        <option value="3">I generally enjoy it</option>
        <option value="4">I love it &ndash; cooking is a highlight of my day</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-enjoy-cooking" onchange="handleSkip('a-enjoy-cooking')"><label for="skip-enjoy-cooking">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Waste Reduction</h4>

<div class="assess-input-group" id="ig-waste-pct">
    <span class="assess-label">What percentage of the food you buy ends up thrown away?</span>
    <span class="assess-hint">Check your bin over a few days if you're unsure. Include uneaten leftovers, expired items, and spoiled produce. The average UK household wastes roughly 18% of purchased food.</span>
    <select id="a-waste-pct" onchange="handleAssessInput('a-waste-pct')">
        <option value="">Select...</option>
        <option value="0">More than 30%</option>
        <option value="1">20 &ndash; 30%</option>
        <option value="2">10 &ndash; 20% (around average)</option>
        <option value="3">5 &ndash; 10%</option>
        <option value="4">Less than 5%</option>
        <option value="5">Virtually nothing &ndash; I waste almost no food</option>
    </select> <span class="assess-percentile-hint" id="pct-waste-pct"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-waste-pct" onchange="handleSkip('a-waste-pct')"><label for="skip-waste-pct">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-fridge-audit">
    <span class="assess-label">Do you know what is currently in the back of your fridge?</span>
    <span class="assess-hint">Open the fridge and check now if you're not sure. This is a useful baseline.</span>
    <select id="a-fridge-audit" onchange="handleAssessInput('a-fridge-audit')">
        <option value="">Select...</option>
        <option value="0">No idea &ndash; there are probably items I've forgotten about</option>
        <option value="1">Rough idea, but I'd find some surprises</option>
        <option value="2">I know what's there but not always the dates</option>
        <option value="3">I know exactly what's in there and when it needs using</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-fridge-audit" onchange="handleSkip('a-fridge-audit')"><label for="skip-fridge-audit">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-leftover-plan">
    <span class="assess-label">What do you typically do with leftovers?</span>
    <span class="assess-hint">Think about the last three times you had food left over after a meal.</span>
    <select id="a-leftover-plan" onchange="handleAssessInput('a-leftover-plan')">
        <option value="">Select...</option>
        <option value="0">They usually get thrown away</option>
        <option value="1">I keep them but often forget to eat them</option>
        <option value="2">I eat them within a day or two</option>
        <option value="3">I plan around them &ndash; freezing, repurposing, or eating them reliably</option>
    </select> <span class="assess-percentile-hint" id="pct-leftover-plan"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-leftover-plan" onchange="handleSkip('a-leftover-plan')"><label for="skip-leftover-plan">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-competence">
        <span class="assess-summary-label">Competence</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-competence" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-competence">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-waste_reduction">
        <span class="assess-summary-label">Waste Reduction</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-waste_reduction" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-waste_reduction">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published household food surveys. Craft items are recorded for your awareness but not scored, as the available data does not support reliable percentile estimates.</p>
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

<p>You now understand why food management matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about competence, craft, and waste reduction. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/food-management/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Food Management Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Food Management. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/food-management/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'food-management';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-meals-cooked', 'a-planning-method', 'a-fallback',
        'a-technique-count', 'a-new-recipes', 'a-enjoy-cooking',
        'a-waste-pct', 'a-fridge-audit', 'a-leftover-plan'
    ];

    // Scoring thresholds: [{value, percentile}, ...] sorted by value ascending
    // Sources: USDA ERS data on home cooking frequency, WRAP household food waste surveys
    var THRESHOLDS = {
        'a-meals-cooked': [
            {v:0,p:5},{v:3,p:15},{v:7,p:30},{v:10,p:50},{v:14,p:70},{v:17,p:85},{v:21,p:95}
        ],
        'a-planning-method': [
            {v:'0',p:15},{v:'1',p:35},{v:'2',p:55},{v:'3',p:75},{v:'4',p:92}
        ],
        'a-waste-pct': [
            {v:'0',p:10},{v:'1',p:25},{v:'2',p:50},{v:'3',p:72},{v:'4',p:88},{v:'5',p:96}
        ],
        'a-leftover-plan': [
            {v:'0',p:15},{v:'1',p:35},{v:'2',p:60},{v:'3',p:85}
        ]
    };

    var VALUE_ITEMS = {
        competence: ['a-meals-cooked', 'a-planning-method'],
        waste_reduction: ['a-waste-pct', 'a-leftover-plan']
    };

    // These items are recorded but not scored (insufficient population data for percentiles)
    var UNSCORED_ITEMS = ['a-fallback', 'a-technique-count', 'a-new-recipes', 'a-enjoy-cooking', 'a-fridge-audit'];

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
        ['competence', 'waste_reduction'].forEach(function(vk) {
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
        ['competence', 'waste_reduction'].forEach(function(vk) {
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
