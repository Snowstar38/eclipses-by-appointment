# TIC 120029059: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[25, 78, 79]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=3.9188796724 ±0.0000270796d, reference eclipse epoch BTJD1992.7941562, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S79 deficit peak[7, 8] vs target pixel[8, 8]; deficit-target separation5.909arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.423. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths104.749/101.439/94.107ppt, with 4 stacked predicted windows. QLP selected-kind fitted median109.639ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR34465737394712806272, P=3.9191167014±0.0001278734d, e=0.168077, omega=296.8544deg. Closest edge-on conjunction offset-0.078894d (-0.020131phase), full-SB1-covariance linear propagated Gaia uncertainty0.061003d at the measured epoch. Near-Gaia-reference projected eclipse offset0.018051d (photometric period projection allowance0.011076d). The approximate central duration4.63h vs observed median3.53h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Representative raw eclipses recur. Depths remain diluted and sector dependent; timing errors omit uncalibrated extraction and shape systematics.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 25 | 2 | 1992.7939376 | 0.010417 | 110.015 | included timing center |
| 78 | 370 | 3434.9419823 | 0.001157 | 109.263 | included timing center |
| 78 | 371 | 3438.8604468 | 0.001157 | 108.254 | included timing center |
| 78 | 372 | 3442.7797493 | 0.001157 | 109.075 | included timing center |
| 79 | 375 | 3454.5366244 | 0.001157 | 110.526 | included timing center |
| 79 | 378 | 3466.2929153 | 0.001157 | 110.442 | included timing center |
| 79 | 379 | 3470.2116903 | 0.001157 | 111.699 | included timing center |
| 79 | 381 | 3478.0493918 | 0.001157 | 108.978 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s79.json, historical/diff_s79.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R376. [Deciding evidence](../../evidence/120029059/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/120029059/measurements.json), [raw eclipse plots](../../evidence/120029059/raw-events.png), [raw flux windows](../../evidence/120029059/raw-windows.csv), [Gaia geometry](../../analysis/batch04/gaia-geometry.json), [independent audit](../../analysis/batch04/helper-audit.md), [difference image](../../evidence/120029059/historical/diff_s79.png).
