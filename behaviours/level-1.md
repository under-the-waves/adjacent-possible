---
layout: default
title: "Behaviours – Level 1: Awareness"
life_area_slug: behaviours
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

<h1>Behaviours: Level 1</h1>

<p class="l1-subtitle">Understand what behavioural change means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Behaviours Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why behaviours matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Automatic behavioural patterns – addictions, compulsions, emotional reactions, avoidance – often run in the background of daily life, shaping decisions without conscious input. Most people have at least a few patterns that work against their stated goals, yet only about <a href="https://www.addictionhelp.com/recovery/statistics/" target="_blank">24% of those who would benefit</a> from addressing them actually do so.</p>

<p>The costs of unchecked patterns tend to compound. Reactive behaviours can erode relationships, undermine career progress, and worsen mental health over time. <a href="https://www.who.int/news-room/fact-sheets/detail/mental-disorders" target="_blank">WHO data</a> suggests that 1 in 8 people globally live with an anxiety or depressive disorder, and emotional dysregulation is a contributing factor in both conditions.</p>

<p>On the other side, people who develop the capacity to choose their responses – rather than defaulting to compulsive ones – generally report greater life satisfaction, stronger relationships, and more resilience during difficult periods. The evidence from <a href="https://substanceabusepolicy.biomedcentral.com/articles/10.1186/1747-597X-6-17" target="_blank">relapse prevention research</a> indicates that behavioural awareness is a necessary foundation for lasting change, even if awareness alone is not sufficient.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about behavioural change</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue behavioural change for different reasons. This site scores every behaviours intervention across four core values. Later, you'll set your own weighting across these values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Freedom & Control</h3>
<p>Liberation from compulsive patterns and automatic responses that limit your choices. Breaking free from addictions, managing impulses, and developing the ability to pause between trigger and response. People who lean towards this value focus on restoring genuine choice in their actions, even when it requires significant upfront effort or temporary discomfort.</p>

<h3>Emotional Regulation</h3>
<p>Developing healthier responses to emotional triggers like stress, anxiety, anger, or boredom. Moving from reactive emotional patterns to more measured, intentional responses. Those who lean towards this value focus on building emotional skills and alternative coping strategies, accepting that feeling emotions fully may be temporarily more difficult than numbing them.</p>

<h3>Social & Relational Patterns</h3>
<p>Changing automatic interpersonal behaviours like people-pleasing, conflict avoidance, codependency, social withdrawal, or defensive reactions. People who lean towards this value work on assertiveness, boundary-setting, and staying present during difficult social situations.</p>

<h3>Resilience & Adaptability</h3>
<p>Building sustainable behavioural change that survives life disruptions and does not require constant vigilance. Developing multiple coping strategies, planning for setbacks, and creating robust systems. Those who lean towards this value are willing to progress more slowly to ensure changes last through major life transitions or crises.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each behaviours value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Freedom & Control &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Anthony_Hopkins" target="_blank">Anthony Hopkins</a> stopped drinking on 29 December 1975 after what he has described as years of destructive alcoholism. He has maintained sobriety for over 50 years while working continuously in one of the most high-pressure industries in the world. He credits daily discipline and a complete change in daily habits for his sustained recovery, and by all accounts has not relapsed despite decades of public life and professional stress.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Emotional Regulation &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Marsha_M._Linehan" target="_blank">Marsha Linehan</a> developed Dialectical Behaviour Therapy after her own experience of severe emotional dysregulation and psychiatric hospitalisation as a young woman. She publicly disclosed in 2011 that she had been a patient at the Institute of Living, where she was diagnosed with schizophrenia and subjected to electroshock treatment. She went on to build a daily practice of the emotional regulation skills she later formalised into DBT, and has maintained that practice for over 40 years.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Social & Relational Patterns &ndash; Level 5</div>
    <p><a href="https://www.gottman.com/about/john-julie-gottman/" target="_blank">John Gottman</a> has spent over 40 years researching couple interactions and can predict relationship outcomes with roughly 90% accuracy based on behavioural patterns. Beyond his research, he practises what he studies – maintaining a long-term partnership while navigating the pressures of public intellectual life. His work on repairing conflict patterns and maintaining authentic connection under pressure reflects mastery-level relational skill.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Resilience & Adaptability &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Nelson_Mandela" target="_blank">Nelson Mandela</a> spent 27 years in prison, including 18 on Robben Island, and emerged without evident bitterness towards his captors. He maintained daily exercise routines, studied by correspondence, and cultivated relationships with guards throughout his imprisonment. After his release in 1990 he led South Africa's transition away from apartheid through negotiation, demonstrating a capacity to adapt his behaviour to radically different circumstances while sustaining purpose across decades.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes of honest reflection. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've thought it through).</p>

<div class="assess-group">
<h4>Freedom & Control</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-compulsive-patterns">
    <label for="a-compulsive-patterns">I can name 2 &ndash; 3 specific behaviours where I act compulsively or automatically against my better judgment.<br><span class="assess-hint">These might involve substances, screens, food, spending, procrastination, or anything else you do despite wanting to stop.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-triggers">
    <label for="a-triggers">I know the primary triggers that lead to my most problematic automatic behaviours.<br><span class="assess-hint">Common triggers include boredom, stress, loneliness, fatigue, specific times of day, or particular social situations.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-pause">
    <label for="a-pause">I have a sense of whether I can currently pause between a trigger and my response, or whether the behaviour feels genuinely automatic.<br><span class="assess-hint">Some patterns feel like a conscious choice you keep making; others feel like they happen before you notice.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Emotional Regulation</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-emotional-triggers">
    <label for="a-emotional-triggers">I can identify which emotions most often lead me to engage in problematic behaviours.<br><span class="assess-hint">Stress, anxiety, anger, boredom, sadness, loneliness &ndash; different people have different emotional triggers.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-coping">
    <label for="a-coping">I know what coping strategies I currently use when experiencing difficult emotions, and whether they help or make things worse.<br><span class="assess-hint">Coping might include exercise, talking to someone, distraction, avoidance, substance use, or rumination.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-emotional-frequency">
    <label for="a-emotional-frequency">I have a rough sense of how often stress or emotional discomfort leads me to act in ways I later regret.<br><span class="assess-hint">Daily? A few times a week? Occasionally? Almost never?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Social & Relational Patterns</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-interpersonal-defaults">
    <label for="a-interpersonal-defaults">I can describe my default response during interpersonal conflict or social pressure.<br><span class="assess-hint">Common defaults include people-pleasing, withdrawal, defensiveness, aggression, or shutting down emotionally.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-boundaries">
    <label for="a-boundaries">I know whether I find it easy or difficult to express my needs and set boundaries in close relationships.<br><span class="assess-hint">Think about your most important relationships &ndash; partner, family, close friends, work colleagues.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-social-avoidance">
    <label for="a-social-avoidance">I have a sense of whether I avoid certain social situations because of anxiety, past experiences, or fear of conflict.<br><span class="assess-hint">Avoidance can be obvious (declining invitations) or subtle (staying quiet, changing the subject, leaving early).</span></label>
</div>
</div>

<div class="assess-group">
<h4>Resilience & Adaptability</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-past-attempts">
    <label for="a-past-attempts">I can recall past attempts to change a behaviour and identify what worked, what failed, and why.<br><span class="assess-hint">New Year's resolutions, attempts to quit something, efforts to be more assertive &ndash; what happened?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-disruption">
    <label for="a-disruption">I know which of my current positive behaviours tend to collapse during stressful periods or life changes.<br><span class="assess-hint">Exercise routines, sleep schedules, dietary habits, social commitments &ndash; which ones survive disruption?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-backup-strategies">
    <label for="a-backup-strategies">I have a sense of whether I rely on a single coping strategy or have multiple alternatives available.<br><span class="assess-hint">If your main stress-relief method becomes unavailable, do you have a backup, or do you default to something unhelpful?</span></label>
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

<p>You now understand why behaviours matter, what different people get out of behavioural change, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about freedom and control, emotional regulation, social and relational patterns, and resilience. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/behaviours/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Behaviours Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Behaviours. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/behaviours/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'behaviours';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-compulsive-patterns', 'a-triggers', 'a-pause',
        'a-emotional-triggers', 'a-coping', 'a-emotional-frequency',
        'a-interpersonal-defaults', 'a-boundaries', 'a-social-avoidance',
        'a-past-attempts', 'a-disruption', 'a-backup-strategies'
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
