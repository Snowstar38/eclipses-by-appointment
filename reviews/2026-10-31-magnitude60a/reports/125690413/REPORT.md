# TIC 125690413: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 18 distinct eclipse events in selected sectors[15, 41, 55]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 18 same-kind midtimes give P=3.6868965634 ±0.0000323523d, fitted ephemeris intercept at earliest retained cycle BTJD1712.7815721, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S41 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation7.799arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.454. Capable neighbours: Gaia 1841055774590654720: 24.35 arcsec, G15.751, required fractional eclipse0.759, pixel fractional loss0.016480613631840144; Gaia 1841055770295761664: 42.81 arcsec, G15.802, required fractional eclipse0.795, pixel fractional loss0.004229247182978673; Gaia 1841055740230914688: 50.54 arcsec, G15.518, required fractional eclipse0.617, pixel fractional loss0.0027038765085001747
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths22.331/22.134/21.692ppt, with 7 stacked events. QLP selected-kind fitted median21.909ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31841056496145163776, P=3.6869823318±0.0002444206d, e=0.064161, omega=270.3731deg. Closest edge-on conjunction offset-0.058793d (-0.015946phase), full-SB1-covariance linear propagated Gaia uncertainty0.075668d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.028002d (photometric period projection allowance0.011614d). The approximate central duration8.23h vs observed median4.44h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Structured sector41 baseline gives broad34ppt cycle196, residual -0.038d and reduced chi square5.25. Retained event and inflated covariance document this; clean22ppt repeats occur in sectors15/55. Capable neighbors are24.35arcsec or farther,1.55pixel or farther from deficit vs0.371pixel target. Timing errors are not total uncertainty.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 15 | 0 | 1712.7861357 | 0.010417 | 21.906 | usable; same-kind selection applies |
| 15 | 1 | 1716.4713407 | 0.010417 | 21.202 | usable; same-kind selection applies |
| 15 | 4 | 1727.5374256 | 0.010417 | 21.256 | usable; same-kind selection applies |
| 15 | 5 | 1731.2263891 | 0.010417 | 21.295 | usable; same-kind selection applies |
| 41 | 192 | 2420.6701880 | 0.003472 | 22.428 | usable; same-kind selection applies |
| 41 | 193 | 2424.3549531 | 0.003472 | 23.614 | usable; same-kind selection applies |
| 41 | 194 | 2428.0444513 | 0.003472 | 22.786 | usable; same-kind selection applies |
| 41 | 195 | 2431.7296216 | 0.003472 | 22.501 | usable; same-kind selection applies |
| 41 | 196 | 2435.3752955 | 0.004378 | 33.997 | usable; same-kind selection applies |
| 41 | 197 | 2439.0933329 | 0.007020 | 20.348 | usable; same-kind selection applies |
| 41 | 198 | 2442.7891347 | 0.003607 | 16.274 | usable; same-kind selection applies |
| 55 | 295 | 2800.4166636 | 0.003472 | 21.750 | usable; same-kind selection applies |
| 55 | 296 | 2804.1036165 | 0.003472 | 22.065 | usable; same-kind selection applies |
| 55 | 297 | 2807.7905523 | 0.003472 | 22.439 | usable; same-kind selection applies |
| 55 | 298 | 2811.4786764 | 0.003472 | 22.534 | usable; same-kind selection applies |
| 55 | 299 | 2815.1641441 | 0.003472 | 21.911 | usable; same-kind selection applies |
| 55 | 300 | 2818.8511683 | 0.003472 | 21.302 | usable; same-kind selection applies |
| 55 | 301 | 2822.5382277 | 0.003472 | 21.720 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s41.json, historical/diff_s41.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.

Timing sensitivity: omitting the complete structured-baseline sector41 gives P=3.6868774377158258d, only -0.00001913d from the adopted all-event ephemeris. See timing-sensitivity.json; this is a robustness diagnostic, not the adopted precision estimate.


Stable review key: R228. [Deciding evidence](../../evidence/125690413/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
