# TIC 109560492 — appointment full review (lead draft)

**Physical verdict: probable.** Three B eclipses in sectors 7, 61 and 88 span 47 and 23 cycles, rejecting adjacent cycle aliases. Two A-like dips also appear, but the sector-34 A event has a truncated left baseline and is excluded from timing. The s88 pixel deficit peaks near the Gaia target; a G≈9.9 source only ~22 arcsec away dominates the blended light. TARS reproduces the event at 18 ppt versus QLP 79 ppt, showing strong aperture dependence. Source attribution remains likely but not resolved to a calibrated level.

The frozen queue identifies Gaia DR3 5613374508997583232 at (113.37215593306139, -25.89363992284914) deg, G=11.526461, SB1 period 31.606334 d. The measured **B eclipse** ephemeris is BTJD 1495.03216 + E × 31.6201394 d, with conditional statistical period error 0.0000661 d. The epoch names the observed B event; deeper primary designation is uncertain because the opposite eclipse is not securely established. The period assumes the listed integer-cycle assignment. Timing covariance includes half-cadence floors and residual-scatter inflation, but not common pipeline offsets, model systematics, or all alias uncertainty.

Raw QLP quality-zero SAP eclipse fits ([event montage](event-montage.png)):

- s88 A: BTJD 3715.83963, 73.5 ppt, 5.0 h, ±1.7 min conditional timing floor
- s61 B: BTJD 2981.17868, 84.4 ppt, 5.1 h, ±1.7 min conditional timing floor
- s88 B: BTJD 3708.44193, 78.9 ppt, 4.8 h, ±1.7 min conditional timing floor

Additional products were fetched adaptively after the 256-target screening was frozen; they do not alter its denominator or screening status:

- adaptive older s7 B: BTJD 1495.03293, 77.5 ppt, 4.8 h, ±15.0 min conditional timing floor

The representative realized QLP central depth is 78.9 ppt, the median of usable B event fits. Each depth is the realized trapezoid loss, `amplitude × min(1,width/(2×ingress))`; aperture dilution changes across sectors. [Numeric measurements](measurements.json) preserve separate model amplitudes and event errors. 

Independent TESS processing of the **same photons** in sector 88 (TARS) reproduces the dip: FLUX 18.0 ppt, compared with QLP 78.9 ppt ([alternative reduction](alternative-event.png)). These are reduction cross-checks, not independent observing epochs. TARS has no QUALITY field in the s88 file; its event is visually continuous but its quality provenance is limited.

TESScut sector 88 shows a deficit 1.9 arcsec from the target coordinate and 16.2 arcsec from the local blended-light centroid ([pixel difference](pixels/pixel-difference.png)). The cone contains 93 Gaia DR3 sources within 60 arcsec; 2 meet a two-star G-band depth feasibility test. The difference image and each capable neighbor must be read together. A neighbor's required *intrinsic* eclipse depth cannot be compared directly with diluted pixel fractional loss. This is one FFI sector and uncalibrated centroid precision.

Source-specific full Gaia NSS covariance was independently sampled by Terra in [helper-gaia-covariance.json](batch-shared/helper-gaia-covariance.json); all original usable event centers lie within 2.38 reported central-68%-halfwidth units of conjunction medians. Correlated predictions across cycles are not independent significance tests. [Helper audit](batch-shared/helper-audit.md) checks the numeric and pixel evidence. The Gaia SB1 orbit supplies an appointment and physical plausibility, not automatic proof that the target is the eclipsing source.

Catalogue checks: vsx: unavailable (0 rows); asassn: unavailable (0 rows); prsa2022: success (0 rows); ijspeert2024: unavailable (0 rows); kostov2025_table3: unavailable (0 rows); kostov2025_table4: unavailable (0 rows). Initial catalogue services were partly unavailable. The nearby brighter star and its aliases require explicit novelty/attribution checks. [Shared receipts](shared-catalogues/catalogue-results.json) and [source hashes](batch-shared/SOURCE-SNAPSHOT.json) preserve provenance. Physical verdict and novelty gate are separate; root will decide count eligibility.

**Limitations / next check:** Initial catalogue services were partly unavailable. The nearby brighter star and its aliases require explicit novelty/attribution checks. Quantify crowded-source attribution using another sector or calibrated PSF basis if a definitive target assignment is needed.
