# TIC 113810700: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 22 distinct eclipse events in selected sectors[42, 44, 71]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 22 same-kind midtimes give P=2.7284265924 ±0.0000036417d, reference eclipse epoch BTJD2449.5539561, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S70 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.046arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.433. Capable neighbours: Gaia 60689300937937920: 57.10 arcsec, G15.397, required fractional eclipse0.924
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths33.426/33.144/31.944ppt, with 8 stacked predicted windows. QLP selected-kind fitted median34.363ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR360689193562928512, P=2.7284185865±0.0001165221d, e=0.057487, omega=53.9806deg. Closest edge-on conjunction offset0.028502d (0.010446phase), full-SB1-covariance linear propagated Gaia uncertainty0.094242d at the measured epoch. Near-Gaia-reference projected eclipse offset0.022458d (photometric period projection allowance0.002749d). The approximate central duration4.70h vs observed median4.23h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Representative raw eclipses recur. Depths remain diluted and sector dependent; timing errors omit uncalibrated extraction and shape systematics.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 42 | 0 | 2449.5536236 | 0.003473 | 34.496 | included timing center |
| 42 | 1 | 2452.2824437 | 0.003473 | 34.302 | included timing center |
| 42 | 2 | 2455.0107777 | 0.003473 | 34.087 | included timing center |
| 42 | 5 | 2463.1974482 | 0.003473 | 35.917 | included timing center |
| 42 | 6 | 2465.9249403 | 0.003473 | 34.578 | included timing center |
| 42 | 7 | 2468.6527539 | 0.003473 | 34.284 | included timing center |
| 42 | 8 | 2471.3816855 | 0.003473 | 34.125 | included timing center |
| 44 | 19 | 2501.3941823 | 0.003472 | 34.279 | included timing center |
| 44 | 21 | 2506.8503510 | 0.003472 | 35.140 | included timing center |
| 44 | 22 | 2509.5784516 | 0.003472 | 34.790 | included timing center |
| 44 | 24 | 2515.0357068 | 0.003472 | 35.584 | included timing center |
| 44 | 25 | 2517.7642280 | 0.003472 | 34.788 | included timing center |
| 44 | 26 | 2520.4939123 | 0.003472 | 35.210 | included timing center |
| 44 | 27 | 2523.2212149 | 0.003472 | 34.318 | included timing center |
| 71 | 288 | 3235.3398853 | 0.001157 | 34.354 | included timing center |
| 71 | 289 | 3238.0697129 | 0.001157 | 34.204 | included timing center |
| 71 | 290 | 3240.7970380 | 0.001157 | 34.023 | included timing center |
| 71 | 291 | 3243.5265239 | 0.001157 | 34.373 | included timing center |
| 71 | 293 | 3248.9838239 | 0.001157 | 33.364 | included timing center |
| 71 | 294 | 3251.7112147 | 0.001157 | 34.349 | included timing center |
| 71 | 295 | 3254.4404550 | 0.001157 | 34.376 | included timing center |
| 71 | 296 | 3257.1675145 | 0.001157 | 34.595 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s70.json, historical/diff_s70.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R375. [Deciding evidence](../../2026-10-31-bright73/evidence/113810700) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/113810700/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/113810700/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/113810700/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch04/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch04/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/113810700/historical/diff_s70.png).
