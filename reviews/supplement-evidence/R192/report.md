# TIC 270260727: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 4 distinct eclipse events in selected sectors[67, 95]. The lead inspected raw-event plots and numeric fitting summaries. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=10.2916499025 ±0.0000194560d, reference primary epoch BTJD3129.8498677. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S27 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation1.281arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.715. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths4.589/5.482/5.221ppt, with 2 stacked events. QLP primary fitted median5.805ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36377229804026269184, P=10.2925042178±0.0014381993d, e=0.316068, omega=77.3278deg. Closest edge-on conjunction offset-0.205903d (-0.020005phase), full-SB1-covariance linear propagated Gaia uncertainty0.368617d at the measured epoch. Near-Gaia-reference projected eclipse offset0.021344d (photometric period projection allowance0.005175d). The approximate central duration4.34h vs observed median1.86h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Shallow localized repeated eclipses are resolved in sectors67 and95; raw scatter and trapezoid approximation limit precision. No capable neighbour within60arcsec under G flux budget.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 67 | 175 | 3129.8487012 | 0.001528 | 6.462 |
| 67 | 177 | 3150.4343910 | 0.001549 | 6.206 |
| 95 | 249 | 3891.4325817 | 0.001523 | 5.403 |
| 95 | 250 | 3901.7232234 | 0.001180 | 5.378 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp/QLP FITS; historical/diff_s27.json, historical/diff_s27.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R192. [Deciding evidence](../../evidence/270260727/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
