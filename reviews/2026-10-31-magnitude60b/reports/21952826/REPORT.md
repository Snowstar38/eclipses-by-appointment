# TIC 21952826: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 4 distinct eclipse events in selected sectors[62, 99]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=9.7685847110 +/-0.0000106665d, reference eclipse epoch BTJD2995.8445787, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S35 deficit peak[8, 8] vs target pixel[8, 7]; deficit-target separation7.214arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.137. Capable neighbours: Gaia 5659918043089101184: 40.76 arcsec, G15.240, required fractional eclipse0.520; Gaia 5659918008729365120: 55.61 arcsec, G15.689, required fractional eclipse0.774
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths24.848/24.899/23.814ppt, with 2 stacked events. QLP selected-kind fitted median25.067ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35659920998026599936, P=9.7676391567+/-0.0023223683d, e=0.018212, omega=79.9643deg. Closest edge-on conjunction offset0.238592d (0.024427phase), full-SB1-covariance linear propagated Gaia uncertainty0.691423d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.013871d (photometric period projection allowance0.002848d). The approximate central duration4.73h vs observed median2.44h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Four measured repeats, with consecutive events in sector62. Deficit0.344pixel from target; nearest capable neighbor2.08pixels from deficit. Sector-dependent depth may reflect aperture dilution.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 62 | 151 | 2995.8451919 | 0.001157 | 27.208 | usable; same-kind selection applies |
| 62 | 152 | 3005.6125381 | 0.001157 | 30.099 | usable; same-kind selection applies |
| 99 | 259 | 4050.8520827 | 0.001157 | 22.925 | usable; same-kind selection applies |
| 99 | 261 | 4070.3885538 | 0.001157 | 21.919 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s35.json, historical/diff_s35.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R300. [Deciding evidence](../../evidence/21952826/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
