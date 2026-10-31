# TIC 345794632: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 5 distinct eclipse events in selected sectors[15, 16, 83]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=14.6442648499 ±0.0000425120d, reference primary epoch BTJD1712.6089011. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S15 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation2.925arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.575. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths69.463/67.069/60.990ppt, with 2 stacked events. QLP primary fitted median73.387ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31973038504696356096, P=14.6450193761±0.0011842092d, e=0.123987, omega=43.5911deg. Closest edge-on conjunction offset-0.048332d (-0.003300phase), full-SB1-covariance linear propagated Gaia uncertainty0.120492d at the measured epoch. Near-Gaia-reference projected eclipse offset0.019576d (photometric period projection allowance0.003826d). The approximate central duration22.47h vs observed median12.91h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Large historical PSF fractional residual0.57 reflects imperfect scaled out-image morphology in a crowded field. No listed neighbour within60arcsec can supply the approximately73ppt eclipse under the G-band flux-budget screen, and the lost-light core coincides with the target. The weaker localization calibration remains a limitation.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 15 | 0 | 1712.6060656 | 0.010417 | 76.327 |
| 15 | 1 | 1727.2509117 | 0.010417 | 74.813 |
| 83 | 127 | 3572.4305360 | 0.001157 | 72.809 |
| 16 | 2 | 1741.9002939 | 0.010417 | 73.387 |
| 16 | 3 | 1756.5440034 | 0.010417 | 73.098 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, raw/QLP FITS; historical/diff_s15.json, historical/diff_s15.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R183. [Deciding evidence](../../evidence/345794632/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
