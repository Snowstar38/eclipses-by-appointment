# TIC 169303527: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 10 distinct eclipse events in selected sectors[29, 69, 96]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 10 same-kind midtimes give P=5.4456847708 ±0.0000051113d, reference eclipse epoch BTJD2091.7221616, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S69 deficit peak[8, 8] vs target pixel[8, 7]; deficit-target separation1.330arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.165. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths131.025/128.228/120.717ppt, with 4 stacked events. QLP selected-kind fitted median132.330ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32326446555743706112, P=5.4456409811±0.0011930950d, e=0.165642, omega=93.6455deg. Closest edge-on conjunction offset0.022408d (0.004115phase), full-SB1-covariance linear propagated Gaia uncertainty0.264837d at the measured epoch. Near-Gaia-reference projected eclipse offset0.008702d (photometric period projection allowance0.001600d). The approximate central duration3.96h vs observed median3.17h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated isolated eclipses show sector-dependent dilution/depth. No capable catalogued neighbor under approximate Gaia brightness screen.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 29 | 0 | 2091.7229281 | 0.003472 | 132.553 | usable; same-kind selection applies |
| 29 | 1 | 2097.1687307 | 0.003472 | 132.107 | usable; same-kind selection applies |
| 69 | 201 | 3186.3046405 | 0.001157 | 133.930 | usable; same-kind selection applies |
| 69 | 202 | 3191.7501075 | 0.001157 | 134.793 | usable; same-kind selection applies |
| 69 | 203 | 3197.1961780 | 0.001157 | 133.455 | usable; same-kind selection applies |
| 69 | 204 | 3202.6419381 | 0.001157 | 133.461 | usable; same-kind selection applies |
| 96 | 334 | 3910.5807085 | 0.001157 | 115.495 | usable; same-kind selection applies |
| 96 | 335 | 3916.0264305 | 0.001157 | 115.316 | usable; same-kind selection applies |
| 96 | 337 | 3926.9181463 | 0.001157 | 112.695 | usable; same-kind selection applies |
| 96 | 338 | 3932.3639560 | 0.001157 | 111.422 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s69.json, historical/diff_s69.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R283. [Deciding evidence](../../evidence/169303527/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
