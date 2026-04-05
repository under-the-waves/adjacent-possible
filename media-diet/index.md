---
layout: default
title: Media Diet
life_area_slug: media-diet
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
    Media Diet
</div>

# Media Diet

**What it is**
- The informational content you regularly consume &ndash; news, podcasts, newsletters, non-fiction books, documentaries, and online publications. Your media diet shapes how well-informed you are about the world and provides the raw material for your [worldview]({{ site.baseurl }}/worldview/).

**Why it matters**
- Most people consume information reactively through algorithmic feeds and push notifications, leading to fragmented understanding and poor retention. A deliberately curated media diet improves decision-making, reduces information anxiety, and compounds over time &ndash; the sources you choose today shape the mental models you rely on for years.

**Related life areas**
- [Consumptive Leisure]({{ site.baseurl }}/consumptive-leisure/) &ndash; entertainment media such as fiction, film, and gaming
- [Information Management]({{ site.baseurl }}/information-management/) &ndash; the systems you use to organise, store, and retrieve information
- [Worldview]({{ site.baseurl }}/worldview/) &ndash; the beliefs and mental models built from your information consumption

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Media Diet yet.</strong><br>It takes about 15 minutes and helps you understand what a media diet means to you.</p>
    <a href="{{ site.baseurl }}/media-diet/level-1" class="btn-cta">Start Level 1</a>
</div>

## What people value about media diet

People pursue better information consumption for different reasons. This site scores every media diet intervention across four core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Information Quality & Depth</h3>
<p>The accuracy, nuance, and intellectual rigour of consumed information. Prioritising books over articles, primary sources over summaries, and expert analysis over hot takes.</p>
</div>

<div class="value-card">
<h3>Actionable Relevance</h3>
<p>How directly the information supports decision-making and practical outcomes in your life. Career-relevant developments, investment insights, health discoveries, and information that changes behaviour or choices.</p>
</div>

<div class="value-card">
<h3>Breadth & Discovery</h3>
<p>Exposure to diverse perspectives, unexpected insights, and information outside your existing knowledge areas. Following curiosity into unfamiliar domains and maintaining intellectual openness.</p>
</div>

<div class="value-card">
<h3>Cognitive Efficiency</h3>
<p>Optimising the retention-to-effort ratio and minimising cognitive overhead from information consumption. Choosing formats that match your processing style and avoiding redundant coverage.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/media-diet/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand media diet, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/media-diet/personalised" class="path-interventions">
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
    var mediaDiet = progress['media-diet'] || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return mediaDiet[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights['media-diet'];

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Media Diet.</strong></p>' +
            '<a href="{{ site.baseurl }}/media-diet/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/media-diet/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(mediaDiet).length > 0) {
        var completed = steps.filter(function(s) { return mediaDiet[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/media-diet/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
