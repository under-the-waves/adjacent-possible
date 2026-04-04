---
layout: default
title: "Mental Health – Level 1: Awareness"
life_area_slug: mental-health
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

<h1>Mental Health: Level 1</h1>

<p class="l1-subtitle">Understand what mental health means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Mental Health Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why mental health matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Mental health shapes how you think, feel, and act in daily life. It influences your decision-making, your relationships, your physical health, and your capacity to handle stress. The effects are measurable and far-reaching.</p>

<p>Depression increases <a href="https://www.verywellmind.com/the-mental-and-physical-health-connection-7255857" target="_blank">cardiovascular disease risk by 20 &ndash; 40%</a>, whilst chronic physical conditions raise depression risk in turn. About <a href="https://www.cdc.gov/social-connectedness/risk-factors/index.html" target="_blank">1 in 3 adults</a> report feeling lonely, and loneliness is linked to increased risks of heart disease, stroke, and premature mortality.</p>

<p>The workplace effects are substantial: the <a href="https://www.who.int/teams/mental-health-and-substance-use/promotion-prevention/mental-health-in-the-workplace" target="_blank">WHO estimates</a> that 12 billion working days are lost annually to depression and anxiety, costing the global economy $1 trillion per year. And <a href="https://www.hhs.gov/surgeongeneral/reports-and-publications/workplace-well-being/index.html" target="_blank">76% of workers</a> report experiencing mental health symptoms, with 84% saying workplace conditions contributed.</p>

<p>The good news is that mental health responds to intervention. Evidence-based therapies, self-management practices, and lifestyle changes all produce measurable improvements &ndash; and many of the highest-impact approaches are accessible without specialist referral.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about mental health</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach mental health for different reasons. This site scores every mental health intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Professional Treatment & Support</h3>
<p>Working with qualified mental health professionals and building strong support networks. Therapy, counselling, medication when appropriate, and leveraging relationships for mental health support. People who lean towards this value focus on expert guidance and community-based approaches to mental wellness.</p>

<h3>Self-Management & Independence</h3>
<p>Developing personal skills and practices to manage your own mental health independently. Mindfulness, journalling, exercise, and other self-directed interventions that build internal capabilities. People who lean towards this value focus on self-reliance and building their own emotional toolkit.</p>

<h3>Integration & Holistic Approach</h3>
<p>Viewing mental health as interconnected with all other life areas and addressing it through lifestyle, relationships, purpose, and environment. People who lean towards this value see mental wellness as emerging from overall life balance and meaning, and would pursue it even if they had no specific symptoms to address.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each mental health value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Professional Treatment & Support &ndash; Level 5</div>
    <p><a href="https://www.stephenfry.com/" target="_blank">Stephen Fry</a> has spoken and written extensively about living with bipolar disorder over several decades, including periods of hospitalisation and suicidal ideation. He has maintained ongoing professional treatment throughout, and his documentary <em>The Secret Life of the Manic Depressive</em> documented his relationship with psychiatry in detail. He appears to use professional support as a sustained foundation for functioning at a high level across multiple careers.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Self-Management & Independence &ndash; Level 5</div>
    <p><a href="https://www.thetoolsbook.com/phil-stutz.html" target="_blank">Phil Stutz</a>, the psychotherapist featured in the Netflix documentary <em>Stutz</em>, has managed Parkinson's disease, chronic pain, and depression throughout his career using a structured set of self-directed practices he developed over decades. His approach centres on daily internal exercises &ndash; visualisation, body awareness, and emotional regulation routines &ndash; which he reportedly practises himself, making him an unusually visible example of a practitioner who lives his own methods.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Integration & Holistic Approach &ndash; Level 5</div>
    <p><a href="https://johannhari.com/" target="_blank">Johann Hari</a>, after researching and writing <em>Lost Connections</em>, restructured his own life around the social and environmental contributors to depression he had identified &ndash; changing his work patterns, investing in community, and redesigning his daily routines around connection and purpose. He has discussed publicly how these lifestyle changes, alongside professional treatment, produced more lasting improvements than medication alone had done for him.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to reflect on. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've worked it out).</p>

<div class="assess-group">
<h4>Professional Treatment & Support</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-prof-access">
    <label for="a-prof-access">I know how to access professional mental health support in my area, including at least one specific service I could contact.<br><span class="assess-hint">GP referral, local counselling service, employee assistance programme, or a specific therapist.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-prof-history">
    <label for="a-prof-history">I can describe my history with professional mental health support &ndash; whether I've used it, what worked, and what didn't.<br><span class="assess-hint">"Never tried it," "saw a counsellor for six months in 2019," or "currently in therapy" all count.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-prof-network">
    <label for="a-prof-network">I know whether I have at least one person I trust enough to discuss mental health concerns with honestly.<br><span class="assess-hint">A friend, partner, family member, or colleague &ndash; someone you would actually talk to, not just theoretically could.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Self-Management & Independence</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-self-triggers">
    <label for="a-self-triggers">I can name my three most common stress triggers and describe how I typically respond to each.<br><span class="assess-hint">Work deadlines, conflict, financial pressure, loneliness &ndash; and whether you withdraw, ruminate, exercise, talk to someone, etc.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-self-techniques">
    <label for="a-self-techniques">I know which stress management techniques I currently use and whether they actually help.<br><span class="assess-hint">Meditation, exercise, journalling, breathing exercises, talking it through &ndash; or nothing structured at all.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-self-emotions">
    <label for="a-self-emotions">I can usually identify what I'm feeling during a difficult moment, using a more specific word than "bad" or "stressed."<br><span class="assess-hint">Anxious, frustrated, overwhelmed, lonely, ashamed, bored &ndash; the ability to name emotions accurately is a core self-management skill.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Integration & Holistic Approach</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-int-sleep">
    <label for="a-int-sleep">I have a sense of how my sleep quality affects my mood and mental clarity the following day.<br><span class="assess-hint">Better after good sleep, worse after poor sleep, or genuinely unsure &ndash; all count as long as you've thought about it.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-int-exercise">
    <label for="a-int-exercise">I know whether regular exercise noticeably changes how I feel mentally, and roughly how much it takes to have an effect.<br><span class="assess-hint">A 20-minute walk, a gym session, a run &ndash; or you've noticed no mental health effect from exercise. Either answer is useful.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-int-social">
    <label for="a-int-social">I can identify which relationships or social situations consistently improve my mental state and which drain it.<br><span class="assess-hint">Specific people, group sizes, types of interaction &ndash; knowing your social energy patterns.</span></label>
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

<p>You now understand why mental health matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about professional support, self-management, and holistic integration. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/mental-health/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Mental Health Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Mental Health. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/mental-health/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'mental-health';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-prof-access', 'a-prof-history', 'a-prof-network',
        'a-self-triggers', 'a-self-techniques', 'a-self-emotions',
        'a-int-sleep', 'a-int-exercise', 'a-int-social'
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
