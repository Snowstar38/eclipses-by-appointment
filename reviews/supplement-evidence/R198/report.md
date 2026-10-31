# TIC 397178704: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 11 distinct eclipse events in selected sectors [10, 37, 90]. The lead inspected the raw-event contact plot and numeric fit output. All fitted windows are preserved, including excluded anomalous windows described below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=11.0096850472 ±0.0000177172 d, reference primary epoch BTJD 1578.4727019. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S65 deficit peak [8, 7] vs target pixel [8, 7]; deficit-target separation 2.858 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.676. Capable neighbours: Gaia 5233172429035086848: 45.82 arcsec, G 12.303, required fractional eclipse 0.467, pixel fractional loss 0.014161864689712712
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 153.625/140.797/97.827 ppt, with 4 stacked events. QLP primary fitted median 175.670 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 5233172532114305408, P=11.0086850571±0.0011569463 d, e=0.075755, omega=344.1277 deg. Closest edge-on conjunction offset 0.262492 d (0.023844 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.142187 d at the measured epoch. Near-Gaia-reference projected eclipse offset 0.154493 d (photometric period projection allowance 0.001913 d). The approximate central duration 10.12 h vs median local-model width 7.11 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating primary and secondary eclipses establish twice the historical 5.50484 d event spacing. Only deeper odd cycles enter the primary ephemeris. The historical stack mixes both kinds. Large PSF residual 0.676 reflects surrounding light rather than an off-target core; the one capable neighbour lies 45.82 arcsec away from the compact deficit.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 10 | 0 | 1572.9579597 | 0.010417 | 158.351 |
| 10 | 1 | 1578.4713392 | 0.010417 | 169.482 |
| 10 | 3 | 1589.4942243 | 0.010417 | 166.545 |
| 10 | 4 | 1594.9772619 | 0.010417 | 160.213 |
| 37 | 135 | 2316.1206625 | 0.003472 | 178.427 |
| 37 | 136 | 2321.6173962 | 0.003472 | 167.318 |
| 37 | 137 | 2327.1304672 | 0.003472 | 178.470 |
| 90 | 396 | 3752.8767815 | 0.001157 | 159.019 |
| 90 | 397 | 3758.3904114 | 0.001157 | 174.613 |
| 90 | 398 | 3763.8860307 | 0.001157 | 167.746 |
| 90 | 399 | 3769.4000221 | 0.001157 | 176.727 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s65.json, historical/diff_s65.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R198. [Deciding evidence](../../evidence/397178704/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
