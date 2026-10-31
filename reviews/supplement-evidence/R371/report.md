# TIC 74717164: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 12 distinct eclipse events in selected sectors[8, 36, 89]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 12 same-kind midtimes give P=4.7665054846 ±0.0000054999d, reference eclipse epoch BTJD1520.9571959, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S62 deficit peak[7, 8] vs target pixel[7, 7]; deficit-target separation4.426arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.268. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths145.095/137.072/121.642ppt, with 6 stacked predicted windows. QLP selected-kind fitted median161.796ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35427268800062049792, P=4.7669038760±0.0002652066d, e=0.011747, omega=19.5123deg. Closest edge-on conjunction offset-0.096457d (-0.020235phase), full-SB1-covariance linear propagated Gaia uncertainty0.084036d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.002038d (photometric period projection allowance0.001303d). The approximate central duration6.18h vs observed median5.64h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Representative raw eclipses recur. Depths remain diluted and sector dependent; timing errors omit uncalibrated extraction and shape systematics.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 8 | 0 | 1520.9679571 | 0.010417 | 155.437 | included timing center |
| 8 | 1 | 1525.7335383 | 0.010417 | 155.225 | included timing center |
| 8 | 4 | 1540.0331209 | 0.010417 | 153.583 | included timing center |
| 36 | 160 | 2283.5977269 | 0.003472 | 168.836 | included timing center |
| 36 | 161 | 2288.3619604 | 0.003472 | 166.596 | included timing center |
| 36 | 163 | 2297.8960431 | 0.003472 | 167.187 | included timing center |
| 36 | 164 | 2302.6634024 | 0.003472 | 173.439 | included timing center |
| 89 | 462 | 3723.0825840 | 0.001157 | 158.638 | included timing center |
| 89 | 463 | 3727.8499626 | 0.001157 | 161.394 | included timing center |
| 89 | 464 | 3732.6150904 | 0.001157 | 162.197 | included timing center |
| 89 | 465 | 3737.3829364 | 0.001157 | 163.950 | included timing center |
| 89 | 466 | 3742.1483320 | 0.001157 | 158.422 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s62.json, historical/diff_s62.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R371. [Deciding evidence](../../2026-10-31-bright73/evidence/74717164) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/74717164/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/74717164/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/74717164/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch04/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch04/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/74717164/historical/diff_s62.png).
