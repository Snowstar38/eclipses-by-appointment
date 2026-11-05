# TIC 449012335: PROBABLE

Review R720, sealed exact-ten queue position 8. **Bounded physical review COMPLETE; physical verdict PROBABLE.** Completion is separate from verdict. Root acceptance remains pending. Gaia DR3 source 5849122141470273280.

The screening window clipped a roughly1.6 d flat-bottomed eclipse. New local raw fits require coverage at both contacts; sector11 and101 provide centers, while gapped fits are retained but excluded. A separate TESScut sector100 contact fit gives BTJD4085.18444, agreeing with the raw period prediction to0.00561 d and rejecting nearby integer counts. This reduction shares TESS photons but sector100 is a different observing occasion from sectors11/101. A neighbor10.43 arcsec away and others remain capable, so ownership is unresolved. Long-baseline orbital modulation and aperture drift require local baselines.

## Raw events, clocks and actual coverage

Every source receipt and FITS header identity was checked against the sealed snapshot (`batch-shared/source-verification.json`); 9 available QLP files are retained. Quality-zero finite positive raw SAP flux is fitted with free-center local linear-baseline trapezoids. Predicted screening centers only locate windows; the following are measured centers. Fits are bounded representative checks (at most six sectors for ordinary timing), not an all-event analysis. Cadences with nonzero quality are excluded from precision timing but retained in coverage counts; incomplete or flagged windows are never clean nulls.

Adopted selected-kind period 21.653350555 d; reference epoch BTJD1616.69686711 at cycle0. Quoted fit period error 0.000245950 d and epoch error 0.02000000 d have this meaning: Representative contact-covered long-eclipse trapezoids; individual max(formal covariance, 0.02 day conservative model allowance), scatter inflated if reduced chi square >1. The 0.02 day allowance is not a calibrated statistical error. The epoch names the selected eclipse kind, not an assumed deeper primary. Median central loss in the selected timing/hypothesis sample is 41.62 ppt. Depths are diluted and baseline dependent; model amplitude and realized central loss are distinct where retained. Full records and exclusions are in `measurements.json`; raw panels in `raw-events.png` (for449, use `refined-raw-events.png`).

| Sector | cycle/branch | mid BTJD | timing usable | formal center error d | central loss ppt |
| --- | --- | --- | --- | --- | --- |
| 11 | 0 | 1616.69687 | True | 0.002158 | 39.84 |
| 65 | 68 | 3089.13417 | False | 0.002064 | 43.94 |
| 101 | 115 | 4106.83218 | True | 0.002450 | 43.40 |


Actual SAP coverage and tested integer alternatives are in `batch-shared/coverage-alias.json`. A sensitive null requires≥75% central expected cadence coverage,≥3 clean core samples,≥4 clean sideband samples on each side, local scatter below one-quarter observed depth, and core deficit+5 scatter/sqrt(N)<0.4 observed depth; a putative null must additionally have deficit below max(0.1 depth,3 scatter/sqrt(N)), so a shallower opposite eclipse is retained as a depth-inconsistent event rather than a zero-signal null. These are descriptive sensitivity cuts, not calibrated detection probabilities. Each alias records exact predicted centers, clean/flagged samples and local deficits. The table's timing rejection uses actual usable centers (for349, original conditional gapped-center estimates are included only as a branch test); half/third periods can pass timing algebra even when coverage or eclipse kinds reject them. Shorter/double branches are interpreted by eclipse kind rather than counted as independent same-kind events. This is a bounded local N±2 alias test, not an exhaustive uniqueness proof.

| Hypothesis | period d | rejected by usable timings | candidate sensitive nulls |
| --- | --- | --- | --- |
| selected | 21.6533506 | False | 0 |
| half | 10.8266753 | False | 0 |
| third | 7.2177835 | False | 6 |
| double | 43.3067011 | True | 0 |
| integer_113 | 22.0365957 | False | 3 |
| integer_114 | 21.8432922 | False | 2 |
| integer_116 | 21.4666837 | False | 0 |
| integer_117 | 21.2832078 | False | 2 |


Third-occasion evidence for436 and449 is in `batch-shared/third-occasion-aliases.json`, overriding the two-center ambiguity where appropriate. For253 the sector99 aperture shows suppression of both dip sequences; its candidate nulls cannot alone reject an orbital branch. `opposite-eclipse-kind.json/png` retains the actual opposite-dip measurements, with comparable depths and unresolved kind identity. For449 opposite-half-phase deficits are shallower eclipses/modulation, not clean zero-flux nulls or same-kind centers; their lower depth can reject equal-kind P/2 but is not counted as another recurrence of the selected deep eclipse.

## Source and alternative extraction

Separately extracted background-subtracted TESScut sector100 1x1/3x3/5x5 aperture losses are 32.07/37.85/36.75 ppt. This is an alternative reduction of the same TESS photons, not an independent astrophysical occasion. Positive difference-centroid offset is 0.291 pixel, descriptive rather than a calibrated localization probability. The helper inspected actual difference images relative to the target and every Gaia neighbor passing the optimistic capability test. The60-arcsec Gaia cone has 241 entries; at the minimum tested aperture loss 32.07 ppt, 6 neighbor(s) could in principle supply the deficit with intrinsic loss≤100%. Gaia G-band and unit/full throughput are proxies; the intrinsic fraction is not directly compared to a blended pixel deficit. Sources outside60 arcsec, uncatalogued sources, extreme colors and unresolved multiplicity are limitations. Local TESScut contact fits1x1/3x3/5x5 give4085.17954/4085.18444/4085.18456 d; iid formal errors0.001775/0.000827/0.001248 d omit correlated noise and model/background systematics. The0.0051 d aperture spread is descriptive. The refined local difference image supersedes the provisional figure; see custom-local-fit.json and custom-local-difference.json.

| Gaia DR3 neighbor | sep arcsec | G | required intrinsic eclipse % |
| --- | --- | --- | --- |
| 5849122068442724096 | 48.07 | 15.06 | 67.3 |
| 5849122107110526592 | 42.89 | 14.16 | 31.0 |
| 5849122141470269440 | 10.43 | 14.85 | 55.8 |
| 5849122141470283008 | 28.27 | 14.50 | 41.5 |
| 5849122313268979072 | 53.69 | 14.78 | 52.5 |
| 5849122347628711040 | 23.02 | 14.01 | 27.5 |


Raw cutout/QLP source receipts, cone response, extraction scripts and image panels are in `batch-shared/helper-pixels/`; helper numeric and final audits are referenced by `batch-shared/LEAD-AUDIT.md`.

## Gaia orbit, catalogue and final assessment

Source-specific Gaia SB1 P=21.65603832±0.00371932 d, e=0.0645, omega=223.553 deg. Primary-velocity mass function=0.17945 solar masses. Closest edge-on conjunctionB minus measured/branch epoch comparison: observed offset0.26412 d (0.01220 phase), Gaia source-specific full-covariance linear error0.18011 d. Both conjunctions, covariance order, eigenvalue and source identity are in `batch-shared/gaia-geometry.json`. Approximate edge-on geometry and linear errors are descriptive, not calibrated association probabilities. For conditional/dip branches this comparison does not establish orbital ownership. The depths and durations permit stellar eclipses without requiring fitted component masses or radii.

Catalogue status: **UNKNOWN_INCOMPLETE_SCOPED_CHECKS**. Scoped catalogue recovery remains incomplete, including service failures. No positive match has been identified in the successful checks so far; unknown is not a non-match and no uncatalogued/new-system claim is made. Receipts: `batch-shared/../unmatched512/catalogue-recovery-selected12/`, especially `live-vsx/`. Catalogue service failures remain unknown and physical status is separate.

**Limitations:** The screening window clipped a roughly1.6 d flat-bottomed eclipse. New local raw fits require coverage at both contacts; sector11 and101 provide centers, while gapped fits are retained but excluded. A separate TESScut sector100 contact fit gives BTJD4085.18444, agreeing with the raw period prediction to0.00561 d and rejecting nearby integer counts. This reduction shares TESS photons but sector100 is a different observing occasion from sectors11/101. A neighbor10.43 arcsec away and others remain capable, so ownership is unresolved. Long-baseline orbital modulation and aperture drift require local baselines. TESScut is a separate reduction of the same photons. Gaia G-band flux ratios and full throughput are optimistic neighbor capability proxies, not TESS PRF likelihoods. No exhaustive all-event fitting, precision stellar characterization, or Monte Carlo was performed.

**Next deciding check:** Obtain higher-resolution eclipse photometry to resolve capable neighbors.
