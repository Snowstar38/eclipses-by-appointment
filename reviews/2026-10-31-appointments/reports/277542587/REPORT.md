# TIC 277542587: bounded current-criteria review

Physical verdict: **CONFIRMED**. Full review completion: **complete** (bounded, data-permitted five-check audit). Completion describes execution and is distinct from passing all five scientific checks. Historical CONFIRMED is not grandfathered.

The original source report and deciding artifacts in `appointments/vet277542587/` were reused with SHA-256 provenance. The review evaluates representative available events, timing, alternative reductions, source attribution and Gaia geometry; it is not an all-sector or all-event rerun. Catalogue novelty is supplied separately by the central seven-group review.

1. **Raw eclipse evidence:** TESS s80 contains A at 3488.8242 +/-0.0020 BTJD (77.6 ppt,12.37 h) and B at 3496.7501 +/-0.0027 (149.2 ppt,9.98 h). A mostly uses flagged scattered-light cadences and is treated cautiously; B is clean. Validated KELT photometry independently repeats A over 2011-2017. The helper reproduces a central-half box S/N 13.31 with 28 points and a 4.64% diluted deficit, and both time subsets independently retain the signal.
2. **Photometric period/timing:** KELT scanning anchored to the measured TESS A gives 24.33180 d,0.84 sigma from Gaia; adopt 24.3318 +/-0.0002 d. This uncertainty is a conservative working grid/window precision, not a calibrated Gaussian 1-sigma result. Fine-grid and full-box optima differ slightly; the original coarse fold peak 24.33200 is grid resolution, not a contradiction. The old report Gaia-only period is superseded. Exact 10-night claim is not used because the helper finds a binning-dependent count.
3. **Pixels and capable neighbours:** TESS TESScut B deficit is 0.4 arcsec from light centroid and depths 150.3/148.8/147.7 ppt for 1/3/5-pixel squares; A depths 78.2/78.1/77.9 ppt and 0.3-arcsec offset. The capable G13.32 neighbour at 84.5 arcsec is flat on its own pixel; fainter neighbours cannot supply B. This localizes TESS eclipses; broad KELT aperture alone does not localize them.
4. **Alternative reduction:** No second archive pipeline exists for s80. Custom TESScut aperture photometry independently reduces the same TESS photons and reproduces both events. KELT is a separate instrument and supplies actual repeated observations.
5. **Gaia/physical geometry:** The original source-specific Gaia covariance gives A/B conjunction offsets 0.60/0.83 sigma and B-A separation 0.77 sigma. The working measured period shifts the fractional separation negligibly. A grazing/B central two-sphere geometry gives e sin omega about-0.186 against Gaia-0.196; radii fit an evolved F primary plus near-solar companion. A quality/background caveat remains, supported by later clean repeats in KELT.

Adopted row: period 24.3318 d; period error 0.0002 d; epoch BTJD 3488.8242 (A; KELT+TESS period); representative depth 77.6 ppt. Epoch labels follow the historical A/B convention; B can be the deeper eclipse. The CSV field `primary_epoch_btjd` stores the named reference eclipse, with `epoch_kind` making that convention explicit. Gaia-only values for plausible systems are not photometric ephemerides.

Limitations: TESS A mostly flagged; only one TESS A+B pair. KELT period precision is heuristic and anchored to TESS; broad ground aperture dilutes depth. Sparse KELT B is supporting only. Historical exact-night count not adopted.

Next material check: Obtain another full well-calibrated A/B pair and an event-timing based period uncertainty.

Deciding artifact register: `REPORT.md`, `gaia.json`, `archives2.json`, `ecl.json`, `ecl.py`, `ecl.png`, `conj.json`, `conjmc.py`, `pix_A.txt`, `pix_B.txt`, `pixtrap.py`, `pix_s80A_allq.json`, `pix_s80B.json`, `pix_s80B.png`, `ebfit_s80.json`, `ebfit_s80.py`, `physics.txt`, `physics.py`. Hashes are in `manifest.json`; helper validation is in `terra/HELPER-AUDIT.md`.

The later KELT evidence supersedes the old period status; see `ground/kelt/SINGLES.md`, validated light curve, scan script and helper recheck.


Public evidence: [historical report](../../evidence/277542587/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P022.
