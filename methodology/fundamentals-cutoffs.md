---
layout: default
title: Fundamentals Cutoffs
permalink: /methodology/fundamentals-cutoffs/
---

# Fundamentals Cutoffs

The [Prioritisation]({{ site.baseurl }}/prioritisation/) section recommends starting with the five upstream areas where evidence supports broad cross-domain effects: sleep, mental health, foundational finances, key relationships and social connection, and physical activity and nutrition. This document defines the cutoff at which the system flags a "significant gap" in each of these areas, along with the screening item used and the underlying evidence.

## Principles for cutoff design

The cutoffs follow four rules.

**Use validated thresholds where they exist.** PHQ-2 ≥ 3 for depression, GAD-2 ≥ 3 for anxiety, WHO-5 ≤ 50% for poor wellbeing, and UCLA-3 ≥ 6 for loneliness are all established cutoffs from the underlying psychometric literature. Where a validated cutoff exists, we use it rather than inventing one.

**Anchor to where the harm curve steepens.** Official guidelines often describe optimal targets, not the threshold at which lacking the behaviour starts to matter. The CDC sleep guideline is 7–9 hours, but mortality and cognitive harm rise sharply only below 6 hours. The WHO physical activity guideline is 150 minutes per week, but the largest absolute mortality gain is between zero and around 60 minutes per week. Flagging cutoffs target the steep part of the curve, not the optimum.

**Prefer false positives to false negatives.** Flagging fundamentals to someone who did not strictly need it costs them an override click. Failing to flag someone who did need it defeats the purpose. Where a cutoff sits at the edge between two interpretations, we err on the side of surfacing.

**Use validated short forms on-site, point to fuller instruments off-site.** The first-touch screen uses two-to-five item validated short forms (PHQ-2, GAD-2, AUDIT-C, WHO-5, UCLA-3, Hunger Vital Sign). When something flags, the result links to the full instrument (PHQ-9, GAD-7, AUDIT, UCLA-20) for users who want a more thorough check. This keeps the on-site screen short while preserving access to validated long forms.

## Sleep

| | |
|--|--|
| **Cutoff** | Fewer than 6 hours per night on typical work nights |
| **Screen item** | "On a typical work night, roughly how many hours of sleep do you get?" with bands: under 5 / 5–6 / 6–7 / 7–8 / 8 or more. Flag at the under 5 and 5–6 bands. |
| **Citations** | [Walker, 2017](https://www.nature.com/articles/s41562-017-0220-4); Cappuccio, D'Elia, Strazzullo, and Miller (2010), *Sleep* meta-analysis on duration and all-cause mortality; Hirshkowitz et al. (2015), *Sleep Health* National Sleep Foundation consensus. |

Cappuccio et al. (2010) pooled 16 prospective cohort studies covering 1.4 million participants. Sleeping under 6 hours per night was associated with a 12% increase in all-cause mortality, with the effect concentrated below 6 hours rather than between 6 and 7. Walker (2017) summarises the wider evidence on cognition, mood, metabolic, and immune effects, which follow a similar pattern: detectable but modest decrements between 6 and 7 hours, sharper below 6.

The CDC and National Sleep Foundation recommend 7–9 hours for adults. We do not flag 6–7 hours because the marginal harm in that band is small relative to the volume of users it would surface. Below 6 hours, the harm is consistent enough across outcomes that flagging is worth it even allowing for some over-reporters who actually sleep 6.5.

## Mental health (sub-clinical)

| | |
|--|--|
| **Cutoff** | WHO-5 raw score ≤ 13 (percentage score ≤ 52%) |
| **Screen item** | The five WHO-5 items on the standard 0–5 frequency scale ("none of the time" to "all of the time"), reverse-scored. Sum and flag at total ≤ 13. The on-site screen can use the lead item ("I have felt cheerful and in good spirits") with a cutoff at ≤ 2 ("less than half the time") as a faster proxy, accepting some sensitivity loss. |
| **Citations** | Topp, Østergaard, Søndergaard, and Bech (2015), *Psychotherapy and Psychosomatics* systematic review of WHO-5; Bech, Olsen, Kjoller, and Rasmussen (2003) for the 50% cutoff. |

The WHO-5 Wellbeing Index is one of the most extensively validated brief measures of subjective wellbeing in use, with five items rated over the past two weeks. The standard cutoff for "poor wellbeing" is a raw score of 13 or less out of 25, equivalent to a percentage score of 52% or less. Below this threshold, follow-up screening for depression is generally indicated.

Triage already catches clinical-grade depression (PHQ-2 ≥ 3) and anxiety (GAD-2 ≥ 3). The fundamentals layer uses WHO-5 to capture sub-clinical wellbeing impairment that does not meet the depression or anxiety cutoffs but still indicates that mental health is meaningfully in the way of daily functioning. A user can clear PHQ-2 and GAD-2 yet still score poorly on WHO-5, in which case general optimisation content is unlikely to land well until the underlying wellbeing issue is being addressed.

The WHO-5 is freely available for use with attribution to the WHO Collaborating Centre in Mental Health (Frederiksborg General Hospital, Denmark).

## Foundational finances

| | |
|--|--|
| **Cutoff** | Either: (a) less than $1,000 in liquid emergency savings, or (b) carrying revolving balances on high-interest debt (credit cards, payday loans, overdrafts charging more than 15% APR). |
| **Screen item** | Two single-item questions. "If you had an unexpected $400 expense, could you cover it from cash or savings without borrowing?" (yes / no). "Are you currently carrying balances on credit cards, payday loans, or overdrafts that charge interest?" (yes / no). Flag if either flags. |
| **Citations** | [Mani, Mullainathan, Shafir, and Zhao (2013)](https://www.science.org/doi/10.1126/science.1238041), *Science*; [Federal Reserve Economic Well-Being of US Households reports](https://www.federalreserve.gov/publications/report-economic-well-being-us-households.htm). |

Mani et al. (2013) demonstrated that financial scarcity imposes a measurable cognitive load, equivalent to losing roughly 13 IQ points in their experimental conditions. The mechanism is reasonably well established: chronic financial worry consumes attentional resources that would otherwise be available for the rest of life. The implication for prioritisation is that recommending career, productivity, or relationship interventions to someone with acute financial pressure tends to fail, because the underlying scarcity is the binding constraint on bandwidth.

The Federal Reserve's annual Survey of Household Economics and Decisionmaking has used a $400 unexpected-expense question for over a decade. In recent years, around a third of US adults could not cover such an expense from cash or savings. This question correlates well with measured financial fragility and is short enough to use as a single-item screen.

The high-interest debt cutoff is set at 15% APR because typical credit card and payday loan rates exceed this, while most mortgage and student loan rates do not. Mortgage debt in particular is not flagged at this stage; the harm curve for mortgage debt is far flatter than for revolving consumer credit, and flagging it would surface most of the homeowning population without useful signal.

The more acute end of financial distress – missed essential payments, eviction risk, insolvency – is handled in the triage layer rather than fundamentals.

## Key relationships and social connection

| | |
|--|--|
| **Cutoff** | Either: (a) UCLA-3 loneliness score ≥ 6, or (b) fewer than weekly meaningful contact with close friends or family. |
| **Screen item** | The three UCLA-3 items, each rated hardly ever (1) / some of the time (2) / often (3): "How often do you feel that you lack companionship?", "How often do you feel left out?", "How often do you feel isolated from others?" Flag at total score ≥ 6. Accompanied by a single contact-frequency item: "How often do you have meaningful contact with close friends or family (in person, by phone, or video)?" with bands: daily / weekly / monthly / less than monthly. Flag at monthly or less. |
| **Citations** | [Holt-Lunstad, Smith, Baker, Harris, and Stephenson (2015)](https://journals.sagepub.com/doi/10.1177/1745691614568352), *Perspectives on Psychological Science* meta-analysis; Hughes, Waite, Hawkley, and Cacioppo (2004), *Research on Aging*, for the UCLA-3 short form; Harvard Study of Adult Development. |

Holt-Lunstad et al. (2015) pooled 70 prospective studies covering 3.4 million participants. Social isolation, loneliness, and living alone were each associated with mortality risk increases comparable in magnitude to smoking 15 cigarettes per day. The effect sizes survive control for baseline health. The Harvard Study of Adult Development, the longest-running cohort study of adult life, finds relationship quality predicts late-life health and wellbeing more strongly than any other measured factor.

The UCLA-3 is the validated short form of the longer UCLA Loneliness Scale, with established cutoffs in the literature. A score of 6 or above indicates loneliness; a score of 9 (the maximum) indicates severe loneliness. The cutoff at 6 catches users where roughly two of the three feelings are present "some of the time" or where one is "often", which is the threshold at which lasting health and wellbeing effects emerge in the literature.

The contact frequency item is included as a behavioural complement because subjective loneliness and objective social contact are partly independent: someone with frequent contact may still feel lonely, and someone with little contact may not. Flagging on either keeps the false-negative rate low.

## Physical activity and nutrition

| | |
|--|--|
| **Cutoff** | Either: (a) less than 60 minutes per week of moderate-to-vigorous physical activity, or (b) fewer than 3 daily servings of vegetables or fruit on a typical day. |
| **Screen item** | "In a typical week, roughly how many minutes of activity that raises your heart rate noticeably do you do? (Brisk walking, cycling, sport, gym, manual work all count.)" with bands: 0 / under 60 / 60–150 / 150–300 / over 300. Flag at the 0 and under 60 bands. Accompanied by: "On a typical day, how many servings of vegetables or fruit do you eat? (One serving is roughly a fist-sized portion.)" with bands: 0–1 / 2 / 3–4 / 5 or more. Flag at the 0–1 and 2 bands. |
| **Citations** | Lee et al. (2012), *Lancet*, on physical inactivity and global mortality; WHO (2020), *Guidelines on Physical Activity and Sedentary Behaviour*; Aune et al. (2017), *International Journal of Epidemiology*, fruit and vegetable intake and mortality dose-response. |

The WHO and most national guidelines recommend 150–300 minutes per week of moderate activity, or 75–150 minutes vigorous, plus muscle-strengthening twice weekly. The mortality benefit, however, is sharply non-linear. Lee et al. (2012) and subsequent dose-response work show that the largest absolute mortality reduction occurs between zero and roughly 60 minutes per week of moderate activity. Going from 0 to 60 minutes per week is associated with a substantially larger relative risk reduction than going from 150 to 300. The fundamentals cutoff therefore targets the inactive part of the population, where the gain from any activity at all is largest, rather than flagging users who are below the optimal target but above the inactive baseline.

For diet, single-item cutoffs are more reductive than the underlying evidence supports. The most defensible single-item screen is daily vegetable and fruit intake, where Aune et al. (2017) found dose-response reductions in all-cause mortality up to around 5 servings per day, with the steepest gains in the first 2–3 servings. Flagging at fewer than 3 servings catches users at the low end of the curve where the marginal gain from improvement is largest. This is a deliberately narrow nutrition signal; broader dietary issues (ultra-processed food share, sugar intake, fibre) are addressed in the Nutrition life area rather than the fundamentals screen.

## Calibration and future revision

These cutoffs are stated with more precision than the underlying evidence supports. The harm curves are continuous; we have drawn discrete lines so that the system can flag or not flag. We will revise the cutoffs as the literature develops, as the screen accumulates response data, and as users push back on flags that they consider unwarranted.

Two specific revision triggers worth noting. First, if a substantial share of users flag on fundamentals but then dismiss the recommendation and report later that the flag was not useful, the cutoff is set too loose. Second, if users who reach later parts of the framework consistently report that an unflagged fundamentals issue was undermining their progress, the cutoff is set too tight. Both signals require dashboard data we do not yet have, so for Phase 1 the cutoffs above are best-evidence defaults, not calibrated to user behaviour.
