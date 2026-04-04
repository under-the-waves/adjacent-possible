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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to look up or test. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've found it out).</p>

<div class="assess-group">
<h4>Competence</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-meals-per-week">
    <label for="a-meals-per-week">I know how many meals per week I prepare at home versus buy prepared.<br><span class="assess-hint">Count breakfasts, lunches, and dinners separately. Include meal kits and reheated batch-cooked meals as home-prepared.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-planning-method">
    <label for="a-planning-method">I can describe my current meal planning method (or confirm I don't have one).<br><span class="assess-hint">Weekly plan, daily improvisation, rotating set of staples, or something else entirely.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-fallback">
    <label for="a-fallback">I know what I do when my usual food plan breaks down &ndash; unexpected guests, empty fridge, no energy to cook.<br><span class="assess-hint">Reliable fallback options might include a go-to takeaway, freezer meals, or a 10-minute storecupboard recipe.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Craft</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-technique-count">
    <label for="a-technique-count">I know roughly how many cooking techniques I can execute confidently (e.g. roasting, stir-frying, braising, baking).<br><span class="assess-hint">Count only methods you use without needing to look up the basics each time.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-new-recipes">
    <label for="a-new-recipes">I know how often I try a new recipe or technique &ndash; weekly, monthly, rarely, or never.<br><span class="assess-hint">This is about frequency, not success rate. Attempting and failing counts.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-enjoy-cooking">
    <label for="a-enjoy-cooking">I have a clear sense of whether I enjoy the process of cooking, tolerate it, or actively dislike it.<br><span class="assess-hint">There is no right answer. Knowing your honest reaction helps you choose the right interventions.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Waste Reduction</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-waste-amount">
    <label for="a-waste-amount">I know roughly how much food I throw away in a typical week.<br><span class="assess-hint">Check your bin over a few days if you're unsure. Include uneaten leftovers, expired items, and spoiled produce.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-fridge-audit">
    <label for="a-fridge-audit">I know what is currently in the back of my fridge and whether any of it has gone off.<br><span class="assess-hint">Open the fridge and check now if you're not sure. This is a useful baseline.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-leftover-plan">
    <label for="a-leftover-plan">I know what I typically do with leftovers &ndash; eat them, freeze them, or throw them away.<br><span class="assess-hint">Think about the last three times you had food left over after a meal.</span></label>
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
        'a-meals-per-week', 'a-planning-method', 'a-fallback',
        'a-technique-count', 'a-new-recipes', 'a-enjoy-cooking',
        'a-waste-amount', 'a-fridge-audit', 'a-leftover-plan'
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
