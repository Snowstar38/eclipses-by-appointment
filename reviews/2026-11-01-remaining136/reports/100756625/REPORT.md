# TIC 100756625: CONFIRMED

Full bounded physical review: **COMPLETE**. Physical outcome and catalogue novelty are separate; a known recovery is not a new addition.

1. **Raw repeated events.** 11 free-center local trapezoid measurements in quality-zero QLP SAP_FLUX; 11 centers enter timing, in sectors [6, 33, 98]. Predictions locate windows and are not measurements. Flagged or uncovered windows are not clean nulls. Eleven deep selected events recur; four shallow secondary candidates lie near phase 0.49956. Compact target deficit and no capable neighbor within 60 arcsec.
2. **Timing and aliases.** Measured recurring-eclipse period P=7.0214288325 +/- 0.0000066060 days, epoch BTJD=1473.3814673. Epoch kind is the selected recurring eclipse; deeper-primary rank is not assumed. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. There are 5 adjacent same-kind pairs within sectors. Selected depths occur comparably in both cycle parities; doubling does not reveal alternating selected-event kinds. Halving interleaves a shallow secondary or sampled baseline, not the selected eclipse. Actual measured secondary-candidate phase=0.499562, depth=4.57 ppt, 4 usable fits. Actual phase scans and candidate fits are retained; secondary usability is a heuristic amplitude/local-scatter check, not calibrated significance. No exhaustive all-alias search or calibrated secondary-null confidence is asserted.
3. **Pixel attribution.** Fresh S32 difference stack contains 4 selected eclipses. Target WCS pixel=[7.331913353204918, 7.398452520054139], deficit centroid=[7.337889737414169, 7.510039391148359], descriptive offset=0.112 pixel. Neither offset nor image residual is a calibrated localization uncertainty or universal veto. All capable Gaia neighbors: None under the approximate pairwise G-band flux screen within 60 arcsec.. Capability is a G-band pairwise flux-budget proxy; color and aperture response limit precision. Intrinsic neighbor losses are never equated to diluted pixel fractional loss. Same-unit actual deficits and field morphology are independently recorded in [../terra-pixel-audit.json](../../campaign/batch04/terra-pixel-audit.json); close blends retain uncertainty.
4. **Alternative reduction.** Reused, read and rerun TESScut primitive subtracts faint-pixel background, with symmetric local side windows and selected eclipse core; fresh target-centered 1x1/3x3/5x5 depths=71.60/71.64/70.78 ppt. QLP fitted median=62.88 ppt. Aperture, dilution and background response explain why these are not intrinsic-depth measurements. The cutout sector is absent from the retained QLP files. It is a distinct observing occasion on TESS and an alternative extraction of that sector; no direct same-sector QLP comparison is claimed. Distinct sectors remain occasions on one instrument.
5. **Gaia geometry.** Source 2903428510920674816; P=7.0205749150 +/- 0.0011569319 days, e=0.04190. Closest edge-on conjunction offset=0.05130 days (0.00731 phase), source-specific full covariance linear allowance=0.18513 days. Other conjunction relative phase=0.47572, linear phase allowance=0.02903. Full correlation matrix minimum eigenvalue=0.000540187. These linear allowances are descriptive, not calibrated significance. Near Gaia reference the projected epoch offset=-0.08021 days, period-projection allowance alone=0.00102 days (ignores fit covariance/model systematics). Mass function=0.010412 solar masses; adopted primary mass=0.994, minimum secondary mass=0.253. Approximate central duration=4.37 hours versus observed median=4.00 hours. TIC radius, edge-on geometry and main-sequence secondary assumptions make this a plausibility test, not a fitted physical characterization. Impact parameter can shorten duration. Agreement does not by itself establish ownership.

**Deciding limitation:** Eleven deep selected events recur; four shallow secondary candidates lie near phase 0.49956. Compact target deficit and no capable neighbor within 60 arcsec.

**Next check:** Optional resolved photometry and spectroscopy for improved localization and physical parameters.

Shared catalogue results are in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv). Successful no-matches are distinct from failed queries; no exhaustive priority claim is made. TIC 295771108 is a known exact ASAS-SN EA recovery.

| Sector | Search cycle | Measured BTJD | Formal error d | Input allowance d | Depth ppt | Status |
|---|---:|---:|---:|---:|---:|---|
| 6 | 0 | 1473.3801831 | 0.00018754 | 0.0104166 | 62.88 | used |
| 6 | 1 | 1480.4012630 | 0.000207135 | 0.0104166 | 62.32 | used |
| 6 | 2 | 1487.4222243 | 0.00039962 | 0.0104166 | 65.90 | used |
| 33 | 104 | 2203.6093144 | 0.000479887 | 0.00347218 | 74.57 | used |
| 33 | 105 | 2210.6316166 | 0.000226114 | 0.00347218 | 72.08 | used |
| 33 | 106 | 2217.6542908 | 0.000557113 | 0.00347218 | 70.63 | used |
| 33 | 107 | 2224.6743798 | 0.000277817 | 0.00347218 | 73.13 | used |
| 98 | 360 | 4001.0959270 | 0.000228484 | 0.00115742 | 59.39 | used |
| 98 | 362 | 4015.1387627 | 0.00018432 | 0.00115742 | 59.84 | used |
| 98 | 364 | 4029.1815326 | 0.000219175 | 0.00115742 | 57.56 | used |
| 98 | 366 | 4043.2242886 | 0.000318969 | 0.00115742 | 57.52 | used |

Evidence: [measurements.json](../../campaign/batch04/100756625/measurements.json), [raw-windows.csv](../../campaign/batch04/100756625/raw-windows.csv), [raw-events.png](../../campaign/batch04/100756625/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch04/100756625/fresh-pixels/diff_fresh.json)/png, historical originals, [../identity-check.json](../../campaign/batch04/identity-check.json), [../alias-audit.json](../../campaign/batch04/alias-audit.json), [../secondary-measurements.json](../../campaign/batch04/secondary-measurements.json), [../secondary-phase-scan.json](../../campaign/batch04/secondary-phase-scan.json)/png, [../gaia-geometry.json](../../campaign/batch04/gaia-geometry.json), [../terra-pixel-audit.json](../../campaign/batch04/terra-pixel-audit.json) and [../helper-audit.md](../../campaign/batch04/helper-audit.md). Exact sources and outputs are covered by [../SHA256SUMS.json](../../campaign/batch04/SHA256SUMS.json). The methods snapshot freezes the read methods without hashing a mutable canonical page.


Stable review key: R577.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch04/100756625/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch04/100756625/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch04/100756625/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch04/100756625/fresh-pixels/run.log)
- [historical/diff_s32.json](../../campaign/batch04/100756625/historical/diff_s32.json)
- [historical/diff_s32.png](../../campaign/batch04/100756625/historical/diff_s32.png)
- [historical/gaia.json](../../campaign/batch04/100756625/historical/gaia.json)
- [measurements.json](../../campaign/batch04/100756625/measurements.json)
- [raw-events.png](../../campaign/batch04/100756625/raw-events.png)
- [raw-windows.csv](../../campaign/batch04/100756625/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch04/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
