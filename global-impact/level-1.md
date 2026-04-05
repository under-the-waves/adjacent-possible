---
layout: default
title: "Global Impact – Level 1: Awareness"
life_area_slug: global-impact
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

<h1>Global Impact: Level 1</h1>

<p class="l1-subtitle">Understand what global impact means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Global Impact Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why global impact matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>The resources you direct toward improving the world &ndash; through charitable giving, career choices, or advocacy &ndash; vary enormously in their effectiveness. <a href="https://www.givewell.org/how-we-work/our-criteria/cost-effectiveness" target="_blank">Research by GiveWell</a> shows that the best health interventions can be over 100 times more cost-effective than average ones addressing the same problem. Where you give matters far more than how much.</p>

<p>This is not just theoretical. GiveWell has directed over <a href="https://www.givewell.org/impact" target="_blank">$2.6 billion to recommended charities</a>, contributing to an estimated 340,000 lives saved &ndash; primarily through interventions like malaria prevention and vitamin A supplementation. Pledging movements like <a href="https://www.givingwhatwecan.org/" target="_blank">Giving What We Can</a> have demonstrated that sustained, planned philanthropy from ordinary earners can create extraordinary impact over a lifetime.</p>

<p>Beyond effectiveness, giving reliably improves the giver's own wellbeing. Research consistently shows that <a href="https://doi.org/10.1126/science.1150952" target="_blank">spending money on others produces greater happiness</a> than spending it on oneself, and this effect holds across income levels and cultures. Strategic generosity is one of the rare investments that benefits both the world and the person making it.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about global impact</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach global impact for different reasons. This site scores every global impact intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Impartiality</h3>
<p>Directing resources toward causes based on evidence of impact rather than personal connection or emotional appeal. Cost-effectiveness analysis, cause prioritisation informed by research, and willingness to support unfamiliar causes if the evidence warrants it. People who lean towards this value treat philanthropy as a problem to be optimised.</p>

<h3>Passion</h3>
<p>Contributing to causes you genuinely care about &ndash; areas that resonate with your personal experience, interests, and values. Volunteering in areas that energise you and choosing impact channels that sustain your motivation over decades. People who lean towards this value believe sustained commitment requires personal meaning.</p>

<h3>Sustainability</h3>
<p>Maintaining your global impact practice over the long term without burnout, guilt, or financial strain. Setting sustainable giving levels, building impact habits that fit your life, and ensuring that your philanthropic practice enhances rather than diminishes your wellbeing. People who lean towards this value plan for decades of contribution.</p>

<h3>Fulfilment</h3>
<p>The personal satisfaction and sense of purpose derived from making a positive difference. Feeling that your contributions matter, experiencing gratitude and meaning from giving, and ensuring that your impact work is a source of joy rather than obligation. People who lean towards this value see giving as enriching their own life.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each global impact value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Impartiality &ndash; Level 5</div>
    <p><a href="https://www.thelifeyoucansave.org/about-us/" target="_blank">Toby Ord</a> is a moral philosopher at Oxford who co-founded Giving What We Can and wrote <em>The Precipice</em> on existential risk. He has pledged to give everything he earns above &pound;18,000 to the most effective charities he can find, and his research on cause prioritisation has influenced billions of pounds in philanthropic allocation. His approach treats global impact as a rigorous intellectual and moral project.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Passion &ndash; Level 5</div>
    <p><a href="https://www.womenonwaves.org/en/page/2591/about-women-on-waves" target="_blank">Rebecca Gomperts</a> is a Dutch physician who founded Women on Waves and Women on Web, providing reproductive healthcare access to women in countries with restrictive laws. Her work stems from direct clinical experience treating women harmed by unsafe procedures. Over two decades, her organisations have assisted hundreds of thousands of women, driven entirely by personal conviction about a cause she witnessed first-hand.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Sustainability &ndash; Level 5</div>
    <p><a href="https://founderspledge.com/about" target="_blank">David Goldberg</a> co-founded Founders Pledge, through which technology entrepreneurs commit to donating a percentage of their proceeds from company exits to effective charities. The organisation has facilitated over $10 billion in pledges from more than 1,800 founders. It demonstrates how building giving into the structure of a career creates sustained, compounding impact over a lifetime.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Fulfilment &ndash; Level 5</div>
    <p><a href="https://www.roomtoread.org/about/our-story/" target="_blank">John Wood</a> left a senior role at Microsoft after visiting schools in Nepal and seeing empty library shelves. He founded Room to Read, which has benefited over 40 million children across 23 countries with literacy and gender equality programmes. He frequently speaks about how leaving a lucrative career for philanthropic work was the most fulfilling decision of his life.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to look up. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've found it out).</p>

<div class="assess-group">
<h4>Impartiality</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-giving-total">
    <label for="a-giving-total">I know roughly how much I donated to charity last year, in total.<br><span class="assess-hint">Check your bank statements or tax records if you're unsure.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-charity-evaluators">
    <label for="a-charity-evaluators">I know whether any of my donations went to charities recommended by evaluators like GiveWell, The Life You Can Save, or Animal Charity Evaluators.<br><span class="assess-hint">If you haven't heard of these organisations, that's useful information too.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-cost-effectiveness">
    <label for="a-cost-effectiveness">I understand the concept that different charities can vary by 100x or more in cost-effectiveness for the same type of problem.<br><span class="assess-hint">This is the core insight of effective giving &ndash; where you give matters more than how much.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Passion</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-causes-care">
    <label for="a-causes-care">I can name the causes I genuinely care about, as opposed to causes I give to out of social pressure or habit.<br><span class="assess-hint">Think about what keeps you up at night or what news stories genuinely move you.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-volunteering">
    <label for="a-volunteering">I know whether I currently volunteer or contribute non-financial resources to any cause, and if so, how many hours per month.<br><span class="assess-hint">Include pro bono work, board service, advocacy, mentoring, or other non-monetary contributions.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-motivation">
    <label for="a-motivation">I have a sense of whether my giving feels motivated by genuine care or by guilt, obligation, or social expectation.<br><span class="assess-hint">There's no wrong answer &ndash; the question is whether you've reflected on it.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Sustainability</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-giving-percentage">
    <label for="a-giving-percentage">I know what percentage of my income I give to charity annually.<br><span class="assess-hint">Divide your total annual donations by your annual income. Even a rough estimate is useful.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-giving-budget">
    <label for="a-giving-budget">I know whether I have a giving budget or plan, or whether I give sporadically in response to appeals.<br><span class="assess-hint">Planned giving tends to result in both higher total impact and lower decision fatigue.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-financial-strain">
    <label for="a-financial-strain">I have a sense of whether my current giving level is sustainable or causes financial strain.<br><span class="assess-hint">Sustainable giving over 30 years beats generous giving that leads to burnout after 3.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Fulfilment</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-satisfaction">
    <label for="a-satisfaction">I know whether my current giving and impact activities are a source of satisfaction or a source of guilt.<br><span class="assess-hint">Many people feel guilty about not doing enough rather than good about what they do. Either is common.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-connection">
    <label for="a-connection">I have a sense of how connected I feel to the impact of my contributions &ndash; whether I can see or feel the difference I make.<br><span class="assess-hint">Some people feel disconnected from the results of their giving, which can erode motivation.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-identity">
    <label for="a-identity">I know whether being someone who contributes to global causes is an important part of my identity or something I rarely think about.<br><span class="assess-hint">Neither answer is wrong &ndash; but knowing where you stand helps you decide what to build toward.</span></label>
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

<p>You now understand why global impact matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about impartiality, passion, sustainability, and fulfilment. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/global-impact/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Global Impact Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Global Impact. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/global-impact/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'global-impact';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-giving-total', 'a-charity-evaluators', 'a-cost-effectiveness',
        'a-causes-care', 'a-volunteering', 'a-motivation',
        'a-giving-percentage', 'a-giving-budget', 'a-financial-strain',
        'a-satisfaction', 'a-connection', 'a-identity'
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
