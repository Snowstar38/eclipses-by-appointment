# TIC 322679338: CONFIRMED

Full bounded physical review: **COMPLETE**. Physical outcome and catalogue novelty are separate; a known recovery is not a new addition.

1. **Raw repeated events.** 4 free-center local trapezoid measurements in quality-zero QLP SAP_FLUX; 4 centers enter timing, in sectors [60, 73]. Predictions locate windows and are not measurements. Flagged or uncovered windows are not clean nulls. Four deep events form consecutive pairs in S60/S73. Two shallow secondary candidates in S19 lie at actual phase 0.54415, with other-sector confirmation limited. The capable neighbor at 54.93 arcsec is separate from the target deficit.
2. **Timing and aliases.** Measured recurring-eclipse period P=15.9220326620 +/- 0.0000525550 days, epoch BTJD=2942.7593854. Epoch kind is the selected recurring eclipse; deeper-primary rank is not assumed. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. There are 2 adjacent same-kind pairs within sectors. Selected depths occur comparably in both cycle parities; doubling does not reveal alternating selected-event kinds. Halving interleaves a shallow secondary or sampled baseline, not the selected eclipse. Actual measured secondary-candidate phase=0.544147, depth=5.39 ppt, 2 usable fits. Actual phase scans and candidate fits are retained; secondary usability is a heuristic amplitude/local-scatter check, not calibrated significance. No exhaustive all-alias search or calibrated secondary-null confidence is asserted.
3. **Pixel attribution.** Fresh S20 difference stack contains 2 selected eclipses. Target WCS pixel=[7.134597425825657, 7.989513142108965], deficit centroid=[7.426056128055689, 8.0361007363305], descriptive offset=0.295 pixel. Neither offset nor image residual is a calibrated localization uncertainty or universal veto. All capable Gaia neighbors: Gaia 1004675112045220352: 54.93 arcsec, G=14.588, intrinsic-loss proxy=0.485. Capability is a G-band pairwise flux-budget proxy; color and aperture response limit precision. Intrinsic neighbor losses are never equated to diluted pixel fractional loss. Same-unit actual deficits and field morphology are independently recorded in [../terra-pixel-audit.json](../../campaign/batch04/terra-pixel-audit.json); close blends retain uncertainty.
4. **Alternative reduction.** Reused, read and rerun TESScut primitive subtracts faint-pixel background, with symmetric local side windows and selected eclipse core; fresh target-centered 1x1/3x3/5x5 depths=59.23/57.02/50.67 ppt. QLP fitted median=59.45 ppt. Aperture, dilution and background response explain why these are not intrinsic-depth measurements. The cutout sector is absent from the retained QLP files. It is a distinct observing occasion on TESS and an alternative extraction of that sector; no direct same-sector QLP comparison is claimed. Distinct sectors remain occasions on one instrument.
5. **Gaia geometry.** Source 1004675146404805888; P=15.9191458295 +/- 0.007424117 days, e=0.15158. Closest edge-on conjunction offset=0.21015 days (0.01320 phase), source-specific full covariance linear allowance=1.11199 days. Other conjunction relative phase=0.51939, linear phase allowance=0.05055. Full correlation matrix minimum eigenvalue=0.00377364. These linear allowances are descriptive, not calibrated significance. Near Gaia reference the projected epoch offset=-0.25174 days, period-projection allowance alone=0.00841 days (ignores fit covariance/model systematics). Mass function=0.015095 solar masses; adopted primary mass=1.24, minimum secondary mass=0.334. Approximate central duration=5.87 hours versus observed median=5.70 hours. TIC radius, edge-on geometry and main-sequence secondary assumptions make this a plausibility test, not a fitted physical characterization. Impact parameter can shorten duration. Agreement does not by itself establish ownership.

**Deciding limitation:** Four deep events form consecutive pairs in S60/S73. Two shallow secondary candidates in S19 lie at actual phase 0.54415, with other-sector confirmation limited. The capable neighbor at 54.93 arcsec is separate from the target deficit.

**Next check:** Optional resolved photometry and spectroscopy for improved localization and physical parameters.

Shared catalogue results are in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv). Successful no-matches are distinct from failed queries; no exhaustive priority claim is made. TIC 295771108 is a known exact ASAS-SN EA recovery.

| Sector | Search cycle | Measured BTJD | Formal error d | Input allowance d | Depth ppt | Status |
|---|---:|---:|---:|---:|---:|---|
| 60 | 70 | 2942.7595051 | 0.000362647 | 0.00115739 | 57.87 | used |
| 60 | 71 | 2958.6812734 | 0.000314788 | 0.00115739 | 58.81 | used |
| 73 | 92 | 3293.0445300 | 0.000333904 | 0.00115742 | 61.27 | used |
| 73 | 93 | 3308.9657353 | 0.000331667 | 0.00115742 | 60.08 | used |

Evidence: [measurements.json](../../campaign/batch04/322679338/measurements.json), [raw-windows.csv](../../campaign/batch04/322679338/raw-windows.csv), [raw-events.png](../../campaign/batch04/322679338/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch04/322679338/fresh-pixels/diff_fresh.json)/png, historical originals, [../identity-check.json](../../campaign/batch04/identity-check.json), [../alias-audit.json](../../campaign/batch04/alias-audit.json), [../secondary-measurements.json](../../campaign/batch04/secondary-measurements.json), [../secondary-phase-scan.json](../../campaign/batch04/secondary-phase-scan.json)/png, [../gaia-geometry.json](../../campaign/batch04/gaia-geometry.json), [../terra-pixel-audit.json](../../campaign/batch04/terra-pixel-audit.json) and [../helper-audit.md](../../campaign/batch04/helper-audit.md). Exact sources and outputs are covered by [../SHA256SUMS.json](../../campaign/batch04/SHA256SUMS.json). The methods snapshot freezes the read methods without hashing a mutable canonical page.


Stable review key: R575.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch04/322679338/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch04/322679338/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch04/322679338/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch04/322679338/fresh-pixels/run.log)
- [historical/diff_s20.json](../../campaign/batch04/322679338/historical/diff_s20.json)
- [historical/diff_s20.png](../../campaign/batch04/322679338/historical/diff_s20.png)
- [historical/gaia.json](../../campaign/batch04/322679338/historical/gaia.json)
- [measurements.json](../../campaign/batch04/322679338/measurements.json)
- [raw-events.png](../../campaign/batch04/322679338/raw-events.png)
- [raw-windows.csv](../../campaign/batch04/322679338/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch04/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
