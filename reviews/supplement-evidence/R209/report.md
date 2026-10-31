# TIC 37948318: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section 2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 9 distinct eclipse events in selected sectors [5, 32, 98]. The lead inspected representative raw-event plots and numeric fit output; the helper independently audited timing and pixel exceptions. All fitted windows are preserved. Timing includes historical cycles [0, 1, 2, 91, 317, 319, 321, 322]; excluded cycles [93] remain in the raw evidence. Fits with midpoint covariance uncertainty larger than the seeded eclipse duration are excluded as unconstrained, not treated as timing measurements. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 retained reference-eclipse midtimes give P=8.0567270177 +/-0.0000120865 d, observed reference eclipse epoch BTJD 1444.2226216. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S98 deficit peak [8, 7] vs target pixel [7, 7]; deficit-target separation 15.096 arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual 0.197. Capable neighbours: Gaia 3191831957073992960: 53.65 arcsec, G 13.726, required fractional eclipse 0.080, pixel fractional loss 0.0009833145507867729
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths 11.870/11.463/10.353 ppt, with 6 stacked events. QLP retained-reference fitted median 11.182 ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3 3191832060153207296, P=8.0560480995+/-0.0007371091 d, e=0.027806, omega=108.0360 deg. Closest edge-on conjunction offset 0.067844 d (0.008422 phase), full-SB1-covariance linear propagated Gaia uncertainty 0.109490 d at the measured epoch. Near-Gaia-reference projected eclipse offset -0.021094 d (photometric period projection allowance 0.001583 d). The approximate central duration 8.86 h vs median local-model width 3.58 h is only an approximate comparison; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** The historical absolute target-to-deficit offset is 15.1 arcsec (0.719 pixel), while light-to-deficit separation is 3.51 arcsec; these are distinct comparisons. The capable G13.73 neighbour is 53.65 arcsec away and opposite the deficit displacement. Independent per-event pixel checks find target-pixel losses 9.03-10.59 electrons/s against 0.185-0.437 at that neighbour in cycles317,319,321. This supports the target over the capable neighbour at TESS resolution, with an uncalibrated absolute-centroid systematic and residual crowding uncertainty. Historical cycles316/318 have common-mode excursions and are not individually decisive. QLP cycle93 has singular timing covariance and is excluded from timing.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 5 | 0 | 1444.2231929 | 0.010417 | 11.186 |
| 5 | 1 | 1452.2757562 | 0.010417 | 10.988 |
| 5 | 2 | 1460.3370736 | 0.010417 | 10.984 |
| 32 | 91 | 2177.3849525 | 0.003472 | 11.022 |
| 32 | 93 | 2193.5064324 | 217601.015807 | 8.345 |
| 98 | 317 | 3998.2062823 | 0.001157 | 11.182 |
| 98 | 319 | 4014.3179369 | 0.001157 | 11.202 |
| 98 | 321 | 4030.4314268 | 0.001157 | 11.427 |
| 98 | 322 | 4038.4886732 | 0.001825 | 11.181 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp QLP FITS; historical/diff_s98.json, historical/diff_s98.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R209. [Deciding evidence](../../evidence/37948318/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
