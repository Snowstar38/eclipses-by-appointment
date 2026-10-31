# Independent helper audit

## TIC 277542587

KELT cleaned time series, scan script, report, fold table and fold figure audited. The plot shows a sharp peak and concentrated deficit near phase zero. Independently reran the script's `load` and `scan` on a 0.00005 d grid, anchored to BTJD 3488.8242: central half best 24.33180 d, S/N 13.31, depth 4.64%, 28 points. Split at JD 2456658 gives 10.83 (12 points) and 8.32 (16 points), corroborating the signal across separated epochs. The range within one S/N unit of peak is 24.33170–24.33180 d, but this is a heuristic peak-width measure, not a calibrated 1σ interval. The published ±0.0002 d is a working uncertainty, not independently established by this audit; avoid portraying it as a formally measured 1σ error. S/N is point-based, and temporal correlations or search trials are not accounted for. Reproduction groups the 28 points by floor(JD) into 8 bins, whereas SINGLES reports 10 nights: date definition or implementation requires checking before repeating that exact count. The multi-year signal remains evident. TESS A/B are one-sector events; KELT repeated signal tests period independently. The coarse archived fold table/figure peaks at 24.33200, consistent with the finer grid and should not be confused with the fine estimate.

## TIC 8853239

Historical report records one A event; inspected `pix_s48.png`: deficit concentrated at target. The KELT scan is coverage-limited with no reliable second detection; many Gaia-compatible periods remain untested. Current bounded criteria: plausible, not confirmed/probable from repetition. A later-sectors note checked here concerns four different objects and supplies no additional coverage check for this TIC. No claim that subsequent sectors do not exist.

## TIC 12864953

One A+B pair in s69; one of each kind does not measure a period. Inspected `pix3_B_W0.6.png`: deficit centred on marked target. Historical report states s29 QLP all NaN and TESScut off detector, so it cannot test a repeat. Photometric separation differs from Gaia prediction by 3.4σ, conditional on Gaia P; do not explain away as established error. Current criterion: plausible, with period untested and tension retained. KELT note says no matching source in the relevant field; later-sectors NOTE concerns four different targets and supplies no newer coverage assessment. No assertion all later data have been exhausted.

Source hashes, including inspected figures, are in `terra/sources.csv`; reproducible calculation in `terra/recheck.py`. Other targets and full five-check audit are assigned to the batch lead. No historical report was edited.
