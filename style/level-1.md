---
layout: default
title: "Style – Level 1: Awareness"
life_area_slug: style
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

<h1>Style: Level 1</h1>

<p class="l1-subtitle">Understand what style means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Style Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why style matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your clothing and grooming choices shape how others perceive you and how you feel about yourself. The effects are measurable and surprisingly large.</p>

<p>A <a href="https://news.temple.edu/news/2023-06-01/when-you-look-good-you-feel-good-research-shows-you-might-even-be-more-productive" target="_blank">Temple University study</a> tracking 808 employee days found that people who dressed better than usual had stronger self-esteem and performed better on tasks. Research from Northwestern University showed participants wearing lab coats made significantly fewer mistakes on attention tasks compared to those in everyday clothing.</p>

<p>In the workplace, <a href="https://www.academia.edu/34496959/ASSESSING_THE_RELATIONSHIP_AND_EFFECT_OF_WORKPLACE_DRESS_CODE_ON_EMPLOYEE_PRODUCTIVITY" target="_blank">41% of employers</a> report that employees who dress professionally are more likely to be promoted, rising to 55% in financial services. Clothing also functions as a <a href="https://fashionandtextiles.springeropen.com/articles/10.1186/s40691-014-0020-7" target="_blank">communication system</a>, conveying information about competence, status, and identity before you ever speak.</p>

<p>Most people underinvest in style relative to its impact. Research shows the average person spends 17 minutes daily choosing outfits, wears only 44% of their wardrobe regularly, and frequently experiences clothing-related stress that affects punctuality and mood. Even modest improvements in how you dress can yield disproportionate returns in confidence, professional outcomes, and social interactions.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about style</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue style for different reasons. This site scores every style intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Attractiveness</h3>
<p>Looking appealing to others across romantic and social contexts through deliberate clothing, grooming, and presentation choices. People who lean towards this value focus on flattering fit, body-appropriate silhouettes, and building wardrobes that make them look their best to the widest range of people.</p>

<h3>Status & Professional</h3>
<p>Signalling competence, authority, and taste through clothing in career and social settings. People who lean towards this value invest in pieces that communicate success and command respect in professional and social hierarchies, understanding dress codes and making strategic wardrobe choices for advancement.</p>

<h3>Self-Expression</h3>
<p>Communicating identity, values, and affiliations through distinctive clothing choices. People who lean towards this value choose clothing that reflects their personality and signals membership in chosen communities, developing a personal aesthetic and visual storytelling about who they are.</p>

<h3>Comfort & Function</h3>
<p>Prioritising clothing that supports daily activities, physical comfort, and practical needs. People who lean towards this value focus on weather appropriateness, ease of movement, durable fabrics, and minimising decision fatigue through streamlined wardrobe systems.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each style value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Attractiveness &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Zendaya" target="_blank">Zendaya</a> has become one of the most closely watched figures in contemporary fashion, consistently appearing on best-dressed lists since her early twenties. She works closely with stylist Law Roach to curate looks that reference fashion history while remaining distinctive. Her red carpet appearances regularly generate significant media coverage, and she was the youngest person to receive the CFDA Fashion Icon Award in 2021.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Status & Professional &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Christine_Lagarde" target="_blank">Christine Lagarde</a>, President of the European Central Bank, is widely noted for projecting authority and credibility through her wardrobe choices. She consistently dresses at executive standards across formal, diplomatic, and media settings, demonstrating how strategic clothing choices can reinforce leadership presence at the highest levels.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Self-Expression &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Iris_Apfel" target="_blank">Iris Apfel</a> developed one of the most recognisable personal aesthetics of anyone in the public eye. Her bold, layered style combined vintage, couture, and flea-market finds into a signature look that was entirely her own. She became a style icon in her 80s and remained one into her 100s, demonstrating that distinctive self-expression through clothing can be sustained across a lifetime.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Comfort & Function &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Steve_Jobs" target="_blank">Steve Jobs</a> famously wore the same black turtleneck, jeans, and trainers combination daily, eliminating decision fatigue entirely whilst maintaining a polished, recognisable appearance. His approach demonstrated that a fully systematised wardrobe can simultaneously achieve comfort, consistency, and a distinctive professional image.</p>
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
<h4>Attractiveness</h4>

<div class="assess-input-group" id="ig-fit">
    <span class="assess-label">How well do your most-worn clothes actually fit your body?</span>
    <span class="assess-hint">Check shoulders, chest, waist, and trouser length. Ill-fitting clothes are the single biggest detractor from appearance.</span>
    <select id="a-fit" onchange="handleAssessInput('a-fit')">
        <option value="">Select...</option>
        <option value="poor">Poor &ndash; most items are noticeably too big, too small, or the wrong shape</option>
        <option value="mixed">Mixed &ndash; some fit well, others do not</option>
        <option value="reasonable">Reasonable &ndash; generally fine but not tailored</option>
        <option value="good">Good &ndash; I pay attention to fit and most items suit my body</option>
        <option value="excellent">Excellent &ndash; nearly everything is well-fitted or tailored</option>
    </select> <span class="assess-percentile-hint" id="pct-fit"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-fit" onchange="handleSkip('a-fit')"><label for="skip-fit">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-colours">
    <span class="assess-label">How well do you know which colours suit your skin tone?</span>
    <span class="assess-hint">Hold different coloured tops near your face in natural light. Some will make you look healthier; others will wash you out.</span>
    <select id="a-colours" onchange="handleAssessInput('a-colours')">
        <option value="">Select...</option>
        <option value="no-idea">No idea &ndash; I have never thought about this</option>
        <option value="vague">Vague &ndash; I have a rough sense but have not tested it</option>
        <option value="moderate">Moderate &ndash; I know a few colours that work and a few that do not</option>
        <option value="confident">Confident &ndash; I consistently choose colours that suit me</option>
    </select> <span class="assess-percentile-hint" id="pct-colours"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-colours" onchange="handleSkip('a-colours')"><label for="skip-colours">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-grooming">
    <span class="assess-label">How would you rate your grooming standards?</span>
    <span class="assess-hint">Hair, skin, nails, and overall upkeep. Grooming is often more impactful than clothing choices for overall presentation.</span>
    <select id="a-grooming" onchange="handleAssessInput('a-grooming')">
        <option value="">Select...</option>
        <option value="minimal">Minimal &ndash; basic hygiene only</option>
        <option value="inconsistent">Inconsistent &ndash; sometimes make an effort, often do not</option>
        <option value="moderate">Moderate &ndash; reasonably consistent routine</option>
        <option value="strong">Strong &ndash; daily routine that I maintain reliably</option>
        <option value="meticulous">Meticulous &ndash; comprehensive routine I rarely miss</option>
    </select> <span class="assess-percentile-hint" id="pct-grooming"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-grooming" onchange="handleSkip('a-grooming')"><label for="skip-grooming">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Status &amp; Professional</h4>

<div class="assess-input-group" id="ig-dresscode">
    <span class="assess-label">How well do you understand the dress code expectations in your professional context?</span>
    <span class="assess-hint">Consider what the most respected people in your environment wear, not just the minimum standard.</span>
    <select id="a-dresscode" onchange="handleAssessInput('a-dresscode')">
        <option value="">Select...</option>
        <option value="unaware">Unaware &ndash; I have not thought about it</option>
        <option value="vague">Vague &ndash; I have a rough sense but do not dress to it</option>
        <option value="adequate">Adequate &ndash; I meet the minimum standard</option>
        <option value="good">Good &ndash; I dress appropriately and slightly above the norm</option>
        <option value="strategic">Strategic &ndash; I deliberately dress for professional advantage</option>
    </select> <span class="assess-percentile-hint" id="pct-dresscode"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-dresscode" onchange="handleSkip('a-dresscode')"><label for="skip-dresscode">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-quality">
    <span class="assess-label">Can you tell the difference between well-made and poorly-made clothing?</span>
    <span class="assess-hint">Check stitching, fabric weight, button quality, and how garments hold their shape after washing.</span>
    <select id="a-quality" onchange="handleAssessInput('a-quality')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I cannot tell the difference</option>
        <option value="slightly">Slightly &ndash; I notice obvious extremes</option>
        <option value="moderately">Moderately &ndash; I can spot the main indicators</option>
        <option value="well">Well &ndash; I reliably identify quality differences</option>
        <option value="expert">Expert &ndash; I have a detailed understanding of fabrics, construction, and finishing</option>
    </select> <span class="assess-percentile-hint" id="pct-quality"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-quality" onchange="handleSkip('a-quality')"><label for="skip-quality">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-contexts">
    <span class="assess-label">Do you have appropriate outfits for different professional situations?</span>
    <span class="assess-hint">Think beyond your daily work outfit to meetings, networking events, and presentations where first impressions matter most.</span>
    <select id="a-contexts" onchange="handleAssessInput('a-contexts')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I wear the same thing regardless of context</option>
        <option value="limited">Limited &ndash; I have one or two options but gaps remain</option>
        <option value="adequate">Adequate &ndash; I can dress appropriately for most situations</option>
        <option value="well-covered">Well covered &ndash; I have reliable outfits for all common professional contexts</option>
    </select> <span class="assess-percentile-hint" id="pct-contexts"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-contexts" onchange="handleSkip('a-contexts')"><label for="skip-contexts">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Self-Expression</h4>

<div class="assess-input-group" id="ig-aesthetic">
    <span class="assess-label">Does your clothing reflect your personality?</span>
    <span class="assess-hint">Consider whether someone who knows you well would say your clothes "look like you".</span>
    <select id="a-aesthetic" onchange="handleAssessInput('a-aesthetic')">
        <option value="">Select...</option>
        <option value="autopilot">Autopilot &ndash; I grab whatever is available without thinking</option>
        <option value="functional">Functional &ndash; I dress for practicality, not personality</option>
        <option value="somewhat">Somewhat &ndash; some items reflect me, most are generic</option>
        <option value="mostly">Mostly &ndash; my wardrobe generally reflects who I am</option>
        <option value="strongly">Strongly &ndash; my clothing is a deliberate expression of my identity</option>
    </select> <span class="assess-percentile-hint" id="pct-aesthetic"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-aesthetic" onchange="handleSkip('a-aesthetic')"><label for="skip-aesthetic">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-inspiration">
    <span class="assess-label">Can you name a style or aesthetic direction you are drawn to?</span>
    <span class="assess-hint">This could be a subculture, a colour palette, a level of formality, or a general mood.</span>
    <select id="a-inspiration" onchange="handleAssessInput('a-inspiration')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I have no sense of a style direction</option>
        <option value="vague">Vague &ndash; I know what I like when I see it but cannot describe it</option>
        <option value="emerging">Emerging &ndash; I have a general direction but have not developed it</option>
        <option value="clear">Clear &ndash; I can describe my preferred aesthetic and name influences</option>
    </select> <span class="assess-percentile-hint" id="pct-inspiration"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-inspiration" onchange="handleSkip('a-inspiration')"><label for="skip-inspiration">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-confidence">
    <span class="assess-label">Do you know which outfits make you feel most confident?</span>
    <span class="assess-hint">Think about what you reach for when you want to feel good versus what you default to.</span>
    <select id="a-confidence" onchange="handleAssessInput('a-confidence')">
        <option value="">Select...</option>
        <option value="no">No &ndash; nothing in my wardrobe particularly boosts my confidence</option>
        <option value="vaguely">Vaguely &ndash; I have a sense but have not thought about why</option>
        <option value="yes-few">Yes &ndash; I have a few go-to outfits that make me feel good</option>
        <option value="yes-many">Yes &ndash; most of my wardrobe makes me feel confident</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-confidence" onchange="handleSkip('a-confidence')"><label for="skip-confidence">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Comfort &amp; Function</h4>

<div class="assess-input-group" id="ig-wardrobe-use">
    <span class="assess-label">What percentage of your wardrobe do you actually wear regularly?</span>
    <span class="assess-hint">The average person wears about 44% of their wardrobe. Check whether you have a large number of unworn items.</span>
    <select id="a-wardrobe-use" onchange="handleAssessInput('a-wardrobe-use')">
        <option value="">Select...</option>
        <option value="very-low">Very low &ndash; less than a quarter</option>
        <option value="low">Low &ndash; roughly a quarter to a third</option>
        <option value="average">Average &ndash; about half</option>
        <option value="high">High &ndash; most of my wardrobe gets worn</option>
        <option value="nearly-all">Nearly all &ndash; I wear almost everything I own</option>
    </select> <span class="assess-percentile-hint" id="pct-wardrobe-use"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-wardrobe-use" onchange="handleSkip('a-wardrobe-use')"><label for="skip-wardrobe-use">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-decision-time">
    <span class="assess-label">How long do you spend choosing what to wear each morning?</span>
    <span class="assess-hint">The average is about 17 minutes. Consider whether this feels like a source of stress or friction.</span>
    <select id="a-decision-time" onchange="handleAssessInput('a-decision-time')">
        <option value="">Select...</option>
        <option value="no-thought">No thought &ndash; I grab whatever is to hand</option>
        <option value="under-5">Under 5 minutes &ndash; quick and easy</option>
        <option value="5-15">5 &ndash; 15 minutes &ndash; some consideration</option>
        <option value="15-30">15 &ndash; 30 minutes &ndash; it takes a while</option>
        <option value="over-30">Over 30 minutes &ndash; choosing is a significant daily task</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-decision-time" onchange="handleSkip('a-decision-time')"><label for="skip-decision-time">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-comfort-gaps">
    <span class="assess-label">Do you have recurring comfort issues with your clothing?</span>
    <span class="assess-hint">Items that pinch, ride up, or do not suit the weather. Physical discomfort from clothing affects mood and focus throughout the day.</span>
    <select id="a-comfort-gaps" onchange="handleAssessInput('a-comfort-gaps')">
        <option value="">Select...</option>
        <option value="frequent">Frequent &ndash; I am regularly uncomfortable in my clothes</option>
        <option value="occasional">Occasional &ndash; a few items cause problems</option>
        <option value="rare">Rare &ndash; comfort issues come up now and then</option>
        <option value="none">None &ndash; my clothing is consistently comfortable</option>
    </select> <span class="assess-percentile-hint" id="pct-comfort-gaps"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-comfort-gaps" onchange="handleSkip('a-comfort-gaps')"><label for="skip-comfort-gaps">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-attractiveness">
        <span class="assess-summary-label">Attractiveness</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-attractiveness" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-attractiveness">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-status">
        <span class="assess-summary-label">Status &amp; Professional</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-status" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-status">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-expression">
        <span class="assess-summary-label">Self-Expression</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-expression" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-expression">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-comfort">
        <span class="assess-summary-label">Comfort &amp; Function</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-comfort" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-comfort">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published data on clothing habits, wardrobe usage, and grooming standards. Unscored items (confidence outfits, decision time) are excluded from calculations.</p>
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

<p>You now understand why style matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about attractiveness, status and professional signalling, self-expression, and comfort. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/style/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Style Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Style. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/style/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'style';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-fit', 'a-colours', 'a-grooming',
        'a-dresscode', 'a-quality', 'a-contexts',
        'a-aesthetic', 'a-inspiration', 'a-confidence',
        'a-wardrobe-use', 'a-decision-time', 'a-comfort-gaps'
    ];

    var THRESHOLDS = {
        'a-fit': [
            // ~70% of people wear ill-fitting clothes; well-fitted wardrobe is ~15%
            {v:'poor',p:10},{v:'mixed',p:30},{v:'reasonable',p:50},{v:'good',p:78},{v:'excellent',p:95}
        ],
        'a-colours': [
            // ~60% have never thought about which colours suit them
            {v:'no-idea',p:15},{v:'vague',p:40},{v:'moderate',p:65},{v:'confident',p:90}
        ],
        'a-grooming': [
            // ~15% do minimal grooming; meticulous routine is ~8%
            {v:'minimal',p:10},{v:'inconsistent',p:30},{v:'moderate',p:50},{v:'strong',p:75},{v:'meticulous',p:93}
        ],
        'a-dresscode': [
            // ~30% are unaware of dress code expectations; strategic dressing is ~10%
            {v:'unaware',p:10},{v:'vague',p:30},{v:'adequate',p:50},{v:'good',p:75},{v:'strategic',p:93}
        ],
        'a-quality': [
            // Most people cannot distinguish garment quality beyond obvious extremes
            {v:'no',p:10},{v:'slightly',p:30},{v:'moderately',p:55},{v:'well',p:78},{v:'expert',p:95}
        ],
        'a-contexts': [
            // ~25% wear the same thing regardless; well-covered is ~20%
            {v:'no',p:10},{v:'limited',p:35},{v:'adequate',p:60},{v:'well-covered',p:88}
        ],
        'a-aesthetic': [
            // ~35% dress on autopilot; deliberate self-expression through clothing is ~12%
            {v:'autopilot',p:10},{v:'functional',p:30},{v:'somewhat',p:50},{v:'mostly',p:75},{v:'strongly',p:93}
        ],
        'a-inspiration': [
            // ~45% have no sense of style direction; clear aesthetic with named influences is ~15%
            {v:'no',p:12},{v:'vague',p:38},{v:'emerging',p:65},{v:'clear',p:90}
        ],
        'a-wardrobe-use': [
            // Average person wears ~44% of wardrobe; wearing nearly all is very uncommon
            {v:'very-low',p:10},{v:'low',p:28},{v:'average',p:50},{v:'high',p:75},{v:'nearly-all',p:93}
        ],
        'a-comfort-gaps': [
            // ~40% report regular clothing discomfort; no issues at all is ~20%
            {v:'frequent',p:10},{v:'occasional',p:35},{v:'rare',p:65},{v:'none',p:90}
        ]
    };

    var VALUE_ITEMS = {
        attractiveness: ['a-fit', 'a-colours', 'a-grooming'],
        status: ['a-dresscode', 'a-quality', 'a-contexts'],
        expression: ['a-aesthetic', 'a-inspiration'],
        comfort: ['a-wardrobe-use', 'a-comfort-gaps']
    };

    var UNSCORED_ITEMS = ['a-confidence', 'a-decision-time'];

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
        hintEl.textContent = pct !== null ? '~' + ordinalSuffix(pct) + ' percentile' : '';
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['attractiveness', 'status', 'expression', 'comfort'].forEach(function(vk) {
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
        ['attractiveness', 'status', 'expression', 'comfort'].forEach(function(vk) {
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
