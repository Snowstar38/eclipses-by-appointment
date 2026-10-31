# TIC 401138717: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 3 distinct eclipse events in selected sectors[38, 101]. The lead inspected raw-event plots and numeric fitting summaries. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 3 same-kind midtimes give P=19.7928484049 ±0.0000402097d, reference primary epoch BTJD2338.1094210. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S38 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation2.355arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.976. Capable neighbours: Gaia 6059375874538434688: 36.73 arcsec, G13.483, required fractional eclipse0.726, pixel fractional loss0.012136886658324623; Gaia 6059374397069672832: 45.88 arcsec, G13.250, required fractional eclipse0.606, pixel fractional loss0.0003268121523994738; Gaia 6059374397069669504: 55.21 arcsec, G8.266, required fractional eclipse0.111, pixel fractional loss0.00037149356202306885
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths70.076/37.681/12.642ppt, with 2 stacked events. QLP primary fitted median111.598ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36059375943257920000, P=19.7872890022±0.0033433246d, e=0.337643, omega=172.1929deg. Closest edge-on conjunction offset0.616978d (0.031181phase), full-SB1-covariance linear propagated Gaia uncertainty0.285169d at the measured epoch. Near-Gaia-reference projected eclipse offset0.072157d (photometric period projection allowance0.003941d). The approximate central duration13.30h vs observed median9.30h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Three capable neighbours and high scaled-out-image residual0.976 limit PSF precision. Target-centered compact loss and aperture-depth growth support attribution. Known EB42.73arcsec away has P0.363740d, distinct from19.79d. Gaia period differs by0.00556d, accounting for much of the accumulated conjunction offset; this physical tension is retained.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 38 | 38 | 2338.1081311 | 0.003472 | 111.598 |
| 38 | 39 | 2357.9035737 | 0.003472 | 120.005 |
| 101 | 128 | 4119.4657691 | 0.002631 | 86.769 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp/QLP FITS; historical/diff_s38.json, historical/diff_s38.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R187. [Deciding evidence](../../evidence/401138717/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
