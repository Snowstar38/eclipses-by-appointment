# TIC 250562568: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[18, 85]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=4.8539745097 ±0.0000139746d, reference eclipse epoch BTJD1793.7829364, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S18 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation3.867arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.317. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths61.057/62.870/63.120ppt, with 4 stacked events. QLP selected-kind fitted median60.978ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3359013773655012096, P=4.8534475881±0.0003560668d, e=0.073594, omega=200.0311deg. Closest edge-on conjunction offset0.023951d (0.004935phase), full-SB1-covariance linear propagated Gaia uncertainty0.099201d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.128329d (photometric period projection allowance0.004039d). The approximate central duration7.63h vs observed median6.42h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated isolated eclipse; alternative aperture supports target. Depth varies with aperture/dilution.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 18 | 0 | 1793.7825787 | 0.010417 | 61.898 | usable; same-kind selection applies |
| 18 | 1 | 1798.6368853 | 0.010417 | 61.381 | usable; same-kind selection applies |
| 18 | 3 | 1808.3447864 | 0.010417 | 60.687 | usable; same-kind selection applies |
| 18 | 4 | 1813.1987722 | 0.010417 | 61.127 | usable; same-kind selection applies |
| 85 | 375 | 3614.0243173 | 0.001157 | 61.361 | usable; same-kind selection applies |
| 85 | 376 | 3618.8776580 | 0.001157 | 60.830 | usable; same-kind selection applies |
| 85 | 377 | 3623.7301999 | 0.001157 | 57.765 | usable; same-kind selection applies |
| 85 | 379 | 3633.4391631 | 0.001157 | 60.464 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s18.json, historical/diff_s18.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R224. [Deciding evidence](../../evidence/250562568/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
