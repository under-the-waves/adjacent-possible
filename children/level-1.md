---
layout: default
title: "Children – Level 1: Awareness"
life_area_slug: children
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

<h1>Children: Level 1</h1>

<p class="l1-subtitle">Understand what parenting involves, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Children Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why parenting matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>The parent-child relationship is one of the most consequential human bonds. The quality of this relationship &ndash; not specific parenting techniques &ndash; is what predicts outcomes most strongly.</p>

<p>Cross-cultural research in <a href="https://www.nature.com/articles/s44271-024-00161-x" target="_blank">Communications Psychology (2024)</a> found that higher recalled parent-child relationship quality predicted adult flourishing and current mental health across a diverse group of countries. The foundations for lifelong wellbeing begin in the early years.</p>

<p>Quality of interaction matters more than quantity. Research in the <a href="https://pubmed.ncbi.nlm.nih.gov/37775429/" target="_blank">Journal of Developmental and Behavioral Pediatrics (2023)</a> found that insufficient parent-child quality time is associated with lower flourishing, and specific interactive activities like singing and storytelling drove the strongest outcomes.</p>

<p>Across <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4784487/" target="_blank">more than a thousand studies</a>, greater wellbeing is seen for children with higher combined parental care and lower combined parental psychological control. Warmth, responsiveness, and appropriate boundaries matter far more than any particular parenting method.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about parenting</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach parenting with different priorities. This site scores every parenting intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Wellbeing</h3>
<p>Supporting your child's overall physical, emotional, and psychological health. Creating a stable, nurturing environment, attending to mental health, ensuring adequate sleep and nutrition, and prioritising the child's current happiness alongside future outcomes. People who lean towards this value focus on the child thriving now, not just preparing for later.</p>

<h3>Relationship</h3>
<p>The quality of the parent-child bond &ndash; warmth, trust, communication, and genuine connection. Being emotionally available, enjoying time together, knowing your child's inner life, and building a relationship they want to maintain into adulthood. People who lean towards this value invest in connection as an end in itself.</p>

<h3>Achievement</h3>
<p>Supporting your child's cognitive, academic, and skill development. Structured enrichment, high expectations communicated warmly, and preparation for future success. People who lean towards this value believe parents should actively cultivate capability.</p>

<h3>Development</h3>
<p>Fostering independence, resilience, and character through age-appropriate challenges and progressively expanding autonomy. Allowing risk-taking, supporting self-direction, and building executive function. People who lean towards this value focus on who the child is becoming, not just what they can do.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each parenting value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Wellbeing &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Magda_Gerber" target="_blank">Magda Gerber</a> developed the Resources for Infant Educarers (RIE) approach, built around deep observation and respect for children's emotional states from birth. She raised her own three children using these principles before formalising them into a teaching methodology. Her approach &ndash; treating even very young children as full people whose emotional experiences deserve attention &ndash; produced measurably more secure attachment outcomes in the children of parents she trained, and her methods are now used in early childhood programmes across the world.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Relationship &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Barack_Obama" target="_blank">Barack Obama</a> maintained nightly family dinners throughout his presidency, rarely missing them even during major crises. He has spoken extensively about structuring his schedule around his daughters' school events, sports fixtures, and everyday conversations. Both Sasha and Malia Obama have described their father as deeply present and emotionally available despite the pressures of his role, and the family's closeness has remained visibly strong through their adult years.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Achievement &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/L%C3%A1szl%C3%B3_Polg%C3%A1r" target="_blank">L&aacute;szl&oacute; Polg&aacute;r</a> set out to test his theory that any child could reach exceptional levels in a chosen field with early, deliberate training. He and his wife Klara raised their three daughters &ndash; Susan, Sofia, and Judit &ndash; to become chess prodigies. All three became among the strongest female players in history, with Judit widely regarded as the greatest female chess player of all time. Polg&aacute;r documented his methods and the children's development in detail, and all three daughters have spoken positively about their upbringing.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Development &ndash; Level 5</div>
    <p><a href="https://letgrow.org/about/" target="_blank">Lenore Skenazy</a> became known as "America's worst mom" after writing about letting her nine-year-old son ride the New York subway alone. She went on to found the Let Grow movement, advocating for age-appropriate independence and unsupervised play. Her own children grew up with progressively expanded freedoms &ndash; navigating public transport, managing their own schedules, and solving problems without parental rescue &ndash; and she has documented how this approach built their confidence and self-direction over years.</p>
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
<h4>Wellbeing</h4>

<div class="assess-input-group" id="ig-emotional-climate">
    <span class="assess-label">How safe does your child feel expressing negative emotions at home?</span>
    <span class="assess-hint">Think about how your child behaves when upset, angry, or disappointed. Do they come to you or withdraw?</span>
    <select id="a-emotional-climate" onchange="handleAssessInput('a-emotional-climate')">
        <option value="">Select...</option>
        <option value="withdrawn">Withdrawn &ndash; rarely expresses negative emotions at home</option>
        <option value="cautious">Cautious &ndash; sometimes shares but often holds back</option>
        <option value="mixed">Mixed &ndash; expresses some emotions but suppresses others</option>
        <option value="mostly-open">Mostly open &ndash; generally comes to me when upset</option>
        <option value="fully-open">Fully open &ndash; freely shares both positive and negative feelings</option>
    </select> <span class="assess-percentile-hint" id="pct-emotional-climate"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-emotional-climate" onchange="handleSkip('a-emotional-climate')"><label for="skip-emotional-climate">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-sleep-nutrition">
    <span class="assess-label">Is your child getting adequate sleep and nutrition for their age?</span>
    <span class="assess-hint">Check NHS or WHO guidelines for age-appropriate sleep hours and nutritional needs.</span>
    <select id="a-sleep-nutrition" onchange="handleAssessInput('a-sleep-nutrition')">
        <option value="">Select...</option>
        <option value="poor-both">Poor on both &ndash; inadequate sleep and nutrition</option>
        <option value="poor-one">Poor on one &ndash; sleep or nutrition is lacking</option>
        <option value="adequate">Adequate &ndash; meets minimum guidelines for both</option>
        <option value="good">Good &ndash; consistently meets guidelines</option>
        <option value="excellent">Excellent &ndash; well above guidelines on both</option>
    </select> <span class="assess-percentile-hint" id="pct-sleep-nutrition"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-sleep-nutrition" onchange="handleSkip('a-sleep-nutrition')"><label for="skip-sleep-nutrition">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-stress-signs">
    <span class="assess-label">How well can you identify when your child is stressed or struggling?</span>
    <span class="assess-hint">Common signs include changes in sleep, appetite, withdrawal, irritability, or regression to earlier behaviours.</span>
    <select id="a-stress-signs" onchange="handleAssessInput('a-stress-signs')">
        <option value="">Select...</option>
        <option value="rarely-notice">Rarely notice &ndash; usually surprised when something is wrong</option>
        <option value="sometimes">Sometimes &ndash; pick up on obvious signs but miss subtler ones</option>
        <option value="usually">Usually &ndash; notice most signs within a day or two</option>
        <option value="quickly">Quickly &ndash; tend to spot changes early</option>
        <option value="very-attuned">Very attuned &ndash; pick up on subtle shifts in mood or behaviour promptly</option>
    </select> <span class="assess-percentile-hint" id="pct-stress-signs"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-stress-signs" onchange="handleSkip('a-stress-signs')"><label for="skip-stress-signs">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Relationship</h4>

<div class="assess-input-group" id="ig-quality-time">
    <span class="assess-label">How much genuine one-on-one connection time do you spend with your child in a typical week?</span>
    <span class="assess-hint">Count time spent talking, playing, reading together, or doing shared activities &ndash; not transport, meals in front of screens, or homework supervision.</span>
    <select id="a-quality-time" onchange="handleAssessInput('a-quality-time')">
        <option value="">Select...</option>
        <option value="under-1h">Under 1 hour per week</option>
        <option value="1-3h">1 &ndash; 3 hours per week</option>
        <option value="3-5h">3 &ndash; 5 hours per week</option>
        <option value="5-10h">5 &ndash; 10 hours per week</option>
        <option value="over-10h">Over 10 hours per week</option>
    </select> <span class="assess-percentile-hint" id="pct-quality-time"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-quality-time" onchange="handleSkip('a-quality-time')"><label for="skip-quality-time">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-inner-life">
    <span class="assess-label">How well do you know your child's inner life?</span>
    <span class="assess-hint">Could you name your child's current best friend, their biggest worry, and something they are looking forward to?</span>
    <select id="a-inner-life" onchange="handleAssessInput('a-inner-life')">
        <option value="">Select...</option>
        <option value="very-little">Very little &ndash; would struggle to answer any of those</option>
        <option value="some">Some &ndash; know one or two but not all three</option>
        <option value="reasonable">Reasonable &ndash; could answer most with some thought</option>
        <option value="well">Well &ndash; could answer all three confidently</option>
        <option value="deeply">Deeply &ndash; know far more than the basics about their worries, joys, and friendships</option>
    </select> <span class="assess-percentile-hint" id="pct-inner-life"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-inner-life" onchange="handleSkip('a-inner-life')"><label for="skip-inner-life">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-seeks-comfort">
    <span class="assess-label">When your child is upset, who do they go to first?</span>
    <span class="assess-hint">Think about the last time your child was upset. Did they come to you first, go to another adult, or handle it alone?</span>
    <select id="a-seeks-comfort" onchange="handleAssessInput('a-seeks-comfort')">
        <option value="">Select...</option>
        <option value="avoids-all">Avoids everyone &ndash; deals with it alone or shuts down</option>
        <option value="others-first">Others first &ndash; goes to another adult, sibling, or friend</option>
        <option value="depends">Depends &ndash; sometimes me, sometimes others</option>
        <option value="usually-me">Usually me &ndash; I am their first port of call most of the time</option>
        <option value="always-me">Always me &ndash; consistently seeks me out for comfort and conversation</option>
    </select> <span class="assess-percentile-hint" id="pct-seeks-comfort"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-seeks-comfort" onchange="handleSkip('a-seeks-comfort')"><label for="skip-seeks-comfort">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Achievement</h4>

<div class="assess-input-group" id="ig-academic-level">
    <span class="assess-label">Where does your child stand relative to age expectations in their main academic or skill areas?</span>
    <span class="assess-hint">This might come from school reports, teacher conversations, or your own observation of their reading, writing, and numeracy.</span>
    <select id="a-academic-level" onchange="handleAssessInput('a-academic-level')">
        <option value="">Select...</option>
        <option value="well-behind">Well behind &ndash; significantly below age expectations</option>
        <option value="slightly-behind">Slightly behind &ndash; a little below in some areas</option>
        <option value="at-level">At level &ndash; meeting age expectations</option>
        <option value="above">Above &ndash; ahead in one or more areas</option>
        <option value="well-above">Well above &ndash; significantly ahead across most areas</option>
    </select> <span class="assess-percentile-hint" id="pct-academic-level"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-academic-level" onchange="handleSkip('a-academic-level')"><label for="skip-academic-level">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-enrichment">
    <span class="assess-label">Does your child have regular structured enrichment beyond school?</span>
    <span class="assess-hint">Count activities you do together (reading, puzzles, projects) as well as formal clubs or tutoring.</span>
    <select id="a-enrichment" onchange="handleAssessInput('a-enrichment')">
        <option value="">Select...</option>
        <option value="none">None &ndash; no regular enrichment activities</option>
        <option value="occasional">Occasional &ndash; something now and then but nothing consistent</option>
        <option value="one-regular">One regular &ndash; one consistent activity or habit</option>
        <option value="several">Several &ndash; two or three regular enrichment activities</option>
        <option value="extensive">Extensive &ndash; a well-rounded programme of enrichment</option>
    </select> <span class="assess-percentile-hint" id="pct-enrichment"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-enrichment" onchange="handleSkip('a-enrichment')"><label for="skip-enrichment">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-strengths-gaps">
    <span class="assess-label">Can you identify your child's strengths and gaps relative to peers?</span>
    <span class="assess-hint">Think about academic subjects, social skills, motor skills, or practical capabilities.</span>
    <select id="a-strengths-gaps" onchange="handleAssessInput('a-strengths-gaps')">
        <option value="">Select...</option>
        <option value="no-idea">No idea &ndash; have not thought about this</option>
        <option value="vague">Vague sense &ndash; could guess but not confidently</option>
        <option value="know-strengths">Know strengths &ndash; clear on what they are good at but less sure about gaps</option>
        <option value="know-both">Know both &ndash; can name at least one strength and one area for support</option>
        <option value="detailed">Detailed picture &ndash; clear understanding of multiple strengths and gaps</option>
    </select> <span class="assess-percentile-hint" id="pct-strengths-gaps"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-strengths-gaps" onchange="handleSkip('a-strengths-gaps')"><label for="skip-strengths-gaps">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Development</h4>

<div class="assess-input-group" id="ig-independence">
    <span class="assess-label">How much independent decision-making does your child exercise daily?</span>
    <span class="assess-hint">Consider how many of your child's daily decisions &ndash; what to wear, what to eat, how to spend free time &ndash; they actually make themselves.</span>
    <select id="a-independence" onchange="handleAssessInput('a-independence')">
        <option value="">Select...</option>
        <option value="very-little">Very little &ndash; I direct most of their choices</option>
        <option value="some">Some &ndash; they choose a few things but I guide most</option>
        <option value="moderate">Moderate &ndash; roughly balanced between their choices and mine</option>
        <option value="substantial">Substantial &ndash; they make most daily decisions themselves</option>
        <option value="high">High &ndash; they are largely self-directing with me as a safety net</option>
    </select> <span class="assess-percentile-hint" id="pct-independence"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-independence" onchange="handleSkip('a-independence')"><label for="skip-independence">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-consequences">
    <span class="assess-label">Does your child experience natural consequences for their choices?</span>
    <span class="assess-hint">Think about the last time your child forgot something or made a poor choice. Did you rescue them or let them deal with it?</span>
    <select id="a-consequences" onchange="handleAssessInput('a-consequences')">
        <option value="">Select...</option>
        <option value="always-rescue">Always rescue &ndash; I step in before consequences land</option>
        <option value="usually-rescue">Usually rescue &ndash; tend to fix things most of the time</option>
        <option value="mixed">Mixed &ndash; sometimes let consequences play out, sometimes intervene</option>
        <option value="usually-allow">Usually allow &ndash; let them experience consequences with occasional support</option>
        <option value="consistently-allow">Consistently allow &ndash; let natural consequences land unless safety is at risk</option>
    </select> <span class="assess-percentile-hint" id="pct-consequences"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-consequences" onchange="handleSkip('a-consequences')"><label for="skip-consequences">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-self-direction">
    <span class="assess-label">How self-directed is your child compared to their peers?</span>
    <span class="assess-hint">Does your child start projects or activities independently, or do they wait for you to organise their time?</span>
    <select id="a-self-direction" onchange="handleAssessInput('a-self-direction')">
        <option value="">Select...</option>
        <option value="very-dependent">Very dependent &ndash; waits for me to organise almost everything</option>
        <option value="mostly-dependent">Mostly dependent &ndash; needs prompting for most activities</option>
        <option value="average">Average &ndash; initiates some things but needs prompting for others</option>
        <option value="mostly-independent">Mostly independent &ndash; starts most activities on their own</option>
        <option value="highly-independent">Highly independent &ndash; consistently self-starting and self-sustaining</option>
    </select> <span class="assess-percentile-hint" id="pct-self-direction"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-self-direction" onchange="handleSkip('a-self-direction')"><label for="skip-self-direction">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-wellbeing">
        <span class="assess-summary-label">Wellbeing</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-wellbeing" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-wellbeing">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-relationship">
        <span class="assess-summary-label">Relationship</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-relationship" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-relationship">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-achievement">
        <span class="assess-summary-label">Achievement</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-achievement" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-achievement">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-development">
        <span class="assess-summary-label">Development</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-development" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-development">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published research on parenting behaviours and child development. All items in this area are scored.</p>
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

<p>You now understand why parenting matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about wellbeing, relationship, achievement, and development. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/children/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Children Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Children. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/children/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'children';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-emotional-climate', 'a-sleep-nutrition', 'a-stress-signs',
        'a-quality-time', 'a-inner-life', 'a-seeks-comfort',
        'a-academic-level', 'a-enrichment', 'a-strengths-gaps',
        'a-independence', 'a-consequences', 'a-self-direction'
    ];

    var UNSCORED_ITEMS = [];

    var THRESHOLDS = {
        'a-emotional-climate': [
            {v:'withdrawn',p:10},{v:'cautious',p:25},{v:'mixed',p:50},{v:'mostly-open',p:72},{v:'fully-open',p:92}
        ],
        'a-sleep-nutrition': [
            {v:'poor-both',p:8},{v:'poor-one',p:25},{v:'adequate',p:50},{v:'good',p:75},{v:'excellent',p:93}
        ],
        'a-stress-signs': [
            {v:'rarely-notice',p:12},{v:'sometimes',p:35},{v:'usually',p:58},{v:'quickly',p:78},{v:'very-attuned',p:94}
        ],
        'a-quality-time': [
            {v:'under-1h',p:8},{v:'1-3h',p:25},{v:'3-5h',p:50},{v:'5-10h',p:75},{v:'over-10h',p:93}
        ],
        'a-inner-life': [
            {v:'very-little',p:8},{v:'some',p:25},{v:'reasonable',p:50},{v:'well',p:75},{v:'deeply',p:93}
        ],
        'a-seeks-comfort': [
            {v:'avoids-all',p:8},{v:'others-first',p:22},{v:'depends',p:45},{v:'usually-me',p:72},{v:'always-me',p:92}
        ],
        'a-academic-level': [
            {v:'well-behind',p:8},{v:'slightly-behind',p:25},{v:'at-level',p:50},{v:'above',p:75},{v:'well-above',p:93}
        ],
        'a-enrichment': [
            {v:'none',p:12},{v:'occasional',p:30},{v:'one-regular',p:50},{v:'several',p:75},{v:'extensive',p:93}
        ],
        'a-strengths-gaps': [
            {v:'no-idea',p:8},{v:'vague',p:25},{v:'know-strengths',p:50},{v:'know-both',p:75},{v:'detailed',p:93}
        ],
        'a-independence': [
            {v:'very-little',p:10},{v:'some',p:30},{v:'moderate',p:50},{v:'substantial',p:75},{v:'high',p:93}
        ],
        'a-consequences': [
            {v:'always-rescue',p:8},{v:'usually-rescue',p:25},{v:'mixed',p:50},{v:'usually-allow',p:78},{v:'consistently-allow',p:94}
        ],
        'a-self-direction': [
            {v:'very-dependent',p:8},{v:'mostly-dependent',p:25},{v:'average',p:50},{v:'mostly-independent',p:75},{v:'highly-independent',p:93}
        ],
    };

    var VALUE_ITEMS = {
        wellbeing: ['a-emotional-climate', 'a-sleep-nutrition', 'a-stress-signs'],
        relationship: ['a-quality-time', 'a-inner-life', 'a-seeks-comfort'],
        achievement: ['a-academic-level', 'a-enrichment', 'a-strengths-gaps'],
        development: ['a-independence', 'a-consequences', 'a-self-direction'],
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
        ['wellbeing', 'relationship', 'achievement', 'development'].forEach(function(vk) {
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
        ['wellbeing', 'relationship', 'achievement', 'development'].forEach(function(vk) {
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
