# TIC 90285860: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 3 distinct eclipse events in selected sectors[41, 74]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 3 same-kind midtimes give P=18.5945632879 ±0.0000559615d, reference eclipse epoch BTJD2422.5645534, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S41 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation2.713arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.356. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths162.253/156.481/137.458ppt, with 2 stacked predicted windows. QLP selected-kind fitted median178.980ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32025804617486100992, P=18.5977982181±0.0019708206d, e=0.436172, omega=250.9028deg. Closest edge-on conjunction offset-0.451898d (-0.024298phase), full-SB1-covariance linear propagated Gaia uncertainty0.202050d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.099291d (photometric period projection allowance0.006100d). The approximate central duration10.47h vs observed median7.88h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Three measured eclipses include within-sector S41 recurrence, testing long-baseline cycle count. Closest Gaia conjunction offset-0.4519d (-0.0243phase) versus propagated0.2020d is retained as descriptive association tension, without arbitrary sigma veto; updated spectroscopy would test it.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 41 | 0 | 2422.5646616 | 0.003472 | 179.306 | included timing center |
| 41 | 1 | 2441.1590062 | 0.003472 | 178.980 | included timing center |
| 74 | 49 | 3333.6981548 | 0.001157 | 178.305 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s41.json, historical/diff_s41.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R370. [Deciding evidence](../../evidence/90285860/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/90285860/measurements.json), [raw eclipse plots](../../evidence/90285860/raw-events.png), [raw flux windows](../../evidence/90285860/raw-windows.csv), [Gaia geometry](../../analysis/batch04/gaia-geometry.json), [independent audit](../../analysis/batch04/helper-audit.md), [difference image](../../evidence/90285860/historical/diff_s41.png).
