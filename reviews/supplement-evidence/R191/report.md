# TIC 152086769: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 9 distinct eclipse events in selected sectors[2, 69, 96]. The lead inspected raw-event plots and numeric fitting summaries. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 9 same-kind midtimes give P=6.3322039761 ±0.0000079047d, reference primary epoch BTJD1356.8092972. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S29 deficit peak[8, 8] vs target pixel[8, 7]; deficit-target separation0.183arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.783. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths263.413/258.932/233.354ppt, with 3 stacked events. QLP primary fitted median279.743ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32340498864102877824, P=6.3321286286±0.0002353598d, e=0.041230, omega=343.5423deg. Closest edge-on conjunction offset0.064331d (0.010159phase), full-SB1-covariance linear propagated Gaia uncertainty0.053697d at the measured epoch. Near-Gaia-reference projected eclipse offset0.052803d (photometric period projection allowance0.001209d). The approximate central duration5.90h vs observed median4.83h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep flat-bottom repeated eclipses; sector96 aperture depth is lower than earlier sectors. No capable neighbour within60arcsec in approximate G flux budget.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 2 | 0 | 1356.8097738 | 0.010417 | 281.790 |
| 2 | 1 | 1363.1410445 | 0.010417 | 280.834 |
| 2 | 2 | 1369.4673288 | 0.010417 | 268.369 |
| 69 | 289 | 3186.8159539 | 0.001157 | 279.743 |
| 69 | 290 | 3193.1481766 | 0.001157 | 276.857 |
| 69 | 291 | 3199.4816285 | 0.001157 | 281.412 |
| 69 | 292 | 3205.8127354 | 0.001157 | 282.614 |
| 96 | 404 | 3915.0195179 | 0.001157 | 232.172 |
| 96 | 406 | 3927.6840904 | 0.001157 | 230.402 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp/QLP FITS; historical/diff_s29.json, historical/diff_s29.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R191. [Deciding evidence](../../evidence/152086769/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
