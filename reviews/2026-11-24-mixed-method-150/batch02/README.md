# BATCH02 TESS aperture review

Reviewed 10 targets using 267 original target-sector QLP light curves. The sector/camera/flux-column guard removed 4 otherwise usable cadences.

The 66,150 trial predictions comprise 11,261 measurable windows, 4,030 insufficiently sampled windows within a sector range and 50,859 predictions outside the loaded sector ranges. Different clocks can predict the same elapsed time. All counts use the minimum 55% sampling rule.

| TIC | Finding | Pilot windows measured | Weak in either product |
| --- | --- | ---: | ---: |
| 122992696 | Independent 0.694 d folding shows broad rounded minima across an entire smooth wave in both products. The pilot occasionally samples these unrelated troughs. | 9 | 2 |
| 237289923 | S22 and S78/S79 flagged decreases are SAP ramps and steps around gaps. At the pilot period 20 of 21 measured windows are weak and none exceeds 2 ppt in both. | 21 | 20 |
| 149390282 | S64 through S88 archive depressions recover or terminate at gaps and are weak after correction. All 36 measurable pilot windows and 244 leading alternate windows are weak. | 36 | 36 |
| 279569875 | Strong S13 S62 and S64 raw trends sit next to gaps while corrected flux remains nearly flat. All 30 measured pilot cycles are weak in at least one product. | 30 | 30 |
| 356671554 | S20 and S40 features are rounded SAP depressions that flatten in corrected flux. Each of the four pilot and four strongest alternate predictions with adequate sampling is weak. | 4 | 4 |
| 149391651 | S27 and S33 SAP steps lie across gaps and flatten in corrected data. The apparent late clock gives no strong recovered events and all 36 pilot windows are weak. | 36 | 36 |
| 438605423 | S37 and S38 show smooth roughly two-day SAP troughs that flatten in corrected flux. The leading alternate has 69 measurable yet weak windows. | 1 | 1 |
| 334799022 | SAP exhibits an approximately 13.22 d smooth high-amplitude wave. Corrected flux suppresses most sectors; the late 12.93 d box has 39 weak windows out of 40 and one high-scatter S40 disturbance. | 30 | 30 |
| 459982149 | Early flags lie on raw steps at gaps. The late S84 excursion reaches 10.86 ppt in corrected flux but 0.03 ppt in SAP. All 43 measurable pilot windows are weak. | 43 | 43 |
| 461541830 | Prior S18 to S20 declines are sloping SAP baselines. The coarse alternative selects an S85 flux step, and all six measurable pilot cycles are weak. | 6 | 6 |

## Diagnostics

- [Outcomes](outcomes.csv), [input FITS inventory](files.csv), [archive windows](events.csv) and [auxiliary window measurements](aux-windows.csv). The auxiliary table lists original cadence ID, quality counts, and SAP position and sky-background shifts relative to local shoulders.
- [Clock fits](clocks.csv), [per-cycle measurements](predictions.csv) and [coverage sensitivity](coverage-summary.csv). The sensitivity table repeats counts at 55%, 80%, and 95% minimum sampling in the core and shoulders. Weak means at or below 0.75 ppt in raw or corrected flux.
- [Original-cadence contact sheets](plots/contact-1.png) and [second set](plots/contact-2.png). See the individual prior, Pilot, Gaia, coarse alternate and refined plots in [plots](plots/).
- [Independent split-sample clocks](independent-clocks.csv) and [phase-binned sector overlays](plots/independent-morphology.png). The plot compares raw and corrected aperture data and helps separate smooth modulation from a localized recurring loss.

## Reproduction

From this batch directory, run `python ../batch01/review.py --batch-dir .`, `python ../batch01/diagnostics.py .`, then `python ../batch01/crosscheck.py .`. Python dependencies are NumPy, Astropy, Matplotlib, and Pillow. Use `--fits-dir`, `--prior-dir`, `--mask` or `--clock-dir` with the applicable scripts to override workspace defaults.

The direct measurements use finite original aperture flux and pipeline-corrected flux at QUALITY=0. A local line through shoulder medians defines the baseline. The trial periods include Gaia, the pilot, their harmonics or subdivisions, a coarse blind box search, short-period searches on early and late segments, and fine searches around selected periods. The pilot is tested both with a free phase and anchored to the strongest flagged time. The coarse frequency grid can miss narrow peaks over multi-year baselines. Periods recorded for smooth modulation describe the photometric timescale. The aperture data do not assign the signal to a source.
