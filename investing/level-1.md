---
layout: default
title: "Investing – Level 1: Awareness"
life_area_slug: investing
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

<h1>Investing: Level 1</h1>

<p class="l1-subtitle">Understand what investing means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Investing Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why investing matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Investing is one of the few financial decisions where time does most of the work for you. A portfolio growing at 7% annually (the long-run average for global equities after inflation) doubles roughly every ten years. Someone who invests $500 a month starting at 25 would have over $1 million by 55 &ndash; and more than half of that total comes from returns on returns, not from the money they put in.</p>

<p>Most people who invest still underperform. <a href="https://www.dalbar.com/QAIB/Index" target="_blank">DALBAR's annual studies</a> consistently show that the average equity fund investor trails the S&amp;P 500 by 3 &ndash; 5% annually over 20-year periods. The gap comes from behavioural mistakes &ndash; buying after gains and selling after losses &ndash; rather than poor fund selection. Basic discipline and a long time horizon put you ahead of the majority.</p>

<p>Professional management seldom helps. The <a href="https://www.spglobal.com/spdji/en/research-insights/spiva/" target="_blank">SPIVA scorecard</a> shows that 94% of actively managed domestic equity funds underperform their benchmark over 20 years. Low-cost index funds, which require almost no expertise to use, tend to beat most professionals over long periods. This makes investing unusual among skills: a simple, passive approach is genuinely difficult to improve upon.</p>

<p>Financial literacy remains surprisingly rare. Research by <a href="https://www.nber.org/papers/w17107" target="_blank">Lusardi and Mitchell</a> found that only 43% of adults worldwide can correctly answer three basic questions about compound interest, inflation, and diversification. Even foundational knowledge &ndash; understanding what you own and why &ndash; represents a meaningful advantage.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about investing</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People invest for different reasons. This site scores every investing intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Growth</h3>
<p>Maximising the long-term increase in your invested wealth. People who lean towards this value focus on compounding, appropriate asset allocation, and consistent contributions over decades. They tend to accept short-term volatility in exchange for higher expected returns, and they measure success by the total value of their portfolio over time.</p>

<h3>Safety</h3>
<p>Protecting your capital from catastrophic loss. People who lean towards this value prioritise diversification, position sizing, and resilient portfolio construction. They want to avoid scenarios where a single bad bet, market crash, or economic shift could wipe out years of progress. They measure success by how well their portfolio holds up in the worst periods.</p>

<h3>Simplicity</h3>
<p>Keeping your investment approach straightforward and low-maintenance. People who lean towards this value want a system they can set up once and sustain for decades without active management, frequent trading, or specialist knowledge. They measure success by how little time and attention their investments require while still delivering reasonable returns.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each investing value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Growth &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Warren_Buffett" target="_blank">Warren Buffett</a> compounded Berkshire Hathaway's book value at roughly 20% annually for over 58 years, turning an initial investment in a struggling textile company into one of the world's largest conglomerates. His approach relies on buying businesses with durable competitive advantages and holding them indefinitely. That rate of compounding, sustained over that duration, appears to be without precedent in public markets.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Safety &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Ray_Dalio" target="_blank">Ray Dalio</a> built Bridgewater Associates into the world's largest hedge fund, managing over $150 billion at its peak. His All Weather portfolio strategy, designed in the 1990s, allocates across asset classes to perform acceptably in any economic regime &ndash; growth, recession, rising inflation, or falling inflation. The approach has likely influenced a generation of institutional and retail portfolio construction, and variations of it are now widely used by individual investors.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Simplicity &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/John_C._Bogle" target="_blank">John C. Bogle</a> founded Vanguard in 1975 and launched the first retail index fund the following year. He spent decades arguing that most investors would do better with a low-cost, broadly diversified index fund than with any actively managed alternative &ndash; a claim that subsequent data has strongly supported. By the time of his death in 2019, index funds held trillions of dollars and had become the default recommendation for most individual investors.</p>
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
<h4>Growth</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-contrib-rate">
    <label for="a-contrib-rate">I know what percentage of my income I currently invest each month.<br><span class="assess-hint">Include pension contributions, ISAs, brokerage accounts, and any other investment vehicles.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-asset-allocation">
    <label for="a-asset-allocation">I know the approximate split between equities, bonds, and cash across all my accounts.<br><span class="assess-hint">Check your pension, ISA, and any other investment accounts. Many providers show this on a summary page.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-total-return">
    <label for="a-total-return">I know roughly how my investments have performed over the past year.<br><span class="assess-hint">Look for a total return or performance figure in your account dashboard. A rough number is fine.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Safety</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-diversification">
    <label for="a-diversification">I know how many different funds or holdings I own and whether they overlap significantly.<br><span class="assess-hint">Two global equity index funds from different providers may hold largely the same stocks.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-largest-position">
    <label for="a-largest-position">I know what my single largest holding is and what percentage of my total portfolio it represents.<br><span class="assess-hint">Include employer shares, property investments, and individual stock positions.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-emergency-fund">
    <label for="a-emergency-fund">I know how many months of expenses I could cover without selling investments.<br><span class="assess-hint">Count cash savings and easily accessible funds that are separate from your investment portfolio.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Simplicity</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-time-spent">
    <label for="a-time-spent">I know roughly how much time I spend on my investments each month.<br><span class="assess-hint">Include research, trading, checking prices, reading financial news, and rebalancing.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-fees">
    <label for="a-fees">I know the total annual fees I pay on my investments, including platform fees and fund charges.<br><span class="assess-hint">Check your provider's fee schedule. Many platforms list a combined figure as a percentage of your portfolio.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-auto-contributions">
    <label for="a-auto-contributions">I know whether my contributions are automated or whether I invest manually each time.<br><span class="assess-hint">Check if you have a standing order or direct debit set up for regular investments.</span></label>
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

<p>You now understand why investing matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about growth, safety, and simplicity. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/investing/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Investing Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Investing. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/investing/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'investing';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-contrib-rate', 'a-asset-allocation', 'a-total-return',
        'a-diversification', 'a-largest-position', 'a-emergency-fund',
        'a-time-spent', 'a-fees', 'a-auto-contributions'
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
