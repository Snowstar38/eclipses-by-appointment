# TIC 439808137: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 10 distinct eclipse events in selected sectors[42, 82, 92]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 10 same-kind midtimes give P=6.4350026636 ±0.0000108672d, reference eclipse epoch BTJD2448.1647207, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S82 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation3.089arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.286. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths102.553/100.621/93.986ppt, with 4 stacked predicted windows. QLP selected-kind fitted median105.158ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32676240237202012544, P=6.4354242696±0.0006605117d, e=0.023885, omega=293.9222deg. Closest edge-on conjunction offset-0.099754d (-0.015501phase), full-SB1-covariance linear propagated Gaia uncertainty0.226322d at the measured epoch. Near-Gaia-reference projected eclipse offset0.035159d (photometric period projection allowance0.003477d). The approximate central duration5.54h vs observed median4.53h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Representative raw eclipses recur. Depths remain diluted and sector dependent; timing errors omit uncalibrated extraction and shape systematics.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 42 | -1 | 2448.1647697 | 0.003472 | 110.994 | included timing center |
| 42 | 2 | 2467.4695528 | 0.003472 | 106.059 | included timing center |
| 82 | 168 | 3535.6802741 | 0.001157 | 106.751 | included timing center |
| 82 | 169 | 3542.1151315 | 0.001157 | 106.351 | included timing center |
| 82 | 170 | 3548.5501821 | 0.001157 | 105.859 | included timing center |
| 82 | 171 | 3554.9851673 | 0.001157 | 104.457 | included timing center |
| 92 | 210 | 3805.9503635 | 0.001158 | 99.183 | included timing center |
| 92 | 211 | 3812.3852699 | 0.001158 | 100.160 | included timing center |
| 92 | 212 | 3818.8204620 | 0.001158 | 101.345 | included timing center |
| 92 | 213 | 3825.2550097 | 0.001158 | 101.630 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s82.json, historical/diff_s82.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R367. [Deciding evidence](../../2026-10-31-bright73/evidence/439808137) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/439808137/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/439808137/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/439808137/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch04/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch04/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/439808137/historical/diff_s82.png).
