# BATCH01 TESS aperture review

Reviewed 10 targets using 163 original target-sector QLP light curves. The sector/camera/flux-column guard removed 4 otherwise usable cadences.

The 60,468 trial predictions comprise 8,992 measurable windows, 2,882 insufficiently sampled windows within a sector range and 48,594 predictions outside the loaded sector ranges. Different clocks can predict the same elapsed time. All counts use the minimum 55% sampling rule.

| TIC | Finding | Pilot windows measured | Weak in either product |
| --- | --- | ---: | ---: |
| 367737263 | Raw ramps dominate S24 S52 S53 and late flags. The S52 feature occurs at the same S52 camera 3 CCD4 cadence 216309 as TIC 160183798. Twenty-two of 23 pilot windows are weak. | 23 | 22 |
| 381977551 | S4 and S7 contain slow SAP-only bowls. All 33 measurable pilot windows and all 28 measurable leading alternate predictions are weak. | 33 | 33 |
| 67436119 | S15 and S41 archive flags trace smooth raw ramps or gap-adjacent troughs. The 7.49 d alternate selects covered windows with varying raw slopes, and all 23 are weak in either product. | 11 | 11 |
| 268120053 | Large SAP gradients in S8 S9 S34 and S36 leave little corrected structure. The nine adequate pilot windows and seven leading alternate windows are weak. | 9 | 9 |
| 399865006 | At 28.555625 d, 13 of 15 measurable windows show positive losses in both channels, with two covered brightenings. The largest apparent losses coincide with a centroid excursion or flare. Low-amplitude peaks survive their exclusion in both eras; the phase and period were fitted on the full sample. | 15 | 9 |
| 7773469 | The strongest windows are raw steps and recoveries beside gaps in S14 S53 S54 and S74. None of eight sampled pilot predictions exceeds 2 ppt in both products. | 8 | 7 |
| 272551501 | S33 S64 and S66 archive features coincide with SAP steps across gaps. All 16 measurable pilot predictions and all six highest coarse-alternate predictions are weak. | 16 | 16 |
| 160183798 | S14 S19 and S21 show raw gap-edge trends and steps. The S52 flag matches the same exposure as a raw artifact in TIC 367737263. Nine of ten pilot windows are weak. | 10 | 9 |
| 447421411 | S12 and S66 show broad changing raw troughs, and S100 and S101 include SAP steps around gaps. All five measurable pilot window depths are weak in at least one product. | 5 | 5 |
| 320010029 | Archive losses are chiefly SAP gap-edge changes. The 64.90 d coarse peak selects a corrected-only decline at the S103 edge with insufficient shoulder coverage. Five measurable pilot windows are weak. | 5 | 5 |

## Diagnostics

- [Outcomes](outcomes.csv), [input FITS inventory](files.csv), [archive windows](events.csv) and [auxiliary window measurements](aux-windows.csv). The auxiliary table lists original cadence ID, quality counts, and SAP position and sky-background shifts relative to local shoulders.
- [Clock fits](clocks.csv), [per-cycle measurements](predictions.csv) and [coverage sensitivity](coverage-summary.csv). The sensitivity table repeats counts at 55%, 80%, and 95% minimum sampling in the core and shoulders. Weak means at or below 0.75 ppt in raw or corrected flux.
- [Original-cadence contact sheets](plots/contact-1.png) and [second set](plots/contact-2.png). See the individual prior, Pilot, Gaia, coarse alternate and refined plots in [plots](plots/).

## Reproduction

From this batch directory, run `python ./review.py --batch-dir .`, `python ./diagnostics.py .`. If the independent clock files are available, run `python ./crosscheck.py .`. Python dependencies are NumPy, Astropy, Matplotlib, and Pillow. Use `--fits-dir`, `--prior-dir`, `--mask` or `--clock-dir` with the applicable scripts to override workspace defaults.

The direct measurements use finite original aperture flux and pipeline-corrected flux at QUALITY=0. A local line through shoulder medians defines the baseline. The trial periods include Gaia, the pilot, their harmonics or subdivisions, a coarse blind box search, short-period searches on early and late segments, and fine searches around selected periods. The pilot is tested both with a free phase and anchored to the strongest flagged time. The coarse frequency grid can miss narrow peaks over multi-year baselines. Periods recorded for smooth modulation describe the photometric timescale. The aperture data do not assign the signal to a source.

## Marginal 28.555625 d clock in TIC 399865006

The trial ephemeris is BTJD 1698.26165017 + 28.55562495 × cycle, with a 0.060 d core. Its median depth is 0.907 ppt in raw SAP and 0.803 ppt in corrected flux. Thirteen of 15 measurable windows have positive depth in both products. The two well-covered bright windows are at BTJD 1698.262 (S14) and 2440.708 (S41). S59 and S82 contribute the strongest apparent losses, but those windows show a local centroid excursion or a neighboring flare. The median timing profile remains shallow in both products near the predicted epoch when both sectors are excluded and the rest are split at BTJD 2900. The fitted period and epoch were selected using the full sample. Thirteen interleaved covered half-cycle windows have near-zero median depth. The aperture origin and repeat interpretation remain provisional.

[Original-cadence windows](plots/399865006-Fine_1.png) · [Primary and half-cycle flux and centroid profiles](399865006/plots/local-control.png) · [Early and late sensitivity after excluding S59 and S82](399865006/plots/phase-holdout.png)

Run `python window_controls.py . 399865006 28.555624947689658 1698.2616501655923 .06` and `python phase_holdout.py . 399865006 28.555624947689658 1698.2616501655923 .06 2900 --exclude 59 --exclude 82` to regenerate these diagnostics.
