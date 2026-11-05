# TIC 25320385: PROBABLE

Review R714, sealed exact-ten queue position 2. **Bounded physical review COMPLETE; physical verdict PROBABLE.** Completion is separate from verdict. Root acceptance remains pending. Gaia DR3 source 5437589645131664896.

Repeated V-shaped eclipse-like dips are secure, but the raw clock is a harmonic of the screening clock: dips occur near every 3.5906 d and a 7.18125 d branch also fits. Opposite dips have comparable depths with changing widths; primary/secondary identity and a unique orbital factor of two are unestablished. The crowded difference image is offset 0.83 pixel and dilution changes strongly with aperture. The event source cannot be uniquely assigned to this Gaia star, and it cannot be declared a definite Gaia by-catch. Generic orbital ephemeris fields are blank.

## Raw events, clocks and actual coverage

Every source receipt and FITS header identity was checked against the sealed snapshot (`batch-shared/source-verification.json`); 6 available QLP files are retained. Quality-zero finite positive raw SAP flux is fitted with free-center local linear-baseline trapezoids. Predicted screening centers only locate windows; the following are measured centers. Fits are bounded representative checks (at most six sectors for ordinary timing), not an all-event analysis. Cadences with nonzero quality are excluded from precision timing but retained in coverage counts; incomplete or flagged windows are never clean nulls.

Conditional/dip-branch fit only: 7.181248958 d, formal/allowed fit error 0.000018700 d, branch epoch BTJD1525.04797146. These values are not a uniquely established orbital ephemeris. Generic orbital period, error and epoch are blank. The epoch names the selected eclipse kind, not an assumed deeper primary. Median central loss in the selected timing/hypothesis sample is 7.86 ppt. Depths are diluted and baseline dependent; model amplitude and realized central loss are distinct where retained. Full records and exclusions are in `measurements.json`; raw panels in `raw-events.png` (for449, use `refined-raw-events.png`).

| Sector | cycle/branch | mid BTJD | timing usable | formal center error d | central loss ppt |
| --- | --- | --- | --- | --- | --- |
| 8 | -2 | 1525.06517 | True | 0.015973 | 6.54 |
| 8 | 0 | 1539.39587 | True | 0.008472 | 7.53 |
| 9 | 1 | 1546.59694 | True | 0.007910 | 8.87 |
| 9 | 2 | 1553.76193 | True | 0.007177 | 7.75 |
| 9 | 3 | 1560.94927 | True | 0.007564 | 7.61 |
| 62 | 205 | 3011.57369 | True | 0.005603 | 8.22 |
| 89 | 304 | 3722.50781 | True | 0.005712 | 8.88 |
| 89 | 305 | 3729.69309 | True | 0.006391 | 8.24 |
| 89 | 306 | 3736.86137 | True | 0.003989 | 9.45 |
| 89 | 307 | 3744.05954 | True | 0.004569 | 8.70 |


Actual SAP coverage and tested integer alternatives are in `batch-shared/coverage-alias.json`. A sensitive null requires≥75% central expected cadence coverage,≥3 clean core samples,≥4 clean sideband samples on each side, local scatter below one-quarter observed depth, and core deficit+5 scatter/sqrt(N)<0.4 observed depth; a putative null must additionally have deficit below max(0.1 depth,3 scatter/sqrt(N)), so a shallower opposite eclipse is retained as a depth-inconsistent event rather than a zero-signal null. These are descriptive sensitivity cuts, not calibrated detection probabilities. Each alias records exact predicted centers, clean/flagged samples and local deficits. The table's timing rejection uses actual usable centers (for349, original conditional gapped-center estimates are included only as a branch test); half/third periods can pass timing algebra even when coverage or eclipse kinds reject them. Shorter/double branches are interpreted by eclipse kind rather than counted as independent same-kind events. This is a bounded local N±2 alias test, not an exhaustive uniqueness proof.

| Hypothesis | period d | rejected by usable timings | candidate sensitive nulls |
| --- | --- | --- | --- |
| selected | 7.1812490 | False | 0 |
| half | 3.5906245 | False | 2 |
| third | 2.3937497 | False | 3 |
| double | 14.3624979 | True | 0 |
| integer_307 | 7.2279947 | True | 2 |
| integer_308 | 7.2045272 | True | 1 |
| integer_310 | 7.1580464 | True | 2 |
| integer_311 | 7.1350301 | True | 1 |


Third-occasion evidence for436 and449 is in `batch-shared/third-occasion-aliases.json`, overriding the two-center ambiguity where appropriate. For253 the sector99 aperture shows suppression of both dip sequences; its candidate nulls cannot alone reject an orbital branch. `opposite-eclipse-kind.json/png` retains the actual opposite-dip measurements, with comparable depths and unresolved kind identity. For449 opposite-half-phase deficits are shallower eclipses/modulation, not clean zero-flux nulls or same-kind centers; their lower depth can reject equal-kind P/2 but is not counted as another recurrence of the selected deep eclipse.

## Source and alternative extraction

Separately extracted background-subtracted TESScut sector8 1x1/3x3/5x5 aperture losses are 1.83/1.27/3.42 ppt. This is an alternative reduction of the same TESS photons, not an independent astrophysical occasion. Positive difference-centroid offset is 0.831 pixel, descriptive rather than a calibrated localization probability. The helper inspected actual difference images relative to the target and every Gaia neighbor passing the optimistic capability test. The60-arcsec Gaia cone has 32 entries; at the minimum tested aperture loss 1.27 ppt, 14 neighbor(s) could in principle supply the deficit with intrinsic loss≤100%. Gaia G-band and unit/full throughput are proxies; the intrinsic fraction is not directly compared to a blended pixel deficit. Sources outside60 arcsec, uncatalogued sources, extreme colors and unresolved multiplicity are limitations. 

| Gaia DR3 neighbor | sep arcsec | G | required intrinsic eclipse % |
| --- | --- | --- | --- |
| 5437589537751695872 | 56.68 | 17.74 | 49.6 |
| 5437589572111487360 | 17.70 | 17.97 | 61.4 |
| 5437589576410550272 | 44.07 | 18.36 | 87.9 |
| 5437589576410552192 | 22.88 | 16.58 | 17.1 |
| 5437589606471197440 | 47.42 | 17.94 | 59.8 |
| 5437589606471212032 | 31.15 | 18.40 | 91.1 |
| 5437589610770291456 | 37.10 | 14.77 | 3.3 |
| 5437589610770291584 | 21.49 | 16.04 | 10.4 |
| 5437589610770294400 | 55.94 | 15.50 | 6.4 |
| 5437589640830964608 | 20.64 | 17.06 | 26.5 |
| 5437589645127546112 | 5.53 | 17.83 | 53.7 |
| 5437589645130025856 | 40.03 | 16.80 | 20.9 |
| 5437590366684536704 | 56.70 | 15.80 | 8.4 |
| 5437590401044271232 | 46.55 | 13.10 | 0.8 |


Raw cutout/QLP source receipts, cone response, extraction scripts and image panels are in `batch-shared/helper-pixels/`; helper numeric and final audits are referenced by `batch-shared/LEAD-AUDIT.md`.

## Gaia orbit, catalogue and final assessment

Source-specific Gaia SB1 P=21.41573842±0.02931931 d, e=0.3852, omega=88.200 deg. Primary-velocity mass function=0.00362 solar masses. Closest edge-on conjunctionA minus measured/branch epoch comparison: observed offset-1.54272 d (-0.07204 phase), Gaia source-specific full-covariance linear error1.25852 d. Both conjunctions, covariance order, eigenvalue and source identity are in `batch-shared/gaia-geometry.json`. Approximate edge-on geometry and linear errors are descriptive, not calibrated association probabilities. For conditional/dip branches this comparison does not establish orbital ownership. The depths and durations permit stellar eclipses without requiring fitted component masses or radii.

Catalogue status: **UNKNOWN_INCOMPLETE_SCOPED_CHECKS**. Scoped catalogue recovery remains incomplete, including service failures. No positive match has been identified in the successful checks so far; unknown is not a non-match and no uncatalogued/new-system claim is made. Receipts: `batch-shared/../unmatched512/catalogue-recovery-selected12/`, especially `live-vsx/`. Catalogue service failures remain unknown and physical status is separate.

**Limitations:** Repeated V-shaped eclipse-like dips are secure, but the raw clock is a harmonic of the screening clock: dips occur near every 3.5906 d and a 7.18125 d branch also fits. Opposite dips have comparable depths with changing widths; primary/secondary identity and a unique orbital factor of two are unestablished. The crowded difference image is offset 0.83 pixel and dilution changes strongly with aperture. The event source cannot be uniquely assigned to this Gaia star, and it cannot be declared a definite Gaia by-catch. Generic orbital ephemeris fields are blank. TESScut is a separate reduction of the same photons. Gaia G-band flux ratios and full throughput are optimistic neighbor capability proxies, not TESS PRF likelihoods. No exhaustive all-event fitting, precision stellar characterization, or Monte Carlo was performed.

**Next deciding check:** Obtain resolved eclipse photometry and distinguish primary/secondary clocks before assigning a unique Gaia-target orbital period.
