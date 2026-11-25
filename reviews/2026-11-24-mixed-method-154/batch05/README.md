# BATCH05 TESS aperture review

Reviewed 10 targets using 77 original target-sector QLP light curves. The sector/camera/flux-column guard removed 0 otherwise usable cadences.

The 115,127 trial predictions comprise 6,153 measurable windows, 2,332 insufficiently sampled windows within a sector range and 106,642 predictions outside the loaded sector ranges. Different clocks can predict the same elapsed time. All counts use the minimum 55% sampling rule.

| TIC | Finding | Pilot windows measured | Weak in either product |
| --- | --- | ---: | ---: |
| 231922372 | The S7 and S32 features contain changing SAP baselines and gaps. The 43 d search includes a large S98 endpoint step. Five of six sampled pilot windows are weak. | 6 | 5 |
| 233787943 | The S14 S76 and S83 raw declines are slopes interrupted by gaps while corrected flux remains comparatively level. Seven of nine measurable pilot predictions are weak. | 9 | 7 |
| 289538389 | The short S34 and S88 archive hits are rounded depressions among rapid waves. The 3.38634 d fold selects several comparable troughs and the phase-zero dip is weak in S99. | 4 | 1 |
| 8483002 | The S24 S52 S78 and S79 raw ramps lie beside gaps. The strong 16.35 d score uses a corrected depression beside a raw step and a large nearby brightening. | 3 | 2 |
| 459244300 | Early flag windows show smooth changing SAP waves and broad troughs that flatten after correction. All six pilot predictions and the one measurable leading alternate are weak. | 6 | 6 |
| 294965347 | S9 and later prior windows lie amid smooth oscillatory profiles. The 1.618 d fit catches broad troughs with varying phase and 38 adequately sampled weak predictions. | 6 | 1 |
| 134594093 | S7 and S8 flags sit within broad raw oscillations. The S62 loss is interrupted by a gap and suppressed in corrected flux. The 62 d clock has only one adequately sampled prediction. | 5 | 2 |
| 201859475 | The 1.71858 d fold shows three sawtooth cycles in each product, with a steep rise following broad decay. The approximately 0.572 d modulation persists across sectors at changing amplitudes. | 4 | 2 |
| 297253037 | The archive windows include smooth rounded S9 troughs and broader late disturbances. Seventy-seven of 91 measurements at the 1.61 d trial clock are weak in either product. | 4 | 3 |
| 447040645 | The S12 S101 and S102 features include uncorrected slopes and raw gap steps. All six well-sampled pilot predictions are weak. The strongest alternate has only one measurable decline. | 6 | 6 |

## Diagnostics

- [Outcomes](outcomes.csv), [input FITS inventory](files.csv), [archive windows](events.csv) and [auxiliary window measurements](aux-windows.csv). The auxiliary table lists original cadence ID, quality counts, and SAP position and sky-background shifts relative to local shoulders.
- [Clock fits](clocks.csv), [per-cycle measurements](predictions.csv) and [coverage sensitivity](coverage-summary.csv). The sensitivity table repeats counts at 55%, 80%, and 95% minimum sampling in the core and shoulders. Weak means at or below 0.75 ppt in raw or corrected flux.
- [Original-cadence contact sheets](plots/contact-1.png) and [second set](plots/contact-2.png). See the individual prior, Pilot, Gaia, coarse alternate and refined plots in [plots](plots/).

## Reproduction

From this batch directory, run `python ../batch01/review.py --batch-dir .`, `python ../batch01/diagnostics.py .`. If the independent clock files are available, run `python ../batch01/crosscheck.py .`. Python dependencies are NumPy, Astropy, Matplotlib, and Pillow. Use `--fits-dir`, `--prior-dir`, `--mask` or `--clock-dir` with the applicable scripts to override workspace defaults.

The direct measurements use finite original aperture flux and pipeline-corrected flux at QUALITY=0. A local line through shoulder medians defines the baseline. The trial periods include Gaia, the pilot, their harmonics or subdivisions, a coarse blind box search, short-period searches on early and late segments, and fine searches around selected periods. The pilot is tested both with a free phase and anchored to the strongest flagged time. The coarse frequency grid can miss narrow peaks over multi-year baselines. Periods recorded for smooth modulation describe the photometric timescale. The aperture data do not assign the signal to a source.
