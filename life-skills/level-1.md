---
layout: default
title: "Life Skills – Level 1: Awareness"
life_area_slug: life-skills
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

<h1>Life Skills: Level 1</h1>

<p class="l1-subtitle">Understand what life skills means, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Life Skills Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why life skills matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Practical competence is one of the quieter foundations of a well-functioning life. Most people don't think much about it until something breaks, someone gets hurt, or a bill arrives that could have been avoided.</p>

<p>The financial case is reasonably straightforward. Households in the US spend an average of roughly <a href="https://www.homeadvisor.com/r/true-cost-report/" target="_blank">$10,000 a year on home maintenance</a>, and a significant share of that goes to tasks that a moderately skilled person could handle. Basic car maintenance can prevent repairs costing <a href="https://www.aaa.com/autorepair/articles/car-maintenance-basics" target="_blank">three to four times more</a> than the upkeep itself. Even modest DIY proficiency tends to pay for itself fairly quickly.</p>

<p>Beyond money, there is a psychological dimension. Research on self-efficacy suggests that successfully handling practical challenges builds confidence that carries over into other areas of life. People who feel capable of dealing with everyday problems – a leaking tap, a flat tyre, a medical emergency – generally report lower anxiety about unexpected situations.</p>

<p>Practical skills also strengthen social ties. Being the person who can help a neighbour fix a fence or teach a friend to cook a proper meal creates bonds that are difficult to build in other ways. Communities with higher concentrations of practical know-how tend to have stronger mutual-aid networks.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about life skills</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People develop practical skills for different reasons. This site scores every life skills intervention across three core values. Later, you'll set your own weighting across these three values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>High-Impact Capabilities</h3>
<p>Focusing on the handful of practical abilities that provide disproportionate benefits when needed – skills like first aid, basic car maintenance, essential home repairs, and core cooking techniques. People who lean towards this value want to master the specific capabilities that matter most, rather than trying to learn everything.</p>

<h3>Systematic Competence</h3>
<p>Building organised, methodical approaches to practical knowledge and maintenance rather than learning skills reactively as problems arise. Creating reference systems, following preventive schedules, maintaining proper tools, and developing frameworks for tackling unfamiliar tasks. People who lean towards this value want structured, reliable approaches to practical life management.</p>

<h3>Teaching & Sharing</h3>
<p>Using practical skills as opportunities to help others, connect with family and friends, or contribute to community. Teaching skills to children, helping neighbours with projects, being the person others turn to for practical advice, or participating in skill-sharing activities. People who lean towards this value see life skills as ways to build relationships and contribute meaningfully to others' lives.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each life skills value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">High-Impact Capabilities &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Larry_Haun" target="_blank">Larry Haun</a> was a carpenter who spent over 50 years building houses and could frame an entire wall in minutes. He wrote multiple books on efficient building techniques, could handle plumbing, electrical, roofing, and finishing work to professional standards, and remained actively competent across virtually every practical domain relevant to residential construction well into his 70s.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Systematic Competence &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Adam_Savage" target="_blank">Adam Savage</a> is a maker, fabricator, and former MythBusters host whose workshop organisation and systematic approach to practical problem-solving are widely documented. He maintains comprehensive tool systems, applies methodical processes to unfamiliar challenges, and has demonstrated professional-level competence across metalworking, woodworking, electronics, sewing, and model-making.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Teaching & Sharing &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Norm_Abram" target="_blank">Norm Abram</a> hosted <em>The New Yankee Workshop</em> and <em>This Old House</em> for decades, teaching millions of viewers to tackle home improvement projects. His clear, patient instruction style made complex woodworking and renovation techniques accessible to beginners, and he is widely credited with inspiring a generation of DIY practitioners.</p>
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
<h4>High-Impact Capabilities</h4>

<div class="assess-input-group" id="ig-home-repair">
    <span class="assess-label">How many basic home repairs can you handle yourself?</span>
    <span class="assess-hint">Fixing a leaking tap, unclogging a drain, patching a wall, resetting a tripped circuit breaker.</span>
    <select id="a-home-repair" onchange="handleAssessInput('a-home-repair')">
        <option value="">Select...</option>
        <option value="none">None &ndash; I'd call someone for anything</option>
        <option value="one-or-two">One or two &ndash; I can handle the simplest things</option>
        <option value="several">Several &ndash; I can do a range of basic repairs</option>
        <option value="most">Most &ndash; I'm confident with most common household repairs</option>
        <option value="extensive">Extensive &ndash; I can handle complex repairs and minor renovations</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-home-repair" onchange="handleSkip('a-home-repair')"><label for="skip-home-repair">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-first-aid">
    <span class="assess-label">Could you administer basic first aid in an emergency?</span>
    <span class="assess-hint">CPR, treating burns, stopping bleeding, recognising signs of a stroke or heart attack.</span>
    <select id="a-first-aid" onchange="handleAssessInput('a-first-aid')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I wouldn't know what to do</option>
        <option value="very-basic">Very basic &ndash; I know to call 999 and apply a plaster</option>
        <option value="some">Some &ndash; I could handle minor injuries</option>
        <option value="trained">Trained &ndash; I've done a first aid course</option>
        <option value="current">Current &ndash; I have up-to-date first aid training</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-first-aid" onchange="handleSkip('a-first-aid')"><label for="skip-first-aid">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-cooking">
    <span class="assess-label">How many meals can you cook from scratch without a recipe?</span>
    <span class="assess-hint">Dishes where you could buy raw ingredients and produce a complete meal.</span>
    <select id="a-cooking" onchange="handleAssessInput('a-cooking')">
        <option value="">Select...</option>
        <option value="zero">Zero &ndash; I can't cook</option>
        <option value="1-3">1&ndash;3 meals</option>
        <option value="4-10">4&ndash;10 meals</option>
        <option value="10-20">10&ndash;20 meals</option>
        <option value="over-20">Over 20 meals</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-cooking" onchange="handleSkip('a-cooking')"><label for="skip-cooking">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Systematic Competence</h4>

<div class="assess-input-group" id="ig-tools">
    <span class="assess-label">Do you own the basic tools and know where they are?</span>
    <span class="assess-hint">Screwdrivers, pliers, adjustable spanner, hammer, tape measure, drill.</span>
    <select id="a-tools" onchange="handleAssessInput('a-tools')">
        <option value="">Select...</option>
        <option value="none">No tools at all</option>
        <option value="minimal">Minimal &ndash; a couple of items, not sure where they are</option>
        <option value="basics">Basics &ndash; I have the essentials and can find them</option>
        <option value="well-equipped">Well equipped &ndash; a solid toolkit, well organised</option>
        <option value="comprehensive">Comprehensive &ndash; I have specialist tools for most jobs</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-tools" onchange="handleSkip('a-tools')"><label for="skip-tools">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-maintenance">
    <span class="assess-label">Do you follow any preventive maintenance schedule for your home or car?</span>
    <span class="assess-hint">Regular boiler servicing, gutter clearing, oil changes, tyre pressure checks.</span>
    <select id="a-maintenance" onchange="handleAssessInput('a-maintenance')">
        <option value="">Select...</option>
        <option value="nothing">Nothing &ndash; I wait until things break</option>
        <option value="reactive">Mostly reactive &ndash; I fix things when prompted</option>
        <option value="some">Some &ndash; I do a few regular checks</option>
        <option value="consistent">Consistent &ndash; I follow a maintenance schedule</option>
        <option value="thorough">Thorough &ndash; I track and plan all maintenance proactively</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-maintenance" onchange="handleSkip('a-maintenance')"><label for="skip-maintenance">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-approach">
    <span class="assess-label">How do you typically approach an unfamiliar practical problem?</span>
    <span class="assess-hint">Search for a tutorial, ask someone, have a go and see what happens, or avoid it entirely?</span>
    <select id="a-approach" onchange="handleAssessInput('a-approach')">
        <option value="">Select...</option>
        <option value="avoid">Avoid it &ndash; I pay someone or ignore it</option>
        <option value="ask">Ask someone &ndash; I rely on others for practical help</option>
        <option value="search">Search &ndash; I look up a tutorial and follow it</option>
        <option value="try-then-search">Try then search &ndash; I have a go first and look things up if stuck</option>
        <option value="confident">Confident &ndash; I assess the problem and work through it methodically</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-approach" onchange="handleSkip('a-approach')"><label for="skip-approach">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Teaching &amp; Sharing</h4>

<div class="assess-input-group" id="ig-help-others">
    <span class="assess-label">How regularly do you help friends, family, or neighbours with practical tasks?</span>
    <span class="assess-hint">Fixing things, cooking for others, helping with moves, lending tools or expertise.</span>
    <select id="a-help-others" onchange="handleAssessInput('a-help-others')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I don't have the skills to help</option>
        <option value="rarely">Rarely &ndash; once or twice a year</option>
        <option value="occasionally">Occasionally &ndash; every month or two</option>
        <option value="regularly">Regularly &ndash; multiple times a month</option>
        <option value="frequently">Frequently &ndash; I'm a go-to person for practical help</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-help-others" onchange="handleSkip('a-help-others')"><label for="skip-help-others">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-teach">
    <span class="assess-label">Does anyone come to you for practical advice or help?</span>
    <span class="assess-hint">Are you the person people ring when something breaks, or do you tend to be the one asking?</span>
    <select id="a-teach" onchange="handleAssessInput('a-teach')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I'm always the one asking</option>
        <option value="rarely">Rarely &ndash; people don't think of me for practical help</option>
        <option value="sometimes">Sometimes &ndash; for one or two specific things</option>
        <option value="often">Often &ndash; people know I'm handy and ask regularly</option>
        <option value="go-to">Go-to person &ndash; I'm the first call for multiple types of problem</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-teach" onchange="handleSkip('a-teach')"><label for="skip-teach">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-community">
    <span class="assess-label">Do you participate in any skill-sharing or community repair activities?</span>
    <span class="assess-hint">Repair cafes, maker spaces, tool libraries, community gardens, or informal skill swaps.</span>
    <select id="a-community" onchange="handleAssessInput('a-community')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I've never participated</option>
        <option value="interested">Interested but haven't tried</option>
        <option value="tried-once">Tried once &ndash; attended an event or two</option>
        <option value="occasional">Occasional &ndash; I participate a few times a year</option>
        <option value="regular">Regular &ndash; I'm an active member of a skill-sharing community</option>
    </select>
    <div class="assess-skip"><input type="checkbox" id="skip-community" onchange="handleSkip('a-community')"><label for="skip-community">I know but prefer not to say</label></div>
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

<p>You now understand why life skills matter, what different people get out of them, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about high-impact capabilities, systematic competence, and teaching and sharing. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/life-skills/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Life Skills Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Life Skills. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/life-skills/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'life-skills';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-home-repair', 'a-first-aid', 'a-cooking',
        'a-tools', 'a-maintenance', 'a-approach',
        'a-help-others', 'a-teach', 'a-community'
    ];

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
        var scores = {
            capabilities: null,
            competence: null,
            sharing: null
        };
        if (typeof APStorage !== 'undefined') {
            var all = APStorage.load('ap-level1-scores') || {};
            all[AREA] = scores;
            APStorage.save('ap-level1-scores', all);
        }
    }

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
