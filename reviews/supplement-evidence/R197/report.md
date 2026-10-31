# TIC 43785616: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 4 distinct eclipse events in selected sectors [5, 32]. The lead inspected the raw-event contact plot and numeric fit output. All fitted windows are preserved, including excluded anomalous windows described below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=17.9111228161 ±0.0001892149 d, reference primary epoch BTJD 1440.8508244. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S5 deficit peak [8, 8] vs target pixel [8, 8]; deficit-target separation 5.190 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.368. Capable neighbours: None within 60 arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 24.513/24.741/24.787 ppt, with 2 stacked events. QLP primary fitted median 23.115 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 3182410104496905344, P=17.9129197903±0.0059901956 d, e=0.050997, omega=88.2029 deg. Closest edge-on conjunction offset -0.515453 d (-0.028776 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.440210 d at the measured epoch. Near-Gaia-reference projected eclipse offset -0.409432 d (photometric period projection allowance 0.011164 d). The approximate central duration 6.54 h vs median local-model width 9.12 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Observed trapezoid duration exceeds a central estimate based on default primary mass and minimum companion mass. That approximate estimate is not an upper bound: stellar properties and inclination are not fitted. Repeated flat-bottomed events and matching period support association; detailed binary modeling remains optional.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 5 | 0 | 1440.8499147 | 0.010417 | 22.553 |
| 5 | 1 | 1458.7628980 | 0.010417 | 22.840 |
| 32 | 41 | 2175.2067735 | 0.003472 | 23.391 |
| 32 | 42 | 2193.1180644 | 0.003472 | 23.422 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s05.json, historical/diff_s05.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R197. [Deciding evidence](../../evidence/43785616/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
