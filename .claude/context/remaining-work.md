# Worthwhile – Remaining Work

Last updated: 2026-05-02. This file captures all discussed-but-not-done work from recent sessions.

---

## 1. Achievement Checklist for Level Progression – COMPLETE

**Status:** Built and shipped. `_includes/level-progression.html` is included in all 53 life-area `index.md` files. Reads benchmarks from `_data/life_areas/{slug}.yml`, gates on Level 1 completion + slider weights, stores per-value checklist state in `ap-level-checklist`, computes weighted-average overall level, syncs to `ap-dashboard-levels`.

**Reframing pass on 2026-05-02:** Header changed from "Level Progression" to "Where You Sit"; overall hint changed from "weighted average, rounded down" to "weighted by your value priorities". Aligns with the percentile-bands reframing (see Quick Reference).

---

## 2. Scoring Backlog – COMPLETE

**Status:** Fully complete as of 2026-04-26. Total scored: 78.

**Updated scoring prompt:** `.claude/prompts/intervention.md` includes baseline framing rules and confidence field requirements.

---

## 3. Intervention Page Creation for New Interventions – COMPLETE

**Status:** Complete as of 2026-04-26. All intervention YAMLs have corresponding pages in `resources/intervention-database/` using the `intervention` layout.

**Pre-existing follow-ups (not addressed):**
- `calisthenics.md` exists as a page but has no YAML in `_data/interventions/`. Either add the YAML or remove the page.
- `hiit-training.md` page title ("High-Intensity Interval Training (HIIT)") differs from the YAML name ("High Intensity Interval Training"). Reconcile if the canonical name has shifted.

---

## 4. Personalised UAR

**Status:** Discussed, deferred. Likely the next big conceptual piece.

**What:** UAR is currently per-intervention (same for everyone). A personalised UAR would estimate how likely THIS user is to stick with THIS intervention, based on:
- User's habit consistency score (from Habits life area Level 1 assessment, which already exists)
- Self-reported adherence tendency
- Intervention complexity vs user's available time

**Why this is the next big piece:** PBS is already personalised (via baseline percentile + sigmoid diminishing returns), and weights are already personalised (via slider weights). UAR is the remaining un-personalised variable. Closing this gap completes the personalisation triangle.

**Requires:** New user data collection mechanism (probably extension of Habits life area Level 1) plus calibration of the UAR adjustment formula.

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

## 8. Extract Shared Assessment JS

**Status:** Noted as future work.

**What:** All 53 level-1.md files have duplicated JS (ordinal suffix helper, percentile computation, save/restore, etc.). Extract shared functions into a single file like `assets/js/assessment-common.js` so fixes apply everywhere.

**Why not done yet:** Structural refactor touching 53 files with no user-visible value. Worth doing opportunistically the next time these files are touched, not as a standalone push.

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
- **Scoring prompt:** `.claude/prompts/intervention.md` has baseline framing, confidence rules, and updated output format
- **Split interventions:** Daily Reflection Writing split into Daily Decision Review (goals/work) and Expressive Journaling (mental health)
- **PBS re-audit:** All original 169 scoring triples rewritten with baseline → endpoint → delta framing
- **Confidence re-audit:** All original 169 triples individually assessed (15 high, 89 medium, 65 low)
- **Media diet thresholds:** Non-fiction book percentiles updated to reflect non-fiction-specific reading rates
- **Achievement checklist:** `_includes/level-progression.html` shipped to all 53 life-area index pages (per-value checklists, weighted overall level, dashboard sync)
- **Tick-off-existing-habits MVP:** Toggle on intervention pages and per-row checkmarks on personalised pages, with aggregate-magnitude summary
- **Level reframing (percentile bands):** Thematic level names (Foundation/Proficiency/Excellence/Mastery) replaced with percentile labels (Top 20% / Top 5% / Top 1% / Top 0.1%) on 2026-05-02. Level 1 stays as Awareness. Internal data structures (`level_1` keys, `level-N.md` filenames) unchanged. Canonical user-facing explainer at `other-resources/5-levels.md`.
- **Legacy level subpage cleanup:** Orphaned `nutrition/level-{2-5}.md` and `housework/level-{2-5}.md` pages deleted on 2026-05-02. Their benchmarks were superseded by the per-value YAML structure; their action/habit/cost content was partially superseded by the intervention library. Original content also exists in `.claude/context/archived-level-pages/` (along with archived fitness pages and others).
- **In-repo archive folder:** `.claude/context/archived-level-pages/` (gitignored) holds historic versions of life-area pages from before the new pattern – useful when content needs to be recovered or referenced.
