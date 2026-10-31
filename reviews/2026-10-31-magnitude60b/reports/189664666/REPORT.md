# TIC 189664666: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 4 distinct eclipse events in selected sectors[91]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 3 same-kind midtimes give P=3.4725104030 ±0.0005545785d, reference eclipse epoch BTJD3778.6307516, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Unreliable fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S91 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation1.658arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.056. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths43.381/43.134/42.826ppt, with 2 stacked events. Historical event coordinates guide these stacks and are not newly measured midtimes. QLP selected-kind fitted median43.073ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36300823508357068672, P=3.4727173222±0.0003480687d, e=0.061438, omega=290.4505deg. Closest edge-on conjunction offset0.002382d (0.000686phase), full-SB1-covariance linear propagated Gaia uncertainty0.359401d at the measured epoch. Near-Gaia-reference projected eclipse offset0.204335d (photometric period projection allowance0.541269d). The approximate central duration5.39h vs observed median5.01h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Four real raw eclipses in sector91; discontinuous egress/baseline ramp in cycle5 makes its trapezoid center unreliable and excluded. Three other same-kind timings fit the period. No capable catalogued neighbor in approximate brightness test. Timing baseline is only14d, not precision long-baseline characterization.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 91 | 0 | 3778.6310718 | 0.001157 | 43.774 | usable; same-kind selection applies |
| 91 | 3 | 3789.0470020 | 0.001157 | 42.146 | usable; same-kind selection applies |
| 91 | 4 | 3792.5217538 | 0.001157 | 43.073 | usable; same-kind selection applies |
| 91 | 5 | 3795.9952516 | 0.001157 | 43.976 | excluded unreliable timing fit |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s91.json, historical/diff_s91.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R292. [Deciding evidence](../../evidence/189664666/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
