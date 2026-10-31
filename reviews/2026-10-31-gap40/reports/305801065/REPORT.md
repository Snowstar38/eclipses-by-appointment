# TIC 305801065: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 7 distinct eclipse events in selected sectors[15, 57, 85]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=6.0450293176 ±0.0000361616d, reference primary epoch BTJD1727.4094898. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S56 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation1.892arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.142. Capable neighbours: Gaia 2192612243770726016: 28.07 arcsec, G17.284, required fractional eclipse0.762, pixel fractional loss0.0049794454906507924; Gaia 2192612144989688192: 33.30 arcsec, G16.710, required fractional eclipse0.450, pixel fractional loss0.004025655733937976; Gaia 2192612144989688320: 54.57 arcsec, G16.272, required fractional eclipse0.302, pixel fractional loss0.0018812626929620051
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths4.343/4.217/4.030ppt, with 4 stacked events. QLP primary fitted median5.065ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32192612213709164416, P=6.0451741506±0.0003743317d, e=0.037874, omega=130.3501deg. Closest edge-on conjunction offset-0.072174d (-0.011939phase), full-SB1-covariance linear propagated Gaia uncertainty0.076707d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.040166d (photometric period projection allowance0.007992d). The approximate central duration16.20h vs observed median5.48h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** The shallow eclipse is clearly repeated with localized ingress/egress despite higher scatter in newer sectors. Three capable neighbours at28.07,33.30,54.57arcsec are separated from the compact target deficit. Depth depends on dilution and trapezoid shape; historical median3.8ppt is not a precision intrinsic depth.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 15 | 1 | 1727.4069331 | 0.010417 | 4.819 |
| 85 | 313 | 3613.4616142 | 0.005848 | 4.872 |
| 85 | 314 | 3619.5037444 | 0.003317 | 5.537 |
| 85 | 316 | 3631.5924011 | 0.003144 | 5.065 |
| 57 | 188 | 2857.8306942 | 0.003403 | 5.493 |
| 57 | 190 | 2869.9111189 | 0.003055 | 6.749 |
| 57 | 191 | 2875.9730302 | 0.002887 | 4.844 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, raw/QLP FITS; historical/diff_s56.json, historical/diff_s56.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R182. [Deciding evidence](../../evidence/305801065/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
