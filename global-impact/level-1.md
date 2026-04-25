---
layout: default
title: "Global Impact – Level 1: Awareness"
life_area_slug: global-impact
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

<h1>Global Impact: Level 1</h1>

<p class="l1-subtitle">Understand what global impact means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Global Impact Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why global impact matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>The resources you direct toward improving the world &ndash; through charitable giving, career choices, or advocacy &ndash; vary enormously in their effectiveness. <a href="https://www.givewell.org/how-we-work/our-criteria/cost-effectiveness" target="_blank">Research by GiveWell</a> shows that the best health interventions can be over 100 times more cost-effective than average ones addressing the same problem. Where you give matters far more than how much.</p>

<p>This is not just theoretical. GiveWell has directed over <a href="https://www.givewell.org/impact" target="_blank">$2.6 billion to recommended charities</a>, contributing to an estimated 340,000 lives saved &ndash; primarily through interventions like malaria prevention and vitamin A supplementation. Pledging movements like <a href="https://www.givingwhatwecan.org/" target="_blank">Giving What We Can</a> have demonstrated that sustained, planned philanthropy from ordinary earners can create extraordinary impact over a lifetime.</p>

<p>Beyond effectiveness, giving reliably improves the giver's own wellbeing. Research consistently shows that <a href="https://doi.org/10.1126/science.1150952" target="_blank">spending money on others produces greater happiness</a> than spending it on oneself, and this effect holds across income levels and cultures. Strategic generosity is one of the rare investments that benefits both the world and the person making it.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about global impact</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach global impact for different reasons. This site scores every global impact intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Impartiality</h3>
<p>Directing resources toward causes based on evidence of impact rather than personal connection or emotional appeal. Cost-effectiveness analysis, cause prioritisation informed by research, and willingness to support unfamiliar causes if the evidence warrants it. People who lean towards this value treat philanthropy as a problem to be optimised.</p>

<h3>Passion</h3>
<p>Contributing to causes you genuinely care about &ndash; areas that resonate with your personal experience, interests, and values. Volunteering in areas that energise you and choosing impact channels that sustain your motivation over decades. People who lean towards this value believe sustained commitment requires personal meaning.</p>

<h3>Sustainability</h3>
<p>Maintaining your global impact practice over the long term without burnout, guilt, or financial strain. Setting sustainable giving levels, building impact habits that fit your life, and ensuring that your philanthropic practice enhances rather than diminishes your wellbeing. People who lean towards this value plan for decades of contribution.</p>

<h3>Fulfilment</h3>
<p>The personal satisfaction and sense of purpose derived from making a positive difference. Feeling that your contributions matter, experiencing gratitude and meaning from giving, and ensuring that your impact work is a source of joy rather than obligation. People who lean towards this value see giving as enriching their own life.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each global impact value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Impartiality &ndash; Level 5</div>
    <p><a href="https://www.thelifeyoucansave.org/about-us/" target="_blank">Toby Ord</a> is a moral philosopher at Oxford who co-founded Giving What We Can and wrote <em>The Precipice</em> on existential risk. He has pledged to give everything he earns above &pound;18,000 to the most effective charities he can find, and his research on cause prioritisation has influenced billions of pounds in philanthropic allocation. His approach treats global impact as a rigorous intellectual and moral project.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Passion &ndash; Level 5</div>
    <p><a href="https://www.womenonwaves.org/en/page/2591/about-women-on-waves" target="_blank">Rebecca Gomperts</a> is a Dutch physician who founded Women on Waves and Women on Web, providing reproductive healthcare access to women in countries with restrictive laws. Her work stems from direct clinical experience treating women harmed by unsafe procedures. Over two decades, her organisations have assisted hundreds of thousands of women, driven entirely by personal conviction about a cause she witnessed first-hand.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Sustainability &ndash; Level 5</div>
    <p><a href="https://founderspledge.com/about" target="_blank">David Goldberg</a> co-founded Founders Pledge, through which technology entrepreneurs commit to donating a percentage of their proceeds from company exits to effective charities. The organisation has facilitated over $10 billion in pledges from more than 1,800 founders. It demonstrates how building giving into the structure of a career creates sustained, compounding impact over a lifetime.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Fulfilment &ndash; Level 5</div>
    <p><a href="https://www.roomtoread.org/about/our-story/" target="_blank">John Wood</a> left a senior role at Microsoft after visiting schools in Nepal and seeing empty library shelves. He founded Room to Read, which has benefited over 40 million children across 23 countries with literacy and gender equality programmes. He frequently speaks about how leaving a lucrative career for philanthropic work was the most fulfilling decision of his life.</p>
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

<div class="assess-privacy">Your answers are stored only on your device and are never sent to our servers. Only your estimated percentile scores (single numbers, not your answers) may be synced if you create an account. Percentile estimates are approximate – they position you roughly relative to the general population based on your self-report, but could easily be off by 10–15 points.</div>

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to reflect on.</p>

<div class="assess-group">
<h4>Impartiality</h4>

<div class="assess-input-group" id="ig-giving-total">
    <span class="assess-label">How much did you donate to charity last year?</span>
    <span class="assess-hint">Check your bank statements or tax records if you're unsure.</span>
    <select id="a-giving-total" onchange="handleAssessInput('a-giving-total')"><option value="">Select...</option><option value="nothing">Nothing</option><option value="under-100">Under &pound;100</option><option value="100-to-500">&pound;100 &ndash; &pound;500</option><option value="500-to-2000">&pound;500 &ndash; &pound;2,000</option><option value="over-2000">Over &pound;2,000</option></select> <span class="assess-percentile-hint" id="pct-giving-total"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-giving-total" onchange="handleSkip('a-giving-total')"><label for="skip-giving-total">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-charity-evaluators">
    <span class="assess-label">Did any of your donations go to charities recommended by evaluators like GiveWell or Animal Charity Evaluators?</span>
    <span class="assess-hint">If you haven't heard of these organisations, that's useful information too.</span>
    <select id="a-charity-evaluators" onchange="handleAssessInput('a-charity-evaluators')"><option value="">Select...</option><option value="never-heard">Never heard of charity evaluators</option><option value="aware-but-no">Aware of them but have never used their recommendations</option><option value="some">Some &ndash; a portion of my giving goes to recommended charities</option><option value="most">Most &ndash; the majority of my giving follows evaluator recommendations</option><option value="all">All &ndash; I give exclusively to evidence-backed charities</option></select> <span class="assess-percentile-hint" id="pct-charity-evaluators"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-charity-evaluators" onchange="handleSkip('a-charity-evaluators')"><label for="skip-charity-evaluators">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-cost-effectiveness">
    <span class="assess-label">How well do you understand that different charities vary by 100x or more in cost-effectiveness?</span>
    <span class="assess-hint">This is the core insight of effective giving &ndash; where you give matters more than how much.</span>
    <select id="a-cost-effectiveness" onchange="handleAssessInput('a-cost-effectiveness')"><option value="">Select...</option><option value="unaware">Unaware &ndash; this is new to me</option><option value="heard-of-it">Heard of it &ndash; but haven't looked into it</option><option value="basic">Basic understanding &ndash; I know the concept</option><option value="good">Good understanding &ndash; I've read about it and it influences my giving</option><option value="deep">Deep understanding &ndash; cost-effectiveness is central to how I allocate donations</option></select> <span class="assess-percentile-hint" id="pct-cost-effectiveness"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-cost-effectiveness" onchange="handleSkip('a-cost-effectiveness')"><label for="skip-cost-effectiveness">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Passion</h4>

<div class="assess-input-group" id="ig-causes-care">
    <span class="assess-label">Can you name the causes you genuinely care about, as opposed to those you give to out of habit?</span>
    <span class="assess-hint">Think about what keeps you up at night or what news stories genuinely move you.</span>
    <select id="a-causes-care" onchange="handleAssessInput('a-causes-care')"><option value="">Select...</option><option value="no">No &ndash; I haven't thought about which causes matter most to me</option><option value="vaguely">Vaguely &ndash; I have a general sense but nothing specific</option><option value="one-or-two">One or two &ndash; I know my primary cause areas</option><option value="clearly">Clearly &ndash; I can articulate why each cause matters to me</option><option value="deeply-considered">Deeply considered &ndash; I've researched and deliberately chosen my cause areas</option></select> <span class="assess-percentile-hint" id="pct-causes-care"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-causes-care" onchange="handleSkip('a-causes-care')"><label for="skip-causes-care">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-volunteering">
    <span class="assess-label">How many hours per month do you volunteer or contribute non-financial resources to any cause?</span>
    <span class="assess-hint">Include pro bono work, board service, advocacy, mentoring, or other non-monetary contributions.</span>
    <select id="a-volunteering" onchange="handleAssessInput('a-volunteering')"><option value="">Select...</option><option value="none">None</option><option value="1-to-3">1 &ndash; 3 hours per month</option><option value="4-to-8">4 &ndash; 8 hours per month</option><option value="9-to-16">9 &ndash; 16 hours per month</option><option value="over-16">Over 16 hours per month</option></select> <span class="assess-percentile-hint" id="pct-volunteering"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-volunteering" onchange="handleSkip('a-volunteering')"><label for="skip-volunteering">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-motivation">
    <span class="assess-label">Is your giving motivated by genuine care, guilt, obligation, or social expectation?</span>
    <span class="assess-hint">There's no wrong answer &ndash; the question is whether you've reflected on it.</span>
    <select id="a-motivation" onchange="handleAssessInput('a-motivation')"><option value="">Select...</option><option value="dont-give">I don't currently give</option><option value="guilt-obligation">Primarily guilt or obligation</option><option value="social-expectation">Primarily social expectation</option><option value="mixed">Mixed &ndash; some genuine care, some obligation</option><option value="genuine-care">Primarily genuine care &ndash; I give because I want to</option></select> <span class="assess-percentile-hint" id="pct-motivation"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-motivation" onchange="handleSkip('a-motivation')"><label for="skip-motivation">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Sustainability</h4>

<div class="assess-input-group" id="ig-giving-percentage">
    <span class="assess-label">What percentage of your income do you give to charity annually?</span>
    <span class="assess-hint">Divide your total annual donations by your annual income. Even a rough estimate is useful.</span>
    <select id="a-giving-percentage" onchange="handleAssessInput('a-giving-percentage')"><option value="">Select...</option><option value="zero">0% &ndash; I don't donate</option><option value="under-1">Under 1%</option><option value="1-to-3">1 &ndash; 3%</option><option value="3-to-10">3 &ndash; 10%</option><option value="over-10">Over 10%</option></select> <span class="assess-percentile-hint" id="pct-giving-percentage"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-giving-percentage" onchange="handleSkip('a-giving-percentage')"><label for="skip-giving-percentage">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-giving-budget">
    <span class="assess-label">Do you have a giving budget or plan, or do you give sporadically?</span>
    <span class="assess-hint">Planned giving tends to result in both higher total impact and lower decision fatigue.</span>
    <select id="a-giving-budget" onchange="handleAssessInput('a-giving-budget')"><option value="">Select...</option><option value="no-giving">I don't give</option><option value="sporadic">Sporadic &ndash; I give in response to appeals or requests</option><option value="rough-plan">Rough plan &ndash; I have a general sense of how much I'll give</option><option value="budget">Budget &ndash; I have a set amount allocated annually</option><option value="structured">Structured &ndash; budget with planned recipients and timing</option></select> <span class="assess-percentile-hint" id="pct-giving-budget"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-giving-budget" onchange="handleSkip('a-giving-budget')"><label for="skip-giving-budget">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-financial-strain">
    <span class="assess-label">Is your current giving level sustainable?</span>
    <span class="assess-hint">Sustainable giving over 30 years beats generous giving that leads to burnout after 3.</span>
    <select id="a-financial-strain" onchange="handleAssessInput('a-financial-strain')"><option value="">Select...</option><option value="no-giving">I don't give</option><option value="straining">Straining &ndash; it causes noticeable financial pressure</option><option value="tight">Tight &ndash; I could sustain it but it's uncomfortable</option><option value="comfortable">Comfortable &ndash; I give without financial stress</option><option value="easy">Easy &ndash; I could give more without difficulty</option></select> <span class="assess-percentile-hint" id="pct-financial-strain"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-financial-strain" onchange="handleSkip('a-financial-strain')"><label for="skip-financial-strain">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Fulfilment</h4>

<div class="assess-input-group" id="ig-satisfaction">
    <span class="assess-label">Are your giving and impact activities a source of satisfaction or guilt?</span>
    <span class="assess-hint">Many people feel guilty about not doing enough rather than good about what they do.</span>
    <select id="a-satisfaction" onchange="handleAssessInput('a-satisfaction')"><option value="">Select...</option><option value="strong-guilt">Strong guilt &ndash; I feel bad about how little I do</option><option value="some-guilt">Some guilt &ndash; I appreciate what I do but feel I should do more</option><option value="neutral">Neutral &ndash; I don't think about it much</option><option value="mostly-satisfied">Mostly satisfied &ndash; I feel good about my contributions</option><option value="deeply-satisfied">Deeply satisfied &ndash; my giving is a consistent source of meaning</option></select> <span class="assess-percentile-hint" id="pct-satisfaction"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-satisfaction" onchange="handleSkip('a-satisfaction')"><label for="skip-satisfaction">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-connection">
    <span class="assess-label">How connected do you feel to the impact of your contributions?</span>
    <span class="assess-hint">Some people feel disconnected from the results of their giving, which can erode motivation.</span>
    <select id="a-connection" onchange="handleAssessInput('a-connection')"><option value="">Select...</option><option value="completely-disconnected">Completely disconnected &ndash; I have no sense of impact</option><option value="mostly-disconnected">Mostly disconnected &ndash; I hope it helps but don't really know</option><option value="somewhat">Somewhat connected &ndash; I get occasional updates</option><option value="well-connected">Well connected &ndash; I can see concrete results</option><option value="deeply-connected">Deeply connected &ndash; I have a clear, personal sense of the difference I make</option></select> <span class="assess-percentile-hint" id="pct-connection"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-connection" onchange="handleSkip('a-connection')"><label for="skip-connection">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-identity">
    <span class="assess-label">Is contributing to global causes an important part of your identity?</span>
    <span class="assess-hint">There's no wrong answer &ndash; the question is whether you've reflected on it.</span>
    <select id="a-identity" onchange="handleAssessInput('a-identity')"><option value="">Select...</option><option value="not-at-all">Not at all &ndash; I rarely think about it</option><option value="peripherally">Peripherally &ndash; it's something I do but not who I am</option><option value="somewhat">Somewhat &ndash; it matters to me but isn't central</option><option value="important">Important &ndash; it's a significant part of how I see myself</option><option value="core">Core &ndash; it's fundamental to my identity and values</option></select> <span class="assess-percentile-hint" id="pct-identity"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-identity" onchange="handleSkip('a-identity')"><label for="skip-identity">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-impartiality">
        <span class="assess-summary-label">Impartiality</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-impartiality" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-impartiality">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-passion">
        <span class="assess-summary-label">Passion</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-passion" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-passion">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-sustainability">
        <span class="assess-summary-label">Sustainability</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-sustainability" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-sustainability">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-fulfilment">
        <span class="assess-summary-label">Fulfilment</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-fulfilment" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-fulfilment">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on charitable giving, volunteering, and philanthropic engagement among adults. All items in this area are scored.</p>
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

<p>You now understand why global impact matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about impartiality, passion, sustainability, and fulfilment. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/global-impact/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Global Impact Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Global Impact. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/global-impact/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'global-impact';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-giving-total', 'a-charity-evaluators', 'a-cost-effectiveness',
        'a-causes-care', 'a-volunteering', 'a-motivation',
        'a-giving-percentage', 'a-giving-budget', 'a-financial-strain',
        'a-satisfaction', 'a-connection', 'a-identity'
    ];
    // Scoring thresholds: [{v, p}, ...] mapping dropdown values to percentiles.
    // Based on population data: ~60% of adults donate to charity, median donation ~$500/year,
    // ~25% volunteer, <5% use charity evaluators, ~3% give >5% of income.
    var THRESHOLDS = {
        'a-giving-total': [
            // ~40% give nothing; over 2000 is top ~15%
            {v:'nothing',p:15},{v:'under-100',p:35},{v:'100-to-500',p:55},{v:'500-to-2000',p:75},{v:'over-2000',p:92}
        ],
        'a-charity-evaluators': [
            // <5% of donors have heard of GiveWell; using evaluator recommendations is very rare
            {v:'never-heard',p:20},{v:'aware-but-no',p:50},{v:'some',p:75},{v:'most',p:90},{v:'all',p:98}
        ],
        'a-cost-effectiveness': [
            // Most people are unaware of cost-effectiveness variation; deep understanding is very rare
            {v:'unaware',p:20},{v:'heard-of-it',p:45},{v:'basic',p:65},{v:'good',p:85},{v:'deep',p:97}
        ],
        'a-causes-care': [
            // Most people have not deliberately chosen cause areas; deeply considered is rare
            {v:'no',p:15},{v:'vaguely',p:35},{v:'one-or-two',p:55},{v:'clearly',p:78},{v:'deeply-considered',p:95}
        ],
        'a-volunteering': [
            // ~25% volunteer at all; over 16 hours/month is very uncommon
            {v:'none',p:25},{v:'1-to-3',p:50},{v:'4-to-8',p:70},{v:'9-to-16',p:88},{v:'over-16',p:97}
        ],
        'a-motivation': [
            // Many give out of obligation; genuine care as primary motivator is less common than expected
            {v:'dont-give',p:10},{v:'guilt-obligation',p:25},{v:'social-expectation',p:40},{v:'mixed',p:60},{v:'genuine-care',p:85}
        ],
        'a-giving-percentage': [
            // Median US giving ~2% of income; >10% is very rare (~3% of households)
            {v:'zero',p:15},{v:'under-1',p:35},{v:'1-to-3',p:55},{v:'3-to-10',p:80},{v:'over-10',p:97}
        ],
        'a-giving-budget': [
            // Most giving is sporadic; having a structured budget is uncommon
            {v:'no-giving',p:10},{v:'sporadic',p:30},{v:'rough-plan',p:55},{v:'budget',p:78},{v:'structured',p:95}
        ],
        'a-financial-strain': [
            // Among donors, most give comfortably; straining suggests over-commitment
            {v:'no-giving',p:10},{v:'straining',p:25},{v:'tight',p:45},{v:'comfortable',p:70},{v:'easy',p:90}
        ],
        'a-satisfaction': [
            // Many people feel guilt about not doing enough; deep satisfaction is uncommon
            {v:'strong-guilt',p:10},{v:'some-guilt',p:30},{v:'neutral',p:50},{v:'mostly-satisfied',p:75},{v:'deeply-satisfied',p:95}
        ],
        'a-connection': [
            // Most donors feel disconnected from impact; deep connection is rare
            {v:'completely-disconnected',p:10},{v:'mostly-disconnected',p:30},{v:'somewhat',p:55},{v:'well-connected',p:78},{v:'deeply-connected',p:95}
        ],
        'a-identity': [
            // For most, giving is peripheral to identity; core identity is rare
            {v:'not-at-all',p:15},{v:'peripherally',p:35},{v:'somewhat',p:55},{v:'important',p:78},{v:'core',p:95}
        ]
    };

    var VALUE_ITEMS = {
        impartiality: ['a-giving-total', 'a-charity-evaluators', 'a-cost-effectiveness'],
        passion: ['a-causes-care', 'a-volunteering', 'a-motivation'],
        sustainability: ['a-giving-percentage', 'a-giving-budget', 'a-financial-strain'],
        fulfilment: ['a-satisfaction', 'a-connection', 'a-identity']
    };

    // All global-impact items are scorable
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
            setTimeout(function() { openStep(STEPS[idx + 1]); }, 300);
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
        hintEl.textContent = pct !== null ? 'roughly ' + ordinalSuffix(Math.round(pct / 10) * 10) + ' percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['impartiality', 'passion', 'sustainability', 'fulfilment'].forEach(function(vk) {
            var pct = computeValuePercentile(vk);
            var barEl = document.getElementById('bar-' + vk);
            var valEl = document.getElementById('val-' + vk);
            if (barEl && valEl) {
                if (pct !== null) {
                    barEl.style.width = pct + '%';
                    valEl.textContent = ordinalSuffix(Math.round(pct / 10) * 10);
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
        ['impartiality', 'passion', 'sustainability', 'fulfilment'].forEach(function(vk) {
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
