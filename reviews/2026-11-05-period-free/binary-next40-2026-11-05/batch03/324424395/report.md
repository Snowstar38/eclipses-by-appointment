# F022 TIC 324424395: PROBABLE

**Completion:** COMPLETE bounded review. **Selection:** repeat_sector_dip; Gaia DR3 6415022359433384576 (SB 27.751344966266142 d).

**Physical assessment.** Deep alternating eclipse-like events recur in raw SAP from S13 through S103. Eight predicted deep cores have actual full quality-zero coverage and bilateral baseline; representative local losses are 56-85 ppt. Raw SAP BLS favors about 27.7685 d as a diagnostic, near VSX ESD 27.760 d, and the sector-93 TESSCut difference is concentrated on the target PSF. The G10.05 target has no Gaia neighbor individually bright enough to cause a 50-60 ppt blended loss.

**Catalogue status.** KNOWN_PUBLISHED_EB_ALERT; inspect prior row. The exact queue catalogue evidence is in `../../shared-catalogues/target-evidence.json`; a primary-table nonmatch alone would not establish novelty.

**Limits.** The bounded BLS does not settle nearby long-baseline integer aliases or establish a precision primary timing, so no orbital period or epoch is adopted. Gaia SB1 period 27.751345 d differs from the diagnostic raw clock, and the S39 measured deep event is +0.836 d from the nearest source-specific Gaia conjunction versus 0.189 d linear covariance. Local trapezoids hit bounds or are gap affected. QLP corrected flux suppresses the long eclipses; the TESSCut extraction uses the same photons. ASAS-SN ROT conflicts with the near-identical VSX ESD identification. Pixel centroid is offset by baseline/gap effects and is not precision localization.

**Next check.** Obtain an independent pipeline or follow-up eclipse timing and reconcile the Gaia SB1 phase; treat as a known VSX EB recovery.

**Evidence and reproduction.** The packet at `../../source-packets/324424395/sources.json` identifies and SHA256-verifies every source QLP FITS file. `lead-measurements.json` has actual quality-zero cadence coverage, source hashes and the raw local windows; `lead-event-panels.png`, `lead-alternative.json` and `lead-alternative.png` show raw and alternate QLP extraction of the same photons. The bounded scripts and shared source catalogue receipts are in the batch root. A predicted window is never treated as a fitted eclipse center.

- [lead-longperiod.json](lead-longperiod.json)
- [lead-coverage.json](lead-coverage.json)
- [helper-pixels.json](helper-pixels.json)
