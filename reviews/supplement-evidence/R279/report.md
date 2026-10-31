# TIC 123220126: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 12 distinct eclipse events in selected sectors[8, 62, 99]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=7.9647365731 ±0.0000076939d, reference eclipse epoch BTJD1519.0816018, kind: Deeper repeating eclipse; even half-period cycles. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S62 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.449arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.558. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths105.928/103.207/96.327ppt, with 6 stacked events. QLP selected-kind fitted median120.347ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR33824101617499474304, P=7.9648895117±0.0004901494d, e=0.017204, omega=144.7292deg. Closest edge-on conjunction offset-0.099881d (-0.012540phase), full-SB1-covariance linear propagated Gaia uncertainty0.050834d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.078164d (photometric period projection allowance0.001093d). The approximate central duration6.89h vs observed median4.58h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating eclipse depths establish doubled orbital period. Even historical half-period cycles alone define deeper-eclipse ephemeris; historical cutout stack mixes kinds.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 8 | 0 | 1519.0864143 | 0.010417 | 114.184 | usable; same-kind selection applies |
| 8 | 1 | 1523.0667550 | 0.010417 | 79.475 | usable; same-kind selection applies |
| 8 | 2 | 1527.0467454 | 0.010417 | 119.345 | usable; same-kind selection applies |
| 62 | 370 | 2992.5576999 | 0.001157 | 136.052 | usable; same-kind selection applies |
| 62 | 371 | 2996.5404004 | 0.001157 | 92.284 | usable; same-kind selection applies |
| 62 | 372 | 3000.5228394 | 0.001157 | 137.775 | usable; same-kind selection applies |
| 62 | 373 | 3004.5049693 | 0.001157 | 92.278 | usable; same-kind selection applies |
| 62 | 374 | 3008.4871198 | 0.001157 | 137.932 | usable; same-kind selection applies |
| 62 | 375 | 3012.4692650 | 0.001157 | 89.354 | usable; same-kind selection applies |
| 99 | 636 | 4051.8678251 | 0.001157 | 120.347 | usable; same-kind selection applies |
| 99 | 639 | 4063.8153617 | 0.001157 | 79.716 | usable; same-kind selection applies |
| 99 | 640 | 4067.7974018 | 0.001157 | 118.182 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s62.json, historical/diff_s62.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R279. [Deciding evidence](../../2026-10-31-magnitude60b/evidence/123220126) and [catalogue coverage](../../2026-10-31-magnitude60b/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
