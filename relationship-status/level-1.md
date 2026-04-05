---
layout: default
title: "Relationship Status – Level 1: Awareness"
life_area_slug: relationship-status
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

<h1>Relationship Status: Level 1</h1>

<p class="l1-subtitle">Understand what relationship status means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Relationship Status Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why relationship status matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your relationship status &ndash; whether you are single, dating, or in a committed partnership &ndash; is one of the most consequential aspects of your life. But the quality of your decisions around it matters far more than the status itself.</p>

<p>A <a href="https://www.pnas.org/doi/10.1073/pnas.1917036117" target="_blank">machine-learning analysis</a> of 43 longitudinal couple studies (11,196 couples) found that relationship-specific perceptions at the outset &ndash; perceived commitment, appreciation, sexual satisfaction &ndash; predicted relationship quality far more than individual traits or partner characteristics. In other words, who you choose matters more than how hard you try to make it work afterwards.</p>

<p>At the same time, <a href="https://psycnet.apa.org/record/2013-36062-001" target="_blank">research on fear of being single</a> shows it consistently predicts settling for less responsive and less attractive partners, greater dependence in unsatisfying relationships, and lower selectivity during dating &ndash; even after controlling for attachment anxiety. Many people stay in relationships far longer than they should because leaving feels harder than staying.</p>

<p>And being single is not the deficit it is often assumed to be. <a href="https://journals.sagepub.com/doi/10.1177/02654075231197728" target="_blank">Comparative research</a> finds that singles and couples have overlapping ranges of happiness, and that the strongest predictors of life satisfaction for single people are the same as for everyone: strong friendships, high self-esteem, and low stress.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about relationship status</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach relationship status for different reasons. This site scores every relationship-status intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Partner Selection</h3>
<p>Choosing well: understanding what you genuinely need in a partner vs. what you think you want. Evaluating compatibility effectively, recognising red flags early, and avoiding common selection biases like prioritising excitement over stability. People who lean towards this value invest in self-knowledge and dating skills before committing.</p>

<h3>Independence</h3>
<p>Being comfortable and fulfilled without a romantic partner. Building a rich single life, resisting social pressure to couple up, and knowing when being single is the right choice. People who lean towards this value ensure their happiness does not depend on relationship status.</p>

<h3>Transition Navigation</h3>
<p>Managing romantic transitions gracefully &ndash; entering relationships deliberately, leaving when needed, and processing breakups constructively. People who lean towards this value develop emotional resilience and decision-making skills around relationship changes, recovering quickly and extracting lessons rather than repeating patterns.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each relationship-status value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Partner Selection &ndash; Level 5</div>
    <p><a href="https://www.obamalibrary.gov/obamas/michelle-obama" target="_blank">Michelle Robinson</a> has spoken extensively about her deliberate approach to choosing a partner. When she met Barack Obama, she was his mentor at a law firm and initially resisted dating him. She assessed their compatibility across values, ambition, and family orientation over months before committing. In interviews and in her memoir <em>Becoming</em>, she describes evaluating whether he would be a genuine partner in domestic life and parenting &ndash; not just a charismatic match &ndash; and negotiating expectations before marriage. The result was a partnership that has weathered extraordinary public pressure for over 30 years.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Independence &ndash; Level 5</div>
    <p><a href="https://dfranceschi.medium.com/" target="_blank">Diane Franceschi</a>, a retired NYPD detective, spent decades living alone by choice while building one of the most distinguished investigative careers in the department's history. She has spoken and written about constructing a rich life around deep friendships, professional purpose, and personal interests without treating singleness as a gap to fill. Her life demonstrates that relationship status can be fully decoupled from identity and fulfilment.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Transition Navigation &ndash; Level 5</div>
    <p><a href="https://terrycrews.com/" target="_blank">Terry Crews</a> and his wife Rebecca separated after he disclosed a pornography addiction that had damaged their marriage. Rather than letting the relationship end in acrimony or pretending nothing was wrong, Crews publicly took responsibility, entered intensive therapy, and the couple spent over a year in structured separation before reconciling. His account of that period &ndash; in his book <em>Manhood</em> and in interviews &ndash; describes navigating the transition with unusual emotional honesty, minimal blame, and genuine self-examination.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to reflect on. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've thought about it).</p>

<div class="assess-group">
<h4>Partner Selection</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-past-patterns">
    <label for="a-past-patterns">I can identify my own partner-selection patterns &ndash; what has attracted me in the past and which choices led to good or poor outcomes.<br><span class="assess-hint">Think about your last two or three relationships or significant interests. What drew you in?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-needs-vs-wants">
    <label for="a-needs-vs-wants">I can distinguish between what I genuinely need in a partner and what I find initially exciting but unimportant long-term.<br><span class="assess-hint">For example, shared values vs. physical type, or emotional availability vs. social status.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-red-flags">
    <label for="a-red-flags">I know which red flags I have previously overlooked or rationalised in partners.<br><span class="assess-hint">Common ones include inconsistency, contempt, unwillingness to compromise, or misaligned life goals.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Independence</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-single-comfort">
    <label for="a-single-comfort">I have an honest sense of how comfortable I am being single &ndash; whether it feels like a genuine choice or a problem to be solved.<br><span class="assess-hint">Consider whether you feel pressure from yourself, family, or society to be in a relationship.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-solo-fulfilment">
    <label for="a-solo-fulfilment">I know whether my daily life &ndash; friendships, hobbies, mental health &ndash; is fulfilling independently of my relationship status.<br><span class="assess-hint">Would your life feel meaningfully emptier without a partner, or roughly the same?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-fear-single">
    <label for="a-fear-single">I can recognise when fear of being alone (rather than genuine desire) is driving my relationship decisions.<br><span class="assess-hint">Have you ever stayed in or entered a relationship primarily because being single felt worse?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Transition Navigation</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-breakup-speed">
    <label for="a-breakup-speed">I know how long I typically stay in a relationship after recognising it is not working.<br><span class="assess-hint">Weeks, months, or years? Some people leave quickly; others stay for years past the point of knowing.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-recovery-time">
    <label for="a-recovery-time">I have a sense of how long it takes me to recover emotionally from a breakup.<br><span class="assess-hint">Research suggests most people return to baseline within about three months, but individual variation is large.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-transition-patterns">
    <label for="a-transition-patterns">I can identify my post-breakup patterns &ndash; whether I tend towards rumination, rebound relationships, avoidance, or constructive processing.<br><span class="assess-hint">Think about your last significant breakup. What did you actually do in the weeks that followed?</span></label>
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

<p>You now understand why relationship status matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about partner selection, independence, and transition navigation. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/relationship-status/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Relationship Status Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Relationship Status. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/relationship-status/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'relationship-status';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-past-patterns', 'a-needs-vs-wants', 'a-red-flags',
        'a-single-comfort', 'a-solo-fulfilment', 'a-fear-single',
        'a-breakup-speed', 'a-recovery-time', 'a-transition-patterns'
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
