# TIC 146463944: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 9 distinct eclipse events in selected sectors[5, 32, 98]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 9 same-kind midtimes give P=6.9896922117 ±0.0000074444d, reference eclipse epoch BTJD1444.7562858, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S98 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation4.021arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.054. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths274.775/272.253/263.827ppt, with 5 stacked predicted windows. QLP selected-kind fitted median246.336ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32975084645776224896, P=6.9895742942±0.0002845635d, e=0.112660, omega=95.4246deg. Closest edge-on conjunction offset0.031213d (0.004466phase), full-SB1-covariance linear propagated Gaia uncertainty0.056178d at the measured epoch. Near-Gaia-reference projected eclipse offset0.013407d (photometric period projection allowance0.001124d). The approximate central duration5.62h vs observed median4.39h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Representative raw eclipses recur. Depths remain diluted and sector dependent; timing errors omit uncalibrated extraction and shape systematics.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 5 | 0 | 1444.7556265 | 0.010417 | 231.789 | included timing center |
| 5 | 2 | 1458.7347272 | 0.010417 | 232.438 | included timing center |
| 32 | 105 | 2178.6739255 | 0.003472 | 273.968 | included timing center |
| 32 | 107 | 2192.6533520 | 0.003472 | 274.285 | included timing center |
| 32 | 108 | 2199.6432936 | 0.003472 | 274.127 | included timing center |
| 98 | 365 | 3995.9942097 | 0.001157 | 241.859 | included timing center |
| 98 | 369 | 4023.9526829 | 0.001157 | 244.863 | included timing center |
| 98 | 370 | 4030.9421693 | 0.001157 | 246.336 | included timing center |
| 98 | 372 | 4044.9217827 | 0.001157 | 246.361 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s98.json, historical/diff_s98.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R374. [Deciding evidence](../../evidence/146463944/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/146463944/measurements.json), [raw eclipse plots](../../evidence/146463944/raw-events.png), [raw flux windows](../../evidence/146463944/raw-windows.csv), [Gaia geometry](../../analysis/batch04/gaia-geometry.json), [independent audit](../../analysis/batch04/helper-audit.md), [difference image](../../evidence/146463944/historical/diff_s98.png).
