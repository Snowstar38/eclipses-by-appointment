# TIC 24668377 — appointment full review (lead draft)

**Physical verdict: confirmed.** Deep A and B eclipses recur across three separated sectors. Depth varies with aperture/sector; four A timings span 85 cycles and B timings are consistent. The exact Gaia/TIC entry in IJspeert et al. (2024) means this is a known EB recovery for the scoped novelty gate.

The frozen queue identifies Gaia DR3 2902439805151595008 at (84.5730053110888, -31.095543165783827) deg, G=11.521738, SB1 period 21.555987 d. The measured **A eclipse** ephemeris is BTJD 2212.55062 + E × 21.5523446 d, with conditional statistical period error 0.0000400 d. The epoch names the observed A event; deeper primary designation is supported by the observed shallower opposite eclipse. The period assumes the listed integer-cycle assignment. Timing covariance includes half-cadence floors and residual-scatter inflation, but not common pipeline offsets, model systematics, or all alias uncertainty.

Raw QLP quality-zero SAP eclipse fits ([event montage](event-montage.png)):

- s33 A: BTJD 2212.54946, 229.4 ppt, 6.1 h, ±5.0 min conditional timing floor
- s87 A: BTJD 3678.11073, 205.9 ppt, 6.0 h, ±1.7 min conditional timing floor
- s98 A: BTJD 4001.39497, 180.7 ppt, 6.1 h, ±1.7 min conditional timing floor
- s98 A: BTJD 4044.49963, 179.2 ppt, 6.1 h, ±1.7 min conditional timing floor
- s33 B: BTJD 2221.13594, 51.6 ppt, 9.6 h, ±5.0 min conditional timing floor
- s87 B: BTJD 3665.15476, 60.0 ppt, 9.7 h, ±8.7 min conditional timing floor
- s87 B: BTJD 3686.69503, 49.5 ppt, 9.6 h, ±1.7 min conditional timing floor

Additional products were fetched adaptively after the 256-target screening was frozen; they do not alter its denominator or screening status:

- No older product needed to establish recurrence.

The representative realized QLP central depth is 193.3 ppt, the median of usable A event fits. Each depth is the realized trapezoid loss, `amplitude × min(1,width/(2×ingress))`; aperture dilution changes across sectors. [Numeric measurements](measurements.json) preserve separate model amplitudes and event errors. 

Independent TESS processing of the **same photons** in sector 33 (TESS-SPOC) reproduces the dip: SAP_FLUX 216.8 ppt, PDCSAP_FLUX 220.2 ppt, compared with QLP 229.4 ppt ([alternative reduction](alternative-event.png)). These are reduction cross-checks, not independent observing epochs. TESS-SPOC QUALITY=0 cadences were used.

TESScut sector 98 shows a deficit 1.9 arcsec from the target coordinate and 1.5 arcsec from the local blended-light centroid ([pixel difference](pixels/pixel-difference.png)). The cone contains 8 Gaia DR3 sources within 60 arcsec; 0 meet a two-star G-band depth feasibility test. The difference image and each capable neighbor must be read together. A neighbor's required *intrinsic* eclipse depth cannot be compared directly with diluted pixel fractional loss. This is one FFI sector and uncalibrated centroid precision.

Source-specific full Gaia NSS covariance was independently sampled by Terra in [helper-gaia-covariance.json](batch-shared/helper-gaia-covariance.json); all original usable event centers lie within 2.38 reported central-68%-halfwidth units of conjunction medians. Correlated predictions across cycles are not independent significance tests. [Helper audit](batch-shared/helper-audit.md) checks the numeric and pixel evidence. The Gaia SB1 orbit supplies an appointment and physical plausibility, not automatic proof that the target is the eclipsing source.

Catalogue checks: vsx: unavailable (0 rows); asassn: success (0 rows); prsa2022: success (0 rows); ijspeert2024: success (1 row); kostov2025_table3: success (0 rows); kostov2025_table4: success (0 rows). VSX query was unavailable; the exact IJspeert EB catalogue row already makes the object a known recovery. [Shared receipts](shared-catalogues/catalogue-results.json) and [source hashes](batch-shared/SOURCE-SNAPSHOT.json) preserve provenance. Physical verdict and novelty gate are separate; root will decide count eligibility.

**Limitations / next check:** VSX query was unavailable; the exact IJspeert EB catalogue row already makes the object a known recovery. Complete root catalogue gate and independent final audit.
