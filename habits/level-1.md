---
layout: default
title: "Habits – Level 1: Awareness"
life_area_slug: habits
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

<h1>Habits: Level 1</h1>

<p class="l1-subtitle">Understand what habit formation means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Habits Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why habits matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>About <a href="https://dornsife.usc.edu/assets/sites/545/docs/Wendy_Wood_Research_Articles/Habits/wood.quinn.kashy.2002_habits_in_everyday_life.pdf" target="_blank">40% of your daily actions</a> are performed habitually &ndash; not through conscious decision but through automatic routines triggered by context. Understanding and shaping these routines is one of the highest-leverage investments you can make in your life.</p>

<p>Once a habit is established, it persists even after conscious motivation fades. This is both the power and the danger of habits: good ones compound silently in the background, while bad ones drain your health, time, and relationships without requiring any deliberate choice on your part.</p>

<p>Research shows that habit formation takes <a href="https://onlinelibrary.wiley.com/doi/abs/10.1002/ejsp.674" target="_blank">18 to 254 days</a>, with an average of 66 days &ndash; far longer than the popular "21 days" myth suggests. Yet <a href="https://www.weforum.org/stories/2024/04/healthy-habit-formation-public-health/" target="_blank">77% of people</a> abandon new behaviours within a single week. The gap between wanting to change and actually embedding new habits is where most people get stuck.</p>

<p>Well-designed habits free mental resources for higher-level thinking. Every behaviour that becomes automatic is one fewer decision you need to make, reducing decision fatigue and creating capacity for the things that require your full attention.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about habits</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach habit formation for different reasons. This site scores every habits intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Impact</h3>
<p>Choosing and designing habits that create meaningful positive change in important life areas. Focusing on keystone habits that trigger other positive behaviours, aligning habits with personal values and goals, and ensuring habit choices deliver measurable benefits. People who lean towards this value want their habit energy invested in behaviours that create the greatest life improvement.</p>

<h3>Consistency</h3>
<p>Building habits that stick and perform reliably over time without constant conscious effort. Establishing routines that become automatic, maintaining behaviours even during difficult periods, and creating systems that work regardless of motivation levels. People who lean towards this value focus on habit durability and want behaviours that persist through life's ups and downs.</p>

<h3>Enjoyment</h3>
<p>Making habit formation and maintenance as pleasant and rewarding as possible. Choosing habits that feel intrinsically satisfying, designing routines that enhance daily experience, and creating positive associations with beneficial behaviours. People who lean towards this value seek habits that improve both outcomes and quality of life.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each habits value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Impact &ndash; Level 5</div>
    <p><a href="https://jamesclear.com/about" target="_blank">James Clear</a> spent years studying and practising habit formation before writing <em>Atomic Habits</em>, which has sold over 15 million copies. His personal system centres on identifying and stacking keystone habits &ndash; small behaviours that cascade into larger life improvements. He has maintained a consistent writing, fitness, and photography practice for over a decade, each habit deliberately chosen for its compound returns across multiple life areas.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Consistency &ndash; Level 5</div>
    <p><a href="https://www.jerryeinfeld.com/" target="_blank">Jerry Seinfeld</a> famously maintained a "don't break the chain" practice for joke-writing, marking a red X on a wall calendar every day he wrote new material. He sustained this daily writing habit across decades, through career changes, touring schedules, and life transitions. His consistency methodology has become one of the most widely cited examples of habit maintenance in popular psychology.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Enjoyment &ndash; Level 5</div>
    <p><a href="https://www.bfrb.org/storage/documents/Expert_consensus_guidelines2016w.pdf" target="_blank">BJ Fogg</a>, founder of the <a href="https://behaviordesign.stanford.edu/" target="_blank">Behavior Design Lab</a> at Stanford, developed the Tiny Habits method after two decades of research into what makes behaviours stick. His system emphasises celebration and positive emotion as the core mechanism of habit formation &ndash; deliberately engineering feelings of success and satisfaction after each repetition. He has personally maintained dozens of "tiny habits" for years, each designed to feel rewarding from the first day.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to reflect on. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've found it out).</p>

<div class="assess-group">
<h4>Impact</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-current-habits">
    <label for="a-current-habits">I can list the daily and weekly habits I currently maintain, both helpful and unhelpful.<br><span class="assess-hint">Think about your morning routine, work patterns, evening habits, and weekend routines.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-keystone">
    <label for="a-keystone">I've thought about which of my current habits have the biggest positive or negative ripple effects on other areas of my life.<br><span class="assess-hint">For example, does exercising in the morning make you more productive all day? Does staying up late make everything harder?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-habit-goals">
    <label for="a-habit-goals">I know whether my current habits are aligned with my most important goals and values.<br><span class="assess-hint">Are your daily routines actually moving you towards the things you say matter most?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Consistency</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-formation-time">
    <label for="a-formation-time">I have a sense of how long it typically takes me to form a new habit.<br><span class="assess-hint">Think about the last habit you successfully built &ndash; how long before it felt automatic?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-disruption">
    <label for="a-disruption">I know what tends to disrupt my habits &ndash; travel, stress, weekends, or changes in routine.<br><span class="assess-hint">Identifying your habit-breaking triggers is the first step to building more resilient routines.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-bad-habits">
    <label for="a-bad-habits">I can identify at least one habit I've tried and failed to break, and I have a sense of why it persisted.<br><span class="assess-hint">Understanding why unwanted habits stick helps you design better approaches to changing them.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Enjoyment</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-enjoy-habits">
    <label for="a-enjoy-habits">I've thought about which of my current habits I genuinely enjoy and which feel like a chore.<br><span class="assess-hint">Habits that feel rewarding are far more likely to persist than those maintained through willpower alone.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-cues">
    <label for="a-cues">I know whether I use any deliberate cues or triggers to prompt my habits.<br><span class="assess-hint">Linking a new habit to an existing routine (habit stacking) is one of the most effective formation techniques.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-rewards">
    <label for="a-rewards">I have a sense of whether my habits have built-in rewards or whether I rely on discipline to maintain them.<br><span class="assess-hint">Intrinsic rewards (the behaviour itself feels good) are more sustainable than extrinsic ones (doing it to earn something else).</span></label>
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

<p>You now understand why habits matter, what different people get out of habit formation, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about impact, consistency, and enjoyment. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/habits/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Habits Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Habits. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/habits/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'habits';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-current-habits', 'a-keystone', 'a-habit-goals',
        'a-formation-time', 'a-disruption', 'a-bad-habits',
        'a-enjoy-habits', 'a-cues', 'a-rewards'
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
