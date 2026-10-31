# TIC 373621318: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 11 distinct eclipse events in selected sectors[58, 85]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass with disclosed cycle assumptions.** 11 same-kind midtimes give P=4.1104208467 ±0.0000052818d, reference eclipse epoch BTJD2883.5677296, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S58 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation2.280arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.941. Capable neighbours: Gaia 511214808904243584: 30.05 arcsec, G14.117, required fractional eclipse0.169, pixel fractional loss0.004656160732442441; Gaia 511214052989995264: 33.49 arcsec, G13.916, required fractional eclipse0.145, pixel fractional loss0.0054985862487090705; Gaia 511214430947407872: 34.68 arcsec, G15.661, required fractional eclipse0.614, pixel fractional loss0.005682766497404662; Gaia 511214774544514560: 34.80 arcsec, G15.160, required fractional eclipse0.397, pixel fractional loss0.004714198414336461; Gaia 511214430947117824: 41.03 arcsec, G14.835, required fractional eclipse0.302, pixel fractional loss0.005682766497404662; Gaia 511214430947115264: 45.57 arcsec, G15.688, required fractional eclipse0.629, pixel fractional loss0.005682766497404662; Gaia 511214362227651712: 51.37 arcsec, G15.873, required fractional eclipse0.741, pixel fractional loss0.008128411725709894
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths26.264/17.422/6.989ppt, with 7 stacked events. Historical outputs are retained as measured pipeline evidence. QLP selected-kind fitted median29.444ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3511214048684134528, P=4.1103587301±0.0002578027d, e=0.020847, omega=29.4745deg. Closest edge-on conjunction offset0.061699d (0.015011phase), full-SB1-covariance linear propagated Gaia uncertainty0.158656d at the measured epoch. Near-Gaia-reference projected eclipse offset0.023994d (photometric period projection allowance0.003206d). The approximate central duration6.16h vs observed median3.62h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated isolated narrow eclipses and target-centered deficit favor target; bright field source affects whole-image PSF residual and dilution.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 58 | 0 | 2883.5681774 | 0.001157 | 26.815 | usable; same-kind selection applies |
| 58 | 1 | 2887.6759071 | 0.001157 | 29.832 | usable; same-kind selection applies |
| 58 | 2 | 2891.7886027 | 0.001157 | 31.608 | usable; same-kind selection applies |
| 58 | 4 | 2900.0092722 | 0.001157 | 32.323 | usable; same-kind selection applies |
| 58 | 5 | 2904.1212799 | 0.001157 | 28.857 | usable; same-kind selection applies |
| 58 | 6 | 2908.2307234 | 0.001157 | 27.630 | usable; same-kind selection applies |
| 85 | 177 | 3611.1102951 | 0.001157 | 29.444 | usable; same-kind selection applies |
| 85 | 178 | 3615.2249131 | 0.001157 | 29.014 | usable; same-kind selection applies |
| 85 | 179 | 3619.3347543 | 0.001157 | 30.474 | usable; same-kind selection applies |
| 85 | 182 | 3631.6632148 | 0.001157 | 28.443 | usable; same-kind selection applies |
| 85 | 183 | 3635.7738019 | 0.001157 | 30.219 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): ../helper/pixel-identity-audit.json, ../helper/same-sector-refits.json, ../helper/314047448-measured-diff.json, ../helper/48108063-measured-diff.json; measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s58.json, historical/diff_s58.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R250. [Deciding evidence](../../evidence/373621318/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
