---
layout: default
title: "Financial Planning and Tracking – Level 1: Awareness"
life_area_slug: financial-planning-tracking
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

<h1>Financial Planning and Tracking: Level 1</h1>

<p class="l1-subtitle">Understand what financial planning means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Financial Planning Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why financial planning and tracking matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Financial planning and tracking form the foundation for virtually every other financial decision you make. The evidence for their impact is broad and consistent.</p>

<p>People with a written financial plan report <a href="https://fpsb.org/about-financial-planning/the-value-of-financial-planning/" target="_blank">38% improved financial wellbeing</a>, 37% greater financial confidence, and 36% better understanding of financial matters. Over half say financial planning has positively affected their mental health and family life.</p>

<p>Yet most people operate without systematic tracking. <a href="https://www.thepennyhoarder.com/budgeting/budgeting-statistics/" target="_blank">55% of Americans</a> do not use any form of budget, and most who claim to budget are simply reviewing bank statements after the fact. Only <a href="https://www.schwab.com/learn/story/modern-wealth-survey" target="_blank">36% have a written financial plan</a>, despite widespread recognition that planning works.</p>

<p>The psychological benefits extend well beyond money management. Having a clear picture of your finances reduces the mental burden of constant uncertainty &ndash; 74% of Americans report stress over personal finances, but those with financial plans report significantly lower anxiety. Tracking also improves cognitive performance by providing clear information for decisions, reducing the errors that come from guessing or estimating.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about financial planning</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach financial planning for different reasons. This site scores every financial planning intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Accuracy & Control</h3>
<p>Having precise, reliable financial information and clear oversight of money flows. People who lean towards this value want comprehensive data and tight control over their financial picture, enabling informed decisions based on complete information. They track every category, reconcile accounts, and know exactly where money goes.</p>

<h3>Simplicity & Convenience</h3>
<p>Making financial management effortless and low-friction. People who lean towards this value want good financial outcomes without having to think about money regularly. They prefer automated systems, minimal time investment, and approaches that work in the background with occasional check-ins.</p>

<h3>Insight & Optimisation</h3>
<p>Using financial data to make better decisions and identify opportunities. People who lean towards this value enjoy the analytical side &ndash; trend analysis, finding inefficiencies, and turning tracking data into actionable improvements that compound over time.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each financial planning value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Accuracy & Control &ndash; Level 5</div>
    <p><a href="https://www.youneedabudget.com/the-four-rules/" target="_blank">Jesse Mecham</a> founded YNAB (You Need A Budget) in 2004 after developing a meticulous envelope-based budgeting system as a newly married university student. He built it into a company used by millions of people worldwide, all grounded in the principle that every pound should be assigned a specific purpose before it is spent. His personal financial tracking system accounts for every transaction across all accounts in real time, and his methodology has demonstrably changed the financial behaviour of hundreds of thousands of users.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Simplicity & Convenience &ndash; Level 5</div>
    <p><a href="https://jlcollinsnh.com/about/" target="_blank">JL Collins</a> spent decades refining his personal finances into the simplest possible system &ndash; a single index fund, automated contributions, and minimal ongoing management. His approach, documented in <em>The Simple Path to Wealth</em>, deliberately rejects complexity in favour of systems that require almost no maintenance while delivering strong long-term outcomes. He manages his own portfolio in under an hour per year.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Insight & Optimisation &ndash; Level 5</div>
    <p><a href="https://www.madfientist.com/about/" target="_blank">Brandon Ganch</a> (the Mad Fientist) built detailed analytical models of his own finances, systematically optimising tax strategies, account structures, and spending patterns. His spreadsheets and calculators, published freely online, helped him retire at 34 by identifying and eliminating financial inefficiencies that most people never notice. He treats personal finance as an engineering problem, quantifying the impact of every decision.</p>
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
<h4>Accuracy & Control</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-monthly-spending">
    <label for="a-monthly-spending">I know roughly how much I spent last month, within 10% of the actual figure.<br><span class="assess-hint">Check your bank statements or budgeting app if you're not sure.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-net-worth">
    <label for="a-net-worth">I know my current net worth &ndash; total assets minus total debts.<br><span class="assess-hint">Include savings, investments, property, pensions, and any outstanding loans, credit cards, or mortgages.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-top-categories">
    <label for="a-top-categories">I know my three largest spending categories and roughly how much goes to each.<br><span class="assess-hint">Common categories include housing, food, transport, and subscriptions.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Simplicity & Convenience</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-tracking-method">
    <label for="a-tracking-method">I know what system (if any) I currently use to track my finances, and whether I use it consistently.<br><span class="assess-hint">This could be a spreadsheet, an app, a notebook, or nothing at all.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-time-on-finances">
    <label for="a-time-on-finances">I know roughly how much time I spend managing my finances each month.<br><span class="assess-hint">Include bill-paying, budgeting, checking accounts, and any financial admin.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-automated">
    <label for="a-automated">I know which of my regular payments and savings are automated and which I handle manually.<br><span class="assess-hint">Check standing orders, direct debits, and any manual transfers you make each month.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Insight & Optimisation</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-financial-goals">
    <label for="a-financial-goals">I have at least one specific financial goal with a target amount and date.<br><span class="assess-hint">Examples: "Save &pound;10,000 by December 2027" or "Pay off credit card by March 2026."</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-spending-trends">
    <label for="a-spending-trends">I know whether my total spending has been going up, down, or staying flat over the past 6 months.<br><span class="assess-hint">Even a rough sense counts &ndash; you don't need exact figures.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-unnecessary-costs">
    <label for="a-unnecessary-costs">I have identified at least one regular expense I could reduce or eliminate without meaningfully affecting my quality of life.<br><span class="assess-hint">Subscriptions, insurance premiums, and energy tariffs are common candidates.</span></label>
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

<p>You now understand why financial planning matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about accuracy and control, simplicity and convenience, and insight and optimisation. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/financial-planning-tracking/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Financial Planning Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Financial Planning and Tracking. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/financial-planning-tracking/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'financial-planning-tracking';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-monthly-spending', 'a-net-worth', 'a-top-categories',
        'a-tracking-method', 'a-time-on-finances', 'a-automated',
        'a-financial-goals', 'a-spending-trends', 'a-unnecessary-costs'
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
