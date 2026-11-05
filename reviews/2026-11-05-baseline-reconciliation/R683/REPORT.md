# TIC 331650047 — appointment full review (lead draft)

**Physical verdict: confirmed.** Four same-kind narrow eclipses, including adaptive older sector 59, recur with a 25.9936-d period. Three covered odd half-period windows contain no comparable eclipse, excluding the 12.9968-d equal-depth train. Difference image favors the target over a 51-arcsec capable neighbor. Gaia conjunction offset is marginal (~2.4 full-covariance 68%-halfwidth units), so association with the spectroscopic orbit is less secure than eclipse reality.

The frozen queue identifies Gaia DR3 550563615634343424 at (70.04115437969662, 76.71988728890283) deg, G=11.539937, SB1 period 25.974814 d. The measured **A eclipse** ephemeris is BTJD 2934.13030 + E × 25.9936140 d, with conditional statistical period error 0.0000565 d. The epoch names the observed A event; deeper primary designation is uncertain because the opposite eclipse is not securely established. The period assumes the listed integer-cycle assignment. Timing covariance includes half-cadence floors and residual-scatter inflation, but not common pipeline offsets, model systematics, or all alias uncertainty.

Raw QLP quality-zero SAP eclipse fits ([event montage](event-montage.png)):

- s73 A: BTJD 3298.04121, 149.0 ppt, 3.7 h, ±1.7 min conditional timing floor
- s79 A: BTJD 3454.00237, 148.7 ppt, 3.7 h, ±1.7 min conditional timing floor
- s86 A: BTJD 3661.95148, 143.2 ppt, 3.7 h, ±1.7 min conditional timing floor

Additional products were fetched adaptively after the 256-target screening was frozen; they do not alter its denominator or screening status:

- adaptive older s59 A: BTJD 2934.13020, 144.7 ppt, 3.7 h, ±1.7 min conditional timing floor

The representative realized QLP central depth is 146.7 ppt, the median of usable A event fits. Each depth is the realized trapezoid loss, `amplitude × min(1,width/(2×ingress))`; aperture dilution changes across sectors. [Numeric measurements](measurements.json) preserve separate model amplitudes and event errors. [Half-period null windows](half-alias-windows.json) test the 331650047 alias.

Independent TESS processing of the **same photons** in sector 79 (TESS-SPOC) reproduces the dip: SAP_FLUX 142.0 ppt, PDCSAP_FLUX 148.3 ppt, compared with QLP 148.7 ppt ([alternative reduction](alternative-event.png)). These are reduction cross-checks, not independent observing epochs. TESS-SPOC QUALITY=0 cadences were used.

TESScut sector 79 shows a deficit 1.7 arcsec from the target coordinate and 5.8 arcsec from the local blended-light centroid ([pixel difference](pixels/pixel-difference.png)). The cone contains 14 Gaia DR3 sources within 60 arcsec; 1 meet a two-star G-band depth feasibility test. The difference image and each capable neighbor must be read together. A neighbor's required *intrinsic* eclipse depth cannot be compared directly with diluted pixel fractional loss. This is one FFI sector and uncalibrated centroid precision.

Source-specific full Gaia NSS covariance was independently sampled by Terra in [helper-gaia-covariance.json](batch-shared/helper-gaia-covariance.json); all original usable event centers lie within 2.38 reported central-68%-halfwidth units of conjunction medians. Correlated predictions across cycles are not independent significance tests. [Helper audit](batch-shared/helper-audit.md) checks the numeric and pixel evidence. The Gaia SB1 orbit supplies an appointment and physical plausibility, not automatic proof that the target is the eclipsing source.

Catalogue checks: vsx: success (1 row); asassn: success (0 rows); prsa2022: success (0 rows); ijspeert2024: success (0 rows); kostov2025_table3: success (0 rows); kostov2025_table4: unavailable (0 rows). VSX lists exact Gaia source as ROT, not an EB; this does not negate the observed eclipse. One Kostov table query remains unavailable; root must reconcile novelty. [Shared receipts](shared-catalogues/catalogue-results.json) and [source hashes](batch-shared/SOURCE-SNAPSHOT.json) preserve provenance. Physical verdict and novelty gate are separate; root will decide count eligibility.

**Limitations / next check:** VSX lists exact Gaia source as ROT, not an EB; this does not negate the observed eclipse. One Kostov table query remains unavailable; root must reconcile novelty. Complete root catalogue gate and independent final audit.
