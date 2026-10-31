# TIC 88811793: PROBABLE

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 10 distinct eclipse events in selected sectors[13, 93, 104]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 10 same-kind midtimes give P=7.4357138600 +/-0.0000172221d, reference eclipse epoch BTJD1660.0553916, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: unresolved after check.** Deciding S93 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation1.829arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.732. Capable neighbours: Gaia 6721228062775457920: 14.54 arcsec, G12.652, required fractional eclipse0.161, pixel fractional loss0.024512582723309626; Gaia 6721225146508733184: 27.33 arcsec, G10.653, required fractional eclipse0.078, pixel fractional loss0.002358223522502439
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths44.826/23.910/14.579ppt, with 4 stacked events. QLP selected-kind fitted median63.740ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36721228062775458304, P=7.4358869328+/-0.0013790350d, e=0.068823, omega=310.9380deg. Closest edge-on conjunction offset0.081898d (0.011014phase), full-SB1-covariance linear propagated Gaia uncertainty0.348216d at the measured epoch. Near-Gaia-reference projected eclipse offset0.111493d (photometric period projection allowance0.002945d). The approximate central duration9.19h vs observed median7.58h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unresolved close-neighbor attribution after completed check. Capable neighbor14.54arcsec away lies0.75pixel from deficit centroid; target is0.087pixel away. Another capable neighbor27.33arcsec away is spatially distinct. Deficit favors target, but no calibrated multi-source PRF localization excludes the closest source. Strong aperture dilution: cutout45/24/15ppt versus QLP approximately60ppt. Pixel fractional loss is blended light, not source-intrinsic required eclipse.

**Next check:** Resolved eclipse photometry or multi-source PRF localization of this signal.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 13 | 0 | 1660.0504423 | 0.010416 | 63.001 | usable; same-kind selection applies |
| 13 | 2 | 1674.9231024 | 0.010416 | 64.479 | usable; same-kind selection applies |
| 93 | 292 | 3831.2811996 | 0.001388 | 68.170 | usable; same-kind selection applies |
| 93 | 293 | 3838.7214210 | 0.001701 | 68.095 | usable; same-kind selection applies |
| 93 | 294 | 3846.1566901 | 0.001436 | 67.941 | usable; same-kind selection applies |
| 93 | 295 | 3853.5926349 | 0.001559 | 65.753 | usable; same-kind selection applies |
| 104 | 339 | 4180.7615783 | 0.002137 | 57.446 | usable; same-kind selection applies |
| 104 | 340 | 4188.1977932 | 0.001313 | 58.441 | usable; same-kind selection applies |
| 104 | 341 | 4195.6333412 | 0.001633 | 55.911 | usable; same-kind selection applies |
| 104 | 342 | 4203.0690200 | 0.004059 | 60.207 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s93.json, historical/diff_s93.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] For TIC407207285 the deciding revised cutout is revised-cutout/diff_revised-long-window.json and .png; historical extraction remains for comparison. Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R258. [Deciding evidence](../../evidence/88811793/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
