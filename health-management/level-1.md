---
layout: default
title: "Health Management – Level 1: Awareness"
life_area_slug: health-management
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

<h1>Health Management: Level 1</h1>

<p class="l1-subtitle">Understand what health management means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Health Management Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why health management matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>How you manage your health &ndash; the decisions you make about prevention, screening, providers, and medical care &ndash; has an outsized effect on your long-term outcomes. The evidence is clear: proactive health management leads to substantially better results than reacting to problems as they arise.</p>

<p>Patients who actively engage with their healthcare experience <a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2012.1061" target="_blank">15 &ndash; 25% better outcomes</a> across chronic conditions, along with lower overall healthcare costs. Yet only <a href="https://www.cdc.gov/mmwr/volumes/68/wr/mm6840a2.htm" target="_blank">8% of Americans</a> receive all recommended preventive services. The gap between what is available and what most people actually do is enormous.</p>

<p>Effective health management extends well beyond annual checkups. It includes understanding your personal risk factors, building relationships with providers who know your history, coordinating care when you need multiple specialists, and creating systems that keep you on track without constant effort. People who develop these capabilities <a href="https://www.commonwealthfund.org/publications/issue-briefs/2019/jan/economic-case-us-foundation-high-performance-health-system" target="_blank">report less health-related stress</a> and catch problems earlier, when treatment is simpler and more effective.</p>

<p>Few investments compound as reliably as learning to manage your own health well. The skills and systems you build now pay dividends for decades.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about health management</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach health management for different reasons. This site scores every health management intervention across four core values. Later, you'll set your own weighting across these values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Long-term Health</h3>
<p>Disease prevention, longevity optimisation, and maintaining physical and cognitive function throughout life. People who lean towards this value invest time and resources in comprehensive preventive care, understanding genetic risks, and implementing evidence-based interventions for healthy ageing.</p>

<h3>Present Vitality</h3>
<p>Immediate energy, cognitive function, and daily wellbeing through optimised health practices. People who lean towards this value focus on addressing symptoms that affect quality of life and ensuring their health decisions support current life goals and activities.</p>

<h3>Personal Control</h3>
<p>The knowledge, skills, and confidence to make informed health decisions and advocate effectively within healthcare systems. People who lean towards this value want to be active participants in their healthcare &ndash; understanding medical information, building productive relationships with providers, and taking ownership of health outcomes.</p>

<h3>Simplicity</h3>
<p>Efficient, low-maintenance systems that deliver good health outcomes without consuming excessive time or mental energy. People who lean towards this value seek streamlined approaches to preventive care, clear protocols for common health issues, and automated systems that integrate seamlessly with their lifestyle.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each health management value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Long-term Health &ndash; Level 5</div>
    <p><a href="https://peterattiamd.com/about/" target="_blank">Peter Attia</a> is a physician who structures his entire life around longevity optimisation. He undergoes quarterly blood panels, annual full-body MRI and DEXA scans, continuous glucose monitoring, and regular cardiovascular stress testing. He has spoken publicly about adjusting his exercise, nutrition, and sleep protocols based on biomarker trends tracked over more than a decade. His practice centres on what he calls "Medicine 3.0" &ndash; a preventive approach that aims to extend healthspan.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Present Vitality &ndash; Level 5</div>
    <p><a href="https://www.foundmyfitness.com/about" target="_blank">Rhonda Patrick</a> holds a PhD in biomedical science and applies detailed self-experimentation to optimise her daily energy and cognitive performance. She has documented her use of sauna protocols, cold exposure, micronutrient tracking, and time-restricted eating, adjusting each based on how they affect her day-to-day function. She appears to maintain consistently high output across research, public communication, and parenting.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Personal Control &ndash; Level 5</div>
    <p><a href="https://epatientdave.com/about-dave/" target="_blank">Dave deBronkart</a> ("e-Patient Dave") was diagnosed with stage IV kidney cancer in 2007. He researched his condition extensively, identified a clinical trial through an online patient community, and worked with his oncologists to secure access to a treatment that contributed to his full remission. He went on to co-found the Society for Participatory Medicine and has <a href="https://www.bmj.com/content/346/bmj.f1990" target="_blank">published in the BMJ</a> on patient engagement.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Simplicity &ndash; Level 5</div>
    <p><a href="https://www.atulawande.org/" target="_blank">Atul Gawande</a> is a surgeon and public health researcher whose work focuses on making complex healthcare processes more reliable and efficient. His <a href="https://www.nejm.org/doi/full/10.1056/NEJMsa0810119" target="_blank">surgical checklist research</a> reduced post-operative deaths by 47% across eight hospitals. He applies systems-level thinking to his own health management and has written extensively about building simple, effective protocols for complex problems.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to look up or check. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've found it out).</p>

<div class="assess-group">
<h4>Long-term Health</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-last-checkup">
    <label for="a-last-checkup">I know when I last had a general health checkup or physical examination.<br><span class="assess-hint">Include any visit where a doctor reviewed your overall health, not just a specific complaint.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-screenings">
    <label for="a-screenings">I know which preventive screenings are recommended for my age and sex, and whether I'm up to date on them.<br><span class="assess-hint">Common examples: blood pressure, cholesterol, blood glucose, cancer screenings, dental checkups.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-family-history">
    <label for="a-family-history">I know my family's major health history and any conditions that increase my personal risk.<br><span class="assess-hint">Heart disease, diabetes, cancer, and mental health conditions in parents, siblings, or grandparents.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Present Vitality</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-energy-patterns">
    <label for="a-energy-patterns">I can describe my typical daily energy pattern &ndash; when I feel most alert and when I tend to flag.<br><span class="assess-hint">Morning person vs night owl, post-lunch dip, weekend vs weekday differences.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-persistent-symptoms">
    <label for="a-persistent-symptoms">I know whether I have any persistent symptoms I've been ignoring or tolerating.<br><span class="assess-hint">Recurring headaches, digestive issues, joint pain, skin conditions, fatigue, or anything you've learned to live with.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-medications">
    <label for="a-medications">I can list any medications or supplements I take regularly and I know why I take each one.<br><span class="assess-hint">Include prescriptions, over-the-counter medicines, vitamins, and supplements.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Personal Control</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-provider-relationship">
    <label for="a-provider-relationship">I know who my primary care provider is and when I last saw them.<br><span class="assess-hint">A GP, family doctor, or equivalent who knows your health history.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-ask-questions">
    <label for="a-ask-questions">I have a sense of how comfortable I am asking questions and raising concerns during medical appointments.<br><span class="assess-hint">Do you tend to accept what's recommended without question, or do you ask about alternatives and side effects?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-health-records">
    <label for="a-health-records">I know where my health records are and whether I can access them.<br><span class="assess-hint">Patient portals, paper files, or simply knowing which practices hold your records.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Simplicity</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-insurance">
    <label for="a-insurance">I understand my health insurance coverage &ndash; what's included, what my excess is, and how to make a claim.<br><span class="assess-hint">Or, if you rely on a public health system, you know what services are available and how to access them.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-reminders">
    <label for="a-reminders">I know whether I have any system for tracking upcoming appointments, screenings, or prescription renewals.<br><span class="assess-hint">Calendar reminders, patient portal notifications, a list on your phone, or nothing at all.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-urgent-care">
    <label for="a-urgent-care">I know what I would do if I had a health concern outside normal hours &ndash; where to go and who to call.<br><span class="assess-hint">Urgent care clinic, NHS 111, emergency department, or a nurse helpline.</span></label>
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

<p>You now understand why health management matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about long-term health, present vitality, personal control, and simplicity. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/health-management/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Health Management Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Health Management. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/health-management/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'health-management';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-last-checkup', 'a-screenings', 'a-family-history',
        'a-energy-patterns', 'a-persistent-symptoms', 'a-medications',
        'a-provider-relationship', 'a-ask-questions', 'a-health-records',
        'a-insurance', 'a-reminders', 'a-urgent-care'
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
