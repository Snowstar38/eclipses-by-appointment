# T087 / TIC 200743349: CONFIRMED

Queue stratum: repeat_sector_dip. Bounded physical review: complete. Catalogue novelty: UNKNOWN.

## Deciding evidence

Four same-kind raw eclipses at BTJD 2135.654, 2162.187, 3939.892 and 3966.425 occur at cycles 0, 1, 68 and 69, giving 26.532911 d with a maximum selected residual below 0.001 d. The adjacent pairs fix the cycle spacing; well-covered P/2 windows in s31 and s97 are flat. Gaia has 26.536860 +/- 0.003424 d, consistent at about 1.2 sigma. The TESSCut aperture repeats a target-region eclipse deficit with valid positive target flux and no nominal capable Gaia neighbor. Gaia AstroSpectroSB1 Thiele-Innes A/B/F/G recover inclination 91.89 deg and argument of periastron 39.76 deg, checked against C/H. The observed epoch is 0.193 d before the edge-on conjunction prediction, with 0.197-d source-specific linear full-covariance uncertainty (0.98 sigma).

## Measurement and scope

Gaia source 4749907416157959424; selection orbit 26.536860248348678 d; Gaia G 10.481409. The raw QLP SAP analysis inspected 5 hash-verified FITS sectors and 5 retained dip windows, including actual quality and time coverage. Local trapezoid centers, event depths, sectors, and source hashes are in [lead-numeric.json](lead-numeric.json); representative profiles are in lead-raw-*.png. These retained detector windows were not taken as verdicts.
Source packet SHA-256: 346f23fdacd2406bb9a56f79ccdf22a469f55172c50c110e909fe737fd8ea616. Bulk-result SHA-256: 27efc24e9a557fde72bf99081f36d31df3fe5292ac28c8566f6fd18b75838f34.

Selected same-kind fit: P = 26.532911 d; T0 = 2135.653621 BTJD; conditional formal period error = 3.804779e-05 d.
Cycle numbers, chosen eclipse kind and residuals: [lead-timing.json](../lead-timing.json).

The helper independently extracted the strongest event from TESSCut with a positive-flux target aperture and checked the difference pixels; see [helper audit](../helper-audit.md), [numeric pixel audit](../helper-pixel-audit.json), and helper-difference.png. It is a second reduction of the same TESS photons.

Actual half-period opposite-kind coverage: [lead-half-alias.json](../lead-half-alias.json).

Gaia orientation and point conjunction from [Thiele-Innes inversion](../lead-thiele.json); C/H cross-checks the angular branch. Source-specific full NSS covariance propagation: [lead-thiele-covariance.json](../lead-thiele-covariance.json).

## Limits and next check

The Gaia conjunction covariance is linearly propagated from the full 15-parameter fit; nonlinear tails and orbital model systematics are not calibrated. The custom aperture is the same TESS photons, not another observing occasion. A formal timing error is conditional.

Remeasure the eclipses in another time-series pipeline and complete the unavailable catalogue gates before any novelty claim.

Catalogue status uses the [shared queue-wide audit](../../shared-catalogues/REPORT.md). Its four unavailable VizieR gates are unknown, not negative matches.
