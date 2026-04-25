---
layout: default
title: "Physical Safety – Level 1: Awareness"
life_area_slug: physical-safety
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

<h1>Physical Safety: Level 1</h1>

<p class="l1-subtitle">Understand what physical safety means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Physical Safety Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why physical safety matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Physical safety is one of those areas people tend not to think about until something goes wrong. But preventable injuries are a <a href="https://www.cdc.gov/injury/wisqars/LeadingCauses.html" target="_blank">leading cause of death</a> for people under 45, and the gap between those who practise basic safety habits and those who don't is surprisingly large.</p>

<p>Many of the highest-impact safety measures require minimal effort. Consistent seat belt use <a href="https://www.nhtsa.gov/risky-driving/seat-belts" target="_blank">reduces the risk of fatal injury by about 45%</a> for front-seat passengers. Basic home security measures – visible cameras, locked doors, motion-sensor lighting – deter the majority of burglars, with <a href="https://www.unc.edu/news/research-in-action/do-security-cameras-reduce-crime/" target="_blank">University of North Carolina research</a> finding that 83% check for security systems before attempting entry.</p>

<p>Beyond prevention, knowing how to respond in an emergency can be decisive. Bystander CPR roughly <a href="https://cpr.heart.org/en/resources/history-of-cpr" target="_blank">doubles or triples survival rates</a> from cardiac arrest, yet only around 18% of adults maintain current certification. Self-defence training has been shown to <a href="https://doi.org/10.1177/088626001016009001" target="_blank">reduce completed assault rates by 46%</a> and tends to increase general confidence and reduce anxiety well beyond the specific scenarios trained for.</p>

<p>Physical safety skills also expand what you feel comfortable doing. People with solid safety foundations tend to travel more freely, engage in a wider range of activities, and experience less background anxiety about potential threats.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about physical safety</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach physical safety for different reasons. This site scores every physical safety intervention across two core values. Later, you'll set your own weighting across these two values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Risk Reduction</h3>
<p>Minimising the probability and severity of physical harm through systematic hazard management, protective measures, and evidence-based safety practices. People who lean towards this value focus on comprehensive protection – preventive systems, current certifications, and proven methods for reducing various categories of risk including accidents, violence, and property crime.</p>

<h3>Freedom and Convenience</h3>
<p>Maintaining lifestyle flexibility and spontaneity whilst achieving reasonable safety. The ability to travel, explore, and engage in desired activities without excessive safety-related restrictions, delays, or anxiety. People who lean towards this value seek protective capabilities that integrate smoothly into daily life, and would prefer a slightly less comprehensive system that doesn't require significant lifestyle modifications.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each physical safety value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Risk Reduction &ndash; Level 5</div>
    <p><a href="https://www.gavindebecker.com/about/" target="_blank">Gavin de Becker</a> is a security specialist who has advised three US presidents and numerous public figures on threat assessment. His book <em>The Gift of Fear</em> popularised evidence-based approaches to personal safety, emphasising intuitive threat recognition and systematic risk reduction. He maintains advanced training across multiple security domains and has built protective systems used by thousands of organisations worldwide.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Freedom and Convenience &ndash; Level 5</div>
    <p><a href="https://www.levison-wood.com/about" target="_blank">Levison Wood</a> is a British explorer and former army officer who has walked the length of the Nile, traversed the Himalayas, and crossed Central America on foot. He operates confidently in environments that most people would avoid entirely, relying on a combination of military training, situational awareness, and local knowledge. His approach to safety is characterised by thorough preparation that enables freedom of movement in high-risk settings.</p>
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

<div class="assess-privacy">Your answers are stored only on your device and are never sent to our servers. Only your estimated percentile scores (single numbers, not your answers) may be synced if you create an account.</div>

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to look up or test.</p>

<div class="assess-group">
<h4>Risk Reduction</h4>

<div class="assess-input-group" id="ig-home-security">
    <span class="assess-label">What security measures are currently in place at your home?</span>
    <span class="assess-hint">Door locks, window locks, motion-sensor lighting, cameras, alarm systems &ndash; or the absence of any of these.</span>
    <select id="a-home-security" onchange="handleAssessInput('a-home-security')">
        <option value="">Select...</option>
        <option value="none">None &ndash; no deliberate security measures beyond a basic door lock</option>
        <option value="minimal">Minimal &ndash; standard locks only</option>
        <option value="basic">Basic &ndash; good locks plus one or two additional measures (e.g. motion light)</option>
        <option value="solid">Solid &ndash; multiple layers including cameras or an alarm</option>
        <option value="comprehensive">Comprehensive &ndash; thorough system covering locks, lighting, cameras, and alarm</option>
    </select> <span class="assess-percentile-hint" id="pct-home-security"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-home-security" onchange="handleSkip('a-home-security')"><label for="skip-home-security">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-first-aid">
    <span class="assess-label">Do you hold a current first aid or CPR certification?</span>
    <span class="assess-hint">Check any cards or certificates you have. 'Never had one' is a valid answer.</span>
    <select id="a-first-aid" onchange="handleAssessInput('a-first-aid')">
        <option value="">Select...</option>
        <option value="never">Never had one</option>
        <option value="expired-long">Expired more than two years ago</option>
        <option value="expired-recent">Expired within the last two years</option>
        <option value="current-basic">Current basic first aid certificate</option>
        <option value="current-advanced">Current advanced first aid or CPR certification</option>
    </select> <span class="assess-percentile-hint" id="pct-first-aid"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-first-aid" onchange="handleSkip('a-first-aid')"><label for="skip-first-aid">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-hazard-audit">
    <span class="assess-label">How well have you thought about the main physical risks in your daily routine?</span>
    <span class="assess-hint">Driving or cycling habits, neighbourhood safety, workplace hazards, fire risks at home &ndash; anything that could cause injury.</span>
    <select id="a-hazard-audit" onchange="handleAssessInput('a-hazard-audit')">
        <option value="">Select...</option>
        <option value="not-at-all">Not at all &ndash; have not considered my daily physical risks</option>
        <option value="vaguely">Vaguely &ndash; aware of one or two risks but not systematically</option>
        <option value="some-thought">Some thought &ndash; have identified a few key risks</option>
        <option value="thorough">Thorough &ndash; have assessed most areas of daily risk</option>
        <option value="systematic">Systematic &ndash; have done a deliberate audit and taken action on findings</option>
    </select> <span class="assess-percentile-hint" id="pct-hazard-audit"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-hazard-audit" onchange="handleSkip('a-hazard-audit')"><label for="skip-hazard-audit">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Freedom and Convenience</h4>

<div class="assess-input-group" id="ig-avoidance">
    <span class="assess-label">Do you avoid activities or places because of safety concerns?</span>
    <span class="assess-hint">Walking alone at night, travelling to certain areas, particular sports or outdoor activities &ndash; or nothing at all.</span>
    <select id="a-avoidance" onchange="handleAssessInput('a-avoidance')">
        <option value="">Select...</option>
        <option value="many">Many &ndash; I avoid a lot of things because of safety concerns</option>
        <option value="several">Several &ndash; a few activities or places I steer clear of</option>
        <option value="one-or-two">One or two &ndash; a specific avoidance but mostly unrestricted</option>
        <option value="none">None &ndash; safety concerns do not limit my activities</option>
    </select> <span class="assess-percentile-hint" id="pct-avoidance"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-avoidance" onchange="handleSkip('a-avoidance')"><label for="skip-avoidance">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-confidence">
    <span class="assess-label">How confident do you feel navigating unfamiliar environments?</span>
    <span class="assess-hint">New cities, rural areas, foreign countries, crowded events &ndash; comfortable, cautious, or anxious?</span>
    <select id="a-confidence" onchange="handleAssessInput('a-confidence')">
        <option value="">Select...</option>
        <option value="anxious">Anxious &ndash; unfamiliar environments make me very uncomfortable</option>
        <option value="cautious">Cautious &ndash; manage but with noticeable unease</option>
        <option value="moderate">Moderate &ndash; some caution but generally cope</option>
        <option value="comfortable">Comfortable &ndash; at ease in most new settings</option>
        <option value="very-confident">Very confident &ndash; thrive in unfamiliar environments</option>
    </select> <span class="assess-percentile-hint" id="pct-confidence"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-confidence" onchange="handleSkip('a-confidence')"><label for="skip-confidence">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-lifestyle-cost">
    <span class="assess-label">Do your current safety practices create inconvenience or restrict your activities?</span>
    <span class="assess-hint">Do you spend significant time on security routines, avoid spontaneous plans, or feel limited by safety concerns?</span>
    <select id="a-lifestyle-cost" onchange="handleAssessInput('a-lifestyle-cost')">
        <option value="">Select...</option>
        <option value="significant">Significant &ndash; safety concerns noticeably restrict my lifestyle</option>
        <option value="some">Some &ndash; a few inconveniences but manageable</option>
        <option value="minimal">Minimal &ndash; safety practices are well integrated and barely noticeable</option>
        <option value="none">None &ndash; I have no safety practices that create any friction</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-lifestyle-cost" onchange="handleSkip('a-lifestyle-cost')"><label for="skip-lifestyle-cost">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-riskReduction">
        <span class="assess-summary-label">Risk Reduction</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-riskReduction" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-riskReduction">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-freedomConvenience">
        <span class="assess-summary-label">Freedom &amp; Convenience</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-freedomConvenience" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-freedomConvenience">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published data on home security adoption, first aid certification rates, and safety behaviour. Unscored items (lifestyle cost of safety practices) are excluded from calculations.</p>
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

<p>You now understand why physical safety matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about risk reduction versus freedom and convenience. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/physical-safety/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Physical Safety Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Physical Safety. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/physical-safety/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'physical-safety';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-home-security', 'a-first-aid', 'a-hazard-audit',
        'a-avoidance', 'a-confidence', 'a-lifestyle-cost'
    ];

    var THRESHOLDS = {
        'a-home-security': [
            // ~30% have no security beyond a basic lock; comprehensive systems ~10%
            {v:'none',p:10},{v:'minimal',p:30},{v:'basic',p:55},{v:'solid',p:78},{v:'comprehensive',p:95}
        ],
        'a-first-aid': [
            // ~70% have never held a first aid certificate; current advanced is ~5%
            {v:'never',p:12},{v:'expired-long',p:35},{v:'expired-recent',p:55},{v:'current-basic',p:78},{v:'current-advanced',p:95}
        ],
        'a-hazard-audit': [
            // ~50% have not considered daily physical risks; systematic audit is ~5%
            {v:'not-at-all',p:10},{v:'vaguely',p:30},{v:'some-thought',p:55},{v:'thorough',p:78},{v:'systematic',p:95}
        ],
        'a-avoidance': [
            // ~40% avoid many activities due to safety; no limitations is ~25%
            {v:'many',p:10},{v:'several',p:35},{v:'one-or-two',p:62},{v:'none',p:88}
        ],
        'a-confidence': [
            // ~20% are anxious in unfamiliar environments; very confident is ~15%
            {v:'anxious',p:8},{v:'cautious',p:25},{v:'moderate',p:50},{v:'comfortable',p:75},{v:'very-confident',p:93}
        ]
    };

    var VALUE_ITEMS = {
        riskReduction: ['a-home-security', 'a-first-aid', 'a-hazard-audit'],
        freedomConvenience: ['a-avoidance', 'a-confidence']
    };

    var UNSCORED_ITEMS = ['a-lifestyle-cost'];

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
        if (UNSCORED_ITEMS.indexOf(itemId) !== -1) return null;
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return null;

        var el = document.getElementById(itemId);
        if (!el) return null;
        var val = el.value;
        if (val === '' || val === null) return null;
        if (!THRESHOLDS[itemId]) return null;
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
        hintEl.textContent = pct !== null ? '~' + ordinalSuffix(pct) + ' percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['riskReduction', 'freedomConvenience'].forEach(function(vk) {
            var pct = computeValuePercentile(vk);
            var barEl = document.getElementById('bar-' + vk);
            var valEl = document.getElementById('val-' + vk);
            if (barEl && valEl) {
                if (pct !== null) {
                    barEl.style.width = pct + '%';
                    valEl.textContent = ordinalSuffix(pct);
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
        ['riskReduction', 'freedomConvenience'].forEach(function(vk) {
            scores[vk] = computeValuePercentile(vk);
        });
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-scores') || {};
            all[AREA] = scores;
            APStorage.save('ap-level1-scores', all);
        }
    }

    // --- Event handlers ---

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

    // --- Restore saved answers ---

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
