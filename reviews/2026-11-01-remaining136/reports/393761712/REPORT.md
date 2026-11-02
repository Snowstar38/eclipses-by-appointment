# TIC 393761712: CONFIRMED

Full bounded physical review: COMPLETE. Physical verdict is separate from catalogue novelty. The epoch is the selected recurring eclipse; no deeper-primary rank is assumed.

**Deciding evidence and limitation:** Four deep eclipses repeat across three QLP sectors, with consecutive same-kind S72 events. Compact target deficit and no capable Gaia source in60arcsec support target attribution.

Raw QLP SAP_FLUX representative windows contain 4 accepted free-center measurements in sectors [20, 47, 72]. Predicted windows are search guides, not timings. Quality-zero points enter fits; flagged or uncovered windows are not clean nulls. Rejected fits remain visible in numerical artifacts. Raw event plots and full recurrence phase plots were inspected; fitted dips alone do not establish eclipse morphology (TIC290749976 remains plausible).

Measured recurrence P=11.3286747389 +/- 0.0000486314 days; selected-eclipse reference BTJD=1859.7472252; fitted median depth=73.110ppt. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Singular/unidentifiable timing covariance is excluded. Within-sector cycle counts/parity are in [../alias-audit.json](../../campaign/batch03/alias-audit.json). Full-phase inspection tests secondary structure at its observed phase, without imposing phase0.5; unequal secondaries do not halve same-kind periods. Half/double ambiguity is described explicitly above where material. No exhaustive alias search is claimed. Sparse349452680 additionally has current availability and bounded sampled-null receipts.

Fresh TESScut sector20 stacks 2 actual covered events. Deficit-target offset=0.105pixel, target pixel=[7.133785170811102, 7.130107863557841], deficit centroid=[7.077080695832156, 7.218069767439698]. The image-model residual=0.917 is not a calibrated location error. Actual target pixel deficit=44.682 electron/s and baseline=568.63 electron/s. All flux-capable Gaia neighbors within60arcsec are below; their actual signed deficit and baseline are evaluated in common electron/s units at each source's rounded pixel. Overlapping PSFs prevent deblended ownership. Intrinsic required eclipse fraction uses pairwise Gaia G brightness; it is not directly comparable with diluted fractional pixel loss. Color, aperture response and unlisted faint/unresolved sources limit this approximate screen.

| Gaia source | separation arcsec | G | intrinsic required loss proxy | actual signed pixel deficit e/s | pixel baseline e/s |
|---|---:|---:|---:|---:|---:|
| None capable within60arcsec | | | | | |

Alternative background-subtracted target-centered TESScut1x1/3x3/5x5 depths=78.578/77.575/76.493ppt. These custom extractions test reduction robustness. All QLP and cutouts use TESS photons; same-sector extractions are not independent observations. Distinct sectors are distinct observing occasions on one instrument. Depth changes can be dilution/aperture/background effects; these numbers are not intrinsic eclipse depths. Pixel-arrays.npz preserves actual stacked images.

Gaia DR3 source=878893455728757760, P=11.329658980d, e=0.04789. Closest edge-on conjunction offset=-0.25755d (-0.02273phase); source-specific full covariance linear timing allowance=0.24832d. This descriptive linear allowance is not a calibrated significance veto. Geometry code retains both eccentric conjunctions. Mass function=0.040276 solar masses; TIC/adopted primary mass=1.080, minimum secondary mass=0.456, TIC radius=1.898 solar radii. Approximate central duration=8.191h versus measured median=7.565h. TIC radius and main-sequence minimum-mass companion assumptions make this a plausibility screen, not a fitted binary model. Orbit agreement alone does not establish target ownership.

| Sector | Search cycle | midpoint BTJD | formal center error d | timing input error d | depth ppt | status |
|---|---:|---:|---:|---:|---:|---|
|20|1|1859.7463853|0.00042639|0.010417|74.512|used|
|47|65|2584.7826617|0.00054338|0.0034722|75.771|used|
|72|125|3264.5024722|0.00037681|0.0011575|71.709|used|
|72|126|3275.8319704|0.00041103|0.0011575|70.634|used|

**Next check:** Optional resolved follow-up for physical parameters and orbital eclipse labeling.

Seven-group catalogue receipts are in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv); known recovery and physical outcome are separate. No exhaustive priority claim. Evidence: [measurements.json](../../campaign/batch03/393761712/measurements.json), [raw-windows.csv](../../campaign/batch03/393761712/raw-windows.csv), [raw-events.png](../../campaign/batch03/393761712/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch03/393761712/fresh-pixels/diff_fresh.json)/png and pixel-arrays.npz; batch identity/hash receipts, geometry, phase and alias artifacts, helper audit. Source hashes and SHA256SUMS.json cover retained sources and outputs. Methods are preserved in a read snapshot rather than mutable manuscript hashes.


Stable review key: R564.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch03/393761712/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch03/393761712/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch03/393761712/fresh-pixels/gaia.json)
- [fresh-pixels/pixel-arrays.npz](../../campaign/batch03/393761712/fresh-pixels/pixel-arrays.npz)
- [fresh-pixels/run.log](../../campaign/batch03/393761712/fresh-pixels/run.log)
- [historical/diff_s20.json](../../campaign/batch03/393761712/historical/diff_s20.json)
- [historical/diff_s20.png](../../campaign/batch03/393761712/historical/diff_s20.png)
- [historical/gaia.json](../../campaign/batch03/393761712/historical/gaia.json)
- [measurements.json](../../campaign/batch03/393761712/measurements.json)
- [raw-events.png](../../campaign/batch03/393761712/raw-events.png)
- [raw-windows.csv](../../campaign/batch03/393761712/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch03/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
