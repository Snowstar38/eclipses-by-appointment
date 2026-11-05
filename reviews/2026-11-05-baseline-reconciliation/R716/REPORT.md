# TIC 260797021: PROBABLE

Review R716, sealed exact-ten queue position 4. **Bounded physical review COMPLETE; physical verdict PROBABLE.** Completion is separate from verdict. Root acceptance remains pending. Gaia DR3 source 6387602188702034944.

Deep flat-bottomed eclipses repeat with consecutive anchors. A target-centered difference image and separate extraction support an on-target eclipsing source, but Gaia has P=20.3196973 d versus measured about20.29960 d. Both period and conjunction disagree by about five formal Gaia standard deviations. Published-orbit errors or different motion remain possible; this is not a geometry-consistent confirmation of the selecting Gaia companion. The ingress-gapped sector67 fit is excluded from adopted timing.

## Raw events, clocks and actual coverage

Every source receipt and FITS header identity was checked against the sealed snapshot (`batch-shared/source-verification.json`); 10 available QLP files are retained. Quality-zero finite positive raw SAP flux is fitted with free-center local linear-baseline trapezoids. Predicted screening centers only locate windows; the following are measured centers. Fits are bounded representative checks (at most six sectors for ordinary timing), not an all-event analysis. Cadences with nonzero quality are excluded from precision timing but retained in coverage counts; incomplete or flagged windows are never clean nulls.

Adopted selected-kind period 20.299601238 d; reference epoch BTJD1326.75223751 at cycle0. Quoted fit period error 0.000027842 d and epoch error 0.00368427 d have this meaning: Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. The epoch names the selected eclipse kind, not an assumed deeper primary. Median central loss in the selected timing/hypothesis sample is 88.81 ppt. Depths are diluted and baseline dependent; model amplitude and realized central loss are distinct where retained. Full records and exclusions are in `measurements.json`; raw panels in `raw-events.png` (for449, use `refined-raw-events.png`).

| Sector | cycle/branch | mid BTJD | timing usable | formal center error d | central loss ppt |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 1326.76088 | True | 0.000411 | 94.44 |
| 27 | 35 | 2037.23779 | True | 0.000283 | 100.71 |
| 27 | 36 | 2057.53719 | True | 0.000343 | 100.70 |
| 67 | 89 | 3133.41919 | False | 0.000860 | 100.94 |
| 94 | 125 | 3864.20187 | True | 0.000260 | 87.02 |
| 102 | 138 | 4128.09933 | True | 0.000270 | 84.26 |
| 102 | 139 | 4148.39717 | True | 0.000228 | 88.81 |
| 104 | 141 | 4188.99408 | True | 0.000303 | 80.77 |


Actual SAP coverage and tested integer alternatives are in `batch-shared/coverage-alias.json`. A sensitive null requires≥75% central expected cadence coverage,≥3 clean core samples,≥4 clean sideband samples on each side, local scatter below one-quarter observed depth, and core deficit+5 scatter/sqrt(N)<0.4 observed depth; a putative null must additionally have deficit below max(0.1 depth,3 scatter/sqrt(N)), so a shallower opposite eclipse is retained as a depth-inconsistent event rather than a zero-signal null. These are descriptive sensitivity cuts, not calibrated detection probabilities. Each alias records exact predicted centers, clean/flagged samples and local deficits. The table's timing rejection uses actual usable centers (for349, original conditional gapped-center estimates are included only as a branch test); half/third periods can pass timing algebra even when coverage or eclipse kinds reject them. Shorter/double branches are interpreted by eclipse kind rather than counted as independent same-kind events. This is a bounded local N±2 alias test, not an exhaustive uniqueness proof.

| Hypothesis | period d | rejected by usable timings | candidate sensitive nulls |
| --- | --- | --- | --- |
| selected | 20.2996012 | False | 0 |
| half | 10.1498006 | False | 7 |
| third | 6.7665337 | False | 20 |
| double | 40.5992025 | True | 0 |
| integer_139 | 20.5916057 | True | 8 |
| integer_140 | 20.4445228 | True | 7 |
| integer_142 | 20.1565718 | True | 7 |
| integer_143 | 20.0156168 | True | 8 |


Third-occasion evidence for436 and449 is in `batch-shared/third-occasion-aliases.json`, overriding the two-center ambiguity where appropriate. For253 the sector99 aperture shows suppression of both dip sequences; its candidate nulls cannot alone reject an orbital branch. `opposite-eclipse-kind.json/png` retains the actual opposite-dip measurements, with comparable depths and unresolved kind identity. For449 opposite-half-phase deficits are shallower eclipses/modulation, not clean zero-flux nulls or same-kind centers; their lower depth can reject equal-kind P/2 but is not counted as another recurrence of the selected deep eclipse.

## Source and alternative extraction

Separately extracted background-subtracted TESScut sector1 1x1/3x3/5x5 aperture losses are 95.16/92.95/90.96 ppt. This is an alternative reduction of the same TESS photons, not an independent astrophysical occasion. Positive difference-centroid offset is 0.164 pixel, descriptive rather than a calibrated localization probability. The helper inspected actual difference images relative to the target and every Gaia neighbor passing the optimistic capability test. The60-arcsec Gaia cone has 15 entries; at the minimum tested aperture loss 84.99 ppt, 0 neighbor(s) could in principle supply the deficit with intrinsic loss≤100%. Gaia G-band and unit/full throughput are proxies; the intrinsic fraction is not directly compared to a blended pixel deficit. Sources outside60 arcsec, uncatalogued sources, extreme colors and unresolved multiplicity are limitations. 

No neighbor in the bounded Gaia cone passes that optimistic capability test.

Raw cutout/QLP source receipts, cone response, extraction scripts and image panels are in `batch-shared/helper-pixels/`; helper numeric and final audits are referenced by `batch-shared/LEAD-AUDIT.md`.

## Gaia orbit, catalogue and final assessment

Source-specific Gaia SB1 P=20.31969730±0.00376799 d, e=0.3633, omega=103.276 deg. Primary-velocity mass function=0.25340 solar masses. Closest edge-on conjunctionA minus measured/branch epoch comparison: observed offset-1.00887 d (-0.04965 phase), Gaia source-specific full-covariance linear error0.19936 d. Both conjunctions, covariance order, eigenvalue and source identity are in `batch-shared/gaia-geometry.json`. Approximate edge-on geometry and linear errors are descriptive, not calibrated association probabilities. For conditional/dip branches this comparison does not establish orbital ownership. The depths and durations permit stellar eclipses without requiring fitted component masses or radii.

Catalogue status: **UNKNOWN_INCOMPLETE_SCOPED_CHECKS**. Scoped catalogue recovery remains incomplete, including service failures. No positive match has been identified in the successful checks so far; unknown is not a non-match and no uncatalogued/new-system claim is made. Receipts: `batch-shared/../unmatched512/catalogue-recovery-selected12/`, especially `live-vsx/`. Catalogue service failures remain unknown and physical status is separate.

**Limitations:** Deep flat-bottomed eclipses repeat with consecutive anchors. A target-centered difference image and separate extraction support an on-target eclipsing source, but Gaia has P=20.3196973 d versus measured about20.29960 d. Both period and conjunction disagree by about five formal Gaia standard deviations. Published-orbit errors or different motion remain possible; this is not a geometry-consistent confirmation of the selecting Gaia companion. The ingress-gapped sector67 fit is excluded from adopted timing. TESScut is a separate reduction of the same photons. Gaia G-band flux ratios and full throughput are optimistic neighbor capability proxies, not TESS PRF likelihoods. No exhaustive all-event fitting, precision stellar characterization, or Monte Carlo was performed.

**Next deciding check:** Compare the eclipse clock with a new radial-velocity orbit and investigate Gaia orbit/systematic errors.
