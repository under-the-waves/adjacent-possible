---
layout: default
title: "Style – Level 1: Awareness"
life_area_slug: style
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

<h1>Style: Level 1</h1>

<p class="l1-subtitle">Understand what style means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Style Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why style matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your clothing and grooming choices shape how others perceive you and how you feel about yourself. The effects are measurable and surprisingly large.</p>

<p>A <a href="https://news.temple.edu/news/2023-06-01/when-you-look-good-you-feel-good-research-shows-you-might-even-be-more-productive" target="_blank">Temple University study</a> tracking 808 employee days found that people who dressed better than usual had stronger self-esteem and performed better on tasks. Research from Northwestern University showed participants wearing lab coats made significantly fewer mistakes on attention tasks compared to those in everyday clothing.</p>

<p>In the workplace, <a href="https://www.academia.edu/34496959/ASSESSING_THE_RELATIONSHIP_AND_EFFECT_OF_WORKPLACE_DRESS_CODE_ON_EMPLOYEE_PRODUCTIVITY" target="_blank">41% of employers</a> report that employees who dress professionally are more likely to be promoted, rising to 55% in financial services. Clothing also functions as a <a href="https://fashionandtextiles.springeropen.com/articles/10.1186/s40691-014-0020-7" target="_blank">communication system</a>, conveying information about competence, status, and identity before you ever speak.</p>

<p>Most people underinvest in style relative to its impact. Research shows the average person spends 17 minutes daily choosing outfits, wears only 44% of their wardrobe regularly, and frequently experiences clothing-related stress that affects punctuality and mood. Even modest improvements in how you dress can yield disproportionate returns in confidence, professional outcomes, and social interactions.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about style</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue style for different reasons. This site scores every style intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Attractiveness</h3>
<p>Looking appealing to others across romantic and social contexts through deliberate clothing, grooming, and presentation choices. People who lean towards this value focus on flattering fit, body-appropriate silhouettes, and building wardrobes that make them look their best to the widest range of people.</p>

<h3>Status & Professional</h3>
<p>Signalling competence, authority, and taste through clothing in career and social settings. People who lean towards this value invest in pieces that communicate success and command respect in professional and social hierarchies, understanding dress codes and making strategic wardrobe choices for advancement.</p>

<h3>Self-Expression</h3>
<p>Communicating identity, values, and affiliations through distinctive clothing choices. People who lean towards this value choose clothing that reflects their personality and signals membership in chosen communities, developing a personal aesthetic and visual storytelling about who they are.</p>

<h3>Comfort & Function</h3>
<p>Prioritising clothing that supports daily activities, physical comfort, and practical needs. People who lean towards this value focus on weather appropriateness, ease of movement, durable fabrics, and minimising decision fatigue through streamlined wardrobe systems.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each style value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Attractiveness &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Zendaya" target="_blank">Zendaya</a> has become one of the most closely watched figures in contemporary fashion, consistently appearing on best-dressed lists since her early twenties. She works closely with stylist Law Roach to curate looks that reference fashion history while remaining distinctive. Her red carpet appearances regularly generate significant media coverage, and she was the youngest person to receive the CFDA Fashion Icon Award in 2021.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Status & Professional &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Christine_Lagarde" target="_blank">Christine Lagarde</a>, President of the European Central Bank, is widely noted for projecting authority and credibility through her wardrobe choices. She consistently dresses at executive standards across formal, diplomatic, and media settings, demonstrating how strategic clothing choices can reinforce leadership presence at the highest levels.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Self-Expression &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Iris_Apfel" target="_blank">Iris Apfel</a> developed one of the most recognisable personal aesthetics of anyone in the public eye. Her bold, layered style combined vintage, couture, and flea-market finds into a signature look that was entirely her own. She became a style icon in her 80s and remained one into her 100s, demonstrating that distinctive self-expression through clothing can be sustained across a lifetime.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Comfort & Function &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Steve_Jobs" target="_blank">Steve Jobs</a> famously wore the same black turtleneck, jeans, and trainers combination daily, eliminating decision fatigue entirely whilst maintaining a polished, recognisable appearance. His approach demonstrated that a fully systematised wardrobe can simultaneously achieve comfort, consistency, and a distinctive professional image.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to look up or test. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've found it out).</p>

<div class="assess-group">
<h4>Attractiveness</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-fit">
    <label for="a-fit">I've assessed how well my most-worn clothes actually fit my body.<br><span class="assess-hint">Check shoulders, chest, waist, and trouser length. Ill-fitting clothes are the single biggest detractor from appearance.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-colours">
    <label for="a-colours">I know which colours suit my skin tone and which ones don't.<br><span class="assess-hint">Hold different coloured tops near your face in natural light. Some will make you look healthier; others will wash you out.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-grooming">
    <label for="a-grooming">I've honestly evaluated my grooming standards &ndash; hair, skin, nails, and overall upkeep.<br><span class="assess-hint">Grooming is often more impactful than clothing choices for overall presentation.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Status & Professional</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-dresscode">
    <label for="a-dresscode">I understand the dress code expectations in my workplace or primary professional context.<br><span class="assess-hint">Consider what the most respected people in your environment wear, not just the minimum standard.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-quality">
    <label for="a-quality">I can identify the difference between well-made and poorly-made clothing in my wardrobe.<br><span class="assess-hint">Check stitching, fabric weight, button quality, and how garments hold their shape after washing.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-contexts">
    <label for="a-contexts">I know whether I have appropriate outfits for different professional situations &ndash; meetings, networking events, presentations.<br><span class="assess-hint">Think beyond your daily work outfit to situations where first impressions matter most.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Self-Expression</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-aesthetic">
    <label for="a-aesthetic">I've thought about whether my clothing reflects my personality or whether I dress on autopilot.<br><span class="assess-hint">Consider whether someone who knows you well would say your clothes "look like you".</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-inspiration">
    <label for="a-inspiration">I can name a style or aesthetic direction I'm drawn to, even if I don't currently dress that way.<br><span class="assess-hint">This could be a subculture, a colour palette, a level of formality, or a general mood.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-confidence">
    <label for="a-confidence">I know which outfits make me feel most confident and which I wear despite not liking them.<br><span class="assess-hint">Think about what you reach for when you want to feel good versus what you default to.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Comfort & Function</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-wardrobe-use">
    <label for="a-wardrobe-use">I have a rough sense of what percentage of my wardrobe I actually wear regularly.<br><span class="assess-hint">The average person wears about 44% of their wardrobe. Check whether you have a large number of unworn items.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-decision-time">
    <label for="a-decision-time">I know roughly how long I spend choosing what to wear each morning.<br><span class="assess-hint">The average is about 17 minutes. Consider whether this feels like a source of stress or friction.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-comfort-gaps">
    <label for="a-comfort-gaps">I've identified any recurring comfort issues with my clothing &ndash; items that pinch, ride up, or don't suit the weather.<br><span class="assess-hint">Physical discomfort from clothing affects mood and focus throughout the day.</span></label>
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

<p>You now understand why style matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about attractiveness, status and professional signalling, self-expression, and comfort. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/style/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Style Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Style. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/style/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'style';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-fit', 'a-colours', 'a-grooming',
        'a-dresscode', 'a-quality', 'a-contexts',
        'a-aesthetic', 'a-inspiration', 'a-confidence',
        'a-wardrobe-use', 'a-decision-time', 'a-comfort-gaps'
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
