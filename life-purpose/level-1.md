---
layout: default
title: "Life Purpose – Level 1: Awareness"
life_area_slug: life-purpose
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

<h1>Life Purpose: Level 1</h1>

<p class="l1-subtitle">Understand what life purpose means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Life Purpose Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why life purpose matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Having a clear sense of purpose is one of the strongest predictors of psychological wellbeing across cultures and age groups. The evidence connects purpose to outcomes in health, resilience, and overall life satisfaction.</p>

<p>People with a well-defined sense of purpose show <a href="https://psycnet.apa.org/record/2016-17273-001" target="_blank">roughly 40% greater resilience</a> during major life stressors, recovering more quickly from setbacks and maintaining perspective during difficulties. They also tend to score <a href="https://psycnet.apa.org/record/2009-05474-001" target="_blank">25 &ndash; 30% higher</a> on life satisfaction measures and report lower rates of depression and anxiety.</p>

<p>Purpose also affects physical health. A <a href="https://journals.sagepub.com/doi/10.1177/0956797619831612" target="_blank">meta-analysis of over 136,000 participants</a> found that having a strong sense of purpose was associated with reduced all-cause mortality. The mechanism likely involves better health behaviours, lower chronic stress, and stronger social connections &ndash; all of which tend to follow from purposeful living.</p>

<p>Perhaps most practically, purpose improves the quality of everyday decisions. When you know what matters to you, it becomes easier to evaluate opportunities, say no to distractions, and commit to long-term projects without constant second-guessing.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about life purpose</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People develop life purpose for different reasons. This site scores every life purpose intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Clarity &amp; Direction</h3>
<p>Having a clear sense of what you want to achieve and why it matters to you personally. Understanding your core motivations, having frameworks for major life decisions, and feeling confident about your chosen path. People who lean towards this value focus on reducing existential confusion, developing coherent long-term vision, and maintaining certainty about their direction even when circumstances change.</p>

<h3>Meaning &amp; Fulfilment</h3>
<p>The degree to which your life purpose provides deep satisfaction, emotional resonance, and a sense that your existence matters. Feeling that your goals are personally meaningful rather than externally imposed, experiencing regular fulfilment from working towards your purpose, and having a sense that your life has significance. People who lean towards this value seek purposes that genuinely inspire and motivate them.</p>

<h3>Integration &amp; Coherence</h3>
<p>How well your life purpose connects with and organises other aspects of your life &ndash; career, relationships, daily activities, and personal growth. Having a purpose that provides a unifying framework for life decisions, reduces internal conflict between different life domains, and creates synergy between various activities. People who lean towards this value want their purpose to serve as an organising principle that makes their whole life more coherent.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each life purpose value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Clarity &amp; Direction &ndash; Level 5</div>
    <p><a href="https://80000hours.org/about/#team" target="_blank">Benjamin Todd</a> co-founded 80,000 Hours at age 24 after concluding that career choice was the highest-leverage way most people could do good. He has spent over a decade refining and acting on that thesis, maintaining a consistent direction through organisational growth, public criticism, and shifts in the effective altruism movement. His written frameworks for career decisions are used by tens of thousands of people.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Meaning &amp; Fulfilment &ndash; Level 5</div>
    <p><a href="https://www.nobelprize.org/prizes/peace/2014/satyarthi/biographical/" target="_blank">Kailash Satyarthi</a> has worked to end child labour since the early 1980s, directly participating in the rescue of over 80,000 children from forced labour. He continued this work for decades before receiving the Nobel Peace Prize in 2014, sustaining motivation through legal battles, physical attacks, and the deaths of colleagues. His purpose appears to have been the primary organising force of his adult life.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Integration &amp; Coherence &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Yo-Yo_Ma" target="_blank">Yo-Yo Ma</a> has spent over 50 years as a cellist, but his career consistently reflects a broader purpose &ndash; using music to build connection across cultures. His Silk Road Ensemble brings together musicians from dozens of countries, his community concerts take place in settings from prisons to refugee camps, and his public statements frame music as a tool for empathy. His concert schedule, teaching, and advocacy all appear to serve a single coherent vision rather than separate professional tracks.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes of reflection. Tick each one once you've considered it (you don't need to enter the answer here, just confirm you've thought it through).</p>

<div class="assess-group">
<h4>Clarity &amp; Direction</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-articulate-purpose">
    <label for="a-articulate-purpose">I've tried to articulate what I want my life to be about in one or two sentences.<br><span class="assess-hint">This doesn't need to be polished &ndash; even a rough attempt counts.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-decision-framework">
    <label for="a-decision-framework">I know whether I have a framework for making major life decisions, or whether I tend to decide based on what feels right in the moment.<br><span class="assess-hint">Think about your last major decision &ndash; moving, changing jobs, starting or ending a relationship. What guided it?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-direction-confidence">
    <label for="a-direction-confidence">I have a sense of how confident I feel about my current life direction &ndash; whether I feel on track, uncertain, or adrift.<br><span class="assess-hint">There's no right answer here. The point is noticing where you stand.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Meaning &amp; Fulfilment</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-fulfilment-sources">
    <label for="a-fulfilment-sources">I can identify the activities or contexts that give me the deepest sense of fulfilment.<br><span class="assess-hint">These might be professional, personal, creative, or relational. Think about when you feel most alive.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-meaning-vs-external">
    <label for="a-meaning-vs-external">I've considered whether my current goals feel personally meaningful or mainly driven by external expectations.<br><span class="assess-hint">External expectations include family pressure, social norms, or what seems impressive to others.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-setback-motivation">
    <label for="a-setback-motivation">I know how my motivation tends to respond during setbacks or difficult periods.<br><span class="assess-hint">Do you push through, lose interest, pivot, or go numb? All are common patterns worth noticing.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Integration &amp; Coherence</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-values-alignment">
    <label for="a-values-alignment">I've assessed whether my daily activities broadly align with what I say matters to me.<br><span class="assess-hint">Compare how you spend a typical week with what you'd list as your top priorities.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-domain-conflict">
    <label for="a-domain-conflict">I know whether different areas of my life (work, relationships, personal projects) feel like they support each other or compete for time and energy.<br><span class="assess-hint">Conflict between domains is extremely common &ndash; the point is noticing the pattern.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-purpose-decisions">
    <label for="a-purpose-decisions">I can recall whether I've ever made a significant life decision based on purpose or values rather than convenience, money, or default expectations.<br><span class="assess-hint">This could be a career change, a move, ending something comfortable, or starting something risky.</span></label>
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

<p>You now understand why life purpose matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about clarity and direction, meaning and fulfilment, and integration and coherence. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/life-purpose/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Life Purpose Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Life Purpose. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/life-purpose/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'life-purpose';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-articulate-purpose', 'a-decision-framework', 'a-direction-confidence',
        'a-fulfilment-sources', 'a-meaning-vs-external', 'a-setback-motivation',
        'a-values-alignment', 'a-domain-conflict', 'a-purpose-decisions'
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
