# TIC 276277940: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 9 distinct eclipse events in selected sectors[15, 76, 83]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=6.8645586129 +/-0.0000230538d, reference eclipse epoch BTJD1717.7413603, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S55 deficit peak[7, 8] vs target pixel[7, 7]; deficit-target separation4.635arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.931. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths109.693/109.506/90.147ppt, with 4 stacked events. QLP selected-kind fitted median150.628ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32163384274080095616, P=6.8634769946+/-0.0015596212d, e=0.171838, omega=314.6172deg. Closest edge-on conjunction offset0.141873d (0.020671phase), full-SB1-covariance linear propagated Gaia uncertainty0.270100d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.067961d (photometric period projection allowance0.004472d). The approximate central duration6.68h vs observed median4.75h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep raw eclipses recur across three sectors, with sector-dependent depths130-160ppt. Sector83 cycle271 singular center covariance is excluded from timing. Historical cutout1/3/5 depths109.7/109.5/90.1ppt show aperture dilution; no capable catalogued neighbor under approximate brightness screen.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 15 | 0 | 1717.7455895 | 0.010417 | 136.535 | usable; same-kind selection applies |
| 15 | 2 | 1731.4750235 | 0.010417 | 130.121 | usable; same-kind selection applies |
| 76 | 241 | 3372.1000060 | 0.001157 | 146.002 | usable; same-kind selection applies |
| 76 | 242 | 3378.9657159 | 0.001157 | 147.832 | usable; same-kind selection applies |
| 76 | 243 | 3385.8274449 | 0.001157 | 160.030 | usable; same-kind selection applies |
| 76 | 244 | 3392.6929583 | 0.001157 | 156.758 | usable; same-kind selection applies |
| 83 | 269 | 3564.3081827 | 0.001157 | 153.424 | usable; same-kind selection applies |
| 83 | 270 | 3571.1726924 | 0.001157 | 155.728 | usable; same-kind selection applies |
| 83 | 271 | 3578.0460711 | 194277.187178 | 145.755 | excluded singular timing fit |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s55.json, historical/diff_s55.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R304. [Deciding evidence](../../evidence/276277940/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
