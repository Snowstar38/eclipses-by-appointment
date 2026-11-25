# BATCH01 TESS aperture review

Reviewed 10 targets using 148 original target-sector QLP light curves. The sector/camera/flux-column guard removed 2 otherwise usable cadences.

The 81,393 trial predictions comprise 9,454 measurable windows, 2,495 insufficiently sampled windows within a sector range and 69,444 predictions outside the loaded sector ranges. Different clocks can predict the same elapsed time. All counts use the minimum 55% sampling rule.

| TIC | Finding | Pilot windows measured | Weak in either product |
| --- | --- | ---: | ---: |
| 230124102 | The early flags are SAP ramps and gap boundaries. All 33 measurable pilot windows are weak in one or both products. | 33 | 33 |
| 185331661 | Repeated broad rounded SAP troughs dominate sectors S14 S15 and later. Correction strips most of the amplitude. All seven pilot predictions are weak. The independent clock folds to broad continuous variation. | 7 | 7 |
| 235559080 | S16 and S24 raw dips are contiguous smooth waves recurring about every 2.3 d and strongly attenuated after correction. All three measurable pilot windows are weak. | 3 | 3 |
| 41780082 | Deep broad oscillatory minima and similar neighboring peaks change phase and shape between sectors. The pilot and 58 d alternate include covered windows at different points on the oscillation. The independent clock folds to broad continuous variation. | 7 | 3 |
| 440546908 | The 1.6926252 d fold shows three smooth nearly spaced troughs per fitted cycle in both products throughout eight sectors. The covered pilot windows do not isolate a short dip. The independent clock folds to broad continuous variation. | 5 | 3 |
| 198355899 | S23 and S56 flags mostly trace SAP-only broad depressions or edges. 24 of 27 pilot windows are weak in either product and none reaches 2 ppt in both. | 27 | 24 |
| 351406966 | The S15 and S16 features are rounded minima on short timescales. The 3.28 d alternative leaves numerous shallow windows and the pilot does not isolate a discrete repeat. | 7 | 5 |
| 434533064 | S17 and S57 show changing broad waveform troughs. The isolated S85 comparison dip is shared with unrelated sources at overlapping exposures in the earlier camera check. The independent clock folds to broad continuous variation. | 10 | 8 |
| 287636970 | Original S2 and S5 windows show strong smooth changing waves in SAP and weaker corrected counterparts. The 1.63 d fold selects troughs and crests. | 25 | 17 |
| 326370715 | The 0.3303004 d phase fold shows a single smooth minimum and full phase variation in all eight sectors despite a box score supported by 498 measurable windows. | 6 | 2 |

## Diagnostics

- [Outcomes](outcomes.csv), [input FITS inventory](files.csv), [archive windows](events.csv) and [auxiliary window measurements](aux-windows.csv). The auxiliary table lists original cadence ID, quality counts, and SAP position and sky-background shifts relative to local shoulders.
- [Clock fits](clocks.csv), [per-cycle measurements](predictions.csv) and [coverage sensitivity](coverage-summary.csv). The sensitivity table repeats counts at 55%, 80%, and 95% minimum sampling in the core and shoulders. Weak means at or below 0.75 ppt in raw or corrected flux.
- [Original-cadence contact sheets](plots/contact-1.png) and [second set](plots/contact-2.png). See the individual prior, Pilot, Gaia, coarse alternate and refined plots in [plots](plots/).
- [Independent split-sample clocks](independent-clocks.csv) and [phase-binned sector overlays](plots/independent-morphology.png). The plot compares raw and corrected aperture data and helps separate smooth modulation from a localized recurring loss.

## Reproduction

From this batch directory, run `python ./review.py --batch-dir .`, `python ./diagnostics.py .`, then `python ./crosscheck.py .`. Python dependencies are NumPy, Astropy, Matplotlib, and Pillow. Use `--fits-dir`, `--prior-dir`, `--mask` or `--clock-dir` with the applicable scripts to override workspace defaults.

The direct measurements use finite original aperture flux and pipeline-corrected flux at QUALITY=0. A local line through shoulder medians defines the baseline. The trial periods include Gaia, the pilot, their harmonics or subdivisions, a coarse blind box search, short-period searches on early and late segments, and fine searches around selected periods. The pilot is tested both with a free phase and anchored to the strongest flagged time. The coarse frequency grid can miss narrow peaks over multi-year baselines. Periods recorded for smooth modulation describe the photometric timescale. The aperture data do not assign the signal to a source.
