# TIC 300969635: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 11 distinct eclipse events in selected sectors [1, 37, 98]. The lead inspected representative raw-event plots and numeric fit output; the helper independently audited timing and pixel exceptions. All fitted windows are preserved. Timing includes historical cycles [0, 1, 2, 3, 133, 134, 135, 360, 362, 364, 366]; excluded cycles [] remain in the raw evidence. Fits with midpoint covariance uncertainty larger than the seeded eclipse duration are excluded as unconstrained, not treated as timing measurements. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 retained reference-eclipse midtimes give P=7.4207275328 +/-0.0000078157 d, observed reference eclipse epoch BTJD 1328.2542487. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S33 deficit peak [7, 8] vs target pixel [7, 8]; deficit-target separation 3.496 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.657. Capable neighbours: None within 60 arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 213.987/196.358/182.802 ppt, with 4 stacked events. QLP retained-reference fitted median 217.538 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 5270681477928794752, P=7.4211188474+/-0.0005357254 d, e=0.017042, omega=195.0962 deg. Closest edge-on conjunction offset -0.058560 d (-0.007891 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.073044 d at the measured epoch. Near-Gaia-reference projected eclipse offset -0.008864 d (photometric period projection allowance 0.000993 d). The approximate central duration 4.03 h vs median local-model width 3.20 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep repeated eclipses persist in S1,37,98. Aperture depth changes from about210 to248 ppt; pooled parity depths confound sector coverage and do not establish stable unequal eclipse kinds. Gaia period matches the measured spacing. Intrinsic depth requires dilution modeling.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 1 | 0 | 1328.2517519 | 0.010416 | 217.538 |
| 1 | 1 | 1335.6716155 | 0.010416 | 205.101 |
| 1 | 2 | 1343.1002121 | 0.010416 | 205.799 |
| 1 | 3 | 1350.5195079 | 0.010416 | 217.890 |
| 37 | 133 | 2315.2110898 | 0.003472 | 246.410 |
| 37 | 134 | 2322.6314876 | 0.003472 | 249.660 |
| 37 | 135 | 2330.0523427 | 0.003472 | 248.190 |
| 98 | 360 | 3999.7160415 | 0.001157 | 214.731 |
| 98 | 362 | 4014.5578813 | 0.001157 | 213.837 |
| 98 | 364 | 4029.3988661 | 0.001157 | 219.377 |
| 98 | 366 | 4044.2405950 | 0.001157 | 209.145 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s33.json, historical/diff_s33.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R211. [Deciding evidence](../../evidence/300969635/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
