# TIC 30753325: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[64, 102]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass with disclosed cycle assumptions.** 8 same-kind midtimes give P=3.8144612029 ±0.0000028664d, reference eclipse epoch BTJD3043.2158652, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S37 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.566arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.353. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths58.070/57.472/55.477ppt, with 6 stacked events. Historical outputs are retained as measured pipeline evidence. QLP selected-kind fitted median58.989ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36165669060874249984, P=3.8146327900±0.0002474851d, e=0.061242, omega=70.4217deg. Closest edge-on conjunction offset-0.055060d (-0.014434phase), full-SB1-covariance linear propagated Gaia uncertainty0.155049d at the measured epoch. Near-Gaia-reference projected eclipse offset0.064365d (photometric period projection allowance0.001995d). The approximate central duration4.07h vs observed median2.74h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Clean triangular repeating eclipses, target-centered deficit and no capable catalogued neighbor. Depth changes between sectors; no intrinsic undiluted depth inferred.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 64 | 378 | 3043.2156965 | 0.001157 | 66.336 | usable; same-kind selection applies |
| 64 | 379 | 3047.0303056 | 0.001157 | 63.061 | usable; same-kind selection applies |
| 64 | 380 | 3050.8447263 | 0.001157 | 62.955 | usable; same-kind selection applies |
| 64 | 382 | 3058.4739603 | 0.001157 | 64.027 | usable; same-kind selection applies |
| 102 | 663 | 4130.3376092 | 0.001157 | 54.165 | usable; same-kind selection applies |
| 102 | 664 | 4134.1517113 | 0.001157 | 55.024 | usable; same-kind selection applies |
| 102 | 666 | 4141.7805440 | 0.001157 | 54.718 | usable; same-kind selection applies |
| 102 | 668 | 4149.4095188 | 0.001157 | 54.840 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): ../helper/pixel-identity-audit.json, ../helper/same-sector-refits.json, ../helper/314047448-measured-diff.json, ../helper/48108063-measured-diff.json; measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s37.json, historical/diff_s37.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R255. [Deciding evidence](../../evidence/30753325/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
