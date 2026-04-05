---
layout: default
title: Children
life_area_slug: children
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
    Family &gt;
    Children
</div>

# Children

**What it is**
- Your relationship with your children, or decisions about becoming a parent. The ongoing project of nurturing their health, building your bond with them, supporting their capabilities, and fostering the independence they will need to thrive on their own.

**Why it matters**
- The parent-child relationship predicts lifelong wellbeing more strongly than most other factors. Across more than a thousand studies, parenting practices consistently predict children's mental health outcomes, and the quality of interactive time matters more than the quantity.

**Related life areas**
- [Extended Family]({{ site.baseurl }}/extended-family/) &ndash; your relationships with relatives beyond your immediate household
- [Family of Origin]({{ site.baseurl }}/family-of-origin/) &ndash; your relationship with the family you grew up in

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Children yet.</strong><br>It takes about 15 minutes and helps you understand what parenting means to you.</p>
    <a href="{{ site.baseurl }}/children/level-1" class="btn-cta">Start Level 1</a>
</div>

## What people value about parenting

People approach parenting for different reasons. This site scores every parenting intervention across four core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Wellbeing</h3>
<p>Supporting your child's overall physical, emotional, and psychological health. Creating a stable, nurturing environment, attending to mental health, ensuring adequate sleep and nutrition, and prioritising the child's current happiness alongside future outcomes.</p>
</div>

<div class="value-card">
<h3>Relationship</h3>
<p>The quality of the parent-child bond &ndash; warmth, trust, communication, and genuine connection. Being emotionally available, enjoying time together, knowing your child's inner life, and building a relationship they want to maintain into adulthood.</p>
</div>

<div class="value-card">
<h3>Achievement</h3>
<p>Supporting your child's cognitive, academic, and skill development. Structured enrichment, high expectations communicated warmly, and preparation for future success.</p>
</div>

<div class="value-card">
<h3>Development</h3>
<p>Fostering independence, resilience, and character through age-appropriate challenges and progressively expanding autonomy. Allowing risk-taking, supporting self-direction, and building executive function.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/children/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand parenting, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/children/personalised" class="path-interventions">
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
    var children = progress.children || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return children[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights.children;

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Children.</strong></p>' +
            '<a href="{{ site.baseurl }}/children/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/children/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(children).length > 0) {
        var completed = steps.filter(function(s) { return children[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/children/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
