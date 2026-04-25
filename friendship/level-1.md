---
layout: default
title: "Friendship – Level 1: Awareness"
life_area_slug: friendship
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

<h1>Friendship: Level 1</h1>

<p class="l1-subtitle">Understand what friendship means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Friendship Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why friendship matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Friendship is one of the strongest predictors of wellbeing across the lifespan. A <a href="https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000316" target="_blank">meta-analysis of 148 studies</a> covering over 300,000 people found that those with strong social relationships had a 50% higher likelihood of survival over a given follow-up period. The health risk of weak social ties is comparable to smoking 15 cigarettes a day and exceeds the risks associated with obesity or physical inactivity.</p>

<p>The benefits extend well beyond physical health. A <a href="https://www.pewresearch.org/short-reads/2023/10/12/what-does-friendship-look-like-in-america/" target="_blank">2023 Pew Research survey</a> found that 61% of US adults consider close friendships extremely or very important for a fulfilling life &ndash; a higher proportion than for marriage (23%), having children (26%), or having money (24%). Longitudinal research on cognitive ageing suggests that <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7483134/" target="_blank">frequent contact with friends</a> is associated with slower cognitive decline, and the effect appears to be stronger for friends than for family members.</p>

<p>Despite this, friendship is in decline across much of the developed world. The percentage of American adults reporting no close friends tripled from 3% in 1990 to 12% in 2021, while those with ten or more close friends fell from 33% to 13%. Similar trends have been documented in the UK, Australia, and Japan. This means that even modest investment in friendship puts you ahead of a growing portion of the population.</p>

<p>Friendship also compounds over time. Research on social capital consistently finds that the longest-standing friendships provide the most emotional support, the broadest access to information and opportunities, and the strongest buffer against stress. Starting early and maintaining friendships matters more than having many of them at any one point.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about friendship</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue friendship for different reasons. This site scores every friendship intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Depth</h3>
<p>Close friendships built on high trust, vulnerability, and mutual understanding. People who lean towards this value invest heavily in a smaller number of relationships where they can share honestly, rely on each other during difficult periods, and feel fully known. Depth tends to require regular one-on-one time, emotional availability, and a willingness to have hard conversations.</p>

<h3>Breadth</h3>
<p>A diverse network of friendships spanning different contexts, communities, and walks of life. People who lean towards this value enjoy meeting new people, maintaining ties across settings &ndash; work, hobbies, neighbourhoods, online communities &ndash; and connecting others who might benefit from knowing each other. Breadth brings access to varied perspectives, information, and social opportunities.</p>

<h3>Growth</h3>
<p>Friendships that challenge you to improve, learn, and develop as a person. People who lean towards this value seek out friends who hold them accountable, introduce them to new ideas, give honest feedback, and push them beyond their comfort zone. Growth-oriented friendships often centre on shared projects, intellectual discussion, or mutual goal-setting.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each friendship value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Depth &ndash; Level 5</div>
    <p><a href="https://www.cs-lewis.com/biography/" target="_blank">C.S. Lewis</a> and <a href="https://www.tolkiensociety.org/author/biography/" target="_blank">J.R.R. Tolkien</a> met at Oxford in 1926 and remained close friends for over 30 years through the Inklings, a literary group that met weekly to read and critique each other's work. Tolkien was instrumental in Lewis's conversion to Christianity &ndash; a pivotal moment in Lewis's life. Lewis, in turn, provided years of encouragement that kept Tolkien working on <em>The Lord of the Rings</em> during long periods of doubt. Their friendship weathered significant disagreements, including over Lewis's marriage and theological differences, and both men described it as one of the most important relationships of their lives.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Breadth &ndash; Level 5</div>
    <p><a href="https://keithferrazzi.com/" target="_blank">Keith Ferrazzi</a> built a career around the deliberate practice of relationship-building. His book <em>Never Eat Alone</em> describes his system for maintaining genuine connections with thousands of people across industries and countries. Ferrazzi appears to treat relationship maintenance as a structured discipline &ndash; tracking contacts, reaching out regularly, and actively looking for ways to help people in his network before asking for anything in return. He is widely cited as an example of someone who combines very large social networks with authentic personal investment in each connection.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Growth &ndash; Level 5</div>
    <p><a href="https://www.fi.edu/en/benjamin-franklin" target="_blank">Benjamin Franklin</a> founded the Junto in 1727, a mutual improvement club of 12 friends drawn from different trades in Philadelphia. Members met weekly to discuss questions of morals, politics, and natural philosophy, and held each other accountable to personal development goals. The group ran for over 30 years and generated several lasting civic institutions, including a lending library that became the Library Company of Philadelphia and an academy that eventually became the University of Pennsylvania. Franklin credited the Junto with shaping much of his intellectual development.</p>
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
<h4>Depth</h4>

<div class="assess-input-group" id="ig-close-count">
    <span class="assess-label">How many friends could you call at 2 a.m. with a genuine emergency and be confident they would pick up?</span>
    <span class="assess-hint">Think through your contacts and count the people you would actually ring in a crisis.</span>
    <select id="a-close-count" onchange="handleAssessInput('a-close-count')">
        <option value="">Select&hellip;</option>
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2-3">2 &ndash; 3</option>
        <option value="4-5">4 &ndash; 5</option>
        <option value="6+">6 or more</option>
    </select> <span class="assess-percentile-hint" id="pct-close-count"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-close-count" onchange="handleSkip('a-close-count')"><label for="skip-close-count">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-vulnerability">
    <span class="assess-label">Have you shared something genuinely personal or difficult with a friend in the past month?</span>
    <span class="assess-hint">Something beyond surface-level updates &ndash; a worry, a failure, an uncertainty about the future.</span>
    <select id="a-vulnerability" onchange="handleAssessInput('a-vulnerability')">
        <option value="">Select&hellip;</option>
        <option value="no-never">No &ndash; I rarely or never share personal things with friends</option>
        <option value="no-recent">No &ndash; not in the past month, but I have before</option>
        <option value="once">Yes &ndash; once in the past month</option>
        <option value="several">Yes &ndash; several times in the past month</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-vulnerability" onchange="handleSkip('a-vulnerability')"><label for="skip-vulnerability">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-one-on-one">
    <span class="assess-label">How often do you spend one-on-one time with a close friend in a typical month?</span>
    <span class="assess-hint">In person, on the phone, or on a video call &ndash; but with enough time for real conversation, not just brief messages.</span>
    <select id="a-one-on-one" onchange="handleAssessInput('a-one-on-one')">
        <option value="">Select&hellip;</option>
        <option value="never">Never or almost never</option>
        <option value="once">About once a month</option>
        <option value="2-3">2 &ndash; 3 times a month</option>
        <option value="weekly">About once a week</option>
        <option value="multiple-weekly">Multiple times a week</option>
    </select> <span class="assess-percentile-hint" id="pct-one-on-one"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-one-on-one" onchange="handleSkip('a-one-on-one')"><label for="skip-one-on-one">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Breadth</h4>

<div class="assess-input-group" id="ig-contexts">
    <span class="assess-label">How many distinct contexts do you currently have friends in?</span>
    <span class="assess-hint">Work, hobbies, neighbourhood, university, online, sports, religious community, etc.</span>
    <select id="a-contexts" onchange="handleAssessInput('a-contexts')">
        <option value="">Select&hellip;</option>
        <option value="0-1">0 &ndash; 1 context</option>
        <option value="2">2 contexts</option>
        <option value="3">3 contexts</option>
        <option value="4+">4 or more contexts</option>
    </select> <span class="assess-percentile-hint" id="pct-contexts"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-contexts" onchange="handleSkip('a-contexts')"><label for="skip-contexts">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-new-people">
    <span class="assess-label">When did you last make a new friend you now see or speak to regularly?</span>
    <span class="assess-hint">Think about whether your social circle has grown, shrunk, or stayed the same recently.</span>
    <select id="a-new-people" onchange="handleAssessInput('a-new-people')">
        <option value="">Select&hellip;</option>
        <option value="cant-recall">I can't recall making a new friend recently</option>
        <option value="over-2-years">More than 2 years ago</option>
        <option value="1-2-years">1 &ndash; 2 years ago</option>
        <option value="past-year">Within the past year</option>
        <option value="past-few-months">Within the past few months</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-new-people" onchange="handleSkip('a-new-people')"><label for="skip-new-people">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-diversity">
    <span class="assess-label">How diverse is your friend group in age, background, and interests?</span>
    <span class="assess-hint">Consider age range, professions, cultural backgrounds, and how they spend their time.</span>
    <select id="a-diversity" onchange="handleAssessInput('a-diversity')">
        <option value="">Select&hellip;</option>
        <option value="very-similar">Very similar &ndash; mostly people like me</option>
        <option value="some-variety">Some variety &ndash; a mix in one or two dimensions</option>
        <option value="diverse">Diverse &ndash; genuine variety across age, background, and interests</option>
        <option value="very-diverse">Very diverse &ndash; friends from many different walks of life</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-diversity" onchange="handleSkip('a-diversity')"><label for="skip-diversity">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Growth</h4>

<div class="assess-input-group" id="ig-feedback">
    <span class="assess-label">Have any of your friends given you honest, constructive feedback in the past six months?</span>
    <span class="assess-hint">Feedback on your work, your behaviour, your decisions &ndash; something that helped you see a blind spot.</span>
    <select id="a-feedback" onchange="handleAssessInput('a-feedback')">
        <option value="">Select&hellip;</option>
        <option value="never">Never &ndash; my friends don't give me critical feedback</option>
        <option value="not-recently">Not in the past six months</option>
        <option value="once-or-twice">Once or twice</option>
        <option value="regularly">Regularly &ndash; it's a normal part of our dynamic</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-feedback" onchange="handleSkip('a-feedback')"><label for="skip-feedback">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-learning">
    <span class="assess-label">Can you identify something you have learned or a way you have changed because of a friend's influence?</span>
    <span class="assess-hint">A book they recommended, a habit you picked up, a perspective they shifted.</span>
    <select id="a-learning" onchange="handleAssessInput('a-learning')">
        <option value="">Select&hellip;</option>
        <option value="nothing">Nothing comes to mind</option>
        <option value="vague">Vaguely &ndash; I'm sure they've influenced me but I can't name specifics</option>
        <option value="one">One clear example</option>
        <option value="several">Several examples &ndash; my friends regularly shape my thinking</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-learning" onchange="handleSkip('a-learning')"><label for="skip-learning">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-accountability">
    <span class="assess-label">Do you have a friend who holds you accountable to a goal, standard, or commitment?</span>
    <span class="assess-hint">Someone who checks in on your progress, calls you out when you slack, or shares a goal with you.</span>
    <select id="a-accountability" onchange="handleAssessInput('a-accountability')">
        <option value="">Select&hellip;</option>
        <option value="no">No &ndash; nobody holds me accountable</option>
        <option value="informal">Informally &ndash; a friend sometimes checks in but it's not deliberate</option>
        <option value="yes-one">Yes &ndash; one friend who actively holds me accountable</option>
        <option value="yes-several">Yes &ndash; multiple friends or a structured accountability setup</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-accountability" onchange="handleSkip('a-accountability')"><label for="skip-accountability">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-depth">
        <span class="assess-summary-label">Depth</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-depth" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-depth">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-breadth">
        <span class="assess-summary-label">Breadth</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-breadth" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-breadth">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-growth">
        <span class="assess-summary-label">Growth</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-growth" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-growth">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on friendship behaviour among adults. Items without reliable population benchmarks are not scored.</p>
</div>

<div class="assess-recorded" id="assessRecorded">Your answers have been recorded.</div>

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

<p>You now understand why friendship matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about depth, breadth, and growth. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/friendship/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Friendship Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Friendship. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/friendship/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'friendship';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-close-count', 'a-vulnerability', 'a-one-on-one',
        'a-contexts', 'a-new-people', 'a-diversity',
        'a-feedback', 'a-learning', 'a-accountability'
    ];

    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: 12% of US adults report zero close friends (2021);
    // median close-friend count is 3 – 5; weekly one-on-one contact is uncommon;
    // most adults draw friends from 1 – 2 contexts.
    var THRESHOLDS = {
        'a-close-count': [
            // 12% have zero close friends; 6+ is top decile
            {v:'0',p:8},{v:'1',p:25},{v:'2-3',p:50},{v:'4-5',p:75},{v:'6+',p:92}
        ],
        'a-one-on-one': [
            // Most adults see close friends less than once a month; weekly is uncommon
            {v:'never',p:12},{v:'once',p:35},{v:'2-3',p:58},{v:'weekly',p:80},{v:'multiple-weekly',p:95}
        ],
        'a-contexts': [
            // Most people draw friends from 1 – 2 settings; 4+ is rare
            {v:'0-1',p:15},{v:'2',p:40},{v:'3',p:65},{v:'4+',p:88}
        ]
    };

    var VALUE_ITEMS = {
        depth: ['a-close-count', 'a-one-on-one'],
        breadth: ['a-contexts'],
        growth: []
    };

    // Items without reliable population benchmarks
    var UNSCORED_ITEMS = [
        'a-vulnerability', 'a-new-people', 'a-diversity',
        'a-feedback', 'a-learning', 'a-accountability'
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
        if (!THRESHOLDS[itemId]) return null;
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
        if (!items || items.length === 0) return null;
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
        ['depth', 'breadth', 'growth'].forEach(function(vk) {
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
        ['depth', 'breadth', 'growth'].forEach(function(vk) {
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
