---
layout: default
title: Progressive Strength Training
---

{% assign intervention = site.data.interventions.fitness.progressive_strength_training %}

# {{ intervention.name }}

{{ intervention.description }}

## Scoring ##
The below numbers are based on a logarithmic scale from -10 to 10. For more information, see the [Fitness Value Scoring Framework]({{ site.baseurl }}/fitness/value-scoring-framework).

### Health & Longevity
**Potential Benefit Score: +{{ intervention.values.health.potential_score }}** - {{ intervention.values.health.justification_potential }}

**Expected Benefit Score: +{{ intervention.values.health.expected_score }}** - {{ intervention.values.health.justification_expected }}

### Performance

**Potential Benefit Score: +{{ intervention.values.performance.potential_score }}** - {{ intervention.values.performance.justification_potential }}

**Expected Benefit Score: +{{ intervention.values.performance.expected_score }}** - {{ intervention.values.performance.justification_expected }}

### Appearance

**Potential Benefit Score: +{{ intervention.values.appearance.potential_score }}** - {{ intervention.values.appearance.justification_potential }}

**Expected Benefit Score: +{{ intervention.values.appearance.expected_score }}** - {{ intervention.values.appearance.justification_expected }}

### Enjoyment

**Potential Benefit Score: +{{ intervention.values.enjoyment.potential_score }}** - {{ intervention.values.enjoyment.justification_potential }}

**Expected Benefit Score: +{{ intervention.values.enjoyment.expected_score }}** - {{ intervention.values.enjoyment.justification_expected }}

## Resource Requirements

**Upfront Cost: ${{ intervention.resources.upfront_cost }}** - {{ intervention.resources.upfront_cost_justification }}

**Ongoing Cost: ${{ intervention.resources.ongoing_cost_weekly }}/week** - {{ intervention.resources.ongoing_cost_justification }}

**Upfront Time Investment: {{ intervention.resources.upfront_time }} hours** - {{ intervention.resources.upfront_time_justification }}

**Ongoing Time Investment: {{ intervention.resources.ongoing_time_weekly }} hours/week** - {{ intervention.resources.ongoing_time_justification }}

## Prerequisites

{% for prerequisite in intervention.prerequisites %}
- {{ prerequisite }}
{% endfor %}
