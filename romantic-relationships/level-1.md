---
layout: default
title: "Relationship Quality – Level 1: Awareness"
life_area_slug: romantic-relationships
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

<h1>Relationship Quality: Level 1</h1>

<p class="l1-subtitle">Understand what relationship quality means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Relationship Quality Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why relationship quality matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>The quality of your romantic partnership is one of the strongest predictors of overall life satisfaction. Well over 90% of people marry or enter long-term partnerships at some point, yet <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8186435/" target="_blank">40 &ndash; 50% of marriages end in divorce</a>, and many that survive fall into comfortable mediocrity. Only about 30% of marriages maintain what researchers call "vital" or "total" quality over the long term.</p>

<p>The good news is that relationship satisfaction appears to be shaped more by skills than by selection. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9136471/" target="_blank">Meta-analytic research</a> shows that satisfaction correlates at 0.34 with communication quality, 0.36 with togetherness, and &ndash;0.35 with frequency of disagreements. These are learnable, improvable skills &ndash; not fixed traits.</p>

<p>Parenthood is a particular stress test. For most couples, marital satisfaction remains relatively stable over time, but <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3061469/" target="_blank">by the time the first child reaches 15</a>, parents' satisfaction has declined by nearly one standard deviation. Couples who invest deliberately in their relationship appear to weather this transition considerably better.</p>

<p>Relationship quality also cascades into other domains. People in satisfying partnerships tend to report better physical health, lower rates of depression, stronger friendships, and greater career satisfaction. Few other investments touch as many areas of life simultaneously.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about relationship quality</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue relationship quality for different reasons. This site scores every relationship quality intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Connection</h3>
<p>Emotional closeness, vulnerability, trust, and deep mutual understanding. Sharing your inner life, feeling genuinely known and accepted, and maintaining emotional and physical intimacy through life's changes. People who lean towards this value invest in communication skills, emotional availability, and the courage to be vulnerable.</p>

<h3>Harmony</h3>
<p>Low-conflict, smoothly functioning daily life together. Constructive disagreement, equitable division of responsibilities, aligned approaches to finances and parenting, and the ability to navigate differences without erosion of goodwill. People who lean towards this value focus on making the partnership work well day to day.</p>

<h3>Alignment</h3>
<p>Shared values, compatible life goals, and a common vision for the relationship's future. Agreement on major life decisions, compatible priorities, and the sense that you are building towards the same things. People who lean towards this value ensure long-term compatibility underpins the relationship.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each relationship quality value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Connection &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Esther_Perel" target="_blank">Esther Perel</a> has spent over 35 years studying and practising what sustains emotional and erotic connection in long-term partnerships. Her clinical work, books, and podcast <em>Where Should We Begin?</em> demonstrate an unusually deep understanding of vulnerability, desire, and intimacy. She and her husband have maintained their own partnership across decades while she has helped thousands of couples rebuild emotional closeness after betrayal, stagnation, or loss.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Harmony &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Julie_Schwartz_Gottman" target="_blank">Julie Schwartz Gottman</a> co-founded the Gottman Institute with her husband John, and the two have built one of the most cited bodies of research on what makes marriages succeed or fail. Their own partnership &ndash; running a business, raising a daughter, and maintaining a marriage across four decades &ndash; serves as a working example of the conflict resolution and daily collaboration principles they teach. Julie developed the Gottman Couples Therapy method and has trained thousands of therapists worldwide.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Alignment &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Barack_Obama" target="_blank">Barack and Michelle Obama</a> have described their marriage as built on explicit shared values &ndash; public service, family priority, and intellectual partnership &ndash; negotiated and renegotiated over more than 30 years. They navigated career sacrifices (Michelle leaving her legal career for his political ambitions), eight years of intense public scrutiny in the White House, and the pressures of raising children under constant observation. Both have spoken candidly about the work involved, including marriage counselling, suggesting a relationship sustained by deliberate alignment rather than effortless compatibility.</p>
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
<h4>Connection</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-attachment">
    <label for="a-attachment">I have a sense of my own attachment style and how it shows up in my relationship.<br><span class="assess-hint">Secure, anxious, avoidant, or disorganised &ndash; even a rough sense is useful.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-vulnerability">
    <label for="a-vulnerability">I know whether I have shared something genuinely personal or difficult with my partner in the past fortnight.<br><span class="assess-hint">Something beyond logistics &ndash; a fear, a hope, a frustration, an appreciation.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-quality-time">
    <label for="a-quality-time">I know how much undistracted, one-on-one time I spend with my partner in a typical week.<br><span class="assess-hint">Time without screens, children, or other distractions &ndash; focused on each other.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Harmony</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-conflict-patterns">
    <label for="a-conflict-patterns">I can identify our most common conflict pattern &ndash; what triggers it and how it typically ends.<br><span class="assess-hint">Does one person pursue while the other withdraws? Do arguments escalate or get swept under the carpet?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-responsibilities">
    <label for="a-responsibilities">I know whether both partners feel the division of household and life responsibilities is fair.<br><span class="assess-hint">Cooking, cleaning, finances, childcare, emotional labour &ndash; consider all of it.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-repair">
    <label for="a-repair">I know how long it typically takes us to repair after an argument &ndash; hours, days, or longer.<br><span class="assess-hint">Think about the last few disagreements. How quickly did you return to normal?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Alignment</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-values-match">
    <label for="a-values-match">I can name the core values I share with my partner and any significant areas where we diverge.<br><span class="assess-hint">Money, religion, politics, ambition, family, lifestyle &ndash; where do you agree and disagree?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-future-vision">
    <label for="a-future-vision">I know whether we have discussed and agreed on what we want our lives to look like in five years.<br><span class="assess-hint">Location, careers, children, finances, retirement &ndash; do you have a shared picture?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-decisions">
    <label for="a-decisions">I can recall the last major decision we made together and whether both of us felt genuinely heard.<br><span class="assess-hint">A move, a purchase, a career change, a family decision &ndash; how did the process feel?</span></label>
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

<p>You now understand why relationship quality matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about connection, harmony, and alignment. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/romantic-relationships/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Relationship Quality Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Relationship Quality. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/romantic-relationships/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'romantic-relationships';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-attachment', 'a-vulnerability', 'a-quality-time',
        'a-conflict-patterns', 'a-responsibilities', 'a-repair',
        'a-values-match', 'a-future-vision', 'a-decisions'
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
