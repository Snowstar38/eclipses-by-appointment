# TIC 341118777: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[13, 101, 104]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=6.8474689646 +/-0.0000169388d, reference eclipse epoch BTJD1665.0429604, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S67 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation0.609arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.056. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths112.012/112.820/109.723ppt, with 4 stacked events. QLP selected-kind fitted median95.174ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36454272480705278848, P=6.8477864674+/-0.0007556392d, e=0.070259, omega=102.3940deg. Closest edge-on conjunction offset0.013863d (0.002024phase), full-SB1-covariance linear propagated Gaia uncertainty0.171384d at the measured epoch. Near-Gaia-reference projected eclipse offset0.072919d (photometric period projection allowance0.003151d). The approximate central duration4.74h vs observed median3.81h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep repeated events in sectors13/101. Sector104 cycle371 singular center covariance is excluded from timing; its real partial/noisy morphology is retained as documentation. No capable neighbor under approximate flux-budget screen.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 13 | 1 | 1665.0455748 | 0.010417 | 105.879 | usable; same-kind selection applies |
| 13 | 2 | 1671.8894812 | 0.010417 | 102.644 | usable; same-kind selection applies |
| 13 | 3 | 1678.7357199 | 0.010417 | 101.600 | usable; same-kind selection applies |
| 101 | 357 | 4102.7425263 | 0.001157 | 95.174 | usable; same-kind selection applies |
| 101 | 358 | 4109.5896726 | 0.001157 | 94.603 | usable; same-kind selection applies |
| 101 | 359 | 4116.4366276 | 0.001157 | 94.736 | usable; same-kind selection applies |
| 101 | 360 | 4123.2836410 | 0.001157 | 95.114 | usable; same-kind selection applies |
| 104 | 371 | 4198.5971566 | 41218.230390 | 99.299 | excluded singular timing fit |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s67.json, historical/diff_s67.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R299. [Deciding evidence](../../evidence/341118777/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
