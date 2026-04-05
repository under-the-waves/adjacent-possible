---
layout: default
title: "Consumptive Leisure – Level 1: Awareness"
life_area_slug: consumptive-leisure
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

<h1>Consumptive Leisure: Level 1</h1>

<p class="l1-subtitle">Understand what consumptive leisure means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Consumptive Leisure Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why consumptive leisure matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>The average adult spends <a href="https://www.bls.gov/news.release/atus.nr0.htm" target="_blank">over 5 hours per day</a> on leisure activities, and the majority of that time goes to media consumption &ndash; watching, reading, listening, and browsing. How you spend those hours has a substantial effect on your mood, energy, knowledge, and overall quality of life.</p>

<p>Research consistently shows that not all leisure consumption is equal. A <a href="https://link.springer.com/article/10.1007/s12529-024-10307-0" target="_blank">longitudinal study</a> found that different types of screen-based leisure &ndash; social media, news, video, gaming &ndash; have distinct effects on 24 parameters of wellbeing. Some consumption restores and enriches; some merely fills time; some actively depletes.</p>

<p>The good news is that curating your consumptive leisure is one of the most accessible quality-of-life upgrades available. It requires no special equipment, no major life changes, and no money. It requires only awareness of what you currently consume, what effects it has on you, and what you might choose differently.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about consumptive leisure</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People consume media for different reasons. This site scores every consumptive leisure intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Restoration</h3>
<p>Using leisure consumption to genuinely recover from work and stress. Activities that leave you feeling recharged rather than drained. People who lean towards this value are deliberate about choosing media that provides genuine mental rest, and avoid consumption patterns that feel easy but leave them more depleted than before.</p>

<h3>Enrichment</h3>
<p>Consuming media and content that expands your knowledge, perspectives, and capabilities. Reading non-fiction, watching documentaries, listening to educational podcasts, and engaging with challenging art. People who lean towards this value seek to grow through their leisure and retain what they learn.</p>

<h3>Enjoyment</h3>
<p>The direct pleasure and satisfaction derived from leisure activities. Following curiosity, allowing yourself pure entertainment without guilt, and choosing what genuinely delights you rather than what feels productive. People who lean towards this value recognise that joy is a legitimate end in itself.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each consumptive leisure value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Restoration &ndash; Level 5</div>
    <p><a href="https://www.nytimes.com/by/jenny-odell" target="_blank">Jenny Odell</a> is an artist and author whose book <em>How to Do Nothing</em> became a bestseller on the art of resisting the attention economy. She practises and teaches deliberate disengagement from productivity-driven media consumption, using birdwatching, deep observation, and curated reading as restorative practices. Her work demonstrates mastery of using consumptive leisure for genuine recovery rather than mere distraction.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Enrichment &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Susan_Sontag" target="_blank">Susan Sontag</a> was one of the 20th century's most voracious and deliberate consumers of culture &ndash; film, literature, philosophy, theatre, and visual art. Her journals, published posthumously, reveal someone who treated cultural consumption as a serious practice, maintaining detailed reading lists and viewing schedules from her teenage years until her death in 2004. Her critical essays consistently drew connections across domains in ways that reflected genuinely deep engagement with what she consumed.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Enjoyment &ndash; Level 5</div>
    <p><a href="https://letterboxd.com/about/" target="_blank">Matthew Buchanan</a> co-founded Letterboxd, a social platform for film lovers with over 15 million members. His deep, lifelong love of cinema &ndash; not just watching films but savouring, discussing, and curating them &ndash; led him to build a platform that helps millions of others develop their own relationship with film. He exemplifies how genuine enjoyment of a consumptive medium can become a defining source of meaning.</p>
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
<h4>Restoration</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-energy-after">
    <label for="a-energy-after">I can identify which of my regular leisure activities leave me genuinely recharged versus which leave me feeling drained or sluggish.<br><span class="assess-hint">Think about how you feel after an hour of scrolling versus an hour of reading, for example.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-screen-time">
    <label for="a-screen-time">I know roughly how much screen time I have per day on leisure activities.<br><span class="assess-hint">Check your phone's screen time report or estimate from your typical evening routine.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-wind-down">
    <label for="a-wind-down">I know whether I have a deliberate wind-down routine or whether I default to whatever is easiest when I'm tired.<br><span class="assess-hint">Defaulting is common &ndash; the question is whether you're aware of the pattern.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Enrichment</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-learning-proportion">
    <label for="a-learning-proportion">I have a rough sense of what proportion of my leisure consumption teaches me something valuable versus merely occupies time.<br><span class="assess-hint">Books, podcasts, documentaries, articles &ndash; versus passive scrolling, background television, etc.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-books-per-year">
    <label for="a-books-per-year">I know how many books I finished in the past year.<br><span class="assess-hint">Include audiobooks and e-books. A rough number is fine.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-retention">
    <label for="a-retention">I can recall and explain the main ideas from at least one book, podcast, or documentary I consumed recently.<br><span class="assess-hint">If you can't, that's useful information &ndash; it suggests consumption without retention.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Enjoyment</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-genuine-pleasure">
    <label for="a-genuine-pleasure">I can name 3 &ndash; 5 media sources (shows, podcasts, authors, games, music) that I reliably enjoy.<br><span class="assess-hint">Sources you actively look forward to, not just whatever appears in your feed.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-wasted-time">
    <label for="a-wasted-time">I have a sense of how much of my leisure time I spend on things I don't actually enjoy &ndash; habitual consumption rather than genuine pleasure.<br><span class="assess-hint">Scrolling out of boredom, watching shows you've lost interest in, checking feeds reflexively.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-guilt-free">
    <label for="a-guilt-free">I know whether I can enjoy pure entertainment without guilt, or whether I feel I should always be doing something productive.<br><span class="assess-hint">Some people struggle to watch a film without feeling they're wasting time.</span></label>
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

<p>You now understand why consumptive leisure matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about restoration, enrichment, and enjoyment. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/consumptive-leisure/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Consumptive Leisure Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Consumptive Leisure. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/consumptive-leisure/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'consumptive-leisure';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-energy-after', 'a-screen-time', 'a-wind-down',
        'a-learning-proportion', 'a-books-per-year', 'a-retention',
        'a-genuine-pleasure', 'a-wasted-time', 'a-guilt-free'
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
