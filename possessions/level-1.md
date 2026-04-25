---
layout: default
title: "Possessions – Level 1: Awareness"
life_area_slug: possessions
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

<h1>Possessions: Level 1</h1>

<p class="l1-subtitle">Understand what possessions mean, what's possible, and where you stand. About 15 minutes.</p>

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

<!-- Step 1: Why Possessions Matter -->
<div class="l1-step" id="step-why" data-step="why">
    <div class="l1-step-header" onclick="toggleStep('why')">
        <div class="l1-step-number">1</div>
        <div class="l1-step-title">Why possessions matter</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>Your possessions shape your daily experience more than most people realise. The average household contains over <a href="https://www.becomingminimalist.com/clutter-stats/" target="_blank">300,000 items</a>, and the management burden of those items – storing, finding, cleaning, maintaining, and moving them – consumes significant time and mental energy.</p>

<p>The costs of unmanaged possessions are measurable. Over a lifetime, the average person spends <a href="https://www.becomingminimalist.com/clutter-stats/" target="_blank">3,680 hours searching for misplaced items</a>. Research shows that people who feel bothered by household clutter exhibit elevated <a href="https://pubmed.ncbi.nlm.nih.gov/19934011/" target="_blank">cortisol levels</a>, a physiological stress response with long-term health implications. Eliminating clutter reduces housework by an estimated 40%.</p>

<p>Beyond the practical costs, your relationship with your possessions reflects your values. What you choose to own, maintain, and let go of says something about what matters to you. Intentional possession management frees up time, space, money, and attention for the things you care about most.</p>

<button class="l1-mark-done" onclick="completeStep('why')">I've read this &ndash; continue</button>

        </div>
    </div>
</div>

<!-- Step 2: What Different People Value -->
<div class="l1-step" id="step-values" data-step="values">
    <div class="l1-step-header" onclick="toggleStep('values')">
        <div class="l1-step-number">2</div>
        <div class="l1-step-title">What different people value about possessions</div>
        <div class="l1-step-check">&#10003;</div>
        <div class="l1-step-expand">&#9660;</div>
    </div>
    <div class="l1-step-body">
        <div class="l1-step-content">

<p>People relate to their possessions for different reasons. This site scores every possessions intervention across four core values. Later, you'll set your own weighting across these four values, and the site will rank interventions by how well they deliver on the things you actually care about.</p>

<h3>Functionality</h3>
<p>Ensuring that the things you own serve clear purposes and support your daily activities effectively. Having the right tools, maintaining them in working order, and ensuring possessions enhance rather than hinder your routines. People who prioritise this value assess items by their utility.</p>

<h3>Simplicity</h3>
<p>Maintaining a curated, manageable collection of possessions that reduces cognitive load. Regular decluttering, resistance to unnecessary acquisition, and a preference for fewer, well-chosen items over abundance. People who prioritise this value find freedom in owning less.</p>

<h3>Quality</h3>
<p>Investing in well-made, durable items that provide lasting value. Understanding materials and construction, maintaining items properly, and accepting higher upfront costs for lower lifetime costs. People who prioritise this value buy less but buy better.</p>

<h3>Meaning</h3>
<p>Owning items that carry personal, sentimental, or aesthetic significance beyond mere function. Heirlooms, handmade objects, curated collections, and possessions that tell a story or connect you to people and experiences you value. People who prioritise this value see certain objects as expressions of identity and memory.</p>

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

<p>Level 5 in this framework represents the top 0.1% &ndash; roughly 1 in 1,000 people. To give you a sense of what that looks like for each possessions value:</p>

<div class="exemplar-card">
    <div class="exemplar-value">Functionality &ndash; Level 5</div>
    <p><a href="https://en.wikipedia.org/wiki/Alton_Brown" target="_blank">Alton Brown</a> is known for insisting that every kitchen tool must serve multiple functions &ndash; he famously refuses to own any single-purpose gadget except a fire extinguisher. This principle extends to his broader approach to possessions: each item earns its place by being genuinely useful. His long-running show <em>Good Eats</em> consistently demonstrated how a small, well-chosen set of tools can outperform a cluttered kitchen full of specialised equipment.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Simplicity &ndash; Level 5</div>
    <p><a href="https://mnmlist.com/" target="_blank">Leo Babauta</a> is the author of Zen Habits and mnmlist. He moved his family from Guam to San Francisco with minimal possessions, and has written about reducing his belongings to the point where he can inventory them from memory. His approach focuses on eliminating everything that does not directly support the life he wants to live.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Quality &ndash; Level 5</div>
    <p><a href="https://www.buymeonce.com/" target="_blank">Tara Button</a> founded BuyMeOnce, a platform dedicated to identifying and recommending the most durable consumer goods available. She has spent years researching materials, construction methods, and product lifespans, and wrote <em>A Life Less Throwaway</em> on building a life around fewer, better-made possessions.</p>
</div>

<div class="exemplar-card">
    <div class="exemplar-value">Meaning &ndash; Level 5</div>
    <p><a href="https://www.significantobjects.com/" target="_blank">Rob Walker</a> is a journalist and author of <em>The Art of Noticing</em> who co-created the Significant Objects project, demonstrating how narrative and personal meaning transform the perceived value of ordinary items. His work explores how the stories we attach to objects shape our relationship with them and, by extension, our sense of identity.</p>
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
<h4>Functionality</h4>

<div class="assess-input-group" id="ig-unused-items">
    <span class="assess-label">What proportion of your possessions have you used in the past year?</span>
    <span class="assess-hint">Think room by room &ndash; kitchen gadgets, wardrobe, garage, storage areas.</span>
    <select id="a-unused-items" onchange="handleAssessInput('a-unused-items')">
        <option value="">Select...</option>
        <option value="minority">A minority &ndash; most things sit unused</option>
        <option value="about-half">About half</option>
        <option value="most">Most &ndash; I use the majority of what I own</option>
        <option value="nearly-all">Nearly all &ndash; very little goes unused</option>
        <option value="everything">Everything &ndash; if I don't use it, I get rid of it</option>
    </select> <span class="assess-percentile-hint" id="pct-unused-items"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-unused-items" onchange="handleSkip('a-unused-items')"><label for="skip-unused-items">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-broken-items">
    <span class="assess-label">How many broken or malfunctioning items do you work around?</span>
    <span class="assess-hint">A drawer that sticks, a tool with a loose handle, a device with a cracked screen.</span>
    <select id="a-broken-items" onchange="handleAssessInput('a-broken-items')">
        <option value="">Select...</option>
        <option value="many">Many &ndash; five or more</option>
        <option value="several">Several &ndash; three or four</option>
        <option value="a-couple">A couple &ndash; one or two</option>
        <option value="none">None &ndash; everything works properly</option>
        <option value="proactive">Proactive &ndash; I fix or replace things as soon as they break</option>
    </select> <span class="assess-percentile-hint" id="pct-broken-items"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-broken-items" onchange="handleSkip('a-broken-items')"><label for="skip-broken-items">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-finding-things">
    <span class="assess-label">How long does it typically take you to find things when you need them?</span>
    <span class="assess-hint">Passport, spare keys, a specific tool &ndash; do you know where they are?</span>
    <select id="a-finding-things" onchange="handleAssessInput('a-finding-things')">
        <option value="">Select...</option>
        <option value="long-search">Long search &ndash; I often can't find what I need</option>
        <option value="several-minutes">Several minutes &ndash; I usually find things but it takes effort</option>
        <option value="a-minute">About a minute &ndash; I have a rough idea where things are</option>
        <option value="quickly">Quickly &ndash; most things are in their designated place</option>
        <option value="instantly">Instantly &ndash; everything has a place and I know where it is</option>
    </select> <span class="assess-percentile-hint" id="pct-finding-things"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-finding-things" onchange="handleSkip('a-finding-things')"><label for="skip-finding-things">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Simplicity</h4>

<div class="assess-input-group" id="ig-volume">
    <span class="assess-label">How aware are you of how many possessions you own in key categories?</span>
    <span class="assess-hint">Clothes, books, kitchen items, electronics &ndash; even a rough estimate.</span>
    <select id="a-volume" onchange="handleAssessInput('a-volume')">
        <option value="">Select...</option>
        <option value="no-idea">No idea &ndash; I couldn't begin to estimate</option>
        <option value="vague">Vague &ndash; I have a rough sense for one or two categories</option>
        <option value="approximate">Approximate &ndash; I could estimate most categories</option>
        <option value="good-sense">Good sense &ndash; I know roughly what I own</option>
        <option value="precise">Precise &ndash; I've inventoried my possessions</option>
    </select> <span class="assess-percentile-hint" id="pct-volume"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-volume" onchange="handleSkip('a-volume')"><label for="skip-volume">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-acquisition">
    <span class="assess-label">How well do you understand your acquisition patterns?</span>
    <span class="assess-hint">What you tend to buy, how often, and what triggers purchases.</span>
    <select id="a-acquisition" onchange="handleAssessInput('a-acquisition')">
        <option value="">Select...</option>
        <option value="unaware">Unaware &ndash; I buy without thinking about patterns</option>
        <option value="some-awareness">Some awareness &ndash; I know I buy too much of certain things</option>
        <option value="aware">Aware &ndash; I understand my triggers and tendencies</option>
        <option value="controlled">Controlled &ndash; I've changed my habits based on this awareness</option>
        <option value="intentional">Intentional &ndash; every purchase is deliberate and considered</option>
    </select> <span class="assess-percentile-hint" id="pct-acquisition"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-acquisition" onchange="handleSkip('a-acquisition')"><label for="skip-acquisition">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-declutter">
    <span class="assess-label">When did you last do a significant declutter?</span>
    <span class="assess-hint">A whole room or category, not just tidying a single drawer.</span>
    <select id="a-declutter" onchange="handleAssessInput('a-declutter')">
        <option value="">Select...</option>
        <option value="never">Never</option>
        <option value="years-ago">Years ago</option>
        <option value="within-a-year">Within the past year</option>
        <option value="within-months">Within the past few months</option>
        <option value="regular">Regular &ndash; I declutter on a schedule</option>
    </select> <span class="assess-percentile-hint" id="pct-declutter"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-declutter" onchange="handleSkip('a-declutter')"><label for="skip-declutter">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Quality</h4>

<div class="assess-input-group" id="ig-lifetime-cost">
    <span class="assess-label">How often have you found that buying cheap cost more in the long run?</span>
    <span class="assess-hint">Shoes that wore out in months, a cheap drill that broke, furniture that fell apart.</span>
    <select id="a-lifetime-cost" onchange="handleAssessInput('a-lifetime-cost')">
        <option value="">Select...</option>
        <option value="frequently">Frequently &ndash; I keep replacing cheap items</option>
        <option value="several-times">Several times &ndash; I can think of clear examples</option>
        <option value="once-or-twice">Once or twice &ndash; I've mostly learned this lesson</option>
        <option value="rarely">Rarely &ndash; I usually buy at a quality level that lasts</option>
        <option value="never">Never &ndash; I research and invest in quality from the start</option>
    </select> <span class="assess-percentile-hint" id="pct-lifetime-cost"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-lifetime-cost" onchange="handleSkip('a-lifetime-cost')"><label for="skip-lifetime-cost">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-maintenance">
    <span class="assess-label">Do you keep up with maintaining the possessions that need it?</span>
    <span class="assess-hint">Sharpening knives, oiling tools, conditioning leather, servicing appliances.</span>
    <select id="a-maintenance" onchange="handleAssessInput('a-maintenance')">
        <option value="">Select...</option>
        <option value="never">Never &ndash; I don't maintain anything</option>
        <option value="rarely">Rarely &ndash; only when something stops working</option>
        <option value="sometimes">Sometimes &ndash; I maintain some things but not consistently</option>
        <option value="mostly">Mostly &ndash; I keep up with most maintenance</option>
        <option value="always">Always &ndash; I have a maintenance routine for everything that needs it</option>
    </select> <span class="assess-percentile-hint" id="pct-maintenance"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-maintenance" onchange="handleSkip('a-maintenance')"><label for="skip-maintenance">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-best-items">
    <span class="assess-label">Can you identify your best-quality possessions and explain what makes them good?</span>
    <span class="assess-hint">Materials, construction, how long you've had them, how well they still perform.</span>
    <select id="a-best-items" onchange="handleAssessInput('a-best-items')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I don't think about quality</option>
        <option value="vaguely">Vaguely &ndash; I know some things are better but can't say why</option>
        <option value="a-few">A few &ndash; I can point to two or three well-made items</option>
        <option value="several">Several &ndash; I deliberately own quality items and know what makes them good</option>
        <option value="knowledgeable">Knowledgeable &ndash; I can assess quality in most product categories</option>
    </select> <span class="assess-percentile-hint" id="pct-best-items"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-best-items" onchange="handleSkip('a-best-items')"><label for="skip-best-items">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-group">
<h4>Meaning</h4>

<div class="assess-input-group" id="ig-sentimental">
    <span class="assess-label">Can you distinguish which possessions have genuine personal significance?</span>
    <span class="assess-hint">Gifts, heirlooms, travel souvenirs, handmade items, things tied to important memories.</span>
    <select id="a-sentimental" onchange="handleAssessInput('a-sentimental')">
        <option value="">Select...</option>
        <option value="no">No &ndash; I haven't thought about this</option>
        <option value="vaguely">Vaguely &ndash; I know a few things matter but haven't reflected on it</option>
        <option value="somewhat">Somewhat &ndash; I can name my most meaningful items</option>
        <option value="clearly">Clearly &ndash; I know exactly which items matter and why</option>
        <option value="curated">Curated &ndash; I've deliberately kept meaningful items and let go of the rest</option>
    </select> <span class="assess-percentile-hint" id="pct-sentimental"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-sentimental" onchange="handleSkip('a-sentimental')"><label for="skip-sentimental">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-display">
    <span class="assess-label">Are your most meaningful possessions stored, displayed, or used?</span>
    <span class="assess-hint">A meaningful photo in a box vs on the wall; an heirloom in storage vs in daily use.</span>
    <select id="a-display" onchange="handleAssessInput('a-display')">
        <option value="">Select...</option>
        <option value="stored">Stored &ndash; mostly packed away or forgotten</option>
        <option value="some-visible">Some visible &ndash; a few are out but most are in storage</option>
        <option value="mixed">Mixed &ndash; some displayed, some stored</option>
        <option value="mostly-visible">Mostly visible &ndash; I can see or use most of them daily</option>
        <option value="intentional">Intentional &ndash; every meaningful item is displayed or used as I want it</option>
    </select> <span class="assess-percentile-hint" id="pct-display"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-display" onchange="handleSkip('a-display')"><label for="skip-display">I know but prefer not to say</label></div>
</div>

<div class="assess-input-group" id="ig-identity">
    <span class="assess-label">Do your possessions as a whole reflect the person you are or want to be?</span>
    <span class="assess-hint">Do your surroundings feel like yours, or like they belong to a previous version of you?</span>
    <select id="a-identity" onchange="handleAssessInput('a-identity')">
        <option value="">Select...</option>
        <option value="not-at-all">Not at all &ndash; my surroundings feel disconnected from who I am</option>
        <option value="somewhat-outdated">Somewhat outdated &ndash; they reflect a previous version of me</option>
        <option value="partly">Partly &ndash; some things fit, others don't</option>
        <option value="mostly">Mostly &ndash; my possessions generally reflect who I am now</option>
        <option value="fully">Fully &ndash; my surroundings are a deliberate expression of who I am</option>
    </select> <span class="assess-percentile-hint" id="pct-identity"></span>
    <div class="assess-skip"><input type="checkbox" id="skip-identity" onchange="handleSkip('a-identity')"><label for="skip-identity">I know but prefer not to say</label></div>
</div>
</div>

<div class="assess-summary" id="assessSummary">
    <h4>Your estimated position</h4>
    <div class="assess-summary-row" id="sum-functionality">
        <span class="assess-summary-label">Functionality</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-functionality" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-functionality">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-simplicity">
        <span class="assess-summary-label">Simplicity</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-simplicity" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-simplicity">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-quality">
        <span class="assess-summary-label">Quality</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-quality" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-quality">&ndash;</span>
    </div>
    <div class="assess-summary-row" id="sum-meaning">
        <span class="assess-summary-label">Meaning</span>
        <div class="assess-summary-bar"><div class="assess-summary-fill" id="bar-meaning" style="width:0%"></div></div>
        <span class="assess-summary-value" id="val-meaning">&ndash;</span>
    </div>
    <p class="assess-summary-text">Percentiles are estimates based on published population data on possession management behaviour among adults. All items in this area are scored.</p>
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

<p>You now understand why possessions matter, what different people get out of managing them well, what's achievable, and where you currently stand. The final step is to set your personal value weightings and see which interventions are the best fit for you.</p>

<p>On the interventions page, adjust the sliders to reflect how much you care about functionality, simplicity, quality, and meaning. The table will re-rank interventions to match your priorities.</p>

<p><a href="{{ site.baseurl }}/possessions/personalised" class="l1-mark-done" style="text-decoration:none; text-align:center; display:inline-block;">Go to Possessions Interventions &rarr;</a></p>

        </div>
    </div>
</div>

<!-- Completion banner (shown when all steps done) -->
<div class="l1-complete" id="completeBanner">
    <h2>Level 1 Complete</h2>
    <p>You've built your foundation in Possessions. Your self-assessment and value weightings are saved.</p>
    <a href="{{ site.baseurl }}/possessions/personalised" class="btn-cta">View Your Interventions</a>
</div>

</div>

<script>
(function() {
    'use strict';

    var AREA = 'possessions';
    var STEPS = ['why', 'values', 'achievable', 'assess', 'interventions'];
    var ASSESS_IDS = [
        'a-unused-items',
        'a-broken-items',
        'a-finding-things',
        'a-volume',
        'a-acquisition',
        'a-declutter',
        'a-lifetime-cost',
        'a-maintenance',
        'a-best-items',
        'a-sentimental',
        'a-display',
        'a-identity'
    ];

    var THRESHOLDS = {
        'a-unused-items': [
            // Most people have significant unused possessions; using everything is very rare
            {v:'minority',p:15},{v:'about-half',p:35},{v:'most',p:55},{v:'nearly-all',p:78},{v:'everything',p:95}
        ],
        'a-broken-items': [
            // Most households have several broken items; proactive repair is uncommon
            {v:'many',p:10},{v:'several',p:30},{v:'a-couple',p:55},{v:'none',p:78},{v:'proactive',p:95}
        ],
        'a-finding-things': [
            // Average person spends significant time searching; instant retrieval is rare
            {v:'long-search',p:10},{v:'several-minutes',p:30},{v:'a-minute',p:55},{v:'quickly',p:78},{v:'instantly',p:95}
        ],
        'a-volume': [
            // Very few people have inventoried their possessions; most have no idea
            {v:'no-idea',p:15},{v:'vague',p:35},{v:'approximate',p:55},{v:'good-sense',p:78},{v:'precise',p:95}
        ],
        'a-acquisition': [
            // Most people buy without reflecting on patterns; intentional purchasing is rare
            {v:'unaware',p:10},{v:'some-awareness',p:30},{v:'aware',p:55},{v:'controlled',p:78},{v:'intentional',p:95}
        ],
        'a-declutter': [
            // Regular scheduled decluttering is very uncommon; most people never do a major declutter
            {v:'never',p:10},{v:'years-ago',p:30},{v:'within-a-year',p:55},{v:'within-months',p:78},{v:'regular',p:95}
        ],
        'a-lifetime-cost': [
            // Most people frequently replace cheap items; researching quality from the start is rare
            {v:'frequently',p:10},{v:'several-times',p:30},{v:'once-or-twice',p:55},{v:'rarely',p:78},{v:'never',p:95}
        ],
        'a-maintenance': [
            // Most people rarely maintain possessions; a full maintenance routine is very uncommon
            {v:'never',p:10},{v:'rarely',p:30},{v:'sometimes',p:50},{v:'mostly',p:75},{v:'always',p:95}
        ],
        'a-best-items': [
            // Few people can articulate what makes their possessions high-quality
            {v:'no',p:10},{v:'vaguely',p:30},{v:'a-few',p:55},{v:'several',p:78},{v:'knowledgeable',p:95}
        ],
        'a-sentimental': [
            // Most people haven't reflected on which possessions carry genuine significance
            {v:'no',p:10},{v:'vaguely',p:30},{v:'somewhat',p:55},{v:'clearly',p:78},{v:'curated',p:95}
        ],
        'a-display': [
            // Most meaningful items end up in storage; intentional display is uncommon
            {v:'stored',p:10},{v:'some-visible',p:30},{v:'mixed',p:50},{v:'mostly-visible',p:75},{v:'intentional',p:95}
        ],
        'a-identity': [
            // Most people's surroundings don't fully reflect who they are now
            {v:'not-at-all',p:10},{v:'somewhat-outdated',p:30},{v:'partly',p:50},{v:'mostly',p:75},{v:'fully',p:95}
        ]
    };

    var VALUE_ITEMS = {
        functionality: ['a-unused-items', 'a-broken-items', 'a-finding-things'],
        simplicity: ['a-volume', 'a-acquisition', 'a-declutter'],
        quality: ['a-lifetime-cost', 'a-maintenance', 'a-best-items'],
        meaning: ['a-sentimental', 'a-display', 'a-identity']
    };

    // All possessions items are scorable
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
        ['functionality', 'simplicity', 'quality', 'meaning'].forEach(function(vk) {
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
        ['functionality', 'simplicity', 'quality', 'meaning'].forEach(function(vk) {
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
