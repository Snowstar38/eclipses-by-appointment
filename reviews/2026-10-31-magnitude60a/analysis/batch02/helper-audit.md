# Independent helper audit, batch 02

All ten queued TICs covered. Examined the event measurements, historical target-pixel stack and neighbor lists, QLP and cutout extraction comparison, and Gaia geometry output. Recomputed weighted straight-line fits directly from `mid_btjd`, cycle and timing errors for every usable event: period, epoch and inflated covariance error reproduce saved values to numerical precision. These are measured trapezoid centers, not the `predicted_btjd` windows. Reported epoch is the fitted intercept at the minimum used cycle, not necessarily any individual measured center; selected repeating eclipse is called primary by convention, without proof of deeper eclipse identity. Per-event errors are max(formal covariance, half cadence); fit covariance is inflated by sqrt(max(reduced chi-square,1)). This is a statistical/model-dependent allowance, not calibrated coverage or total systematic error. Quality-zero selection excludes flagged cadences, which must not be called clean non-detections.

Each selected photometric period is close to the full Gaia orbital period. In the three explicitly checked parity cases 125690413, 120037640 and 256665207, even/odd measured depth medians are 22.07/21.75, 22.78/24.04, and 6.81/6.14 ppt, respectively; these combine sectors with differing apertures/noise and are not a definitive equality test. No basis to silently double the orbital period. Duration comparison assumes a central edge-on orbit, approximate TIC radius and minimum-mass companion; conjunction covariance is linear and not a hard sigma veto. Alternative TESScut aperture and QLP are reductions of the same photons, not independent observing occasions. Historical image event `t` values are predicted stacking centers, not measured timings. Capable-neighbor tests use Gaia G brightness as a proxy and ignore color and detailed PSF uncertainties.

For TIC 129565419 the old global difference peak is remote and the 9x9 PSF residual is 0.968. A fresh local re-stack from the same historical pixels using 3.23 h duration and a 5x5 fit gives residual 0.115; three events, 1/3/5-aperture depths 24.40/23.92/22.14 ppt, and target offset (?0.02,+0.01) px. The remote image feature does not control the target-centered fit; remaining neighbor at 38.9 arcsec could nominally produce the depth. New files are `helper/129565419/diff_helper.json` and `.png`; reduction script `Fable 5/made/sb1-scale/diffimg/diffstack.py` uses its printed 9x9 label even when DIFF_FITR=2 selects 5x5.

For TIC 448485777, a G=13.14 neighbor 16.26 arcsec away can nominally cause the dip with 16% loss. Difference centroid is 0.25 pixel from target and 0.62 pixel from neighbor. Target is favored, but 0.77-pixel separation and no calibrated localization uncertainties leave crowding a material caveat; this helper does not assert decisive source attribution. For 125690413 cycle 196 has a broader, deeper distorted shape, with timing residual ~?0.038 d and full-fit reduced chi-square 5.25; compare excluding that sector and do not claim the inflated error captures all systematics. For 120037640 Gaia phase offset ?0.051 is a physical tension relative to linear covariance and period projection; a threshold alone is not a rejection.

## Coverage, measured periods and historical pixel evidence

Period and epoch values below refer to measurements.json, not Gaia predictions. Offset is historical deficit centroid relative to the target; capable neighbors are count with nominal depth_needed <= 1. Depths are cutout aperture1/3/5 in ppt. A blank capable count is zero. Hashes are SHA-256.

| TIC | P days | N measured | pixel sector | offset px | capable | aperture depths ppt | measurement SHA-256 | historical diff SHA-256 |
|---|---:|---:|---:|---|---:|---|---|---|
| 129565419 | 8.983706971 | 5 | 56 | -0.039, +0.010 | 1 | 25.89/25.70/23.79 | `b0fca9e7c920e720b2016d9bd7af36a79ab30b7224670322892c15d3a579557e` | `8b1eb846064ec1ecb46de53da2cc10af238dd93751459380ab92e8716bf5339e` |
| 125690413 | 3.686896563 | 18 | 41 | -0.216, +0.302 | 3 | 22.33/22.13/21.69 | `ebe686839a204ecb27bb6e7b59c676d44cd8e03885526d55eddb8e1d89170143` | `833a1cda815930b1805149abe3dbcfb960717b6c01506ad875a75bf45ffb1e0e` |
| 445045766 | 5.036480387 | 6 | 47 | +0.125, -0.138 | 0 | 23.31/23.87/22.97 | `3467458104c16203c208aac5fa94934a71ae984d51d43926b7b7d4ad3a7c55eb` | `353e0cbd0e24038650da50bbc11ee830dfcf44b3bee473e16dc630fa0f41e2ae` |
| 120037640 | 3.698262407 | 11 | 66 | +0.168, +0.059 | 2 | 22.77/22.27/20.12 | `7e36d585e4adfc89aeef50f6de3854f227fcccd279d9a7c01a952106d5e393cb` | `6b7b6064d0179a61c86f35b5825d58ff92cef470444d21f69f7a4aec05c8ba50` |
| 448485777 | 5.895288239 | 8 | 11 | -0.205, +0.147 | 6 | 33.27/29.82/29.13 | `91a1b9bf1dba935e05c440fb64736eb34912187c4f390c57483bc51c39627d49` | `3e3c1626b871c0a6c25c8bd39ce2b8580e638c38238d70d4c8553359b4213b8e` |
| 158647370 | 6.013232322 | 6 | 29 | -0.050, +0.155 | 0 | 87.13/86.01/85.16 | `fbb452efac9b5fceb9bae0bc439fd6cf263a71d69acac13ed70e24d7c36b17e3` | `8a6ac37156946a4708575b1388eed4a545796954626ac1dd8af2bb0347773ff6` |
| 302190527 | 9.470306482 | 8 | 57 | +0.064, +0.182 | 0 | 263.44/258.28/255.10 | `c94163e048523496407fbd2747fab4615d6be96919e8be73d1b1461f771b85ca` | `66ad698b1d9e8df858bdd1d089d9bb5d7a1d0bd181f0f3f6e3503fe77a85b516` |
| 138941853 | 11.598591213 | 5 | 98 | -0.084, -0.024 | 4 | 9.20/8.30/6.81 | `54492240075e5a9234aaeb148a6b0e7b0fa9fa677dcd6f717a8a61a23f886a08` | `813f91b510b7e8a765c8e8bc7694c294a6660a58f0ba46c5fcad7c989da7b80f` |
| 256665207 | 2.790738578 | 19 | 55 | +0.142, -0.086 | 2 | 7.14/6.68/6.61 | `082c09c7538d017cb10edd21e081fbcab756369b43ae0da589442238ee35b48e` | `cfb0a02d4cb071c1415274cbae83e37ae1dc3efe17744d6e375ef0f7c77a5109` |
| 91628894 | 6.766119320 | 7 | 63 | -0.318, +0.204 | 8 | 9.97/10.40/9.92 | `b6f42f01a0e8e69a8afa39581ddb3673324f8c5f0b2ef11b9253022840cb846a` | `f6566f3095ec13447a881387d93865164d651ffd2f6c94059584ff33f61f3dde` |

## Additional deciding artifact hashes

- `[local path omitted] `ea8e471a716287742ff9aaf557fdd31e9e6dc3910fa5ad18eecf5ae50510efb4`
- `[local path omitted] `72a8e72271829ef4a6c045258fa8ca194dfefde3a084bf495b236015d6da55d9`
- `[local path omitted] `d5701ec8a4501662bb430ea518645f1366c59686648752905308d88dd62492c4`
- `[local path omitted] 5\made\sb1-scale\diffimg\diffstack.py`: `3cfcaff17bdce7ae6e7facac18879eb5b443718be2f7ec947b4f82b1b752ecf4`
- `[local path omitted] `ca324de762736948c5143e464620614444559f876a4ff72b3dc9aed6aa94a2ba`
- `[local path omitted] `53eef31c9f169c9b1ab7353177dc20d99809c57262176248894de013750a5cbc`
- `[local path omitted] `c7ceb8d64f2fe71a31c42e17f7e3ee4d7b69ebdd8ff2df9a16980f701557c6bb`

Lead owns final physical verdict and report. Review evidence does not establish absence of unmodeled companions or rule out all astrophysical alternatives.

## Final result cross-check

All ten RESULTS rows have existing reports; period, period error, fitted epoch and depth exactly match each target?s measurements.json. An initial sector-label typo for TIC 138941853 (33 instead of 32) was reported to the lead for correction; the measurement file and event tables show sectors 6, 32 and 98. The lead retains ownership of classification and final report hashes.
