# Batch 6 | Ten single-sector QLP leads

The strongest pair in the TIC 212431508 aperture recovers the known project lead T092 via spillover from TIC 212431520. In S81, trapezoid fits give the following event times and depths. Quoted depths are peak SAP model depths.

| Event | Center BTJD | Width (d) | TIC 212431508 (ppt) | TIC 212431520 (ppt) |
| --- | ---: | ---: | ---: | ---: |
| Primary | 3512.51681 | 0.82583 | 130.19 | 179.98 |
| Secondary | 3532.14421 | 0.22385 | 42.58 | 57.65 |

The adjacent aperture is about 36 arcsec away. The deeper event is strongly attenuated by the QLP correction, but the original SAP eclipse is coherent in both apertures. The current TESS-SPOC difference-image fit places the primary flux deficit 0.592 arcsec from Gaia DR3 4230027841458799744 (TIC 212431520) and 36.235 arcsec from the nominal target. Left/right baseline sensitivity is 0.11 arcsec. The late event has inadequate pre-event imaging coverage for that fit. The prior November 5 T092 report records the same primary in TIC 212431520, which also has an existing Kostov et al. machine flag. The two apertures sample the same primary photons. [Pixel-fit measurements](../pixels/fits.csv) · [T092 source report](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-05-period-free/binary-priority100-2026-11-05/batch10/212431520/REPORT.md) · [Current aperture comparison](212431508-212431520-eclipse-pair.png)

The nominal target's 29.32834 d Gaia clock places the only S54 primary prediction in a gap near 2779.30829 BTJD. The simple 19.62741 d spacing test predicts an empty S54 window at 2786.30270 BTJD, and doubling that separation predicts an empty secondary there. The depths and durations are unequal. The orbital clock remains unestablished.

The other nine leads have specific background or common-exposure explanations. The strongest common-mode grouping is S94. TICs 254045444 and 276602565 show the same S94 camera 1 CCD 4 raw dip at 3869.5119 BTJD. At that cadence, 28 of 61 camera peers with at least 22% core sampling and sufficient side samples have raw losses over 3 ppt. None crosses that threshold in corrected flux. The later S94 3874.8057 window shows the same pattern in 36 of 37 sampled camera peers. These are counts in the locally cached QLP catalog. The camera comparison is especially diagnostic where the phase window is heavily gapped.

TIC 236784353 retains ~29 ppt in corrected S14 flux, but its deepest dip coincides with a square ~30,000-unit rise in the target's QLP background estimate. S14 1690.8853 and 1692.7604 also show strong matched changes. The 17.6043 d separation produces 54 adequately sampled predictions and only the two S14 anchors dip above 3 ppt in both products. The 3.1459 d test produces 281 adequate predictions and three matches, all in S14. At nominal Gaia epoch, one of 28 adequate windows shows a deep dip. QLP records from forty-two sectors were available.

TIC 160617691 has ten S51 windows with two-product drops over 3 ppt on the local 1.013873 d clock. Their broad shapes covary with the local background. None of the other 836 adequately sampled predictions crosses both thresholds. QLP records from forty sectors were available. TIC 150969347's apparent independent S57 dip is a side-window brightening that inflates a relative depth estimate, as the local chart shows.

## Reproduce

Run the following scripts in this directory using Python with NumPy, SciPy, Astropy and Matplotlib. They derive the workspace root from the directory of the script. The fitted comparisons use local original QLP FITS, the archived screen JSONs, and the camera-specific sector 26 guard. S26 contains one guard exposure in the TIC 236784353 time series.

1. `python -B review.py` writes original per-sector and event plots, all archived-window measurements, sector coverage and predicted windows for Gaia, its half and double harmonics, and manually selected local clocks.
2. `python -B scan_other_sectors.py` ranks independent dips in both products over each complete sector for 0.12, 0.24, 0.48, 0.96 and 1.6 d widths. The classifier uses window means as a first pass and reports side-median signed depths for the resulting candidates. Inspect the actual shapes before interpreting these ranks.
3. `python -B controls.py` matches windows by exposure cadence number within each sector and camera and generates target and comparison-star diagnostic plots. Gray lines are same-CCD SAP comparisons. Positive comparison depths are losses relative to the linear local baseline. Negative `bkg_native` is an increase in SAP_BKG.
4. `python -B fit_pair.py` writes both aperture fits for the S81 pair and their direct visual comparison.

Numeric coverage tallies require at least 65% nominal core sampling plus two measurements on each side, except the separate common-mode screen described above. Window tables also retain maximum core gap and side-window scatter. Quality-zero samples are used in both flux series. Corrected QLP flux uses KSPSAP_FLUX or DET_FLUX depending on product generation. [Disposition of all ten targets](outcomes.csv)
