# TIC 49416839: bounded current-criteria review

Physical verdict: **CONFIRMED**. Full review completion: **complete** (bounded, data-permitted five-check audit). Completion describes execution and is distinct from passing all five scientific checks. Historical CONFIRMED is not grandfathered.

The original source report and deciding artifacts in `appointments/vet49416839/` were reused with SHA-256 provenance. The review evaluates representative available events, timing, alternative reductions, source attribution and Gaia geometry; it is not an all-sector or all-event rerun. Catalogue novelty is supplied separately by the central seven-group review.

1. **Raw eclipse evidence:** Three deep B eclipses at 1558.2868,2286.8527,3272.5624 BTJD are 11.5-13.5 ppt and about 5.8-6.1 h long. Three shallow A events recur at the same phase. The s36 background spike is one flagged cadence, absent from unflagged eclipse fits; the event spans many clean cadences. Common-mode measurements are much shallower.
2. **Photometric period/timing:** Weighted B timings over cycles 0,34,80 give 21.4284666 +/-0.0000477 d and residuals under 3 min. The saved covariance and source timings are retained; s9 timing was conservatively enlarged to 0.007139 d. The independent shallow-A fit agrees. Gaia P differs by-0.48 sigma and the tested P/2 epochs are flat.
3. **Pixels and capable neighbours:** TESScut B regression in three sectors gives deficit-target offsets 3.4-4.2 arcsec and central depths 11.6-12.7 ppt. Neighbour TIC 49416838 at 28.8 arcsec is capable by dilution but its pixel has only 5.6-6.6 ppt and the deficit lies nearer target. Brighter distant neighbours are flat. The nearby unvetted ML-list flag does not relocate the source.
4. **Alternative reduction:** TESS-SPOC and TARS reproduce each deep B event, with eleanor additionally in s9; shallow A is supported by alternative reductions. All share the TESS photons.
5. **Gaia/physical geometry:** Gaia source-specific covariance predicts B conjunctions within 0.41 sigma. Phase separation is 2.3 sigma from Gaia; this is retained as modest association tension. A grazing primary transit and more central B occultation fit depths/durations with a late-K/early-M companion and primary radius 1.7-1.9 solar radii.

Adopted row: period 21.428466564976848 d; period error 4.771732314e-05 d; epoch BTJD 1558.284949338288 (B (dominant deep eclipse)); representative depth 13.3 ppt. Epoch labels follow the historical A/B convention; B can be the deeper eclipse. The CSV field `primary_epoch_btjd` stores the named reference eclipse, with `epoch_kind` making that convention explicit. Gaia-only values for plausible systems are not photometric ephemerides.

Limitations: A3 lacks egress and is weak. B-A phase separation is 2.3 sigma from Gaia; simple joint geometry has limited constraints. Dominant deep eclipse is labelled B in source.

Next material check: Obtain a complete A event and joint free-eccentricity model to test the phase-separation tension.

Deciding artifact register: `REPORT.md`, `gaia.json`, `archives2.json`, `ecl.json`, `ecl.py`, `ecl_fits.png`, `afit.json`, `afit.py`, `ephem.json`, `ephem.py`, `conj.json`, `conjmc.py`, `pixreg.txt`, `pixreg.py`, `pix_s9B.json`, `pix_s36B.json`, `pix_s72B.json`, `pix_s72B.png`, `physics.txt`, `physics.py`, `windows.txt`, `windows.py`. Hashes are in `manifest.json`; helper validation is in `terra/HELPER-AUDIT.md`.

Representative raw-SAP sanity measurements are in `raw-audit.json`. Central-half median box depths are sanity checks and do not replace fitted depths or timing errors.


Public evidence: [historical report](../../evidence/49416839/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P019.
