# T088 / TIC 287035536: PLAUSIBLE

Queue stratum: repeat_sector_dip. Bounded physical review: complete. Catalogue novelty: UNKNOWN.

## Deciding evidence

A deep raw s50 eclipse-shaped event near BTJD 2670.511 and a shallower s77 event near 3422.485 are real in two different observing occasions; independent TESSCut extractions show about 219 and 30 ppt in target-region apertures. Their separation and Gaia phases do not form a demonstrated same-kind 31.75594-day clock. A 12.16-arcsec Gaia neighbor with approximate G flux ratio 0.04 could supply the s77 blended depth.

## Measurement and scope

Gaia source 1241798366670426112; selection orbit 31.75593679485067 d; Gaia G 11.402299. The raw QLP SAP analysis inspected 2 hash-verified FITS sectors and 2 retained dip windows, including actual quality and time coverage. Local trapezoid centers, event depths, sectors, and source hashes are in [lead-numeric.json](lead-numeric.json); representative profiles are in lead-raw-*.png. These retained detector windows were not taken as verdicts.
Source packet SHA-256: f228f58cb379f8e167d01e5fcfe3376a482cf0db48583a8a65593324a223c0d4. Bulk-result SHA-256: 4d1b456aa234eecdc1b5c8725f2db0c2453bc44641be52bb4b216e522bd1be82.

No supported unique same-kind eclipse period is reported for this queued target.

The helper independently extracted the strongest event from TESSCut with a positive-flux target aperture and checked the difference pixels; see [helper audit](../helper-audit.md), [numeric pixel audit](../helper-pixel-audit.json), and helper-difference.png. It is a second reduction of the same TESS photons.

## Limits and next check

The two events have very different depths, are at different Gaia phases and are not securely attributed to one source or eclipse kind. There is no measured repeating period. The Gaia-neighbor flux ratio is only an approximate screening bound.

Use source-resolving difference/PSF photometry for both events and obtain another same-kind eclipse before testing cycle aliases.

Catalogue status uses the [shared queue-wide audit](../../shared-catalogues/REPORT.md). Its four unavailable VizieR gates are unknown, not negative matches.
