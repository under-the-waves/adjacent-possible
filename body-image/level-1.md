---
layout: default
title: "Body Image – Level 1: Awareness"
life_area_slug: body-image
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

<h1>Body Image: Level 1</h1>

<p class="l1-subtitle">Understand what body image means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Body Image Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why body image matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Body image &ndash; how you perceive, feel about, and present your physical self &ndash; has a measurable effect on wellbeing. Research by <a href="https://doi.org/10.1016/B978-012167053-8/50004-8" target="_blank">Thomas Cash</a> found that roughly a quarter of our self-esteem is determined by how positively we view our bodies.</p>

<p>The effects extend well beyond self-esteem. Body dissatisfaction is a <a href="https://doi.org/10.1037/0022-006X.70.1.103" target="_blank">significant risk factor</a> for eating disorders and is associated with higher levels of depression and anxiety. People with poor body image are more likely to withdraw from social situations, avoid physical activities, and limit intimate relationships.</p>

<p>Conversely, positive body image enhances social confidence and life engagement. People who feel comfortable in their bodies are more willing to try new activities, form relationships, and present themselves authentically. Few aspects of self-perception touch as many areas of daily life.</p>

<p>Body image encompasses body composition, skin health, hair quality, posture, grooming, and body language &ndash; the physical impression you make without clothing considerations. It overlaps with but is distinct from <a href="{{ site.baseurl }}/style/">style</a>, which covers clothing and visual presentation, and <a href="{{ site.baseurl }}/fitness/">fitness</a>, which covers what your body can do.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about body image</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People care about body image for different reasons. This site scores every body image intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Youthfulness & Vitality</h3>
<p>Maintaining or enhancing a youthful, energetic appearance through body condition and grooming. People who lean towards this value focus on skin health, hair quality, posture, and energy levels &ndash; interventions that make them look and feel younger, healthier, and more vibrant over time.</p>

<h3>Romantic Appeal</h3>
<p>Developing physical attractiveness and body language that appeals to potential or current romantic partners. People who lean towards this value focus on body composition, grooming standards, confident movement, and physical presence in romantic contexts.</p>

<h3>Weight Management</h3>
<p>Achieving desired changes in body composition, whether gaining muscle mass, losing body fat, or maintaining current weight. People who lean towards this value focus on reaching specific body composition goals that serve both aesthetic and functional purposes.</p>

<h3>Body Confidence</h3>
<p>Feeling comfortable, at home, and confident in your own body regardless of changes. People who lean towards this value focus on improving their relationship with their body &ndash; body acceptance, posture, confident movement, and reduced body-related anxiety &ndash; rather than necessarily changing it.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each body image value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Youthfulness & Vitality &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Cate_Blanchett" target="_blank">Cate Blanchett</a> has maintained a notably youthful appearance and high energy through her 50s whilst sustaining a demanding career. She is frequently cited for her skin quality, posture, and vitality, and has spoken publicly about prioritising sleep, sun protection, and consistent skincare over cosmetic procedures.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Romantic Appeal &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/David_Beckham" target="_blank">David Beckham</a> has maintained strong physical presence and grooming standards from his 20s into his late 40s, adapting his presentation across decades whilst remaining widely regarded as physically attractive. His attention to body composition, grooming, and confident body language has remained consistent through major life transitions.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Weight Management &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Hugh_Jackman" target="_blank">Hugh Jackman</a> has demonstrated precise body composition control over two decades of film roles, repeatedly transforming his physique for specific demands and returning to a healthy baseline. He has maintained this capacity into his mid-50s, adjusting his approach as he ages.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Body Confidence &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Lizzo" target="_blank">Lizzo</a> has built a career around genuine body acceptance and physical confidence, performing demanding choreography in body-exposing outfits and speaking openly about maintaining positive body image through public scrutiny. Her confidence appears authentic and consistent across contexts.</p>
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
<h4>Youthfulness &amp; Vitality</h4>

<div class="assess-input-group" id="ig-skin-routine">
    <span class="assess-label">Do you have a regular skincare routine?</span>
    <span class="assess-hint">Cleansing, moisturising, sun protection &ndash; or nothing at all. All answers count.</span>
    <select id="a-skin-routine" onchange="handleAssessInput('a-skin-routine')">
        <option value="">Select...</option>
        <option value="none">No routine at all</option>
        <option value="minimal">Minimal &ndash; one or two steps occasionally</option>
        <option value="basic">Basic &ndash; cleanse and moisturise most days</option>
        <option value="consistent">Consistent &ndash; daily routine including sun protection</option>
        <option value="comprehensive">Comprehensive &ndash; dedicated multi-step routine with targeted treatments</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-skin-routine" onchange="handleSkip('a-skin-routine')"><label for="skip-skin-routine">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-energy-levels">
    <span class="assess-label">How would you describe your typical energy levels throughout the day?</span>
    <span class="assess-hint">Think about your energy on a normal day, not an unusually good or bad one.</span>
    <select id="a-energy-levels" onchange="handleAssessInput('a-energy-levels')">
        <option value="">Select...</option>
        <option value="low">Consistently low &ndash; feel tired most of the day</option>
        <option value="variable">Variable &ndash; noticeable crashes or dips</option>
        <option value="moderate">Moderate &ndash; enough energy for daily tasks but not much more</option>
        <option value="good">Good &ndash; feel energetic most of the day</option>
        <option value="excellent">Excellent &ndash; consistently high energy from morning to evening</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-energy-levels" onchange="handleSkip('a-energy-levels')"><label for="skip-energy-levels">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-posture">
    <span class="assess-label">How would you rate your posture?</span>
    <span class="assess-hint">Check in a mirror or ask someone. Do you slouch, round your shoulders, or stand tall?</span>
    <select id="a-posture" onchange="handleAssessInput('a-posture')">
        <option value="">Select...</option>
        <option value="poor">Poor &ndash; noticeably slouched or hunched</option>
        <option value="below-average">Below average &ndash; tend to round shoulders or lean</option>
        <option value="average">Average &ndash; reasonable but not something I think about</option>
        <option value="good">Good &ndash; generally stand and sit upright</option>
        <option value="excellent">Excellent &ndash; consistently tall, open posture</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-posture" onchange="handleSkip('a-posture')"><label for="skip-posture">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Romantic Appeal</h4>

<div class="assess-input-group" id="ig-grooming">
    <span class="assess-label">How consistent is your grooming routine?</span>
    <span class="assess-hint">Hair, facial hair, nails, dental care &ndash; whatever applies to you.</span>
    <select id="a-grooming" onchange="handleAssessInput('a-grooming')">
        <option value="">Select...</option>
        <option value="minimal">Minimal &ndash; basic hygiene only</option>
        <option value="inconsistent">Inconsistent &ndash; sometimes make an effort, often don't</option>
        <option value="moderate">Moderate &ndash; reasonably consistent routine</option>
        <option value="strong">Strong &ndash; daily routine that I maintain reliably</option>
        <option value="meticulous">Meticulous &ndash; comprehensive routine I rarely miss</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-grooming" onchange="handleSkip('a-grooming')"><label for="skip-grooming">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-body-language">
    <span class="assess-label">How would you describe your body language around others?</span>
    <span class="assess-hint">Eye contact, open vs closed posture, how you move in social settings.</span>
    <select id="a-body-language" onchange="handleAssessInput('a-body-language')">
        <option value="">Select...</option>
        <option value="closed">Mostly closed &ndash; avoid eye contact, arms crossed, tense</option>
        <option value="reserved">Reserved &ndash; somewhat guarded but functional</option>
        <option value="neutral">Neutral &ndash; neither notably open nor closed</option>
        <option value="open">Open &ndash; comfortable eye contact, relaxed posture</option>
        <option value="confident">Confident &ndash; naturally open, expressive, and at ease</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-body-language" onchange="handleSkip('a-body-language')"><label for="skip-body-language">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-physical-confidence">
    <span class="assess-label">How comfortable do you feel with physical closeness and touch in romantic contexts?</span>
    <span class="assess-hint">Any honest answer works &ndash; this is about self-awareness, not judgement.</span>
    <select id="a-physical-confidence" onchange="handleAssessInput('a-physical-confidence')">
        <option value="">Select...</option>
        <option value="avoidant">Avoidant &ndash; tend to pull away or feel very uncomfortable</option>
        <option value="anxious">Anxious &ndash; willing but noticeably tense</option>
        <option value="neutral">Neutral &ndash; neither uncomfortable nor fully at ease</option>
        <option value="comfortable">Comfortable &ndash; generally relaxed and natural</option>
        <option value="very-comfortable">Very comfortable &ndash; fully at ease with physical closeness</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-physical-confidence" onchange="handleSkip('a-physical-confidence')"><label for="skip-physical-confidence">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Weight Management</h4>

<div class="assess-input-group" id="ig-body-comp">
    <span class="assess-label">How satisfied are you with your current body composition?</span>
    <span class="assess-hint">You don't need exact numbers &ndash; just your honest sense of where you are relative to where you'd like to be.</span>
    <select id="a-body-comp" onchange="handleAssessInput('a-body-comp')">
        <option value="">Select...</option>
        <option value="very-dissatisfied">Very dissatisfied &ndash; far from where I want to be</option>
        <option value="dissatisfied">Dissatisfied &ndash; noticeably different from my goal</option>
        <option value="neutral">Neutral &ndash; not something I think about much</option>
        <option value="mostly-satisfied">Mostly satisfied &ndash; close to where I'd like to be</option>
        <option value="satisfied">Satisfied &ndash; happy with my current body composition</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-body-comp" onchange="handleSkip('a-body-comp')"><label for="skip-body-comp">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-weight-history">
    <span class="assess-label">How has your weight changed over the past year?</span>
    <span class="assess-hint">A rough sense is fine. Has your weight changed noticeably?</span>
    <select id="a-weight-history" onchange="handleAssessInput('a-weight-history')">
        <option value="">Select...</option>
        <option value="gained-significant">Gained significantly &ndash; noticeable increase</option>
        <option value="gained-some">Gained some &ndash; slight upward trend</option>
        <option value="stable">Stable &ndash; roughly the same</option>
        <option value="lost-some">Lost some &ndash; slight downward trend</option>
        <option value="lost-significant">Lost significantly &ndash; noticeable decrease</option>
        <option value="fluctuating">Fluctuating &ndash; gone up and down repeatedly</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-weight-history" onchange="handleSkip('a-weight-history')"><label for="skip-weight-history">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-food-relationship">
    <span class="assess-label">How would you describe your relationship with food?</span>
    <span class="assess-hint">Do you eat in response to emotions? Feel guilt about food? Eat mindfully? No judgement here.</span>
    <select id="a-food-relationship" onchange="handleAssessInput('a-food-relationship')">
        <option value="">Select...</option>
        <option value="difficult">Difficult &ndash; frequent guilt, emotional eating, or disordered patterns</option>
        <option value="complicated">Complicated &ndash; some unhealthy patterns I'm aware of</option>
        <option value="neutral">Neutral &ndash; don't think about it much either way</option>
        <option value="mostly-healthy">Mostly healthy &ndash; generally mindful with occasional lapses</option>
        <option value="healthy">Healthy &ndash; eat mindfully without guilt or anxiety</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-food-relationship" onchange="handleSkip('a-food-relationship')"><label for="skip-food-relationship">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Body Confidence</h4>

<div class="assess-input-group" id="ig-mirror">
    <span class="assess-label">How do you feel when you look at yourself in the mirror?</span>
    <span class="assess-hint">Think about your honest, unguarded reaction &ndash; not what you think you should feel.</span>
    <select id="a-mirror" onchange="handleAssessInput('a-mirror')">
        <option value="">Select...</option>
        <option value="avoidant">Avoidant &ndash; I try not to look</option>
        <option value="critical">Critical &ndash; I focus on flaws</option>
        <option value="neutral">Neutral &ndash; no strong reaction either way</option>
        <option value="mostly-positive">Mostly positive &ndash; generally pleased with what I see</option>
        <option value="positive">Positive &ndash; I like how I look</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-mirror" onchange="handleSkip('a-mirror')"><label for="skip-mirror">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-clothing-comfort">
    <span class="assess-label">Do you avoid certain clothing or activities because of how your body looks?</span>
    <span class="assess-hint">Swimming, form-fitting clothes, sleeveless tops, photos &ndash; do you avoid any of these?</span>
    <select id="a-clothing-comfort" onchange="handleAssessInput('a-clothing-comfort')">
        <option value="">Select...</option>
        <option value="many">Yes &ndash; I avoid many things because of my body</option>
        <option value="some">Some &ndash; there are a few things I steer away from</option>
        <option value="rarely">Rarely &ndash; occasional self-consciousness but it doesn't stop me</option>
        <option value="no">No &ndash; I wear and do what I want without hesitation</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-clothing-comfort" onchange="handleSkip('a-clothing-comfort')"><label for="skip-clothing-comfort">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-self-talk">
    <span class="assess-label">What is your internal dialogue about your body like?</span>
    <span class="assess-hint">Pay attention to what you say to yourself when getting dressed or catching your reflection.</span>
    <select id="a-self-talk" onchange="handleAssessInput('a-self-talk')">
        <option value="">Select...</option>
        <option value="very-negative">Very negative &ndash; frequent harsh self-criticism</option>
        <option value="mostly-negative">Mostly negative &ndash; tend to focus on what I dislike</option>
        <option value="mixed">Mixed &ndash; some positive, some negative</option>
        <option value="mostly-positive">Mostly positive &ndash; generally kind to myself</option>
        <option value="positive">Positive &ndash; consistently accepting and appreciative</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-self-talk" onchange="handleSkip('a-self-talk')"><label for="skip-self-talk">I know but prefer not to say</label></div>
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

<p>You now understand why body image matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about youthfulness and vitality, romantic appeal, weight management, and body confidence. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/body-image/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Body Image Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Body Image. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/body-image/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'body-image';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-skin-routine', 'a-energy-levels', 'a-posture',
        'a-grooming', 'a-body-language', 'a-physical-confidence',
        'a-body-comp', 'a-weight-history', 'a-food-relationship',
        'a-mirror', 'a-clothing-comfort', 'a-self-talk'
    ];

    // All body image items are qualitative and unscored (no reliable percentile data)
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
        // All body image items are unscored; save null for each value
        var scores = {
            vitality: null,
            romantic: null,
            weight: null,
            confidence: null
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
