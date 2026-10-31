# TIC 167105778: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[15, 75, 83]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=8.5865668060 ±0.0000273371d, reference eclipse epoch BTJD1718.8649126, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S56 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation3.804arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.490. Capable neighbours: Gaia 1968960312990727296: 10.12 arcsec, G14.833, required fractional eclipse0.441, pixel fractional loss0.02316814965491679; Gaia 1968960278623106176: 55.49 arcsec, G14.881, required fractional eclipse0.460, pixel fractional loss-0.001106644215653597
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths23.168/22.598/20.538ppt, with 4 stacked events. QLP selected-kind fitted median24.975ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31968960312990725888, P=8.5870099785±0.0010707120d, e=0.017110, omega=153.5675deg. Closest edge-on conjunction offset-0.155334d (-0.018089phase), full-SB1-covariance linear propagated Gaia uncertainty0.199645d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.086642d (photometric period projection allowance0.004237d). The approximate central duration9.82h vs observed median6.95h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Capable G14.83 neighbor10.1arcsec away requires44% eclipse. Deficit is0.18pixel from target and0.47pixel from neighbor; image favors target, with uncalibrated centroid resolution retained as limitation.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 15 | 0 | 1718.8711042 | 0.010417 | 25.465 | usable; same-kind selection applies |
| 15 | 1 | 1727.4578265 | 0.010417 | 25.730 | usable; same-kind selection applies |
| 75 | 189 | 3341.7252905 | 0.001282 | 23.103 | usable; same-kind selection applies |
| 75 | 190 | 3350.3114455 | 0.001157 | 24.975 | usable; same-kind selection applies |
| 75 | 191 | 3358.8998480 | 0.001274 | 25.117 | usable; same-kind selection applies |
| 83 | 215 | 3564.9855222 | 74778.289228 | 23.830 | excluded singular timing fit |
| 83 | 216 | 3573.5637494 | 0.001157 | 24.259 | usable; same-kind selection applies |
| 83 | 217 | 3582.1505608 | 0.001157 | 24.167 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s56.json, historical/diff_s56.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R218. [Deciding evidence](../../evidence/167105778/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
