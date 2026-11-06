# U001 — TIC 259614821

**Physical verdict:** PROBABLE (provisional lead classification). **Bounded review:** COMPLETE. **Catalogue status:** NO_EXACT_MATCH_IN_CHECKED_SCOPE; no new-system claim is made here. The shared-catalogue receipts define the checked scope.

## Raw events and coverage

Seven fitted deep same-kind events in S38, S39, S65, S100, S101 and S102 have resolved symmetric contacts, with additional shallower dips offset by about 8 d. Raw SAP minima are 20–29% below local baseline. S38 and S39 contain adjacent orbital occurrences, anchoring the cycle directly; the seven-event fit has P=23.2081746 d and 0.00093 d unweighted timing residual RMS. The S12 near-edge feature is partial and was excluded from the clock.

Cached QLP sector coverage: 12,38,39,65,99,100,101,102. Lead verified SHA256 of every used FITS and bulk-result file before measuring. `lead-context.json` contains cadence endpoints, quality-zero sample counts and flagged-window measurements; `lead-timing.json` contains local trapezoid measurements. The gallery `lead-raw-context.png` shows representative raw SAP alongside KSPSAP where present. Detector window centers were used only as search seeds.

## Timing and Gaia geometry

A half-period alias predicts an extra deep event in S38 at BTJD 2351.113 between observed S38/S39 occurrences. That actual S38 core has 36 quality-zero points, local baselines and -0.8 ppt median deficit versus about 275 ppt at the eclipse. The photometric period differs from Gaia SB1 P=23.2464098±0.0116866 d by 0.0382 d. An edge-on Gaia conjunction estimate is offset by -0.0973 phase at the fitted S38 epoch; the simple period-accumulation allowance alone is 0.97 d and full covariance is not available here. Thus the photometric binary is real, but tying this clock to the Gaia SB1 orbit is not secure.

## Source and alternate reduction

S38 TESSCut difference flux peaks on the target WCS pixel with positive target-region baseline; this supports target-region origin at TESS resolution. SAP and KSPSAP preserve the principal dip; the helper pixel aperture is an alternate reduction of the same photons. Close unresolved blends are not excluded.

## Limits and next check

Gaia orbital association and close-source ownership remain unresolved. Catalogue novelty is separately assessed by the shared catalogue worker.

Obtain spatially resolved eclipse photometry and a covariance-aware Gaia conjunction comparison.

## Provenance

`../queue.csv`, `../lead-source-hashes.json`, `../lead_context.py`, `../lead_timing.py`, `../lead-clocks.json`, `../lead-geometry.json`, helper pixel scripts/receipts/images and shared-catalogues exact target receipts form the audit trail. For current-sector additions see `../lead-current-sector-inventory.json`, `../lead-extra-sector-receipts.json`, and, for U009, `lead-new-clock.json` and `lead-alias-check.json`. Same photons in different reductions are not independent observations.
