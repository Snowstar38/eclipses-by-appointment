# U004 — TIC 86182628

**Physical verdict:** PROBABLE (provisional lead classification). **Bounded review:** COMPLETE. **Catalogue status:** KNOWN_PRIOR_EB; no new-system claim is made here. The shared-catalogue receipts define the checked scope.

## Raw events and coverage

Two raw S22 dips at BTJD 1909.499 and 1922.893 recur in S49 at 2648.641 and 2662.034, respectively, with stable narrow morphology and about 23/29 ppt fitted depths. Each sector supplies both conjunction-like kinds; the separation repeats at 13.39 d. The two deep centers differ by 739.141 d.

Cached QLP sector coverage: 22,49. Lead verified SHA256 of every used FITS and bulk-result file before measuring. `lead-context.json` contains cadence endpoints, quality-zero sample counts and flagged-window measurements; `lead-timing.json` contains local trapezoid measurements. The gallery `lead-raw-context.png` shows representative raw SAP alongside KSPSAP where present. Detector window centers were used only as search seeds.

## Timing and Gaia geometry

A conditional 25-cycle assignment gives P=29.56564 d, near Gaia SB1 P=29.54222 d. Other integers remain possible over the 739 d gap with only two observed sectors; therefore no adopted photometric period or precision error is reported. PRSA lists exact TIC 86182628 as an eclipsing-binary recovery with one-sector P=26.543965±0.200737 d, which is inconsistent with the conditional 25-cycle value and is not silently adopted. The source-specific edge-on Gaia conjunction differs by about 1.27 d from S22 deep center; the simple accumulated formal-period allowance is 0.79 d and full covariance remains untested.

## Source and alternate reduction

S22/S49 raw SAP and corrected light curves retain the dips. TESSCut difference peaks near the target WCS pixel. This supports target-region source but not unique ownership against unresolved blends.

## Limits and next check

Real repeating two-kind eclipses are supported; exact cycle count and Gaia orbital association remain unresolved. Exact TIC is a known PRSA EB recovery, independent of this physical-period uncertainty.

Obtain an intervening or newer event to eliminate integer aliases and refine Gaia conjunction timing.

## Provenance

`../queue.csv`, `../lead-source-hashes.json`, `../lead_context.py`, `../lead_timing.py`, `../lead-clocks.json`, `../lead-geometry.json`, helper pixel scripts/receipts/images and shared-catalogues exact target receipts form the audit trail. For current-sector additions see `../lead-current-sector-inventory.json`, `../lead-extra-sector-receipts.json`, and, for U009, `lead-new-clock.json` and `lead-alias-check.json`. Same photons in different reductions are not independent observations.
