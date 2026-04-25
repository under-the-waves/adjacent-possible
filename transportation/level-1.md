---
layout: default
title: "Transportation – Level 1: Awareness"
life_area_slug: transportation
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

<h1>Transportation: Level 1</h1>

<p class="l1-subtitle">Understand what transportation means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Transportation Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why transportation matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>How you get around each day is one of those things most people accept as fixed rather than actively design. Yet transportation consumes a significant share of both your time and money, and the choices you make about it affect your health, stress levels, and overall quality of life.</p>

<p>Average commute times range from <a href="https://link.springer.com/article/10.1007/s11116-019-09983-9" target="_blank">40 to 80 minutes per day</a>, and transportation is typically the second-largest household expense after housing. Many people spend 15 – 20% of their income on getting around.</p>

<p>The mode you choose matters more than you might expect. Research consistently shows that <a href="https://www.sciencedirect.com/science/article/pii/S0965856420305620" target="_blank">active commuters – walkers and cyclists – report the highest satisfaction</a>, while long car and public transit commutes generate the lowest. Switching from car travel to active travel shows <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4262577/" target="_blank">significant positive effects on psychological wellbeing</a>.</p>

<p>Unlike many life areas, transportation can often be substantially improved through a single decision: moving closer to work, changing commute mode, or restructuring errand patterns. Few other changes deliver such a large daily quality-of-life improvement for a one-off effort.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about transportation</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach transportation for different reasons. This site scores every transportation intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Efficiency</h3>
<p>Minimising the time, money, and cognitive effort spent on transportation. People who lean towards this value treat transportation as a resource to optimise – reducing unnecessary trips, batching errands, choosing modes that maximise productive or enjoyable use of travel time, and structuring their lives to minimise wasted transit.</p>

<h3>Comfort</h3>
<p>The physical and psychological experience of your daily transportation – pleasant, stress-free, and compatible with your preferences. People who lean towards this value invest in making the journey itself enjoyable: vehicle quality, commute environment, protection from weather, and the overall pleasantness of their travel experience.</p>

<h3>Safety</h3>
<p>Minimising the risk of injury, accident, or incident during transportation. People who lean towards this value make travel decisions based on risk reduction: vehicle safety features, route selection, defensive driving or cycling practices, and choosing modes with strong safety records.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each transportation value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Efficiency &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Chris_Boardman" target="_blank">Chris Boardman</a> is an Olympic gold medallist cyclist who became Greater Manchester's cycling and walking commissioner. He commutes by bike, uses public transport, and has structured his own daily travel around efficiency rather than speed. His advocacy for active transport infrastructure is grounded in his personal practice &ndash; he has said he does not own a car and designs his life around not needing one.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Comfort &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Doug_DeMuro" target="_blank">Doug DeMuro</a> has built a career around evaluating the comfort and experience of vehicles across every price range. He owns and has personally tested hundreds of cars, and his detailed reviews focus heavily on ride quality, cabin environment, and the day-to-day experience of living with a vehicle. His approach treats every journey as an experience worth optimising.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Safety &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Tiff_Needell" target="_blank">Tiff Needell</a> is a former racing driver and long-time motoring presenter who has spent decades teaching advanced driving techniques to the public. His work on defensive and high-performance driving combines professional-level vehicle control with an emphasis on hazard anticipation and safe road behaviour, demonstrated across thousands of hours of on-road instruction.</p>
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
<h4>Efficiency</h4>

<div class="assess-input-group" id="ig-commute-time">
    <span class="assess-label">How long is your daily commute, door to door?</span>
    <span class="assess-hint">Include walking to and from your vehicle or station, waiting time, and any transfers.</span>
    <select id="a-commute-time" onchange="handleAssessInput('a-commute-time')">
        <option value="">Select...</option>
        <option value="over-60">Over 60 minutes each way</option>
        <option value="40-60">40&ndash;60 minutes each way</option>
        <option value="20-40">20&ndash;40 minutes each way</option>
        <option value="under-20">Under 20 minutes each way</option>
        <option value="wfh">I work from home or within walking distance</option>
    </select> <span class="assess-percentile-hint" id="pct-commute-time"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-commute-time" onchange="handleSkip('a-commute-time')"><label for="skip-commute-time">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-transport-cost">
    <span class="assess-label">How much do you spend on transportation each month?</span>
    <span class="assess-hint">Include fuel or fares, insurance, maintenance, parking, and any vehicle payments.</span>
    <select id="a-transport-cost" onchange="handleAssessInput('a-transport-cost')">
        <option value="">Select...</option>
        <option value="over-500">Over &pound;500</option>
        <option value="300-500">&pound;300&ndash;&pound;500</option>
        <option value="150-300">&pound;150&ndash;&pound;300</option>
        <option value="50-150">&pound;50&ndash;&pound;150</option>
        <option value="under-50">Under &pound;50</option>
    </select> <span class="assess-percentile-hint" id="pct-transport-cost"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-transport-cost" onchange="handleSkip('a-transport-cost')"><label for="skip-transport-cost">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-errand-pattern">
    <span class="assess-label">Are your errands batched or spread across multiple separate trips?</span>
    <span class="assess-hint">Grocery shopping, appointments, and other regular tasks that require travel.</span>
    <select id="a-errand-pattern" onchange="handleAssessInput('a-errand-pattern')">
        <option value="">Select...</option>
        <option value="many-trips">Many separate trips &ndash; one errand per outing</option>
        <option value="mostly-separate">Mostly separate &ndash; I batch occasionally</option>
        <option value="mixed">Mixed &ndash; I batch some but not all</option>
        <option value="mostly-batched">Mostly batched &ndash; I combine errands when I can</option>
        <option value="fully-batched">Fully batched &ndash; I plan routes and combine everything</option>
    </select> <span class="assess-percentile-hint" id="pct-errand-pattern"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-errand-pattern" onchange="handleSkip('a-errand-pattern')"><label for="skip-errand-pattern">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Comfort</h4>

<div class="assess-input-group" id="ig-commute-experience">
    <span class="assess-label">How does your daily commute feel?</span>
    <span class="assess-hint">Noise, crowding, temperature, traffic, and how you feel when you arrive.</span>
    <select id="a-commute-experience" onchange="handleAssessInput('a-commute-experience')">
        <option value="">Select...</option>
        <option value="stressful">Stressful &ndash; I dread it</option>
        <option value="unpleasant">Unpleasant &ndash; tolerable but draining</option>
        <option value="neutral">Neutral &ndash; it's fine</option>
        <option value="pleasant">Pleasant &ndash; I don't mind it</option>
        <option value="enjoyable">Enjoyable &ndash; I use the time well or actively enjoy it</option>
    </select> <span class="assess-percentile-hint" id="pct-commute-experience"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-commute-experience" onchange="handleSkip('a-commute-experience')"><label for="skip-commute-experience">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-vehicle-condition">
    <span class="assess-label">What is the condition of your primary mode of transport?</span>
    <span class="assess-hint">Car, bicycle, bus, or train &ndash; is it well-maintained, comfortable, and reliable?</span>
    <select id="a-vehicle-condition" onchange="handleAssessInput('a-vehicle-condition')">
        <option value="">Select...</option>
        <option value="poor">Poor &ndash; unreliable or uncomfortable</option>
        <option value="fair">Fair &ndash; works but has issues</option>
        <option value="adequate">Adequate &ndash; functional and reasonably comfortable</option>
        <option value="good">Good &ndash; well-maintained and comfortable</option>
        <option value="excellent">Excellent &ndash; reliable, comfortable, and well-suited to my needs</option>
    </select> <span class="assess-percentile-hint" id="pct-vehicle-condition"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-vehicle-condition" onchange="handleSkip('a-vehicle-condition')"><label for="skip-vehicle-condition">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-weather-impact">
    <span class="assess-label">How much does weather affect your transportation experience?</span>
    <span class="assess-hint">Do rain, cold, or heat make your commute significantly worse?</span>
    <select id="a-weather-impact" onchange="handleAssessInput('a-weather-impact')">
        <option value="">Select...</option>
        <option value="severely">Severely &ndash; bad weather makes travel very difficult</option>
        <option value="significantly">Significantly &ndash; it's noticeably worse</option>
        <option value="moderately">Moderately &ndash; some impact but manageable</option>
        <option value="slightly">Slightly &ndash; I'm mostly protected from weather</option>
        <option value="not-at-all">Not at all &ndash; weather has no effect on my transport</option>
    </select> <span class="assess-percentile-hint" id="pct-weather-impact"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-weather-impact" onchange="handleSkip('a-weather-impact')"><label for="skip-weather-impact">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Safety</h4>

<div class="assess-input-group" id="ig-risk-awareness">
    <span class="assess-label">How well do you know the main safety risks of your current transportation modes?</span>
    <span class="assess-hint">Accident rates, dangerous junctions on your route, or common hazards.</span>
    <select id="a-risk-awareness" onchange="handleAssessInput('a-risk-awareness')">
        <option value="">Select...</option>
        <option value="unaware">Unaware &ndash; I haven't thought about this</option>
        <option value="vague">Vague &ndash; I know driving/cycling has risks but nothing specific</option>
        <option value="basic">Basic &ndash; I know the main risks</option>
        <option value="informed">Informed &ndash; I know specific risks for my routes and modes</option>
        <option value="proactive">Proactive &ndash; I've adjusted my behaviour based on risk knowledge</option>
    </select> <span class="assess-percentile-hint" id="pct-risk-awareness"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-risk-awareness" onchange="handleSkip('a-risk-awareness')"><label for="skip-risk-awareness">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-safety-features">
    <span class="assess-label">Do you know what safety features your primary vehicle or mode has?</span>
    <span class="assess-hint">ABS, airbags, tyre condition, lights, reflective gear, helmet.</span>
    <select id="a-safety-features" onchange="handleAssessInput('a-safety-features')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I don't know</option>
        <option value="vague">Vague &ndash; I know it has some but not the details</option>
        <option value="basic">Basic &ndash; I know the main safety features</option>
        <option value="detailed">Detailed &ndash; I know what I have and what I'm missing</option>
        <option value="optimised">Optimised &ndash; I've added or upgraded safety features</option>
    </select> <span class="assess-percentile-hint" id="pct-safety-features"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-safety-features" onchange="handleSkip('a-safety-features')"><label for="skip-safety-features">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-defensive-habits">
    <span class="assess-label">Do you practise defensive habits when travelling?</span>
    <span class="assess-hint">Consistent seat belt use, mirror checks, safe following distance, cycling with lights and a helmet.</span>
    <select id="a-defensive-habits" onchange="handleAssessInput('a-defensive-habits')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I don't think about it</option>
        <option value="sometimes">Sometimes &ndash; I'm inconsistent</option>
        <option value="mostly">Mostly &ndash; I usually follow safe practices</option>
        <option value="consistently">Consistently &ndash; defensive habits are automatic</option>
        <option value="exemplary">Exemplary &ndash; I go beyond basics with advanced safety practices</option>
    </select> <span class="assess-percentile-hint" id="pct-defensive-habits"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-defensive-habits" onchange="handleSkip('a-defensive-habits')"><label for="skip-defensive-habits">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-efficiency">
        <span class="assess-summary-label">Efficiency</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-efficiency" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-efficiency">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-comfort">
        <span class="assess-summary-label">Comfort</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-comfort" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-comfort">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-safety">
        <span class="assess-summary-label">Safety</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-safety" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-safety">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on transportation behaviour among adults. All items in this area are scored.</p>
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

<p>You now understand why transportation matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about efficiency, comfort, and safety. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/transportation/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Transportation Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Transportation. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/transportation/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'transportation';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-commute-time',
        'a-transport-cost',
        'a-errand-pattern',
        'a-commute-experience',
        'a-vehicle-condition',
        'a-weather-impact',
        'a-risk-awareness',
        'a-safety-features',
        'a-defensive-habits'
    ];

    var THRESHOLDS = {
        'a-commute-time': [
            // Median UK commute is ~30 min each way; WFH or under 20 min is top quartile
            {v:'over-60',p:10},{v:'40-60',p:30},{v:'20-40',p:55},{v:'under-20',p:78},{v:'wfh',p:95}
        ],
        'a-transport-cost': [
            // Median UK transport spend is ~\u00a3200-300/month; under \u00a350 is very low
            {v:'over-500',p:10},{v:'300-500',p:30},{v:'150-300',p:50},{v:'50-150',p:75},{v:'under-50',p:95}
        ],
        'a-errand-pattern': [
            // Most people make many separate trips; fully batched route planning is rare
            {v:'many-trips',p:10},{v:'mostly-separate',p:30},{v:'mixed',p:50},{v:'mostly-batched',p:75},{v:'fully-batched',p:95}
        ],
        'a-commute-experience': [
            // Most commuters report neutral to negative experiences; genuinely enjoyable is uncommon
            {v:'stressful',p:10},{v:'unpleasant',p:25},{v:'neutral',p:50},{v:'pleasant',p:75},{v:'enjoyable',p:95}
        ],
        'a-vehicle-condition': [
            // Most vehicles are adequate; excellent condition and fit is uncommon
            {v:'poor',p:10},{v:'fair',p:25},{v:'adequate',p:50},{v:'good',p:75},{v:'excellent',p:95}
        ],
        'a-weather-impact': [
            // Weather significantly affects most commuters; full protection is relatively uncommon
            {v:'severely',p:10},{v:'significantly',p:30},{v:'moderately',p:50},{v:'slightly',p:75},{v:'not-at-all',p:95}
        ],
        'a-risk-awareness': [
            // Most people have only vague awareness of transport safety risks
            {v:'unaware',p:10},{v:'vague',p:30},{v:'basic',p:55},{v:'informed',p:78},{v:'proactive',p:95}
        ],
        'a-safety-features': [
            // Most people know their vehicle has safety features but not the details
            {v:'no',p:10},{v:'vague',p:30},{v:'basic',p:55},{v:'detailed',p:78},{v:'optimised',p:95}
        ],
        'a-defensive-habits': [
            // Most people follow basic safety practices; exemplary defensive habits are rare
            {v:'no',p:10},{v:'sometimes',p:25},{v:'mostly',p:50},{v:'consistently',p:78},{v:'exemplary',p:95}
        ]
    };

    var VALUE_ITEMS = {
        efficiency: ['a-commute-time', 'a-transport-cost', 'a-errand-pattern'],
        comfort: ['a-commute-experience', 'a-vehicle-condition', 'a-weather-impact'],
        safety: ['a-risk-awareness', 'a-safety-features', 'a-defensive-habits']
    };

    // All transportation items are scorable
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
        hintEl.textContent = pct !== null ? '~' + ordinalSuffix(pct) + ' percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['efficiency', 'comfort', 'safety'].forEach(function(vk) {
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
        ['efficiency', 'comfort', 'safety'].forEach(function(vk) {
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
