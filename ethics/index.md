---
layout: default
title: Ethics
life_area_slug: ethics
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
    Ethics
</div>

# Ethics

**What it is**
- Your moral principles, the frameworks you use to reason about right and wrong, and how consistently you act on your convictions. Ethics covers both the intellectual work of understanding moral questions and the practical challenge of living according to what you believe.

**Why it matters**
- People with clear ethical frameworks report higher life satisfaction and less decision-making stress, according to <a href="https://psycnet.apa.org/record/2004-16788-000" target="_blank">Peterson &amp; Seligman (2004)</a>. Ethical clarity also tends to strengthen relationships and build trust over time, because others can rely on your consistency. Few investments in self-development touch as many areas of life &ndash; from career decisions to how you treat strangers &ndash; as developing a coherent moral framework and the integrity to follow it.

**Related life areas**
- [Life purpose]({{ site.baseurl }}/life-purpose/) &ndash; your sense of direction, meaning, and overarching life goals
- [Value system]({{ site.baseurl }}/value-system/) &ndash; the principles and values that guide your decisions and priorities
- [Rationality]({{ site.baseurl }}/rationality/) &ndash; your ability to think clearly, avoid biases, and reason well

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Ethics yet.</strong><br>It takes about 15 minutes and helps you understand what ethics means to you.</p>
    <a href="{{ site.baseurl }}/ethics/level-1" class="btn-cta">Start Level 1</a>
</div>

## What people value about ethics

People pursue ethical development for different reasons. This site scores every ethics intervention across four core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Philosophical Depth</h3>
<p>Comprehensive understanding of ethical theories, moral philosophy, and rigorous reasoning about complex moral questions.</p>
</div>

<div class="value-card">
<h3>Practical Guidance</h3>
<p>Clear, actionable ethical frameworks that provide reliable guidance for daily decisions and life choices.</p>
</div>

<div class="value-card">
<h3>Moral Integrity</h3>
<p>Living according to your ethical convictions consistently, even when it requires personal sacrifice, social awkwardness, or going against popular opinion.</p>
</div>

<div class="value-card">
<h3>Community Ethics &amp; Belonging</h3>
<p>Understanding and fulfilling your moral obligations within your communities, families, and relationships whilst contributing to collective moral flourishing.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/ethics/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand ethics, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/ethics/personalised" class="path-interventions">
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
    var ethics = progress.ethics || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return ethics[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights.ethics;

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Ethics.</strong></p>' +
            '<a href="{{ site.baseurl }}/ethics/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/ethics/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(ethics).length > 0) {
        var completed = steps.filter(function(s) { return ethics[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/ethics/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
