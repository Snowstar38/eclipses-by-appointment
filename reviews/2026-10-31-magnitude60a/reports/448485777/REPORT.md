# TIC 448485777: PROBABLE

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[11, 99, 102]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=5.8952882395 ±0.0000227545d, fitted ephemeris intercept at earliest retained cycle BTJD1603.4712444, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: unresolved after check.** Historical S11 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation5.303arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.300. Capable neighbours: Gaia 5847716106616806784: 14.44 arcsec, G15.332, required fractional eclipse0.976, pixel fractional loss0.0215936791346104; Gaia 5847716102285049344: 16.26 arcsec, G13.144, required fractional eclipse0.161, pixel fractional loss0.01979753444323785; Gaia 5847715728659680000: 20.52 arcsec, G14.358, required fractional eclipse0.419, pixel fractional loss0.03241426402958959; Gaia 5847715728659676800: 21.71 arcsec, G15.306, required fractional eclipse0.954, pixel fractional loss0.03276142993066764; Gaia 5847716102285056384: 25.76 arcsec, G15.235, required fractional eclipse0.896, pixel fractional loss0.0215936791346104; Gaia 5847716106616813440: 57.68 arcsec, G14.848, required fractional eclipse0.638, pixel fractional loss0.005557348234906238
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths33.268/29.822/29.128ppt, with 4 stacked events. QLP selected-kind fitted median37.981ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35847715724327436160, P=5.8948949185±0.0003771119d, e=0.086403, omega=238.3671deg. Closest edge-on conjunction offset0.143279d (0.024306phase), full-SB1-covariance linear propagated Gaia uncertainty0.087194d at the measured epoch. Near-Gaia-reference projected eclipse offset0.062255d (photometric period projection allowance0.004687d). The approximate central duration11.63h vs observed median6.69h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Crowded field: G13.14 neighbor16.26arcsec away requires16.1% eclipse, deficit0.615pixel from neighbor vs0.252pixel target. Another14.44arcsec neighbor requires97.6%. Target is favored by central deficit and deeper1x1 aperture, but blending and uncalibrated localization leave attribution physically unresolved after completed checks.

**Next check:** Resolved eclipse photometry or multi-source PRF localization of this signal.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 11 | 0 | 1603.4657715 | 0.010417 | 41.254 | usable; same-kind selection applies |
| 11 | 2 | 1615.2598235 | 0.010417 | 38.170 | usable; same-kind selection applies |
| 11 | 3 | 1621.1553002 | 0.010417 | 37.643 | usable; same-kind selection applies |
| 99 | 415 | 4050.0166038 | 0.001157 | 39.084 | usable; same-kind selection applies |
| 99 | 418 | 4067.7045691 | 0.001157 | 36.015 | usable; same-kind selection applies |
| 102 | 429 | 4132.5485969 | 0.001157 | 37.135 | usable; same-kind selection applies |
| 102 | 431 | 4144.3414105 | 0.001157 | 38.856 | usable; same-kind selection applies |
| 102 | 432 | 4150.2326655 | 0.001157 | 37.792 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s11.json, historical/diff_s11.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R231. [Deciding evidence](../../evidence/448485777/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
