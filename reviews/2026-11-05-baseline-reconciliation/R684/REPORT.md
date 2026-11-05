# TIC 384744604 — appointment full review (lead draft)

**Physical verdict: confirmed.** Three A events in sectors 13, 39 and 101 have distinct cycle spacings 13 and 32, rejecting adjacent cycle aliases; two shallow B events support the same orbital morphology. Difference image is target-centered. The older s13 observation is 30-min cadence and its timing error is floored at half cadence.

The frozen queue identifies Gaia DR3 5776280282072990208 at (258.8388229297673, -79.33929690219503) deg, G=11.523727, SB1 period 54.171364 d. The measured **A eclipse** ephemeris is BTJD 1680.65075 + E × 54.1813283 d, with conditional statistical period error 0.0001041 d. The epoch names the observed A event; deeper primary designation is supported by the observed shallower opposite eclipse. The period assumes the listed integer-cycle assignment. Timing covariance includes half-cadence floors and residual-scatter inflation, but not common pipeline offsets, model systematics, or all alias uncertainty.

Raw QLP quality-zero SAP eclipse fits ([event montage](event-montage.png)):

- s39 A: BTJD 2385.00802, 41.2 ppt, 10.8 h, ±5.0 min conditional timing floor
- s101 A: BTJD 4118.81053, 33.9 ppt, 10.7 h, ±1.7 min conditional timing floor
- s39 B: BTJD 2371.24668, 2.9 ppt, 8.8 h, ±8.6 min conditional timing floor
- s101 B: BTJD 4105.05336, 2.9 ppt, 8.5 h, ±10.6 min conditional timing floor

Additional products were fetched adaptively after the 256-target screening was frozen; they do not alter its denominator or screening status:

- adaptive older s13 A: BTJD 1680.65074, 38.6 ppt, 10.8 h, ±15.0 min conditional timing floor

The representative realized QLP central depth is 38.6 ppt, the median of usable A event fits. Each depth is the realized trapezoid loss, `amplitude × min(1,width/(2×ingress))`; aperture dilution changes across sectors. [Numeric measurements](measurements.json) preserve separate model amplitudes and event errors. 

Independent TESS processing of the **same photons** in sector 39 (TESS-SPOC) reproduces the dip: SAP_FLUX 38.4 ppt, PDCSAP_FLUX 39.8 ppt, compared with QLP 41.2 ppt ([alternative reduction](alternative-event.png)). These are reduction cross-checks, not independent observing epochs. TESS-SPOC QUALITY=0 cadences were used.

TESScut sector 101 shows a deficit 3.3 arcsec from the target coordinate and 0.7 arcsec from the local blended-light centroid ([pixel difference](pixels/pixel-difference.png)). The cone contains 23 Gaia DR3 sources within 60 arcsec; 0 meet a two-star G-band depth feasibility test. The difference image and each capable neighbor must be read together. A neighbor's required *intrinsic* eclipse depth cannot be compared directly with diluted pixel fractional loss. This is one FFI sector and uncalibrated centroid precision.

Source-specific full Gaia NSS covariance was independently sampled by Terra in [helper-gaia-covariance.json](batch-shared/helper-gaia-covariance.json); all original usable event centers lie within 2.38 reported central-68%-halfwidth units of conjunction medians. Correlated predictions across cycles are not independent significance tests. [Helper audit](batch-shared/helper-audit.md) checks the numeric and pixel evidence. The Gaia SB1 orbit supplies an appointment and physical plausibility, not automatic proof that the target is the eclipsing source.

Catalogue checks: vsx: unavailable (0 rows); asassn: unavailable (0 rows); prsa2022: unavailable (0 rows); ijspeert2024: unavailable (0 rows); kostov2025_table3: unavailable (0 rows); kostov2025_table4: unavailable (0 rows). Several catalogue services were unavailable in the initial pass; absence of rows is not a nonmatch. Root must complete novelty reconciliation. [Shared receipts](shared-catalogues/catalogue-results.json) and [source hashes](batch-shared/SOURCE-SNAPSHOT.json) preserve provenance. Physical verdict and novelty gate are separate; root will decide count eligibility.

**Limitations / next check:** Several catalogue services were unavailable in the initial pass; absence of rows is not a nonmatch. Root must complete novelty reconciliation. Complete root catalogue gate and independent final audit.
