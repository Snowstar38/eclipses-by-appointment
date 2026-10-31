# TIC 22705959: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 6 distinct eclipse events in selected sectors [20, 47, 60]. The lead inspected the raw-event contact plot and numeric fit output. All fitted windows are preserved, including excluded anomalous windows described below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=11.3768104522 ±0.0000570223 d, reference primary epoch BTJD 1843.6400352. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S20 deficit peak [7, 8] vs target pixel [8, 8]; deficit-target separation 3.640 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.275. Capable neighbours: Gaia 930540059504937344: 39.75 arcsec, G 13.434, required fractional eclipse 0.884, pixel fractional loss 0.0327311642163424
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 133.056/122.988/111.050 ppt, with 2 stacked events. QLP primary fitted median 140.885 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 930540158288480128, P=11.3782568753±0.0013112244 d, e=0.042943, omega=14.8614 deg. Closest edge-on conjunction offset -0.160237 d (-0.014083 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.150148 d at the measured epoch. Near-Gaia-reference projected eclipse offset 0.024905 d (photometric period projection allowance 0.007299 d). The approximate central duration 7.23 h vs median local-model width 6.02 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** A capable neighbour at 39.75 arcsec is separated from the target deficit. The target sits near a pixel boundary: the global deficit peak rounds to an adjacent pixel, while the centroid is only 3.64 arcsec from the actual target. This is not evidence for a different source.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 20 | -1 | 1843.6392184 | 0.010417 | 141.995 |
| 20 | 1 | 1866.3938198 | 0.010417 | 142.452 |
| 47 | 64 | 2583.1331069 | 0.003472 | 141.338 |
| 47 | 66 | 2605.8861406 | 0.003472 | 139.703 |
| 60 | 96 | 2947.1906762 | 0.001157 | 140.432 |
| 60 | 97 | 2958.5674185 | 0.001157 | 140.064 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s20.json, historical/diff_s20.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R202. [Deciding evidence](../../evidence/22705959/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
