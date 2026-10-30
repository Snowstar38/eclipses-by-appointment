# Batch E reproducibility and review notes

Ten full reviews, all physical CONFIRMED; component characterization and novelty are separate. Source CSV/vet folders rechecked before taking targets; no original edits or commits.

Use RESULTS.csv/JSON; absolute REPORT paths. Own fit, covariance, secondary/coverage, geometry, independent reduction, pixel and archives receipts are preserved. Bulk FITS are ignored in data/. A/previous scripts were copied and adapted within E; do not rerun make_reports.py on arbitrary targets as an automatic classifier.

Important portability fixes: handle SB2 bit255/21 correlations (323434013) with seven-parameter covariance order, verified against ESA; raw primaries can have fewer than two distinct acceptable events (365181558), so period is explicitly held and error null. Full resolved period is necessary when P2 search has higher z (323434013 and377656542). 119301005 needed a widened shape grid; old upper-bound duration was biased.

119301005 is broad and variable; baseline sensitivity remains material, geometry lacks TIC radius/mass. Its nearby known EA at2.44349d is distinct; own pixel target attribution favors target. 377656542/323434013 fixed-TIC geometry is poor and not a measured e sin omega constraint. 82620363 null limits are width/baseline sensitive; do not quote one blanket tight limit.

Pixel model is a circular Gaussian calibrated on own Gaia cone positions; it is a source discrimination experiment with residual mismatch, not a calibrated high-precision centroid. Same TESS pixels/alternate reductions are not an independent observatory. All capable-neighbor tests favor target event-by-event. Broad/missing secondary windows retain exclusions in JSON.

Primary event and secondary event errors include red-noise/cadence floors; phase-optimized formal significance is not a blind discovery significance. Null tests are pointwise conditional over five widths/nine phases; geometry radii hypotheses do not constrain real components. Future predictions are conditional, especially365181558.
