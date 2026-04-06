---
layout: default
title: "Behaviours – Level 1: Awareness"
life_area_slug: behaviours
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

<h1>Behaviours: Level 1</h1>

<p class="l1-subtitle">Understand what behavioural change means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Behaviours Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why behaviours matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Automatic behavioural patterns – addictions, compulsions, emotional reactions, avoidance – often run in the background of daily life, shaping decisions without conscious input. Most people have at least a few patterns that work against their stated goals, yet only about <a href="https://www.addictionhelp.com/recovery/statistics/" target="_blank">24% of those who would benefit</a> from addressing them actually do so.</p>

<p>The costs of unchecked patterns tend to compound. Reactive behaviours can erode relationships, undermine career progress, and worsen mental health over time. <a href="https://www.who.int/news-room/fact-sheets/detail/mental-disorders" target="_blank">WHO data</a> suggests that 1 in 8 people globally live with an anxiety or depressive disorder, and emotional dysregulation is a contributing factor in both conditions.</p>

<p>On the other side, people who develop the capacity to choose their responses – rather than defaulting to compulsive ones – generally report greater life satisfaction, stronger relationships, and more resilience during difficult periods. The evidence from <a href="https://substanceabusepolicy.biomedcentral.com/articles/10.1186/1747-597X-6-17" target="_blank">relapse prevention research</a> indicates that behavioural awareness is a necessary foundation for lasting change, even if awareness alone is not sufficient.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about behavioural change</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue behavioural change for different reasons. This site scores every behaviours intervention across four core values. Later, you'll set your own weighting across these values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Freedom & Control</h3>
<p>Liberation from compulsive patterns and automatic responses that limit your choices. Breaking free from addictions, managing impulses, and developing the ability to pause between trigger and response. People who lean towards this value focus on restoring genuine choice in their actions, even when it requires significant upfront effort or temporary discomfort.</p>

<h3>Emotional Regulation</h3>
<p>Developing healthier responses to emotional triggers like stress, anxiety, anger, or boredom. Moving from reactive emotional patterns to more measured, intentional responses. Those who lean towards this value focus on building emotional skills and alternative coping strategies, accepting that feeling emotions fully may be temporarily more difficult than numbing them.</p>

<h3>Social & Relational Patterns</h3>
<p>Changing automatic interpersonal behaviours like people-pleasing, conflict avoidance, codependency, social withdrawal, or defensive reactions. People who lean towards this value work on assertiveness, boundary-setting, and staying present during difficult social situations.</p>

<h3>Resilience & Adaptability</h3>
<p>Building sustainable behavioural change that survives life disruptions and does not require constant vigilance. Developing multiple coping strategies, planning for setbacks, and creating robust systems. Those who lean towards this value are willing to progress more slowly to ensure changes last through major life transitions or crises.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each behaviours value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Freedom & Control &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Anthony_Hopkins" target="_blank">Anthony Hopkins</a> stopped drinking on 29 December 1975 after what he has described as years of destructive alcoholism. He has maintained sobriety for over 50 years while working continuously in one of the most high-pressure industries in the world. He credits daily discipline and a complete change in daily habits for his sustained recovery, and by all accounts has not relapsed despite decades of public life and professional stress.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Emotional Regulation &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Marsha_M._Linehan" target="_blank">Marsha Linehan</a> developed Dialectical Behaviour Therapy after her own experience of severe emotional dysregulation and psychiatric hospitalisation as a young woman. She publicly disclosed in 2011 that she had been a patient at the Institute of Living, where she was diagnosed with schizophrenia and subjected to electroshock treatment. She went on to build a daily practice of the emotional regulation skills she later formalised into DBT, and has maintained that practice for over 40 years.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Social & Relational Patterns &ndash; Level 5</div>
    <p><a href="https://www.gottman.com/about/john-julie-gottman/" target="_blank">John Gottman</a> has spent over 40 years researching couple interactions and can predict relationship outcomes with roughly 90% accuracy based on behavioural patterns. Beyond his research, he practises what he studies – maintaining a long-term partnership while navigating the pressures of public intellectual life. His work on repairing conflict patterns and maintaining authentic connection under pressure reflects mastery-level relational skill.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Resilience & Adaptability &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Nelson_Mandela" target="_blank">Nelson Mandela</a> spent 27 years in prison, including 18 on Robben Island, and emerged without evident bitterness towards his captors. He maintained daily exercise routines, studied by correspondence, and cultivated relationships with guards throughout his imprisonment. After his release in 1990 he led South Africa's transition away from apartheid through negotiation, demonstrating a capacity to adapt his behaviour to radically different circumstances while sustaining purpose across decades.</p>
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
<h4>Freedom &amp; Control</h4>

<div class="assess-input-group" id="ig-compulsive-patterns">
    <span class="assess-label">How many specific behaviours can you name where you act compulsively or automatically against your better judgement?</span>
    <span class="assess-hint">Substances, screens, food, spending, procrastination, or anything else you do despite wanting to stop.</span>
    <select id="a-compulsive-patterns" onchange="handleAssessInput('a-compulsive-patterns')">
        <option value="">Select&hellip;</option>
        <option value="0">None &ndash; I don't have compulsive patterns</option>
        <option value="1">One &ndash; I can name one specific behaviour</option>
        <option value="2-3">Two or three</option>
        <option value="4+">Four or more</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-compulsive-patterns" onchange="handleSkip('a-compulsive-patterns')"><label for="skip-compulsive-patterns">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-triggers">
    <span class="assess-label">How well do you know the triggers that lead to your most problematic automatic behaviours?</span>
    <span class="assess-hint">Common triggers include boredom, stress, loneliness, fatigue, specific times of day, or particular social situations.</span>
    <select id="a-triggers" onchange="handleAssessInput('a-triggers')">
        <option value="">Select&hellip;</option>
        <option value="no-idea">No idea &ndash; the behaviours seem to happen randomly</option>
        <option value="vague">Vague sense &ndash; I know some triggers but not the full picture</option>
        <option value="good-map">Good map &ndash; I can name the main triggers for each behaviour</option>
        <option value="detailed">Detailed &ndash; I know triggers, context, and early warning signs</option>
    </select> <span class="assess-percentile-hint" id="pct-triggers"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-triggers" onchange="handleSkip('a-triggers')"><label for="skip-triggers">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-pause">
    <span class="assess-label">Can you currently pause between a trigger and your response?</span>
    <span class="assess-hint">Some patterns feel like a conscious choice you keep making; others feel like they happen before you notice.</span>
    <select id="a-pause" onchange="handleAssessInput('a-pause')">
        <option value="">Select&hellip;</option>
        <option value="no-pause">No pause &ndash; the behaviour feels genuinely automatic</option>
        <option value="sometimes">Sometimes &ndash; I can occasionally catch myself</option>
        <option value="usually">Usually &ndash; I notice the urge but sometimes act on it anyway</option>
        <option value="reliable">Reliably &ndash; I can pause and choose a different response</option>
    </select> <span class="assess-percentile-hint" id="pct-pause"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-pause" onchange="handleSkip('a-pause')"><label for="skip-pause">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Emotional Regulation</h4>

<div class="assess-input-group" id="ig-emotional-triggers">
    <span class="assess-label">Which emotions most often lead you to engage in problematic behaviours?</span>
    <span class="assess-hint">Stress, anxiety, anger, boredom, sadness, loneliness &ndash; different people have different emotional triggers.</span>
    <select id="a-emotional-triggers" onchange="handleAssessInput('a-emotional-triggers')">
        <option value="">Select&hellip;</option>
        <option value="stress-anxiety">Stress or anxiety</option>
        <option value="boredom">Boredom or restlessness</option>
        <option value="sadness-loneliness">Sadness or loneliness</option>
        <option value="anger-frustration">Anger or frustration</option>
        <option value="multiple">Multiple emotions &ndash; several of the above</option>
        <option value="unsure">I'm not sure which emotions drive my behaviours</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-emotional-triggers" onchange="handleSkip('a-emotional-triggers')"><label for="skip-emotional-triggers">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-coping">
    <span class="assess-label">Do your current coping strategies help or make things worse when you experience difficult emotions?</span>
    <span class="assess-hint">Coping might include exercise, talking to someone, distraction, avoidance, substance use, or rumination.</span>
    <select id="a-coping" onchange="handleAssessInput('a-coping')">
        <option value="">Select&hellip;</option>
        <option value="mostly-worse">Mostly worse &ndash; my coping strategies create new problems</option>
        <option value="mixed">Mixed &ndash; some help, some make things worse</option>
        <option value="mostly-help">Mostly help &ndash; my strategies generally work</option>
        <option value="no-strategies">I don't have deliberate coping strategies</option>
    </select> <span class="assess-percentile-hint" id="pct-coping"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-coping" onchange="handleSkip('a-coping')"><label for="skip-coping">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-emotional-frequency">
    <span class="assess-label">How often does stress or emotional discomfort lead you to act in ways you later regret?</span>
    <span class="assess-hint">Think about the past month as a typical period.</span>
    <select id="a-emotional-frequency" onchange="handleAssessInput('a-emotional-frequency')">
        <option value="">Select&hellip;</option>
        <option value="daily">Daily or almost daily</option>
        <option value="several-weekly">Several times a week</option>
        <option value="weekly">About once a week</option>
        <option value="occasionally">Occasionally &ndash; a few times a month</option>
        <option value="rarely">Rarely or never</option>
    </select> <span class="assess-percentile-hint" id="pct-emotional-frequency"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-emotional-frequency" onchange="handleSkip('a-emotional-frequency')"><label for="skip-emotional-frequency">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Social &amp; Relational Patterns</h4>

<div class="assess-input-group" id="ig-interpersonal-defaults">
    <span class="assess-label">What is your default response during interpersonal conflict or social pressure?</span>
    <span class="assess-hint">Think about the last two or three disagreements or uncomfortable social situations you experienced.</span>
    <select id="a-interpersonal-defaults" onchange="handleAssessInput('a-interpersonal-defaults')">
        <option value="">Select&hellip;</option>
        <option value="people-pleasing">People-pleasing &ndash; I agree to keep the peace</option>
        <option value="withdrawal">Withdrawal &ndash; I disengage or go quiet</option>
        <option value="defensiveness">Defensiveness &ndash; I push back or justify myself</option>
        <option value="aggression">Aggression &ndash; I escalate or become confrontational</option>
        <option value="shutdown">Shutdown &ndash; I freeze or go numb emotionally</option>
        <option value="assertive">Assertive &ndash; I express my position calmly</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-interpersonal-defaults" onchange="handleSkip('a-interpersonal-defaults')"><label for="skip-interpersonal-defaults">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-boundaries">
    <span class="assess-label">How easy or difficult do you find it to express your needs and set boundaries in close relationships?</span>
    <span class="assess-hint">Think about your most important relationships &ndash; partner, family, close friends, work colleagues.</span>
    <select id="a-boundaries" onchange="handleAssessInput('a-boundaries')">
        <option value="">Select&hellip;</option>
        <option value="very-difficult">Very difficult &ndash; I almost never set boundaries</option>
        <option value="difficult">Difficult &ndash; I can sometimes but it causes me significant anxiety</option>
        <option value="depends">Depends on the relationship &ndash; easy with some, hard with others</option>
        <option value="mostly-easy">Mostly easy &ndash; I can usually express my needs clearly</option>
        <option value="comfortable">Comfortable &ndash; boundary-setting is a natural part of my relationships</option>
    </select> <span class="assess-percentile-hint" id="pct-boundaries"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-boundaries" onchange="handleSkip('a-boundaries')"><label for="skip-boundaries">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-social-avoidance">
    <span class="assess-label">Do you avoid certain social situations because of anxiety, past experiences, or fear of conflict?</span>
    <span class="assess-hint">Avoidance can be obvious (declining invitations) or subtle (staying quiet, changing the subject, leaving early).</span>
    <select id="a-social-avoidance" onchange="handleAssessInput('a-social-avoidance')">
        <option value="">Select&hellip;</option>
        <option value="frequently">Frequently &ndash; I regularly avoid social situations</option>
        <option value="sometimes">Sometimes &ndash; specific situations trigger avoidance</option>
        <option value="subtly">Subtly &ndash; I attend but disengage (go quiet, leave early)</option>
        <option value="rarely">Rarely &ndash; I generally face social situations even when uncomfortable</option>
        <option value="never">Never &ndash; social situations don't cause me avoidance</option>
    </select> <span class="assess-percentile-hint" id="pct-social-avoidance"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-social-avoidance" onchange="handleSkip('a-social-avoidance')"><label for="skip-social-avoidance">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Resilience &amp; Adaptability</h4>

<div class="assess-input-group" id="ig-past-attempts">
    <span class="assess-label">How successful have your past attempts to change a behaviour been?</span>
    <span class="assess-hint">New Year's resolutions, attempts to quit something, efforts to be more assertive &ndash; what happened?</span>
    <select id="a-past-attempts" onchange="handleAssessInput('a-past-attempts')">
        <option value="">Select&hellip;</option>
        <option value="never-tried">I haven't tried to change a behaviour</option>
        <option value="always-failed">Always failed &ndash; nothing has stuck</option>
        <option value="mixed">Mixed &ndash; some changes stuck, others didn't</option>
        <option value="mostly-succeeded">Mostly succeeded &ndash; I can change when I commit</option>
    </select> <span class="assess-percentile-hint" id="pct-past-attempts"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-past-attempts" onchange="handleSkip('a-past-attempts')"><label for="skip-past-attempts">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-disruption">
    <span class="assess-label">How many of your positive behaviours tend to collapse during stressful periods or life changes?</span>
    <span class="assess-hint">Exercise routines, sleep schedules, dietary habits, social commitments &ndash; which ones survive disruption?</span>
    <select id="a-disruption" onchange="handleAssessInput('a-disruption')">
        <option value="">Select&hellip;</option>
        <option value="all">All of them &ndash; everything collapses under stress</option>
        <option value="most">Most &ndash; only one or two survive</option>
        <option value="some">Some &ndash; a mix of resilient and fragile habits</option>
        <option value="few">Few &ndash; most of my routines hold up</option>
        <option value="none">None &ndash; my routines are robust through disruption</option>
    </select> <span class="assess-percentile-hint" id="pct-disruption"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-disruption" onchange="handleSkip('a-disruption')"><label for="skip-disruption">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-backup-strategies">
    <span class="assess-label">How many alternative coping strategies do you have if your main one becomes unavailable?</span>
    <span class="assess-hint">If your main stress-relief method becomes unavailable, do you have a backup, or do you default to something unhelpful?</span>
    <select id="a-backup-strategies" onchange="handleAssessInput('a-backup-strategies')">
        <option value="">Select&hellip;</option>
        <option value="none">None &ndash; I rely on one strategy or default to something unhelpful</option>
        <option value="one">One backup &ndash; but I rarely use it</option>
        <option value="several">Several alternatives &ndash; I can switch between them</option>
        <option value="flexible">Flexible toolkit &ndash; I adapt my approach to the situation</option>
    </select> <span class="assess-percentile-hint" id="pct-backup-strategies"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-backup-strategies" onchange="handleSkip('a-backup-strategies')"><label for="skip-backup-strategies">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-freedom">
        <span class="assess-summary-label">Freedom &amp; Control</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-freedom" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-freedom">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-emotional">
        <span class="assess-summary-label">Emotional Regulation</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-emotional" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-emotional">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-social">
        <span class="assess-summary-label">Social &amp; Relational Patterns</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-social" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-social">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-resilience">
        <span class="assess-summary-label">Resilience &amp; Adaptability</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-resilience" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-resilience">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on behavioural self-regulation among adults. Items without a clear ordinal scale are left unscored.</p>
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

<p>You now understand why behaviours matter, what different people get out of behavioural change, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about freedom and control, emotional regulation, social and relational patterns, and resilience. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/behaviours/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Behaviours Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Behaviours. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/behaviours/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'behaviours';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-compulsive-patterns', 'a-triggers', 'a-pause',
        'a-emotional-triggers', 'a-coping', 'a-emotional-frequency',
        'a-interpersonal-defaults', 'a-boundaries', 'a-social-avoidance',
        'a-past-attempts', 'a-disruption', 'a-backup-strategies'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: ~24% who would benefit from behavioural change actually address it,
    // relapse rates for substance/habit change are 40-60% (NIDA), most people lack structured coping.
    var THRESHOLDS = {
        'a-triggers': [
            // Most people have only a vague sense of their behavioural triggers
            {v:'no-idea',p:10},{v:'vague',p:35},{v:'good-map',p:65},{v:'detailed',p:92}
        ],
        'a-pause': [
            // Reliably pausing between trigger and response requires significant practice
            {v:'no-pause',p:12},{v:'sometimes',p:38},{v:'usually',p:68},{v:'reliable',p:92}
        ],
        'a-coping': [
            // Most people have mixed or counterproductive coping; effective strategies are uncommon
            {v:'mostly-worse',p:10},{v:'no-strategies',p:25},{v:'mixed',p:55},{v:'mostly-help',p:85}
        ],
        'a-emotional-frequency': [
            // Daily regrettable actions are common; rarely or never is uncommon
            {v:'daily',p:8},{v:'several-weekly',p:22},{v:'weekly',p:45},{v:'occasionally',p:70},{v:'rarely',p:92}
        ],
        'a-boundaries': [
            // Most people find boundary-setting difficult; comfortable boundary-setting is uncommon
            {v:'very-difficult',p:8},{v:'difficult',p:25},{v:'depends',p:50},{v:'mostly-easy',p:75},{v:'comfortable',p:92}
        ],
        'a-social-avoidance': [
            // Social avoidance is common; facing situations consistently despite discomfort is uncommon
            {v:'frequently',p:10},{v:'sometimes',p:30},{v:'subtly',p:50},{v:'rarely',p:75},{v:'never',p:92}
        ],
        'a-past-attempts': [
            // Most behaviour change attempts fail; consistent success is uncommon
            {v:'never-tried',p:12},{v:'always-failed',p:25},{v:'mixed',p:55},{v:'mostly-succeeded',p:88}
        ],
        'a-disruption': [
            // Most people's routines collapse under stress; robustness is rare
            {v:'all',p:8},{v:'most',p:25},{v:'some',p:50},{v:'few',p:75},{v:'none',p:95}
        ],
        'a-backup-strategies': [
            // Most people rely on one strategy or default to something unhelpful
            {v:'none',p:12},{v:'one',p:35},{v:'several',p:65},{v:'flexible',p:92}
        ]
    };

    var VALUE_ITEMS = {
        freedom: ['a-triggers', 'a-pause'],
        emotional: ['a-coping', 'a-emotional-frequency'],
        social: ['a-boundaries', 'a-social-avoidance'],
        resilience: ['a-past-attempts', 'a-disruption', 'a-backup-strategies']
    };

    // Items without a clear ordinal scale (categorical choices)
    var UNSCORED_ITEMS = ['a-compulsive-patterns', 'a-emotional-triggers', 'a-interpersonal-defaults'];

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
        ['freedom', 'emotional', 'social', 'resilience'].forEach(function(vk) {
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
        ['freedom', 'emotional', 'social', 'resilience'].forEach(function(vk) {
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
