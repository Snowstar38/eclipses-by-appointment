# T090 / TIC 71294892: PROBABLE

Queue stratum: repeat_sector_dip. Bounded physical review: complete. Catalogue novelty: UNKNOWN.

## Deciding evidence

A dense raw eclipse train across sectors 20, 47, 60, 73 and 74 has 18 selected same-kind centers fitting about 3.208895 d (cycles 0-462; largest residual 0.021 d, dominated by coarse/variable profiles). Another eclipse kind is interleaved. The independent TESSCut aperture sees a target-region 139 ppt dip. Gaia SB2 period 23.932237 +/- 0.001717 d is not an integer multiple of the short eclipse clock.

## Measurement and scope

Gaia source 1108499486795034368; selection orbit 23.932236512546446 d; Gaia G 11.143923. The raw QLP SAP analysis inspected 5 hash-verified FITS sectors and 20 retained dip windows, including actual quality and time coverage. Local trapezoid centers, event depths, sectors, and source hashes are in [lead-numeric.json](lead-numeric.json); representative profiles are in lead-raw-*.png. These retained detector windows were not taken as verdicts.
Source packet SHA-256: aa04653ec57914cdcb9d0906dd3ae672c0973da8441defc09c4a978652e3e3a4. Bulk-result SHA-256: 4be5baa044c8558648e7b8a6a0b610a417f4ebc529230357dc377048ebe5fba8.

Selected same-kind fit: P approximately 3.2089 d; T0 = 1843.975913 BTJD; formal period error not reported because profile scatter/systematics dominate.
Cycle numbers, chosen eclipse kind and residuals: [lead-timing.json](../lead-timing.json).

The helper independently extracted the strongest event from TESSCut with a positive-flux target aperture and checked the difference pixels; see [helper audit](../helper-audit.md), [numeric pixel audit](../helper-pixel-audit.json), and helper-difference.png. It is a second reduction of the same TESS photons.

## Limits and next check

The short-period binary may be an unresolved component or a separate system within the aperture. The precise physical connection to the Gaia SB2 is unproved; the formal fit error understates profile and pipeline systematics.

Deblend the aperture and compare separate eclipse kinds in an independent pipeline and spectroscopy to identify the 3.209-day system.

Catalogue status uses the [shared queue-wide audit](../../shared-catalogues/REPORT.md). Its four unavailable VizieR gates are unknown, not negative matches.
