---
layout: default
title: "Ethics – Level 1: Awareness"
life_area_slug: ethics
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

<h1>Ethics: Level 1</h1>

<p class="l1-subtitle">Understand what ethics means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Ethics Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why ethics matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Most people absorb their moral frameworks from family, culture, and religion without examining them closely. That inherited toolkit may work well enough for routine situations, but it tends to break down when decisions get genuinely difficult &ndash; when values conflict, when the stakes are high, or when social pressure pulls against what you believe is right.</p>

<p>Developing your ethical thinking deliberately has measurable effects. <a href="https://psycnet.apa.org/record/2004-16788-000" target="_blank">Peterson and Seligman (2004)</a> found that character strengths including integrity and fairness are among the strongest predictors of life satisfaction across cultures. People with clearer moral frameworks also tend to experience less <a href="https://www.swarthmore.edu/SocSci/bschwar1/Sci.Amer.pdf" target="_blank">decision paralysis</a> when facing complex choices, likely because they have stable criteria for evaluating options.</p>

<p>There is a practical dimension too. Consistent ethical behaviour builds social trust over time. <a href="https://www.bowlingalone.com/" target="_blank">Putnam (2000)</a> found that communities with higher levels of moral trust have better social and economic outcomes. On an individual level, the people others turn to for advice in difficult situations are almost always those whose integrity has been tested and held.</p>

<p>Ethics also intersects with nearly every other area of life &ndash; how you manage money, how you treat colleagues, how you raise children, what career you choose. Strengthening your ethical framework may be one of the broadest-impact investments available.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about ethics</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue ethical development for different reasons. This site scores every ethics intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Philosophical Depth</h3>
<p>Comprehensive understanding of ethical theories, moral philosophy, and rigorous reasoning about complex moral questions. Studying major frameworks like utilitarianism, deontology, and virtue ethics, understanding their historical development and contemporary applications, and developing analytical skills for moral reasoning. People who lean towards this value seek deep engagement with ethics as an intellectual discipline.</p>

<h3>Practical Guidance</h3>
<p>Clear, actionable ethical frameworks that provide reliable guidance for daily decisions and life choices. Developing decision-making processes for common moral dilemmas, creating personal principles that can be applied consistently across different contexts, and translating abstract moral insights into concrete behavioural guidelines. People who lean towards this value focus on ethics that actually helps them navigate real-world situations with confidence.</p>

<h3>Moral Integrity</h3>
<p>Living according to your ethical convictions consistently, even when it requires personal sacrifice, social awkwardness, or going against popular opinion. Developing the courage to act on moral principles when it's difficult, maintaining consistency between private beliefs and public behaviour, and building character traits that support ethical action under pressure. People who lean towards this value focus on closing the gap between knowing what's right and actually doing it.</p>

<h3>Community Ethics &amp; Belonging</h3>
<p>Understanding and fulfilling your moral obligations within your communities, families, and relationships whilst contributing to collective moral flourishing. Aligning with the ethical expectations of groups you value belonging to, understanding your moral duties to others based on your roles and relationships, and seeing ethics as fundamentally about service to others. People who lean towards this value focus on how their ethical choices strengthen their communities.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each ethics value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Philosophical Depth &ndash; Level 5</div>
    <p><a href="https://www.utilitarianism.net/utilitarian-thinker/peter-singer" target="_blank">Peter Singer</a> has spent over five decades developing and refining utilitarian arguments on animal welfare, global poverty, and effective altruism. His 1975 book <em>Animal Liberation</em> provided the philosophical foundation for the modern animal rights movement. He has consistently revised his positions in response to counter-arguments &ndash; a rarity among public intellectuals &ndash; and his practical ethics framework is taught in most university philosophy programmes worldwide.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Practical Guidance &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Bryan_Stevenson" target="_blank">Bryan Stevenson</a> founded the Equal Justice Initiative in 1989 and has since won relief for over 140 wrongly condemned prisoners on death row. His ethical framework &ndash; centred on proximity to suffering as a prerequisite for moral understanding &ndash; translates directly into legal strategy, organisational decisions, and public advocacy. His approach has been adopted by law schools, public defenders' offices, and criminal justice organisations across the United States.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Moral Integrity &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Dietrich_Bonhoeffer" target="_blank">Dietrich Bonhoeffer</a> was a German theologian who returned to Nazi Germany from the safety of the United States in 1939 because he believed he could not participate in rebuilding German moral life after the war if he had not shared the trials of his countrymen. He joined the resistance, was arrested in 1943, and was executed in April 1945. His theological writings on the cost of moral conviction, composed largely in prison, continue to influence ethical thought eight decades later.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Community Ethics &amp; Belonging &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Ela_Bhatt" target="_blank">Ela Bhatt</a> founded the Self-Employed Women's Association (SEWA) in India in 1972, building it into a union of over 2 million members. She developed ethical frameworks for economic cooperation rooted in Gandhian principles and applied them at scale, creating banking, insurance, and housing cooperatives that transformed the lives of some of the poorest women in the world. Her model of community-centred ethics has been replicated across dozens of countries.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to reflect on. Tick each one once you've thought it through (you don't need to enter the answer here, just confirm you've considered it).</p>

<div class="assess-group">
<h4>Philosophical Depth</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-frameworks">
    <label for="a-frameworks">I can name at least one ethical framework (e.g. utilitarianism, deontology, virtue ethics) and explain its basic idea.<br><span class="assess-hint">If none come to mind, that's useful information too &ndash; just tick to confirm you've checked.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-reasoning">
    <label for="a-reasoning">I've thought about whether I tend to judge actions by their outcomes, their intentions, or some other standard.<br><span class="assess-hint">There's no right answer here &ndash; this is about noticing your default approach.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-dilemma">
    <label for="a-dilemma">I can recall a moral dilemma I've faced and describe how I reasoned through it.<br><span class="assess-hint">A time when two principles you hold pulled in different directions.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Practical Guidance</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-principles">
    <label for="a-principles">I have a sense of my core moral principles &ndash; the rules or commitments I try to follow in daily life.<br><span class="assess-hint">These might be explicit or just patterns you notice in how you make decisions.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-consistency">
    <label for="a-consistency">I've considered whether I apply my moral principles consistently or whether they shift depending on context.<br><span class="assess-hint">For example, whether you hold yourself to the same standards you hold others to.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-blindspots">
    <label for="a-blindspots">I can identify at least one area where my moral decision-making feels unclear or where I suspect I might have a blind spot.<br><span class="assess-hint">Common examples: spending habits, environmental impact, how you treat people you'll never see again.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Moral Integrity</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-gap">
    <label for="a-gap">I've honestly assessed the gap between what I believe is right and how I actually behave.<br><span class="assess-hint">Most people have some gap here. The point is to see it clearly.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-courage">
    <label for="a-courage">I can recall a time I acted on a moral conviction despite it costing me something &ndash; or a time I failed to.<br><span class="assess-hint">Social disapproval, financial cost, inconvenience, or awkwardness all count.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-pressure">
    <label for="a-pressure">I have a sense of how much social pressure affects my moral choices.<br><span class="assess-hint">Do you tend to go along with the group, or hold your ground? In which situations?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Community Ethics &amp; Belonging</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-obligations">
    <label for="a-obligations">I've thought about what moral obligations I have to the communities I belong to.<br><span class="assess-hint">Family, friends, workplace, neighbourhood, religious community, or broader society.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-impact">
    <label for="a-impact">I have a sense of how my ethical choices affect the people around me.<br><span class="assess-hint">Both the direct effects and the example you set.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-contribute">
    <label for="a-contribute">I've considered whether I actively contribute to the moral health of my communities or mostly follow existing norms.<br><span class="assess-hint">Do you raise ethical concerns, mediate disputes, or set standards &ndash; or leave that to others?</span></label>
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

<p>You now understand why ethics matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about philosophical depth, practical guidance, moral integrity, and community ethics. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/ethics/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Ethics Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Ethics. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/ethics/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'ethics';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-frameworks', 'a-reasoning', 'a-dilemma',
        'a-principles', 'a-consistency', 'a-blindspots',
        'a-gap', 'a-courage', 'a-pressure',
        'a-obligations', 'a-impact', 'a-contribute'
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
