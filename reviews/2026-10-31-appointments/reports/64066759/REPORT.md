# TIC 64066759: bounded current-criteria review

Physical verdict: **CONFIRMED**. Full review completion: **complete** (bounded, data-permitted five-check audit). Completion describes execution and is distinct from passing all five scientific checks. Historical CONFIRMED is not grandfathered.

The original source report and deciding artifacts in `appointments/vet64066759/` were reused with SHA-256 provenance. The review evaluates representative available events, timing, alternative reductions, source attribution and Gaia geometry; it is not an all-sector or all-event rerun. Catalogue novelty is supplied separately by the central seven-group review.

1. **Raw eclipse evidence:** Complete unflagged grazing A events in s87/s88 are 22.0/23.5 ppt deep,4.16/4.22 h long, and repeat in TARS. A partial s7 event has matching bottom and egress in four reductions. No event-shaped background change explains the complete events.
2. **Photometric period/timing:** P=40.9377055 +/-0.0000402 d uses epochs-53,0,1. The s87-s88 pair alone gives 40.9377 +/-0.0011 d; the fixed-shape partial s7 event agrees when projected back 53 cycles. The long-baseline uncertainty explicitly includes a 3-min minimum s7 timing error. P is +0.68 sigma from Gaia; P/2 and P/3 covered aliases lack dips.
3. **Pixels and capable neighbours:** TESScut s87/s88 deficit offsets are 3.1/1.1 arcsec from target with target-pixel depths 22.6/23.2 ppt. Close faint neighbours cannot provide the total deficit; the equal-brightness neighbour 78.3 arcsec away has no eclipse on its pixel. The deficit is centred on the target rather than that bright neighbour.
4. **Alternative reduction:** QLP and TARS reproduce both complete events; TESS-SPOC and eleanor additionally reproduce the partial s7 event. This is same-photon reduction robustness.
5. **Gaia/physical geometry:** Source-specific Gaia covariance predicts each A within 0.63 sigma. A grazing K-dwarf transit near periastron fits the durations; B cannot eclipse at the inferred inclination because its separation is 2.67 times larger. A fully covered B window is flat to 3.7-4.9 ppt. The depth favours R1 about 1.6 solar radii rather than the TIC 2.05, a retained stellar-model limitation.

Adopted row: period 40.93770552812586 d; period error 4.02430562196e-05 d; epoch BTJD 3674.520856303387 (A); representative depth 22.0 ppt. Epoch labels follow the historical A/B convention; B can be the deeper eclipse. The CSV field `primary_epoch_btjd` stores the named reference eclipse, with `epoch_kind` making that convention explicit. Gaia-only values for plausible systems are not photometric ephemerides.

Limitations: Long-baseline precision partly depends on a fixed-shape partial s7 event; three events total. Simplified geometry favours smaller primary radius than TIC. No B expected.

Next material check: Fit a full limb-darkened joint A model and constrain primary radius spectroscopically.

Deciding artifact register: `REPORT.md`, `gaia.json`, `archives2.json`, `ecl.json`, `ecl.py`, `ecl_fits.png`, `ephem.json`, `ephem.py`, `conj.json`, `conjmc.py`, `pix_s87.json`, `pix_s88.json`, `pix_s87.png`, `pix_s88.png`, `pixreg_trap.py`, `physics.txt`, `physics.py`, `bnull.txt`, `bnull.py`. Hashes are in `manifest.json`; helper validation is in `terra/HELPER-AUDIT.md`.

Representative raw-SAP sanity measurements are in `raw-audit.json`. Central-half median box depths are sanity checks and do not replace fitted depths or timing errors.


Public evidence: [historical report](../../evidence/64066759/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P018.
