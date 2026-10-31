# TIC 152400959: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 11 distinct eclipse events in selected sectors[7, 34, 88]. The lead inspected raw-event plots and numeric fitting summaries. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 same-kind midtimes give P=5.5128574495 ±0.0000063398d, reference primary epoch BTJD1492.1132318. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S7 deficit peak[8, 8] vs target pixel[8, 7]; deficit-target separation4.210arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.959. Capable neighbours: Gaia 5594494902225244160: 55.47 arcsec, G10.157, required fractional eclipse0.066, pixel fractional loss0.0003869186084721213; Gaia 5594494902225244672: 58.02 arcsec, G10.321, required fractional eclipse0.068, pixel fractional loss0.0003869186084721213
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths50.239/25.011/9.987ppt, with 4 stacked events. QLP primary fitted median54.372ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35594495275878677632, P=5.5134762690±0.0002135603d, e=0.241108, omega=1.8534deg. Closest edge-on conjunction offset-0.071963d (-0.013052phase), full-SB1-covariance linear propagated Gaia uncertainty0.052295d at the measured epoch. Near-Gaia-reference projected eclipse offset0.051801d (photometric period projection allowance0.001268d). The approximate central duration5.76h vs observed median3.98h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Known EB27.09arcsec away at0.257384d differs from5.513d signal. Two capable neighbours and residual0.959 limit PSF precision; compact target-centered deficit and small-aperture eclipse support attribution.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 7 | -1 | 1492.1103737 | 0.010417 | 49.358 |
| 7 | 0 | 1497.6273109 | 0.010417 | 54.372 |
| 7 | 2 | 1508.6524440 | 0.010417 | 48.896 |
| 34 | 133 | 2230.8347011 | 0.003472 | 51.406 |
| 34 | 134 | 2236.3504424 | 0.003472 | 50.678 |
| 34 | 136 | 2247.3754145 | 0.003472 | 56.803 |
| 34 | 137 | 2252.8870730 | 0.003472 | 50.158 |
| 88 | 399 | 3697.2551241 | 0.001157 | 55.871 |
| 88 | 400 | 3702.7694013 | 0.001157 | 56.341 |
| 88 | 401 | 3708.2821947 | 0.001157 | 55.227 |
| 88 | 402 | 3713.7952555 | 0.001157 | 54.376 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp/QLP FITS; historical/diff_s07.json, historical/diff_s07.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R190. [Deciding evidence](../../evidence/152400959/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
