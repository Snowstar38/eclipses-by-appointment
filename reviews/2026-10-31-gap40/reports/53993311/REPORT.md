# TIC 53993311: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 4 distinct eclipse events in selected sectors [68, 95]. The lead inspected the raw-event contact plot and numeric fit output. All fitted windows are preserved, including excluded anomalous windows described below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=14.5428334094 ±0.0000231439 d, reference primary epoch BTJD 3157.6706598. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S28 deficit peak [7, 7] vs target pixel [7, 7]; deficit-target separation 1.428 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.035. Capable neighbours: None within 60 arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 102.900/102.856/101.894 ppt, with 2 stacked events. QLP primary fitted median 97.186 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 6812467324352893952, P=14.5383792659±0.0050945887 d, e=0.043960, omega=139.8471 deg. Closest edge-on conjunction offset 0.707888 d (0.048691 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.958534 d at the measured epoch. Near-Gaia-reference projected eclipse offset -0.138399 d (photometric period projection allowance 0.004397 d). The approximate central duration 8.24 h vs median local-model width 7.11 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Aperture-dependent primary depth changes from about 107 ppt in S68 to 85 ppt in S95; the same localized eclipse morphology repeats. Gaia conjunction uncertainty is substantial; a phase offset alone is not a veto.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 68 | 125 | 3157.6707302 | 0.001157 | 107.223 |
| 68 | 126 | 3172.2134177 | 0.001157 | 106.957 |
| 95 | 175 | 3884.8125205 | 0.001157 | 87.415 |
| 95 | 176 | 3899.3549786 | 0.001157 | 84.684 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s28.json, historical/diff_s28.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R196. [Deciding evidence](../../evidence/53993311/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
