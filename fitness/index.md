---
layout: default
title: Fitness
life_area_slug: fitness
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
    Fitness
</div>

# Fitness

**What it is**
- Your physical exercise habits, training approach, and overall activity level. Fitness is about what your body can do and how exercise affects your health and happiness.

**Why it matters**
- Regular exercise reduces your risk of death from any cause by 30 – 40%, improves mental health, and touches more areas of life simultaneously than almost any other investment.

**Related life areas**
- [Body image]({{ site.baseurl }}/body-image/) – your physical appearance, including body composition, grooming, and vitality
- [Nutrition]({{ site.baseurl }}/nutrition/) – your dietary knowledge, food choices, and the nutritional quality of what you eat
- [Sleep]({{ site.baseurl }}/sleep/) – your sleep quality, duration, and bedtime routines
- [Health management]({{ site.baseurl }}/health-management/) – how you monitor and manage your physical health and medical needs

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Fitness yet.</strong><br>It takes about 15 minutes and helps you understand what fitness means to you.</p>
    <a href="{{ site.baseurl }}/fitness/level-1/" class="btn-cta">Start Level 1</a>
</div>

## What people value about fitness

People pursue fitness for different reasons. This site scores every fitness intervention across three core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Health & Longevity</h3>
<p>Cardiovascular health, muscle mass for healthy ageing, joint integrity, and metabolic health. Sustainable practices with minimal injury risk.</p>
<p class="exemplar">Level 5 example: <a href="https://richroll.com/bio/" target="_blank">Rich Roll</a> went from sedentary at 39 to completing five Ironman-distance triathlons in five days, driven primarily by longevity rather than competition.</p>
</div>

<div class="value-card">
<h3>Physical Performance</h3>
<p>Strength, endurance, power, speed, coordination, and specific skills. What your body can do.</p>
<p class="exemplar">Level 5 example: <a href="https://games.crossfit.com/athlete/32551" target="_blank">Adam Klink</a>, a CrossFit coach who ran a sub-5-minute mile and back squatted 500 lb in the same day at 97 kg bodyweight.</p>
</div>

<div class="value-card">
<h3>Enjoyment & Psychological Benefits</h3>
<p>Stress reduction, mood enhancement, community connection, and the satisfaction of movement itself.</p>
<p class="exemplar">Level 5 example: <a href="https://themirnavator.com/" target="_blank">Mirna Valerio</a>, an ultrarunner and 2018 National Geographic Adventurer of the Year who runs primarily for joy and community rather than competition.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/fitness/level-1/" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand fitness, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/fitness/personalised" class="path-interventions">
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
    var fitness = progress.fitness || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return fitness[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights.fitness;

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Fitness.</strong></p>' +
            '<a href="{{ site.baseurl }}/fitness/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/fitness/level-1/" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(fitness).length > 0) {
        var completed = steps.filter(function(s) { return fitness[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/fitness/level-1/" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
