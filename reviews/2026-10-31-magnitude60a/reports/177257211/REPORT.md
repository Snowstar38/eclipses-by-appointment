# TIC 177257211: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 17 distinct eclipse events in selected sectors[1, 38, 98]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 17 same-kind midtimes give P=3.5443290949 +/-0.0000030739d, reference eclipse epoch BTJD1329.0245577, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Deciding S97 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation3.827arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.403. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths62.101/59.341/55.456ppt, with 16 stacked events. QLP selected-kind fitted median55.820ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35260874173508490880, P=3.5442836835+/-0.0003211078d, e=0.026413, omega=251.8290deg. Closest edge-on conjunction offset0.042646d (0.012032phase), full-SB1-covariance linear propagated Gaia uncertainty0.104328d at the measured epoch. Near-Gaia-reference projected eclipse offset0.030612d (photometric period projection allowance0.000815d). The approximate central duration5.70h vs observed median3.57h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Seventeen raw repeated events across three sectors; no capable neighbor. Target-centered deficit and56-62ppt cutout/raw amplitudes. Historical253 events are screening statistics, not measured timing count.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 1 | 0 | 1329.0238243 | 0.010417 | 55.747 | usable; same-kind selection applies |
| 1 | 1 | 1332.5665308 | 0.010417 | 56.768 | usable; same-kind selection applies |
| 1 | 2 | 1336.1134253 | 0.010417 | 60.495 | usable; same-kind selection applies |
| 1 | 6 | 1350.2918981 | 0.010417 | 56.906 | usable; same-kind selection applies |
| 38 | 285 | 2339.1581439 | 0.003472 | 65.499 | usable; same-kind selection applies |
| 38 | 286 | 2342.7023435 | 0.003472 | 64.357 | usable; same-kind selection applies |
| 38 | 288 | 2349.7915677 | 0.003472 | 64.572 | usable; same-kind selection applies |
| 38 | 289 | 2353.3359850 | 0.003472 | 64.276 | usable; same-kind selection applies |
| 38 | 290 | 2356.8802599 | 0.003472 | 65.126 | usable; same-kind selection applies |
| 98 | 753 | 3997.9045538 | 0.001157 | 55.813 | usable; same-kind selection applies |
| 98 | 754 | 4001.4485625 | 0.001157 | 55.587 | usable; same-kind selection applies |
| 98 | 757 | 4012.0816396 | 0.001157 | 54.990 | usable; same-kind selection applies |
| 98 | 758 | 4015.6258855 | 0.001157 | 54.638 | usable; same-kind selection applies |
| 98 | 761 | 4026.2591449 | 0.001157 | 54.557 | usable; same-kind selection applies |
| 98 | 762 | 4029.8033523 | 0.001157 | 53.978 | usable; same-kind selection applies |
| 98 | 765 | 4040.4361945 | 0.001157 | 55.820 | usable; same-kind selection applies |
| 98 | 766 | 4043.9806979 | 0.001157 | 53.961 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s97.json, historical/diff_s97.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] For TIC407207285 the deciding revised cutout is revised-cutout/diff_revised-long-window.json and .png; historical extraction remains for comparison. Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R263. [Deciding evidence](../../evidence/177257211/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
