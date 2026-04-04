---
layout: default
title: "Sleep – Level 1: Awareness"
life_area_slug: sleep
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

<h1>Sleep: Level 1</h1>

<p class="l1-subtitle">Understand what sleep does, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Sleep Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why sleep matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Sleep occupies roughly a third of your life, and what happens during those hours shapes nearly everything about the other two-thirds. The evidence for its importance is broad and consistent across decades of research.</p>

<p>Adults who regularly sleep fewer than seven hours have a <a href="https://pubmed.ncbi.nlm.nih.gov/28364328/" target="_blank">13% higher risk</a> of dying from any cause. Short sleep is independently linked to heart disease, type 2 diabetes, obesity, and depression. The relationship between sleep and health runs in both directions: poor sleep worsens chronic conditions, and chronic conditions worsen sleep.</p>

<p>The effects on daily performance are equally striking. After <a href="https://pubmed.ncbi.nlm.nih.gov/10984335/" target="_blank">17 – 19 hours without sleep</a>, reaction time and decision-making deteriorate to levels comparable to a blood alcohol concentration of 0.05%. Cumulative sleep restriction over two weeks – sleeping six hours a night instead of eight – produces <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2656292/" target="_blank">cognitive impairment equivalent to two nights of total sleep deprivation</a>, and people consistently underestimate how impaired they are.</p>

<p>Sleep also consolidates memory, regulates appetite hormones, supports immune function, and affects emotional resilience. Few other behaviours touch as many systems simultaneously, and unlike many health interventions, improving sleep often produces noticeable benefits within days.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about sleep</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People improve their sleep for different reasons. This site scores every sleep intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Daily Functioning</h3>
<p>Mental alertness, energy levels, focus, mood stability, and physical recovery. People who lean towards this value want sleep that makes them feel sharp and capable the next day. They tend to care most about waking refreshed, sustaining concentration through the afternoon, and having steady energy without relying on caffeine.</p>

<h3>Long-term Health</h3>
<p>Disease prevention, longevity, and brain health over years and decades. People who lean towards this value treat sleep as a long-term investment. They focus on consistent duration, sleep architecture (the balance of deep and REM sleep), and reducing the cumulative health risks that come from chronic sleep debt.</p>

<h3>Comfort & Experience</h3>
<p>The subjective quality of sleep itself – how easily you fall asleep, whether you stay asleep through the night, and how pleasant the experience feels. People who lean towards this value care about the sleep environment, bedtime routines, and waking without an alarm. They want sleep to feel good, not just be adequate.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each sleep value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Daily Functioning &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/LeBron_James" target="_blank">LeBron James</a> averages around 10 &ndash; 12 hours of sleep per day, split between 8 &ndash; 9 hours at night and a 2 &ndash; 3 hour afternoon nap. He keeps his bedroom at 20 &ndash; 21&deg;C, completely dark, and avoids screens for 45 minutes before bed. He has called sleep "the best way for your body to physically and emotionally recover and get back to 100 percent." He seems to have maintained this routine throughout a 21-season NBA career, playing at a high level into his early 40s.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Long-term Health &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Tom_Brady" target="_blank">Tom Brady</a> went to bed at 8:30 pm and slept at least 9 hours a night for most of his professional career, treating sleep as a central pillar of his TB12 Method alongside nutrition and training. He played in the NFL until age 45, winning his seventh Super Bowl at 43 &ndash; an age at which most players have been retired for over a decade. By all accounts, his sleep discipline was non-negotiable rather than aspirational.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Comfort &amp; Experience &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Roger_Federer" target="_blank">Roger Federer</a> slept 10 &ndash; 12 hours a day throughout his professional tennis career and has said that "if I don't sleep 11 to 12 hours per day, it's not right." He appears to have genuinely enjoyed sleep as an experience rather than treating it purely as recovery, and maintained a 24-year career at the top of professional tennis. Few athletes have spoken about sleep with the same combination of volume and evident satisfaction.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few days to observe. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've found it out).</p>

<div class="assess-group">
<h4>Daily Functioning</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-wake-refreshed">
    <label for="a-wake-refreshed">I know how often I wake up feeling genuinely refreshed and alert.<br><span class="assess-hint">Think about the past two weeks. Most days? Some days? Rarely?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-afternoon-energy">
    <label for="a-afternoon-energy">I know whether I typically experience an afternoon energy dip that affects my focus.<br><span class="assess-hint">A mild dip is normal. Think about whether it regularly disrupts your work or concentration.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-caffeine-dependence">
    <label for="a-caffeine-dependence">I know how much caffeine I consume and how late in the day I have it.<br><span class="assess-hint">Count coffees, teas, energy drinks, and soft drinks. Note the time of your last one each day.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Long-term Health</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-sleep-duration">
    <label for="a-sleep-duration">I know how many hours I typically sleep on weeknights and weekends.<br><span class="assess-hint">Check your phone's screen time or a sleep tracker, or estimate from when you get into bed and when you get up.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-sleep-consistency">
    <label for="a-sleep-consistency">I know how consistent my bedtime and wake time are across the week.<br><span class="assess-hint">A difference of more than an hour between weekday and weekend times counts as inconsistent.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-snoring">
    <label for="a-snoring">I know whether I snore, gasp, or stop breathing during sleep.<br><span class="assess-hint">Ask a partner or housemate, or use a phone app that records audio overnight. This can indicate sleep apnoea.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Comfort & Experience</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-fall-asleep-time">
    <label for="a-fall-asleep-time">I know roughly how long it takes me to fall asleep on a typical night.<br><span class="assess-hint">Under 10 minutes may suggest you're overtired. Over 30 minutes may suggest difficulty winding down. 10 – 20 minutes is typical.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-night-waking">
    <label for="a-night-waking">I know how often I wake during the night and whether I can get back to sleep easily.<br><span class="assess-hint">Once or twice briefly is normal. Lying awake for 20+ minutes is worth noting.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-sleep-environment">
    <label for="a-sleep-environment">I know the temperature, light level, and noise level in my bedroom at night.<br><span class="assess-hint">Is the room dark enough? Cool enough? Quiet enough? Can you identify specific issues?</span></label>
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

<p>You now understand why sleep matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about daily functioning, long-term health, and comfort and experience. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/sleep/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Sleep Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Sleep. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/sleep/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'sleep';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-wake-refreshed', 'a-afternoon-energy', 'a-caffeine-dependence',
        'a-sleep-duration', 'a-sleep-consistency', 'a-snoring',
        'a-fall-asleep-time', 'a-night-waking', 'a-sleep-environment'
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
