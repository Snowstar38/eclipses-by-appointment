# TIC 388052602: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 21 distinct eclipse events in selected sectors[46, 88]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 10 same-kind midtimes give P=4.5139686736 ±0.0000064790d, reference eclipse epoch BTJD2552.6908935, kind: Deeper repeating eclipse; odd half-period cycles. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S46 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation2.269arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.546. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths64.003/63.122/58.832ppt, with 11 stacked events. QLP selected-kind fitted median97.691ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR33147149694307614080, P=4.5134701102±0.0001857166d, e=0.019114, omega=5.4854deg. Closest edge-on conjunction offset0.307071d (0.068034phase), full-SB1-covariance linear propagated Gaia uncertainty0.101429d at the measured epoch. Near-Gaia-reference projected eclipse offset0.068259d (photometric period projection allowance0.003103d). The approximate central duration5.61h vs observed median3.48h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Stable alternating depths establish doubled orbital period. Ten deeper odd historical half-period events alone define ephemeris; historical cutout stack mixes both kinds. Gaia conjunction offset0.307d (0.068phase) exceeds the linear propagated0.101d error, but near-reference projected offset is0.06826d with independently propagated Gaia uncertainty0.02888d (about2.36 descriptive sigma) and the measured period differs from Gaia by0.000499d. Independent helper geometry388.py finds about3.03 descriptive sigma at the observed epoch. These are linear model uncertainties, not calibrated total coverage. Period accumulation explains much of the distant-epoch offset; low-eccentricity omega/periastron are strongly correlated. This association tension is retained without a sigma veto; updated spectroscopy would test it. Mass function0.126solar and approximate central duration5.61h versus observed3.48h admit noncentral binary geometry.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 46 | 469 | 2552.6912073 | 0.003472 | 97.409 | included timing center |
| 46 | 470 | 2554.9481087 | 0.003472 | 42.644 | usable center; excluded opposite eclipse kind |
| 46 | 471 | 2557.2048891 | 0.003472 | 101.314 | included timing center |
| 46 | 472 | 2559.4614116 | 0.003472 | 41.894 | usable center; excluded opposite eclipse kind |
| 46 | 473 | 2561.7189195 | 0.003472 | 100.507 | included timing center |
| 46 | 474 | 2563.9757522 | 0.003472 | 42.439 | usable center; excluded opposite eclipse kind |
| 46 | 476 | 2568.4907964 | 0.003472 | 43.866 | usable center; excluded opposite eclipse kind |
| 46 | 477 | 2570.7464032 | 0.003472 | 100.765 | included timing center |
| 46 | 478 | 2573.0041426 | 0.003472 | 41.961 | usable center; excluded opposite eclipse kind |
| 46 | 479 | 2575.2606474 | 0.003472 | 98.805 | included timing center |
| 46 | 480 | 2577.5170125 | 0.003472 | 44.175 | usable center; excluded opposite eclipse kind |
| 88 | 975 | 3694.7252793 | 0.001157 | 97.972 | included timing center |
| 88 | 976 | 3696.9976478 | 211733.137317 | 36.554 | excluded singular timing fit |
| 88 | 977 | 3699.2388694 | 0.001157 | 93.808 | included timing center |
| 88 | 978 | 3701.4963538 | 0.001157 | 42.496 | usable center; excluded opposite eclipse kind |
| 88 | 979 | 3703.7527191 | 0.001157 | 94.557 | included timing center |
| 88 | 980 | 3706.0094214 | 0.001157 | 40.326 | usable center; excluded opposite eclipse kind |
| 88 | 981 | 3708.2667280 | 0.001157 | 95.139 | included timing center |
| 88 | 982 | 3710.5243085 | 0.001157 | 40.072 | usable center; excluded opposite eclipse kind |
| 88 | 983 | 3712.7809332 | 0.001157 | 94.660 | included timing center |
| 88 | 984 | 3715.0389528 | 0.001157 | 41.521 | usable center; excluded opposite eclipse kind |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s46.json, historical/diff_s46.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R356. [Deciding evidence](../../evidence/388052602/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/388052602/measurements.json), [raw eclipse plots](../../evidence/388052602/raw-events.png), [raw flux windows](../../evidence/388052602/raw-windows.csv), [Gaia geometry](../../analysis/batch02/gaia-geometry.json), [independent audit](../../analysis/batch02/helper-audit.md), [difference image](../../evidence/388052602/historical/diff_s46.png).
