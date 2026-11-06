# TIC 233462817: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 4 distinct eclipse events in selected sectors[49, 77]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=10.1615169478 ±0.0000405203d, reference eclipse epoch BTJD2644.8490471, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S49 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation11.160arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.554. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths3.174/2.700/2.949ppt, with 2 stacked events. QLP selected-kind fitted median3.817ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31512692949146107520, P=10.1598188069±0.0010289917d, e=0.023474, omega=64.8980deg. Closest edge-on conjunction offset0.416191d (0.040964phase), full-SB1-covariance linear propagated Gaia uncertainty0.245151d at the measured epoch. Near-Gaia-reference projected eclipse offset0.039204d (photometric period projection allowance0.008996d). The approximate central duration5.89h vs observed median1.49h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Shallow repeated raw eclipses in sectors49/77; no capable listed neighbor. Deficit centroid0.53pixel offset and noisy difference image limit precise localization. Gaia conjunction offset0.041phase is interpreted with full covariance (0.245d), short observed duration allowing noncentral geometry; no arbitrary sigma veto.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 49 | 91 | 2644.8459518 | 0.003472 | 3.330 | used in ephemeris |
| 49 | 92 | 2655.0137168 | 0.003472 | 3.268 | used in ephemeris |
| 77 | 165 | 3396.8006857 | 0.002535 | 4.305 | used in ephemeris |
| 77 | 166 | 3406.9633220 | 0.002353 | 5.197 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s49.json, historical/diff_s49.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R358. [Deciding evidence](../../evidence/233462817/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/233462817/measurements.json), [raw eclipse plots](../../evidence/233462817/raw-events.png), [raw flux windows](../../evidence/233462817/raw-windows.csv), [Gaia geometry](../../analysis/batch03/gaia-geometry.json), [independent audit](../../analysis/batch03/helper-audit.md), [difference image](../../evidence/233462817/historical/diff_s49.png).
