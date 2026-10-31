# TIC 240771237: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 7 distinct eclipse events in selected sectors[84, 85]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=5.4961100628 Ãƒâ€šÃ‚±0.0001675565d, reference eclipse epoch BTJD3589.7561345, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S57 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation1.433arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.329. Capable neighbours: Gaia 415340212454228096: 31.45 arcsec, G14.768, required fractional eclipse0.620, pixel fractional loss0.015431025956409657
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths37.852/35.024/31.849ppt, with 4 stacked events. QLP selected-kind fitted median40.756ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3415340178091153024, P=5.4961262607Ãƒâ€šÃ‚±0.0001875488d, e=0.029793, omega=317.7859deg. Closest edge-on conjunction offset0.109935d (0.020002phase), full-SB1-covariance linear propagated Gaia uncertainty0.109819d at the measured epoch. Near-Gaia-reference projected eclipse offset0.119362d (photometric period projection allowance0.097518d). The approximate central duration5.44h vs observed median2.63h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Seven measured newer-sector repeats; historical sector57 did not pass present fitting window requirements and is not a null. Capable neighbor31.4arcsec away is separated from the target-centered deficit.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 84 | 331 | 3589.7558172 | 0.001157 | 40.300 | usable; same-kind selection applies |
| 84 | 332 | 3595.2523916 | 0.001157 | 42.845 | usable; same-kind selection applies |
| 84 | 333 | 3600.7487471 | 0.001157 | 43.689 | usable; same-kind selection applies |
| 84 | 334 | 3606.2449399 | 0.001157 | 41.407 | usable; same-kind selection applies |
| 85 | 335 | 3611.7392832 | 0.001157 | 40.756 | usable; same-kind selection applies |
| 85 | 337 | 3622.7337666 | 0.001157 | 40.341 | usable; same-kind selection applies |
| 85 | 339 | 3633.7246371 | 0.001157 | 39.981 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s57.json, historical/diff_s57.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R238. [Deciding evidence](../../evidence/240771237/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
