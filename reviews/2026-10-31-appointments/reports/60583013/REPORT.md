# TIC 60583013: bounded current-criteria review

Physical verdict: **CONFIRMED**. Full review completion: **complete** (bounded, data-permitted five-check audit). Completion describes execution and is distinct from passing all five scientific checks. Historical CONFIRMED is not grandfathered.

The original source report and deciding artifacts in `appointments/vet60583013/` were reused with SHA-256 provenance. The review evaluates representative available events, timing, alternative reductions, source attribution and Gaia geometry; it is not an all-sector or all-event rerun. Catalogue novelty is supplied separately by the central seven-group review.

1. **Raw eclipse evidence:** A clean primary at 2210.9657 BTJD is 41.2 ppt deep and 9.77 h long. Two B events at 1478.8272 and 2225.0600 are 2.3-3.0 ppt deep, lasting about 9-11 h. The s6 B event follows a post-gap ramp, but its background is flat through ingress/egress and a 240-star common-mode check has median 0.03 ppt against target 2.39 ppt.
2. **Photometric period/timing:** Two B events separated by 28 cycles (746.233 d) give 26.65117 +/-0.00023 d using cross-pipeline timing scatter for the older event. Adjacent cycle counts differ from Gaia by about 100 sigma. P differs from Gaia by-0.6 sigma. Only one A exists; the A ephemeris assumes the B period and two B events have zero O-C by construction.
3. **Pixels and capable neighbours:** s33 target deficit is 1.2 arcsec from target at A and 1.3 arcsec at B. A central depth 40.78 ppt and B2.70 ppt are stable across aperture sizes. s6 B pixels are inconclusive at 3.8 sigma, so attribution relies on the strong representative s33 events. Capable B neighbours are inconsistent with the s33 centred deficit.
4. **Alternative reduction:** TESS-SPOC and TARS reproduce both s33 events and the older B; TGLC supports the latter. Poor eleanor timing is excluded from precise ephemeris use. These pipelines share the same photons.
5. **Gaia/physical geometry:** All conjunction offsets are within 0.7 sigma using the star's own Gaia covariance. Phase separation gives e cos omega=0.0453 against Gaia 0.0736 +/-0.0238; duration-based e sin omega is crude but compatible. Mass function, radius ratio and a/R1 are consistent with a 0.36-solar-mass dwarf. No limb-darkened precision fit is claimed.

Adopted row: period 26.65117 d; period error 0.00023 d; epoch BTJD 2210.9657 (A (period measured from B)); representative depth 41.2 ppt. Epoch labels follow the historical A/B convention; B can be the deeper eclipse. The CSV field `primary_epoch_btjd` stores the named reference eclipse, with `epoch_kind` making that convention explicit. Gaia-only values for plausible systems are not photometric ephemerides.

Limitations: Period relies on two secondaries, one after a data gap; one primary only. Older B pixel test inconclusive. Duration geometry is approximate.

Next material check: Obtain a second primary and joint limb-darkened model to test phase separation and geometry.

Deciding artifact register: `REPORT.md`, `gaia.json`, `arch2.json`, `ecl.json`, `ecl.py`, `ecl_fits.png`, `ephem.txt`, `ephem.py`, `conj.json`, `conjmc.py`, `cm6.txt`, `cm6.py`, `zoom6.png`, `zoom6.py`, `pixtrap.txt`, `pixtrap.py`, `pix_s33A.json`, `pix_s33B.json`, `pix_s6B.json`, `pix_s33B.png`. Hashes are in `manifest.json`; helper validation is in `terra/HELPER-AUDIT.md`.

Representative raw-SAP sanity measurements are in `raw-audit.json`. Central-half median box depths are sanity checks and do not replace fitted depths or timing errors.


Public evidence: [historical report](../../evidence/60583013/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P021.
