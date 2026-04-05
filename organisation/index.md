---
layout: default
title: Organisation
life_area_slug: organisation
---

<style>
.la-home { max-width: 800px; margin: 0 auto; }

.breadcrumb-nav {
    font-size: 0.9em;
    color: #666;
    margin-bottom: 8px;
}
.breadcrumb-nav a {
    color: #155799;
    text-decoration: none;
}
.breadcrumb-nav a:hover {
    text-decoration: underline;
}

.la-banner {
    border-radius: 8px;
    padding: 20px 24px;
    margin: 24px 0;
    text-align: center;
}
.la-banner--start {
    background: #f0f7f0;
    border: 2px solid #28a745;
}
.la-banner--complete {
    background: #f0f4ff;
    border: 2px solid #155799;
}
.la-banner p { margin: 0 0 12px 0; }
.la-banner .btn-cta {
    display: inline-block;
    padding: 10px 24px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
    color: white;
    background: #28a745;
    transition: background 0.2s;
}
.la-banner .btn-cta:hover { background: #218838; }
.la-banner .btn-secondary {
    display: inline-block;
    padding: 10px 24px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
    color: #155799;
    background: white;
    border: 1px solid #155799;
    margin-left: 12px;
    transition: background 0.2s;
}
.la-banner .btn-secondary:hover { background: #e8eef5; }

.value-card {
    background: #f8f9fa;
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 12px;
}
.value-card h3 { margin: 0 0 6px 0; font-size: 1.05em; }
.value-card p { margin: 0; font-size: 0.95em; color: #444; }
.value-card .exemplar {
    margin-top: 8px;
}

.la-paths {
    display: flex;
    gap: 16px;
    margin-top: 28px;
}
.la-paths a {
    flex: 1;
    display: block;
    padding: 16px;
    border-radius: 8px;
    text-decoration: none;
    text-align: center;
    font-weight: 600;
    transition: background 0.2s, box-shadow 0.2s;
}
.la-paths .path-level1 {
    background: #f0f7f0;
    border: 2px solid #28a745;
    color: #1a6b2a;
}
.la-paths .path-level1:hover { background: #e0f0e0; box-shadow: 0 2px 8px rgba(40,167,69,0.2); }
.la-paths .path-interventions {
    background: #f0f4ff;
    border: 2px solid #155799;
    color: #155799;
}
.la-paths .path-interventions:hover { background: #e0eaff; box-shadow: 0 2px 8px rgba(21,87,153,0.2); }
.la-paths .path-desc {
    font-weight: normal;
    font-size: 0.85em;
    color: #666;
    margin-top: 4px;
}

@media (max-width: 600px) {
    .la-paths { flex-direction: column; }
}
</style>

<div class="la-home" markdown="1">

<div class="breadcrumb-nav">
    <a href="{{ site.baseurl }}/">Home</a> &gt;
    <a href="{{ site.baseurl }}/life-areas/">Life Areas</a> &gt;
    Organise Your Life &gt;
    Productivity &gt;
    Organisation
</div>

# Organisation

**What it is**
- How well you keep your tasks, spaces, and commitments in order. Organisation is the invisible infrastructure behind reliability and clarity &ndash; the practice of structuring your environment, tasks, and information so that things are where you need them, when you need them.

**Why it matters**
- The average person spends 8.5 minutes per day searching for misplaced items, and knowledge workers lose 1.8 &ndash; 2.5 hours per day hunting for information. 41% of to-do list items are never completed. Even basic organisational competence is rare enough that modest improvements place you well above the majority.

**Related life areas**
- [Systems]({{ site.baseurl }}/systems) &ndash; the tools, automations, and workflows you build to handle recurring tasks and manage information
- [Time Management]({{ site.baseurl }}/time-management) &ndash; how you plan, schedule, and protect your time
- [Goals]({{ site.baseurl }}/goals) &ndash; specific outcomes you commit to achieving within a defined timeframe
- [Habits]({{ site.baseurl }}/habits) &ndash; the repeated behaviours that form the foundation of personal effectiveness

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Organisation yet.</strong><br>It takes about 15 minutes and helps you understand what organisation means to you.</p>
    <a href="{{ site.baseurl }}/organisation/level-1" class="btn-cta">Start Level 1</a>
</div>

## What people value about organisation

People pursue organisation for different reasons. This site scores every organisation intervention across three core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Tracking</h3>
<p>Capturing and monitoring all commitments, tasks, and information so nothing falls through the cracks. Maintaining a trusted system for recording what needs doing, reviewing progress regularly, and ensuring everything important is visible and accounted for.</p>
</div>

<div class="value-card">
<h3>Order</h3>
<p>Maintaining structured, predictable systems for physical and digital environments. Consistent filing, clear storage systems, labelled locations for everything, and routines that keep spaces and information organised.</p>
</div>

<div class="value-card">
<h3>Speed</h3>
<p>Minimising the time spent on organisational overhead so you can move quickly from intention to action. Rapid processing of incoming tasks, fast retrieval of information, and systems designed for throughput over perfection.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/organisation/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand organisation, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/organisation/personalised" class="path-interventions">
        Browse Interventions
        <div class="path-desc">See personalised recommendations based on your priorities</div>
    </a>
</div>

</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    var banner = document.getElementById('level1Banner');
    if (!banner || typeof APStorage === 'undefined') return;

    var progress = APStorage.load('ap-level1-progress') || {};
    var organisation = progress.organisation || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return organisation[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights.organisation;

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Organisation.</strong></p>' +
            '<a href="{{ site.baseurl }}/organisation/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/organisation/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(organisation).length > 0) {
        var completed = steps.filter(function(s) { return organisation[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/organisation/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
