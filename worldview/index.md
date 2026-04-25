---
layout: default
title: Worldview
life_area_slug: worldview
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
    Expand Your Awareness &gt;
    Knowledge &gt;
    Worldview
</div>

# Worldview

**What it is**
- Your understanding of how the world works across key domains &ndash; history, economics, psychology, politics, culture, and technology. Worldview is about the mental models and frameworks you use to interpret events, make decisions, and navigate complexity.

**Why it matters**
- People with well-developed worldviews make better predictions, spot manipulation more readily, and navigate uncertainty with greater confidence. Deliberate worldview development is one of the few investments that compounds across every other area of life, yet most people's beliefs are shaped more by social environment than by systematic study.

**Related life areas**
- [Media Diet]({{ site.baseurl }}/media-diet/) &ndash; the informational content you regularly consume, which provides raw material for your worldview
- [Information Management]({{ site.baseurl }}/information-management/) &ndash; the systems you use to organise, store, and retrieve information
- [Rationality]({{ site.baseurl }}/rationality/) &ndash; your ability to think clearly, avoid biases, and reason well

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Worldview yet.</strong><br>It takes about 15 minutes and helps you understand what worldview means to you.</p>
    <a href="{{ site.baseurl }}/worldview/level-1" class="btn-cta">Start Level 1</a>
</div>

{% include level-progression.html %}

## What people value about worldview

People develop their worldviews for different reasons. This site scores every worldview intervention across four core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Breadth</h3>
<p>Developing understanding across multiple domains that shape how the world works &ndash; history, economics, psychology, politics, culture, and technology. Seeing connections between different fields and avoiding blind spots that come from narrow knowledge.</p>
</div>

<div class="value-card">
<h3>Depth</h3>
<p>Building sophisticated, nuanced understanding within specific domains. Mastering fewer areas thoroughly, understanding complex theories, and analysing subtle distinctions rather than maintaining broad but shallow knowledge.</p>
</div>

<div class="value-card">
<h3>Utility</h3>
<p>A worldview that enhances real-world decision-making, prediction, and practical navigation of complex situations. Understanding how systems actually work, not just how they are supposed to work.</p>
</div>

<div class="value-card">
<h3>Meaning</h3>
<p>Understanding that provides psychological grounding, moral framework, and sense of purpose. Coherent narratives about human nature, progress, and your place in the larger story that offer stability during uncertainty.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/worldview/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand worldview, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/worldview/personalised" class="path-interventions">
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
    var worldview = progress.worldview || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return worldview[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights.worldview;

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Worldview.</strong></p>' +
            '<a href="{{ site.baseurl }}/worldview/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/worldview/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(worldview).length > 0) {
        var completed = steps.filter(function(s) { return worldview[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/worldview/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
