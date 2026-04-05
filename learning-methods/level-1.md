---
layout: default
title: "Learning Methods – Level 1: Awareness"
life_area_slug: learning-methods
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

<h1>Learning Methods: Level 1</h1>

<p class="l1-subtitle">Understand what learning methods means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Learning Methods Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why learning methods matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>How you learn determines how quickly you grow in every other area of life. The techniques you use to study, practise, and retain information are a force multiplier: improve them once, and the benefits compound across everything you do.</p>

<p>The evidence for better methods is unusually clear. Spaced practice &ndash; spreading study sessions over time &ndash; produces <a href="https://link.springer.com/article/10.3758/s13421-010-0035-2" target="_blank">roughly double the long-term retention</a> of cramming, yet over 80% of people rate cramming as equally or more effective. Active recall &ndash; testing yourself rather than rereading &ndash; is <a href="https://www.science.org/doi/10.1126/science.1199327" target="_blank">one of the most effective study techniques</a> known, but most learners default to passive methods like highlighting and rereading.</p>

<p>The gap between typical and effective methods is large enough that switching techniques alone &ndash; without spending more time &ndash; can dramatically improve outcomes. Few other investments offer this kind of return: you don't need to work harder, just differently.</p>

<p>Beyond efficiency, learning how to learn well builds confidence, reduces the anxiety of tackling unfamiliar subjects, and makes it possible to adapt as the knowledge and skills the world demands continue to shift.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about learning methods</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue better learning methods for different reasons. This site scores every learning methods intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Efficiency & Speed</h3>
<p>Maximising learning outcomes per unit of time invested. People who lean towards this value focus on methods with proven time-to-competency ratios and systematic approaches that eliminate wasted effort. They want to learn more in less time.</p>

<h3>Depth & Mastery</h3>
<p>Achieving deep, transferable understanding rather than surface-level knowledge. People who lean towards this value prefer methods that sacrifice speed for comprehensive understanding and lasting expertise. They want to build robust mental models that enable creative application across contexts.</p>

<h3>Enjoyment & Motivation</h3>
<p>Learning approaches that maintain engagement and intrinsic motivation over time. People who lean towards this value choose techniques they can maintain consistently because they find the process inherently satisfying. They would keep learning even without external pressure.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each learning methods value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Efficiency & Speed &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Scott_Young_(author)" target="_blank">Scott Young</a> completed MIT's four-year computer science curriculum in 12 months using structured self-study, then learned four languages in a year by living in each country and applying targeted immersion techniques. His approach centres on identifying the highest-leverage study methods for each domain and eliminating low-return activity.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Depth & Mastery &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Josh_Waitzkin" target="_blank">Josh Waitzkin</a> became a national chess champion as a child, then switched to tai chi push hands and won a world championship in that discipline too. His book <em>The Art of Learning</em> describes a deliberate practice methodology built around identifying and internalising core principles deeply enough to transfer them across unrelated domains.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Enjoyment & Motivation &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Richard_Feynman" target="_blank">Richard Feynman</a> maintained a lifelong habit of learning for its own sake &ndash; picking locks, studying biology, learning to draw, playing bongo drums, and deciphering Mayan hieroglyphs alongside his physics work. He sustained deep curiosity across dozens of fields for over 40 years, driven almost entirely by the pleasure of figuring things out.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to think about. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've thought it through).</p>

<div class="assess-group">
<h4>Efficiency & Speed</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-study-methods">
    <label for="a-study-methods">I can name at least two study techniques I use regularly.<br><span class="assess-hint">E.g. rereading, highlighting, flashcards, practice problems, summarising, teaching someone else.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-spacing">
    <label for="a-spacing">I know whether I typically spread learning over multiple sessions or concentrate it into one sitting.<br><span class="assess-hint">Think about the last time you needed to learn something new. Did you revisit it over days, or cover it all at once?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-time-spent">
    <label for="a-time-spent">I have a rough sense of how many hours per week I spend intentionally learning something new.<br><span class="assess-hint">Count structured study, courses, deliberate practice &ndash; not passive consumption like scrolling or background listening.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Depth & Mastery</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-feedback">
    <label for="a-feedback">I know whether I regularly seek feedback on my learning or practise.<br><span class="assess-hint">This could be a teacher, mentor, test scores, recording yourself, or any way of checking whether you actually understand.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-connections">
    <label for="a-connections">I have a sense of whether I connect new information to what I already know, or tend to treat new topics as isolated.<br><span class="assess-hint">When you learn something, do you naturally think about how it relates to other things you know?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-weakness">
    <label for="a-weakness">I can identify at least one skill area where I actively work on specific weaknesses rather than just general practice.<br><span class="assess-hint">Deliberate practice means targeting what you find difficult, not repeating what you're already comfortable with.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Enjoyment & Motivation</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-enjoy-learning">
    <label for="a-enjoy-learning">I've thought about which types of learning I find energising and which I find draining.<br><span class="assess-hint">Reading vs doing, solo vs group, structured vs exploratory, short bursts vs long sessions.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-consistency">
    <label for="a-consistency">I know whether I can sustain a learning routine for more than a few weeks.<br><span class="assess-hint">Think about past attempts to learn something. Did you keep going, or did motivation fade?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-curiosity">
    <label for="a-curiosity">I can name at least one topic I've explored recently out of pure curiosity rather than necessity.<br><span class="assess-hint">Something you learned because you wanted to, not because you had to for work or school.</span></label>
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

<p>You now understand why learning methods matter, what different people get out of them, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about efficiency and speed, depth and mastery, and enjoyment and motivation. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/learning-methods/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Learning Methods Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Learning Methods. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/learning-methods/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'learning-methods';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-study-methods', 'a-spacing', 'a-time-spent',
        'a-feedback', 'a-connections', 'a-weakness',
        'a-enjoy-learning', 'a-consistency', 'a-curiosity'
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
