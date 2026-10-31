# TIC 140281693: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 15 distinct eclipse events in selected sectors[5, 33, 98]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 15 same-kind midtimes give P=3.8719820163 Ãƒâ€šÃ‚±0.0000030426d, reference eclipse epoch BTJD1440.1160470, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S32 deficit peak[8, 8] vs target pixel[8, 7]; deficit-target separation2.132arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual1.000. Capable neighbours: Gaia 2903798530942872704: 37.49 arcsec, G14.214, required fractional eclipse0.428, pixel fractional loss0.0062627425786385355; Gaia 2903798634022085504: 56.76 arcsec, G14.826, required fractional eclipse0.720, pixel fractional loss0.008418660852396504
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths40.235/37.239/29.706ppt, with 7 stacked events. QLP selected-kind fitted median42.031ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32903798565302609536, P=3.8720833801Ãƒâ€šÃ‚±0.0002902097d, e=0.100248, omega=219.1844deg. Closest edge-on conjunction offset-0.037247d (-0.009619phase), full-SB1-covariance linear propagated Gaia uncertainty0.069345d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.009778d (photometric period projection allowance0.000825d). The approximate central duration4.57h vs observed median3.89h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Target-centered deficit despite poor0.9999 total-light PSF residual caused by unrelated bright light outside target core. Capable neighbors37.5/56.8arcsec are spatially separate. Raw depth34-45ppt depends on sector aperture.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 5 | 0 | 1440.1153374 | 0.010417 | 41.132 | usable; same-kind selection applies |
| 5 | 2 | 1447.8590467 | 0.010417 | 42.031 | usable; same-kind selection applies |
| 5 | 5 | 1459.4790570 | 0.010417 | 42.655 | usable; same-kind selection applies |
| 33 | 197 | 2202.8964232 | 0.003472 | 43.750 | usable; same-kind selection applies |
| 33 | 198 | 2206.7686474 | 0.003472 | 43.818 | usable; same-kind selection applies |
| 33 | 199 | 2210.6410010 | 0.003472 | 44.018 | usable; same-kind selection applies |
| 33 | 201 | 2218.3841162 | 0.003472 | 44.681 | usable; same-kind selection applies |
| 33 | 202 | 2222.2567471 | 0.003472 | 44.732 | usable; same-kind selection applies |
| 33 | 203 | 2226.1275199 | 0.003472 | 43.278 | usable; same-kind selection applies |
| 98 | 661 | 3999.4965366 | 0.001157 | 34.683 | usable; same-kind selection applies |
| 98 | 664 | 4011.1119223 | 0.001157 | 34.553 | usable; same-kind selection applies |
| 98 | 665 | 4014.9838019 | 0.001157 | 34.442 | usable; same-kind selection applies |
| 98 | 668 | 4026.6000678 | 0.001157 | 34.935 | usable; same-kind selection applies |
| 98 | 669 | 4030.4720694 | 0.001157 | 34.958 | usable; same-kind selection applies |
| 98 | 672 | 4042.0879774 | 0.001157 | 33.925 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s32.json, historical/diff_s32.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R245. [Deciding evidence](../../evidence/140281693/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
