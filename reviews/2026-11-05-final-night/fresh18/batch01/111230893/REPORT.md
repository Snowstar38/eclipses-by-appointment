# Y005 — TIC 111230893

**Physical verdict: CONFIRMED. Bounded review: COMPLETE.** Catalogue status: NO_EXACT_MATCH_IN_CHECKED_SCOPE. Physical classification and bounded catalogue nonmatch do not themselves authorize a new-system claim; supervisor owns novelty and acceptance.

Gaia DR3 5604949883412428032; actual Gaia G=11.949298; frozen stratum repeated_discrete. Exact eight-row membership is in `../queue.csv`. The initial visual label is selection provenance, not an outcome.

## Raw event morphology

S34, S61 and S87 show matching flat-bottom/steep-contact approximately 6% dips with resolved wings. S88 contains a partial fourth event cut by a gap and is retained as corroboration, not as a fitted midpoint.

| Sector | Kind | Measured BTJD | Model depth (ppt) | Contact duration (d) | Usable midpoint |
|---|---|---:|---:|---:|---|
| 34 | candidate | 2243.28767 | 59.48 | 0.166 | True |
| 61 | candidate | 2980.89425 | 61.84 | 0.168 | True |
| 87 | candidate | 3675.11065 | 54.04 | 0.169 | True |
| 88 | candidate | 3696.85443 | 104.98 | 0.262 | False |

Timing models are local trapezoids with a linear baseline, seeded by detector windows, fitted to finite positive quality-zero raw SAP. Reported contact durations and depths describe this approximate model, not binary-model parameters. Timing covariance is local; half-cadence floors were used in the clock. See `lead-timing.json`. Unusable fits are displayed for transparency and excluded from the clock. No opposite conjunction is used as a same-kind repeat.

## Clock and actual coverage

Three complete same-kind events span 34 and 66 cycles at 21.69427 d; unweighted timing residual RMS is 0.00054 d. The adopted cycle clock matches source-specific Gaia conjunction evolution. Covered P/2 through P/6 windows contain no comparable eclipse.

The measured adopted recurrence is 21.69427377 d, epoch BTJD 2243.28871; integer cycles [0, 34, 66]. Formal covariance and scatter inflation are retained in `../lead-clocks.json`, but no uniform total period error is claimed in RESULTS.csv. These are bounded representative checks, not an exhaustive all-period posterior.

| Alternative | Representative actual sector | Predicted BTJD | Core samples | Coverage fraction | Median deficit (ppt) | Baseline scatter (ppt) |
|---|---:|---:|---:|---:|---:|---:|
| P/2 | 61 | 2970.04688 | 108 | 1.000 | -0.037 | 2.216 |
| P/3 | 87 | 3667.87935 | 108 | 1.000 | -0.070 | 2.090 |
| P/4 | 61 | 2970.04688 | 108 | 1.000 | -0.037 | 2.216 |
| P/5 | 87 | 3670.77192 | 108 | 1.000 | 0.018 | 2.398 |
| P/6 | 88 | 3693.18934 | 108 | 1.000 | 0.002 | 2.676 |

The full actual-cadence table is `../lead-alias-covered-windows.json`; each row records quality-zero core coverage, maximum core gap, two populated local sidebands and source hash. A missing window is not a null. Event-matched test durations are 0.55 d for Y001 and 0.25 d otherwise. Y001 uses closer uncontaminated sidebands to avoid its opposite eclipse about one day from the half-period prediction. These tests address short same-kind recurrence aliases; they do not prove every long superperiod is impossible.

## Source-specific Gaia orbit

Gaia SB1 P=21.69972860 ± 0.00657434 d; e=0.3631, omega=119.666°, T_periastron=BTJD 378.25802. Mass function f(M)=0.1163 solar masses, consistent with a stellar binary interpretation. The edge-on conjunction estimate uses this source's orbital parameters and full SB1 correlation submatrix (P,e,omega,Tp), with the epoch conversion +389 d.

| Sector | Observed BTJD | Closest conjunction kind | Offset (d) | Local covariance sigma (d) |
|---|---:|---|---:|---:|
| 34 | 2243.28767 | 0 | -0.350 | 0.538 |
| 61 | 2980.89425 | 0 | -0.534 | 0.753 |
| 87 | 3675.11065 | 0 | -0.709 | 0.958 |

This is fixed-cycle local linear propagation with the source-specific correlation vector, not a full nonlinear ephemeris posterior or a calibrated sigma veto. Individual coincidence does not establish orbital association for a train with a different recurrence. The complete two-conjunction numbers and source CSV hash are in `../lead-gaia-covariance.json`. No Gaia period was fixed when fitting photometric midpoints.

## Pixel attribution and alternate reduction

Representative S61 TESSCut difference flux lies near the target WCS position: descriptive positive-deficit centroid offset 0.081 pixel. The median exterior-pixel difference offset 0.526 flux units was removed before centroiding; this matters especially for Y009's uniform negative background change. The 3×3 target aperture with cadence-specific median outer-border background subtraction reproduces a 62.42 ppt median event deficit from 30 core and 173 baseline cadences. This independently written extraction reuses the same photons and is not another observing occasion.

Nearby Gaia sources in the 180 arcsec query are mapped through the cutout WCS in `../lead-source-localization.json`; `gaia-neighbors.csv` retains all retrieved rows. Closest neighbors:

| Gaia DR3 | Separation (arcsec) | G | G flux relative to target |
|---|---:|---:|---:|
| 5604949814689919360 | 13.33 | 19.41 | 0.00103 |
| 5604949883409397504 | 17.15 | 19.14 | 0.00133 |
| 5604949814690405120 | 17.65 | 21.07 | 0.00022 |
| 5604949883405116032 | 20.36 | 19.34 | 0.00110 |

G flux ratios are approximate feasibility screens, not TESS-band flux budgets. The deficit location is judged against capable neighbors and resolved background structures, not merely the brightest pixel. TESS cannot exclude all close unresolved companions.

## Completed scope, limits and next check

The partial S88 event supplies no usable midpoint. Epoch-dependent instrumental timing offsets and dilution are not precision-calibrated.

Next check: Measure another complete eclipse and refine the orbital ephemeris with radial velocities.

All selected raw QLP FITS, population/download records, bulk and appointment metadata identities were checked and hashed in `../identity-audit.json`; raw event and sector coverage are in `lead-context.json`. Source identifiers were matched exactly and FITS TIC/sector headers verified. Representative images were visually inspected by the lead; helper scope is stated in `../helper-audit.md`.

Shared scoped catalogue receipts cover VSX and ASAS-SN 60 arcsec queries, Gaia EB and NSS/SIMBAD, Prša/IJspeert exact tables, full vetted Kostov tables, and the enabled Kepler EB/TOI tables. No matched prior EB is assigned to these eight in the current receipts. The bounded 244-paper identifier scan found no hits. Those successful scoped nonmatches do not establish exhaustive novelty or settle ownership of a nearby contaminant. Shared receipts live in `../../shared-catalogues/`; supervisor adjudicates novelty independently.

## Provenance

Reproducible code and numerical receipts: `../lead_context.py`, `../lead_timing.py`, `../lead_clocks.py`, `../lead_aliases.py`, `../lead_two_kinds.py`, `../lead_gaia_covariance.py`, `../lead_cuts.py`, `../lead_pixels.py`, `../lead_independent.py`, `../lead_neighbors.py`, `../lead_localization.py`, `../identity_audit.py`; corresponding JSON receipts and source file hashes. `../SHA256SUMS.json` seals this batch. No catalogue ledger or publication files were edited.
