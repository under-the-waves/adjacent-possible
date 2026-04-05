---
layout: default
title: "Current Work – Level 1: Awareness"
life_area_slug: current-work
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

<h1>Current Work: Level 1</h1>

<p class="l1-subtitle">Understand what current work means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Current Work Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why current work matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your current work dominates your waking life. The average person spends roughly <a href="https://www.gettysburg.edu/news/stories?id=79db7b34-630c-4f49-ad32-4ab9ea48e72b" target="_blank">90,000 hours</a> at work over a lifetime – more time than almost any other single activity.</p>

<p>Yet most people underperform relative to their potential. The average worker is genuinely productive for just <a href="https://www.vouchercloud.com/resources/office-worker-productivity" target="_blank">2 hours and 53 minutes</a> of an 8-hour day. Only <a href="https://www.gallup.com/workplace/349484/state-of-the-global-workplace.aspx" target="_blank">21% of employees globally</a> are actively engaged, and 45% report working primarily for pay rather than purpose.</p>

<p>The gap between typical and exceptional is enormous. Top performers in complex roles are up to <a href="https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights" target="_blank">800% more productive</a> than average, with the top 5% producing 26% of total output. Flow states – which occupy roughly 5% of working hours for the average person – can nearly double productivity when increased.</p>

<p>Small improvements compound dramatically. Moving from disengaged to engaged, from reactive to intentional, or from competent to skilled can transform both your output and your experience of work.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about current work</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach their working lives for different reasons. This site scores every current work intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Rewards</h3>
<p>The tangible returns you receive for your work – compensation, recognition, status, and career advancement. People who lean towards this value ensure their work delivers fair returns for the effort invested, and actively manage their compensation trajectory.</p>

<h3>Competence</h3>
<p>Skill and effectiveness at performing your role's core responsibilities. Technical proficiency, consistent quality of output, and the ability to handle increasing complexity. People who lean towards this value focus on mastering the craft of their work and continuously raising their standard.</p>

<h3>Engagement</h3>
<p>Psychological investment, motivation, and meaning found in daily work. Experiencing flow states, feeling intrinsically motivated, and finding genuine interest in problems. People who lean towards this value seek roles and tasks that align with their strengths and actively shape their work to be absorbing.</p>

<h3>Balance</h3>
<p>Maintaining sustainable boundaries between work and the rest of life. Manageable hours, predictable schedules, the ability to disconnect, and ensuring work does not crowd out health, relationships, or personal interests. People who lean towards this value protect their non-work life as a deliberate choice.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each current work value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Rewards &ndash; Level 5</div>
    <p><a href="https://www.crunchbase.com/person/stewart-butterfield" target="_blank">Stewart Butterfield</a> co-founded Flickr and Slack, both of which emerged from failed video game projects. He sold Flickr to Yahoo for an estimated $25 million and built Slack into a company valued at $27.7 billion when Salesforce acquired it in 2021. His career demonstrates how exceptional rewards follow from building things people genuinely need.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Competence &ndash; Level 5</div>
    <p><a href="https://jvns.ca/" target="_blank">Julia Evans</a> is a software engineer known for explaining complex systems concepts with unusual clarity. Her zines, blog posts, and tools have become widely used learning resources across the industry. She exemplifies competence that goes beyond performing a role well – she advances how others understand and practise their craft.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Engagement &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/John_Carmack" target="_blank">John Carmack</a> has spent decades working at the frontier of real-time graphics and virtual reality, from Doom to Oculus. He is known for sustained, deep focus – often working 60+ hour weeks by choice – and has described programming as the activity he would do regardless of compensation. His engagement is inseparable from his identity.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Balance &ndash; Level 5</div>
    <p><a href="https://basecamp.com/about/jason-fried" target="_blank">Jason Fried</a>, co-founder of Basecamp, built a profitable technology company while publicly advocating for 40-hour weeks, no meetings on certain days, and company-wide sabbaticals. He has sustained high performance over two decades while deliberately protecting personal time, and his writing on work-life integration has influenced how thousands of companies operate.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to look up or reflect on. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've found it out).</p>

<div class="assess-group">
<h4>Rewards</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-comp-market">
    <label for="a-comp-market">I know how my total compensation compares to the market rate for my role and experience level.<br><span class="assess-hint">Check Glassdoor, Levels.fyi, or industry salary surveys for your role and location.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-last-raise">
    <label for="a-last-raise">I know when I last received a pay rise or promotion, and whether it kept pace with inflation.<br><span class="assess-hint">Check your employment records or payslips.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-recognition">
    <label for="a-recognition">I have a sense of how often my contributions are recognised by my manager or organisation.<br><span class="assess-hint">Think about the last 6 months – have you received specific, positive feedback on your work?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Competence</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-performance">
    <label for="a-performance">I know my most recent performance rating or how my manager would describe my performance.<br><span class="assess-hint">If you don't have formal reviews, consider what feedback you've received informally.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-skills-gap">
    <label for="a-skills-gap">I can identify the two or three skills that would most improve my effectiveness in my current role.<br><span class="assess-hint">Think about where you struggle, where you spend the most time, or where mistakes happen.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-output">
    <label for="a-output">I have a rough sense of how my output compares to peers in a similar role.<br><span class="assess-hint">Consider speed, quality, and the complexity of work you handle relative to others.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Engagement</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-flow">
    <label for="a-flow">I know roughly how much of my working day I spend in a state of genuine focus or flow.<br><span class="assess-hint">Estimate the percentage of your day where you are deeply absorbed in meaningful work.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-motivation">
    <label for="a-motivation">I can describe whether I am primarily motivated by the work itself, by external rewards, or by neither.<br><span class="assess-hint">Would you do this work if the pay were lower? Do you look forward to the tasks themselves?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-meaning">
    <label for="a-meaning">I have thought about whether my work feels meaningful to me, and if so, why.<br><span class="assess-hint">Meaning can come from the work itself, its impact, the people, or the learning it provides.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Balance</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-hours">
    <label for="a-hours">I know how many hours I actually work in a typical week, including any after-hours checking of messages.<br><span class="assess-hint">Track a normal week honestly – include evening email, weekend work, and commuting time.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-disconnect">
    <label for="a-disconnect">I know whether I can fully disconnect from work in evenings and weekends without anxiety.<br><span class="assess-hint">Consider whether you check messages out of habit, obligation, or genuine need.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-crowding">
    <label for="a-crowding">I have identified whether work is currently crowding out health, relationships, or personal interests.<br><span class="assess-hint">Think about the last month – has work prevented you from exercising, seeing friends, or pursuing hobbies?</span></label>
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

<p>You now understand why current work matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about rewards, competence, engagement, and balance. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/current-work/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Current Work Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Current Work. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/current-work/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'current-work';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-comp-market', 'a-last-raise', 'a-recognition',
        'a-performance', 'a-skills-gap', 'a-output',
        'a-flow', 'a-motivation', 'a-meaning',
        'a-hours', 'a-disconnect', 'a-crowding'
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
