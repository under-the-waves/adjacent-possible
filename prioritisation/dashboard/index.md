---
layout: default
title: Life Areas Dashboard
---

<style>
body .main-content {
    max-width: none !important;
    padding: 1rem !important;
}

.dashboard-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
}

.dashboard-header {
    text-align: center;
    margin-bottom: 30px;
}

.dashboard-header h1 {
    font-weight: normal;
    color: #000;
    margin-bottom: 10px;
}

.dashboard-header p {
    color: #555;
    max-width: 700px;
    margin: 0 auto;
}

/* ── Tier selector cards ── */

.tier-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
    max-width: 900px;
    margin: 0 auto 30px;
}

.tier-card {
    border: 2px solid #e0e0e0;
    border-radius: 12px;
    padding: 24px;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s;
    position: relative;
}

.tier-card:hover:not(.disabled) {
    border-color: #4CAF50;
    box-shadow: 0 4px 12px rgba(21,87,153,0.15);
}

.tier-card.disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.tier-card .tier-name {
    font-size: 1.3em;
    font-weight: 600;
    margin-bottom: 6px;
}

.tier-card .tier-time {
    color: #4CAF50;
    font-size: 0.95em;
    margin-bottom: 10px;
}

.tier-card .tier-desc {
    color: #666;
    font-size: 0.85em;
    line-height: 1.4;
}

.tier-card .tier-badge {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 12px;
    font-size: 0.75em;
    font-weight: 600;
    margin-top: 10px;
}

.tier-card .tier-badge.recommended {
    background: #e8f5e9;
    color: #4CAF50;
}

.tier-card .tier-badge.coming-soon {
    background: #f5f5f5;
    color: #999;
}

/* ── Question card ── */

.survey-container {
    max-width: 700px;
    margin: 0 auto;
}

.progress-bar-container {
    margin-bottom: 24px;
}

.progress-bar-outer {
    height: 8px;
    background: #e0e0e0;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 8px;
}

.progress-bar-fill {
    height: 100%;
    border-radius: 4px;
    transition: width 0.3s ease, background-color 0.3s ease;
}

.progress-info {
    display: flex;
    justify-content: space-between;
    font-size: 0.8em;
    color: #666;
}

.pillar-divider {
    text-align: center;
    padding: 30px 20px;
    margin-bottom: 0;
}

.pillar-divider .pillar-divider-name {
    font-size: 1.4em;
    font-weight: 600;
    margin-bottom: 6px;
}

.pillar-divider .pillar-divider-desc {
    color: #666;
    font-size: 0.9em;
}

.question-card {
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 28px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.question-card .q-area-name {
    font-size: 1.2em;
    font-weight: 600;
    margin-bottom: 4px;
}

.question-card .q-domain-name {
    font-size: 0.85em;
    color: #888;
    margin-bottom: 16px;
}

.question-card .q-area-desc {
    font-size: 0.85em;
    color: #666;
    margin-bottom: 16px;
    line-height: 1.4;
}

.question-card .q-prompt {
    font-size: 0.95em;
    color: #444;
    margin-bottom: 16px;
}

.radio-option {
    display: block;
    padding: 12px 16px;
    margin-bottom: 8px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.15s;
    font-size: 0.9em;
    line-height: 1.4;
    color: #333;
}

.radio-option:hover {
    border-color: #4CAF50;
    background: #f8fbff;
}

.radio-option.selected {
    border-color: #4CAF50;
    background: #e8f5e9;
}

.radio-option input[type="radio"] {
    display: none;
}

.radio-option .level-label {
    font-weight: 600;
    color: #4CAF50;
    display: block;
    margin-bottom: 2px;
    font-size: 0.85em;
}

.question-nav {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
    gap: 10px;
}

.question-nav button {
    padding: 10px 24px;
    border: 1px solid #ddd;
    border-radius: 6px;
    background: #f8f9fa;
    cursor: pointer;
    font-size: 0.9em;
    transition: all 0.2s;
}

.question-nav button:hover {
    background: #e9ecef;
}

.question-nav button.btn-primary {
    background: #4CAF50;
    color: white;
    border-color: #4CAF50;
}

.question-nav button.btn-primary:hover {
    background: #2e7d32;
}


/* ── Results grid (reused from original dashboard) ── */

.dashboard-controls {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-bottom: 25px;
    flex-wrap: wrap;
}

.dashboard-controls button {
    padding: 8px 16px;
    border: 1px solid #ddd;
    border-radius: 6px;
    background: #f8f9fa;
    cursor: pointer;
    font-size: 0.9em;
    transition: all 0.2s;
}

.dashboard-controls button:hover {
    background: #e9ecef;
}

.dashboard-controls button.active {
    background: #4CAF50;
    color: white;
    border-color: #4CAF50;
}

.dashboard-controls button.btn-danger {
    color: #c62828;
    border-color: #e0b0b0;
}

.dashboard-controls button.btn-danger:hover {
    background: #c62828;
    color: white;
    border-color: #c62828;
}

.summary-bar {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 30px;
    flex-wrap: wrap;
}

.summary-stat {
    text-align: center;
    padding: 12px 20px;
    background: #f8f9fa;
    border-radius: 8px;
    min-width: 120px;
}

.summary-stat .stat-value {
    font-size: 1.8em;
    font-weight: bold;
    color: #4CAF50;
}

.summary-stat .stat-value.stat-text {
    font-size: 0.95em;
    line-height: 1.2;
    word-break: break-word;
}

.summary-stat .stat-label {
    font-size: 0.8em;
    color: #666;
    margin-top: 4px;
}

.pillar-section {
    margin-bottom: 30px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    overflow: hidden;
}

.pillar-header {
    padding: 12px 20px;
    font-weight: 600;
    font-size: 1.1em;
    color: white;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.pillar-header .pillar-avg {
    font-size: 0.85em;
    opacity: 0.9;
}

.dashboard-container .pillar-header { background: #37474f; }

.pillar-body {
    padding: 15px 20px;
    transition: max-height 0.3s ease, padding 0.3s ease;
    overflow: hidden;
}

.pillar-section.collapsed .pillar-body {
    max-height: 0;
    padding-top: 0;
    padding-bottom: 0;
}

.pillar-header .collapse-icon {
    font-size: 0.8em;
    margin-left: 8px;
    transition: transform 0.3s ease;
}

.pillar-section.collapsed .collapse-icon {
    transform: rotate(-90deg);
}

.domain-group {
    margin-bottom: 15px;
}

.domain-label {
    font-weight: 600;
    color: #555;
    font-size: 0.85em;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
}

.area-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 8px;
}

.area-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    padding: 8px 12px;
    background: #f8f9fa;
    border-radius: 6px;
    border-left: 4px solid #ddd;
    transition: all 0.2s;
}

.area-card:hover {
    background: #e9ecef;
}

.area-card-main {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.area-next-row {
    font-size: 0.75em;
    color: #666;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.area-next-row a {
    color: #4CAF50;
    text-decoration: none;
}

.area-next-row a:hover {
    text-decoration: underline;
}

.area-card.level-0 { border-left-color: #bdbdbd; }
.area-card.level-1 { border-left-color: #e53935; }
.area-card.level-2 { border-left-color: #fb8c00; }
.area-card.level-3 { border-left-color: #fdd835; }
.area-card.level-4 { border-left-color: #43a047; }
.area-card.level-5 { border-left-color: #388e3c; }

.area-name {
    font-size: 0.9em;
    color: #333;
    flex: 1;
}

.area-doing {
    font-size: 0.78em;
    color: #666;
    margin: 0 10px;
    white-space: nowrap;
}

.area-doing.has-progress {
    color: #2a5a32;
    font-weight: 600;
}

.area-pct {
    font-size: 0.78em;
    color: #555;
    margin: 0 6px 0 0;
    white-space: nowrap;
    cursor: help;
}

.dashboard-tip {
    background: #e8f5e9;
    border-left: 4px solid #4CAF50;
    border-radius: 6px;
    padding: 14px 18px;
    margin-bottom: 20px;
    font-size: 0.92em;
    color: #2a5a32;
    line-height: 1.55;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 14px;
}
.dashboard-tip .dashboard-tip-text { flex: 1; min-width: 240px; }
.dashboard-tip strong { color: #1b5e20; }
.dashboard-tip-dismiss {
    padding: 5px 12px;
    background: transparent;
    color: #2a5a32;
    border: 1px solid #4CAF50;
    border-radius: 4px;
    font-size: 0.85em;
    cursor: pointer;
}
.dashboard-tip-dismiss:hover {
    background: #4CAF50;
    color: white;
}

.area-name a {
    color: #333;
    text-decoration: none;
}

.area-name a:hover {
    color: #4CAF50;
    text-decoration: underline;
}

.area-level-badge {
    display: inline-block;
    min-width: 28px;
    height: 28px;
    line-height: 28px;
    text-align: center;
    border-radius: 4px;
    font-size: 0.8em;
    font-weight: 600;
    color: white;
}

.area-level-badge.lb-0 { background: #bdbdbd; }
.area-level-badge.lb-1 { background: #e53935; }
.area-level-badge.lb-2 { background: #fb8c00; }
.area-level-badge.lb-3 { background: #fdd835; color: #333; }
.area-level-badge.lb-4 { background: #43a047; }
.area-level-badge.lb-5 { background: #388e3c; }

.area-level-badge.propagated {
    font-style: italic;
    opacity: 0.75;
}

.level-legend {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-bottom: 20px;
    flex-wrap: wrap;
    font-size: 0.8em;
    color: #666;
}

.legend-item {
    display: flex;
    align-items: center;
    gap: 4px;
}

.legend-dot {
    width: 12px;
    height: 12px;
    border-radius: 3px;
}

/* ── Weight sliders (Tier 3) ── */

/* ── Responsive ── */

@media (max-width: 768px) {
    .area-grid {
        grid-template-columns: 1fr;
    }

    .summary-bar {
        gap: 10px;
    }

    .summary-stat {
        min-width: 80px;
        padding: 8px 12px;
    }

    .tier-cards {
        grid-template-columns: 1fr;
    }

    .question-card {
        padding: 20px;
    }
}
</style>

<div class="dashboard-container">
    <div id="viewLanding" style="display:none;"></div>
    <div id="viewSurvey" style="display:none;"></div>
    <div id="viewResults" style="display:none;"></div>
</div>

<script>
// ── YAML data embedded via Liquid ──
const SURVEY_DATA = {
{% for area in site.data.life_areas %}
    '{{ area[0] }}': {{ area[1] | jsonify }},
{% endfor %}
};

// Intervention data – only the fields needed to compute personalised top-5 per
// life area. Keys are intervention slugs; values: applicable_domains list and
// per-value PBS/ISR/UAR/confidence triples.
const INTERVENTIONS = {
{% for entry in site.data.interventions %}
    {% assign slug = entry[0] %}
    {% assign data = entry[1] %}
    '{{ slug }}': {
        name: {{ data.name | jsonify }},
        applicable_domains: {{ data.applicable_domains | default: '' | jsonify }},
        values: {
            {% for vp in data.values %}
            '{{ vp[0] }}': { pbs: {{ vp[1].pbs }}, isr: {{ vp[1].isr }}, uar: {{ vp[1].uar }}, conf: {{ vp[1].confidence | default: 'medium' | jsonify }} }{% unless forloop.last %},{% endunless %}
            {% endfor %}
        }
    }{% unless forloop.last %},{% endunless %}
{% endfor %}
};

// Confidence factors and the EBS / WBS formulas, mirroring _layouts/personalised.html
// exactly so the dashboard ranking matches what users see on each personalised page.
const CONF_FACTORS = { high: 1.0, medium: 0.75, low: 0.5 };

function computeEbsForRanking(pbs, isr, uar, conf) {
    var sign = Math.sign(pbs);
    if (sign === 0) return 0;
    var pbsMag = Math.pow(2, Math.abs(pbs)) - 1;
    var linearEv = sign * pbsMag * (isr / 100) * (uar / 100) * (CONF_FACTORS[conf] || 0.75);
    return Math.sign(linearEv) * Math.log2(1 + Math.abs(linearEv));
}

// Read slider weights for an area; if none, fall back to equal weights across
// the area's scored values. Output is a {fullKey: weight_percent} map.
function userValuesForArea(areaSlug) {
    var sliderWeights = (typeof APStorage !== 'undefined')
        ? APStorage.load('ap-slider-weights') : null;
    if (!sliderWeights) sliderWeights = {};
    var areaSliders = sliderWeights[areaSlug] || {};

    // Discover the area's value keys by scanning the interventions library.
    var valueKeys = new Set();
    Object.values(INTERVENTIONS).forEach(function(itv) {
        Object.keys(itv.values).forEach(function(fk) {
            if (fk.indexOf(areaSlug + '.') === 0) valueKeys.add(fk);
        });
    });
    var keys = Array.from(valueKeys);
    if (keys.length === 0) return {};

    var map = {};
    var hasAnySliderForArea = keys.some(function(k) {
        var vName = k.substring(areaSlug.length + 1);
        return typeof areaSliders[vName] === 'number';
    });
    if (hasAnySliderForArea) {
        keys.forEach(function(k) {
            var vName = k.substring(areaSlug.length + 1);
            map[k] = (typeof areaSliders[vName] === 'number') ? areaSliders[vName] : 0;
        });
    } else {
        var eq = 100 / keys.length;
        keys.forEach(function(k) { map[k] = eq; });
    }
    return map;
}

// Weighted Benefit Score for an intervention against an area's user weights.
function computeWbsForArea(intervention, userValues) {
    var wbs = 0;
    Object.keys(userValues).forEach(function(k) {
        var v = intervention.values[k];
        if (!v) return;
        var weight = userValues[k] / 100;
        wbs += computeEbsForRanking(v.pbs, v.isr, v.uar, v.conf) * weight;
    });
    return wbs;
}

// Top 5 intervention slugs for a life area, ranked by user-weighted WBS.
function topInterventionsForArea(areaSlug) {
    var userValues = userValuesForArea(areaSlug);
    var candidates = [];
    Object.keys(INTERVENTIONS).forEach(function(slug) {
        var itv = INTERVENTIONS[slug];
        var domains = itv.applicable_domains || [];
        if (domains.indexOf(areaSlug) === -1) return;
        var wbs = computeWbsForArea(itv, userValues);
        if (wbs > 0) candidates.push({ slug: slug, wbs: wbs });
    });
    candidates.sort(function(a, b) { return b.wbs - a.wbs; });
    return candidates.slice(0, 5).map(function(c) { return c.slug; });
}

// Highest-WBS intervention for an area that the user isn't already doing
// (tier < 2). Returns { slug, name } or null when nothing qualifies.
// Surfaces a concrete next action on the dashboard so band+percentile data
// translates into an actual click target.
function topNotDoingForArea(areaSlug) {
    var userValues = userValuesForArea(areaSlug);
    var tierMap = {};
    try {
        var raw = localStorage.getItem('ap-habits-tier');
        if (raw) tierMap = JSON.parse(raw);
    } catch (e) {}
    var best = null;
    Object.keys(INTERVENTIONS).forEach(function(slug) {
        var itv = INTERVENTIONS[slug];
        var domains = itv.applicable_domains || [];
        if (domains.indexOf(areaSlug) === -1) return;
        var t = tierMap[slug];
        if (typeof t === 'number' && t >= 2) return;
        var wbs = computeWbsForArea(itv, userValues);
        if (wbs <= 0) return;
        if (!best || wbs > best.wbs) best = { slug: slug, name: itv.name, wbs: wbs };
    });
    return best;
}

function interventionUrl(slug) {
    return '{{ site.baseurl }}/resources/intervention-database/' + slug.replace(/_/g, '-');
}

// Load per-area, per-value percentile estimates from the Awareness assessment.
// Shape: { areaSlug: { valueKey: percentile } }. Returns {} when the user hasn't
// completed any per-area assessments yet.
function loadPercentileScores() {
    try {
        var raw = localStorage.getItem('ap-level1-scores');
        return raw ? JSON.parse(raw) : {};
    } catch (e) { return {}; }
}

// Mean percentile for an area, treating "answered" values only. Returns null
// when the user has no assessment data for the area, so callers can decide how
// to handle the absence (sort neutrally vs. hide).
function averagePercentileForArea(slug, allScores) {
    var scores = allScores && allScores[slug];
    if (!scores) return null;
    var nums = [];
    Object.keys(scores).forEach(function(k) {
        var n = scores[k];
        if (typeof n === 'number' && !isNaN(n)) nums.push(n);
    });
    if (nums.length === 0) return null;
    return nums.reduce(function(s, n) { return s + n; }, 0) / nums.length;
}

// Count how many of a slug list the user is doing at tier >= 2.
function countDoingFromList(slugs) {
    var tierMap = {};
    try {
        var raw = localStorage.getItem('ap-habits-tier');
        if (raw) tierMap = JSON.parse(raw);
    } catch (e) {}
    return slugs.reduce(function(acc, slug) {
        var t = tierMap[slug];
        return acc + ((typeof t === 'number' && t >= 2) ? 1 : 0);
    }, 0);
}

// ── Layout ordering ──
const PILLARS = [
    {
        name: "Expand Your Awareness",
        class: "pillar-1",
        color: "#6a1b9a",
        domains: [
            { name: "Values", areas: [
                { slug: "self-awareness", label: "Self-awareness" },
                { slug: "value-system", label: "Value system" }
            ]},
            { name: "Purpose", areas: [
                { slug: "life-purpose", label: "Life purpose" },
                { slug: "ethics", label: "Ethics" }
            ]},
            { name: "Knowledge", areas: [
                { slug: "media-diet", label: "Media diet" },
                { slug: "information-management", label: "Information management" },
                { slug: "worldview", label: "Worldview" },
                { slug: "rationality", label: "Rationality" }
            ]},
            { name: "Learning", areas: [
                { slug: "cognitive-skills", label: "Cognitive skills" },
                { slug: "life-skills", label: "Life skills" },
                { slug: "learning-methods", label: "Learning methods" }
            ]}
        ]
    },
    {
        name: "Look After Yourself",
        class: "pillar-2",
        color: "#388e3c",
        domains: [
            { name: "Health", areas: [
                { slug: "fitness", label: "Fitness" },
                { slug: "nutrition", label: "Nutrition" },
                { slug: "sleep", label: "Sleep" },
                { slug: "health-management", label: "Health management" }
            ]},
            { name: "Wellbeing", areas: [
                { slug: "mindfulness", label: "Mindfulness" },
                { slug: "mental-health", label: "Mental health" },
                { slug: "behaviours", label: "Behaviours" }
            ]},
            { name: "Security", areas: [
                { slug: "physical-safety", label: "Physical safety" },
                { slug: "emergency-preparedness", label: "Emergency preparedness" },
                { slug: "digital-safety", label: "Digital safety" },
                { slug: "legal-matters", label: "Legal matters" }
            ]}
        ]
    },
    {
        name: "Connect with Others",
        class: "pillar-3",
        color: "#2e7d32",
        domains: [
            { name: "Expression", areas: [
                { slug: "body-image", label: "Body image" },
                { slug: "style", label: "Style" },
                { slug: "personality", label: "Personality" },
                { slug: "communication", label: "Communication" }
            ]},
            { name: "Family", areas: [
                { slug: "family-of-origin", label: "Family of origin" },
                { slug: "extended-family", label: "Extended family" },
                { slug: "children", label: "Children" }
            ]},
            { name: "Friends and Relationships", areas: [
                { slug: "friendship", label: "Friendship" },
                { slug: "relationship-status", label: "Relationship Status" },
                { slug: "relationship-quality", label: "Relationship Quality" },
                { slug: "sex", label: "Sex" }
            ]}
        ]
    },
    {
        name: "Organise Your Life",
        class: "pillar-4",
        color: "#e65100",
        domains: [
            { name: "Environment", areas: [
                { slug: "housing", label: "Housing" },
                { slug: "possessions", label: "Possessions" },
                { slug: "transportation", label: "Transportation" },
                { slug: "housework", label: "Housework" }
            ]},
            { name: "Finances", areas: [
                { slug: "financial-planning-tracking", label: "Planning and tracking" },
                { slug: "saving", label: "Saving" },
                { slug: "investing", label: "Investing" }
            ]},
            { name: "Productivity", areas: [
                { slug: "organisation", label: "Organisation" },
                { slug: "systems", label: "Systems" },
                { slug: "time-management", label: "Time management" },
                { slug: "goals", label: "Goals" },
                { slug: "habits", label: "Habits" }
            ]}
        ]
    },
    {
        name: "Create & Contribute",
        class: "pillar-5",
        color: "#c62828",
        domains: [
            { name: "Career", areas: [
                { slug: "current-work", label: "Current work" },
                { slug: "career-planning", label: "Career planning" },
                { slug: "networks", label: "Networks" }
            ]},
            { name: "Leisure", areas: [
                { slug: "participatory-leisure", label: "Participatory leisure" },
                { slug: "consumptive-leisure", label: "Consumptive leisure" }
            ]},
            { name: "Impact", areas: [
                { slug: "global-impact", label: "Global impact" },
                { slug: "community-contribution", label: "Community contribution" }
            ]}
        ]
    }
];

const LEVEL_NAMES = ['Not assessed', 'Awareness', 'Top 20%', 'Top 5%', 'Top 1%', 'Top 0.1%'];
const LEVEL_COLORS = ['#bdbdbd', '#e53935', '#fb8c00', '#fdd835', '#43a047', '#388e3c'];

// ── Storage (via APStorage abstraction) ──
function loadLevels() { return APStorage.load('ap-dashboard-levels') || {}; }
function saveLevels(levels) { APStorage.save('ap-dashboard-levels', levels); }
function loadTier() { return APStorage.load('ap-survey-tier') || 0; }
function saveTier(t) { APStorage.save('ap-survey-tier', t); }
function loadResponses() { return APStorage.load('ap-survey-responses') || {}; }
function saveResponses(r) { APStorage.save('ap-survey-responses', r); }

// ── Helpers ──

function getPrimaryValue(slug) {
    const data = SURVEY_DATA[slug];
    if (!data || !data.values) return null;
    // Highest-weight value that has benchmarks
    let best = null;
    for (const v of data.values) {
        if (v.benchmarks && v.benchmarks.level_1) {
            if (!best || v.weight > best.weight) best = v;
        }
    }
    return best;
}

function areaBenchmarks(slug) {
    const pv = getPrimaryValue(slug);
    if (!pv) return null;
    return pv.benchmarks;
}

function areaHasBenchmarks(slug) {
    return !!areaBenchmarks(slug);
}

function isDomainRep(slug) {
    const data = SURVEY_DATA[slug];
    return data && data.domain_representative === true;
}

function getAllAreas() {
    const areas = [];
    PILLARS.forEach(p => p.domains.forEach(d => d.areas.forEach(a => areas.push(a))));
    return areas;
}

function getDomainForSlug(slug) {
    for (const p of PILLARS) {
        for (const d of p.domains) {
            for (const a of d.areas) {
                if (a.slug === slug) return { pillar: p, domain: d };
            }
        }
    }
    return null;
}

// ── Question generation ──

function getQuestions(tier) {
    const questions = [];
    PILLARS.forEach((pillar, pi) => {
        // Add pillar divider
        questions.push({ type: 'divider', pillar: pillar });
        pillar.domains.forEach(domain => {
            domain.areas.forEach(area => {
                if (tier === 1) {
                    // Tier 1: domain representatives only
                    if (!isDomainRep(area.slug)) return;
                    if (!areaHasBenchmarks(area.slug)) return;
                    const pv = getPrimaryValue(area.slug);
                    questions.push({
                        type: 'question',
                        slug: area.slug,
                        label: area.label,
                        domain: domain.name,
                        pillar: pillar,
                        valueName: pv.name,
                        benchmarks: pv.benchmarks,
                        propagate: true
                    });
                } else if (tier === 2) {
                    // Tier 2: all areas with benchmarks, primary value only
                    if (!areaHasBenchmarks(area.slug)) return;
                    const pv = getPrimaryValue(area.slug);
                    questions.push({
                        type: 'question',
                        slug: area.slug,
                        label: area.label,
                        domain: domain.name,
                        pillar: pillar,
                        valueName: pv.name,
                        benchmarks: pv.benchmarks,
                        propagate: false
                    });
                } else if (tier === 3) {
                    // Tier 3: all areas, all values with benchmarks
                    const data = SURVEY_DATA[area.slug];
                    if (!data) return;
                    const valuesWithBench = data.values.filter(v => v.benchmarks && v.benchmarks.level_1);
                    if (valuesWithBench.length === 0) return;
                    valuesWithBench.forEach(v => {
                        questions.push({
                            type: 'question',
                            slug: area.slug,
                            label: area.label,
                            domain: domain.name,
                            pillar: pillar,
                            valueName: v.name,
                            valueKey: v.key,
                            benchmarks: v.benchmarks,
                            propagate: false,
                            tier3: true
                        });
                    });
                }
            });
        });
    });
    // Remove trailing/leading dividers with no questions after them
    return cleanDividers(questions);
}

function cleanDividers(questions) {
    const cleaned = [];
    for (let i = 0; i < questions.length; i++) {
        if (questions[i].type === 'divider') {
            // Only keep if there's a non-divider after it
            let hasContent = false;
            for (let j = i + 1; j < questions.length; j++) {
                if (questions[j].type === 'divider') break;
                hasContent = true;
                break;
            }
            if (hasContent) cleaned.push(questions[i]);
        } else {
            cleaned.push(questions[i]);
        }
    }
    return cleaned;
}

// ── Survey state ──
let surveyQuestions = [];
let surveyIndex = 0;
let surveyAnswers = {};  // slug -> level (tier 1/2) or slug:valueKey -> level (tier 3)
let currentTier = 0;

// ── Views ──

function showView(name) {
    document.getElementById('viewLanding').style.display = name === 'landing' ? '' : 'none';
    document.getElementById('viewSurvey').style.display = name === 'survey' ? '' : 'none';
    document.getElementById('viewResults').style.display = name === 'results' ? '' : 'none';
}

// ── LANDING ──

function renderLanding() {
    const hasResults = Object.keys(loadLevels()).length > 0;
    if (hasResults) {
        renderResults();
        showView('results');
        return;
    }

    const el = document.getElementById('viewLanding');
    el.innerHTML = `
        <div class="dashboard-header">
            <h1>Life Areas Assessment</h1>
            <p>Assess your current level across ${getAllAreas().length} life areas. Choose a survey depth that suits you.</p>
        </div>
        <div class="tier-cards">
            <div class="tier-card" onclick="startSurvey(1)">
                <div class="tier-name">Quick</div>
                <div class="tier-time">~2 minutes</div>
                <div class="tier-desc">One question per domain (16 questions). Your answer is applied to all areas in that domain.</div>
            </div>
            <div class="tier-card" onclick="startSurvey(2)">
                <div class="tier-name">Standard</div>
                <div class="tier-time">~10 minutes</div>
                <div class="tier-desc">One question per life area, using the most important value for each. Covers all areas with benchmarks.</div>
                <span class="tier-badge recommended">Recommended</span>
            </div>
            <div class="tier-card" onclick="startSurvey(3)">
                <div class="tier-name">Detailed</div>
                <div class="tier-time">~30 minutes</div>
                <div class="tier-desc">Multiple questions per life area (one per value). Optional weight adjustment. Most precise scoring.</div>
            </div>
        </div>
    `;
    showView('landing');
}

// ── SURVEY ──

function startSurvey(tier) {
    currentTier = tier;
    saveTier(tier);
    surveyQuestions = getQuestions(tier);
    surveyIndex = 0;
    surveyAnswers = {};
    renderIntro();
    showView('survey');
}

function renderIntro() {
    const el = document.getElementById('viewSurvey');
    const questionCount = surveyQuestions.filter(x => x.type === 'question').length;
    const areaCount = new Set(surveyQuestions.filter(x => x.type === 'question').map(x => x.slug)).size;
    const scopeLabel = currentTier === 3
        ? `<strong>${questionCount} values</strong> across <strong>${areaCount} life areas</strong>`
        : `<strong>${questionCount} life areas</strong>`;
    el.innerHTML = `<div class="survey-container">
        <div class="question-card">
            <h2 style="margin-top:0;">Before you begin</h2>
            <p>This survey assesses your current band across ${scopeLabel}. For each area, pick the description that best matches where you are right now.</p>
            <h3>What the bands mean</h3>
            <p>The five bands correspond to population percentiles among American adults:</p>
            <ul style="line-height:1.8;">
                <li><strong>Awareness:</strong> You know this area exists and have basic awareness.</li>
                <li><strong>Top 20%:</strong> Solid basics in place.</li>
                <li><strong>Top 5%:</strong> Notably more capable than most people.</li>
                <li><strong>Top 1%:</strong> Exceptional capability.</li>
                <li><strong>Top 0.1%:</strong> Roughly 1 in 1,000 people.</li>
            </ul>
            <p style="color:#555;"><strong>Most people sit in the lower bands across most life areas.</strong> That is completely normal &ndash; there simply is not enough time in life to excel at everything. The purpose of this survey is not to score highly. It is to identify where you are now so you can decide where to focus.</p>
            <div class="question-nav" style="margin-top:24px;">
                <button onclick="renderLanding(); showView('landing');">Back</button>
                <button class="btn-primary" onclick="renderQuestion()">Begin survey</button>
            </div>
        </div>
    </div>`;
}

function renderQuestion() {
    const el = document.getElementById('viewSurvey');

    if (surveyIndex >= surveyQuestions.length) {
        finishSurvey();
        return;
    }

    const q = surveyQuestions[surveyIndex];
    const totalQ = surveyQuestions.filter(x => x.type === 'question').length;
    const answeredQ = surveyQuestions.slice(0, surveyIndex).filter(x => x.type === 'question').length;

    let html = '<div class="survey-container">';

    // Progress bar
    const pct = totalQ > 0 ? Math.round((answeredQ / totalQ) * 100) : 0;
    html += `<div class="progress-bar-container">
        <div class="progress-bar-outer">
            <div class="progress-bar-fill" style="width:${pct}%; background:#4CAF50;"></div>
        </div>
        <div class="progress-info">
            <span>${answeredQ} of ${totalQ}</span>
            <span>${q.pillar ? q.pillar.name : ''}</span>
        </div>
    </div>`;

    if (q.type === 'divider') {
        html += `<div class="pillar-divider" style="color:#37474f;">
            <div class="pillar-divider-name">${q.pillar.name}</div>
            <div class="pillar-divider-desc">Next section</div>
        </div>
        <div class="question-nav">
            <div></div>
            <button class="btn-primary" onclick="surveyIndex++; renderQuestion();">Continue</button>
        </div>`;
    } else {
        // Question card
        const answerKey = q.tier3 ? q.slug + ':' + q.valueKey : q.slug;
        const currentAnswer = surveyAnswers[answerKey];

        const areaDesc = SURVEY_DATA[q.slug] && SURVEY_DATA[q.slug].survey_description ? SURVEY_DATA[q.slug].survey_description : '';
        html += `<div class="question-card">
            <div class="q-area-name">${q.label}</div>
            <div class="q-domain-name">${q.domain} ${q.tier3 ? ' -- ' + q.valueName : ''}</div>
            ${areaDesc ? '<div class="q-area-desc">' + areaDesc + '</div>' : ''}
            <div class="q-prompt">Which best describes you?</div>`;

        // "I'm not sure" option
        html += `<label class="radio-option${currentAnswer === -1 ? ' selected' : ''}" onclick="selectAnswer('${answerKey}', -1)">
            <input type="radio" name="q-${surveyIndex}" value="-1" ${currentAnswer === -1 ? 'checked' : ''}>
            <span class="level-label">I'm not sure</span>
            I haven't thought about this, or I'm not sure where I stand.
        </label>`;

        for (let lvl = 1; lvl <= 5; lvl++) {
            const bKey = 'level_' + lvl;
            const bench = q.benchmarks[bKey];
            if (!bench) continue;
            const sel = currentAnswer === lvl ? ' selected' : '';
            html += `<label class="radio-option${sel}" onclick="selectAnswer('${answerKey}', ${lvl})">
                <input type="radio" name="q-${surveyIndex}" value="${lvl}" ${currentAnswer === lvl ? 'checked' : ''}>
                <span class="level-label">${LEVEL_NAMES[lvl]}</span>
                ${bench.text}
            </label>`;
        }

        html += `</div>`;
        const notAnswered = surveyAnswers[answerKey] === undefined;
        html += `<div class="question-nav">
            ${surveyIndex > 0 ? '<button onclick="surveyBack()">Back</button>' : '<div></div>'}
            <button class="btn-primary" onclick="nextQuestion()" ${notAnswered ? 'disabled style="opacity:0.5;cursor:not-allowed;"' : ''} id="btnNext">Next</button>
        </div>`;
    }

    html += '</div>';
    el.innerHTML = html;
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

let autoAdvanceTimer = null;

function selectAnswer(key, level) {
    if (autoAdvanceTimer) clearTimeout(autoAdvanceTimer);
    surveyAnswers[key] = level;
    renderQuestion();
    autoAdvanceTimer = setTimeout(() => {
        autoAdvanceTimer = null;
        surveyIndex++;
        renderQuestion();
    }, 350);
}

function skipQuestion(key) {
    if (autoAdvanceTimer) clearTimeout(autoAdvanceTimer);
    delete surveyAnswers[key];
    surveyIndex++;
    renderQuestion();
}

function nextQuestion() {
    surveyIndex++;
    renderQuestion();
}

function surveyBack() {
    if (autoAdvanceTimer) clearTimeout(autoAdvanceTimer);
    if (surveyIndex > 0) surveyIndex--;
    renderQuestion();
}

// ── Finish survey ──

function finishSurvey() {
    const levels = loadLevels();
    const tier = currentTier;

    if (tier === 1) {
        // Propagate domain representative answers to all areas in domain
        for (const [slug, level] of Object.entries(surveyAnswers)) {
            if (level === -1) continue; // "I'm not sure" -- skip
            const info = getDomainForSlug(slug);
            if (info) {
                info.domain.areas.forEach(a => {
                    levels[a.slug] = level;
                    // Mark propagated
                    if (a.slug !== slug) {
                        levels['_propagated_' + a.slug] = true;
                    } else {
                        delete levels['_propagated_' + a.slug];
                    }
                });
            }
        }
    } else if (tier === 2) {
        for (const [slug, level] of Object.entries(surveyAnswers)) {
            if (level === -1) continue; // "I'm not sure" -- skip
            levels[slug] = level;
            delete levels['_propagated_' + slug];
        }
    } else if (tier === 3) {
        // Weighted average per area
        const areaScores = {};  // slug -> [{level, weight}]

        for (const [key, level] of Object.entries(surveyAnswers)) {
            if (level === -1) continue; // "I'm not sure" -- skip
            const parts = key.split(':');
            const slug = parts[0];
            const valueKey = parts[1];
            if (!areaScores[slug]) areaScores[slug] = [];

            const data = SURVEY_DATA[slug];
            const v = data ? data.values.find(x => x.key === valueKey) : null;
            const weight = v ? v.weight : 1;
            areaScores[slug].push({ level, weight });
        }

        for (const [slug, scores] of Object.entries(areaScores)) {
            const totalWeight = scores.reduce((s, x) => s + x.weight, 0);
            if (totalWeight > 0) {
                const avg = scores.reduce((s, x) => s + x.level * x.weight, 0) / totalWeight;
                levels[slug] = Math.round(avg);
                delete levels['_propagated_' + slug];
            }
        }
    }

    saveLevels(levels);
    saveResponses(surveyAnswers);
    renderResults();
    showView('results');
}

// ── RESULTS ──

function renderResults() {
    const levels = loadLevels();
    const percentileScores = loadPercentileScores();
    const el = document.getElementById('viewResults');
    const baseUrl = '{{ site.baseurl }}';

    let totalAssessed = 0, totalLevel = 0;
    // Track assessed areas to compute lowest/highest with percentile tiebreaks.
    // Plain level comparison ties when multiple areas share a band, which is
    // common after the Quick survey or after only completing per-area
    // Awareness assessments (which always land at band 1).
    const assessedAreas = [];

    let gridHTML = '';
    PILLARS.forEach(pillar => {
        let pillarTotal = 0, pillarCount = 0;
        let bodyHTML = '<div class="pillar-body">';

        pillar.domains.forEach(domain => {
            bodyHTML += `<div class="domain-group"><div class="domain-label">${domain.name}</div><div class="area-grid">`;
            domain.areas.forEach(area => {
                const level = levels[area.slug] || 0;
                const propagated = levels['_propagated_' + area.slug];
                const pct = averagePercentileForArea(area.slug, percentileScores);

                if (level > 0) {
                    totalAssessed++;
                    totalLevel += level;
                    pillarTotal += level;
                    pillarCount++;
                    assessedAreas.push({ name: area.label, level: level, pct: pct });
                }

                const propClass = propagated ? ' propagated' : '';
                const pctLabel = pct != null ? `<span class="area-pct" title="Average percentile across your Awareness assessment answers for this area.">~${Math.round(pct)}th</span>` : '';
                const badgeTitle = level > 0
                    ? LEVEL_NAMES[level] + (propagated ? ' (estimated)' : '') + (pct != null ? ' &middot; ~' + Math.round(pct) + 'th percentile' : '')
                    : '';
                const badge = level > 0
                    ? `<span class="area-level-badge lb-${level}${propClass}" title="${badgeTitle}">${level}</span>`
                    : `<span class="area-level-badge lb-0">-</span>`;

                const top5 = topInterventionsForArea(area.slug);
                const doingCount = countDoingFromList(top5);
                const doingClass = doingCount > 0 ? 'area-doing has-progress' : 'area-doing';
                const doingTitle = top5.length === 0
                    ? 'No scored interventions found for this life area.'
                    : 'Top 5 interventions for this life area, weighted by your priorities: ' + top5.map(s => INTERVENTIONS[s].name).join('; ');
                const doingLabel = top5.length === 0
                    ? ''
                    : `<span class="${doingClass}" title="${doingTitle}">Doing ${doingCount} of ${top5.length}</span>`;

                const nextItv = topNotDoingForArea(area.slug);
                const nextRow = nextItv
                    ? `<div class="area-next-row" title="Highest-WBS intervention you're not yet doing for this area.">Try next: <a href="${interventionUrl(nextItv.slug)}">${nextItv.name}</a></div>`
                    : '';

                bodyHTML += `<div class="area-card level-${level}">
                    <div class="area-card-main">
                        <span class="area-name"><a href="${baseUrl}/${area.slug}/">${area.label}</a></span>
                        ${nextRow}
                    </div>
                    ${doingLabel}
                    ${pctLabel}
                    ${badge}
                </div>`;
            });
            bodyHTML += '</div></div>';
        });
        bodyHTML += '</div>';

        const avg = pillarCount > 0 ? (pillarTotal / pillarCount).toFixed(1) : '--';
        gridHTML += `<div class="pillar-section ${pillar.class}">
            <div class="pillar-header" onclick="togglePillar(this)">
                <span>${pillar.name} <span class="collapse-icon">&#9660;</span></span>
                <span class="pillar-avg">Avg: ${avg}</span>
            </div>${bodyHTML}</div>`;
    });

    // Sort ascending by (level, percentile) so lowest is first and highest is
    // last. Missing percentile is treated as the band's midpoint (50) so areas
    // without assessment data fall neutrally rather than sinking to the floor.
    assessedAreas.sort(function(a, b) {
        if (a.level !== b.level) return a.level - b.level;
        var ap = a.pct == null ? 50 : a.pct;
        var bp = b.pct == null ? 50 : b.pct;
        return ap - bp;
    });
    const lowest = assessedAreas.length > 0
        ? { name: assessedAreas[0].name, level: assessedAreas[0].level }
        : { name: '', level: 6 };
    const highest = assessedAreas.length > 0
        ? { name: assessedAreas[assessedAreas.length - 1].name, level: assessedAreas[assessedAreas.length - 1].level }
        : { name: '', level: 0 };

    const totalAreas = getAllAreas().length;

    el.innerHTML = `
        <div class="dashboard-header">
            <h1>Life Areas Dashboard</h1>
            <p>Your self-assessment results. Areas link to detailed guides.</p>
        </div>

        <div class="level-legend">
            <div class="legend-item"><span class="legend-dot" style="background:#bdbdbd;"></span> Not assessed</div>
            <div class="legend-item"><span class="legend-dot" style="background:#e53935;"></span> Awareness</div>
            <div class="legend-item"><span class="legend-dot" style="background:#fb8c00;"></span> Top 20%</div>
            <div class="legend-item"><span class="legend-dot" style="background:#fdd835;"></span> Top 5%</div>
            <div class="legend-item"><span class="legend-dot" style="background:#43a047;"></span> Top 1%</div>
            <div class="legend-item"><span class="legend-dot" style="background:#388e3c;"></span> Top 0.1%</div>
        </div>

        <div class="summary-bar">
            <div class="summary-stat">
                <div class="stat-value">${totalAssessed} / ${totalAreas}</div>
                <div class="stat-label">Areas assessed</div>
            </div>
            <div class="summary-stat">
                <div class="stat-value${lowest.level < 6 ? ' stat-text' : ''}">${lowest.level < 6 ? lowest.name : '--'}</div>
                <div class="stat-label">Lowest area</div>
            </div>
            <div class="summary-stat">
                <div class="stat-value${highest.level > 0 ? ' stat-text' : ''}">${highest.level > 0 ? highest.name : '--'}</div>
                <div class="stat-label">Highest area</div>
            </div>
        </div>

        ${levelUpTipDismissed() ? '' : `<div class="dashboard-tip" id="dashboardLevelUpTip">
            <span class="dashboard-tip-text"><strong>How do I advance a band?</strong> Bands reflect assessed habits and outcomes, not the survey alone. To move beyond Awareness: retake the survey at <strong>Standard</strong> or <strong>Detailed</strong> depth and pick a higher band when it genuinely describes you, or open a life-area page and check off achievements as you build the underlying habits.</span>
            <button class="dashboard-tip-dismiss" onclick="dismissLevelUpTip()">Got it</button>
        </div>`}

        <div class="dashboard-controls">
            <button onclick="retakeSurvey()">Retake Survey</button>
            <button onclick="exportData()">Export CSV</button>
        </div>

        <div id="dashboardGrid">${gridHTML}</div>
    `;
}

function levelUpTipDismissed() {
    try { return !!localStorage.getItem('ap-dashboard-levelup-dismissed'); }
    catch (e) { return false; }
}

function dismissLevelUpTip() {
    try { localStorage.setItem('ap-dashboard-levelup-dismissed', '1'); } catch (e) {}
    var el = document.getElementById('dashboardLevelUpTip');
    if (el) el.style.display = 'none';
}

function retakeSurvey() {
    if (confirm('Start a new assessment? Your current results will be replaced.')) {
        localStorage.removeItem(STORAGE_LEVELS);
        localStorage.removeItem(STORAGE_RESPONSES);
        localStorage.removeItem(STORAGE_WEIGHTS);
        renderLanding();
    }
}

function exportData() {
    const levels = loadLevels();
    let csv = 'Pillar,Domain,Life Area,Level,Propagated\n';
    PILLARS.forEach(pillar => {
        pillar.domains.forEach(domain => {
            domain.areas.forEach(area => {
                const level = levels[area.slug] || '';
                const prop = levels['_propagated_' + area.slug] ? 'yes' : '';
                csv += `"${pillar.name}","${domain.name}","${area.label}",${level},${prop}\n`;
            });
        });
    });
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'life-areas-assessment.csv';
    a.click();
    URL.revokeObjectURL(url);
}

function togglePillar(header) {
    header.parentElement.classList.toggle('collapsed');
}

// ── Sign-in gate ──

function renderSignInGate() {
    const el = document.getElementById('viewLanding');
    el.innerHTML = `
        <div class="dashboard-header">
            <h1>Your dashboard</h1>
            <p>Sign in to see your personalised dashboard across all {{ site.data.life_areas | size }} life areas.</p>
        </div>
        <div style="text-align: center; margin-top: 32px;">
            <button onclick="window.Clerk && window.Clerk.openSignIn({ afterSignInUrl: window.location.href, afterSignUpUrl: window.location.href })" style="padding: 8px 20px; background: #4CAF50; color: white; border: none; border-radius: 4px; font-size: 0.95em; font-weight: 500; cursor: pointer;">Sign in</button>
        </div>
    `;
    showView('landing');
}

function routeBasedOnAuth() {
    if (window.Clerk && window.Clerk.user) {
        renderLanding();
    } else {
        renderSignInGate();
    }
}

// ── Init ──
document.addEventListener('DOMContentLoaded', function() {
    // Show empty container immediately to avoid flash of stale data
    document.getElementById('viewLanding').innerHTML = '';
    showView('landing');

    if (window.Clerk && window.Clerk.user !== undefined) {
        routeBasedOnAuth();
        return;
    }

    var checkClerk = setInterval(function() {
        if (window.Clerk && window.Clerk.user !== undefined) {
            clearInterval(checkClerk);
            routeBasedOnAuth();
        }
    }, 100);

    // Timeout fallback after 5s -- if Clerk hasn't loaded, treat as not signed in
    setTimeout(function() {
        clearInterval(checkClerk);
        if (!window.Clerk || !window.Clerk.user) {
            renderSignInGate();
        }
    }, 5000);
});

// Re-render if data syncs from Clerk (fires on sign-in)
window.addEventListener('ap-storage-sync', routeBasedOnAuth);
</script>
