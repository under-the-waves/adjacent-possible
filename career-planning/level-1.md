---
layout: default
title: "Career Planning – Level 1: Awareness"
life_area_slug: career-planning
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

<h1>Career Planning: Level 1</h1>

<p class="l1-subtitle">Understand what career planning means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Career Planning Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why career planning matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Most people do not plan their careers. Half of workers view their job as <a href="https://www.pewresearch.org/social-trends/2024/07/24/how-americans-view-their-jobs/" target="_blank">'just a job'</a> rather than a career or calling, and career progression is largely reactive – taking the next obvious step rather than choosing a deliberate direction.</p>

<p>The returns to planning are large. Only <a href="https://mentorcliq.com/mentoring-resources/mentoring-statistics" target="_blank">37% of professionals</a> have a mentor, yet those who do are five times more likely to be promoted. An estimated <a href="https://www.linkedin.com/pulse/new-survey-reveals-85-all-jobs-filled-via-networking-lou-adler/" target="_blank">85% of jobs</a> are filled through networking rather than formal applications, making deliberate relationship-building one of the highest-return career investments.</p>

<p>Skills are expiring faster than ever. The World Economic Forum projects that <a href="https://www.weforum.org/publications/the-future-of-jobs-report-2025/" target="_blank">39% of core skills</a> required for existing jobs will change by 2030, making passive career management increasingly dangerous.</p>

<p>Most people also lack the financial runway to take strategic risks – <a href="https://www.bankrate.com/banking/savings/emergency-savings-report/" target="_blank">59% cannot cover</a> more than three months of expenses. Career planning builds the clarity, positioning, and resilience needed to navigate an increasingly volatile professional landscape.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about career planning</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People plan their careers for different reasons. This site scores every career planning intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Clarity</h3>
<p>Having a clear, informed understanding of where your career is heading and why. Articulating a career thesis, understanding industry trajectories, and regularly revisiting your direction. People who lean towards this value invest in reflection and research rather than defaulting to the next obvious step.</p>

<h3>Advancement</h3>
<p>Progressing toward higher levels of responsibility, compensation, and influence. Building skills beyond your current role, pursuing promotions, developing your professional reputation, and ensuring your trajectory moves upward. People who lean towards this value treat career progression as an active project.</p>

<h3>Security</h3>
<p>Protecting yourself against career disruption through financial runway, transferable skills, and professional optionality. Maintaining multiple income capabilities, building financial buffers, and developing skills that are valuable across industries. People who lean towards this value build careers that are robust to disruption.</p>

<h3>Meaning</h3>
<p>Finding genuine purpose and significance in your professional life – work that aligns with your values and contributes to something you care about. Choosing roles based on mission fit, seeking work that feels inherently worthwhile, and ensuring your career contributes to your sense of identity. People who lean towards this value make career decisions based on purpose, not just advancement.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each career planning value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Clarity &ndash; Level 5</div>
    <p><a href="https://80000hours.org/about/#702" target="_blank">Benjamin Todd</a> co-founded 80,000 Hours, an organisation dedicated to helping people find careers that do the most good. He has spent over a decade researching career strategy and impact, developing frameworks for career decision-making that have influenced thousands of professionals. His career is itself a multi-decade thesis on how to choose professional direction deliberately.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Advancement &ndash; Level 5</div>
    <p><a href="https://www.linkedin.com/in/indranooyi/" target="_blank">Indra Nooyi</a> moved from India to the United States for graduate school and rose to become CEO of PepsiCo, a position she held for 12 years. She navigated multiple industries and geographies, building skills and reputation at each stage. Her trajectory from management consultant to Fortune 50 CEO exemplifies deliberate, sustained career advancement over decades.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Security &ndash; Level 5</div>
    <p><a href="https://tferriss.com/about/" target="_blank">Tim Ferriss</a> built a career structure that is genuinely antifragile – spanning bestselling books, a top-ranked podcast, angel investing, and public speaking. He has navigated multiple career transitions and income streams, ensuring that no single disruption could threaten his professional standing. His approach to career design emphasises optionality and redundancy.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Meaning &ndash; Level 5</div>
    <p><a href="https://paulgraham.com/bio.html" target="_blank">Paul Graham</a> co-founded Y Combinator after careers as a programmer, writer, and painter. His professional choices have consistently reflected a personal philosophy about what kind of work matters – from writing influential essays on startups and technology to funding early-stage founders. His career legacy is inseparable from his intellectual convictions.</p>
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
<h4>Clarity</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-direction">
    <label for="a-direction">I can describe where I want my career to be in three years and why.<br><span class="assess-hint">If you can't, that's useful information too – it tells you clarity is a priority.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-industry">
    <label for="a-industry">I understand the major trends shaping my industry over the next five years.<br><span class="assess-hint">Consider AI, regulation, market shifts, and emerging roles in your field.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-written-plan">
    <label for="a-written-plan">I have a written career plan or direction document, even if it's rough.<br><span class="assess-hint">This could be a document, a note on your phone, or a structured journal entry.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Advancement</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-skills-beyond">
    <label for="a-skills-beyond">I am currently developing at least one skill beyond what my current role requires.<br><span class="assess-hint">Think about courses, side projects, or deliberate practice in adjacent areas.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-mentor">
    <label for="a-mentor">I have a mentor, sponsor, or professional advisor who is actively helping my career.<br><span class="assess-hint">A mentor gives advice; a sponsor advocates for you in rooms you're not in.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-reputation">
    <label for="a-reputation">I know what I am known for professionally – the thing people would say is my strength.<br><span class="assess-hint">If you're unsure, ask two or three colleagues what they see as your distinctive contribution.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Security</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-runway">
    <label for="a-runway">I know how many months of expenses I could cover if I lost my income tomorrow.<br><span class="assess-hint">Check your savings and liquid assets against your monthly expenses.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-transferable">
    <label for="a-transferable">I can name five skills I have that would be valuable in a different industry.<br><span class="assess-hint">Think beyond technical skills – communication, project management, analysis, writing, leadership.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-cv-ready">
    <label for="a-cv-ready">My CV is up to date and I could apply for a job this week if I needed to.<br><span class="assess-hint">Check when you last updated it. If it's more than 6 months old, it probably needs work.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Meaning</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-values-align">
    <label for="a-values-align">I can describe what makes work meaningful to me and whether my current role delivers it.<br><span class="assess-hint">Meaning can come from impact, learning, autonomy, community, or creative expression.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-purpose">
    <label for="a-purpose">I have thought about whether my career contributes to something I genuinely care about.<br><span class="assess-hint">This isn't about grand missions – even feeling that your work helps real people counts.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-tradeoffs">
    <label for="a-tradeoffs">I know what I would change about my career if money were not a constraint.<br><span class="assess-hint">The gap between this answer and your current path reveals how much meaning you are trading away.</span></label>
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

<p>You now understand why career planning matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about clarity, advancement, security, and meaning. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/career-planning/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Career Planning Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Career Planning. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/career-planning/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'career-planning';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-direction', 'a-industry', 'a-written-plan',
        'a-skills-beyond', 'a-mentor', 'a-reputation',
        'a-runway', 'a-transferable', 'a-cv-ready',
        'a-values-align', 'a-purpose', 'a-tradeoffs'
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
