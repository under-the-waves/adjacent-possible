---
layout: default
title: "Saving – Level 1: Awareness"
life_area_slug: saving
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

<h1>Saving: Level 1</h1>

<p class="l1-subtitle">Understand what saving means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Saving Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why saving matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Saving is the single most foundational financial behaviour. The evidence for its impact on wellbeing is strong and consistent.</p>

<p><a href="https://corporate.vanguard.com/content/corporatesite/us/en/corp/articles/emergency-savings-financial-wellbeing.html" target="_blank">Emergency savings are the strongest predictor</a> of overall financial wellbeing &ndash; stronger than income level, debt-to-income ratio, or investment portfolio size. Having even a modest emergency fund significantly reduces financial stress and improves decision-making across all other financial domains.</p>

<p>Yet most people have dangerously thin buffers. <a href="https://www.bankrate.com/banking/savings/emergency-savings-report/" target="_blank">24 – 27% of adults</a> have no emergency savings at all, and only 27 – 28% have six or more months of expenses saved. The <a href="https://fred.stlouisfed.org/series/PSAVERT" target="_blank">national savings rate</a> hovers between 3 – 5%, and the <a href="https://www.bls.gov/cex/tables.htm" target="_blank">bottom 40% of earners</a> have negative savings rates.</p>

<p>The psychological cost is substantial. People without emergency savings spend an average of 7.3 hours per week worrying about finances &ndash; nearly double the rate of those with even a modest buffer. Saving creates genuine choice: a financial buffer turns forced reactions into deliberate decisions, giving you the freedom to leave a bad job, seize an opportunity, or weather a crisis without going into debt.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about saving</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People save for different reasons. This site scores every saving intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Security</h3>
<p>Building and maintaining a financial buffer against unexpected expenses and income disruption. People who lean towards this value focus on emergency funds, insurance, and ensuring their reserves can absorb shocks without resorting to debt. They prioritise stability and protection from downside scenarios.</p>

<h3>Lifestyle</h3>
<p>Saving toward specific lifestyle goals &ndash; holidays, experiences, purchases, and planned upgrades to quality of life. People who lean towards this value see saving as a tool for living better, not just surviving emergencies. They balance present enjoyment with future security and maintain targeted savings accounts for near-term goals.</p>

<h3>Growth</h3>
<p>Accumulating wealth over time through consistently high savings rates. People who lean towards this value focus on the long-term trajectory of their wealth &ndash; steadily increasing net worth, maximising the rate at which savings compound, and sustaining saving discipline across years and decades.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each saving value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Security &ndash; Level 5</div>
    <p><a href="https://www.mrmoneymustache.com/about/" target="_blank">Pete Adeney</a> (Mr. Money Mustache) retired at 30 after saving aggressively on a moderate software engineering salary. He accumulated enough invested assets to cover his family's living expenses indefinitely without earned income, achieving complete financial security through disciplined saving and frugal living. His detailed public accounting of household expenses demonstrates sustained annual spending well below the median, funded entirely by investment returns.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Lifestyle &ndash; Level 5</div>
    <p><a href="https://affordanything.com/about/" target="_blank">Paula Pant</a> built a savings system designed explicitly around lifestyle goals. She saved enough to buy multiple rental properties in her 20s, then used the income to fund extended international travel and eventual full financial independence. Her approach treats saving as the mechanism for buying freedom and experiences, maintaining full liquidity and access to capital at all times while funding a deliberately chosen lifestyle.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Growth &ndash; Level 5</div>
    <p><a href="https://earlyretirementextreme.com/about" target="_blank">Jacob Lund Fisker</a> (Early Retirement Extreme) sustained a savings rate above 75% for five years on a postdoctoral researcher's salary, accumulating 25 times his annual expenses and reaching full financial independence by age 33. His meticulous documentation of the process shows how extreme savings rates compress the timeline to financial independence from decades to years.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to look up. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've found it out).</p>

<div class="assess-group">
<h4>Security</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-monthly-essentials">
    <label for="a-monthly-essentials">I know my monthly essential expenses &ndash; the minimum I need to cover housing, food, utilities, and transport.<br><span class="assess-hint">Add up your non-negotiable outgoings. Exclude discretionary spending like dining out or subscriptions.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-buffer-weeks">
    <label for="a-buffer-weeks">I know how many weeks of financial buffer I currently hold in accessible savings.<br><span class="assess-hint">Divide your accessible savings by your weekly essential expenses.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-income-disruption">
    <label for="a-income-disruption">I know what would happen to my finances if I lost my income for three months.<br><span class="assess-hint">Consider savings, benefits, notice periods, and any other safety nets you have.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Lifestyle</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-liquidity-profile">
    <label for="a-liquidity-profile">I know what proportion of my savings is instantly accessible versus locked away in pensions, notice accounts, or other restricted vehicles.<br><span class="assess-hint">Check how much you could access within 24 hours, within a week, and within a month.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-specific-goals">
    <label for="a-specific-goals">I know whether I am currently saving toward any specific goals, and if so, how much progress I've made.<br><span class="assess-hint">Examples: a holiday, a deposit on a house, a car, or a particular experience.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-enjoyment-tradeoffs">
    <label for="a-enjoyment-tradeoffs">I have a sense of whether my current saving rate feels sustainable or whether it comes at the cost of things I value.<br><span class="assess-hint">Are you saving comfortably, or does it feel like a constant sacrifice?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Growth</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-savings-rate">
    <label for="a-savings-rate">I know my current savings rate &ndash; what percentage of my income I save each month.<br><span class="assess-hint">Divide your monthly savings by your monthly take-home pay. Include pension contributions if you wish.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-total-saved">
    <label for="a-total-saved">I know my total savings balance across all accounts.<br><span class="assess-hint">Include current account buffers, savings accounts, ISAs, and any other liquid assets. Exclude pensions and property.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-savings-trend">
    <label for="a-savings-trend">I know whether my total savings have been growing, shrinking, or staying flat over the past 6 months.<br><span class="assess-hint">Even a rough sense counts &ndash; you don't need exact figures.</span></label>
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

<p>You now understand why saving matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about security, lifestyle, and growth. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/saving/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Saving Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Saving. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/saving/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'saving';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-monthly-essentials', 'a-buffer-weeks', 'a-income-disruption',
        'a-liquidity-profile', 'a-specific-goals', 'a-enjoyment-tradeoffs',
        'a-savings-rate', 'a-total-saved', 'a-savings-trend'
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
