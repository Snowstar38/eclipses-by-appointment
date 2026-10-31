# TIC 309558046: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 9 distinct eclipse events in selected sectors[1, 37, 90]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass with disclosed cycle assumptions.** 6 same-kind midtimes give P=13.0830020618 ±0.0000240012d, reference eclipse epoch BTJD1331.6469978, kind: Deeper primary (even historical half-period cycles). Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S9 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation2.695arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.165. Capable neighbours: Gaia 5277988591691031808: 34.66 arcsec, G15.095, required fractional eclipse0.291, pixel fractional loss0.00740682275584591; Gaia 5277988660410508160: 41.05 arcsec, G16.170, required fractional eclipse0.751, pixel fractional loss0.00817955277592489; Gaia 5277988660410508928: 54.10 arcsec, G16.233, required fractional eclipse0.794, pixel fractional loss0.007053373948642565
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths13.627/14.520/14.475ppt, with 4 stacked events. Historical outputs are retained as measured pipeline evidence. QLP selected-kind fitted median26.962ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35277988587391544320, P=13.0837683530±0.0023013833d, e=0.018445, omega=309.8190deg. Closest edge-on conjunction offset0.062058d (0.004743phase), full-SB1-covariance linear propagated Gaia uncertainty0.209431d at the measured epoch. Near-Gaia-reference projected eclipse offset0.117231d (photometric period projection allowance0.001728d). The approximate central duration17.77h vs observed median14.32h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating eclipses approximately27/17ppt establish orbital period twice historical SAP half period. Even half-period cycles are deeper primaries and alone define ephemeris. Historical cutout stacks mixed eclipse kinds.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 1 | 0 | 1331.6417226 | 0.010416 | 27.658 | usable; same-kind selection applies |
| 1 | 2 | 1344.7258353 | 0.010416 | 26.267 | usable; same-kind selection applies |
| 1 | 3 | 1351.2669693 | 0.024253 | 16.592 | usable; same-kind selection applies |
| 37 | 150 | 2312.8723630 | 0.003472 | 28.847 | usable; same-kind selection applies |
| 37 | 152 | 2325.9567397 | 0.003472 | 28.504 | usable; same-kind selection applies |
| 90 | 370 | 3752.0006882 | 0.002552 | 24.395 | usable; same-kind selection applies |
| 90 | 371 | 3758.5501810 | 0.003074 | 17.174 | usable; same-kind selection applies |
| 90 | 372 | 3765.0864708 | 0.002348 | 25.496 | usable; same-kind selection applies |
| 90 | 373 | 3771.6317568 | 0.002008 | 16.951 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): ../helper/pixel-identity-audit.json, ../helper/same-sector-refits.json, ../helper/314047448-measured-diff.json, ../helper/48108063-measured-diff.json; measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s09.json, historical/diff_s09.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R252. [Deciding evidence](../../evidence/309558046/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
