---
layout: default
title: Time Management
life_area_slug: time-management
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
    Time Management
</div>

# Time Management

**What it is**
- How effectively you allocate and protect your time. Time management covers the systems, habits, and decisions that determine what you spend your hours on and how much control you feel over your schedule.

**Why it matters**
- A meta-analysis of 158 studies found that time management enhances life satisfaction more than job performance, with particularly strong effects on reducing stress. People who feel in control of their time report significantly better work-life balance, lower overload, and less tension.

**Related life areas**
- [Goals]({{ site.baseurl }}/goals) – how you set, track, and achieve meaningful goals
- [Habits]({{ site.baseurl }}/habits) – your ability to build and maintain positive habits
- [Systems]({{ site.baseurl }}/systems) – how you design and maintain the systems that support your daily life
- [Organisation]({{ site.baseurl }}/organisation) – how you manage information, spaces, and commitments

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Time Management yet.</strong><br>It takes about 15 minutes and helps you understand what time management means to you.</p>
    <a href="{{ site.baseurl }}/time-management/level-1" class="btn-cta">Start Level 1</a>
</div>

## What people value about time management

People pursue time management for different reasons. This site scores every time management intervention across three core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Productivity & Achievement</h3>
<p>Maximising output and accomplishing meaningful goals efficiently. Getting more done in less time, meeting deadlines consistently, and making tangible progress on important projects.</p>
</div>

<div class="value-card">
<h3>Balance & Wellbeing</h3>
<p>Creating sustainable rhythms that support long-term effectiveness while maintaining personal wellbeing. Managing energy, preventing burnout, and ensuring time for rest and relationships.</p>
</div>

<div class="value-card">
<h3>Flexibility & Responsiveness</h3>
<p>Maintaining the ability to adapt to changing priorities and unexpected demands while staying effective. Handling interruptions gracefully and remaining productive despite uncertainty.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/time-management/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand time management, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/time-management/personalised" class="path-interventions">
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
    var area = progress['time-management'] || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return area[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights['time-management'];

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Time Management.</strong></p>' +
            '<a href="{{ site.baseurl }}/time-management/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/time-management/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(area).length > 0) {
        var completed = steps.filter(function(s) { return area[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/time-management/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
