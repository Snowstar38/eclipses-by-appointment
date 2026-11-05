# F030 TIC 288649491: REFUTED

**Completion:** COMPLETE bounded review. **Selection:** repeat_sector_dip; Gaia DR3 3027262760354865408 (SB 33.586308275319595 d).

**Physical assessment.** The deep 0.540073-d repeated dip matches the published 0.540070-d VSX eclipsing neighbor Gaia DR3 3027262794714599424 at 13.85 arcsec, rather than the target Gaia SB1 33.5863-d orbit. The neighbor G14.15 versus target G10.84 supplies an approximate 4.7 percent flux ratio, sufficient for the observed 2-3 percent blended dips. Sector-34 TESSCut WCS places the target and VSX star at distinct positions; the difference image and shifted empirical PSF favor the VSX side. The raw dip clock appears in 114 fully covered quality-zero predicted cores.

**Catalogue status.** SCOPED_NONMATCH; no target EB identification in checked tables. The exact queue catalogue evidence is in `../../shared-catalogues/target-evidence.json`; a primary-table nonmatch alone would not establish novelty.

**Limits.** Pixel deblending is approximate, but exact period identity, capable neighbor flux and the spatial difference jointly support off-target ownership. This refutes a target eclipse claim from these dips, not the independent Gaia SB1 orbit. The target-scoped catalogue status remains scoped nonmatch; the nearby EB is known.

**Next check.** Use resolved aperture or high-resolution photometry if target eclipse status must be tested independently.

**Evidence and reproduction.** The packet at `../../source-packets/288649491/sources.json` identifies and SHA256-verifies every source QLP FITS file. `lead-measurements.json` has actual quality-zero cadence coverage, source hashes and the raw local windows; `lead-event-panels.png`, `lead-alternative.json` and `lead-alternative.png` show raw and alternate QLP extraction of the same photons. The bounded scripts and shared source catalogue receipts are in the batch root. A predicted window is never treated as a fitted eclipse center.

- [lead-shortperiod.json](lead-shortperiod.json)
- [lead-coverage.json](lead-coverage.json)
- [helper-pixels.json](helper-pixels.json)
