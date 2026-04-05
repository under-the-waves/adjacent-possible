---
layout: default
title: "Community Contribution – Level 1: Awareness"
life_area_slug: community-contribution
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

<h1>Community Contribution: Level 1</h1>

<p class="l1-subtitle">Understand what community contribution means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Community Contribution Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why community contribution matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Community contribution &ndash; volunteering, neighbourhood involvement, and civic participation &ndash; produces measurable benefits for both the community and the contributor. A <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3890753/" target="_blank">meta-analysis of volunteering research</a> found that volunteers have lower rates of depression, higher life satisfaction, and a 22% reduction in mortality risk compared to non-volunteers.</p>

<p>The threshold for significant health benefits appears to be roughly <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3890753/" target="_blank">100 hours per year</a> &ndash; about 2 hours per week. Those who volunteer 200+ hours annually show a 40% reduction in hypertension risk. These findings hold after controlling for pre-existing health and socioeconomic status, suggesting a genuine causal relationship.</p>

<p>Beyond individual benefits, community contribution builds social capital &ndash; the networks of trust and reciprocity that make communities function. In an era where only <a href="https://americorps.gov/about/our-impact/volunteering-civic-life" target="_blank">23% of adults</a> formally volunteer, and neighbourhood social ties have weakened considerably, deliberate local involvement is both increasingly valuable and increasingly rare.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about community contribution</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People contribute to their communities for different reasons. This site scores every community contribution intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Impact</h3>
<p>Making a measurable, tangible difference in your community through your contributions. Choosing high-leverage volunteer activities, leading projects that produce real outcomes, and evaluating whether your community work is actually improving things rather than just filling time. People who lean towards this value focus on results.</p>

<h3>Belonging</h3>
<p>Feeling genuinely connected to and part of your local community through shared participation. Knowing your neighbours, being recognised as a community member, participating in local traditions, and experiencing the sense of home that comes from mutual investment. People who lean towards this value see community contribution as building their own roots.</p>

<h3>Fulfilment</h3>
<p>The personal satisfaction and meaning derived from contributing to community life. Volunteering in ways that energise you, finding purpose in service, and ensuring community work is a source of joy rather than obligation. People who lean towards this value seek contributions that nourish them as well as the community.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each community contribution value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Impact &ndash; Level 5</div>
    <p><a href="https://www.habitat.org/about/history" target="_blank">Millard Fuller</a> co-founded Habitat for Humanity in 1976, which has since built or repaired over 800,000 homes worldwide, providing shelter for more than 4 million people. He pioneered the "economics of Jesus" model &ndash; no-interest mortgage loans funded by donations and volunteer labour &ndash; proving that community-led housing construction could be scaled globally. His measurable impact on housing security transformed the volunteer construction sector.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Belonging &ndash; Level 5</div>
    <p><a href="https://www.incredibleedible.org.uk/what-we-do/" target="_blank">Pam Warhurst</a> co-founded Incredible Edible Todmorden in 2008, transforming unused public spaces in a small West Yorkshire town into community food-growing plots. The initiative spread to over 100 groups worldwide. By inviting anyone to plant, tend, and harvest food in shared spaces, she turned food growing into a vehicle for neighbourhood connection, making Todmorden measurably more cohesive according to local surveys.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Fulfilment &ndash; Level 5</div>
    <p><a href="https://www.maggiescentres.org/about-us/how-maggies-started/" target="_blank">Maggie Keswick Jencks</a> was diagnosed with cancer in 1988 and spent her remaining years designing a new model of cancer care based on her own experience of what patients need &ndash; not just treatment but warmth, information, and human connection. The first Maggie's Centre opened in Edinburgh in 1996, and there are now over 20 centres across the UK. She described the work as the most meaningful thing she had ever done.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to think about. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've found it out).</p>

<div class="assess-group">
<h4>Impact</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-volunteer-hours">
    <label for="a-volunteer-hours">I know roughly how many hours per month I spend on community activities or volunteering.<br><span class="assess-hint">Include formal volunteering, informal helping, neighbourhood activities, and civic participation.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-local-orgs">
    <label for="a-local-orgs">I can name at least three community organisations or volunteer opportunities in my area.<br><span class="assess-hint">Food banks, neighbourhood associations, school boards, environmental groups, sports clubs, etc.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-skills-match">
    <label for="a-skills-match">I have a sense of whether my current community contributions leverage my professional skills or could be done by anyone.<br><span class="assess-hint">Skills-based volunteering &ndash; using your expertise for a cause &ndash; tends to produce significantly more impact per hour.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Belonging</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-neighbours">
    <label for="a-neighbours">I know my immediate neighbours by name.<br><span class="assess-hint">On both sides and across the road, if applicable. Only 26% of adults know most of their neighbours.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-local-events">
    <label for="a-local-events">I know whether I attend any regular community events, meetings, or gatherings.<br><span class="assess-hint">Parish council meetings, community markets, neighbourhood clean-ups, local festivals, etc.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-rootedness">
    <label for="a-rootedness">I have a sense of how rooted I feel in my local area &ndash; whether it feels like home or just where I happen to live.<br><span class="assess-hint">Rootedness is partly about time spent in a place, but mostly about relationships and shared investment.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Fulfilment</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-enjoy-volunteering">
    <label for="a-enjoy-volunteering">I know whether my current community involvement energises me or drains me.<br><span class="assess-hint">Some people volunteer out of guilt or obligation. Others genuinely look forward to it. Both are common.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-purpose">
    <label for="a-purpose">I have a sense of whether contributing to my community is an important part of my identity or something I rarely think about.<br><span class="assess-hint">There's no wrong answer &ndash; the question is whether you've reflected on it.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-barriers">
    <label for="a-barriers">I can identify the main barriers to greater community involvement in my life, if any.<br><span class="assess-hint">Time, energy, social anxiety, not knowing where to start, feeling like an outsider &ndash; all are common.</span></label>
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

<p>You now understand why community contribution matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about impact, belonging, and fulfilment. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/community-contribution/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Community Contribution Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Community Contribution. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/community-contribution/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'community-contribution';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-volunteer-hours', 'a-local-orgs', 'a-skills-match',
        'a-neighbours', 'a-local-events', 'a-rootedness',
        'a-enjoy-volunteering', 'a-purpose', 'a-barriers'
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
