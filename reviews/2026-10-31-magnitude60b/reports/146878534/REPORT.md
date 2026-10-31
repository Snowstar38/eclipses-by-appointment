# TIC 146878534: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 6 distinct eclipse events in selected sectors[33, 87]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=8.9801438437 ±0.0000144498d, reference eclipse epoch BTJD2207.2276616, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S33 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation1.872arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.982. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths140.094/127.643/68.760ppt, with 3 stacked events. QLP selected-kind fitted median156.945ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32946122444350678656, P=8.9793296680±0.0004372996d, e=0.037114, omega=168.8437deg. Closest edge-on conjunction offset0.112481d (0.012527phase), full-SB1-covariance linear propagated Gaia uncertainty0.109595d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.051982d (photometric period projection allowance0.002919d). The approximate central duration5.91h vs observed median3.52h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Clean repeated sector33 eclipses150-174ppt; sector87 depths113-277ppt have changing steep baselines/noise. Real morphology and timing recur; apparent depth variability is not established astrophysically. Local-model timing systematics remain.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 33 | 82 | 2207.2276538 | 0.003472 | 163.964 | usable; same-kind selection applies |
| 33 | 83 | 2216.2077107 | 0.003472 | 149.927 | usable; same-kind selection applies |
| 33 | 84 | 2225.1881019 | 0.003472 | 173.500 | usable; same-kind selection applies |
| 87 | 245 | 3670.9896667 | 0.002756 | 127.744 | usable; same-kind selection applies |
| 87 | 246 | 3679.9697552 | 0.002272 | 277.076 | usable; same-kind selection applies |
| 87 | 247 | 3688.9528822 | 0.001768 | 113.176 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s33.json, historical/diff_s33.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R278. [Deciding evidence](../../evidence/146878534/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
