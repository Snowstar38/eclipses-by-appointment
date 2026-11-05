# F021 TIC 300599020: REFUTED

**Completion:** COMPLETE bounded review. **Selection:** repeat_sector_dip; Gaia DR3 5268923187036636160 (SB 23.8627678097914 d).

**Physical assessment.** The retained dips are sector gap and baseline artifacts, not a repeated eclipse sequence. S67 BTJD 3146.8 is shared with F026/F029; S88 BTJD 3703.2-3703.5 is shared with F024; S94 BTJD 3875.1 repeats the same asymmetric shape and 3875.79-3876.04 gap in four unrelated targets. S65 3082/3089 and S90 3759 likewise terminate at gaps or abrupt resets. The raw Gaia-period fold has no stable narrow eclipse.

**Catalogue status.** SCOPED_NONMATCH; no target EB identification in checked tables. The exact queue catalogue evidence is in `../../shared-catalogues/target-evidence.json`; a primary-table nonmatch alone would not establish novelty.

**Limits.** This refutes the flagged signal, not the Gaia SB1 orbit or every possible faint eclipse. Available sectors 3 and 30 are uncached but the detected windows already have positive artifact evidence.

**Next check.** Inspect a future independently reduced light curve only if a new phase-coherent event appears.

**Evidence and reproduction.** The packet at `../../source-packets/300599020/sources.json` identifies and SHA256-verifies every source QLP FITS file. `lead-measurements.json` has actual quality-zero cadence coverage, source hashes and the raw local windows; `lead-event-panels.png`, `lead-alternative.json` and `lead-alternative.png` show raw and alternate QLP extraction of the same photons. The bounded scripts and shared source catalogue receipts are in the batch root. A predicted window is never treated as a fitted eclipse center.

- [lead-gaia-fold.json](lead-gaia-fold.json)
