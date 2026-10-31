# TIC 8853239: bounded current-criteria review

Physical verdict: **PLAUSIBLE**. Full review completion: **complete** (bounded, data-permitted five-check audit). Completion describes execution and is distinct from passing all five scientific checks. Historical CONFIRMED is not grandfathered.

The original source report and deciding artifacts in `appointments/vet8853239/` were reused with SHA-256 provenance. The review evaluates representative available events, timing, alternative reductions, source attribution and Gaia geometry; it is not an all-sector or all-event rerun. Catalogue novelty is supplied separately by the central seven-group review.

1. **Raw eclipse evidence:** One clean flat-bottomed A event at 2629.0699 BTJD is about 60 ppt deep and 6.95 h long. No secure B detection exists: the 3-4 ppt B-window structures are also common among unrelated times in the variable baseline. Sector 21 target position is off the active CCD, so its predicted A window was not observed.
2. **Photometric period/timing:** No photometric period is measured. The listed 24.6470 +/-0.0114 d is Gaia SB 1 selection-orbit information only. KELT does not detect a repeat: half the tested Gaia period grid has useful null coverage, while the other half is poorly sampled. A grid-tail S/N 5.1 supported by 3 points is not a detection. This fails the repeated-event/timing requirement. Current HTTP 200 TESScut sector-list lookup on 2026-10-31 returns only s 21/s48; no new available cutout sector was listed.
3. **Pixels and capable neighbours:** s48 TESScut regression gives 59.8 +/-0.4 ppt in the target pixel; aperture depths 59.8/59.8/57.8 ppt and deficit offset 3.6 arcsec from target. The G14.45 neighbour at 50 arcsec would need about 95% eclipse but its pixel shows only 2.3%, consistent with target leakage.
4. **Alternative reduction:** QLP, TESS-SPOC, TARS and custom TESScut recover the same single A event with times within 1.8 min. These reductions do not count as repeated astrophysical events.
5. **Gaia/physical geometry:** A is 0.19 sigma from the Gaia conjunction. Depth and duration are compatible with a roughly 0.35-solar-mass dwarf, but the geometry cannot independently validate a Gaia-only period. The tentative secondary and its 0.61% upper limit remain inconclusive.

Adopted row: period 24.647 d; period error 0.0114 d; epoch BTJD 2629.0699 (A; Gaia-only period); representative depth 60.0 ppt. Epoch labels follow the historical A/B convention; B can be the deeper eclipse. The CSV field `primary_epoch_btjd` stores the named reference eclipse, with `epoch_kind` making that convention explicit. Gaia-only values for plausible systems are not photometric ephemerides.

Limitations: Single secure event; Gaia-only period; KELT null is coverage-limited and not a refutation. Tentative B is not an ephemeris.

Next material check: Measure a second A eclipse to test the cycle period; a B detection alone would still need repeat timing.

Deciding artifact register: `REPORT.md`, `gaia.json`, `arch2.json`, `ecl.json`, `ecl.py`, `ecl_fits.png`, `pixreg.txt`, `pixreg_trap.py`, `pix_s48.json`, `pix_s48.png`, `tc_s21.txt`, `tc21.py`, `bphys.txt`, `bphys.py`, `conj.json`, `conjmc.py`. Hashes are in `manifest.json`; helper validation is in `terra/HELPER-AUDIT.md`.


Public evidence: [historical report](../../evidence/8853239/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P020.
