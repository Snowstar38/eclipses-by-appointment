# TIC 370329832: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 5 distinct eclipse events in selected sectors[38, 90]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=9.4634975241 ±0.0000170165d, reference eclipse epoch BTJD2344.0833839, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Unreliable fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S63 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation1.495arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.582. Capable neighbours: Gaia 5219338717319681536: 35.44 arcsec, G15.976, required fractional eclipse0.980; Gaia 5219338511161254272: 38.70 arcsec, G12.998, required fractional eclipse0.084; Gaia 5219340263507912448: 47.07 arcsec, G15.901, required fractional eclipse0.916; Gaia 5219338751679414528: 59.13 arcsec, G15.279, required fractional eclipse0.527
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths22.301/21.219/17.450ppt, with 3 stacked events. Historical event coordinates guide these stacks and are not newly measured midtimes. QLP selected-kind fitted median24.210ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35219338713019999360, P=9.4629554699±0.0011615825d, e=0.014692, omega=346.6392deg. Closest edge-on conjunction offset0.099963d (0.010564phase), full-SB1-covariance linear propagated Gaia uncertainty0.214371d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.012242d (photometric period projection allowance0.003522d). The approximate central duration8.06h vs observed median3.32h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Five measured shallow eclipses include adjacent repeated pairs in sectors38/90, testing period recurrence. Target-deficit0.071pixel vs closest capable neighbor1.86pixels favors target. Sector63 alternative extraction depths22.30/21.22/17.45ppt show dilution. No calibrated localization error.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 38 | 81 | 2344.0836175 | 0.003472 | 24.926 | usable; same-kind selection applies |
| 38 | 82 | 2353.5466544 | 0.003472 | 25.382 | usable; same-kind selection applies |
| 90 | 230 | 3754.1446441 | 0.001157 | 23.211 | usable; same-kind selection applies |
| 90 | 231 | 3763.6076196 | 0.001157 | 24.210 | usable; same-kind selection applies |
| 90 | 232 | 3773.0717732 | 0.001157 | 22.746 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s63.json, historical/diff_s63.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R296. [Deciding evidence](../../2026-10-31-magnitude60b/evidence/370329832) and [catalogue coverage](../../2026-10-31-magnitude60b/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
