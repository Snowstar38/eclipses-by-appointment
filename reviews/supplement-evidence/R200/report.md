# TIC 314041837: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 13 distinct eclipse events in selected sectors [17, 77, 85]. The lead inspected the raw-event contact plot and numeric fit output. All fitted windows are preserved, including excluded anomalous windows described below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 13 same-kind midtimes give P=4.4779956510 ±0.0000153414 d, reference primary epoch BTJD 1770.0417343. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S24 deficit peak [7, 7] vs target pixel [7, 7]; deficit-target separation 5.683 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.595. Capable neighbours: Gaia 2013547914676675456: 27.40 arcsec, G 14.937, required fractional eclipse 0.684, pixel fractional loss 0.020156189636425306; Gaia 2013547090042960640: 53.17 arcsec, G 14.840, required fractional eclipse 0.628, pixel fractional loss 0.0038196993836605766
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 30.364/29.166/27.018 ppt, with 6 stacked events. QLP primary fitted median 44.521 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 2013547154462321152, P=4.4771653875±0.0004155553 d, e=0.092195, omega=238.1338 deg. Closest edge-on conjunction offset 0.076024 d (0.016980 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.117104 d at the measured epoch. Near-Gaia-reference projected eclipse offset -0.179697 d (photometric period projection allowance 0.004725 d). The approximate central duration 15.94 h vs median local-model width 18.79 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** The target is a large star (TIC radius 5.09 solar radii) with ellipsoidal modulation plus localized eclipses. A two-harmonic baseline fitted outside the primary core in S77 leaves a 30.31 ppt localized deficit; its double-wave modulation does not explain the eclipse. See harmonic-test.json and png. The 18.79 h local-linear trapezoid width includes smooth variability and is not a physical eclipse duration. The reported depth likewise describes that local model, not intrinsic eclipse depth. Capable neighbours at 27.40 and 53.17 arcsec are away from the target-centered deficit; PSF residual 0.595 limits morphology precision.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 17 | 0 | 1770.0505977 | 0.010873 | 40.728 |
| 17 | 1 | 1774.5159591 | 0.012706 | 42.786 |
| 17 | 3 | 1783.4760001 | 0.014540 | 43.534 |
| 17 | 4 | 1787.9540554 | 0.010417 | 38.134 |
| 77 | 364 | 3400.0271499 | 0.004037 | 46.345 |
| 77 | 365 | 3404.5080948 | 0.004156 | 47.249 |
| 77 | 368 | 3417.9439679 | 0.004058 | 44.492 |
| 77 | 369 | 3422.4211395 | 0.004401 | 44.657 |
| 85 | 412 | 3614.9760782 | 0.004250 | 44.701 |
| 85 | 413 | 3619.4567318 | 0.004025 | 43.943 |
| 85 | 414 | 3623.9446547 | 0.004697 | 46.044 |
| 85 | 415 | 3628.4076451 | 0.004320 | 44.521 |
| 85 | 416 | 3632.8843678 | 0.004183 | 44.619 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s24.json, historical/diff_s24.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R200. [Deciding evidence](../../evidence/314041837/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
