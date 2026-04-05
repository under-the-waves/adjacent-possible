---
layout: default
title: "Communication – Level 1: Awareness"
life_area_slug: communication
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

<h1>Communication: Level 1</h1>

<p class="l1-subtitle">Understand what communication means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Communication Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why communication matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Communication is the medium through which almost everything in your life happens. Every relationship, every collaboration, every negotiation, and every conflict runs on it. Improving how you communicate has an unusually broad impact because it touches so many domains at once.</p>

<p>The evidence for its importance is consistent across contexts. Employers rank communication as the <a href="https://www.naceweb.org/talent-acquisition/candidate-selection/key-attributes-employers-want-to-see-on-students-resumes/" target="_blank">most sought-after skill</a> in job candidates across industries. People with strong interpersonal skills experience <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4968942/" target="_blank">less loneliness</a> and build deeper social networks. An estimated <a href="https://haiilo.com/blog/top-internal-communication-statistics/" target="_blank">86% of workplace failures</a> are attributed to poor communication or collaboration.</p>

<p>Communication is also unusually trainable. Unlike personality traits, which are relatively stable, specific communication skills – listening, structuring arguments, managing conflict, reading a room – respond well to deliberate practice. Small improvements compound quickly because you use these skills dozens of times a day.</p>

<p>Roughly 75% of people experience public speaking anxiety, and fewer than 5% communicate assertively in everyday situations. This means that even moderate competence puts you well above the median.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about communication</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People develop their communication for different reasons. This site scores every communication intervention across four core values. Later, you'll set your own weighting across these values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Influence</h3>
<p>The ability to persuade others, drive decisions, and create change through your communication. People who lean towards this value focus on strategic messaging, understanding what motivates different audiences, and developing the credibility and presence needed to shape outcomes.</p>

<h3>Connection</h3>
<p>Building genuine relationships, emotional intimacy, and mutual understanding through communication. People who lean towards this value focus on listening deeply, sharing vulnerably, and creating the emotional safety that allows relationships to flourish over time.</p>

<h3>Performance</h3>
<p>Excelling in high-stakes or formal communication situations – public speaking, presentations, job interviews, media appearances. People who lean towards this value develop skills specifically for moments when communication performance directly impacts important outcomes.</p>

<h3>Conflict Navigation</h3>
<p>Handling disagreements, difficult conversations, and interpersonal tensions constructively while maintaining relationships. People who lean towards this value become comfortable with necessary tension and develop frameworks for working through differences without damaging bonds.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each communication value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Influence &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/William_Ury" target="_blank">William Ury</a> co-founded the Harvard Program on Negotiation and co-authored <em>Getting to Yes</em>, one of the most widely read books on negotiation. He has mediated conflicts between corporations, governments, and ethnic groups on five continents, and his frameworks for principled negotiation have shaped how millions of people approach persuasion and deal-making.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Connection &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Terry_Gross" target="_blank">Terry Gross</a> has hosted <em>Fresh Air</em> on NPR since 1975, conducting thousands of interviews across nearly five decades. She is widely regarded as one of the most skilled interviewers alive – guests routinely disclose things to her they have never shared publicly, citing her deep listening and genuine curiosity as the reason.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Performance &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Hans_Rosling" target="_blank">Hans Rosling</a> was a Swedish physician and statistician whose TED talks have been viewed over 35 million times. He used animated data visualisations and physical props to make global health statistics compelling and memorable. His presentations consistently changed audience beliefs about world poverty and development &ndash; measurably, as he tested audiences before and after. He maintained this level of public communication for over a decade until his death in 2017.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Conflict Navigation &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/George_J._Mitchell" target="_blank">George Mitchell</a> chaired the Northern Ireland peace negotiations that produced the 1998 Good Friday Agreement, ending three decades of sectarian violence. Participants on all sides credited his patience, impartiality, and skill at finding common ground in situations where others saw none. He later served as US special envoy for Middle East peace.</p>
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
<h4>Influence</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-persuade">
    <label for="a-persuade">I can think of a recent situation where I tried to persuade someone and know whether it worked.<br><span class="assess-hint">A meeting, negotiation, request, or argument where you wanted someone to change their mind or take action.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-ideas-adopted">
    <label for="a-ideas-adopted">I have a sense of how often my ideas get adopted in group discussions at work or in my social circle.<br><span class="assess-hint">Do people generally act on your suggestions, or do your points tend to get talked over?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-audience">
    <label for="a-audience">I know whether I adjust how I communicate depending on who I'm talking to.<br><span class="assess-hint">Do you speak differently to your manager, your friends, and a stranger? Or roughly the same way?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Connection</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-deep-conv">
    <label for="a-deep-conv">I know how often I have conversations that go beyond small talk in a typical week.<br><span class="assess-hint">Conversations where you discuss something personal, meaningful, or emotionally honest.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-listening">
    <label for="a-listening">I have a sense of whether I'm a good listener or tend to wait for my turn to speak.<br><span class="assess-hint">Do people seek you out to talk through problems? Do you remember details from past conversations?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-vulnerable">
    <label for="a-vulnerable">I know how comfortable I am sharing personal feelings or admitting uncertainty.<br><span class="assess-hint">Can you say "I don't know" or "I'm struggling with this" to people you trust?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Performance</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-public-speaking">
    <label for="a-public-speaking">I know my comfort level with speaking in front of a group.<br><span class="assess-hint">Could you give a five-minute presentation to 10 people tomorrow? Would anxiety interfere?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-writing">
    <label for="a-writing">I have a sense of how clearly I write when it matters – emails, reports, or messages to people I don't know well.<br><span class="assess-hint">Do people ask you to clarify what you meant, or do they usually understand first time?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Conflict Navigation</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-conflict-pattern">
    <label for="a-conflict-pattern">I know whether I tend to avoid difficult conversations, confront them head-on, or something in between.<br><span class="assess-hint">Think about the last time you disagreed with someone. Did you raise it, let it go, or escalate?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-apologise">
    <label for="a-apologise">I know whether I find it easy or hard to apologise when I'm wrong.<br><span class="assess-hint">Can you say "I was wrong about that" without it feeling like a threat to your identity?</span></label>
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

<p>You now understand why communication matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about influence, connection, performance, and conflict navigation. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/communication/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Communication Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Communication. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/communication/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'communication';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-persuade', 'a-ideas-adopted', 'a-audience',
        'a-deep-conv', 'a-listening', 'a-vulnerable',
        'a-public-speaking', 'a-writing',
        'a-conflict-pattern', 'a-apologise'
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
