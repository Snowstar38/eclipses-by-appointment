# TIC 131331287: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 8 distinct eclipse events in selected sectors[37, 64, 102]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=6.8447853694 Ã‚+/-0.0000054333d, reference eclipse epoch BTJD2313.5253293, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S64 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation1.201arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.046. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths121.693/118.758/116.981ppt, with 3 stacked events. QLP selected-kind fitted median135.367ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36169826348699703424, P=6.8443655076Ã‚+/-0.0009405552d, e=0.259533, omega=305.2292deg. Closest edge-on conjunction offset0.053274d (0.007784phase), full-SB1-covariance linear propagated Gaia uncertainty0.199939d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.064708d (photometric period projection allowance0.001527d). The approximate central duration6.94h vs observed median5.70h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep repeated events have reduced depths in sector102 relative to37/64; aperture dilution or baseline changes possible, no intrinsic depth variation claimed.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 37 | 0 | 2313.5221586 | 0.003472 | 135.542 | used in ephemeris |
| 37 | 2 | 2327.2120790 | 0.003472 | 135.193 | used in ephemeris |
| 64 | 107 | 3045.9176080 | 0.001157 | 140.625 | used in ephemeris |
| 64 | 108 | 3052.7625806 | 0.001157 | 139.738 | used in ephemeris |
| 64 | 109 | 3059.6073706 | 0.001157 | 139.546 | used in ephemeris |
| 102 | 266 | 4134.2384426 | 0.001157 | 110.040 | used in ephemeris |
| 102 | 267 | 4141.0827260 | 0.001157 | 110.358 | used in ephemeris |
| 102 | 268 | 4147.9274541 | 0.001157 | 110.766 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s64.json, historical/diff_s64.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R339. [Deciding evidence](../../2026-10-31-bright73/evidence/131331287) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/131331287/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/131331287/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/131331287/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch01/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch01/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/131331287/historical/diff_s64.png).
