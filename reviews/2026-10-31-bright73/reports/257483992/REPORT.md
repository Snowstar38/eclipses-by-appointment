# TIC 257483992: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[3, 30, 97]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=8.7868298591 ±0.0000112166d, reference eclipse epoch BTJD1392.1739129, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S97 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation1.034arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.084. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths21.166/21.235/20.570ppt, with 4 stacked events. QLP selected-kind fitted median18.882ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35147695536082116352, P=8.7875714993±0.0016554215d, e=0.153182, omega=203.5610deg. Closest edge-on conjunction offset-0.112963d (-0.012855phase), full-SB1-covariance linear propagated Gaia uncertainty0.222418d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.028416d (photometric period projection allowance0.001279d). The approximate central duration7.97h vs observed median6.42h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Representative raw eclipses recur. Depths remain diluted and sector dependent; timing errors omit uncalibrated extraction and shape systematics.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 3 | 0 | 1392.1752764 | 0.014321 | 20.715 | included timing center |
| 3 | 1 | 1400.9615218 | 0.010417 | 20.032 | included timing center |
| 30 | 83 | 2121.4811951 | 0.003472 | 19.700 | included timing center |
| 30 | 85 | 2139.0538306 | 0.003472 | 21.420 | included timing center |
| 97 | 290 | 3940.3538705 | 0.001157 | 17.503 | included timing center |
| 97 | 292 | 3957.9294558 | 0.001157 | 17.092 | included timing center |
| 97 | 293 | 3966.7147318 | 0.001157 | 18.065 | included timing center |
| 97 | 295 | 3984.2885342 | 0.001157 | 17.907 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s97.json, historical/diff_s97.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R355. [Deciding evidence](../../evidence/257483992/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/257483992/measurements.json), [raw eclipse plots](../../evidence/257483992/raw-events.png), [raw flux windows](../../evidence/257483992/raw-windows.csv), [Gaia geometry](../../analysis/batch02/gaia-geometry.json), [independent audit](../../analysis/batch02/helper-audit.md), [difference image](../../evidence/257483992/historical/diff_s97.png).
