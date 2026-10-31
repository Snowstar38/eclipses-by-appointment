# TIC 207148517: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[69, 97]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=7.7713883517 +/-0.0000320555d, reference eclipse epoch BTJD3187.7124533, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S97 deficit peak[8, 8] vs target pixel[7, 8]; deficit-target separation2.732arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual1.000. Capable neighbours: Gaia 4728689624881108864: 40.99 arcsec, G17.789, required fractional eclipse0.736
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths2.980/3.417/3.404ppt, with 8 stacked events. QLP selected-kind fitted median3.405ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR34728686635582532352, P=7.7705559611+/-0.0010075925d, e=0.050853, omega=206.9657deg. Closest edge-on conjunction offset0.315934d (0.040658phase), full-SB1-covariance linear propagated Gaia uncertainty0.422468d at the measured epoch. Near-Gaia-reference projected eclipse offset0.016274d (photometric period projection allowance0.011540d). The approximate central duration5.68h vs observed median1.86h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Shallow repeat signal is measured in sectors69/97; individual fits vary and broad sector69 cycle236 is baseline-sensitive. Median depth is diluted. Historical PSF-scaled residual0.9997 is poor because bright off-center source dominates wide fit; local deficit core0.130pixel from target versus capable neighbor1.84pixels away supports target. Neighbor intrinsic requirement0.736 is not compared directly with its blended pixel fractional loss. Precision timing/shape is limited by low signal and baseline model.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 69 | 235 | 3187.7226688 | 0.002686 | 2.930 | usable; same-kind selection applies |
| 69 | 236 | 3195.4886084 | 0.004264 | 5.930 | usable; same-kind selection applies |
| 69 | 237 | 3203.2529147 | 0.001157 | 3.334 | usable; same-kind selection applies |
| 97 | 332 | 3941.5374232 | 0.001836 | 5.363 | usable; same-kind selection applies |
| 97 | 334 | 3957.0855244 | 0.002183 | 3.195 | usable; same-kind selection applies |
| 97 | 335 | 3964.8475080 | 0.001907 | 3.537 | usable; same-kind selection applies |
| 97 | 336 | 3972.6218020 | 0.003256 | 3.247 | usable; same-kind selection applies |
| 97 | 338 | 3988.1650616 | 0.002008 | 3.476 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s97.json, historical/diff_s97.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R306. [Deciding evidence](../../2026-10-31-magnitude60b/evidence/207148517) and [catalogue coverage](../../2026-10-31-magnitude60b/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
