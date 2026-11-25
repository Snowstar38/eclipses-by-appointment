# TIC 356752132, sector 42 single event

The dip near BTJD 2454.7637 is a background-subtraction artifact. A bright positive feature moved along the edge of the target-pixel stamp, outside the five-pixel SPOC aperture. The background estimate rose across the whole stamp while aperture counts remained stable. The motion is consistent with a moving foreground object. Its identity and any changes elsewhere on the spacecraft were outside this check.

The native two-minute data are from camera 4, CCD 3. Comparing the 17 core cadences within 0.012 days of BTJD 2454.769 against 86 bracketing cadences, all at quality zero, gives the following median changes.

| Measurement | Core minus shoulders |
| --- | ---: |
| SAP_FLUX | −148.05 e−/s |
| PDCSAP_FLUX | −226.42 e−/s |
| SAP_BKG | +156.74 e−/s |
| SAP_FLUX + SAP_BKG | +11.50 e−/s |
| Raw aperture counts | +201.5 counts, about 0.019% of the baseline |
| Quiet off-aperture pixels, calibrated | −31.84 e−/s per pixel |
| Quiet off-aperture pixels, with background restored | +0.26 e−/s per pixel |

The background median image adds 31.35 e−/s per pixel across all 121 pixels. The brightest positive excess traverses 10 stamp rows over roughly four hours and is absent from the target aperture. The pointing corrections change by approximately 0.001 pixel in each axis between core and shoulders. The signal appears in both SAP and PDCSAP because the background subtraction is upstream of both.

CROWDSAP is 0.890. Interpreting the apparent 47.8% SAP loss as a real drop would imply a roughly 53.7% loss of target light after dilution correction. The aperture before that background subtraction shows a small gain, so dilution does not support any eclipse interpretation. This event should be excluded from astrophysical single-dip counts.

The archive URLs and FITS SHA-256 hashes are in evidence.json. window.csv contains matched cadences, flux controls and the moving excess positions. event.png shows the flux budget, spatial difference and motion.
