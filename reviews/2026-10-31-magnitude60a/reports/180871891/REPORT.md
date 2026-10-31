# TIC 180871891: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 4 distinct eclipse events in selected sectors[29, 104]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=13.0367888505 ±0.0000275594d, reference eclipse epoch BTJD2097.6610275, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S29 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation0.910arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.310. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths8.024/7.114/6.961ppt, with 2 stacked events. QLP selected-kind fitted median6.596ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR34988096574291711488, P=13.0390915897±0.0016464671d, e=0.106260, omega=327.0889deg. Closest edge-on conjunction offset-0.327420d (-0.025111phase), full-SB1-covariance linear propagated Gaia uncertainty0.217962d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.025761d (photometric period projection allowance0.003610d). The approximate central duration6.79h vs observed median3.08h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Four measured shallow eclipses across sectors29/104 establish repeatability and period. Target-centered deficit0.043pixel and no capable catalogued neighbor support attribution. Sector2 was downloaded but no event window passed coverage cuts; it is not a clean non-detection. No single-event availability gap remains.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 29 | 56 | 2097.6628371 | 0.003472 | 6.437 | usable; same-kind selection applies |
| 29 | 57 | 2110.6960642 | 0.003472 | 8.496 | usable; same-kind selection applies |
| 104 | 216 | 4183.5443929 | 0.001767 | 5.637 | usable; same-kind selection applies |
| 104 | 217 | 4196.5863524 | 0.001598 | 6.754 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s29.json, historical/diff_s29.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R226. [Deciding evidence](../../evidence/180871891/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
