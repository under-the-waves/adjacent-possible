---
layout: default
title: "Digital Safety – Level 1: Awareness"
life_area_slug: digital-safety
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

<h1>Digital Safety: Level 1</h1>

<p class="l1-subtitle">Understand what digital safety means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Digital Safety Matters -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why digital safety matters</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your digital life is one of the most under-protected parts of your existence. Most people store sensitive financial, medical, and personal information across dozens of online accounts, yet fewer than half take basic steps to secure them.</p>

<p>The consequences of poor digital safety are tangible. <a href="https://secureframe.com/blog/cybersecurity-statistics" target="_blank">85% of data breaches involve human factors</a> &ndash; meaning they happen because of something the victim did or failed to do, not because a hacker broke through advanced defences. Identity theft, financial fraud, and privacy violations affect <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8853293/" target="_blank">roughly a quarter of the population</a> at some point.</p>

<p>The good news is that a handful of straightforward measures can dramatically reduce your risk. Enabling two-factor authentication, for instance, <a href="https://www.microsoft.com/en-us/security/blog/2019/08/20/one-simple-action-you-can-take-to-prevent-99-9-percent-of-account-attacks/" target="_blank">prevents 99.9% of automated account attacks</a>. Using a password manager makes credential theft substantially less likely. These interventions require modest effort to set up and minimal ongoing maintenance.</p>

<p>Beyond preventing harm, good digital safety practices give you confidence to use online services &ndash; banking, healthcare portals, cloud storage &ndash; without the nagging worry that you might be exposing yourself to unnecessary risk.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about digital safety</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People approach digital safety with different priorities. This site scores every digital safety intervention across two core values. Later, you'll set your own weighting across these two values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Comprehensive Security</h3>
<p>Minimising exposure to cyber threats, data breaches, privacy violations, and digital fraud through systematic security measures, privacy controls, and threat awareness. People who lean towards this value focus on thorough protection across devices and platforms, proactive security practices, and evidence-based methods for reducing digital risk &ndash; even when that means accepting some inconvenience or reduced functionality.</p>

<h3>Usability and Convenience</h3>
<p>Maintaining digital functionality and ease of use whilst achieving reasonable security. People who lean towards this value seek protective measures that integrate into existing digital workflows without excessive friction, complexity, or technical barriers. They want to keep using their preferred platforms and services without security getting in the way.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each digital safety value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Comprehensive Security &ndash; Level 5</div>
    <p><a href="https://micahflee.com/" target="_blank">Micah Lee</a> is a technologist and journalist who served as a technical adviser to Edward Snowden and helped establish <a href="https://theintercept.com/" target="_blank">The Intercept's</a> secure communication infrastructure. He develops and maintains open-source security tools including <a href="https://onionshare.org/" target="_blank">OnionShare</a>, practises rigorous operational security in his own digital life, and has written extensively about practical threat modelling for non-experts. His work demonstrates that comprehensive personal security can be maintained consistently over many years.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Usability and Convenience &ndash; Level 5</div>
    <p><a href="https://troyhunt.com/" target="_blank">Troy Hunt</a> is the creator of <a href="https://haveibeenpwned.com/" target="_blank">Have I Been Pwned</a> and a long-time advocate for making security accessible to ordinary users. He uses and publicly documents a streamlined personal security setup &ndash; password manager, hardware security keys, automated monitoring &ndash; that provides strong protection with minimal daily friction. His writing consistently emphasises practical, low-effort security measures over comprehensive but burdensome approaches.</p>
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

<p>Awareness means knowing your starting point. Answer each question below &ndash; some you might know off the top of your head, others might take a few minutes to check.</p>

<div class="assess-group">
<h4>Comprehensive Security</h4>

<div class="assess-input-group" id="ig-password-reuse">
    <span class="assess-label">Roughly how many of your online accounts share the same password?</span>
    <span class="assess-hint">Think about your email, banking, social media, and shopping accounts. Count accounts where you use an identical or near-identical password.</span>
    <input type="number" id="a-password-reuse" min="0" max="100" step="1" placeholder="e.g. 5" onchange="handleAssessInput('a-password-reuse')"> <span class="assess-percentile-hint" id="pct-password-reuse"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-password-reuse" onchange="handleSkip('a-password-reuse')"><label for="skip-password-reuse">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-2fa-adoption">
    <span class="assess-label">How many of your important accounts have two-factor authentication enabled?</span>
    <span class="assess-hint">Check your email, banking, and social media accounts. Look for settings labelled "two-step verification", "2FA", or "login verification".</span>
    <select id="a-2fa-adoption" onchange="handleAssessInput('a-2fa-adoption')">
        <option value="">Select...</option>
        <option value="0">None</option>
        <option value="1">One or two accounts</option>
        <option value="2">About half of my important accounts</option>
        <option value="3">Most of my important accounts</option>
        <option value="4">All of my important accounts</option>
    </select> <span class="assess-percentile-hint" id="pct-2fa-adoption"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-2fa-adoption" onchange="handleSkip('a-2fa-adoption')"><label for="skip-2fa-adoption">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-phishing-awareness">
    <span class="assess-label">How confident are you at spotting phishing emails or messages?</span>
    <span class="assess-hint">Think about sender addresses, urgency cues, suspicious links, and requests for personal information.</span>
    <select id="a-phishing-awareness" onchange="handleAssessInput('a-phishing-awareness')">
        <option value="">Select...</option>
        <option value="0">I'm not sure what phishing is</option>
        <option value="1">I've heard of it but wouldn't feel confident spotting it</option>
        <option value="2">I can spot obvious phishing but might miss sophisticated attempts</option>
        <option value="3">I reliably spot phishing and check sender details, links, and context</option>
        <option value="4">I can identify advanced social engineering and spear-phishing attempts</option>
    </select> <span class="assess-percentile-hint" id="pct-phishing-awareness"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-phishing-awareness" onchange="handleSkip('a-phishing-awareness')"><label for="skip-phishing-awareness">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Usability and Convenience</h4>

<div class="assess-input-group" id="ig-password-method">
    <span class="assess-label">How do you currently manage your passwords?</span>
    <span class="assess-hint">There's no wrong answer here. The point is knowing your current method.</span>
    <select id="a-password-method" onchange="handleAssessInput('a-password-method')">
        <option value="">Select...</option>
        <option value="0">I memorise them or use the same one everywhere</option>
        <option value="1">I write them down on paper or in a note</option>
        <option value="2">I let my browser save them</option>
        <option value="3">I use a dedicated password manager for some accounts</option>
        <option value="4">I use a dedicated password manager for all accounts</option>
    </select> <span class="assess-percentile-hint" id="pct-password-method"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-password-method" onchange="handleSkip('a-password-method')"><label for="skip-password-method">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-update-habits">
    <span class="assess-label">Are your devices set to install software updates automatically?</span>
    <span class="assess-hint">Check your phone and computer settings. On most devices, look for "Software Update" or "Windows Update" settings.</span>
    <select id="a-update-habits" onchange="handleAssessInput('a-update-habits')">
        <option value="">Select...</option>
        <option value="0">I don't know or I usually dismiss update prompts</option>
        <option value="1">I install updates occasionally when reminded</option>
        <option value="2">I install updates within a week of them appearing</option>
        <option value="3">Automatic updates are on for all my devices</option>
    </select> <span class="assess-percentile-hint" id="pct-update-habits"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-update-habits" onchange="handleSkip('a-update-habits')"><label for="skip-update-habits">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-backup-frequency">
    <span class="assess-label">How often do you back up your important files?</span>
    <span class="assess-hint">Consider cloud sync, external hard drives, or any other backup method for documents, photos, and other files you'd hate to lose.</span>
    <select id="a-backup-frequency" onchange="handleAssessInput('a-backup-frequency')">
        <option value="">Select...</option>
        <option value="0">I don't back up my files</option>
        <option value="1">Rarely &ndash; less than once a year</option>
        <option value="2">Occasionally &ndash; a few times a year</option>
        <option value="3">Regularly &ndash; monthly or when I remember</option>
        <option value="4">Continuously &ndash; automatic cloud or scheduled backups</option>
    </select> <span class="assess-percentile-hint" id="pct-backup-frequency"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-backup-frequency" onchange="handleSkip('a-backup-frequency')"><label for="skip-backup-frequency">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>General Awareness</h4>

<div class="assess-input-group" id="ig-privacy-settings">
    <span class="assess-label">How well do you know the privacy settings on your most-used platforms?</span>
    <span class="assess-hint">Check who can see your posts, whether your profile appears in search engines, and what data the platform collects about you.</span>
    <select id="a-privacy-settings" onchange="handleAssessInput('a-privacy-settings')">
        <option value="">Select...</option>
        <option value="0">I've never looked at them</option>
        <option value="1">I've glanced at them but not changed much</option>
        <option value="2">I've reviewed and adjusted settings on my main platforms</option>
        <option value="3">I regularly review privacy settings across all platforms I use</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-privacy-settings" onchange="handleSkip('a-privacy-settings')"><label for="skip-privacy-settings">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-breach-history">
    <span class="assess-label">Have you ever checked whether your accounts have been involved in a data breach?</span>
    <span class="assess-hint">You can check at <a href="https://haveibeenpwned.com/" target="_blank">haveibeenpwned.com</a>.</span>
    <select id="a-breach-history" onchange="handleAssessInput('a-breach-history')">
        <option value="">Select...</option>
        <option value="0">No, I've never checked</option>
        <option value="1">I've checked once but didn't act on the results</option>
        <option value="2">I've checked and changed passwords for affected accounts</option>
        <option value="3">I check periodically and act on any new breaches</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-breach-history" onchange="handleSkip('a-breach-history')"><label for="skip-breach-history">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-security-confidence">
    <span class="assess-label">Overall, how confident do you feel about your digital security?</span>
    <span class="assess-hint">A gut check &ndash; do you feel your accounts, devices, and data are reasonably well protected?</span>
    <select id="a-security-confidence" onchange="handleAssessInput('a-security-confidence')">
        <option value="">Select...</option>
        <option value="0">Not confident at all &ndash; I know I'm exposed</option>
        <option value="1">Slightly uneasy &ndash; I've done the basics but suspect gaps</option>
        <option value="2">Fairly confident &ndash; I've taken deliberate steps</option>
        <option value="3">Very confident &ndash; I have a systematic approach</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-security-confidence" onchange="handleSkip('a-security-confidence')"><label for="skip-security-confidence">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-security">
        <span class="assess-summary-label">Comprehensive Security</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-security" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-security">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-convenience">
        <span class="assess-summary-label">Usability &amp; Convenience</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-convenience" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-convenience">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published cybersecurity survey data for the general population. General Awareness items are recorded for your awareness but not scored, as the available data does not support reliable percentile estimates.</p>
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

<p>You now understand why digital safety matters, what different people get out of it, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about comprehensive security versus usability and convenience. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/digital-safety/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Digital Safety Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Digital Safety. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/digital-safety/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'digital-safety';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-password-reuse', 'a-2fa-adoption', 'a-phishing-awareness',
        'a-password-method', 'a-update-habits', 'a-backup-frequency',
        'a-privacy-settings', 'a-breach-history', 'a-security-confidence'
    ];

    // Scoring thresholds: [{v, p}, ...] sorted by value
    // password-reuse is inverted: fewer reused passwords = better
    var THRESHOLDS = {
        'a-password-reuse': [ // inverted: lower is better
            {v:20,p:5},{v:15,p:15},{v:10,p:30},{v:5,p:50},{v:2,p:70},{v:1,p:85},{v:0,p:95}
        ],
        'a-2fa-adoption': [
            {v:'0',p:20},{v:'1',p:40},{v:'2',p:55},{v:'3',p:75},{v:'4',p:92}
        ],
        'a-phishing-awareness': [
            {v:'0',p:10},{v:'1',p:30},{v:'2',p:55},{v:'3',p:78},{v:'4',p:93}
        ],
        'a-password-method': [
            {v:'0',p:15},{v:'1',p:30},{v:'2',p:50},{v:'3',p:72},{v:'4',p:90}
        ],
        'a-update-habits': [
            {v:'0',p:15},{v:'1',p:35},{v:'2',p:60},{v:'3',p:82}
        ],
        'a-backup-frequency': [
            {v:'0',p:10},{v:'1',p:25},{v:'2',p:45},{v:'3',p:65},{v:'4',p:85}
        ]
    };

    var VALUE_ITEMS = {
        security: ['a-password-reuse', 'a-2fa-adoption', 'a-phishing-awareness'],
        convenience: ['a-password-method', 'a-update-habits', 'a-backup-frequency']
    };

    // General Awareness items are recorded but not scored (insufficient population data)
    var UNSCORED_ITEMS = ['a-privacy-settings', 'a-breach-history', 'a-security-confidence'];

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
        hintEl.textContent = pct !== null ? '~' + pct + 'th percentile' : '';
    }

    function updateInputGroupState(itemId) {
        var group = document.getElementById('ig-' + itemId.replace('a-', ''));
        if (group) group.classList.toggle('answered', isItemAnswered(itemId));
    }

    function updateAssessSummary() {
        var anyAnswered = false;
        ['security', 'convenience'].forEach(function(vk) {
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
        ['security', 'convenience'].forEach(function(vk) {
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
