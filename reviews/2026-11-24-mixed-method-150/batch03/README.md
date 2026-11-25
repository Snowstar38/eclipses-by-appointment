# BATCH03 TESS aperture review

Reviewed 10 targets using 133 original target-sector QLP light curves. The sector/camera/flux-column guard removed 1 otherwise usable cadences.

The 87,096 trial predictions comprise 10,118 measurable windows, 2,994 insufficiently sampled windows within a sector range and 73,984 predictions outside the loaded sector ranges. Different clocks can predict the same elapsed time. All counts use the minimum 55% sampling rule.

| TIC | Finding | Pilot windows measured | Weak in either product |
| --- | --- | ---: | ---: |
| 19084617 | S8 prior losses fall in smooth changing oscillations. The 0.613 d clock aligns broad depletions in SAP with different corrected amplitudes and no localized event. | 7 | 2 |
| 27699273 | The independent 0.5947 d fold shows rounded phase-wide modulation in both products over multiple sectors. The long pilot catches broad troughs and its shoulders remain sloping. | 4 | 0 |
| 5619059 | Original S35 event flags fall on a smooth high-amplitude wave. BLS aliases select the same broad minima and the 1.53775 d fold shows ten troughs per period in both products. | 10 | 0 |
| 214428527 | The 0.625 d window brings broad raw troughs into phase across sectors with strongly differing corrected amplitudes. There is no abrupt dip inside the smooth minima. | 1 | 1 |
| 257056883 | S15 SAP flags sit on smooth wave troughs suppressed after correction. All four pilot and three strongest alternative predictions with adequate coverage are weak. | 4 | 4 |
| 41680093 | The 3.90776 d SAP waveform has bright flanks and a broad smooth center that is no deeper than other raw minima. Corrected flux has a smooth near-11th harmonic. Centroid X and sky background show no consistent phase-zero change in the sector folds. | 5 | 1 |
| 219293764 | S27 has successive broad SAP troughs separated by maxima. The corrected profile stays flat there, and all four covered pilot predictions are weak. | 4 | 4 |
| 243333427 | The 0.4683 d fold shows a broad low-amplitude trough in both products. The earlier archive windows select deeper isolated SAP variation, and 19 of 21 pilot predictions are weak. | 21 | 19 |
| 237115309 | S18 to S20 flagged raw depletions are broad baseline excursions and flatten in corrected flux. 33 of 34 measured pilot predictions are weak. | 34 | 33 |
| 424701226 | Raw SAP gives a coherent smooth 1.40365 d wave. Correction largely removes it and all 24 measurable pilot predictions are weak. | 24 | 24 |

## Diagnostics

- [Outcomes](outcomes.csv), [input FITS inventory](files.csv), [archive windows](events.csv) and [auxiliary window measurements](aux-windows.csv). The auxiliary table lists original cadence ID, quality counts, and SAP position and sky-background shifts relative to local shoulders.
- [Clock fits](clocks.csv), [per-cycle measurements](predictions.csv) and [coverage sensitivity](coverage-summary.csv). The sensitivity table repeats counts at 55%, 80%, and 95% minimum sampling in the core and shoulders. Weak means at or below 0.75 ppt in raw or corrected flux.
- [Original-cadence contact sheets](plots/contact-1.png) and [second set](plots/contact-2.png). See the individual prior, Pilot, Gaia, coarse alternate and refined plots in [plots](plots/).
- [Independent split-sample clocks](independent-clocks.csv) and [phase-binned sector overlays](plots/independent-morphology.png). The plot compares raw and corrected aperture data and helps separate smooth modulation from a localized recurring loss.

## Reproduction

From this batch directory, run `python ../batch01/review.py --batch-dir .`, `python ../batch01/diagnostics.py .`, then `python ../batch01/crosscheck.py .`. Python dependencies are NumPy, Astropy, Matplotlib, and Pillow. Use `--fits-dir`, `--prior-dir`, `--mask` or `--clock-dir` with the applicable scripts to override workspace defaults.

The direct measurements use finite original aperture flux and pipeline-corrected flux at QUALITY=0. A local line through shoulder medians defines the baseline. The trial periods include Gaia, the pilot, their harmonics or subdivisions, a coarse blind box search, short-period searches on early and late segments, and fine searches around selected periods. The pilot is tested both with a free phase and anchored to the strongest flagged time. The coarse frequency grid can miss narrow peaks over multi-year baselines. Periods recorded for smooth modulation describe the photometric timescale. The aperture data do not assign the signal to a source.
TIC 41680093 has an [additional alias and auxiliary-column comparison](plots/41680093-alias-comparison.png). The phase-zero trough is flanked by bright humps and has a depth relative to the sector median comparable to other minima.
