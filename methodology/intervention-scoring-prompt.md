---
layout: default
title: "Intervention Scoring Prompt"
permalink: /methodology/intervention-scoring-prompt/
---

# Intervention Scoring Prompt

This is the methodology used to score every intervention in the Worthwhile database. The prompt is fed to a Claude model, which produces a YAML record with PBS / ISR / UAR scores, baseline framing, sources, and content fields. Every intervention page links back to the version of this prompt that produced it via a commit-pinned URL.

---

You are an expert in evidence-based personal development and quantitative assessment. Your task is to score the following intervention using a systematic methodology.

## Intervention to Score

**Name:** [INSERT INTERVENTION NAME]

**Primary Domain(s):** [INSERT PRIMARY LIFE AREA(S) - e.g., "fitness", "sleep", "goals"]

## Scoring Framework

### Three Components to Score
You must score this intervention across ALL applicable value domains (primary + cross-domain, identified in the Cross-Domain Discovery step below). For each value domain, provide:

1. **Potential Benefit Score (PBS)**: Maximum theoretical benefit under ideal conditions (0-10 logarithmic scale)
2. **Intervention Success Rate (ISR)**: Likelihood the intervention succeeds when followed properly (0-100%)
3. **User Adherence Rate (UAR)**: Likelihood users will follow the intervention properly (0-100%)

### Logarithmic Scale (0-10)
Each point represents roughly 2x the impact:
- Score 10 = Maximum possible benefit for that value domain
- Score 8 = 25% of maximum
- Score 6 = 6.25% of maximum
- Score 4 = 1.56% of maximum
- Score 2 = 0.39% of maximum

**Calculating PBS from a linear anchor:**

For linear anchors (e.g. "25% body weight lost", "15 years additional lifespan"), use this formula:

    PBS = 10 + log₂(effect_size / anchor_max)

Examples with a 25% body weight loss anchor:
- 15% loss: 10 + log₂(15/25) = 10 − 0.74 = **9.3** (round to 9)
- 6% loss: 10 + log₂(6/25) = 10 − 2.06 = **7.9** (round to 8)
- 3% loss: 10 + log₂(3/25) = 10 − 3.06 = **6.9** (round to 7)
- 1.5% loss: 10 + log₂(1.5/25) = 10 − 4.06 = **5.9** (round to 6)

Do NOT use linear interpolation (e.g. 15/25 × 10 = 6). This is a common error that systematically underscores PBS.

### Baseline framing

PBS represents the **magnitude of change** the intervention produces, not the absolute level a successful user ends up at. Every value in `_data/values.yml` declares a `baseline_percentile` field – the percentile of the typical non-adopter, who is the implicit subject of the score.

Default `baseline_percentile` is 35: most adults who would consider an intervention in a given area are below the median in that area, otherwise they would not be looking for help. A few areas have higher baselines (e.g. `housing.affordability` baseline = 50, because most people live in average housing).

When writing PBS reasoning, follow this pattern explicitly:

1. **State the baseline.** "Baseline (per `values.yml`): 35th percentile."
2. **State the predicted endpoint.** "After successful adherence, a user could plausibly reach the 60th percentile."
3. **Compute the delta.** "Delta = 25 percentile points of improvement."
4. **Map the delta to PBS using the log formula** with the value's anchor.

The PBS represents step 4 – the size of the change, not where you end up. A user who is already at the 80th percentile would see less benefit because there is less room to improve; that's handled by the personalisation layer at display time, not in the PBS itself.

### `baseline_percentile` vs. Tier 0 – do not conflate

These two concepts describe different axes and are easy to muddle when both appear on the same page.

- **`baseline_percentile`** lives on the **outcome axis**: the value's percentile (fitness.health percentile, mental-health.stability percentile, etc.). It calibrates *where on the outcome the typical non-adopter sits* and is the implicit subject of the PBS delta.
- **Tier 0** in the intervention's `dose_response` block lives on the **intervention-adherence axis**: how much of *this specific intervention* the user is currently doing. Tier 0 means "not deliberately doing it" – e.g., walking under 3,000 steps a day from incidental movement only.

The two correlate for some interventions but decouple frequently. A marathon runner can be at Tier 0 on walking (zero deliberate walks) while sitting at the 90th percentile on fitness.health (because their running makes them fit). A user who has never done meditation can be at Tier 0 on it while still having an 80th-percentile mental-health.stability score (because they have a steady job, supportive partner, and good sleep).

The system treats them as orthogonal:
- The tier multiplier scales the *captured benefit* of the intervention based on adherence (Tier 0 = 0% captured).
- The sigmoid personalisation discounts EBS based on the gap between the user's outcome percentile (from Level 1) and `baseline_percentile` – independent of which tier they report.

When you write a PBS reasoning that says "baseline 35th percentile, endpoint 65th, delta 30 points", you are speaking about the outcome axis – the typical non-adopter at the 35th percentile on the value. You are *also* implicitly speaking about a Tier 0 starting point on the intervention (they're not doing it yet), but that's not the same statement. The PBS captures the *delta achievable by progressing from Tier 0 to Tier 3*, for someone who starts at the value's baseline percentile.

### Critical Reasoning Requirements

For each score, you must provide reasoning that directly justifies the specific number. Consider:

**PBS Reasoning:**
- **Begin with the baseline framing**: state the value's `baseline_percentile`, the predicted endpoint percentile after successful adherence, and the delta. The PBS represents the size of the delta, not the endpoint.
- PBS measures the magnitude of benefit for someone who succeeds – how big is the payoff if it works?
- Do NOT discount PBS for low probability of success – that is what ISR captures. A high-risk, high-reward intervention (e.g. starting a business) should have high PBS and low ISR, not medium PBS.
- The same rule applies to **rare-event protective interventions** (smoke alarms, seat belts, vaccinations, emergency kits, advance directives). PBS captures the conditional benefit *if the rare event occurs and the intervention succeeds* – e.g. a fire death prevented, a serious accident survived. ISR captures the lifetime probability of being protected (typically 0.1%–1% over a lifetime). Do NOT pre-multiply PBS by the base rate of the rare event – e.g. for smoke alarms, PBS is the conditional life-saved magnitude on the mortality anchor, NOT "expected mortality reduction averaged across the population." Putting the base rate in PBS double-counts when ISR is also applied and gives misleadingly modest PBS values for what are conditionally life-saving interventions.
- **Negative PBS** is allowed and meaningful: it expresses that the intervention directly harms the value. Example: enabling 2FA on `digital-safety.security` has positive PBS (substantial security gain) but negative PBS on `digital-safety.convenience` (extra friction at every login). Score harms honestly with a negative magnitude rather than skipping the value or rounding to zero.
- For objectively measurable values (linear anchors like years of lifespan, savings rate, fitness percentile), cite specific studies, meta-analyses, or systematic reviews that demonstrate effect sizes for successful cases.
- For subjective values (e.g. enjoyment, comfort, engagement), use common-sense reasoning about the activity's inherent characteristics. Sources are welcome where they directly measure the construct in question, but do not force citations that measure a different construct (e.g. mood/anxiety studies do not measure enjoyment). Unsourced reasoning is fine for PBS on subjective values.
- PBS and ISR must make distinct arguments. PBS answers "how big is the benefit?" while ISR answers "how reliably does it happen?" Do not repeat the same argument in both.
- Consider: "For someone starting at the baseline percentile who follows this intervention and it works, how much improvement do they get?"

**Avoiding PBS/ISR overlap on linear anchors:**

For objectively measurable values (% body weight lost, years of lifespan, fitness percentile), both PBS and ISR tend to cite the same RCT data. To keep them distinct:

- **PBS** uses trial data to answer: "Successful adherents achieve X outcome." Focus on the effect size for people who respond. Do not mention what proportion respond.
- **ISR** uses trial data to answer: "X% of adherent participants achieve meaningful results." Focus on response rates, non-responder prevalence, and mechanistic reliability. Do not restate the effect size.

Example (calorie tracking for fat loss):
- PBS: "Successful calorie trackers sustain 5–8% body weight loss at 12 months, mapping to score 7 on the anchor."
- ISR: "Among consistent trackers, 54% achieve clinically significant (>5%) weight loss. The remainder underreport intake or fail to maintain a deficit despite logging."

**ISR Reasoning:**
- What proportion of people who follow this intervention properly achieve meaningful results?
- This is primarily a success rate: of everyone who does this correctly, what percentage actually gets the benefit?
- ISR can be very low (even below 1%) for interventions with genuine but improbable benefits – e.g. lottery tickets, speculative investments, cold-approaching for sales
- Evidence quality is a secondary factor: weak evidence widens the uncertainty around the ISR estimate and should push toward more conservative values. The ISR value itself represents the best estimate of the actual success rate, not a rating of evidence quality.
- For subjective values, ISR should address the reliability of the benefit across the population – what proportion of adherent people actually experience it? This is where survey data, preference studies, and individual variation research belong.
- Consider: "Out of 100 people who follow this intervention properly, how many achieve meaningful results?"

**UAR Reasoning:**
- What percentage of people can realistically maintain this intervention long-term?
- Use real-world adherence data, dropout rates, retention statistics
- Consider barriers: complexity, time requirements, cost, lifestyle changes needed
- Factor in typical human behavior patterns and motivation challenges
- This is about human psychology and practical constraints, not evidence quality

### Reasoning Format

All reasoning fields (pbs_reasoning, isr_reasoning, uar_reasoning) must be formatted as a bulleted list of 3-4 points. Use this format in the YAML:

    pbs_reasoning: |
      - Point one with [source](url) where available
      - Point two – common-sense reasoning is fine for subjective values
      - Point three with [source](url)

Each point in ISR and UAR reasoning should cite a specific source. PBS reasoning for subjective values may use unsourced common-sense arguments where no direct evidence exists – do not cite studies that measure a different construct just to have a citation.

## Description Requirements

Provide a description as a bulleted list (using `|` YAML multiline syntax with `- ` prefixed lines). Include 3-5 bullets covering:
- Exactly what the person does (specific actions, techniques, protocols)
- Key terminology defined clearly for general audience
- For habits: frequency (daily/weekly), duration per session, total timeframe to see results
- Any important variations or progressive elements
- What makes this intervention distinct from similar approaches

When citing evidence in descriptions, embed hyperlinks inline without naming the source – e.g. write `[Research](url) shows that...` not `Research from Thaler and Benartzi (2004) shows that...`. The reader can click through for attribution; naming authors adds clutter.

## Country-Neutral Framing

The site is intended for users globally, mostly in the Global North. Population data and cost defaults use US-aligned figures (most data available, large population) and currency is USD throughout. The user can override individual time and money costs for their own context via the "Personalise these costs" affordance on each intervention page. **The framing of all prose fields, however, must be country-neutral** so a reader in any country recognises the guidance as applicable to them.

### Term substitution table

Apply these in prose fields (`what_it_is`, `how_to_do_it`, `success_looks_like`, `common_pitfalls`, `description`, `prerequisites`, and any `*_reasoning` field):

| Avoid | Use instead |
|---|---|
| GP, GPs (UK/Australia) | primary care doctor, primary-care appointment, primary-care consultation |
| NHS / NHS-eligible (prescriptive) | "your healthcare system", "national health insurance or insurer", or drop the qualifier |
| ISA, 401(k), Roth IRA, RRSP, TFSA, pension (UK) | tax-advantaged savings, tax-advantaged retirement contributions, retirement plan |
| current account (UK), checking account (US) | main bank account |
| standing order, direct debit (UK terms) | scheduled bank transfer, automated payment |
| salary sacrifice (UK) | pre-tax payroll deduction |
| £, GBP, mixed-currency figures like "$32 (~£25)" | USD only, per site convention |
| "in the UK", "in the US", "Britons", "Americans" | drop the qualifier; use global stats where possible |
| Zocdoc, NHS app (prescriptive booking link) | "your local appointment-booking system" or drop |

### Citations stay country-specific

Attributed evidence sources (the NHS, NIMH, Vanguard's *How America Saves*, the CDC, the FSA, etc.) are fine to cite even when country-specific. The reader sees them as data sources, not prescriptions. Only change the *surrounding claim* if it's framed as country-specific. For example:

- ✗ "GP appointments are free on the NHS" – prescriptive, country-specific
- ✓ "[NHS appointment non-attendance rates](url) run at 15–20%, broadly consistent with attendance studies in other healthcare systems" – attributed evidence, country-neutral framing

### Specific instruments

Where an intervention depends on a country-specific tax or savings vehicle (e.g. ISA, 401k), use the generic label in the body and trust the reader to map it to their local equivalent. A separate per-intervention `country_resources` YAML block will eventually handle explicit per-country specifics (links, instrument names, exact prices) – not in scope for new intervention scoring.

### Cost reasoning

Cost figures in `upfront_cost` / `ongoing_cost` are USD and default to US-aligned figures. Where a cost varies dramatically by country or healthcare system (typical for medical care, dental work, therapy, etc.), say so in the cost reasoning field and direct the reader to the override:

> Costs vary widely by country and healthcare system. Where care is covered by national health insurance, out-of-pocket cost may be near zero. Where care is paid privately or via insurance copay, costs may include [specific US-aligned figures]. Users with private-pay healthcare should adjust via 'Personalise these costs'.

### British spelling stays

British spelling is a project convention and unaffected by this section. Keep "optimisation", "behaviour", "coeliac", "optician", etc. These are writing-convention choices, not country-specific institutional terms.

## Value Domain Key Format

**CRITICAL:** Use the exact format `[life_area].[value_name]` for all value domain keys. Examples:
- For fitness interventions: `fitness.health`, `fitness.performance`, `fitness.appearance`, `fitness.enjoyment`
- For sleep interventions: `sleep.daily_functioning`, `sleep.long_term_health`, `sleep.comfort_experience`
- For nutrition interventions: `nutrition.physical_wellbeing`, `nutrition.pleasure_connection`, `nutrition.ethical_environmental`

Do NOT create new top-level categories like `health.longevity` or `performance.athletic`. Always use the life area as the top-level key.

## Valid Value Domain Keys

The following domains and values are defined in `_data/values.yml`. Use ONLY these keys — do not invent new ones. If the intervention requires a value domain not listed here, flag it rather than creating a new key.

All {{ site.data.life_areas | size }} life areas are now scoreable. Full list in `_data/values.yml`. Use ONLY these keys — do not invent new ones. If the intervention requires a value domain not listed here, flag it rather than creating a new key.

| Domain | Values |
|---|---|
| `behaviours` | `freedom`, `emotional`, `social`, `resilience` |
| `body-image` | `fat_loss`, `muscle_gain` |
| `career-planning` | `clarity`, `advancement`, `security` |
| `children` | `wellbeing`, `relationship`, `achievement`, `development` |
| `cognitive-skills` | `memory`, `focus`, `reasoning`, `lifestyle` |
| `communication` | `influence`, `connection`, `performance`, `conflict` |
| `community-contribution` | `impact`, `belonging`, `fulfilment` |
| `consumptive-leisure` | `restoration`, `enrichment`, `enjoyment` |
| `current-work` | `competence`, `engagement`, `rewards` |
| `digital-safety` | `security`, `convenience` |
| `emergency-preparedness` | `self-reliance`, `community`, `baseline`, `catastrophic` |
| `ethics` | `philosophical`, `practical`, `integrity`, `community` |
| `extended-family` | `harmony`, `closeness`, `balance` |
| `family-of-origin` | `autonomy`, `connection`, `healing`, `duty` |
| `financial-planning-tracking` | `accuracy`, `simplicity`, `insight` |
| `fitness` | `health`, `performance`, `enjoyment` |
| `food-management` | `competence`, `craft`, `waste_reduction` |
| `friendship` | `depth`, `breadth`, `growth` |
| `global-impact` | `impartiality`, `passion`, `sustainability`, `fulfilment` |
| `goals` | `clarity`, `follow_through`, `adaptability` |
| `habits` | `impact`, `consistency`, `enjoyment` |
| `health-management` | `longterm`, `vitality`, `control`, `simplicity` |
| `housework` | `health`, `order`, `aesthetics`, `environmental` |
| `housing` | `comfort`, `affordability`, `location` |
| `information-management` | `retention`, `retrieval`, `insight`, `simplicity` |
| `investing` | `growth`, `safety`, `simplicity` |
| `learning-methods` | `efficiency`, `depth`, `enjoyment` |
| `legal-matters` | `protection`, `simplicity`, `strategic`, `access` |
| `life-purpose` | `clarity`, `meaning`, `integration` |
| `life-skills` | `high`, `systematic`, `teaching` |
| `media-diet` | `quality`, `relevance`, `breadth`, `efficiency` |
| `mental-health` | `stability`, `resilience`, `flourishing` |
| `mindfulness` | `clarity`, `emotional`, `knowledge`, `spiritual` |
| `networks` | `depth`, `breadth`, `relevance` |
| `nutrition` | `physical_wellbeing`, `pleasure_connection`, `ethical_environmental` |
| `organisation` | `tracking`, `order`, `speed` |
| `participatory-leisure` | `social`, `achievement`, `adventure` |
| `personality` | `alignment`, `growth` |
| `physical-safety` | `risk`, `freedom` |
| `possessions` | `functionality`, `simplicity`, `quality`, `meaning` |
| `rationality` | `accurate-beliefs`, `decision-making`, `intellectual-honesty` |
| `relationship-status` | `partner-selection`, `meeting-new-partners`, `independence`, `transition-navigation` |
| `relationship-quality` | `connection`, `harmony`, `alignment` |
| `saving` | `security`, `growth`, `lifestyle` |
| `self-awareness` | `psychological`, `contemplative`, `relational`, `experiential` |
| `sex` | `frequency`, `variety`, `pleasure`, `contentment` |
| `sleep` | `daily_functioning`, `long_term_health`, `comfort_experience` |
| `style` | `attractiveness`, `status-professional`, `expression`, `comfort` |
| `systems` | `power`, `simplicity`, `reliability` |
| `time-management` | `productivity`, `balance`, `flexibility` |
| `transportation` | `efficiency`, `comfort`, `safety` |
| `value-system` | `practical`, `insight`, `authentic`, `evolution` |
| `worldview` | `breadth`, `depth`, `utility`, `meaning` |

## Cross-Domain Discovery

After identifying the primary domain(s), systematically scan the full domain table above to find secondary benefits. For each value, ask: "Would a successful practitioner of this intervention plausibly see a meaningful effect on this value?"

### Inclusion guardrails

A cross-domain value should only be scored if ALL of the following are true:

1. **PBS >= 4**: The benefit is at least 1.56% of the anchor maximum – not a trace effect
2. **One-sentence causal pathway**: You can state the mechanism in one sentence without hand-waving (e.g., "yoga improves sleep quality via stress reduction and parasympathetic activation" passes; "yoga might somehow help career advancement" fails)

There is no cap on the number of secondary domains. If an intervention genuinely meets both tests for many domains, score all of them – broad-spectrum interventions are exactly what cross-domain scoring is designed to surface.

### Cross-domain scoring notes

- Cross-domain PBS is typically lower than primary-domain PBS. If a secondary domain scores higher, reconsider whether you have the right primary domain.
- ISR may differ across domains – the evidence base for secondary effects is often thinner, so be more conservative.
- UAR is shared across domains (same person, same intervention). For cross-domain values, reference the primary domain's UAR reasoning rather than writing redundant justification. In the YAML, still provide a uar and uar_reasoning field, but the reasoning can be brief: "See [primary domain] UAR – same intervention, same adherence profile."

### Flagging unscoreable domains

If the intervention plausibly benefits a life area that is NOT in the checklist above (e.g., mental health, time management, friends, communication), add it to the `flagged_domains` field in the output. This creates a backlog for when those areas get scoring anchors. Format:

```yaml
flagged_domains:
  - domain: "mental-health"
    rationale: "Reduces anxiety and rumination via parasympathetic activation"
  - domain: "communication"
    rationale: "Improves active listening through increased present-moment awareness"
```

## Resource Requirements Guidelines

**Upfront Costs:** Include only one-time purchases and setup expenses. Do NOT include ongoing costs like subscriptions or memberships as upfront costs. **Use conservative estimates** representing the minimum amount needed to begin the intervention effectively.

**Ongoing Costs:** Include recurring expenses like subscriptions, memberships, consumables, or regular services. **Use conservative estimates** representing the lowest-cost viable option.

**Time Requirements:** Estimate the minimum time investment needed for effective implementation, not optimal or average scenarios.

## Prerequisites Guidelines

Provide exactly 3-4 bullet points that represent true prerequisites (things that must exist before starting).

**Do NOT include:**
- Time commitments (covered in Resource Requirements)
- Cost considerations (covered in Resource Requirements)
- Alternative interventions or suggestions
- Motivation or willpower requirements

**DO include:**
- Physical capabilities or health clearances needed
- Access to specific equipment, facilities, or services
- Foundational knowledge or skills required
- Legal, age, or safety prerequisites

## Confidence

Each scoring triple must include a `confidence` field reflecting the strength of evidence behind the combined PBS/ISR/UAR estimate for that (intervention, value) pair. Use one of:

- `high`: multiple RCTs or a strong meta-analysis directly studying this intervention on this outcome
- `medium`: at least one good study directly on this intervention, or strong evidence on closely-related interventions
- `low`: mechanism is plausible; evidence is indirect, observational, or extrapolated from adjacent research

Confidence is shrinkage applied to the EBS at display time (high → factor 1.0, medium → 0.75, low → 0.5). It captures epistemic uncertainty (how well the numbers are known) and is distinct from ISR, which captures aleatoric uncertainty (variation between people).

When in doubt, default to `medium`. Reserve `high` for cases where you genuinely have strong direct evidence; reserve `low` for cases where you are extrapolating significantly.

## Dose-Response

Every intervention must include a `dose_response` block defining how the benefit scales with the user's level of engagement. The block has three parts: the metric and tier criteria (specific to the intervention), and a `value_templates` map naming a shared curve template for each scored (intervention, value) pair.

### Tier criteria

Define four tiers (0–3), each with a `level`, `label`, and `criterion`. The criterion describes a concrete user state in the intervention's natural unit (steps per day, minutes per session, nights per week, etc.). Tier 0 must represent "not doing the intervention". Tier 3 must represent the dose the PBS values are scored against (set `scored_at_tier: 3`). Tiers 1 and 2 are intermediate stages where most users live.

Labels should be intervention-specific and human-readable in context (e.g. "Sedentary / Light / Moderate / Active" for walking, "Never / Occasional / Most nights / Every night" for a sleep mask). Don't try to impose a shared vocabulary across interventions – the labels carry meaning the multipliers can't.

Default to graded tiers even for nominally on/off interventions. Most have quality and consistency dimensions that justify grading: a sleep mask can be ill-fitting or worn only some nights; a will can be outdated, incomplete, or never professionally reviewed. Reserve `binary` for genuinely one-off events.

### Choosing a template

For each scored value, pick one of the templates in `_data/dose_response_templates.yml`:

- `steep_diminishing` – biological saturation outcomes (mortality, cardiovascular events, depression symptom reduction). Half the full benefit comes from tier 1 alone; the rest from sustaining and increasing dose. Most physiological outcomes have this shape.
- `mild_diminishing` – subjective wellbeing, habit consolidation, sleep quality, enjoyment, and other outcomes that accrue with practice volume but lack a sharp plateau or have noisy evidence. **Safe default when uncertain.**
- `near_linear` – outcomes proportional to dose itself (caloric burn, time-based outcomes, financial savings, raw practice hours). Equal benefit per tier.
- `threshold` – outcomes with a clear biological minimum below which the mechanism doesn't fire (minimum sleep duration, minimum protein dose for muscle protein synthesis). No benefit until tier 2, then most of the rest there.
- `binary` – escape hatch. Only when degrees genuinely don't apply.

### Authoring rationale

Include a `rationale` field explaining (i) why the tier cuts fall where they do, anchored to the specific evidence base, and (ii) why each value got the template it did. The template choice is a judgment call about mechanism shape; make the reasoning legible so future audits can interrogate it.

## Provenance Fields (REQUIRED)

Every intervention YAML must include three provenance fields at the top level so the rendered page can show when, by which model, and against which version of this prompt the scoring was produced.

```yaml
evaluated_at: [YYYY-MM-DD]     # Today's UTC date when scoring was completed
evaluated_by: [model-id]       # Your own model ID, e.g. claude-opus-4-7
prompt_sha: [short-sha]        # Short commit SHA of this prompt at scoring time
```

**To obtain `evaluated_at`**, run:

    date -u +%Y-%m-%d

Use whatever this command returns. **Do not copy the date from a prior version of the YAML if re-evaluating an existing intervention** – the field records *when this evaluation happened*, not when the original was written.

**To obtain `prompt_sha`**, run:

    git log -1 --format=%h methodology/intervention-scoring-prompt.md

Place these three fields at the very top of the YAML, before `name:`. They are non-optional.

## Output Format

Structure your response as YAML:

```yaml
evaluated_at: [YYYY-MM-DD]
evaluated_by: [model-id]
prompt_sha: [short SHA from git log -1 --format=%h methodology/intervention-scoring-prompt.md]
name: "[Intervention Name]"
description: |
  - What the person does and how it works
  - Key details: frequency, duration, protocols
  - [Evidence](url) for key claims without naming authors
  - What makes this distinct from similar approaches
applicable_domains: ["[primary]", "[secondary1]", "[secondary2]"] # All scored domains (primary + cross-domain)

values:
  [life_area].[value_name]: # Use exact format - e.g., fitness.health, sleep.daily_functioning
    pbs: [0-10]
    isr: [0-100]
    uar: [0-100]
    confidence: [low|medium|high]
    pbs_reasoning: |
      - Baseline (per values.yml): [N]th percentile. Endpoint: [M]th percentile. Delta: [M-N] points.
      - [Specific finding with source link supporting the delta size]
      - [Specific finding with source link]
    isr_reasoning: |
      - [Specific finding with source link]
      - [Specific finding with source link]
      - [Specific finding with source link]
    uar_reasoning: |
      - [Specific finding with source link]
      - [Specific finding with source link]
      - [Specific finding with source link]

dose_response:
  metric: [snake_case_metric_id] # e.g. steps_per_day_average, minutes_per_session, nights_per_week
  metric_label: "[Human-readable label]"
  metric_help: "[Brief help text shown to user when reporting their tier]"
  scored_at_tier: 3 # The PBS values above assume this tier; almost always 3
  tiers:
    - level: 0
      label: "[Intervention-specific label]"
      criterion: "[Concrete criterion in intervention's natural unit]"
    - level: 1
      label: "[Intervention-specific label]"
      criterion: "[Concrete criterion]"
    - level: 2
      label: "[Intervention-specific label]"
      criterion: "[Concrete criterion]"
    - level: 3
      label: "[Intervention-specific label]"
      criterion: "[Concrete criterion]"
  value_templates:
    [life_area].[value_name]: [steep_diminishing|mild_diminishing|near_linear|threshold|binary]
    # ...one entry per scored value
  rationale: |
    - [Why the tier cuts fall where they do, with citations to the evidence base]
    - [Why each value got the template it did, grouped by template choice]

resources:
  upfront_cost: [USD]
  upfront_cost_reasoning: "[Minimum one-time expenses - basic equipment, essential setup only]"
  ongoing_cost: [USD]
  ongoing_cost_period: "[week/month/year]"
  ongoing_cost_reasoning: "[Minimum recurring expenses - lowest-cost viable options]"
  upfront_time: [hours]
  upfront_time_reasoning: "[Minimum time for basic setup and essential learning]"
  ongoing_time: [hours]
  ongoing_time_period: "[week/month]"
  ongoing_time_reasoning: "[Minimum effective time commitment per period]"

prerequisites:
  - "[Physical/health requirement]"
  - "[Access/equipment requirement]"
  - "[Knowledge/skill requirement]"

flagged_domains: # Life areas that plausibly benefit but lack scoring anchors
  - domain: "[life-area-slug]"
    rationale: "[One-sentence causal pathway]"
```

## Key Reminders

- Score the primary domain(s) first, then run Cross-Domain Discovery to find secondary benefits
- Use the exact `[life_area].[value_name]` format for all value domain keys
- Be conservative – err toward lower scores when evidence is limited
- Distinguish between theoretical potential and proven real-world effectiveness
- Ensure reasoning directly supports the numerical scores given
- Consider evidence quality as much as evidence quantity
- Account for individual variation in responses
- Separate one-time costs from ongoing costs appropriately
- Keep prerequisites focused and limited to 3-4 essential items only
- Use ONLY value domain keys from the Valid Value Domain Keys table above
- Flag (don't invent) any relevant life areas that lack scoring anchors
- Always include `evaluated_at`, `evaluated_by`, and `prompt_sha` at the top of the YAML
