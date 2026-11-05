# T086 / TIC 398402989: CONFIRMED

Queue stratum: repeat_sector_dip. Bounded physical review: complete. Catalogue novelty: KNOWN.

## Deciding evidence

Four clean same-kind raw eclipses in sectors 13, 39, 67 and 93 fit 58.731513 d at cycles 0, 12, 25 and 37, with max timing residual below 0.001 d; this agrees with Gaia 58.732564 +/- 0.007279 d. Actual P/2 alternative windows in s12 and s101 are well covered and flat. A second TESSCut extraction has a target-centered 59 ppt deficit with valid background. Gaia Thiele-Innes inversion gives inclination 90.47 deg and argument of periastron about 30.33 deg; the observed epoch is 0.064 d from predicted conjunction with 0.177-d source-specific linear full-covariance uncertainty (0.36 sigma). Public Chopard v1.2.0 independently records this exact Gaia source and TIC as an eclipser in four of seven conjunction windows, with QLP and TESS-SPOC agreement and an orbit-consistency flag.

## Measurement and scope

Gaia source 6360777231720947328; selection orbit 58.73256395072352 d; Gaia G 9.971982. The raw QLP SAP analysis inspected 8 hash-verified FITS sectors and 6 retained dip windows, including actual quality and time coverage. Local trapezoid centers, event depths, sectors, and source hashes are in [lead-numeric.json](lead-numeric.json); representative profiles are in lead-raw-*.png. These retained detector windows were not taken as verdicts.
Source packet SHA-256: c0a14ff3e0919cc5f0d6be185c6282a0f71f72b4a51babc3ebe10dd8a4b065da. Bulk-result SHA-256: 0c06997064c4fb644cbac16ee86e0aff9216240a5e3eddfdb19d37970f560f78.

Selected same-kind fit: P = 58.731513 d; T0 = 1666.211178 BTJD; conditional formal period error = 0.0001051991 d.
Cycle numbers, chosen eclipse kind and residuals: [lead-timing.json](../lead-timing.json).

The helper independently extracted the strongest event from TESSCut with a positive-flux target aperture and checked the difference pixels; see [helper audit](../helper-audit.md), [numeric pixel audit](../helper-pixel-audit.json), and helper-difference.png. It is a second reduction of the same TESS photons.

Public exact-ID receipt: [shared Chopard overlap](../../shared-catalogues/chopard-overlaps.json), SHA-256 ac8794a178e9916df1bc8d742e57b1b1af097f20a2780f12904c862aa35bb3d1, Gaia DR3 6360777231720947328, vetting/dossier.csv. This establishes KNOWN even though four other catalogue gates failed.

Actual half-period opposite-kind coverage: [lead-half-alias.json](../lead-half-alias.json).

Gaia orientation and point conjunction from [Thiele-Innes inversion](../lead-thiele.json); C/H cross-checks the angular branch. Source-specific full NSS covariance propagation: [lead-thiele-covariance.json](../lead-thiele-covariance.json).

## Limits and next check

The source is previously identified, so it is a known recovery and cannot enter a new-system count. Gaia conjunction covariance is linearly propagated from the full 15-parameter fit; nonlinear tails and orbital model systematics are not calibrated. The public dossier quotes 2.034% depth, different from the roughly 4.6-6% raw/custom-aperture depth here; the reduction or event-definition cause is untested. The fitted timing uncertainty is conditional.

Cite the public Chopard v1.2.0 dossier if discussing this known recovery; refine its ephemeris with a full independent reduction if needed.

Catalogue status uses the [shared queue-wide audit](../../shared-catalogues/REPORT.md). Its four unavailable VizieR gates are unknown, not negative matches.
