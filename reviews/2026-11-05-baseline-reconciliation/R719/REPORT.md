# TIC 349527829: PLAUSIBLE

Review R719, sealed exact-ten queue position 7. **Bounded physical review COMPLETE; physical verdict PLAUSIBLE.** Completion is separate from verdict. Root acceptance remains pending. Gaia DR3 source 3683392166690829056.

Two similar raw eclipse occasions are separated by about1230 d. Several nearby integer-cycle aliases have no sensitive actual coverage null and remain untested. The sector91 ingress is gapped, making its reconstructed center additionally model dependent. Difference imaging and a separate extraction support the target, but do not supply a third observing occasion. The conditional period and formal fit error in saved numeric artifacts are hypotheses, not an established ephemeris; generic orbital fields are blank.

## Raw events, clocks and actual coverage

Every source receipt and FITS header identity was checked against the sealed snapshot (`batch-shared/source-verification.json`); 2 available QLP files are retained. Quality-zero finite positive raw SAP flux is fitted with free-center local linear-baseline trapezoids. Predicted screening centers only locate windows; the following are measured centers. Fits are bounded representative checks (at most six sectors for ordinary timing), not an all-event analysis. Cadences with nonzero quality are excluded from precision timing but retained in coverage counts; incomplete or flagged windows are never clean nulls.

Conditional/dip-branch fit only: 22.780464245 d, formal/allowed fit error 0.000068455 d, branch epoch BTJD2559.36752961. These values are not a uniquely established orbital ephemeris. Generic orbital period, error and epoch are blank. The epoch names the selected eclipse kind, not an assumed deeper primary. Median central loss in the selected timing/hypothesis sample is 60.32 ppt. Depths are diluted and baseline dependent; model amplitude and realized central loss are distinct where retained. Full records and exclusions are in `measurements.json`; raw panels in `raw-events.png` (for449, use `refined-raw-events.png`).

| Sector | cycle/branch | mid BTJD | timing usable | formal center error d | central loss ppt |
| --- | --- | --- | --- | --- | --- |
| 46 | 0 | 2559.36753 | True | 0.000480 | 60.06 |
| 91 | 54 | 3789.51260 | False | 0.001267 | 60.57 |


Actual SAP coverage and tested integer alternatives are in `batch-shared/coverage-alias.json`. A sensitive null requires≥75% central expected cadence coverage,≥3 clean core samples,≥4 clean sideband samples on each side, local scatter below one-quarter observed depth, and core deficit+5 scatter/sqrt(N)<0.4 observed depth; a putative null must additionally have deficit below max(0.1 depth,3 scatter/sqrt(N)), so a shallower opposite eclipse is retained as a depth-inconsistent event rather than a zero-signal null. These are descriptive sensitivity cuts, not calibrated detection probabilities. Each alias records exact predicted centers, clean/flagged samples and local deficits. The table's timing rejection uses actual usable centers (for349, original conditional gapped-center estimates are included only as a branch test); half/third periods can pass timing algebra even when coverage or eclipse kinds reject them. Shorter/double branches are interpreted by eclipse kind rather than counted as independent same-kind events. This is a bounded local N±2 alias test, not an exhaustive uniqueness proof.

| Hypothesis | period d | rejected by usable timings | candidate sensitive nulls |
| --- | --- | --- | --- |
| selected | 22.7804642 | False | 0 |
| half | 11.3902321 | False | 2 |
| third | 7.5934881 | False | 2 |
| double | 45.5609285 | False | 0 |
| integer_52 | 23.6566359 | False | 0 |
| integer_53 | 23.2102843 | False | 0 |
| integer_55 | 22.3662740 | False | 0 |
| integer_56 | 21.9668762 | False | 0 |


Third-occasion evidence for436 and449 is in `batch-shared/third-occasion-aliases.json`, overriding the two-center ambiguity where appropriate. For253 the sector99 aperture shows suppression of both dip sequences; its candidate nulls cannot alone reject an orbital branch. `opposite-eclipse-kind.json/png` retains the actual opposite-dip measurements, with comparable depths and unresolved kind identity. For449 opposite-half-phase deficits are shallower eclipses/modulation, not clean zero-flux nulls or same-kind centers; their lower depth can reject equal-kind P/2 but is not counted as another recurrence of the selected deep eclipse.

## Source and alternative extraction

Separately extracted background-subtracted TESScut sector46 1x1/3x3/5x5 aperture losses are 58.08/58.08/56.67 ppt. This is an alternative reduction of the same TESS photons, not an independent astrophysical occasion. Positive difference-centroid offset is 0.122 pixel, descriptive rather than a calibrated localization probability. The helper inspected actual difference images relative to the target and every Gaia neighbor passing the optimistic capability test. The60-arcsec Gaia cone has 3 entries; at the minimum tested aperture loss 56.67 ppt, 0 neighbor(s) could in principle supply the deficit with intrinsic loss≤100%. Gaia G-band and unit/full throughput are proxies; the intrinsic fraction is not directly compared to a blended pixel deficit. Sources outside60 arcsec, uncatalogued sources, extreme colors and unresolved multiplicity are limitations. 

No neighbor in the bounded Gaia cone passes that optimistic capability test.

Raw cutout/QLP source receipts, cone response, extraction scripts and image panels are in `batch-shared/helper-pixels/`; helper numeric and final audits are referenced by `batch-shared/LEAD-AUDIT.md`.

## Gaia orbit, catalogue and final assessment

Source-specific Gaia SB1 P=22.79993757±0.02113204 d, e=0.2032, omega=346.498 deg. Primary-velocity mass function=0.01704 solar masses. Closest edge-on conjunctionA minus measured/branch epoch comparison: observed offset-1.69673 d (-0.07442 phase), Gaia source-specific full-covariance linear error1.84943 d. Both conjunctions, covariance order, eigenvalue and source identity are in `batch-shared/gaia-geometry.json`. Approximate edge-on geometry and linear errors are descriptive, not calibrated association probabilities. For conditional/dip branches this comparison does not establish orbital ownership. The depths and durations permit stellar eclipses without requiring fitted component masses or radii.

Catalogue status: **UNKNOWN_INCOMPLETE_SCOPED_CHECKS**. Scoped catalogue recovery remains incomplete, including service failures. No positive match has been identified in the successful checks so far; unknown is not a non-match and no uncatalogued/new-system claim is made. Receipts: `batch-shared/../unmatched512/catalogue-recovery-selected12/`, especially `live-vsx/`. Catalogue service failures remain unknown and physical status is separate.

**Limitations:** Two similar raw eclipse occasions are separated by about1230 d. Several nearby integer-cycle aliases have no sensitive actual coverage null and remain untested. The sector91 ingress is gapped, making its reconstructed center additionally model dependent. Difference imaging and a separate extraction support the target, but do not supply a third observing occasion. The conditional period and formal fit error in saved numeric artifacts are hypotheses, not an established ephemeris; generic orbital fields are blank. TESScut is a separate reduction of the same photons. Gaia G-band flux ratios and full throughput are optimistic neighbor capability proxies, not TESS PRF likelihoods. No exhaustive all-event fitting, precision stellar characterization, or Monte Carlo was performed.

**Next deciding check:** Acquire a third clean eclipse occasion that discriminates integer-cycle aliases.
