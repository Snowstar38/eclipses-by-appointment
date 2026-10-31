# TIC 279823568: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 11 distinct eclipse events in selected sectors[21, 47]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 same-kind midtimes give P=4.4197074796 ±0.0000283837d, reference eclipse epoch BTJD1873.6000620, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S21 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation5.456arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.069. Capable neighbours: Gaia 1012826405920802560: 45.32 arcsec, G16.425, required fractional eclipse0.927
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths12.160/11.633/11.566ppt, with 6 stacked events. QLP selected-kind fitted median11.191ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31012826204057700608, P=4.4200216973±0.0006874443d, e=0.100927, omega=16.0548deg. Closest edge-on conjunction offset0.027673d (0.006261phase), full-SB1-covariance linear propagated Gaia uncertainty0.264185d at the measured epoch. Near-Gaia-reference projected eclipse offset0.133250d (photometric period projection allowance0.009537d). The approximate central duration5.27h vs observed median5.65h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Representative raw eclipses recur. Depths remain diluted and sector dependent; timing errors omit uncalibrated extraction and shape systematics.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 21 | 0 | 1873.6018611 | 0.010417 | 12.177 | included timing center |
| 21 | 1 | 1878.0207227 | 0.010417 | 10.993 | included timing center |
| 21 | 2 | 1882.4435239 | 0.010417 | 11.191 | included timing center |
| 21 | 3 | 1886.8656536 | 0.010417 | 11.658 | included timing center |
| 21 | 4 | 1891.2653482 | 0.010417 | 12.250 | included timing center |
| 21 | 5 | 1895.6986739 | 0.010417 | 11.354 | included timing center |
| 47 | 160 | 2580.7563940 | 0.004243 | 9.759 | included timing center |
| 47 | 161 | 2585.1713439 | 0.003472 | 10.566 | included timing center |
| 47 | 162 | 2589.5919178 | 0.003472 | 11.485 | included timing center |
| 47 | 164 | 2598.4312080 | 0.003472 | 10.915 | included timing center |
| 47 | 165 | 2602.8529769 | 0.003472 | 10.956 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s21.json, historical/diff_s21.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R351. [Deciding evidence](../../evidence/279823568/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/279823568/measurements.json), [raw eclipse plots](../../evidence/279823568/raw-events.png), [raw flux windows](../../evidence/279823568/raw-windows.csv), [Gaia geometry](../../analysis/batch02/gaia-geometry.json), [independent audit](../../analysis/batch02/helper-audit.md), [difference image](../../evidence/279823568/historical/diff_s21.png).
