# U003 — TIC 412521418

**Physical verdict:** REFUTED (provisional lead classification). **Bounded review:** COMPLETE. **Catalogue status:** NO_EXACT_MATCH_IN_CHECKED_SCOPE; no new-system claim is made here. The shared-catalogue receipts define the checked scope.

## Raw events and coverage

The dips in S7, S34, S61, S87 and S88 sit in a repeating roughly 1.79 d train. Five independent local centers fit P=1.79159267 d, matching the cataloged EA neighbor TIC 412521403 at 30.57 arcsec and P=1.7916 d, rather than the target Gaia SB1 P=35.699912 d.

Cached QLP sector coverage: 7,34,61,87,88. Lead verified SHA256 of every used FITS and bulk-result file before measuring. `lead-context.json` contains cadence endpoints, quality-zero sample counts and flagged-window measurements; `lead-timing.json` contains local trapezoid measurements. The gallery `lead-raw-context.png` shows representative raw SAP alongside KSPSAP where present. Detector window centers were used only as search seeds.

## Timing and Gaia geometry

The repeated short-period clock is directly present in raw SAP; a long Gaia-period selection of some windows is a cadence of this neighbor train, not evidence for a 35.7 d target eclipse. The selected events have no source-specific Gaia conjunction support.

## Source and alternate reduction

The S34 TESSCut difference image peaks at the known EA neighbor position (about pixel 4.55,4.48), displaced from target WCS (3.52,3.42). The cataloged neighbor also has the matching exact short clock. This positively identifies contamination at TESS resolution.

## Limits and next check

The selected dip interpretation as a target Gaia-binary eclipse is refuted; an unrelated weak target eclipse elsewhere is not excluded. The neighbor is a cataloged EB, not a new target discovery.

If target-specific eclipses are sought, use higher-resolution photometry separated from TIC 412521403.

## Provenance

`../queue.csv`, `../lead-source-hashes.json`, `../lead_context.py`, `../lead_timing.py`, `../lead-clocks.json`, `../lead-geometry.json`, helper pixel scripts/receipts/images and shared-catalogues exact target receipts form the audit trail. For current-sector additions see `../lead-current-sector-inventory.json`, `../lead-extra-sector-receipts.json`, and, for U009, `lead-new-clock.json` and `lead-alias-check.json`. Same photons in different reductions are not independent observations.
