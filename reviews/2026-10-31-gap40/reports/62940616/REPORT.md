# TIC 62940616: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 7 distinct eclipse events in selected sectors [46, 72]. The lead inspected the raw-event contact plot and numeric fit output. All fitted windows are preserved, including excluded anomalous windows described below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=4.9985872939 ±0.0000131921 d, reference primary epoch BTJD 2556.4440266. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S46 deficit peak [8, 7] vs target pixel [8, 7]; deficit-target separation 4.310 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.145. Capable neighbours: Gaia 3600574305187842176: 22.67 arcsec, G 13.447, required fractional eclipse 0.329, pixel fractional loss 0.04157460368672594
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 47.812/44.599/42.097 ppt, with 4 stacked events. QLP primary fitted median 52.594 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 3600574305187842304, P=4.9982995596±0.0002208867 d, e=0.031476, omega=231.2156 deg. Closest edge-on conjunction offset 0.087414 d (0.017489 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.100248 d at the measured epoch. Near-Gaia-reference projected eclipse offset -0.037462 d (photometric period projection allowance 0.005725 d). The approximate central duration 6.60 h vs median local-model width 4.91 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** One capable neighbour at 22.67 arcsec requires a 0.329 fractional eclipse to explain the signal, but the lost-light centroid lies 0.205 pixel from the target versus 1.33 pixels from that neighbour, displaced away from it. Its pixel fractional loss 0.0416 is a blended-pixel value and does not measure the neighbour intrinsic eclipse depth. The target-centered depth increases in the 1x1 aperture, consistent with target dilution in larger apertures. TESS resolution and G-to-TESS colour differences limit attribution precision.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 46 | 0 | 2556.4439771 | 0.003473 | 52.594 |
| 46 | 1 | 2561.4422765 | 0.003473 | 53.064 |
| 46 | 3 | 2571.4397492 | 0.003473 | 52.700 |
| 46 | 4 | 2576.4387841 | 0.003473 | 53.194 |
| 72 | 142 | 3266.2436945 | 0.001158 | 50.712 |
| 72 | 143 | 3271.2418776 | 0.001158 | 50.489 |
| 72 | 144 | 3276.2404587 | 0.001158 | 50.745 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s46.json, historical/diff_s46.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R203. [Deciding evidence](../../evidence/62940616/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
