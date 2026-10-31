# TIC 423657976: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[37, 64]. The lead inspected raw-event plots and numeric fitting summaries. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=6.6164167932 ±0.0000164775d, reference primary epoch BTJD2310.5996711. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S37 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation1.183arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.050. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths84.471/82.835/81.952ppt, with 4 stacked events. QLP primary fitted median93.973ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36194789076579972992, P=6.6172062581±0.0008867054d, e=0.023556, omega=59.1528deg. Closest edge-on conjunction offset-0.245165d (-0.037050phase), full-SB1-covariance linear propagated Gaia uncertainty0.251243d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.016220d (photometric period projection allowance0.004778d). The approximate central duration5.70h vs observed median4.00h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated isolated eclipses with stable approximately94ppt QLP depth. No capable neighbour within60arcsec under approximate G flux budget.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 37 | 111 | 2310.5996425 | 0.003472 | 95.470 |
| 37 | 112 | 2317.2161820 | 0.003472 | 95.141 |
| 37 | 113 | 2323.8322489 | 0.003472 | 92.723 |
| 37 | 114 | 2330.4490935 | 0.003472 | 93.255 |
| 64 | 222 | 3045.0219829 | 0.001157 | 93.568 |
| 64 | 223 | 3051.6382109 | 0.001157 | 93.389 |
| 64 | 224 | 3058.2551511 | 0.001157 | 95.504 |
| 64 | 225 | 3064.8708985 | 0.001157 | 94.378 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp/QLP FITS; historical/diff_s37.json, historical/diff_s37.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R194. [Deciding evidence](../../evidence/423657976/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
