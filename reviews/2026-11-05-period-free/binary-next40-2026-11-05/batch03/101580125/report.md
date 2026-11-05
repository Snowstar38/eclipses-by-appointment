# F029 TIC 101580125: REFUTED

**Completion:** COMPLETE bounded review. **Selection:** repeat_sector_dip; Gaia DR3 6667552039706187776 (SB 25.433856489399524 d).

**Physical assessment.** Both retained flags are the same common-mode sector event: S67 BTJD 3146.8 coincides with F021/F026 and the 3147.707-3147.927 gap; S94 BTJD 3875.1 coincides with F021/F024/F026 and the 3875.808-3876.048 gap. Raw plots show a broad asymmetric fall and abrupt reset, not repeated self-contained eclipses. The Gaia-period fold is biased by these two events.

**Catalogue status.** SCOPED_NONMATCH; no target EB identification in checked tables. The exact queue catalogue evidence is in `../../shared-catalogues/target-evidence.json`; a primary-table nonmatch alone would not establish novelty.

**Limits.** This positive artifact finding addresses the flagged dips only. S105 is currently available but uncached; it is not needed to explain the two artifacts and remains an untested future check.

**Next check.** Inspect S105 or another independent sector only if a clean eclipse away from the common gaps is identified.

**Evidence and reproduction.** The packet at `../../source-packets/101580125/sources.json` identifies and SHA256-verifies every source QLP FITS file. `lead-measurements.json` has actual quality-zero cadence coverage, source hashes and the raw local windows; `lead-event-panels.png`, `lead-alternative.json` and `lead-alternative.png` show raw and alternate QLP extraction of the same photons. The bounded scripts and shared source catalogue receipts are in the batch root. A predicted window is never treated as a fitted eclipse center.

- [lead-gaia-fold.json](lead-gaia-fold.json)
