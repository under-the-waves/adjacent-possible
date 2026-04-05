---
layout: default
title: "Worldview – Level 1: Awareness"
life_area_slug: worldview
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

<h1>Worldview: Level 1</h1>

<p class="l1-subtitle">Understand what worldview means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Worldview Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why worldview matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your worldview &ndash; the collection of mental models, beliefs, and frameworks you use to interpret what happens around you &ndash; shapes nearly every significant decision you make. It determines which opportunities you notice, which risks you take seriously, and how well you predict what comes next.</p>

<p>Research on <a href="https://www.hup.harvard.edu/books/9780674975866" target="_blank">superforecasting</a> found that the best predictors share a common trait: they draw on broad, well-integrated knowledge rather than deep expertise in a single domain. People with well-developed worldviews were roughly <a href="https://goodjudgment.com/resources/the-superforecasters/" target="_blank">30% more accurate</a> at predicting geopolitical and economic events than intelligence analysts with access to classified information.</p>

<p>The practical consequences are substantial. Understanding basic economics helps you evaluate career decisions and financial choices. Knowing how political systems function lets you anticipate policy changes that affect your life. Familiarity with psychology helps you recognise when you are being manipulated &ndash; or when you are fooling yourself. A <a href="https://journals.sagepub.com/doi/10.1177/0956797611421206" target="_blank">2012 study</a> found that people with greater knowledge of how the world works were significantly less susceptible to conspiracy theories and misinformation.</p>

<p>Perhaps most importantly, a coherent worldview provides psychological grounding. People with well-examined beliefs about human nature, progress, and their place in the broader story tend to cope better with uncertainty and report greater life satisfaction. Your worldview is not just an intellectual exercise &ndash; it is the operating system your mind runs on.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about worldview</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People develop their worldviews for different reasons. This site scores every worldview intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Breadth</h3>
<p>Developing understanding across multiple domains that shape how the world works &ndash; history, economics, psychology, politics, culture, and technology. People who lean towards this value focus on seeing connections between different fields and avoiding the blind spots that come from narrow knowledge. They tend to favour comprehensive coverage over deep specialisation.</p>

<h3>Depth</h3>
<p>Building sophisticated, nuanced understanding within specific domains rather than surface-level familiarity. People who lean towards this value focus on mastering fewer areas thoroughly, understanding complex theories, and analysing subtle distinctions. They would rather know two subjects well enough to teach them than know ten subjects well enough to discuss them at a dinner party.</p>

<h3>Utility</h3>
<p>A worldview that enhances real-world decision-making, prediction, and practical navigation of complex situations. People who lean towards this value focus on understanding how systems actually work &ndash; not how they are supposed to work &ndash; and they tend to prioritise frameworks that improve their ability to achieve goals and avoid common mistakes.</p>

<h3>Meaning</h3>
<p>Developing understanding that provides psychological grounding, moral framework, and sense of purpose. People who lean towards this value focus on building coherent narratives about human nature, progress, and their place in the larger story. They want a worldview that offers stability and direction during uncertainty, not just analytical power.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each worldview value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Breadth &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Vaclav_Smil" target="_blank">Vaclav Smil</a> has published over 40 books spanning energy, food production, environmental change, economics, demographics, and technical innovation. His writing regularly integrates data from half a dozen disciplines in a single argument. Bill Gates has called him his favourite author, largely because Smil's analyses draw on a range of domains that few specialists can match. He holds no public office and runs no institute &ndash; the breadth of his published work is itself the evidence.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Depth &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/David_Deutsch" target="_blank">David Deutsch</a> is a physicist at Oxford who developed the quantum theory of computation and has written two books &ndash; <em>The Fabric of Reality</em> and <em>The Beginning of Infinity</em> &ndash; that attempt to unify physics, epistemology, evolution, and computation into a single explanatory framework. His work demonstrates an unusual depth of engagement with fundamental questions across multiple disciplines, sustained over several decades.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Utility &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Philip_Tetlock" target="_blank">Philip Tetlock</a> spent over 20 years tracking the accuracy of expert predictions and demonstrated that most experts performed barely better than chance. He then developed the Good Judgment Project, which identified ordinary people whose forecasting accuracy consistently exceeded that of intelligence analysts. His work on superforecasting has been adopted by intelligence agencies and investment firms as a practical framework for decision-making under uncertainty.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Meaning &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Wendell_Berry" target="_blank">Wendell Berry</a> has spent over 60 years farming, writing, and teaching from the same small farm in Henry County, Kentucky. His novels, essays, and poetry articulate a worldview built around land stewardship, community, and the limits of industrial progress &ndash; and he has lived according to those principles consistently, farming without a tractor for decades and refusing to own a computer. His worldview appears to be genuinely load-bearing in his daily decisions rather than a theoretical position.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to think through. Tick each one once you have an honest answer (you don't need to enter the answer here, just confirm you've considered it).</p>

<div class="assess-group">
<h4>Breadth</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-domains-map">
    <label for="a-domains-map">I can list the major domains that shape how the world works and identify which ones I know well versus which ones I'm largely ignorant about.<br><span class="assess-hint">Consider history, economics, psychology, politics, science, technology, philosophy, and culture.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-cross-domain">
    <label for="a-cross-domain">I can think of a recent situation where knowledge from one domain helped me understand something in a completely different domain.<br><span class="assess-hint">For example, understanding psychology helped you interpret a political event, or knowledge of history informed a business decision.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-blind-spots">
    <label for="a-blind-spots">I have identified at least two major domains where my understanding is superficial enough that I could easily be misled.<br><span class="assess-hint">Be honest &ndash; most people have significant gaps in economics, statistics, or geopolitics even if they follow the news.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Depth</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-deep-area">
    <label for="a-deep-area">I can identify at least one area where my knowledge goes beyond surface-level familiarity &ndash; where I understand underlying principles, not just conclusions.<br><span class="assess-hint">Could you explain why something works, not just that it does? Could you teach it to someone else?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-assumption-check">
    <label for="a-assumption-check">I have tested whether my understanding in a subject I consider myself knowledgeable about holds up under scrutiny.<br><span class="assess-hint">Have you read a serious book or taken a course in your area of interest, or is your knowledge mostly from articles and conversation?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-nuance">
    <label for="a-nuance">I can articulate the strongest arguments against my own views on at least one important topic.<br><span class="assess-hint">If you can't steelman the opposition, your understanding may be shallower than it feels.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Utility</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-decision-quality">
    <label for="a-decision-quality">I can think of a significant decision I made in the past year where my understanding of how systems work led to a better outcome.<br><span class="assess-hint">A career choice, financial decision, or navigating an institutional process, for instance.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-manipulation">
    <label for="a-manipulation">I can identify common manipulation tactics in advertising, politics, or social situations when I encounter them.<br><span class="assess-hint">Think about dark patterns online, rhetorical tricks in news coverage, or high-pressure sales tactics.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-prediction">
    <label for="a-prediction">I have a rough sense of how often my predictions about events turn out to be correct.<br><span class="assess-hint">Most people overestimate their predictive accuracy. Have you ever tracked your predictions?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Meaning</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-purpose">
    <label for="a-purpose">I have thought about whether my worldview gives me a sense of purpose and direction, or whether I feel adrift on larger questions.<br><span class="assess-hint">Do you have a framework for deciding what matters, or do you mostly react to whatever feels urgent?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-resilience">
    <label for="a-resilience">I have a sense of how well my worldview holds up during difficult periods &ndash; whether my beliefs provide stability or crumble under stress.<br><span class="assess-hint">Think about the last time something went seriously wrong. Did your understanding of the world help you cope?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-moral-framework">
    <label for="a-moral-framework">I can articulate the moral principles that guide my major decisions, and I know where those principles come from.<br><span class="assess-hint">Not everyone has a formal ethical system, but most people have implicit rules. Can you name yours?</span></label>
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

<p>You now understand why worldview matters, what different people get out of developing theirs, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about breadth, depth, utility, and meaning. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/worldview/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Worldview Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Worldview. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/worldview/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'worldview';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-domains-map', 'a-cross-domain', 'a-blind-spots',
        'a-deep-area', 'a-assumption-check', 'a-nuance',
        'a-decision-quality', 'a-manipulation', 'a-prediction',
        'a-purpose', 'a-resilience', 'a-moral-framework'
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
