# TIC 220617848: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 5 distinct eclipse events in selected sectors[32, 33]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=9.9217119096 ±0.0009025586d, reference eclipse epoch BTJD2177.2176816, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S33 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation1.858arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.355. Capable neighbours: Gaia 4802940366659639808: 46.36 arcsec, G15.176, required fractional eclipse0.849
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths33.374/31.962/30.168ppt, with 3 stacked events. QLP selected-kind fitted median36.320ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR34802939984405335936, P=9.9222605876±0.0022063493d, e=0.263062, omega=113.6466deg. Closest edge-on conjunction offset-0.117564d (-0.011849phase), full-SB1-covariance linear propagated Gaia uncertainty0.384956d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.018802d (photometric period projection allowance0.162461d). The approximate central duration3.56h vs observed median2.43h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Representative raw eclipses recur. Depths remain diluted and sector dependent; timing errors omit uncalibrated extraction and shape systematics.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 32 | 74 | 2177.2175890 | 0.003472 | 34.230 | included timing center |
| 32 | 76 | 2197.0613830 | 0.003472 | 32.929 | included timing center |
| 33 | 77 | 2206.9830260 | 0.003472 | 37.543 | included timing center |
| 33 | 78 | 2216.9037423 | 0.003472 | 36.320 | included timing center |
| 33 | 79 | 2226.8266345 | 0.003472 | 37.286 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s33.json, historical/diff_s33.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R353. [Deciding evidence](../../2026-10-31-bright73/evidence/220617848) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/220617848/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/220617848/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/220617848/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch02/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch02/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/220617848/historical/diff_s33.png).
