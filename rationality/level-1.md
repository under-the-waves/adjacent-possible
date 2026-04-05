---
layout: default
title: "Rationality – Level 1: Awareness"
life_area_slug: rationality
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

<h1>Rationality: Level 1</h1>

<p class="l1-subtitle">Understand what rationality means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Rationality Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why rationality matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>The quality of your thinking shapes nearly every outcome in your life. Career choices, financial decisions, relationships, health habits &ndash; all of these depend on how well you reason under uncertainty, how accurately you model the world, and how reliably you can identify the best course of action.</p>

<p>Most people overestimate the accuracy of their beliefs and the quality of their decisions. Research on <a href="https://www.sciencedirect.com/science/article/pii/S0010028516300421" target="_blank">calibration</a> consistently shows that people's confidence in their judgements tends to exceed their actual accuracy. This gap between perceived and real reasoning ability is one of the most robust findings in psychology.</p>

<p>The good news is that reasoning skills are trainable. Studies from the <a href="https://goodjudgment.com/resources/the-good-judgment-project/" target="_blank">Good Judgment Project</a> found that relatively brief training in probabilistic thinking and bias recognition improved forecasting accuracy by around 30%. Participants who practised structured reasoning outperformed professional intelligence analysts with access to classified information.</p>

<p>Rationality also serves as a multiplier for other life areas. Better reasoning about nutrition evidence helps you eat well. Clearer thinking about financial risk helps you invest wisely. More accurate models of other people help you build stronger relationships. Few skills compound across as many domains.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about rationality</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People develop their thinking for different reasons. This site scores every rationality intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Accurate Beliefs</h3>
<p>Developing more accurate beliefs about how the world actually works. Better calibration (your confidence matching actual accuracy), making more accurate forecasts and predictions, updating appropriately when presented with new evidence, and building superior mental models and heuristics for navigating complexity. People who lean towards this value focus on the outcomes of thinking &ndash; actually having true beliefs and understanding reality correctly, even when the truth is inconvenient or uncomfortable.</p>

<h3>Effective Decision-Making</h3>
<p>Using clear thinking to achieve your actual goals across all life domains. Avoiding costly mistakes from cognitive biases, developing systematic approaches to complex choices, improving your track record of successful outcomes, and building effective models and heuristics for practical decision-making. People who lean towards this value see rationality as a practical toolkit for getting what they want more reliably and avoiding expensive errors in judgement.</p>

<h3>Intellectual Honesty</h3>
<p>Maintaining truthful reasoning processes and admitting uncertainty appropriately. Changing your mind when evidence warrants it, acknowledging the limits of your knowledge, following arguments where they lead even when conclusions are personally uncomfortable, and recognising when your reasoning is motivated by comfort rather than truth. People who lean towards this value focus on the process of thinking &ndash; maintaining genuine truth-seeking as important in itself, regardless of whether it leads to immediately better outcomes.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each rationality value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Accurate Beliefs &ndash; Level 5</div>
    <p><a href="https://www.gjopen.com/" target="_blank">The top superforecasters</a> from the Good Judgment Project consistently outperformed professional intelligence analysts by 30% or more, despite having no access to classified information. These individuals &ndash; ordinary people with no special credentials &ndash; achieved this through disciplined calibration, granular probability estimates, and systematic belief updating. Over four years of geopolitical forecasting tournaments funded by IARPA, the best of them maintained Brier scores that placed them in the top fraction of a percent of all participants.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Effective Decision-Making &ndash; Level 5</div>
    <p><a href="https://fs.blog/annie-duke/" target="_blank">Annie Duke</a> was one of the top female poker players in history, winning a World Series of Poker bracelet and over $4 million in tournament earnings. She later applied the same structured decision-making frameworks &ndash; expected value calculations, separating decision quality from outcome quality, pre-mortems &ndash; to advising organisations and writing on decision science. Her track record spans thousands of high-stakes decisions under genuine uncertainty, with verifiable outcomes.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Intellectual Honesty &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Douglas_Hofstadter" target="_blank">Douglas Hofstadter</a> has spent decades publicly grappling with questions about consciousness, cognition, and artificial intelligence, consistently revising his positions as evidence and arguments demanded. Despite his strong initial scepticism about AI systems replicating aspects of human thought, he has openly acknowledged being shaken by recent developments and has discussed the discomfort of confronting evidence that challenges his life's work. This willingness to sit with uncertainty on questions central to his identity is unusual among prominent intellectuals.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to reflect on. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've thought it through).</p>

<div class="assess-group">
<h4>Accurate Beliefs</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-calibration">
    <label for="a-calibration">I've thought about how often I'm right when I feel very confident about something.<br><span class="assess-hint">When you say "I'm 90% sure", are you actually right about 90% of the time? Most people are right considerably less often than their confidence suggests.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-predictions">
    <label for="a-predictions">I can identify a recent prediction I made (about anything) and whether it turned out to be accurate.<br><span class="assess-hint">This could be about work, politics, sports, relationships &ndash; any forward-looking claim you made.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-updating">
    <label for="a-updating">I can think of a belief I changed in the past year based on new evidence.<br><span class="assess-hint">This could be about anything &ndash; a factual claim, an opinion about a person, a view on how something works.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Effective Decision-Making</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-past-decisions">
    <label for="a-past-decisions">I can identify a significant decision I made in the past year and assess whether my process was sound.<br><span class="assess-hint">Think about how you made the decision, not just whether it worked out. Good processes sometimes produce bad outcomes and vice versa.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-frameworks">
    <label for="a-frameworks">I know whether I use any structured approach when facing important decisions.<br><span class="assess-hint">Pros/cons lists, decision matrices, seeking outside views, pre-mortems, expected value calculations &ndash; or nothing systematic at all.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-biases">
    <label for="a-biases">I can name at least one cognitive bias that has likely affected my decisions.<br><span class="assess-hint">Sunk cost fallacy, confirmation bias, anchoring, status quo bias &ndash; or perhaps you're not sure what these terms mean yet. Either answer is fine.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Intellectual Honesty</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-motivated">
    <label for="a-motivated">I've considered whether there are topics where I might hold beliefs because they're comforting rather than because the evidence supports them.<br><span class="assess-hint">Politics, religion, career choices, relationships &ndash; areas where being wrong would be personally costly or uncomfortable.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-disagreement">
    <label for="a-disagreement">I have a sense of how I typically react when someone disagrees with me on something I care about.<br><span class="assess-hint">Do you get defensive? Curious? Dismissive? Do you engage with their actual argument or focus on finding flaws?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-uncertainty">
    <label for="a-uncertainty">I can identify an important question where I genuinely don't know the answer and am comfortable saying so.<br><span class="assess-hint">This is harder than it sounds. Most people have opinions on most topics, even when the evidence is genuinely unclear.</span></label>
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

<p>You now understand why rationality matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about accurate beliefs, effective decision-making, and intellectual honesty. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/rationality/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Rationality Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Rationality. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/rationality/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'rationality';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-calibration', 'a-predictions', 'a-updating',
        'a-past-decisions', 'a-frameworks', 'a-biases',
        'a-motivated', 'a-disagreement', 'a-uncertainty'
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
