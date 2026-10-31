# TIC 280881615: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 6 distinct eclipse events in selected sectors[59, 86]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=5.2631068082 ±0.0000072351d, reference eclipse epoch BTJD2912.9426599, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S53 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation2.424arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.210. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths133.539/131.270/126.773ppt, with 5 stacked events. QLP selected-kind fitted median139.117ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3500313662204983936, P=5.2629890551±0.0002254657d, e=0.010989, omega=299.7018deg. Closest edge-on conjunction offset0.087594d (0.016643phase), full-SB1-covariance linear propagated Gaia uncertainty0.099605d at the measured epoch. Near-Gaia-reference projected eclipse offset0.031073d (photometric period projection allowance0.003473d). The approximate central duration5.07h vs observed median3.46h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Triangular ingress and egress repeat cleanly. No capable neighbor under the approximate G-band flux screen.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 59 | 176 | 2912.9427546 | 0.001157 | 139.489 | usable; same-kind selection applies |
| 59 | 177 | 2918.2058723 | 0.001157 | 139.237 | usable; same-kind selection applies |
| 59 | 179 | 2928.7319403 | 0.001157 | 138.997 | usable; same-kind selection applies |
| 59 | 180 | 2933.9949223 | 0.001157 | 139.691 | usable; same-kind selection applies |
| 86 | 315 | 3644.5144895 | 0.001157 | 137.296 | usable; same-kind selection applies |
| 86 | 318 | 3660.3038478 | 0.001157 | 137.591 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s53.json, historical/diff_s53.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R221. [Deciding evidence](../../evidence/280881615/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
