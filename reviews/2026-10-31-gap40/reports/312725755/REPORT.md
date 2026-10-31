# TIC 312725755: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 5 distinct eclipse events in selected sectors [19, 45, 73]. The lead inspected representative raw-event plots and numeric fit output; the helper independently audited timing and pixel exceptions. All fitted windows are preserved. Timing includes historical cycles [0, 1, 63, 64, 130]; excluded cycles [] remain in the raw evidence. Fits with midpoint covariance uncertainty larger than the seeded eclipse duration are excluded as unconstrained, not treated as timing measurements. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 retained reference-eclipse midtimes give P=11.3049942194 +/-0.0000343148 d, observed reference eclipse epoch BTJD 1823.1102837. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S19 deficit peak [7, 7] vs target pixel [7, 7]; deficit-target separation 4.360 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.563. Capable neighbours: Gaia 3451087895436075136: 38.86 arcsec, G 14.703, required fractional eclipse 0.813, pixel fractional loss 0.00961169700126623
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 43.459/44.495/41.201 ppt, with 2 stacked events. QLP retained-reference fitted median 47.711 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 3451087861074378752, P=11.3048869586+/-0.0034114104 d, e=0.136183, omega=311.3174 deg. Closest edge-on conjunction offset 0.134039 d (0.011857 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.514953 d at the measured epoch. Near-Gaia-reference projected eclipse offset 0.120417 d (photometric period projection allowance 0.004358 d). The approximate central duration 11.87 h vs median local-model width 8.50 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Five fitted repeating eclipses span S19,45,73. The measured widths are long but compatible with approximate Gaia/TIC geometry; intrinsic depths and stellar parameters need detailed modeling.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 19 | 0 | 1823.1124593 | 0.010417 | 47.711 |
| 19 | 1 | 1834.4206438 | 0.010417 | 46.795 |
| 45 | 63 | 2535.3256905 | 0.003472 | 49.215 |
| 45 | 64 | 2546.6274894 | 0.003472 | 49.857 |
| 73 | 130 | 3292.7596228 | 0.001157 | 43.994 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s19.json, historical/diff_s19.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R214. [Deciding evidence](../../evidence/312725755/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
