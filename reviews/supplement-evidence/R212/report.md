# TIC 317800184: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 18 distinct eclipse events in selected sectors [6, 87, 98]. The lead inspected representative raw-event plots and numeric fit output; the helper independently audited timing and pixel exceptions. All fitted windows are preserved. Timing includes historical cycles [1, 2, 3, 4, 595, 596, 597, 598, 599, 600, 601, 685, 688, 689, 692, 693, 696, 697]; excluded cycles [] remain in the raw evidence. Fits with midpoint covariance uncertainty larger than the seeded eclipse duration are excluded as unconstrained, not treated as timing measurements. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 18 retained reference-eclipse midtimes give P=3.6897809447 +/-0.0000051256 d, observed reference eclipse epoch BTJD 1475.6552350. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S33 deficit peak [8, 7] vs target pixel [8, 7]; deficit-target separation 1.572 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.114. Capable neighbours: Gaia 2992486788106386560: 5.80 arcsec, G 12.206, required fractional eclipse 0.143, pixel fractional loss 0.031893555945530914
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 31.894/33.228/32.967 ppt, with 7 stacked events. QLP retained-reference fitted median 50.474 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 2992486788106386688, P=3.6896677330+/-0.0001218264 d, e=0.023021, omega=7.7054 deg. Closest edge-on conjunction offset 0.055950 d (0.015164 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.048574 d at the measured epoch. Near-Gaia-reference projected eclipse offset 0.022552 d (photometric period projection allowance 0.001512 d). The approximate central duration 3.92 h vs median local-model width 2.36 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated eclipses span S6,87,98 with sector-dependent depths around45-62 ppt. This limits precision but does not erase the localized repeat pattern.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 6 | 1 | 1475.6533405 | 0.010417 | 52.985 |
| 6 | 2 | 1479.3433976 | 0.010417 | 53.165 |
| 6 | 3 | 1483.0328064 | 0.010417 | 47.963 |
| 6 | 4 | 1486.7242234 | 0.010417 | 47.055 |
| 87 | 595 | 3667.3857385 | 0.001157 | 60.383 |
| 87 | 596 | 3671.0754940 | 0.001157 | 58.933 |
| 87 | 597 | 3674.7646548 | 0.001157 | 59.681 |
| 87 | 598 | 3678.4540912 | 0.001157 | 59.934 |
| 87 | 599 | 3682.1435828 | 0.001157 | 60.547 |
| 87 | 600 | 3685.8343756 | 0.001157 | 60.010 |
| 87 | 601 | 3689.5238421 | 0.001157 | 62.675 |
| 98 | 685 | 3999.4650514 | 0.001157 | 45.118 |
| 98 | 688 | 4010.5343533 | 0.001157 | 45.059 |
| 98 | 689 | 4014.2244778 | 0.001157 | 44.129 |
| 98 | 692 | 4025.2938535 | 0.001157 | 44.760 |
| 98 | 693 | 4028.9834465 | 0.001157 | 45.655 |
| 98 | 696 | 4040.0533295 | 0.001157 | 45.957 |
| 98 | 697 | 4043.7429454 | 0.001157 | 46.813 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s33.json, historical/diff_s33.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R212. [Deciding evidence](../../evidence/317800184/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
