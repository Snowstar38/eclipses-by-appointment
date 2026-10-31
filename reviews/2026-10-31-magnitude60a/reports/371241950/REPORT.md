# TIC 371241950: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 13 distinct eclipse events in selected sectors[10, 38, 90]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 13 same-kind midtimes give P=5.8085988833 +/-0.0000066634d, reference eclipse epoch BTJD1575.3856200, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Deciding S90 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation1.325arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.363. Capable neighbours: Gaia 5243963620257188736: 45.52 arcsec, G14.028, required fractional eclipse0.536, pixel fractional loss0.017013504837050105
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths80.317/75.007/63.791ppt, with 4 stacked events. QLP selected-kind fitted median83.558ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35243963688976670592, P=5.8081279932+/-0.0004474477d, e=0.047392, omega=328.0911deg. Closest edge-on conjunction offset0.172284d (0.029663phase), full-SB1-covariance linear propagated Gaia uncertainty0.095187d at the measured epoch. Near-Gaia-reference projected eclipse offset0.076223d (photometric period projection allowance0.001359d). The approximate central duration7.35h vs observed median4.34h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Thirteen measured repeats span three sectors; capable neighbor45.52arcsec is spatially separated from deficit core. Gaia phase offset0.030 is discussed with covariance rather than arbitrary cutoff; observed4.3h duration can be noncentral.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 10 | 0 | 1575.3860340 | 0.010417 | 78.605 | usable; same-kind selection applies |
| 10 | 1 | 1581.1912528 | 0.010417 | 73.981 | usable; same-kind selection applies |
| 10 | 2 | 1587.0026511 | 0.010417 | 73.432 | usable; same-kind selection applies |
| 10 | 3 | 1592.8118838 | 0.010417 | 82.230 | usable; same-kind selection applies |
| 38 | 132 | 2342.1201329 | 0.003472 | 84.376 | usable; same-kind selection applies |
| 38 | 133 | 2347.9294237 | 0.003472 | 84.047 | usable; same-kind selection applies |
| 38 | 134 | 2353.7379595 | 0.003472 | 83.362 | usable; same-kind selection applies |
| 38 | 135 | 2359.5471217 | 0.003472 | 85.296 | usable; same-kind selection applies |
| 90 | 374 | 3747.8019640 | 0.001157 | 84.022 | usable; same-kind selection applies |
| 90 | 375 | 3753.6100691 | 0.001157 | 83.899 | usable; same-kind selection applies |
| 90 | 376 | 3759.4188695 | 0.001157 | 84.903 | usable; same-kind selection applies |
| 90 | 377 | 3765.2272652 | 0.001157 | 82.496 | usable; same-kind selection applies |
| 90 | 378 | 3771.0358210 | 0.001157 | 83.558 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s90.json, historical/diff_s90.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] For TIC407207285 the deciding revised cutout is revised-cutout/diff_revised-long-window.json and .png; historical extraction remains for comparison. Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R261. [Deciding evidence](../../evidence/371241950/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
