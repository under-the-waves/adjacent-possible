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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to look up or test. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've found it out).</p>

<div class="assess-group">
<h4>Health & Longevity</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-fruit-veg">
    <label for="a-fruit-veg">I know roughly how many servings of fruit and vegetables I eat on a typical day.<br><span class="assess-hint">Count each distinct portion &ndash; a handful of berries, a side salad, roasted vegetables with dinner.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-upf">
    <label for="a-upf">I know roughly what proportion of my diet comes from ultra-processed foods.<br><span class="assess-hint">Things like crisps, ready meals, sugary cereals, packaged snacks, and soft drinks.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-fibre">
    <label for="a-fibre">I know whether I am likely meeting the recommended 30g of daily fibre.<br><span class="assess-hint">Track a typical day using a free app like MyFitnessPal, or estimate from your usual foods.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Enjoyment & Culture</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-distinct-foods">
    <label for="a-distinct-foods">I know roughly how many distinct foods I eat in a typical week.<br><span class="assess-hint">Count individual ingredients &ndash; rice, chicken, broccoli, olive oil each count separately.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-cooking">
    <label for="a-cooking">I know how many times per week I cook a meal from scratch.<br><span class="assess-hint">From scratch means assembling raw or minimally processed ingredients, not reheating.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-social-meals">
    <label for="a-social-meals">I know how many meals per week I share with other people.<br><span class="assess-hint">Eating together at the same table, whether at home, at a restaurant, or at someone else's house.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Ethical & Environmental Impact</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-meat-frequency">
    <label for="a-meat-frequency">I know how many days per week I eat meat or fish.<br><span class="assess-hint">Count any day where you eat at least one serving of meat, poultry, or fish.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-food-waste">
    <label for="a-food-waste">I have a rough sense of how much food I throw away each week.<br><span class="assess-hint">Check your bin over a few days. Include leftovers, expired items, and uneaten portions.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-sourcing">
    <label for="a-sourcing">I know where most of my food comes from &ndash; supermarket, local shops, markets, or online.<br><span class="assess-hint">Think about your main weekly shop and any other regular food purchases.</span></label>
</div>
</div>

<button class="l1-mark-done" id="assessBtn" onclick="completeStep('assess')" disabled>Tick all items to continue</button>

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

    window.toggleAssess = function(el) {
        var cb = el.querySelector('input[type="checkbox"]');
        if (!cb) return;
        // Toggle if the click wasn't directly on the checkbox
        if (document.activeElement !== cb) {
            cb.checked = !cb.checked;
        }
        el.classList.toggle('checked', cb.checked);

        // Save checklist state
        var checklist = {};
        ASSESS_IDS.forEach(function(id) {
            var box = document.getElementById(id);
            if (box) checklist[id] = box.checked;
        });
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-assess') || {};
            all[AREA] = checklist;
            APStorage.save('ap-level1-assess', all);
        }

        // Enable button when all checked
        var allChecked = ASSESS_IDS.every(function(id) {
            var box = document.getElementById(id);
            return box && box.checked;
        });
        var btn = document.getElementById('assessBtn');
        if (btn) {
            btn.disabled = !allChecked;
            btn.textContent = allChecked ? 'All done \u2013 continue' : 'Tick all items to continue';
        }
    };

    function restoreChecklist() {
        if (typeof APStorage === 'undefined') return;
        var all = APStorage.load('ap-level1-assess') || {};
        var checklist = all[AREA] || {};
        ASSESS_IDS.forEach(function(id) {
            var box = document.getElementById(id);
            if (box && checklist[id]) {
                box.checked = true;
                var item = box.closest('.assess-item');
                if (item) item.classList.add('checked');
            }
        });
        // Check if all are already ticked
        var allChecked = ASSESS_IDS.every(function(id) {
            var box = document.getElementById(id);
            return box && box.checked;
        });
        var btn = document.getElementById('assessBtn');
        if (btn && allChecked) {
            btn.disabled = false;
            btn.textContent = 'All done \u2013 continue';
        }
    }

    document.addEventListener('DOMContentLoaded', function() {
        restoreChecklist();
        updateUI();
    });
})();
</script>
