# TIC 134193638: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 15 distinct eclipse events in selected sectors[6, 34, 88]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 15 same-kind midtimes give P=4.0538858989 ±0.0000171546d, reference eclipse epoch BTJD1476.1660599, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S87 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation1.286arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.191. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths30.037/30.552/28.579ppt, with 5 stacked predicted windows. QLP selected-kind fitted median31.643ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35559345130381927424, P=4.0539744870±0.0004631847d, e=0.084801, omega=205.8049deg. Closest edge-on conjunction offset-0.087266d (-0.021526phase), full-SB1-covariance linear propagated Gaia uncertainty0.124551d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.063525d (photometric period projection allowance0.004597d). The approximate central duration9.97h vs observed median5.67h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated sharp raw eclipses coexist with strong oscillatory variability, especially sectors34/88. Free trapezoids can absorb background oscillation; timing reduced chi-square about9 is scatter inflated and uncalibrated shape/baseline systematics remain.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 6 | 1 | 1476.1598733 | 0.016060 | 30.617 | included timing center |
| 6 | 2 | 1480.2272868 | 0.010417 | 39.105 | included timing center |
| 6 | 3 | 1484.2785717 | 0.010709 | 32.524 | included timing center |
| 6 | 4 | 1488.3313258 | 0.010417 | 29.815 | included timing center |
| 34 | 187 | 2230.1775933 | 0.005450 | 31.891 | included timing center |
| 34 | 188 | 2234.2403065 | 0.005115 | 69.739 | included timing center |
| 34 | 189 | 2238.3028897 | 0.004174 | 31.095 | included timing center |
| 34 | 191 | 2246.3996140 | 0.004258 | 40.017 | included timing center |
| 34 | 192 | 2250.4613313 | 0.004077 | 30.993 | included timing center |
| 88 | 548 | 3693.6609777 | 0.002936 | 30.594 | included timing center |
| 88 | 549 | 3697.6724459 | 0.003413 | 30.702 | included timing center |
| 88 | 550 | 3701.7507853 | 0.002321 | 51.107 | included timing center |
| 88 | 551 | 3705.8086631 | 0.002312 | 30.201 | included timing center |
| 88 | 552 | 3709.8482450 | 0.002514 | 31.643 | included timing center |
| 88 | 553 | 3713.9103364 | 0.004836 | 41.788 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s87.json, historical/diff_s87.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R372. [Deciding evidence](../../evidence/134193638/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/134193638/measurements.json), [raw eclipse plots](../../evidence/134193638/raw-events.png), [raw flux windows](../../evidence/134193638/raw-windows.csv), [Gaia geometry](../../analysis/batch04/gaia-geometry.json), [independent audit](../../analysis/batch04/helper-audit.md), [difference image](../../evidence/134193638/historical/diff_s87.png).
