# TIC 421951253: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 11 distinct eclipse events in selected sectors[1, 68, 95]. The representative raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 same-kind midtimes give P=5.1102857278 +/-0.0000053139d, reference eclipse epoch BTJD1327.5694426, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S28 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation2.504arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.101. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths43.861/43.412/43.001ppt, with 4 stacked events. QLP selected-kind fitted median42.001ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36819963794630918784, P=5.1105848877+/-0.0003627777d, e=0.081883, omega=85.1163deg. Closest edge-on conjunction offset-0.052807d (-0.010333phase), full-SB1-covariance linear propagated Gaia uncertainty0.073267d at the measured epoch. Near-Gaia-reference projected eclipse offset0.002239d (photometric period projection allowance0.000978d). The approximate central duration5.61h vs observed median4.43h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated isolated eclipses across widely separated sectors; no capable listed neighbor. Diluted fitted depths vary by sector aperture.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 1 | 0 | 1327.5687926 | 0.010417 | 42.001 | used in ephemeris |
| 1 | 1 | 1332.6798393 | 0.010417 | 43.810 | used in ephemeris |
| 1 | 3 | 1342.9011012 | 0.010417 | 41.749 | used in ephemeris |
| 68 | 358 | 3157.0511831 | 0.001157 | 43.389 | used in ephemeris |
| 68 | 359 | 3162.1620065 | 0.001157 | 43.939 | used in ephemeris |
| 68 | 361 | 3172.3824542 | 0.001157 | 43.371 | used in ephemeris |
| 68 | 362 | 3177.4935875 | 0.001157 | 43.353 | used in ephemeris |
| 95 | 501 | 3887.8224600 | 0.001157 | 39.253 | used in ephemeris |
| 95 | 502 | 3892.9327738 | 0.001157 | 38.989 | used in ephemeris |
| 95 | 503 | 3898.0427180 | 0.001157 | 37.906 | used in ephemeris |
| 95 | 504 | 3903.1541154 | 0.001157 | 38.400 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s28.json, historical/diff_s28.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R381. [Deciding evidence](../../evidence/421951253/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/421951253/measurements.json), [raw eclipse plots](../../evidence/421951253/raw-events.png), [raw flux windows](../../evidence/421951253/raw-windows.csv), [Gaia geometry](../../analysis/batch05/gaia-geometry.json), [independent audit](../../analysis/batch05/helper-audit.md), [difference image](../../evidence/421951253/historical/diff_s28.png).
