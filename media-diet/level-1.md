---
layout: default
title: "Media Diet – Level 1: Awareness"
life_area_slug: media-diet
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

<h1>Media Diet: Level 1</h1>

<p class="l1-subtitle">Understand what a media diet is, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Media Diet Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why your media diet matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>The information you consume shapes how you understand the world, the decisions you make, and the quality of your thinking. Yet most people's information intake is determined largely by algorithms and habit rather than deliberate choice.</p>

<p>The average knowledge worker checks email <a href="https://hbr.org/2019/01/how-to-spend-way-less-time-on-email-every-day" target="_blank">every six minutes</a> and spends a substantial portion of the day processing fragmented information. Research suggests that this reactive consumption pattern <a href="https://www.sciencedirect.com/science/article/abs/pii/S0747563217305216" target="_blank">increases anxiety</a> and reduces the capacity for sustained attention, without proportionally improving understanding.</p>

<p>People who intentionally curate their information sources tend to develop more accurate mental models, make better predictions, and experience less cognitive fatigue. Philip Tetlock's research on <a href="https://press.princeton.edu/books/hardcover/9780691175904/superforecasting" target="_blank">superforecasters</a> found that the best predictors consume information from diverse, high-quality sources and actively seek out viewpoints that challenge their assumptions.</p>

<p>A well-constructed media diet also compounds over time. The sources you choose today shape the frameworks you use to interpret new information for years. Few other habits have such a broad and lasting influence on your intellectual development.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about media diet</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People curate their information consumption for different reasons. This site scores every media diet intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Information Quality & Depth</h3>
<p>The accuracy, nuance, and intellectual rigour of consumed information. Prioritising books over articles, primary sources over summaries, expert analysis over hot takes, and comprehensive coverage over fragmented updates. People who lean towards this value invest time in fewer, higher-quality sources that provide deep understanding.</p>

<h3>Actionable Relevance</h3>
<p>How directly the information supports decision-making and practical outcomes in your life. Career-relevant developments, investment insights, health discoveries, and information that changes behaviour or choices. Those who lean towards this value curate their consumption around information with clear utility for their specific circumstances and goals.</p>

<h3>Breadth & Discovery</h3>
<p>Exposure to diverse perspectives, unexpected insights, and information outside your existing knowledge areas. Following curiosity into unfamiliar domains, consuming content from different cultural perspectives, and maintaining intellectual openness to ideas that might reshape your thinking. People who lean towards this value deliberately seek out information that challenges assumptions and expands mental models.</p>

<h3>Cognitive Efficiency</h3>
<p>Optimising the retention-to-effort ratio and minimising cognitive overhead from information consumption. Choosing formats that match your processing style, avoiding redundant coverage, and consuming information at optimal timing and frequency. Those who lean towards this value focus on maximum informational value with minimal mental fatigue or wasted attention.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each media diet value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Information Quality & Depth &ndash; Level 5</div>
    <p><a href="https://tylercowen.com/" target="_blank">Tyler Cowen</a> is an economics professor at George Mason University who reads roughly 50 &ndash; 80 books per year across economics, history, fiction, science, and philosophy. He maintains <a href="https://marginalrevolution.com/" target="_blank">Marginal Revolution</a>, where he has published daily posts synthesising academic papers, policy documents, and primary sources for over twenty years. His reading method &ndash; skimming aggressively, abandoning books quickly, and focusing retention on what changes his thinking &ndash; reflects an unusually disciplined approach to information quality.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Actionable Relevance &ndash; Level 5</div>
    <p><a href="https://patrickcollison.com/" target="_blank">Patrick Collison</a>, co-founder of Stripe, maintains a public bookshelf and has spoken extensively about how his reading directly informs business and policy decisions. His information diet spans economic history, infrastructure development, and scientific progress, and he has described specific cases where insights from these domains shaped Stripe's strategy. His reading appears tightly integrated with his decision-making rather than pursued as a separate activity.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Breadth & Discovery &ndash; Level 5</div>
    <p><a href="https://www.mariapopova.com/" target="_blank">Maria Popova</a> created <a href="https://www.themarginalian.org/" target="_blank">The Marginalian</a> (formerly Brain Pickings), where she has published daily essays connecting ideas across philosophy, science, art, literature, and psychology for over fifteen years. Her work draws on sources spanning centuries and disciplines, and she reads in multiple languages. The site is a public record of an exceptionally broad and sustained information diet.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Cognitive Efficiency &ndash; Level 5</div>
    <p><a href="https://calnewport.com/" target="_blank">Cal Newport</a> is a computer science professor at Georgetown who has written extensively about attention management and deep work. He does not use social media, limits his news consumption to a small number of curated sources, and has described specific systems for batching information processing and protecting cognitive resources. His academic output &ndash; multiple books and a consistent research programme &ndash; suggests these practices translate into measurable productivity.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to look up or reflect on. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've thought about it).</p>

<div class="assess-group">
<h4>Information Quality & Depth</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-source-types">
    <label for="a-source-types">I know roughly what proportion of my information comes from long-form sources (books, in-depth articles, documentaries) versus short-form (social media, news headlines, notifications).<br><span class="assess-hint">Estimate the split over a typical week.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-books-read">
    <label for="a-books-read">I know how many non-fiction books I read in the past year.<br><span class="assess-hint">Include audiobooks if you use them. An approximate count is fine.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-primary-sources">
    <label for="a-primary-sources">I can think of at least one topic where I've read a primary source rather than relying on summaries or commentary.<br><span class="assess-hint">Academic papers, original reports, legislation, company filings &ndash; anything unfiltered.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Actionable Relevance</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-decision-influence">
    <label for="a-decision-influence">I can identify at least one decision I made in the past year that was directly influenced by something I read or listened to.<br><span class="assess-hint">Career moves, financial choices, health changes, relationship approaches &ndash; anything concrete.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-goal-alignment">
    <label for="a-goal-alignment">I have a sense of whether my current information sources align with my actual goals and priorities.<br><span class="assess-hint">Compare what you consume most with what you're trying to achieve.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-noise-ratio">
    <label for="a-noise-ratio">I can estimate how much of my weekly information consumption has no practical application to my life.<br><span class="assess-hint">Content that's interesting but doesn't inform any decision or skill.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Breadth & Discovery</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-echo-chamber">
    <label for="a-echo-chamber">I know whether most of my information sources share a similar political or cultural perspective.<br><span class="assess-hint">Think about the range of viewpoints across your regular sources.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-unfamiliar-topics">
    <label for="a-unfamiliar-topics">I can recall the last time I deliberately explored a topic I knew nothing about.<br><span class="assess-hint">Not something recommended by an algorithm &ndash; something you chose out of curiosity.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-international">
    <label for="a-international">I know whether I regularly consume information from sources based outside my own country.<br><span class="assess-hint">News outlets, commentators, or publications from other regions.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Cognitive Efficiency</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-time-spent">
    <label for="a-time-spent">I know roughly how many hours per day I spend consuming news, social media, and informational content.<br><span class="assess-hint">Screen time data on your phone can help here.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-retention">
    <label for="a-retention">I have a sense of how much I retain from what I consume &ndash; could I summarise the most important thing I read last week?<br><span class="assess-hint">Try it now. If nothing comes to mind, that's useful information.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-overload">
    <label for="a-overload">I know whether I regularly experience information overload or feel anxious about keeping up with the news.<br><span class="assess-hint">A sense of falling behind, compulsive checking, or fatigue from too much input.</span></label>
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

<p>You now understand why your media diet matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about information quality, actionable relevance, breadth, and cognitive efficiency. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/media-diet/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Media Diet Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Media Diet. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/media-diet/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'media-diet';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-source-types', 'a-books-read', 'a-primary-sources',
        'a-decision-influence', 'a-goal-alignment', 'a-noise-ratio',
        'a-echo-chamber', 'a-unfamiliar-topics', 'a-international',
        'a-time-spent', 'a-retention', 'a-overload'
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
