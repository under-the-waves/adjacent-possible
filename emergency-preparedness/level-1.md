---
layout: default
title: "Emergency Preparedness – Level 1: Awareness"
life_area_slug: emergency-preparedness
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

<h1>Emergency Preparedness: Level 1</h1>

<p class="l1-subtitle">Understand what emergency preparedness means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Emergency Preparedness Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why emergency preparedness matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Emergency preparedness is one of those areas where a relatively small investment of time and resources can make an outsized difference when it counts. The evidence suggests that prepared households fare substantially better during crises across virtually every measurable dimension.</p>

<p>Studies from <a href="https://www.fema.gov/emergency-managers/national-preparedness/report" target="_blank">FEMA's National Household Survey</a> consistently find that households with emergency plans and supplies experience less financial strain, faster recovery times, and reduced need for external assistance during emergencies. Prepared households also tend to report <a href="https://doi.org/10.1016/j.ijdrr.2019.101348" target="_blank">lower psychological distress</a> both during and after disaster events.</p>

<p>Community-level preparedness appears to create multiplying effects beyond individual households. Neighbourhoods with higher preparedness participation rates tend to experience faster emergency response, more effective resource sharing, and stronger social cohesion during crises. Even basic coordination among neighbours – knowing who has medical training, who has a generator, who might need help evacuating – can meaningfully improve outcomes.</p>

<p>Perhaps most notably, the gap between "unprepared" and "minimally prepared" is where the largest gains seem to lie. Roughly half of Americans lack a basic household emergency plan, which means that even modest preparation places you well ahead of the general population.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about emergency preparedness</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue preparedness for different reasons. This site scores every emergency preparedness intervention across four core values. Later, you'll set your own weighting across these values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Self-Reliance</h3>
<p>Building personal and family capability to handle emergencies independently. People who lean towards this value focus on stockpiling resources, learning practical skills like first aid and basic repairs, and ensuring their household can function autonomously when normal support systems fail.</p>

<h3>Community Resilience</h3>
<p>Developing collective preparedness through social networks, mutual aid, and coordinated community response. People who lean towards this value focus on strengthening social bonds, organising neighbourhood preparedness efforts, and building trust networks that can mobilise quickly during emergencies.</p>

<h3>Baseline Resilience</h3>
<p>Concentrating on probable, manageable disruptions – regional natural disasters, infrastructure failures, economic downturns, temporary supply chain interruptions. People who lean towards this value focus on realistic scenarios they are likely to face, ensuring solid preparation for events that occur regularly in their region.</p>

<h3>Catastrophic Resilience</h3>
<p>Preparing for rare but potentially civilisation-altering scenarios – global pandemics, economic collapse, technological failures affecting critical infrastructure, or societal breakdown. People who lean towards this value invest significant resources in scenarios that might require extended self-sufficiency or adaptation to entirely new social conditions.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each preparedness value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Self-Reliance &ndash; Level 5</div>
    <p><a href="https://www.chelseagreen.com/writer/ben-falk/" target="_blank">Ben Falk</a> is a designer, builder, and land steward who has spent over two decades developing a 10-acre homestead in Vermont designed for long-term self-sufficiency. His property includes year-round food production, multiple water systems, renewable energy infrastructure, and perennial agriculture – all documented in his book <em>The Resilient Farm and Homestead</em>. He maintains the capacity to sustain his household independently for extended periods through integrated systems he has built and refined over years.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Community Resilience &ndash; Level 5</div>
    <p><a href="https://www.intoresilience.net/" target="_blank">Daniel Aldrich</a> is a political scientist who studies disaster recovery and social capital. His research across multiple disaster contexts – including the 2004 Indian Ocean tsunami, Hurricane Katrina, and the 2011 Fukushima disaster – has consistently found that community social networks are the strongest predictor of post-disaster recovery. He practises what he studies, maintaining deep mutual-aid networks across multiple communities and advising governments worldwide on community resilience strategies.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Baseline Resilience &ndash; Level 5</div>
    <p><a href="https://www.buildingscience.com/about-us" target="_blank">Joseph Lstiburek</a> is a building scientist and engineer who has spent decades designing homes and structures that withstand regional hazards – hurricanes, floods, extreme temperatures, and wildfire – whilst remaining energy-efficient and comfortable. His work with the Building Science Corporation has shaped building codes across North America, and his own properties serve as demonstrations of professional-grade resilience against the specific regional threats they face.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Catastrophic Resilience &ndash; Level 5</div>
    <p><a href="https://www.garrettonbain.com/" target="_blank">Garrett M. Bain</a> is a former nuclear weapons designer turned security consultant who advises on worst-case scenario preparedness. He has developed comprehensive frameworks for preparing individuals and organisations for civilisation-level disruptions, including nuclear events, pandemic collapse, and infrastructure failure. His approach combines military-grade planning methodology with practical household implementation across multiple contingency locations.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to look up or check. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've found it out).</p>

<div class="assess-group">
<h4>Self-Reliance</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-supplies">
    <label for="a-supplies">I know how many days of food and water my household currently has on hand.<br><span class="assess-hint">Count everything in your cupboards, fridge, and any stored supplies. Include water or the means to purify it.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-first-aid">
    <label for="a-first-aid">I know where my first aid kit is and whether it's adequately stocked.<br><span class="assess-hint">Check for basics: plasters, bandages, antiseptic, pain relief, any prescription medications. Note anything missing.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-skills">
    <label for="a-skills">I know which practical emergency skills I have and which I lack.<br><span class="assess-hint">Consider: basic first aid, CPR, fire extinguisher use, water shut-off, fuse box operation, basic cooking without power.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Community Resilience</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-neighbours">
    <label for="a-neighbours">I know my immediate neighbours well enough to ask for or offer help in an emergency.<br><span class="assess-hint">Could you knock on their door at 2 a.m. during a crisis? Do you know if any are elderly, disabled, or live alone?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-local-resources">
    <label for="a-local-resources">I know what emergency resources exist in my local area.<br><span class="assess-hint">Nearest hospital, fire station, emergency shelter, community centre. Do you know the non-emergency police number?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-contact-plan">
    <label for="a-contact-plan">I have a way to contact family members if mobile networks go down.<br><span class="assess-hint">An agreed meeting point, a landline number, an out-of-area contact person, or a backup communication method.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Baseline Resilience</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-regional-risks">
    <label for="a-regional-risks">I know the most likely natural disasters and infrastructure risks for my specific location.<br><span class="assess-hint">Flooding, storms, heatwaves, wildfires, earthquakes – what has actually happened in your area in the past decade?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-insurance">
    <label for="a-insurance">I know whether my insurance covers the most probable emergencies for my area.<br><span class="assess-hint">Check your home/contents insurance for flood, storm, and fire coverage. Note any exclusions or gaps.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-evac-plan">
    <label for="a-evac-plan">I know my evacuation routes and have thought about where I would go if I had to leave home quickly.<br><span class="assess-hint">Two routes out of your neighbourhood, a destination (friend, family, shelter), and what you'd grab in 10 minutes.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Catastrophic Resilience</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-cash">
    <label for="a-cash">I know how much cash I have accessible if electronic payments stop working.<br><span class="assess-hint">ATMs and card machines can go offline during power outages or cyberattacks. How many days of expenses could you cover in cash?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-documents">
    <label for="a-documents">I know where my critical documents are and whether I have copies stored separately.<br><span class="assess-hint">Passport, birth certificate, insurance policies, medical records. Do you have digital backups or copies at a second location?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-scenarios">
    <label for="a-scenarios">I have thought about what I would do during an extended disruption lasting several weeks or more.<br><span class="assess-hint">A major pandemic, prolonged power outage, or supply chain collapse. Even a rough mental plan counts.</span></label>
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

<p>You now understand why emergency preparedness matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about self-reliance, community resilience, baseline resilience, and catastrophic resilience. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/emergency-preparedness/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Emergency Preparedness Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Emergency Preparedness. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/emergency-preparedness/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'emergency-preparedness';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-supplies', 'a-first-aid', 'a-skills',
        'a-neighbours', 'a-local-resources', 'a-contact-plan',
        'a-regional-risks', 'a-insurance', 'a-evac-plan',
        'a-cash', 'a-documents', 'a-scenarios'
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
