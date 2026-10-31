# TIC 300148401: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 8 distinct eclipse events in selected sectors[6, 33, 98]. The representative raw-event plot and numeric raw-windows.csv were inspected. The raw morphology, ingress/egress and local baselines were inspected independently of fitted curves; target-specific interpretation follows below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=8.7876379642 +/-0.0000126985d, reference eclipse epoch BTJD1469.3015561, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S32 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation1.674arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.504. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths45.737/46.373/45.311ppt, with 3 stacked events. QLP selected-kind fitted median52.895ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32884583087778756224, P=8.7880603922+/-0.0014557943d, e=0.142219, omega=170.3694deg. Closest edge-on conjunction offset0.026216d (0.002983phase), full-SB1-covariance linear propagated Gaia uncertainty0.174132d at the measured epoch. Near-Gaia-reference projected eclipse offset0.078174d (photometric period projection allowance0.001562d). The approximate central duration6.82h vs observed median5.07h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated narrow eclipse cores on curved variable baseline; early S6 is sparse at30min cadence, while S33/98 resolve recurrence. Linear baseline and depth precision are limited by curvature; no capable listed neighbor.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 6 | 0 | 1469.3028231 | 0.010417 | 52.704 | used in ephemeris |
| 6 | 2 | 1486.8816622 | 0.021990 | 28.101 | used in ephemeris |
| 33 | 84 | 2207.4746549 | 0.005693 | 60.142 | used in ephemeris |
| 33 | 85 | 2216.2472697 | 0.003472 | 56.352 | used in ephemeris |
| 33 | 86 | 2225.0371901 | 0.003472 | 55.892 | used in ephemeris |
| 98 | 288 | 4000.1439610 | 0.003506 | 53.086 | used in ephemeris |
| 98 | 291 | 4026.5043511 | 0.001561 | 41.323 | used in ephemeris |
| 98 | 293 | 4044.0766302 | 0.003304 | 41.625 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s32.json, historical/diff_s32.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are [local path omitted] and [local path omitted] No historical evidence overwritten.


Stable review key: R398. [Deciding evidence](../../evidence/300148401/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/300148401/measurements.json), [raw eclipse plots](../../evidence/300148401/raw-events.png), [raw flux windows](../../evidence/300148401/raw-windows.csv), [Gaia geometry](../../analysis/batch07/gaia-geometry.json), [independent audit](../../analysis/batch07/helper-audit.md), [difference image](../../evidence/300148401/historical/diff_s32.png).
