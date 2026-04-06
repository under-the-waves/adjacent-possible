---
layout: default
title: "Habits – Level 1: Awareness"
life_area_slug: habits
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

<h1>Habits: Level 1</h1>

<p class="l1-subtitle">Understand what habit formation means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Habits Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why habits matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>About <a href="https://dornsife.usc.edu/assets/sites/545/docs/Wendy_Wood_Research_Articles/Habits/wood.quinn.kashy.2002_habits_in_everyday_life.pdf" target="_blank">40% of your daily actions</a> are performed habitually &ndash; not through conscious decision but through automatic routines triggered by context. Understanding and shaping these routines is one of the highest-leverage investments you can make in your life.</p>

<p>Once a habit is established, it persists even after conscious motivation fades. This is both the power and the danger of habits: good ones compound silently in the background, while bad ones drain your health, time, and relationships without requiring any deliberate choice on your part.</p>

<p>Research shows that habit formation takes <a href="https://onlinelibrary.wiley.com/doi/abs/10.1002/ejsp.674" target="_blank">18 to 254 days</a>, with an average of 66 days &ndash; far longer than the popular "21 days" myth suggests. Yet <a href="https://www.weforum.org/stories/2024/04/healthy-habit-formation-public-health/" target="_blank">77% of people</a> abandon new behaviours within a single week. The gap between wanting to change and actually embedding new habits is where most people get stuck.</p>

<p>Well-designed habits free mental resources for higher-level thinking. Every behaviour that becomes automatic is one fewer decision you need to make, reducing decision fatigue and creating capacity for the things that require your full attention.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about habits</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach habit formation for different reasons. This site scores every habits intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Impact</h3>
<p>Choosing and designing habits that create meaningful positive change in important life areas. Focusing on keystone habits that trigger other positive behaviours, aligning habits with personal values and goals, and ensuring habit choices deliver measurable benefits. People who lean towards this value want their habit energy invested in behaviours that create the greatest life improvement.</p>

<h3>Consistency</h3>
<p>Building habits that stick and perform reliably over time without constant conscious effort. Establishing routines that become automatic, maintaining behaviours even during difficult periods, and creating systems that work regardless of motivation levels. People who lean towards this value focus on habit durability and want behaviours that persist through life's ups and downs.</p>

<h3>Enjoyment</h3>
<p>Making habit formation and maintenance as pleasant and rewarding as possible. Choosing habits that feel intrinsically satisfying, designing routines that enhance daily experience, and creating positive associations with beneficial behaviours. People who lean towards this value seek habits that improve both outcomes and quality of life.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each habits value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Impact &ndash; Level 5</div>
    <p><a href="https://jamesclear.com/about" target="_blank">James Clear</a> spent years studying and practising habit formation before writing <em>Atomic Habits</em>, which has sold over 15 million copies. His personal system centres on identifying and stacking keystone habits &ndash; small behaviours that cascade into larger life improvements. He has maintained a consistent writing, fitness, and photography practice for over a decade, each habit deliberately chosen for its compound returns across multiple life areas.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Consistency &ndash; Level 5</div>
    <p><a href="https://www.jerryeinfeld.com/" target="_blank">Jerry Seinfeld</a> famously maintained a "don't break the chain" practice for joke-writing, marking a red X on a wall calendar every day he wrote new material. He sustained this daily writing habit across decades, through career changes, touring schedules, and life transitions. His consistency methodology has become one of the most widely cited examples of habit maintenance in popular psychology.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Enjoyment &ndash; Level 5</div>
    <p><a href="https://www.bfrb.org/storage/documents/Expert_consensus_guidelines2016w.pdf" target="_blank">BJ Fogg</a>, founder of the <a href="https://behaviordesign.stanford.edu/" target="_blank">Behavior Design Lab</a> at Stanford, developed the Tiny Habits method after two decades of research into what makes behaviours stick. His system emphasises celebration and positive emotion as the core mechanism of habit formation &ndash; deliberately engineering feelings of success and satisfaction after each repetition. He has personally maintained dozens of "tiny habits" for years, each designed to feel rewarding from the first day.</p>
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
<h4>Impact</h4>

<div class="assess-input-group" id="ig-current-habits">
    <span class="assess-label">How many daily or weekly habits do you currently maintain?</span>
    <span class="assess-hint">Think about your morning routine, work patterns, evening habits, and weekend routines &ndash; both helpful and unhelpful.</span>
    <select id="a-current-habits" onchange="handleAssessInput('a-current-habits')">
        <option value="">Select...</option>
        <option value="dont-know">I don't know &ndash; I haven't thought about it</option>
        <option value="few">A few &ndash; one or two I could name</option>
        <option value="several">Several &ndash; 3 &ndash; 5 deliberate habits</option>
        <option value="many">Many &ndash; 6 &ndash; 10 habits across different areas</option>
        <option value="comprehensive">Comprehensive &ndash; 10+ habits forming a structured routine</option>
    </select> <span class="assess-percentile-hint" id="pct-current-habits"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-current-habits" onchange="handleSkip('a-current-habits')"><label for="skip-current-habits">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-keystone">
    <span class="assess-label">Have you identified which of your habits have the biggest ripple effects on other areas of your life?</span>
    <span class="assess-hint">For example, does exercising in the morning make you more productive all day? Does staying up late make everything harder?</span>
    <select id="a-keystone" onchange="handleAssessInput('a-keystone')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I haven't thought about which habits affect others</option>
        <option value="vaguely">Vaguely &ndash; I have a general sense but nothing specific</option>
        <option value="some">Some &ndash; I've identified one or two keystone habits</option>
        <option value="mostly">Mostly &ndash; I understand the main connections between my habits</option>
        <option value="clearly">Clearly &ndash; I've mapped how my habits influence each other</option>
    </select> <span class="assess-percentile-hint" id="pct-keystone"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-keystone" onchange="handleSkip('a-keystone')"><label for="skip-keystone">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-habit-goals">
    <span class="assess-label">Are your current habits aligned with your most important goals and values?</span>
    <span class="assess-hint">Are your daily routines actually moving you towards the things you say matter most?</span>
    <select id="a-habit-goals" onchange="handleAssessInput('a-habit-goals')">
        <option value="">Select...</option>
        <option value="misaligned">Misaligned &ndash; my habits work against my goals</option>
        <option value="mostly-unrelated">Mostly unrelated &ndash; my habits and goals don't connect</option>
        <option value="partially">Partially &ndash; some habits support my goals, some don't</option>
        <option value="mostly-aligned">Mostly aligned &ndash; the majority of my habits serve my goals</option>
        <option value="fully-aligned">Fully aligned &ndash; my habits are deliberately designed around my goals</option>
    </select> <span class="assess-percentile-hint" id="pct-habit-goals"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-habit-goals" onchange="handleSkip('a-habit-goals')"><label for="skip-habit-goals">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Consistency</h4>

<div class="assess-input-group" id="ig-formation-time">
    <span class="assess-label">How long does it typically take you to form a new habit?</span>
    <span class="assess-hint">Think about the last habit you successfully built &ndash; how long before it felt automatic?</span>
    <select id="a-formation-time" onchange="handleAssessInput('a-formation-time')">
        <option value="">Select...</option>
        <option value="dont-know">I don't know &ndash; I've rarely succeeded at forming new habits</option>
        <option value="months">Months &ndash; it takes a very long time for anything to stick</option>
        <option value="six-to-eight-weeks">Six to eight weeks &ndash; consistent effort over several weeks</option>
        <option value="three-to-four-weeks">Three to four weeks &ndash; relatively quick once I commit</option>
        <option value="two-weeks-or-less">Two weeks or less &ndash; I pick up new habits quickly</option>
    </select> <span class="assess-percentile-hint" id="pct-formation-time"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-formation-time" onchange="handleSkip('a-formation-time')"><label for="skip-formation-time">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-disruption">
    <span class="assess-label">What tends to disrupt your habits?</span>
    <span class="assess-hint">Identifying your habit-breaking triggers is the first step to building more resilient routines.</span>
    <select id="a-disruption" onchange="handleAssessInput('a-disruption')">
        <option value="">Select...</option>
        <option value="everything">Everything &ndash; any change in routine breaks my habits</option>
        <option value="travel-and-stress">Travel and stress &ndash; big disruptions derail me</option>
        <option value="weekends">Weekends &ndash; I maintain habits on weekdays but lose them at weekends</option>
        <option value="major-only">Major life changes only &ndash; day-to-day variation doesn't bother me</option>
        <option value="almost-nothing">Almost nothing &ndash; my habits persist through most disruptions</option>
    </select> <span class="assess-percentile-hint" id="pct-disruption"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-disruption" onchange="handleSkip('a-disruption')"><label for="skip-disruption">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-bad-habits">
    <span class="assess-label">How well do you understand why your unwanted habits persist?</span>
    <span class="assess-hint">Understanding why unwanted habits stick helps you design better approaches to changing them.</span>
    <select id="a-bad-habits" onchange="handleAssessInput('a-bad-habits')">
        <option value="">Select...</option>
        <option value="no-idea">No idea &ndash; I don't understand why I keep doing things I want to stop</option>
        <option value="vague-sense">Vague sense &ndash; I can guess but haven't thought deeply about it</option>
        <option value="some-understanding">Some understanding &ndash; I know the triggers for some bad habits</option>
        <option value="good-understanding">Good understanding &ndash; I've analysed most of my unwanted habits</option>
        <option value="thorough">Thorough &ndash; I understand the cue-routine-reward loop for each one</option>
    </select> <span class="assess-percentile-hint" id="pct-bad-habits"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-bad-habits" onchange="handleSkip('a-bad-habits')"><label for="skip-bad-habits">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Enjoyment</h4>

<div class="assess-input-group" id="ig-enjoy-habits">
    <span class="assess-label">How many of your current habits do you genuinely enjoy?</span>
    <span class="assess-hint">Habits that feel rewarding are far more likely to persist than those maintained through willpower alone.</span>
    <select id="a-enjoy-habits" onchange="handleAssessInput('a-enjoy-habits')">
        <option value="">Select...</option>
        <option value="none">None &ndash; they all feel like obligations</option>
        <option value="few">A few &ndash; one or two are pleasant</option>
        <option value="about-half">About half &ndash; a mix of enjoyable and effortful</option>
        <option value="most">Most &ndash; the majority feel rewarding</option>
        <option value="all">All &ndash; I've designed my habits to be enjoyable</option>
    </select> <span class="assess-percentile-hint" id="pct-enjoy-habits"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-enjoy-habits" onchange="handleSkip('a-enjoy-habits')"><label for="skip-enjoy-habits">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-cues">
    <span class="assess-label">Do you use deliberate cues or triggers to prompt your habits?</span>
    <span class="assess-hint">Linking a new habit to an existing routine (habit stacking) is one of the most effective formation techniques.</span>
    <select id="a-cues" onchange="handleAssessInput('a-cues')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I rely on memory or motivation</option>
        <option value="occasionally">Occasionally &ndash; for one or two habits</option>
        <option value="some">Some &ndash; a few habits have deliberate triggers</option>
        <option value="most">Most &ndash; the majority of my habits have clear cues</option>
        <option value="all">All &ndash; every habit is linked to a specific cue or routine</option>
    </select> <span class="assess-percentile-hint" id="pct-cues"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-cues" onchange="handleSkip('a-cues')"><label for="skip-cues">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-rewards">
    <span class="assess-label">Do your habits have built-in rewards, or do you rely on discipline to maintain them?</span>
    <span class="assess-hint">Intrinsic rewards (the behaviour itself feels good) are more sustainable than extrinsic ones (doing it to earn something else).</span>
    <select id="a-rewards" onchange="handleAssessInput('a-rewards')">
        <option value="">Select...</option>
        <option value="pure-discipline">Pure discipline &ndash; I force myself through willpower</option>
        <option value="mostly-discipline">Mostly discipline &ndash; a few have natural rewards</option>
        <option value="mixed">Mixed &ndash; about half feel rewarding, half require effort</option>
        <option value="mostly-rewarding">Mostly rewarding &ndash; the majority feel good</option>
        <option value="intrinsically-rewarding">Intrinsically rewarding &ndash; my habits are designed to feel satisfying</option>
    </select> <span class="assess-percentile-hint" id="pct-rewards"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-rewards" onchange="handleSkip('a-rewards')"><label for="skip-rewards">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-impact">
        <span class="assess-summary-label">Impact</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-impact" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-impact">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-consistency">
        <span class="assess-summary-label">Consistency</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-consistency" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-consistency">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-enjoyment">
        <span class="assess-summary-label">Enjoyment</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-enjoyment" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-enjoyment">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on habit formation and maintenance among adults. All items in this area are scored.</p>
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

<p>You now understand why habits matter, what different people get out of habit formation, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about impact, consistency, and enjoyment. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/habits/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Habits Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Habits. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/habits/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'habits';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-current-habits', 'a-keystone', 'a-habit-goals',
        'a-formation-time', 'a-disruption', 'a-bad-habits',
        'a-enjoy-habits', 'a-cues', 'a-rewards'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: 77% abandon new behaviours within a week,
    // most people have no deliberate habit system, few use cue-based design.
    var THRESHOLDS = {
        'a-current-habits': [
            // Most people have not identified deliberate habits; a structured routine of 10+ is very rare
            {v:'dont-know',p:10},{v:'few',p:30},{v:'several',p:55},{v:'many',p:78},{v:'comprehensive',p:95}
        ],
        'a-keystone': [
            // The concept of keystone habits is relatively niche; mapping habit interactions is very rare
            {v:'no',p:15},{v:'vaguely',p:35},{v:'some',p:58},{v:'mostly',p:80},{v:'clearly',p:95}
        ],
        'a-habit-goals': [
            // Most people's habits are not deliberately aligned with goals
            {v:'misaligned',p:5},{v:'mostly-unrelated',p:20},{v:'partially',p:50},{v:'mostly-aligned',p:78},{v:'fully-aligned',p:95}
        ],
        'a-formation-time': [
            // Most people rarely succeed at forming habits; quick formation indicates strong skill
            {v:'dont-know',p:10},{v:'months',p:30},{v:'six-to-eight-weeks',p:55},{v:'three-to-four-weeks',p:78},{v:'two-weeks-or-less',p:93}
        ],
        'a-disruption': [
            // Most people lose habits to routine disruptions; maintaining through most disruptions is rare
            {v:'everything',p:10},{v:'travel-and-stress',p:30},{v:'weekends',p:50},{v:'major-only',p:75},{v:'almost-nothing',p:93}
        ],
        'a-bad-habits': [
            // Most people don't deeply analyse their unwanted habits; understanding cue-routine-reward is rare
            {v:'no-idea',p:10},{v:'vague-sense',p:30},{v:'some-understanding',p:55},{v:'good-understanding',p:78},{v:'thorough',p:95}
        ],
        'a-enjoy-habits': [
            // Most people maintain habits through obligation; designing for enjoyment is uncommon
            {v:'none',p:10},{v:'few',p:30},{v:'about-half',p:55},{v:'most',p:78},{v:'all',p:95}
        ],
        'a-cues': [
            // Most people rely on motivation/memory; deliberate cue design for all habits is very rare
            {v:'no',p:15},{v:'occasionally',p:35},{v:'some',p:55},{v:'most',p:78},{v:'all',p:95}
        ],
        'a-rewards': [
            // Most people rely on discipline; designing intrinsically rewarding habits is rare
            {v:'pure-discipline',p:10},{v:'mostly-discipline',p:30},{v:'mixed',p:55},{v:'mostly-rewarding',p:78},{v:'intrinsically-rewarding',p:95}
        ]
    };

    var VALUE_ITEMS = {
        impact: ['a-current-habits', 'a-keystone', 'a-habit-goals'],
        consistency: ['a-formation-time', 'a-disruption', 'a-bad-habits'],
        enjoyment: ['a-enjoy-habits', 'a-cues', 'a-rewards']
    };

    // All habits items are scorable
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
        // All habits items use string keys (dropdowns)
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
        ['impact', 'consistency', 'enjoyment'].forEach(function(vk) {
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
        ['impact', 'consistency', 'enjoyment'].forEach(function(vk) {
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
