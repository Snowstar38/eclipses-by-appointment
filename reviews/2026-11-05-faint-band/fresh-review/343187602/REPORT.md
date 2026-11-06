# U008 — TIC 343187602

**Physical verdict:** PLAUSIBLE (provisional lead classification). **Bounded review:** COMPLETE. **Catalogue status:** NO_EXACT_MATCH_IN_CHECKED_SCOPE; no new-system claim is made here. The shared-catalogue receipts define the checked scope.

## Raw events and coverage

S24 shows one compact raw SAP depression near BTJD 1970.103, fitted about 21 ppt, with rapid recovery and a post-event overshoot. Other QLP sectors S16/S17/S57/S77/S83/S84 do not show a securely matching same-kind event. The S24 dip remains a singular candidate.

Cached QLP sector coverage: 16,17,24,57,77,83,84. Lead verified SHA256 of every used FITS and bulk-result file before measuring. `lead-context.json` contains cadence endpoints, quality-zero sample counts and flagged-window measurements; `lead-timing.json` contains local trapezoid measurements. The gallery `lead-raw-context.png` shows representative raw SAP alongside KSPSAP where present. Detector window centers were used only as search seeds.

## Timing and Gaia geometry

At Gaia P=50.60815 d, a predicted S17 core at 1767.670 has 6/6 nominal 30-minute cadences, baseline 12+11 and median depth 0.1 ppt; S84 at 3589.564 has 51/52 core cadences and 0.3 ppt. These are local nulls at the nominal epoch, not phase-wide exclusions: Gaia period error 0.10017 d accumulates to about 0.4 d at S17 and 3.2 d at S84. The current TESSCut inventory adds S76 to the frozen QLP sectors, but its 5x5 target-region net flux is only about 0.4 e/s, so it is not a sensitive null.

## Source and alternate reduction

S24 difference imagery is dominated by an approximately 30 e/s common background offset, preventing reliable pixel localization in the bounded cut. SAP and KSPSAP show the same photons, with the post-event overshoot requiring caution.

## Limits and next check

One event with uncertain source and possible reduction/systematic alternative; recurrence and Gaia orbital link are unproven.

Acquire a second uninterrupted event and a valid target-flux cutout for localization.

## Provenance

`../queue.csv`, `../lead-source-hashes.json`, `../lead_context.py`, `../lead_timing.py`, `../lead-clocks.json`, `../lead-geometry.json`, helper pixel scripts/receipts/images and shared-catalogues exact target receipts form the audit trail. For current-sector additions see `../lead-current-sector-inventory.json`, `../lead-extra-sector-receipts.json`, and, for U009, `lead-new-clock.json` and `lead-alias-check.json`. Same photons in different reductions are not independent observations.
