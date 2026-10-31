# TIC 300217120: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 3 distinct eclipse events in selected sectors[67, 94]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 3 same-kind midtimes give P=14.1585774920 ±0.0000275211d, reference primary epoch BTJD3141.0351408. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S27 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.744arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.167. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths42.769/41.065/39.999ppt, with 1 stacked events. QLP primary fitted median37.866ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36692312629248544512, P=14.1570493482±0.0030226820d, e=0.361127, omega=263.6297deg. Closest edge-on conjunction offset0.117178d (0.008277phase), full-SB1-covariance linear propagated Gaia uncertainty0.528972d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.179282d (photometric period projection allowance0.005339d). The approximate central duration15.03h vs observed median10.88h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** The nearby other eclipse in S67 contaminates a wider baseline window; the final fit uses a narrower 1.65-search-duration half-window and shows the repeated primary. Historical S27 TESScut contains one event but QLP independently shows three primaries in S67/S94.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 94 | 155 | 3863.1220326 | 0.001157 | 37.866 |
| 94 | 156 | 3877.2817199 | 0.001157 | 37.629 |
| 67 | 104 | 3141.0351516 | 0.001157 | 42.190 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, raw/QLP FITS; historical/diff_s27.json, historical/diff_s27.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R175. [Deciding evidence](../../evidence/300217120/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
