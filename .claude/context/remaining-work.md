# Worthwhile – Remaining Work

Last updated: 2026-05-02. This file captures all discussed-but-not-done work from recent sessions.

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

**Phase 3 candidates (not built):**
- **Dashboard integration** – show habit count + aggregate magnitude per life area on the prioritisation dashboard
- **Counterfactual** – "If you stopped doing X, you'd lose Y" on intervention pages
- **Graded intervention support** – currently binary doing/not-doing. Things like "I meditate 3 days/week" vs "daily" aren't reflected. Needs dose-response parameterisation per intervention.

---

## 7. Confidence Factor Inconsistency Between Pages – FIXED

**Status:** Fixed 2026-05-02. The `_layouts/personalised.html` WBS Liquid template now includes `+ Math.log2(confidence_factor)` (1.0 / 0.75 / 0.5 for high / medium / low). Personalised-page WBS now matches intervention-page EBS exactly.

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
