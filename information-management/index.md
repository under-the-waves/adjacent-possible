---
layout: default
title: Information Management
life_area_slug: information-management
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
    Information Management
</div>

# Information Management

**What it is**
- How you capture, organise, and retrieve information you need. Information management covers the systems and habits you use to preserve valuable knowledge from reading, conversations, and experience &ndash; and to find it again when it matters.

**Why it matters**
- Knowledge workers spend an estimated 15 &ndash; 30% of their time searching for information, and most people lose the majority of valuable insights from books and articles within weeks of encountering them. Even modest improvements to how you manage information tend to compound over time, improving decision-making across every other life area.

**Related life areas**
- [Media Diet]({{ site.baseurl }}/media-diet/) &ndash; the sources and quality of information you consume
- [Rationality]({{ site.baseurl }}/rationality/) &ndash; your ability to reason clearly and update beliefs based on evidence
- [Worldview]({{ site.baseurl }}/worldview/) &ndash; the beliefs and mental models built from your information consumption
- [Learning Methods]({{ site.baseurl }}/learning-methods/) &ndash; how you acquire and retain new skills and knowledge

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Information Management yet.</strong><br>It takes about 15 minutes and helps you understand what information management means to you.</p>
    <a href="{{ site.baseurl }}/information-management/level-1" class="btn-cta">Start Level 1</a>
</div>

{% include level-progression.html %}

## What people value about information management

People manage information for different reasons. This site scores every information management intervention across four core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Information Retention</h3>
<p>Capturing and preserving valuable insights, ideas, and knowledge from various sources without losing them over time. Comprehensive coverage &ndash; the more you retain, the more valuable your knowledge base becomes.</p>
</div>

<div class="value-card">
<h3>Retrieval Efficiency</h3>
<p>Finding the right information quickly when you need it. Having relevant knowledge accessible at decision points is what makes information management valuable for real-world outcomes.</p>
</div>

<div class="value-card">
<h3>Insight Generation</h3>
<p>Connecting ideas across sources to generate new understanding, identify patterns, and develop original thinking. Systems that help you see relationships between concepts and build coherent mental models.</p>
</div>

<div class="value-card">
<h3>System Simplicity</h3>
<p>Approaches that minimise ongoing cognitive overhead and maintenance burden, whether through minimal analogue systems or highly automated digital setups. An information system that supports your thinking without becoming a project unto itself.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/information-management/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand information management, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/information-management/personalised" class="path-interventions">
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
    var im = progress['information-management'] || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return im[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights['information-management'];

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Information Management.</strong></p>' +
            '<a href="{{ site.baseurl }}/information-management/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/information-management/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(im).length > 0) {
        var completed = steps.filter(function(s) { return im[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/information-management/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
