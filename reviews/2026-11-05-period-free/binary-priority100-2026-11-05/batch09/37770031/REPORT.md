# T081 / TIC 37770031: PROBABLE

Queue stratum: repeat_sector_dip. Bounded physical review: complete. Catalogue novelty: UNKNOWN.

## Deciding evidence

Five coherent same-kind deep raw eclipses in sectors 6, 33 and 87 have a 10.5182414-day clock (cycles 0, 1, 70, 71, 209; max selected fit residual 0.0003 d). Other flagged events sit at a distinct phase. The stronger local event is about 290 ppt, and the independent TESSCut aperture shows a target-region deficit. The Gaia SB2 orbit is 40.00793 +/- 0.00942 d, not this clock or a supported integer harmonic.

## Measurement and scope

Gaia source 2912271058309989376; selection orbit 40.0079326059106 d; Gaia G 10.957841. The raw QLP SAP analysis inspected 3 hash-verified FITS sectors and 12 retained dip windows, including actual quality and time coverage. Local trapezoid centers, event depths, sectors, and source hashes are in [lead-numeric.json](lead-numeric.json); representative profiles are in lead-raw-*.png. These retained detector windows were not taken as verdicts.
Source packet SHA-256: 4195def30df27604ea2e2816c1895c90b6c6343edc8c8b270cae67f6ce3e48c9. Bulk-result SHA-256: 62754f5287208bee750eedbd69a6278c54409565102159e94e61e6455baad0b6.

Selected same-kind fit: P = 10.518241 d; T0 = 1474.786339 BTJD; conditional formal period error = 1.7648e-05 d.
Cycle numbers, chosen eclipse kind and residuals: [lead-timing.json](../lead-timing.json).

The helper independently extracted the strongest event from TESSCut with a positive-flux target aperture and checked the difference pixels; see [helper audit](../helper-audit.md), [numeric pixel audit](../helper-pixel-audit.json), and helper-difference.png. It is a second reduction of the same TESS photons.

## Limits and next check

The event source is localized to the target region, but an unresolved companion inside the TESS aperture remains possible. A separate short-period EB or hierarchical system is by-catch; no Gaia-orbit eclipse is established. Conditional timing error omits selection and pipeline systematics.

Deblend the target and nearby unresolved light, obtain a second pipeline time series, and determine whether the short-period EB belongs to the Gaia SB2 system.

Catalogue status uses the [shared queue-wide audit](../../shared-catalogues/REPORT.md). Its four unavailable VizieR gates are unknown, not negative matches.
