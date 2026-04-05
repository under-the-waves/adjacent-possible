---
layout: default
title: "Networks – Level 1: Awareness"
life_area_slug: networks
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

<h1>Networks: Level 1</h1>

<p class="l1-subtitle">Understand what professional networks mean, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Networks Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why networks matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Professional networks are one of the strongest predictors of career outcomes. An estimated <a href="https://www.apollotechnical.com/networking-statistics/" target="_blank">85% of jobs are filled through networking</a>, and 70% are never publicly posted. Referral candidates are <a href="https://www.zippia.com/advice/networking-statistics/" target="_blank">four times more likely</a> to receive an interview and are hired up to 70% faster.</p>

<p>The information advantage is equally important. A landmark MIT study using LinkedIn data found that <a href="https://www.science.org/doi/10.1126/science.abl4476" target="_blank">moderately weak ties</a> – casual acquaintances rather than close contacts – had the greatest impact on job mobility, because they connect you to networks that do not overlap with your own.</p>

<p>Despite 80% of professionals considering networking important, most people network reactively – reaching out only when they need something. Deliberate, sustained network building is uncommon and disproportionately rewarded. The difference between a passive and an active networker compounds over years into dramatically different career trajectories.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about networks</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People build professional networks for different reasons. This site scores every networks intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Depth</h3>
<p>The quality and strength of key professional relationships – trusted advisors, mentors, collaborators, and allies who genuinely understand your work and advocate for you. People who lean towards this value cultivate a smaller number of high-value relationships, investing time in deepening trust and providing genuine value.</p>

<h3>Breadth</h3>
<p>The range and diversity of your professional network – connections across different industries, roles, seniority levels, and backgrounds. People who lean towards this value actively expand their circle, maintain weak ties, and ensure their network provides access to diverse information and opportunities.</p>

<h3>Relevance</h3>
<p>Ensuring your network connections are aligned with your current and future professional direction. People who lean towards this value regularly evaluate whether their network serves their goals, prune connections that no longer add value, and deliberately build relationships in areas where they are heading.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each networks value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Depth &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Esther_Dyson" target="_blank">Esther Dyson</a> has maintained deep professional relationships with technology founders, investors, and policymakers for over 40 years. She was an early investor in Flickr, del.icio.us, and 23andMe, in each case building on years of genuine relationships with the founders. She is known for maintaining a small number of close professional ties that she invests in deeply over decades rather than collecting contacts.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Breadth &ndash; Level 5</div>
    <p><a href="https://rfreedman.org/" target="_blank">Reid Hoffman</a> co-founded LinkedIn and built a professional network spanning technology, venture capital, politics, media, and academia. He is known for connecting people across industries and geographies, and his network routinely surfaces emerging opportunities, talent, and ideas before they become widely known. His book <em>The Start-up of You</em> codified his approach to network building.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Relevance &ndash; Level 5</div>
    <p><a href="https://www.ycombinator.com/people/michael-seibel" target="_blank">Michael Seibel</a>, CEO of Y Combinator, has built a network that evolves in precise alignment with his professional direction. As he moved from founding Justin.tv (later Twitch) to leading YC, his network shifted from media and gaming to early-stage startups, ensuring that his connections anticipate where he is heading and proactively surface relevant founders and opportunities.</p>
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
<h4>Depth</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-strong-ties">
    <label for="a-strong-ties">I can name the professional contacts who would actively recommend or advocate for me if asked.<br><span class="assess-hint">Think about who would take a phone call from a hiring manager on your behalf.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-mentor-sponsor">
    <label for="a-mentor-sponsor">I know whether I currently have a mentor or sponsor in my professional life.<br><span class="assess-hint">A mentor gives advice; a sponsor advocates for you in rooms you're not in. Both count.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-reciprocity">
    <label for="a-reciprocity">I have thought about what I offer to my strongest professional relationships, not just what I receive.<br><span class="assess-hint">Introductions, expertise, feedback, emotional support – value flows both ways.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Breadth</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-network-size">
    <label for="a-network-size">I have a rough sense of the size of my professional network and how many contexts it spans.<br><span class="assess-hint">Count separate professional contexts: current work, previous roles, industry groups, alumni networks, conferences.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-diversity">
    <label for="a-diversity">I know whether my network is concentrated in one industry or role, or spans multiple areas.<br><span class="assess-hint">Check your LinkedIn connections by industry – are 90% in the same field?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-new-connections">
    <label for="a-new-connections">I know roughly how often I make meaningful new professional connections.<br><span class="assess-hint">Count the last 6 months – how many new people have you had a substantive conversation with?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Relevance</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-alignment">
    <label for="a-alignment">I have assessed whether my current network connections are aligned with where my career is heading.<br><span class="assess-hint">Are most of your strong connections in areas relevant to your future, or mainly from your past?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-gaps">
    <label for="a-gaps">I can identify the industries, roles, or seniority levels where I lack connections but would benefit from them.<br><span class="assess-hint">Think about your career goals – who would you need to know to reach them?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-maintenance">
    <label for="a-maintenance">I have a sense of how actively I maintain my existing professional relationships.<br><span class="assess-hint">When did you last reach out to a former colleague or professional contact without needing something?</span></label>
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

<p>You now understand why networks matter, what different people get out of them, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about depth, breadth, and relevance. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/networks/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Networks Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Networks. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/networks/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'networks';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-strong-ties', 'a-mentor-sponsor', 'a-reciprocity',
        'a-network-size', 'a-diversity', 'a-new-connections',
        'a-alignment', 'a-gaps', 'a-maintenance'
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
        if (document.activeElement !== cb) {
            cb.checked = !cb.checked;
        }
        el.classList.toggle('checked', cb.checked);

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
