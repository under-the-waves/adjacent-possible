---
layout: default
title: "Family of Origin – Level 1: Awareness"
life_area_slug: family-of-origin
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

<h1>Family of Origin: Level 1</h1>

<p class="l1-subtitle">Understand what family of origin means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Family of Origin Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why family of origin matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your family of origin &ndash; the people who raised you and your siblings &ndash; shaped your earliest understanding of relationships, conflict, and emotional safety. These patterns do not disappear in adulthood. Research consistently shows that the quality of parent-child relationships predicts <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5954612/" target="_blank">relationship satisfaction, conflict resolution skills, and emotional regulation</a> in adult partnerships.</p>

<p>Family relationship problems are the <a href="https://www.mentalhealth.org.uk/explore-mental-health/statistics/relationships-community-statistics" target="_blank">single biggest presenting issue</a> in child and adolescent mental health services, and their effects persist well into adulthood. Adults who have unresolved family difficulties report higher rates of depression, anxiety, and difficulty forming secure attachments in other relationships.</p>

<p>These relationships also provide ongoing practical support. Research shows that <a href="https://www.pewresearch.org/social-trends/2013/01/30/financial-support-across-generations/" target="_blank">75% of people</a> believe adult children have a responsibility to provide financial support to ageing parents, while 23% of adults are in the "sandwich generation" &ndash; providing support to both ageing parents and their own children simultaneously.</p>

<p>The dynamics are complex because you did not choose these people, they knew you before you developed your adult identity, and the relationships carry decades of history. Even small improvements in how you navigate family of origin relationships tend to produce outsized benefits across other areas of your life.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about family of origin</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach family of origin relationships for different reasons. This site scores every family of origin intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Personal Autonomy</h3>
<p>Being true to yourself and setting limits that protect your wellbeing, even when this creates family conflict or guilt. People who lean towards this value focus on establishing healthy boundaries, making life choices based on their own values rather than family expectations, and refusing to participate in dysfunctional family patterns.</p>

<h3>Emotional Connection</h3>
<p>Maintaining close emotional bonds and investing significant time and energy in family relationships. People who lean towards this value focus on regular communication, being present for important family events, creating shared experiences, and preserving the emotional intimacy that comes from deep family ties.</p>

<h3>Active Healing</h3>
<p>Working through family dysfunction, addressing past trauma, and pushing for healthier dynamics rather than accepting problematic patterns for the sake of peace. People who lean towards this value are willing to have difficult conversations, seek therapy or family counselling, and challenge generational patterns even when this creates temporary instability.</p>

<h3>Family Duty</h3>
<p>Fulfilling obligations to family members, providing concrete support, and meeting cultural or family expectations about your role. People who lean towards this value focus on financial support for ageing parents, helping siblings, maintaining family traditions, and making life choices that honour family values.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each family of origin value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Personal Autonomy &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Tara_Westover" target="_blank">Tara Westover</a> grew up in a survivalist family in rural Idaho with no formal schooling, facing intense pressure to conform to her family's beliefs and way of life. She taught herself enough to gain university admission at 17, eventually earning a PhD from Cambridge. She maintained her own values and identity despite sustained family opposition, estrangement, and attempts to pull her back, documenting the process in her memoir <em>Educated</em>.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Emotional Connection &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Andre_Agassi" target="_blank">Andre Agassi</a> grew up under a domineering father who pushed him relentlessly into professional tennis from early childhood. In his memoir <em>Open</em>, he described years of resentment and emotional distance. As an adult, he gradually rebuilt the relationship on his own terms, eventually developing genuine closeness with his father while setting clear boundaries. He has spoken about the process as one of the most meaningful things he has done outside of tennis.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Active Healing &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Edith_Eger" target="_blank">Edith Eger</a> survived Auschwitz as a teenager, losing both parents in the Holocaust. She spent decades working through the trauma of her family's destruction, eventually becoming a clinical psychologist specialising in trauma recovery. In her 90s, she published <em>The Choice</em>, describing how she transformed her relationship with her family's history from one of paralysing grief into a source of meaning and purpose. She continued treating patients past the age of 90.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Family Duty &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Malala_Yousafzai" target="_blank">Ziauddin Yousafzai</a>, Malala's father, dedicated his career to providing educational opportunities in Pakistan's Swat Valley, founding schools despite Taliban threats. He publicly championed his daughter's right to education at great personal risk, and after the family was forced into exile, he continued working to support extended family members in Pakistan while building a foundation to educate girls worldwide. His approach to family duty extended from immediate care for his children to sustained support across generations.</p>
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
<h4>Personal Autonomy</h4>

<div class="assess-input-group" id="ig-boundary-awareness">
    <span class="assess-label">How often do you compromise your own values or wellbeing to avoid family conflict?</span>
    <span class="assess-hint">Think about decisions you make differently when family members are involved versus when they are not.</span>
    <select id="a-boundary-awareness" onchange="handleAssessInput('a-boundary-awareness')">
        <option value="">Select...</option>
        <option value="frequently">Frequently &ndash; I regularly go against my own judgement to keep the peace</option>
        <option value="sometimes">Sometimes &ndash; in certain areas I defer to family even when I disagree</option>
        <option value="rarely">Rarely &ndash; I mostly make my own choices but avoid a few topics</option>
        <option value="almost-never">Almost never &ndash; I make decisions based on my own values</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-boundary-awareness" onchange="handleSkip('a-boundary-awareness')"><label for="skip-boundary-awareness">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-guilt-patterns">
    <span class="assess-label">How strongly does guilt affect your decisions when your family disapproves?</span>
    <span class="assess-hint">Consider recent decisions about career, relationships, lifestyle, or how you spend your time.</span>
    <select id="a-guilt-patterns" onchange="handleAssessInput('a-guilt-patterns')">
        <option value="">Select...</option>
        <option value="dominant">Dominant &ndash; guilt frequently overrides what I actually want</option>
        <option value="significant">Significant &ndash; I feel strong guilt and it often sways me</option>
        <option value="moderate">Moderate &ndash; I feel guilt but can usually act on my own judgement</option>
        <option value="mild">Mild &ndash; some discomfort but it does not change my decisions</option>
        <option value="minimal">Minimal &ndash; I can make independent choices without significant guilt</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-guilt-patterns" onchange="handleSkip('a-guilt-patterns')"><label for="skip-guilt-patterns">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-family-expectations">
    <span class="assess-label">How clearly can you name the expectations your family has of you that differ from your own?</span>
    <span class="assess-hint">Career path, living location, relationship choices, religious or cultural practices, how often you visit.</span>
    <select id="a-family-expectations" onchange="handleAssessInput('a-family-expectations')">
        <option value="">Select...</option>
        <option value="unclear">Unclear &ndash; I have not thought about this</option>
        <option value="vague">Vague &ndash; I sense tension but cannot pinpoint the specifics</option>
        <option value="partial">Partial &ndash; I can name some expectations but not all</option>
        <option value="clear">Clear &ndash; I can name the main areas of divergence</option>
        <option value="none">Not applicable &ndash; my family's expectations align with my own</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-family-expectations" onchange="handleSkip('a-family-expectations')"><label for="skip-family-expectations">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Emotional Connection</h4>

<div class="assess-input-group" id="ig-contact-frequency">
    <span class="assess-label">How often do you have meaningful contact with each family member?</span>
    <span class="assess-hint">Think about each parent and sibling separately. "Meaningful" means enough time to talk about how you are both actually doing.</span>
    <select id="a-contact-frequency" onchange="handleAssessInput('a-contact-frequency')">
        <option value="">Select...</option>
        <option value="rarely">Rarely &ndash; meaningful contact happens a few times a year at most</option>
        <option value="monthly">Monthly &ndash; roughly once a month with most family members</option>
        <option value="fortnightly">Fortnightly &ndash; every couple of weeks with key family members</option>
        <option value="weekly">Weekly &ndash; regular meaningful contact with most family members</option>
        <option value="daily">Daily &ndash; frequent meaningful contact with close family</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-contact-frequency" onchange="handleSkip('a-contact-frequency')"><label for="skip-contact-frequency">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-emotional-safety">
    <span class="assess-label">How many family members do you feel emotionally safe with?</span>
    <span class="assess-hint">Emotional safety means being able to share difficulties without being judged, dismissed, or having it used against you later.</span>
    <select id="a-emotional-safety" onchange="handleAssessInput('a-emotional-safety')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I do not feel safe being vulnerable with any family member</option>
        <option value="one">One &ndash; there is one person I can be open with</option>
        <option value="a-few">A few &ndash; I have two or three family members I trust emotionally</option>
        <option value="most">Most &ndash; I feel safe with the majority of my family</option>
        <option value="all">All &ndash; I feel emotionally safe with everyone in my family</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-emotional-safety" onchange="handleSkip('a-emotional-safety')"><label for="skip-emotional-safety">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-family-gatherings">
    <span class="assess-label">How do you feel about family gatherings?</span>
    <span class="assess-hint">Think about how you feel in the days leading up to a family visit or holiday.</span>
    <select id="a-family-gatherings" onchange="handleAssessInput('a-family-gatherings')">
        <option value="">Select...</option>
        <option value="dread">Dread &ndash; I feel anxious or want to avoid them</option>
        <option value="reluctant">Reluctant &ndash; I go but would rather not</option>
        <option value="neutral">Neutral &ndash; neither positive nor negative</option>
        <option value="mostly-positive">Mostly positive &ndash; I generally enjoy them with some reservations</option>
        <option value="look-forward">Look forward &ndash; I genuinely enjoy family gatherings</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-family-gatherings" onchange="handleSkip('a-family-gatherings')"><label for="skip-family-gatherings">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Active Healing</h4>

<div class="assess-input-group" id="ig-unresolved-issues">
    <span class="assess-label">How well can you identify the main unresolved issues in your family?</span>
    <span class="assess-hint">Past events, ongoing resentments, topics that are off-limits, patterns that repeat across years.</span>
    <select id="a-unresolved-issues" onchange="handleAssessInput('a-unresolved-issues')">
        <option value="">Select...</option>
        <option value="unaware">Unaware &ndash; I have not thought about this</option>
        <option value="vague">Vague &ndash; I sense tension but cannot name the issues</option>
        <option value="partial">Partial &ndash; I can name some but suspect there are others</option>
        <option value="clear">Clear &ndash; I have a good understanding of the unresolved dynamics</option>
        <option value="none">Not applicable &ndash; there are no significant unresolved issues</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-unresolved-issues" onchange="handleSkip('a-unresolved-issues')"><label for="skip-unresolved-issues">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-generational-patterns">
    <span class="assess-label">Are you repeating any patterns from your family of origin in your own relationships?</span>
    <span class="assess-hint">Communication habits, conflict styles, emotional avoidance, controlling behaviour, people-pleasing.</span>
    <select id="a-generational-patterns" onchange="handleAssessInput('a-generational-patterns')">
        <option value="">Select...</option>
        <option value="unaware">Unaware &ndash; I have not considered this</option>
        <option value="possibly">Possibly &ndash; I suspect I might be but am not sure which patterns</option>
        <option value="yes-some">Yes &ndash; I can identify some patterns I am repeating</option>
        <option value="yes-working">Yes &ndash; I know the patterns and am actively working on them</option>
        <option value="resolved">Resolved &ndash; I have identified and addressed the main patterns</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-generational-patterns" onchange="handleSkip('a-generational-patterns')"><label for="skip-generational-patterns">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-professional-help">
    <span class="assess-label">Have you sought professional help for family-related issues?</span>
    <span class="assess-hint">Therapy, counselling, family mediation, or structured programmes for family dynamics.</span>
    <select id="a-professional-help" onchange="handleAssessInput('a-professional-help')">
        <option value="">Select...</option>
        <option value="no-not-needed">No &ndash; and I do not think I need to</option>
        <option value="no-might-help">No &ndash; but I think it might help</option>
        <option value="considered">Considered &ndash; I have thought about it but not acted</option>
        <option value="tried">Yes &ndash; I have tried it in the past</option>
        <option value="ongoing">Yes &ndash; I am currently working with a professional</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-professional-help" onchange="handleSkip('a-professional-help')"><label for="skip-professional-help">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Family Duty</h4>

<div class="assess-input-group" id="ig-current-support">
    <span class="assess-label">How clear are you on the support you provide to and receive from family members?</span>
    <span class="assess-hint">Money, time, childcare, eldercare, emotional availability, advice, housing.</span>
    <select id="a-current-support" onchange="handleAssessInput('a-current-support')">
        <option value="">Select...</option>
        <option value="unclear">Unclear &ndash; I have not mapped this out</option>
        <option value="vague">Vague &ndash; I have a rough sense but no clear picture</option>
        <option value="partial">Partial &ndash; I know the main flows but may be missing some</option>
        <option value="clear">Clear &ndash; I have a detailed understanding of support in both directions</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-current-support" onchange="handleSkip('a-current-support')"><label for="skip-current-support">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-future-obligations">
    <span class="assess-label">How much have you thought about your family obligations in 5 &ndash; 10 years?</span>
    <span class="assess-hint">Caregiving, financial support, living arrangements, coordination with siblings as parents age.</span>
    <select id="a-future-obligations" onchange="handleAssessInput('a-future-obligations')">
        <option value="">Select...</option>
        <option value="not-at-all">Not at all &ndash; I have not considered this</option>
        <option value="briefly">Briefly &ndash; I have thought about it in passing</option>
        <option value="somewhat">Somewhat &ndash; I have a general sense of what may be needed</option>
        <option value="seriously">Seriously &ndash; I have thought through specific scenarios</option>
        <option value="planned">Planned &ndash; I have discussed and planned with family members</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-future-obligations" onchange="handleSkip('a-future-obligations')"><label for="skip-future-obligations">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-traditions">
    <span class="assess-label">Do you know which family traditions you want to maintain versus those you keep out of obligation?</span>
    <span class="assess-hint">Holidays, religious observances, regular visits, family rituals, communication norms.</span>
    <select id="a-traditions" onchange="handleAssessInput('a-traditions')">
        <option value="">Select...</option>
        <option value="unclear">Unclear &ndash; I have not distinguished between the two</option>
        <option value="vague">Vague &ndash; I have a general sense but have not examined it closely</option>
        <option value="mostly-clear">Mostly clear &ndash; I know for most traditions whether I value them or not</option>
        <option value="clear">Clear &ndash; I have a deliberate view on which traditions serve me</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-traditions" onchange="handleSkip('a-traditions')"><label for="skip-traditions">I know but prefer not to say</label></div>
</div>
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

<p>You now understand why family of origin matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about personal autonomy, emotional connection, active healing, and family duty. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/family-of-origin/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Family of Origin Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Family of Origin. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/family-of-origin/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'family-of-origin';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-boundary-awareness', 'a-guilt-patterns', 'a-family-expectations',
        'a-contact-frequency', 'a-emotional-safety', 'a-family-gatherings',
        'a-unresolved-issues', 'a-generational-patterns', 'a-professional-help',
        'a-current-support', 'a-future-obligations', 'a-traditions'
    ];

    // All family-of-origin items are qualitative and unscored (no reliable percentile data)
    var UNSCORED_ITEMS = ASSESS_IDS.slice();

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
        // All family-of-origin items are unscored; save null for each value
        var scores = {
            autonomy: null,
            connection: null,
            healing: null,
            duty: null
        };
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-scores') || {};
            all[AREA] = scores;
            APStorage.save('ap-level1-scores', all);
        }
    }

    // --- Event handlers ---

    window.handleAssessInput = function(itemId) {
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessRecorded();
        updateAssessCompletion();
    };

    window.handleSkip = function(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        var input = document.getElementById(itemId);
        if (skipBox && input) {
            input.disabled = skipBox.checked;
            if (skipBox.checked && input.tagName === 'SELECT') input.value = '';
        }
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessRecorded();
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

            updateInputGroupState(id);
        });

        updateAssessRecorded();
        updateAssessCompletion();
    }

    document.addEventListener('DOMContentLoaded', function() {
        restoreAssessment();
        updateUI();
    });
})();
</script>
