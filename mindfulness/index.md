---
layout: default
title: Mindfulness
life_area_slug: mindfulness
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
    Look After Yourself &gt;
    Wellbeing &gt;
    Mindfulness
</div>

# Mindfulness

**What it is**
- Deliberate practices that cultivate present-moment awareness, attention regulation, and non-judgmental observation of thoughts, emotions, and sensations. This includes formal meditation, informal mindfulness integrated into daily activities, contemplative reflection, and embodied awareness techniques.

**Why it matters**
- Regular mindfulness practice improves <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5103185/" target="_blank">attention, working memory, and executive function</a>, reduces stress and anxiety, and builds emotional resilience. People who practise report <a href="https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/1809754" target="_blank">measurable reductions in psychological distress</a> across diverse populations.

**Related life areas**
- [Self-Awareness]({{ site.baseurl }}/self-awareness/) &ndash; understanding your own character, values, motivations, and patterns of thought
- [Mental Health]({{ site.baseurl }}/mental-health/) &ndash; your psychological functioning, emotional balance, and capacity to cope with life's demands
- [Sleep]({{ site.baseurl }}/sleep/) &ndash; your sleep quality, duration, and bedtime routines
- [Behaviours]({{ site.baseurl }}/behaviours/) &ndash; your habitual actions, routines, and behavioural patterns

<div class="la-banner la-banner--start" id="level1Banner">
    <p><strong>You haven't completed Level 1 for Mindfulness yet.</strong><br>It takes about 15 minutes and helps you understand what mindfulness means to you.</p>
    <a href="{{ site.baseurl }}/mindfulness/level-1" class="btn-cta">Start Level 1</a>
</div>

## What people value about mindfulness

People pursue mindfulness for different reasons. This site scores every mindfulness intervention across four core values, and ranks them by how well they deliver on the things you actually care about.

<div class="value-card">
<h3>Mental Clarity</h3>
<p>Enhanced cognitive function including sustained attention, mental focus, and clarity of thinking. Improved concentration at work, reduced mental fog, and greater ability to direct attention deliberately.</p>
</div>

<div class="value-card">
<h3>Emotional Wellbeing</h3>
<p>Increased emotional resilience, reduced reactivity, and greater equanimity during challenging situations. Better stress management, less overwhelm during difficult periods, and the ability to respond rather than react to emotional triggers.</p>
</div>

<div class="value-card">
<h3>Self-Knowledge</h3>
<p>Deeper understanding of your own thought patterns, emotional triggers, habitual behaviours, and unconscious motivations. Insight into why you react certain ways and awareness of previously hidden aspects of your psychology.</p>
</div>

<div class="value-card">
<h3>Spiritual Development</h3>
<p>Connection to meaning, purpose, transcendence, and broader existential questions. Experiences of interconnectedness, development of compassion and loving-kindness, and exploration of consciousness itself.</p>
</div>

<div class="la-paths">
    <a href="{{ site.baseurl }}/mindfulness/level-1" class="path-level1">
        Complete Level 1
        <div class="path-desc">Understand mindfulness, set your values, assess where you are</div>
    </a>
    <a href="{{ site.baseurl }}/mindfulness/personalised" class="path-interventions">
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
    var mindfulness = progress.mindfulness || {};
    var steps = ['why', 'values', 'achievable', 'assess'];
    var done = steps.every(function(s) { return mindfulness[s]; });
    var sliderWeights = APStorage.load('ap-slider-weights') || {};
    var hasSliders = !!sliderWeights.mindfulness;

    if (done && hasSliders) {
        banner.className = 'la-banner la-banner--complete';
        banner.innerHTML = '<p><strong>You have completed Level 1: Awareness in Mindfulness.</strong></p>' +
            '<a href="{{ site.baseurl }}/mindfulness/personalised" class="btn-cta" style="background:#155799;">View Your Interventions</a>' +
            '<a href="{{ site.baseurl }}/mindfulness/level-1" class="btn-secondary">Redo Level 1</a>';
    } else if (Object.keys(mindfulness).length > 0) {
        var completed = steps.filter(function(s) { return mindfulness[s]; }).length;
        if (hasSliders) completed++;
        banner.innerHTML = '<p><strong>Level 1 in progress (' + completed + '/5 steps complete).</strong></p>' +
            '<a href="{{ site.baseurl }}/mindfulness/level-1" class="btn-cta">Continue Level 1</a>';
    }
});
</script>
