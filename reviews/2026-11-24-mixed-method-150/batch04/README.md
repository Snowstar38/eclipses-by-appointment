# BATCH04 TESS aperture review

Reviewed 10 targets using 90 original target-sector QLP light curves. The sector/camera/flux-column guard removed 1 otherwise usable cadences.

The 114,474 trial predictions comprise 7,556 measurable windows, 2,259 insufficiently sampled windows within a sector range and 104,659 predictions outside the loaded sector ranges. Different clocks can predict the same elapsed time. All counts use the minimum 55% sampling rule.

| TIC | Finding | Pilot windows measured | Weak in either product |
| --- | --- | ---: | ---: |
| 290485142 | The 0.6297 d split-sample clock aligns broad smooth raw and corrected troughs. The pilot and 1.89 d alternate mostly sample different parts of that waveform. | 5 | 0 |
| 148040354 | The 1.5644 d fold contains about ten successive troughs in both products. Original windows show fast amplitude-varying oscillation extending through the surrounding phases. | 5 | 0 |
| 426707327 | The flags recur amid rapid changing oscillations in S39 S65 S66 and S93. The 0.32246 d corrected fold has two broad troughs with changing sector amplitudes. S102 is a SAP step at a gap. | 5 | 3 |
| 340329315 | The 0.7274 d SAP wave shows a consistent broad trough with strong suppression in corrected flux. The long pilot contains covered weak windows. | 4 | 2 |
| 442872831 | S5 SAP troughs repeat as a roughly 1.35 d smooth wave and flatten after correction. The 18.21 d alternate selects both sloped and covered weak windows. | 3 | 2 |
| 357542720 | S9 and S36 rounded raw troughs disappear after correction. A roughly 2.63 d SAP modulation aligns only broadly across sectors and five of six pilot predictions are weak. | 6 | 5 |
| 256560912 | S54 through S82 flagged declines start or end at raw flux steps and gaps. Corrected flux is flat in those windows and all measured pilot and coarse alternate windows are weak. | 5 | 5 |
| 50284183 | The 0.5995 d aperture waveform has a smooth rounded trough in both products across four sectors. The 1.80 d alternate is a multiple of this broad waveform. | 5 | 1 |
| 263023294 | The 0.80477 d fold shows five smooth troughs per cycle. The independent 0.322 d fold shows two broad waves and the shape matches raw and corrected photometry. | 7 | 2 |
| 47975189 | S15 and S55 strongest losses are smooth SAP ramps or troughs interrupted by gaps. Corrected measurements strongly suppress them. Seven of eight pilot windows are weak. | 8 | 7 |

## Diagnostics

- [Outcomes](outcomes.csv), [input FITS inventory](files.csv), [archive windows](events.csv) and [auxiliary window measurements](aux-windows.csv). The auxiliary table lists original cadence ID, quality counts, and SAP position and sky-background shifts relative to local shoulders.
- [Clock fits](clocks.csv), [per-cycle measurements](predictions.csv) and [coverage sensitivity](coverage-summary.csv). The sensitivity table repeats counts at 55%, 80%, and 95% minimum sampling in the core and shoulders. Weak means at or below 0.75 ppt in raw or corrected flux.
- [Original-cadence contact sheets](plots/contact-1.png) and [second set](plots/contact-2.png). See the individual prior, Pilot, Gaia, coarse alternate and refined plots in [plots](plots/).
- [Independent split-sample clocks](independent-clocks.csv) and [phase-binned sector overlays](plots/independent-morphology.png). The plot compares raw and corrected aperture data and helps separate smooth modulation from a localized recurring loss.

## Reproduction

From this batch directory, run `python ../batch01/review.py --batch-dir .`, `python ../batch01/diagnostics.py .`, then `python ../batch01/crosscheck.py .`. Python dependencies are NumPy, Astropy, Matplotlib, and Pillow. Use `--fits-dir`, `--prior-dir`, `--mask` or `--clock-dir` with the applicable scripts to override workspace defaults.

The direct measurements use finite original aperture flux and pipeline-corrected flux at QUALITY=0. A local line through shoulder medians defines the baseline. The trial periods include Gaia, the pilot, their harmonics or subdivisions, a coarse blind box search, short-period searches on early and late segments, and fine searches around selected periods. The pilot is tested both with a free phase and anchored to the strongest flagged time. The coarse frequency grid can miss narrow peaks over multi-year baselines. Periods recorded for smooth modulation describe the photometric timescale. The aperture data do not assign the signal to a source.
