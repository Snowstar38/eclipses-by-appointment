# TIC 466336052: bounded current-criteria review

Physical verdict: **CONFIRMED**. Full review completion: **complete** (bounded, data-permitted five-check audit). Completion describes execution and is distinct from passing all five scientific checks. Historical CONFIRMED is not grandfathered.

The original source report and deciding artifacts in `appointments/vet466336052/` were reused with SHA-256 provenance. The review evaluates representative available events, timing, alternative reductions, source attribution and Gaia geometry; it is not an all-sector or all-event rerun. Catalogue novelty is supplied separately by the central seven-group review.

1. **Raw eclipse evidence:** Two complete A events at BTJD 2818.4830 and 3557.6840 are 44.1 and 42.8 ppt deep in QLP, lasting 9.62 and 9.64 h. Unflagged event fits agree with TESS-SPOC and TARS. The second event has a background ramp, but the first has the same shape without it.
2. **Photometric period/timing:** The two A events span 23 cycles (739.201 d): P = 32.139199 +/- 0.000037 d. Adjacent cycle counts differ from Gaia by about 30 sigma. The error comes from profile timing errors with red-noise inflation; two events give no independent O-C residual test. Gaia period agreement is -0.16 sigma.
3. **Pixels and capable neighbours:** TESScut s55/s82 difference maps put the deficit on the target: 1.9/2.9 arcsec from the light centroid. Aperture depths are 43/42/41 and 44/42/39 ppt for 1/3/5-pixel squares. The capable G13.97 neighbour at 65.5 arcsec has only 3-4 ppt on its pixel and would need about 430 ppt to explain A.
4. **Alternative reduction:** TESS-SPOC and TARS reproduce both events at 39.5-44.1 ppt, with mid-times within 1.9 min. These are alternative reductions of the same TESS photons.
5. **Gaia/physical geometry:** The source-specific Gaia covariance gives A timing agreement within 0.12 sigma. A limb-darkened model gives R1=1.42-1.60 solar radii and R2 about 0.29 solar radii, consistent with the primary and mass function. B is expected in scattered-light gaps; the null constraint leaves the Gaia-supported separation range available.

Adopted row: period 32.139199 d; period error 3.7e-05 d; epoch BTJD 2818.48299 (A); representative depth 44.1 ppt. Epoch labels follow the historical A/B convention; B can be the deeper eclipse. The CSV field `primary_epoch_btjd` stores the named reference eclipse, with `epoch_kind` making that convention explicit. Gaia-only values for plausible systems are not photometric ephemerides.

Limitations: Only two A eclipses; no internal timing residual test. B windows are contaminated or missing; no B detection. Gaia conjunction uncertainty is 3-4 d.

Next material check: Observe a third A eclipse and a clean B window near 0.3% precision.

Deciding artifact register: `REPORT.md`, `gaia.json`, `archives2.json`, `ecl.json`, `ecl.py`, `ecl_fits.png`, `physics.txt`, `physics.py`, `conj.json`, `conjmc.py`, `diff.txt`, `diffimg.py`, `diff_s55A.png`, `diff_s82A.png`, `afit.txt`, `afit.py`, `bnull.txt`, `bnull.py`. Hashes are in `manifest.json`; helper validation is in `terra/HELPER-AUDIT.md`.

Representative raw-SAP sanity measurements are in `raw-audit.json`. Central-half median box depths are sanity checks and do not replace fitted depths or timing errors.


Public evidence: [historical report](../../evidence/466336052/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P017.
