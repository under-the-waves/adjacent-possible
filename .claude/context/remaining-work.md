# Worthwhile – Remaining Work

Last updated: 2026-06-01 (after the new signed-log EBS/EROI rollout, Quick Wins page, dose-response authoring across all 134 interventions, and tier-aware personalised table). This file captures all discussed-but-not-done work from recent sessions.

---

## 1. Achievement Checklist for Level Progression – COMPLETE

**Status:** Built and shipped. `_includes/level-progression.html` is included in all 53 life-area `index.md` files. Reads benchmarks from `_data/life_areas/{slug}.yml`, gates on Level 1 completion + slider weights, stores per-value checklist state in `ap-level-checklist`, computes weighted-average overall level, syncs to `ap-dashboard-levels`.

**Reframing pass on 2026-05-02:** Header changed from "Level Progression" to "Where You Sit"; overall hint changed from "weighted average, rounded down" to "weighted by your value priorities". Aligns with the percentile-bands reframing (see Quick Reference).

---

## 2. Scoring Backlog – COMPLETE

**Status:** Fully complete as of 2026-04-26. Total scored: 78.

**Updated scoring prompt:** `methodology/intervention-scoring-prompt.md` includes baseline framing rules, confidence field requirements, and country-neutral framing rules.

---

## 3. Intervention Page Creation for New Interventions – COMPLETE

**Status:** Complete as of 2026-04-26. All intervention YAMLs have corresponding pages in `resources/intervention-database/` using the `intervention` layout. Two pre-existing follow-ups (calisthenics missing YAML; hiit-training page/YAML name mismatch) verified resolved 2026-05-02 – calisthenics.yml exists and matches its page; hiit-training YAML name is now "High-Intensity Interval Training (HIIT)", matching the page title.

---

## 4. Personalised UAR – APPROACH CHANGED

**Status:** Earlier plan (infer UAR from Habits L1 assessment) replaced by a simpler explicit-edit approach. See Item 9 for the user-editable scoring discussion.

**Original idea:** Infer adherence from Habits life area assessment, calibrate per-intervention UAR adjustments. Substantial work requiring data-collection design and formula calibration.

**Replacement plan:** Add a single global UAR multiplier slider where the user self-rates their habit consistency. Scales all UARs by one factor. Less prone to motivated bias than per-intervention UAR overrides because users have to commit to one self-assessment, not 78 individual ones.

**Status:** Not yet implemented. Plan was agreed on 2026-05-02 alongside the cost-override feature (Item 9).

---

## 5. Population Percentile Mapping

**Status:** Explicitly deferred.

**What:** Map EBS scores to percentile shifts (e.g. "this intervention is estimated to move you from the 35th to the 60th percentile"). Currently the summary uses magnitude labels (slight/modest/meaningful/strong/transformative).

**Why deferred:** Population distributions are not bell-shaped for many life areas. Needs careful per-value research. Could produce misleading precision if done hastily.

**When to revisit:** After the framework has real users whose data could inform distribution estimates.

---

## 6. "Tick Off Existing Habits" – MVP + FILTER SHIPPED

**Status:** MVP shipped 2026-05-02. Phase 2 filter shipped 2026-05-02. Users can mark interventions they currently do (state in `ap-habits-current`) and optionally hide them from the personalised recommendations table (state in `ap-habits-hide-doing`).

**What's built:**
- Toggle row on intervention pages (below H1) with magnitude indicator that updates when "For you" / "Typical" view changes
- Per-row checkmark on personalised pages; marked rows get a faded green background
- Summary line above the personalised table: "You're already doing N habits in this area, providing a [magnitude] benefit to your priorities"
- Aggregate magnitude uses log-sum-exp across positive WBS contributions (correct for log-scale benefits)
- Filter checkbox: "Hide them from recommendations" appears below the summary when at least one habit is marked. Persisted in localStorage. Summary count remains accurate (uses unfiltered list).

**Phase 3 status:**
- **Dashboard integration** – SHIPPED 2026-05-19. Dashboard cards show "Doing X of 5" per life area, using priority-weighted WBS ranking and the new graded tier data. See Item 13.
- **Graded intervention support** – SHIPPED 2026-05-18 to 2026-05-19 via Item 13. Binary doing/not-doing is now replaced by the four-tier dose-response model across all 134 interventions.
- **Counterfactual** – not built. "If you stopped doing X, you'd lose Y" on intervention pages. Now naturally expressible as the captured benefit at the current tier; the framing copy is the remaining work.

---

## 7. Confidence Factor Inconsistency Between Pages – FIXED

**Status:** Fixed 2026-05-02. The `_layouts/personalised.html` WBS Liquid template now includes `+ Math.log2(confidence_factor)` (1.0 / 0.75 / 0.5 for high / medium / low). Personalised-page WBS now matches intervention-page EBS exactly.

---

## 12. X-risk-focused interventions and worldview-relativity – DEFERRED

**Status:** Discussed 2026-05-02. Not yet implemented; the framework needs to mature further before adding these. Capturing the design here so the thinking doesn't get lost.

**The argument that surfaced this:** Many interventions implicitly assume civilisational continuity over decades (retirement-account-maximisation, long-term index investing, career planning). A user who assigns meaningful probability to existential catastrophe within a few years – particularly from AGI – should rationally weight these differently. More strongly: if catastrophe is genuinely imminent and the user has any leverage, x-risk reduction work plausibly dominates ordinary personal-flourishing interventions.

**Where this lands philosophically:** The framework should accommodate this worldview without endorsing it. Build the interventions; let the slider-weight mechanism surface them for users who weight relevant values heavily.

**Three candidate interventions:**

1. **Donating to x-risk reduction organisations** – Long-Term Future Fund, Open Philanthropy longtermist grants, AI safety orgs (MIRI, Redwood, etc.), biosecurity orgs. Parallel to the existing `effective-giving` but cause-area-specific. Likely scoring: PBS 10 saturated on `global-impact.impartiality`, ISR ~20% (real uncertainty about which orgs reduce risk), UAR ~65% (automated donation).
2. **Career pivot to x-risk reduction** – technical AI alignment, AI governance, biosecurity, evals work. PBS 10 on impartiality, 7-8 on `life-purpose.meaning` and `current-work.engagement`, negative on `saving.security`. ISR ~40%, UAR ~10% (career pivots are rare).
3. **AI policy engagement** – public comments on AI regulation, writing to representatives, consultation participation. Lower PBS (~8), low ISR (~15%), moderate UAR (~30%).

**Architectural notes:**
- PBS saturates at 10 honestly rather than pretending the scale extends further. The longtermist case has unbounded value mathematically; the framework's scale doesn't.
- ISR and UAR pull EBS back to realistic levels (estimated EBS roughly 4-8 across the three).
- Cross-domain scoring is what surfaces these for the right users. Career pivot scored across `global-impact`, `life-purpose`, `current-work`, `saving` (negatively) – appears on multiple personalised pages.
- Slider weights are the worldview input. A user with strong x-risk priors weights `global-impact.impartiality` heavily and sees x-risk interventions float to the top automatically. No parallel recommendation tracks needed.

**Time-horizon discount interaction:** If the horizon-discount feature (Item 13 below, hypothetical) is built, x-risk interventions need a `time_horizon: continuity` tag exempting them from the discount. They're not "long-horizon payoff" interventions; they're "preserve the existence of the long horizon at all" interventions. Different category.

**Why deferred:** The framework needs to mature in other dimensions first (Layer 2 country-resources, dashboard integration, UAR multiplier, larger user base). Adding x-risk interventions now risks looking partisan or specific to one subculture before the framework has enough breadth to absorb them as one set among many.

**When to revisit:** When the library is broader, when the worldview-discount mechanism is built (or explicitly rejected), or when user feedback indicates demand. The architectural readiness is fine; the editorial readiness is not.

---

## 11. Editorial decisions flagged by 2026-05-02 coverage expansion – RESOLVED

All three resolved 2026-05-02:

1. **`retirement-account-maximisation` vs `basic-tax-optimisation`**: kept distinct. They serve different jobs (foundational understanding of tax wrappers vs the operational annual maxing waterfall). Cross-references already present in both entries.
2. **`smartphone-greyscale-minimalism` vs `phone-notification-management`**: kept distinct, cross-reference added in both directions. The two interventions address complementary failure modes (input curation vs perceptual pull) and stack cleanly.
3. **`optimising-lighting` renamed**: now `light-anchored-sleep-schedule` (file, slug, stub title, YAML name, opening framing). The previous name undersold the intervention's purpose; new name is sleep-discoverable. Internal references checked: nothing else in the repo referenced the old slug.

---

## 9. User-Editable Resource Estimates – TIME AND MONEY SHIPPED

**Status:** Time and money cost overrides shipped 2026-05-02. UAR multiplier still pending (see Item 4).

**Concept:** PBS and ISR represent the science (locked, evidence-based). UAR and resource costs are population estimates that vary widely by user circumstances – worth letting users override.

**What's built (cost overrides):**
- Intervention page has a "Personalise these costs" expandable section under the Cost list
- Four numeric inputs (upfront cost, ongoing cost, upfront time, ongoing time) plus period dropdowns (day/week/month/year)
- Save and Reset buttons; Save persists via APStorage (`ap-intervention-overrides`) so values sync across devices when authenticated
- Edited values shown in italic with "(your estimate)" tag in the cost list
- Personalised page applies overrides to Time EROI and Money EROI calculations; edited cells in the table show italic with a red asterisk
- Reasoning popups continue to show the original population breakdown – the override is the user's adjustment, not a replacement of the evidence

**Storage shape:**
```js
{ "intervention-key": { upfront_cost: 0, ongoing_time: 0.5, ongoing_time_period: "day" } }
```
Only fields differing from population are stored. Empty object removed entirely on reset.

**What's NOT in scope for cost overrides:**
- PBS, ISR, confidence – locked
- UAR – needs the global multiplier approach (Item 4)

---

## 8. Extract Shared Assessment JS

**Status:** Noted as future work.

**What:** All 53 level-1.md files have duplicated JS (ordinal suffix helper, percentile computation, save/restore, etc.). Extract shared functions into a single file like `assets/js/assessment-common.js` so fixes apply everywhere.

**Why not done yet:** Structural refactor touching 53 files with no user-visible value. Worth doing opportunistically the next time these files are touched, not as a standalone push.

---

## 10. Country-Neutral Framing – DONE FOR LAYER 1

**Status:** Layer 1 (country-neutral body, US-aligned cost defaults) shipped 2026-05-02. Layer 2 (per-intervention `country_resources` YAML block) still pending.

**Background:** Site originally mixed UK and US framing inconsistently. We agreed on a three-layer approach:
- Layer 1 (DONE): Body prose goes country-neutral. Population data and cost defaults use US-aligned figures. Citations stay country-specific where attributed. British spelling stays.
- Layer 2 (NOT DONE): Per-intervention `country_resources` YAML block for genuinely country-specific links and prices. User picks country once, layout shows the matching block.
- Layer 3 (DONE): User cost overrides (Item 9) handle the long tail of individual variation.

**What's been built (Layer 1):**
- `methodology/intervention-scoring-prompt.md` has a "Country-Neutral Framing" section: term substitution table (GP/NHS/ISA/401k/etc), citation-vs-prescription distinction, cost-reasoning guidance for healthcare-system-variable interventions
- 24 of 78 intervention YAMLs reworded for country-neutral prose (pilot 2 + sweep 22). Five files in the candidate list were already neutral.
- US-aligned cost defaults applied to healthcare and driving interventions: getting-diagnosed ($25 → $300), therapy-cbt ($120 → $400/month), quitting-smoking ($30 → $80/month), learning-to-drive ($800 → $500). Other healthcare interventions (family-of-origin-therapy, glp1-agonists, dental-hygiene-optimisation, preventive-health-screening) already had US-aligned figures.

**Layer 2 plan (when ready):**
```yaml
country_resources:
  UK:
    booking: "..."
    typical_cost: "Free at point of use (NHS)"
    references: ["..."]
  US:
    booking: "..."
    typical_cost: "$200-400 self-pay or insurance copay"
    references: ["..."]
  default:
    guidance: "..."
```
Layout reads `ap-user-country` from localStorage (set once at first visit or via a settings link), shows the matching block, falls back to `default`. Adding a new country = appending one section. Probably ~20-30% of the library actually needs this.

**Country detection:** Don't auto-detect from IP. Add a one-time prompt at first visit; save to `ap-user-country` localStorage; settings link in the footer to change.

---

## 13. Graded Interventions / Dose-Response – AUTHORING, DASHBOARD, PERSONALISED TABLE SHIPPED

**Status:** Major chunks shipped between 2026-05-18 and 2026-05-19. Authoring complete across all 134 interventions. Intervention-page UX, dashboard rollup, and personalised-page table are all tier-aware.

**Design decisions (locked):**
- Every intervention defines its own 4-tier scale (level 0 = not doing, level 3 = the dose PBS was scored against) with intervention-specific labels and concrete criteria in the metric's natural units. See `daily-walking.yml` as the reference.
- A shared template library at `_data/dose_response_templates.yml` defines five named curve shapes via multiplier arrays: `steep_diminishing`, `mild_diminishing` (default for noisy subjective outcomes), `near_linear`, `threshold`, `binary` (escape hatch, rarely used).
- Each (intervention, value) pair in `dose_response.value_templates` names one template. Explicit per-pair, no intervention-level default. Tier labels are intervention-specific (no shared vocabulary).
- Default to graded even for nominally on/off interventions – most have quality or consistency dimensions (sleep-mask fit, will currency, 2FA account coverage) that justify grading.
- `baseline_percentile` (outcome calibration) and Tier 0 (intervention adherence) are orthogonal axes; the methodology subsection in the scoring prompt explains the distinction.
- UAR represents future adherence and applies to the *remaining-tier* portion when the user reports being partially adherent. We do not model per-transition UAR – sticking with one intervention-level UAR avoids over-crediting users at higher tiers due to incidental factors (a marathon runner with 2,000 commute steps hasn't demonstrated walking adherence).
- T3-vs-original framing is preserved: at tier 3, graded EBS exceeds the original UAR-weighted EBS because the user has demonstrated adherence. Copy on the intervention page distinguishes "Your current benefits" (no UAR) from population averages.
- Dashboard ranking is priority-weighted WBS (matching the personalised page); "Doing" threshold is tier ≥ 2.

**What shipped:**
- `_data/dose_response_templates.yml` – five curve shapes with corrected (front-loaded) multipliers.
- `_data/interventions/*.yml` – all 134 interventions now declare a `dose_response` block with metric, tier criteria, value_templates, and rationale.
- `methodology/intervention-scoring-prompt.md` – new `## Dose-Response` section, `dose_response` YAML block in the output-format template, and the `baseline_percentile` vs. Tier 0 distinction subsection. Future scoring runs include it automatically.
- `_layouts/intervention.html` – tier picker, "Your current benefits" summary, progression list with magnitude-language descriptions, sustainability paragraph (conditional on low UAR), "Going strong" badge at the scored tier, ordinal-suffix bug fix (71st rather than 71th). Hidden when an intervention lacks `dose_response` (no current cases since all 134 are authored).
- `prioritisation/dashboard/index.md` – every life-area card on the dashboard shows "Doing X of 5" alongside its level badge. Ranking inlines all interventions plus the EBS/WBS computation and reads `ap-habits-tier` localStorage.
- `_layouts/personalised.html` (shipped 2026-05-19, commit `21068d1`) – per-row WBS is tier-aware via `computeEbsForTier`, the table reads `ap-habits-tier` with a legacy fallback to `ap-habits-current` (treated as tier 2), a tier badge appears next to interventions the user is doing, and the "Hide them from recommendations" filter uses the dashboard's tier ≥ 2 threshold. The aggregate-magnitude summary line uses log-sum-exp over the tier-aware WBS contributions.

**Not yet done:**
- **Storage migration / cleanup.** Old `ap-habits-current` (binary `{key: true}`) still exists alongside the new `ap-habits-tier` (`{key: tier_index}`). The personalised page reads both (legacy `true` → tier 2); the intervention page only writes `ap-habits-tier`. A one-shot migration that copies `ap-habits-current` into `ap-habits-tier` (and clears the legacy key) at first read would let us delete the fallback branch and the dead `toggleHabit` / `getCurrentHabits` helpers in `personalised.html`. The ungraded-intervention branch in `_layouts/intervention.html` (`habit-toggle`, `initHabitToggle`) is also dead since all 134 interventions now have a `dose_response` block.
- **Magnitude-language extension to the dashboard and personalised table.** The dashboard currently shows a count ("Doing 2 of 5"). It could also surface aggregate magnitude ("a strong benefit captured so far") using log-sum-exp across the user's tier-weighted EBS for the area, matching the existing intervention-page summary sentence style.
- **Rationale-block audit for stretched templates.** Several authoring agents used `threshold` for behavioural all-or-nothing mechanisms (calorie-tracking, accessible health records, memento-mori brief vs. sustained engagement). Methodology currently describes `threshold` as a biological-minimum cutoff. Either broaden the methodology subsection or revisit those template assignments.
- **Copy refinement.** The "Sustainability" sentence is only shown when median UAR < 70%; works for walking and smoking. Other low-UAR interventions (gym-based training, journaling) should be spot-checked to confirm the copy lands.

---

## 14. Baseline Percentile Audit – DEFERRED

**Status:** Discussed 2026-05-18, deferred.

**What:** The `baseline_percentile` field on each of 176 values in `_data/values.yml` defaults to 35 (the calibration point against which PBS represents its scored value). The default is reasonable for most subjective wellness outcomes, but is plausibly wrong for three categories:
- **Completeness / one-off values** ("has an up-to-date will", "has an emergency fund") – non-adopters are at ~5–10th percentile, not 35. Current default makes user discounts too aggressive.
- **Universally average values** – most people sit near the middle (housing.affordability already overrides to 50). Default may understate baseline elsewhere too.
- **High-floor subjective values** – e.g. life satisfaction tends to cluster at 40–50 even for non-adopters. Default may understate.

**Suggested approach when revisited:** Targeted audit of the ~30 values that plausibly fall in one of the three patterns, rather than full pass over all 176. Most values can stay at 35.

**Why deferred:** Recommendations are mostly defensible at the current defaults; cost of being wrong is "slightly mis-calibrated", not "system breaks". Lower priority than the dose-response work and dashboard integration.

---

## Quick Reference: What's Been Built

For context on what's already in place (so you don't rebuild it):

- **Intervention page template:** `_layouts/intervention.html` with What it is / Cost / How to do it / Success / Pitfalls / Prerequisites / Expected effects table / Collapsible detailed scoring
- **Intervention page content:** All 78 intervention YAMLs have `what_it_is`, `how_to_do_it`, `success_looks_like`, and `common_pitfalls` filled in
- **Intervention scoring:** 78 interventions fully scored (PBS, ISR, UAR, confidence, resources, prerequisites) using baseline framing methodology
- **Summary sentence:** Auto-generated at top of each intervention page using magnitude labels + user_description. Info popups for personalised data and effect size.
- **Bidirectional anchor scales:** All 176 values have -10 to +10 scales (benefit magnitudes, not absolute states)
- **Confidence system:** `confidence: low|medium|high` on every scoring triple, applied as shrinkage to EBS on intervention pages and to WBS on personalised pages (matched as of 2026-05-02)
- **Baseline + personalisation:** `baseline_percentile` on every value, sigmoid diminishing returns, "For you" / "Typical" toggle on intervention pages
- **User descriptions:** `user_description` field on all 176 values for plain-English display
- **Ordinal suffixes:** Fixed across all 53 level-1.md files
- **Percentile rounding:** Displayed as "roughly Nth percentile" (rounded to nearest 10) with uncertainty caveat
- **Scoring prompt:** `methodology/intervention-scoring-prompt.md` has baseline framing, confidence rules, country-neutral framing rules, and updated output format
- **Split interventions:** Daily Reflection Writing split into Daily Decision Review (goals/work) and Expressive Journaling (mental health)
- **PBS re-audit:** All original 169 scoring triples rewritten with baseline → endpoint → delta framing
- **Confidence re-audit:** All original 169 triples individually assessed (15 high, 89 medium, 65 low)
- **Media diet thresholds:** Non-fiction book percentiles updated to reflect non-fiction-specific reading rates
- **Achievement checklist:** `_includes/level-progression.html` shipped to all 53 life-area index pages (per-value checklists, weighted overall level, dashboard sync)
- **Tick-off-existing-habits MVP:** Toggle on intervention pages and per-row checkmarks on personalised pages, with aggregate-magnitude summary
- **Level reframing (percentile bands):** Thematic level names (Foundation/Proficiency/Excellence/Mastery) replaced with percentile labels (Top 20% / Top 5% / Top 1% / Top 0.1%) on 2026-05-02. Level 1 stays as Awareness. Internal data structures (`level_1` keys, `level-N.md` filenames) unchanged. Canonical user-facing explainer at `other-resources/5-levels.md`.
- **Legacy level subpage cleanup:** Orphaned `nutrition/level-{2-5}.md` and `housework/level-{2-5}.md` pages deleted on 2026-05-02. Their benchmarks were superseded by the per-value YAML structure; their action/habit/cost content was partially superseded by the intervention library. Original content also exists in `.claude/context/archived-level-pages/` (along with archived fitness pages and others).
- **In-repo archive folder:** `.claude/context/archived-level-pages/` (gitignored) holds historic versions of life-area pages from before the new pattern – useful when content needs to be recovered or referenced.
- **Country-neutral framing pass:** Body prose audited and rewritten across the intervention library (24/78 files modified, others already neutral). US-aligned cost defaults applied to healthcare and driving interventions. Citations stay country-specific where attributed; British spelling stays as a writing convention. Layer 2 (per-intervention `country_resources` YAML for explicit per-country links and prices) still pending.
- **Coverage expansion (2026-05-02):** Library grew from ~78 to ~92 scored interventions. 16 new interventions filled gaps in children, relationships, sex, finance behaviours, productivity habits, housework, food management, and community contribution. Filenames: `leveraging-personality-strengths`, `developing-signature-style`, `authoritative-parenting-routines`, `daily-outdoor-play-children`, `gottman-couple-skills`, `sexual-communication-script`, `retirement-account-maximisation`, `sinking-fund-system`, `alcohol-moderation-trial`, `implementation-intentions`, `weekly-review-ritual`, `smartphone-greyscale-minimalism`, `daily-home-reset-routine`, `weekly-meal-planning`, `weekly-third-place-attendance`, `regular-blood-donation`. Backlog file (`.claude/context/potential-interventions.md`) was pruned to remove items now scored.
- **Signed-log EBS formula (2026-05-04):** Both `_layouts/intervention.html` and `_layouts/personalised.html` use `EBS = sign(EV) × log₂(1 + |EV|)` where the linear EV is `sign(PBS) × (2^|PBS| − 1) × ISR × UAR × confidence × drFactor`. The new formula keeps EBS positive for any positive expected value (no log-of-small-number trap), negative for negative-PBS harms, and approximately doubles per unit for typical magnitudes. Commits `f10115a` and `a924447`.
- **Signed-log EROI formula with per-value `scale_factor` (2026-05-04):** `EROI = sign(EBS) × log₂(1 + (linear EV / cost) / scale_factor)`, applied to both Time and Money EROI. Each value in `_data/values.yml` carries `scale_factor_money` and `scale_factor_time`, calibrated empirically so the median intervention sits at EROI ≈ 5 within the value. Commit `19e77e2`.
- **Driver column on personalised pages (2026-05-04):** Each row's WBS surfaces the value whose weighted contribution has the largest absolute magnitude. EROIs are computed against that Driver value's scale factors. Commit `a924447`.
- **Quick Wins page (2026-05-04):** New page at `prioritisation/quick-wins/` surfaces interventions flagged with `quick_win: true` and `quick_win_cadence: setup | rare_check | routine`. Filter uses an EROI floor rather than EBS to capture rare-event protective interventions (smoke alarms, beneficiary designations, 2FA) where the asymmetric payoff dominates. 10 new interventions added. Commits `b865c42`, `c89d179`, `ab61345`, `9cf9a71`.
- **Rare-event protective scoring rule + QALY calibration (2026-05-04):** `methodology/intervention-scoring-prompt.md` documents that PBS captures the conditional life-saved magnitude and ISR captures the lifetime probability of being saved, rather than folding base rate into PBS. QALY anchoring with the $100K/QALY threshold and 2× loss-aversion multiplier for safety/health values is documented. Commit `0030570`.
- **Bands as user-facing term (2026-05-04):** Replaced "levels" with "bands" in user-facing copy across the site and rewrote the How to Use page. Internal data keys (`level_1`, `level-N.md`, `/5-levels/`) retain the original naming. Commit `a130963`.
- **Sign-in gating on intervention-page personalisation (2026-05-04):** Personalised EBS only displays when Clerk reports the user as signed in; anonymous localStorage data is treated as transient. Page re-renders on `ap-clerk-ready` and `ap-auth-change`. Commits `36709f4`, `24896dd`, `464dab5`.
- **Tier-aware personalised page (2026-05-19):** See Item 13.
- **Dose-response authoring across all 134 interventions (2026-05-18 to 2026-05-19):** See Item 13.
