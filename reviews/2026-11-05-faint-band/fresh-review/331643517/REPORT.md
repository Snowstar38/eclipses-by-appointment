# U007 — TIC 331643517

**Physical verdict:** REFUTED (provisional lead classification). **Bounded review:** COMPLETE. **Catalogue status:** KNOWN_PRIOR_EB; no new-system claim is made here. The shared-catalogue receipts define the checked scope.

## Raw events and coverage

S56, S76 and S83 show many narrow deep and flanking shallower dips. Selected deep centers fit P=1.11451118 d across cycles 0,492,655, with a 0.00003 d residual RMS. This is the known short-period EB clock of TIC 331643515, 41.995 arcsec from the queued TIC 331643517. The neighbor table gives P_TESS=1.114507 d; its VSX P=1.67164 d is an alias.

Cached QLP sector coverage: 16,56,76,83. Lead verified SHA256 of every used FITS and bulk-result file before measuring. `lead-context.json` contains cadence endpoints, quality-zero sample counts and flagged-window measurements; `lead-timing.json` contains local trapezoid measurements. The gallery `lead-raw-context.png` shows representative raw SAP alongside KSPSAP where present. Detector window centers were used only as search seeds.

## Timing and Gaia geometry

Selecting distant dips by Gaia P=53.251724 d confuses the 1.1145 d train with the spectroscopic target orbit. No measured target-owned same-kind 53.25 d eclipse clock follows from these events. S16 is sparse and does not rescue that association.

## Source and alternate reduction

S56 TESSCut difference maximum at pixel (6,2) is displaced about two pixels from queued target WCS (3.71,3.47) and lies in the predicted direction of TIC 331643515 at (5.47,2.46). This positive spatial/clock match identifies the selected train as neighbor contamination. An IJspeert table separately has an exact queued TIC/Gaia row; that identity fact must not be conflated with ownership of this 1.1145 d train.

## Limits and next check

The selected dips are not evidence that the queued Gaia SB1 is eclipsing. The exact-target IJspeert catalogue row requires its own interpretation; this review does not refute an independent target eclipse below the contaminated signal.

Separate both sources spatially and inspect the IJspeert target row and its underlying event train.

## Provenance

`../queue.csv`, `../lead-source-hashes.json`, `../lead_context.py`, `../lead_timing.py`, `../lead-clocks.json`, `../lead-geometry.json`, helper pixel scripts/receipts/images and shared-catalogues exact target receipts form the audit trail. For current-sector additions see `../lead-current-sector-inventory.json`, `../lead-extra-sector-receipts.json`, and, for U009, `lead-new-clock.json` and `lead-alias-check.json`. Same photons in different reductions are not independent observations.
