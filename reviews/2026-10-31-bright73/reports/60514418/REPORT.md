# TIC 60514418: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 5 distinct eclipse events in selected sectors[43, 44, 71]. The representative raw-event plot and numeric raw-windows.csv were inspected. The raw morphology, ingress/egress and local baselines were inspected independently of fitted curves; target-specific interpretation follows below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=11.6952161043 +/-0.0000339692d, reference eclipse epoch BTJD2475.7039155, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S44 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation0.747arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.202. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths35.497/34.959/34.188ppt, with 2 stacked events. QLP selected-kind fitted median38.420ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3153384449055145856, P=11.6940432568+/-0.0012138569d, e=0.063286, omega=211.5158deg. Closest edge-on conjunction offset0.160480d (0.013723phase), full-SB1-covariance linear propagated Gaia uncertainty0.190129d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.048287d (photometric period projection allowance0.006047d). The approximate central duration8.77h vs observed median3.72h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated V-shaped eclipses in S43/44/71; consecutive S44 cycles test recurrence. No capable listed neighbor; observed duration3.72h is shorter than illustrative central duration8.77h, compatible with noncentral eclipse.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 43 | 0 | 2475.7036610 | 0.003473 | 40.742 | used in ephemeris |
| 44 | 3 | 2510.7897311 | 0.003472 | 38.658 | used in ephemeris |
| 44 | 4 | 2522.4847784 | 0.003472 | 38.037 | used in ephemeris |
| 71 | 65 | 3235.8933198 | 0.001157 | 36.920 | used in ephemeris |
| 71 | 67 | 3259.2830468 | 0.001157 | 38.420 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s44.json, historical/diff_s44.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are [local path omitted] and [local path omitted] No historical evidence overwritten.


Stable review key: R400. [Deciding evidence](../../evidence/60514418/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/60514418/measurements.json), [raw eclipse plots](../../evidence/60514418/raw-events.png), [raw flux windows](../../evidence/60514418/raw-windows.csv), [Gaia geometry](../../analysis/batch07/gaia-geometry.json), [independent audit](../../analysis/batch07/helper-audit.md), [difference image](../../evidence/60514418/historical/diff_s44.png).
