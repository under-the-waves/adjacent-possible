# Worthwhile – Remaining Work

Last updated: 2026-04-26. This file captures all discussed-but-not-done work from recent sessions.

---

## 1. Achievement Checklist for Level Progression

**Status:** Design discussed, benchmarks rewritten, not yet built.

**What:** Users currently get stuck at Level 1 forever. Build a checklist UI on each life area index page where users confirm they meet outcome benchmarks for each level, advancing from Level 1 → 2 → 3 → 4 → 5.

**Design decisions already made:**
- Levels per value, not per life area. Each value tracks its own level independently.
- Overall life area level = weighted average (using the user's slider weights from the personalised page), rounded down.
- 59 method-focused benchmarks were rewritten to be outcome-focused so they work as checkable achievements.
- The 136 "mixed" benchmarks (mention methods alongside outcomes) should be reviewed but are probably fine.

**Implementation plan:**
- Create `_includes/level-progression.html` – self-contained component with CSS, HTML, and JS
- Reads benchmark data from `_data/life_areas/{slug}.yml` via Liquid (embedded as JS object)
- Reads current level from `ap-dashboard-levels` in localStorage
- Shows per-value progress bars + checklist for the next level on each value
- Stores checkbox state in `ap-level-checklist[slug]` in localStorage
- Computes weighted average across values using weights from `ap-slider-weights`
- Updates `ap-dashboard-levels` when a value advances
- Add `{% include level-progression.html %}` to all 53 life area index pages (scriptable)
- Only shows after Level 1 is complete (reads `ap-level1-progress`)

**Key files:**
- `_data/life_areas/*.yml` – 53 benchmark files (read-only, data source)
- `*/index.md` – 53 life area index pages (need the include added)
- `_layouts/personalised.html` – where Level 1 completion currently sets dashboard level
- `prioritisation/dashboard/index.md` – reads `ap-dashboard-levels` for display

---

## 2. Scoring Backlog – COMPLETE

**Status:** Fully complete as of 2026-04-26. The remaining 10 interventions identified on 2026-04-25 have all been scored, bringing the total to 78.

**Scored on 2026-04-26 (10 new):**
- Giving genuine compliments
- Weekly family check-ins
- Reading to children daily
- Asking for help/favours strategically
- Career planning
- Building a personal website/portfolio
- Contact management system
- Learning a musical instrument
- Learning to drive
- Basic car maintenance

**Updated scoring prompt:** `.claude/prompts/intervention.md` now includes baseline framing rules and confidence field requirements.

---

## 3. Intervention Page Creation for New Interventions – COMPLETE

**Status:** Complete as of 2026-04-26. All 42 intervention YAMLs now have corresponding stub pages in `resources/intervention-database/` using the `intervention` layout. The layout reads YAML content via `intervention_key`, so the stubs only need frontmatter (layout, title, intervention_key).

**Pre-existing follow-ups noticed during this work (not addressed):**
- `calisthenics.md` exists as a page but has no YAML in `_data/interventions/`. Either add the YAML or remove the page.
- `hiit-training.md` page title ("High-Intensity Interval Training (HIIT)") differs from the YAML name ("High Intensity Interval Training"). Reconcile if the canonical name has shifted.

---

## 4. Personalised UAR

**Status:** Discussed, deferred.

**What:** UAR is currently per-intervention (same for everyone). A personalised UAR would estimate how likely THIS user is to stick with THIS intervention, based on:
- User's habit consistency score (from habits life area assessment)
- Self-reported adherence tendency
- Intervention complexity vs user's available time

**Requires:** New user data collection mechanism (probably a short questionnaire or extension of existing Level 1 assessment for the Habits life area).

---

## 5. Population Percentile Mapping

**Status:** Discussed, deferred.

**What:** Map EBS scores to percentile shifts (e.g. "this intervention is estimated to move you from the 35th to the 60th percentile"). Currently the summary uses magnitude labels (slight/modest/meaningful/strong/transformative) instead.

**Why deferred:** Population distributions are not bell-shaped for many life areas. Needs careful per-value research on actual distributions. Could produce misleading precision if done hastily.

**When to revisit:** After the achievement checklist is built and the framework has real users whose data could inform distribution estimates.

---

## 6. "Tick Off Existing Habits" Feature

**Status:** Discussed, not built.

**What:** Users can mark interventions they already do, and see the benefit they're currently getting. Motivational (appreciate existing habits), functional (filter already-done interventions from recommendations), and informational (show counterfactual: "if you stopped doing X, you'd lose Y").

**Design consideration:** For graded interventions (e.g. smoking cessation), needs a dose-response parameterisation, not separate interventions per baseline.

---

## 7. Extract Shared Assessment JS

**Status:** Noted as future work.

**What:** All 53 level-1.md files have duplicated JS (ordinal suffix helper, percentile computation, save/restore, etc.). Extract shared functions into a single file like `assets/js/assessment-common.js` so fixes apply everywhere.

**Why not done yet:** Structural refactor touching 53 files. The ordinal suffix and rounding fixes were done via scripted find-replace, which works but doesn't solve the duplication.

---

## Quick Reference: What's Been Built

For context on what's already in place (so you don't rebuild it):

- **Intervention page template:** `_layouts/intervention.html` – new layout with What it is / Cost / How to do it / Success / Pitfalls / Prerequisites / Expected effects table / Collapsible detailed scoring
- **Intervention page content:** All 68 intervention YAMLs have `what_it_is`, `how_to_do_it`, `success_looks_like`, and `common_pitfalls` filled in
- **Intervention scoring:** 68 interventions fully scored (PBS, ISR, UAR, confidence, resources, prerequisites) using baseline framing methodology
- **Summary sentence:** Auto-generated at top of each intervention page using magnitude labels + user_description. Info popups for personalised data and effect size.
- **Bidirectional anchor scales:** All 176 values have -10 to +10 scales (benefit magnitudes, not absolute states)
- **Confidence system:** `confidence: low|medium|high` on every scoring triple, applied as shrinkage to EBS
- **Baseline + personalisation:** `baseline_percentile` on every value, sigmoid diminishing returns, "For you" / "Typical" toggle on intervention pages
- **User descriptions:** `user_description` field on all 176 values for plain-English display
- **Ordinal suffixes:** Fixed across all 53 level-1.md files
- **Percentile rounding:** Displayed as "roughly Nth percentile" (rounded to nearest 10) with uncertainty caveat
- **Scoring prompt:** `.claude/prompts/intervention.md` has baseline framing, confidence rules, and updated output format
- **Split interventions:** Daily Reflection Writing split into Daily Decision Review (goals/work) and Expressive Journaling (mental health)
- **PBS re-audit:** All original 169 scoring triples rewritten with baseline → endpoint → delta framing
- **Confidence re-audit:** All original 169 triples individually assessed (15 high, 89 medium, 65 low)
- **Media diet thresholds:** Non-fiction book percentiles updated to reflect non-fiction-specific reading rates (not all-books data)
- **Level subpage migration:** Old housework/nutrition level subpages archived; "under development" text removed from index.md
