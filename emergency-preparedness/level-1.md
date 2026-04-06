---
layout: default
title: "Emergency Preparedness – Level 1: Awareness"
life_area_slug: emergency-preparedness
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
.assess-recorded {
    background: #f0f7f0;
    border: 2px solid #28a745;
    border-radius: 8px;
    padding: 16px 20px;
    margin-top: 24px;
    text-align: center;
    font-size: 0.95em;
    color: #1a6b2a;
    display: none;
}
.assess-recorded.visible { display: block; }

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

<h1>Emergency Preparedness: Level 1</h1>

<p class="l1-subtitle">Understand what emergency preparedness means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Emergency Preparedness Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why emergency preparedness matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Emergency preparedness is one of those areas where a relatively small investment of time and resources can make an outsized difference when it counts. The evidence suggests that prepared households fare substantially better during crises across virtually every measurable dimension.</p>

<p>Studies from <a href="https://www.fema.gov/emergency-managers/national-preparedness/report" target="_blank">FEMA's National Household Survey</a> consistently find that households with emergency plans and supplies experience less financial strain, faster recovery times, and reduced need for external assistance during emergencies. Prepared households also tend to report <a href="https://doi.org/10.1016/j.ijdrr.2019.101348" target="_blank">lower psychological distress</a> both during and after disaster events.</p>

<p>Community-level preparedness appears to create multiplying effects beyond individual households. Neighbourhoods with higher preparedness participation rates tend to experience faster emergency response, more effective resource sharing, and stronger social cohesion during crises. Even basic coordination among neighbours – knowing who has medical training, who has a generator, who might need help evacuating – can meaningfully improve outcomes.</p>

<p>Perhaps most notably, the gap between "unprepared" and "minimally prepared" is where the largest gains seem to lie. Roughly half of Americans lack a basic household emergency plan, which means that even modest preparation places you well ahead of the general population.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about emergency preparedness</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue preparedness for different reasons. This site scores every emergency preparedness intervention across four core values. Later, you'll set your own weighting across these values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Self-Reliance</h3>
<p>Building personal and family capability to handle emergencies independently. People who lean towards this value focus on stockpiling resources, learning practical skills like first aid and basic repairs, and ensuring their household can function autonomously when normal support systems fail.</p>

<h3>Community Resilience</h3>
<p>Developing collective preparedness through social networks, mutual aid, and coordinated community response. People who lean towards this value focus on strengthening social bonds, organising neighbourhood preparedness efforts, and building trust networks that can mobilise quickly during emergencies.</p>

<h3>Baseline Resilience</h3>
<p>Concentrating on probable, manageable disruptions – regional natural disasters, infrastructure failures, economic downturns, temporary supply chain interruptions. People who lean towards this value focus on realistic scenarios they are likely to face, ensuring solid preparation for events that occur regularly in their region.</p>

<h3>Catastrophic Resilience</h3>
<p>Preparing for rare but potentially civilisation-altering scenarios – global pandemics, economic collapse, technological failures affecting critical infrastructure, or societal breakdown. People who lean towards this value invest significant resources in scenarios that might require extended self-sufficiency or adaptation to entirely new social conditions.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each preparedness value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Self-Reliance &ndash; Level 5</div>
    <p><a href="https://www.chelseagreen.com/writer/ben-falk/" target="_blank">Ben Falk</a> is a designer, builder, and land steward who has spent over two decades developing a 10-acre homestead in Vermont designed for long-term self-sufficiency. His property includes year-round food production, multiple water systems, renewable energy infrastructure, and perennial agriculture – all documented in his book <em>The Resilient Farm and Homestead</em>. He maintains the capacity to sustain his household independently for extended periods through integrated systems he has built and refined over years.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Community Resilience &ndash; Level 5</div>
    <p><a href="https://www.intoresilience.net/" target="_blank">Daniel Aldrich</a> is a political scientist who studies disaster recovery and social capital. His research across multiple disaster contexts – including the 2004 Indian Ocean tsunami, Hurricane Katrina, and the 2011 Fukushima disaster – has consistently found that community social networks are the strongest predictor of post-disaster recovery. He practises what he studies, maintaining deep mutual-aid networks across multiple communities and advising governments worldwide on community resilience strategies.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Baseline Resilience &ndash; Level 5</div>
    <p><a href="https://www.buildingscience.com/about-us" target="_blank">Joseph Lstiburek</a> is a building scientist and engineer who has spent decades designing homes and structures that withstand regional hazards – hurricanes, floods, extreme temperatures, and wildfire – whilst remaining energy-efficient and comfortable. His work with the Building Science Corporation has shaped building codes across North America, and his own properties serve as demonstrations of professional-grade resilience against the specific regional threats they face.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Catastrophic Resilience &ndash; Level 5</div>
    <p><a href="https://www.garrettonbain.com/" target="_blank">Garrett M. Bain</a> is a former nuclear weapons designer turned security consultant who advises on worst-case scenario preparedness. He has developed comprehensive frameworks for preparing individuals and organisations for civilisation-level disruptions, including nuclear events, pandemic collapse, and infrastructure failure. His approach combines military-grade planning methodology with practical household implementation across multiple contingency locations.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to reflect on.</p>

<div class="assess-group">
<h4>Self-Reliance</h4>

<div class="assess-input-group" id="ig-supplies">
    <span class="assess-label">How many days of food and water does your household currently have on hand?</span>
    <span class="assess-hint">Count everything in your cupboards, fridge, and any stored supplies.</span>
    <select id="a-supplies" onchange="handleAssessInput('a-supplies')">
        <option value="">Select...</option>
        <option value="under-1">Under 1 day</option>
        <option value="1-3">1&ndash;3 days</option>
        <option value="3-7">3&ndash;7 days</option>
        <option value="1-2-weeks">1&ndash;2 weeks</option>
        <option value="over-2-weeks">Over 2 weeks</option>
    </select> <span class="assess-percentile-hint" id="pct-supplies"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-supplies" onchange="handleSkip('a-supplies')"><label for="skip-supplies">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-first-aid">
    <span class="assess-label">Where is your first aid kit and is it adequately stocked?</span>
    <span class="assess-hint">Plasters, bandages, antiseptic, pain relief, any prescription medications.</span>
    <select id="a-first-aid" onchange="handleAssessInput('a-first-aid')">
        <option value="">Select...</option>
        <option value="no-kit">I don't have one</option>
        <option value="have-but-unknown">I have one but don't know what's in it</option>
        <option value="basic">Basic &ndash; I know where it is but it's probably incomplete</option>
        <option value="stocked">Stocked &ndash; I know where it is and it covers the basics</option>
        <option value="comprehensive">Comprehensive &ndash; well-stocked, regularly checked, and I know how to use everything</option>
    </select> <span class="assess-percentile-hint" id="pct-first-aid"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-first-aid" onchange="handleSkip('a-first-aid')"><label for="skip-first-aid">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-skills">
    <span class="assess-label">Which practical emergency skills do you have?</span>
    <span class="assess-hint">Basic first aid, CPR, fire extinguisher use, water shut-off, fuse box operation, cooking without power.</span>
    <select id="a-skills" onchange="handleAssessInput('a-skills')">
        <option value="">Select...</option>
        <option value="none">None of these</option>
        <option value="one-or-two">One or two &ndash; e.g. I know where my fuse box is</option>
        <option value="several">Several &ndash; I'm confident with three or four of these</option>
        <option value="most">Most &ndash; I could handle most common household emergencies</option>
        <option value="all">All of these and more</option>
    </select> <span class="assess-percentile-hint" id="pct-skills"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-skills" onchange="handleSkip('a-skills')"><label for="skip-skills">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Community Resilience</h4>

<div class="assess-input-group" id="ig-neighbours">
    <span class="assess-label">How well do you know your immediate neighbours?</span>
    <span class="assess-hint">Could you knock on their door at 2 a.m. during a crisis?</span>
    <select id="a-neighbours" onchange="handleAssessInput('a-neighbours')">
        <option value="">Select...</option>
        <option value="dont-know">I don't know any of them</option>
        <option value="recognise">Recognise faces &ndash; but wouldn't ask for help</option>
        <option value="greet">On greeting terms &ndash; we say hello</option>
        <option value="friendly">Friendly &ndash; we chat and could ask small favours</option>
        <option value="close">Close &ndash; I'd be comfortable asking for help in a crisis</option>
    </select> <span class="assess-percentile-hint" id="pct-neighbours"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-neighbours" onchange="handleSkip('a-neighbours')"><label for="skip-neighbours">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-local-resources">
    <span class="assess-label">How well do you know the emergency resources in your local area?</span>
    <span class="assess-hint">Nearest hospital, fire station, emergency shelter, community centre, non-emergency police number.</span>
    <select id="a-local-resources" onchange="handleAssessInput('a-local-resources')">
        <option value="">Select...</option>
        <option value="none">I don't know any of these</option>
        <option value="hospital-only">I know where the nearest hospital is</option>
        <option value="a-few">A few &ndash; I know two or three key locations</option>
        <option value="most">Most &ndash; I know the main emergency resources</option>
        <option value="comprehensive">Comprehensive &ndash; I could direct someone to any local emergency resource</option>
    </select> <span class="assess-percentile-hint" id="pct-local-resources"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-local-resources" onchange="handleSkip('a-local-resources')"><label for="skip-local-resources">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-contact-plan">
    <span class="assess-label">Do you have a way to contact family members if mobile networks go down?</span>
    <span class="assess-hint">An agreed meeting point, a landline number, an out-of-area contact person.</span>
    <select id="a-contact-plan" onchange="handleAssessInput('a-contact-plan')">
        <option value="">Select...</option>
        <option value="no-plan">No plan &ndash; I've never thought about this</option>
        <option value="vague">Vague &ndash; I'd probably go to a family member's house</option>
        <option value="partial">Partial &ndash; I have one backup method</option>
        <option value="solid">Solid &ndash; I have agreed plans with key people</option>
        <option value="comprehensive">Comprehensive &ndash; multiple backup methods and regular check-ins about the plan</option>
    </select> <span class="assess-percentile-hint" id="pct-contact-plan"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-contact-plan" onchange="handleSkip('a-contact-plan')"><label for="skip-contact-plan">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Baseline Resilience</h4>

<div class="assess-input-group" id="ig-regional-risks">
    <span class="assess-label">How well do you know the most likely natural disasters and infrastructure risks for your location?</span>
    <span class="assess-hint">Flooding, storms, heatwaves, wildfires, earthquakes &ndash; what has actually happened in your area?</span>
    <select id="a-regional-risks" onchange="handleAssessInput('a-regional-risks')">
        <option value="">Select...</option>
        <option value="unaware">Unaware &ndash; I haven't looked into this</option>
        <option value="vague">Vague &ndash; I have a general sense</option>
        <option value="informed">Informed &ndash; I know the main risks</option>
        <option value="detailed">Detailed &ndash; I know risks, their likelihood, and how they'd affect me</option>
        <option value="prepared">Prepared &ndash; I've taken specific steps based on my risk assessment</option>
    </select> <span class="assess-percentile-hint" id="pct-regional-risks"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-regional-risks" onchange="handleSkip('a-regional-risks')"><label for="skip-regional-risks">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-insurance">
    <span class="assess-label">Does your insurance cover the most probable emergencies for your area?</span>
    <span class="assess-hint">Check your home/contents insurance for flood, storm, and fire coverage.</span>
    <select id="a-insurance" onchange="handleAssessInput('a-insurance')">
        <option value="">Select...</option>
        <option value="no-insurance">I don't have relevant insurance</option>
        <option value="dont-know">I don't know what my insurance covers</option>
        <option value="probably">Probably &ndash; I have insurance but haven't checked the details</option>
        <option value="checked">Checked &ndash; I've reviewed my cover and it's adequate</option>
        <option value="optimised">Optimised &ndash; I've tailored my cover to my specific risks</option>
    </select> <span class="assess-percentile-hint" id="pct-insurance"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-insurance" onchange="handleSkip('a-insurance')"><label for="skip-insurance">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-evac-plan">
    <span class="assess-label">Do you know your evacuation routes and have you thought about where you'd go?</span>
    <span class="assess-hint">Two routes out of your neighbourhood, a destination, and what you'd grab in 10 minutes.</span>
    <select id="a-evac-plan" onchange="handleAssessInput('a-evac-plan')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I haven't thought about this</option>
        <option value="one-route">One route &ndash; I know how to leave but haven't planned beyond that</option>
        <option value="basic-plan">Basic plan &ndash; I have a route and a rough destination</option>
        <option value="solid-plan">Solid plan &ndash; multiple routes, a destination, and a grab bag list</option>
        <option value="practised">Practised &ndash; I've rehearsed my evacuation plan</option>
    </select> <span class="assess-percentile-hint" id="pct-evac-plan"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-evac-plan" onchange="handleSkip('a-evac-plan')"><label for="skip-evac-plan">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Catastrophic Resilience</h4>

<div class="assess-input-group" id="ig-cash">
    <span class="assess-label">How much cash do you have accessible if electronic payments stop working?</span>
    <span class="assess-hint">ATMs and card machines can go offline during power outages or cyberattacks.</span>
    <select id="a-cash" onchange="handleAssessInput('a-cash')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I don't carry or store cash</option>
        <option value="a-day">Enough for a day or two</option>
        <option value="a-week">Enough for about a week</option>
        <option value="2-weeks">Enough for two weeks</option>
        <option value="a-month">Enough for a month or more</option>
    </select> <span class="assess-percentile-hint" id="pct-cash"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-cash" onchange="handleSkip('a-cash')"><label for="skip-cash">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-documents">
    <span class="assess-label">Where are your critical documents, and do you have copies stored separately?</span>
    <span class="assess-hint">Passport, birth certificate, insurance policies, medical records.</span>
    <select id="a-documents" onchange="handleAssessInput('a-documents')">
        <option value="">Select...</option>
        <option value="scattered">Scattered &ndash; I'm not sure where they all are</option>
        <option value="one-place">One place &ndash; they're together but I don't have copies</option>
        <option value="organised">Organised &ndash; together and I know where they are</option>
        <option value="backed-up">Backed up &ndash; I have digital copies or duplicates</option>
        <option value="redundant">Redundant &ndash; originals and copies in separate locations</option>
    </select> <span class="assess-percentile-hint" id="pct-documents"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-documents" onchange="handleSkip('a-documents')"><label for="skip-documents">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-scenarios">
    <span class="assess-label">Have you thought about what you'd do during an extended disruption lasting several weeks?</span>
    <span class="assess-hint">A major pandemic, prolonged power outage, or supply chain collapse.</span>
    <select id="a-scenarios" onchange="handleAssessInput('a-scenarios')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I haven't considered this</option>
        <option value="briefly">Briefly &ndash; I've had passing thoughts</option>
        <option value="some-thought">Some thought &ndash; I have a rough mental plan</option>
        <option value="planned">Planned &ndash; I've thought through specific scenarios</option>
        <option value="prepared">Prepared &ndash; I have supplies and plans for extended disruption</option>
    </select> <span class="assess-percentile-hint" id="pct-scenarios"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-scenarios" onchange="handleSkip('a-scenarios')"><label for="skip-scenarios">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-self_reliance">
        <span class="assess-summary-label">Self-Reliance</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-self_reliance" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-self_reliance">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-community">
        <span class="assess-summary-label">Community Resilience</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-community" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-community">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-baseline">
        <span class="assess-summary-label">Baseline Resilience</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-baseline" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-baseline">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-catastrophic">
        <span class="assess-summary-label">Catastrophic Resilience</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-catastrophic" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-catastrophic">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on household preparedness among adults. All items in this area are scored.</p>
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

<p>You now understand why emergency preparedness matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about self-reliance, community resilience, baseline resilience, and catastrophic resilience. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/emergency-preparedness/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Emergency Preparedness Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Emergency Preparedness. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/emergency-preparedness/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'emergency-preparedness';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-supplies', 'a-first-aid', 'a-skills',
        'a-neighbours', 'a-local-resources', 'a-contact-plan',
        'a-regional-risks', 'a-insurance', 'a-evac-plan',
        'a-cash', 'a-documents', 'a-scenarios'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: ~50% of Americans lack a basic emergency plan (FEMA),
    // ~40% couldn't cover a $400 emergency, ~30% have 3+ days of supplies.
    var THRESHOLDS = {
        'a-supplies': [
            // ~50% have less than 3 days; 2+ weeks is very uncommon
            {v:'under-1',p:10},{v:'1-3',p:35},{v:'3-7',p:60},{v:'1-2-weeks',p:82},{v:'over-2-weeks',p:95}
        ],
        'a-first-aid': [
            // ~40% don't have a first aid kit; comprehensive is rare
            {v:'no-kit',p:12},{v:'have-but-unknown',p:30},{v:'basic',p:50},{v:'stocked',p:75},{v:'comprehensive',p:95}
        ],
        'a-skills': [
            // ~30% have taken first aid training; having all skills is very rare
            {v:'none',p:10},{v:'one-or-two',p:35},{v:'several',p:58},{v:'most',p:80},{v:'all',p:95}
        ],
        'a-neighbours': [
            // Urban areas: ~35% don't know neighbours; close relationships are uncommon
            {v:'dont-know',p:12},{v:'recognise',p:30},{v:'greet',p:50},{v:'friendly',p:72},{v:'close',p:92}
        ],
        'a-local-resources': [
            // Most people know the nearest hospital; comprehensive knowledge is rare
            {v:'none',p:8},{v:'hospital-only',p:30},{v:'a-few',p:55},{v:'most',p:78},{v:'comprehensive',p:95}
        ],
        'a-contact-plan': [
            // ~60% have no communication plan for network outages
            {v:'no-plan',p:15},{v:'vague',p:35},{v:'partial',p:55},{v:'solid',p:78},{v:'comprehensive',p:95}
        ],
        'a-regional-risks': [
            // ~45% are unaware of specific local risks; having taken action is rare
            {v:'unaware',p:12},{v:'vague',p:32},{v:'informed',p:55},{v:'detailed',p:78},{v:'prepared',p:95}
        ],
        'a-insurance': [
            // ~30% are underinsured; optimised coverage is uncommon
            {v:'no-insurance',p:8},{v:'dont-know',p:25},{v:'probably',p:45},{v:'checked',p:75},{v:'optimised',p:95}
        ],
        'a-evac-plan': [
            // ~65% have no evacuation plan; having practised is very rare
            {v:'no',p:15},{v:'one-route',p:35},{v:'basic-plan',p:55},{v:'solid-plan',p:80},{v:'practised',p:95}
        ],
        'a-cash': [
            // ~30% carry no cash at all; a month of cash reserves is very uncommon
            {v:'none',p:12},{v:'a-day',p:35},{v:'a-week',p:60},{v:'2-weeks',p:82},{v:'a-month',p:95}
        ],
        'a-documents': [
            // Most people don't have organised document storage; redundant copies are rare
            {v:'scattered',p:12},{v:'one-place',p:35},{v:'organised',p:55},{v:'backed-up',p:78},{v:'redundant',p:95}
        ],
        'a-scenarios': [
            // Most people haven't thought about extended disruption; being prepared is rare
            {v:'never',p:15},{v:'briefly',p:35},{v:'some-thought',p:55},{v:'planned',p:78},{v:'prepared',p:95}
        ]
    };

    var VALUE_ITEMS = {
        self_reliance: ['a-supplies', 'a-first-aid', 'a-skills'],
        community: ['a-neighbours', 'a-local-resources', 'a-contact-plan'],
        baseline: ['a-regional-risks', 'a-insurance', 'a-evac-plan'],
        catastrophic: ['a-cash', 'a-documents', 'a-scenarios']
    };

    // All emergency-preparedness items are scorable
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
        hintEl.textContent = pct !== null ? '~' + pct + 'th percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['self_reliance', 'community', 'baseline', 'catastrophic'].forEach(function(vk) {
            var pct = computeValuePercentile(vk);
            var barEl = document.getElementById('bar-' + vk);
            var valEl = document.getElementById('val-' + vk);
            if (barEl && valEl) {
                if (pct !== null) {
                    barEl.style.width = pct + '%';
                    valEl.textContent = pct + 'th';
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
        ['self_reliance', 'community', 'baseline', 'catastrophic'].forEach(function(vk) {
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
