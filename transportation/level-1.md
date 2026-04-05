---
layout: default
title: "Transportation – Level 1: Awareness"
life_area_slug: transportation
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

<h1>Transportation: Level 1</h1>

<p class="l1-subtitle">Understand what transportation means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Transportation Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why transportation matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>How you get around each day is one of those things most people accept as fixed rather than actively design. Yet transportation consumes a significant share of both your time and money, and the choices you make about it affect your health, stress levels, and overall quality of life.</p>

<p>Average commute times range from <a href="https://link.springer.com/article/10.1007/s11116-019-09983-9" target="_blank">40 to 80 minutes per day</a>, and transportation is typically the second-largest household expense after housing. Many people spend 15 – 20% of their income on getting around.</p>

<p>The mode you choose matters more than you might expect. Research consistently shows that <a href="https://www.sciencedirect.com/science/article/pii/S0965856420305620" target="_blank">active commuters – walkers and cyclists – report the highest satisfaction</a>, while long car and public transit commutes generate the lowest. Switching from car travel to active travel shows <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4262577/" target="_blank">significant positive effects on psychological wellbeing</a>.</p>

<p>Unlike many life areas, transportation can often be substantially improved through a single decision: moving closer to work, changing commute mode, or restructuring errand patterns. Few other changes deliver such a large daily quality-of-life improvement for a one-off effort.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about transportation</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach transportation for different reasons. This site scores every transportation intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Efficiency</h3>
<p>Minimising the time, money, and cognitive effort spent on transportation. People who lean towards this value treat transportation as a resource to optimise – reducing unnecessary trips, batching errands, choosing modes that maximise productive or enjoyable use of travel time, and structuring their lives to minimise wasted transit.</p>

<h3>Comfort</h3>
<p>The physical and psychological experience of your daily transportation – pleasant, stress-free, and compatible with your preferences. People who lean towards this value invest in making the journey itself enjoyable: vehicle quality, commute environment, protection from weather, and the overall pleasantness of their travel experience.</p>

<h3>Safety</h3>
<p>Minimising the risk of injury, accident, or incident during transportation. People who lean towards this value make travel decisions based on risk reduction: vehicle safety features, route selection, defensive driving or cycling practices, and choosing modes with strong safety records.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each transportation value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Efficiency &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Chris_Boardman" target="_blank">Chris Boardman</a> is an Olympic gold medallist cyclist who became Greater Manchester's cycling and walking commissioner. He commutes by bike, uses public transport, and has structured his own daily travel around efficiency rather than speed. His advocacy for active transport infrastructure is grounded in his personal practice &ndash; he has said he does not own a car and designs his life around not needing one.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Comfort &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Doug_DeMuro" target="_blank">Doug DeMuro</a> has built a career around evaluating the comfort and experience of vehicles across every price range. He owns and has personally tested hundreds of cars, and his detailed reviews focus heavily on ride quality, cabin environment, and the day-to-day experience of living with a vehicle. His approach treats every journey as an experience worth optimising.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Safety &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Tiff_Needell" target="_blank">Tiff Needell</a> is a former racing driver and long-time motoring presenter who has spent decades teaching advanced driving techniques to the public. His work on defensive and high-performance driving combines professional-level vehicle control with an emphasis on hazard anticipation and safe road behaviour, demonstrated across thousands of hours of on-road instruction.</p>
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
<h4>Efficiency</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-commute-time">
    <label for="a-commute-time">I know how long my daily commute takes, door to door.<br><span class="assess-hint">Include walking to and from your vehicle or station, waiting time, and any transfers.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-transport-cost">
    <label for="a-transport-cost">I know roughly how much I spend on transportation each month.<br><span class="assess-hint">Include fuel or fares, insurance, maintenance, parking, and any vehicle payments or depreciation.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-errand-pattern">
    <label for="a-errand-pattern">I know whether my errands are batched or spread across multiple separate trips.<br><span class="assess-hint">Think about grocery shopping, appointments, and other regular tasks that require travel.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Comfort</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-commute-experience">
    <label for="a-commute-experience">I have a sense of whether my daily commute feels pleasant, neutral, or stressful.<br><span class="assess-hint">Consider noise, crowding, temperature, traffic, and how you feel when you arrive.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-vehicle-condition">
    <label for="a-vehicle-condition">I know the condition and comfort level of my primary mode of transport.<br><span class="assess-hint">Whether it's a car, bicycle, bus, or train – is it well-maintained, comfortable, and reliable?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-weather-impact">
    <label for="a-weather-impact">I know how weather affects my transportation experience.<br><span class="assess-hint">Do rain, cold, or heat make your commute significantly worse? Do you have adequate protection?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Safety</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-risk-awareness">
    <label for="a-risk-awareness">I know the main safety risks associated with my current transportation modes.<br><span class="assess-hint">Accident rates for your mode, dangerous junctions on your route, or common hazards.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-safety-features">
    <label for="a-safety-features">I know what safety features my primary vehicle or mode has (and doesn't have).<br><span class="assess-hint">ABS, airbags, tyre condition, lights, reflective gear, helmet – whatever applies to your mode.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-defensive-habits">
    <label for="a-defensive-habits">I have a sense of whether I practise defensive habits when travelling.<br><span class="assess-hint">Consistent seat belt use, mirror checks, safe following distance, or cycling with lights and a helmet.</span></label>
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

<p>You now understand why transportation matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about efficiency, comfort, and safety. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/transportation/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Transportation Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Transportation. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/transportation/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'transportation';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-commute-time', 'a-transport-cost', 'a-errand-pattern',
        'a-commute-experience', 'a-vehicle-condition', 'a-weather-impact',
        'a-risk-awareness', 'a-safety-features', 'a-defensive-habits'
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
