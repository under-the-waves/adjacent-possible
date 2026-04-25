---
layout: default
title: "Nutrition – Level 1: Awareness"
life_area_slug: nutrition
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

<h1>Nutrition: Level 1</h1>

<p class="l1-subtitle">Understand what nutrition means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Nutrition Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why nutrition matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>What you eat affects nearly every system in your body. The <a href="https://doi.org/10.1016/S0140-6736(19)30041-8" target="_blank">Global Burden of Disease study</a> found that dietary risks are the leading risk factor for death worldwide &ndash; responsible for roughly 11 million deaths per year, more than tobacco or high blood pressure.</p>

<p>The biggest dietary risks are not exotic deficiencies. They are low intake of whole grains, fruit, and vegetables, combined with high intake of sodium and processed meat. The average American scores just 59 out of 100 on the <a href="https://www.fns.usda.gov/cnpp/healthy-eating-index-hei" target="_blank">Healthy Eating Index</a>, and only about <a href="https://www.cdc.gov/mmwr/volumes/71/wr/mm7101a1.htm" target="_blank">10 &ndash; 12% of adults</a> meet basic fruit and vegetable recommendations.</p>

<p>Diet also shapes how you feel day to day. Higher diet quality is consistently associated with <a href="https://doi.org/10.1017/S0033291718002896" target="_blank">lower rates of depression</a>, and a randomised trial found that young adults who increased their fruit and vegetable intake for two weeks reported improvements in motivation and vitality. Beyond personal health, the food system accounts for roughly <a href="https://doi.org/10.1126/science.aaq0216" target="_blank">26% of global greenhouse gas emissions</a>, making what you eat one of the most significant daily environmental choices you make.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about nutrition</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People care about food for different reasons. This site scores every nutrition intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Health & Longevity</h3>
<p>Diet quality that supports bodily health and function &ndash; nutrient adequacy, disease prevention, energy provision, digestive health, and metabolic balance. People who lean towards this value focus on food choices that deliver optimal nutrition for immediate function and long-term health, with particular attention to nutrient density and physiological effects.</p>

<h3>Enjoyment & Culture</h3>
<p>The sensory pleasure and social dimensions of eating &ndash; taste satisfaction, dietary variety, cultural food traditions, and the role of meals in relationships and community. People who lean towards this value emphasise building a diet they genuinely enjoy, maintaining food traditions that connect them to others, and treating meals as experiences.</p>

<h3>Ethical & Environmental Impact</h3>
<p>The broader consequences of dietary choices on the planet and other beings &ndash; sustainability, carbon footprint, animal welfare, biodiversity, and fair labour practices. People who lean towards this value focus on what they choose to eat and where it comes from, favouring diets with lower environmental impact and greater alignment with their moral commitments.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each nutrition value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Health & Longevity &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Bryan_Johnson_(entrepreneur)" target="_blank">Bryan Johnson</a> eats a precisely measured, plant-heavy diet of around 1,950 calories per day as part of his Blueprint protocol. Every meal is designed around specific nutrient targets and tracked against regular blood panels, organ scans, and dozens of biomarkers. His biological age markers appear to have reversed measurably since he started in 2021. Whether or not the overall programme is replicable, his dietary discipline and the level of evidence-based optimisation behind it seem to be genuinely in the top fraction of the population.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Enjoyment & Culture &ndash; Level 5</div>
    <p><a href="https://ottolenghi.co.uk/pages/about" target="_blank">Yotam Ottolenghi</a> seems to maintain an extraordinarily diverse and joyful relationship with food. He draws on Middle Eastern, Mediterranean, and Asian culinary traditions, regularly develops original recipes, and has built a visible community around shared meals and cultural exchange through food. His cooking repertoire spans hundreds of dishes across many cuisines, and his public work centres on the pleasure and connection that food creates.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Ethical & Environmental Impact &ndash; Level 5</div>
    <p><a href="https://www.riverford.co.uk/ethics-and-environment" target="_blank">Guy Singh-Watson</a>, founder of Riverford Organic Farmers, by all accounts eats a diet closely tied to what his farm produces seasonally. He grows organic produce, runs a veg box scheme with minimal packaging and food waste, pays workers above industry standard, and has structured his business as an employee-owned trust. His dietary footprint is unusually low because most of what he eats is local, seasonal, and organically grown.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to look up or test.</p>

<div class="assess-group">
<h4>Health &amp; Longevity</h4>

<div class="assess-input-group" id="ig-fruit-veg">
    <span class="assess-label">How many servings of fruit and vegetables do you eat on a typical day?</span>
    <span class="assess-hint">Count each distinct portion &ndash; a handful of berries, a side salad, roasted vegetables with dinner.</span>
    <input type="number" id="a-fruit-veg" min="0" max="20" step="1" placeholder="e.g. 4" onchange="handleAssessInput('a-fruit-veg')"> <span class="assess-percentile-hint" id="pct-fruit-veg"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-fruit-veg" onchange="handleSkip('a-fruit-veg')"><label for="skip-fruit-veg">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-upf">
    <span class="assess-label">What proportion of your diet comes from ultra-processed foods?</span>
    <span class="assess-hint">Things like crisps, ready meals, sugary cereals, packaged snacks, and soft drinks.</span>
    <select id="a-upf" onchange="handleAssessInput('a-upf')">
        <option value="">Select...</option>
        <option value="75">Most of it (75%+)</option>
        <option value="55">About half (50 &ndash; 74%)</option>
        <option value="35">A fair amount (25 &ndash; 49%)</option>
        <option value="15">A small amount (10 &ndash; 24%)</option>
        <option value="5">Very little (&lt;10%)</option>
    </select> <span class="assess-percentile-hint" id="pct-upf"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-upf" onchange="handleSkip('a-upf')"><label for="skip-upf">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-fibre">
    <span class="assess-label">How many grams of fibre do you eat per day?</span>
    <span class="assess-hint">Track a typical day using a free app like MyFitnessPal, or estimate from your usual foods. The UK recommendation is 30 g.</span>
    <input type="number" id="a-fibre" min="0" max="80" step="1" placeholder="e.g. 18" onchange="handleAssessInput('a-fibre')"> <span class="assess-percentile-hint" id="pct-fibre"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-fibre" onchange="handleSkip('a-fibre')"><label for="skip-fibre">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Enjoyment &amp; Culture</h4>

<div class="assess-input-group" id="ig-distinct-foods">
    <span class="assess-label">How many distinct foods do you eat in a typical week?</span>
    <span class="assess-hint">Count individual ingredients &ndash; rice, chicken, broccoli, olive oil each count separately.</span>
    <input type="number" id="a-distinct-foods" min="0" max="100" step="1" placeholder="e.g. 15" onchange="handleAssessInput('a-distinct-foods')"> <span class="assess-percentile-hint" id="pct-distinct-foods"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-distinct-foods" onchange="handleSkip('a-distinct-foods')"><label for="skip-distinct-foods">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-cooking">
    <span class="assess-label">How many times per week do you cook a meal from scratch?</span>
    <span class="assess-hint">From scratch means assembling raw or minimally processed ingredients, not reheating.</span>
    <input type="number" id="a-cooking" min="0" max="21" step="1" placeholder="e.g. 4" onchange="handleAssessInput('a-cooking')"> <span class="assess-percentile-hint" id="pct-cooking"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-cooking" onchange="handleSkip('a-cooking')"><label for="skip-cooking">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-social-meals">
    <span class="assess-label">How many meals per week do you share with other people?</span>
    <span class="assess-hint">Eating together at the same table, whether at home, at a restaurant, or at someone else's house.</span>
    <input type="number" id="a-social-meals" min="0" max="21" step="1" placeholder="e.g. 5" onchange="handleAssessInput('a-social-meals')"> <span class="assess-percentile-hint" id="pct-social-meals"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-social-meals" onchange="handleSkip('a-social-meals')"><label for="skip-social-meals">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Ethical &amp; Environmental Impact</h4>

<div class="assess-input-group" id="ig-meat-frequency">
    <span class="assess-label">How many days per week do you eat meat or fish?</span>
    <span class="assess-hint">Count any day where you eat at least one serving of meat, poultry, or fish.</span>
    <select id="a-meat-frequency" onchange="handleAssessInput('a-meat-frequency')">
        <option value="">Select...</option>
        <option value="7">Every day</option>
        <option value="6">6 days</option>
        <option value="5">5 days</option>
        <option value="4">4 days</option>
        <option value="3">3 days</option>
        <option value="2">2 days</option>
        <option value="1">1 day</option>
        <option value="0">None &ndash; fully plant-based</option>
    </select> <span class="assess-percentile-hint" id="pct-meat-frequency"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-meat-frequency" onchange="handleSkip('a-meat-frequency')"><label for="skip-meat-frequency">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-food-waste">
    <span class="assess-label">How much of the food you buy goes to waste?</span>
    <span class="assess-hint">Check your bin over a few days. Include leftovers, expired items, and uneaten portions.</span>
    <select id="a-food-waste" onchange="handleAssessInput('a-food-waste')">
        <option value="">Select...</option>
        <option value="30">A lot (30%+)</option>
        <option value="20">A fair amount (15 &ndash; 30%)</option>
        <option value="12">Some (10 &ndash; 15%)</option>
        <option value="7">A little (5 &ndash; 10%)</option>
        <option value="2">Almost none (&lt;5%)</option>
    </select> <span class="assess-percentile-hint" id="pct-food-waste"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-food-waste" onchange="handleSkip('a-food-waste')"><label for="skip-food-waste">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-sourcing">
    <span class="assess-label">Where does most of your food come from?</span>
    <span class="assess-hint">Think about your main weekly shop and any other regular food purchases.</span>
    <select id="a-sourcing" onchange="handleAssessInput('a-sourcing')">
        <option value="">Select...</option>
        <option value="0">Mostly takeaway, delivery, or ready meals</option>
        <option value="1">Mostly supermarket, little attention to sourcing</option>
        <option value="2">Supermarket with some attention to sourcing (e.g. free-range, organic)</option>
        <option value="3">Mix of supermarket and local shops, markets, or veg boxes</option>
        <option value="4">Mostly local, seasonal, or direct-from-producer sources</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-sourcing" onchange="handleSkip('a-sourcing')"><label for="skip-sourcing">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-health">
        <span class="assess-summary-label">Health &amp; Longevity</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-health" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-health">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-ethical">
        <span class="assess-summary-label">Ethical &amp; Environmental</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-ethical" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-ethical">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data for UK and US adults. Enjoyment &amp; Culture items are recorded for your awareness but not scored, as the available data does not support reliable percentile estimates.</p>
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

<p>You now understand why nutrition matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about health and longevity, enjoyment and culture, and ethical and environmental impact. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/nutrition/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Nutrition Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Nutrition. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/nutrition/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'nutrition';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-fruit-veg', 'a-upf', 'a-fibre',
        'a-distinct-foods', 'a-cooking', 'a-social-meals',
        'a-meat-frequency', 'a-food-waste', 'a-sourcing'
    ];

    // Scoring thresholds: [{value, percentile}, ...] sorted by value ascending
    // For inverted scales (lower = better), thresholds are sorted by value descending
    var THRESHOLDS = {
        'a-fruit-veg': [
            {v:0,p:5},{v:1,p:15},{v:2,p:30},{v:3,p:50},{v:5,p:70},{v:7,p:88},{v:10,p:97}
        ],
        'a-upf': [ // inverted: lower UPF is better
            {v:'75',p:10},{v:'55',p:30},{v:'35',p:55},{v:'15',p:80},{v:'5',p:95}
        ],
        'a-fibre': [
            {v:5,p:5},{v:10,p:15},{v:15,p:30},{v:19,p:50},{v:25,p:70},{v:30,p:88},{v:35,p:95},{v:40,p:99}
        ],
        'a-meat-frequency': [ // inverted: fewer days = higher ethical percentile
            {v:'7',p:10},{v:'6',p:20},{v:'5',p:30},{v:'4',p:45},{v:'3',p:60},{v:'2',p:75},{v:'1',p:88},{v:'0',p:97}
        ],
        'a-food-waste': [ // inverted: less waste = higher percentile
            {v:'30',p:10},{v:'20',p:30},{v:'12',p:50},{v:'7',p:75},{v:'2',p:95}
        ]
    };

    var VALUE_ITEMS = {
        health: ['a-fruit-veg', 'a-upf', 'a-fibre'],
        ethical: ['a-meat-frequency', 'a-food-waste']
    };

    // Enjoyment items plus sourcing are recorded but not scored (insufficient population data for reliable percentiles)
    var UNSCORED_ITEMS = ['a-distinct-foods', 'a-cooking', 'a-social-meals', 'a-sourcing'];

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

    function ordinalSuffix(n) {
        var s = ['th','st','nd','rd'];
        var v = n % 100;
        return n + (s[(v-20)%10] || s[v] || s[0]);
    }
    function interpolatePercentile(value, thresholds) {
        var num = parseFloat(value);
        // Check if thresholds use string keys (dropdowns)
        if (typeof thresholds[0].v === 'string') {
            for (var i = 0; i < thresholds.length; i++) {
                if (thresholds[i].v === String(value)) return thresholds[i].p;
            }
            return null;
        }
        // Check if inverted (first threshold has higher value than last)
        var inverted = thresholds[0].v > thresholds[thresholds.length - 1].v;
        if (inverted) {
            if (num >= thresholds[0].v) return thresholds[0].p;
            if (num <= thresholds[thresholds.length - 1].v) return thresholds[thresholds.length - 1].p;
            for (var i = 0; i < thresholds.length - 1; i++) {
                if (num <= thresholds[i].v && num >= thresholds[i + 1].v) {
                    var t = (thresholds[i].v - num) / (thresholds[i].v - thresholds[i + 1].v);
                    return Math.round(thresholds[i].p + t * (thresholds[i + 1].p - thresholds[i].p));
                }
            }
        } else {
            if (num <= thresholds[0].v) return thresholds[0].p;
            if (num >= thresholds[thresholds.length - 1].v) return thresholds[thresholds.length - 1].p;
            for (var i = 0; i < thresholds.length - 1; i++) {
                if (num >= thresholds[i].v && num <= thresholds[i + 1].v) {
                    var t = (num - thresholds[i].v) / (thresholds[i + 1].v - thresholds[i].v);
                    return Math.round(thresholds[i].p + t * (thresholds[i + 1].p - thresholds[i].p));
                }
            }
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
        hintEl.textContent = pct !== null ? 'roughly ' + ordinalSuffix(Math.round(pct / 10) * 10) + ' percentile' : '';
    }

    function updateInputGroupState(itemId) {
        var group = document.getElementById('ig-' + itemId.replace('a-', ''));
        if (group) group.classList.toggle('answered', isItemAnswered(itemId));
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['health', 'ethical'].forEach(function(vk) {
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
        ['health', 'ethical'].forEach(function(vk) {
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
