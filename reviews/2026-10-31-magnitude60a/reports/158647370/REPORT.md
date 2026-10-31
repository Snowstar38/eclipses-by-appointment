# TIC 158647370: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 6 distinct eclipse events in selected sectors[69, 104]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=6.0132323218 ±0.0000060378d, fitted ephemeris intercept at earliest retained cycle BTJD3189.6585657, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S29 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation3.428arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.024. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths87.134/86.012/85.155ppt, with 5 stacked events. QLP selected-kind fitted median85.396ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR34916321559038719488, P=6.0135821955±0.0002440543d, e=0.037327, omega=306.8532deg. Closest edge-on conjunction offset-0.114751d (-0.019082phase), full-SB1-covariance linear propagated Gaia uncertainty0.124315d at the measured epoch. Near-Gaia-reference projected eclipse offset0.048291d (photometric period projection allowance0.002814d). The approximate central duration5.66h vs observed median3.38h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** No capable catalogued neighbor. Approximately85-95ppt eclipses repeat; custom aperture depths85-87ppt agree.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 69 | 305 | 3189.6587472 | 0.001157 | 94.880 | usable; same-kind selection applies |
| 69 | 306 | 3195.6716091 | 0.001157 | 94.455 | usable; same-kind selection applies |
| 104 | 470 | 4181.8423089 | 0.001157 | 85.271 | usable; same-kind selection applies |
| 104 | 471 | 4187.8552064 | 0.001157 | 84.760 | usable; same-kind selection applies |
| 104 | 472 | 4193.8680622 | 0.001157 | 85.521 | usable; same-kind selection applies |
| 104 | 473 | 4199.8814193 | 0.001157 | 84.317 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s29.json, historical/diff_s29.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R232. [Deciding evidence](../../evidence/158647370/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
