---
layout: default
title: "Legal Matters – Level 1: Awareness"
life_area_slug: legal-matters
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

<h1>Legal Matters: Level 1</h1>

<p class="l1-subtitle">Understand what legal matters means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Legal Matters Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why legal matters matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Legal preparedness is one of those areas most people ignore until something goes wrong &ndash; and by then, the cost of catching up can be substantial. The evidence suggests that proactive legal planning prevents far more problems than it creates.</p>

<p>Around <a href="https://www.americanbar.org/groups/journal/articles/2021/two-thirds-of-americans-experience-legal-problems--says-new-nati/" target="_blank">two-thirds of Americans</a> experience at least one legal problem over any four-year period, ranging from employment disputes to housing issues to family law matters. Yet only about 20% of those affected seek professional help, often because they don't recognise the situation as a legal problem in the first place.</p>

<p>The consequences of poor preparation tend to be concentrated and severe. Dying without a will can leave families facing months of probate proceedings and costs reaching <a href="https://www.financialsense.com/blog/21022/alarming-estate-planning-statistics" target="_blank">up to 10% of the estate's value</a>. Not knowing your rights during a police encounter or tenancy dispute can lead to outcomes that proper knowledge would have prevented. Even basic documents like a healthcare directive can spare your family agonising decisions during a medical crisis.</p>

<p>Legal preparedness also creates positive opportunities. Understanding contract terms, knowing when professional consultation is worthwhile, and structuring your affairs thoughtfully can yield meaningful financial and strategic benefits over time.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about legal matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach legal matters for different reasons. This site scores every legal matters intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Comprehensive Protection</h3>
<p>Complete safeguarding of assets, rights, and interests through proper documentation, risk mitigation, and legal structures. Having essential documents like wills and powers of attorney, understanding potential legal vulnerabilities, and implementing protective strategies. People who lean towards this value focus on maximising legal security even when it requires some complexity or ongoing maintenance.</p>

<h3>Simplicity & Peace of Mind</h3>
<p>Maintaining legal affairs in a streamlined, low-maintenance way that reduces anxiety and cognitive load. Straightforward arrangements, clear documentation, and systems that work without constant attention or complexity. Those who lean towards this value prefer basic but effective legal structures over sophisticated arrangements that require ongoing management.</p>

<h3>Strategic Advantage</h3>
<p>Leveraging legal knowledge and structures to optimise outcomes in business, taxes, estate planning, and major life decisions. Using legal entities effectively, understanding regulatory advantages, and structuring affairs to maximise beneficial legal treatment. People who lean towards this value are willing to invest in sophisticated planning that goes beyond basic protection.</p>

<h3>Access & Empowerment</h3>
<p>Understanding your rights and having the knowledge to navigate legal situations confidently. Knowing how to interact with law enforcement, understanding consumer and employment rights, recognising when you need legal help, and being able to advocate for yourself effectively. Those who lean towards this value prefer developing personal legal literacy over relying entirely on professional services or avoidance.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each legal matters value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Comprehensive Protection &ndash; Level 5</div>
    <p><a href="https://www.nolo.com/legal-encyclopedia/about-nolo" target="_blank">Ralph Warner</a> co-founded Nolo, a legal self-help publisher, in 1971 after working as a legal aid lawyer. Over five decades he developed and maintained comprehensive personal legal structures while writing extensively about estate planning, small business law, and consumer rights. His own legal affairs reportedly serve as a working model of the layered protection strategies his books describe.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Simplicity & Peace of Mind &ndash; Level 5</div>
    <p><a href="https://www.suzeorman.com/about" target="_blank">Suze Orman</a> is a financial adviser and author who has spent decades advocating for straightforward legal and financial arrangements. She consistently emphasises basic documents &ndash; wills, revocable living trusts, advance directives &ndash; over complex structures, and has spoken publicly about maintaining her own legal affairs in a simple, well-organised system that requires minimal ongoing attention.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Strategic Advantage &ndash; Level 5</div>
    <p><a href="https://www.wealthcounsel.com/about" target="_blank">Robert Esperti</a> co-founded WealthCounsel, a network of estate planning solicitors, and co-authored multiple books on asset protection and estate planning strategy. His practice focused on advanced legal structures &ndash; family limited partnerships, irrevocable trusts, and multi-entity arrangements &ndash; designed to optimise tax treatment and protect wealth across generations.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Access & Empowerment &ndash; Level 5</div>
    <p><a href="https://www.law.georgetown.edu/faculty/peter-edelman/" target="_blank">Peter Edelman</a> is a Georgetown law professor and former senior government official who has spent his career working on access to justice. He served as legislative director to Robert Kennedy and later held positions at the Department of Health and Human Services. His writing and teaching focus on empowering individuals to understand and exercise their legal rights effectively.</p>
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

<p>Awareness means knowing your starting point. Work through the checklist below &ndash; some items you might know off the top of your head, others might take a few minutes to look up or check. Tick each one once you know the answer (you don't need to enter the answer here, just confirm you've found it out).</p>

<div class="assess-group">
<h4>Comprehensive Protection</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-will">
    <label for="a-will">I know whether I have a valid, up-to-date will.<br><span class="assess-hint">If you have one, do you know where it is and when it was last updated?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-poa">
    <label for="a-poa">I know whether I have a power of attorney and a healthcare directive.<br><span class="assess-hint">These documents let someone act on your behalf if you're unable to make decisions.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-insurance">
    <label for="a-insurance">I know what legal risks I'm currently exposed to that aren't covered by insurance or documentation.<br><span class="assess-hint">Think about your housing situation, employment, family circumstances, and assets.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Simplicity & Peace of Mind</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-organised">
    <label for="a-organised">I know where all my important legal documents are stored.<br><span class="assess-hint">Could a family member find your will, insurance policies, and property deeds if they needed to?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-anxiety">
    <label for="a-anxiety">I've identified which legal matters cause me the most anxiety or uncertainty.<br><span class="assess-hint">Is it estate planning, tax, employment rights, housing, or something else?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-family-aware">
    <label for="a-family-aware">I know whether my family or next of kin are aware of my legal arrangements.<br><span class="assess-hint">Have you discussed your wishes and document locations with the relevant people?</span></label>
</div>
</div>

<div class="assess-group">
<h4>Strategic Advantage</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-tax">
    <label for="a-tax">I know whether my current legal and financial structures are tax-efficient.<br><span class="assess-hint">Are you using ISAs, pensions, or other tax-advantaged structures effectively?</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-contracts">
    <label for="a-contracts">I know whether I've reviewed the key contracts that affect my life.<br><span class="assess-hint">Employment contract, tenancy agreement, mortgage terms, insurance policies.</span></label>
</div>
</div>

<div class="assess-group">
<h4>Access & Empowerment</h4>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-rights-police">
    <label for="a-rights-police">I know my basic rights during a police encounter.<br><span class="assess-hint">What you're required to do, what you can decline, and when you should ask for legal representation.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-rights-work">
    <label for="a-rights-work">I know my core employment rights.<br><span class="assess-hint">Notice periods, unfair dismissal protections, holiday entitlement, discrimination protections.</span></label>
</div>

<div class="assess-item" onclick="toggleAssess(this)">
    <input type="checkbox" id="a-legal-help">
    <label for="a-legal-help">I know how to find appropriate legal help if I needed it.<br><span class="assess-hint">Do you know the difference between a solicitor and a barrister? How to access legal aid or free advice?</span></label>
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

<p>You now understand why legal matters matter, what different people get out of legal preparedness, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about comprehensive protection, simplicity, strategic advantage, and access. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/legal-matters/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Legal Matters Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Legal Matters. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/legal-matters/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'legal-matters';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-will', 'a-poa', 'a-insurance',
        'a-organised', 'a-anxiety', 'a-family-aware',
        'a-tax', 'a-contracts',
        'a-rights-police', 'a-rights-work', 'a-legal-help'
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
