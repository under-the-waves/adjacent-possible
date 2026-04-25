---
layout: default
title: "Health Management – Level 1: Awareness"
life_area_slug: health-management
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
.assess-input-group input[type="number"] {
    width: 100px;
    padding: 6px 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 0.95em;
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

<h1>Health Management: Level 1</h1>

<p class="l1-subtitle">Understand what health management means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Health Management Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why health management matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>How you manage your health &ndash; the decisions you make about prevention, screening, providers, and medical care &ndash; has an outsized effect on your long-term outcomes. The evidence is clear: proactive health management leads to substantially better results than reacting to problems as they arise.</p>

<p>Patients who actively engage with their healthcare experience <a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2012.1061" target="_blank">15 &ndash; 25% better outcomes</a> across chronic conditions, along with lower overall healthcare costs. Yet only <a href="https://www.cdc.gov/mmwr/volumes/68/wr/mm6840a2.htm" target="_blank">8% of Americans</a> receive all recommended preventive services. The gap between what is available and what most people actually do is enormous.</p>

<p>Effective health management extends well beyond annual checkups. It includes understanding your personal risk factors, building relationships with providers who know your history, coordinating care when you need multiple specialists, and creating systems that keep you on track without constant effort. People who develop these capabilities <a href="https://www.commonwealthfund.org/publications/issue-briefs/2019/jan/economic-case-us-foundation-high-performance-health-system" target="_blank">report less health-related stress</a> and catch problems earlier, when treatment is simpler and more effective.</p>

<p>Few investments compound as reliably as learning to manage your own health well. The skills and systems you build now pay dividends for decades.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about health management</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach health management for different reasons. This site scores every health management intervention across four core values. Later, you'll set your own weighting across these values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Long-term Health</h3>
<p>Disease prevention, longevity optimisation, and maintaining physical and cognitive function throughout life. People who lean towards this value invest time and resources in comprehensive preventive care, understanding genetic risks, and implementing evidence-based interventions for healthy ageing.</p>

<h3>Present Vitality</h3>
<p>Immediate energy, cognitive function, and daily wellbeing through optimised health practices. People who lean towards this value focus on addressing symptoms that affect quality of life and ensuring their health decisions support current life goals and activities.</p>

<h3>Personal Control</h3>
<p>The knowledge, skills, and confidence to make informed health decisions and advocate effectively within healthcare systems. People who lean towards this value want to be active participants in their healthcare &ndash; understanding medical information, building productive relationships with providers, and taking ownership of health outcomes.</p>

<h3>Simplicity</h3>
<p>Efficient, low-maintenance systems that deliver good health outcomes without consuming excessive time or mental energy. People who lean towards this value seek streamlined approaches to preventive care, clear protocols for common health issues, and automated systems that integrate seamlessly with their lifestyle.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each health management value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Long-term Health &ndash; Level 5</div>
    <p><a href="https://peterattiamd.com/about/" target="_blank">Peter Attia</a> is a physician who structures his entire life around longevity optimisation. He undergoes quarterly blood panels, annual full-body MRI and DEXA scans, continuous glucose monitoring, and regular cardiovascular stress testing. He has spoken publicly about adjusting his exercise, nutrition, and sleep protocols based on biomarker trends tracked over more than a decade. His practice centres on what he calls "Medicine 3.0" &ndash; a preventive approach that aims to extend healthspan.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Present Vitality &ndash; Level 5</div>
    <p><a href="https://www.foundmyfitness.com/about" target="_blank">Rhonda Patrick</a> holds a PhD in biomedical science and applies detailed self-experimentation to optimise her daily energy and cognitive performance. She has documented her use of sauna protocols, cold exposure, micronutrient tracking, and time-restricted eating, adjusting each based on how they affect her day-to-day function. She appears to maintain consistently high output across research, public communication, and parenting.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Personal Control &ndash; Level 5</div>
    <p><a href="https://epatientdave.com/about-dave/" target="_blank">Dave deBronkart</a> ("e-Patient Dave") was diagnosed with stage IV kidney cancer in 2007. He researched his condition extensively, identified a clinical trial through an online patient community, and worked with his oncologists to secure access to a treatment that contributed to his full remission. He went on to co-found the Society for Participatory Medicine and has <a href="https://www.bmj.com/content/346/bmj.f1990" target="_blank">published in the BMJ</a> on patient engagement.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Simplicity &ndash; Level 5</div>
    <p><a href="https://www.atulawande.org/" target="_blank">Atul Gawande</a> is a surgeon and public health researcher whose work focuses on making complex healthcare processes more reliable and efficient. His <a href="https://www.nejm.org/doi/full/10.1056/NEJMsa0810119" target="_blank">surgical checklist research</a> reduced post-operative deaths by 47% across eight hospitals. He applies systems-level thinking to his own health management and has written extensively about building simple, effective protocols for complex problems.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to look up or check.</p>

<div class="assess-group">
<h4>Long-term Health</h4>

<div class="assess-input-group" id="ig-last-checkup">
    <span class="assess-label">When did you last have a general health checkup or physical examination?</span>
    <span class="assess-hint">Include any visit where a doctor reviewed your overall health, not just a specific complaint.</span>
    <select id="a-last-checkup" onchange="handleAssessInput('a-last-checkup')">
        <option value="">Select...</option>
        <option value="0">More than 5 years ago or never</option>
        <option value="1">3 &ndash; 5 years ago</option>
        <option value="2">1 &ndash; 3 years ago</option>
        <option value="3">Within the last year</option>
        <option value="4">Within the last 6 months</option>
    </select> <span class="assess-percentile-hint" id="pct-last-checkup"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-last-checkup" onchange="handleSkip('a-last-checkup')"><label for="skip-last-checkup">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-screenings">
    <span class="assess-label">How up to date are you on recommended preventive screenings for your age and sex?</span>
    <span class="assess-hint">Common examples: blood pressure, cholesterol, blood glucose, cancer screenings, dental checkups.</span>
    <select id="a-screenings" onchange="handleAssessInput('a-screenings')">
        <option value="">Select...</option>
        <option value="0">I don't know which screenings are recommended for me</option>
        <option value="1">I know what's recommended but I'm overdue on most</option>
        <option value="2">I'm up to date on some but not all</option>
        <option value="3">I'm up to date on most recommended screenings</option>
        <option value="4">I'm fully up to date on all recommended screenings</option>
    </select> <span class="assess-percentile-hint" id="pct-screenings"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-screenings" onchange="handleSkip('a-screenings')"><label for="skip-screenings">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-family-history">
    <span class="assess-label">How well do you know your family's major health history?</span>
    <span class="assess-hint">Heart disease, diabetes, cancer, and mental health conditions in parents, siblings, or grandparents.</span>
    <select id="a-family-history" onchange="handleAssessInput('a-family-history')">
        <option value="">Select...</option>
        <option value="0">I know very little about my family's health history</option>
        <option value="1">I have a rough idea of major conditions</option>
        <option value="2">I know the main conditions in my immediate family</option>
        <option value="3">I have a detailed understanding including extended family</option>
        <option value="4">I've discussed my family history with a doctor and adjusted my care accordingly</option>
    </select> <span class="assess-percentile-hint" id="pct-family-history"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-family-history" onchange="handleSkip('a-family-history')"><label for="skip-family-history">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Present Vitality</h4>

<div class="assess-input-group" id="ig-symptoms-addressed">
    <span class="assess-label">How do you handle persistent symptoms or health niggles?</span>
    <span class="assess-hint">Recurring headaches, digestive issues, joint pain, skin conditions, fatigue, or anything you've learnt to live with.</span>
    <select id="a-symptoms-addressed" onchange="handleAssessInput('a-symptoms-addressed')">
        <option value="">Select...</option>
        <option value="0">I have symptoms I've been ignoring for a long time</option>
        <option value="1">I tend to tolerate things unless they become severe</option>
        <option value="2">I address most things eventually, though I sometimes delay</option>
        <option value="3">I address symptoms promptly and follow through on treatment</option>
        <option value="4">I have no unaddressed symptoms &ndash; I deal with issues as they arise</option>
    </select> <span class="assess-percentile-hint" id="pct-symptoms-addressed"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-symptoms-addressed" onchange="handleSkip('a-symptoms-addressed')"><label for="skip-symptoms-addressed">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-medications-managed">
    <span class="assess-label">How well do you manage your medications and supplements?</span>
    <span class="assess-hint">Include prescriptions, over-the-counter medicines, vitamins, and supplements.</span>
    <select id="a-medications-managed" onchange="handleAssessInput('a-medications-managed')">
        <option value="">Select...</option>
        <option value="0">I don't take any, or I take things without really knowing why</option>
        <option value="1">I take what's prescribed but don't track closely</option>
        <option value="2">I know what I take and why, and I'm mostly consistent</option>
        <option value="3">I take everything as directed, understand interactions, and review periodically with a provider</option>
    </select> <span class="assess-percentile-hint" id="pct-medications-managed"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-medications-managed" onchange="handleSkip('a-medications-managed')"><label for="skip-medications-managed">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-health-impact-days">
    <span class="assess-label">How many days per month do health issues noticeably affect your daily function?</span>
    <span class="assess-hint">Days where pain, fatigue, illness, or other health problems reduced your energy or productivity.</span>
    <input type="number" id="a-health-impact-days" min="0" max="30" step="1" placeholder="e.g. 3" onchange="handleAssessInput('a-health-impact-days')"> <span class="assess-percentile-hint" id="pct-health-impact-days"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-health-impact-days" onchange="handleSkip('a-health-impact-days')"><label for="skip-health-impact-days">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Personal Control</h4>

<div class="assess-input-group" id="ig-provider-relationship">
    <span class="assess-label">How would you describe your relationship with your primary care provider?</span>
    <span class="assess-hint">A GP, family doctor, or equivalent who knows your health history.</span>
    <select id="a-provider-relationship" onchange="handleAssessInput('a-provider-relationship')">
        <option value="">Select...</option>
        <option value="0">I don't have a primary care provider</option>
        <option value="1">I have one but rarely visit</option>
        <option value="2">I see them when needed but we don't have a strong relationship</option>
        <option value="3">I see them regularly and they know my history well</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-provider-relationship" onchange="handleSkip('a-provider-relationship')"><label for="skip-provider-relationship">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-ask-questions">
    <span class="assess-label">How comfortable are you asking questions and raising concerns during medical appointments?</span>
    <span class="assess-hint">Do you tend to accept what's recommended without question, or do you ask about alternatives and side effects?</span>
    <select id="a-ask-questions" onchange="handleAssessInput('a-ask-questions')">
        <option value="">Select...</option>
        <option value="0">I rarely ask questions &ndash; I accept what the doctor says</option>
        <option value="1">I sometimes ask questions but often feel uncomfortable doing so</option>
        <option value="2">I ask questions when something concerns me</option>
        <option value="3">I routinely ask about options, risks, and alternatives</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-ask-questions" onchange="handleSkip('a-ask-questions')"><label for="skip-ask-questions">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-health-records">
    <span class="assess-label">Can you access your health records?</span>
    <span class="assess-hint">Patient portals, paper files, or simply knowing which practices hold your records.</span>
    <select id="a-health-records" onchange="handleAssessInput('a-health-records')">
        <option value="">Select...</option>
        <option value="0">I don't know where my records are</option>
        <option value="1">I know which practices hold my records but can't easily access them</option>
        <option value="2">I can access my records through a patient portal or on request</option>
        <option value="3">I maintain organised, accessible records and review them periodically</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-health-records" onchange="handleSkip('a-health-records')"><label for="skip-health-records">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Simplicity</h4>

<div class="assess-input-group" id="ig-insurance">
    <span class="assess-label">How well do you understand your health insurance or public health system coverage?</span>
    <span class="assess-hint">What's included, what your excess is, how to make a claim, or what services are available.</span>
    <select id="a-insurance" onchange="handleAssessInput('a-insurance')">
        <option value="">Select...</option>
        <option value="0">I don't understand my coverage at all</option>
        <option value="1">I have a rough idea but couldn't explain the details</option>
        <option value="2">I understand the basics &ndash; what's covered and how to claim</option>
        <option value="3">I fully understand my coverage and use it strategically</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-insurance" onchange="handleSkip('a-insurance')"><label for="skip-insurance">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-reminders">
    <span class="assess-label">Do you have a system for tracking upcoming appointments, screenings, or prescription renewals?</span>
    <span class="assess-hint">Calendar reminders, patient portal notifications, a list on your phone, or nothing at all.</span>
    <select id="a-reminders" onchange="handleAssessInput('a-reminders')">
        <option value="">Select...</option>
        <option value="0">No system at all &ndash; I rely on memory or react when prompted</option>
        <option value="1">I use ad hoc reminders but nothing consistent</option>
        <option value="2">I have a basic system that covers most things</option>
        <option value="3">I have a reliable system that ensures nothing falls through the cracks</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-reminders" onchange="handleSkip('a-reminders')"><label for="skip-reminders">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-urgent-care">
    <span class="assess-label">Do you know what to do if you have a health concern outside normal hours?</span>
    <span class="assess-hint">Urgent care clinic, NHS 111, emergency department, or a nurse helpline.</span>
    <select id="a-urgent-care" onchange="handleAssessInput('a-urgent-care')">
        <option value="">Select...</option>
        <option value="0">I have no idea &ndash; I'd just go to A&amp;E</option>
        <option value="1">I have a vague idea but haven't looked into it</option>
        <option value="2">I know my options and could act quickly if needed</option>
        <option value="3">I have a clear plan including after-hours contacts and nearest facilities</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-urgent-care" onchange="handleSkip('a-urgent-care')"><label for="skip-urgent-care">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-longterm">
        <span class="assess-summary-label">Long-term Health</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-longterm" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-longterm">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-vitality">
        <span class="assess-summary-label">Present Vitality</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-vitality" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-vitality">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data for American adults. Personal Control and Simplicity items are recorded for your awareness but not scored, as the available data does not support reliable percentile estimates.</p>
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

<p>You now understand why health management matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about long-term health, present vitality, personal control, and simplicity. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/health-management/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Health Management Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Health Management. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/health-management/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'health-management';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-last-checkup', 'a-screenings', 'a-family-history',
        'a-symptoms-addressed', 'a-medications-managed', 'a-health-impact-days',
        'a-provider-relationship', 'a-ask-questions', 'a-health-records',
        'a-insurance', 'a-reminders', 'a-urgent-care'
    ];

    // Scoring thresholds: [{value, percentile}, ...] sorted by value ascending
    // For inverted scales (lower = better), thresholds are sorted by value descending
    var THRESHOLDS = {
        'a-last-checkup': [
            {v:'0',p:10},{v:'1',p:25},{v:'2',p:50},{v:'3',p:75},{v:'4',p:90}
        ],
        'a-screenings': [
            {v:'0',p:8},{v:'1',p:25},{v:'2',p:50},{v:'3',p:75},{v:'4',p:92}
        ],
        'a-family-history': [
            {v:'0',p:15},{v:'1',p:35},{v:'2',p:55},{v:'3',p:80},{v:'4',p:92}
        ],
        'a-symptoms-addressed': [
            {v:'0',p:15},{v:'1',p:35},{v:'2',p:55},{v:'3',p:78},{v:'4',p:92}
        ],
        'a-medications-managed': [
            {v:'0',p:20},{v:'1',p:45},{v:'2',p:70},{v:'3',p:90}
        ],
        'a-health-impact-days': [ // inverted: lower is better
            {v:20,p:5},{v:10,p:20},{v:5,p:45},{v:3,p:60},{v:1,p:78},{v:0,p:92}
        ],
        'a-provider-relationship': [
            {v:'0',p:20},{v:'1',p:40},{v:'2',p:60},{v:'3',p:85}
        ],
        'a-ask-questions': [
            {v:'0',p:20},{v:'1',p:40},{v:'2',p:60},{v:'3',p:85}
        ],
        'a-health-records': [
            {v:'0',p:20},{v:'1',p:40},{v:'2',p:65},{v:'3',p:88}
        ],
        'a-insurance': [
            {v:'0',p:15},{v:'1',p:35},{v:'2',p:60},{v:'3',p:85}
        ],
        'a-reminders': [
            {v:'0',p:20},{v:'1',p:40},{v:'2',p:65},{v:'3',p:88}
        ],
        'a-urgent-care': [
            {v:'0',p:20},{v:'1',p:40},{v:'2',p:65},{v:'3',p:88}
        ]
    };

    var VALUE_ITEMS = {
        longterm: ['a-last-checkup', 'a-screenings', 'a-family-history'],
        vitality: ['a-symptoms-addressed', 'a-medications-managed', 'a-health-impact-days']
    };

    // Personal Control and Simplicity items are recorded but not scored
    // (insufficient population data for reliable percentile estimates)
    var UNSCORED_ITEMS = [
        'a-provider-relationship', 'a-ask-questions', 'a-health-records',
        'a-insurance', 'a-reminders', 'a-urgent-care'
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
        var num = parseFloat(value);
        // Check if thresholds use string keys (dropdowns)
        if (typeof thresholds[0].v === 'string') {
            for (var i = 0; i < thresholds.length; i++) {
                if (thresholds[i].v === String(value)) return thresholds[i].p;
            }
            return null;
        }
        // Check if inverted (first threshold has higher value than last)
        var inverted = thresholds[0].v > thresholds[thresholds.length - 1].v;
        if (inverted) {
            if (num >= thresholds[0].v) return thresholds[0].p;
            if (num <= thresholds[thresholds.length - 1].v) return thresholds[thresholds.length - 1].p;
            for (var i = 0; i < thresholds.length - 1; i++) {
                if (num <= thresholds[i].v && num >= thresholds[i + 1].v) {
                    var t = (thresholds[i].v - num) / (thresholds[i].v - thresholds[i + 1].v);
                    return Math.round(thresholds[i].p + t * (thresholds[i + 1].p - thresholds[i].p));
                }
            }
        } else {
            if (num <= thresholds[0].v) return thresholds[0].p;
            if (num >= thresholds[thresholds.length - 1].v) return thresholds[thresholds.length - 1].p;
            for (var i = 0; i < thresholds.length - 1; i++) {
                if (num >= thresholds[i].v && num <= thresholds[i + 1].v) {
                    var t = (num - thresholds[i].v) / (thresholds[i + 1].v - thresholds[i].v);
                    return Math.round(thresholds[i].p + t * (thresholds[i + 1].p - thresholds[i].p));
                }
            }
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

    function isItemAnswered(itemId) {
        var skipBox = document.getElementById('skip-' + itemId.replace('a-', ''));
        if (skipBox && skipBox.checked) return true;

        var el = document.getElementById(itemId);
        return el && el.value !== '' && el.value !== null;
    }

    function updatePercentileHint(itemId) {
        if (UNSCORED_ITEMS.indexOf(itemId) !== -1) return; // no hints for unscored items
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

    function updateInputGroupState(itemId) {
        var group = document.getElementById('ig-' + itemId.replace('a-', ''));
        if (group) group.classList.toggle('answered', isItemAnswered(itemId));
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['longterm', 'vitality'].forEach(function(vk) {
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
        ['longterm', 'vitality'].forEach(function(vk) {
            scores[vk] = computeValuePercentile(vk);
        });
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-scores') || {};
            all[AREA] = scores;
            APStorage.save('ap-level1-scores', all);
        }
    }

    function updateAssessCompletion() {
        var allAnswered = ASSESS_IDS.every(function(id) { return isItemAnswered(id); });
        var btn = document.getElementById('assessBtn');
        if (btn) {
            btn.disabled = !allAnswered;
            btn.textContent = allAnswered ? 'All done \u2013 continue' : 'Answer all items to continue';
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
            if (skipBox.checked && input.type === 'number') input.value = '';
        }
        updatePercentileHint(itemId);
        updateInputGroupState(itemId);
        saveAnswers();
        updateAssessSummary();
        updateAssessCompletion();
    };

    // Override completeStep to also save scores
    var _origCompleteStep = window.completeStep;
    window.completeStep = function(step) {
        if (step === 'assess') saveScores();
        _origCompleteStep(step);
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
