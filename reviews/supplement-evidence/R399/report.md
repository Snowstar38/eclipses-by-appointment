# TIC 167125054: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 8 distinct eclipse events in selected sectors[1, 36, 98]. The representative raw-event plot and numeric raw-windows.csv were inspected. The raw morphology, ingress/egress and local baselines were inspected independently of fitted curves; target-specific interpretation follows below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=9.1223775152 +/-0.0000113717d, reference eclipse epoch BTJD1326.8709038, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S1 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation5.019arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.417. Capable neighbours: Gaia 5283286313593528192: 38.02 arcsec, G12.828, required fractional eclipse0.203
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths62.675/55.530/44.226ppt, with 3 stacked events. QLP selected-kind fitted median60.330ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35283286103133262208, P=9.1224018521+/-0.0010396464d, e=0.006947, omega=77.3211deg. Closest edge-on conjunction offset-0.079784d (-0.008746phase), full-SB1-covariance linear propagated Gaia uncertainty0.167676d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.077277d (photometric period projection allowance0.001171d). The approximate central duration10.42h vs observed median9.16h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated broad flat-bottom eclipses in S1/36/99; depth near60ppt. Target deficit0.239pixel versus capable neighbor2.036pixels.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 1 | 0 | 1326.8708926 | 0.010417 | 60.114 | used in ephemeris |
| 1 | 1 | 1335.9939294 | 0.010417 | 59.777 | used in ephemeris |
| 1 | 2 | 1345.1161249 | 0.010417 | 60.243 | used in ephemeris |
| 36 | 105 | 2284.7201107 | 0.003472 | 63.700 | used in ephemeris |
| 36 | 107 | 2302.9656415 | 0.003472 | 63.649 | used in ephemeris |
| 98 | 293 | 3999.7274128 | 0.001157 | 60.535 | used in ephemeris |
| 98 | 296 | 4027.0938736 | 0.001157 | 59.743 | used in ephemeris |
| 98 | 298 | 4045.3402771 | 0.001157 | 60.416 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s01.json, historical/diff_s01.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are [local path omitted] and [local path omitted] No historical evidence overwritten.


Stable review key: R399. [Deciding evidence](../../2026-10-31-bright73/evidence/167125054) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/167125054/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/167125054/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/167125054/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch07/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch07/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/167125054/historical/diff_s01.png).
