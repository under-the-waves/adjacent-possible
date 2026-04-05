---
layout: default
title: "Information Management – Level 1: Awareness"
life_area_slug: information-management
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

<h1>Information Management: Level 1</h1>

<p class="l1-subtitle">Understand what information management is, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Information Management Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why information management matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Most of what you read, hear, and learn disappears within weeks. Research on the <a href="https://en.wikipedia.org/wiki/Forgetting_curve" target="_blank">forgetting curve</a> consistently shows that people lose 70 &ndash; 80% of newly learned information within days unless they take active steps to retain it. For most people, the books they read last year might as well not have been read at all.</p>

<p>The cost goes beyond wasted reading time. Without a reliable way to capture and retrieve information, you end up re-researching the same questions, losing track of useful sources, and making decisions based on whatever happens to be in your head at the time. Surveys of knowledge workers suggest they spend <a href="https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-social-economy" target="_blank">15 &ndash; 30% of their working hours</a> searching for information they have encountered before.</p>

<p>Good information management compounds over time. Each piece of well-organised knowledge makes future learning easier, because you have more existing context to connect new ideas to. People who maintain effective personal knowledge systems tend to develop richer mental models, spot patterns across domains more readily, and make better-informed decisions.</p>

<p>The good news is that even simple, consistent practices &ndash; a reliable place to capture notes, a workable way to find them again &ndash; put you well ahead of most people. You do not need a sophisticated system to see substantial benefits.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about information management</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People manage information for different reasons. This site scores every information management intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Information Retention</h3>
<p>Capturing and preserving valuable insights, ideas, and knowledge from various sources without losing them over time. Comprehensive coverage &ndash; the more you retain, the more valuable your knowledge base becomes. People who lean towards this value focus on broad capture across many sources and contexts, and measure success by how little slips through the cracks.</p>

<h3>Retrieval Efficiency</h3>
<p>Finding the right information quickly when you need it. Having relevant knowledge accessible at decision points is what makes information management valuable for real-world outcomes. People who lean towards this value focus on search capabilities, organisation schemes, and fast access &ndash; and judge their system by how quickly it surfaces what they need.</p>

<h3>Insight Generation</h3>
<p>Connecting ideas across sources to generate new understanding, identify patterns, and develop original thinking. People who lean towards this value focus on systems that help them see relationships between concepts and build coherent mental models. They want their notes to produce ideas they would not have had otherwise.</p>

<h3>System Simplicity</h3>
<p>Preferring approaches that minimise ongoing cognitive overhead and maintenance burden, whether through minimal analogue systems (notebooks, index cards) or highly automated digital setups. People who lean towards this value want their information system to support their thinking without becoming a project unto itself.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each information management value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Information Retention &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Niklas_Luhmann" target="_blank">Niklas Luhmann</a> was a German sociologist who maintained a Zettelkasten (slip-box) of roughly 90,000 index cards over three decades. Each card captured a single idea with cross-references to related cards, allowing him to preserve and connect insights across his entire reading life. He published over 70 books and 400 articles, and attributed much of his productivity to the system's ability to retain and surface ideas that would otherwise have been forgotten. The archive is now <a href="https://niklas-luhmann-archiv.de/bestand/zettelkasten/zettel/ZK_1_NB_1_1_V" target="_blank">digitised and publicly accessible</a>.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Retrieval Efficiency &ndash; Level 5</div>
    <p><a href="https://www.gwern.net/About" target="_blank">Gwern Branwen</a> maintains an extensive personal website covering statistics, psychology, technology, and philosophy, with a sophisticated tagging and cross-linking system. His pages are heavily annotated with sources, and he has described his workflow for rapidly locating prior research across thousands of notes and references. The site functions as a public demonstration of a retrieval system that makes years of accumulated knowledge accessible within seconds.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Insight Generation &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Vannevar_Bush" target="_blank">Vannevar Bush</a> was a scientist and engineer who directed the U.S. Office of Scientific Research and Development during the Second World War. His 1945 essay <a href="https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/" target="_blank">"As We May Think"</a> described the Memex, a hypothetical device for storing and cross-referencing personal knowledge &ndash; effectively anticipating hypertext and personal knowledge management systems decades before they existed. Bush's ability to synthesise insights across electrical engineering, analogue computing, and library science into a coherent vision exemplifies cross-domain insight generation at an exceptional level.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">System Simplicity &ndash; Level 5</div>
    <p><a href="https://rfrfrfr.substack.com/" target="_blank">Robert Greene</a> has described a consistent, low-tech research system he has used across all of his books, including <em>The 48 Laws of Power</em> and <em>Mastery</em>. He reads widely, writes notes on index cards with thematic labels, and sorts them into categories by hand. The system involves no specialised software and has remained essentially unchanged for over 25 years, yet it has supported the synthesis of hundreds of sources per book. Its longevity and simplicity, given the volume of material it handles, make it a strong example of sustainable system design.</p>
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
<h4>Information Retention</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-capture-method">
    <label for="a-capture-method">I know whether I have a consistent method for capturing notes from what I read, watch, or hear.<br><span class="assess-hint">This could be a notebook, an app, marginalia, or nothing at all &ndash; just identify what you currently do.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-retention-rate">
    <label for="a-retention-rate">I have a sense of how much I retain from books or articles I read more than a month ago.<br><span class="assess-hint">Pick something you read recently and try to recall the key points. How much comes back?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-capture-sources">
    <label for="a-capture-sources">I know which information sources I capture from and which I let pass without recording anything.<br><span class="assess-hint">Books, podcasts, conversations, meetings, articles, courses &ndash; where do you take notes, and where don't you?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Retrieval Efficiency</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-find-speed">
    <label for="a-find-speed">I know roughly how long it takes me to find a specific piece of information I've saved before.<br><span class="assess-hint">Think of something you noted down in the past few months. How quickly could you find it right now?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-organisation">
    <label for="a-organisation">I can describe how my notes and files are currently organised (or whether they are organised at all).<br><span class="assess-hint">Folders, tags, chronological order, search-only, scattered across multiple apps &ndash; whatever the reality is.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-reresearch">
    <label for="a-reresearch">I have a sense of how often I end up re-researching something I know I've looked into before.<br><span class="assess-hint">Recipes, product comparisons, technical solutions, factual questions &ndash; anything you've searched for more than once.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Insight Generation</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-connections">
    <label for="a-connections">I can recall a time when connecting ideas from different sources produced a new insight or changed my thinking.<br><span class="assess-hint">This could be a conversation that clicked with something you read, or two articles that illuminated each other.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-review-habit">
    <label for="a-review-habit">I know whether I regularly review or revisit my notes, or whether they sit untouched after being written.<br><span class="assess-hint">Do you ever go back to old notes? Weekly, monthly, never?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-synthesis">
    <label for="a-synthesis">I have a sense of whether my current system helps me think, or whether it is purely for storage.<br><span class="assess-hint">Some systems generate ideas; others just hold them. Which is yours?</span></label>
</div>
</div>

<div class="assess-group">
<h4>System Simplicity</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-maintenance">
    <label for="a-maintenance">I know how much time I spend maintaining my information system each week (if I have one).<br><span class="assess-hint">Filing, tagging, reorganising, migrating between tools &ndash; all of it counts.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-abandoned">
    <label for="a-abandoned">I can count how many information management tools or systems I've tried and abandoned.<br><span class="assess-hint">Apps, notebooks, methods &ndash; anything you started with good intentions and stopped using.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-friction">
    <label for="a-friction">I have a sense of whether my current approach feels sustainable or whether it creates friction I tend to avoid.<br><span class="assess-hint">Do you skip capturing things because the process feels like too much effort?</span></label>
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

<p>You now understand why information management matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about information retention, retrieval efficiency, insight generation, and system simplicity. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/information-management/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Information Management Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Information Management. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/information-management/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'information-management';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-capture-method', 'a-retention-rate', 'a-capture-sources',
        'a-find-speed', 'a-organisation', 'a-reresearch',
        'a-connections', 'a-review-habit', 'a-synthesis',
        'a-maintenance', 'a-abandoned', 'a-friction'
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
