# BATCH02 TESS aperture review

Reviewed 10 targets using 51 original target-sector QLP light curves. The sector/camera/flux-column guard removed 0 otherwise usable cadences.

The 171,659 trial predictions comprise 8,685 measurable windows, 2,805 insufficiently sampled windows within a sector range and 160,169 predictions outside the loaded sector ranges. Different clocks can predict the same elapsed time. All counts use the minimum 55% sampling rule.

| TIC | Finding | Pilot windows measured | Weak in either product |
| --- | --- | ---: | ---: |
| 374726121 | S12 S39 and S65 flags are broad SAP bowls or ramps with little corrected depth. The one measurable pilot and all five coarse-alternate windows are weak. | 1 | 1 |
| 161221229 | S1 bowls and S68/S95 gap-adjacent declines are largely raw baseline effects. All three measurable pilot windows are weak. The only measured 54.39 d peak lands on one S103 trough. | 3 | 3 |
| 262811457 | All three sectors have near-identical smooth oscillations in SAP and corrected flux. Ten broad troughs appear per 1.64751 d alias, and the shorter waveform is close to 0.16475 d. | 3 | 0 |
| 386378137 | The 1.85503 d trial aligns a complex oscillatory waveform with comparably deep minima near other phases. Covered troughs have continuously changing curved shoulders. | 3 | 0 |
| 12700606 | The S41 S55 and S74 low points join broader rolling profiles with nearby peaks. The leading 47 d alternatives align dissimilar parts of that waveform. | 4 | 3 |
| 26804406 | The 1.5565 d trial contains six smooth periods of the raw and corrected waveform in every sector. The 1.55 d coarse BLS detections follow the same continuous modulation. | 4 | 1 |
| 22714041 | The 1.73689 d fold shows three rounded minima and three maxima in both products. The 0.579 d clock follows a broad smooth wave through all six sectors. | 2 | 0 |
| 74885936 | All seven sectors show roughly seven smooth cycles per 1.6914 d alias. Nearly all leading trial windows sample a broad oscillatory minimum. Separate S35 exposure-local changes were identified in the prior camera review. | 5 | 1 |
| 6953953 | S44 flags and the 0.533 d alternate fall on smooth oscillations with changing amplitude and phase. The 32.19 d peak is a single adequately sampled trough. | 3 | 1 |
| 71723446 | The 1.69182 d fold has at least three broad minima with sloped shoulders, and their relative depths vary between S6 S33 and S87. | 3 | 0 |

## Diagnostics

- [Outcomes](outcomes.csv), [input FITS inventory](files.csv), [archive windows](events.csv) and [auxiliary window measurements](aux-windows.csv). The auxiliary table lists original cadence ID, quality counts, and SAP position and sky-background shifts relative to local shoulders.
- [Clock fits](clocks.csv), [per-cycle measurements](predictions.csv) and [coverage sensitivity](coverage-summary.csv). The sensitivity table repeats counts at 55%, 80%, and 95% minimum sampling in the core and shoulders. Weak means at or below 0.75 ppt in raw or corrected flux.
- [Original-cadence contact sheets](plots/contact-1.png) and [second set](plots/contact-2.png). See the individual prior, Pilot, Gaia, coarse alternate and refined plots in [plots](plots/).

## Reproduction

From this batch directory, run `python ../batch01/review.py --batch-dir .`, `python ../batch01/diagnostics.py .`. If the independent clock files are available, run `python ../batch01/crosscheck.py .`. Python dependencies are NumPy, Astropy, Matplotlib, and Pillow. Use `--fits-dir`, `--prior-dir`, `--mask` or `--clock-dir` with the applicable scripts to override workspace defaults.

The direct measurements use finite original aperture flux and pipeline-corrected flux at QUALITY=0. A local line through shoulder medians defines the baseline. The trial periods include Gaia, the pilot, their harmonics or subdivisions, a coarse blind box search, short-period searches on early and late segments, and fine searches around selected periods. The pilot is tested both with a free phase and anchored to the strongest flagged time. The coarse frequency grid can miss narrow peaks over multi-year baselines. Periods recorded for smooth modulation describe the photometric timescale. The aperture data do not assign the signal to a source.
