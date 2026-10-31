# TIC 245474316: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 4 distinct eclipse events in selected sectors[58, 85]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=15.0172912209 ±0.0000236159d, reference primary epoch BTJD2884.3381092. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S58 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation1.339arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.251. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths211.230/200.007/179.092ppt, with 2 stacked events. QLP primary fitted median219.834ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3465063255000893824, P=15.0160303467±0.0023990301d, e=0.112486, omega=223.7112deg. Closest edge-on conjunction offset0.004132d (0.000275phase), full-SB1-covariance linear propagated Gaia uncertainty0.372564d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.205174d (photometric period projection allowance0.003920d). The approximate central duration10.65h vs observed median8.68h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep repeated eclipses are isolated in both reductions; all four measured primary events support the timing solution.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 58 | 0 | 2884.3382264 | 0.001157 | 218.220 |
| 58 | 1 | 2899.3552650 | 0.001157 | 219.495 |
| 85 | 49 | 3620.1861623 | 0.001157 | 220.174 |
| 85 | 50 | 3635.2019054 | 0.001157 | 220.966 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, raw/QLP FITS; historical/diff_s58.json, historical/diff_s58.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R180. [Deciding evidence](../../evidence/245474316/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
