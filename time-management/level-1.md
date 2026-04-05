---
layout: default
title: "Time Management – Level 1: Awareness"
life_area_slug: time-management
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

<h1>Time Management: Level 1</h1>

<p class="l1-subtitle">Understand what time management means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Time Management Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why time management matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Time is the one resource you cannot earn more of. How you allocate it determines almost everything about the shape of your life &ndash; your career progress, your relationships, your health, and your sense of control.</p>

<p>A <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7799745/" target="_blank">meta-analysis of 158 studies</a> (n = 53,957) found that effective time management enhances life satisfaction more than job performance &ndash; the effect on life satisfaction was 72% stronger than on job satisfaction. Time management is not primarily a work skill; it is a life skill.</p>

<p>Research shows that <a href="https://www.timewatch.com/blog/time-management-statistics/" target="_blank">91% of people</a> who implement structured time management practices report reduced stress, and 94% report increased productivity. People who feel in control of their time report significantly better work-life balance, lower feelings of overload, and <a href="https://journals.sagepub.com/doi/full/10.1177/2158244018824506" target="_blank">less tension</a> than their peers.</p>

<p>Yet only 18% of people have any formal time management system, and just 5% use structured approaches like time blocking. Even basic practices place you well ahead of most people.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about time management</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People manage their time for different reasons. This site scores every time management intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Productivity & Achievement</h3>
<p>Maximising output and accomplishing meaningful goals efficiently. Getting more done in less time, meeting deadlines consistently, and making tangible progress on important projects. People who lean towards this value focus on systems and techniques that measurably increase their productive capacity.</p>

<h3>Balance & Wellbeing</h3>
<p>Creating sustainable rhythms that support long-term effectiveness while maintaining personal wellbeing. Managing energy levels, preventing burnout, maintaining boundaries between work and personal time, and ensuring time for rest and relationships. People who lean towards this value seek approaches that enhance both performance and life satisfaction.</p>

<h3>Flexibility & Responsiveness</h3>
<p>Maintaining the ability to adapt to changing priorities and unexpected demands while staying effective. Handling interruptions gracefully, pivoting between tasks smoothly, and remaining productive despite uncertainty. People who lean towards this value want systems that work across different contexts and can accommodate life's unpredictability.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each time management value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Productivity & Achievement &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Elon_Musk" target="_blank">Elon Musk</a> runs multiple companies simultaneously by scheduling his day in five-minute blocks and batching similar tasks together. Whatever one thinks of his other attributes, his time management output is verifiable: he has sustained CEO-level involvement across Tesla, SpaceX, and other ventures for over a decade. His system appears to be built around extreme scheduling discipline rather than delegation.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Balance & Wellbeing &ndash; Level 5</div>
    <p><a href="https://www.sarahknightbooks.com/" target="_blank">Sarah Knight</a> left a high-pressure publishing career in New York to redesign her life around sustainable work rhythms. She went on to write multiple bestselling books about prioritisation and boundary-setting while living in the Dominican Republic, maintaining what she describes as a deliberately structured schedule that protects time for relationships, rest, and enjoyment. Her work focuses specifically on the intersection of productivity and personal wellbeing.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Flexibility & Responsiveness &ndash; Level 5</div>
    <p><a href="https://www.oliverburkeman.com/" target="_blank">Oliver Burkeman</a> spent years as a productivity journalist before writing <em>Four Thousand Weeks</em>, a book that reframes time management around embracing finitude rather than maximising output. He maintains a writing career, family life, and speaking schedule while openly practising a flexible approach to planning that accommodates uncertainty. His system explicitly rejects rigid scheduling in favour of adaptable structures that work across changing circumstances.</p>
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
<h4>Productivity & Achievement</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-system">
    <label for="a-system">I can describe my current system for capturing and organising tasks.<br><span class="assess-hint">Do you use a to-do list, calendar, app, notebook, or nothing at all?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-completion">
    <label for="a-completion">I have a rough sense of what percentage of my planned tasks I actually complete in a typical week.<br><span class="assess-hint">Think about last week &ndash; how much of what you intended to do actually got done?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-peak">
    <label for="a-peak">I know when my peak performance hours are during the day.<br><span class="assess-hint">Morning, afternoon, or evening? When do you do your best focused work?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Balance & Wellbeing</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-boundaries">
    <label for="a-boundaries">I know whether I have clear boundaries between work time and personal time.<br><span class="assess-hint">Do you have a defined end to your work day, or does work bleed into evenings and weekends?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-breaks">
    <label for="a-breaks">I know how often I take breaks during focused work and whether I schedule them deliberately.<br><span class="assess-hint">Do you take regular breaks, or do you work until you're exhausted?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-protected">
    <label for="a-protected">I know whether I have protected time for relationships, health, and personal interests.<br><span class="assess-hint">Is time for these things scheduled, or do they only happen when work permits?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Flexibility & Responsiveness</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-interruptions">
    <label for="a-interruptions">I have a sense of how well I handle interruptions and unexpected tasks during the day.<br><span class="assess-hint">Do you recover quickly, or does an interruption derail your whole afternoon?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-reprioritise">
    <label for="a-reprioritise">I know how I currently respond when priorities shift mid-week.<br><span class="assess-hint">Do you adjust your plan, or do you try to do everything and end up overwhelmed?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-contexts">
    <label for="a-contexts">I've thought about whether my time management approach works across different contexts (work, home, travel).<br><span class="assess-hint">Does your system travel with you, or does it only work at your desk?</span></label>
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

<p>You now understand why time management matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about productivity and achievement, balance and wellbeing, and flexibility and responsiveness. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/time-management/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Time Management Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Time Management. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/time-management/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'time-management';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-system', 'a-completion', 'a-peak',
        'a-boundaries', 'a-breaks', 'a-protected',
        'a-interruptions', 'a-reprioritise', 'a-contexts'
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
