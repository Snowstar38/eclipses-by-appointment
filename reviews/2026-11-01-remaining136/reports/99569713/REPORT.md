# TIC 99569713: PROBABLE

Full bounded physical review: COMPLETE. Physical verdict is separate from catalogue novelty. The epoch is the selected recurring eclipse; no deeper-primary rank is assumed.

**Deciding evidence and limitation:** Ten repeated raw eclipses. Capable G15.57 source at5arcsec is unresolved within the target deficit; ownership remains unresolved. A farther source33arcsec away overlaps the wings.

Raw QLP SAP_FLUX representative windows contain 10 accepted free-center measurements in sectors [20, 73, 74]. Predicted windows are search guides, not timings. Quality-zero points enter fits; flagged or uncovered windows are not clean nulls. Rejected fits remain visible in numerical artifacts. Raw event plots and full recurrence phase plots were inspected; fitted dips alone do not establish eclipse morphology (TIC290749976 remains plausible).

Measured recurrence P=5.2326290195 +/- 0.0000213523 days; selected-eclipse reference BTJD=1848.0644657; fitted median depth=39.098ppt. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Singular/unidentifiable timing covariance is excluded. Within-sector cycle counts/parity are in [../alias-audit.json](../../campaign/batch03/alias-audit.json). Full-phase inspection tests secondary structure at its observed phase, without imposing phase0.5; unequal secondaries do not halve same-kind periods. Half/double ambiguity is described explicitly above where material. No exhaustive alias search is claimed. Sparse349452680 additionally has current availability and bounded sampled-null receipts.

Fresh TESScut sector74 stacks 4 actual covered events. Deficit-target offset=0.344pixel, target pixel=[7.781927206513501, 7.671035884768308], deficit centroid=[8.07134657900216, 7.856092487187115]. The image-model residual=0.386 is not a calibrated location error. Actual target pixel deficit=22.078 electron/s and baseline=607.88 electron/s. All flux-capable Gaia neighbors within60arcsec are below; their actual signed deficit and baseline are evaluated in common electron/s units at each source's rounded pixel. Overlapping PSFs prevent deblended ownership. Intrinsic required eclipse fraction uses pairwise Gaia G brightness; it is not directly comparable with diluted fractional pixel loss. Color, aperture response and unlisted faint/unresolved sources limit this approximate screen.

| Gaia source | separation arcsec | G | intrinsic required loss proxy | actual signed pixel deficit e/s | pixel baseline e/s |
|---|---:|---:|---:|---:|---:|
| 1102067481211251328 | 5.00 | 15.573 | 0.7623 | 14.868 | 442.2 |
| 1102064629352866304 | 33.29 | 13.634 | 0.1604 | 4.5959 | 286.98 |

Alternative background-subtracted target-centered TESScut1x1/3x3/5x5 depths=36.320/31.997/30.300ppt. These custom extractions test reduction robustness. All QLP and cutouts use TESS photons; same-sector extractions are not independent observations. Distinct sectors are distinct observing occasions on one instrument. Depth changes can be dilution/aperture/background effects; these numbers are not intrinsic eclipse depths. Pixel-arrays.npz preserves actual stacked images.

Gaia DR3 source=1102067476915290624, P=5.232723124d, e=0.12363. Closest edge-on conjunction offset=0.04468d (0.00854phase); source-specific full covariance linear timing allowance=0.23268d. This descriptive linear allowance is not a calibrated significance veto. Geometry code retains both eccentric conjunctions. Mass function=0.0098116 solar masses; TIC/adopted primary mass=1.070, minimum secondary mass=0.259, TIC radius=1.681 solar radii. Approximate central duration=5.507h versus measured median=5.210h. TIC radius and main-sequence minimum-mass companion assumptions make this a plausibility screen, not a fitted binary model. Orbit agreement alone does not establish target ownership.

| Sector | Search cycle | midpoint BTJD | formal center error d | timing input error d | depth ppt | status |
|---|---:|---:|---:|---:|---:|---|
|20|0|1848.0623800|0.00052327|0.010417|37.784|used|
|20|1|1853.2988967|0.0013999|0.010417|38.625|used|
|20|2|1858.5294235|0.0011585|0.010417|39.737|used|
|20|3|1863.7547087|1.442e+06|1.442e+06|38.525|rejected: Singular or unidentifiable center covariance: formal timing uncertainty exceeds search duration; excluded from ephemeris.|
|73|276|3292.2662357|3.6016e+05|3.6016e+05|39.725|rejected: Singular or unidentifiable center covariance: formal timing uncertainty exceeds search duration; excluded from ephemeris.|
|73|277|3297.5024285|0.00075714|0.0011574|39.579|used|
|73|279|3307.9686793|0.00043745|0.0011574|39.956|used|
|74|280|3313.2024396|0.0018421|0.0018421|39.027|used|
|74|281|3318.4324634|0.0006715|0.0011574|41.106|used|
|74|282|3323.6658271|0.00056952|0.0011574|38.985|used|
|74|284|3334.1305243|0.00077908|0.0011574|39.168|used|
|74|285|3339.3639341|0.00050783|0.0011574|38.978|used|

**Next check:** Resolved photometry through an eclipse to establish ownership; additional timing for remaining period/shape limits.

Seven-group catalogue receipts are in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv); known recovery and physical outcome are separate. No exhaustive priority claim. Evidence: [measurements.json](../../campaign/batch03/99569713/measurements.json), [raw-windows.csv](../../campaign/batch03/99569713/raw-windows.csv), [raw-events.png](../../campaign/batch03/99569713/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch03/99569713/fresh-pixels/diff_fresh.json)/png and pixel-arrays.npz; batch identity/hash receipts, geometry, phase and alias artifacts, helper audit. Source hashes and SHA256SUMS.json cover retained sources and outputs. Methods are preserved in a read snapshot rather than mutable manuscript hashes.


Stable review key: R561.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch03/99569713/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch03/99569713/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch03/99569713/fresh-pixels/gaia.json)
- [fresh-pixels/pixel-arrays.npz](../../campaign/batch03/99569713/fresh-pixels/pixel-arrays.npz)
- [fresh-pixels/run.log](../../campaign/batch03/99569713/fresh-pixels/run.log)
- [historical/diff_s74.json](../../campaign/batch03/99569713/historical/diff_s74.json)
- [historical/diff_s74.png](../../campaign/batch03/99569713/historical/diff_s74.png)
- [historical/gaia.json](../../campaign/batch03/99569713/historical/gaia.json)
- [measurements.json](../../campaign/batch03/99569713/measurements.json)
- [raw-events.png](../../campaign/batch03/99569713/raw-events.png)
- [raw-windows.csv](../../campaign/batch03/99569713/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch03/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
