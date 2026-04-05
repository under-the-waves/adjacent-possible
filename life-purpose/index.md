---
layout: default
title: Life Purpose
life_area_slug: life-purpose
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
    Purpose &gt;
    Life Purpose
</div>

# Life Purpose

**What it is**
- Your sense of direction, meaning, and overarching life goals. Life purpose is about knowing what you want your life to be about and why it matters to you.

**Why it matters**
- People with a clear sense of purpose report <a href="https://psycnet.apa.org/record/2016-17273-001" target="_blank">roughly 40% greater resilience</a> during major life stressors and score <a href="https://psycnet.apa.org/record/2009-05474-001" target="_blank">significantly higher</a> on life satisfaction measures. Purpose also appears to improve decision-making quality by providing consistent criteria for evaluating opportunities.

**Related life areas**
- [Ethics]({{ site.baseurl }}/ethics/) &ndash; your moral principles and how you navigate ethical decisions
- [Value System]({{ site.baseurl }}/value-system/) &ndash; your personal values, what you prioritise, and how you resolve trade-offs
- [Self-Awareness]({{ site.baseurl }}/self-awareness/) &ndash; your understanding of your own thoughts, emotions, and behavioural patterns
- [Goals]({{ site.baseurl }}/goals/) &ndash; how you set, track, and achieve specific objectives
- [Career Planning]({{ site.baseurl }}/career-planning/) &ndash; your long-term professional direction and development

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Life Purpose yet.</strong><br>It takes about 15 minutes and helps you understand what life purpose means to you.</p>
    <a href="{{ site.baseurl }}/life-purpose/level-1" class="btn-cta">Start Level 1</a>
</div>

## What people value about life purpose

People develop life purpose for different reasons. This site scores every life purpose intervention across three core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Clarity &amp; Direction</h3>
<p>Having a clear sense of what you want to achieve and why it matters to you personally. Understanding your core motivations, having frameworks for major life decisions, and feeling confident about your chosen path.</p>
</div>

<div class="value-card">
<h3>Meaning &amp; Fulfilment</h3>
<p>The degree to which your life purpose provides deep satisfaction, emotional resonance, and a sense that your existence matters. Feeling that your goals are personally meaningful and experiencing regular fulfilment from working towards your purpose.</p>
</div>

<div class="value-card">
<h3>Integration &amp; Coherence</h3>
<p>How well your life purpose connects with and organises other aspects of your life &ndash; career, relationships, daily activities, and personal growth. Having a purpose that serves as a unifying framework and reduces internal conflict between different life domains.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/life-purpose/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand life purpose, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/life-purpose/personalised" class="path-interventions">
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
    var area = progress['life-purpose'] || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return area[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights['life-purpose'];

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Life Purpose.</strong></p>' +
            '<a href="{{ site.baseurl }}/life-purpose/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/life-purpose/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(area).length > 0) {
        var completed = steps.filter(function(s) { return area[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/life-purpose/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
