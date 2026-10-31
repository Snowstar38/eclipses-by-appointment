# TIC 334379409: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 15 distinct eclipse events in selected sectors[20, 60, 74]. The lead inspected raw-event plots and numeric fitting summaries. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 15 same-kind midtimes give P=3.9471266750 ±0.0000086262d, reference primary epoch BTJD1846.4992369. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S20 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation2.967arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.052. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths8.815/9.122/9.021ppt, with 6 stacked events. QLP primary fitted median9.703ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31084122553796196608, P=3.9478875756±0.0002427008d, e=0.119742, omega=0.8238deg. Closest edge-on conjunction offset-0.086809d (-0.021989phase), full-SB1-covariance linear propagated Gaia uncertainty0.086629d at the measured epoch. Near-Gaia-reference projected eclipse offset0.193963d (photometric period projection allowance0.003183d). The approximate central duration6.43h vs observed median4.49h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated raw eclipses have modest baseline variability. Gaia period mismatch accumulates over the baseline; propagated covariance and conjunction comparison are descriptive rather than a sigma threshold.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 20 | 0 | 1846.5014050 | 0.010417 | 10.743 |
| 20 | 1 | 1850.4438860 | 0.010417 | 11.272 |
| 20 | 2 | 1854.3929606 | 0.010417 | 9.934 |
| 20 | 3 | 1858.3435270 | 0.010417 | 9.627 |
| 20 | 4 | 1862.2895218 | 0.010417 | 8.704 |
| 20 | 5 | 1866.2346501 | 0.010417 | 8.661 |
| 60 | 277 | 2939.8524606 | 0.006043 | 7.589 |
| 60 | 279 | 2947.7469758 | 0.002563 | 9.703 |
| 60 | 281 | 2955.6437236 | 0.001502 | 10.355 |
| 60 | 282 | 2959.5876637 | 0.001234 | 10.407 |
| 74 | 373 | 3318.7783821 | 0.001812 | 10.675 |
| 74 | 374 | 3322.7236565 | 0.001157 | 9.863 |
| 74 | 375 | 3326.6719807 | 0.001157 | 9.071 |
| 74 | 377 | 3334.5668688 | 0.001731 | 8.592 |
| 74 | 378 | 3338.5135701 | 0.002641 | 8.692 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp/QLP FITS; historical/diff_s20.json, historical/diff_s20.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R188. [Deciding evidence](../../evidence/334379409/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
