---
layout: default
title: Fitness Personalised
---

<style>
/* Main container */
.fitness-test-container {
    max-width: none !important;
    width: 95% !important;
    margin: 0 auto;
    padding: 20px;
    font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
}

.breadcrumb-nav {
    font-size: 0.9em;
    color: #666;
    margin-bottom: 20px;
    text-align: center;
}

.breadcrumb-nav a {
    color: #155799;
    text-decoration: none;
}

.breadcrumb-nav a:hover {
    text-decoration: underline;
}
    
/* Container for top section - normal width */
.top-section {
    max-width: 800px;
    margin: 0 auto;
    padding: 15px;
    margin-bottom: 0px
}

/* Container for bottom section - full width */
.bottom-section {
    max-width: none !important;
    width: 95% !important;
    margin: 0 auto;
    padding: 0px 20px;
}

.controls-section {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    gap: 30px;
    margin-bottom: 10px;
    justify-content: center;
}

.sliders-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    max-width: 600px;
    width: 100%;
    flex: 1;
}

.chart-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
    
body .main-content {
    max-width: none !important;
    padding: 1rem !important;
}
    
.header-section {
    text-align: center;
    margin-bottom: 20px;
}

.header-section h1 {
    color: #000000;
    margin-bottom: 15px;
    font-weight: normal;
}

.header-section p {
    color: #000000;
    font-size: 1.1em;
    margin-bottom: 0;
}

.header-description {
    max-width: 400px;
    margin: 0 auto;
}

.header-description p {
    margin-bottom: 0;
}
    
/* Controls layout */

/* Slider styling */
.value-slider {
    margin-bottom: 0px;
    padding: 12px;
    border-radius: 8px;
    background: #f8f9fa;
}

.slider-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
}

.slider-label {
    font-weight: 600;
    color: #333;
    font-size: 1.1em;
    margin: 0;
}

.slider-percentage {
    font-weight: bold;
    font-size: 1.1em;
    color: #155799;
    min-width: 40px;
    text-align: right;
}

.slider-track {
    width: 100%;
    height: 6px;
    border-radius: 3px;
    background: #e9ecef;
    outline: none;
    -webkit-appearance: none;
    appearance: none;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-bottom: 15px;
}

.slider-description {
    font-size: 0.9em;
    color: #666;
    margin: 0;
    line-height: 1.3;
}

.slider-track::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: #155799;
    cursor: pointer;
    border: 3px solid white;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    transition: all 0.3s ease;
}

.slider-track::-webkit-slider-thumb:hover {
    transform: scale(1.1);
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

.slider-track::-moz-range-thumb {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: #155799;
    cursor: pointer;
    border: 3px solid white;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}

/* Color coding for sliders - solid colors */
.health-slider .slider-track { background: #28a745; }
.performance-slider .slider-track { background: #dc3545; }
.appearance-slider .slider-track { background: #ffc107; }
.enjoyment-slider .slider-track { background: #007bff; }

/* Pie chart */
/* Pie chart */
.pie-chart {
    width: 200px;
    height: 200px;
}

/* Hide legend since we don't need it */
.chart-legend {
    display: none;
}

/* Recommendations section */
.recommendations-section {
    background: white;
    border-radius: 8px;
    padding: 5px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.recommendations-header {
    margin-top: 0;
    margin-bottom: 10px;
    text-align: center;
}

.recommendations-header h2 {
    color: #000000;
    margin-top: 0;
    margin-bottom: 10px;
    font-weight: normal;
}

.recommendations-header p {
    color: #000000;
}

.methodology-note {
    background: #f8f9fa;
    padding: 15px;
    border-radius: 6px;
    margin-top: 15px;
    font-size: 0.9em;
    text-align: left;
}

.methodology-note p {
    margin: 0;
}

.methodology-note a {
    color: #155799;
    text-decoration: none;
}

.methodology-note a:hover {
    text-decoration: underline;
}

/* Sort controls */
.sort-controls {
    display: none;
}

/* Table styling */
.recommendations-table {
    width: 100%;
    border-collapse: collapse;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.recommendations-table th {
    background: #f8f9fa;
    padding: 15px 12px;
    text-align: left;
    font-weight: 600;
    color: #333;
    border-bottom: 2px solid #dee2e6;
    font-size: 0.9em;
    cursor: pointer;
    position: relative;
    user-select: none;
    transition: background-color 0.3s;
}

.recommendations-table th:hover {
    background: #e9ecef;
}

.recommendations-table th.active {
    background: #155799;
    color: white;
}

.recommendations-table td {
    padding: 15px 12px;
    border-bottom: 1px solid #e9ecef;
    vertical-align: middle;
}

.recommendations-table tbody tr:hover {
    background: #f8f9fa;
}

.recommendations-table tbody tr:last-child td {
    border-bottom: none;
}

/* Intervention name column */
.intervention-name {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    min-width: 200px;
    flex-wrap: wrap;
}

.intervention-link {
    color: #155799;
    text-decoration: none;
    font-weight: 600;
    font-size: 1.05em;
}

.intervention-link:hover {
    text-decoration: underline;
}

.table-description-icon {
    background-color: #155799;
    color: white;
    border-radius: 50%;
    width: 18px;
    height: 18px;
    display: flex; /* Changed from inline-flex */
    align-items: center;
    justify-content: center;
    font-size: 11px;
    cursor: pointer;
    transition: background-color 0.3s;
    user-select: none;
    flex-shrink: 0;
    margin-top: 2px;
}

.table-description-icon:hover {
    background-color: #0d47a1;
}

/* Score columns */
.wbs-score {
    font-weight: bold;
    color: #e63946;
    font-size: 1.1em;
}

.eroi-score {
    font-weight: 600;
    color: #155799;
}

/* Cost and time columns */
.cost-cell, .time-cell {
    font-size: 0.9em;
}

/* Sort indicators in headers */
.sort-indicator {
    display: inline;
    margin-left: 5px;
    font-size: 1em;
    opacity: 1;
}

.recommendations-table th:hover .sort-indicator {
    opacity: 1;
}

.recommendations-table th.active .sort-indicator {
    opacity: 1;
}

/* Mobile responsiveness */
@media (max-width: 1024px) {
    .recommendations-table {
        font-size: 0.85em;
    }
    
    .recommendations-table th,
    .recommendations-table td {
        padding: 10px 8px;
    }
    
    .intervention-name {
        min-width: 150px;
    }
}

@media (max-width: 768px) {
    .recommendations-table {
        display: block;
        overflow-x: auto;
        white-space: nowrap;
    }
    
    .recommendations-table th,
    .recommendations-table td {
        padding: 8px 6px;
        min-width: 80px;
    }
    
    .intervention-name {
        min-width: 120px;
        white-space: normal;
    }
    
    .intervention-link {
        font-size: 0.95em;
    }
}

/* Mobile responsiveness */
@media (max-width: 768px) {
    .controls-section {
        flex-direction: column;
        align-items: center;
        gap: 20px;
    }
    
    .sliders-container {
        grid-template-columns: 1fr; /* Single column on mobile */
    }
    
    .recommendations-table {
        font-size: 0.8em;
    }
    
    .recommendations-table th,
    .recommendations-table td {
        padding: 8px 4px;
    }
    
    .intervention-name {
        min-width: 100px;
    }
    
    .pie-chart {
        width: 240px;
        height: 240px;
    }
    
    .chart-legend {
        max-width: 240px;
    }
    
    .sort-controls {
        flex-direction: column;
        align-items: center;
    }
}

/* Loading state */
.loading {
    text-align: center;
    padding: 40px;
    color: #666;
}

/* Popup styles */
.popup-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.5);
    z-index: 999;
}

.popup-overlay.visible {
    display: block;
}

.description-popup {
    display: none;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    max-width: 500px;
    width: 90%;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    z-index: 1000;
}

.description-popup.visible {
    display: block;
}

.popup-close {
    position: absolute;
    top: 10px;
    right: 15px;
    background: none;
    border: none;
    font-size: 20px;
    cursor: pointer;
    color: #666;
}

.popup-close:hover {
    color: #333;
}

.popup-title {
    font-weight: bold;
    margin-bottom: 15px;
    color: #155799;
    font-size: 1.2em;
}

.popup-content {
    line-height: 1.5;
    color: #333;
}
</style>

<div class="fitness-test-container">
    <div class="breadcrumb-nav">
        <a href="{{ site.baseurl }}/">Home</a> > 
        <a href="{{ site.baseurl }}/fitness/">Fitness</a> > 
        Personalised Recommendations
    </div>
    
    <div class="top-section">
        <div class="header-section">
            <h1>Fitness Personalised</h1>
            <div class="header-description">
                <p>Adjust the sliders below to reflect what matters most to you in fitness, and we'll recommend the best interventions for your priorities.</p>
            </div>
        </div>

        <div class="controls-section">
            <div class="chart-container">
                <canvas class="pie-chart" id="pieChart" width="200" height="200"></canvas>
            </div>
            
            <div class="sliders-container">
                <div class="value-slider health-slider">
                    <div class="slider-header">
                        <label class="slider-label">Health & Longevity</label>
                        <span class="slider-percentage" id="healthPercent">35%</span>
                    </div>
                    <input type="range" min="0" max="100" value="35" class="slider-track" id="healthSlider">
                    <p class="slider-description">Fitness that supports long-term wellbeing and disease prevention.</p>
                </div>
                
                <div class="value-slider performance-slider">
                    <div class="slider-header">
                        <label class="slider-label">Physical Performance</label>
                        <span class="slider-percentage" id="performancePercent">30%</span>
                    </div>
                    <input type="range" min="0" max="100" value="30" class="slider-track" id="performanceSlider">
                    <p class="slider-description">Developing functional capabilities such as strength, endurance, power, speed, coordination, and specific skills.</p>
                </div>
                
                <div class="value-slider appearance-slider">
                    <div class="slider-header">
                        <label class="slider-label">Appearance</label>
                        <span class="slider-percentage" id="appearancePercent">20%</span>
                    </div>
                    <input type="range" min="0" max="100" value="20" class="slider-track" id="appearanceSlider">
                    <p class="slider-description">Physical aesthetics including muscle definition, body composition, and overall physique.</p>
                </div>
                
                <div class="value-slider enjoyment-slider">
                    <div class="slider-header">
                        <label class="slider-label">Enjoyment & Psychological Benefits</label>
                        <span class="slider-percentage" id="enjoymentPercent">15%</span>
                    </div>
                    <input type="range" min="0" max="100" value="15" class="slider-track" id="enjoymentSlider">
                    <p class="slider-description">The pleasure, mental health benefits, and positive experiences derived from physical activity.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="bottom-section">
        <div class="recommendations-section">
            <div class="recommendations-header">
                <h2>Your Recommended Interventions</h2>
                <p>Based on your priorities, here are the fitness interventions that will give you the best results:</p>
                <div class="methodology-note">
                    <p><strong>How scoring works:</strong> Each intervention is scored using a logarithmic scale where each point represents roughly 2× the impact. Expected benefit scores account for realistic success rates, then these are combined using your personal weightings to calculate Weighted Benefit Scores (WBS). Time and Money EROI show efficiency per hour and per dollar respectively. <a href="{{ site.baseurl }}/fitness/value-scoring-framework">Learn more about the methodology.</a></p>
                </div>
            </div>

            <table class="recommendations-table" id="recommendationsTable">
                <thead>
                    <tr>
                        <th data-sort="name">
                            Intervention <span class="sort-indicator">^v</span>
                        </th>
                        <th data-sort="wbs" class="active">
                            WBS <span class="sort-indicator">↓</span>
                        </th>
                        <th data-sort="upfront-cost">
                            Upfront Cost (USD) <span class="sort-indicator">^v</span>
                        </th>
                        <th data-sort="ongoing-cost">
                            Ongoing Cost <span class="sort-indicator">^v</span>
                        </th>
                        <th data-sort="upfront-time">
                            Upfront Time <span class="sort-indicator">^v</span>
                        </th>
                        <th data-sort="ongoing-time">
                            Ongoing Time <span class="sort-indicator">^v</span>
                        </th>
                        <th data-sort="time-eroi">
                            Time EROI <span class="sort-indicator">^v</span>
                        </th>
                        <th data-sort="money-eroi">
                            Money EROI <span class="sort-indicator">^v</span>
                        </th>
                    </tr>
                </thead>
                <tbody id="recommendationsBody">
                    <tr>
                        <td colspan="8" class="loading">Loading recommendations...</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>

<!-- Popup overlay -->
<div class="popup-overlay" id="popupOverlay" onclick="hideDescriptionPopup()"></div>

<!-- Description popup -->
<div class="description-popup" id="descriptionPopup">
    <button class="popup-close" onclick="hideDescriptionPopup()">×</button>
    <div class="popup-title" id="popupTitle"></div>
    <div class="popup-content" id="popupContent"></div>
</div>

<script>
// Build interventions data from Jekyll data files
const fitnessInterventions = {
{% for intervention_file in site.data.interventions %}
    {% assign intervention_key = intervention_file[0] %}
    {% assign intervention_data = intervention_file[1] %}
    {% if intervention_data.applicable_domains contains "fitness" %}
    "{{ intervention_key }}": {
        name: {{ intervention_data.name | jsonify }},
        description: {{ intervention_data.description | jsonify }},
        values: {
            health: {% if intervention_data.values["fitness.health"] %}{{ intervention_data.values["fitness.health"].pbs | plus: 0.0 }} + Math.log2({{ intervention_data.values["fitness.health"].isr | plus: 0.0 }}/100) + Math.log2({{ intervention_data.values["fitness.health"].uar | plus: 0.0 }}/100){% else %}0{% endif %},
            performance: {% if intervention_data.values["fitness.performance"] %}{{ intervention_data.values["fitness.performance"].pbs | plus: 0.0 }} + Math.log2({{ intervention_data.values["fitness.performance"].isr | plus: 0.0 }}/100) + Math.log2({{ intervention_data.values["fitness.performance"].uar | plus: 0.0 }}/100){% else %}0{% endif %},
            appearance: {% if intervention_data.values["fitness.appearance"] %}{{ intervention_data.values["fitness.appearance"].pbs | plus: 0.0 }} + Math.log2({{ intervention_data.values["fitness.appearance"].isr | plus: 0.0 }}/100) + Math.log2({{ intervention_data.values["fitness.appearance"].uar | plus: 0.0 }}/100){% else %}0{% endif %},
            enjoyment: {% if intervention_data.values["fitness.enjoyment"] %}{{ intervention_data.values["fitness.enjoyment"].pbs | plus: 0.0 }} + Math.log2({{ intervention_data.values["fitness.enjoyment"].isr | plus: 0.0 }}/100) + Math.log2({{ intervention_data.values["fitness.enjoyment"].uar | plus: 0.0 }}/100){% else %}0{% endif %}
        },
        resources: {
            upfront_cost: {{ intervention_data.resources.upfront_cost | plus: 0 }},
            ongoing_cost: {{ intervention_data.resources.ongoing_cost | plus: 0.0 }},
            ongoing_cost_period: {{ intervention_data.resources.ongoing_cost_period | jsonify }},
            ongoing_cost_weekly: {% if intervention_data.resources.ongoing_cost_period == "week" %}{{ intervention_data.resources.ongoing_cost | plus: 0.0 }}{% elsif intervention_data.resources.ongoing_cost_period == "month" %}{{ intervention_data.resources.ongoing_cost | plus: 0.0 | divided_by: 4.33 }}{% else %}{{ intervention_data.resources.ongoing_cost | plus: 0.0 | divided_by: 52.0 }}{% endif %},
            upfront_time: {{ intervention_data.resources.upfront_time | plus: 0 }},
            ongoing_time: {{ intervention_data.resources.ongoing_time | plus: 0.0 }},
            ongoing_time_period: {{ intervention_data.resources.ongoing_time_period | jsonify }},
            ongoing_time_weekly: {% if intervention_data.resources.ongoing_time_period == "week" %}{{ intervention_data.resources.ongoing_time | plus: 0.0 }}{% elsif intervention_data.resources.ongoing_time_period == "month" %}{{ intervention_data.resources.ongoing_time | plus: 0.0 | divided_by: 4.33 }}{% else %}{{ intervention_data.resources.ongoing_time | plus: 0.0 | divided_by: 52.0 }}{% endif %}
        }
    }{% unless forloop.last %},{% endunless %}
    {% endif %}
{% endfor %}
};

console.log('Loaded interventions:', fitnessInterventions);

// Color scheme - standard colors
const colors = {
    health: '#28a745',     // Green
    performance: '#dc3545', // Red
    appearance: '#ffc107',  // Yellow
    enjoyment: '#007bff'    // Blue
};

// Current values and sort method
let currentValues = {
    health: 35,
    performance: 30,
    appearance: 20,
    enjoyment: 15
};

let currentSort = 'wbs';

// Get DOM elements
const sliders = {
    health: document.getElementById('healthSlider'),
    performance: document.getElementById('performanceSlider'),
    appearance: document.getElementById('appearanceSlider'),
    enjoyment: document.getElementById('enjoymentSlider')
};

const percentLabels = {
    health: document.getElementById('healthPercent'),
    performance: document.getElementById('performancePercent'),
    appearance: document.getElementById('appearancePercent'),
    enjoyment: document.getElementById('enjoymentPercent')
};

const canvas = document.getElementById('pieChart');
const ctx = canvas.getContext('2d');
const recommendationsTable = document.getElementById('recommendationsTable');
const recommendationsBody = document.getElementById('recommendationsBody');

// Smart slider adjustment function
function adjustSliders(changedSlider, newValue) {
    const oldValue = currentValues[changedSlider];
    const difference = newValue - oldValue;
    
    // Update the changed slider
    currentValues[changedSlider] = newValue;
    
    // Calculate total of other sliders
    const otherSliders = Object.keys(currentValues).filter(key => key !== changedSlider);
    const otherTotal = otherSliders.reduce((sum, key) => sum + currentValues[key], 0);
    
    // If other sliders total is 0, distribute evenly
    if (otherTotal === 0) {
        const remainingValue = 100 - newValue;
        const perSlider = remainingValue / otherSliders.length;
        otherSliders.forEach(key => {
            currentValues[key] = perSlider;
        });
    } else {
        // Proportionally adjust other sliders
        const remainingValue = 100 - newValue;
        const scaleFactor = remainingValue / otherTotal;
        
        otherSliders.forEach(key => {
            currentValues[key] = Math.max(0, currentValues[key] * scaleFactor);
        });
    }
    
    // Ensure we sum to exactly 100
    const total = Object.values(currentValues).reduce((sum, val) => sum + val, 0);
    if (total !== 100) {
        const adjustment = 100 - total;
        currentValues[changedSlider] += adjustment;
    }
    
    // Update all controls
    updateAllControls();
}

function updateAllControls() {
    // Update sliders
    Object.keys(sliders).forEach(key => {
        sliders[key].value = currentValues[key];
    });
    
    // Update percentage labels
    Object.keys(percentLabels).forEach(key => {
        percentLabels[key].textContent = Math.round(currentValues[key]) + '% ';
    });
    
    // Update pie chart
    drawPieChart();
    
    // Update recommendations
    updateRecommendations();
}

function drawPieChart() {
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const radius = 100;
    
    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Calculate angles
    let currentAngle = -Math.PI / 2; // Start at top
    const values = Object.keys(currentValues);
    
    values.forEach(key => {
        const sliceAngle = (currentValues[key] / 100) * 2 * Math.PI;
        
        // Draw slice
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + sliceAngle);
        ctx.closePath();
        ctx.fillStyle = colors[key];
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 3;
        ctx.stroke();
        
        currentAngle += sliceAngle;
    });
}

// Get intervention URL - fix for Jekyll
function getInterventionUrl(key) {
    // Convert snake_case to kebab-case for URLs
    const urlKey = key.replace(/_/g, '-');
    return '{{ site.baseurl }}/resources/intervention-database/' + urlKey;
}

function calculateWBS(intervention, userValues) {
    return Object.keys(userValues).reduce((sum, key) => {
        return sum + (intervention.values[key] * userValues[key] / 100);
    }, 0);
}

function calculateTimeEROI(wbs, timeWeekly) {
    return wbs / Math.max(1, timeWeekly);
}

function calculateMoneyEROI(wbs, upfrontCost, ongoingCostWeekly) {
    // Calculate equivalent weekly cost (assuming 1 year timeframe for upfront costs)
    const weeklyEquivalentCost = (upfrontCost / 52) + ongoingCostWeekly;
    return wbs / Math.max(1, weeklyEquivalentCost);
}

function showDescriptionPopup(interventionName, description) {
    document.getElementById('popupTitle').textContent = interventionName;
    document.getElementById('popupContent').textContent = description;
    document.getElementById('popupOverlay').classList.add('visible');
    document.getElementById('descriptionPopup').classList.add('visible');
}

function hideDescriptionPopup() {
    document.getElementById('popupOverlay').classList.remove('visible');
    document.getElementById('descriptionPopup').classList.remove('visible');
}

function updateRecommendations() {
    // Calculate scores for all interventions
    const scoredInterventions = Object.keys(fitnessInterventions).map(key => {
        const intervention = fitnessInterventions[key];
        const wbs = calculateWBS(intervention, currentValues);
        const timeEROI = calculateTimeEROI(wbs, intervention.resources.ongoing_time_weekly);
        const moneyEROI = calculateMoneyEROI(wbs, intervention.resources.upfront_cost, intervention.resources.ongoing_cost_weekly);
        
        return { 
            key, 
            ...intervention, 
            wbs: wbs,
            timeEROI: timeEROI,
            moneyEROI: moneyEROI
        };
    });
    
    // Sort by current sort method
    switch(currentSort) {
        case 'wbs':
            scoredInterventions.sort((a, b) => b.wbs - a.wbs);
            break;
        case 'time-eroi':
            scoredInterventions.sort((a, b) => b.timeEROI - a.timeEROI);
            break;
        case 'money-eroi':
            scoredInterventions.sort((a, b) => b.moneyEROI - a.moneyEROI);
            break;
    }
    
    // Update sort indicators
    updateSortIndicators();
    
    // Display all interventions in table format
    recommendationsBody.innerHTML = scoredInterventions.map(intervention => `
        <tr>
            <td>
                <div class="intervention-name">
                    <a href="${getInterventionUrl(intervention.key)}" class="intervention-link">${intervention.name}</a>
                    <span class="table-description-icon" onclick="showDescriptionPopup('${intervention.name.replace(/'/g, "\\'")}', '${intervention.description.replace(/'/g, "\\'")}')">i</span>
                </div>
            </td>
            <td class="wbs-score">${intervention.wbs.toFixed(1)}</td>
            <td class="cost-cell">$${intervention.resources.upfront_cost}</td>
            <td class="cost-cell">$${intervention.resources.ongoing_cost}/${intervention.resources.ongoing_cost_period}</td>
            <td class="time-cell">${intervention.resources.upfront_time}h</td>
            <td class="time-cell">${intervention.resources.ongoing_time}h/${intervention.resources.ongoing_time_period}</td>
            <td class="eroi-score">${intervention.timeEROI.toFixed(2)}</td>
            <td class="eroi-score">${intervention.moneyEROI.toFixed(2)}</td>
        </tr>
    `).join('');
}

function updateSortIndicators() {
    // Clear all indicators
    document.querySelectorAll('.sort-indicator').forEach(indicator => {
        indicator.textContent = '';
    });
    
    // Remove active class from all headers
    document.querySelectorAll('.sortable-header').forEach(header => {
        header.classList.remove('active');
    });
    
    // Set active indicator
    const activeHeader = document.querySelector(`[data-sort="${currentSort}"]`);
    if (activeHeader && activeHeader.classList.contains('sortable-header')) {
        activeHeader.classList.add('active');
        const indicator = activeHeader.querySelector('.sort-indicator');
        if (indicator) {
            indicator.textContent = '↓';
        }
    }
}

// Event listeners for sliders
Object.keys(sliders).forEach(key => {
    sliders[key].addEventListener('input', function() {
        adjustSliders(key, parseFloat(this.value));
    });
});

// Event listeners for table header sorting
document.querySelectorAll('th[data-sort]').forEach(header => {
    header.addEventListener('click', function() {
        // Update sort method
        currentSort = this.dataset.sort;
        
        // Refresh recommendations
        updateRecommendations();
    });
});

// Close popup with Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        hideDescriptionPopup();
    }
});

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    updateAllControls();
});
</script>
