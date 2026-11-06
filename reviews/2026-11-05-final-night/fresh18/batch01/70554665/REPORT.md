# Y003 — TIC 70554665

**Physical verdict: CONFIRMED. Bounded review: COMPLETE.** Catalogue status: NO_EXACT_MATCH_IN_CHECKED_SCOPE. Physical classification and bounded catalogue nonmatch do not themselves authorize a new-system claim; supervisor owns novelty and acceptance.

Gaia DR3 4970149490807806720; actual Gaia G=11.9121; frozen stratum repeated_discrete. Exact eight-row membership is in `../queue.csv`. The initial visual label is selection provenance, not an outcome.

## Raw event morphology

Three compact matching approximately 1% dips occur in S97 (two adjacent occurrences) and S104. Contacts and both wings are resolved; S104 has less distant post-event coverage but retains immediate recovery.

| Sector | Kind | Measured BTJD | Model depth (ppt) | Contact duration (d) | Usable midpoint |
|---|---|---:|---:|---:|---|
| 97 | candidate | 3939.52294 | 9.76 | 0.222 | True |
| 97 | candidate | 3968.94746 | 9.43 | 0.232 | True |
| 104 | candidate | 4204.32569 | 10.19 | 0.223 | True |

Timing models are local trapezoids with a linear baseline, seeded by detector windows, fitted to finite positive quality-zero raw SAP. Reported contact durations and depths describe this approximate model, not binary-model parameters. Timing covariance is local; half-cadence floors were used in the clock. See `lead-timing.json`. Unusable fits are displayed for transparency and excluded from the clock. No opposite conjunction is used as a same-kind repeat.

## Clock and actual coverage

Two S97 events separated by 29.4245 d directly anchor adjacent recurrence. The S104 event lies nine adopted cycles after the first. A measured 29.4224 d clock has 0.00086 d unweighted residual RMS. Representative covered P/2 through P/6 predicted events have no comparable deficit.

The measured adopted recurrence is 29.42241330 d, epoch BTJD 3939.52403; integer cycles [0, 1, 9]. Formal covariance and scatter inflation are retained in `../lead-clocks.json`, but no uniform total period error is claimed in RESULTS.csv. These are bounded representative checks, not an exhaustive all-period posterior.

| Alternative | Representative actual sector | Predicted BTJD | Core samples | Coverage fraction | Median deficit (ppt) | Baseline scatter (ppt) |
|---|---:|---:|---:|---:|---:|---:|
| P/2 | 104 | 4189.61455 | 97 | 0.898 | 0.126 | 1.674 |
| P/3 | 3 | 1399.38902 | 12 | 1.000 | 0.009 | 0.483 |
| P/4 | 30 | 2122.69001 | 35 | 0.972 | -0.026 | 1.098 |
| P/5 | 3 | 1391.54304 | 11 | 0.917 | -0.061 | 0.461 |
| P/6 | 3 | 1399.38902 | 12 | 1.000 | 0.009 | 0.483 |

The full actual-cadence table is `../lead-alias-covered-windows.json`; each row records quality-zero core coverage, maximum core gap, two populated local sidebands and source hash. A missing window is not a null. Event-matched test durations are 0.55 d for Y001 and 0.25 d otherwise. Y001 uses closer uncontaminated sidebands to avoid its opposite eclipse about one day from the half-period prediction. These tests address short same-kind recurrence aliases; they do not prove every long superperiod is impossible.

## Source-specific Gaia orbit

Gaia SB1 P=29.42798069 ± 0.03254426 d; e=0.0686, omega=89.562°, T_periastron=BTJD 379.49408. Mass function f(M)=0.0014 solar masses, consistent with a stellar binary interpretation. The edge-on conjunction estimate uses this source's orbital parameters and full SB1 correlation submatrix (P,e,omega,Tp), with the epoch conversion +389 d.

| Sector | Observed BTJD | Closest conjunction kind | Offset (d) | Local covariance sigma (d) |
|---|---:|---|---:|---:|
| 97 | 3939.52294 | 0 | -0.788 | 3.512 |
| 97 | 3968.94746 | 0 | -0.791 | 3.545 |
| 104 | 4204.32569 | 0 | -0.837 | 3.803 |

This is fixed-cycle local linear propagation with the source-specific correlation vector, not a full nonlinear ephemeris posterior or a calibrated sigma veto. Individual coincidence does not establish orbital association for a train with a different recurrence. The complete two-conjunction numbers and source CSV hash are in `../lead-gaia-covariance.json`. No Gaia period was fixed when fitting photometric midpoints.

## Pixel attribution and alternate reduction

Representative S97 TESSCut difference flux lies near the target WCS position: descriptive positive-deficit centroid offset 0.163 pixel. The median exterior-pixel difference offset 0.201 flux units was removed before centroiding; this matters especially for Y009's uniform negative background change. The 3×3 target aperture with cadence-specific median outer-border background subtraction reproduces a 10.50 ppt median event deficit from 30 core and 173 baseline cadences. This independently written extraction reuses the same photons and is not another observing occasion.

Nearby Gaia sources in the 180 arcsec query are mapped through the cutout WCS in `../lead-source-localization.json`; `gaia-neighbors.csv` retains all retrieved rows. Closest neighbors:

| Gaia DR3 | Separation (arcsec) | G | G flux relative to target |
|---|---:|---:|---:|
| 4970149486510330240 | 14.34 | 18.82 | 0.00172 |
| 4970149555229809664 | 38.92 | 18.45 | 0.00242 |
| 4970149559524872576 | 41.91 | 20.43 | 0.00039 |
| 4970149525168007296 | 50.36 | 20.94 | 0.00024 |

G flux ratios are approximate feasibility screens, not TESS-band flux budgets. The deficit location is judged against capable neighbors and resolved background structures, not merely the brightest pixel. TESS cannot exclude all close unresolved companions.

## Completed scope, limits and next check

QLP timing model is approximate and same-photon independent extraction retains spacecraft background trends. No calibrated system-wide period uncertainty or unresolved-companion exclusion is claimed.

Next check: Obtain a further eclipse with independent observing equipment and refine the ephemeris.

All selected raw QLP FITS, population/download records, bulk and appointment metadata identities were checked and hashed in `../identity-audit.json`; raw event and sector coverage are in `lead-context.json`. Source identifiers were matched exactly and FITS TIC/sector headers verified. Representative images were visually inspected by the lead; helper scope is stated in `../helper-audit.md`.

Shared scoped catalogue receipts cover VSX and ASAS-SN 60 arcsec queries, Gaia EB and NSS/SIMBAD, Prša/IJspeert exact tables, full vetted Kostov tables, and the enabled Kepler EB/TOI tables. No matched prior EB is assigned to these eight in the current receipts. The bounded 244-paper identifier scan found no hits. Those successful scoped nonmatches do not establish exhaustive novelty or settle ownership of a nearby contaminant. Shared receipts live in `../../shared-catalogues/`; supervisor adjudicates novelty independently.

## Provenance

Reproducible code and numerical receipts: `../lead_context.py`, `../lead_timing.py`, `../lead_clocks.py`, `../lead_aliases.py`, `../lead_two_kinds.py`, `../lead_gaia_covariance.py`, `../lead_cuts.py`, `../lead_pixels.py`, `../lead_independent.py`, `../lead_neighbors.py`, `../lead_localization.py`, `../identity_audit.py`; corresponding JSON receipts and source file hashes. `../SHA256SUMS.json` seals this batch. No catalogue ledger or publication files were edited.
