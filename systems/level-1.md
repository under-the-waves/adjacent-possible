---
layout: default
title: "Systems – Level 1: Awareness"
life_area_slug: systems
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

<h1>Systems: Level 1</h1>

<p class="l1-subtitle">Understand what personal systems are, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Systems Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why systems matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Personal systems are the tools, automations, and workflows you build to handle recurring tasks and manage information. They are the infrastructure that lets you spend your attention on decisions and creative work rather than on logistics.</p>

<p><a href="https://www.breeze.pm/blog/task-management-statistics" target="_blank">94% of employees</a> regularly perform repetitive tasks that consume significant time, and around 54% believe automation could save them more than 5 hours per week. <a href="https://www.cflowapps.com/workflow-automation-statistics/" target="_blank">Workflow automation</a> can reduce repetitive tasks by 60 &ndash; 95%, saving up to 77% of time on routine activities.</p>

<p>Without intentional systems, <a href="https://www.breeze.pm/blog/task-management-statistics" target="_blank">approximately 70% of projects</a> fall short of their goals in timely delivery, budget, or scope. Teams that prioritise tasks effectively are 1.4 times more likely to outperform their peers.</p>

<p>The gap compounds over time. Systematic approaches accumulate benefits whilst ad hoc approaches accumulate costs. The best systems are invisible &ndash; they are obvious only in their absence, working quietly in the background so you can focus on what actually matters.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about systems</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue systems for different reasons. This site scores every systems intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Power</h3>
<p>Maximising what your personal systems can do &ndash; automation depth, feature richness, customisation, and the ability to handle complex workflows and edge cases. People who prioritise this value invest significant time building systems that save large amounts of time once complete, accepting complexity as a worthwhile cost.</p>

<h3>Simplicity</h3>
<p>Keeping personal systems as minimal, intuitive, and easy to understand as possible. Using fewer tools, avoiding over-engineering, choosing solutions that require no documentation to use, and preferring manual processes over complex automations that might break. People who prioritise this value believe the best system is one you actually use consistently, and that complexity is the enemy of sustained adoption.</p>

<h3>Reliability</h3>
<p>Ensuring your systems work consistently and fail gracefully, with minimal unplanned maintenance or debugging. Choosing proven tools over cutting-edge ones, building in redundancy, testing automations before depending on them, and designing systems that degrade gracefully when something breaks. People who prioritise this value accept less capability or more manual work in exchange for systems they can trust.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each systems value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Power &ndash; Level 5</div>
    <p><a href="https://www.youtube.com/@NetworkChuck" target="_blank">Chuck Keith</a> (NetworkChuck) is a network engineer and content creator who has built comprehensive personal infrastructure including self-hosted servers, automated backups, network monitoring, smart home integrations, and custom dashboards that manage nearly every aspect of his digital life. He documents these builds publicly, demonstrating systems that handle complex conditional logic across personal and professional domains whilst remaining maintainable by a single person.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Simplicity &ndash; Level 5</div>
    <p><a href="https://dereksivers.com/" target="_blank">Derek Sivers</a> is a programmer, author, and former founder of CD Baby (which he sold for $22 million). He runs his entire life from a small set of plain-text files, a custom-built personal database, and minimal tooling he wrote himself. His systems handle contacts, projects, finances, and media &ndash; all designed to be so simple that they survive moves between countries and decades of use without needing redesign.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Reliability &ndash; Level 5</div>
    <p><a href="https://www.hanselman.com/about" target="_blank">Scott Hanselman</a> is a software engineer, podcaster, and speaker who has maintained the same core personal productivity systems for over 20 years. He has published extensively about his setup, which prioritises proven tools, redundant backups, and graceful degradation. His systems have survived multiple job changes, technology migrations, and a Type 1 diabetes diagnosis that required integrating medical device data into his daily workflow without disrupting everything else.</p>
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
<h4>Power</h4>

<div class="assess-input-group" id="ig-automation-count">
    <span class="assess-label">How many automated workflows do you currently have running?</span>
    <span class="assess-hint">Email filters, scheduled backups, smart home routines, IFTTT or Zapier automations, scripts, cron jobs.</span>
    <select id="a-automation-count" onchange="handleAssessInput('a-automation-count')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I do everything manually</option>
        <option value="one-two">One or two &ndash; a couple of basic automations</option>
        <option value="several">Several &ndash; 3 &ndash; 5 automations across different areas</option>
        <option value="many">Many &ndash; 6 &ndash; 10 automations that handle significant work</option>
        <option value="comprehensive">Comprehensive &ndash; 10+ automations covering most recurring tasks</option>
    </select> <span class="assess-percentile-hint" id="pct-automation-count"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-automation-count" onchange="handleSkip('a-automation-count')"><label for="skip-automation-count">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-manual-recurring">
    <span class="assess-label">How many recurring tasks do you currently do manually that could be automated?</span>
    <span class="assess-hint">Think about what you do every day or week that follows the same steps each time.</span>
    <select id="a-manual-recurring" onchange="handleAssessInput('a-manual-recurring')">
        <option value="">Select...</option>
        <option value="many">Many &ndash; most of my recurring tasks are manual</option>
        <option value="several">Several &ndash; I can easily name 5+</option>
        <option value="a-few">A few &ndash; 2 &ndash; 3 obvious candidates</option>
        <option value="one-or-two">One or two &ndash; most things are already handled</option>
        <option value="none">None &ndash; everything automatable is already automated</option>
    </select> <span class="assess-percentile-hint" id="pct-manual-recurring"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-manual-recurring" onchange="handleSkip('a-manual-recurring')"><label for="skip-manual-recurring">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-edge-cases">
    <span class="assess-label">What happens when your current systems encounter an unusual situation or edge case?</span>
    <span class="assess-hint">Do they handle it gracefully, require manual intervention, or just break?</span>
    <select id="a-edge-cases" onchange="handleAssessInput('a-edge-cases')">
        <option value="">Select...</option>
        <option value="no-systems">No systems &ndash; I don't have systems to speak of</option>
        <option value="break">Break &ndash; unusual situations cause failures I have to fix</option>
        <option value="manual">Manual intervention &ndash; I have to step in and handle it</option>
        <option value="mostly-graceful">Mostly graceful &ndash; minor issues but nothing critical</option>
        <option value="robust">Robust &ndash; my systems handle edge cases well</option>
    </select> <span class="assess-percentile-hint" id="pct-edge-cases"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-edge-cases" onchange="handleSkip('a-edge-cases')"><label for="skip-edge-cases">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Simplicity</h4>

<div class="assess-input-group" id="ig-tool-count">
    <span class="assess-label">How would you describe your set of organisational tools and apps?</span>
    <span class="assess-hint">Count them. Is it a small, deliberate set, or have you accumulated dozens over the years?</span>
    <select id="a-tool-count" onchange="handleAssessInput('a-tool-count')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I don't use dedicated tools</option>
        <option value="accumulated">Accumulated &ndash; many tools gathered over time with lots of overlap</option>
        <option value="moderate">Moderate &ndash; a reasonable number but not fully deliberate</option>
        <option value="curated">Curated &ndash; a small, intentional set that works together</option>
        <option value="minimal">Minimal &ndash; the fewest possible tools, each chosen carefully</option>
    </select> <span class="assess-percentile-hint" id="pct-tool-count"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-tool-count" onchange="handleSkip('a-tool-count')"><label for="skip-tool-count">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-explain-system">
    <span class="assess-label">Could you explain your organisational system to someone else in under five minutes?</span>
    <span class="assess-hint">If it would take longer, or if you're not sure you could explain it at all, that's useful information.</span>
    <select id="a-explain-system" onchange="handleAssessInput('a-explain-system')">
        <option value="">Select...</option>
        <option value="no-system">No &ndash; I don't really have a system to explain</option>
        <option value="couldnt">Probably not &ndash; it's too messy or complex to describe quickly</option>
        <option value="with-effort">With effort &ndash; I could explain it but it would take a while</option>
        <option value="yes-mostly">Yes, mostly &ndash; the core is simple even if details are complex</option>
        <option value="easily">Easily &ndash; it's simple enough to explain in a few minutes</option>
    </select> <span class="assess-percentile-hint" id="pct-explain-system"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-explain-system" onchange="handleSkip('a-explain-system')"><label for="skip-explain-system">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-abandoned-tools">
    <span class="assess-label">How many tools or systems have you tried and abandoned in the past two years?</span>
    <span class="assess-hint">Apps you downloaded and stopped using, notebooks you started and forgot, systems you set up and never maintained.</span>
    <select id="a-abandoned-tools" onchange="handleAssessInput('a-abandoned-tools')">
        <option value="">Select...</option>
        <option value="many">Many &ndash; 6 or more abandoned tools</option>
        <option value="several">Several &ndash; 4 &ndash; 5 abandoned tools</option>
        <option value="a-few">A few &ndash; 2 &ndash; 3 abandoned tools</option>
        <option value="one">One &ndash; mostly stable but one thing didn't work out</option>
        <option value="none">None &ndash; I've stuck with everything I've adopted</option>
    </select> <span class="assess-percentile-hint" id="pct-abandoned-tools"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-abandoned-tools" onchange="handleSkip('a-abandoned-tools')"><label for="skip-abandoned-tools">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Reliability</h4>

<div class="assess-input-group" id="ig-backup-status">
    <span class="assess-label">Are your important files and data backed up, and when did the last backup run?</span>
    <span class="assess-hint">Photos, documents, passwords, financial records. Could you recover if your computer died today?</span>
    <select id="a-backup-status" onchange="handleAssessInput('a-backup-status')">
        <option value="">Select...</option>
        <option value="no-backups">No backups &ndash; I'd lose important data if my devices failed</option>
        <option value="partial">Partial &ndash; some things are backed up but significant gaps exist</option>
        <option value="manual">Manual &ndash; I back up occasionally but not on a schedule</option>
        <option value="mostly-automated">Mostly automated &ndash; regular backups with a few gaps</option>
        <option value="fully-automated">Fully automated &ndash; everything important is backed up and I've verified recovery</option>
    </select> <span class="assess-percentile-hint" id="pct-backup-status"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-backup-status" onchange="handleSkip('a-backup-status')"><label for="skip-backup-status">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-system-failures">
    <span class="assess-label">When did one of your systems last fail or require unplanned maintenance?</span>
    <span class="assess-hint">An automation that stopped working, a tool that updated and broke your workflow, data you couldn't find.</span>
    <select id="a-system-failures" onchange="handleAssessInput('a-system-failures')">
        <option value="">Select...</option>
        <option value="constantly">Constantly &ndash; something breaks every week</option>
        <option value="recently">Recently &ndash; within the past month</option>
        <option value="a-while-ago">A while ago &ndash; a few months back</option>
        <option value="rarely">Rarely &ndash; can't remember the last time</option>
        <option value="never">Never &ndash; my systems have been rock-solid</option>
    </select> <span class="assess-percentile-hint" id="pct-system-failures"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-system-failures" onchange="handleSkip('a-system-failures')"><label for="skip-system-failures">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-single-points">
    <span class="assess-label">Do any of your systems have single points of failure?</span>
    <span class="assess-hint">If one tool, device, or account were lost, would your whole system collapse?</span>
    <select id="a-single-points" onchange="handleAssessInput('a-single-points')">
        <option value="">Select...</option>
        <option value="dont-know">I don't know &ndash; I haven't thought about it</option>
        <option value="yes-many">Yes &ndash; several critical single points of failure</option>
        <option value="yes-some">Yes &ndash; one or two areas with no redundancy</option>
        <option value="mostly-covered">Mostly covered &ndash; I've addressed the biggest risks</option>
        <option value="fully-redundant">Fully redundant &ndash; no single point of failure in any critical system</option>
    </select> <span class="assess-percentile-hint" id="pct-single-points"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-single-points" onchange="handleSkip('a-single-points')"><label for="skip-single-points">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-power">
        <span class="assess-summary-label">Power</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-power" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-power">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-simplicity">
        <span class="assess-summary-label">Simplicity</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-simplicity" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-simplicity">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-reliability">
        <span class="assess-summary-label">Reliability</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-reliability" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-reliability">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published data on personal systems and automation adoption among adults. All items in this area are scored.</p>
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

<p>You now understand why systems matter, what different people get out of them, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about power, simplicity, and reliability. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/systems/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Systems Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Systems. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/systems/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'systems';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-automation-count',
        'a-manual-recurring',
        'a-edge-cases',
        'a-tool-count',
        'a-explain-system',
        'a-abandoned-tools',
        'a-backup-status',
        'a-system-failures',
        'a-single-points'
    ];

    var THRESHOLDS = {
        'a-automation-count': [
            // Most people have no personal automations; 10+ is very rare
            {v:'none',p:15},{v:'one-two',p:35},{v:'several',p:60},{v:'many',p:80},{v:'comprehensive',p:95}
        ],
        'a-manual-recurring': [
            // Most people do many recurring tasks manually; fully automated is very rare
            {v:'many',p:10},{v:'several',p:30},{v:'a-few',p:55},{v:'one-or-two',p:78},{v:'none',p:95}
        ],
        'a-edge-cases': [
            // Most people have no systems or fragile ones; robust edge-case handling is rare
            {v:'no-systems',p:10},{v:'break',p:25},{v:'manual',p:50},{v:'mostly-graceful',p:78},{v:'robust',p:95}
        ],
        'a-tool-count': [
            // Most people accumulate tools; a minimal, curated set is uncommon
            {v:'none',p:15},{v:'accumulated',p:25},{v:'moderate',p:50},{v:'curated',p:78},{v:'minimal',p:95}
        ],
        'a-explain-system': [
            // Most people can't explain their organisational approach quickly
            {v:'no-system',p:10},{v:'couldnt',p:25},{v:'with-effort',p:50},{v:'yes-mostly',p:75},{v:'easily',p:95}
        ],
        'a-abandoned-tools': [
            // Most people have tried and abandoned several tools; sticking with everything is rare
            {v:'many',p:10},{v:'several',p:25},{v:'a-few',p:50},{v:'one',p:78},{v:'none',p:95}
        ],
        'a-backup-status': [
            // ~30% of people have never backed up; fully automated with verified recovery is very rare
            {v:'no-backups',p:10},{v:'partial',p:30},{v:'manual',p:50},{v:'mostly-automated',p:78},{v:'fully-automated',p:95}
        ],
        'a-system-failures': [
            // Most people experience regular system issues; rock-solid reliability is uncommon
            {v:'constantly',p:10},{v:'recently',p:30},{v:'a-while-ago',p:55},{v:'rarely',p:78},{v:'never',p:95}
        ],
        'a-single-points': [
            // Most people haven't thought about single points of failure; full redundancy is rare
            {v:'dont-know',p:10},{v:'yes-many',p:20},{v:'yes-some',p:45},{v:'mostly-covered',p:75},{v:'fully-redundant',p:95}
        ]
    };

    var VALUE_ITEMS = {
        power: ['a-automation-count', 'a-manual-recurring', 'a-edge-cases'],
        simplicity: ['a-tool-count', 'a-explain-system', 'a-abandoned-tools'],
        reliability: ['a-backup-status', 'a-system-failures', 'a-single-points']
    };

    // All systems items are scorable
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
        ['power', 'simplicity', 'reliability'].forEach(function(vk) {
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
        ['power', 'simplicity', 'reliability'].forEach(function(vk) {
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
