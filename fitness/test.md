---
layout: default
title: Fitness Test - Personalised Recommendations
---

<style>
/* Main container */
.fitness-test-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
}

.header-section {
    text-align: center;
    margin-bottom: 40px;
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

/* Controls layout */
.controls-section {
    display: flex;
    gap: 40px;
    margin-bottom: 40px;
    align-items: flex-start;
}

.sliders-container {
    flex: 1;
    min-width: 300px;
}

.chart-container {
    flex: 1;
    min-width: 300px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Slider styling */
.value-slider {
    margin-bottom: 25px;
}

.slider-label {
    display: block;
    font-weight: 600;
    margin-bottom: 8px;
    color: #333;
    font-size: 1.1em;
}

.slider-track {
    width: 100%;
    height: 8px;
    border-radius: 4px;
    background: #e9ecef;
    outline: none;
    -webkit-appearance: none;
    appearance: none;
    cursor: pointer;
    transition: all 0.3s ease;
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
.pie-chart {
    width: 280px;
    height: 280px;
    margin-bottom: 20px;
}

.chart-legend {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    width: 100%;
    max-width: 280px;
}

.legend-item {
    display: flex;
    align-items: center;
    font-size: 0.9em;
}

.legend-color {
    width: 16px;
    height: 16px;
    border-radius: 3px;
    margin-right: 8px;
}

.legend-health { background: #28a745; }
.legend-performance { background: #dc3545; }
.legend-appearance { background: #ffc107; }
.legend-enjoyment { background: #007bff; }

/* Recommendations section */
.recommendations-section {
    background: white;
    border-radius: 8px;
    padding: 30px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.recommendations-header {
    margin-bottom: 25px;
    text-align: center;
}

.recommendations-header h2 {
    color: #000000;
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
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 25px;
    flex-wrap: wrap;
}

.sort-button {
    background: #f8f9fa;
    border: 2px solid #dee2e6;
    padding: 8px 16px;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 0.9em;
    font-weight: 500;
}

.sort-button:hover {
    background: #e9ecef;
}

.sort-button.active {
    background: #155799;
    color: white;
    border-color: #155799;
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
    align-items: center;
    gap: 8px;
    min-width: 200px;
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
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    cursor: pointer;
    transition: background-color 0.3s;
    user-select: none;
    flex-shrink: 0;
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
.sortable-header {
    cursor: pointer;
    position: relative;
    user-select: none;
}

.sortable-header:hover {
    background: #e9ecef;
}

.sortable-header.active {
    background: #155799;
    color: white;
}

.sort-indicator {
    position: absolute;
    right: 5px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 0.8em;
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
        gap: 30px;
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
    <div class="header-section">
        <h1>Personalised Fitness Recommendations</h1>
        <p>Adjust the sliders below to reflect what matters most to you in fitness, and we'll recommend the best interventions for your priorities.</p>
    </div>

    <div class="controls-section">
        <div class="sliders-container">
            <div class="value-slider health-slider">
                <label class="slider-label" for="healthSlider">Health & Longevity</label>
                <input type="range" min="0" max="100" value="35" class="slider-track" id="healthSlider">
            </div>
            
            <div class="value-slider performance-slider">
                <label class="slider-label" for="performanceSlider">Performance</label>
                <input type="range" min="0" max="100" value="30" class="slider-track" id="performanceSlider">
            </div>
            
            <div class="value-slider appearance-slider">
                <label class="slider-label" for="appearanceSlider">Appearance</label>
                <input type="range" min="0" max="100" value="20" class="slider-track" id="appearanceSlider">
            </div>
            
            <div class="value-slider enjoyment-slider">
                <label class="slider-label" for="enjoymentSlider">Enjoyment</label>
                <input type="range" min="0" max="100" value="15" class="slider-track" id="enjoymentSlider">
            </div>
        </div>

        <div class="chart-container">
            <canvas class="pie-chart" id="pieChart" width="280" height="280"></canvas>
            <div class="chart-legend">
                <div class="legend-item">
                    <div class="legend-color legend-health"></div>
                    <span id="healthPercent">35%</span> Health
                </div>
                <div class="legend-item">
                    <div class="legend-color legend-performance"></div>
                    <span id="performancePercent">30%</span> Performance
                </div>
                <div class="legend-item">
                    <div class="legend-color legend-appearance"></div>
                    <span id="appearancePercent">20%</span> Appearance
                </div>
                <div class="legend-item">
                    <div class="legend-color legend-enjoyment"></div>
                    <span id="enjoymentPercent">15%</span> Enjoyment
                </div>
            </div>
        </div>
    </div>

    <div class="recommendations-section">
        <div class="recommendations-header">
            <h2>Your Recommended Interventions</h2>
            <p>Based on your priorities, here are the fitness interventions that will give you the best results:</p>
            <div class="methodology-note">
                <p><strong>How scoring works:</strong> Each intervention is scored using a logarithmic scale where each point represents roughly 2× the impact. Expected benefit scores account for realistic success rates, then these are combined using your personal weightings to calculate Weighted Benefit Scores (WBS). Time and Money EROI show efficiency per hour and per dollar respectively. <a href="{{ site.baseurl }}/fitness/value-scoring-framework">Learn more about the methodology.</a></p>
            </div>
        </div>

        <div class="sort-controls">
            <button class="sort-button active" data-sort="wbs">Sort by WBS</button>
            <button class="sort-button" data-sort="time-eroi">Sort by Time EROI</button>
            <button class="sort-button" data-sort="money-eroi">Sort by Money EROI</button>
        </div>

        <table class="recommendations-table" id="recommendationsTable">
            <thead>
                <tr>
                    <th>Intervention</th>
                    <th class="sortable-header" data-sort="wbs">
                        WBS <span class="sort-indicator">↓</span>
                    </th>
                    <th>Upfront Cost</th>
                    <th>Ongoing Cost</th>
                    <th>Upfront Time</th>
                    <th>Ongoing Time</th>
                    <th class="sortable-header" data-sort="time-eroi">
                        Time EROI <span class="sort-indicator"></span>
                    </th>
                    <th class="sortable-header" data-sort="money-eroi">
                        Money EROI <span class="sort-indicator"></span>
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
            <td class="cost-cell">${intervention.resources.upfront_cost}</td>
            <td class="cost-cell">${intervention.resources.ongoing_cost}/${intervention.resources.ongoing_cost_period}</td>
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

// Event listeners for sort buttons
document.querySelectorAll('.sort-button').forEach(button => {
    button.addEventListener('click', function() {
        // Update active state
        document.querySelectorAll('.sort-button').forEach(btn => btn.classList.remove('active'));
        this.classList.add('active');
        
        // Update sort method and refresh recommendations
        currentSort = this.dataset.sort;
        updateRecommendations();
    });
});

// Event listeners for table header sorting
document.querySelectorAll('.sortable-header').forEach(header => {
    header.addEventListener('click', function() {
        // Update sort method
        currentSort = this.dataset.sort;
        
        // Update button states
        document.querySelectorAll('.sort-button').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.sort === currentSort);
        });
        
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
