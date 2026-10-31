# TIC 239572145: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 17 distinct eclipse events in selected sectors[15, 55, 82]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=6.3129271986 ±0.0000162239d, reference eclipse epoch BTJD1714.9544368, kind: Deeper eclipse; even historical half-period cycles. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S55 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation1.430arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.792. Capable neighbours: Gaia 1852594221418982144: 28.33 arcsec, G13.286, required fractional eclipse0.278
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths98.238/86.360/78.576ppt, with 8 stacked predicted windows. QLP selected-kind fitted median150.972ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31852594255778719488, P=6.3125426224±0.0003139626d, e=0.044112, omega=17.4791deg. Closest edge-on conjunction offset0.190656d (0.030203phase), full-SB1-covariance linear propagated Gaia uncertainty0.071723d at the measured epoch. Near-Gaia-reference projected eclipse offset0.109895d (photometric period projection allowance0.003407d). The approximate central duration6.77h vs observed median5.69h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Stable alternating depths near150/55ppt establish doubled orbital period; six deeper even historical half-period events define ephemeris. Historical pixel stack mixes both eclipse kinds; concentrated target deficit supports localization. Closest Gaia conjunction offset+0.1907d (0.0302phase) versus linear covariance0.0717d is retained as descriptive association tension without arbitrary sigma veto.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 15 | -1 | 1711.7928386 | 0.010417 | 56.617 | usable center; excluded opposite eclipse kind |
| 15 | 0 | 1714.9504919 | 0.010417 | 152.615 | included timing center |
| 15 | 1 | 1718.1060346 | 0.010417 | 57.330 | usable center; excluded opposite eclipse kind |
| 15 | 4 | 1727.5767403 | 0.010417 | 151.458 | included timing center |
| 15 | 5 | 1730.7318327 | 0.010417 | 58.018 | usable center; excluded opposite eclipse kind |
| 55 | 343 | 2797.6227382 | 0.003472 | 55.933 | usable center; excluded opposite eclipse kind |
| 55 | 344 | 2800.7784811 | 0.003472 | 150.485 | included timing center |
| 55 | 345 | 2803.9352346 | 0.003472 | 54.691 | usable center; excluded opposite eclipse kind |
| 55 | 348 | 2813.4047013 | 0.003472 | 149.223 | included timing center |
| 55 | 349 | 2816.5592973 | 0.003472 | 55.697 | usable center; excluded opposite eclipse kind |
| 55 | 350 | 2819.7172580 | 0.003472 | 150.059 | included timing center |
| 82 | 577 | 3536.2338340 | 0.001157 | 54.913 | usable center; excluded opposite eclipse kind |
| 82 | 579 | 3542.5461712 | 0.001157 | 54.741 | usable center; excluded opposite eclipse kind |
| 82 | 580 | 3545.7118361 | 121226.206053 | 147.482 | excluded singular timing fit |
| 82 | 581 | 3548.8590316 | 0.001157 | 54.329 | usable center; excluded opposite eclipse kind |
| 82 | 582 | 3552.0161153 | 0.001157 | 151.477 | included timing center |
| 82 | 583 | 3555.1726501 | 0.001157 | 55.813 | usable center; excluded opposite eclipse kind |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s55.json, historical/diff_s55.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R369. [Deciding evidence](../../evidence/239572145/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/239572145/measurements.json), [raw eclipse plots](../../evidence/239572145/raw-events.png), [raw flux windows](../../evidence/239572145/raw-windows.csv), [Gaia geometry](../../analysis/batch04/gaia-geometry.json), [independent audit](../../analysis/batch04/helper-audit.md), [difference image](../../evidence/239572145/historical/diff_s55.png).
