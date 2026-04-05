---
layout: default
title: Saving
life_area_slug: saving
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
    Finances &gt;
    Saving
</div>

# Saving

**What it is**
- Setting aside money you have earned rather than spending it, building a reserve that protects you from shocks and funds the things you want in life.

**Why it matters**
- Emergency savings are the single strongest predictor of financial wellbeing &ndash; stronger than income, debt levels, or investment returns. Yet 24 – 27% of adults have no emergency savings at all, and the national savings rate hovers between 3 – 5%. Even modest, consistent saving behaviour places you well above population averages.

**Related life areas**
- [Financial planning & tracking]({{ site.baseurl }}/financial-planning-tracking/) &ndash; budgeting, net worth tracking, and financial goal-setting
- [Investing]({{ site.baseurl }}/investing/) &ndash; putting accumulated capital to work in assets that grow over time
- [Current work]({{ site.baseurl }}/current-work/) &ndash; your primary income source that funds savings
- [Housing]({{ site.baseurl }}/housing/) &ndash; typically your largest expense, directly affecting how much you can save

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Saving yet.</strong><br>It takes about 15 minutes and helps you understand what saving means to you.</p>
    <a href="{{ site.baseurl }}/saving/level-1" class="btn-cta">Start Level 1</a>
</div>

## What people value about saving

People save for different reasons. This site scores every saving intervention across three core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Security</h3>
<p>Building and maintaining a financial buffer against unexpected expenses and income disruption. Emergency funds, insurance, and ensuring reserves can absorb shocks without resorting to debt.</p>
</div>

<div class="value-card">
<h3>Lifestyle</h3>
<p>Saving toward specific lifestyle goals &ndash; holidays, experiences, purchases, and planned upgrades to quality of life. Balancing present enjoyment with future security.</p>
</div>

<div class="value-card">
<h3>Growth</h3>
<p>Accumulating wealth over time through consistently high savings rates and sustained discipline. Steadily increasing net worth and maximising the rate at which savings compound.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/saving/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand saving, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/saving/personalised" class="path-interventions">
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
    var areaProgress = progress.saving || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return areaProgress[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights.saving;

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Saving.</strong></p>' +
            '<a href="{{ site.baseurl }}/saving/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/saving/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(areaProgress).length > 0) {
        var completed = steps.filter(function(s) { return areaProgress[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/saving/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
