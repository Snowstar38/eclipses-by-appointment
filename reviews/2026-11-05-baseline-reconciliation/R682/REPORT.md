# TIC 150465032 — appointment full review (lead draft)

**Physical verdict: confirmed.** Three A and three B events recur across sectors 34, 61 and 88. TESS-SPOC reproduces the eclipse. A crowded field contains two magnitude-feasible Gaia neighbors at 33 and 44 arcsec, but the independent pixel deficit is target-centered and displaced from both.

The frozen queue identifies Gaia DR3 5587540216297835136 at (117.6216673770398, -35.26009419203414) deg, G=11.525344, SB1 period 27.657083 d. The measured **A eclipse** ephemeris is BTJD 2246.97527 + E × 27.6528044 d, with conditional statistical period error 0.0000503 d. The epoch names the observed A event; deeper primary designation is supported by the observed shallower opposite eclipse. The period assumes the listed integer-cycle assignment. Timing covariance includes half-cadence floors and residual-scatter inflation, but not common pipeline offsets, model systematics, or all alias uncertainty.

Raw QLP quality-zero SAP eclipse fits ([event montage](event-montage.png)):

- s34 A: BTJD 2246.97457, 48.5 ppt, 10.4 h, ±5.0 min conditional timing floor
- s61 A: BTJD 2965.94834, 47.7 ppt, 10.3 h, ±1.7 min conditional timing floor
- s88 A: BTJD 3712.57383, 46.3 ppt, 10.3 h, ±1.7 min conditional timing floor
- s34 B: BTJD 2235.33028, 5.7 ppt, 13.1 h, ±5.8 min conditional timing floor
- s61 B: BTJD 2981.93649, 6.5 ppt, 14.0 h, ±7.8 min conditional timing floor
- s88 B: BTJD 3700.91998, 5.5 ppt, 13.1 h, ±6.2 min conditional timing floor

Additional products were fetched adaptively after the 256-target screening was frozen; they do not alter its denominator or screening status:

- No older product needed to establish recurrence.

The representative realized QLP central depth is 47.7 ppt, the median of usable A event fits. Each depth is the realized trapezoid loss, `amplitude × min(1,width/(2×ingress))`; aperture dilution changes across sectors. [Numeric measurements](measurements.json) preserve separate model amplitudes and event errors. 

Independent TESS processing of the **same photons** in sector 34 (TESS-SPOC) reproduces the dip: SAP_FLUX 40.7 ppt, PDCSAP_FLUX 46.5 ppt, compared with QLP 48.5 ppt ([alternative reduction](alternative-event.png)). These are reduction cross-checks, not independent observing epochs. TESS-SPOC QUALITY=0 cadences were used.

TESScut sector 61 shows a deficit 4.0 arcsec from the target coordinate and 1.4 arcsec from the local blended-light centroid ([pixel difference](pixels/pixel-difference.png)). The cone contains 57 Gaia DR3 sources within 60 arcsec; 2 meet a two-star G-band depth feasibility test. The difference image and each capable neighbor must be read together. A neighbor's required *intrinsic* eclipse depth cannot be compared directly with diluted pixel fractional loss. This is one FFI sector and uncalibrated centroid precision.

Source-specific full Gaia NSS covariance was independently sampled by Terra in [helper-gaia-covariance.json](batch-shared/helper-gaia-covariance.json); all original usable event centers lie within 2.38 reported central-68%-halfwidth units of conjunction medians. Correlated predictions across cycles are not independent significance tests. [Helper audit](batch-shared/helper-audit.md) checks the numeric and pixel evidence. The Gaia SB1 orbit supplies an appointment and physical plausibility, not automatic proof that the target is the eclipsing source.

Catalogue checks: vsx: success (0 rows); asassn: success (0 rows); prsa2022: success (0 rows); ijspeert2024: success (0 rows); kostov2025_table3: success (0 rows); kostov2025_table4: success (0 rows). Current six VizieR EB/variable catalogues returned successful empty exact-area results; root must complete final alias/novelty reconciliation. [Shared receipts](shared-catalogues/catalogue-results.json) and [source hashes](batch-shared/SOURCE-SNAPSHOT.json) preserve provenance. Physical verdict and novelty gate are separate; root will decide count eligibility.

**Limitations / next check:** Current six VizieR EB/variable catalogues returned successful empty exact-area results; root must complete final alias/novelty reconciliation. Complete root catalogue gate and independent final audit.
