---
layout: default
title: Valuing Health and Life
permalink: /methodology/valuing-health-and-life/
---

# Valuing Health and Life

Several Worthwhile interventions affect health, longevity, or rare-but-catastrophic outcomes. To rank them alongside financial and other interventions, the framework needs an explicit way to value health gains and avoided harms. This page explains the two calibration choices that drive that valuation: the cost-effectiveness threshold and the loss-aversion adjustment for premature death.

These are calibration choices, not metaphysical claims. They make cross-domain ranking tractable; they do not assert that health and money are interchangeable in any deep philosophical sense.

## QALYs as the benefit unit for health and safety

For values in the Health and Safety domains, benefit magnitudes are denominated in **Quality-Adjusted Life Years (QALYs)**. One QALY is one year of life in perfect health. A year lived with moderate chronic pain or disability counts as a fraction of a QALY (typically 0.5–0.8, depending on severity and the source weighting). A year lost to premature death is a full QALY lost (subject to the loss-aversion adjustment below).

QALYs are the standard unit in health economics for cost-effectiveness analysis. Major bodies that use QALYs include [NICE](https://www.nice.org.uk/process/pmg9/chapter/the-reference-case) (UK), the [WHO](https://www.who.int/publications/i/item/9789241549363), and [academic health-economics literature](https://www.jhsph.edu/research/centers-and-institutes/center-for-population-health-information-technology/) globally. Worthwhile uses QALYs to keep its safety-domain scoring directly comparable to that established literature.

## The $100,000-per-QALY cost-effectiveness threshold

To compute Money EROI for health-domain interventions, the framework treats **$100,000 per QALY** as the break-even cost-effectiveness threshold. An intervention that delivers more QALYs per dollar than that produces a positive Money EROI; one that delivers fewer produces a negative Money EROI.

This figure is the conventional US-aligned threshold for cost-effective health interventions. Lower thresholds are more conservative; the UK's NICE typically uses £20,000–30,000/QALY (~$25,000–38,000/QALY). US studies and policy analyses commonly use $50,000/QALY as a lower bound and $150,000–200,000/QALY as an upper bound, with $100,000 sitting near the middle. Some references:

- [Neumann, Cohen, & Weinstein (2014), *NEJM*](https://www.nejm.org/doi/full/10.1056/NEJMp1405158) – argues for raising US thresholds from the historical $50K to $100K–150K/QALY
- [WHO-CHOICE thresholds](https://www.who.int/news-room/fact-sheets/detail/cost-effectiveness-of-interventions) – per-capita-GDP-anchored thresholds; $100K/QALY corresponds roughly to "highly cost-effective" in high-income countries
- [Bertram et al. (2016), *Bulletin of WHO*](https://www.who.int/bulletin/volumes/94/12/15-164418/en/) – discussion of how cost-effectiveness thresholds are used across health systems

Worthwhile uses the middle of the US range to avoid both excessive conservatism (where almost no health intervention looks cost-effective) and excessive permissiveness (where almost any intervention does).

## The 2× loss-aversion multiplier for premature death

For QALYs lost to premature death specifically, the framework applies a **2× multiplier** before computing EBS. A 30-QALY loss from a premature death is treated as equivalent to a 60-QALY symmetric loss elsewhere on the scale.

The reasoning combines two well-established findings in behavioural and welfare economics:

1. **Loss aversion** – Kahneman and Tversky's prospect theory found that humans typically weight losses ~2× as heavily as equivalent-magnitude gains. The seminal references are [Kahneman & Tversky (1979), *Econometrica*](https://www.jstor.org/stable/1914185) and [Tversky & Kahneman (1991), *Quarterly Journal of Economics*](https://doi.org/10.2307/2937956). Subsequent meta-analyses [Brown et al. (2024)](https://www.sciencedirect.com/science/article/pii/S2214804323001234) confirm a robust loss-aversion ratio in the 1.5–2.5 range across domains.
2. **Asymmetry of irreversible end-of-life outcomes** – Avoiding premature death isn't equivalent to extending healthy life by the same number of years. Death ends all future utility, eliminates optionality, and produces grief externalities for survivors. A symmetric QALY count systematically understates the badness of these outcomes.

A 2× multiplier sits at the conservative end of both literatures. It avoids over-weighting premature death (which would distort cross-domain ranking) while still capturing the asymmetry that vanilla QALY accounting misses. The multiplier is applied only to QALYs lost to premature death; QALYs lost to non-fatal chronic conditions use vanilla QALY weights.

## Why these are calibration choices, not absolute claims

Both numbers – the threshold and the multiplier – are choices that affect rankings. Different choices would produce different rankings. Worthwhile makes them explicit so that:

- Users who disagree with the calibration can reason about how the rankings would shift if the numbers were different
- Future revisions of the framework are auditable against the same explicit benchmarks
- Cross-domain comparisons are coherent within the framework, even though no single number can capture how individual users weight health vs money vs other values

If you find the threshold unhelpfully high or low for your own context, the rankings within the Health and Safety domains are unaffected (they're driven by relative QALY-per-dollar, not by absolute thresholds). What shifts is whether health interventions look more or less cost-effective relative to financial interventions in cross-domain views.

## What this does not cover

Worthwhile uses QALYs and the threshold *only* for Health and Safety domain values. Abstract values (mood, life purpose, enjoyment) keep their own native units and value-specific calibration. There is no claim that mood-months convert to QALYs at any specific rate, or that any Worthwhile value is exchangeable with any other in a deep philosophical sense. The framework deliberately preserves apples-to-apples comparison within each value while accepting that cross-value comparison is rough at best.
