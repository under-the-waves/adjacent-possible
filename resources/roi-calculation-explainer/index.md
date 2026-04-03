---
layout: default
title: How ROI Calculations Work
---

[← Back to Intervention Database](../intervention-database/)

# How ROI Calculations Work

Every intervention in the database is scored using a consistent system designed to answer one question: **how much benefit can you realistically expect per unit of time and money invested?**

The system uses a logarithmic scale, meaning each unit increase represents roughly double the impact. This reflects how real-world benefits work – the difference between doing nothing and starting a basic exercise routine is far larger than the difference between an advanced programme and an elite one.

## The Four Core Metrics

### Potential Benefit Score (PBS) – 0 to 10

The maximum benefit an intervention could deliver if it works perfectly. Each point on the scale represents approximately twice the impact of the point below it.

PBS is anchored to concrete outcomes for each value domain. For example, in fitness health, a score of 10 corresponds to roughly 15 additional years of healthy lifespan. A score of 8 would represent about 25% of that maximum (roughly 3.75 years), and a score of 6 about 6.25% (roughly 1 year).

PBS does not factor in probability – a high-risk, high-reward intervention has a high PBS and a low ISR.

### Intervention Success Rate (ISR) – 0% to 100%

The proportion of people who achieve meaningful results when they follow the intervention properly. This captures how reliable the intervention is – does it actually work for most people, or only under ideal conditions?

An ISR of 85% means that roughly 85 out of 100 people who follow the intervention correctly will see meaningful benefits. ISR can fall below 1% for interventions with genuine but improbable benefits.

### User Adherence Rate (UAR) – 0% to 100%

The likelihood that a typical person will actually stick with the intervention long enough to see results. This is the realism check – many interventions work in theory but fail in practice because people stop doing them.

A UAR of 35% means that only about a third of people who start the intervention will maintain it consistently.

### Expected Benefit Score (EBS)

The realistic expected benefit after accounting for both reliability and adherence. Calculated as:

**EBS = PBS + log₂(ISR / 100) + log₂(UAR / 100)**

Because the scale is logarithmic, ISR and UAR act as discounts. An intervention with PBS 8, ISR 85%, and UAR 35% gives:

- 8 + log₂(0.85) + log₂(0.35)
- 8 + (−0.23) + (−1.51)
- **EBS = 6.25**

The discount from 8 to 6.25 reflects that the intervention is fairly reliable but hard to stick with.

## Expected ROI (EROI)

EROI measures efficiency – how much benefit per unit of resource invested:

- **Time EROI** = EBS ÷ weekly time cost (hours)
- **Money EROI** = EBS ÷ monthly money cost

Higher EROI means better value for your time or money. This is what makes the system useful for prioritisation – two interventions might offer similar total benefits, but one might require a fraction of the time.

## Resource Requirements

Each intervention lists four cost dimensions:

- **Upfront time** – hours for initial setup or learning
- **Ongoing time** – hours per week to maintain
- **Upfront money** – initial investment required
- **Ongoing money** – recurring expenses

## Cross-Domain Scoring

Many interventions benefit more than one area of life. A weekly walk with friends, for example, scores on fitness, social connection, and mental health values simultaneously. The system captures this by scoring the intervention against each relevant value domain.

This naturally elevates interventions that provide multiple benefits – often the most worthwhile investments are the ones that improve several areas at once.

## Values and Anchors

Each life area has 2 to 4 core values (e.g. Fitness has Health & Longevity, Physical Performance, Appearance, and Enjoyment). Interventions are scored against each value using domain-specific anchors that define what a score of 10 means in concrete terms.

Anchors use measurable units wherever possible – dollars, years, percentages – rather than abstract descriptions. This keeps scoring grounded and comparable across different domains.
