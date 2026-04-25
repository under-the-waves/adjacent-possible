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

/* Assessment inputs */
.assess-privacy {
    background: #f0f4ff;
    border-left: 4px solid #155799;
    border-radius: 6px;
    padding: 14px 18px;
    margin-bottom: 24px;
    font-size: 0.9em;
    color: #333;
    line-height: 1.5;
}
.assess-group { margin-bottom: 24px; }
.assess-group h4 { margin: 0 0 12px 0; }
.assess-input-group {
    padding: 14px 18px;
    margin-bottom: 10px;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    font-size: 0.93em;
    line-height: 1.4;
    transition: border-color 0.2s;
}
.assess-input-group.answered { border-color: #28a745; background: #f9fdf9; }
.assess-input-group .assess-label {
    display: block;
    font-weight: 500;
    margin-bottom: 6px;
}
.assess-input-group .assess-hint {
    font-size: 0.85em;
    color: #888;
    margin-bottom: 8px;
}
.assess-input-group select {
    padding: 6px 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 0.95em;
    max-width: 100%;
}
.assess-skip {
    display: flex;
    align-items: center;
    gap: 6px;
    margin-top: 8px;
    font-size: 0.85em;
    color: #888;
}
.assess-skip input[type="checkbox"] {
    accent-color: #888;
}
.assess-percentile-hint {
    display: inline-block;
    margin-left: 12px;
    font-size: 0.85em;
    color: #888;
    font-style: italic;
}
.assess-summary {
    background: #f8f9fa;
    border: 2px solid #155799;
    border-radius: 8px;
    padding: 20px 24px;
    margin-top: 24px;
    display: none;
}
.assess-summary.visible { display: block; }
.assess-summary h4 { margin: 0 0 14px 0; color: #155799; }
.assess-summary-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 10px;
    font-size: 0.93em;
}
.assess-summary-label { flex: 0 0 200px; font-weight: 500; }
.assess-summary-bar {
    flex: 1;
    height: 8px;
    background: #e0e0e0;
    border-radius: 4px;
    overflow: hidden;
}
.assess-summary-fill {
    height: 100%;
    background: #28a745;
    border-radius: 4px;
    transition: width 0.4s;
}
.assess-summary-value {
    flex: 0 0 60px;
    text-align: right;
    font-weight: 600;
    color: #155799;
}
.assess-summary-text {
    font-size: 0.88em;
    color: #555;
    margin-top: 2px;
}
@media (max-width: 600px) {
    .assess-summary-label { flex: 0 0 120px; }
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

<div class="assess-privacy">Your answers are stored only on your device and are never sent to our servers. Only your estimated percentile scores (single numbers, not your answers) may be synced if you create an account. Percentile estimates are approximate – they position you roughly relative to the general population based on your self-report, but could easily be off by 10–15 points.</div>

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to reflect on.</p>

<div class="assess-group">
<h4>Comprehensive Protection</h4>

<div class="assess-input-group" id="ig-will">
    <span class="assess-label">Do you have a valid, up-to-date will?</span>
    <span class="assess-hint">If you have one, do you know where it is and when it was last updated?</span>
    <select id="a-will" onchange="handleAssessInput('a-will')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I don't have a will</option>
        <option value="outdated">Outdated &ndash; I have one but it needs updating</option>
        <option value="have-one">I have one but I'm not sure it covers everything</option>
        <option value="current">Current &ndash; valid and reviewed within the past few years</option>
        <option value="comprehensive">Comprehensive &ndash; recently reviewed with professional advice</option>
    </select> <span class="assess-percentile-hint" id="pct-will"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-will" onchange="handleSkip('a-will')"><label for="skip-will">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-poa">
    <span class="assess-label">Do you have a power of attorney and a healthcare directive?</span>
    <span class="assess-hint">These documents let someone act on your behalf if you're unable to make decisions.</span>
    <select id="a-poa" onchange="handleAssessInput('a-poa')">
        <option value="">Select...</option>
        <option value="neither">Neither &ndash; I don't have either</option>
        <option value="considered">Considered &ndash; I've thought about it but not acted</option>
        <option value="one-only">One only &ndash; I have one but not the other</option>
        <option value="both-basic">Both &ndash; basic versions in place</option>
        <option value="both-comprehensive">Both &ndash; professionally prepared and regularly reviewed</option>
    </select> <span class="assess-percentile-hint" id="pct-poa"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-poa" onchange="handleSkip('a-poa')"><label for="skip-poa">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-insurance">
    <span class="assess-label">What legal risks are you currently exposed to that aren't covered by insurance or documentation?</span>
    <span class="assess-hint">Think about your housing situation, employment, family circumstances, and assets.</span>
    <select id="a-insurance" onchange="handleAssessInput('a-insurance')">
        <option value="">Select...</option>
        <option value="dont-know">I don't know &ndash; I've never assessed this</option>
        <option value="probably-gaps">Probably gaps &ndash; I suspect I'm exposed but haven't checked</option>
        <option value="some-awareness">Some awareness &ndash; I know a few areas that need attention</option>
        <option value="mostly-covered">Mostly covered &ndash; I've addressed the main risks</option>
        <option value="fully-assessed">Fully assessed &ndash; I've had a professional review of my exposure</option>
    </select> <span class="assess-percentile-hint" id="pct-insurance"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-insurance" onchange="handleSkip('a-insurance')"><label for="skip-insurance">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Simplicity &amp; Peace of Mind</h4>

<div class="assess-input-group" id="ig-organised">
    <span class="assess-label">Could a family member find your important legal documents if they needed to?</span>
    <span class="assess-hint">Will, insurance policies, property deeds &ndash; are they accessible?</span>
    <select id="a-organised" onchange="handleAssessInput('a-organised')">
        <option value="">Select...</option>
        <option value="no">No &ndash; they wouldn't know where to start</option>
        <option value="unlikely">Unlikely &ndash; documents are scattered or unfiled</option>
        <option value="with-effort">With effort &ndash; they're in the house somewhere</option>
        <option value="yes">Yes &ndash; they're in a known location</option>
        <option value="easily">Easily &ndash; there's a clear index or guide to all documents</option>
    </select> <span class="assess-percentile-hint" id="pct-organised"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-organised" onchange="handleSkip('a-organised')"><label for="skip-organised">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-anxiety">
    <span class="assess-label">Which legal matters cause you the most anxiety or uncertainty?</span>
    <span class="assess-hint">Estate planning, tax, employment rights, housing, or something else?</span>
    <select id="a-anxiety" onchange="handleAssessInput('a-anxiety')">
        <option value="">Select...</option>
        <option value="many">Many &ndash; I feel anxious about several legal areas</option>
        <option value="a-few">A few &ndash; two or three specific areas worry me</option>
        <option value="one">One &ndash; there's a single area I need to address</option>
        <option value="minor">Minor &ndash; I have small uncertainties but nothing major</option>
        <option value="none">None &ndash; I feel confident about my legal position</option>
    </select> <span class="assess-percentile-hint" id="pct-anxiety"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-anxiety" onchange="handleSkip('a-anxiety')"><label for="skip-anxiety">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-family-aware">
    <span class="assess-label">Are your family or next of kin aware of your legal arrangements?</span>
    <span class="assess-hint">Have you discussed your wishes and document locations with the relevant people?</span>
    <select id="a-family-aware" onchange="handleAssessInput('a-family-aware')">
        <option value="">Select...</option>
        <option value="no">No &ndash; nobody knows my arrangements</option>
        <option value="vague">Vaguely &ndash; they know I have some documents but not the details</option>
        <option value="partial">Partially &ndash; some people know some things</option>
        <option value="mostly">Mostly &ndash; key people know the important details</option>
        <option value="fully">Fully &ndash; everyone relevant has been briefed and knows where to find things</option>
    </select> <span class="assess-percentile-hint" id="pct-family-aware"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-family-aware" onchange="handleSkip('a-family-aware')"><label for="skip-family-aware">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Strategic Advantage</h4>

<div class="assess-input-group" id="ig-tax">
    <span class="assess-label">Are your current legal and financial structures tax-efficient?</span>
    <span class="assess-hint">ISAs, pensions, or other tax-advantaged structures.</span>
    <select id="a-tax" onchange="handleAssessInput('a-tax')">
        <option value="">Select...</option>
        <option value="dont-know">I don't know</option>
        <option value="probably-not">Probably not &ndash; I haven't optimised anything</option>
        <option value="basic">Basic &ndash; I use one or two tax-efficient structures</option>
        <option value="good">Good &ndash; I've made deliberate choices to minimise tax</option>
        <option value="optimised">Optimised &ndash; I've had professional advice and act on it regularly</option>
    </select> <span class="assess-percentile-hint" id="pct-tax"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-tax" onchange="handleSkip('a-tax')"><label for="skip-tax">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-contracts">
    <span class="assess-label">Have you reviewed the key contracts that affect your life?</span>
    <span class="assess-hint">Employment contract, tenancy agreement, mortgage terms, insurance policies.</span>
    <select id="a-contracts" onchange="handleAssessInput('a-contracts')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I've never read any of them properly</option>
        <option value="glanced">Glanced &ndash; I've skimmed one or two</option>
        <option value="some">Some &ndash; I've read a few but not all</option>
        <option value="most">Most &ndash; I've reviewed the main ones</option>
        <option value="all">All &ndash; I've read and understood every key contract</option>
    </select> <span class="assess-percentile-hint" id="pct-contracts"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-contracts" onchange="handleSkip('a-contracts')"><label for="skip-contracts">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Access &amp; Empowerment</h4>

<div class="assess-input-group" id="ig-rights-police">
    <span class="assess-label">How well do you know your rights during a police encounter?</span>
    <span class="assess-hint">What you're required to do, what you can decline, and when to ask for legal representation.</span>
    <select id="a-rights-police" onchange="handleAssessInput('a-rights-police')">
        <option value="">Select...</option>
        <option value="no-idea">No idea</option>
        <option value="vague">Vague &ndash; I have a rough sense but wouldn't be confident</option>
        <option value="basic">Basic &ndash; I know the essentials</option>
        <option value="solid">Solid &ndash; I know my rights and could assert them calmly</option>
        <option value="thorough">Thorough &ndash; I could explain them to someone else</option>
    </select> <span class="assess-percentile-hint" id="pct-rights-police"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-rights-police" onchange="handleSkip('a-rights-police')"><label for="skip-rights-police">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-rights-work">
    <span class="assess-label">How well do you know your core employment rights?</span>
    <span class="assess-hint">Notice periods, unfair dismissal protections, holiday entitlement, discrimination protections.</span>
    <select id="a-rights-work" onchange="handleAssessInput('a-rights-work')">
        <option value="">Select...</option>
        <option value="no-idea">No idea</option>
        <option value="vague">Vague &ndash; I know I have rights but not the specifics</option>
        <option value="basic">Basic &ndash; I know the main protections</option>
        <option value="solid">Solid &ndash; I know my rights and have checked my contract against them</option>
        <option value="thorough">Thorough &ndash; I could advise someone else on basic employment rights</option>
    </select> <span class="assess-percentile-hint" id="pct-rights-work"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-rights-work" onchange="handleSkip('a-rights-work')"><label for="skip-rights-work">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-legal-help">
    <span class="assess-label">Would you know how to find appropriate legal help if you needed it?</span>
    <span class="assess-hint">Solicitor vs barrister, legal aid, free advice services.</span>
    <select id="a-legal-help" onchange="handleAssessInput('a-legal-help')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I wouldn't know where to start</option>
        <option value="search-online">I'd search online and hope for the best</option>
        <option value="basic">Basic &ndash; I know to contact a solicitor but not much more</option>
        <option value="informed">Informed &ndash; I know the different types of legal help and how to access them</option>
        <option value="connected">Connected &ndash; I already have a solicitor or know exactly who to call</option>
    </select> <span class="assess-percentile-hint" id="pct-legal-help"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-legal-help" onchange="handleSkip('a-legal-help')"><label for="skip-legal-help">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-protection">
        <span class="assess-summary-label">Comprehensive Protection</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-protection" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-protection">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-simplicity">
        <span class="assess-summary-label">Simplicity &amp; Peace of Mind</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-simplicity" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-simplicity">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-strategic">
        <span class="assess-summary-label">Strategic Advantage</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-strategic" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-strategic">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-access">
        <span class="assess-summary-label">Access &amp; Empowerment</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-access" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-access">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on legal preparedness among adults. All items in this area are scored.</p>
</div>

<button class="l1-mark-done" id="assessBtn" onclick="completeStep('assess')" disabled>Answer all items to continue</button>

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

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: ~33% of adults have a will, ~20% have POA/healthcare directives,
    // ~80% have never assessed legal exposure, ~70% couldn't locate key documents quickly.
    var THRESHOLDS = {
        'a-will': [
            // ~33% of UK adults have a valid will; comprehensive professional review is very rare
            {v:'no',p:20},{v:'outdated',p:40},{v:'have-one',p:55},{v:'current',p:75},{v:'comprehensive',p:95}
        ],
        'a-poa': [
            // ~20% have any form of POA or healthcare directive; both professionally prepared is very rare
            {v:'neither',p:15},{v:'considered',p:30},{v:'one-only',p:55},{v:'both-basic',p:78},{v:'both-comprehensive',p:95}
        ],
        'a-insurance': [
            // ~80% have never formally assessed their legal exposure
            {v:'dont-know',p:10},{v:'probably-gaps',p:30},{v:'some-awareness',p:55},{v:'mostly-covered',p:78},{v:'fully-assessed',p:95}
        ],
        'a-organised': [
            // ~70% of families would struggle to locate key documents in an emergency
            {v:'no',p:10},{v:'unlikely',p:25},{v:'with-effort',p:50},{v:'yes',p:75},{v:'easily',p:95}
        ],
        'a-anxiety': [
            // Most people have at least some legal anxiety; full confidence is uncommon
            {v:'many',p:10},{v:'a-few',p:30},{v:'one',p:55},{v:'minor',p:78},{v:'none',p:95}
        ],
        'a-family-aware': [
            // Most people haven't discussed legal arrangements with family
            {v:'no',p:10},{v:'vague',p:30},{v:'partial',p:50},{v:'mostly',p:75},{v:'fully',p:95}
        ],
        'a-tax': [
            // Most people use basic tax-efficient structures at best; professional optimisation is rare
            {v:'dont-know',p:10},{v:'probably-not',p:25},{v:'basic',p:50},{v:'good',p:78},{v:'optimised',p:95}
        ],
        'a-contracts': [
            // Most people never read their key contracts properly
            {v:'none',p:10},{v:'glanced',p:30},{v:'some',p:55},{v:'most',p:78},{v:'all',p:95}
        ],
        'a-rights-police': [
            // Most people have only a vague idea of their rights during police encounters
            {v:'no-idea',p:10},{v:'vague',p:30},{v:'basic',p:55},{v:'solid',p:78},{v:'thorough',p:95}
        ],
        'a-rights-work': [
            // Many people know they have employment rights but not the specifics
            {v:'no-idea',p:10},{v:'vague',p:30},{v:'basic',p:55},{v:'solid',p:78},{v:'thorough',p:95}
        ],
        'a-legal-help': [
            // Most people would search online; having a solicitor on call is rare
            {v:'no',p:10},{v:'search-online',p:30},{v:'basic',p:55},{v:'informed',p:78},{v:'connected',p:95}
        ]
    };

    var VALUE_ITEMS = {
        protection: ['a-will', 'a-poa', 'a-insurance'],
        simplicity: ['a-organised', 'a-anxiety', 'a-family-aware'],
        strategic: ['a-tax', 'a-contracts'],
        access: ['a-rights-police', 'a-rights-work', 'a-legal-help']
    };

    // All legal-matters items are scorable
    var UNSCORED_ITEMS = [];

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
        if (step === 'assess') saveScores();
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

    // --- Scoring functions ---

    function ordinalSuffix(n) {
        var s = ['th','st','nd','rd'];
        var v = n % 100;
        return n + (s[(v-20)%10] || s[v] || s[0]);
    }
    function interpolatePercentile(value, thresholds) {
        if (typeof thresholds[0].v === 'string') {
            for (var i = 0; i < thresholds.length; i++) {
                if (thresholds[i].v === String(value)) return thresholds[i].p;
            }
            return null;
        }
        return null;
    }

    function getItemPercentile(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return null;

        var el = document.getElementById(itemId);
        if (!el) return null;
        var val = el.value;
        if (val === '' || val === null) return null;
        return interpolatePercentile(val, THRESHOLDS[itemId]);
    }

    function computeValuePercentile(valueKey) {
        var items = VALUE_ITEMS[valueKey];
        var total = 0, count = 0;
        items.forEach(function(id) {
            var pct = getItemPercentile(id);
            if (pct !== null) { total += pct; count++; }
        });
        return count > 0 ? Math.round(total / count) : null;
    }

    function updatePercentileHint(itemId) {
        if (UNSCORED_ITEMS.indexOf(itemId) !== -1) return;
        var hintEl = document.getElementById('pct-' + itemId.replace('a-', ''));
        if (!hintEl) return;
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) {
            hintEl.textContent = 'Skipped';
            return;
        }
        var pct = getItemPercentile(itemId);
        hintEl.textContent = pct !== null ? 'roughly ' + ordinalSuffix(Math.round(pct / 10) * 10) + ' percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['protection', 'simplicity', 'strategic', 'access'].forEach(function(vk) {
            var pct = computeValuePercentile(vk);
            var barEl = document.getElementById('bar-' + vk);
            var valEl = document.getElementById('val-' + vk);
            if (barEl && valEl) {
                if (pct !== null) {
                    barEl.style.width = pct + '%';
                    valEl.textContent = ordinalSuffix(Math.round(pct / 10) * 10);
                    anyAnswered = true;
                } else {
                    barEl.style.width = '0%';
                    valEl.innerHTML = '&ndash;';
                }
            }
        });
        var summary = document.getElementById('assessSummary');
        if (summary) summary.classList.toggle('visible', anyAnswered);
    }

    // --- Assessment helpers ---

    function isItemAnswered(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return true;
        var el = document.getElementById(itemId);
        return el && el.value !== '' && el.value !== null;
    }

    function updateInputGroupState(itemId) {
        var group = document.getElementById('ig-' + itemId.replace('a-', ''));
        if (group) group.classList.toggle('answered', isItemAnswered(itemId));
    }

    function updateAssessCompletion() {
        var allAnswered = ASSESS_IDS.every(function(id) { return isItemAnswered(id); });
        var btn = document.getElementById('assessBtn');
        if (btn) {
            btn.disabled = !allAnswered;
            btn.textContent = allAnswered ? 'All done \u2013 continue' : 'Answer all items to continue';
        }
    }

    function saveAnswers() {
        var answers = {};
        ASSESS_IDS.forEach(function(id) {
            var skipBox = document.getElementById('skip-' + id.replace('a-', ''));
            var skipped = skipBox && skipBox.checked;
            var value = null;
            if (!skipped) {
                var el = document.getElementById(id);
                if (el && el.value !== '') value = el.value;
            }
            answers[id] = { value: value, skipped: skipped };
        });
        var allAnswers = {};
        try { allAnswers = JSON.parse(localStorage.getItem('ap-level1-answers')) || {}; } catch(e) {}
        allAnswers[AREA] = answers;
        localStorage.setItem('ap-level1-answers', JSON.stringify(allAnswers));

        var checklist = {};
        ASSESS_IDS.forEach(function(id) { checklist[id] = isItemAnswered(id); });
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-assess') || {};
            all[AREA] = checklist;
            APStorage.save('ap-level1-assess', all);
        }
    }

    function saveScores() {
        var scores = {};
        ['protection', 'simplicity', 'strategic', 'access'].forEach(function(vk) {
            scores[vk] = computeValuePercentile(vk);
        });
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-scores') || {};
            all[AREA] = scores;
            APStorage.save('ap-level1-scores', all);
        }
    }

    window.handleAssessInput = function(itemId) {
        updatePercentileHint(itemId);
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessSummary();
        updateAssessCompletion();
    };

    window.handleSkip = function(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        var input = document.getElementById(itemId);
        if (skipBox && input) {
            input.disabled = skipBox.checked;
            if (skipBox.checked && input.tagName === 'SELECT') input.value = '';
        }
        updatePercentileHint(itemId);
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessSummary();
        updateAssessCompletion();
    };

    function restoreAssessment() {
        var allAnswers = {};
        try { allAnswers = JSON.parse(localStorage.getItem('ap-level1-answers')) || {}; } catch(e) {}
        var answers = allAnswers[AREA];
        if (!answers) return;

        ASSESS_IDS.forEach(function(id) {
            var item = answers[id];
            if (!item) return;
            if (item.skipped) {
                var skipBox = document.getElementById('skip-' + id.replace('a-', ''));
                if (skipBox) {
                    skipBox.checked = true;
                    var input = document.getElementById(id);
                    if (input) input.disabled = true;
                }
            } else if (item.value !== null) {
                var el = document.getElementById(id);
                if (el) el.value = item.value;
            }

            updatePercentileHint(id);
            updateInputGroupState(id);
        });

        updateAssessSummary();
        updateAssessCompletion();
    }

    document.addEventListener('DOMContentLoaded', function() {
        restoreAssessment();
        updateUI();
    });
})();
</script>
