# BATCH04 TESS aperture review

Reviewed 10 targets using 120 original target-sector QLP light curves. The sector/camera/flux-column guard removed 0 otherwise usable cadences.

The 128,476 trial predictions comprise 7,760 measurable windows, 3,268 insufficiently sampled windows within a sector range and 117,448 predictions outside the loaded sector ranges. Different clocks can predict the same elapsed time. All counts use the minimum 55% sampling rule.

| TIC | Finding | Pilot windows measured | Weak in either product |
| --- | --- | ---: | ---: |
| 41497557 | Five smooth broad troughs are evenly spaced through the 1.80001 d fold. The resulting roughly 0.36 d flux modulation persists across six sectors. | 4 | 0 |
| 18175839 | S17 and S57 archive features are smooth broad SAP downturns amid a full wave. The corrected product suppresses much of the structure, and both covered pilot windows are weak. | 2 | 2 |
| 204618651 | Rounded lows in S10 and S63 form part of a smooth waveform with sloped shoulders. The 55.4 d refinement selects different points on broad raw and corrected curves. | 4 | 1 |
| 381978657 | S87 S90 S94 and S96 archive flags cluster around raw discontinuities and gaps. All 25 sampled pilot and seven strongest alternate predictions are weak. | 25 | 25 |
| 349778234 | A coherent roughly 0.783 d oscillation dominates raw SAP curves. The corrected troughs vary in depth and timing and 34 of 55 sampled coarse alternate predictions are weak. | 4 | 3 |
| 114482163 | The large long-period score comes from a single broad S8 trough with smooth descending and rising shoulders in both products. Both adequately sampled pilot predictions are weak. | 2 | 2 |
| 462428788 | Early SAP curves show a smooth high-amplitude wave near 0.775 d. The strongest long BLS clock selects one S10 trough with different raw and corrected phases. | 6 | 4 |
| 31379644 | The S65 S67 and S87 archive losses are broad SAP slopes into gaps. All 32 measured pilot and all 14 leading alternate windows are weak. | 32 | 32 |
| 103409910 | Rounded S36 and S90 SAP troughs repeat between nearby maxima and largely disappear in corrected flux. Thirty-nine of 42 strongest alternate predictions are weak. | 5 | 4 |
| 310212446 | S9 S35 and S62 archive flags follow raw gap-boundary steps. Seven of eight pilot windows and the largest corrected-only excursions lack a matching raw loss. | 8 | 7 |

## Diagnostics

- [Outcomes](outcomes.csv), [input FITS inventory](files.csv), [archive windows](events.csv) and [auxiliary window measurements](aux-windows.csv). The auxiliary table lists original cadence ID, quality counts, and SAP position and sky-background shifts relative to local shoulders.
- [Clock fits](clocks.csv), [per-cycle measurements](predictions.csv) and [coverage sensitivity](coverage-summary.csv). The sensitivity table repeats counts at 55%, 80%, and 95% minimum sampling in the core and shoulders. Weak means at or below 0.75 ppt in raw or corrected flux.
- [Original-cadence contact sheets](plots/contact-1.png) and [second set](plots/contact-2.png). See the individual prior, Pilot, Gaia, coarse alternate and refined plots in [plots](plots/).

## Reproduction

From this batch directory, run `python ../batch01/review.py --batch-dir .`, `python ../batch01/diagnostics.py .`. If the independent clock files are available, run `python ../batch01/crosscheck.py .`. Python dependencies are NumPy, Astropy, Matplotlib, and Pillow. Use `--fits-dir`, `--prior-dir`, `--mask` or `--clock-dir` with the applicable scripts to override workspace defaults.

The direct measurements use finite original aperture flux and pipeline-corrected flux at QUALITY=0. A local line through shoulder medians defines the baseline. The trial periods include Gaia, the pilot, their harmonics or subdivisions, a coarse blind box search, short-period searches on early and late segments, and fine searches around selected periods. The pilot is tested both with a free phase and anchored to the strongest flagged time. The coarse frequency grid can miss narrow peaks over multi-year baselines. Periods recorded for smooth modulation describe the photometric timescale. The aperture data do not assign the signal to a source.
