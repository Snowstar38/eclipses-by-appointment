# Independent phase and window review of 35 TIC targets

This review uses the 35 recorded ephemerides in `../batch.csv` and the original TESS-SPOC FFI cadence cache in `sky/data/fable52-ffi-tce-2026-11-24/cadences`. The groups are reviewed in batch order (10, 10, 10, 5). Candidate discovery uses only cadence times and flux, independent of the recorded ephemeris and machine flag.


## Results

The review found 15 alternate clocks and four additional alternatives with competing aliases. Nine recorded clocks are inconsistent with sensitive covered windows and have no strong replacement, six targets are inconclusive, and one is coverage-limited. All 19 alternates have PDC dips in both temporal halves and the same significant-window count in SAP. The strongest repeats were TIC 376993642 at 13.19943 d (39/39 windows, 20 sectors), TIC 199572139 at 16.63696 d (29/29, 21 sectors), TIC 219433150 at 17.49269 d (16/16, 10 sectors), and TIC 219113068 at 21.77567 d (10/10, nine sectors).

Competitive aliases include TIC 17131560 at 37.73086 and 25.15496 d, TIC 76044496 at 39.94766 and 26.63495 d, and TIC 247785232 at 24.55146 and 24.46488 d. For TIC 91357417, closely spaced 20.30 d solutions compete on phase and window placement. TIC 76044496 also lies near the 40 d search boundary. TIC 437693405 has four significant recorded windows in its only cached sector.
## Reproduce the audit

Run `python sky/fold-test-2026-11-24/fable-fold-35/sol/audit.py` from the workspace root with Python, NumPy, SciPy, and Astropy. The run used NumPy 2.4.2, SciPy 1.18.1, and Astropy 8.0.1. Use `--group 1` through `--group 4` to reproduce separate group outputs. `--cache` and `--batch` override the defaults. `--recheck` repeats the coverage, SAP, and alias annotations using the saved search output.

- `outcome.csv` gives one outcome and reason per TIC. Ephemerides are in days and BTJD (BJD − 2,457,000). Depth is in parts per thousand. Period and epoch values are grid estimates, and their displayed digits are not error bars.
- `candidates.csv` records 18 independently searched candidates per TIC, ranked by window recurrence, with their BLS scores and timing relation to the recorded clock.
- `events.csv` records every covered recorded and alternate window tested in PDC and SAP, including local depth, noise estimate, significance, and the sensitive-empty flag. The expected-window total in `outcome.csv` uses sector spans, so major gaps between sectors are excluded from that total.

## Timing tests

1. Filter finite positive flux, sort by time, and break each sector at gaps larger than 0.35 d. Divide each block by a smoothed 2.2 d running 65th-percentile baseline. Search and evaluate hourly median flux with a robust scatter estimate per block.
2. Run a weighted Box Least Squares search over 0.60–40 d using nominal durations 0.09, 0.17, 0.30, and 0.52 d. Retain 18 separated high BLS peaks and rank them by significant-window count, hit fraction, sectors with hits, and sensitive empty windows. Separately test the exact recorded epoch, the best phase at the recorded period, and fixed half- and double-period fits.
3. Evaluate each predicted center using the median of central samples against the average of the two shoulder medians. A window needs samples near the center and on both shoulders to count as covered. A significant dip exceeds three times the local noise estimate. A covered window is sensitive and empty when its depth plus two estimated uncertainties falls below 45% of the median significant depth for that clock. In the absence of a significant dip, there is no reference for this flag. Coverage gaps are tabulated separately.
4. Check early and late groups using the midpoint of the observed time span. Compare alternate PDC events with SAP, inspect phase-center depth, ingress and egress shoulders, relative half-phase depth, odd/even median-depth difference, and alternate half-phase windows. Flag competing retained clocks when they would drift by an eclipse width or differ in phase and their recurrence score is within 10% of the top clock.

An alternate clock requires at least three significant PDC windows in at least two sectors, at least 65% of covered windows significant, and at most one sensitive empty window. A distinct or harmonic period must improve the recorded clock by this criterion or by producing fewer sensitive empty windows. A same-period solution with an independently recovered epoch is reported separately. SAP and alias annotations qualify this result. A recorded clock with at least two sensitive empty windows and no strong replacement is classified as inconsistent. Inconclusive rows have insufficient repeat evidence to support a clock under these thresholds.

## Limits

These are flux-window tests of the cached apertures. SAP and PDC share photons and do not establish sky localization or host identity. TESS gaps can leave distinct cycle counts observationally equivalent, and identical alternating eclipses can double the orbital period. Independent candidates were selected and scored on the same sectors, so early/late counts measure stability in the available record. The local uncertainties are screening estimates and do not include a trials-wide false-alarm correction. Hourly binning reduces sensitivity to narrow events, and the detrending can attenuate broad or shallow variability. This search can miss periods outside its range, eclipse durations away from the searched boxes, and changing or nonperiodic events.
