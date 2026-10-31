# TIC 267094867: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 13 distinct eclipse events in selected sectors[1, 67, 96]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 12 same-kind midtimes give P=3.4708302926 ±0.0000031344d, reference eclipse epoch BTJD1345.8329151, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Unreliable fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S66 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation1.558arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.036. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths67.600/68.139/67.682ppt, with 8 stacked events. Historical event coordinates guide these stacks and are not newly measured midtimes. QLP selected-kind fitted median65.115ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR34639899319293628160, P=3.4710058980±0.0001561795d, e=0.015578, omega=37.0096deg. Closest edge-on conjunction offset-0.037602d (-0.010833phase), full-SB1-covariance linear propagated Gaia uncertainty0.038192d at the measured epoch. Near-Gaia-reference projected eclipse offset0.010865d (photometric period projection allowance0.000865d). The approximate central duration6.12h vs observed median4.02h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep eclipses recur in sectors1/67/96; sector-dependent depths and shapes retained. Singular sector67 cycle520 fit excluded from timing. No capable catalogued neighbor in approximate brightness test.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 1 | 5 | 1345.8342689 | 0.010417 | 65.545 | usable; same-kind selection applies |
| 1 | 7 | 1352.7735477 | 0.010417 | 64.684 | usable; same-kind selection applies |
| 67 | 519 | 3129.8395208 | 0.001157 | 75.267 | usable; same-kind selection applies |
| 67 | 520 | 3133.3214697 | 118740.580542 | 65.654 | excluded unreliable timing fit |
| 67 | 521 | 3136.7811360 | 0.001157 | 75.230 | usable; same-kind selection applies |
| 67 | 523 | 3143.7229409 | 0.001157 | 75.953 | usable; same-kind selection applies |
| 67 | 524 | 3147.1941038 | 0.001157 | 75.635 | usable; same-kind selection applies |
| 67 | 525 | 3150.6648322 | 0.001157 | 79.582 | usable; same-kind selection applies |
| 96 | 744 | 3910.7766784 | 0.001157 | 62.725 | usable; same-kind selection applies |
| 96 | 746 | 3917.7180340 | 0.001157 | 63.889 | usable; same-kind selection applies |
| 96 | 748 | 3924.6597605 | 0.001157 | 62.610 | usable; same-kind selection applies |
| 96 | 749 | 3928.1308625 | 0.001157 | 62.576 | usable; same-kind selection applies |
| 96 | 750 | 3931.6012908 | 0.001157 | 63.284 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s66.json, historical/diff_s66.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R290. [Deciding evidence](../../evidence/267094867/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
