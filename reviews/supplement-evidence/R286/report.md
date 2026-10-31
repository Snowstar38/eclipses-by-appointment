# TIC 365864542: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 6 distinct eclipse events in selected sectors[15, 75, 83]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=13.3838603016 ±0.0000467881d, reference eclipse epoch BTJD1717.1172335, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S15 deficit peak[7, 8] vs target pixel[8, 8]; deficit-target separation2.180arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.482. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths257.577/247.957/195.923ppt, with 2 stacked events. QLP selected-kind fitted median277.197ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32168065960222645632, P=13.3807392140±0.0042403250d, e=0.382153, omega=217.8118deg. Closest edge-on conjunction offset0.192270d (0.014369phase), full-SB1-covariance linear propagated Gaia uncertainty0.445137d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.116718d (photometric period projection allowance0.004632d). The approximate central duration13.08h vs observed median9.73h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep repeated isolated eclipses across three sectors; one singular center-covariance fit excluded. Aperture/sector depth differences retained; no intrinsic undiluted depth inferred.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 15 | 0 | 1717.1157569 | 0.010417 | 272.104 | usable; same-kind selection applies |
| 15 | 1 | 1730.5001172 | 0.010417 | 274.416 | usable; same-kind selection applies |
| 75 | 122 | 3349.9484463 | 0.001157 | 277.197 | usable; same-kind selection applies |
| 75 | 123 | 3363.3410291 | 45629.070605 | 278.227 | excluded singular timing fit |
| 83 | 138 | 3564.0897989 | 0.001157 | 284.372 | usable; same-kind selection applies |
| 83 | 139 | 3577.4737458 | 0.001157 | 283.622 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s15.json, historical/diff_s15.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R286. [Deciding evidence](../../2026-10-31-magnitude60b/evidence/365864542) and [catalogue coverage](../../2026-10-31-magnitude60b/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
