# T042 / TIC 255912894: PROBABLE

Gaia DR3 5811265337623194752; queue stratum cross_method_dip; Gaia selection P=47.35116416322056 d. This is sample position T042, not a physical rank.

## Bounded physical finding

Four narrow same-kind raw SAP dips: S13 1678.65847, S66 3100.27375, S100 4095.40239, S102 4142.78887 BTJD. S66 and S102 were unflagged by the period-free detector. Cycles 0/30/51/52 give P=47.387088 d; residuals are below 0.0023 d. Actual covered nulls reject representative nearby cycle aliases; half-phase S93 and S101 have 69 and 58 core cadences spanning +/-0.078 d and only 0.12 and -0.01 ppt against ~4-ppt events. Independent S66 TESSCut target-centered 3x3 raw loss is 3.51 ppt; side-minus-core pixels peak in the target vicinity. The nearest Gaia edge-on conjunction offset is 2.628 d / 1.425 d linear covariance sigma = 1.84 sigma.

The source packet SHA-256 is `2d5c256422c4e6b1bab1623b2f0e5944d2e7ee43f973db2adfb07e817e8d40c6`. `lead-numeric.json` records SHA-256 of each used QLP FITS, raw quality-zero sector endpoints, cadence, largest internal gaps and representative screen-seed fits. The detector times and fold predictions are not assumed to be measured eclipse centers. `lead-fold-windows.json` records actual cadence coverage at the independently selected fold-screen period. The raw and pixel figures show deciding context. Source packet and FITS hashes were verified before measurement.

## Limits and next check

Capable close Gaia G=14.43 and G=16.19 neighbors are not spatially resolved from the target; source attribution remains uncertain. QLP and TESSCut use the same TESS photons. The four-center formal period error is 0.000130 d; the reported 0.0005 d is a conservative allowance for event shape and pipeline timing, not a calibrated uncertainty.

Next: Resolve the blended source with higher-resolution time-series photometry or a reliable pixel localization.

Physical review completion: COMPLETE (bounded review of the selected claim). Catalogue novelty: UNKNOWN; shared seven-group work left VSX, ASAS-SN and Kostov 2025 tables 3/4 unqueried after failed positive controls. No new-system count follows from this physical verdict.

Supporting local artifacts: `lead-numeric.json`, `lead-fold-windows.json`, `lead-raw-01.png`, `lead-alias.json`, `lead-clock.json`, `lead-third.png`, `lead-fourth.png`, `lead-halfphase.json`. Shared catalogue receipts: `../../shared-catalogues/TARGET-STATUS.csv` and `../../shared-catalogues/gaia-neighbors.json`. Helper independent findings: `../helper-audit.md`.
