---
layout: default
title: "Cognitive Skills – Level 1: Awareness"
life_area_slug: cognitive-skills
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

<h1>Cognitive Skills: Level 1</h1>

<p class="l1-subtitle">Understand what cognitive skills are, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Cognitive Skills Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why cognitive skills matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your cognitive abilities – memory, focus, reasoning, problem-solving – underpin almost everything you do. They determine how quickly you learn, how well you make decisions, and how effectively you handle complex situations at work and in daily life.</p>

<p>The good news is that these abilities are more trainable than most people assume. Meta-analyses of memory training show that <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3399982/" target="_blank">evidence-based techniques can improve retention by 200 – 300%</a> over baseline methods. Even short periods of attention training – as little as five days – appear to <a href="https://www.pnas.org/content/104/43/17152" target="_blank">improve executive attention and reduce stress-related cortisol</a>.</p>

<p>Lifestyle factors matter too. Regular exercise <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2441149/" target="_blank">increases BDNF by 15 – 30%</a>, a protein that supports learning and memory. Sleep optimisation enhances memory consolidation substantially. These gains compound: better cognitive function speeds up learning in every domain, which in turn opens more opportunities for growth elsewhere.</p>

<p>Yet most adults have never received any formal training in how to think, remember, or focus more effectively. Fewer than 3% use evidence-based memory techniques regularly, and fewer than 10% can sustain focus on demanding work for 30 minutes without distraction. This means even modest investment tends to yield disproportionate returns.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about cognitive skills</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue cognitive improvement for different reasons. This site scores every cognitive skills intervention across four core values. Later, you'll set your own weighting across these values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Memory</h3>
<p>Developing systematic approaches to encode, store, and retrieve information efficiently. People who lean towards this value want measurably better recall for learning, professional tasks, and accessing stored knowledge when it matters. They tend to gravitate towards techniques like spaced repetition, method of loci, and elaborative encoding.</p>

<h3>Focus</h3>
<p>Sustained attention, concentration, and cognitive control. People who lean towards this value want better command over where their mind goes and stays during demanding tasks. They may pursue mindfulness meditation, attention training, or environmental design to reduce distraction and improve task-switching ability.</p>

<h3>Reasoning & Problem-Solving</h3>
<p>Fluid intelligence, abstract reasoning, and creative problem-solving. People who lean towards this value want to think through complex problems more effectively – breaking challenges into components, spotting patterns, and generating novel solutions. They often pursue working memory training and systematic reasoning exercises.</p>

<h3>Lifestyle Integration</h3>
<p>Cognitive enhancement through sustainable daily practices. People who lean towards this value want cognitive benefits that emerge from overall wellbeing – optimised sleep, regular exercise, good nutrition, and stress management – rather than dedicated cognitive training sessions.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each cognitive skills value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Memory &ndash; Level 5</div>
    <p><a href="https://www.mullen.memory/" target="_blank">Alex Mullen</a> is a three-time World Memory Champion who memorised a shuffled deck of cards in 15.61 seconds and over 3,000 digits in an hour. He trained using the method of loci and spaced repetition while completing medical school, demonstrating that exceptional memory performance is compatible with a demanding professional career. He now teaches memory techniques through his platform Mullen Memory.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Focus &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Mihaly_Csikszentmihalyi" target="_blank">Mihaly Csikszentmihalyi</a> spent over 40 years researching the psychology of optimal experience and coined the concept of "flow." He reportedly structured his own working life around the conditions he studied &ndash; long uninterrupted blocks, intrinsic motivation, and clear goals &ndash; and maintained a prolific research output across psychology, creativity, and education until his death in 2021 at age 87.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Reasoning & Problem-Solving &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Terence_Tao" target="_blank">Terence Tao</a> is a mathematician at UCLA who has published over 300 research papers across multiple subfields and won the Fields Medal in 2006. His ability to identify patterns and generate novel approaches across diverse areas of mathematics – from harmonic analysis to combinatorics to partial differential equations – reflects extraordinary reasoning ability sustained at the highest level for decades.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Lifestyle Integration &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Sanjay_Gupta" target="_blank">Sanjay Gupta</a> is a practising neurosurgeon and CNN's chief medical correspondent who wrote <em>Keep Sharp</em> based on his clinical experience with cognitive decline. He maintains a personal regimen of daily exercise, sleep discipline, and continuous learning that he describes as non-negotiable for his own cognitive performance. He has sustained demanding parallel careers in surgery and broadcasting for over 20 years, suggesting the lifestyle integration he advocates is one he genuinely practises.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to think through. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've found it out).</p>

<div class="assess-group">
<h4>Memory</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-recall-names">
    <label for="a-recall-names">I have a sense of how well I remember names of people I've recently met.<br><span class="assess-hint">Think about the last few social or professional settings where you met new people. Could you recall their names the next day?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-memory-techniques">
    <label for="a-memory-techniques">I know whether I currently use any deliberate memory techniques.<br><span class="assess-hint">Spaced repetition apps, mnemonics, method of loci, note-taking systems designed for retention – or none at all.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-retention">
    <label for="a-retention">I have a rough idea of how much I retain from articles, books, or presentations after a week.<br><span class="assess-hint">Think about something you read or watched last week. How much can you recall now?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Focus</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-focus-duration">
    <label for="a-focus-duration">I know roughly how long I can sustain focus on demanding work before getting distracted.<br><span class="assess-hint">Think about a typical work session on something cognitively challenging. How many minutes before you check your phone, open a new tab, or lose your train of thought?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-distraction-triggers">
    <label for="a-distraction-triggers">I can identify my main distraction triggers.<br><span class="assess-hint">Phone notifications, email, social media, noise, boredom, anxiety, fatigue – which ones pull you away most often?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-attention-practices">
    <label for="a-attention-practices">I know whether I do anything deliberate to train or protect my attention.<br><span class="assess-hint">Meditation, phone-free periods, website blockers, structured work intervals – or nothing specific.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Reasoning & Problem-Solving</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-problem-approach">
    <label for="a-problem-approach">I've thought about how I typically approach complex problems.<br><span class="assess-hint">Do you break them into parts? Jump to solutions? Seek advice? Use frameworks? Work through trial and error?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-reasoning-biases">
    <label for="a-reasoning-biases">I have some awareness of my reasoning biases or blind spots.<br><span class="assess-hint">Confirmation bias, anchoring, availability heuristic – do you know which ones affect your thinking most?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-reasoning-training">
    <label for="a-reasoning-training">I know whether I've had any formal or informal training in reasoning or critical thinking.<br><span class="assess-hint">Logic courses, debate, philosophy, scientific method, decision-making frameworks – or just learning on the job.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Lifestyle Integration</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-sleep-cognition">
    <label for="a-sleep-cognition">I have a sense of how my sleep affects my mental clarity and cognitive performance.<br><span class="assess-hint">Do you notice a difference in your thinking on days after good vs poor sleep?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-exercise-cognition">
    <label for="a-exercise-cognition">I know whether exercise noticeably affects my mental sharpness.<br><span class="assess-hint">Some people think more clearly after exercise. Others don't notice a difference. Which is true for you?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-lifestyle-deliberate">
    <label for="a-lifestyle-deliberate">I know whether I do anything deliberately to support my cognitive performance through lifestyle choices.<br><span class="assess-hint">Optimised sleep schedule, exercise for brain health, nutrition choices, stress management – or nothing specific.</span></label>
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

<p>You now understand why cognitive skills matter, what different people get out of developing them, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about memory, focus, reasoning and problem-solving, and lifestyle integration. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/cognitive-skills/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Cognitive Skills Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Cognitive Skills. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/cognitive-skills/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'cognitive-skills';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-recall-names', 'a-memory-techniques', 'a-retention',
        'a-focus-duration', 'a-distraction-triggers', 'a-attention-practices',
        'a-problem-approach', 'a-reasoning-biases', 'a-reasoning-training',
        'a-sleep-cognition', 'a-exercise-cognition', 'a-lifestyle-deliberate'
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
