# Where the lost light falls in the full-frame pixels

Forty-eight of 51 event windows favor the nominal Gaia DR3 position. All 13 stars with an alternate period in Fable's transferred table and three further stars from Sol's independent search have at least two sectors with a compact source-centered loss. The largest offset in these 48 events is 3.10 arcseconds (about 0.15 TESS pixel). These tests locate light lost at supplied times. Timing, system classification and prior discovery credit have separate assessments. [Measured fits](fits.csv) · [Selected events](windows.csv) · [Archive URLs and SHA-256](inputs.csv)

| TIC | Sectors with stable localization | Stable windows | Largest target offset (arcsec) | Other windows |
| --- | --- | ---: | ---: | --- |
| [17131560](17131560.png) | 14, 75 | 4 | 1.12 | |
| [51271205](51271205.png) | 48, 49 | 2 | 1.22 | Sector 76 has no covered right shoulder |
| [76044496](76044496.png) | 26, 52 | 4 | 1.62 | Sector 26 shallow event also has broad sky variability |
| [86121903](86121903.png) | 25, 52 | 4 | 0.85 | A plausible neighbor is about half a pixel from the fitted center |
| [91357417](91357417.png) | 17, 42, 71 | 4 | 3.09 | One sector 71 primary changes location between one-sided baselines |
| [155230509](155230509.png) | 44, 72 | 2 | 0.54 | |
| [199572139](199572139.png) | 15, 85 | 2 | 3.10 | |
| [219113068](219113068.png) | 16, 55 | 2 | 0.43 | |
| [219433150](219433150.png) | 14, 75 | 4 | 1.61 | |
| [237115356](237115356.png) | 16, 81 | 2 | 0.86 | |
| [243241330](243241330.png) | 17, 43 | 2 | 1.25 | |
| [328775473](328775473.png) | 19, 53 | 3 | 2.27 | A plausible neighbor is 9.8 arcseconds from the fitted center |
| [345352706](345352706.png) | 24, 51 | 2 | 0.21 | |
| [376993642](376993642.png) | 21, 77 | 4 | 1.24 | Both eclipse families give the same position |
| [416116421](416116421.png) | 25, 41 | 3 | 1.61 | |
| [458654591](458654591.png) | 7, 44, 72 | 4 | 1.20 | Sector 72 shallow event has no covered left shoulder |

The windows come from the timed dips in Fable's 35-row transfer. For each of its 13 fitted clocks we took the first and last sectors containing a primary, then the deepest measured event in each available phase family in each sector. A primary lands within the larger of 0.4 day and 2% of the trial period from phase zero. We also sampled one intervening sector each for TIC 51271205, 91357417 and 458654591 after the endpoint extractions showed missing baseline or instability. For TIC 376993642, Sol supplied the 13.1994337-day trial clock with epoch BTJD 1689.78739. We checked one primary and one other-family dip in each of two well-separated sectors (21 and 77) after a ground-survey cross-check motivated the additional target. TIC 219113068 and TIC 243241330 subsequently showed matching dimmings from the ground. We tested the earliest and latest hit in Sol's alternate-period PDC series per star, with an inner core spanning 60% of the fitted full duration. The window table records the sector, measured time, core width, Gaia ID and trial ephemeris for every attempted event.

The images use native TESS-SPOC full-frame target pixel files at quality zero. We take the median per pixel within half the reported core width on each side of the event center. Left and right baseline medians span 1.35 to 2.7 core widths from the center, with at least three cadences in each interval. Linear interpolation between the baseline medians gives the expected image at the event. Red shows the flux missing from that image. Each panel has a separate intensity scale.

We propagate Gaia DR3 coordinates to the exposure year using available proper motions and register the out-of-eclipse scene to the pixels with a common Gaussian width, displacement, brightness scale and background. We fit the centroid of the difference image independently. The orange crosses show Gaia stars within 90 arcseconds that could contribute at least one quarter of the undiluted eclipse depth in relative flux, using RP or G where RP is absent. The aperture mask is outlined in gray. A window favors the target when the loss center is within 8 arcseconds of its registered position and at least 8 arcseconds closer to it than any screened neighbor. The one-sided baseline and background-restored fits must each reproduce the difference centroid to within 8 arcseconds, and the scene registration must avoid its displacement bound. These thresholds describe a sensitivity check. The small measured offsets carry additional uncertainties from the approximate point-spread function, bandpass, catalog coverage and source blending. Close companions unresolved by TESS or Gaia can share the centroid.

All 48 stable windows retain a local loss after restoring FLUX_BKG and removing the median difference at distances greater than 3.5 pixels from the target and outside the pipeline aperture. One event illustrates the distinction. At the sector 26 shallow minimum of TIC 76044496, the aperture loses 41.39 electrons per second after pipeline sky subtraction. The sky-restored aperture gains 27.76 electrons per second amid a broad field change. Relative to the surrounding pixels, the local loss is 41.68 electrons per second. Its sector 52 counterpart also localizes on the target. The 16 rendered figures were inspected for spatial structure.

## Replay

Python requires numpy, scipy, astropy, matplotlib and requests. Run the commands below from this directory. The first downloads the 35 TESS pixel files, uses the archived Gaia scenes and verifies input hashes. The second writes the event table and charts.

~~~sh
python retrieve.py CACHE_DIRECTORY
python measure.py CACHE_DIRECTORY
~~~
