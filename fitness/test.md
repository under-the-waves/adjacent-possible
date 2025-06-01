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

.recommendations-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 20px;
}

.recommendation-card {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
    transition: all 0.3s ease;
    background: #fafafa;
}

.recommendation-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transform: translateY(-2px);
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}

.card-title {
    font-size: 1.3em;
    font-weight: bold;
    color: #155799;
    margin: 0;
    text-decoration: none;
}

.card-title:hover {
    text-decoration: underline;
}

.card-score {
    font-size: 1.4em;
    font-weight: bold;
    color: #e63946;
    background: #f8f9fa;
    padding: 6px 12px;
    border-radius: 15px;
    margin-left: auto;
}

.card-description {
    color: #666;
    margin-bottom: 15px;
    font-size: 0.95em;
    line-height: 1.4;
}

.card-stats {
    display: flex;
    justify-content: space-between;
    font-size: 0.85em;
    color: #888;
    margin-bottom: 10px;
}

.value-bars {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
}

.value-bar {
    text-align: center;
    font-size: 0.8em;
}

.value-bar-fill {
    height: 6px;
    border-radius: 3px;
    margin-bottom: 4px;
}

.bar-health { background: #28a745; }
.bar-performance { background: #dc3545; }
.bar-appearance { background: #ffc107; }
.bar-enjoyment { background: #007bff; }

/* Mobile responsiveness */
@media (max-width: 768px) {
    .controls-section {
        flex-direction: column;
        gap: 30px;
    }
    
    .recommendations-grid {
        grid-template-columns: 1fr;
    }
    
    .pie-chart {
        width: 240px;
        height: 240px;
    }
    
    .chart-legend {
        max-width: 240px;
    }
}

/* Loading state */
.loading {
    text-align: center;
    padding: 40px;
    color: #666;
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
                <p><strong>How scoring works:</strong> Each intervention is scored using a logarithmic scale where each point represents roughly 2× the impact. Expected benefit scores account for realistic success rates, then these are combined using your personal weightings to calculate total scores. <a href="{{ site.baseurl }}/fitness/value-scoring-framework">Learn more about the methodology.</a></p>
            </div>
        </div>
        <div class="recommendations-grid" id="recommendationsGrid">
            <div class="loading">Loading recommendations...</div>
        </div>
    </div>
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
            ongoing_cost_weekly: {% if intervention_data.resources.ongoing_cost_period == "week" %}{{ intervention_data.resources.ongoing_cost | plus: 0.0 }}{% elsif intervention_data.resources.ongoing_cost_period == "month" %}{{ intervention_data.resources.ongoing_cost | plus: 0.0 | divided_by: 4.33 }}{% else %}{{ intervention_data.resources.ongoing_cost | plus: 0.0 | divided_by: 52.0 }}{% endif %},
            upfront_time: {{ intervention_data.resources.upfront_time | plus: 0 }},
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

// Current values
let currentValues = {
    health: 35,
    performance: 30,
    appearance: 20,
    enjoyment: 15
};

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
const recommendationsGrid = document.getElementById('recommendationsGrid');

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
    
    // Update all sliders and labels
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

function calculateScore(intervention, userValues) {
    const total = Object.keys(userValues).reduce((sum, key) => {
        return sum + (intervention.values[key] * userValues[key] / 100);
    }, 0);
    return total;
}

function updateRecommendations() {
    // Calculate scores for all interventions
    const scoredInterventions = Object.keys(fitnessInterventions).map(key => {
        const intervention = fitnessInterventions[key];
        const score = calculateScore(intervention, currentValues);
        return { key, ...intervention, totalScore: score };
    });
    
    // Sort by score (highest first)
    scoredInterventions.sort((a, b) => b.totalScore - a.totalScore);
    
    // Display top 6 recommendations
    const topRecommendations = scoredInterventions.slice(0, 6);
    
    recommendationsGrid.innerHTML = topRecommendations.map(intervention => `
        <div class="recommendation-card">
            <div class="card-header">
                <a href="${getInterventionUrl(intervention.key)}" class="card-title">${intervention.name}</a>
                <div class="card-score">${intervention.totalScore.toFixed(1)}</div>
            </div>
            <p class="card-description">${intervention.description}</p>
            <div class="card-stats">
                <span>Cost: $${intervention.resources.upfront_cost}</span>
                <span>Time: ${intervention.resources.ongoing_time_weekly.toFixed(1)}h/week</span>
            </div>
            <div class="value-bars">
                <div class="value-bar">
                    <div class="value-bar-fill bar-health" style="width: ${Math.max(0, (intervention.values.health / 10) * 100)}%"></div>
                    <div>H: ${intervention.values.health.toFixed(1)}</div>
                </div>
                <div class="value-bar">
                    <div class="value-bar-fill bar-performance" style="width: ${Math.max(0, (intervention.values.performance / 10) * 100)}%"></div>
                    <div>P: ${intervention.values.performance.toFixed(1)}</div>
                </div>
                <div class="value-bar">
                    <div class="value-bar-fill bar-appearance" style="width: ${Math.max(0, (intervention.values.appearance / 10) * 100)}%"></div>
                    <div>A: ${intervention.values.appearance.toFixed(1)}</div>
                </div>
                <div class="value-bar">
                    <div class="value-bar-fill bar-enjoyment" style="width: ${Math.max(0, (intervention.values.enjoyment / 10) * 100)}%"></div>
                    <div>E: ${intervention.values.enjoyment.toFixed(1)}</div>
                </div>
            </div>
        </div>
    `).join('');
}

// Event listeners for sliders
Object.keys(sliders).forEach(key => {
    sliders[key].addEventListener('input', function() {
        adjustSliders(key, parseFloat(this.value));
    });
});

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    updateAllControls();
});
</script>
