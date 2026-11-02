# TIC 28116156: CONFIRMED

Full bounded physical review: **COMPLETE**. Physical outcome and catalogue novelty are separate; a known recovery is not a new addition.

1. **Raw repeated events.** 9 free-center local trapezoid measurements in quality-zero QLP SAP_FLUX; 9 centers enter timing, in sectors [30]. Predictions locate windows and are not measurements. Flagged or uncovered windows are not clean nulls. Nine short eclipses in S30 establish same-kind recurrence; the period/error use this actual within-sector baseline. Coarse S3 does not contribute precise timings. The capable neighbor at 30.94 arcsec is spatially distinct from the compact deficit.
2. **Timing and aliases.** Measured recurring-eclipse period P=1.5922960846 +/- 0.0002318805 days, epoch BTJD=2117.3845444. Epoch kind is the selected recurring eclipse; deeper-primary rank is not assumed. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. There are 4 adjacent same-kind pairs within sectors. Selected depths occur comparably in both cycle parities; doubling does not reveal alternating selected-event kinds. Halving interleaves a shallow secondary or sampled baseline, not the selected eclipse. No significant repeated secondary center is claimed; this is not proof of absence. Actual phase scans and candidate fits are retained; secondary usability is a heuristic amplitude/local-scatter check, not calibrated significance. No exhaustive all-alias search or calibrated secondary-null confidence is asserted.
3. **Pixel attribution.** Fresh S30 difference stack contains 13 selected eclipses. Target WCS pixel=[7.182217395273183, 7.11712281687406], deficit centroid=[7.319444970737896, 7.254837847209099], descriptive offset=0.194 pixel. Neither offset nor image residual is a calibrated localization uncertainty or universal veto. All capable Gaia neighbors: Gaia 2355817466259768448: 30.94 arcsec, G=14.559, intrinsic-loss proxy=0.173. Capability is a G-band pairwise flux-budget proxy; color and aperture response limit precision. Intrinsic neighbor losses are never equated to diluted pixel fractional loss. Same-unit actual deficits and field morphology are independently recorded in [../terra-pixel-audit.json](../../campaign/batch04/terra-pixel-audit.json); close blends retain uncertainty.
4. **Alternative reduction.** Reused, read and rerun TESScut primitive subtracts faint-pixel background, with symmetric local side windows and selected eclipse core; fresh target-centered 1x1/3x3/5x5 depths=19.84/17.47/16.58 ppt. QLP fitted median=21.60 ppt. Aperture, dilution and background response explain why these are not intrinsic-depth measurements. This reduction and the retained QLP sector share TESS photons, testing processing robustness rather than independent observations. Distinct sectors remain occasions on one instrument.
5. **Gaia geometry.** Source 2355817565042831232; P=1.5923420791 +/- 8.154e-05 days, e=0.03598. Closest edge-on conjunction offset=-0.08013 days (-0.05032 phase), source-specific full covariance linear allowance=0.09512 days. Other conjunction relative phase=0.51027, linear phase allowance=0.02247. Full correlation matrix minimum eigenvalue=0.000493799. These linear allowances are descriptive, not calibrated significance. Near Gaia reference the projected epoch offset=-0.03023 days, period-projection allowance alone=0.25159 days (ignores fit covariance/model systematics). Mass function=0.059513 solar masses; adopted primary mass=1.17, minimum secondary mass=0.563. Approximate central duration=3.49 hours versus observed median=1.40 hours. TIC radius, edge-on geometry and main-sequence secondary assumptions make this a plausibility test, not a fitted physical characterization. Impact parameter can shorten duration. Agreement does not by itself establish ownership.

**Deciding limitation:** Nine short eclipses in S30 establish same-kind recurrence; the period/error use this actual within-sector baseline. Coarse S3 does not contribute precise timings. The capable neighbor at 30.94 arcsec is spatially distinct from the compact deficit.

**Next check:** Optional resolved photometry and spectroscopy for improved localization and physical parameters.

Shared catalogue results are in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv). Successful no-matches are distinct from failed queries; no exhaustive priority claim is made. TIC 295771108 is a known exact ASAS-SN EA recovery.

| Sector | Search cycle | Measured BTJD | Formal error d | Input allowance d | Depth ppt | Status |
|---|---:|---:|---:|---:|---:|---|
| 30 | 460 | 2117.3839584 | 0.00193591 | 0.00347219 | 21.84 | used |
| 30 | 461 | 2118.9773778 | 0.00210344 | 0.00347219 | 23.19 | used |
| 30 | 464 | 2123.7548855 | 0.00212481 | 0.00347219 | 21.65 | used |
| 30 | 465 | 2125.3440626 | 0.00265762 | 0.00347219 | 21.60 | used |
| 30 | 469 | 2131.7161471 | 0.000554862 | 0.00347219 | 20.72 | used |
| 30 | 470 | 2133.3073925 | 0.00053522 | 0.00347219 | 20.42 | used |
| 30 | 471 | 2134.9002135 | 0.00191663 | 0.00347219 | 20.62 | used |
| 30 | 473 | 2138.0851194 | 0.000953467 | 0.00347219 | 19.93 | used |
| 30 | 475 | 2141.2678764 | 0.00152062 | 0.00347219 | 22.60 | used |

Evidence: [measurements.json](../../campaign/batch04/28116156/measurements.json), [raw-windows.csv](../../campaign/batch04/28116156/raw-windows.csv), [raw-events.png](../../campaign/batch04/28116156/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch04/28116156/fresh-pixels/diff_fresh.json)/png, historical originals, [../identity-check.json](../../campaign/batch04/identity-check.json), [../alias-audit.json](../../campaign/batch04/alias-audit.json), [../secondary-measurements.json](../../campaign/batch04/secondary-measurements.json), [../secondary-phase-scan.json](../../campaign/batch04/secondary-phase-scan.json)/png, [../gaia-geometry.json](../../campaign/batch04/gaia-geometry.json), [../terra-pixel-audit.json](../../campaign/batch04/terra-pixel-audit.json) and [../helper-audit.md](../../campaign/batch04/helper-audit.md). Exact sources and outputs are covered by [../SHA256SUMS.json](../../campaign/batch04/SHA256SUMS.json). The methods snapshot freezes the read methods without hashing a mutable canonical page.


Stable review key: R574.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch04/28116156/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch04/28116156/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch04/28116156/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch04/28116156/fresh-pixels/run.log)
- [historical/diff_s30.json](../../campaign/batch04/28116156/historical/diff_s30.json)
- [historical/diff_s30.png](../../campaign/batch04/28116156/historical/diff_s30.png)
- [historical/gaia.json](../../campaign/batch04/28116156/historical/gaia.json)
- [measurements.json](../../campaign/batch04/28116156/measurements.json)
- [raw-events.png](../../campaign/batch04/28116156/raw-events.png)
- [raw-windows.csv](../../campaign/batch04/28116156/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch04/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
