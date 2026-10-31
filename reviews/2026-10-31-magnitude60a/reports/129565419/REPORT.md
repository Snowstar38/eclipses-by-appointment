# TIC 129565419: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 5 distinct eclipse events in selected sectors[57, 84]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=8.9837069710 ±0.0000373305d, fitted ephemeris intercept at earliest retained cycle BTJD2860.2271612, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S56 deficit peak[14, 12] vs target pixel[7, 8]; deficit-target separation0.846arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.968. Capable neighbours: Gaia 1931241188635723264: 38.91 arcsec, G14.422, required fractional eclipse0.353, pixel fractional loss0.012421269831853259
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths25.891/25.695/23.795ppt, with 3 stacked events. QLP selected-kind fitted median30.212ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31931241188635725696, P=8.9845539995±0.0011354221d, e=0.046905, omega=323.0527deg. Closest edge-on conjunction offset-0.297531d (-0.033116phase), full-SB1-covariance linear propagated Gaia uncertainty0.325225d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.064598d (photometric period projection allowance0.010266d). The approximate central duration6.22h vs observed median3.23h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Remote bright region dominates historical unrestricted peak and PSF residual0.968. Independent helper local5x5 re-stack residual0.115 and target centroid offset(-0.02,+0.01)pixel recover the target eclipse; three aperture depths24.40/23.92/22.14ppt support it. Capable neighbor38.91arcsec away lies1.90pixel from original deficit vs0.040pixel target.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 57 | 124 | 2860.2234867 | 0.001309 | 31.829 | usable; same-kind selection applies |
| 57 | 125 | 2869.2111081 | 0.001387 | 25.332 | usable; same-kind selection applies |
| 57 | 126 | 2878.1972885 | 0.001157 | 26.420 | usable; same-kind selection applies |
| 84 | 205 | 3587.9099069 | 0.001157 | 34.643 | usable; same-kind selection applies |
| 84 | 207 | 3605.8723510 | 0.001157 | 30.212 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s56.json, historical/diff_s56.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R227. [Deciding evidence](../../evidence/129565419/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
