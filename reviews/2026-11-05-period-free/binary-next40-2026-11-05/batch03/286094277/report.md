# F023 TIC 286094277: CONFIRMED

**Completion:** COMPLETE bounded review. **Selection:** repeat_sector_dip; Gaia DR3 2167586710592820096 (SB 27.388301314923662 d).

**Physical assessment.** Eight non-singular same-kind raw SAP dips in S16, S41, S55, S56, S75, S76, S82 and S83 fit 27.371657 d with about 0.001 d timing residuals; consecutive sector pairs fix the integer cycles. Eight of nine predicted quality-zero cores are fully covered with bilateral baselines and show 10.1-11.1 ppt loss. Eight covered half-cycle and thirteen covered third-cycle extra-phase windows have no comparable dip (maximum 0.27 ppt), rejecting those short same-kind aliases. QLP corrected flux preserves the first three checked dips. Sector-16 TESSCut difference is 0.345 pixel from the target WCS position, with valid positive target flux and sky; the capable G15.06 neighbor at 27.83 arcsec is on the opposite side, 1.8 pixels from the deficit. The source-specific Gaia SB1 conjunction offset is -0.845 d against 0.929 d linear covariance early and -1.960 d against 2.207 d late; its period differs by 0.01664 d against a 0.01980 d Gaia error.

**Catalogue status.** KNOWN_PUBLISHED_EB_ALERT; inspect prior row. The exact queue catalogue evidence is in `../../shared-catalogues/target-evidence.json`; a primary-table nonmatch alone would not establish novelty.

**Limits.** Period precision is bounded by sector-dependent raw timing model systematics; no formal period error is adopted. Half/third phase nulls do not exclude a shallow secondary kind. TESSCut is the same TESS photons. This is the already published Tarrants-Mendes TOI-5149 exact-Gaia EB row, not a new discovery.

**Next check.** Use independent ground-based timing only if a refined ephemeris is needed.

**Evidence and reproduction.** The packet at `../../source-packets/286094277/sources.json` identifies and SHA256-verifies every source QLP FITS file. `lead-measurements.json` has actual quality-zero cadence coverage, source hashes and the raw local windows; `lead-event-panels.png`, `lead-alternative.json` and `lead-alternative.png` show raw and alternate QLP extraction of the same photons. The bounded scripts and shared source catalogue receipts are in the batch root. A predicted window is never treated as a fitted eclipse center.

- [lead-longperiod.json](lead-longperiod.json)
- [lead-alias.json](lead-alias.json)
- [lead-coverage.json](lead-coverage.json)
- [lead-pixels.json](lead-pixels.json)
- [lead-null-windows.png](lead-null-windows.png)
