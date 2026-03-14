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

.pillar-1 .pillar-header { background: #6a1b9a; }
.pillar-2 .pillar-header { background: #1565c0; }
.pillar-3 .pillar-header { background: #2e7d32; }
.pillar-4 .pillar-header { background: #e65100; }
.pillar-5 .pillar-header { background: #c62828; }

.pillar-body {
    padding: 15px 20px;
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

.level-selector {
    display: flex;
    gap: 2px;
}

.level-btn {
    width: 28px;
    height: 28px;
    border: 1px solid #ddd;
    border-radius: 4px;
    background: white;
    cursor: pointer;
    font-size: 0.75em;
    font-weight: 600;
    color: #666;
    transition: all 0.15s;
    display: flex;
    align-items: center;
    justify-content: center;
}

.level-btn:hover {
    background: #e9ecef;
}

.level-btn.selected {
    color: white;
    border-color: transparent;
}

.level-btn.selected.l0 { background: #bdbdbd; }
.level-btn.selected.l1 { background: #e53935; }
.level-btn.selected.l2 { background: #fb8c00; }
.level-btn.selected.l3 { background: #fdd835; color: #333; }
.level-btn.selected.l4 { background: #43a047; }
.level-btn.selected.l5 { background: #1565c0; }

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
}
</style>

<div class="dashboard-container">
    <div class="dashboard-header">
        <h1>Life Areas Dashboard</h1>
        <p>Self-assess your current level (1 -- 5) in each life area. Your selections are saved locally in your browser.</p>
    </div>

    <div class="level-legend">
        <div class="legend-item"><span class="legend-dot" style="background: #bdbdbd;"></span> Not assessed</div>
        <div class="legend-item"><span class="legend-dot" style="background: #e53935;"></span> 1 -- Awareness</div>
        <div class="legend-item"><span class="legend-dot" style="background: #fb8c00;"></span> 2 -- Foundation</div>
        <div class="legend-item"><span class="legend-dot" style="background: #fdd835;"></span> 3 -- Proficiency</div>
        <div class="legend-item"><span class="legend-dot" style="background: #43a047;"></span> 4 -- Excellence</div>
        <div class="legend-item"><span class="legend-dot" style="background: #1565c0;"></span> 5 -- Mastery</div>
    </div>

    <div class="summary-bar">
        <div class="summary-stat">
            <div class="stat-value" id="areasAssessed">0</div>
            <div class="stat-label">Areas assessed</div>
        </div>
        <div class="summary-stat">
            <div class="stat-value" id="averageLevel">--</div>
            <div class="stat-label">Average level</div>
        </div>
        <div class="summary-stat">
            <div class="stat-value" id="lowestArea">--</div>
            <div class="stat-label">Lowest area</div>
        </div>
        <div class="summary-stat">
            <div class="stat-value" id="highestArea">--</div>
            <div class="stat-label">Highest area</div>
        </div>
    </div>

    <div class="dashboard-controls">
        <button onclick="resetAll()">Reset All</button>
        <button onclick="exportData()">Export CSV</button>
    </div>

    <div id="dashboardGrid"></div>
</div>

<script>
const PILLARS = [
    {
        name: "Expand Your Awareness",
        class: "pillar-1",
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
                { slug: "romantic-relationships", label: "Romantic relationships" },
                { slug: "sex", label: "Sex" }
            ]}
        ]
    },
    {
        name: "Organise Your Life",
        class: "pillar-4",
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

const STORAGE_KEY = 'ap-dashboard-levels';

function loadLevels() {
    try {
        const stored = localStorage.getItem(STORAGE_KEY);
        return stored ? JSON.parse(stored) : {};
    } catch (e) {
        return {};
    }
}

function saveLevels(levels) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(levels));
}

function setLevel(slug, level) {
    const levels = loadLevels();
    if (level === 0) {
        delete levels[slug];
    } else {
        levels[slug] = level;
    }
    saveLevels(levels);
    renderDashboard();
}

function resetAll() {
    if (confirm('Reset all self-assessments? This cannot be undone.')) {
        localStorage.removeItem(STORAGE_KEY);
        renderDashboard();
    }
}

function exportData() {
    const levels = loadLevels();
    let csv = 'Pillar,Domain,Life Area,Level\n';
    PILLARS.forEach(pillar => {
        pillar.domains.forEach(domain => {
            domain.areas.forEach(area => {
                const level = levels[area.slug] || '';
                csv += `"${pillar.name}","${domain.name}","${area.label}",${level}\n`;
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

function renderDashboard() {
    const levels = loadLevels();
    const grid = document.getElementById('dashboardGrid');
    grid.innerHTML = '';

    let totalAssessed = 0;
    let totalLevel = 0;
    let lowest = { name: '', level: 6 };
    let highest = { name: '', level: 0 };

    PILLARS.forEach(pillar => {
        const section = document.createElement('div');
        section.className = `pillar-section ${pillar.class}`;

        let pillarTotal = 0;
        let pillarCount = 0;

        let bodyHTML = '<div class="pillar-body">';
        pillar.domains.forEach(domain => {
            bodyHTML += `<div class="domain-group"><div class="domain-label">${domain.name}</div><div class="area-grid">`;
            domain.areas.forEach(area => {
                const level = levels[area.slug] || 0;
                if (level > 0) {
                    totalAssessed++;
                    totalLevel += level;
                    pillarTotal += level;
                    pillarCount++;
                    if (level < lowest.level) { lowest = { name: area.label, level }; }
                    if (level > highest.level) { highest = { name: area.label, level }; }
                }

                let btns = '';
                for (let i = 0; i <= 5; i++) {
                    const sel = i === level ? `selected l${i}` : '';
                    const label = i === 0 ? '-' : i;
                    btns += `<button class="level-btn ${sel}" onclick="setLevel('${area.slug}', ${i})">${label}</button>`;
                }

                const baseUrl = '{{ site.baseurl }}';
                bodyHTML += `<div class="area-card level-${level}">
                    <span class="area-name"><a href="${baseUrl}/${area.slug}/">${area.label}</a></span>
                    <div class="level-selector">${btns}</div>
                </div>`;
            });
            bodyHTML += '</div></div>';
        });
        bodyHTML += '</div>';

        const avg = pillarCount > 0 ? (pillarTotal / pillarCount).toFixed(1) : '--';
        section.innerHTML = `<div class="pillar-header"><span>${pillar.name}</span><span class="pillar-avg">Avg: ${avg}</span></div>${bodyHTML}`;
        grid.appendChild(section);
    });

    document.getElementById('areasAssessed').textContent = totalAssessed;
    document.getElementById('averageLevel').textContent = totalAssessed > 0 ? (totalLevel / totalAssessed).toFixed(1) : '--';
    document.getElementById('lowestArea').textContent = lowest.level < 6 ? lowest.name : '--';
    document.getElementById('highestArea').textContent = highest.level > 0 ? highest.name : '--';
}

document.addEventListener('DOMContentLoaded', renderDashboard);
</script>
