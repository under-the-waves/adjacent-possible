---
layout: default
title: "Relationship Quality – Level 1: Awareness"
life_area_slug: romantic-relationships
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

<h1>Relationship Quality: Level 1</h1>

<p class="l1-subtitle">Understand what relationship quality means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Relationship Quality Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why relationship quality matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>The quality of your romantic partnership is one of the strongest predictors of overall life satisfaction. Well over 90% of people marry or enter long-term partnerships at some point, yet <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8186435/" target="_blank">40 &ndash; 50% of marriages end in divorce</a>, and many that survive fall into comfortable mediocrity. Only about 30% of marriages maintain what researchers call "vital" or "total" quality over the long term.</p>

<p>The good news is that relationship satisfaction appears to be shaped more by skills than by selection. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9136471/" target="_blank">Meta-analytic research</a> shows that satisfaction correlates at 0.34 with communication quality, 0.36 with togetherness, and &ndash;0.35 with frequency of disagreements. These are learnable, improvable skills &ndash; not fixed traits.</p>

<p>Parenthood is a particular stress test. For most couples, marital satisfaction remains relatively stable over time, but <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3061469/" target="_blank">by the time the first child reaches 15</a>, parents' satisfaction has declined by nearly one standard deviation. Couples who invest deliberately in their relationship appear to weather this transition considerably better.</p>

<p>Relationship quality also cascades into other domains. People in satisfying partnerships tend to report better physical health, lower rates of depression, stronger friendships, and greater career satisfaction. Few other investments touch as many areas of life simultaneously.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about relationship quality</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue relationship quality for different reasons. This site scores every relationship quality intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Connection</h3>
<p>Emotional closeness, vulnerability, trust, and deep mutual understanding. Sharing your inner life, feeling genuinely known and accepted, and maintaining emotional and physical intimacy through life's changes. People who lean towards this value invest in communication skills, emotional availability, and the courage to be vulnerable.</p>

<h3>Harmony</h3>
<p>Low-conflict, smoothly functioning daily life together. Constructive disagreement, equitable division of responsibilities, aligned approaches to finances and parenting, and the ability to navigate differences without erosion of goodwill. People who lean towards this value focus on making the partnership work well day to day.</p>

<h3>Alignment</h3>
<p>Shared values, compatible life goals, and a common vision for the relationship's future. Agreement on major life decisions, compatible priorities, and the sense that you are building towards the same things. People who lean towards this value ensure long-term compatibility underpins the relationship.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each relationship quality value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Connection &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Esther_Perel" target="_blank">Esther Perel</a> has spent over 35 years studying and practising what sustains emotional and erotic connection in long-term partnerships. Her clinical work, books, and podcast <em>Where Should We Begin?</em> demonstrate an unusually deep understanding of vulnerability, desire, and intimacy. She and her husband have maintained their own partnership across decades while she has helped thousands of couples rebuild emotional closeness after betrayal, stagnation, or loss.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Harmony &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Julie_Schwartz_Gottman" target="_blank">Julie Schwartz Gottman</a> co-founded the Gottman Institute with her husband John, and the two have built one of the most cited bodies of research on what makes marriages succeed or fail. Their own partnership &ndash; running a business, raising a daughter, and maintaining a marriage across four decades &ndash; serves as a working example of the conflict resolution and daily collaboration principles they teach. Julie developed the Gottman Couples Therapy method and has trained thousands of therapists worldwide.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Alignment &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Barack_Obama" target="_blank">Barack and Michelle Obama</a> have described their marriage as built on explicit shared values &ndash; public service, family priority, and intellectual partnership &ndash; negotiated and renegotiated over more than 30 years. They navigated career sacrifices (Michelle leaving her legal career for his political ambitions), eight years of intense public scrutiny in the White House, and the pressures of raising children under constant observation. Both have spoken candidly about the work involved, including marriage counselling, suggesting a relationship sustained by deliberate alignment rather than effortless compatibility.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to think about.</p>

<div class="assess-group">
<h4>Connection</h4>

<div class="assess-input-group" id="ig-attachment">
    <span class="assess-label">What is your sense of your own attachment style?</span>
    <span class="assess-hint">Secure, anxious, avoidant, or disorganised &ndash; even a rough sense is useful.</span>
    <select id="a-attachment" onchange="handleAssessInput('a-attachment')">
        <option value="">Select...</option>
        <option value="no-idea">No idea &ndash; have not thought about this</option>
        <option value="vague">Vague sense &ndash; have heard the terms but unsure which fits</option>
        <option value="know-style">Know my style &ndash; can identify it but not sure how it shows up day to day</option>
        <option value="understand-impact">Understand impact &ndash; know my style and how it affects my relationship</option>
        <option value="actively-working">Actively working on it &ndash; aware of my patterns and adjusting them</option>
    </select> <span class="assess-percentile-hint" id="pct-attachment"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-attachment" onchange="handleSkip('a-attachment')"><label for="skip-attachment">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-vulnerability">
    <span class="assess-label">Have you shared something genuinely personal or difficult with your partner in the past fortnight?</span>
    <span class="assess-hint">Something beyond logistics &ndash; a fear, a hope, a frustration, an appreciation.</span>
    <select id="a-vulnerability" onchange="handleAssessInput('a-vulnerability')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I do not share personal things with my partner</option>
        <option value="rarely">Rarely &ndash; it has been months since I shared something vulnerable</option>
        <option value="not-recently">Not recently &ndash; not in the past fortnight</option>
        <option value="yes-once">Yes &ndash; at least once in the past fortnight</option>
        <option value="yes-regularly">Yes, regularly &ndash; this is a normal part of how we communicate</option>
    </select> <span class="assess-percentile-hint" id="pct-vulnerability"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-vulnerability" onchange="handleSkip('a-vulnerability')"><label for="skip-vulnerability">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-quality-time">
    <span class="assess-label">How much undistracted, one-on-one time do you spend with your partner in a typical week?</span>
    <span class="assess-hint">Time without screens, children, or other distractions &ndash; focused on each other.</span>
    <select id="a-quality-time" onchange="handleAssessInput('a-quality-time')">
        <option value="">Select...</option>
        <option value="almost-none">Almost none &ndash; less than 30 minutes per week</option>
        <option value="minimal">Minimal &ndash; 30 minutes to 1 hour per week</option>
        <option value="some">Some &ndash; 1 to 3 hours per week</option>
        <option value="regular">Regular &ndash; 3 to 5 hours per week</option>
        <option value="substantial">Substantial &ndash; over 5 hours per week</option>
    </select> <span class="assess-percentile-hint" id="pct-quality-time"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-quality-time" onchange="handleSkip('a-quality-time')"><label for="skip-quality-time">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Harmony</h4>

<div class="assess-input-group" id="ig-conflict-patterns">
    <span class="assess-label">What is your most common conflict pattern as a couple?</span>
    <span class="assess-hint">Does one person pursue while the other withdraws? Do arguments escalate or get swept under the carpet?</span>
    <select id="a-conflict-patterns" onchange="handleAssessInput('a-conflict-patterns')">
        <option value="">Select...</option>
        <option value="no-idea">No idea &ndash; have not identified a pattern</option>
        <option value="escalation">Escalation &ndash; arguments tend to spiral and intensify</option>
        <option value="pursue-withdraw">Pursue-withdraw &ndash; one pushes, the other retreats</option>
        <option value="avoidance">Avoidance &ndash; issues get swept under the carpet</option>
        <option value="constructive">Constructive &ndash; we disagree but resolve things without lasting damage</option>
    </select> <span class="assess-percentile-hint" id="pct-conflict-patterns"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-conflict-patterns" onchange="handleSkip('a-conflict-patterns')"><label for="skip-conflict-patterns">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-responsibilities">
    <span class="assess-label">Do both partners feel the division of household and life responsibilities is fair?</span>
    <span class="assess-hint">Cooking, cleaning, finances, childcare, emotional labour &ndash; consider all of it.</span>
    <select id="a-responsibilities" onchange="handleAssessInput('a-responsibilities')">
        <option value="">Select...</option>
        <option value="very-unequal">Very unequal &ndash; one person carries most of the load</option>
        <option value="somewhat-unequal">Somewhat unequal &ndash; noticeable imbalance</option>
        <option value="mostly-fair">Mostly fair &ndash; some imbalances but broadly acceptable</option>
        <option value="fair">Fair &ndash; both feel it is equitable</option>
        <option value="not-sure">Not sure &ndash; have not discussed this recently</option>
    </select> <span class="assess-percentile-hint" id="pct-responsibilities"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-responsibilities" onchange="handleSkip('a-responsibilities')"><label for="skip-responsibilities">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-repair">
    <span class="assess-label">How long does it typically take you to repair after an argument?</span>
    <span class="assess-hint">Think about the last few disagreements. How quickly did you return to normal?</span>
    <select id="a-repair" onchange="handleAssessInput('a-repair')">
        <option value="">Select...</option>
        <option value="days-or-longer">Days or longer &ndash; arguments linger for a long time</option>
        <option value="overnight">Overnight &ndash; usually resolved by the next day</option>
        <option value="hours">Hours &ndash; we cool down and reconnect within the same day</option>
        <option value="quickly">Quickly &ndash; we repair within an hour or so</option>
        <option value="immediately">Immediately &ndash; we can disagree and reconnect almost straight away</option>
    </select> <span class="assess-percentile-hint" id="pct-repair"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-repair" onchange="handleSkip('a-repair')"><label for="skip-repair">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Alignment</h4>

<div class="assess-input-group" id="ig-values-match">
    <span class="assess-label">How well do you know where your core values align and diverge with your partner?</span>
    <span class="assess-hint">Money, religion, politics, ambition, family, lifestyle &ndash; where do you agree and disagree?</span>
    <select id="a-values-match" onchange="handleAssessInput('a-values-match')">
        <option value="">Select...</option>
        <option value="not-discussed">Not discussed &ndash; we have never explicitly talked about our values</option>
        <option value="assumed">Assumed alignment &ndash; I think we agree but we have not checked</option>
        <option value="some-discussion">Some discussion &ndash; we have talked about a few areas</option>
        <option value="clear-picture">Clear picture &ndash; we know where we align and where we diverge</option>
        <option value="actively-managed">Actively managed &ndash; we revisit and negotiate differences regularly</option>
    </select> <span class="assess-percentile-hint" id="pct-values-match"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-values-match" onchange="handleSkip('a-values-match')"><label for="skip-values-match">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-future-vision">
    <span class="assess-label">Have you discussed and agreed on what you want your lives to look like in five years?</span>
    <span class="assess-hint">Location, careers, children, finances, retirement &ndash; do you have a shared picture?</span>
    <select id="a-future-vision" onchange="handleAssessInput('a-future-vision')">
        <option value="">Select...</option>
        <option value="never-discussed">Never discussed &ndash; we have not talked about the future together</option>
        <option value="vague">Vague &ndash; general sense but nothing specific</option>
        <option value="some-areas">Some areas &ndash; agreed on a few things but not others</option>
        <option value="mostly-aligned">Mostly aligned &ndash; shared picture with a few open questions</option>
        <option value="fully-aligned">Fully aligned &ndash; clear, shared vision we both feel good about</option>
    </select> <span class="assess-percentile-hint" id="pct-future-vision"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-future-vision" onchange="handleSkip('a-future-vision')"><label for="skip-future-vision">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-decisions">
    <span class="assess-label">In your last major joint decision, did both of you feel genuinely heard?</span>
    <span class="assess-hint">A move, a purchase, a career change, a family decision &ndash; how did the process feel?</span>
    <select id="a-decisions" onchange="handleAssessInput('a-decisions')">
        <option value="">Select...</option>
        <option value="one-sided">One-sided &ndash; one person decided and the other went along</option>
        <option value="somewhat-heard">Somewhat heard &ndash; input was taken but one voice dominated</option>
        <option value="mostly-heard">Mostly heard &ndash; both contributed but not equally</option>
        <option value="fully-heard">Fully heard &ndash; both felt genuinely heard and the decision was collaborative</option>
        <option value="no-recent">No recent major decision to reflect on</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-decisions" onchange="handleSkip('a-decisions')"><label for="skip-decisions">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-connection">
        <span class="assess-summary-label">Connection</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-connection" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-connection">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-harmony">
        <span class="assess-summary-label">Harmony</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-harmony" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-harmony">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-alignment">
        <span class="assess-summary-label">Alignment</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-alignment" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-alignment">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published research on relationship quality, communication, and conflict resolution among couples. The 'decisions' item is not scored.</p>
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

<p>You now understand why relationship quality matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about connection, harmony, and alignment. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/romantic-relationships/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Relationship Quality Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Relationship Quality. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/romantic-relationships/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'romantic-relationships';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-attachment', 'a-vulnerability', 'a-quality-time',
        'a-conflict-patterns', 'a-responsibilities', 'a-repair',
        'a-values-match', 'a-future-vision', 'a-decisions'
    ];

    var UNSCORED_ITEMS = ['a-decisions'];

    var THRESHOLDS = {
        'a-attachment': [
            {v:'no-idea',p:8},{v:'vague',p:25},{v:'know-style',p:48},{v:'understand-impact',p:75},{v:'actively-working',p:93}
        ],
        'a-vulnerability': [
            {v:'never',p:5},{v:'rarely',p:18},{v:'not-recently',p:38},{v:'yes-once',p:65},{v:'yes-regularly',p:92}
        ],
        'a-quality-time': [
            {v:'almost-none',p:8},{v:'minimal',p:22},{v:'some',p:48},{v:'regular',p:75},{v:'substantial',p:93}
        ],
        'a-conflict-patterns': [
            {v:'no-idea',p:15},{v:'escalation',p:12},{v:'pursue-withdraw',p:25},{v:'avoidance',p:30},{v:'constructive',p:85}
        ],
        'a-responsibilities': [
            {v:'very-unequal',p:8},{v:'somewhat-unequal',p:28},{v:'mostly-fair',p:55},{v:'fair',p:85},{v:'not-sure',p:20}
        ],
        'a-repair': [
            {v:'days-or-longer',p:8},{v:'overnight',p:28},{v:'hours',p:52},{v:'quickly',p:78},{v:'immediately',p:95}
        ],
        'a-values-match': [
            {v:'not-discussed',p:8},{v:'assumed',p:25},{v:'some-discussion',p:48},{v:'clear-picture',p:78},{v:'actively-managed',p:95}
        ],
        'a-future-vision': [
            {v:'never-discussed',p:8},{v:'vague',p:25},{v:'some-areas',p:48},{v:'mostly-aligned',p:75},{v:'fully-aligned',p:95}
        ],
    };

    var VALUE_ITEMS = {
        connection: ['a-attachment', 'a-vulnerability', 'a-quality-time'],
        harmony: ['a-conflict-patterns', 'a-responsibilities', 'a-repair'],
        alignment: ['a-values-match', 'a-future-vision'],
    };

    // --- Scoring functions ---

    function ordinalSuffix(n) {
        var s = ['th','st','nd','rd'];
        var v = n % 100;
        return n + (s[(v-20)%10] || s[v] || s[0]);
    }
    function interpolatePercentile(value, thresholds) {
        for (var i = 0; i < thresholds.length; i++) {
            if (thresholds[i].v === String(value)) return thresholds[i].p;
        }
        return null;
    }

    function getItemPercentile(itemId) {
        if (UNSCORED_ITEMS.indexOf(itemId) !== -1) return null;
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
        ['connection', 'harmony', 'alignment'].forEach(function(vk) {
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

    function updateAssessRecorded() {
        var allAnswered = ASSESS_IDS.every(function(id) { return isItemAnswered(id); });
        var recorded = document.getElementById('assessRecorded');
        if (recorded) recorded.classList.toggle('visible', allAnswered);
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
        ['connection', 'harmony', 'alignment'].forEach(function(vk) {
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
