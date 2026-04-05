---
layout: default
title: "Sex – Level 1: Awareness"
life_area_slug: sex
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

<h1>Sex: Level 1</h1>

<p class="l1-subtitle">Understand what sexual wellbeing means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Sex Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why sexual wellbeing matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Sexual wellbeing is a significant component of quality of life for most adults. Research published in the <em>Journal of Sexual Medicine</em> found that <a href="https://pubmed.ncbi.nlm.nih.gov/27671968/" target="_blank">62% of men and 43% of women</a> rate sexual health as highly important to their overall quality of life.</p>

<p>The benefits extend well beyond the bedroom. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11601183/" target="_blank">Sexual satisfaction and regular sexual activity</a> are associated with improved cardiovascular health, lower rates of depression, and stronger relationship satisfaction. Among a representative sample of 16,000 American adults, sexual frequency was a strong positive predictor of self-reported happiness.</p>

<p>Yet there is a substantial gap between desired and actual sexual experience for many people. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10364113/" target="_blank">International research</a> identifies open sexual communication as one of the strongest predictors of both frequency and satisfaction, but most couples rarely discuss their sexual needs explicitly. The result is that many people carry chronic dissatisfaction they never address.</p>

<p>The relationship between frequency and satisfaction also has a ceiling. Beyond a baseline threshold, quality and connection matter considerably more than frequency alone. Understanding what you actually value about your sexual life &ndash; and where the gaps are &ndash; is the starting point for meaningful improvement.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about sex</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue sexual wellbeing for different reasons. This site scores every sex intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Frequency</h3>
<p>Maintaining a satisfying rate of sexual activity that meets both partners' needs. Initiating regularly, managing desire discrepancies constructively, and ensuring sexual intimacy remains a consistent part of the relationship rather than something that fades over time.</p>

<h3>Variety</h3>
<p>Diversity and novelty in sexual experiences &ndash; exploring new activities, settings, dynamics, and expressions of intimacy. Openness to experimentation, comfort discussing preferences, and actively introducing novelty to prevent routine.</p>

<h3>Pleasure</h3>
<p>The direct experience of physical and psychological enjoyment from sexual activity. Knowledge of your own body, ability to communicate desires, and the pursuit of mutually satisfying experiences.</p>

<h3>Contentment</h3>
<p>Overall satisfaction with your sexual life as a whole &ndash; feeling at peace with the role sex plays in your life and relationship. Acceptance, realistic expectations, and the sense that your sexual life is genuinely fulfilling.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each sexual wellbeing value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Frequency &amp; Variety &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Dan_Savage" target="_blank">Dan Savage</a> has written the syndicated sex advice column <em>Savage Love</em> since 1991 and hosts the <em>Savage Lovecast</em> podcast. Over more than three decades, he has publicly discussed and modelled how long-term couples can sustain sexual frequency and novelty through open communication, negotiation, and willingness to explore. He coined the concept of being "GGG" (good, giving, and game) as a practical framework for maintaining sexual generosity in committed relationships, and has been with his husband Terry Miller since 1995.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Pleasure &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Emily_Nagoski" target="_blank">Emily Nagoski</a> is a sex educator and researcher whose book <em>Come As You Are</em> synthesises decades of sexual response research into a practical framework for understanding arousal, desire, and pleasure. Her work on the dual control model of sexual response &ndash; distinguishing between sexual "accelerators" and "brakes" &ndash; has helped hundreds of thousands of people understand their own patterns of desire and expand their capacity for enjoyment. She holds a PhD from Indiana University's Kinsey Institute.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Contentment &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Peggy_Kleinplatz" target="_blank">Peggy Kleinplatz</a> is a clinical psychologist and sex therapist at the University of Ottawa who has spent over 20 years researching what she calls "optimal sexual experiences." Her studies of people who report extraordinary sexual satisfaction &ndash; including couples in their 70s and 80s &ndash; found that the common thread was not technique or frequency but presence, authenticity, and deep interpersonal connection. Her research provides some of the strongest evidence that sexual fulfilment can be sustained and even deepen across the lifespan.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know straight away, others might take a few minutes of honest reflection. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've thought it through).</p>

<div class="assess-group">
<h4>Frequency</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-current-frequency">
    <label for="a-current-frequency">I know roughly how often I have sex in a typical month, and whether that rate has changed over the past year.<br><span class="assess-hint">An honest estimate is fine &ndash; precision is less important than awareness.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-desire-gap">
    <label for="a-desire-gap">I have a sense of whether there is a gap between how often I want sex and how often it happens.<br><span class="assess-hint">Consider both your own desires and your partner's. Is there a discrepancy?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-initiation">
    <label for="a-initiation">I know who typically initiates sex in my relationship and whether that pattern works for both of us.<br><span class="assess-hint">Is initiation roughly balanced, or does one person carry most of the responsibility?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Variety</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-routine">
    <label for="a-routine">I can describe whether my sexual experiences tend to follow a predictable pattern or include meaningful variation.<br><span class="assess-hint">Same time, same place, same sequence &ndash; or do things change?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-curiosities">
    <label for="a-curiosities">I have thought about whether there are things I am curious about but have not tried or discussed with my partner.<br><span class="assess-hint">Unexpressed curiosities are common &ndash; the point is to notice them, not to act on all of them.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Pleasure</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-own-body">
    <label for="a-own-body">I know my own body well enough to identify what I find most pleasurable and what does not work for me.<br><span class="assess-hint">Consider whether you could clearly describe your preferences to a partner.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-communication">
    <label for="a-communication">I know whether I am comfortable communicating my sexual preferences and needs to my partner.<br><span class="assess-hint">Both giving feedback ("I like this") and asking for what you want.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Contentment</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-overall-satisfaction">
    <label for="a-overall-satisfaction">I have honestly assessed whether my sexual life is a source of fulfilment, frustration, or indifference.<br><span class="assess-hint">Not how you think it should be, but how it actually feels to you right now.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-comparison">
    <label for="a-comparison">I am aware of whether I compare my sexual life to external standards &ndash; media, peers, past relationships &ndash; and how that affects my satisfaction.<br><span class="assess-hint">Comparison can distort your sense of what is genuinely enough for you.</span></label>
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

<p>You now understand why sexual wellbeing matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about frequency, variety, pleasure, and contentment. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/sex/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Sex Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Sex. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/sex/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'sex';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-current-frequency', 'a-desire-gap', 'a-initiation',
        'a-routine', 'a-curiosities',
        'a-own-body', 'a-communication',
        'a-overall-satisfaction', 'a-comparison'
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
