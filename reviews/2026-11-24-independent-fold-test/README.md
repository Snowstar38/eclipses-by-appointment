# Independent test of a depth discrepancy in saved TESS folds

In an earlier review, some folded light curves showed a much deeper dip than the scalar depth recorded by the pipeline. We applied the same flag to a separate set of 561 previously pipeline-rejected apertures. A flag requires two adjacent folded bins each at least 10 parts per thousand below baseline, with the shallower bin at least five times the recorded depth (using a floor of 1 ppt for that depth). Nineteen apertures triggered the flag. The question was whether inspecting original TESS time series would recover at least two discrete eclipse-like events.

| Independently reviewed sample | Flagged apertures meeting endpoint | Comparison apertures meeting endpoint |
|---|---:|---:|
| Two-minute matched pilot, 24 sectors | 0 of 5 | 0 of 5 |
| Full-frame extension, 43 sectors | 3 of 5 | 0 of 8 |

Sol measured the events on the original time axis in SAP and PDCSAP flux. Terra independently inspected each sector and event shape with the flags masked. An aperture met the endpoint only when both reviewers identified a pair of separated, discrete dips with observed bracketing baselines, each deeper than 10 ppt and five times local scatter, sustained for at least three cadences. The chosen endpoint identifies eclipse-like dimming in an aperture. A stellar catalogue admission requires further evidence about the host and companion.

**Two-minute observations.** The original salted draw produced five two-minute pairs. All five pairs tied with neither member meeting the endpoint. TIC 63898806 had two quantitatively deep troughs within a single disturbed interval with bright crests between them. Noise and gaps limit the conclusions for several other apertures. [All ten decisions](outcomes.csv) · [Original sampling and outcome protocol](protocol.md).

**Full-frame observations.** The earlier study’s additions all came from full-frame data. Once we saw that the initial draw contained only two-minute targets, we registered a separate extension covering every eligible full-frame aperture. TIC 160193535, TIC 321912132 and TIC 441584021 met the endpoint. In TIC 321912132 the short interval between two dips also predicts a well-covered window with no dip. These data support repeated dimming while leaving its orbital period open. One comparison, TIC 270225500, showed one deep eclipse-like event. [All thirteen decisions](ffi/outcomes.csv) · [Extension protocol](ffi/protocol.md) · [Visual readings](ffi/terra/readings.txt).

**Which stars dimmed?** A separate check of two individual eclipses per positive aperture favored the nominal Gaia counterpart in all six difference images. For TIC 441584021 these images tested only the deeper eclipse family. TIC 160193535 is a known double-lined spectroscopic binary with a 12.13261-day orbit; the deep photometric events suggest a different clock. The component responsible remains open. TIC 321912132 and TIC 441584021 both had earlier machine-selected flags. [Source measurements](localization/fits.csv) · [Prior identifications](credit/README.md).

**What to try next.** The full-frame results support checking individual events when adjacent bins disagree with the saved depth. The two-minute pilot illustrates how oscillations and noisy segments can produce that discrepancy. The full-frame subgroup contains only thirteen stars, and the two-minute sample contains ten. Neither provides a general success rate. Both cohorts started with candidates that Fable’s earlier pipeline had rejected.

The earlier [402-aperture review](../2026-11-24-fable-paired-review/README.md) motivated this test. We excluded TICs already in the original 707-aperture shortlist or the published top-level review and claim registers. We also excluded exact matches and positions within 30 arcseconds of the available 798-source Chopard-Vilhem comparison list. That check is limited to the available lists. The [eligible apertures](eligible.csv), [masked pilot draw](batch.csv), [pair assignments](assignments.csv), and [original folded arrays and measurements](original-folds.zip) preserve the selection.

Run `python verify.py` in this directory to reproduce the draw and check both outcome tables. Add `--inputs` with NumPy installed to recompute the fold statistics from the archived measurements. Sector URLs, product hashes and event measurements are in each cohort’s `sol` directory. Individual sector plots are in its `terra` directory.

The subsequent [TIC 160193535 timing study](timing-160193535/README.md) fits a 17.1488321-day eclipse period in thirteen sectors. Both eclipse families favor the nominal Gaia position, whose published spectroscopic orbital period differs.

A [second batch of ten two-minute apertures](second-2min/README.md) recovered the 1.179-day signal of HD 276904 in three sectors, along with one 40% dip. Target pixels explain two isolated events on other stars as background-subtraction artifacts. The [spectroscopy follow-up on TIC 160193535](timing-160193535/spectroscopy/README.md) records which archives were checked and the velocity separation predicted by the published orbit.

An [asteroid search in 20 fresh apertures](background-pilot/README.md) identified Vesta illuminating the background pixels near TIC 630314437. The event checker records crossings and near misses, with controls and coincident-eclipse tests.

A [paired review of 35 full-frame apertures from Fable](fable-fold-35/README.md) recovered 19 alternative eclipse schedules, four with competing periods. Eight were independently recovered in ZTF photometry and localized at the target in TESS images.
