# TIC 343926224: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 7 distinct eclipse events in selected sectors [15, 76, 84]. The lead inspected the raw-event contact plot and numeric fit output. All fitted windows are preserved, including excluded anomalous windows described below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=10.7289779063 ±0.0001985830 d, reference primary epoch BTJD 1716.2856364. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S76 deficit peak [8, 7] vs target pixel [8, 7]; deficit-target separation 1.439 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.350. Capable neighbours: Gaia 2189412291279426432: 55.00 arcsec, G 13.916, required fractional eclipse 0.414, pixel fractional loss 0.003238694850407246
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 34.297/34.868/34.349 ppt, with 3 stacked events. QLP primary fitted median 42.292 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 2189412256919685888, P=10.7249538611±0.0028660106 d, e=0.214758, omega=124.7057 deg. Closest edge-on conjunction offset 0.251123 d (0.023415 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.280852 d at the measured epoch. Near-Gaia-reference projected eclipse offset -0.247858 d (photometric period projection allowance 0.024624 d). The approximate central duration 11.18 h vs median local-model width 7.49 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Five clean primary repeats determine the ephemeris. S76 historical cycle 154 has structured excursions and an anomalously weak fitted dip; S84 cycle 176 has a broad distorted profile. Both remain in raw-windows.csv and plots but are excluded from the timing fit. The capable neighbour at 55.00 arcsec is separated from the compact target deficit. Aperture and local baseline variations limit depth precision. The retained timing fit has reduced chi-square 18.08; residual timing scatter materially inflates the stated period error and shows model/baseline limitations.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 15 | 0 | 1716.2949834 | 0.010417 | 41.496 |
| 15 | 1 | 1727.0163759 | 0.010417 | 25.970 |
| 76 | 154 | 3368.5876261 | 0.002145 | 14.410 |
| 76 | 155 | 3379.2842908 | 0.002003 | 47.405 |
| 76 | 156 | 3389.9973168 | 0.001781 | 46.416 |
| 84 | 175 | 3593.8740337 | 0.004303 | 42.292 |
| 84 | 176 | 3604.6250638 | 0.006209 | 68.147 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s76.json, historical/diff_s76.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R195. [Deciding evidence](../../evidence/343926224/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
