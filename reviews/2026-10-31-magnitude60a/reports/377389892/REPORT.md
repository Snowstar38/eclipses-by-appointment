# TIC 377389892: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 11 distinct eclipse events in selected sectors[21, 48, 75]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 same-kind midtimes give P=4.5881927790 +/-0.0000096916d, reference eclipse epoch BTJD1875.0768278, kind: Deeper primary; shallower secondary at orbital phase0.5. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Deciding S21 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation2.123arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.044. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths228.894/227.798/226.259ppt, with 4 stacked events. QLP selected-kind fitted median227.447ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3854441274902991616, P=4.5880638447+/-0.0001891317d, e=0.018288, omega=77.4620deg. Closest edge-on conjunction offset0.028670d (0.006249phase), full-SB1-covariance linear propagated Gaia uncertainty0.068238d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.013105d (photometric period projection allowance0.003140d). The approximate central duration5.18h vs observed median4.54h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Known VSX EA within0.02arcsec; excluded from new-system count. Catalogue1.147d is a quarter-period alias: raw fold shows deeper primary each4.588d and shallower secondary at phase0.5. Fold at1.147d mixes out-of-eclipse and unequal eclipse points. Primary epoch identifies deeper eclipse; physical Gaia orbit association retained.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 21 | 0 | 1875.0772236 | 0.010417 | 227.447 | usable; same-kind selection applies |
| 21 | 1 | 1879.6688126 | 0.010417 | 214.370 | usable; same-kind selection applies |
| 21 | 3 | 1888.8417538 | 0.010417 | 230.928 | usable; same-kind selection applies |
| 21 | 4 | 1893.4307987 | 0.010417 | 218.572 | usable; same-kind selection applies |
| 48 | 161 | 2613.7758350 | 0.003472 | 225.265 | usable; same-kind selection applies |
| 48 | 162 | 2618.3634915 | 0.003472 | 226.593 | usable; same-kind selection applies |
| 48 | 164 | 2627.5402139 | 0.003472 | 226.614 | usable; same-kind selection applies |
| 48 | 165 | 2632.1281960 | 0.003472 | 229.113 | usable; same-kind selection applies |
| 75 | 321 | 3347.8867371 | 0.001157 | 234.356 | usable; same-kind selection applies |
| 75 | 322 | 3352.4748173 | 0.001157 | 235.871 | usable; same-kind selection applies |
| 75 | 325 | 3366.2396089 | 0.001157 | 236.295 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s21.json, historical/diff_s21.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] For TIC407207285 the deciding revised cutout is revised-cutout/diff_revised-long-window.json and .png; historical extraction remains for comparison. Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R257. [Deciding evidence](../../evidence/377389892/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
