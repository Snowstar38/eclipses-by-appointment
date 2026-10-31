# TIC 375058760: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 9 distinct eclipse events in selected sectors[1, 36, 98]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=7.1293749205 Ã‚+/-0.0000079011d, reference eclipse epoch BTJD1329.2625675, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S97 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.295arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.055. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths392.706/389.647/379.041ppt, with 6 stacked events. QLP selected-kind fitted median393.515ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35478722237683230464, P=7.1284859943Ã‚+/-0.0003946301d, e=0.021598, omega=6.5168deg. Closest edge-on conjunction offset0.175983d (0.024687phase), full-SB1-covariance linear propagated Gaia uncertainty0.072295d at the measured epoch. Near-Gaia-reference projected eclipse offset0.058645d (photometric period projection allowance0.001043d). The approximate central duration5.36h vs observed median4.29h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep repeated V eclipses show sector-dependent morphology and fitted depths; raw baseline/shape systematics remain and fitted depths are diluted. No detailed binary characterization claimed.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 1 | 0 | 1329.2624358 | 0.010417 | 400.217 | used in ephemeris |
| 1 | 1 | 1336.3942674 | 0.010417 | 347.800 | used in ephemeris |
| 1 | 3 | 1350.6505991 | 0.010417 | 386.813 | used in ephemeris |
| 36 | 134 | 2284.5987869 | 0.003472 | 424.631 | used in ephemeris |
| 36 | 135 | 2291.7281639 | 0.003472 | 419.137 | used in ephemeris |
| 36 | 136 | 2298.8572551 | 0.003472 | 417.119 | used in ephemeris |
| 98 | 375 | 4002.7712239 | 42631.591806 | 369.645 | Singular or unidentifiable center covariance: formal timing uncertainty exceeds search duration; excluded from ephemeris. |
| 98 | 379 | 4031.2953609 | 0.001157 | 372.982 | used in ephemeris |
| 98 | 381 | 4045.5547256 | 0.001157 | 367.255 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s97.json, historical/diff_s97.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R361. [Deciding evidence](../../evidence/375058760/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/375058760/measurements.json), [raw eclipse plots](../../evidence/375058760/raw-events.png), [raw flux windows](../../evidence/375058760/raw-windows.csv), [Gaia geometry](../../analysis/batch03/gaia-geometry.json), [independent audit](../../analysis/batch03/helper-audit.md), [difference image](../../evidence/375058760/historical/diff_s97.png).
