# TIC 428691463: PROBABLE

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 15 distinct eclipse events in selected sectors[59, 86]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 15 same-kind midtimes give P=2.2025512596 ±0.0000032099d, reference eclipse epoch BTJD2912.7110288, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: unresolved after check.** Historical S59 deficit peak[7, 7] vs target pixel[8, 7]; deficit-target separation3.708arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.815. Capable neighbours: Gaia 251403200552910592: 6.95 arcsec, G12.261, required fractional eclipse0.023, pixel fractional loss0.005518074279438695; Gaia 251403200553995008: 13.52 arcsec, G16.015, required fractional eclipse0.465, pixel fractional loss0.005042044222833572; Gaia 251403234912639616: 39.32 arcsec, G15.736, required fractional eclipse0.361, pixel fractional loss0.0023197334242561615
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths5.316/4.931/4.325ppt, with 10 stacked events. QLP selected-kind fitted median10.135ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3251403200552912128, P=2.2025752205±0.0000738127d, e=0.023863, omega=315.1974deg. Closest edge-on conjunction offset-0.031275d (-0.014199phase), full-SB1-covariance linear propagated Gaia uncertainty0.077205d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.003816d (photometric period projection allowance0.003679d). The approximate central duration3.88h vs observed median1.34h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unresolved attribution: capable neighbor Gaia251403200552910592 at6.95arcsec needs only2.3% fractional eclipse. Deficit centroid lies between target and neighbor; PSF residual0.815 and uncalibrated centroid cannot discriminate. Real repeated eclipses remain probable for this target.

**Next check:** Resolved eclipse photometry or multi-source PRF localization of this signal.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 59 | 496 | 2912.7101110 | 0.002139 | 10.628 | usable; same-kind selection applies |
| 59 | 497 | 2914.9109222 | 0.001157 | 8.703 | usable; same-kind selection applies |
| 59 | 498 | 2917.1127333 | 0.001780 | 10.766 | usable; same-kind selection applies |
| 59 | 499 | 2919.3221369 | 0.001960 | 11.576 | usable; same-kind selection applies |
| 59 | 500 | 2921.5194762 | 0.002219 | 8.957 | usable; same-kind selection applies |
| 59 | 502 | 2925.9265644 | 0.001157 | 8.434 | usable; same-kind selection applies |
| 59 | 503 | 2928.1295658 | 0.001157 | 10.135 | usable; same-kind selection applies |
| 59 | 505 | 2932.5369579 | 0.002308 | 12.706 | usable; same-kind selection applies |
| 59 | 506 | 2934.7386079 | 0.001157 | 8.687 | usable; same-kind selection applies |
| 86 | 826 | 3639.5553104 | 0.002137 | 7.859 | usable; same-kind selection applies |
| 86 | 828 | 3643.9576304 | 0.001347 | 10.204 | usable; same-kind selection applies |
| 86 | 829 | 3646.1598615 | 0.001841 | 10.219 | usable; same-kind selection applies |
| 86 | 830 | 3648.3627624 | 0.002785 | 8.065 | usable; same-kind selection applies |
| 86 | 835 | 3659.3751737 | 0.002683 | 8.426 | usable; same-kind selection applies |
| 86 | 836 | 3661.5784863 | 0.001237 | 12.621 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s59.json, historical/diff_s59.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R217. [Deciding evidence](../../evidence/428691463/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
