# BATCH05 TESS aperture review

Reviewed 10 targets using 57 original target-sector QLP light curves. The sector/camera/flux-column guard removed 0 otherwise usable cadences.

The 66,663 trial predictions comprise 3,036 measurable windows, 1,101 insufficiently sampled windows within a sector range and 62,526 predictions outside the loaded sector ranges. Different clocks can predict the same elapsed time. All counts use the minimum 55% sampling rule.

| TIC | Finding | Pilot windows measured | Weak in either product |
| --- | --- | ---: | ---: |
| 119343809 | S13 and S66 archive flags are broad variable raw baselines with weak corrected traces. All three measured pilot predictions and the single measurable coarse alternate are weak. | 3 | 3 |
| 360739540 | S13 and S94 raw troughs flatten after correction. S103 is a sharp raw step after a gap. The five measurable pilot predictions are all weak. | 5 | 5 |
| 436468787 | SAP has broad minima and maxima at about half of the independent 6.68 d clock. Corrected flux stays flat. All measurable pilot and coarse alternate predictions are weak. | 5 | 5 |
| 433082891 | SAP shows low-amplitude broad modulation near 2.03 d that is strongly attenuated by pipeline correction. All four adequate pilot predictions are weak. | 4 | 4 |
| 359911369 | S9 through S11 prior troughs include raw gap edges or low broad curves without a matching corrected shape. All seven pilot and 93 strongest alternate predictions are weak. | 7 | 7 |
| 278721356 | Original panels show broad successive SAP troughs and smooth recoveries with flat corrected flux. The pilot has no adequately sampled predicted windows, and the coarse alternate has one weak window. | 0 | 0 |
| 346625850 | S43 S44 and S70 contain smooth raw broad troughs. The strong 46.84 d BLS score comes chiefly from a step-bounded corrected-only depression in S44. All four pilot windows are weak. | 4 | 4 |
| 9133993 | S19 and later dips are broad rounded minima. The 0.502 d short alternative yields varying full-phase profiles in corrected flux, and 22 of 34 leading coarse alternate predictions are weak. | 4 | 1 |
| 156991337 | Recovered a discrete 6.90564 d QLP aperture signal. All 20 measurable cycles have positive depths in both products. The signal matches TOI-691.01, the nearby eclipsing binary reported by Karen Collins and TFOP in ExoFOP. | 5 | 5 |
| 317924609 | The short-period folds and original S6 panels show a shallow smooth trough with gradual shoulders. No short loss is distinct from this waveform. | 6 | 1 |

## Diagnostics

- [Outcomes](outcomes.csv), [input FITS inventory](files.csv), [archive windows](events.csv) and [auxiliary window measurements](aux-windows.csv). The auxiliary table lists original cadence ID, quality counts, and SAP position and sky-background shifts relative to local shoulders.
- [Clock fits](clocks.csv), [per-cycle measurements](predictions.csv) and [coverage sensitivity](coverage-summary.csv). The sensitivity table repeats counts at 55%, 80%, and 95% minimum sampling in the core and shoulders. Weak means at or below 0.75 ppt in raw or corrected flux.
- [Original-cadence contact sheets](plots/contact-1.png) and [second set](plots/contact-2.png). See the individual prior, Pilot, Gaia, coarse alternate and refined plots in [plots](plots/).
- [Independent split-sample clocks](independent-clocks.csv) and [phase-binned sector overlays](plots/independent-morphology.png). The plot compares raw and corrected aperture data and helps separate smooth modulation from a localized recurring loss.

## Reproduction

From this batch directory, run `python ../batch01/review.py --batch-dir .`, `python ../batch01/diagnostics.py .`, then `python ../batch01/crosscheck.py .`. Python dependencies are NumPy, Astropy, Matplotlib, and Pillow. Use `--fits-dir`, `--prior-dir`, `--mask` or `--clock-dir` with the applicable scripts to override workspace defaults.

The direct measurements use finite original aperture flux and pipeline-corrected flux at QUALITY=0. A local line through shoulder medians defines the baseline. The trial periods include Gaia, the pilot, their harmonics or subdivisions, a coarse blind box search, short-period searches on early and late segments, and fine searches around selected periods. The pilot is tested both with a free phase and anchored to the strongest flagged time. The coarse frequency grid can miss narrow peaks over multi-year baselines. Periods recorded for smooth modulation describe the photometric timescale. The aperture data do not assign the signal to a source.

## Known nearby eclipsing binary recovered in TIC 156991337

A blind QLP box search recovered a 6.9056436027 d recurrence at BTJD 1474.38988108 with a 0.080 d core. In six sectors, all 20 measurable cycles show positive median losses in both flux products. The median window depths are 0.818 ppt raw and 0.732 ppt corrected. The Gaia and pilot clocks each have five well-sampled weak predictions.

The source matches TOI-691.01 in ExoFOP. Karen Collins and the TESS Follow-up Observing Program resolved a nearby eclipsing binary with LCO observations on 2021-10-29. Using the registered 6.90559082635 d period with the QLP epoch, all 20 sampled eclipse-phase windows again show losses in both products. The median raw depth is 0.894 ppt. The 18 interleaved half-period windows have median raw and corrected depths of about 0.16 and 0.08 ppt, respectively. The original QLP centroid Y median shifts by +0.00095 px during the eclipse, compared with -0.00007 px at the interleaved phase. Centroid X and background show no comparable eclipse-phase feature. [ExoFOP TIC 156991337](https://exofop.ipac.caltech.edu/tess/target.php?id=156991337)

[Original-cadence BLS windows](plots/156991337-BLS_1.png) · [Eclipse and interleaved half-cycle stacks](156991337/plots/local-control.png) · [Per-window quality, photometry, centroid and background](156991337/refined-windows.csv)

From this batch directory, run `python ../batch01/review.py --batch-dir . --target 156991337 --output-dir 156991337 --seed 6.9056`, then `python refine_156991337.py` to repeat the targeted checks.
