# TIC 122557124: CONFIRMED

Review R715, sealed exact-ten queue position 3. **Bounded physical review COMPLETE; physical verdict CONFIRMED.** Completion is separate from verdict. Root acceptance remains pending. Gaia DR3 source 5063790085781507456.

Three full raw eclipses across 110 cycles establish a consistent clock; the other integer counts tested fail actual timing or coverage. Deep, flat-bottomed stellar eclipses survive the separate extraction, with a target-centered deficit and no capable Gaia neighbor in the bounded cone. Gaia conjunction is compatible.

## Raw events, clocks and actual coverage

Every source receipt and FITS header identity was checked against the sealed snapshot (`batch-shared/source-verification.json`); 4 available QLP files are retained. Quality-zero finite positive raw SAP flux is fitted with free-center local linear-baseline trapezoids. Predicted screening centers only locate windows; the following are measured centers. Fits are bounded representative checks (at most six sectors for ordinary timing), not an all-event analysis. Cadences with nonzero quality are excluded from precision timing but retained in coverage counts; incomplete or flagged windows are never clean nulls.

Adopted selected-kind period 23.198562380 d; reference epoch BTJD1401.73125349 at cycle0. Quoted fit period error 0.000042224 d and epoch error 0.00440133 d have this meaning: Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. The epoch names the selected eclipse kind, not an assumed deeper primary. Median central loss in the selected timing/hypothesis sample is 196.80 ppt. Depths are diluted and baseline dependent; model amplitude and realized central loss are distinct where retained. Full records and exclusions are in `measurements.json`; raw panels in `raw-events.png` (for449, use `refined-raw-events.png`).

| Sector | cycle/branch | mid BTJD | timing usable | formal center error d | central loss ppt |
| --- | --- | --- | --- | --- | --- |
| 3 | 0 | 1401.73102 | True | 0.000112 | 196.80 |
| 30 | 31 | 2120.88672 | True | 0.000095 | 213.68 |
| 97 | 110 | 3953.57311 | True | 0.000073 | 193.55 |


Actual SAP coverage and tested integer alternatives are in `batch-shared/coverage-alias.json`. A sensitive null requires≥75% central expected cadence coverage,≥3 clean core samples,≥4 clean sideband samples on each side, local scatter below one-quarter observed depth, and core deficit+5 scatter/sqrt(N)<0.4 observed depth; a putative null must additionally have deficit below max(0.1 depth,3 scatter/sqrt(N)), so a shallower opposite eclipse is retained as a depth-inconsistent event rather than a zero-signal null. These are descriptive sensitivity cuts, not calibrated detection probabilities. Each alias records exact predicted centers, clean/flagged samples and local deficits. The table's timing rejection uses actual usable centers (for349, original conditional gapped-center estimates are included only as a branch test); half/third periods can pass timing algebra even when coverage or eclipse kinds reject them. Shorter/double branches are interpreted by eclipse kind rather than counted as independent same-kind events. This is a bounded local N±2 alias test, not an exhaustive uniqueness proof.

| Hypothesis | period d | rejected by usable timings | candidate sensitive nulls |
| --- | --- | --- | --- |
| selected | 23.1985624 | False | 0 |
| half | 11.5992812 | False | 5 |
| third | 7.7328541 | False | 7 |
| double | 46.3971248 | True | 0 |
| integer_108 | 23.6281675 | True | 2 |
| integer_109 | 23.4113953 | True | 0 |
| integer_111 | 22.9895684 | True | 1 |
| integer_112 | 22.7843044 | True | 1 |


Third-occasion evidence for436 and449 is in `batch-shared/third-occasion-aliases.json`, overriding the two-center ambiguity where appropriate. For253 the sector99 aperture shows suppression of both dip sequences; its candidate nulls cannot alone reject an orbital branch. `opposite-eclipse-kind.json/png` retains the actual opposite-dip measurements, with comparable depths and unresolved kind identity. For449 opposite-half-phase deficits are shallower eclipses/modulation, not clean zero-flux nulls or same-kind centers; their lower depth can reject equal-kind P/2 but is not counted as another recurrence of the selected deep eclipse.

## Source and alternative extraction

Separately extracted background-subtracted TESScut sector3 1x1/3x3/5x5 aperture losses are 196.91/189.03/186.64 ppt. This is an alternative reduction of the same TESS photons, not an independent astrophysical occasion. Positive difference-centroid offset is 0.149 pixel, descriptive rather than a calibrated localization probability. The helper inspected actual difference images relative to the target and every Gaia neighbor passing the optimistic capability test. The60-arcsec Gaia cone has 6 entries; at the minimum tested aperture loss 178.10 ppt, 0 neighbor(s) could in principle supply the deficit with intrinsic loss≤100%. Gaia G-band and unit/full throughput are proxies; the intrinsic fraction is not directly compared to a blended pixel deficit. Sources outside60 arcsec, uncatalogued sources, extreme colors and unresolved multiplicity are limitations. 

No neighbor in the bounded Gaia cone passes that optimistic capability test.

Raw cutout/QLP source receipts, cone response, extraction scripts and image panels are in `batch-shared/helper-pixels/`; helper numeric and final audits are referenced by `batch-shared/LEAD-AUDIT.md`.

## Gaia orbit, catalogue and final assessment

Source-specific Gaia SB1 P=23.20028537±0.00334034 d, e=0.2487, omega=321.612 deg. Primary-velocity mass function=0.06701 solar masses. Closest edge-on conjunctionA minus measured/branch epoch comparison: observed offset-0.16020 d (-0.00691 phase), Gaia source-specific full-covariance linear error0.18389 d. Both conjunctions, covariance order, eigenvalue and source identity are in `batch-shared/gaia-geometry.json`. Approximate edge-on geometry and linear errors are descriptive, not calibrated association probabilities. For conditional/dip branches this comparison does not establish orbital ownership. The depths and durations permit stellar eclipses without requiring fitted component masses or radii.

Catalogue status: **UNKNOWN_INCOMPLETE_SCOPED_CHECKS**. Scoped catalogue recovery remains incomplete, including service failures. No positive match has been identified in the successful checks so far; unknown is not a non-match and no uncatalogued/new-system claim is made. Receipts: `batch-shared/../unmatched512/catalogue-recovery-selected12/`, especially `live-vsx/`. Catalogue service failures remain unknown and physical status is separate.

**Limitations:** Three full raw eclipses across 110 cycles establish a consistent clock; the other integer counts tested fail actual timing or coverage. Deep, flat-bottomed stellar eclipses survive the separate extraction, with a target-centered deficit and no capable Gaia neighbor in the bounded cone. Gaia conjunction is compatible. TESScut is a separate reduction of the same photons. Gaia G-band flux ratios and full throughput are optimistic neighbor capability proxies, not TESS PRF likelihoods. No exhaustive all-event fitting, precision stellar characterization, or Monte Carlo was performed.

**Next deciding check:** Acquire a future clean eclipse to refine the named-kind ephemeris.
