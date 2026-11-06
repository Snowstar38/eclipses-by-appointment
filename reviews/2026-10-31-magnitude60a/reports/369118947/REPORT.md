# TIC 369118947: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 9 distinct eclipse events in selected sectors[12, 93, 104]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 9 same-kind midtimes give P=5.3592734775 ±0.0000136631d, reference eclipse epoch BTJD1632.7557204, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S39 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation3.683arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.923. Capable neighbours: Gaia 5949510916010450048: 53.79 arcsec, G12.654, required fractional eclipse0.622, pixel fractional loss0.0011707993086129812
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths169.328/127.739/59.283ppt, with 4 stacked events. QLP selected-kind fitted median186.853ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35949512427837846144, P=5.3589663376±0.0003517770d, e=0.023477, omega=279.2669deg. Closest edge-on conjunction offset0.104460d (0.019493phase), full-SB1-covariance linear propagated Gaia uncertainty0.058542d at the measured epoch. Near-Gaia-reference projected eclipse offset0.033204d (photometric period projection allowance0.003170d). The approximate central duration6.24h vs observed median4.73h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Target-centered deficit despite poor0.923 total-light PSF residual in crowded field. Capable neighbor53.8arcsec away is well separated. Aperture-dependent diluted depth retained.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 12 | 0 | 1632.7355450 | 0.010417 | 186.853 | usable; same-kind selection applies |
| 12 | 3 | 1648.8152110 | 0.010417 | 209.905 | usable; same-kind selection applies |
| 93 | 411 | 3835.4179474 | 0.001157 | 226.111 | usable; same-kind selection applies |
| 93 | 413 | 3846.1372029 | 0.001157 | 222.733 | usable; same-kind selection applies |
| 93 | 414 | 3851.4960744 | 0.001157 | 223.445 | usable; same-kind selection applies |
| 104 | 476 | 4183.7692321 | 0.001157 | 185.159 | usable; same-kind selection applies |
| 104 | 477 | 4189.1284814 | 0.001157 | 183.137 | usable; same-kind selection applies |
| 104 | 478 | 4194.4874165 | 0.001157 | 184.678 | usable; same-kind selection applies |
| 104 | 479 | 4199.8470706 | 0.001157 | 183.464 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s39.json, historical/diff_s39.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R239. [Deciding evidence](../../evidence/369118947/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
