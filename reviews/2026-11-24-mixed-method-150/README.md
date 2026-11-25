# 150 more mixed-method TESS leads

We reviewed 150 distinct stars in fifteen groups of ten, using 1,693 original target-sector QLP light curves. Four apertures picked up previously identified eclipsing binaries in neighboring stars. No new host qualified for the eclipse catalogue. This brings individually reviewed targets from the original pool of 2,904 to 600, with 2,304 still outside these reviews. [Individual outcomes](outcomes.csv) · [Target roster and original screening ranks](roster.csv)

## Where the eclipses came from

| Nominated target | What repeated in TESS | Source of the light loss |
| --- | --- | --- |
| TIC 240799649 | Deeper and shallower eclipses every 0.456000 d. Four sectors contributed 204 primary and 206 secondary windows to the images. | All eight eclipse centers fall within one arcsecond of the known contact binary WISE J004852.7+510946, 63.8 arcseconds from the target. Independent ZTF green and red measurements show the deeper eclipse at the phase predicted by TESS. [Images](followup/240799649.png) |
| TIC 307642177 | Unequal minima every 0.35888635 d, with 192 covered primary and 197 covered secondary windows. | Three sectors independently locate both eclipses within one arcsecond of WISE J032146.2+595213, about 59 arcseconds away. [Images](followup/307642177.png) |
| TIC 37378337 | 157 covered minima spaced 0.60029538 d apart. | Four sector images favor Gaia DR3 5647533728231982976, 26.4 arcseconds away. Its published 1.20059987 d orbit accounts for two minima each cycle. [Images](followup/37378337.png) |
| TIC 156991337 | A roughly 0.08% dip repeated at all 20 covered predictions, every 6.90564 d. | This is the published TOI-691.01 signal. Ground-based follow-up in 2021 identified an eclipsing binary in the nearest neighbor. TESS images favor Gaia DR3 5569479844450569216, with appreciable scatter between sectors. [Images](followup/156991337.png) · [ExoFOP observing record](https://exofop.ipac.caltech.edu/tess/target.php?id=156991337) |

## A moving asteroid and a switching pixel

On 2024 September 29, light in the aperture of TIC 137785497 rose by 52%. The TESS images show a bright point crossing the field in about 1.6 hours. All 20 measured positions are 3.05–3.86 arcseconds from the JPL Horizons track of **(1036) Ganymed** as seen from TESS. An Earth-centered search placed Ganymed about 12 arcminutes from the TESS field position at the search time. The observer location matters when checking apparent stellar events against asteroid tracks. [Watch the crossing](followup/ganymed.gif) · [Measured positions](followup/track-137785497.csv) · [Horizons ephemeris](followup/horizons-1036.txt)

TIC 219846230 showed three square dips in both the raw and corrected aperture light curves. Each loss came from the same detector pixel, switching by 56–60 electrons per second. The eight adjacent pixels lacked the change that nearby stars' measured light profiles predict. The evidence points to an unstable pixel. [Native pixel time series](batch14/219846230-native-pixel.png)

## What remains open

Six multi-sector dip leads retain explicit open dispositions, and other entries retain isolated events. TIC 341293943 has five broad minima near a 38.87 d interval, with timing and image locations sensitive to how the baseline is measured. Independent ground photometry did not resolve those six cases. None of the 30 brightening leads established a new heartbeat system. [Open-lead ground tests](batch06/ground-open/README.md)

An additional search fitted periods on earlier TESS sectors and carried those predictions into later sectors. Twenty-two targets passed its repeatability screen. Several folded into smooth waves with broad minima. The separate ground check used fixed TESS phases and obtained usable ASAS-SN or ZTF series at 146 of 150 target positions. Only two known neighboring binaries passed the ground threshold at their own coordinates. Sparse coverage and noisy photometry limit the interpretation of misses. [Later-sector results](independent/later-repeats.csv) · [Fold gallery 1](independent/folds-1.png) · [2](independent/folds-2.png) · [3](independent/folds-3.png) · [Ground measurements](ground/fixed-windows.csv) · [Resolved ZTF light curves](ground/ztf-neighbors.png)

## Selection and reproduction

The roster contains 100 multi-sector dip leads, 30 brightening leads and 20 single-sector dip leads. Half of the multi-sector sample had a period suggested by the earlier recurrence search. These targeted choices limit comparisons of yield. Individual reports include measured windows, rejected trial periods, gaps, and plots for all ten stars in each group.

**Batch reports** · [01](batch01/README.md) · [02](batch02/README.md) · [03](batch03/README.md) · [04](batch04/README.md) · [05](batch05/README.md) · [06](batch06/README.md) · [07](batch07/README.md) · [08](batch08/README.md) · [09](batch09/README.md) · [10](batch10/README.md) · [11](batch11/README.md) · [12](batch12/README.md) · [13](batch13/README.md) · [14](batch14/README.md) · [15](batch15/README.md)

From this directory in a repository checkout, run `python inputs/prepare.py 7` and `python batch06/review_lane.py 7` to reproduce the batch 07 event measurements. The first command verifies every downloaded FITS file against its archived SHA-256. Substitute another group number when preparing its inputs, adding `--controls` for the optional same-camera comparison stars. Dependencies include Requests, NumPy, SciPy, Astropy and Matplotlib. [QLP input manifest](inputs/qlp.csv) · [TESS image inputs](followup/inputs.csv) · [Pixel measurements](followup/measurements.csv)
