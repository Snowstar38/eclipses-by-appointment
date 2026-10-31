# TIC 382631802: PLAUSIBLE

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: recurrence detected; eclipse interpretation insecure.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 28 distinct eclipse events in selected sectors[1, 36, 97]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 28 same-kind midtimes give P=2.5954869623 ±0.0000430249d, reference eclipse epoch BTJD1328.5030929, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Freshly extracted S97 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation4.628arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.460. Capable neighbours: Gaia 5290921322334100480: 48.54 arcsec, G16.282, required fractional eclipse0.564; Gaia 5290921287974360448: 57.75 arcsec, G16.856, required fractional eclipse0.951
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths5.739/5.663/5.407ppt, with 19 stacked predicted windows. QLP selected-kind fitted median8.947ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: unresolved after completed check.** DR35290921356693837568, P=2.5956559888±0.0001178502d, e=0.268983, omega=78.2783deg. Closest edge-on conjunction offset-0.055532d (-0.021394phase), full-SB1-covariance linear propagated Gaia uncertainty0.064915d at the measured epoch. Near-Gaia-reference projected eclipse offset0.005655d (photometric period projection allowance0.015575d). The approximate central duration3.21h vs observed median7.58h exceeds the simple model and remains unresolved; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** PLAUSIBLE: recurring V-shaped dips ride structured variability. No stable sharp contacts or flat-bottomed occultation signature is resolved across representative windows; free trapezoids alone do not distinguish eclipses from pulsation or tidal minima. Eclipse interpretation itself is insecure. Free trapezoid duration median7.58h exceeds approximate central3.21h using TIC radius1.64solar and main-sequence minimum-mass companion. Difference centroid favors target0.220pixel versus capable neighbours2.38/2.67pixel; PSF fractional residual0.46 limits precision. Peak is measured within the central target5x5 box, excluding invalid peripheral cutout pixels; peripheral invalid pixels do not decide attribution. Model durations vary1.58-14.05h, indicating baseline/shape contamination. Timing reduced chi-square about126 requires scatter inflation. Geometry and eclipse identity are unresolved after completed checks; alternative variability and revised radii require testing.

**Next check:** Fit pulsation/background and eclipse jointly; test stellar radii and obtain resolved photometry.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 1 | 0 | 1328.5812055 | 0.010417 | 9.111 | included timing center |
| 1 | 1 | 1331.0120150 | 0.019902 | 8.926 | included timing center |
| 1 | 2 | 1333.6020632 | 0.052052 | 28.663 | included timing center |
| 1 | 3 | 1336.3461388 | 0.011229 | 16.578 | included timing center |
| 1 | 5 | 1341.4693760 | 0.026132 | 13.075 | included timing center |
| 1 | 6 | 1344.0601145 | 0.135325 | 0.960 | included timing center |
| 1 | 7 | 1346.7001347 | 0.010793 | 11.626 | included timing center |
| 1 | 9 | 1351.8802014 | 0.022025 | 12.263 | included timing center |
| 36 | 368 | 2283.6109148 | 0.010744 | 3.464 | included timing center |
| 36 | 369 | 2286.2843727 | 0.008316 | 13.363 | included timing center |
| 36 | 370 | 2288.6786321 | 0.007128 | 12.305 | included timing center |
| 36 | 371 | 2291.4025187 | 0.009587 | 7.672 | included timing center |
| 36 | 373 | 2296.7469743 | 0.015301 | 7.709 | included timing center |
| 36 | 374 | 2299.1663617 | 0.005423 | 7.725 | included timing center |
| 36 | 375 | 2301.9361800 | 0.006910 | 13.205 | included timing center |
| 36 | 376 | 2304.2976439 | 0.018354 | 13.907 | included timing center |
| 97 | 1006 | 3939.5763559 | 0.002833 | 11.292 | included timing center |
| 97 | 1007 | 3942.1418373 | 0.004789 | 5.472 | included timing center |
| 97 | 1008 | 3944.7198978 | 0.002105 | 12.902 | included timing center |
| 97 | 1011 | 3952.4717370 | 0.010255 | 5.919 | included timing center |
| 97 | 1012 | 3955.1845224 | 0.007913 | 7.162 | included timing center |
| 97 | 1013 | 3957.6122346 | 0.007956 | 6.112 | included timing center |
| 97 | 1016 | 3965.5937512 | 0.003300 | 7.595 | included timing center |
| 97 | 1017 | 3968.0753467 | 0.006071 | 8.186 | included timing center |
| 97 | 1018 | 3970.6765769 | 0.009017 | 2.254 | included timing center |
| 97 | 1019 | 3973.3286723 | 0.003551 | 12.547 | included timing center |
| 97 | 1023 | 3983.7445661 | 0.003163 | 8.968 | included timing center |
| 97 | 1024 | 3986.1490173 | 0.005594 | 8.300 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s97.json, historical/diff_s97.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R368. [Deciding evidence](../../2026-10-31-bright73/evidence/382631802) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/382631802/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/382631802/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/382631802/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch04/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch04/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/382631802/historical/diff_s97.png).
