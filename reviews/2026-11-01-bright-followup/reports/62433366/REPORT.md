# TIC 62433366: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate. This report reviews the frozen batch04 target; historical screening is not an admission verdict.

1. **Raw events.** Quality-zero QLP SAP_FLUX shows 12 timing-selected measured eclipses in sectors [15, 76, 84]. Local trapezoid fits allow free centers and baseline. Predicted windows are search guides only; flagged or sparsely sampled windows are not null detections. Numeric windows and the raw plot retain the evidence.
2. **Timing and aliases.** Measured same-kind centers give P=4.7597184350 d, fit error=0.0000117166 d, epoch BTJD 1717.6797337 (Deeper repeating eclipse; historical half-period parity 0). There are 6 consecutive within-sector same-kind cycle pairs. The inventory period was 4.75970 d and the historical SAP search branch was 2.3798505904 d. Deeper parity 0 of historical half-period cycles; consecutive same-kind events have orbital-cycle count one. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The fit error is not calibrated total uncertainty. This bounded alias check is not an exhaustive blind period search.
3. **Pixel attribution: favors target at TESS resolution.** Historical S56 TESScut deficit core is 1.91 arcsec from the target coordinate; peak pixel [7, 8] and target pixel [7, 8]. Fractional PSF model residual is 0.405, not a localization uncertainty. Capable Gaia neighbors: 51.0 arcsec, G=14.00, intrinsic-loss requirement ~0.23. The full list and flux-budget calculation are in historical/diff_s56.json; the original cutout and stacked image are retained and hashed.
4. **Alternative reduction.** A target-centered, background-subtracted TESScut extraction gives 1x1/3x3/5x5 stacked depths 35.29/34.01/29.65 ppt from 10 selected windows. Median selected QLP raw fit depth is 40.07 ppt. Aperture dilution, event-kind mixing and model residuals limit direct depth comparisons. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument.
5. **Gaia orbit.** The matched DR3 NSS source 2175713785143071360 has P=4.7596067442 d and e=0.01266. Closest edge-on conjunction differs from the measured epoch by 0.01077 in phase (0.05124 d); linear propagation of the source-specific full SB1 covariance gives 0.05299 d as a descriptive timing scale. The rough central-duration estimate is 13.51 h versus trapezoid median 6.17 h; these assume a TIC radius and minimum-mass main-sequence companion and are not a full geometry fit or a sigma gate.

**Deciding interpretation and limitation.** Even historical half-period cycles are modestly but persistently deeper than odd cycles in S76 and S84, supporting the 4.7597 d orbital period. The duration is only a rough trapezoid shape measure.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is evaluated centrally against seven scoped groups in ../../shared-catalogues/coverage-matrix.csv. This physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 15 | 0 | 1717.6831262 | 0.010417 | 40.18 | used |
| 15 | 4 | 1727.1993403 | 0.010417 | 38.05 | used |
| 15 | 5 | 1729.5828742 | 0.010417 | 35.04 | other eclipse kind |
| 15 | 6 | 1731.9623506 | 0.010417 | 38.58 | used |
| 76 | 694 | 3369.3007811 | 0.001157 | 39.46 | used |
| 76 | 695 | 3371.6818953 | 0.001157 | 36.40 | other eclipse kind |
| 76 | 696 | 3374.0525045 | 69105.867428 | 39.51 | excluded: unidentifiable center covariance |
| 76 | 697 | 3376.4414970 | 0.001157 | 36.42 | other eclipse kind |
| 76 | 698 | 3378.8210860 | 0.001157 | 41.23 | used |
| 76 | 699 | 3381.2015616 | 0.001183 | 36.31 | other eclipse kind |
| 76 | 700 | 3383.5818120 | 0.001157 | 40.94 | used |
| 76 | 701 | 3385.9613345 | 0.001157 | 37.25 | other eclipse kind |
| 76 | 702 | 3388.3405430 | 74615.274606 | 41.44 | excluded: unidentifiable center covariance |
| 76 | 703 | 3390.7214454 | 0.001157 | 37.46 | other eclipse kind |
| 76 | 704 | 3393.1009750 | 0.001157 | 41.70 | used |
| 84 | 785 | 3585.8702706 | 0.001157 | 38.12 | other eclipse kind |
| 84 | 786 | 3588.2496231 | 0.001157 | 40.09 | used |
| 84 | 787 | 3590.6295307 | 0.001157 | 36.54 | other eclipse kind |
| 84 | 788 | 3593.0082983 | 0.001157 | 40.05 | used |
| 84 | 789 | 3595.3870047 | 0.001157 | 35.52 | other eclipse kind |
| 84 | 790 | 3597.7685395 | 0.001157 | 38.21 | used |
| 84 | 791 | 3600.1486071 | 0.001157 | 35.99 | other eclipse kind |
| 84 | 792 | 3602.5287240 | 0.001157 | 39.26 | used |
| 84 | 793 | 3604.9075849 | 0.001157 | 37.18 | other eclipse kind |
| 84 | 794 | 3607.2879584 | 0.001157 | 41.04 | used |
| 84 | 795 | 3609.6676856 | 0.001157 | 35.34 | other eclipse kind |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s56.json, historical/diff_s56.png, historical/gaia.json, original TESScut [local path omitted] and ../helper-audit.md. The original cutout and source files are SHA-256 recorded in ../source-hashes.json and ../SHA256SUMS.json.


Stable review key: R445. Public evidence files: [diff_s56.json](../../evidence/62433366/historical/diff_s56.json), [diff_s56.png](../../evidence/62433366/historical/diff_s56.png), [gaia.json](../../evidence/62433366/historical/gaia.json), [measurements.json](../../evidence/62433366/measurements.json), [raw-events.png](../../evidence/62433366/raw-events.png), [raw-windows.csv](../../evidence/62433366/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch04/INDEX.md). 
