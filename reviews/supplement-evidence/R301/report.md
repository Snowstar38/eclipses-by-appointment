# TIC 308986181: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 11 distinct eclipse events in selected sectors[9, 89, 100]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 same-kind midtimes give P=5.4022635217 +/-0.0000095649d, reference eclipse epoch BTJD1548.8549832, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S89 deficit peak[7, 8] vs target pixel[7, 7]; deficit-target separation3.686arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.246. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths32.580/32.803/31.486ppt, with 4 stacked events. QLP selected-kind fitted median31.450ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35659806507082067200, P=5.4023202539+/-0.0006108168d, e=0.039226, omega=160.9576deg. Closest edge-on conjunction offset-0.103122d (-0.019088phase), full-SB1-covariance linear propagated Gaia uncertainty0.138927d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.090925d (photometric period projection allowance0.002056d). The approximate central duration5.81h vs observed median4.85h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Eleven clear measured eclipses in three widely separated sectors. No capable neighbor under approximate Gaia flux-budget screen; target deficit0.176pixel from target.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 9 | 0 | 1548.8488599 | 0.010417 | 31.049 | usable; same-kind selection applies |
| 9 | 1 | 1554.2519120 | 0.010417 | 30.490 | usable; same-kind selection applies |
| 9 | 2 | 1559.6549102 | 0.010417 | 32.323 | usable; same-kind selection applies |
| 9 | 3 | 1565.0562199 | 0.010417 | 31.312 | usable; same-kind selection applies |
| 89 | 402 | 3720.5668740 | 0.001157 | 32.581 | usable; same-kind selection applies |
| 89 | 403 | 3725.9678623 | 0.001157 | 33.241 | usable; same-kind selection applies |
| 89 | 404 | 3731.3692487 | 0.001157 | 33.325 | usable; same-kind selection applies |
| 89 | 405 | 3736.7713877 | 0.001157 | 31.450 | usable; same-kind selection applies |
| 89 | 406 | 3742.1736932 | 0.001157 | 31.756 | usable; same-kind selection applies |
| 100 | 468 | 4077.1142603 | 0.001157 | 30.305 | usable; same-kind selection applies |
| 100 | 469 | 4082.5150569 | 0.001157 | 29.049 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s89.json, historical/diff_s89.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R301. [Deciding evidence](../../2026-10-31-magnitude60b/evidence/308986181) and [catalogue coverage](../../2026-10-31-magnitude60b/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
