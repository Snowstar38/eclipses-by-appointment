# TIC 219033622: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 4 distinct eclipse events in selected sectors [15, 23]. The lead inspected representative raw-event plots and numeric fit output; the helper independently audited timing and pixel exceptions. All fitted windows are preserved. Timing includes historical cycles [0, 2, 31]; excluded cycles [32] remain in the raw evidence. Fits with midpoint covariance uncertainty larger than the seeded eclipse duration are excluded as unconstrained, not treated as timing measurements. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 3 retained reference-eclipse midtimes give P=6.9464765822 +/-0.0004245408 d, observed reference eclipse epoch BTJD 1713.8087063. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S16 deficit peak [7, 7] vs target pixel [7, 7]; deficit-target separation 2.063 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.101. Capable neighbours: None within 60 arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 127.885/127.103/125.218 ppt, with 4 stacked events. QLP retained-reference fitted median 132.326 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 1558979055781011712, P=6.9468940696+/-0.0004207749 d, e=0.016919, omega=104.5859 deg. Closest edge-on conjunction offset -0.043887 d (-0.006317 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.093470 d at the measured epoch. Near-Gaia-reference projected eclipse offset 0.035853 d (photometric period projection allowance 0.081087 d). The approximate central duration 6.09 h vs median local-model width 3.02 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Three constrained same-kind events in S15 and S23 determine the ephemeris; S23 cycle32 is retained as a raw repeat but excluded from timing because sparse sampling leaves its egress poorly constrained. S76 did not supply a usable selected event window and is not a clean non-detection. The independent S16 cutout contains four repeating deep target-centered deficits. The timing baseline is shorter than the available sector list suggests.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 15 | 0 | 1713.8098089 | 0.010416 | 138.270 |
| 15 | 2 | 1727.7004809 | 0.010416 | 132.326 |
| 23 | 31 | 1929.1495564 | 0.010417 | 131.866 |
| 23 | 32 | 1936.0971100 | 0.010417 | 138.976 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s16.json, historical/diff_s16.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R213. [Deciding evidence](../../evidence/219033622/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
