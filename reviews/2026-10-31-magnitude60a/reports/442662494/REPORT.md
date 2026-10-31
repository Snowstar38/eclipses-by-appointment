# TIC 442662494: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 5 distinct eclipse events in selected sectors[9, 37, 90]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=15.8202440581 ±0.0000267968d, reference eclipse epoch BTJD1555.0654980, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S36 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.803arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.968. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths279.938/261.135/234.930ppt, with 2 stacked events. QLP selected-kind fitted median317.962ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35257808361458224128, P=15.8200347806±0.0026074222d, e=0.103885, omega=111.0794deg. Closest edge-on conjunction offset0.003691d (0.000233phase), full-SB1-covariance linear propagated Gaia uncertainty0.256392d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.011796d (photometric period projection allowance0.001983d). The approximate central duration7.35h vs observed median5.41h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Historical PSF fit residual0.968 is poor, though target-centered deficit and no capable catalogued neighbor support attribution. Aperture/sector-dependent depths approximately277-331ppt; no intrinsic undiluted depth is inferred.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 9 | 0 | 1555.0638588 | 0.010417 | 317.962 | usable; same-kind selection applies |
| 37 | 48 | 2314.4374794 | 0.003472 | 331.002 | usable; same-kind selection applies |
| 37 | 49 | 2330.2574750 | 0.003472 | 329.508 | usable; same-kind selection applies |
| 90 | 139 | 3754.0793461 | 0.001157 | 276.333 | usable; same-kind selection applies |
| 90 | 140 | 3769.8997306 | 0.001157 | 277.645 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s36.json, historical/diff_s36.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R220. [Deciding evidence](../../evidence/442662494/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
