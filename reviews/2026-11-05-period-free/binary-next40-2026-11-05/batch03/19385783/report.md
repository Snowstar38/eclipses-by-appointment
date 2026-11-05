# F028 TIC 19385783: PROBABLE

**Completion:** COMPLETE bounded review. **Selection:** repeat_sector_dip; Gaia DR3 3062493586800148992 (SB 35.085635650028166 d).

**Physical assessment.** Narrow raw SAP dips recur in S7, S34, S61 and S88. Twelve non-singular centers in the latter three sectors fit the 2.065942-d dip recurrence with 0.0014 d RMS. Explicit neighboring integer-cycle aliases at 2.060152 and 2.071765 d have 0.0178 and 0.0189 d RMS; 45 predicted windows have actual full quality-zero core plus bilateral baseline and typically 7-11 ppt losses. QLP corrected flux independently preserves S7/S34 dips. The nearest Gaia G21.25 source at 12.19 arcsec lacks enough approximate total flux to supply the observed deficit.

**Catalogue status.** SCOPED_NONMATCH; no target EB identification in checked tables. The exact queue catalogue evidence is in `../../shared-catalogues/target-evidence.json`; a primary-table nonmatch alone would not establish novelty.

**Limits.** The sector-34 TESSCut difference image is inconclusive for ownership because an unrelated excess biases its centroid. Gaia SB1 P35.0856 d is not the measured dip recurrence and its conjunction is 0.231 phase away at S34; the orbital relationship is unresolved. The physical orbit might be an integer multiple of the observed dip cadence; the reported clock is a photometric recurrence, with no defensible period error.

**Next check.** Obtain a clean difference image or ground-based resolved photometry and test the Gaia orbit versus a separate short-period binary.

**Evidence and reproduction.** The packet at `../../source-packets/19385783/sources.json` identifies and SHA256-verifies every source QLP FITS file. `lead-measurements.json` has actual quality-zero cadence coverage, source hashes and the raw local windows; `lead-event-panels.png`, `lead-alternative.json` and `lead-alternative.png` show raw and alternate QLP extraction of the same photons. The bounded scripts and shared source catalogue receipts are in the batch root. A predicted window is never treated as a fitted eclipse center.

- [lead-shortperiod.json](lead-shortperiod.json)
- [lead-alias.json](lead-alias.json)
- [lead-coverage.json](lead-coverage.json)
- [helper-pixels.json](helper-pixels.json)
