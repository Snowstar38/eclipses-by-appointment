# TIC 445045766: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 6 distinct eclipse events in selected sectors[60, 74]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=5.0364803869 ±0.0000125874d, fitted ephemeris intercept at earliest retained cycle BTJD2939.7678090, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S47 deficit peak[8, 8] vs target pixel[7, 8]; deficit-target separation3.908arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.781. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths23.308/23.874/22.969ppt, with 5 stacked events. QLP selected-kind fitted median25.792ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31040848116886576128, P=5.0364132762±0.0002075065d, e=0.017166, omega=36.3338deg. Closest edge-on conjunction offset0.083686d (0.016616phase), full-SB1-covariance linear propagated Gaia uncertainty0.104481d at the measured epoch. Near-Gaia-reference projected eclipse offset0.049728d (photometric period projection allowance0.006369d). The approximate central duration4.07h vs observed median1.94h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** No capable catalogued neighbor within60arcsec. Deficit0.186pixel from target; three alternative aperture depths23.3-23.9ppt agree.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 60 | 217 | 2939.7669090 | 0.001157 | 21.547 | usable; same-kind selection applies |
| 60 | 218 | 2944.8046715 | 0.001157 | 25.020 | usable; same-kind selection applies |
| 60 | 221 | 2959.9142466 | 0.001157 | 27.232 | usable; same-kind selection applies |
| 74 | 292 | 3317.5049774 | 0.001157 | 26.651 | usable; same-kind selection applies |
| 74 | 293 | 3322.5396657 | 0.001157 | 25.911 | usable; same-kind selection applies |
| 74 | 296 | 3337.6492749 | 0.001157 | 25.674 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s47.json, historical/diff_s47.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R229. [Deciding evidence](../../evidence/445045766/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
