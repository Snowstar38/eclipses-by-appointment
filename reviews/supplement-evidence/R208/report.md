# TIC 436724968: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 23 distinct eclipse events in selected sectors [43, 44, 71]. The lead inspected representative raw-event plots and numeric fit output; the helper independently audited timing and pixel exceptions. All fitted windows are preserved. Timing includes historical cycles [0, 1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 279, 280, 281, 282, 284, 285, 286, 287]; excluded cycles [] remain in the raw evidence. Fits with midpoint covariance uncertainty larger than the seeded eclipse duration are excluded as unconstrained, not treated as timing measurements. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 23 retained reference-eclipse midtimes give P=2.7321550784 +/-0.0000037340 d, observed reference eclipse epoch BTJD 2475.2746864. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S43 deficit peak [7, 7] vs target pixel [7, 7]; deficit-target separation 5.654 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.458. Capable neighbours: Gaia 3405581312479002624: 35.19 arcsec, G 13.629, required fractional eclipse 0.317, pixel fractional loss 0.007404879626139636; Gaia 3405581308183975552: 35.89 arcsec, G 12.381, required fractional eclipse 0.130, pixel fractional loss 0.007404879626139636
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 41.459/36.665/28.902 ppt, with 8 stacked events. QLP retained-reference fitted median 48.530 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 3405581312480317184, P=2.7321672331+/-0.0000779633 d, e=0.019821, omega=313.1687 deg. Closest edge-on conjunction offset 0.004140 d (0.001515 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.059868 d at the measured epoch. Near-Gaia-reference projected eclipse offset 0.013426 d (photometric period projection allowance 0.002853 d). The approximate central duration 5.02 h vs median local-model width 2.87 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** QLP free-trapezoid depths show modest parity differences, especially in S71; local baseline and aperture dependence are material. Independent S43 3x3 cutout depths are 35.34-37.19 ppt for eight events including consecutive odd/even cycles, without a stable unequal alternating pattern. Gaia P=2.732167 d matches the measured event spacing. These data do not establish two distinct alternating eclipse kinds or require doubling; report the fitted period as the adopted orbit with this depth-model limitation, and the epoch as an observed reference eclipse. Capable neighbours at 35.19 and 35.89 arcsec are displaced from the compact target deficit.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 43 | 0 | 2475.2741855 | 0.003473 | 45.540 |
| 43 | 1 | 2478.0091335 | 0.003473 | 46.144 |
| 43 | 2 | 2480.7380468 | 0.003473 | 46.271 |
| 43 | 3 | 2483.4711931 | 0.003473 | 51.031 |
| 43 | 5 | 2488.9354834 | 0.005180 | 56.709 |
| 43 | 6 | 2491.6677576 | 0.003473 | 43.820 |
| 43 | 7 | 2494.4004403 | 0.003473 | 52.132 |
| 43 | 8 | 2497.1318516 | 0.003473 | 44.343 |
| 44 | 10 | 2502.5986040 | 0.003472 | 36.783 |
| 44 | 11 | 2505.3280294 | 0.003472 | 53.445 |
| 44 | 12 | 2508.0599929 | 0.003472 | 48.530 |
| 44 | 13 | 2510.7935035 | 0.003472 | 53.573 |
| 44 | 15 | 2516.2490143 | 0.004992 | 28.983 |
| 44 | 16 | 2518.9893760 | 0.003472 | 46.577 |
| 44 | 17 | 2521.7205393 | 0.003472 | 50.893 |
| 71 | 279 | 3237.5472987 | 0.001157 | 54.328 |
| 71 | 280 | 3240.2773799 | 0.001157 | 52.383 |
| 71 | 281 | 3243.0098666 | 0.001157 | 54.169 |
| 71 | 282 | 3245.7436936 | 0.001157 | 40.113 |
| 71 | 284 | 3251.2066756 | 0.001157 | 46.589 |
| 71 | 285 | 3253.9408093 | 0.001157 | 53.815 |
| 71 | 286 | 3256.6730068 | 0.002426 | 41.251 |
| 71 | 287 | 3259.3994417 | 0.001157 | 53.084 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s43.json, historical/diff_s43.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R208. [Deciding evidence](../../evidence/436724968/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
