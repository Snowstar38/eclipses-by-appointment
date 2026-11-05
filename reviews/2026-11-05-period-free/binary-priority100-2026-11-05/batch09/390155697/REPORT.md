# T082 / TIC 390155697: PROBABLE

Queue stratum: repeat_sector_dip. Bounded physical review: complete. Catalogue novelty: UNKNOWN.

## Deciding evidence

Nine same-kind raw eclipses from sectors 10, 37, 38, 64, 100 and 101 fit 16.2039887 d (cycles 0, 1, 46-48, 91, 155-157; max residual 0.0016 d). Deep opposite-kind events are interleaved. The target-region TESSCut deficit is real. Three times the eclipse period is 48.61197 d, 0.25948 d below the Gaia SB2 period 48.87145 +/- 0.00975 d, so a simple third-harmonic identity fails.

## Measurement and scope

Gaia source 6072185425508943744; selection orbit 48.871449941734575 d; Gaia G 10.867524. The raw QLP SAP analysis inspected 8 hash-verified FITS sectors and 17 retained dip windows, including actual quality and time coverage. Local trapezoid centers, event depths, sectors, and source hashes are in [lead-numeric.json](lead-numeric.json); representative profiles are in lead-raw-*.png. These retained detector windows were not taken as verdicts.
Source packet SHA-256: 27e6ee86841cc0bb58b3fa5e0f2b0fe2e6d493cf402c7a20678e89b08c4c195d. Bulk-result SHA-256: 05f3b158f845a3c6a056a61fba53c80377d94604f0c4f2fdfa4496d747782cc6.

Selected same-kind fit: P = 16.203989 d; T0 = 1577.439874 BTJD; conditional formal period error = 1.464431e-05 d.
Cycle numbers, chosen eclipse kind and residuals: [lead-timing.json](../lead-timing.json).

The helper independently extracted the strongest event from TESSCut with a positive-flux target aperture and checked the difference pixels; see [helper audit](../helper-audit.md), [numeric pixel audit](../helper-pixel-audit.json), and helper-difference.png. It is a second reduction of the same TESS photons.

## Limits and next check

The local pixel check does not exclude an unresolved source or establish a physical link to the Gaia SB2. The Gaia-period association fails even though the short-period eclipse train is real. Conditional timing error omits model and reduction systematics.

Fit separate eclipse kinds in an independent pipeline and obtain source-resolved photometry or spectroscopy to identify the 16.204-day binary.

Catalogue status uses the [shared queue-wide audit](../../shared-catalogues/REPORT.md). Its four unavailable VizieR gates are unknown, not negative matches.
