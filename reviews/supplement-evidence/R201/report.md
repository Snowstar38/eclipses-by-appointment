# TIC 7446763: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 23 distinct eclipse events in selected sectors [4, 32, 98]. The lead inspected the raw-event contact plot and numeric fit output. All fitted windows are preserved, including excluded anomalous windows described below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 12 same-kind midtimes give P=5.9119066682 ±0.0000054818 d, reference primary epoch BTJD 1415.6444465. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S98 deficit peak [8, 7] vs target pixel [8, 7]; deficit-target separation 1.268 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.099. Capable neighbours: None within 60 arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 52.841/52.588/50.932 ppt, with 17 stacked events. QLP primary fitted median 72.076 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 4798935876591849088, P=5.9116154455±0.0003030802 d, e=0.013640, omega=116.4877 deg. Closest edge-on conjunction offset 0.070541 d (0.011933 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.077901 d at the measured epoch. Near-Gaia-reference projected eclipse offset 0.019868 d (photometric period projection allowance 0.000954 d). The approximate central duration 9.34 h vs median local-model width 7.52 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Primary eclipses are approximately twice secondary depth. Only deeper odd historical half-period cycles determine the ephemeris; the reported orbital period doubles the historical 2.95595 d spacing. Historical S98 aperture stack mixes both eclipse kinds.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 4 | 0 | 1412.6894404 | 0.010417 | 36.543 |
| 4 | 1 | 1415.6441526 | 0.010417 | 72.127 |
| 4 | 5 | 1427.4690252 | 0.010417 | 72.752 |
| 4 | 6 | 1430.4248834 | 0.010417 | 36.054 |
| 4 | 7 | 1433.3798852 | 0.010417 | 72.024 |
| 32 | 258 | 2175.3254133 | 0.003472 | 36.891 |
| 32 | 259 | 2178.2807585 | 0.003472 | 74.305 |
| 32 | 260 | 2181.2370527 | 0.003472 | 36.752 |
| 32 | 261 | 2184.1925623 | 0.003472 | 73.972 |
| 32 | 263 | 2190.1041470 | 0.003472 | 74.638 |
| 32 | 264 | 2193.0601727 | 0.003472 | 36.990 |
| 32 | 265 | 2196.0155599 | 0.003472 | 74.799 |
| 32 | 266 | 2198.9721952 | 0.003472 | 35.844 |
| 98 | 874 | 3996.1925164 | 0.001157 | 33.345 |
| 98 | 875 | 3999.1475663 | 0.001157 | 66.890 |
| 98 | 876 | 4002.1040387 | 0.001157 | 33.429 |
| 98 | 879 | 4010.9714862 | 0.001157 | 67.728 |
| 98 | 880 | 4013.9273533 | 0.001157 | 34.299 |
| 98 | 881 | 4016.8680979 | 116856.320084 | 66.082 |
| 98 | 884 | 4025.7512338 | 0.001157 | 33.870 |
| 98 | 885 | 4028.7075696 | 0.001157 | 67.853 |
| 98 | 889 | 4040.5307153 | 0.001157 | 68.095 |
| 98 | 890 | 4043.4883661 | 0.001157 | 34.008 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s98.json, historical/diff_s98.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R201. [Deciding evidence](../../evidence/7446763/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
