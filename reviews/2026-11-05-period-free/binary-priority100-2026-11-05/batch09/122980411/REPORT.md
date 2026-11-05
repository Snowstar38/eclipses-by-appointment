# T085 / TIC 122980411: REFUTED

Queue stratum: repeat_sector_dip. Bounded physical review: complete. Catalogue novelty: UNKNOWN.

## Deciding evidence

The QLP raw light curve contains a strong 4.23712-day double-eclipse train, including the sector-7 1492.016 dip. This is not a target eclipse: the prior dedicated vet122980411 investigation stacked both kinds across three sectors and found deficit centroids 0.5-0.7 TESS pixels east of the target, within 0.2-0.35 pixels of HJ 68 B. Single-source fits favored that 17-arcsec neighbor by delta chi-square 1,300-48,600. Deblended TGLC s7 primary depths were 3.6% at the queued target versus 40.7% and 51.9% for the two Gaia components of B. The present independent TESSCut signed difference moment also points toward B.

## Measurement and scope

Gaia source 3080899205293455232; selection orbit 51.02521925734591 d; Gaia G 10.89651. The raw QLP SAP analysis inspected 4 hash-verified FITS sectors and 16 retained dip windows, including actual quality and time coverage. Local trapezoid centers, event depths, sectors, and source hashes are in [lead-numeric.json](lead-numeric.json); representative profiles are in lead-raw-*.png. These retained detector windows were not taken as verdicts.
Source packet SHA-256: 42eb3331f58c79a64eda4b79a219ed7836f727df1ddef3e35f260384a3ebb221. Bulk-result SHA-256: e92009ae3432aebfc71e4c958715f72641bd7cdcc9424775f576101bc20ecb4d.

No supported unique same-kind eclipse period is reported for this queued target.

The helper independently extracted the strongest event from TESSCut with a positive-flux target aperture and checked the difference pixels; see [helper audit](../helper-audit.md), [numeric pixel audit](../helper-pixel-audit.json), and helper-difference.png. It is a second reduction of the same TESS photons.

Prior decisive source receipt: [local-path-redacted] 5.1\made\appointments\vet122980411\progress.md; SHA-256 dcdf8adfc0a076e5d5c92a9452215d8e35ee692ae48acbb4134535c682cae100. Its pipeline comparisons and stacked difference-image PSF test supersede the single current cutout.

## Limits and next check

The neighboring EB is real; this verdict refutes its assignment to the queued Gaia SB1 target, whose distinct 51.025-day spectroscopic orbit is not disproved. The present single-event moment alone would be insufficient; prior stacked PSF/deblended evidence decides attribution.

If revisiting the 51.025-day Gaia target orbit, search for a separate target-centered eclipse after modeling HJ 68 B contamination.

Catalogue status uses the [shared queue-wide audit](../../shared-catalogues/REPORT.md). Its four unavailable VizieR gates are unknown, not negative matches.
