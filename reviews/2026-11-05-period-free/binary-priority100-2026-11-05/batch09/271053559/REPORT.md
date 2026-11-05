# T083 / TIC 271053559: PROBABLE

Queue stratum: repeat_sector_dip. Bounded physical review: complete. Catalogue novelty: UNKNOWN.

## Deciding evidence

Sector 89 contains a 313 ppt A eclipse at BTJD 3735.576 and two B eclipses at 3721.493 and 3746.148; the B spacing is 24.6552 d, near the Gaia SB1 24.6796 d. Explicit two-to-five-cycle shorter aliases predict intermediate B eclipses in fully covered s89 core windows, but none approaches the observed 50-55 ppt B depth. Prior vet23 measured all three in QLP and TARS, localized them on target pixels, and found no corresponding deep eclipse at covered earlier s8, s9 and s62 conjunctions. The present TESSCut difference peak is also on target. Gaia has a second 300.8-day astrometric solution, so evolving eclipse geometry is plausible but unproved.

## Measurement and scope

Gaia source 5523899796082005376; selection orbit 24.67963932843361 d; Gaia G 10.567686. The raw QLP SAP analysis inspected 5 hash-verified FITS sectors and 16 retained dip windows, including actual quality and time coverage. Local trapezoid centers, event depths, sectors, and source hashes are in [lead-numeric.json](lead-numeric.json); representative profiles are in lead-raw-*.png. These retained detector windows were not taken as verdicts.
Source packet SHA-256: da3d1f8ad69c6afa25a777fd475cd8ca50222cf2fb6c50a3af5c79f57b017663. Bulk-result SHA-256: 1a0db8d93fac0da1db5e4801077d5a0f153dc165996082d65cac062b12f18e55.

Selected same-kind fit: P = 24.655219 d; T0 = 3721.492796 BTJD; conditional formal period error = 0.001636819 d.
Cycle numbers, chosen eclipse kind and residuals: [lead-timing.json](../lead-timing.json).

The helper independently extracted the strongest event from TESSCut with a positive-flux target aperture and checked the difference pixels; see [helper audit](../helper-audit.md), [numeric pixel audit](../helper-pixel-audit.json), and helper-difference.png. It is a second reduction of the same TESS photons.

Prior target-specific receipt: [local-path-redacted] 5.1\made\appointments\vet23\REPORT.md, section 4; SHA-256 de0535249ca2890408e10e04c13a3e23784367ef5b0921aabcc26cc8edf63348. The older data and precession hypothesis are reused as documented. Explicit within-sector alias checks: [lead-alias-t083.json](../lead-alias-t083.json).

## Limits and next check

The real on-target eclipses repeat within sector 89, yet the same ephemeris failed in earlier covered sectors. A persistent Gaia-orbit eclipse geometry or precession explanation is unproved, leaving a failed stability check and a probable verdict. Prior local investigation is not a published exact-target eclipse match; four current catalogue gates remain unknown. TESS s110/s111 are planned rather than available in the present footprint query.

Measure the next available sector 110/111 eclipses and compare depth and timing with the sector 89 events; obtain radial velocities of the proposed outer body.

Catalogue status uses the [shared queue-wide audit](../../shared-catalogues/REPORT.md). Its four unavailable VizieR gates are unknown, not negative matches.
