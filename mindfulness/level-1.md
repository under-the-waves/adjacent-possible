---
layout: default
title: "Mindfulness – Level 1: Awareness"
life_area_slug: mindfulness
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

<h1>Mindfulness: Level 1</h1>

<p class="l1-subtitle">Understand what mindfulness means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Mindfulness Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why mindfulness matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Mindfulness &ndash; the systematic practice of present-moment awareness &ndash; is one of the most extensively studied approaches to improving psychological functioning. The evidence base spans thousands of studies and multiple decades.</p>

<p>A <a href="https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/1809754" target="_blank">2014 meta-analysis in JAMA Internal Medicine</a> found that mindfulness meditation programmes produce moderate improvements in anxiety, depression, and pain. These effects are comparable to the benefits of antidepressant medication for mild-to-moderate depression, without the side effects.</p>

<p>Regular practice also improves <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5103185/" target="_blank">attention, working memory, and executive function</a>. People who meditate consistently show measurable changes in brain regions associated with attention regulation, emotional processing, and self-awareness. Even brief interventions &ndash; as short as four days of practice &ndash; produce <a href="https://pubmed.ncbi.nlm.nih.gov/20363650/" target="_blank">detectable improvements in mood and cognitive performance</a>.</p>

<p>Beyond cognitive and emotional benefits, mindfulness practice is associated with reduced blood pressure, improved immune function, and better sleep quality. Few other practices simultaneously improve thinking, emotional regulation, physical health, and subjective wellbeing.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about mindfulness</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue mindfulness for different reasons. This site scores every mindfulness intervention across four core values. Later, you'll set your own weighting across these values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Mental Clarity</h3>
<p>Enhanced cognitive function including sustained attention, mental focus, and clarity of thinking. Improved concentration at work, reduced mental fog, greater ability to stay present during conversations, and enhanced capacity to direct attention deliberately. People who prioritise this value focus on practices that strengthen the ability to direct and sustain attention.</p>

<h3>Emotional Wellbeing</h3>
<p>Increased emotional resilience, reduced reactivity, and greater equanimity during challenging situations. Better stress management, less overwhelm during difficult periods, improved mood stability, and the ability to respond rather than react to emotional triggers. Those who prioritise this value seek practices that provide immediate stress relief and long-term emotional balance.</p>

<h3>Self-Knowledge</h3>
<p>Deeper understanding of your own thought patterns, emotional triggers, habitual behaviours, and unconscious motivations. Gaining insight into why you react certain ways, recognising recurring mental patterns, and developing awareness of previously hidden aspects of your psychology. People who prioritise this value are drawn to practices that reveal truth about themselves, even when initially uncomfortable.</p>

<h3>Spiritual Development</h3>
<p>Connection to meaning, purpose, transcendence, and broader existential questions. Experiences of interconnectedness, encounters with the sacred or mysterious, development of compassion and loving-kindness, and exploration of consciousness itself. Those who prioritise this value seek practices that address life's deeper questions and cultivate connection beyond the individual self.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each mindfulness value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Mental Clarity &ndash; Level 5</div>
    <p><a href="https://www.alanwallace.org/about" target="_blank">B. Alan Wallace</a> has practised meditation for over 40 years, including multiple solitary retreats lasting up to five months. He trained for over a decade under the Dalai Lama and other Tibetan teachers. His work centres on <a href="https://www.sbinstitute.com/about" target="_blank">shamatha</a> &ndash; the sustained, deliberate cultivation of attentional stability &ndash; and he appears to maintain exceptionally focused attention well into his seventies.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Emotional Wellbeing &ndash; Level 5</div>
    <p><a href="https://www.richardjdavidson.com/" target="_blank">Matthieu Ricard</a>, a former molecular biologist who became a Tibetan Buddhist monk, has logged over 50,000 hours of meditation practice across four decades. Neuroscientist Richard Davidson's lab at the University of Wisconsin found that Ricard's brain showed <a href="https://www.pnas.org/doi/10.1073/pnas.0407401101" target="_blank">unusually high levels of gamma wave activity</a> associated with positive emotions, leading to widespread coverage describing him as one of the calmest people ever measured in a laboratory setting.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Self-Knowledge &ndash; Level 5</div>
    <p><a href="https://www.tarabrach.com/about/" target="_blank">Tara Brach</a> has maintained a daily meditation practice for over 40 years and holds a PhD in clinical psychology. She combines deep contemplative experience with psychological expertise, and her teaching focuses specifically on recognising and understanding one's own patterns of emotional reactivity, self-judgment, and habitual avoidance.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Spiritual Development &ndash; Level 5</div>
    <p><a href="https://jackkornfield.com/teachers-biography/" target="_blank">Jack Kornfield</a> trained as a Buddhist monk in Thailand, Burma, and India for several years before returning to the West, where he has practised and taught meditation for over five decades. He co-founded two major retreat centres and his teaching integrates intensive contemplative practice with psychological insight, emphasising compassion, interconnectedness, and the direct investigation of consciousness.</p>
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

<div class="assess-group">
<h4>Mental Clarity</h4>

<div class="assess-input-group" id="ig-focus-duration">
    <span class="assess-label">How long can you sustain focused attention on a single task before your mind wanders?</span>
    <span class="assess-hint">Think about reading, working, or having a conversation.</span>
    <select id="a-focus-duration" onchange="handleAssessInput('a-focus-duration')">
        <option value="">Select&hellip;</option>
        <option value="seconds">Seconds &ndash; my mind wanders almost immediately</option>
        <option value="1-5-min">1 &ndash; 5 minutes</option>
        <option value="5-15-min">5 &ndash; 15 minutes</option>
        <option value="15-30-min">15 &ndash; 30 minutes</option>
        <option value="30-plus">30 minutes or more</option>
    </select> <span class="assess-percentile-hint" id="pct-focus-duration"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-focus-duration" onchange="handleSkip('a-focus-duration')"><label for="skip-focus-duration">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-mental-fog">
    <span class="assess-label">When during the day does your thinking feel clearest?</span>
    <span class="assess-hint">Morning, afternoon, evening &ndash; when are you sharpest?</span>
    <select id="a-mental-fog" onchange="handleAssessInput('a-mental-fog')">
        <option value="">Select&hellip;</option>
        <option value="morning">Morning &ndash; I'm sharpest early in the day</option>
        <option value="midday">Midday &ndash; I peak around lunchtime</option>
        <option value="afternoon">Afternoon &ndash; I warm up as the day goes on</option>
        <option value="evening">Evening &ndash; I'm at my best late in the day</option>
        <option value="no-pattern">No clear pattern &ndash; it varies or I haven't noticed</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-mental-fog" onchange="handleSkip('a-mental-fog')"><label for="skip-mental-fog">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-distraction">
    <span class="assess-label">How often do you involuntarily check your phone or switch tasks during focused work?</span>
    <span class="assess-hint">Notifications, social media, internal restlessness, boredom &ndash; what pulls your attention away?</span>
    <select id="a-distraction" onchange="handleAssessInput('a-distraction')">
        <option value="">Select&hellip;</option>
        <option value="constantly">Constantly &ndash; every few minutes</option>
        <option value="frequently">Frequently &ndash; several times an hour</option>
        <option value="sometimes">Sometimes &ndash; a few times a session</option>
        <option value="rarely">Rarely &ndash; I can usually resist the urge</option>
        <option value="almost-never">Almost never &ndash; I stay focused easily</option>
    </select> <span class="assess-percentile-hint" id="pct-distraction"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-distraction" onchange="handleSkip('a-distraction')"><label for="skip-distraction">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Emotional Wellbeing</h4>

<div class="assess-input-group" id="ig-stress-response">
    <span class="assess-label">How well can you recognise the early physical signs of stress in your body?</span>
    <span class="assess-hint">Tight shoulders, shallow breathing, clenched jaw, racing heart &ndash; what are your signals?</span>
    <select id="a-stress-response" onchange="handleAssessInput('a-stress-response')">
        <option value="">Select&hellip;</option>
        <option value="no-awareness">I don't notice physical stress signals</option>
        <option value="after-fact">I notice only after the stress has built up</option>
        <option value="sometimes">I sometimes catch the early signs</option>
        <option value="usually">I usually notice early and can name the specific sensations</option>
    </select> <span class="assess-percentile-hint" id="pct-stress-response"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-stress-response" onchange="handleSkip('a-stress-response')"><label for="skip-stress-response">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-recovery-time">
    <span class="assess-label">How long does it typically take you to recover emotionally after something upsets you?</span>
    <span class="assess-hint">Do you bounce back quickly or does frustration linger?</span>
    <select id="a-recovery-time" onchange="handleAssessInput('a-recovery-time')">
        <option value="">Select&hellip;</option>
        <option value="minutes">Minutes &ndash; I reset quickly</option>
        <option value="hours">Hours &ndash; it takes a chunk of the day</option>
        <option value="a-day">About a day</option>
        <option value="days">Several days or more</option>
        <option value="unsure">I'm not sure &ndash; I haven't paid attention to this</option>
    </select> <span class="assess-percentile-hint" id="pct-recovery-time"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-recovery-time" onchange="handleSkip('a-recovery-time')"><label for="skip-recovery-time">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-coping">
    <span class="assess-label">What is your go-to coping mechanism when you feel overwhelmed?</span>
    <span class="assess-hint">Exercise, talking to someone, distraction, avoidance, substances, sleep &ndash; what do you actually do?</span>
    <select id="a-coping" onchange="handleAssessInput('a-coping')">
        <option value="">Select&hellip;</option>
        <option value="avoidance">Avoidance or distraction (scrolling, TV, etc.)</option>
        <option value="substances">Substances (alcohol, food, caffeine)</option>
        <option value="social">Talking to someone or seeking support</option>
        <option value="physical">Physical activity (exercise, walking)</option>
        <option value="contemplative">Contemplative practice (meditation, journalling, breathing)</option>
        <option value="sleep">Sleep or rest</option>
        <option value="no-strategy">I don't have a go-to strategy</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-coping" onchange="handleSkip('a-coping')"><label for="skip-coping">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Self-Knowledge</h4>

<div class="assess-input-group" id="ig-thought-patterns">
    <span class="assess-label">Can you identify a recurring thought pattern or mental habit you fall into regularly?</span>
    <span class="assess-hint">Rumination, worst-case thinking, self-criticism, comparison, planning &ndash; what theme keeps returning?</span>
    <select id="a-thought-patterns" onchange="handleAssessInput('a-thought-patterns')">
        <option value="">Select&hellip;</option>
        <option value="no">No &ndash; I haven't noticed any recurring patterns</option>
        <option value="vague">Vaguely &ndash; I sense a pattern but can't articulate it</option>
        <option value="one">Yes &ndash; I can name one clear pattern</option>
        <option value="several">Yes &ndash; I'm aware of several and how they show up</option>
    </select> <span class="assess-percentile-hint" id="pct-thought-patterns"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-thought-patterns" onchange="handleSkip('a-thought-patterns')"><label for="skip-thought-patterns">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-triggers">
    <span class="assess-label">How well do you know what situations or interactions trigger strong emotional reactions in you?</span>
    <span class="assess-hint">Criticism, feeling ignored, time pressure, conflict &ndash; what sets you off?</span>
    <select id="a-triggers" onchange="handleAssessInput('a-triggers')">
        <option value="">Select&hellip;</option>
        <option value="no-idea">No idea &ndash; strong reactions seem to come out of nowhere</option>
        <option value="some-sense">Some sense &ndash; I can name one or two triggers</option>
        <option value="good-map">Good map &ndash; I know most of my triggers and the emotions they produce</option>
        <option value="detailed">Detailed &ndash; I understand the triggers, the emotions, and the patterns behind them</option>
    </select> <span class="assess-percentile-hint" id="pct-triggers"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-triggers" onchange="handleSkip('a-triggers')"><label for="skip-triggers">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-autopilot">
    <span class="assess-label">How much of your day do you spend on autopilot versus consciously choosing your actions?</span>
    <span class="assess-hint">Scrolling, snacking, commuting, routine tasks &ndash; how often are you fully present?</span>
    <select id="a-autopilot" onchange="handleAssessInput('a-autopilot')">
        <option value="">Select&hellip;</option>
        <option value="mostly-autopilot">Mostly autopilot &ndash; I rarely notice what I'm doing</option>
        <option value="more-auto">More autopilot than not &ndash; occasional moments of awareness</option>
        <option value="mixed">Mixed &ndash; roughly half and half</option>
        <option value="mostly-present">Mostly present &ndash; I'm usually aware of my choices</option>
        <option value="highly-present">Highly present &ndash; I'm consciously engaged most of the time</option>
    </select> <span class="assess-percentile-hint" id="pct-autopilot"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-autopilot" onchange="handleSkip('a-autopilot')"><label for="skip-autopilot">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Spiritual Development</h4>

<div class="assess-input-group" id="ig-meaning">
    <span class="assess-label">How clearly have you identified what gives your life meaning or purpose beyond daily tasks?</span>
    <span class="assess-hint">Relationships, creative work, service, nature, learning &ndash; what makes it feel worthwhile?</span>
    <select id="a-meaning" onchange="handleAssessInput('a-meaning')">
        <option value="">Select&hellip;</option>
        <option value="not-thought">I haven't really thought about this</option>
        <option value="vague">I have a vague sense but nothing I could articulate</option>
        <option value="partial">I can name one or two sources of meaning</option>
        <option value="clear">I have a clear, considered sense of what gives my life purpose</option>
    </select> <span class="assess-percentile-hint" id="pct-meaning"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-meaning" onchange="handleSkip('a-meaning')"><label for="skip-meaning">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-awe">
    <span class="assess-label">When did you last experience a moment of awe, wonder, or deep stillness?</span>
    <span class="assess-hint">In nature, during music, in meditation, watching a sunset &ndash; when did you last feel genuinely moved?</span>
    <select id="a-awe" onchange="handleAssessInput('a-awe')">
        <option value="">Select&hellip;</option>
        <option value="cant-recall">I can't recall one</option>
        <option value="months-ago">Months ago</option>
        <option value="past-few-weeks">Within the past few weeks</option>
        <option value="past-week">Within the past week</option>
        <option value="today">Today or yesterday</option>
    </select> <span class="assess-percentile-hint" id="pct-awe"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-awe" onchange="handleSkip('a-awe')"><label for="skip-awe">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-contemplative">
    <span class="assess-label">Do you currently have any contemplative or reflective practice?</span>
    <span class="assess-hint">Meditation, prayer, journalling, walking in nature, sitting quietly &ndash; or none at all.</span>
    <select id="a-contemplative" onchange="handleAssessInput('a-contemplative')">
        <option value="">Select&hellip;</option>
        <option value="none">None at all</option>
        <option value="informal">Informal &ndash; occasional walks, quiet time, but nothing deliberate</option>
        <option value="sporadic">Sporadic &ndash; I do something deliberate but inconsistently</option>
        <option value="regular">Regular &ndash; a few times a week</option>
        <option value="daily">Daily or near-daily practice</option>
    </select> <span class="assess-percentile-hint" id="pct-contemplative"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-contemplative" onchange="handleSkip('a-contemplative')"><label for="skip-contemplative">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-clarity">
        <span class="assess-summary-label">Mental Clarity</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-clarity" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-clarity">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-emotional">
        <span class="assess-summary-label">Emotional Wellbeing</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-emotional" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-emotional">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-knowledge">
        <span class="assess-summary-label">Self-Knowledge</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-knowledge" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-knowledge">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-spiritual">
        <span class="assess-summary-label">Spiritual Development</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-spiritual" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-spiritual">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on mindfulness practice and self-awareness among adults. Items without a clear ordinal scale are left unscored.</p>
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

<p>You now understand why mindfulness matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about mental clarity, emotional wellbeing, self-knowledge, and spiritual development. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/mindfulness/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Mindfulness Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Mindfulness. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/mindfulness/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'mindfulness';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-focus-duration', 'a-mental-fog', 'a-distraction',
        'a-stress-response', 'a-recovery-time', 'a-coping',
        'a-thought-patterns', 'a-triggers', 'a-autopilot',
        'a-meaning', 'a-awe', 'a-contemplative'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: ~14% of US adults have ever meditated (NHIS 2017),
    // ~5% practise daily, sustained focus >15 min is uncommon in general population.
    var THRESHOLDS = {
        'a-focus-duration': [
            // Most adults report difficulty sustaining attention beyond a few minutes
            {v:'seconds',p:8},{v:'1-5-min',p:25},{v:'5-15-min',p:50},{v:'15-30-min',p:75},{v:'30-plus',p:92}
        ],
        'a-distraction': [
            // ~70% of adults report frequent phone-checking during focused work
            {v:'constantly',p:10},{v:'frequently',p:30},{v:'sometimes',p:55},{v:'rarely',p:78},{v:'almost-never',p:95}
        ],
        'a-stress-response': [
            // Most people notice stress only after it has built up
            {v:'no-awareness',p:10},{v:'after-fact',p:35},{v:'sometimes',p:60},{v:'usually',p:90}
        ],
        'a-recovery-time': [
            // Quick emotional recovery is associated with high mindfulness; "unsure" indicates low awareness
            {v:'unsure',p:8},{v:'days',p:18},{v:'a-day',p:38},{v:'hours',p:62},{v:'minutes',p:88}
        ],
        'a-thought-patterns': [
            // Most people have limited metacognitive awareness of recurring patterns
            {v:'no',p:12},{v:'vague',p:35},{v:'one',p:60},{v:'several',p:90}
        ],
        'a-triggers': [
            // Few people have a detailed map of their emotional triggers
            {v:'no-idea',p:10},{v:'some-sense',p:35},{v:'good-map',p:65},{v:'detailed',p:92}
        ],
        'a-autopilot': [
            // Most people spend the majority of their day on autopilot (Killingsworth & Gilbert, 2010: ~47% mind-wandering)
            {v:'mostly-autopilot',p:10},{v:'more-auto',p:30},{v:'mixed',p:55},{v:'mostly-present',p:78},{v:'highly-present',p:95}
        ],
        'a-meaning': [
            // ~25% of adults report a clear sense of purpose; many have not considered this
            {v:'not-thought',p:10},{v:'vague',p:30},{v:'partial',p:58},{v:'clear',p:88}
        ],
        'a-awe': [
            // Regular experiences of awe are uncommon; daily occurrence is rare
            {v:'cant-recall',p:10},{v:'months-ago',p:30},{v:'past-few-weeks',p:55},{v:'past-week',p:75},{v:'today',p:92}
        ],
        'a-contemplative': [
            // ~14% have ever meditated; ~5% practise daily (NHIS 2017)
            {v:'none',p:15},{v:'informal',p:35},{v:'sporadic',p:55},{v:'regular',p:78},{v:'daily',p:95}
        ]
    };

    var VALUE_ITEMS = {
        clarity: ['a-focus-duration', 'a-distraction'],
        emotional: ['a-stress-response', 'a-recovery-time'],
        knowledge: ['a-thought-patterns', 'a-triggers', 'a-autopilot'],
        spiritual: ['a-meaning', 'a-awe', 'a-contemplative']
    };

    // Items without a clear ordinal scale (categorical choices)
    var UNSCORED_ITEMS = ['a-mental-fog', 'a-coping'];

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
        hintEl.textContent = pct !== null ? '~' + pct + 'th percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['clarity', 'emotional', 'knowledge', 'spiritual'].forEach(function(vk) {
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
        ['clarity', 'emotional', 'knowledge', 'spiritual'].forEach(function(vk) {
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
