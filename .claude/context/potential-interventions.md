# Potential Interventions – Pending Backlog

Pruned 2026-05-02. This file previously contained ~60 candidate interventions; all but a handful have been scored. The list below now tracks only items still pending, plus any new candidates surfaced through ongoing research.

For interventions that have been scored, see `_data/interventions/*.yml`. For editorial decisions on conceptual overlap between existing entries, see Item 11 in `remaining-work.md`.

---

## Deliberately deferred

These three were on the original backlog but the framing is hard to do well as a generic recommendation. They likely need bespoke handling – perhaps a "decision-aid" page format rather than a scored intervention with a recommended action.

- **Changing friend groups** – peer-effects-as-leverage. Cuts against social loyalty norms. Could be reframed as "auditing your social environment" or "deliberately curating peer influences" but the most-impactful framing ("change your friends") is provocative.
- **Breaking up with the wrong romantic partner** – context-dependent and emotionally loaded. The relationship-status life area covers `partner-selection` and `transition-navigation` as values, but a "score this and recommend it" intervention model fits poorly when the answer is genuinely person-specific.
- **Moving city or country** – flagged in the original backlog as "potentially transformative but huge upfront costs (financial, social, emotional)." The PBS could be very high but UAR and ISR are wildly context-dependent. A decision-aid page format would suit this better than a scored entry.

---

## Other ideas worth research before scoring

(Empty for now. Add new candidates here as they emerge from user feedback, literature scans, or coverage-gap analysis. The 2026-05-02 coverage-gap research already identified and scored 14 high-value gaps; future research should focus on areas not covered by that pass.)

---

## Notes for future scoring runs

- **Always check existing files first** by listing `_data/interventions/` and grepping for plausible alternative names. The 2026-05-02 round found 4 candidates already silently scored under different filenames (learning-to-name-emotions-precisely, basic-active-listening-skills, regular-one-on-one-conversations, optimising-lighting covered the candidate light-anchored sleep schedule).
- **Use the agent's overlap-check pattern**: read filename + `name:` field across all existing YAMLs before proposing or scoring. A duplicate written under a new slug creates database mess that's hard to clean up later.
- The current scoring methodology is at `methodology/intervention-scoring-prompt.md` – read its "Country-Neutral Framing" section for the term-substitution rules and the "Baseline Framing" section for the PBS reasoning pattern.
