# Eclipsing binaries at the conjunctions predicted by near-edge-on Gaia DR3 astrometric orbits — data, predictions and code

Théo Chopard-Vilhem (ORCID 0009-0009-6177-3879), "Iuliu Hațieganu" University of Medicine and Pharmacy, Cluj-Napoca, Romania.
Supplement to the Research Note of the AAS of the same title (2026). Cite as: Chopard-Vilhem, T. 2026, Zenodo,
doi:10.5281/zenodo.23405354 (version 1.2.0; all versions: 10.5281/zenodo.23342415).

## What this is
Gaia DR3 astrometric orbits give the inclination and the times of conjunction. The 1726 orbits brighter than G = 14
whose best-fitting inclination lies within 1° of 90° were selected, their uncertainties propagated to the conjunction
times, and the TESS light curves (SPOC, TESS-SPOC, QLP) searched at both conjunctions. This deposit holds every input,
intermediate and result of that search, the code that produced them, and **predictions of the next eclipses**.

## Contents
| Folder / file | Content |
|---|---|
| `n2_numbers.txt` | **every number quoted in the note, recomputed by `code/n2_statistics.py` from these files, with its source** |
| `track3_detail.csv` | the 1726 selected orbits: period, inclination uncertainty, eclipse probability, conjunction-time uncertainties |
| `track3_astrometric_orbits_selected.csv` | their Gaia DR3 orbital elements (`gaiadr3.nss_two_body_orbit`) |
| `pilot_results/` | search windows and flags (`windows.csv`, `flagged.csv`), all single events (`events.csv`), per-star log (`stars.jsonl`), false-alarm trials, catalogue cross-match (`known_check.csv`), artefact vetting (`artefact_vetting.csv`), asteroid veto (`asteroid_veto.csv`), summary |
| `calibration/` | the 256 known eclipses used to calibrate the artefact vetting (`calib_windows.csv`, `calib_detail.csv`) and its verdicts (`calib_vetting.csv`, also at the top level, where `n2_statistics.py` reads it) |
| `injection/` | injection–recovery of eclipses and self-lensing flares (completeness; bounds on compact companions) |
| `diff_images/` | pixel-level difference images (in eclipse minus out of eclipse) and their verdicts |
| `vetting/` | TIC, ExoFOP and SIMBAD checks of the candidates (`literature_summary.csv`, `literature.txt`) |
| `predictions/` | next eclipses with uncertainties (`eclipse_predictions.csv`), calendar for Cluj-Napoca (`observable.ics`), archival search |
| `control/` | **version 1.1.0:** the face-on control — 2000 orbits over 30° from edge-on, which cannot eclipse, searched identically; the search covered all 2000 orbits; 128 of them have windows (387 windows) (`control_detail.csv`, `control_results/windows.csv`, `control_faceon_summary.txt`) |
| `figure/` | the figure of the note |
| `code/` | all scripts; each states its inputs, outputs and options in its header |

## Version history
* **1.2.0 (October 2026), the version cited by the note.** Corrects version 1.1.0, which is superseded:
  - CD−81 705 also has one QLP flag (version 1.1.0 said that all flags of the seven systems were SPOC or TESS-SPOC);
    without it, its chance probability is 3×10⁻⁷;
  - the figure (`figure/`) and the calibration of the Gaia timing uncertainties leave out the two withdrawn systems.
    The offsets of the 14 remaining conjunctions (seven systems and two known binaries) then scatter more than the
    propagated uncertainties: standard deviation 1.10 against 0.87 ± 0.15 expected within the windows; scale factor
    1.8, 68 per cent interval 1.1–4 (version 1.1.0, with the withdrawn systems: 1.02 against 0.87 ± 0.13);
  - counts refer to distinct dips: the 157 flags are 152 dips, of which the vetting passes 123;
  - notes on missing control levels and on the sector number 1751 (below);
  - `code/n2_statistics.py` and `code/make_n2_figure.py` updated accordingly.
* **1.1.0 (15 October 2026).** Adds the face-on control (`control/`, `code/control_faceon.py`, section 3b of
  `n2_numbers.txt`): the same search on 2000 orbits over 30° from edge-on, which cannot eclipse. QLP windows have a
  false-alarm rate of 23 per cent (39 of 171), not the 1 per cent that the shifted windows of version 1.0.0 gave (their
  no-overlap rule kept mostly quiet light curves); SPOC and TESS-SPOC windows give no false alarm in either test (0 of
  216 in the control, 0 of 754 shifted). About 60 of the 157 flags are expected to be false, almost all QLP;
  HD 194593 and BD+85 212 (two flags each, one QLP) are withdrawn; the seven systems stand on their SPOC and TESS-SPOC
  flags. `code/feas_track3_detail.py` and `code/pilot_track3.py` gained the options used for the control (default
  behaviour unchanged).
* **1.0.0 (13 October 2026).** The deposit accompanying the submitted note.

## Notes for re-use
* **Working names.** File and folder names keep the working names of the search: `track3_` and `pilot_results/`
  refer to this search (track 3 of the author's Gaia–TESS programme, run as a "pilot" on all 1726 orbits), and `n2_`
  to the Research Note. They are kept because the scripts use them.
* **False-alarm trials.** `pilot_results/false_alarms.csv` is the pilot's first estimate (123 shifted windows), superseded.
  `pilot_results/false_alarms_extended.csv` holds 6386 trials made by version 1 of `code/false_alarm_rate.py`, which let
  shifted windows overlap the real ones; `code/n2_statistics.py` applies the corrected rule (no overlap with any real
  search window, no real flagged dip inside), which leaves the 1076 clean trials used in the note. Version 2 of
  `false_alarm_rate.py`, deposited here, applies that rule when making new trials.
* **Two stars with two Gaia solutions** (Gaia DR3 2208365672715184256 and 6345896578791113472) appear twice in
  `track3_astrometric_orbits_selected.csv`; the AstroSpectroSB1 solution is the one used. Neither is named in the note.
* **Empty columns** are placeholders of the scripts: bump statistics in `calib_windows.csv` (eclipses only),
  `note` columns, `TESS_EB` in `known_check.csv` (no match), and the SIMBAD columns of `vetting/dossier.csv`, whose
  query failed; the SIMBAD bibliography is in `vetting/literature_summary.csv` and `vetting/literature.txt`.
* **Distinct dips.** A dip can fall in two overlapping windows of the same star; the 157 flags are 152 distinct dips
  (flags of one star less than 0.05 d apart merged), and the vetting counts refer to the distinct dips.
* **Missing control levels.** In 134 of the 769 windows the random-epoch control level could not be computed (no room
  for random epochs away from the conjunctions), so the variability criterion was skipped there (columns `dip_ctrl`,
  `bump_ctrl` empty). The face-on control has the same property (27 per cent of its windows), and its SPOC and TESS-SPOC
  windows without a control level give no false alarm either (0 of 49). Two of the 29 flags of the seven systems lack it.
* **Sector 1751.** Four TESS-SPOC windows carry the sector number 1751, as read from the light-curve product; their
  times (20–24 January 2026) are correct. One of them holds an eclipse of HD 284424.
* **UCAC4 146-021461** (Gaia DR3 5299678829378060288) is present in the files but not named in the note: its
  pixel-level test is inconclusive.

## Reproducing
`python3 code/n2_statistics.py`, run from this folder, rewrites `n2_numbers.txt`. It was reproduced identically on a
second machine (Python 3.12.3, numpy 2.4.4, pandas 2.3.3, scipy 1.17.1, astropy 8.0.1, lightkurve 2.6.0); the search
itself was run with Python 3.13. The full search (`code/pilot_track3.py`, then the vetting, injection and prediction
scripts) needs network access to MAST, the Gaia archive, SIMBAD and ExoFOP; `requirements.txt` lists the packages.

## Testing the predictions
`predictions/eclipse_predictions.csv` gives, for each system, the mid-eclipse time (UTC), its 1σ uncertainty
(`sigma_min`, minutes), the expected depth and duration. Only eclipses **after the publication date of this record**
are genuine forecasts. Observations that confirm or refute them are welcome (t.chopard.research@proton.me).

## Licence
Data, predictions and figure: CC BY 4.0. Code: MIT (see `LICENSE`).
