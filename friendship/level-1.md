---
layout: default
title: "Friendship – Level 1: Awareness"
life_area_slug: friendship
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

<h1>Friendship: Level 1</h1>

<p class="l1-subtitle">Understand what friendship means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Friendship Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why friendship matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Friendship is one of the strongest predictors of wellbeing across the lifespan. A <a href="https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000316" target="_blank">meta-analysis of 148 studies</a> covering over 300,000 people found that those with strong social relationships had a 50% higher likelihood of survival over a given follow-up period. The health risk of weak social ties is comparable to smoking 15 cigarettes a day and exceeds the risks associated with obesity or physical inactivity.</p>

<p>The benefits extend well beyond physical health. A <a href="https://www.pewresearch.org/short-reads/2023/10/12/what-does-friendship-look-like-in-america/" target="_blank">2023 Pew Research survey</a> found that 61% of US adults consider close friendships extremely or very important for a fulfilling life &ndash; a higher proportion than for marriage (23%), having children (26%), or having money (24%). Longitudinal research on cognitive ageing suggests that <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7483134/" target="_blank">frequent contact with friends</a> is associated with slower cognitive decline, and the effect appears to be stronger for friends than for family members.</p>

<p>Despite this, friendship is in decline across much of the developed world. The percentage of American adults reporting no close friends tripled from 3% in 1990 to 12% in 2021, while those with ten or more close friends fell from 33% to 13%. Similar trends have been documented in the UK, Australia, and Japan. This means that even modest investment in friendship puts you ahead of a growing portion of the population.</p>

<p>Friendship also compounds over time. Research on social capital consistently finds that the longest-standing friendships provide the most emotional support, the broadest access to information and opportunities, and the strongest buffer against stress. Starting early and maintaining friendships matters more than having many of them at any one point.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about friendship</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue friendship for different reasons. This site scores every friendship intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Depth</h3>
<p>Close friendships built on high trust, vulnerability, and mutual understanding. People who lean towards this value invest heavily in a smaller number of relationships where they can share honestly, rely on each other during difficult periods, and feel fully known. Depth tends to require regular one-on-one time, emotional availability, and a willingness to have hard conversations.</p>

<h3>Breadth</h3>
<p>A diverse network of friendships spanning different contexts, communities, and walks of life. People who lean towards this value enjoy meeting new people, maintaining ties across settings &ndash; work, hobbies, neighbourhoods, online communities &ndash; and connecting others who might benefit from knowing each other. Breadth brings access to varied perspectives, information, and social opportunities.</p>

<h3>Growth</h3>
<p>Friendships that challenge you to improve, learn, and develop as a person. People who lean towards this value seek out friends who hold them accountable, introduce them to new ideas, give honest feedback, and push them beyond their comfort zone. Growth-oriented friendships often centre on shared projects, intellectual discussion, or mutual goal-setting.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each friendship value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Depth &ndash; Level 5</div>
    <p><a href="https://www.cs-lewis.com/biography/" target="_blank">C.S. Lewis</a> and <a href="https://www.tolkiensociety.org/author/biography/" target="_blank">J.R.R. Tolkien</a> met at Oxford in 1926 and remained close friends for over 30 years through the Inklings, a literary group that met weekly to read and critique each other's work. Tolkien was instrumental in Lewis's conversion to Christianity &ndash; a pivotal moment in Lewis's life. Lewis, in turn, provided years of encouragement that kept Tolkien working on <em>The Lord of the Rings</em> during long periods of doubt. Their friendship weathered significant disagreements, including over Lewis's marriage and theological differences, and both men described it as one of the most important relationships of their lives.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Breadth &ndash; Level 5</div>
    <p><a href="https://keithferrazzi.com/" target="_blank">Keith Ferrazzi</a> built a career around the deliberate practice of relationship-building. His book <em>Never Eat Alone</em> describes his system for maintaining genuine connections with thousands of people across industries and countries. Ferrazzi appears to treat relationship maintenance as a structured discipline &ndash; tracking contacts, reaching out regularly, and actively looking for ways to help people in his network before asking for anything in return. He is widely cited as an example of someone who combines very large social networks with authentic personal investment in each connection.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Growth &ndash; Level 5</div>
    <p><a href="https://www.fi.edu/en/benjamin-franklin" target="_blank">Benjamin Franklin</a> founded the Junto in 1727, a mutual improvement club of 12 friends drawn from different trades in Philadelphia. Members met weekly to discuss questions of morals, politics, and natural philosophy, and held each other accountable to personal development goals. The group ran for over 30 years and generated several lasting civic institutions, including a lending library that became the Library Company of Philadelphia and an academy that eventually became the University of Pennsylvania. Franklin credited the Junto with shaping much of his intellectual development.</p>
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
<h4>Depth</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-close-count">
    <label for="a-close-count">I know how many friends I could call at 2 a.m. with a genuine emergency and be confident they would pick up.<br><span class="assess-hint">Think through your contacts and count the people you would actually ring in a crisis.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-vulnerability">
    <label for="a-vulnerability">I know whether I have shared something genuinely personal or difficult with a friend in the past month.<br><span class="assess-hint">Something beyond surface-level updates &ndash; a worry, a failure, an uncertainty about the future.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-one-on-one">
    <label for="a-one-on-one">I know how often I spend one-on-one time with a close friend in a typical month.<br><span class="assess-hint">In person, on the phone, or on a video call &ndash; but with enough time for real conversation, not just brief messages.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Breadth</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-contexts">
    <label for="a-contexts">I can name the different contexts where I currently have friends (e.g. work, hobbies, neighbourhood, university, online).<br><span class="assess-hint">List each context and roughly how many friends you have in it.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-new-people">
    <label for="a-new-people">I know when I last made a new friend &ndash; someone I now see or speak to regularly who wasn't in my life a year ago.<br><span class="assess-hint">Think about whether your social circle has grown, shrunk, or stayed the same recently.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-diversity">
    <label for="a-diversity">I know whether my friends are mostly similar to me in age, background, and interests, or whether there is real variety.<br><span class="assess-hint">Consider age range, professions, cultural backgrounds, and how they spend their time.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Growth</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-feedback">
    <label for="a-feedback">I know whether any of my friends have given me honest, constructive feedback in the past six months.<br><span class="assess-hint">Feedback on your work, your behaviour, your decisions &ndash; something that helped you see a blind spot.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-learning">
    <label for="a-learning">I can identify a specific thing I have learned or a way I have changed because of a friend's influence.<br><span class="assess-hint">A book they recommended, a habit you picked up, a perspective they shifted.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-accountability">
    <label for="a-accountability">I know whether I have any friend who holds me accountable to a goal, standard, or commitment.<br><span class="assess-hint">Someone who checks in on your progress, calls you out when you slack, or shares a goal with you.</span></label>
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

<p>You now understand why friendship matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about depth, breadth, and growth. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/friendship/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Friendship Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Friendship. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/friendship/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'friendship';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-close-count', 'a-vulnerability', 'a-one-on-one',
        'a-contexts', 'a-new-people', 'a-diversity',
        'a-feedback', 'a-learning', 'a-accountability'
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
