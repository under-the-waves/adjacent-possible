---
layout: default
title: Relationship Quality
life_area_slug: relationship-quality
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
    Connect with Others &gt;
    Friends and Relationships &gt;
    Relationship Quality
</div>

# Relationship Quality

**What it is**
- The quality of your romantic partnership &ndash; how well you connect, collaborate, and grow together with an intimate partner over time. For finding a partner, leaving a relationship, or building a fulfilling single life, see [Relationship Status]({{ site.baseurl }}/relationship-status/).

**Why it matters**
- Partnership quality is among the strongest predictors of life satisfaction. Satisfaction correlates substantially with communication quality and togetherness, and is shaped more by learnable skills than by initial compatibility alone.

**Related life areas**
- [Sex]({{ site.baseurl }}/sex/) &ndash; your sexual wellbeing, satisfaction, and intimacy
- [Friendship]({{ site.baseurl }}/friendship/) &ndash; the quality and breadth of your non-romantic relationships
- [Communication]({{ site.baseurl }}/communication/) &ndash; your ability to express yourself clearly and listen effectively
- [Mental health]({{ site.baseurl }}/mental-health/) &ndash; your psychological wellbeing and resilience

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Relationship Quality yet.</strong><br>It takes about 15 minutes and helps you understand what relationship quality means to you.</p>
    <a href="{{ site.baseurl }}/relationship-quality/level-1" class="btn-cta">Start Level 1</a>
</div>

{% include level-progression.html %}

## What people value about relationship quality

People pursue relationship quality for different reasons. This site scores every relationship quality intervention across three core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Connection</h3>
<p>Emotional closeness, vulnerability, trust, and deep mutual understanding. Sharing your inner life, feeling genuinely known and accepted, and maintaining emotional and physical intimacy through life's changes.</p>
</div>

<div class="value-card">
<h3>Harmony</h3>
<p>Low-conflict, smoothly functioning daily life together. Constructive disagreement, equitable division of responsibilities, and the ability to navigate differences without erosion of goodwill.</p>
</div>

<div class="value-card">
<h3>Alignment</h3>
<p>Shared values, compatible life goals, and a common vision for the relationship's future. Agreement on major life decisions, compatible priorities, and the sense that you are building towards the same things.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/relationship-quality/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand relationship quality, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/relationship-quality/personalised" class="path-interventions">
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
    var area = progress['relationship-quality'] || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return area[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights['relationship-quality'];

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Relationship Quality.</strong></p>' +
            '<a href="{{ site.baseurl }}/relationship-quality/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/relationship-quality/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(area).length > 0) {
        var completed = steps.filter(function(s) { return area[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/relationship-quality/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
