# TIC 117930511: PROBABLE

Review R713, sealed exact-ten queue position 1. **Bounded physical review COMPLETE; physical verdict PROBABLE.** Completion is separate from verdict. Root acceptance remains pending. Gaia DR3 source 2855177989323312768.

Three same-kind raw events include consecutive sector-57 eclipses. The difference image favors the target; the one marginal G-band capable neighbor lies 30.77 arcsec away and would require a roughly 94% intrinsic eclipse under optimistic throughput. The broad TESS PSF overlaps that neighbor at roughly1.5 pixels, so target-like centroid and morphology do not decisively exclude it. Attribution remains unresolved. The measured eclipse clock differs from the prior VSX clock; this does not make the star a new system.

## Raw events, clocks and actual coverage

Every source receipt and FITS header identity was checked against the sealed snapshot (`batch-shared/source-verification.json`); 2 available QLP files are retained. Quality-zero finite positive raw SAP flux is fitted with free-center local linear-baseline trapezoids. Predicted screening centers only locate windows; the following are measured centers. Fits are bounded representative checks (at most six sectors for ordinary timing), not an all-event analysis. Cadences with nonzero quality are excluded from precision timing but retained in coverage counts; incomplete or flagged windows are never clean nulls.

Adopted selected-kind period 20.174001587 d; reference epoch BTJD2855.24690474 at cycle0. Quoted fit period error 0.000038825 d and epoch error 0.00082968 d have this meaning: Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. The epoch names the selected eclipse kind, not an assumed deeper primary. Median central loss in the selected timing/hypothesis sample is 42.35 ppt. Depths are diluted and baseline dependent; model amplitude and realized central loss are distinct where retained. Full records and exclusions are in `measurements.json`; raw panels in `raw-events.png` (for449, use `refined-raw-events.png`).

| Sector | cycle/branch | mid BTJD | timing usable | formal center error d | central loss ppt |
| --- | --- | --- | --- | --- | --- |
| 57 | 0 | 2855.24661 | True | 0.000308 | 42.95 |
| 57 | 1 | 2875.42121 | True | 0.000313 | 42.35 |
| 84 | 37 | 3601.68496 | True | 0.000308 | 41.72 |


Actual SAP coverage and tested integer alternatives are in `batch-shared/coverage-alias.json`. A sensitive null requires≥75% central expected cadence coverage,≥3 clean core samples,≥4 clean sideband samples on each side, local scatter below one-quarter observed depth, and core deficit+5 scatter/sqrt(N)<0.4 observed depth; a putative null must additionally have deficit below max(0.1 depth,3 scatter/sqrt(N)), so a shallower opposite eclipse is retained as a depth-inconsistent event rather than a zero-signal null. These are descriptive sensitivity cuts, not calibrated detection probabilities. Each alias records exact predicted centers, clean/flagged samples and local deficits. The table's timing rejection uses actual usable centers (for349, original conditional gapped-center estimates are included only as a branch test); half/third periods can pass timing algebra even when coverage or eclipse kinds reject them. Shorter/double branches are interpreted by eclipse kind rather than counted as independent same-kind events. This is a bounded local N±2 alias test, not an exhaustive uniqueness proof.

| Hypothesis | period d | rejected by usable timings | candidate sensitive nulls |
| --- | --- | --- | --- |
| selected | 20.1740016 | False | 0 |
| half | 10.0870008 | False | 1 |
| third | 6.7246672 | False | 5 |
| double | 40.3480032 | True | 0 |
| integer_35 | 21.3268100 | True | 1 |
| integer_36 | 20.7343986 | True | 1 |
| integer_38 | 19.6431145 | True | 1 |
| integer_39 | 19.1394449 | True | 1 |


Third-occasion evidence for436 and449 is in `batch-shared/third-occasion-aliases.json`, overriding the two-center ambiguity where appropriate. For253 the sector99 aperture shows suppression of both dip sequences; its candidate nulls cannot alone reject an orbital branch. `opposite-eclipse-kind.json/png` retains the actual opposite-dip measurements, with comparable depths and unresolved kind identity. For449 opposite-half-phase deficits are shallower eclipses/modulation, not clean zero-flux nulls or same-kind centers; their lower depth can reject equal-kind P/2 but is not counted as another recurrence of the selected deep eclipse.

## Source and alternative extraction

Separately extracted background-subtracted TESScut sector57 1x1/3x3/5x5 aperture losses are 40.87/40.11/38.01 ppt. This is an alternative reduction of the same TESS photons, not an independent astrophysical occasion. Positive difference-centroid offset is 0.142 pixel, descriptive rather than a calibrated localization probability. The helper inspected actual difference images relative to the target and every Gaia neighbor passing the optimistic capability test. The60-arcsec Gaia cone has 8 entries; at the minimum tested aperture loss 38.01 ppt, 1 neighbor(s) could in principle supply the deficit with intrinsic loss≤100%. Gaia G-band and unit/full throughput are proxies; the intrinsic fraction is not directly compared to a blended pixel deficit. Sources outside60 arcsec, uncatalogued sources, extreme colors and unresolved multiplicity are limitations. 

| Gaia DR3 neighbor | sep arcsec | G | required intrinsic eclipse % |
| --- | --- | --- | --- |
| 2855178092401865088 | 30.77 | 14.68 | 94.1 |


Raw cutout/QLP source receipts, cone response, extraction scripts and image panels are in `batch-shared/helper-pixels/`; helper numeric and final audits are referenced by `batch-shared/LEAD-AUDIT.md`.

## Gaia orbit, catalogue and final assessment

Source-specific Gaia SB1 P=20.18594425±0.00695459 d, e=0.2925, omega=359.275 deg. Primary-velocity mass function=0.03192 solar masses. Closest edge-on conjunctionA minus measured/branch epoch comparison: observed offset-1.54846 d (-0.07671 phase), Gaia source-specific full-covariance linear error0.84436 d. Both conjunctions, covariance order, eigenvalue and source identity are in `batch-shared/gaia-geometry.json`. Approximate edge-on geometry and linear errors are descriptive, not calibrated association probabilities. For conditional/dip branches this comparison does not establish orbital ownership. The depths and durations permit stellar eclipses without requiring fitted component masses or radii.

Catalogue status: **KNOWN_PRIOR_EB_POSITIONALLY_ASSOCIATED**. Live VSX lists KELT KC13C22465, EA, OID2213304, category “Not checked”, at0.296 arcsec; published P9.7999 d, epochJD2455850.47, differs from our20.174 d clock without an established alias relationship. The target is isolated until28.28 arcsec in Gaia, strongly supporting positional association. The prior report of eclipses is preserved; no novelty claim is made. Receipts: `batch-shared/../unmatched512/catalogue-recovery-selected12/`, especially `live-vsx/`. Catalogue service failures remain unknown and physical status is separate.

**Limitations:** Three same-kind raw events include consecutive sector-57 eclipses. The difference image favors the target; the one marginal G-band capable neighbor lies 30.77 arcsec away and would require a roughly 94% intrinsic eclipse under optimistic throughput. The broad TESS PSF overlaps that neighbor at roughly1.5 pixels, so target-like centroid and morphology do not decisively exclude it. Attribution remains unresolved. The measured eclipse clock differs from the prior VSX clock; this does not make the star a new system. TESScut is a separate reduction of the same photons. Gaia G-band flux ratios and full throughput are optimistic neighbor capability proxies, not TESS PRF likelihoods. No exhaustive all-event fitting, precision stellar characterization, or Monte Carlo was performed.

**Next deciding check:** Obtain higher-resolution eclipse photometry to resolve capable neighbors.
