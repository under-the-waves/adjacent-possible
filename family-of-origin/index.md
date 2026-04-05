---
layout: default
title: Family of Origin
life_area_slug: family-of-origin
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
    Family of Origin
</div>

# Family of Origin

**What it is**
- Your relationships with the people who raised you and your siblings &ndash; parents, stepparents, and anyone else who was part of your core family unit during childhood.

**Why it matters**
- Family of origin relationships create your template for intimacy, conflict resolution, and emotional support. Their quality is one of the strongest predictors of mental health across the lifespan.

**Related life areas**
- [Extended family]({{ site.baseurl }}/extended-family/) &ndash; your relationships with aunts, uncles, cousins, and the wider family network
- [Children]({{ site.baseurl }}/children/) &ndash; your relationship with your children, or decisions about becoming a parent
- [Friendship]({{ site.baseurl }}/friendship/) &ndash; the relationships you build and maintain with people you choose to have in your life
- [Communication]({{ site.baseurl }}/communication/) &ndash; how you express yourself and connect in conversation
- [Mental health]({{ site.baseurl }}/mental-health/) &ndash; your psychological wellbeing and how you manage it

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Family of Origin yet.</strong><br>It takes about 15 minutes and helps you understand what family of origin means to you.</p>
    <a href="{{ site.baseurl }}/family-of-origin/level-1" class="btn-cta">Start Level 1</a>
</div>

## What people value about family of origin

People approach family of origin relationships for different reasons. This site scores every family of origin intervention across four core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Personal Autonomy</h3>
<p>Being true to yourself and setting limits that protect your wellbeing, even when this creates family conflict or guilt. Making life choices based on your own values rather than family expectations.</p>
</div>

<div class="value-card">
<h3>Emotional Connection</h3>
<p>Maintaining close emotional bonds and investing significant time and energy in family relationships. Regular communication, being present for important events, and preserving emotional intimacy.</p>
</div>

<div class="value-card">
<h3>Active Healing</h3>
<p>Working through family dysfunction, addressing past trauma, and pushing for healthier dynamics rather than accepting problematic patterns for the sake of peace.</p>
</div>

<div class="value-card">
<h3>Family Duty</h3>
<p>Fulfilling obligations to family members, providing concrete support, and meeting cultural or family expectations about your role. Financial, practical, and emotional support for those who raised you.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/family-of-origin/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand family of origin, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/family-of-origin/personalised" class="path-interventions">
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
    var areaProgress = progress['family-of-origin'] || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return areaProgress[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights['family-of-origin'];

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Family of Origin.</strong></p>' +
            '<a href="{{ site.baseurl }}/family-of-origin/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/family-of-origin/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(areaProgress).length > 0) {
        var completed = steps.filter(function(s) { return areaProgress[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/family-of-origin/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
