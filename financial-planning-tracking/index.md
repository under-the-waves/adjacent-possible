---
layout: default
title: Financial Planning and Tracking
life_area_slug: financial-planning-tracking
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
    Financial Planning and Tracking
</div>

# Financial Planning and Tracking

**What it is**
- Your budgeting, financial tracking, and overall money management &ndash; the systems and habits you use to understand where your money goes, plan where it should go, and measure progress toward your financial goals.

**Why it matters**
- People with a written financial plan report 37% greater financial confidence and 38% improved financial wellbeing, yet only 36% of Americans have one. Systematic tracking reduces the mental burden of constant financial uncertainty and improves decision-making across every other financial domain.

**Related life areas**
- [Saving]({{ site.baseurl }}/saving/) &ndash; building an emergency fund and accumulating capital
- [Investing]({{ site.baseurl }}/investing/) &ndash; putting accumulated capital to work in assets that grow over time
- [Goals]({{ site.baseurl }}/goals/) &ndash; setting and tracking long-term targets, including financial ones
- [Systems]({{ site.baseurl }}/systems/) &ndash; building reliable personal systems that run with minimal friction

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Financial Planning and Tracking yet.</strong><br>It takes about 15 minutes and helps you understand what financial planning means to you.</p>
    <a href="{{ site.baseurl }}/financial-planning-tracking/level-1" class="btn-cta">Start Level 1</a>
</div>

## What people value about financial planning and tracking

People approach financial management for different reasons. This site scores every financial planning intervention across three core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Accuracy & Control</h3>
<p>Having precise, reliable financial information and clear oversight of money flows. Detailed tracking, categorisation, and understanding exactly where money goes.</p>
</div>

<div class="value-card">
<h3>Simplicity & Convenience</h3>
<p>Making financial management effortless and low-friction. Automated systems, minimal time investment, and approaches that work in the background.</p>
</div>

<div class="value-card">
<h3>Insight & Optimisation</h3>
<p>Using financial data to make better decisions and identify opportunities. Trend analysis, finding inefficiencies, and turning tracking data into actionable improvements.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/financial-planning-tracking/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand financial planning, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/financial-planning-tracking/personalised" class="path-interventions">
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
    var areaProgress = progress['financial-planning-tracking'] || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return areaProgress[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights['financial-planning-tracking'];

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Financial Planning and Tracking.</strong></p>' +
            '<a href="{{ site.baseurl }}/financial-planning-tracking/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/financial-planning-tracking/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(areaProgress).length > 0) {
        var completed = steps.filter(function(s) { return areaProgress[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/financial-planning-tracking/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
