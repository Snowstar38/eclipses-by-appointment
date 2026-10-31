# TIC 156103314: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 9 distinct eclipse events in selected sectors[14, 41, 74]. The representative raw-event plot and numeric raw-windows.csv were inspected. The raw morphology, ingress/egress and local baselines were inspected independently of fitted curves; target-specific interpretation follows below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 9 same-kind midtimes give P=8.1521424200 +/-0.0000185155d, reference eclipse epoch BTJD1691.0673712, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S40 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation3.626arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.140. Capable neighbours: Gaia 1129836918680283008: 36.63 arcsec, G14.967, required fractional eclipse0.510
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths32.550/31.110/29.172ppt, with 4 stacked events. QLP selected-kind fitted median31.470ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31129836845665117312, P=8.1517909446+/-0.0005995836d, e=0.151241, omega=286.0880deg. Closest edge-on conjunction offset0.030193d (0.003704phase), full-SB1-covariance linear propagated Gaia uncertainty0.085527d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.026043d (photometric period projection allowance0.002962d). The approximate central duration8.41h vs observed median6.18h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated flat-bottom eclipses across S14/41/74 with stable31-32ppt depth. Target deficit0.173pixel versus capable neighbor1.864pixels.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 14 | 0 | 1691.0682147 | 0.010417 | 31.668 | used in ephemeris |
| 14 | 1 | 1699.2208326 | 0.010417 | 31.449 | used in ephemeris |
| 14 | 2 | 1707.3742829 | 0.010417 | 31.470 | used in ephemeris |
| 41 | 90 | 2424.7590385 | 0.003472 | 31.947 | used in ephemeris |
| 41 | 92 | 2441.0650222 | 0.003472 | 32.312 | used in ephemeris |
| 74 | 199 | 3313.3417474 | 0.001157 | 32.794 | used in ephemeris |
| 74 | 200 | 3321.4962720 | 0.001157 | 31.290 | used in ephemeris |
| 74 | 201 | 3329.6488137 | 0.001157 | 30.378 | used in ephemeris |
| 74 | 202 | 3337.8008805 | 0.001157 | 31.325 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s40.json, historical/diff_s40.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are [local path omitted] and [local path omitted] No historical evidence overwritten.


Stable review key: R403. [Deciding evidence](../../2026-10-31-bright73/evidence/156103314) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/156103314/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/156103314/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/156103314/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch07/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch07/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/156103314/historical/diff_s40.png).
