---
layout: default
title: "Cognitive Skills – Level 1: Awareness"
life_area_slug: cognitive-skills
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

/* Assessment checklist */
.assess-group { margin-bottom: 20px; }
.assess-group h4 { margin: 0 0 10px 0; }
.assess-item {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 10px 14px;
    margin-bottom: 6px;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    cursor: pointer;
    transition: border-color 0.2s, background 0.2s;
    font-size: 0.93em;
    line-height: 1.4;
}
.assess-item:hover { border-color: #155799; background: #f0f4ff; }
.assess-item.checked { border-color: #28a745; background: #f0f7f0; }
.assess-item input[type="checkbox"] {
    margin-top: 2px;
    flex-shrink: 0;
    accent-color: #28a745;
}
.assess-item label { cursor: pointer; flex: 1; }
.assess-hint {
    font-size: 0.85em;
    color: #888;
    margin-top: 2px;
}

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

<h1>Cognitive Skills: Level 1</h1>

<p class="l1-subtitle">Understand what cognitive skills are, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Cognitive Skills Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why cognitive skills matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your cognitive abilities – memory, focus, reasoning, problem-solving – underpin almost everything you do. They determine how quickly you learn, how well you make decisions, and how effectively you handle complex situations at work and in daily life.</p>

<p>The good news is that these abilities are more trainable than most people assume. Meta-analyses of memory training show that <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3399982/" target="_blank">evidence-based techniques can improve retention by 200 – 300%</a> over baseline methods. Even short periods of attention training – as little as five days – appear to <a href="https://www.pnas.org/content/104/43/17152" target="_blank">improve executive attention and reduce stress-related cortisol</a>.</p>

<p>Lifestyle factors matter too. Regular exercise <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2441149/" target="_blank">increases BDNF by 15 – 30%</a>, a protein that supports learning and memory. Sleep optimisation enhances memory consolidation substantially. These gains compound: better cognitive function speeds up learning in every domain, which in turn opens more opportunities for growth elsewhere.</p>

<p>Yet most adults have never received any formal training in how to think, remember, or focus more effectively. Fewer than 3% use evidence-based memory techniques regularly, and fewer than 10% can sustain focus on demanding work for 30 minutes without distraction. This means even modest investment tends to yield disproportionate returns.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about cognitive skills</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People pursue cognitive improvement for different reasons. This site scores every cognitive skills intervention across four core values. Later, you'll set your own weighting across these values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Memory</h3>
<p>Developing systematic approaches to encode, store, and retrieve information efficiently. People who lean towards this value want measurably better recall for learning, professional tasks, and accessing stored knowledge when it matters. They tend to gravitate towards techniques like spaced repetition, method of loci, and elaborative encoding.</p>

<h3>Focus</h3>
<p>Sustained attention, concentration, and cognitive control. People who lean towards this value want better command over where their mind goes and stays during demanding tasks. They may pursue mindfulness meditation, attention training, or environmental design to reduce distraction and improve task-switching ability.</p>

<h3>Reasoning & Problem-Solving</h3>
<p>Fluid intelligence, abstract reasoning, and creative problem-solving. People who lean towards this value want to think through complex problems more effectively – breaking challenges into components, spotting patterns, and generating novel solutions. They often pursue working memory training and systematic reasoning exercises.</p>

<h3>Lifestyle Integration</h3>
<p>Cognitive enhancement through sustainable daily practices. People who lean towards this value want cognitive benefits that emerge from overall wellbeing – optimised sleep, regular exercise, good nutrition, and stress management – rather than dedicated cognitive training sessions.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each cognitive skills value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Memory &ndash; Level 5</div>
    <p><a href="https://www.mullen.memory/" target="_blank">Alex Mullen</a> is a three-time World Memory Champion who memorised a shuffled deck of cards in 15.61 seconds and over 3,000 digits in an hour. He trained using the method of loci and spaced repetition while completing medical school, demonstrating that exceptional memory performance is compatible with a demanding professional career. He now teaches memory techniques through his platform Mullen Memory.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Focus &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Mihaly_Csikszentmihalyi" target="_blank">Mihaly Csikszentmihalyi</a> spent over 40 years researching the psychology of optimal experience and coined the concept of "flow." He reportedly structured his own working life around the conditions he studied &ndash; long uninterrupted blocks, intrinsic motivation, and clear goals &ndash; and maintained a prolific research output across psychology, creativity, and education until his death in 2021 at age 87.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Reasoning & Problem-Solving &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Terence_Tao" target="_blank">Terence Tao</a> is a mathematician at UCLA who has published over 300 research papers across multiple subfields and won the Fields Medal in 2006. His ability to identify patterns and generate novel approaches across diverse areas of mathematics – from harmonic analysis to combinatorics to partial differential equations – reflects extraordinary reasoning ability sustained at the highest level for decades.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Lifestyle Integration &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Sanjay_Gupta" target="_blank">Sanjay Gupta</a> is a practising neurosurgeon and CNN's chief medical correspondent who wrote <em>Keep Sharp</em> based on his clinical experience with cognitive decline. He maintains a personal regimen of daily exercise, sleep discipline, and continuous learning that he describes as non-negotiable for his own cognitive performance. He has sustained demanding parallel careers in surgery and broadcasting for over 20 years, suggesting the lifestyle integration he advocates is one he genuinely practises.</p>
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
<h4>Memory</h4>

<div class="assess-input-group" id="ig-recall-names">
    <span class="assess-label">How well do you remember names of people you've recently met?</span>
    <span class="assess-hint">Think about the last few social or professional settings where you met new people.</span>
    <select id="a-recall-names" onchange="handleAssessInput('a-recall-names')">
        <option value="">Select...</option>
        <option value="very-poor">Very poorly &ndash; almost never remember</option>
        <option value="poor">Poorly &ndash; forget most names within hours</option>
        <option value="average">Average &ndash; remember some, forget others</option>
        <option value="good">Good &ndash; usually remember after one introduction</option>
        <option value="excellent">Excellent &ndash; rarely forget a name</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-recall-names" onchange="handleSkip('a-recall-names')"><label for="skip-recall-names">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-memory-techniques">
    <span class="assess-label">Do you use any deliberate memory techniques?</span>
    <span class="assess-hint">Spaced repetition apps, mnemonics, method of loci, note-taking systems designed for retention.</span>
    <select id="a-memory-techniques" onchange="handleAssessInput('a-memory-techniques')">
        <option value="">Select...</option>
        <option value="none">None at all</option>
        <option value="occasional">Occasionally &ndash; I've tried one or two but don't use them regularly</option>
        <option value="one-method">One method &ndash; I have a single technique I use fairly consistently</option>
        <option value="several">Several &ndash; I use multiple techniques depending on the material</option>
        <option value="systematic">Systematic &ndash; I have a structured retention system I rely on daily</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-memory-techniques" onchange="handleSkip('a-memory-techniques')"><label for="skip-memory-techniques">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-retention">
    <span class="assess-label">How much do you retain from articles, books, or presentations after a week?</span>
    <span class="assess-hint">Think about something you read or watched last week. How much can you recall now?</span>
    <select id="a-retention" onchange="handleAssessInput('a-retention')">
        <option value="">Select...</option>
        <option value="almost-nothing">Almost nothing &ndash; can barely recall the topic</option>
        <option value="gist-only">Gist only &ndash; remember the general subject but few details</option>
        <option value="key-points">Key points &ndash; remember the main arguments or takeaways</option>
        <option value="good-detail">Good detail &ndash; can summarise accurately and recall specifics</option>
        <option value="thorough">Thorough &ndash; can discuss in depth and connect to other knowledge</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-retention" onchange="handleSkip('a-retention')"><label for="skip-retention">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Focus</h4>

<div class="assess-input-group" id="ig-focus-duration">
    <span class="assess-label">How long can you sustain focus on demanding work before getting distracted?</span>
    <span class="assess-hint">Think about a typical work session on something cognitively challenging.</span>
    <select id="a-focus-duration" onchange="handleAssessInput('a-focus-duration')">
        <option value="">Select...</option>
        <option value="under-10">Under 10 minutes</option>
        <option value="10-25">10&ndash;25 minutes</option>
        <option value="25-50">25&ndash;50 minutes</option>
        <option value="50-90">50&ndash;90 minutes</option>
        <option value="over-90">Over 90 minutes</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-focus-duration" onchange="handleSkip('a-focus-duration')"><label for="skip-focus-duration">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-distraction-triggers">
    <span class="assess-label">How aware are you of your main distraction triggers?</span>
    <span class="assess-hint">Phone notifications, email, social media, noise, boredom, anxiety, fatigue.</span>
    <select id="a-distraction-triggers" onchange="handleAssessInput('a-distraction-triggers')">
        <option value="">Select...</option>
        <option value="unaware">Unaware &ndash; I get distracted but don't know why</option>
        <option value="vague">Vague sense &ndash; I know it happens but haven't analysed it</option>
        <option value="some-awareness">Some awareness &ndash; I can name a few triggers</option>
        <option value="clear">Clear &ndash; I know my main triggers and when they hit</option>
        <option value="detailed">Detailed &ndash; I've mapped my triggers and have strategies for each</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-distraction-triggers" onchange="handleSkip('a-distraction-triggers')"><label for="skip-distraction-triggers">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-attention-practices">
    <span class="assess-label">Do you do anything deliberate to train or protect your attention?</span>
    <span class="assess-hint">Meditation, phone-free periods, website blockers, structured work intervals.</span>
    <select id="a-attention-practices" onchange="handleAssessInput('a-attention-practices')">
        <option value="">Select...</option>
        <option value="nothing">Nothing specific</option>
        <option value="occasional">Occasional &ndash; I've tried a few things but nothing stuck</option>
        <option value="one-practice">One practice &ndash; I have a single habit I maintain</option>
        <option value="several">Several &ndash; I use multiple attention-protection strategies</option>
        <option value="comprehensive">Comprehensive &ndash; I have a structured system for managing attention</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-attention-practices" onchange="handleSkip('a-attention-practices')"><label for="skip-attention-practices">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Reasoning &amp; Problem-Solving</h4>

<div class="assess-input-group" id="ig-problem-approach">
    <span class="assess-label">How do you typically approach complex problems?</span>
    <span class="assess-hint">Breaking them into parts, jumping to solutions, seeking advice, using frameworks, trial and error.</span>
    <select id="a-problem-approach" onchange="handleAssessInput('a-problem-approach')">
        <option value="">Select...</option>
        <option value="avoid">Avoid them &ndash; I tend to put off or delegate complex problems</option>
        <option value="reactive">Reactive &ndash; I jump in without a plan and see what happens</option>
        <option value="basic">Basic structure &ndash; I break them down but don't use formal methods</option>
        <option value="methodical">Methodical &ndash; I have a consistent approach I follow</option>
        <option value="systematic">Systematic &ndash; I select and apply appropriate frameworks depending on the problem</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-problem-approach" onchange="handleSkip('a-problem-approach')"><label for="skip-problem-approach">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-reasoning-biases">
    <span class="assess-label">How aware are you of your reasoning biases or blind spots?</span>
    <span class="assess-hint">Confirmation bias, anchoring, availability heuristic &ndash; do you know which ones affect your thinking most?</span>
    <select id="a-reasoning-biases" onchange="handleAssessInput('a-reasoning-biases')">
        <option value="">Select...</option>
        <option value="unaware">Unaware &ndash; I haven't thought about this</option>
        <option value="heard-of">Heard of them &ndash; I know biases exist but can't identify my own</option>
        <option value="some-awareness">Some awareness &ndash; I can name a few that probably affect me</option>
        <option value="active">Active awareness &ndash; I regularly catch myself falling into biased thinking</option>
        <option value="systematic">Systematic &ndash; I use debiasing techniques and seek disconfirming evidence</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-reasoning-biases" onchange="handleSkip('a-reasoning-biases')"><label for="skip-reasoning-biases">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-reasoning-training">
    <span class="assess-label">Have you had any formal or informal training in reasoning or critical thinking?</span>
    <span class="assess-hint">Logic courses, debate, philosophy, scientific method, decision-making frameworks.</span>
    <select id="a-reasoning-training" onchange="handleAssessInput('a-reasoning-training')">
        <option value="">Select...</option>
        <option value="none">None &ndash; just learning on the job</option>
        <option value="self-taught">Self-taught &ndash; some reading on the topic</option>
        <option value="some-formal">Some formal &ndash; a course or structured programme</option>
        <option value="substantial">Substantial &ndash; multiple courses or significant study</option>
        <option value="extensive">Extensive &ndash; deep training that I actively apply</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-reasoning-training" onchange="handleSkip('a-reasoning-training')"><label for="skip-reasoning-training">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Lifestyle Integration</h4>

<div class="assess-input-group" id="ig-sleep-cognition">
    <span class="assess-label">How much does your sleep affect your mental clarity and cognitive performance?</span>
    <span class="assess-hint">Do you notice a difference in your thinking on days after good vs poor sleep?</span>
    <select id="a-sleep-cognition" onchange="handleAssessInput('a-sleep-cognition')">
        <option value="">Select...</option>
        <option value="unaware">Unaware &ndash; I haven't noticed a connection</option>
        <option value="slight">Slight &ndash; I notice it occasionally</option>
        <option value="moderate">Moderate &ndash; I can usually tell when poor sleep affects my thinking</option>
        <option value="strong">Strong &ndash; sleep quality has a clear, predictable impact</option>
        <option value="managed">Managed &ndash; I optimise my sleep specifically for cognitive performance</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-sleep-cognition" onchange="handleSkip('a-sleep-cognition')"><label for="skip-sleep-cognition">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-exercise-cognition">
    <span class="assess-label">Does exercise noticeably affect your mental sharpness?</span>
    <span class="assess-hint">Some people think more clearly after exercise. Others don't notice a difference.</span>
    <select id="a-exercise-cognition" onchange="handleAssessInput('a-exercise-cognition')">
        <option value="">Select...</option>
        <option value="dont-exercise">I don't exercise regularly enough to tell</option>
        <option value="no-effect">No noticeable effect</option>
        <option value="slight">Slight &ndash; I sometimes feel sharper after exercise</option>
        <option value="noticeable">Noticeable &ndash; I think more clearly on days I exercise</option>
        <option value="significant">Significant &ndash; exercise is a reliable cognitive booster for me</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-exercise-cognition" onchange="handleSkip('a-exercise-cognition')"><label for="skip-exercise-cognition">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-lifestyle-deliberate">
    <span class="assess-label">Do you do anything deliberately to support your cognitive performance through lifestyle choices?</span>
    <span class="assess-hint">Optimised sleep schedule, exercise for brain health, nutrition choices, stress management.</span>
    <select id="a-lifestyle-deliberate" onchange="handleAssessInput('a-lifestyle-deliberate')">
        <option value="">Select...</option>
        <option value="nothing">Nothing specific</option>
        <option value="one-thing">One thing &ndash; I have a single lifestyle habit aimed at cognitive performance</option>
        <option value="a-few">A few &ndash; I've made some deliberate choices</option>
        <option value="several">Several &ndash; I actively manage multiple lifestyle factors for cognitive benefit</option>
        <option value="comprehensive">Comprehensive &ndash; I have an integrated lifestyle strategy for cognitive performance</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-lifestyle-deliberate" onchange="handleSkip('a-lifestyle-deliberate')"><label for="skip-lifestyle-deliberate">I know but prefer not to say</label></div>
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

<p>You now understand why cognitive skills matter, what different people get out of developing them, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about memory, focus, reasoning and problem-solving, and lifestyle integration. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/cognitive-skills/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Cognitive Skills Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Cognitive Skills. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/cognitive-skills/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'cognitive-skills';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-recall-names', 'a-memory-techniques', 'a-retention',
        'a-focus-duration', 'a-distraction-triggers', 'a-attention-practices',
        'a-problem-approach', 'a-reasoning-biases', 'a-reasoning-training',
        'a-sleep-cognition', 'a-exercise-cognition', 'a-lifestyle-deliberate'
    ];

    // All cognitive-skills items are qualitative and unscored (no reliable percentile data)
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
        // All cognitive-skills items are unscored; save null for each value
        var scores = {
            memory: null,
            focus: null,
            reasoning: null,
            lifestyle: null
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
