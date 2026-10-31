# TIC 466690912: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 32 distinct eclipse events in selected sectors[27, 94, 103]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 32 same-kind midtimes give P=2.1159658358 Ãƒâ€šÃ‚±0.0000011526d, reference eclipse epoch BTJD2037.8376563, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S66 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation6.475arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.677. Capable neighbours: Gaia 6366373024352389504: 49.13 arcsec, G15.303, required fractional eclipse0.883, pixel fractional loss0.011787977275723208
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths31.335/31.036/29.192ppt, with 12 stacked events. QLP selected-kind fitted median29.016ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36366373058712130432, P=2.1159665560Ãƒâ€šÃ‚±0.0000929679d, e=0.040428, omega=2.4544deg. Closest edge-on conjunction offset0.022977d (0.010859phase), full-SB1-covariance linear propagated Gaia uncertainty0.073318d at the measured epoch. Near-Gaia-reference projected eclipse offset0.023538d (photometric period projection allowance0.000898d). The approximate central duration5.24h vs observed median5.25h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated flat-bottom eclipses with changing raw sector depths19-35ppt; aperture and baseline dependence is retained. Capable neighbor49.1arcsec away is distinct from the deficit core. Observed duration5.25h agrees approximate central estimate5.24h to the precision of its assumptions.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 27 | 0 | 2037.8361783 | 0.003472 | 34.782 | usable; same-kind selection applies |
| 27 | 1 | 2039.9533091 | 0.003472 | 34.775 | usable; same-kind selection applies |
| 27 | 2 | 2042.0690102 | 0.003472 | 34.784 | usable; same-kind selection applies |
| 27 | 3 | 2044.1840321 | 0.003472 | 35.232 | usable; same-kind selection applies |
| 27 | 4 | 2046.3011911 | 0.003472 | 35.430 | usable; same-kind selection applies |
| 27 | 6 | 2050.5317487 | 0.003472 | 34.694 | usable; same-kind selection applies |
| 27 | 7 | 2052.6482193 | 0.003472 | 34.085 | usable; same-kind selection applies |
| 27 | 8 | 2054.7637686 | 0.003472 | 35.224 | usable; same-kind selection applies |
| 27 | 9 | 2056.8805472 | 0.003472 | 34.224 | usable; same-kind selection applies |
| 27 | 10 | 2058.9964185 | 0.003472 | 35.110 | usable; same-kind selection applies |
| 94 | 860 | 3857.5697483 | 0.001157 | 26.507 | usable; same-kind selection applies |
| 94 | 861 | 3859.6848160 | 0.001157 | 27.726 | usable; same-kind selection applies |
| 94 | 862 | 3861.8012077 | 0.001157 | 27.342 | usable; same-kind selection applies |
| 94 | 863 | 3863.9164637 | 0.001157 | 27.763 | usable; same-kind selection applies |
| 94 | 864 | 3866.0331157 | 0.001157 | 27.412 | usable; same-kind selection applies |
| 94 | 865 | 3868.1484324 | 0.001306 | 24.010 | usable; same-kind selection applies |
| 94 | 866 | 3870.2657924 | 0.001756 | 25.667 | usable; same-kind selection applies |
| 94 | 867 | 3872.3807083 | 0.001157 | 27.539 | usable; same-kind selection applies |
| 94 | 868 | 3874.4974663 | 0.002350 | 27.969 | usable; same-kind selection applies |
| 94 | 869 | 3876.6133249 | 0.001157 | 27.617 | usable; same-kind selection applies |
| 94 | 870 | 3878.7283753 | 0.001157 | 27.917 | usable; same-kind selection applies |
| 103 | 1000 | 4153.8028232 | 0.001521 | 30.062 | usable; same-kind selection applies |
| 103 | 1001 | 4155.9189734 | 0.001157 | 32.520 | usable; same-kind selection applies |
| 103 | 1002 | 4158.0361246 | 0.001157 | 32.474 | usable; same-kind selection applies |
| 103 | 1003 | 4160.1507115 | 0.001157 | 32.529 | usable; same-kind selection applies |
| 103 | 1004 | 4162.2671677 | 0.001157 | 32.057 | usable; same-kind selection applies |
| 103 | 1005 | 4164.3811602 | 0.001157 | 32.014 | usable; same-kind selection applies |
| 103 | 1006 | 4166.4984552 | 0.001996 | 19.166 | usable; same-kind selection applies |
| 103 | 1007 | 4168.6147203 | 0.001157 | 22.145 | usable; same-kind selection applies |
| 103 | 1009 | 4172.8466735 | 0.001157 | 22.417 | usable; same-kind selection applies |
| 103 | 1010 | 4174.9625320 | 0.001157 | 22.742 | usable; same-kind selection applies |
| 103 | 1011 | 4177.0772644 | 0.001157 | 20.903 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s66.json, historical/diff_s66.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R242. [Deciding evidence](../../evidence/466690912/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
