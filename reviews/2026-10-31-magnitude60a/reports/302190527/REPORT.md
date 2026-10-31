# TIC 302190527: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[42, 57, 84]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=9.4703064823 ±0.0000113926d, fitted ephemeris intercept at earliest retained cycle BTJD2450.9782406, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S57 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation4.058arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.114. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths263.443/258.276/255.104ppt, with 3 stacked events. QLP selected-kind fitted median281.535ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32779583640038802560, P=9.4713396104±0.0013422095d, e=0.105048, omega=22.4456deg. Closest edge-on conjunction offset-0.163176d (-0.017228phase), full-SB1-covariance linear propagated Gaia uncertainty0.259643d at the measured epoch. Near-Gaia-reference projected eclipse offset0.062045d (photometric period projection allowance0.002484d). The approximate central duration6.77h vs observed median5.09h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** No capable catalogued neighbor. Approximately275-283ppt raw eclipses repeat across widely separated sectors; alternative aperture depths255-263ppt are diluted extraction values.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 42 | 0 | 2450.9781740 | 0.003472 | 275.645 | usable; same-kind selection applies |
| 42 | 2 | 2469.9187712 | 0.003472 | 274.672 | usable; same-kind selection applies |
| 57 | 43 | 2858.2014181 | 0.001157 | 282.981 | usable; same-kind selection applies |
| 57 | 44 | 2867.6719084 | 0.001157 | 284.177 | usable; same-kind selection applies |
| 57 | 45 | 2877.1418754 | 0.001157 | 284.507 | usable; same-kind selection applies |
| 84 | 120 | 3587.4148446 | 0.001157 | 281.216 | usable; same-kind selection applies |
| 84 | 121 | 3596.8856220 | 0.001157 | 281.562 | usable; same-kind selection applies |
| 84 | 122 | 3606.3555006 | 0.001157 | 281.509 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s57.json, historical/diff_s57.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R233. [Deciding evidence](../../evidence/302190527/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
