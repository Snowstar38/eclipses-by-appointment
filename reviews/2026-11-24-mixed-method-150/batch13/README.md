# Batch 13 | Brightening review

TIC 468915243 has a repeatable 0.925597540 d broad wave in all five available SAP sectors, with about 8 ppt full amplitude. Correction removes most of it. TIC 192515640 has a coherent ~0.199 d smooth wave in both products. The positive windows in these cases are wave maxima.

TIC 344767308's S85 peak is a partial step. At the same cadence, thirteen of 135 comparison apertures cross 3 ppt corrected brightening. TICs 294122936 and 315462449 show short flare-like peaks. TIC 267697387's sub-day pattern varies across visits. There is no coherent detached pulse in this batch. The camera guard removes one S26 exposure for TIC 198354782.

## Review files

- [Outcomes](outcomes.csv) lists all ten dispositions. Periods of smooth variables describe photometric modulation. Epochs for isolated events describe observing windows.
- [Original event measurements](archive-windows.csv), [covered predictions](predicted-windows.csv) and [sector coverage](sector-coverage.csv) use quality-zero QLP flux, with KSPSAP_FLUX or DET_FLUX as corrected flux. Signed depth is positive for a dip. Side-window medians define the local linear baseline. Coverage summaries require at least 65% core coverage and two cadences per side. Internal gaps are retained in the prediction table.
- The [independent scan](independent-scan.csv), [per-sector short periods](periodograms.csv), [background](background.csv) and [camera controls](camera-controls.csv) record supporting evidence. Controls compare cadence numbers within the same sector and camera. In control figures, gray lines are same-CCD SAP and the lower panel is target SAP_BKG. The roster is limited to cached QLP targets.
- The two visual-guide JPGs summarize the rendered and reviewed event panels. Individual sector plots mark Gaia predictions as dashed purple lines. Selected fold and time-series panels provide additional shape detail.
- Shared source is in [batch 11](../batch11). From the project directory run python -B batch11/review.py --batch batchNN, then python -B batch11/independent.py --batch batchNN and python -B batch11/controls.py --batch batchNN. The fold.py and refine_dips.py scripts regenerate folded diagnostics and short-dip coverage. Dependencies are NumPy, Astropy, SciPy and Matplotlib.
