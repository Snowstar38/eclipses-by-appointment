# BATCH03 TESS aperture review

Reviewed 10 targets using 102 original target-sector QLP light curves. The sector/camera/flux-column guard removed 0 otherwise usable cadences.

The 123,507 trial predictions comprise 8,225 measurable windows, 2,652 insufficiently sampled windows within a sector range and 112,630 predictions outside the loaded sector ranges. Different clocks can predict the same elapsed time. All counts use the minimum 55% sampling rule.

| TIC | Finding | Pilot windows measured | Weak in either product |
| --- | --- | ---: | ---: |
| 1137667 | S61 and S62 flags follow broad SAP-only depressions. Five of six pilot windows are weak. The 63 d alternative has just one measured window. | 6 | 5 |
| 290463943 | The 2.79262 d fold has repeated broad troughs across phase including minima near phase zero. The epoch-zero depression varies across sectors and the alternate has 14 weak covered windows. | 7 | 1 |
| 382098944 | S61 S65 and S87 archive losses are raw baseline changes next to gaps, with quiet corrected curves. All 34 pilot windows are weak. | 34 | 34 |
| 293690240 | The 46.0923 d trial catches five rounded lows amid fast many-peaked waves in each local panel. The narrow archive windows also select different troughs of that same waveform. | 5 | 1 |
| 270374997 | The S63 S100 and S101 prior dips sit beside steps in raw SAP. All six pilot windows and ten strongest alternate windows are weak. | 6 | 6 |
| 268808567 | The 22.93968 d pilot refinement samples smooth rounded troughs on the short oscillatory waveform. S94 and S103 show much of the surrounding continuous wave in both products. | 8 | 4 |
| 286156694 | The original S36 S89 and S90 windows follow raw drops into gaps. All eight sampled pilot windows and all four leading alternate predictions are weak. | 8 | 8 |
| 70792227 | The 2.49244 d phase panels show about ten broad troughs in each product, with changing amplitudes. There are no measurable pilot predictions. | 0 | 0 |
| 762167 | The strongest S7 SAP features have slopes and different shoulders. All three measurable pilot and thirteen leading alternate predictions are weak in one or both products. | 3 | 3 |
| 326671490 | The large 59 d box score comes from one S84 correction step adjacent to a raw gap-boundary ramp, with other predictions inadequately sampled. S17 and S58 raw flags lack matching corrected structure. | 1 | 1 |

## Diagnostics

- [Outcomes](outcomes.csv), [input FITS inventory](files.csv), [archive windows](events.csv) and [auxiliary window measurements](aux-windows.csv). The auxiliary table lists original cadence ID, quality counts, and SAP position and sky-background shifts relative to local shoulders.
- [Clock fits](clocks.csv), [per-cycle measurements](predictions.csv) and [coverage sensitivity](coverage-summary.csv). The sensitivity table repeats counts at 55%, 80%, and 95% minimum sampling in the core and shoulders. Weak means at or below 0.75 ppt in raw or corrected flux.
- [Original-cadence contact sheets](plots/contact-1.png) and [second set](plots/contact-2.png). See the individual prior, Pilot, Gaia, coarse alternate and refined plots in [plots](plots/).

## Reproduction

From this batch directory, run `python ../batch01/review.py --batch-dir .`, `python ../batch01/diagnostics.py .`. If the independent clock files are available, run `python ../batch01/crosscheck.py .`. Python dependencies are NumPy, Astropy, Matplotlib, and Pillow. Use `--fits-dir`, `--prior-dir`, `--mask` or `--clock-dir` with the applicable scripts to override workspace defaults.

The direct measurements use finite original aperture flux and pipeline-corrected flux at QUALITY=0. A local line through shoulder medians defines the baseline. The trial periods include Gaia, the pilot, their harmonics or subdivisions, a coarse blind box search, short-period searches on early and late segments, and fine searches around selected periods. The pilot is tested both with a free phase and anchored to the strongest flagged time. The coarse frequency grid can miss narrow peaks over multi-year baselines. Periods recorded for smooth modulation describe the photometric timescale. The aperture data do not assign the signal to a source.
