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
    border-color: #155799;
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
    color: #155799;
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
    background: #e3f2fd;
    color: #155799;
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
    border-color: #155799;
    background: #f8fbff;
}

.radio-option.selected {
    border-color: #155799;
    background: #e3f2fd;
}

.radio-option input[type="radio"] {
    display: none;
}

.radio-option .level-label {
    font-weight: 600;
    color: #155799;
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
    background: #155799;
    color: white;
    border-color: #155799;
}

.question-nav button.btn-primary:hover {
    background: #0d47a1;
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
    background: #155799;
    color: white;
    border-color: #155799;
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
    color: #155799;
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
    padding: 8px 12px;
    background: #f8f9fa;
    border-radius: 6px;
    border-left: 4px solid #ddd;
    transition: all 0.2s;
}

.area-card:hover {
    background: #e9ecef;
}

.area-card.level-0 { border-left-color: #bdbdbd; }
.area-card.level-1 { border-left-color: #e53935; }
.area-card.level-2 { border-left-color: #fb8c00; }
.area-card.level-3 { border-left-color: #fdd835; }
.area-card.level-4 { border-left-color: #43a047; }
.area-card.level-5 { border-left-color: #1565c0; }

.area-name {
    font-size: 0.9em;
    color: #333;
}

.area-name a {
    color: #333;
    text-decoration: none;
}

.area-name a:hover {
    color: #155799;
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
.area-level-badge.lb-5 { background: #1565c0; }

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
        color: "#1565c0",
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
                { slug: "romantic-relationships", label: "Relationship Quality" },
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

const LEVEL_NAMES = ['Not assessed', 'Awareness', 'Foundation', 'Proficiency', 'Excellence', 'Mastery'];
const LEVEL_COLORS = ['#bdbdbd', '#e53935', '#fb8c00', '#fdd835', '#43a047', '#1565c0'];

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
            <p>This survey assesses your current level across ${scopeLabel}. For each area, pick the description that best matches where you are right now.</p>
            <h3>What the levels mean</h3>
            <p>The five levels correspond to population percentiles among American adults:</p>
            <ul style="line-height:1.8;">
                <li><strong>Level 1 &ndash; Awareness:</strong> You know this area exists and have basic awareness.</li>
                <li><strong>Level 2 &ndash; Foundation:</strong> Top 20%. You have solid basics in place.</li>
                <li><strong>Level 3 &ndash; Proficiency:</strong> Top 5%. You are notably better than most people.</li>
                <li><strong>Level 4 &ndash; Excellence:</strong> Top 1%. Exceptional achievement.</li>
                <li><strong>Level 5 &ndash; Mastery:</strong> Top 0.1%. Among the best in 1,000 people.</li>
            </ul>
            <p style="color:#555;"><strong>Most people are at levels 1&ndash;2 in most areas.</strong> That is completely normal. No one is at level 5 for everything &ndash; there simply is not enough time in life to excel at everything. The purpose of this survey is not to score highly. It is to identify where you are now so you can decide where to focus.</p>
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
            <div class="progress-bar-fill" style="width:${pct}%; background:#155799;"></div>
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
                <span class="level-label">Level ${lvl}: ${LEVEL_NAMES[lvl]}</span>
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
    const el = document.getElementById('viewResults');
    const baseUrl = '{{ site.baseurl }}';

    let totalAssessed = 0, totalLevel = 0;
    let lowest = { name: '', level: 6 };
    let highest = { name: '', level: 0 };

    let gridHTML = '';
    PILLARS.forEach(pillar => {
        let pillarTotal = 0, pillarCount = 0;
        let bodyHTML = '<div class="pillar-body">';

        pillar.domains.forEach(domain => {
            bodyHTML += `<div class="domain-group"><div class="domain-label">${domain.name}</div><div class="area-grid">`;
            domain.areas.forEach(area => {
                const level = levels[area.slug] || 0;
                const propagated = levels['_propagated_' + area.slug];

                if (level > 0) {
                    totalAssessed++;
                    totalLevel += level;
                    pillarTotal += level;
                    pillarCount++;
                    if (level < lowest.level) lowest = { name: area.label, level };
                    if (level > highest.level) highest = { name: area.label, level };
                }

                const propClass = propagated ? ' propagated' : '';
                const badge = level > 0
                    ? `<span class="area-level-badge lb-${level}${propClass}" title="${LEVEL_NAMES[level]}${propagated ? ' (estimated)' : ''}">${level}</span>`
                    : `<span class="area-level-badge lb-0">-</span>`;

                bodyHTML += `<div class="area-card level-${level}">
                    <span class="area-name"><a href="${baseUrl}/${area.slug}/">${area.label}</a></span>
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

    const totalAreas = getAllAreas().length;
    const tierLabel = loadTier() > 0 ? ` (Tier ${loadTier()})` : '';

    el.innerHTML = `
        <div class="dashboard-header">
            <h1>Life Areas Dashboard${tierLabel}</h1>
            <p>Your self-assessment results. Areas link to detailed guides.</p>
        </div>

        <div class="level-legend">
            <div class="legend-item"><span class="legend-dot" style="background:#bdbdbd;"></span> Not assessed</div>
            <div class="legend-item"><span class="legend-dot" style="background:#e53935;"></span> 1 -- Awareness</div>
            <div class="legend-item"><span class="legend-dot" style="background:#fb8c00;"></span> 2 -- Foundation</div>
            <div class="legend-item"><span class="legend-dot" style="background:#fdd835;"></span> 3 -- Proficiency</div>
            <div class="legend-item"><span class="legend-dot" style="background:#43a047;"></span> 4 -- Excellence</div>
            <div class="legend-item"><span class="legend-dot" style="background:#1565c0;"></span> 5 -- Mastery</div>
        </div>

        <div class="summary-bar">
            <div class="summary-stat">
                <div class="stat-value">${totalAssessed} / ${totalAreas}</div>
                <div class="stat-label">Areas assessed</div>
            </div>
            <div class="summary-stat">
                <div class="stat-value">${totalAssessed > 0 ? (totalLevel / totalAssessed).toFixed(1) : '--'}</div>
                <div class="stat-label">Average level</div>
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

        <div class="dashboard-controls">
            <button onclick="retakeSurvey()">Retake Survey</button>
            <button onclick="exportData()">Export CSV</button>
        </div>

        <div id="dashboardGrid">${gridHTML}</div>
    `;
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

// ── Init ──
document.addEventListener('DOMContentLoaded', renderLanding);

// Re-render if data syncs from Clerk
window.addEventListener('ap-storage-sync', renderLanding);
</script>
