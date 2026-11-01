# TIC 27732047: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX gives 23 timing-selected measured centers in sectors [15, 56, 83]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative raw morphology shows repeated eclipses.
2. **Timing and aliases.** Selected centers yield P = 5.1671309470 ± 0.0000052202 d and reference epoch BTJD 1730.6628793 (Deeper repeating eclipse; historical half-period parity 1). There are 7 within-sector same-kind adjacent pairs after the specified parity selection. The historical search branch is 2.58356477 d. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This conditional formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 56 TESScut difference image puts the deficit 3.97 arcsec from the target coordinate; peak [8, 8] versus target pixel [8, 8]. Image-model fractional residual 0.864 is not a localization error. Capable Gaia neighbors within 60 arcsec: Gaia 1893685410481942016 (54.40 arcsec, G 11.479, intrinsic required loss about 0.093); Gaia 1893686166394478208 (55.48 arcsec, G 14.610, intrinsic required loss about 0.655). Intrinsic required losses use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut target 1x1/3x3/5x5 apertures yield 86.89/67.21/37.77 ppt in 11 stacked historical events; representative QLP raw median selected depth is 123.94 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. aperture dilution and event choice limit direct depth comparison.
5. **Gaia geometry.** Matched DR3 source 1893685406185047936 has SB1 P = 5.1675861098 d and e = 0.01880. Closest edge-on conjunction offset is -0.09725 d (-0.01882 phase), with 0.07040 d linearly propagated full source-specific SB1 covariance. Rough central duration 6.54 h versus observed median fit 4.09 h assumes TIC radius and a minimum-mass main-sequence companion, not a complete binary model. Agreement does not prove source identity.

**Interpretation and limitation:** Deep and shallow eclipses alternate at the 2.58356-d photometric search period. The 5.16713-d orbital ephemeris uses the eleven deeper odd-parity centers; shallow even-parity eclipses independently support the double-period interpretation. Two nominally capable Gaia neighbors lie beyond 54 arcsec; the source image is structured, but its strongest deficit is on the target core.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 15 | 0 | 1712.5338395 | 0.010417 | 64.48 | used |
| 15 | 2 | 1717.7013600 | 0.010417 | 65.30 | used |
| 15 | 6 | 1728.0365599 | 0.010417 | 65.75 | used |
| 15 | 7 | 1730.6575933 | 0.010417 | 124.34 | used |
| 56 | 431 | 2826.0947577 | 0.001157 | 124.41 | used |
| 56 | 432 | 2828.6404641 | 0.001157 | 65.54 | used |
| 56 | 433 | 2831.2618576 | 0.001157 | 124.37 | used |
| 56 | 434 | 2833.8087977 | 0.001157 | 65.96 | used |
| 56 | 435 | 2836.4289748 | 0.001157 | 123.98 | used |
| 56 | 436 | 2838.9748702 | 0.001157 | 64.57 | used |
| 56 | 437 | 2841.5959721 | 0.001157 | 125.20 | used |
| 56 | 438 | 2844.1422710 | 0.001157 | 64.04 | used |
| 56 | 439 | 2846.7629037 | 0.001157 | 123.38 | used |
| 56 | 440 | 2849.3094867 | 0.001157 | 65.32 | used |
| 56 | 441 | 2851.9304934 | 0.001157 | 123.68 | used |
| 83 | 715 | 3559.8273915 | 0.001157 | 123.43 | used |
| 83 | 716 | 3562.3739161 | 0.001157 | 64.78 | used |
| 83 | 718 | 3567.5412835 | 0.001157 | 65.52 | used |
| 83 | 719 | 3570.1615750 | 0.001157 | 123.76 | used |
| 83 | 720 | 3572.7081264 | 0.001157 | 65.19 | used |
| 83 | 721 | 3575.3285814 | 0.001157 | 123.94 | used |
| 83 | 723 | 3580.4954790 | 0.001157 | 122.52 | used |
| 83 | 724 | 3583.0421157 | 0.001157 | 66.03 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s56.json, historical/diff_s56.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R451. Public evidence files: [diff_s56.json](../../evidence/27732047/historical/diff_s56.json), [diff_s56.png](../../evidence/27732047/historical/diff_s56.png), [gaia.json](../../evidence/27732047/historical/gaia.json), [measurements.json](../../evidence/27732047/measurements.json), [raw-events.png](../../evidence/27732047/raw-events.png), [raw-windows.csv](../../evidence/27732047/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch05/INDEX.md). 
