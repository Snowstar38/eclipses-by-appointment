# TIC 274941915: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 5 distinct eclipse events in selected sectors[76, 83]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=10.1329390738 ±0.0000628576d, reference primary epoch BTJD3371.1764455. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S83 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation5.332arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.265. Capable neighbours: Gaia 1967100282911816960: 32.98 arcsec, G15.918, required fractional eclipse0.586, pixel fractional loss0.010377045342031255; Gaia 1967100282911812224: 40.57 arcsec, G15.999, required fractional eclipse0.630, pixel fractional loss0.00914697883875284; Gaia 1967100385991024896: 47.81 arcsec, G16.085, required fractional eclipse0.682, pixel fractional loss0.005402736181751521
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths10.256/9.725/9.397ppt, with 3 stacked events. QLP primary fitted median10.415ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31967100282911815040, P=10.1324824053±0.0027856675d, e=0.042312, omega=29.1410deg. Closest edge-on conjunction offset0.156872d (0.015482phase), full-SB1-covariance linear propagated Gaia uncertainty0.910278d at the measured epoch. Near-Gaia-reference projected eclipse offset0.022611d (photometric period projection allowance0.018480d). The approximate central duration4.17h vs observed median1.94h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Three capable neighbours at 32.98, 40.57 and 47.81 arcsec are spatially separated from the target-centered compact deficit. The small-aperture reduction retains the eclipse. No calibrated centroid confidence ellipse is available.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 83 | 182 | 3563.7012245 | 0.001157 | 9.731 |
| 83 | 183 | 3573.8355392 | 0.001157 | 10.666 |
| 83 | 184 | 3583.9688425 | 0.001157 | 10.415 |
| 76 | 163 | 3371.1768997 | 0.001757 | 11.308 |
| 76 | 165 | 3391.4422014 | 0.001157 | 10.001 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, raw/QLP FITS; historical/diff_s83.json, historical/diff_s83.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R178. [Deciding evidence](../../evidence/274941915/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
