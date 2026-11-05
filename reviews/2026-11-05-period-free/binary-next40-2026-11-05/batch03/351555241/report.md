# F025 TIC 351555241: REFUTED

**Completion:** COMPLETE bounded review. **Selection:** repeat_sector_dip; Gaia DR3 6426599941995042304 (SB 33.69796608468139 d).

**Physical assessment.** Only two retained flags occur in S101 and S103, and both are abrupt sector gap transitions rather than self-contained eclipses. The S101 event begins after the 4113.264-4114.393 gap and merges into a long baseline slope. The S103 event cuts off at the 4165.080-4166.129 gap; S102 shows a similar large discontinuous state change. Their separation cannot establish a same-kind cycle. The Gaia-period fold is dominated by the repeated sector-step morphology.

**Catalogue status.** SCOPED_NONMATCH; no target EB identification in checked tables. The exact queue catalogue evidence is in `../../shared-catalogues/target-evidence.json`; a primary-table nonmatch alone would not establish novelty.

**Limits.** The false flagged dips do not rule out a separate low-amplitude EB signal. All local flagged-event fits are bound or singular affected.

**Next check.** Require a complete eclipse with ingress, core and egress away from a sector gap.

**Evidence and reproduction.** The packet at `../../source-packets/351555241/sources.json` identifies and SHA256-verifies every source QLP FITS file. `lead-measurements.json` has actual quality-zero cadence coverage, source hashes and the raw local windows; `lead-event-panels.png`, `lead-alternative.json` and `lead-alternative.png` show raw and alternate QLP extraction of the same photons. The bounded scripts and shared source catalogue receipts are in the batch root. A predicted window is never treated as a fitted eclipse center.

- [lead-gaia-fold.json](lead-gaia-fold.json)
