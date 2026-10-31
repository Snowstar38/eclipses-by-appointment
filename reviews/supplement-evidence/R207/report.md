# TIC 383603595: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 11 distinct eclipse events in selected sectors [8, 62, 90]. The lead inspected representative raw-event plots and numeric fit output; the helper independently audited timing and pixel exceptions. All fitted windows are preserved. Timing includes historical cycles [0, 1, 294, 295, 296, 297, 445, 446, 447, 448, 449]; excluded cycles [] remain in the raw evidence. Fits with midpoint covariance uncertainty larger than the seeded eclipse duration are excluded as unconstrained, not treated as timing measurements. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 retained reference-eclipse midtimes give P=5.0148153412 +/-0.0000049551 d, observed reference eclipse epoch BTJD 1520.2020452. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S89 deficit peak [8, 8] vs target pixel [8, 8]; deficit-target separation 0.862 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.931. Capable neighbours: Gaia 5303521141484894592: 9.86 arcsec, G 15.271, required fractional eclipse 0.881, pixel fractional loss 0.02715275445324021; Gaia 5303521137176600576: 16.56 arcsec, G 14.623, required fractional eclipse 0.499, pixel fractional loss 0.021045342368154214; Gaia 5303521038405677568: 24.30 arcsec, G 15.129, required fractional eclipse 0.777, pixel fractional loss 0.02056002298778204; Gaia 5303521141484897664: 56.62 arcsec, G 15.396, required fractional eclipse 0.985, pixel fractional loss 0.003267899249113125; Gaia 5303521210204372224: 58.12 arcsec, G 15.245, required fractional eclipse 0.862, pixel fractional loss 0.0008082498493232974
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 27.153/24.924/19.335 ppt, with 6 stacked events. QLP retained-reference fitted median 32.026 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 5303521038405679232, P=5.0148048769+/-0.0002225298 d, e=0.018777, omega=298.0394 deg. Closest edge-on conjunction offset 0.000726 d (0.000145 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.056590 d at the measured epoch. Near-Gaia-reference projected eclipse offset -0.001639 d (photometric period projection allowance 0.001120 d). The approximate central duration 5.55 h vs median local-model width 2.88 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Eleven fitted repeated eclipses span S8,62,90. Modest aperture/baseline depth variation limits precision; no missing bounded check.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 8 | 0 | 1520.2080281 | 0.010417 | 29.494 |
| 8 | 1 | 1525.2201049 | 0.010417 | 26.411 |
| 62 | 294 | 2994.5585519 | 0.001157 | 32.026 |
| 62 | 295 | 2999.5719773 | 0.001157 | 31.720 |
| 62 | 296 | 3004.5870881 | 0.001157 | 32.304 |
| 62 | 297 | 3009.6019706 | 0.001157 | 32.258 |
| 90 | 445 | 3751.7945559 | 0.001157 | 32.099 |
| 90 | 446 | 3756.8089221 | 0.001157 | 34.487 |
| 90 | 447 | 3761.8250054 | 0.001157 | 29.573 |
| 90 | 448 | 3766.8393974 | 0.001157 | 34.065 |
| 90 | 449 | 3771.8548444 | 0.001157 | 31.390 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s89.json, historical/diff_s89.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R207. [Deciding evidence](../../evidence/383603595/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
