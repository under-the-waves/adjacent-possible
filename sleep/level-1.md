---
layout: default
title: "Sleep – Level 1: Awareness"
life_area_slug: sleep
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

<h1>Sleep: Level 1</h1>

<p class="l1-subtitle">Understand what sleep does, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Sleep Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why sleep matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Sleep occupies roughly a third of your life, and what happens during those hours shapes nearly everything about the other two-thirds. The evidence for its importance is broad and consistent across decades of research.</p>

<p>Adults who regularly sleep fewer than seven hours have a <a href="https://pubmed.ncbi.nlm.nih.gov/28364328/" target="_blank">13% higher risk</a> of dying from any cause. Short sleep is independently linked to heart disease, type 2 diabetes, obesity, and depression. The relationship between sleep and health runs in both directions: poor sleep worsens chronic conditions, and chronic conditions worsen sleep.</p>

<p>The effects on daily performance are equally striking. After <a href="https://pubmed.ncbi.nlm.nih.gov/10984335/" target="_blank">17 &ndash; 19 hours without sleep</a>, reaction time and decision-making deteriorate to levels comparable to a blood alcohol concentration of 0.05%. Cumulative sleep restriction over two weeks &ndash; sleeping six hours a night instead of eight &ndash; produces <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2656292/" target="_blank">cognitive impairment equivalent to two nights of total sleep deprivation</a>, and people consistently underestimate how impaired they are.</p>

<p>Sleep also consolidates memory, regulates appetite hormones, supports immune function, and affects emotional resilience. Few other behaviours touch as many systems simultaneously, and unlike many health interventions, improving sleep often produces noticeable benefits within days.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about sleep</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People improve their sleep for different reasons. This site scores every sleep intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Daily Functioning</h3>
<p>Mental alertness, energy levels, focus, mood stability, and physical recovery. People who lean towards this value want sleep that makes them feel sharp and capable the next day. They tend to care most about waking refreshed, sustaining concentration through the afternoon, and having steady energy without relying on caffeine.</p>

<h3>Long-term Health</h3>
<p>Disease prevention, longevity, and brain health over years and decades. People who lean towards this value treat sleep as a long-term investment. They focus on consistent duration, sleep architecture (the balance of deep and REM sleep), and reducing the cumulative health risks that come from chronic sleep debt.</p>

<h3>Comfort & Experience</h3>
<p>The subjective quality of sleep itself &ndash; how easily you fall asleep, whether you stay asleep through the night, and how pleasant the experience feels. People who lean towards this value care about the sleep environment, bedtime routines, and waking without an alarm. They want sleep to feel good, not just be adequate.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each sleep value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Daily Functioning &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/LeBron_James" target="_blank">LeBron James</a> averages around 10 &ndash; 12 hours of sleep per day, split between 8 &ndash; 9 hours at night and a 2 &ndash; 3 hour afternoon nap. He keeps his bedroom at 20 &ndash; 21&deg;C, completely dark, and avoids screens for 45 minutes before bed. He has called sleep "the best way for your body to physically and emotionally recover and get back to 100 percent." He seems to have maintained this routine throughout a 21-season NBA career, playing at a high level into his early 40s.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Long-term Health &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Tom_Brady" target="_blank">Tom Brady</a> went to bed at 8:30 pm and slept at least 9 hours a night for most of his professional career, treating sleep as a central pillar of his TB12 Method alongside nutrition and training. He played in the NFL until age 45, winning his seventh Super Bowl at 43 &ndash; an age at which most players have been retired for over a decade. By all accounts, his sleep discipline was non-negotiable rather than aspirational.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Comfort &amp; Experience &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Arianna_Huffington" target="_blank">Arianna Huffington</a> treats her transition to sleep as what she calls a "sacrosanct ritual." She takes a hot bath with epsom salts and a candle, changes into dedicated sleepwear, bans all electronic devices from her bedroom, and reads only physical books in bed. She reportedly gets eight hours of sleep 95% of nights. After collapsing from exhaustion in 2007, she redesigned her entire relationship with sleep around comfort and enjoyment rather than treating it as a necessary inconvenience.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few days to observe or look up.</p>

<div class="assess-group">
<h4>Daily Functioning</h4>

<div class="assess-input-group" id="ig-sleep-hours">
    <span class="assess-label">How many hours do you typically sleep per night?</span>
    <span class="assess-hint">Check a sleep tracker or estimate from when you fall asleep to when you wake up. Use your weeknight average.</span>
    <input type="number" id="a-sleep-hours" min="3" max="12" step="0.5" placeholder="e.g. 7" onchange="handleAssessInput('a-sleep-hours')"> <span class="assess-percentile-hint" id="pct-sleep-hours"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-sleep-hours" onchange="handleSkip('a-sleep-hours')"><label for="skip-sleep-hours">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-wake-refreshed">
    <span class="assess-label">How often do you wake up feeling genuinely refreshed and alert?</span>
    <span class="assess-hint">Think about the past two weeks.</span>
    <select id="a-wake-refreshed" onchange="handleAssessInput('a-wake-refreshed')">
        <option value="">Select...</option>
        <option value="0">Rarely or never</option>
        <option value="1">Some days (1 &ndash; 3 per week)</option>
        <option value="2">Most days (4 &ndash; 5 per week)</option>
        <option value="3">Almost every day (6 &ndash; 7 per week)</option>
    </select> <span class="assess-percentile-hint" id="pct-wake-refreshed"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-wake-refreshed" onchange="handleSkip('a-wake-refreshed')"><label for="skip-wake-refreshed">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-caffeine">
    <span class="assess-label">How much do you rely on caffeine to function during the day?</span>
    <span class="assess-hint">Consider coffee, tea, energy drinks, and soft drinks.</span>
    <select id="a-caffeine" onchange="handleAssessInput('a-caffeine')">
        <option value="">Select...</option>
        <option value="0">I need caffeine to feel normal &ndash; 4+ servings per day</option>
        <option value="1">I rely on it most days &ndash; 2 &ndash; 3 servings</option>
        <option value="2">I drink it occasionally but don't need it</option>
        <option value="3">I rarely or never consume caffeine</option>
    </select> <span class="assess-percentile-hint" id="pct-caffeine"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-caffeine" onchange="handleSkip('a-caffeine')"><label for="skip-caffeine">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Long-term Health</h4>

<div class="assess-input-group" id="ig-bedtime-variability">
    <span class="assess-label">By how many minutes does your bedtime vary across the week?</span>
    <span class="assess-hint">Compare your earliest and latest bedtimes over a typical week, including weekends. Enter the difference in minutes.</span>
    <input type="number" id="a-bedtime-variability" min="0" max="300" step="5" placeholder="e.g. 60" onchange="handleAssessInput('a-bedtime-variability')"> <span class="assess-percentile-hint" id="pct-bedtime-variability"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-bedtime-variability" onchange="handleSkip('a-bedtime-variability')"><label for="skip-bedtime-variability">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-weekday-weekend">
    <span class="assess-label">How different is your sleep schedule on weekdays versus weekends?</span>
    <span class="assess-hint">Think about both bedtime and wake time.</span>
    <select id="a-weekday-weekend" onchange="handleAssessInput('a-weekday-weekend')">
        <option value="">Select...</option>
        <option value="0">Very different &ndash; 2+ hours shift on weekends</option>
        <option value="1">Noticeably different &ndash; 1 &ndash; 2 hour shift</option>
        <option value="2">Slightly different &ndash; 30 &ndash; 60 minute shift</option>
        <option value="3">Almost identical &ndash; less than 30 minutes</option>
    </select> <span class="assess-percentile-hint" id="pct-weekday-weekend"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-weekday-weekend" onchange="handleSkip('a-weekday-weekend')"><label for="skip-weekday-weekend">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-snoring">
    <span class="assess-label">Do you snore, gasp, or stop breathing during sleep?</span>
    <span class="assess-hint">Ask a partner or housemate, or use a phone app that records audio overnight. This can indicate sleep apnoea.</span>
    <select id="a-snoring" onchange="handleAssessInput('a-snoring')">
        <option value="">Select...</option>
        <option value="no">No &ndash; confirmed by a bed partner or recording</option>
        <option value="mild">Occasional light snoring</option>
        <option value="yes">Regular snoring, gasping, or possible apnoea</option>
        <option value="unsure">I'm not sure &ndash; I haven't checked</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-snoring" onchange="handleSkip('a-snoring')"><label for="skip-snoring">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Comfort &amp; Experience</h4>

<div class="assess-input-group" id="ig-sleep-latency">
    <span class="assess-label">How many minutes does it typically take you to fall asleep?</span>
    <span class="assess-hint">Under 5 minutes may suggest sleep debt. Over 30 minutes may suggest difficulty winding down. 10 &ndash; 20 minutes is typical.</span>
    <input type="number" id="a-sleep-latency" min="0" max="120" step="1" placeholder="e.g. 15" onchange="handleAssessInput('a-sleep-latency')"> <span class="assess-percentile-hint" id="pct-sleep-latency"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-sleep-latency" onchange="handleSkip('a-sleep-latency')"><label for="skip-sleep-latency">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-sleep-efficiency">
    <span class="assess-label">What is your estimated sleep efficiency?</span>
    <span class="assess-hint">The percentage of time in bed that you spend actually sleeping. If you sleep 7 hours in an 8-hour window, that's about 88%. A sleep tracker can give you this number directly.</span>
    <input type="number" id="a-sleep-efficiency" min="50" max="100" step="1" placeholder="e.g. 88" onchange="handleAssessInput('a-sleep-efficiency')"> <span class="assess-percentile-hint" id="pct-sleep-efficiency"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-sleep-efficiency" onchange="handleSkip('a-sleep-efficiency')"><label for="skip-sleep-efficiency">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-night-waking">
    <span class="assess-label">How often do you wake during the night?</span>
    <span class="assess-hint">Count awakenings you're aware of on a typical night.</span>
    <select id="a-night-waking" onchange="handleAssessInput('a-night-waking')">
        <option value="">Select...</option>
        <option value="0">3+ times, often with difficulty getting back to sleep</option>
        <option value="1">2 &ndash; 3 times, but I get back to sleep fairly quickly</option>
        <option value="2">Once or twice briefly</option>
        <option value="3">I rarely or never wake during the night</option>
    </select> <span class="assess-percentile-hint" id="pct-night-waking"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-night-waking" onchange="handleSkip('a-night-waking')"><label for="skip-night-waking">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-daily">
        <span class="assess-summary-label">Daily Functioning</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-daily" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-daily">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-long">
        <span class="assess-summary-label">Long-term Health</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-long" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-long">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-comfort">
        <span class="assess-summary-label">Comfort &amp; Experience</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-comfort" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-comfort">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data for adults. Snoring awareness is recorded for your information but not scored, as the available data does not support reliable percentile estimates.</p>
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

<p>You now understand why sleep matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about daily functioning, long-term health, and comfort and experience. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/sleep/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Sleep Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Sleep. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/sleep/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'sleep';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-sleep-hours', 'a-wake-refreshed', 'a-caffeine',
        'a-bedtime-variability', 'a-weekday-weekend', 'a-snoring',
        'a-sleep-latency', 'a-sleep-efficiency', 'a-night-waking'
    ];

    // Scoring thresholds: [{v, p}, ...] sorted by value ascending
    // For inverted scales (lower = better), thresholds are sorted by value descending
    var THRESHOLDS = {
        'a-sleep-hours': [ // optimal range is 7-9; both short and long sleep score lower
            {v:4,p:5},{v:5,p:15},{v:5.5,p:25},{v:6,p:35},{v:6.5,p:50},{v:7,p:70},{v:7.5,p:82},{v:8,p:90},{v:8.5,p:85},{v:9,p:75},{v:10,p:50}
        ],
        'a-wake-refreshed': [
            {v:'0',p:15},{v:'1',p:40},{v:'2',p:65},{v:'3',p:90}
        ],
        'a-caffeine': [
            {v:'0',p:10},{v:'1',p:35},{v:'2',p:65},{v:'3',p:92}
        ],
        'a-bedtime-variability': [ // inverted: lower is better
            {v:240,p:5},{v:180,p:10},{v:120,p:20},{v:90,p:35},{v:60,p:55},{v:30,p:80},{v:15,p:92},{v:0,p:98}
        ],
        'a-weekday-weekend': [
            {v:'0',p:10},{v:'1',p:30},{v:'2',p:60},{v:'3',p:88}
        ],
        'a-snoring': 'unscored',
        'a-sleep-latency': [ // optimal is 10-20 min; both very fast and very slow score lower
            {v:0,p:30},{v:5,p:55},{v:10,p:80},{v:15,p:90},{v:20,p:80},{v:30,p:50},{v:45,p:25},{v:60,p:10},{v:90,p:5}
        ],
        'a-sleep-efficiency': [ // higher is better
            {v:60,p:5},{v:70,p:15},{v:75,p:25},{v:80,p:40},{v:85,p:55},{v:88,p:65},{v:90,p:75},{v:93,p:85},{v:95,p:92},{v:98,p:97}
        ],
        'a-night-waking': [
            {v:'0',p:10},{v:'1',p:35},{v:'2',p:65},{v:'3',p:90}
        ]
    };

    var VALUE_ITEMS = {
        daily: ['a-sleep-hours', 'a-wake-refreshed', 'a-caffeine'],
        long: ['a-bedtime-variability', 'a-weekday-weekend'],
        comfort: ['a-sleep-latency', 'a-sleep-efficiency', 'a-night-waking']
    };

    // Snoring is recorded but not scored (qualitative awareness item)
    var UNSCORED_ITEMS = ['a-snoring'];

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

    function getItemPercentile(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return null;

        if (THRESHOLDS[itemId] === 'unscored') return null;

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
        ['daily', 'long', 'comfort'].forEach(function(vk) {
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
                var el = document.getElementById(id);
                if (el && el.value !== '') value = el.value;
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
        ['daily', 'long', 'comfort'].forEach(function(vk) {
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

    window.handleSkip = function(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        var input = document.getElementById(itemId);
        if (skipBox && input) {
            input.disabled = skipBox.checked;
            if (skipBox.checked && input.tagName === 'SELECT') input.value = '';
            if (skipBox.checked && input.type === 'number') input.value = '';
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
