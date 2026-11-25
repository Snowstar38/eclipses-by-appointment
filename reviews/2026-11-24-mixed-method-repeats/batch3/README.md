# Batch 3 | TESS time-series recurrence

TIC 170337570 has a coherent short-period signal in all six available QLP sectors (12, 66, 93, 100, 102, 103). The fitted clock is **0.86898654 d**, with reference center **1626.64576 BTJD** and a **0.060 d** comparison window. Each of 140 adequately sampled predictions shows a positive depression of at least 2.5 ppt in SAP and 3 ppt in corrected flux. Thirty additional predictions intersect available sector time bounds but fail the coverage requirement, with two still showing depressions. The half-period alias puts 137 adequately sampled predictions between the actual events. One crosses both depth thresholds. Both parities of the doubled period repeat, with 71 adequately sampled even dips and 69 odd dips. At the Gaia period of 34.060743 d, the S66 and S100 predictions at 3123.8095 and 4077.5103 BTJD are adequately sampled and empty. S102's prediction is in a gap.

The displayed global box search peaks at 0.8689825 d and prefers a 0.049 d box. The adopted comparison ephemeris uses a robust linear fit of local window centers and gives sector median residuals within 0.005 d. S12 used 30-minute exposures. Its even/odd median corrected depths are 6.75/8.07 ppt. The corresponding values in S66, S93, S100, S102 and S103 are 8.81/9.02, 8.68/8.96, 7.43/7.57, 6.41/6.56 and 7.32/7.70 ppt. The short clock is a TESS aperture measurement. The two flux products cannot establish which source in the aperture varies.

| TIC | Disposition | Specific evidence |
| --- | --- | --- |
| 59974921 | Isolated depression | S8 shows a resolved dip. The S7 screen is mainly raw. Three near-complete Gaia predictions and five later covered 21.0832 d predictions miss. |
| 361991434 | SAP-only broad structure | 4–12 ppt depressions in SAP and approximately zero in corrected flux. The 13.979 d alias follows four consecutive raw troughs in S38/S39 and predicts brightenings in S65. |
| 447292888 | SAP-only or incomplete | S12 corrected depth is consistent with zero. Only 23% of S93's core is sampled. S100, S102 and S103 give well-covered Gaia misses. |
| 464807862 | Isolated depression | Four events were archived across sectors 5 and 98, but only S5 at 1454.4122 BTJD has clear depth in both products. Its core coverage is 69%. Gaia predictions at 2181.5249, 3999.3066 and 4025.2749 BTJD are empty. |
| 247474266 | Continuous variability | S43, S44, S45 and S71 show strongest sector modulation near 0.519 d. S72 shows mixed variability. The 20.2438 d S72 trough separation predicts an empty well-covered S44 window. |
| 22344332 | SAP-only broad structure | Both 1.6 d comparisons are under 2 ppt in SAP and vanish in corrected flux. The other Gaia window has insufficient baseline coverage. |
| 159769101 | Continuous variability | A ~0.295 d modulation accounts for the marked troughs. |
| 326353823 | Irregular short-timescale variability | Strong smooth dips recur on irregular sub-day timescales among other comparable peaks and troughs. |
| 295117482 | Continuous variability | Dominant individual sectors show roughly 0.35–0.36 d oscillatory variability. |

## Reproduce

From the workspace root, run `python sky/mixed-repeats-2026-11-24/batch3/short_clocks.py`, then `python sky/mixed-repeats-2026-11-24/batch3/review.py` with NumPy, Astropy, SciPy and Matplotlib installed. `review.py --root` accepts the common parent directory of `sky` and `Astra`.

- `*-sectors.png` shows local SAP and corrected QLP flux by sector. `*-events.png` centers on flagged archive windows and selected longer alternate clocks. `170337570-short-clock.png` shows the BLS scan and the phased event by sector.
- `archive-windows.csv` measures all archived dip windows. `predicted-windows.csv` measures Gaia, half and double Gaia, and additional clocks in `clocks.csv`. It contains predictions intersecting each sector's time bounds, including internal gaps. Cycles outside all sector bounds are unobserved.
- `sector-coverage.csv` lists time bounds and nominal sampling. `170337570-event-centers.csv` records locally fitted centers and residuals. `short-variability.csv` lists the strongest per-sector Lomb–Scargle signal between 0.2 and 17 cycles/day after subtracting a roughly two-day median filter. A strongest sinusoidal component can be a harmonic.
- Measurements retain finite positive quality-zero samples from original QLP FITS. Corrected flux uses KSPSAP_FLUX or its later DET_FLUX counterpart. Positive ppt depth is a median depression relative to a linear baseline through the two side-window medians. No long-baseline detrending is used in these window measurements. Depths calculated with two or more samples per side can still be unreliable at sector edges and within gaps.
- For the short-clock coverage count, a window needs at least 65% nominal cadence coverage, two samples on each side, and maximum core gap at most 0.029 d. All window CSVs report core and side counts, largest gap, and side scatter for evaluating other event widths.
- The camera-specific exposure guard uses the flagged sector 26 cadence numbers in the existing controls table. Batch 3 has no sector 26 data. The guard provides no control for other sectors.
- `outcomes.csv` records the visual and numerical disposition of each target. Epochs and widths for isolated dips describe observed windows.
