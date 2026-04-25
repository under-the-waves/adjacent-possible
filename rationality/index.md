---
layout: default
title: Rationality
life_area_slug: rationality
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
    Rationality
</div>

# Rationality

**What it is**
- Your ability to think clearly, form accurate beliefs about the world, and make decisions that reliably achieve your goals. Rationality covers calibration, forecasting, bias recognition, structured decision-making, and intellectual honesty.

**Why it matters**
- Reasoning quality shapes outcomes across every other life area. People who develop systematic approaches to thinking and decision-making tend to make fewer costly mistakes, predict events more accurately, and update their beliefs more effectively when confronted with new evidence.

**Related life areas**
- [Worldview]({{ site.baseurl }}/worldview/) – your mental models, frameworks, and understanding of how the world works
- [Information Management]({{ site.baseurl }}/information-management/) – how you find, filter, organise, and retrieve information
- [Media Diet]({{ site.baseurl }}/media-diet/) – what you read, watch, and listen to, and how it shapes your thinking
- [Cognitive Skills]({{ site.baseurl }}/cognitive-skills/) – memory, focus, processing speed, and other foundational cognitive capacities

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Rationality yet.</strong><br>It takes about 15 minutes and helps you understand what rationality means to you.</p>
    <a href="{{ site.baseurl }}/rationality/level-1" class="btn-cta">Start Level 1</a>
</div>

{% include level-progression.html %}

## What people value about rationality

People develop their thinking for different reasons. This site scores every rationality intervention across three core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Accurate Beliefs</h3>
<p>Developing more accurate beliefs about how the world actually works. Better calibration, more accurate forecasts, appropriate updating on new evidence, and superior mental models for navigating complexity.</p>
</div>

<div class="value-card">
<h3>Effective Decision-Making</h3>
<p>Using clear thinking to achieve your actual goals across all life domains. Avoiding costly mistakes from cognitive biases, developing systematic approaches to complex choices, and improving your track record of successful outcomes.</p>
</div>

<div class="value-card">
<h3>Intellectual Honesty</h3>
<p>Maintaining truthful reasoning processes and admitting uncertainty appropriately. Changing your mind when evidence warrants it, acknowledging the limits of your knowledge, and following arguments where they lead.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/rationality/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand rationality, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/rationality/personalised" class="path-interventions">
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
    var rationality = progress.rationality || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return rationality[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights.rationality;

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Rationality.</strong></p>' +
            '<a href="{{ site.baseurl }}/rationality/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/rationality/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(rationality).length > 0) {
        var completed = steps.filter(function(s) { return rationality[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/rationality/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
