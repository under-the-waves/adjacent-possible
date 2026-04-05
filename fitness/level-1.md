---
layout: default
title: "Fitness – Level 1: Awareness"
life_area_slug: fitness
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
.assess-input-group input[type="number"] {
    width: 100px;
    padding: 6px 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 0.95em;
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
.assess-multi-options {
    display: flex;
    flex-wrap: wrap;
    gap: 6px 14px;
    margin-bottom: 4px;
}
.assess-multi-options label {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 0.9em;
    cursor: pointer;
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

<h1>Fitness: Level 1</h1>

<p class="l1-subtitle">Understand what fitness means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Fitness Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why fitness matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Regular physical activity is one of the highest-leverage investments you can make in your quality of life. The evidence is unusually strong and broad.</p>

<p>People who exercise regularly have a <a href="https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(12)61031-9/fulltext" target="_blank">30 – 40% lower risk</a> of dying from any cause, with the biggest gains coming from simply moving from inactive to somewhat active. Even 15 minutes of daily exercise adds roughly 3 years to your lifespan.</p>

<p>The benefits go well beyond living longer. Exercise improves <a href="https://bjsm.bmj.com/content/52/3/154" target="_blank">memory, concentration, and creative thinking</a>. People who exercise report <a href="https://jamanetwork.com/journals/jamapsychiatry/article-abstract/2720689" target="_blank">43% fewer days</a> of poor mental health per month than those who don't. Exercise is now recommended as a <a href="https://www.nice.org.uk/guidance/cg90" target="_blank">first-line treatment</a> for mild-to-moderate depression.</p>

<p>Fitness also builds confidence, strengthens bones and joints, improves sleep quality, and creates opportunities for social connection. Few other investments touch as many areas of life simultaneously.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about fitness</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue fitness for different reasons. This site scores every fitness intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Health & Longevity</h3>
<p>Cardiovascular health, maintaining muscle mass as you age, joint integrity, and metabolic health. People who lean towards this value tend to focus on sustainable habits that keep them healthy for decades, with minimal injury risk.</p>

<h3>Physical Performance</h3>
<p>Strength, endurance, power, speed, coordination, and specific skills. What your body can do. People who lean towards this value often train for measurable improvements, sport-specific goals, or particular physical feats.</p>

<h3>Enjoyment & Psychological Benefits</h3>
<p>The pleasure, stress reduction, mood boost, community, and satisfaction of movement itself. People who lean towards this value pick activities they genuinely look forward to, and would keep exercising even if there were no health benefits.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each fitness value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Health & Longevity &ndash; Level 5</div>
    <p><a href="https://richroll.com/bio/" target="_blank">Rich Roll</a> was sedentary and overweight at 39. He overhauled his lifestyle and went on to complete five Ironman-distance triathlons on five Hawaiian islands in under a week. His writing and podcast focus almost entirely on healthspan and longevity rather than competition, and he seems to maintain very high cardiovascular fitness into his late 50s.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Physical Performance &ndash; Level 5</div>
    <p><a href="https://games.crossfit.com/athlete/32551" target="_blank">Adam Klink</a> is a CrossFit coach and former Division 1 college soccer goalkeeper. In 2020, at a bodyweight of 97 kg, he ran a sub-5-minute mile and back squatted 500 lb in the same day, finishing with 50 unbroken pull-ups. Few people combine that level of strength and endurance simultaneously.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Enjoyment & Psychological Benefits &ndash; Level 5</div>
    <p><a href="https://themirnavator.com/" target="_blank">Mirna Valerio</a> has completed over 14 ultramarathons and was named 2018 National Geographic Adventurer of the Year. She talks and writes primarily about joy, inclusion, and community in running rather than times or podium finishes. She has been running consistently for over 15 years and leads a visible community around it.</p>
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
<h4>Health &amp; Longevity</h4>

<div class="assess-input-group" id="ig-exercise-mins">
    <span class="assess-label">How many minutes of exercise do you get in a typical week?</span>
    <span class="assess-hint">Count anything that raises your heart rate &ndash; walking, cycling, sports, gym sessions.</span>
    <input type="number" id="a-exercise-mins" min="0" max="600" step="5" placeholder="e.g. 150" onchange="handleAssessInput('a-exercise-mins')"> <span class="assess-percentile-hint" id="pct-exercise-mins"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-exercise-mins" onchange="handleSkip('a-exercise-mins')"><label for="skip-exercise-mins">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-rhr">
    <span class="assess-label">What is your resting heart rate (beats per minute)?</span>
    <span class="assess-hint">Check with a fitness tracker, smartwatch, or take your pulse for 60 seconds first thing in the morning.</span>
    <input type="number" id="a-rhr" min="30" max="120" step="1" placeholder="e.g. 68" onchange="handleAssessInput('a-rhr')"> <span class="assess-percentile-hint" id="pct-rhr"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-rhr" onchange="handleSkip('a-rhr')"><label for="skip-rhr">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-strength-training">
    <span class="assess-label">How many strength training sessions do you do per week?</span>
    <span class="assess-hint">Weights, resistance bands, bodyweight exercises, or manual labour.</span>
    <select id="a-strength-training" onchange="handleAssessInput('a-strength-training')">
        <option value="">Select...</option>
        <option value="0">None</option>
        <option value="1">1 session per week</option>
        <option value="2">2 sessions per week</option>
        <option value="3">3 sessions per week</option>
        <option value="4">4 sessions per week</option>
        <option value="5">5+ sessions per week</option>
    </select> <span class="assess-percentile-hint" id="pct-strength-training"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-strength-training" onchange="handleSkip('a-strength-training')"><label for="skip-strength-training">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Physical Performance</h4>

<div class="assess-input-group" id="ig-pushups">
    <span class="assess-label">How many push-ups can you do in one set?</span>
    <span class="assess-hint">Do a quick test if you're not sure. Stop when your form breaks down.</span>
    <input type="number" id="a-pushups" min="0" max="200" step="1" placeholder="e.g. 15" onchange="handleAssessInput('a-pushups')"> <span class="assess-percentile-hint" id="pct-pushups"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-pushups" onchange="handleSkip('a-pushups')"><label for="skip-pushups">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-cardio">
    <span class="assess-label">How far can you run without stopping?</span>
    <span class="assess-hint">A rough estimate is fine. If you don't run, how far could you jog at a comfortable pace?</span>
    <select id="a-cardio" onchange="handleAssessInput('a-cardio')">
        <option value="">Select...</option>
        <option value="0">I can't run continuously at all</option>
        <option value="1">Less than 1 km</option>
        <option value="2">1 &ndash; 2 km</option>
        <option value="3">2 &ndash; 5 km</option>
        <option value="4">5 km (a full 5K)</option>
        <option value="5">5 &ndash; 10 km</option>
        <option value="6">10+ km</option>
    </select> <span class="assess-percentile-hint" id="pct-cardio"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-cardio" onchange="handleSkip('a-cardio')"><label for="skip-cardio">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-flexibility">
    <span class="assess-label">Can you touch your toes with straight legs?</span>
    <span class="assess-hint">A basic flexibility check. Try it now if you're not sure.</span>
    <select id="a-flexibility" onchange="handleAssessInput('a-flexibility')">
        <option value="">Select...</option>
        <option value="0">No &ndash; can't reach past shins</option>
        <option value="1">Almost &ndash; fingertips reach ankles</option>
        <option value="2">Yes &ndash; can touch toes</option>
        <option value="3">Yes &ndash; can place palms flat on floor</option>
    </select> <span class="assess-percentile-hint" id="pct-flexibility"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-flexibility" onchange="handleSkip('a-flexibility')"><label for="skip-flexibility">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Enjoyment &amp; Psychological Benefits</h4>

<div class="assess-input-group" id="ig-enjoy-types">
    <span class="assess-label">Which types of physical activity do you enjoy or think you might enjoy?</span>
    <span class="assess-hint">Select all that apply.</span>
    <div class="assess-multi-options">
        <label><input type="checkbox" class="enjoy-opt" value="team" onchange="handleMultiAssess('a-enjoy-types')"> Team sports</label>
        <label><input type="checkbox" class="enjoy-opt" value="solo" onchange="handleMultiAssess('a-enjoy-types')"> Solo exercise</label>
        <label><input type="checkbox" class="enjoy-opt" value="outdoor" onchange="handleMultiAssess('a-enjoy-types')"> Outdoor activities</label>
        <label><input type="checkbox" class="enjoy-opt" value="indoor" onchange="handleMultiAssess('a-enjoy-types')"> Indoor gym/studio</label>
        <label><input type="checkbox" class="enjoy-opt" value="competitive" onchange="handleMultiAssess('a-enjoy-types')"> Competitive events</label>
        <label><input type="checkbox" class="enjoy-opt" value="noncompetitive" onchange="handleMultiAssess('a-enjoy-types')"> Non-competitive movement</label>
        <label><input type="checkbox" class="enjoy-opt" value="none" onchange="handleMultiAssess('a-enjoy-types')"> None of these appeal to me</label>
    </div>
    <div class="assess-skip"><input type="checkbox" id="skip-enjoy-types" onchange="handleSkip('a-enjoy-types')"><label for="skip-enjoy-types">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-mood">
    <span class="assess-label">How does exercise affect your mood and energy levels?</span>
    <span class="assess-hint">Think about how you feel in the hours after exercising.</span>
    <select id="a-mood" onchange="handleAssessInput('a-mood')">
        <option value="">Select...</option>
        <option value="0">I don't exercise enough to know</option>
        <option value="1">No noticeable effect</option>
        <option value="2">Slight improvement</option>
        <option value="3">Clear positive effect on mood and energy</option>
        <option value="4">Major positive effect &ndash; exercise is my primary mood tool</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-mood" onchange="handleSkip('a-mood')"><label for="skip-mood">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-social">
    <span class="assess-label">Do you have a social or community element to your exercise?</span>
    <span class="assess-hint">A gym buddy, sports team, running group, yoga class, or similar.</span>
    <select id="a-social" onchange="handleAssessInput('a-social')">
        <option value="">Select...</option>
        <option value="0">None at all</option>
        <option value="1">Occasional &ndash; I sometimes exercise with others</option>
        <option value="2">Regular &ndash; I have a gym buddy, team, or class</option>
        <option value="3">Central &ndash; exercise community is a big part of my social life</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-social" onchange="handleSkip('a-social')"><label for="skip-social">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-health">
        <span class="assess-summary-label">Health &amp; Longevity</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-health" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-health">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-performance">
        <span class="assess-summary-label">Physical Performance</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-performance" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-performance">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data for American adults. Enjoyment &amp; Psychological Benefits are recorded for your awareness but not scored, as the available data does not support reliable percentile estimates.</p>
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

<p>You now understand why fitness matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about health and longevity, physical performance, and enjoyment. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/fitness/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Fitness Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Fitness. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/fitness/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'fitness';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-exercise-mins', 'a-rhr', 'a-strength-training',
        'a-pushups', 'a-cardio', 'a-flexibility',
        'a-enjoy-types', 'a-mood', 'a-social'
    ];

    // Scoring thresholds: [{value, percentile}, ...] sorted by value ascending
    // For inverted scales (lower = better), thresholds are sorted by value descending
    var THRESHOLDS = {
        'a-exercise-mins': [
            {v:0,p:5},{v:30,p:20},{v:90,p:40},{v:150,p:60},{v:225,p:72},{v:300,p:85},{v:450,p:95}
        ],
        'a-rhr': [ // inverted: lower is better
            {v:100,p:5},{v:90,p:10},{v:80,p:25},{v:72,p:50},{v:65,p:70},{v:58,p:85},{v:50,p:95},{v:40,p:99}
        ],
        'a-strength-training': [
            {v:'0',p:30},{v:'1',p:55},{v:'2',p:74},{v:'3',p:85},{v:'4',p:92},{v:'5',p:96}
        ],
        'a-pushups': [
            {v:0,p:5},{v:5,p:20},{v:10,p:40},{v:15,p:55},{v:20,p:70},{v:30,p:82},{v:40,p:90},{v:50,p:95}
        ],
        'a-cardio': [
            {v:'0',p:15},{v:'1',p:30},{v:'2',p:45},{v:'3',p:60},{v:'4',p:75},{v:'5',p:85},{v:'6',p:93}
        ],
        'a-flexibility': [
            {v:'0',p:25},{v:'1',p:45},{v:'2',p:65},{v:'3',p:85}
        ],
        'a-enjoy-types': 'multi', // handled separately
        'a-mood': [
            {v:'0',p:20},{v:'1',p:35},{v:'2',p:55},{v:'3',p:75},{v:'4',p:90}
        ],
        'a-social': [
            {v:'0',p:30},{v:'1',p:50},{v:'2',p:75},{v:'3',p:90}
        ]
    };

    var MULTI_THRESHOLDS = {
        'a-enjoy-types': [{count:0,p:15},{count:1,p:35},{count:2,p:55},{count:3,p:70},{count:4,p:85}]
    };

    var VALUE_ITEMS = {
        health: ['a-exercise-mins', 'a-rhr', 'a-strength-training'],
        performance: ['a-pushups', 'a-cardio', 'a-flexibility']
    };

    // Enjoyment items are recorded but not scored (insufficient population data)
    var UNSCORED_ITEMS = ['a-enjoy-types', 'a-mood', 'a-social'];

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

    // --- Scoring functions ---

    function interpolatePercentile(value, thresholds) {
        var num = parseFloat(value);
        // Check if thresholds use string keys (dropdowns)
        if (typeof thresholds[0].v === 'string') {
            for (var i = 0; i < thresholds.length; i++) {
                if (thresholds[i].v === String(value)) return thresholds[i].p;
            }
            return null;
        }
        // Check if inverted (first threshold has higher value than last)
        var inverted = thresholds[0].v > thresholds[thresholds.length - 1].v;
        if (inverted) {
            if (num >= thresholds[0].v) return thresholds[0].p;
            if (num <= thresholds[thresholds.length - 1].v) return thresholds[thresholds.length - 1].p;
            for (var i = 0; i < thresholds.length - 1; i++) {
                if (num <= thresholds[i].v && num >= thresholds[i + 1].v) {
                    var t = (thresholds[i].v - num) / (thresholds[i].v - thresholds[i + 1].v);
                    return Math.round(thresholds[i].p + t * (thresholds[i + 1].p - thresholds[i].p));
                }
            }
        } else {
            if (num <= thresholds[0].v) return thresholds[0].p;
            if (num >= thresholds[thresholds.length - 1].v) return thresholds[thresholds.length - 1].p;
            for (var i = 0; i < thresholds.length - 1; i++) {
                if (num >= thresholds[i].v && num <= thresholds[i + 1].v) {
                    var t = (num - thresholds[i].v) / (thresholds[i + 1].v - thresholds[i].v);
                    return Math.round(thresholds[i].p + t * (thresholds[i + 1].p - thresholds[i].p));
                }
            }
        }
        return null;
    }

    function scoreMulti(itemId) {
        var opts = document.querySelectorAll('.enjoy-opt');
        var noneChecked = false;
        var count = 0;
        opts.forEach(function(cb) {
            if (cb.value === 'none' && cb.checked) noneChecked = true;
            else if (cb.checked) count++;
        });
        if (noneChecked) count = 0;
        var mt = MULTI_THRESHOLDS[itemId];
        for (var i = mt.length - 1; i >= 0; i--) {
            if (count >= mt[i].count) return mt[i].p;
        }
        return mt[0].p;
    }

    function getItemPercentile(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return null;

        if (THRESHOLDS[itemId] === 'multi') {
            var opts = document.querySelectorAll('.enjoy-opt');
            var anyChecked = false;
            opts.forEach(function(cb) { if (cb.checked) anyChecked = true; });
            return anyChecked ? scoreMulti(itemId) : null;
        }

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

    function isItemAnswered(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return true;

        if (THRESHOLDS[itemId] === 'multi') {
            var opts = document.querySelectorAll('.enjoy-opt');
            var any = false;
            opts.forEach(function(cb) { if (cb.checked) any = true; });
            return any;
        }

        var el = document.getElementById(itemId);
        return el && el.value !== '' && el.value !== null;
    }

    function updatePercentileHint(itemId) {
        if (UNSCORED_ITEMS.indexOf(itemId) !== -1) return; // no hints for unscored items
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

    function updateInputGroupState(itemId) {
        var group = document.getElementById('ig-' + itemId.replace('a-', ''));
        if (group) group.classList.toggle('answered', isItemAnswered(itemId));
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['health', 'performance'].forEach(function(vk) {
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

    function saveAnswers() {
        var answers = {};
        ASSESS_IDS.forEach(function(id) {
            var skipBox = document.getElementById('skip-' + id.replace('a-', ''));
            var skipped = skipBox && skipBox.checked;
            var value = null;

            if (!skipped) {
                if (THRESHOLDS[id] === 'multi') {
                    var selected = [];
                    document.querySelectorAll('.enjoy-opt').forEach(function(cb) {
                        if (cb.checked) selected.push(cb.value);
                    });
                    value = selected;
                } else {
                    var el = document.getElementById(id);
                    if (el && el.value !== '') value = el.value;
                }
            }
            answers[id] = { value: value, skipped: skipped };
        });
        // Save raw answers directly to localStorage (NOT via APStorage)
        var allAnswers = {};
        try { allAnswers = JSON.parse(localStorage.getItem('ap-level1-answers')) || {}; } catch(e) {}
        allAnswers[AREA] = answers;
        localStorage.setItem('ap-level1-answers', JSON.stringify(allAnswers));

        // Save booleans to ap-level1-assess for backward compat (via APStorage, syncs to Clerk)
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
        ['health', 'performance'].forEach(function(vk) {
            scores[vk] = computeValuePercentile(vk);
        });
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-scores') || {};
            all[AREA] = scores;
            APStorage.save('ap-level1-scores', all);
        }
    }

    function updateAssessCompletion() {
        var allAnswered = ASSESS_IDS.every(function(id) { return isItemAnswered(id); });
        var btn = document.getElementById('assessBtn');
        if (btn) {
            btn.disabled = !allAnswered;
            btn.textContent = allAnswered ? 'All done \u2013 continue' : 'Answer all items to continue';
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

    window.handleMultiAssess = function(itemId) {
        // If "none" is checked, uncheck all others; if another is checked, uncheck "none"
        var opts = document.querySelectorAll('.enjoy-opt');
        var clickedNone = false;
        opts.forEach(function(cb) {
            if (cb.value === 'none' && cb.checked) clickedNone = true;
        });
        if (clickedNone) {
            opts.forEach(function(cb) { if (cb.value !== 'none') cb.checked = false; });
        } else {
            opts.forEach(function(cb) { if (cb.value === 'none') cb.checked = false; });
        }
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
            if (skipBox.checked && input.type === 'number') input.value = '';
        }
        // For multi-select, disable all checkboxes
        if (THRESHOLDS[itemId] === 'multi') {
            var opts = document.querySelectorAll('.enjoy-opt');
            opts.forEach(function(cb) {
                cb.disabled = skipBox.checked;
                if (skipBox.checked) cb.checked = false;
            });
        }
        updatePercentileHint(itemId);
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessSummary();
        updateAssessCompletion();
    };

    // Override completeStep to also save scores
    var _origCompleteStep = window.completeStep;
    window.completeStep = function(step) {
        if (step === 'assess') saveScores();
        _origCompleteStep(step);
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
                    if (THRESHOLDS[id] === 'multi') {
                        document.querySelectorAll('.enjoy-opt').forEach(function(cb) { cb.disabled = true; });
                    }
                }
            } else if (item.value !== null) {
                if (THRESHOLDS[id] === 'multi' && Array.isArray(item.value)) {
                    document.querySelectorAll('.enjoy-opt').forEach(function(cb) {
                        cb.checked = item.value.indexOf(cb.value) !== -1;
                    });
                } else {
                    var el = document.getElementById(id);
                    if (el) el.value = item.value;
                }
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
