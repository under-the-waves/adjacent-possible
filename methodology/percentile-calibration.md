---
layout: default
title: How percentile estimates are calibrated
permalink: /methodology/percentile-calibration/
human_written: true
---

# How percentile estimates are calibrated

When you take the Awareness assessment for a life area, the site converts your answers into estimated percentiles for each value. This page explains what those numbers mean and how they're derived.

## The rule: population frequency

A percentile here answers a single question: **what fraction of the general adult population would do worse than you in this area?** If you're at the 70th percentile, roughly 70% of people are below you and 30% are above. The framework's five bands map directly to percentile thresholds &ndash; Awareness (anyone can reach it), Top 20% (80th percentile), Top 5% (95th), Top 1% (99th), Top 0.1% (99.9th).

This is the only methodology used consistently across the site. Percentiles are descriptive – where you sit in the population today – not evaluative scores against an idealised ceiling. A common alternative would be to anchor percentiles to best-possible practice, so "I don't know" maps to the bottom decile because it shows lack of awareness. We don't do that here. If 60% of adults have never checked their fridge temperature, "I don't know" puts you in line with that majority, not in the bottom 10% of food-safety competence.

The bands carry the aspirational ladder; the percentile is honest about which rung you're on.

## Where the numbers come from

Three sources, in priority order:

1. **Published survey or census data** where it exists – BRFSS, NHANES, Gallup wellbeing surveys, OECD Better Life, national time-use surveys, sector-specific industry data (e.g. financial planning surveys for emergency-fund prevalence). When a percentile threshold is supported by published data, the JS comment above it cites the source approximation.
2. **Cross-referenced proxy estimates** when the exact question isn't in published surveys but a closely related one is. For instance, "How intentional do you feel about your meals?" doesn't have direct survey data, but Gallup wellbeing measures on intentionality and routine give a credible proxy.
3. **Reasonable best guess** when nothing better is available. A best guess isn't a free pass: it's a defensible estimate of what fraction of adults would land in each bucket, given the question's framing and what we know about adjacent behaviours.

Every threshold is approximate. The site says percentiles "could easily be off by 10–15 points" because self-report is biased upward by roughly that range across most surveys.

## Where this methodology is hardest to apply

- **Subjective values** – self-rated wellbeing, meaning, satisfaction. The distribution is real but compressed; people cluster near a "decent" midpoint and rarely report extremes. Bands at the high end (Top 1%, Top 0.1%) need more interpretation here than for measurable behaviours.
- **Bimodal distributions** – questions where the population splits sharply between "doesn't do it at all" and "does it well" with little middle ground. The bands hide this because they're chunky, but the percentile jump from "doesn't do it" to "does it" is qualitatively a step change, not a smooth slope.
- **Behaviour vs. competence** – "Do you have a will?" is a binary behaviour; "How robust is your will?" is a competence question. The first is well-served by survey data; the second needs proxies.
- **Self-report bias** – people overrate their own practice by roughly 10–15 points across most surveys. The site flags this on every assessment page rather than trying to correct silently. Treat your assessed percentile as the upper bound of where you probably sit.

## Auditing this in practice

Threshold mappings live in the JavaScript on each life-area `level-1.md`, in a `THRESHOLDS` map keyed by question ID. Each entry has the structure `{v: 'response-value', p: 30}` &ndash; `p` is the percentile assigned to that answer.

A growing share of these are calibrated against published data; the rest are best guesses pending review. A pass to migrate every threshold to documented sources (or explicit "best guess based on X") is tracked in `.claude/context/remaining-work.md`. If you spot a threshold that looks off, please flag it &ndash; the methodology only works if the numbers feeding it are honest.
