---
layout: default
title: Friendship
life_area_slug: friendship
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
    Friendship
</div>

# Friendship

**What it is**
- The relationships you build and maintain with people you choose to have in your life, including how you invest in those bonds over time.

**Why it matters**
- People with strong friendships have a <a href="https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000316" target="_blank">50% higher likelihood of survival</a> over a given period compared to those with weak social connections – a health effect comparable to quitting smoking.

**Related life areas**
- [Communication]({{ site.baseurl }}/communication/) – how you express yourself and connect in conversation
- [Romantic relationships]({{ site.baseurl }}/romantic-relationships/) – intimate partnerships and their dynamics
- [Community contribution]({{ site.baseurl }}/community-contribution/) – giving back to the groups you belong to
- [Personality]({{ site.baseurl }}/personality/) – your social traits and how others experience you

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Friendship yet.</strong><br>It takes about 15 minutes and helps you understand what friendship means to you.</p>
    <a href="{{ site.baseurl }}/friendship/level-1" class="btn-cta">Start Level 1</a>
</div>

## What people value about friendship

People pursue friendship for different reasons. This site scores every friendship intervention across three core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Depth</h3>
<p>Close friendships with high trust, vulnerability, and mutual understanding. People who lean towards this value invest heavily in a smaller number of relationships where they can be fully themselves.</p>
</div>

<div class="value-card">
<h3>Breadth</h3>
<p>A diverse network of friendships across different contexts and communities. People who lean towards this value build connections with many different kinds of people and maintain relationships across varied settings.</p>
</div>

<div class="value-card">
<h3>Growth</h3>
<p>Friendships that challenge you to improve, learn, and develop as a person. People who lean towards this value seek out friends who hold them accountable and push them to think differently.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/friendship/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand friendship, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/friendship/personalised" class="path-interventions">
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
    var areaProgress = progress.friendship || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return areaProgress[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights.friendship;

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Friendship.</strong></p>' +
            '<a href="{{ site.baseurl }}/friendship/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/friendship/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(areaProgress).length > 0) {
        var completed = steps.filter(function(s) { return areaProgress[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/friendship/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
