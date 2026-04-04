---
layout: default
title: Food Management
life_area_slug: food-management
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
    Look After Yourself &gt;
    Health &gt;
    Food Management
</div>

# Food Management

**What it is**
- Your ability to plan, source, and prepare food reliably through whatever methods work for you. Food management concerns *how* you get food on the table, whether that involves cooking from scratch, meal kits, takeaway, or any combination.

**Why it matters**
- Deciding what to eat is now rated as <a href="https://dentsu-ho.com/en/articles/9478" target="_blank">more burdensome than the actual cooking or cleanup</a>, and 77% of people report being too exhausted to cook after work. A dependable food system reduces daily stress, minimises waste, and ensures your nutritional goals are actually achievable in practice.

**Related life areas**
- [Food and Nutrition]({{ site.baseurl }}/nutrition/) &ndash; your dietary knowledge, food choices, and the nutritional quality of what you eat
- [Housework]({{ site.baseurl }}/housework/) &ndash; maintaining your living environment, including kitchen cleanliness and organisation
- [Time Management]({{ site.baseurl }}/time-management/) &ndash; how you plan and allocate your time across competing demands
- [Saving]({{ site.baseurl }}/saving/) &ndash; setting aside money rather than spending it, including food budgeting

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Food Management yet.</strong><br>It takes about 15 minutes and helps you understand what food management means to you.</p>
    <a href="{{ site.baseurl }}/food-management/level-1" class="btn-cta">Start Level 1</a>
</div>

## What people value about food management

People approach food management for different reasons. This site scores every food management intervention across three core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Competence</h3>
<p>Reliably getting good food on the table through whatever combination of methods works for you. Planning, sourcing, preparation skill, food safety, adaptability, and the ability to make do with what's available.</p>
</div>

<div class="value-card">
<h3>Craft</h3>
<p>Satisfaction and creative expression derived from the process of preparing food. Skill development, mastery of techniques, culinary exploration, and the meditative or therapeutic aspects of cooking.</p>
</div>

<div class="value-card">
<h3>Waste Reduction</h3>
<p>Minimising the food that gets thrown away through better management practices. Stock management, use-up routines, storage skills, purchasing discipline, and creative use of leftovers.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/food-management/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand food management, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/food-management/personalised" class="path-interventions">
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
    var fm = progress['food-management'] || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return fm[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights['food-management'];

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Food Management.</strong></p>' +
            '<a href="{{ site.baseurl }}/food-management/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/food-management/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(fm).length > 0) {
        var completed = steps.filter(function(s) { return fm[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/food-management/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
