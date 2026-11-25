# An asteroid check for apparent TESS eclipses

One of 20 fresh target apertures showed an apparent dip caused largely by light from **(4) Vesta**. It occurred near TIC 630314437 in sector 108 on 28 September 2026 at 16:00 UTC. Looking for an asteroid crossing the selected background pixels would have missed it. Vesta's center passed **0.42 pixel outside** their nearest edge, and its light spread into them. [Five TESS images](wide-track.png) · [Measured illumination by distance](illumination.csv) · [Spacecraft ephemeris comparison](ephemeris/vesta-wide.json)

## How the identification was made

We reserved 20 near-ecliptic apertures and searched 37 two-minute light curves. The primary search required positive stellar flux and a sustained loss relative to the baseline. It found zero qualifying fresh events in roughly 557.5 aperture-days of shortest-scale geometric coverage. Six windows from an earlier, more permissive version were visually reviewed. Four were dominated by noise and two showed broad changes across the field. The primary version was revised after development-control results and after the project lead had seen the provisional windows. [Roster and protocol](protocol.md) · [Primary measurements](photometry/findings.md) · [Pixel review](pixels/findings.md)

An exploratory second search started from a rise in estimated sky brightness paired with a drop in aperture flux. It allowed the reported flux to go negative. The rule recovered both development asteroids, Phocaea and Brixia, and selected exactly one fresh event. We measured a moving source in five wider TESS images without supplying its predicted position to the centroid fit. All five positions, spanning two hours, agreed with Vesta's JPL Horizons track as seen from TESS to within **7.3 arcseconds** (about one third of a pixel). [Search code](sky_seed.py) · [All three events with archive links](sky-seeds.csv) · [Five measured positions](wide-track.csv)

In the four-pixel stellar aperture, the median sky-subtracted flux fell from +78 to −92 electrons per second. Adding the estimated sky back gave a modest **increase** of 19 electrons per second. The raw detector counts also rose slightly. At the middle full-frame exposure, the six background pixels closest to Vesta brightened by a median of 1,730 electrons per second per pixel, versus 11 for the six farthest away. The photometry, motion and illumination gradient explain the apparent deep eclipse. A smaller simultaneous stellar event could still be hidden. [Target-pixel diagnostic](pixels/630314437-s108/diagnostic.png) · [Window measurements](pixels/630314437-s108/findings.md) · [Illumination calculation](illumination.py)

## Applying the check to another event

Supply the target pixel file and the event time. The command below uses BTJD (BJD on the TDB scale minus 2,457,000) and a half-window of 1.5 hours. The file can also be a public FITS URL. The two-pixel advisory margin is configurable.

```sh
python ephemeris/intercept.py target-pixels.fits --btjd 4312.172652 --half-hours 1.5 --margin-pixels 2 --out event.json
```

Read the coverage field first. The tool uses SkyBoT for candidates and JPL Horizons for the view from TESS. It records crossings and near misses separately for the stellar aperture, background pixels and full stamp. A clear result bounds the bodies, time, speed, brightness and margin actually searched. A geocentric fallback or an unpropagated candidate leaves partial coverage. Bright objects can illuminate pixels beyond the chosen margin. [Tool, worked example and limits](ephemeris/README.md)

For a nearby track, inspect the original pixels and compare sky-subtracted and restored flux on the same cadences. Keep a surviving source loss, poor coverage, excess restored light or an unexplained shape available for follow-up. The event window is the unit of assessment. This pilot used native SPOC two-minute data. Other extraction pipelines can use different sky estimates and masks.

## How much real dimming survives

On HD 276904 the primary screen preserved all 17 recurring eclipses in sector 59 and its separate deep event. In a stress test, we added the same smooth sky overestimate and a simultaneous simulated eclipse at one fixed time per fresh star. The counts below include all 20 apertures at each depth. The sky overestimate peaked at 20% of the local stellar flux. [Control events](photometry/controls-events.csv) · [Stress-test design](protocol.md) · [All 160 paired measurements](stress.json)

| Injected stellar depth | Stellar loss retained | Unresolved trigger | No trigger |
| --- | ---: | ---: | ---: |
| 1.5% | 5 | 1 | 14 |
| 5% | 7 | 0 | 13 |
| 15% | 9 | 0 | 11 |

None of those 60 mixed windows was classified as a clean background artifact. In a separate low-noise simulation, a shallow simultaneous stellar signal of a few parts per thousand could be absorbed into that classification. These are supplied-time tests on selected apertures. A quiet result leaves room for genuine dimming. This pilot adds one identified asteroid passage and no new eclipsing binary. [Low-noise injection grid](photometry/injection-grid.csv)

## Replay

Run the two commands in the photometry replay instructions using a common `--cache` directory to retrieve the original pilot and control light curves. From this directory, `python sky_seed.py CACHE` and `python stress.py CACHE` reproduce the exploratory search and fixed-time injections. `python wide_track.py CACHE` fetches the wider full-frame cutout, and `python illumination.py TARGET_PIXEL_FITS` measures the recorded background pixels using the five measured positions. The figure and tables are written beside the scripts. The frozen roster in batch.csv is the starting point for archive replay. [Photometry replay](photometry/findings.md) · [Ephemeris replay and archived responses](ephemeris/README.md)
