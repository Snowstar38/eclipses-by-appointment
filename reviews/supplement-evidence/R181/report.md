# TIC 397586559: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 11 distinct eclipse events in selected sectors[42, 43, 70]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=9.8662883278 ±0.0000276603d, reference primary epoch BTJD2452.7124847. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S70 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation5.292arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.112. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths213.240/212.272/209.507ppt, with 5 stacked events. QLP primary fitted median253.719ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32751832417527312512, P=9.8675532753±0.0005013266d, e=0.011536, omega=68.9884deg. Closest edge-on conjunction offset-0.280929d (-0.028470phase), full-SB1-covariance linear propagated Gaia uncertainty0.101964d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.016555d (photometric period projection allowance0.005781d). The approximate central duration8.63h vs observed median6.97h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating eclipses (primary median approximately254 ppt, secondary164 ppt) establish orbital period twice the historical4.93316d event spacing. Only deeper even cycles enter the reported primary ephemeris. Historical S70 difference image mixes both eclipse kinds, so its aperture depth is a mixture. Gaia nominal conjunction is0.28093d later at the TESS epoch; measured-Gaia period difference−0.00126495d accumulates this offset. Projecting toward the Gaia2016 reference reduces offset to−0.0166d; the orbit association is physically consistent with an imperfect Gaia period, and the tension is retained rather than subjected to a sigma veto.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 42 | 0 | 2452.7125490 | 0.003472 | 255.778 |
| 42 | 2 | 2462.5789023 | 0.003472 | 256.725 |
| 42 | 3 | 2467.5210695 | 0.003472 | 164.434 |
| 70 | 154 | 3212.4166243 | 0.001157 | 251.660 |
| 70 | 155 | 3217.3583697 | 0.001157 | 161.411 |
| 70 | 156 | 3222.2830146 | 0.001157 | 250.473 |
| 70 | 157 | 3227.2246915 | 0.001157 | 160.994 |
| 70 | 158 | 3232.1492837 | 0.001157 | 250.918 |
| 43 | 5 | 2477.3868167 | 0.003472 | 169.132 |
| 43 | 8 | 2492.1774458 | 0.003472 | 261.402 |
| 43 | 9 | 2497.1193978 | 0.003472 | 168.948 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, raw/QLP FITS; historical/diff_s70.json, historical/diff_s70.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R181. [Deciding evidence](../../evidence/397586559/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
