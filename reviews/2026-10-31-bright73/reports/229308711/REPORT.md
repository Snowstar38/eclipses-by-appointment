# TIC 229308711: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 4 distinct eclipse events in selected sectors[6, 71]. The representative raw-event plot and numeric raw-windows.csv were inspected. The raw morphology, ingress/egress and local baselines were inspected independently of fitted curves; target-specific interpretation follows below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=14.6174947319 +/-0.0000862147d, reference eclipse epoch BTJD1471.0933055, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S6 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.484arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.289. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths15.273/15.231/13.308ppt, with 2 stacked events. QLP selected-kind fitted median27.974ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR33327940359740480768, P=14.6215831706+/-0.0049952480d, e=0.028473, omega=271.7243deg. Closest edge-on conjunction offset-0.249469d (-0.017062phase), full-SB1-covariance linear propagated Gaia uncertainty0.546625d at the measured epoch. Near-Gaia-reference projected eclipse offset0.053076d (photometric period projection allowance0.006380d). The approximate central duration18.67h vs observed median12.78h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Four long flat-bottom eclipses repeat in consecutive pairs in S6 and71. Curved/sloped out-of-eclipse variability and asymmetric troughs limit simple trapezoid midtimes. The timing fit allows scatter inflation when needed (none applied here), but does not include total shape systematics. Historical custom pixel stack confirms target deficit0.118pixel; no capable listed neighbor. Consecutive pairs test recurrence and long-baseline cycle count. Equal eclipse kinds could conceal a doubled orbital alias; Gaia supports the retained branch.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 6 | 0 | 1471.0942435 | 0.010417 | 25.684 | used in ephemeris |
| 6 | 1 | 1485.6981493 | 0.037975 | 27.562 | used in ephemeris |
| 71 | 121 | 3239.8105347 | 0.007298 | 30.553 | used in ephemeris |
| 71 | 122 | 3254.4275867 | 0.003354 | 28.386 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s06.json, historical/diff_s06.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are [local path omitted] and [local path omitted] No historical evidence overwritten. Historical inventory G=12.0132; actual nested Gaia DR3 G=11.995216. All three are inside actual DR3 G11.5-12 despite inventory values above12; this preserves the inventory/DR3 distinction.


Stable review key: R409. [Deciding evidence](../../evidence/229308711/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/229308711/measurements.json), [raw eclipse plots](../../evidence/229308711/raw-events.png), [raw flux windows](../../evidence/229308711/raw-windows.csv), [Gaia geometry](../../analysis/batch08/gaia-geometry.json), [independent audit](../../analysis/batch08/helper-audit.md), [difference image](../../evidence/229308711/historical/diff_s06.png).
