# TIC 416646907: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 20 distinct eclipse events in selected sectors[31, 44, 71]. The lead inspected raw-event plots and numeric fitting summaries. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 same-kind midtimes give P=6.3843147555 ±0.0000100738d, reference primary epoch BTJD2144.9943337. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S31 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation2.764arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.051. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths14.805/15.334/15.238ppt, with 7 stacked events. QLP primary fitted median17.963ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR310938731947598464, P=6.3841880821±0.0003343665d, e=0.019823, omega=261.1834deg. Closest edge-on conjunction offset0.040618d (0.006362phase), full-SB1-covariance linear propagated Gaia uncertainty0.082376d at the measured epoch. Near-Gaia-reference projected eclipse offset0.005783d (photometric period projection allowance0.002770d). The approximate central duration9.19h vs observed median3.56h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Odd historical half-period cycles are deeper in each of three sectors (about18 versus16ppt); deeper odd cycles alone give the primary ephemeris and doubled orbital period. Alternative-reduction stack mixes eclipse kinds. Approximate central duration permits a noncentral chord.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 31 | -1 | 2144.9968313 | 0.003472 | 18.270 |
| 31 | 0 | 2148.1875462 | 0.003472 | 15.713 |
| 31 | 1 | 2151.3802865 | 0.003472 | 18.447 |
| 31 | 2 | 2154.5721613 | 0.003472 | 15.824 |
| 31 | 4 | 2160.9564782 | 0.003472 | 16.815 |
| 31 | 5 | 2164.1487739 | 0.003472 | 18.037 |
| 31 | 6 | 2167.3402453 | 0.003472 | 15.867 |
| 44 | 111 | 2502.5138381 | 0.003472 | 17.450 |
| 44 | 112 | 2505.7052085 | 0.003472 | 16.471 |
| 44 | 113 | 2508.8968386 | 0.003472 | 18.901 |
| 44 | 115 | 2515.2841741 | 0.003472 | 17.269 |
| 44 | 116 | 2518.4735286 | 0.003472 | 15.974 |
| 44 | 117 | 2521.6664559 | 0.003472 | 19.577 |
| 71 | 341 | 3236.7117443 | 0.001157 | 17.363 |
| 71 | 342 | 3239.9037292 | 0.001157 | 16.200 |
| 71 | 343 | 3243.0976204 | 0.001157 | 17.756 |
| 71 | 345 | 3249.4806622 | 0.001157 | 17.963 |
| 71 | 346 | 3252.6700973 | 0.001157 | 15.410 |
| 71 | 347 | 3255.8647995 | 0.001157 | 17.848 |
| 71 | 348 | 3259.0570472 | 0.001157 | 15.410 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp/QLP FITS; historical/diff_s31.json, historical/diff_s31.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R186. [Deciding evidence](../../evidence/416646907/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
