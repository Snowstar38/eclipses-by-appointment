# TIC 379550793: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 19 distinct eclipse events in selected sectors[64, 101]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 19 same-kind midtimes give P=2.4798111572 +/-0.0000014767d, reference eclipse epoch BTJD3041.9007652, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S38 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation6.620arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.700. Capable neighbours: Gaia 6058502724870374912: 15.61 arcsec, G16.097, required fractional eclipse0.529; Gaia 6058502793589851136: 20.31 arcsec, G15.796, required fractional eclipse0.404; Gaia 6058502724870373888: 21.42 arcsec, G13.912, required fractional eclipse0.081; Gaia 6058502724870375552: 27.27 arcsec, G14.352, required fractional eclipse0.115; Gaia 6058502724870373760: 29.18 arcsec, G16.482, required fractional eclipse0.749; Gaia 6058502754891546752: 36.05 arcsec, G16.282, required fractional eclipse0.625; Gaia 6057752102023464064: 38.96 arcsec, G16.156, required fractional eclipse0.558; Gaia 6058502793589852544: 40.20 arcsec, G16.063, required fractional eclipse0.513; Gaia 6058502690510531712: 42.43 arcsec, G16.447, required fractional eclipse0.726; Gaia 6057752136383209344: 42.52 arcsec, G15.938, required fractional eclipse0.458; Gaia 6058502690510531456: 45.24 arcsec, G15.898, required fractional eclipse0.442; Gaia 6058502759230114816: 46.85 arcsec, G14.905, required fractional eclipse0.184; Gaia 6057752136383211136: 48.56 arcsec, G15.402, required fractional eclipse0.284; Gaia 6058502793555875456: 51.23 arcsec, G16.436, required fractional eclipse0.718; Gaia 6058502793589748352: 51.39 arcsec, G14.227, required fractional eclipse0.104; Gaia 6058502621791051776: 53.01 arcsec, G13.381, required fractional eclipse0.054; Gaia 6058502793589748992: 54.98 arcsec, G16.251, required fractional eclipse0.608; Gaia 6058502621791051904: 55.79 arcsec, G15.214, required fractional eclipse0.241; Gaia 6057752136383212800: 56.20 arcsec, G14.549, required fractional eclipse0.136
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths12.036/10.485/7.514ppt, with 11 stacked events. QLP selected-kind fitted median11.453ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36058502724870374272, P=2.4797362150+/-0.0001521287d, e=0.018215, omega=160.3186deg. Closest edge-on conjunction offset0.076701d (0.030931phase), full-SB1-covariance linear propagated Gaia uncertainty0.172965d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.003488d (photometric period projection allowance0.001580d). The approximate central duration4.42h vs observed median1.79h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Crowded field: deficit0.315pixel from target; closest capable neighbor0.856pixel from deficit (G13.91,21.4arcsec). Peak/core favors target, with no calibrated centroid errors; aperture depths12.04/10.48/7.51ppt and sector depths differ through dilution. Intrinsic neighbor eclipse requirements are not directly compared with blended pixel losses.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 64 | 592 | 3041.9001207 | 0.001605 | 14.812 | usable; same-kind selection applies |
| 64 | 593 | 3044.3767653 | 0.001420 | 12.393 | usable; same-kind selection applies |
| 64 | 594 | 3046.8611067 | 0.001157 | 17.351 | usable; same-kind selection applies |
| 64 | 595 | 3049.3416450 | 0.001511 | 11.108 | usable; same-kind selection applies |
| 64 | 596 | 3051.8199952 | 0.001522 | 13.523 | usable; same-kind selection applies |
| 64 | 597 | 3054.2992656 | 0.001450 | 12.556 | usable; same-kind selection applies |
| 64 | 598 | 3056.7792143 | 0.001157 | 10.596 | usable; same-kind selection applies |
| 64 | 599 | 3059.2611263 | 0.001408 | 15.204 | usable; same-kind selection applies |
| 64 | 600 | 3061.7411370 | 0.001418 | 14.044 | usable; same-kind selection applies |
| 64 | 601 | 3064.2188907 | 0.001157 | 14.765 | usable; same-kind selection applies |
| 64 | 602 | 3066.6986276 | 0.001582 | 12.214 | usable; same-kind selection applies |
| 101 | 1020 | 4103.2606006 | 0.001178 | 9.125 | usable; same-kind selection applies |
| 101 | 1021 | 4105.7396162 | 0.001157 | 11.128 | usable; same-kind selection applies |
| 101 | 1022 | 4108.2214580 | 0.001157 | 11.305 | usable; same-kind selection applies |
| 101 | 1023 | 4110.6992867 | 0.001157 | 10.728 | usable; same-kind selection applies |
| 101 | 1025 | 4115.6582089 | 0.001157 | 9.993 | usable; same-kind selection applies |
| 101 | 1026 | 4118.1363897 | 0.001318 | 10.210 | usable; same-kind selection applies |
| 101 | 1027 | 4120.6194115 | 0.001157 | 10.500 | usable; same-kind selection applies |
| 101 | 1028 | 4123.0979682 | 0.001163 | 11.453 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s38.json, historical/diff_s38.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R297. [Deciding evidence](../../evidence/379550793/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
