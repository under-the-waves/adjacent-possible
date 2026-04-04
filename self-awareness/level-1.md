---
layout: default
title: "Self-Awareness – Level 1: Awareness"
life_area_slug: self-awareness
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

<h1>Self-Awareness: Level 1</h1>

<p class="l1-subtitle">Understand what self-awareness means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Self-Awareness Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why self-awareness matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Self-awareness &ndash; the ability to see yourself clearly, understand your emotions and motivations, and recognise how others experience you &ndash; is one of the strongest predictors of personal and professional effectiveness. Yet most people significantly overestimate how well they know themselves.</p>

<p>Organisational psychologist <a href="https://hbr.org/2018/01/what-self-awareness-really-is-and-how-to-cultivate-it" target="_blank">Tasha Eurich's research</a> found that while 95% of people believe they are self-aware, only about 10 &ndash; 15% meet the criteria when tested. This gap between perceived and actual self-knowledge affects decision-making, relationships, and emotional regulation in ways that are difficult to detect from the inside.</p>

<p>People with higher self-awareness tend to be <a href="https://doi.org/10.1016/j.leaqua.2010.03.009" target="_blank">more effective leaders</a>, form stronger relationships, and experience greater psychological wellbeing. They are also better at recognising their own biases, which leads to more accurate judgements in both personal and professional contexts.</p>

<p>Self-awareness has two distinct components: internal self-awareness (understanding your own values, reactions, and impact on others) and external self-awareness (understanding how other people actually perceive you). People who score high on one do not necessarily score high on the other, which means developing both requires different approaches.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about self-awareness</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People develop self-awareness through different approaches. This site scores every self-awareness intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Psychological</h3>
<p>Understanding yourself through analysis of mental patterns, triggers, and unconscious processes. People who lean towards this value tend to explore their emotional reactions, examine recurring thought patterns, and seek to understand why they respond to situations the way they do. This might involve therapy, journalling, personality assessments, or studying psychology.</p>

<h3>Contemplative/Somatic</h3>
<p>Awareness through meditation, mindfulness, body sensations, and embodied presence. People who lean towards this value develop the ability to observe their moment-to-moment experience without judgement. They tend to notice physical signals &ndash; tension, fatigue, gut feelings &ndash; as sources of self-knowledge, and may practise sitting meditation, body scanning, or breathwork.</p>

<h3>Relational</h3>
<p>Understanding yourself through social feedback, interpersonal patterns, and how you show up with others. People who lean towards this value recognise that other people often see things about them that they cannot see themselves. They actively seek honest feedback, pay attention to recurring dynamics in their relationships, and use interactions as a mirror.</p>

<h3>Experiential</h3>
<p>Self-discovery through trying new experiences, challenges, and active personal development. People who lean towards this value learn about themselves by doing &ndash; taking on unfamiliar situations, travelling, changing roles, or pushing personal boundaries. They treat life as a series of experiments that reveal who they are.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each self-awareness value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Psychological &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Carl_Jung" target="_blank">Carl Jung</a> pioneered analytical psychology and the concept of individuation &ndash; a lifelong process of integrating conscious and unconscious aspects of the psyche. He spent decades systematically analysing his own dreams, fantasies, and emotional reactions, documenting the process in his <em>Red Book</em>. His personal self-exploration became the foundation for widely used frameworks including psychological types and the concept of the shadow.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Contemplative/Somatic &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Thich_Nhat_Hanh" target="_blank">Thich Nhat Hanh</a> was a Vietnamese Zen Buddhist monk who maintained a daily mindfulness practice for over 60 years. He developed the concept of "engaged Buddhism", applying contemplative awareness to social action, and founded the Plum Village monastic community in France. His teaching emphasised awareness of breathing, walking, and ordinary daily activities as a path to deep self-knowledge.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Relational &ndash; Level 5</div>
    <p><a href="https://brenebrown.com/" target="_blank">Bren&eacute; Brown</a> has described in detail how her own research into vulnerability forced a personal reckoning &ndash; she sought therapy, confronted her patterns of emotional armour, and began deliberately practising the vulnerability she studied. Her 2010 TED talk, one of the most viewed of all time, was itself an act of public relational exposure. She appears to actively solicit feedback from colleagues, family, and audiences about how she comes across, and has spoken openly about the gap between how she sees herself and how others experience her.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Experiential &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Viktor_Frankl" target="_blank">Viktor Frankl</a> was an Austrian psychiatrist who survived three years in Nazi concentration camps, including Auschwitz. He drew on this direct experience of extreme suffering to develop logotherapy, a therapeutic approach built on the idea that meaning can be found in any circumstances. His book <em>Man's Search for Meaning</em> documented how lived experience &ndash; including the most harrowing kind &ndash; can become a source of profound self-understanding.</p>
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
<h4>Psychological</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-triggers">
    <label for="a-triggers">I can name three situations that reliably trigger a strong emotional reaction in me (e.g. anger, anxiety, defensiveness).<br><span class="assess-hint">Think about recurring patterns at work, in relationships, or in daily life.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-coping">
    <label for="a-coping">I know my default coping mechanisms when I'm stressed (e.g. avoidance, over-working, withdrawal, rumination).<br><span class="assess-hint">Consider what you tend to do automatically, not what you think you should do.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-values-conflict">
    <label for="a-values-conflict">I can identify a recent decision where my actions did not align with my stated values.<br><span class="assess-hint">The gap between what we say we value and what we actually do is one of the most useful things to notice.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Contemplative/Somatic</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-body-signals">
    <label for="a-body-signals">I can describe where in my body I typically feel stress or anxiety (e.g. tight shoulders, stomach tension, clenched jaw).<br><span class="assess-hint">Pause for a moment and scan from head to toe. Notice what's there right now.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-attention">
    <label for="a-attention">I know roughly how long I can sustain focused attention on a single task before my mind wanders.<br><span class="assess-hint">Think about reading, working, or listening. Even a rough estimate counts.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-meditation">
    <label for="a-meditation">I know whether I have any current meditation or mindfulness practice, and if so, how often I do it.<br><span class="assess-hint">This includes formal meditation, breathing exercises, or any deliberate present-moment awareness practice.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Relational</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-feedback">
    <label for="a-feedback">I can recall the last time someone gave me honest, critical feedback, and what it was about.<br><span class="assess-hint">If you can't remember any, that itself is useful information.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-perception">
    <label for="a-perception">I have a sense of how my closest colleagues or friends would describe my main strengths and weaknesses.<br><span class="assess-hint">If you're unsure, consider asking someone you trust.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-conflict">
    <label for="a-conflict">I know my typical pattern in conflict (e.g. I tend to avoid it, escalate it, go quiet, or become overly accommodating).<br><span class="assess-hint">Think about the last two or three disagreements you were involved in.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Experiential</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-comfort-zone">
    <label for="a-comfort-zone">I can identify a specific situation in the past year where I was outside my comfort zone, and what I learnt about myself from it.<br><span class="assess-hint">This could be a new job, a difficult conversation, travel, or any unfamiliar challenge.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-change">
    <label for="a-change">I know one important way my self-understanding has changed in the past five years.<br><span class="assess-hint">Something you once believed about yourself that you no longer think is true, or vice versa.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-experiment">
    <label for="a-experiment">I can name something I haven't tried yet that I suspect would teach me something about myself.<br><span class="assess-hint">A new skill, a different social context, solo travel, a creative pursuit &ndash; anything unfamiliar.</span></label>
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

<p>You now understand why self-awareness matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about psychological understanding, contemplative awareness, relational feedback, and experiential learning. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/self-awareness/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Self-Awareness Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Self-Awareness. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/self-awareness/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'self-awareness';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-triggers', 'a-coping', 'a-values-conflict',
        'a-body-signals', 'a-attention', 'a-meditation',
        'a-feedback', 'a-perception', 'a-conflict',
        'a-comfort-zone', 'a-change', 'a-experiment'
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
