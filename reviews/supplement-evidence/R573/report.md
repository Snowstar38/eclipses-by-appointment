# TIC 295771108: PROBABLE

Full bounded physical review: **COMPLETE**. Physical outcome and catalogue novelty are separate; a known recovery is not a new addition.

1. **Raw repeated events.** 23 free-center local trapezoid measurements in quality-zero QLP SAP_FLUX; 23 centers enter timing, in sectors [93, 102]. Predictions locate windows and are not measurements. Flagged or uncovered windows are not clean nulls. Known ASAS-SN EA recovery, not a new addition. Deep eclipses and shallower phase-0.50052 events repeat, but the capable G=13.79 neighbor at 13.45 arcsec is unresolved: target and neighbor pixels lose 34.85 and 32.18 e-/s. Gaia predicts the other conjunction at phase 0.60848 +/-0.03919 (linear covariance allowance) versus measured 0.50052. This descriptive tension and blend leave geometry/ownership less secure.
2. **Timing and aliases.** Measured recurring-eclipse period P=1.7529583273 +/- 0.0000028609 days, epoch BTJD=3831.5290385. Epoch kind is the selected recurring eclipse; deeper-primary rank is not assumed. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. There are 18 adjacent same-kind pairs within sectors. Selected depths occur comparably in both cycle parities; doubling does not reveal alternating selected-event kinds. Halving interleaves a shallow secondary or sampled baseline, not the selected eclipse. Actual measured secondary-candidate phase=0.500519, depth=17.62 ppt, 24 usable fits. Actual phase scans and candidate fits are retained; secondary usability is a heuristic amplitude/local-scatter check, not calibrated significance. No exhaustive all-alias search or calibrated secondary-null confidence is asserted.
3. **Pixel attribution.** Fresh S39 difference stack contains 15 selected eclipses. Target WCS pixel=[7.468692683084559, 7.500484603313893], deficit centroid=[7.293330989219066, 7.725727339394298], descriptive offset=0.285 pixel. Neither offset nor image residual is a calibrated localization uncertainty or universal veto. All capable Gaia neighbors: Gaia 5782390478649218304: 13.45 arcsec, G=13.792, intrinsic-loss proxy=0.471. Capability is a G-band pairwise flux-budget proxy; color and aperture response limit precision. Intrinsic neighbor losses are never equated to diluted pixel fractional loss. Same-unit actual deficits and field morphology are independently recorded in [../terra-pixel-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/terra-pixel-audit.json); close blends retain uncertainty.
4. **Alternative reduction.** Reused, read and rerun TESScut primitive subtracts faint-pixel background, with symmetric local side windows and selected eclipse core; fresh target-centered 1x1/3x3/5x5 depths=87.57/83.34/73.83 ppt. QLP fitted median=105.13 ppt. Aperture, dilution and background response explain why these are not intrinsic-depth measurements. The cutout sector is absent from the retained QLP files. It is a distinct observing occasion on TESS and an alternative extraction of that sector; no direct same-sector QLP comparison is claimed. Distinct sectors remain occasions on one instrument.
5. **Gaia geometry.** Source 5782390478649219456; P=1.7530448129 +/- 7.2839124e-05 days, e=0.17145. Closest edge-on conjunction offset=-0.06051 days (-0.03452 phase), source-specific full covariance linear allowance=0.12954 days. Other conjunction relative phase=0.60848, linear phase allowance=0.03919. Full correlation matrix minimum eigenvalue=0.00700217. These linear allowances are descriptive, not calibrated significance. Near Gaia reference the projected epoch offset=0.10935 days, period-projection allowance alone=0.00562 days (ignores fit covariance/model systematics). Mass function=0.0423 solar masses; adopted primary mass=1.3, minimum secondary mass=0.519. Approximate central duration=4.32 hours versus observed median=3.45 hours. TIC radius, edge-on geometry and main-sequence secondary assumptions make this a plausibility test, not a fitted physical characterization. Impact parameter can shorten duration. Agreement does not by itself establish ownership.

**Deciding limitation:** Known ASAS-SN EA recovery, not a new addition. Deep eclipses and shallower phase-0.50052 events repeat, but the capable G=13.79 neighbor at 13.45 arcsec is unresolved: target and neighbor pixels lose 34.85 and 32.18 e-/s. Gaia predicts the other conjunction at phase 0.60848 +/-0.03919 (linear covariance allowance) versus measured 0.50052. This descriptive tension and blend leave geometry/ownership less secure.

**Next check:** Resolved eclipse photometry or multi-source PRF analysis of the 13.45-arcsec blend, and a joint orbit/eclipse fit.

Shared catalogue results are in [../../shared-catalogues/coverage-matrix.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/shared-catalogues/coverage-matrix.csv). Successful no-matches are distinct from failed queries; no exhaustive priority claim is made. TIC 295771108 is a known exact ASAS-SN EA recovery.

| Sector | Search cycle | Measured BTJD | Formal error d | Input allowance d | Depth ppt | Status |
|---|---:|---:|---:|---:|---:|---|
| 93 | 1256 | 3831.5292223 | 0.000250746 | 0.0011574 | 107.37 | used |
| 93 | 1257 | 3833.2816702 | 0.000231606 | 0.0011574 | 108.27 | used |
| 93 | 1258 | 3835.0348137 | 0.000263092 | 0.0011574 | 106.27 | used |
| 93 | 1259 | 3836.7879689 | 0.000281906 | 0.0011574 | 106.06 | used |
| 93 | 1260 | 3838.5404906 | 0.000256496 | 0.0011574 | 104.26 | used |
| 93 | 1261 | 3840.2938731 | 0.000275153 | 0.0011574 | 105.22 | used |
| 93 | 1263 | 3843.7997741 | 0.000327624 | 0.0011574 | 107.53 | used |
| 93 | 1264 | 3845.5529533 | 0.000243372 | 0.0011574 | 107.97 | used |
| 93 | 1265 | 3847.3058684 | 0.00028626 | 0.0011574 | 106.92 | used |
| 93 | 1266 | 3849.0588839 | 0.000270049 | 0.0011574 | 105.38 | used |
| 93 | 1267 | 3850.8113452 | 0.000260904 | 0.0011574 | 105.73 | used |
| 93 | 1268 | 3852.5644880 | 0.000291096 | 0.0011574 | 105.30 | used |
| 93 | 1269 | 3854.3175469 | 0.000327214 | 0.0011574 | 105.13 | used |
| 102 | 1426 | 4129.5326569 | 0.000243083 | 0.00115741 | 93.67 | used |
| 102 | 1427 | 4131.2852698 | 0.000214072 | 0.00115741 | 92.11 | used |
| 102 | 1429 | 4134.7911385 | 0.000219308 | 0.00115741 | 92.15 | used |
| 102 | 1430 | 4136.5442859 | 0.000224528 | 0.00115741 | 90.42 | used |
| 102 | 1433 | 4141.8022068 | 0.000252225 | 0.00115741 | 91.51 | used |
| 102 | 1434 | 4143.5554169 | 0.000261007 | 0.00115741 | 92.46 | used |
| 102 | 1435 | 4145.3080866 | 0.000413906 | 0.00115741 | 89.59 | used |
| 102 | 1436 | 4147.0611214 | 0.000233417 | 0.00115741 | 91.88 | used |
| 102 | 1437 | 4148.8140190 | 0.000247007 | 0.00115741 | 91.84 | used |
| 102 | 1438 | 4150.5676908 | 0.00032802 | 0.00115741 | 92.51 | used |

Evidence: [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/measurements.json), [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/raw-windows.csv), [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/raw-events.png), [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/fresh-pixels/diff_fresh.json)/png, historical originals, [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/identity-check.json), [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/alias-audit.json), [../secondary-measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/secondary-measurements.json), [../secondary-phase-scan.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/secondary-phase-scan.json)/png, [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/gaia-geometry.json), [../terra-pixel-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/terra-pixel-audit.json) and [../helper-audit.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/helper-audit.md). Exact sources and outputs are covered by [../SHA256SUMS.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/SHA256SUMS.json). The methods snapshot freezes the read methods without hashing a mutable canonical page.


Stable review key: R573.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/fresh-pixels/run.log)
- [historical/diff_s39.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/historical/diff_s39.json)
- [historical/diff_s39.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/historical/diff_s39.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/measurements.json)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/295771108/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch04/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
