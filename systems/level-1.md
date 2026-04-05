---
layout: default
title: "Systems – Level 1: Awareness"
life_area_slug: systems
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

<h1>Systems: Level 1</h1>

<p class="l1-subtitle">Understand what personal systems are, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Systems Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why systems matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Personal systems are the tools, automations, and workflows you build to handle recurring tasks and manage information. They are the infrastructure that lets you spend your attention on decisions and creative work rather than on logistics.</p>

<p><a href="https://www.breeze.pm/blog/task-management-statistics" target="_blank">94% of employees</a> regularly perform repetitive tasks that consume significant time, and around 54% believe automation could save them more than 5 hours per week. <a href="https://www.cflowapps.com/workflow-automation-statistics/" target="_blank">Workflow automation</a> can reduce repetitive tasks by 60 &ndash; 95%, saving up to 77% of time on routine activities.</p>

<p>Without intentional systems, <a href="https://www.breeze.pm/blog/task-management-statistics" target="_blank">approximately 70% of projects</a> fall short of their goals in timely delivery, budget, or scope. Teams that prioritise tasks effectively are 1.4 times more likely to outperform their peers.</p>

<p>The gap compounds over time. Systematic approaches accumulate benefits whilst ad hoc approaches accumulate costs. The best systems are invisible &ndash; they are obvious only in their absence, working quietly in the background so you can focus on what actually matters.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about systems</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue systems for different reasons. This site scores every systems intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Power</h3>
<p>Maximising what your personal systems can do &ndash; automation depth, feature richness, customisation, and the ability to handle complex workflows and edge cases. People who prioritise this value invest significant time building systems that save large amounts of time once complete, accepting complexity as a worthwhile cost.</p>

<h3>Simplicity</h3>
<p>Keeping personal systems as minimal, intuitive, and easy to understand as possible. Using fewer tools, avoiding over-engineering, choosing solutions that require no documentation to use, and preferring manual processes over complex automations that might break. People who prioritise this value believe the best system is one you actually use consistently, and that complexity is the enemy of sustained adoption.</p>

<h3>Reliability</h3>
<p>Ensuring your systems work consistently and fail gracefully, with minimal unplanned maintenance or debugging. Choosing proven tools over cutting-edge ones, building in redundancy, testing automations before depending on them, and designing systems that degrade gracefully when something breaks. People who prioritise this value accept less capability or more manual work in exchange for systems they can trust.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each systems value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Power &ndash; Level 5</div>
    <p><a href="https://www.youtube.com/@NetworkChuck" target="_blank">Chuck Keith</a> (NetworkChuck) is a network engineer and content creator who has built comprehensive personal infrastructure including self-hosted servers, automated backups, network monitoring, smart home integrations, and custom dashboards that manage nearly every aspect of his digital life. He documents these builds publicly, demonstrating systems that handle complex conditional logic across personal and professional domains whilst remaining maintainable by a single person.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Simplicity &ndash; Level 5</div>
    <p><a href="https://dereksivers.com/" target="_blank">Derek Sivers</a> is a programmer, author, and former founder of CD Baby (which he sold for $22 million). He runs his entire life from a small set of plain-text files, a custom-built personal database, and minimal tooling he wrote himself. His systems handle contacts, projects, finances, and media &ndash; all designed to be so simple that they survive moves between countries and decades of use without needing redesign.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Reliability &ndash; Level 5</div>
    <p><a href="https://www.hanselman.com/about" target="_blank">Scott Hanselman</a> is a software engineer, podcaster, and speaker who has maintained the same core personal productivity systems for over 20 years. He has published extensively about his setup, which prioritises proven tools, redundant backups, and graceful degradation. His systems have survived multiple job changes, technology migrations, and a Type 1 diabetes diagnosis that required integrating medical device data into his daily workflow without disrupting everything else.</p>
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
<h4>Power</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-automation-count">
    <label for="a-automation-count">I know how many automated workflows I currently have running (if any).<br><span class="assess-hint">Email filters, scheduled backups, smart home routines, IFTTT or Zapier automations, scripts, cron jobs.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-manual-recurring">
    <label for="a-manual-recurring">I can identify at least three recurring tasks I currently do manually that could be automated.<br><span class="assess-hint">Think about what you do every day or week that follows the same steps each time.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-edge-cases">
    <label for="a-edge-cases">I know what happens when my current systems encounter an unusual situation or edge case.<br><span class="assess-hint">Do they handle it gracefully, require manual intervention, or just break?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Simplicity</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-tool-count">
    <label for="a-tool-count">I can list every tool and app I use for personal organisation and productivity.<br><span class="assess-hint">Count them. Is it a small, deliberate set, or have you accumulated dozens over the years?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-explain-system">
    <label for="a-explain-system">I could explain my organisational system to someone else in under five minutes.<br><span class="assess-hint">If it would take longer, or if you are not sure you could explain it at all, that is useful information.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-abandoned-tools">
    <label for="a-abandoned-tools">I know how many tools or systems I have tried and abandoned in the past two years.<br><span class="assess-hint">Apps you downloaded and stopped using, notebooks you started and forgot, systems you set up and never maintained.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Reliability</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-backup-status">
    <label for="a-backup-status">I know whether my important files and data are backed up, and when the last backup ran.<br><span class="assess-hint">Photos, documents, passwords, financial records. Could you recover if your computer died today?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-system-failures">
    <label for="a-system-failures">I can recall the last time one of my systems failed or required unplanned maintenance.<br><span class="assess-hint">An automation that stopped working, a tool that updated and broke your workflow, data you could not find.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-single-points">
    <label for="a-single-points">I know whether any of my systems have single points of failure.<br><span class="assess-hint">If one tool, device, or account were lost, would your whole system collapse?</span></label>
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

<p>You now understand why systems matter, what different people get out of them, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about power, simplicity, and reliability. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/systems/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Systems Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Systems. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/systems/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'systems';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-automation-count', 'a-manual-recurring', 'a-edge-cases',
        'a-tool-count', 'a-explain-system', 'a-abandoned-tools',
        'a-backup-status', 'a-system-failures', 'a-single-points'
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
