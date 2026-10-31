# TIC 42960522: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 20 distinct eclipse events in selected sectors[12, 99, 103]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 20 same-kind midtimes give P=2.5438060407 ±0.0000075069d, reference eclipse epoch BTJD1627.7359239, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S38 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation6.451arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.589. Capable neighbours: Gaia 5886342431117033728: 29.06 arcsec, G12.760, required fractional eclipse0.072; Gaia 5886336555601769088: 34.16 arcsec, G13.662, required fractional eclipse0.137; Gaia 5886336521242033536: 58.54 arcsec, G13.330, required fractional eclipse0.107; Gaia 5886342431117035648: 58.97 arcsec, G15.833, required fractional eclipse0.875; Gaia 5886336585650415360: 59.38 arcsec, G15.897, required fractional eclipse0.927
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths20.934/15.800/12.060ppt, with 10 stacked events. QLP selected-kind fitted median22.061ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35886336555601771392, P=2.5437447918±0.0002679482d, e=0.084019, omega=95.1819deg. Closest edge-on conjunction offset0.042597d (0.016746phase), full-SB1-covariance linear propagated Gaia uncertainty0.140235d at the measured epoch. Near-Gaia-reference projected eclipse offset0.012769d (photometric period projection allowance0.003656d). The approximate central duration3.20h vs observed median3.27h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deficit0.307pixel from target; nearest capable neighbor1.55pixels from deficit. Spatial core supports target at TESS resolution; no calibrated centroid errors.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 12 | 0 | 1627.7246309 | 0.010416 | 23.866 | usable; same-kind selection applies |
| 12 | 5 | 1640.4445722 | 0.010416 | 21.960 | usable; same-kind selection applies |
| 12 | 6 | 1642.9885060 | 0.010416 | 23.265 | usable; same-kind selection applies |
| 12 | 7 | 1645.5345634 | 0.010416 | 24.656 | usable; same-kind selection applies |
| 12 | 9 | 1650.6206212 | 0.010416 | 24.767 | usable; same-kind selection applies |
| 99 | 951 | 4046.8975859 | 0.001157 | 22.161 | usable; same-kind selection applies |
| 99 | 952 | 4049.4411514 | 0.001157 | 22.265 | usable; same-kind selection applies |
| 99 | 953 | 4051.9855243 | 0.001157 | 21.386 | usable; same-kind selection applies |
| 99 | 954 | 4054.5294988 | 0.001157 | 22.438 | usable; same-kind selection applies |
| 99 | 958 | 4064.7051281 | 0.001157 | 21.113 | usable; same-kind selection applies |
| 99 | 960 | 4069.7916359 | 0.001157 | 20.224 | usable; same-kind selection applies |
| 103 | 993 | 4153.7349545 | 0.001157 | 21.587 | usable; same-kind selection applies |
| 103 | 994 | 4156.2784550 | 0.001157 | 21.849 | usable; same-kind selection applies |
| 103 | 995 | 4158.8220809 | 0.001157 | 24.906 | usable; same-kind selection applies |
| 103 | 996 | 4161.3646923 | 0.001157 | 21.138 | usable; same-kind selection applies |
| 103 | 997 | 4163.9085124 | 0.001157 | 21.659 | usable; same-kind selection applies |
| 103 | 998 | 4166.4525329 | 0.001614 | 23.179 | usable; same-kind selection applies |
| 103 | 999 | 4168.9956876 | 0.001157 | 21.428 | usable; same-kind selection applies |
| 103 | 1001 | 4174.0831874 | 0.001157 | 21.791 | usable; same-kind selection applies |
| 103 | 1002 | 4176.6281771 | 0.001157 | 22.242 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s38.json, historical/diff_s38.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R280. [Deciding evidence](../../evidence/42960522/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
