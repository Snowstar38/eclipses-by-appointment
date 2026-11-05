# TIC 436013770: PROBABLE

Review R718, sealed exact-ten queue position 6. **Bounded physical review COMPLETE; physical verdict PROBABLE.** Completion is separate from verdict. Root acceptance remains pending. Gaia DR3 source 3339827626624683264.

Two full raw eclipse centers span75 cycles. A third partial raw eclipse in sector98 has actual deep samples nearBTJD4010.12719; it is not used as a precise fitted center. This third occasion rejects the tested nearby integer counts by3.35–10.23 d, while the selected branch agrees to0.039 d. The difference favors the target and 1x1/3x3 losses33.20/33.31 ppt are stable, but the broad TESS PSF overlaps the sole capable neighbor31.7 arcsec away at roughly1.5 pixels. The image does not decisively exclude that source; attribution remains unresolved even though Gaia geometry is compatible.

## Raw events, clocks and actual coverage

Every source receipt and FITS header identity was checked against the sealed snapshot (`batch-shared/source-verification.json`); 4 available QLP files are retained. Quality-zero finite positive raw SAP flux is fitted with free-center local linear-baseline trapezoids. Predicted screening centers only locate windows; the following are measured centers. Fits are bounded representative checks (at most six sectors for ordinary timing), not an all-event analysis. Cadences with nonzero quality are excluded from precision timing but retained in coverage counts; incomplete or flagged windows are never clean nulls.

Adopted selected-kind period 23.735188317 d; reference epoch BTJD1470.42345101 at cycle0. Quoted fit period error 0.000139741 d and epoch error 0.01041648 d have this meaning: Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. The epoch names the selected eclipse kind, not an assumed deeper primary. Median central loss in the selected timing/hypothesis sample is 35.14 ppt. Depths are diluted and baseline dependent; model amplitude and realized central loss are distinct where retained. Full records and exclusions are in `measurements.json`; raw panels in `raw-events.png` (for449, use `refined-raw-events.png`).

| Sector | cycle/branch | mid BTJD | timing usable | formal center error d | central loss ppt |
| --- | --- | --- | --- | --- | --- |
| 6 | 0 | 1470.42345 | True | 0.000882 | 33.83 |
| 71 | 75 | 3250.56257 | True | 0.000774 | 36.44 |
| 98 | 107 | 4010.13392 | False | 356259.565210 | 27.30 |


Actual SAP coverage and tested integer alternatives are in `batch-shared/coverage-alias.json`. A sensitive null requires≥75% central expected cadence coverage,≥3 clean core samples,≥4 clean sideband samples on each side, local scatter below one-quarter observed depth, and core deficit+5 scatter/sqrt(N)<0.4 observed depth; a putative null must additionally have deficit below max(0.1 depth,3 scatter/sqrt(N)), so a shallower opposite eclipse is retained as a depth-inconsistent event rather than a zero-signal null. These are descriptive sensitivity cuts, not calibrated detection probabilities. Each alias records exact predicted centers, clean/flagged samples and local deficits. The table's timing rejection uses actual usable centers (for349, original conditional gapped-center estimates are included only as a branch test); half/third periods can pass timing algebra even when coverage or eclipse kinds reject them. Shorter/double branches are interpreted by eclipse kind rather than counted as independent same-kind events. This is a bounded local N±2 alias test, not an exhaustive uniqueness proof.

| Hypothesis | period d | rejected by usable timings | candidate sensitive nulls |
| --- | --- | --- | --- |
| selected | 23.7351883 | False | 0 |
| half | 11.8675942 | False | 3 |
| third | 7.9117294 | False | 8 |
| double | 47.4703766 | True | 0 |
| integer_73 | 24.3854674 | False | 0 |
| integer_74 | 24.0559341 | False | 1 |
| integer_76 | 23.4228832 | False | 1 |
| integer_77 | 23.1186899 | False | 1 |


Third-occasion evidence for436 and449 is in `batch-shared/third-occasion-aliases.json`, overriding the two-center ambiguity where appropriate. For253 the sector99 aperture shows suppression of both dip sequences; its candidate nulls cannot alone reject an orbital branch. `opposite-eclipse-kind.json/png` retains the actual opposite-dip measurements, with comparable depths and unresolved kind identity. For449 opposite-half-phase deficits are shallower eclipses/modulation, not clean zero-flux nulls or same-kind centers; their lower depth can reject equal-kind P/2 but is not counted as another recurrence of the selected deep eclipse.

## Source and alternative extraction

Separately extracted background-subtracted TESScut sector6 1x1/3x3/5x5 aperture losses are 33.20/33.31/31.54 ppt. This is an alternative reduction of the same TESS photons, not an independent astrophysical occasion. Positive difference-centroid offset is 0.224 pixel, descriptive rather than a calibrated localization probability. The helper inspected actual difference images relative to the target and every Gaia neighbor passing the optimistic capability test. The60-arcsec Gaia cone has 22 entries; at the minimum tested aperture loss 31.54 ppt, 1 neighbor(s) could in principle supply the deficit with intrinsic loss≤100%. Gaia G-band and unit/full throughput are proxies; the intrinsic fraction is not directly compared to a blended pixel deficit. Sources outside60 arcsec, uncatalogued sources, extreme colors and unresolved multiplicity are limitations. 

| Gaia DR3 neighbor | sep arcsec | G | required intrinsic eclipse % |
| --- | --- | --- | --- |
| 3339827630922266880 | 31.70 | 14.16 | 31.0 |


Raw cutout/QLP source receipts, cone response, extraction scripts and image panels are in `batch-shared/helper-pixels/`; helper numeric and final audits are referenced by `batch-shared/LEAD-AUDIT.md`.

## Gaia orbit, catalogue and final assessment

Source-specific Gaia SB1 P=23.73905203±0.00969673 d, e=0.1616, omega=116.912 deg. Primary-velocity mass function=0.05316 solar masses. Closest edge-on conjunctionA minus measured/branch epoch comparison: observed offset-0.13821 d (-0.00582 phase), Gaia source-specific full-covariance linear error0.38046 d. Both conjunctions, covariance order, eigenvalue and source identity are in `batch-shared/gaia-geometry.json`. Approximate edge-on geometry and linear errors are descriptive, not calibrated association probabilities. For conditional/dip branches this comparison does not establish orbital ownership. The depths and durations permit stellar eclipses without requiring fitted component masses or radii.

Catalogue status: **UNKNOWN_INCOMPLETE_SCOPED_CHECKS**. Scoped catalogue recovery remains incomplete, including service failures. No positive match has been identified in the successful checks so far; unknown is not a non-match and no uncatalogued/new-system claim is made. Receipts: `batch-shared/../unmatched512/catalogue-recovery-selected12/`, especially `live-vsx/`. Catalogue service failures remain unknown and physical status is separate.

**Limitations:** Two full raw eclipse centers span75 cycles. A third partial raw eclipse in sector98 has actual deep samples nearBTJD4010.12719; it is not used as a precise fitted center. This third occasion rejects the tested nearby integer counts by3.35–10.23 d, while the selected branch agrees to0.039 d. The difference favors the target and 1x1/3x3 losses33.20/33.31 ppt are stable, but the broad TESS PSF overlaps the sole capable neighbor31.7 arcsec away at roughly1.5 pixels. The image does not decisively exclude that source; attribution remains unresolved even though Gaia geometry is compatible. TESScut is a separate reduction of the same photons. Gaia G-band flux ratios and full throughput are optimistic neighbor capability proxies, not TESS PRF likelihoods. No exhaustive all-event fitting, precision stellar characterization, or Monte Carlo was performed.

**Next deciding check:** Obtain higher-resolution eclipse photometry to resolve capable neighbors.
