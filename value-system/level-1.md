---
layout: default
title: "Value System – Level 1: Awareness"
life_area_slug: value-system
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

<h1>Value System: Level 1</h1>

<p class="l1-subtitle">Understand what a value system is, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Value System Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why your value system matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Most people operate from values they absorbed in childhood &ndash; from family, religion, peer groups, and culture &ndash; without ever examining whether those values are genuinely theirs. Research on <a href="https://www.britannica.com/science/Lawrence-Kohlbergs-stages-of-moral-development" target="_blank">moral development</a> suggests only 10 &ndash; 15% of adults reason from consciously examined principles rather than social convention.</p>

<p>The practical cost of unexamined values is substantial. People without clear priorities tend to experience more <a href="https://www.apa.org/news/press/releases/stress" target="_blank">decision fatigue</a>, more regret after major choices, and a persistent sense that they are living someone else's life. Clarifying your values does not guarantee good outcomes, but it does mean your decisions reflect what you actually care about rather than what you were told to care about.</p>

<p>Values work also affects how you handle pressure. Studies on <a href="https://doi.org/10.1177/0146167211436733" target="_blank">self-affirmation theory</a> show that people who can articulate their core values are measurably more resilient under stress, less defensive when receiving critical feedback, and better able to maintain their priorities when circumstances shift.</p>

<p>Perhaps most importantly, a clear value system gives you a basis for saying no. Without one, you tend to default to whatever is most urgent, most socially rewarded, or most comfortable &ndash; none of which reliably track what matters most.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about a value system</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People do values work for different reasons. This site scores every value system intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Practical Decision-Making</h3>
<p>Having a values framework that actively improves daily choices and major life decisions. People who lean towards this value want clear guidance that reduces decision fatigue and increases confidence in choices. They treat values as stable inputs to efficient decision processes &ndash; tools for resource allocation, career moves, and life direction.</p>

<h3>Comprehensive Insight</h3>
<p>Deep understanding of your authentic values, including recognising inherited versus genuine values, understanding value hierarchies and trade-offs, and knowing when enough is enough for different values. People who lean towards this value focus on thorough discovery and analysis &ndash; achieving clarity about what truly matters and why.</p>

<h3>Authentic Expression</h3>
<p>The courage to live in alignment with your discovered values even when they conflict with social expectations, family pressure, or external incentives. People who lean towards this value prioritise congruence between inner beliefs and outer behaviour &ndash; being true to themselves over efficiency or social approval.</p>

<h3>Values Evolution</h3>
<p>Viewing values as potentially changeable and being open to intentional value development through new experiences, reflection, and life transitions. People who lean towards this value treat values work as ongoing growth rather than one-time discovery, regularly reassessing whether current values still serve them.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each value system value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Practical Decision-Making &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Charlie_Munger" target="_blank">Charlie Munger</a> built his investment career around a set of explicit mental models and decision-making principles that he maintained for over 60 years. He kept a checklist of cognitive biases to guard against, publicly turned down investments that violated his principles regardless of profit potential, and repeatedly described his approach as "invert, always invert" &ndash; testing every decision against what could go wrong. His partnership with Warren Buffett appears to have been grounded in shared values more than shared strategy.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Comprehensive Insight &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Derek_Parfit" target="_blank">Derek Parfit</a> spent his career at Oxford examining the foundations of ethics and personal identity. His book <em>Reasons and Persons</em> (1984) systematically dismantled common assumptions about self-interest, rationality, and what makes a life go well. Colleagues consistently described him as someone whose philosophical conclusions visibly shaped his daily conduct &ndash; he lived with unusual frugality, gave away a large share of his income, and appeared to treat the examined life as a genuine practice rather than an academic exercise.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Authentic Expression &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Václav_Havel" target="_blank">V&aacute;clav Havel</a> spent two decades as a dissident playwright in communist Czechoslovakia, repeatedly imprisoned for writing and speaking according to his values. His 1978 essay "The Power of the Powerless" argued that living authentically &ndash; refusing to participate in official lies &ndash; was itself a political act. When the regime fell in 1989, he became president, applying the same principles to governance. His consistency between private conviction and public action across dramatically different circumstances is well documented.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Values Evolution &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Mahatma_Gandhi" target="_blank">Mahatma Gandhi</a> revised his values publicly and repeatedly over a 50-year period. He started as a conventional lawyer seeking acceptance within the British Empire, adopted nonviolent resistance after experiences in South Africa, and later evolved his views on caste, religion, and economic organisation as his understanding deepened. His autobiography, <em>The Story of My Experiments with Truth</em>, frames his life explicitly as a process of testing and revising values through lived experience.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know straight away, others might take a few minutes of honest reflection. Tick each one once you've considered it (you don't need to enter the answer here, just confirm you've thought it through).</p>

<div class="assess-group">
<h4>Practical Decision-Making</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-core-values">
    <label for="a-core-values">I can name 3 &ndash; 5 values that I consider most important to me.<br><span class="assess-hint">These might include things like honesty, autonomy, compassion, achievement, security, creativity, or fairness.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-recent-decision">
    <label for="a-recent-decision">I can identify a recent major decision where I consciously considered my values.<br><span class="assess-hint">A career move, relationship choice, large purchase, or life change where you weighed what mattered most.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-decision-regret">
    <label for="a-decision-regret">I have a sense of whether I tend to feel confident or regretful after important decisions.<br><span class="assess-hint">Persistent regret often signals a gap between choices and underlying values.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Comprehensive Insight</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-inherited">
    <label for="a-inherited">I've thought about which of my values came from family or culture versus which I've consciously chosen.<br><span class="assess-hint">Consider religious beliefs, attitudes to money, views on success, or political leanings you grew up with.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-conflict">
    <label for="a-conflict">I can identify a situation where two of my values conflict with each other.<br><span class="assess-hint">For example, valuing both ambition and work-life balance, or both honesty and kindness.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-enough">
    <label for="a-enough">I have a sense of "enough" for at least one value &ndash; a point where pursuing it further stops adding to my wellbeing.<br><span class="assess-hint">For instance, knowing how much financial security is enough, or how much achievement satisfies you.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Authentic Expression</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-social-pressure">
    <label for="a-social-pressure">I can identify a situation where I acted against my values because of social pressure or fear of judgement.<br><span class="assess-hint">Times you went along with something you disagreed with, or stayed silent when you wanted to speak up.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-alignment">
    <label for="a-alignment">I have a rough sense of how well my daily life aligns with my stated values.<br><span class="assess-hint">Consider how you spend your time, money, and energy. Do those patterns reflect what you say matters?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Values Evolution</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-changed">
    <label for="a-changed">I can identify at least one value that has changed significantly since my early adulthood.<br><span class="assess-hint">Something you used to prioritise that you no longer do, or vice versa.</span></label>
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

<p>You now understand why a value system matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about practical decision-making, comprehensive insight, authentic expression, and values evolution. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/value-system/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Value System Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Value System. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/value-system/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'value-system';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-core-values', 'a-recent-decision', 'a-decision-regret',
        'a-inherited', 'a-conflict', 'a-enough',
        'a-social-pressure', 'a-alignment',
        'a-changed'
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
