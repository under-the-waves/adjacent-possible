---
layout: default
title: "Children – Level 1: Awareness"
life_area_slug: children
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

<h1>Children: Level 1</h1>

<p class="l1-subtitle">Understand what parenting involves, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Children Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why parenting matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>The parent-child relationship is one of the most consequential human bonds. The quality of this relationship &ndash; not specific parenting techniques &ndash; is what predicts outcomes most strongly.</p>

<p>Cross-cultural research in <a href="https://www.nature.com/articles/s44271-024-00161-x" target="_blank">Communications Psychology (2024)</a> found that higher recalled parent-child relationship quality predicted adult flourishing and current mental health across a diverse group of countries. The foundations for lifelong wellbeing begin in the early years.</p>

<p>Quality of interaction matters more than quantity. Research in the <a href="https://pubmed.ncbi.nlm.nih.gov/37775429/" target="_blank">Journal of Developmental and Behavioral Pediatrics (2023)</a> found that insufficient parent-child quality time is associated with lower flourishing, and specific interactive activities like singing and storytelling drove the strongest outcomes.</p>

<p>Across <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4784487/" target="_blank">more than a thousand studies</a>, greater wellbeing is seen for children with higher combined parental care and lower combined parental psychological control. Warmth, responsiveness, and appropriate boundaries matter far more than any particular parenting method.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about parenting</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach parenting with different priorities. This site scores every parenting intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Wellbeing</h3>
<p>Supporting your child's overall physical, emotional, and psychological health. Creating a stable, nurturing environment, attending to mental health, ensuring adequate sleep and nutrition, and prioritising the child's current happiness alongside future outcomes. People who lean towards this value focus on the child thriving now, not just preparing for later.</p>

<h3>Relationship</h3>
<p>The quality of the parent-child bond &ndash; warmth, trust, communication, and genuine connection. Being emotionally available, enjoying time together, knowing your child's inner life, and building a relationship they want to maintain into adulthood. People who lean towards this value invest in connection as an end in itself.</p>

<h3>Achievement</h3>
<p>Supporting your child's cognitive, academic, and skill development. Structured enrichment, high expectations communicated warmly, and preparation for future success. People who lean towards this value believe parents should actively cultivate capability.</p>

<h3>Development</h3>
<p>Fostering independence, resilience, and character through age-appropriate challenges and progressively expanding autonomy. Allowing risk-taking, supporting self-direction, and building executive function. People who lean towards this value focus on who the child is becoming, not just what they can do.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each parenting value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Wellbeing &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Magda_Gerber" target="_blank">Magda Gerber</a> developed the Resources for Infant Educarers (RIE) approach, built around deep observation and respect for children's emotional states from birth. She raised her own three children using these principles before formalising them into a teaching methodology. Her approach &ndash; treating even very young children as full people whose emotional experiences deserve attention &ndash; produced measurably more secure attachment outcomes in the children of parents she trained, and her methods are now used in early childhood programmes across the world.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Relationship &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Barack_Obama" target="_blank">Barack Obama</a> maintained nightly family dinners throughout his presidency, rarely missing them even during major crises. He has spoken extensively about structuring his schedule around his daughters' school events, sports fixtures, and everyday conversations. Both Sasha and Malia Obama have described their father as deeply present and emotionally available despite the pressures of his role, and the family's closeness has remained visibly strong through their adult years.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Achievement &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/L%C3%A1szl%C3%B3_Polg%C3%A1r" target="_blank">L&aacute;szl&oacute; Polg&aacute;r</a> set out to test his theory that any child could reach exceptional levels in a chosen field with early, deliberate training. He and his wife Klara raised their three daughters &ndash; Susan, Sofia, and Judit &ndash; to become chess prodigies. All three became among the strongest female players in history, with Judit widely regarded as the greatest female chess player of all time. Polg&aacute;r documented his methods and the children's development in detail, and all three daughters have spoken positively about their upbringing.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Development &ndash; Level 5</div>
    <p><a href="https://letgrow.org/about/" target="_blank">Lenore Skenazy</a> became known as "America's worst mom" after writing about letting her nine-year-old son ride the New York subway alone. She went on to found the Let Grow movement, advocating for age-appropriate independence and unsupervised play. Her own children grew up with progressively expanded freedoms &ndash; navigating public transport, managing their own schedules, and solving problems without parental rescue &ndash; and she has documented how this approach built their confidence and self-direction over years.</p>
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
<h4>Wellbeing</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-emotional-climate">
    <label for="a-emotional-climate">I've reflected on the emotional climate of my home &ndash; whether my child generally feels safe to express both positive and negative emotions.<br><span class="assess-hint">Think about how your child behaves when upset, angry, or disappointed. Do they come to you or withdraw?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-sleep-nutrition">
    <label for="a-sleep-nutrition">I know whether my child is getting adequate sleep and nutrition for their age.<br><span class="assess-hint">Check NHS or WHO guidelines for age-appropriate sleep hours and nutritional needs.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-stress-signs">
    <label for="a-stress-signs">I can identify the signs my child shows when they are stressed or struggling.<br><span class="assess-hint">Common signs include changes in sleep, appetite, withdrawal, irritability, or regression to earlier behaviours.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Relationship</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-quality-time">
    <label for="a-quality-time">I know roughly how much one-on-one time I spend with my child in a typical week that involves genuine connection rather than logistics.<br><span class="assess-hint">Count time spent talking, playing, reading together, or doing shared activities &ndash; not transport, meals in front of screens, or homework supervision.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-inner-life">
    <label for="a-inner-life">I have a sense of my child's inner life &ndash; what they worry about, what excites them, and who their close friends are.<br><span class="assess-hint">Could you name your child's current best friend, their biggest worry, and something they're looking forward to?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-seeks-comfort">
    <label for="a-seeks-comfort">I know whether my child actively seeks me out for comfort and conversation, or tends to go elsewhere.<br><span class="assess-hint">Think about the last time your child was upset. Did they come to you first, go to another adult, or handle it alone?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Achievement</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-academic-level">
    <label for="a-academic-level">I know where my child stands relative to age expectations in their main academic or skill areas.<br><span class="assess-hint">This might come from school reports, teacher conversations, or your own observation of their reading, writing, and numeracy.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-enrichment">
    <label for="a-enrichment">I know whether my child has regular structured enrichment beyond school &ndash; reading together, skill-building activities, or academic challenges.<br><span class="assess-hint">Count activities you do together (reading, puzzles, projects) as well as formal clubs or tutoring.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-strengths-gaps">
    <label for="a-strengths-gaps">I can identify at least one area where my child is ahead of peers and one where they could benefit from more support.<br><span class="assess-hint">Think about academic subjects, social skills, motor skills, or practical capabilities.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Development</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-independence">
    <label for="a-independence">I've thought about where I might be over-directing my child's choices and where they could exercise more independent decision-making.<br><span class="assess-hint">Consider how many of your child's daily decisions &ndash; what to wear, what to eat, how to spend free time &ndash; they actually make themselves.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-consequences">
    <label for="a-consequences">I know whether my child experiences natural consequences for their choices, or whether I tend to step in and fix things.<br><span class="assess-hint">Think about the last time your child forgot something or made a poor choice. Did you rescue them or let them deal with it?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-self-direction">
    <label for="a-self-direction">I have a sense of how self-directed my child is compared to their peers &ndash; whether they initiate activities and sustain effort on their own.<br><span class="assess-hint">Does your child start projects or activities independently, or do they wait for you to organise their time?</span></label>
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

<p>You now understand why parenting matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about wellbeing, relationship, achievement, and development. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/children/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Children Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Children. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/children/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'children';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-emotional-climate', 'a-sleep-nutrition', 'a-stress-signs',
        'a-quality-time', 'a-inner-life', 'a-seeks-comfort',
        'a-academic-level', 'a-enrichment', 'a-strengths-gaps',
        'a-independence', 'a-consequences', 'a-self-direction'
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
