# TIC 48108063: PROBABLE

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 10 distinct eclipse events in selected sectors[35, 62, 89]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass with disclosed cycle assumptions.** 10 same-kind midtimes give P=5.7972370881 ±0.0000058204d, reference eclipse epoch BTJD2272.5117326, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: unresolved after check.** Historical S62 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation0.764arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.508. Capable neighbours: Gaia 5439164283215218688: 15.01 arcsec, G11.053, required fractional eclipse0.183, pixel fractional loss0.03502751096712482
4. **Alternative reduction: eclipse recovered with depth discrepancy.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths35.028/31.419/31.304ppt, with 4 stacked events. Historical outputs are retained as measured pipeline evidence. QLP selected-kind fitted median139.304ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35439164283218021888, P=5.7969445240±0.0002979833d, e=0.091414, omega=170.9390deg. Closest edge-on conjunction offset0.077140d (0.013307phase), full-SB1-covariance linear propagated Gaia uncertainty0.096630d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.017943d (photometric period projection allowance0.001892d). The approximate central duration5.41h vs observed median4.53h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep raw eclipses approximately134-143ppt. Independent measured-ephemeris S62 cutout re-extraction gives3x3 core deficit26.5ppt and1x1 32.1ppt; the factor4-5 contrast persists. Dilution and extraction differences are possible, unestablished explanations. Deficit0.036pixel from target vs neighbor0.72pixel favors target, but15arcsec capable neighbor and uncalibrated centroid leave interpretation unresolved.

**Next check:** Resolved eclipse photometry or multi-source PRF localization of this signal.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 35 | 2 | 2272.5102891 | 0.003472 | 139.721 | usable; same-kind selection applies |
| 35 | 3 | 2278.3083799 | 0.003472 | 139.233 | usable; same-kind selection applies |
| 62 | 126 | 2991.3686717 | 0.001157 | 141.236 | usable; same-kind selection applies |
| 62 | 127 | 2997.1668504 | 0.001157 | 140.595 | usable; same-kind selection applies |
| 62 | 128 | 3002.9638159 | 0.001157 | 142.585 | usable; same-kind selection applies |
| 62 | 129 | 3008.7610555 | 0.001157 | 139.374 | usable; same-kind selection applies |
| 89 | 252 | 3721.8212328 | 0.001157 | 133.229 | usable; same-kind selection applies |
| 89 | 253 | 3727.6183945 | 0.001157 | 134.116 | usable; same-kind selection applies |
| 89 | 254 | 3733.4152996 | 0.001157 | 134.076 | usable; same-kind selection applies |
| 89 | 256 | 3745.0095320 | 0.001157 | 134.026 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): ../helper/pixel-identity-audit.json, ../helper/same-sector-refits.json, ../helper/314047448-measured-diff.json, ../helper/48108063-measured-diff.json; measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s62.json, historical/diff_s62.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R256. [Deciding evidence](../../evidence/48108063/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
