# TIC 374589618: PROBABLE

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 23 distinct eclipse events in selected sectors[54, 81]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 9 same-kind midtimes give P=3.1662972967 ±0.0000098424d, reference eclipse epoch BTJD2778.4906828, kind: Deeper repeating eclipse; odd half-period cycles. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: unresolved after check.** Historical S81 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation2.081arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.658. Capable neighbours: Gaia 1802168316060661376: 13.53 arcsec, G17.280, required fractional eclipse0.790; Gaia 1802168311763607936: 24.73 arcsec, G17.409, required fractional eclipse0.889; Gaia 1802168419139874048: 31.65 arcsec, G15.749, required fractional eclipse0.197; Gaia 1802165464202369664: 42.66 arcsec, G16.941, required fractional eclipse0.580; Gaia 1802168384780141824: 43.76 arcsec, G15.783, required fractional eclipse0.203; Gaia 1802168483562365568: 47.58 arcsec, G16.950, required fractional eclipse0.585; Gaia 1802168380483110784: 52.04 arcsec, G16.353, required fractional eclipse0.340; Gaia 1802168449202616960: 53.79 arcsec, G17.242, required fractional eclipse0.763
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths5.646/5.783/5.584ppt, with 14 stacked events. QLP selected-kind fitted median8.042ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31802168419139873280, P=3.1662003845±0.0001950480d, e=0.028319, omega=52.2631deg. Closest edge-on conjunction offset0.107914d (0.034083phase), full-SB1-covariance linear propagated Gaia uncertainty0.120399d at the measured epoch. Near-Gaia-reference projected eclipse offset0.034746d (photometric period projection allowance0.007431d). The approximate central duration5.86h vs observed median1.60h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated shallow alternating eclipses are real; odd half-period cycles define deeper-eclipse timing. Deficit0.099pixel from target favors target, but capable neighbor13.5arcsec away is only0.67pixel from deficit and needs approximately79percent intrinsic eclipse. An undersampled sector54 fit can exaggerate depth (cycle2 fitted15.37ppt versus observed minimum about7-8ppt); that even-parity fit is excluded from the deeper odd-parity ephemeris. Shallow noisy difference image lacks calibrated localization; source attribution remains unresolved after bounded check.

**Next check:** Resolved eclipse photometry or multi-source PRF localization of this signal.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 54 | 2 | 2773.7374851 | 0.003472 | 15.365 | usable; same-kind selection applies |
| 54 | 4 | 2776.8974321 | 0.005716 | 6.642 | usable; same-kind selection applies |
| 54 | 5 | 2778.4855848 | 0.003959 | 8.042 | usable; same-kind selection applies |
| 54 | 6 | 2780.0708114 | 0.005585 | 8.551 | usable; same-kind selection applies |
| 54 | 9 | 2784.8259336 | 0.003472 | 7.175 | usable; same-kind selection applies |
| 54 | 10 | 2786.4000831 | 0.005845 | 3.812 | usable; same-kind selection applies |
| 54 | 11 | 2787.9910721 | 0.003472 | 7.679 | usable; same-kind selection applies |
| 54 | 13 | 2791.1539523 | 0.003472 | 5.668 | excluded singular timing fit |
| 54 | 14 | 2792.7348870 | 0.006090 | 4.583 | usable; same-kind selection applies |
| 54 | 16 | 2795.9030916 | 4.191226 | 18.031 | excluded singular timing fit |
| 81 | 465 | 3506.7395943 | 0.002124 | 8.472 | usable; same-kind selection applies |
| 81 | 466 | 3508.3230973 | 0.002226 | 6.562 | usable; same-kind selection applies |
| 81 | 467 | 3509.9039935 | 0.001199 | 9.904 | usable; same-kind selection applies |
| 81 | 468 | 3511.4786201 | 0.003212 | 5.652 | usable; same-kind selection applies |
| 81 | 469 | 3513.0721228 | 0.001496 | 9.469 | usable; same-kind selection applies |
| 81 | 472 | 3517.8136376 | 0.003690 | 9.062 | usable; same-kind selection applies |
| 81 | 474 | 3520.9864498 | 0.001157 | 5.197 | usable; same-kind selection applies |
| 81 | 475 | 3522.5714060 | 0.001663 | 11.300 | usable; same-kind selection applies |
| 81 | 476 | 3524.1545767 | 0.001247 | 5.174 | usable; same-kind selection applies |
| 81 | 477 | 3525.7353536 | 0.001639 | 7.462 | usable; same-kind selection applies |
| 81 | 478 | 3527.3206150 | 0.002551 | 5.028 | usable; same-kind selection applies |
| 81 | 479 | 3528.9062454 | 0.001913 | 7.414 | usable; same-kind selection applies |
| 81 | 480 | 3530.4794510 | 0.002681 | 5.876 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s81.json, historical/diff_s81.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R281. [Deciding evidence](../../evidence/374589618/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
