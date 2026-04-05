---
layout: default
title: "Goals – Level 1: Awareness"
life_area_slug: goals
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

<h1>Goals: Level 1</h1>

<p class="l1-subtitle">Understand what goal-setting means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Goals Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why goals matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Goal-setting is one of the most validated interventions in behavioural science. <a href="https://psycnet.apa.org/record/2002-15790-003" target="_blank">Locke and Latham's research</a> across over 1,000 studies shows that specific, challenging goals improve outcomes by 10 – 25% compared to vague intentions or "do your best" instructions.</p>

<p>Yet the gap between knowing goals work and actually achieving them is enormous. <a href="https://news.scranton.edu/articles/2021/01/fac-norcross-stories.shtml" target="_blank">92% of goal-setters</a> never reach their goals, and 80% of New Year's resolutions are abandoned by February.</p>

<p>The difference is almost entirely about practice, not willpower. <a href="https://scholar.dominican.edu/psychology-faculty-conference-presentations/3/" target="_blank">Writing goals down</a> increases achievement by 42%. <a href="https://psycnet.apa.org/record/2015-52587-001" target="_blank">Monitoring progress weekly</a> significantly promotes attainment across a wide range of domains. Simple, well-evidenced practices dramatically shift the odds &ndash; but only about a third of goal-setters use any of them.</p>

<p>Goal-setting also shapes your sense of direction and meaning. People with clear goals report higher life satisfaction, greater sense of purpose, and more resilience when facing setbacks.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about goals</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach goal-setting for different reasons. This site scores every goals intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Follow-through</h3>
<p>Consistently completing what you set out to do &ndash; turning goals from intentions into accomplished outcomes. Maintaining momentum, tracking progress, building accountability, and developing the discipline to keep working when motivation fades. People who lean towards this value measure success by completion rate.</p>

<h3>Clarity</h3>
<p>Defining goals with enough precision that you know exactly what success looks like and can tell whether you are on track. Specific, measurable targets, clear deadlines, and unambiguous criteria for completion. People who lean towards this value believe that vague goals produce vague results.</p>

<h3>Adaptability</h3>
<p>Maintaining the ability to change course, adjust timelines, reprioritise, or abandon goals as new information emerges. Treating goals as hypotheses, running regular reviews, and developing the skill of strategic retreat without emotional cost. People who lean towards this value believe that adapting intelligently is more important than persisting stubbornly.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each goals value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Follow-through &ndash; Level 5</div>
    <p><a href="https://www.chrisclear.com/" target="_blank">Chris Nikic</a> became the first person with Down syndrome to complete an Ironman triathlon in 2020, at age 21. He trained for over a year using a system he calls "1% better every day" &ndash; small, trackable daily improvements toward an audacious goal. He has since completed multiple Ironmans and a marathon, each time following the same methodical, incremental approach to follow-through across multi-month timescales.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Clarity &ndash; Level 5</div>
    <p><a href="https://www.samuelthomasdavies.com/" target="_blank">Samuel Thomas Davies</a> is a behavioural scientist and author who publicly documents his goal-setting methodology, including specific measurable targets, weekly progress reviews, and annual retrospectives published in detail. His system treats goal clarity as a discipline &ndash; every goal has explicit success criteria, a deadline, and a tracking mechanism. He has maintained this practice consistently for over a decade.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Adaptability &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Sara_Blakely" target="_blank">Sara Blakely</a> spent two years developing Spanx while working full-time as a door-to-door fax machine salesperson. When her initial patent strategy failed, she rewrote the patent herself. When major retailers rejected her, she demonstrated the product in person at Neiman Marcus. She has spoken about treating each setback as information rather than failure, adjusting her approach without abandoning the goal. Spanx reached $400 million in revenue with no outside funding.</p>
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
<h4>Follow-through</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-current-goals">
    <label for="a-current-goals">I can list the goals I am currently working towards.<br><span class="assess-hint">Not aspirations or wishes &ndash; specific things you are actively pursuing right now.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-completion-rate">
    <label for="a-completion-rate">I have a rough sense of how many goals I've set in the past year and how many I actually completed.<br><span class="assess-hint">Even a rough estimate is useful &ndash; "most," "about half," or "almost none" all count.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-tracking">
    <label for="a-tracking">I know whether I currently track progress on my goals in any systematic way.<br><span class="assess-hint">A spreadsheet, journal, app, or regular review &ndash; or nothing at all.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Clarity</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-written">
    <label for="a-written">I know whether my goals are written down anywhere.<br><span class="assess-hint">Written goals are 42% more likely to be achieved than unwritten ones.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-measurable">
    <label for="a-measurable">I can say, for each of my current goals, exactly what "done" looks like.<br><span class="assess-hint">Could someone else look at the goal and tell you whether you've achieved it?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-deadlines">
    <label for="a-deadlines">I know whether my goals have deadlines attached.<br><span class="assess-hint">A specific date, not "someday" or "when I get round to it."</span></label>
</div>
</div>

<div class="assess-group">
<h4>Adaptability</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-abandoned">
    <label for="a-abandoned">I've thought about goals I've abandoned in the past and whether I made a deliberate decision to stop or just drifted away.<br><span class="assess-hint">There is an important difference between strategic retreat and quiet abandonment.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-review">
    <label for="a-review">I know whether I have any regular process for reviewing and adjusting my goals.<br><span class="assess-hint">Weekly, monthly, quarterly &ndash; or never.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-sunk-cost">
    <label for="a-sunk-cost">I've considered whether I tend to persist with goals that are no longer worth pursuing because of time already invested.<br><span class="assess-hint">Sunk-cost bias is one of the most common obstacles to intelligent goal management.</span></label>
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

<p>You now understand why goals matter, what different people get out of goal-setting, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about follow-through, clarity, and adaptability. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/goals/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Goals Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Goals. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/goals/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'goals';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-current-goals', 'a-completion-rate', 'a-tracking',
        'a-written', 'a-measurable', 'a-deadlines',
        'a-abandoned', 'a-review', 'a-sunk-cost'
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
