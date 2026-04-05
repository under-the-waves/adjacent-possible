---
layout: default
title: Possessions
life_area_slug: possessions
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
    Environment &gt;
    Possessions
</div>

# Possessions

**What it is**
- Your relationship with the physical objects you own – how you acquire, maintain, curate, and let go of the things that fill your daily environment.

**Why it matters**
- The average household contains over 300,000 items, and 54% of people report feeling overwhelmed by clutter. Over a lifetime, the average person spends 3,680 hours searching for misplaced items. Intentional possession management reduces stress, saves time, and frees both physical and mental space.

**Related life areas**
- [Housework]({{ site.baseurl }}/housework/) – your cleaning, tidying, and home maintenance routines
- [Housing]({{ site.baseurl }}/housing/) – your living situation, location, and the physical space you inhabit
- [Food Management]({{ site.baseurl }}/food-management/) – how you plan, shop for, store, and manage food in your household
- [Transportation]({{ site.baseurl }}/transportation/) – how you get around, including vehicle ownership and maintenance

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Possessions yet.</strong><br>It takes about 15 minutes and helps you understand what possessions mean to you.</p>
    <a href="{{ site.baseurl }}/possessions/level-1" class="btn-cta">Start Level 1</a>
</div>

## What people value about possessions

People relate to their possessions for different reasons. This site scores every possessions intervention across four core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Functionality</h3>
<p>Ensuring that the things you own serve clear purposes and support your daily activities effectively. Having the right tools, maintaining them in working order, and ensuring possessions enhance rather than hinder your routines.</p>
</div>

<div class="value-card">
<h3>Simplicity</h3>
<p>Maintaining a curated, manageable collection of possessions that reduces cognitive load. Regular decluttering, resistance to unnecessary acquisition, and a preference for fewer, well-chosen items over abundance.</p>
</div>

<div class="value-card">
<h3>Quality</h3>
<p>Investing in well-made, durable items that provide lasting value. Understanding materials and construction, maintaining items properly, and accepting higher upfront costs for lower lifetime costs.</p>
</div>

<div class="value-card">
<h3>Meaning</h3>
<p>Owning items that carry personal, sentimental, or aesthetic significance beyond mere function. Heirlooms, handmade objects, curated collections, and possessions that tell a story or connect you to people and experiences you value.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/possessions/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand possessions, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/possessions/personalised" class="path-interventions">
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
    var possessions = progress.possessions || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return possessions[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights.possessions;

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Possessions.</strong></p>' +
            '<a href="{{ site.baseurl }}/possessions/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/possessions/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(possessions).length > 0) {
        var completed = steps.filter(function(s) { return possessions[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/possessions/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
