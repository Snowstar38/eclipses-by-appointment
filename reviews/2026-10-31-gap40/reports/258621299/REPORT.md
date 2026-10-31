# TIC 258621299: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 17 distinct eclipse events in selected sectors[20, 60, 73]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 9 same-kind midtimes give P=6.9859704688 ±0.0000173254d, reference primary epoch BTJD1845.3682206. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S20 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation3.195arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.058. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths143.337/141.526/141.187ppt, with 6 stacked events. QLP primary fitted median179.670ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3971297198904724608, P=6.9861245600±0.0003177162d, e=0.040129, omega=343.5407deg. Closest edge-on conjunction offset0.062467d (0.008942phase), full-SB1-covariance linear propagated Gaia uncertainty0.067290d at the measured epoch. Near-Gaia-reference projected eclipse offset0.094518d (photometric period projection allowance0.003604d). The approximate central duration8.56h vs observed median6.53h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating eclipses (primary median approximately180ppt, secondary131ppt) establish orbital period twice the historical3.49299d event spacing. Only deeper even cycles enter the reported primary ephemeris. Historical S20 difference image mixes both eclipse kinds, so its aperture depth is a mixture.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 20 | 0 | 1845.3682888 | 0.010417 | 179.670 |
| 20 | 1 | 1848.8567264 | 0.010417 | 116.069 |
| 20 | 2 | 1852.3539485 | 0.010417 | 178.199 |
| 20 | 4 | 1859.3410816 | 0.010417 | 176.315 |
| 20 | 5 | 1862.8328313 | 0.010417 | 130.696 |
| 20 | 6 | 1866.3264837 | 0.010417 | 177.674 |
| 73 | 413 | 3287.9694596 | 0.001157 | 139.998 |
| 73 | 414 | 3291.4639324 | 0.001157 | 183.540 |
| 73 | 415 | 3294.9567630 | 0.001157 | 131.867 |
| 73 | 416 | 3298.4502901 | 0.001157 | 182.875 |
| 73 | 419 | 3308.9292613 | 0.001157 | 132.982 |
| 60 | 313 | 2938.6728898 | 0.001157 | 130.343 |
| 60 | 314 | 2942.1655592 | 0.001157 | 180.486 |
| 60 | 315 | 2945.6586929 | 0.001157 | 130.856 |
| 60 | 316 | 2949.1514530 | 0.001157 | 180.033 |
| 60 | 318 | 2956.1376017 | 0.001157 | 179.649 |
| 60 | 319 | 2959.6307865 | 0.001157 | 130.113 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, raw/QLP FITS; historical/diff_s20.json, historical/diff_s20.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R184. [Deciding evidence](../../evidence/258621299/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
