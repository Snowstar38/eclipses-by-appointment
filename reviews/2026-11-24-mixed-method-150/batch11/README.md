# Batch 11 | Brightening review

The four-sector feature in TIC 345949499 is a broad asymmetrical SAP wave, about 50 ppt peak-to-trough. The highest local Fourier peak is 0.799113891 d, with comparable aliases. The separately tested 0.79995844 d ephemeris recovers broad maxima in the late sectors. Corrected folds have smaller two-peaked structure. The folded profile has a broad crest. TIC 267687143 also has changing broad sub-day waves and local background covariance, with a strongest component near 0.465 d.

The largest individual pulse, TIC 137785497 S83 at 3582.8748 BTJD, peaks at about 520 ppt in both QLP products, far larger than the matched camera peers. The difference-image peak lies 101.13 arcsec from the nominal target. In the original images, a moving object traverses the 15-pixel stamp in about 1.6 hours and passes closest to the star at the QLP brightening peak. The moving source matches asteroid (1036) Ganymed within 3.05 to 3.86 arcsec in all 20 measured exposures. [Measured track and spacecraft-view positions](../followup/track-137785497.csv) Separate smaller S16 and S75 events have faster rises and slower decays. [Difference-image measurements](../followup/measurements.csv)

The camera guard removes one S26 exposure each for TICs 356701988 and 160535350.

## Review files

- [Outcomes](outcomes.csv) lists all ten dispositions. Periods of smooth variables describe photometric modulation. Epochs for isolated events describe observing windows.
- [Original event measurements](archive-windows.csv), [covered predictions](predicted-windows.csv) and [sector coverage](sector-coverage.csv) use quality-zero QLP flux, with KSPSAP_FLUX or DET_FLUX as corrected flux. Signed depth is positive for a dip. Side-window medians define the local linear baseline. Coverage summaries require at least 65% core coverage and two cadences per side. Internal gaps are retained in the prediction table.
- The [independent scan](independent-scan.csv), [per-sector short periods](periodograms.csv), [background](background.csv) and [camera controls](camera-controls.csv) record supporting evidence. Controls compare cadence numbers within the same sector and camera. In control figures, gray lines are same-CCD SAP and the lower panel is target SAP_BKG. The roster is limited to cached QLP targets.
- The two visual-guide JPGs summarize the rendered and reviewed event panels. Individual sector plots mark Gaia predictions as dashed purple lines. Selected fold and time-series panels provide additional shape detail.
- Shared source is in [batch 11](../batch11). From the project directory run python -B batch11/review.py --batch batchNN, then python -B batch11/independent.py --batch batchNN and python -B batch11/controls.py --batch batchNN. The fold.py and refine_dips.py scripts regenerate folded diagnostics and short-dip coverage. Dependencies are NumPy, Astropy, SciPy and Matplotlib.
