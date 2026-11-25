# Batch 1 repeat review

Original TESS QLP aperture light curves were examined for ten TICs using 79 target-sector files. The review found one repeating aperture candidate, TIC 410900361, and one isolated short event, TIC 137203172. The aperture light curves alone leave the source of each signal unassigned.

## TIC 410900361

The alternate ephemeris is BTJD 1469.1291405 + 3.0910862 E with a 0.080 d box core. The visible ingress and egress extend beyond the box, giving an approximate full extent of 0.12–0.15 d in the better-sampled windows. In the [individual event panels](plots/410900361-Fine_1.png), the narrow loss appears in the original raw and corrected measurements. The [sector phase panels](plots/410900361-Fine_1-phase.png) show it across all 11 sectors, including several changes of CCD and three nominal cadence spacings. A smooth double wave in raw SAP is strongly attenuated by QLP correction, while the acute loss persists. The ephemeris is a fit to these data, and the quoted digits are for reproducing the windows.

- All 72 measurable predictions contain a loss greater than 3.1 ppt in each product, with median depths of 5.03 ppt corrected and 5.51 ppt raw. Seventeen predictions fall within sector spans with insufficient core or shoulder sampling and 648 fall between sector spans.
- At half the period, the 72 even cycles have a median corrected depth of 5.03 ppt and the 71 measurable interleaved cycles have a median corrected depth of 0.08 ppt. At double the period, the [fold](plots/410900361-Fine_1_double-phase.png) shows two narrow losses approximately half a phase cycle apart. This establishes the recurrence interval. The physical orbital period and source still need independent constraints.
- The Gaia period of 51.3164 d gives only three measurable predicted cycles even with a phase optimized for that period. The Gaia ephemeris from this fit gives weak corrected depths at BTJD 2985.114 and 3703.544.
- Suggested high-cadence localization windows with 0.080 d core width are S61 BTJD 2983.761371 (6.66 ppt corrected, 7.75 ppt raw), S62 BTJD 2989.943543 (6.82 / 6.92 ppt), S62 BTJD 2993.034629 (6.57 / 7.01 ppt), and S89 BTJD 3722.530969 (6.31 / 6.65 ppt).

## TIC 137203172

S85 BTJD 3629.32883 is isolated, with a 0.060 d window containing 25 cadences and a median loss of 5.79 ppt corrected and 5.56 ppt raw. The deepest individual points are around 9 ppt below the local baseline. A short-window search found three overlapping measurements of this same event across box widths of 0.04–0.09 d. This search required at least 2 ppt in both flux products. The [prior windows](plots/137203172-prior.png) show why the other flags are morphologically dissimilar. The ~61 d fit takes its strongest contribution from the start of the S85 series, where an edge excursion in corrected flux and lack of shoulder coverage dominate the score. The ~19.66 d alternate has nine measurable predictions with weak depth in at least one product. The period remains undetermined. A subsequent [same-exposure comparison with batch 4](../batch4/plots/camera-S85-1037602.png) shows coincident losses on other chips, including the independently flagged TIC 387410061. An instrumental contribution is plausible.

## Other targets

- TICs 137417837, 329642297, 193630960 and 253463221 show broad or evolving modulation in the raw or corrected profiles. Their alternate folds lack a separate repeatable narrow loss. The 193630960 clock in particular is approximate, as the raw trough drifts when folded over the full baseline.
- TIC 461587120 shows short broad-bottomed minima of varying symmetry with changing shoulders and a number of strong broad SAP-only lows. Six of twelve measurable windows at the Gaia fit have depths at or below 0.75 ppt in at least one flux product. The leading coarse alternate has 50 such windows out of 104.
- TIC 444830591 has pairs at BTJD 1800.306 and 1814.015 (S18) and 1956.840 and 1970.549 (S24). Their separations are both 13.709 d, with SAP ramps or rounded depressions and much weaker correction-domain losses. At the leading coarse alternate, only six windows are measurable and three are at or below 0.75 ppt in either product. An instrumental contribution is plausible.
- TIC 165904352's S99 depressions occur near sampling gaps and SAP jumps. TIC 304391868's S2 loss is confined to a single cadence and its S96 feature is chiefly a gap-adjacent SAP deviation.

## Reproduction and evidence

Run `python review.py` with Python, NumPy, SciPy, Astropy and Matplotlib. The default source locations are derived from the workspace layout. Use `--fits-dir`, `--prior-dir` and `--mask` to change paths. Measurements use the original FITS time series, QUALITY=0, finite BTJD and flux in both products, and the flagged QLP sector/camera/cadenceno mask. The sources use KSPSAP_FLUX or DET_FLUX for pipeline-corrected photometry as recorded in the file inventory. Positive reported depth indicates a flux loss. All times are BJD - 2457000 and all depths are in parts per thousand.

BLS uses corrected flux divided by a moving median continuum, with point weights estimated per sector and mild outlier clipping. The trial clocks include Gaia with free phase, half and double the Gaia period, a coarse 1.5–65 d scan, short scans in early and late data, and fine sweeps around selected alternates. BLS scores rank trial clocks. Depths use original unbinned fluxes in both products, fit with a local line between shoulder medians. A window requires at least two samples and 55% nominal cadence coverage in each of the core and both shoulders. Predictions failing this condition are marked insufficient and windows outside sector ranges are marked separately. The coarse period grid can skip narrow long-baseline solutions. This screen is a morphology and coverage review of these ten aperture time series.

- [outcomes.csv](outcomes.csv) records all ten dispositions. Periods on continuous modulation rows describe the modulation clock.
- [files.csv](files.csv) lists the FITS file, sector, detector, cadence, coverage interval and mask count.
- [events.csv](events.csv) measures the previously flagged windows after masking and in both flux products.
- [clocks.csv](clocks.csv) lists the trial periods, epochs, widths and BLS ranking statistic when fitted.
- [predictions.csv](predictions.csv) gives each expected window and the measured depths or coverage limitations.
- [137203172-short-search.csv](137203172-short-search.csv) records the independent short-event search.
- [plots/](plots/) contains original-cadence window panels and per-sector phase panels. Window plots baseline-subtract each series near the event for comparison. Phase panels divide by a moving median continuum for display.
