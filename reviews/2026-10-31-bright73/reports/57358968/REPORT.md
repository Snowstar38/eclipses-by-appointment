# TIC 57358968: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 7 distinct eclipse events in selected sectors[45, 71, 72]. The representative raw-event plot and numeric raw-windows.csv were inspected. The raw morphology, ingress/egress and local baselines were inspected independently of fitted curves; target-specific interpretation follows below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=7.4961579330 +/-0.0000213829d, reference eclipse epoch BTJD2528.4204021, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S45 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation2.927arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.637. Capable neighbours: Gaia 3365438142952202496: 58.97 arcsec, G13.277, required fractional eclipse0.350
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths80.702/75.505/59.984ppt, with 3 stacked events. QLP selected-kind fitted median91.699ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR33365426387623096576, P=7.4952754576+/-0.0007670721d, e=0.474132, omega=152.8161deg. Closest edge-on conjunction offset0.050735d (0.006769phase), full-SB1-covariance linear propagated Gaia uncertainty0.220431d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.200771d (photometric period projection allowance0.006094d). The approximate central duration4.94h vs observed median3.69h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Seven deep V-shaped eclipses across S45/71/72 with multiple consecutive local cycles; target-localized difference core and capable-neighbor geometry support attribution.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 45 | 0 | 2528.4206133 | 0.003472 | 92.594 | used in ephemeris |
| 45 | 1 | 2535.9167680 | 0.003472 | 91.002 | used in ephemeris |
| 45 | 2 | 2543.4124789 | 0.003472 | 90.469 | used in ephemeris |
| 71 | 97 | 3255.5468668 | 0.001158 | 90.521 | used in ephemeris |
| 72 | 98 | 3263.0441349 | 0.001157 | 93.289 | used in ephemeris |
| 72 | 99 | 3270.5400579 | 0.001157 | 93.177 | used in ephemeris |
| 72 | 100 | 3278.0367542 | 0.001157 | 91.699 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s45.json, historical/diff_s45.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are [local path omitted] and [local path omitted] No historical evidence overwritten.


Stable review key: R406. [Deciding evidence](../../evidence/57358968/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/57358968/measurements.json), [raw eclipse plots](../../evidence/57358968/raw-events.png), [raw flux windows](../../evidence/57358968/raw-windows.csv), [Gaia geometry](../../analysis/batch07/gaia-geometry.json), [independent audit](../../analysis/batch07/helper-audit.md), [difference image](../../evidence/57358968/historical/diff_s45.png).
