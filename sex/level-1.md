---
layout: default
title: "Sex – Level 1: Awareness"
life_area_slug: sex
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

<h1>Sex: Level 1</h1>

<p class="l1-subtitle">Understand what sexual wellbeing means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Sex Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why sexual wellbeing matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Sexual wellbeing is a significant component of quality of life for most adults. Research published in the <em>Journal of Sexual Medicine</em> found that <a href="https://pubmed.ncbi.nlm.nih.gov/27671968/" target="_blank">62% of men and 43% of women</a> rate sexual health as highly important to their overall quality of life.</p>

<p>The benefits extend well beyond the bedroom. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11601183/" target="_blank">Sexual satisfaction and regular sexual activity</a> are associated with improved cardiovascular health, lower rates of depression, and stronger relationship satisfaction. Among a representative sample of 16,000 American adults, sexual frequency was a strong positive predictor of self-reported happiness.</p>

<p>Yet there is a substantial gap between desired and actual sexual experience for many people. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10364113/" target="_blank">International research</a> identifies open sexual communication as one of the strongest predictors of both frequency and satisfaction, but most couples rarely discuss their sexual needs explicitly. The result is that many people carry chronic dissatisfaction they never address.</p>

<p>The relationship between frequency and satisfaction also has a ceiling. Beyond a baseline threshold, quality and connection matter considerably more than frequency alone. Understanding what you actually value about your sexual life &ndash; and where the gaps are &ndash; is the starting point for meaningful improvement.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about sex</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue sexual wellbeing for different reasons. This site scores every sex intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Frequency</h3>
<p>Maintaining a satisfying rate of sexual activity that meets both partners' needs. Initiating regularly, managing desire discrepancies constructively, and ensuring sexual intimacy remains a consistent part of the relationship rather than something that fades over time.</p>

<h3>Variety</h3>
<p>Diversity and novelty in sexual experiences &ndash; exploring new activities, settings, dynamics, and expressions of intimacy. Openness to experimentation, comfort discussing preferences, and actively introducing novelty to prevent routine.</p>

<h3>Pleasure</h3>
<p>The direct experience of physical and psychological enjoyment from sexual activity. Knowledge of your own body, ability to communicate desires, and the pursuit of mutually satisfying experiences.</p>

<h3>Contentment</h3>
<p>Overall satisfaction with your sexual life as a whole &ndash; feeling at peace with the role sex plays in your life and relationship. Acceptance, realistic expectations, and the sense that your sexual life is genuinely fulfilling.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each sexual wellbeing value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Frequency &amp; Variety &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Dan_Savage" target="_blank">Dan Savage</a> has written the syndicated sex advice column <em>Savage Love</em> since 1991 and hosts the <em>Savage Lovecast</em> podcast. Over more than three decades, he has publicly discussed and modelled how long-term couples can sustain sexual frequency and novelty through open communication, negotiation, and willingness to explore. He coined the concept of being "GGG" (good, giving, and game) as a practical framework for maintaining sexual generosity in committed relationships, and has been with his husband Terry Miller since 1995.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Pleasure &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Emily_Nagoski" target="_blank">Emily Nagoski</a> is a sex educator and researcher whose book <em>Come As You Are</em> synthesises decades of sexual response research into a practical framework for understanding arousal, desire, and pleasure. Her work on the dual control model of sexual response &ndash; distinguishing between sexual "accelerators" and "brakes" &ndash; has helped hundreds of thousands of people understand their own patterns of desire and expand their capacity for enjoyment. She holds a PhD from Indiana University's Kinsey Institute.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Contentment &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Peggy_Kleinplatz" target="_blank">Peggy Kleinplatz</a> is a clinical psychologist and sex therapist at the University of Ottawa who has spent over 20 years researching what she calls "optimal sexual experiences." Her studies of people who report extraordinary sexual satisfaction &ndash; including couples in their 70s and 80s &ndash; found that the common thread was not technique or frequency but presence, authenticity, and deep interpersonal connection. Her research provides some of the strongest evidence that sexual fulfilment can be sustained and even deepen across the lifespan.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know straight away, others might take a few minutes of honest reflection.</p>

<div class="assess-group">
<h4>Frequency</h4>

<div class="assess-input-group" id="ig-current-frequency">
    <span class="assess-label">How often do you have sex in a typical month?</span>
    <span class="assess-hint">An honest estimate is fine &ndash; precision is less important than awareness.</span>
    <select id="a-current-frequency" onchange="handleAssessInput('a-current-frequency')">
        <option value="">Select...</option>
        <option value="rarely">Rarely &ndash; less than once a month</option>
        <option value="1-2">1 &ndash; 2 times per month</option>
        <option value="3-4">3 &ndash; 4 times per month (roughly weekly)</option>
        <option value="5-8">5 &ndash; 8 times per month</option>
        <option value="over-8">More than 8 times per month</option>
    </select> <span class="assess-percentile-hint" id="pct-current-frequency"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-current-frequency" onchange="handleSkip('a-current-frequency')"><label for="skip-current-frequency">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-desire-gap">
    <span class="assess-label">Is there a gap between how often you want sex and how often it happens?</span>
    <span class="assess-hint">Consider both your own desires and your partner's. Is there a discrepancy?</span>
    <select id="a-desire-gap" onchange="handleAssessInput('a-desire-gap')">
        <option value="">Select...</option>
        <option value="large-gap-want-more">Large gap &ndash; I want significantly more than happens</option>
        <option value="some-gap-want-more">Some gap &ndash; I would like somewhat more</option>
        <option value="well-matched">Well matched &ndash; frequency suits me</option>
        <option value="some-gap-want-less">Some gap &ndash; I would prefer somewhat less</option>
        <option value="large-gap-want-less">Large gap &ndash; I want significantly less than happens</option>
    </select> <span class="assess-percentile-hint" id="pct-desire-gap"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-desire-gap" onchange="handleSkip('a-desire-gap')"><label for="skip-desire-gap">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-initiation">
    <span class="assess-label">Who typically initiates sex in your relationship?</span>
    <span class="assess-hint">Is initiation roughly balanced, or does one person carry most of the responsibility?</span>
    <select id="a-initiation" onchange="handleAssessInput('a-initiation')">
        <option value="">Select...</option>
        <option value="almost-always-me">Almost always me</option>
        <option value="mostly-me">Mostly me</option>
        <option value="roughly-equal">Roughly equal</option>
        <option value="mostly-partner">Mostly my partner</option>
        <option value="almost-always-partner">Almost always my partner</option>
        <option value="neither">Neither &ndash; it rarely happens</option>
    </select> <span class="assess-percentile-hint" id="pct-initiation"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-initiation" onchange="handleSkip('a-initiation')"><label for="skip-initiation">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Variety</h4>

<div class="assess-input-group" id="ig-routine">
    <span class="assess-label">How much variation is there in your sexual experiences?</span>
    <span class="assess-hint">Same time, same place, same sequence &ndash; or do things change?</span>
    <select id="a-routine" onchange="handleAssessInput('a-routine')">
        <option value="">Select...</option>
        <option value="very-predictable">Very predictable &ndash; almost always the same pattern</option>
        <option value="mostly-predictable">Mostly predictable &ndash; occasional variation but a clear routine</option>
        <option value="some-variation">Some variation &ndash; a mix of familiar and new</option>
        <option value="good-variation">Good variation &ndash; regularly try different things</option>
        <option value="highly-varied">Highly varied &ndash; actively explore and change things up</option>
    </select> <span class="assess-percentile-hint" id="pct-routine"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-routine" onchange="handleSkip('a-routine')"><label for="skip-routine">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-curiosities">
    <span class="assess-label">Are there things you are curious about but have not tried or discussed with your partner?</span>
    <span class="assess-hint">Unexpressed curiosities are common &ndash; the point is to notice them, not to act on all of them.</span>
    <select id="a-curiosities" onchange="handleAssessInput('a-curiosities')">
        <option value="">Select...</option>
        <option value="many-unspoken">Many unspoken &ndash; several curiosities I have not raised</option>
        <option value="a-few-unspoken">A few unspoken &ndash; one or two things I have not mentioned</option>
        <option value="discussed-not-tried">Discussed but not tried &ndash; we have talked about things but not acted</option>
        <option value="exploring">Exploring &ndash; we discuss and try new things regularly</option>
        <option value="fully-expressed">Fully expressed &ndash; I have shared all my curiosities with my partner</option>
    </select> <span class="assess-percentile-hint" id="pct-curiosities"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-curiosities" onchange="handleSkip('a-curiosities')"><label for="skip-curiosities">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Pleasure</h4>

<div class="assess-input-group" id="ig-own-body">
    <span class="assess-label">How well do you know what you find most pleasurable?</span>
    <span class="assess-hint">Consider whether you could clearly describe your preferences to a partner.</span>
    <select id="a-own-body" onchange="handleAssessInput('a-own-body')">
        <option value="">Select...</option>
        <option value="unsure">Unsure &ndash; have not really explored this</option>
        <option value="vague">Vague sense &ndash; know some basics but not in detail</option>
        <option value="reasonable">Reasonable &ndash; know my main preferences</option>
        <option value="well">Well &ndash; could clearly describe what I enjoy and what I do not</option>
        <option value="very-well">Very well &ndash; detailed understanding of my own responses and preferences</option>
    </select> <span class="assess-percentile-hint" id="pct-own-body"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-own-body" onchange="handleSkip('a-own-body')"><label for="skip-own-body">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-communication">
    <span class="assess-label">How comfortable are you communicating your sexual preferences and needs?</span>
    <span class="assess-hint">Both giving feedback ('I like this') and asking for what you want.</span>
    <select id="a-communication" onchange="handleAssessInput('a-communication')">
        <option value="">Select...</option>
        <option value="very-uncomfortable">Very uncomfortable &ndash; almost never say anything</option>
        <option value="uncomfortable">Uncomfortable &ndash; find it difficult and usually avoid it</option>
        <option value="somewhat">Somewhat comfortable &ndash; can manage the basics but not details</option>
        <option value="comfortable">Comfortable &ndash; can communicate clearly about most things</option>
        <option value="very-comfortable">Very comfortable &ndash; open, specific, and at ease discussing preferences</option>
    </select> <span class="assess-percentile-hint" id="pct-communication"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-communication" onchange="handleSkip('a-communication')"><label for="skip-communication">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Contentment</h4>

<div class="assess-input-group" id="ig-overall-satisfaction">
    <span class="assess-label">Overall, is your sexual life a source of fulfilment, frustration, or indifference?</span>
    <span class="assess-hint">Not how you think it should be, but how it actually feels to you right now.</span>
    <select id="a-overall-satisfaction" onchange="handleAssessInput('a-overall-satisfaction')">
        <option value="">Select...</option>
        <option value="frustration">Frustration &ndash; a consistent source of dissatisfaction</option>
        <option value="some-frustration">Some frustration &ndash; more negative than positive</option>
        <option value="indifferent">Indifferent &ndash; not something I think about much</option>
        <option value="mostly-fulfilling">Mostly fulfilling &ndash; generally satisfying with room to improve</option>
        <option value="deeply-fulfilling">Deeply fulfilling &ndash; a genuine source of joy and connection</option>
    </select> <span class="assess-percentile-hint" id="pct-overall-satisfaction"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-overall-satisfaction" onchange="handleSkip('a-overall-satisfaction')"><label for="skip-overall-satisfaction">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-comparison">
    <span class="assess-label">Do you compare your sexual life to external standards, and how does that affect your satisfaction?</span>
    <span class="assess-hint">Comparison can distort your sense of what is genuinely enough for you.</span>
    <select id="a-comparison" onchange="handleAssessInput('a-comparison')">
        <option value="">Select...</option>
        <option value="constant-negative">Constant &ndash; frequently compare and it lowers my satisfaction</option>
        <option value="sometimes-negative">Sometimes &ndash; occasional comparison that makes me feel worse</option>
        <option value="aware-not-affected">Aware but unaffected &ndash; notice comparisons but they do not bother me</option>
        <option value="rarely">Rarely &ndash; almost never compare</option>
        <option value="grounded">Grounded &ndash; my sense of satisfaction is based entirely on my own experience</option>
    </select> <span class="assess-percentile-hint" id="pct-comparison"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-comparison" onchange="handleSkip('a-comparison')"><label for="skip-comparison">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-frequency">
        <span class="assess-summary-label">Frequency</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-frequency" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-frequency">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-variety">
        <span class="assess-summary-label">Variety</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-variety" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-variety">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-pleasure">
        <span class="assess-summary-label">Pleasure</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-pleasure" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-pleasure">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-contentment">
        <span class="assess-summary-label">Contentment</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-contentment" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-contentment">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published research on sexual frequency, satisfaction, and communication among adults. All items in this area are scored.</p>
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

<p>You now understand why sexual wellbeing matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about frequency, variety, pleasure, and contentment. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/sex/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Sex Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Sex. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/sex/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'sex';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-current-frequency', 'a-desire-gap', 'a-initiation',
        'a-routine', 'a-curiosities',
        'a-own-body', 'a-communication',
        'a-overall-satisfaction', 'a-comparison'
    ];

    var UNSCORED_ITEMS = [];

    var THRESHOLDS = {
        'a-current-frequency': [
            {v:'rarely',p:10},{v:'1-2',p:28},{v:'3-4',p:50},{v:'5-8',p:75},{v:'over-8',p:93}
        ],
        'a-desire-gap': [
            {v:'large-gap-want-more',p:10},{v:'some-gap-want-more',p:30},{v:'well-matched',p:80},{v:'some-gap-want-less',p:40},{v:'large-gap-want-less',p:15}
        ],
        'a-initiation': [
            {v:'almost-always-me',p:25},{v:'mostly-me',p:40},{v:'roughly-equal',p:85},{v:'mostly-partner',p:40},{v:'almost-always-partner',p:25},{v:'neither',p:5}
        ],
        'a-routine': [
            {v:'very-predictable',p:10},{v:'mostly-predictable',p:28},{v:'some-variation',p:50},{v:'good-variation',p:78},{v:'highly-varied',p:95}
        ],
        'a-curiosities': [
            {v:'many-unspoken',p:10},{v:'a-few-unspoken',p:30},{v:'discussed-not-tried',p:52},{v:'exploring',p:78},{v:'fully-expressed',p:95}
        ],
        'a-own-body': [
            {v:'unsure',p:8},{v:'vague',p:25},{v:'reasonable',p:50},{v:'well',p:78},{v:'very-well',p:95}
        ],
        'a-communication': [
            {v:'very-uncomfortable',p:5},{v:'uncomfortable',p:20},{v:'somewhat',p:45},{v:'comfortable',p:75},{v:'very-comfortable',p:95}
        ],
        'a-overall-satisfaction': [
            {v:'frustration',p:8},{v:'some-frustration',p:22},{v:'indifferent',p:42},{v:'mostly-fulfilling',p:72},{v:'deeply-fulfilling',p:95}
        ],
        'a-comparison': [
            {v:'constant-negative',p:8},{v:'sometimes-negative',p:28},{v:'aware-not-affected',p:52},{v:'rarely',p:75},{v:'grounded',p:95}
        ],
    };

    var VALUE_ITEMS = {
        frequency: ['a-current-frequency', 'a-desire-gap', 'a-initiation'],
        variety: ['a-routine', 'a-curiosities'],
        pleasure: ['a-own-body', 'a-communication'],
        contentment: ['a-overall-satisfaction', 'a-comparison'],
    };

    // --- Scoring functions ---

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
        hintEl.textContent = pct !== null ? '~' + pct + 'th percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['frequency', 'variety', 'pleasure', 'contentment'].forEach(function(vk) {
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
        ['frequency', 'variety', 'pleasure', 'contentment'].forEach(function(vk) {
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
