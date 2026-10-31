# TIC 265350422: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 5 distinct eclipse events in selected sectors[61, 99]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=8.4481707258 ±0.0000128420d, reference primary epoch BTJD2970.8043462. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S61 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation3.580arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.264. Capable neighbours: Gaia 577614316095585920: 32.85 arcsec, G16.170, required fractional eclipse0.566, pixel fractional loss0.0026182148905397186; Gaia 577614689757476480: 42.38 arcsec, G16.539, required fractional eclipse0.793, pixel fractional loss0.001448830988856897; Gaia 577614316096822528: 51.78 arcsec, G13.539, required fractional eclipse0.057, pixel fractional loss0.0014103835015173963
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths8.432/7.145/6.256ppt, with 3 stacked events. QLP primary fitted median7.800ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3577614689757449728, P=8.4481578354±0.0007776419d, e=0.010725, omega=80.7600deg. Closest edge-on conjunction offset-0.006714d (-0.000795phase), full-SB1-covariance linear propagated Gaia uncertainty0.249030d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.010659d (photometric period projection allowance0.003930d). The approximate central duration4.96h vs observed median1.65h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Three G-band-capable neighbours at 32.85, 42.38 and 51.78 arcsec lie away from the compact deficit on the target. The target-centered dip grows rather than vanishes in the small aperture. No calibrated centroid confidence ellipse is available.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 99 | 299 | 4052.1714299 | 0.001157 | 7.562 |
| 99 | 301 | 4069.0653296 | 0.001157 | 7.657 |
| 61 | 171 | 2970.8035555 | 0.001157 | 8.165 |
| 61 | 172 | 2979.2546286 | 0.001305 | 7.800 |
| 61 | 173 | 2987.6989232 | 0.001629 | 8.287 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, raw/QLP FITS; historical/diff_s61.json, historical/diff_s61.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R177. [Deciding evidence](../../evidence/265350422/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
