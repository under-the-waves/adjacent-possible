---
layout: default
title: "Housing – Level 1: Awareness"
life_area_slug: housing
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

<h1>Housing: Level 1</h1>

<p class="l1-subtitle">Understand what housing means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Housing Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why housing matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Housing is the single largest expense most people face, and its effects extend well beyond the financial. Where and how you live shapes your physical health, mental health, relationships, and daily quality of life.</p>

<p>Research published in the <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9914515/" target="_blank">Journal of Housing and the Built Environment</a> found that households spending more than 30% of income on housing report significantly lower life satisfaction. Nearly <a href="https://www.census.gov/newsroom/press-releases/2024/renter-households-cost-burdened-race.html" target="_blank">half of renters</a> (49.7%) and 23.7% of homeowners exceed this threshold.</p>

<p>The effects go well beyond cost. Housing quality is linked to <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12333583/" target="_blank">material hardship, lower cognitive achievement for children, higher maternal stress, and strained social and familial relationships</a>. Poor housing conditions &ndash; damp, cold, overcrowding, noise &ndash; are associated with respiratory illness, sleep disruption, and chronic stress.</p>

<p>Location matters too. Commute time is one of the strongest predictors of daily wellbeing, with research in <a href="https://link.springer.com/article/10.1007/s11116-019-09983-9" target="_blank">Transportation</a> showing that longer commutes are associated with lower life satisfaction, less sleep, and reduced time for exercise and social connection. Your housing situation is the foundation on which other life areas rest.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about housing</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People make housing decisions for different reasons. This site scores every housing intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Comfort</h3>
<p>The physical quality of your living environment &ndash; space, light, temperature, noise levels, maintenance condition, and overall pleasantness. Having enough room for your activities, a well-functioning home that does not create daily friction, and an environment that supports rest and productivity. People who lean towards this value invest in the quality of their living space.</p>

<h3>Affordability</h3>
<p>Keeping housing costs at a sustainable level that preserves financial flexibility for other life goals. Mortgage or rent payments, utilities, maintenance, insurance, and taxes remaining below burdensome thresholds. People who lean towards this value make housing decisions that protect their broader financial health.</p>

<h3>Location</h3>
<p>Proximity to work, social connections, amenities, nature, and the quality of the surrounding neighbourhood. Commute time, access to services, safety, community character, and the fit between your lifestyle needs and what the location provides. People who lean towards this value choose where to live based on how the location supports their daily life.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each housing value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Comfort &ndash; Level 5</div>
    <p><a href="https://www.christophlowell.com/" target="_blank">Christopher Lowell</a> is an interior designer who has spent decades demonstrating how to create exceptionally comfortable living environments without excessive budgets. His approach centres on spatial flow, natural light maximisation, and designing rooms around daily rhythms. His own homes have consistently reflected these principles &ndash; purpose-designed spaces for work, rest, and socialising with no deferred maintenance or unresolved friction points.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Affordability &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Jay_Shafer" target="_blank">Jay Shafer</a> pioneered the tiny house movement by designing and living in homes under 10 square metres. He founded the Tumbleweed Tiny House Company and has lived in his own small-footprint houses since the late 1990s, consistently keeping his housing costs to a fraction of the national average. His approach demonstrates that deliberate downsizing can free up both money and time without sacrificing comfort.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Location &ndash; Level 5</div>
    <p><a href="https://www.strongtowns.org/charles-marohn" target="_blank">Charles Marohn</a> is an urban planner and author who has written extensively about what makes neighbourhoods work. He lives in a walkable small-town setting that he chose specifically for its combination of community connection, access to daily needs, natural environment, and manageable scale &ndash; a deliberate alignment between location and lifestyle priorities that he has maintained for decades.</p>
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
<h4>Comfort</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-space">
    <label for="a-space">I know which rooms or areas in my home feel too small, too dark, or poorly laid out for their purpose.<br><span class="assess-hint">Consider your bedroom, workspace, kitchen, and any shared living areas.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-temperature">
    <label for="a-temperature">I know whether my home stays at a comfortable temperature year-round without excessive heating or cooling costs.<br><span class="assess-hint">Think about draughts, insulation, and whether any rooms are consistently too hot or cold.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-maintenance">
    <label for="a-maintenance">I know what maintenance issues I have been putting off.<br><span class="assess-hint">Leaking taps, broken fixtures, peeling paint, appliances that don't work properly, damp patches.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Affordability</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-cost-ratio">
    <label for="a-cost-ratio">I know my total housing costs as a percentage of my gross income.<br><span class="assess-hint">Include rent or mortgage, council tax, utilities, insurance, and regular maintenance. The standard affordability threshold is 30%.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-buffer">
    <label for="a-buffer">I know whether I have a financial buffer for unexpected housing costs.<br><span class="assess-hint">A broken boiler, roof repair, or sudden rent increase. Could you cover a &pound;1,000 &ndash; &pound;3,000 housing emergency?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-equity">
    <label for="a-equity">I know whether my current housing situation is building equity or long-term financial value.<br><span class="assess-hint">Homeowners: mortgage principal payments. Renters: whether the flexibility or lower commitment offsets the lack of equity.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Location</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-commute">
    <label for="a-commute">I know my actual door-to-door commute time on a typical day.<br><span class="assess-hint">Include walking to transport, waiting, and any transfers. If you work from home, consider how often you travel to a workplace or clients.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-amenities">
    <label for="a-amenities">I know how far I am from the amenities I use most &ndash; grocery shops, healthcare, green space, and social venues.<br><span class="assess-hint">Walking distance? Driving distance? Do you avoid using certain services because they are inconvenient to reach?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-neighbourhood">
    <label for="a-neighbourhood">I have a clear sense of whether my neighbourhood feels safe, well-connected, and suited to my lifestyle.<br><span class="assess-hint">Consider noise, safety, community character, and whether the area supports or hinders the life you want to live.</span></label>
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

<p>You now understand why housing matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about comfort, affordability, and location. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/housing/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Housing Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Housing. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/housing/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'housing';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-space', 'a-temperature', 'a-maintenance',
        'a-cost-ratio', 'a-buffer', 'a-equity',
        'a-commute', 'a-amenities', 'a-neighbourhood'
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
