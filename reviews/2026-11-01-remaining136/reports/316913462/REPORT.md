# TIC 316913462: CONFIRMED

Full bounded physical review: **COMPLETE**. Physical outcome and catalogue novelty are separate; a known recovery is not a new addition.

1. **Raw repeated events.** 8 free-center local trapezoid measurements in quality-zero QLP SAP_FLUX; 8 centers enter timing, in sectors [95, 104]. Predictions locate windows and are not measurements. Flagged or uncovered windows are not clean nulls. Eight selected events recur in S95/S104, plus five shallow secondary candidates at phase 0.49943, near Gaia prediction 0.49584. Target pixel loss 27.92 e-/s versus 5.85 e-/s at the capable 22.51-arcsec neighbor favors the target at TESS resolution despite overlapping wings. Modern Gaia conjunction offset 0.692 days reflects accumulated period difference: projection near Gaia reference agrees within 0.00132 days; P difference 0.001206 days versus Gaia error 0.000506 days. These descriptive tensions are not a definitive contradiction.
2. **Timing and aliases.** Measured recurring-eclipse period P=6.0758306405 +/- 0.0000174399 days, epoch BTJD=3884.3846087. Epoch kind is the selected recurring eclipse; deeper-primary rank is not assumed. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. There are 6 adjacent same-kind pairs within sectors. Selected depths occur comparably in both cycle parities; doubling does not reveal alternating selected-event kinds. Halving interleaves a shallow secondary or sampled baseline, not the selected eclipse. Actual measured secondary-candidate phase=0.499431, depth=6.60 ppt, 5 usable fits. Actual phase scans and candidate fits are retained; secondary usability is a heuristic amplitude/local-scatter check, not calibrated significance. No exhaustive all-alias search or calibrated secondary-null confidence is asserted.
3. **Pixel attribution.** Fresh S95 difference stack contains 4 selected eclipses. Target WCS pixel=[7.906782929874101, 7.729202811714394], deficit centroid=[7.740687137057815, 7.777263314860381], descriptive offset=0.173 pixel. Neither offset nor image residual is a calibrated localization uncertainty or universal veto. All capable Gaia neighbors: Gaia 6495928548171911168: 22.51 arcsec, G=13.663, intrinsic-loss proxy=0.214. Capability is a G-band pairwise flux-budget proxy; color and aperture response limit precision. Intrinsic neighbor losses are never equated to diluted pixel fractional loss. Same-unit actual deficits and field morphology are independently recorded in [../terra-pixel-audit.json](../../campaign/batch04/terra-pixel-audit.json); close blends retain uncertainty.
4. **Alternative reduction.** Reused, read and rerun TESScut primitive subtracts faint-pixel background, with symmetric local side windows and selected eclipse core; fresh target-centered 1x1/3x3/5x5 depths=41.36/37.43/36.21 ppt. QLP fitted median=53.23 ppt. Aperture, dilution and background response explain why these are not intrinsic-depth measurements. This reduction and the retained QLP sector share TESS photons, testing processing robustness rather than independent observations. Distinct sectors remain occasions on one instrument.
5. **Gaia geometry.** Source 6495928548171911424; P=6.0746245768 +/- 0.00050562446 days, e=0.08962. Closest edge-on conjunction offset=0.69217 days (0.11395 phase), source-specific full covariance linear allowance=0.29493 days. Other conjunction relative phase=0.49584, linear phase allowance=0.01389. Full correlation matrix minimum eigenvalue=0.00335541. These linear allowances are descriptive, not calibrated significance. Near Gaia reference the projected epoch offset=-0.00131 days, period-projection allowance alone=0.01003 days (ignores fit covariance/model systematics). Mass function=0.059768 solar masses; adopted primary mass=1.24, minimum secondary mass=0.584. Approximate central duration=5.73 hours versus observed median=3.55 hours. TIC radius, edge-on geometry and main-sequence secondary assumptions make this a plausibility test, not a fitted physical characterization. Impact parameter can shorten duration. Agreement does not by itself establish ownership.

**Deciding limitation:** Eight selected events recur in S95/S104, plus five shallow secondary candidates at phase 0.49943, near Gaia prediction 0.49584. Target pixel loss 27.92 e-/s versus 5.85 e-/s at the capable 22.51-arcsec neighbor favors the target at TESS resolution despite overlapping wings. Modern Gaia conjunction offset 0.692 days reflects accumulated period difference: projection near Gaia reference agrees within 0.00132 days; P difference 0.001206 days versus Gaia error 0.000506 days. These descriptive tensions are not a definitive contradiction.

**Next check:** Optional resolved photometry and spectroscopy for improved localization and physical parameters.

Shared catalogue results are in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv). Successful no-matches are distinct from failed queries; no exhaustive priority claim is made. TIC 295771108 is a known exact ASAS-SN EA recovery.

| Sector | Search cycle | Measured BTJD | Formal error d | Input allowance d | Depth ppt | Status |
|---|---:|---:|---:|---:|---:|---|
| 95 | 421 | 3884.3842949 | 0.000421103 | 0.00115742 | 49.63 | used |
| 95 | 422 | 3890.4600146 | 0.000477335 | 0.00115742 | 48.66 | used |
| 95 | 423 | 3896.5363538 | 0.00195652 | 0.00195652 | 51.11 | used |
| 95 | 424 | 3902.6128015 | 0.000414073 | 0.00115742 | 48.84 | used |
| 104 | 470 | 4182.1008316 | 0.000373483 | 0.00115741 | 56.41 | used |
| 104 | 471 | 4188.1765393 | 0.000333266 | 0.00115741 | 55.34 | used |
| 104 | 472 | 4194.2517742 | 0.000391464 | 0.00115741 | 56.76 | used |
| 104 | 473 | 4200.3270872 | 0.000319127 | 0.00115741 | 56.26 | used |

Evidence: [measurements.json](../../campaign/batch04/316913462/measurements.json), [raw-windows.csv](../../campaign/batch04/316913462/raw-windows.csv), [raw-events.png](../../campaign/batch04/316913462/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch04/316913462/fresh-pixels/diff_fresh.json)/png, historical originals, [../identity-check.json](../../campaign/batch04/identity-check.json), [../alias-audit.json](../../campaign/batch04/alias-audit.json), [../secondary-measurements.json](../../campaign/batch04/secondary-measurements.json), [../secondary-phase-scan.json](../../campaign/batch04/secondary-phase-scan.json)/png, [../gaia-geometry.json](../../campaign/batch04/gaia-geometry.json), [../terra-pixel-audit.json](../../campaign/batch04/terra-pixel-audit.json) and [../helper-audit.md](../../campaign/batch04/helper-audit.md). Exact sources and outputs are covered by [../SHA256SUMS.json](../../campaign/batch04/SHA256SUMS.json). The methods snapshot freezes the read methods without hashing a mutable canonical page.


Stable review key: R579.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch04/316913462/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch04/316913462/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch04/316913462/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch04/316913462/fresh-pixels/run.log)
- [historical/diff_s95.json](../../campaign/batch04/316913462/historical/diff_s95.json)
- [historical/diff_s95.png](../../campaign/batch04/316913462/historical/diff_s95.png)
- [historical/gaia.json](../../campaign/batch04/316913462/historical/gaia.json)
- [measurements.json](../../campaign/batch04/316913462/measurements.json)
- [raw-events.png](../../campaign/batch04/316913462/raw-events.png)
- [raw-windows.csv](../../campaign/batch04/316913462/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch04/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
