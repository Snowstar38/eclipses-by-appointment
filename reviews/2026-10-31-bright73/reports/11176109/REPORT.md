# TIC 11176109: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 13 distinct eclipse events in selected sectors[7, 61, 88]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 13 same-kind midtimes give P=5.0191531715 ±0.0000048262d, reference eclipse epoch BTJD1501.3234240, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S61 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation2.987arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.565. Capable neighbours: Gaia 5713502188219216384: 16.97 arcsec, G13.638, required fractional eclipse0.762; Gaia 5713502089440751232: 35.79 arcsec, G12.303, required fractional eclipse0.300; Gaia 5713501917642055808: 59.41 arcsec, G13.219, required fractional eclipse0.553
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths100.668/77.592/55.934ppt, with 4 stacked events. QLP selected-kind fitted median110.415ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35713502123800311168, P=5.0189270961±0.0003204633d, e=0.059916, omega=184.1156deg. Closest edge-on conjunction offset-0.004499d (-0.000896phase), full-SB1-covariance linear propagated Gaia uncertainty0.078599d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.054687d (photometric period projection allowance0.001071d). The approximate central duration4.36h vs observed median3.88h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep repeated eclipses. Target0.142pixel from deficit versus nearest capable neighbor0.722pixel, which would require76percent intrinsic loss. Target favored by concentrated deficit core, without calibrated localization uncertainty.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 7 | 1 | 1501.3270834 | 0.010417 | 104.159 | included timing center |
| 7 | 2 | 1506.3445659 | 0.010417 | 106.386 | included timing center |
| 7 | 3 | 1511.3629019 | 0.010417 | 103.604 | included timing center |
| 61 | 293 | 2966.9158740 | 0.001157 | 116.171 | included timing center |
| 61 | 294 | 2971.9353564 | 0.001157 | 114.964 | included timing center |
| 61 | 295 | 2976.9542299 | 0.001157 | 114.557 | included timing center |
| 61 | 296 | 2981.9734669 | 0.001157 | 117.137 | included timing center |
| 61 | 297 | 2986.9931061 | 0.001157 | 115.291 | included timing center |
| 88 | 438 | 3694.6934857 | 0.001157 | 110.545 | included timing center |
| 88 | 439 | 3699.7126828 | 0.001157 | 110.415 | included timing center |
| 88 | 440 | 3704.7314124 | 0.001157 | 110.272 | included timing center |
| 88 | 441 | 3709.7508639 | 0.001157 | 109.855 | included timing center |
| 88 | 442 | 3714.7700513 | 0.001157 | 109.738 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s61.json, historical/diff_s61.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R350. [Deciding evidence](../../evidence/11176109/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/11176109/measurements.json), [raw eclipse plots](../../evidence/11176109/raw-events.png), [raw flux windows](../../evidence/11176109/raw-windows.csv), [Gaia geometry](../../analysis/batch02/gaia-geometry.json), [independent audit](../../analysis/batch02/helper-audit.md), [difference image](../../evidence/11176109/historical/diff_s61.png).
