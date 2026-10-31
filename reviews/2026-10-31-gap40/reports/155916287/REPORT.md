# TIC 155916287: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 7 distinct eclipse events in selected sectors [16, 50, 77]. The lead inspected representative raw-event plots and numeric fit output; the helper independently audited timing and pixel exceptions. All fitted windows are preserved. Timing includes historical cycles [0, 1, 2, 3, 154, 156, 275]; excluded cycles [] remain in the raw evidence. Fits with midpoint covariance uncertainty larger than the seeded eclipse duration are excluded as unconstrained, not treated as timing measurements. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 retained reference-eclipse midtimes give P=6.0531543976 +/-0.0000154319 d, observed reference eclipse epoch BTJD 1741.6770525. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S51 deficit peak [7, 7] vs target pixel [7, 7]; deficit-target separation 1.896 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.052. Capable neighbours: None within 60 arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 31.135/30.140/29.786 ppt, with 3 stacked events. QLP retained-reference fitted median 31.520 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 1585947494733568128, P=6.0530078707+/-0.0002180703 d, e=0.153531, omega=253.9761 deg. Closest edge-on conjunction offset -0.054876 d (-0.009066 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.053462 d at the measured epoch. Near-Gaia-reference projected eclipse offset -0.087551 d (photometric period projection allowance 0.003441 d). The approximate central duration 4.41 h vs median local-model width 2.01 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Seven fitted repeats span S16,50,77. Sector-dependent depth variation and long-cadence integration limit intrinsic depth and duration precision.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 16 | 0 | 1741.6795278 | 0.010416 | 26.482 |
| 16 | 1 | 1747.7282520 | 0.010416 | 31.520 |
| 16 | 2 | 1753.7863780 | 0.010416 | 31.298 |
| 16 | 3 | 1759.8364264 | 0.010416 | 27.304 |
| 50 | 154 | 2673.8620683 | 0.003472 | 33.581 |
| 50 | 156 | 2685.9690311 | 0.003472 | 32.193 |
| 77 | 275 | 3406.2945659 | 0.001157 | 33.475 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s51.json, historical/diff_s51.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R206. [Deciding evidence](../../evidence/155916287/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
