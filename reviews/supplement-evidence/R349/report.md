# TIC 256260982: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 16 distinct eclipse events in selected sectors[26, 53, 80]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 16 same-kind midtimes give P=3.2856228182 ±0.0000056568d, reference eclipse epoch BTJD2031.8784385, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S40 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation3.022arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.197. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths145.050/142.465/141.179ppt, with 5 stacked events. QLP selected-kind fitted median173.195ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR34525405726089981184, P=3.2853698535±0.0001679014d, e=0.050016, omega=131.5130deg. Closest edge-on conjunction offset0.076348d (0.023239phase), full-SB1-covariance linear propagated Gaia uncertainty0.114725d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.050134d (photometric period projection allowance0.002828d). The approximate central duration4.50h vs observed median4.07h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Representative raw eclipses recur. Depths remain diluted and sector dependent; timing errors omit uncalibrated extraction and shape systematics.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 26 | 6 | 2031.8797815 | 0.010417 | 164.255 | included timing center |
| 53 | 223 | 2744.8581590 | 0.003472 | 173.594 | included timing center |
| 53 | 224 | 2748.1451904 | 0.003472 | 174.773 | included timing center |
| 53 | 225 | 2751.4291247 | 0.003472 | 173.172 | included timing center |
| 53 | 226 | 2754.7158517 | 0.003472 | 173.711 | included timing center |
| 53 | 227 | 2758.0007849 | 0.003472 | 173.170 | included timing center |
| 53 | 228 | 2761.2862405 | 0.003472 | 173.218 | included timing center |
| 53 | 229 | 2764.5725357 | 0.003472 | 174.577 | included timing center |
| 53 | 230 | 2767.8578561 | 0.003472 | 174.542 | included timing center |
| 80 | 447 | 3480.8381873 | 0.001157 | 173.873 | included timing center |
| 80 | 448 | 3484.1238251 | 0.001157 | 173.308 | included timing center |
| 80 | 450 | 3490.6955204 | 0.001157 | 156.268 | included timing center |
| 80 | 451 | 3493.9806597 | 0.001157 | 170.559 | included timing center |
| 80 | 452 | 3497.2661390 | 0.001157 | 171.073 | included timing center |
| 80 | 453 | 3500.5514003 | 0.001157 | 169.957 | included timing center |
| 80 | 454 | 3503.8372006 | 0.001157 | 157.425 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s40.json, historical/diff_s40.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R349. [Deciding evidence](../../2026-10-31-bright73/evidence/256260982) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/256260982/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/256260982/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/256260982/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch02/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch02/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/256260982/historical/diff_s40.png).
