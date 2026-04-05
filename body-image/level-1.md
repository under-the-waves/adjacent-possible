---
layout: default
title: "Body Image – Level 1: Awareness"
life_area_slug: body-image
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

<h1>Body Image: Level 1</h1>

<p class="l1-subtitle">Understand what body image means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Body Image Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why body image matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Body image &ndash; how you perceive, feel about, and present your physical self &ndash; has a measurable effect on wellbeing. Research by <a href="https://doi.org/10.1016/B978-012167053-8/50004-8" target="_blank">Thomas Cash</a> found that roughly a quarter of our self-esteem is determined by how positively we view our bodies.</p>

<p>The effects extend well beyond self-esteem. Body dissatisfaction is a <a href="https://doi.org/10.1037/0022-006X.70.1.103" target="_blank">significant risk factor</a> for eating disorders and is associated with higher levels of depression and anxiety. People with poor body image are more likely to withdraw from social situations, avoid physical activities, and limit intimate relationships.</p>

<p>Conversely, positive body image enhances social confidence and life engagement. People who feel comfortable in their bodies are more willing to try new activities, form relationships, and present themselves authentically. Few aspects of self-perception touch as many areas of daily life.</p>

<p>Body image encompasses body composition, skin health, hair quality, posture, grooming, and body language &ndash; the physical impression you make without clothing considerations. It overlaps with but is distinct from <a href="{{ site.baseurl }}/style/">style</a>, which covers clothing and visual presentation, and <a href="{{ site.baseurl }}/fitness/">fitness</a>, which covers what your body can do.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about body image</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People care about body image for different reasons. This site scores every body image intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Youthfulness & Vitality</h3>
<p>Maintaining or enhancing a youthful, energetic appearance through body condition and grooming. People who lean towards this value focus on skin health, hair quality, posture, and energy levels &ndash; interventions that make them look and feel younger, healthier, and more vibrant over time.</p>

<h3>Romantic Appeal</h3>
<p>Developing physical attractiveness and body language that appeals to potential or current romantic partners. People who lean towards this value focus on body composition, grooming standards, confident movement, and physical presence in romantic contexts.</p>

<h3>Weight Management</h3>
<p>Achieving desired changes in body composition, whether gaining muscle mass, losing body fat, or maintaining current weight. People who lean towards this value focus on reaching specific body composition goals that serve both aesthetic and functional purposes.</p>

<h3>Body Confidence</h3>
<p>Feeling comfortable, at home, and confident in your own body regardless of changes. People who lean towards this value focus on improving their relationship with their body &ndash; body acceptance, posture, confident movement, and reduced body-related anxiety &ndash; rather than necessarily changing it.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each body image value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Youthfulness & Vitality &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Cate_Blanchett" target="_blank">Cate Blanchett</a> has maintained a notably youthful appearance and high energy through her 50s whilst sustaining a demanding career. She is frequently cited for her skin quality, posture, and vitality, and has spoken publicly about prioritising sleep, sun protection, and consistent skincare over cosmetic procedures.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Romantic Appeal &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/David_Beckham" target="_blank">David Beckham</a> has maintained strong physical presence and grooming standards from his 20s into his late 40s, adapting his presentation across decades whilst remaining widely regarded as physically attractive. His attention to body composition, grooming, and confident body language has remained consistent through major life transitions.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Weight Management &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Hugh_Jackman" target="_blank">Hugh Jackman</a> has demonstrated precise body composition control over two decades of film roles, repeatedly transforming his physique for specific demands and returning to a healthy baseline. He has maintained this capacity into his mid-50s, adjusting his approach as he ages.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Body Confidence &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Lizzo" target="_blank">Lizzo</a> has built a career around genuine body acceptance and physical confidence, performing demanding choreography in body-exposing outfits and speaking openly about maintaining positive body image through public scrutiny. Her confidence appears authentic and consistent across contexts.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to reflect on. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've thought about it).</p>

<div class="assess-group">
<h4>Youthfulness & Vitality</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-skin-routine">
    <label for="a-skin-routine">I know whether I have a skincare routine and what it consists of.<br><span class="assess-hint">Cleansing, moisturising, sun protection &ndash; or nothing at all. All answers count.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-energy-levels">
    <label for="a-energy-levels">I have a sense of my typical energy levels throughout the day.<br><span class="assess-hint">Do you feel energetic in the morning? Crash in the afternoon? Feel consistently tired?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-posture">
    <label for="a-posture">I know whether my posture is generally good, average, or poor.<br><span class="assess-hint">Check in a mirror or ask someone. Do you slouch, round your shoulders, or stand tall?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Romantic Appeal</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-grooming">
    <label for="a-grooming">I know what my current grooming routine looks like and how consistent it is.<br><span class="assess-hint">Hair, facial hair, nails, dental care &ndash; whatever applies to you.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-body-language">
    <label for="a-body-language">I have a sense of how I carry myself physically around others.<br><span class="assess-hint">Eye contact, open vs closed posture, how you move in social settings.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-physical-confidence">
    <label for="a-physical-confidence">I know how comfortable I feel with physical closeness and touch in romantic contexts.<br><span class="assess-hint">Very comfortable, somewhat anxious, avoidant &ndash; any honest answer works.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Weight Management</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-body-comp">
    <label for="a-body-comp">I have a rough sense of my current body composition and whether I'm satisfied with it.<br><span class="assess-hint">You don't need exact numbers &ndash; just whether you feel you're at, above, or below your desired weight and muscle level.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-weight-history">
    <label for="a-weight-history">I know whether my weight has been stable, trending up, or trending down over the past year.<br><span class="assess-hint">A rough sense is fine. Has your weight changed noticeably?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-food-relationship">
    <label for="a-food-relationship">I have a sense of my relationship with food and whether it feels healthy.<br><span class="assess-hint">Do you eat in response to emotions? Feel guilt about food? Eat mindfully? No judgement here.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Body Confidence</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-mirror">
    <label for="a-mirror">I know how I feel when I look at myself in the mirror.<br><span class="assess-hint">Positive, neutral, critical, avoidant &ndash; whatever your honest reaction is.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-clothing-comfort">
    <label for="a-clothing-comfort">I know whether I avoid certain clothing or activities because of how my body looks.<br><span class="assess-hint">Swimming, form-fitting clothes, sleeveless tops, photos &ndash; do you avoid any of these?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-self-talk">
    <label for="a-self-talk">I have a sense of my internal dialogue about my body &ndash; whether it's mostly positive, neutral, or negative.<br><span class="assess-hint">Pay attention to what you say to yourself when getting dressed or catching your reflection.</span></label>
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

<p>You now understand why body image matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about youthfulness and vitality, romantic appeal, weight management, and body confidence. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/body-image/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Body Image Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Body Image. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/body-image/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'body-image';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-skin-routine', 'a-energy-levels', 'a-posture',
        'a-grooming', 'a-body-language', 'a-physical-confidence',
        'a-body-comp', 'a-weight-history', 'a-food-relationship',
        'a-mirror', 'a-clothing-comfort', 'a-self-talk'
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
