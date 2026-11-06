# Y004 — TIC 93330962

**Physical verdict: PLAUSIBLE. Bounded review: COMPLETE.** Catalogue status: NO_EXACT_MATCH_IN_CHECKED_SCOPE. Physical classification and bounded catalogue nonmatch do not themselves authorize a new-system claim; supervisor owns novelty and acceptance.

Gaia DR3 2915827050713497216; actual Gaia G=11.941597; frozen stratum repeated_discrete. Exact eight-row membership is in `../queue.csv`. The initial visual label is selection provenance, not an outcome.

## Raw event morphology

A narrow S32 dip at BTJD 2184.092 is supported by raw SAP and a separately extracted aperture. The nominal S98 lead instead lies in broad orbit-scale detector/baseline structure and does not provide a matching resolved repeat. S87 is a broad background disturbance.

| Sector | Kind | Measured BTJD | Model depth (ppt) | Contact duration (d) | Usable midpoint |
|---|---|---:|---:|---:|---|
| 32 | candidate | 2184.09238 | 4.74 | 0.291 | True |
| 98 | candidate | 4016.05292 | 0.66 | 0.355 | False |

Timing models are local trapezoids with a linear baseline, seeded by detector windows, fitted to finite positive quality-zero raw SAP. Reported contact durations and depths describe this approximate model, not binary-model parameters. Timing covariance is local; half-cadence floors were used in the clock. See `lead-timing.json`. Unusable fits are displayed for transparency and excluded from the clock. No opposite conjunction is used as a same-kind repeat.

## Clock and actual coverage

Only one credible narrow eclipse-like event is retained. Its source-specific Gaia conjunction offset is about 0.82 d against a 0.75 d local covariance uncertainty, which is compatible but cannot establish recurrence. No photometric period or error is reported.

No recurring photometric clock is established, so no alias table is presented as a period test. The live sector inventory and S107–S109 cutout receipts document the new-sector check. S107 is a failed sensitive data product, not a covered null.

## Source-specific Gaia orbit

Gaia SB1 P=46.04865711 ± 0.01940440 d; e=0.5297, omega=314.555°, T_periastron=BTJD 388.96920. Mass function f(M)=0.0293 solar masses, consistent with a stellar binary interpretation. The edge-on conjunction estimate uses this source's orbital parameters and full SB1 correlation submatrix (P,e,omega,Tp), with the epoch conversion +389 d.

| Sector | Observed BTJD | Closest conjunction kind | Offset (d) | Local covariance sigma (d) |
|---|---:|---|---:|---:|
| 32 | 2184.09238 | 1 | 0.822 | 0.746 |

This is fixed-cycle local linear propagation with the source-specific correlation vector, not a full nonlinear ephemeris posterior or a calibrated sigma veto. Individual coincidence does not establish orbital association for a train with a different recurrence. The complete two-conjunction numbers and source CSV hash are in `../lead-gaia-covariance.json`. No Gaia period was fixed when fitting photometric midpoints.

## Pixel attribution and alternate reduction

Representative S32 TESSCut difference flux lies near the target WCS position: descriptive positive-deficit centroid offset 0.263 pixel. The median exterior-pixel difference offset 0.125 flux units was removed before centroiding; this matters especially for Y009's uniform negative background change. The 3×3 target aperture with cadence-specific median outer-border background subtraction reproduces a 6.18 ppt median event deficit from 10 core and 57 baseline cadences. This independently written extraction reuses the same photons and is not another observing occasion.

Nearby Gaia sources in the 180 arcsec query are mapped through the cutout WCS in `../lead-source-localization.json`; `gaia-neighbors.csv` retains all retrieved rows. Closest neighbors:

| Gaia DR3 | Separation (arcsec) | G | G flux relative to target |
|---|---:|---:|---:|
| 2915821175198237568 | 14.78 | 17.11 | 0.00859 |
| 2915826840256411648 | 23.55 | 20.31 | 0.00045 |
| 2915827046414440960 | 23.64 | 19.56 | 0.00090 |
| 2915821175198239360 | 29.10 | 17.62 | 0.00535 |

G flux ratios are approximate feasibility screens, not TESS-band flux budgets. The deficit location is judged against capable neighbors and resolved background structures, not merely the brightest pixel. TESS cannot exclude all close unresolved companions.

## Completed scope, limits and next check

Single event; no established same-kind recurrence. Source attribution is less precise than for deep events. New S107 cutout has near-zero/no-stellar-PSF data and cannot act as a sensitive null. S108/S109 contain broad spacecraft-shaped variability; no convincing narrow repeat is established.

Next check: Obtain a second complete narrow dip with source localization, then test integer cycles with actual coverage.

All selected raw QLP FITS, population/download records, bulk and appointment metadata identities were checked and hashed in `../identity-audit.json`; raw event and sector coverage are in `lead-context.json`. Source identifiers were matched exactly and FITS TIC/sector headers verified. Representative images were visually inspected by the lead; helper scope is stated in `../helper-audit.md`.

Shared scoped catalogue receipts cover VSX and ASAS-SN 60 arcsec queries, Gaia EB and NSS/SIMBAD, Prša/IJspeert exact tables, full vetted Kostov tables, and the enabled Kepler EB/TOI tables. No matched prior EB is assigned to these eight in the current receipts. The bounded 244-paper identifier scan found no hits. Those successful scoped nonmatches do not establish exhaustive novelty or settle ownership of a nearby contaminant. Shared receipts live in `../../shared-catalogues/`; supervisor adjudicates novelty independently.

## Provenance

Reproducible code and numerical receipts: `../lead_context.py`, `../lead_timing.py`, `../lead_clocks.py`, `../lead_aliases.py`, `../lead_two_kinds.py`, `../lead_gaia_covariance.py`, `../lead_cuts.py`, `../lead_pixels.py`, `../lead_independent.py`, `../lead_neighbors.py`, `../lead_localization.py`, `../identity_audit.py`; corresponding JSON receipts and source file hashes. `../SHA256SUMS.json` seals this batch. No catalogue ledger or publication files were edited.
