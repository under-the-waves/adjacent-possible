---
layout: default
title: "Organisation – Level 1: Awareness"
life_area_slug: organisation
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

<h1>Organisation: Level 1</h1>

<p class="l1-subtitle">Understand what organisation means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Organisation Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why organisation matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Organisation is the invisible infrastructure behind reliability and clarity. When it works, you barely notice it. When it fails, the costs are constant and compounding.</p>

<p>The average person spends <a href="https://www.prnewswire.com/news-releases/lost-and-found-the-average-american-spends-25-days-each-year-looking-for-lost-items-collectively-costing-us-households-27-billion-annually-in-replacement-costs-300449305.html" target="_blank">8.5 minutes per day</a> searching for misplaced items, and knowledge workers lose <a href="https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-social-economy" target="_blank">1.8 &ndash; 2.5 hours per day</a> hunting for information they need. That is roughly a quarter of the working day spent on retrieval rather than productive work.</p>

<p><a href="https://blog.idonethis.com/how-to-master-the-art-of-to-do-lists/" target="_blank">41% of to-do list items</a> are never completed, and <a href="https://www.unitedhealthgroup.com/newsroom/2022/2022-07-20-optum-consumer-survey-better-tools-for-finding-care.html" target="_blank">52% of people</a> missed a healthcare appointment in the past year &ndash; a third of them simply because they forgot. <a href="https://www.acuitytraining.co.uk/news-tips/time-management-statistics-research/" target="_blank">82% of people</a> have no formal time management system at all.</p>

<p>The baseline is so low that even modest improvements in capture, filing, and review place you well above the majority. Organisation is one of the rare areas where the gap between average and competent is enormous, and the effort required to close it is relatively small.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about organisation</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue organisation for different reasons. This site scores every organisation intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Tracking</h3>
<p>Capturing and monitoring all commitments, tasks, and information so nothing falls through the cracks. Maintaining a trusted system for recording what needs doing, reviewing progress regularly, and ensuring everything important is visible and accounted for. People who prioritise this value invest in comprehensive capture and review systems.</p>

<h3>Order</h3>
<p>Maintaining structured, predictable systems for physical and digital environments. Consistent filing, clear storage systems, labelled locations for everything, and routines that keep spaces and information organised. People who prioritise this value believe that external order supports internal clarity.</p>

<h3>Speed</h3>
<p>Minimising the time spent on organisational overhead so you can move quickly from intention to action. Rapid processing of incoming tasks, fast retrieval of information, and systems designed for throughput over perfection. People who prioritise this value accept occasional missed details in exchange for getting more done.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each organisation value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Tracking &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/David_Allen_(author)" target="_blank">David Allen</a> developed Getting Things Done (GTD), one of the most widely adopted personal productivity systems in the world. His methodology centres on comprehensive capture and regular review of all commitments, and he has practised and refined it for over 30 years. His concept of "mind like water" &ndash; a state of zero open loops in your head &ndash; has become the benchmark for what thoroughness in personal organisation looks like.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Order &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Martha_Stewart" target="_blank">Martha Stewart</a> built a media empire around the systematic organisation of domestic life. Her approach to household management treats every domain &ndash; from kitchen storage to seasonal maintenance schedules &ndash; as a system to be designed, documented, and maintained. She has practised and publicly demonstrated this level of domestic order for over 40 years across multiple homes.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Speed &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Tiago_Forte" target="_blank">Tiago Forte</a> developed the "Building a Second Brain" methodology for organising digital information and projects. He practises what he teaches &ndash; maintaining a personal knowledge management system that he uses daily to run a company, write, and teach. His approach prioritises speed of retrieval over comprehensiveness, and he has refined it through over a decade of personal use.</p>
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
<h4>Tracking</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-capture-system">
    <label for="a-capture-system">I know whether I have a single, trusted place where I capture all incoming tasks and commitments.<br><span class="assess-hint">This could be an app, a notebook, a whiteboard &ndash; anything you consistently use to record what needs doing.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-review-frequency">
    <label for="a-review-frequency">I know how often I review my outstanding tasks and commitments.<br><span class="assess-hint">Daily? Weekly? Never? Think about whether you have a regular review habit or rely on memory.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-missed-commitments">
    <label for="a-missed-commitments">I can estimate how many commitments I dropped or forgot in the past month.<br><span class="assess-hint">Missed appointments, forgotten promises, overdue tasks, unanswered messages you meant to reply to.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Order</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-physical-spaces">
    <label for="a-physical-spaces">I know whether my main physical spaces (desk, kitchen, bedroom) have a designated place for every item.<br><span class="assess-hint">Could you tell someone exactly where everything belongs? Or do things accumulate on surfaces?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-digital-files">
    <label for="a-digital-files">I know whether I can find any digital file I need within 60 seconds.<br><span class="assess-hint">Think about documents, photos, receipts, passwords. Do you have a filing system or do you rely on search?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-clutter">
    <label for="a-clutter">I know whether I feel overwhelmed by clutter in my home or workspace.<br><span class="assess-hint">54% of people report feeling overwhelmed by clutter. Be honest about whether this applies to you.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Speed</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-search-time">
    <label for="a-search-time">I have a rough sense of how much time I spend each day searching for things I've misplaced.<br><span class="assess-hint">Keys, wallet, phone, documents, tools. The average is about 8.5 minutes per day.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-inbox-processing">
    <label for="a-inbox-processing">I know how quickly I typically process new tasks and messages that come in.<br><span class="assess-hint">Same day? Same week? Do some sit unprocessed for weeks? Think about email, post, and verbal requests.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-system-count">
    <label for="a-system-count">I can list the tools and systems I currently use to stay organised.<br><span class="assess-hint">Apps, notebooks, calendars, reminders, filing systems. Count them &ndash; is it 1 &ndash; 2 core tools, or a scattered collection?</span></label>
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

<p>You now understand why organisation matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about tracking, order, and speed. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/organisation/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Organisation Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Organisation. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/organisation/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'organisation';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-capture-system', 'a-review-frequency', 'a-missed-commitments',
        'a-physical-spaces', 'a-digital-files', 'a-clutter',
        'a-search-time', 'a-inbox-processing', 'a-system-count'
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
