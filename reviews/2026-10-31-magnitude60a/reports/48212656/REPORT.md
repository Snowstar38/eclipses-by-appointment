# TIC 48212656: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 15 distinct eclipse events in selected sectors[36, 62, 89]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=9.0832698961 ±0.0000108660d, reference eclipse epoch BTJD2290.1567712, kind: Deeper primary (odd half-period cycles). Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S62 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation0.773arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.179. Capable neighbours: Gaia 5463218573976102400: 45.22 arcsec, G13.926, required fractional eclipse0.509, pixel fractional loss0.010378443232646176
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths48.360/47.433/42.752ppt, with 5 stacked events. QLP selected-kind fitted median73.015ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35463218604039665408, P=9.0837171230±0.0011010123d, e=0.012056, omega=249.6383deg. Closest edge-on conjunction offset-0.076515d (-0.008423phase), full-SB1-covariance linear propagated Gaia uncertainty0.253510d at the measured epoch. Near-Gaia-reference projected eclipse offset0.016955d (photometric period projection allowance0.002271d). The approximate central duration8.20h vs observed median5.58h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating eclipses approximately40/73ppt establish doubled orbital period. Odd historical half-period cycles are deeper primaries and alone define ephemeris. Historical cutout mixes eclipse kinds.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 36 | 0 | 2285.6144732 | 0.003472 | 40.112 | usable; same-kind selection applies |
| 36 | 1 | 2290.1571543 | 0.003472 | 73.015 | usable; same-kind selection applies |
| 36 | 3 | 2299.2402837 | 0.003472 | 73.048 | usable; same-kind selection applies |
| 36 | 4 | 2303.7814680 | 0.003472 | 40.339 | usable; same-kind selection applies |
| 62 | 155 | 2989.5682938 | 0.001157 | 73.938 | usable; same-kind selection applies |
| 62 | 156 | 2994.1094979 | 0.001157 | 39.389 | usable; same-kind selection applies |
| 62 | 157 | 2998.6519402 | 0.001157 | 73.423 | usable; same-kind selection applies |
| 62 | 158 | 3003.1922367 | 0.001157 | 40.036 | usable; same-kind selection applies |
| 62 | 159 | 3007.7476989 | 60271.664713 | 69.865 | excluded singular timing fit |
| 62 | 160 | 3012.2751753 | 0.001157 | 38.834 | usable; same-kind selection applies |
| 89 | 316 | 3720.7710087 | 0.001157 | 39.192 | usable; same-kind selection applies |
| 89 | 317 | 3725.3140402 | 0.001157 | 71.449 | usable; same-kind selection applies |
| 89 | 318 | 3729.8537742 | 0.001157 | 39.552 | usable; same-kind selection applies |
| 89 | 319 | 3734.3962781 | 0.001157 | 72.160 | usable; same-kind selection applies |
| 89 | 321 | 3743.4798087 | 0.001157 | 71.532 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s62.json, historical/diff_s62.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R219. [Deciding evidence](../../evidence/48212656/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
