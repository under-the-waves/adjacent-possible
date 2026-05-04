---
layout: default
title: Quick Wins
permalink: /prioritisation/quick-wins/
---

<style>
.qw { max-width: 880px; margin: 0 auto; }

.qw-hero h1 {
    margin: 0 0 8px;
    font-size: 1.9em;
    line-height: 1.2;
    color: #111;
}

.qw-hero .lede {
    margin: 0 0 18px;
    font-size: 1.05em;
    line-height: 1.5;
    color: #444;
}

.qw-criteria {
    background: #f8f9fa;
    border: 1px solid #e0e6ed;
    border-radius: 8px;
    padding: 12px 18px;
    margin: 0 0 28px;
    font-size: 0.93em;
}

.qw-criteria > summary {
    cursor: pointer;
    font-weight: 600;
    color: #155799;
    list-style: none;
    padding: 2px 0;
}

.qw-criteria > summary::-webkit-details-marker { display: none; }

.qw-criteria > summary::before {
    content: "▸";
    color: #888;
    margin-right: 6px;
}

.qw-criteria[open] > summary::before { content: "▾"; }

.qw-criteria ul {
    margin: 8px 0 0 0;
    padding-left: 20px;
    line-height: 1.55;
}

.qw-criteria li { margin-bottom: 6px; }

.qw-cadence-section {
    margin-top: 32px;
    margin-bottom: 8px;
}

.qw-cadence-section h2 {
    margin-bottom: 4px;
    color: #155799;
    font-weight: 600;
    font-size: 1.4em;
}

.qw-cadence-blurb {
    color: #555;
    font-size: 0.95em;
    margin-bottom: 16px;
    line-height: 1.5;
}

.qw-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.qw-card {
    background: white;
    border: 1px solid #e0e6ed;
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 12px;
    transition: border-color 0.15s, box-shadow 0.15s;
}

.qw-card:hover {
    border-color: #155799;
    box-shadow: 0 2px 8px rgba(21, 87, 153, 0.08);
}

.qw-card-title {
    font-weight: 600;
    color: #155799;
    text-decoration: none;
    font-size: 1.05em;
}

.qw-card-title:hover {
    text-decoration: underline;
}

.qw-card-summary {
    color: #444;
    font-size: 0.93em;
    margin-top: 6px;
    margin-bottom: 8px;
    line-height: 1.5;
}

.qw-card-meta {
    color: #888;
    font-size: 0.85em;
}

.qw-card-meta strong {
    color: #555;
}

.qw-empty {
    color: #888;
    font-style: italic;
    padding: 12px 0;
}
</style>

<div class="qw">

<div class="qw-hero">
    <h1>Quick Wins</h1>
    <p class="lede">Cheap, fast actions where the cost of not doing them is much higher than the cost of doing them. Most are one-time setups; the rest are annual checks or low-friction routines.</p>
</div>

<details class="qw-criteria">
    <summary>What counts as a Quick Win</summary>
    <ul>
        <li><strong>Trivial cost.</strong> Setup time under a couple of hours, ongoing time under 30 minutes per week (or annual maintenance). Money cost under $100 upfront, under $50 per year ongoing.</li>
        <li><strong>Asymmetric payoff.</strong> The cost of <em>not</em> doing the intervention is much larger than the cost of doing it – usually because of a rare-but-catastrophic downside, or a compounding upside.</li>
        <li><strong>Low regret.</strong> Almost no scenario where doing the intervention turns out to be a mistake. These are not optimisation choices; they're things any rational person would do if reminded.</li>
    </ul>
    <p style="margin-top: 12px; margin-bottom: 0;">Quick Wins live alongside the broader <a href="{{ site.baseurl }}/resources/intervention-database/">intervention database</a>; they're a curated subset surfaced here because they're easy to overlook and easy to act on. Each links to the full intervention page for more detail.</p>
</details>

{% comment %}
Iterate site.data.interventions which Jekyll exposes in alphabetical key order.
For each cadence section, filter to interventions with quick_win flag and the
matching cadence value.
{% endcomment %}

<div class="qw-cadence-section">
    <h2>One-time setups</h2>
    <p class="qw-cadence-blurb">Configure once, benefit indefinitely. The setup itself is the action; there's little or no ongoing maintenance.</p>
    {% assign setup_count = 0 %}
    {% for pair in site.data.interventions %}
        {% if pair[1].quick_win and pair[1].quick_win_cadence == "setup" %}
            {% assign setup_count = setup_count | plus: 1 %}
        {% endif %}
    {% endfor %}
    {% if setup_count > 0 %}
    <ul class="qw-list">
        {% for pair in site.data.interventions %}
            {% assign ikey = pair[0] %}
            {% assign idata = pair[1] %}
            {% if idata.quick_win and idata.quick_win_cadence == "setup" %}
                {% assign url_key = ikey | replace: "_", "-" %}
                <li class="qw-card">
                    <a href="{{ site.baseurl }}/resources/intervention-database/{{ url_key }}" class="qw-card-title">{{ idata.name }}</a>
                    <div class="qw-card-summary">{{ idata.what_it_is | truncatewords: 30 | strip_newlines }}</div>
                    <div class="qw-card-meta">
                        <strong>Setup:</strong> {{ idata.resources.upfront_time }}h, ${{ idata.resources.upfront_cost }} ·
                        <strong>Ongoing:</strong> {% if idata.resources.ongoing_time and idata.resources.ongoing_time > 0 %}{{ idata.resources.ongoing_time }}h/{{ idata.resources.ongoing_time_period }}{% else %}none{% endif %}{% if idata.resources.ongoing_cost and idata.resources.ongoing_cost > 0 %}, ${{ idata.resources.ongoing_cost }}/{{ idata.resources.ongoing_cost_period }}{% endif %}
                    </div>
                </li>
            {% endif %}
        {% endfor %}
    </ul>
    {% else %}
    <p class="qw-empty">No setup-style Quick Wins yet.</p>
    {% endif %}
</div>

<div class="qw-cadence-section">
    <h2>Annual or rare checks</h2>
    <p class="qw-cadence-blurb">Calendar-anchored or once-a-year tasks. Catch drift, refresh equipment, surface gaps before they bite.</p>
    {% assign rare_count = 0 %}
    {% for pair in site.data.interventions %}
        {% if pair[1].quick_win and pair[1].quick_win_cadence == "rare_check" %}
            {% assign rare_count = rare_count | plus: 1 %}
        {% endif %}
    {% endfor %}
    {% if rare_count > 0 %}
    <ul class="qw-list">
        {% for pair in site.data.interventions %}
            {% assign ikey = pair[0] %}
            {% assign idata = pair[1] %}
            {% if idata.quick_win and idata.quick_win_cadence == "rare_check" %}
                {% assign url_key = ikey | replace: "_", "-" %}
                <li class="qw-card">
                    <a href="{{ site.baseurl }}/resources/intervention-database/{{ url_key }}" class="qw-card-title">{{ idata.name }}</a>
                    <div class="qw-card-summary">{{ idata.what_it_is | truncatewords: 30 | strip_newlines }}</div>
                    <div class="qw-card-meta">
                        <strong>Setup:</strong> {{ idata.resources.upfront_time }}h, ${{ idata.resources.upfront_cost }} ·
                        <strong>Ongoing:</strong> {% if idata.resources.ongoing_time and idata.resources.ongoing_time > 0 %}{{ idata.resources.ongoing_time }}h/{{ idata.resources.ongoing_time_period }}{% else %}none{% endif %}{% if idata.resources.ongoing_cost and idata.resources.ongoing_cost > 0 %}, ${{ idata.resources.ongoing_cost }}/{{ idata.resources.ongoing_cost_period }}{% endif %}
                    </div>
                </li>
            {% endif %}
        {% endfor %}
    </ul>
    {% else %}
    <p class="qw-empty">No annual-check Quick Wins yet.</p>
    {% endif %}
</div>

<div class="qw-cadence-section">
    <h2>Built into a routine</h2>
    <p class="qw-cadence-blurb">Low-friction daily or weekly habits that compound. Add them to an existing routine and they fade into the background.</p>
    {% assign routine_count = 0 %}
    {% for pair in site.data.interventions %}
        {% if pair[1].quick_win and pair[1].quick_win_cadence == "routine" %}
            {% assign routine_count = routine_count | plus: 1 %}
        {% endif %}
    {% endfor %}
    {% if routine_count > 0 %}
    <ul class="qw-list">
        {% for pair in site.data.interventions %}
            {% assign ikey = pair[0] %}
            {% assign idata = pair[1] %}
            {% if idata.quick_win and idata.quick_win_cadence == "routine" %}
                {% assign url_key = ikey | replace: "_", "-" %}
                <li class="qw-card">
                    <a href="{{ site.baseurl }}/resources/intervention-database/{{ url_key }}" class="qw-card-title">{{ idata.name }}</a>
                    <div class="qw-card-summary">{{ idata.what_it_is | truncatewords: 30 | strip_newlines }}</div>
                    <div class="qw-card-meta">
                        <strong>Setup:</strong> {{ idata.resources.upfront_time }}h, ${{ idata.resources.upfront_cost }} ·
                        <strong>Ongoing:</strong> {% if idata.resources.ongoing_time and idata.resources.ongoing_time > 0 %}{{ idata.resources.ongoing_time }}h/{{ idata.resources.ongoing_time_period }}{% else %}none{% endif %}{% if idata.resources.ongoing_cost and idata.resources.ongoing_cost > 0 %}, ${{ idata.resources.ongoing_cost }}/{{ idata.resources.ongoing_cost_period }}{% endif %}
                    </div>
                </li>
            {% endif %}
        {% endfor %}
    </ul>
    {% else %}
    <p class="qw-empty">No routine-style Quick Wins yet.</p>
    {% endif %}
</div>

<div class="qw-cadence-section">
    <h2>Where this fits with the rest of the site</h2>
    <p class="qw-cadence-blurb">Quick Wins are a curated subset of the broader <a href="{{ site.baseurl }}/resources/intervention-database/">intervention database</a>, surfaced together because they're easy to overlook. For a fuller picture of what's worth doing for you specifically, complete an <a href="{{ site.baseurl }}/life-areas/">Awareness assessment</a> for the life areas you care about, or run the <a href="{{ site.baseurl }}/prioritisation-survey/">prioritisation survey</a> to identify your binding focus area.</p>
</div>

</div>
