# TIC 256665207: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 19 distinct eclipse events in selected sectors[58, 86]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 19 same-kind midtimes give P=2.7907385784 ±0.0000027067d, fitted ephemeris intercept at earliest retained cycle BTJD2884.6986301, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S55 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation3.481arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.177. Capable neighbours: Gaia 2238265718901540224: 32.78 arcsec, G16.300, required fractional eclipse0.384, pixel fractional loss0.005700579685187473; Gaia 2238265791919992576: 53.79 arcsec, G16.967, required fractional eclipse0.705, pixel fractional loss0.008951220717294421
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths7.140/6.683/6.612ppt, with 10 stacked events. QLP selected-kind fitted median6.603ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32238265757560253312, P=2.7907557184±0.0000952841d, e=0.051842, omega=220.0501deg. Closest edge-on conjunction offset-0.023180d (-0.008306phase), full-SB1-covariance linear propagated Gaia uncertainty0.096919d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.007857d (photometric period projection allowance0.002420d). The approximate central duration4.78h vs observed median1.41h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Approximately6-7ppt flat-bottom eclipses repeat. No compelling even/odd split establishes half/double alias; full Gaia period agrees with recurrence. Nearest capable source32.78arcsec away,1.70pixel from deficit vs0.166pixel target.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 58 | 430 | 2884.6993485 | 0.001157 | 6.737 | usable; same-kind selection applies |
| 58 | 431 | 2887.4895215 | 0.001398 | 7.157 | usable; same-kind selection applies |
| 58 | 432 | 2890.2804994 | 0.001385 | 6.603 | usable; same-kind selection applies |
| 58 | 433 | 2893.0706498 | 0.001315 | 6.583 | usable; same-kind selection applies |
| 58 | 434 | 2895.8593776 | 0.001479 | 6.543 | usable; same-kind selection applies |
| 58 | 435 | 2898.6525323 | 0.001157 | 5.534 | usable; same-kind selection applies |
| 58 | 436 | 2901.4430937 | 0.001157 | 7.079 | usable; same-kind selection applies |
| 58 | 437 | 2904.2330928 | 0.001343 | 6.060 | usable; same-kind selection applies |
| 58 | 438 | 2907.0251760 | 0.001402 | 6.878 | usable; same-kind selection applies |
| 58 | 439 | 2909.8155043 | 0.001157 | 6.128 | usable; same-kind selection applies |
| 86 | 700 | 3638.2018317 | 0.002793 | 5.639 | usable; same-kind selection applies |
| 86 | 701 | 3640.9897766 | 0.001893 | 6.946 | usable; same-kind selection applies |
| 86 | 702 | 3643.7793978 | 0.001157 | 6.017 | usable; same-kind selection applies |
| 86 | 703 | 3646.5684652 | 0.001526 | 6.952 | usable; same-kind selection applies |
| 86 | 704 | 3649.3637364 | 0.001989 | 8.067 | usable; same-kind selection applies |
| 86 | 705 | 3652.1544705 | 0.006063 | 4.604 | usable; same-kind selection applies |
| 86 | 706 | 3654.9429783 | 0.002169 | 8.794 | usable; same-kind selection applies |
| 86 | 707 | 3657.7327724 | 0.001587 | 6.142 | usable; same-kind selection applies |
| 86 | 708 | 3660.5216443 | 0.002011 | 7.599 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s55.json, historical/diff_s55.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R235. [Deciding evidence](../../evidence/256665207/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
