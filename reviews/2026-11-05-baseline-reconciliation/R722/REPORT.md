# TIC 198358825: CONFIRMED

Review R722, sealed exact-ten queue position 10. **Bounded physical review COMPLETE; physical verdict CONFIRMED.** Completion is separate from verdict. Root acceptance remains pending. Gaia DR3 source 1432279887075354112.

Five usable representative centers over81 cycles, with numerous intervening raw coverage tests, establish a stable same-kind clock. The gapped sector57 event is detected but excluded from center fitting. The deficit is on target and no capable Gaia neighbor appears in the bounded cone. The prior KELT/VSX EA clock agrees closely, making this a known recovery.

## Raw events, clocks and actual coverage

Every source receipt and FITS header identity was checked against the sealed snapshot (`batch-shared/source-verification.json`); 32 available QLP files are retained. Quality-zero finite positive raw SAP flux is fitted with free-center local linear-baseline trapezoids. Predicted screening centers only locate windows; the following are measured centers. Fits are bounded representative checks (at most six sectors for ordinary timing), not an all-event analysis. Cadences with nonzero quality are excluded from precision timing but retained in coverage counts; incomplete or flagged windows are never clean nulls.

Adopted selected-kind period 23.514352220 d; reference epoch BTJD1753.55656902 at cycle0. Quoted fit period error 0.000065874 d and epoch error 0.00492020 d have this meaning: Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. The epoch names the selected eclipse kind, not an assumed deeper primary. Median central loss in the selected timing/hypothesis sample is 46.23 ppt. Depths are diluted and baseline dependent; model amplitude and realized central loss are distinct where retained. Full records and exclusions are in `measurements.json`; raw panels in `raw-events.png` (for449, use `refined-raw-events.png`).

| Sector | cycle/branch | mid BTJD | timing usable | formal center error d | central loss ppt |
| --- | --- | --- | --- | --- | --- |
| 16 | 0 | 1753.55771 | True | 0.000369 | 47.46 |
| 24 | 9 | 1965.18637 | True | 0.000375 | 46.23 |
| 50 | 39 | 2670.61762 | True | 0.000384 | 46.76 |
| 57 | 47 | 2858.72166 | False | 49683.109561 | 47.50 |
| 78 | 72 | 3446.58906 | True | 0.000641 | 45.40 |
| 86 | 81 | 3658.21980 | True | 0.000442 | 46.00 |


Actual SAP coverage and tested integer alternatives are in `batch-shared/coverage-alias.json`. A sensitive null requires≥75% central expected cadence coverage,≥3 clean core samples,≥4 clean sideband samples on each side, local scatter below one-quarter observed depth, and core deficit+5 scatter/sqrt(N)<0.4 observed depth; a putative null must additionally have deficit below max(0.1 depth,3 scatter/sqrt(N)), so a shallower opposite eclipse is retained as a depth-inconsistent event rather than a zero-signal null. These are descriptive sensitivity cuts, not calibrated detection probabilities. Each alias records exact predicted centers, clean/flagged samples and local deficits. The table's timing rejection uses actual usable centers (for349, original conditional gapped-center estimates are included only as a branch test); half/third periods can pass timing algebra even when coverage or eclipse kinds reject them. Shorter/double branches are interpreted by eclipse kind rather than counted as independent same-kind events. This is a bounded local N±2 alias test, not an exhaustive uniqueness proof.

| Hypothesis | period d | rejected by usable timings | candidate sensitive nulls |
| --- | --- | --- | --- |
| selected | 23.5143522 | False | 0 |
| half | 11.7571761 | False | 31 |
| third | 7.8381174 | False | 54 |
| double | 47.0287044 | True | 0 |
| integer_79 | 24.1096467 | True | 24 |
| integer_80 | 23.8082762 | True | 27 |
| integer_82 | 23.2275865 | True | 25 |
| integer_83 | 22.9477361 | True | 27 |


Third-occasion evidence for436 and449 is in `batch-shared/third-occasion-aliases.json`, overriding the two-center ambiguity where appropriate. For253 the sector99 aperture shows suppression of both dip sequences; its candidate nulls cannot alone reject an orbital branch. `opposite-eclipse-kind.json/png` retains the actual opposite-dip measurements, with comparable depths and unresolved kind identity. For449 opposite-half-phase deficits are shallower eclipses/modulation, not clean zero-flux nulls or same-kind centers; their lower depth can reject equal-kind P/2 but is not counted as another recurrence of the selected deep eclipse.

## Source and alternative extraction

Separately extracted background-subtracted TESScut sector16 1x1/3x3/5x5 aperture losses are 45.04/45.47/44.56 ppt. This is an alternative reduction of the same TESS photons, not an independent astrophysical occasion. Positive difference-centroid offset is 0.028 pixel, descriptive rather than a calibrated localization probability. The helper inspected actual difference images relative to the target and every Gaia neighbor passing the optimistic capability test. The60-arcsec Gaia cone has 8 entries; at the minimum tested aperture loss 44.56 ppt, 0 neighbor(s) could in principle supply the deficit with intrinsic loss≤100%. Gaia G-band and unit/full throughput are proxies; the intrinsic fraction is not directly compared to a blended pixel deficit. Sources outside60 arcsec, uncatalogued sources, extreme colors and unresolved multiplicity are limitations. 

No neighbor in the bounded Gaia cone passes that optimistic capability test.

Raw cutout/QLP source receipts, cone response, extraction scripts and image panels are in `batch-shared/helper-pixels/`; helper numeric and final audits are referenced by `batch-shared/LEAD-AUDIT.md`.

## Gaia orbit, catalogue and final assessment

Source-specific Gaia SB1 P=23.51895455±0.01172207 d, e=0.3163, omega=189.600 deg. Primary-velocity mass function=0.01702 solar masses. Closest edge-on conjunctionA minus measured/branch epoch comparison: observed offset-0.54043 d (-0.02298 phase), Gaia source-specific full-covariance linear error0.81844 d. Both conjunctions, covariance order, eigenvalue and source identity are in `batch-shared/gaia-geometry.json`. Approximate edge-on geometry and linear errors are descriptive, not calibrated association probabilities. For conditional/dip branches this comparison does not establish orbital ownership. The depths and durations permit stellar eclipses without requiring fitted component masses or radii.

Catalogue status: **KNOWN_PRIOR_EB_POSITIONALLY_ASSOCIATED**. Live VSX lists KELT KC22C07252, EA, OID2213605, category “Not checked”, at1.274 arcsec; P23.51526 d, epochJD2458001.158. Its close position and period agree with the isolated Gaia target. This is a known recovery. Receipts: `batch-shared/../unmatched512/catalogue-recovery-selected12/`, especially `live-vsx/`. Catalogue service failures remain unknown and physical status is separate.

**Limitations:** Five usable representative centers over81 cycles, with numerous intervening raw coverage tests, establish a stable same-kind clock. The gapped sector57 event is detected but excluded from center fitting. The deficit is on target and no capable Gaia neighbor appears in the bounded cone. The prior KELT/VSX EA clock agrees closely, making this a known recovery. TESScut is a separate reduction of the same photons. Gaia G-band flux ratios and full throughput are optimistic neighbor capability proxies, not TESS PRF likelihoods. No exhaustive all-event fitting, precision stellar characterization, or Monte Carlo was performed.

**Next deciding check:** Acquire a future clean eclipse to refine the named-kind ephemeris.
