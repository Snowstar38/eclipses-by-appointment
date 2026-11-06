# Y001 — TIC 22559994

**Physical verdict: PROBABLE. Bounded review: COMPLETE.** Catalogue status: NO_EXACT_MATCH_IN_CHECKED_SCOPE. Physical classification and bounded catalogue nonmatch do not themselves authorize a new-system claim; supervisor owns novelty and acceptance.

Gaia DR3 6131510399993965312; actual Gaia G=11.941478; frozen stratum repeated_discrete. Exact eight-row membership is in `../queue.csv`. The initial visual label is selection provenance, not an outcome.

## Raw event morphology

Four well-resolved detached eclipse profiles comprise two deep same-kind events in S64/S100 and two shallower same-kind events in S37/S101. The two kinds each recur; their alternating depth is not counted as additional same-kind recurrence. The deep profiles lose about 17-22% and the shallow profiles about 8% of local SAP flux. Sector-dependent dilution explains some depth differences but is not fitted here.

| Sector | Kind | Measured BTJD | Model depth (ppt) | Contact duration (d) | Usable midpoint |
|---|---|---:|---:|---:|---|
| 37 | shallow | 2313.76653 | 81.37 | 0.642 | True |
| 64 | deep | 3043.16141 | 217.23 | 0.565 | True |
| 100 | deep | 4079.85637 | 173.38 | 0.565 | True |
| 101 | shallow | 4104.42081 | 75.09 | 0.647 | True |

Timing models are local trapezoids with a linear baseline, seeded by detector windows, fitted to finite positive quality-zero raw SAP. Reported contact durations and depths describe this approximate model, not binary-model parameters. Timing covariance is local; half-cadence floors were used in the clock. See `lead-timing.json`. Unusable fits are displayed for transparency and excluded from the clock. No opposite conjunction is used as a same-kind repeat.

## Clock and actual coverage

The deep span is 1036.694969 d over an adopted 22 cycles; the shallow span 1790.654283 d over 38 cycles independently agrees to 0.00066 d. Neighboring integer counts for the deep pair fail the shallow span. Timing alone also permits a 94.244997 d family and shorter rational families; the bounded shorter-alias null tests reject P/2 through P/6. The 47.12 d assignment is favored by Gaia but is not a unique timing-only orbital solution.

The measured adopted recurrence is 47.12249860 d, epoch BTJD 3043.16141; integer cycles [0, 22]. Formal covariance and scatter inflation are retained in `../lead-clocks.json`, but no uniform total period error is claimed in RESULTS.csv. These are bounded representative checks, not an exhaustive all-period posterior.

| Alternative | Representative actual sector | Predicted BTJD | Core samples | Coverage fraction | Median deficit (ppt) | Baseline scatter (ppt) |
|---|---:|---:|---:|---:|---:|---:|
| P/2 | 101 | 4103.41762 | 238 | 1.002 | -0.079 | 1.569 |
| P/3 | 64 | 3058.86891 | 237 | 0.997 | 0.026 | 2.239 |
| P/4 | 101 | 4103.41762 | 238 | 1.002 | -0.079 | 1.569 |
| P/5 | 99 | 4051.58288 | 237 | 0.998 | -0.039 | 1.610 |
| P/6 | 64 | 3058.86891 | 237 | 0.997 | 0.026 | 2.239 |

The full actual-cadence table is `../lead-alias-covered-windows.json`; each row records quality-zero core coverage, maximum core gap, two populated local sidebands and source hash. A missing window is not a null. Event-matched test durations are 0.55 d for Y001 and 0.25 d otherwise. Y001 uses closer uncontaminated sidebands to avoid its opposite eclipse about one day from the half-period prediction. These tests address short same-kind recurrence aliases; they do not prove every long superperiod is impossible.

## Source-specific Gaia orbit

Gaia SB1 P=47.15156398 ± 0.01230905 d; e=0.1491, omega=249.180°, T_periastron=BTJD 402.18204. Mass function f(M)=0.1776 solar masses, consistent with a stellar binary interpretation. The edge-on conjunction estimate uses this source's orbital parameters and full SB1 correlation submatrix (P,e,omega,Tp), with the epoch conversion +389 d.

| Sector | Observed BTJD | Closest conjunction kind | Offset (d) | Local covariance sigma (d) |
|---|---:|---|---:|---:|
| 37 | 2313.76653 | 0 | -1.668 | 0.605 |
| 64 | 3043.16141 | 1 | -1.516 | 0.686 |
| 100 | 4079.85637 | 1 | -2.156 | 0.949 |
| 101 | 4104.42081 | 0 | -2.773 | 1.039 |

This is fixed-cycle local linear propagation with the source-specific correlation vector, not a full nonlinear ephemeris posterior or a calibrated sigma veto. Individual coincidence does not establish orbital association for a train with a different recurrence. The complete two-conjunction numbers and source CSV hash are in `../lead-gaia-covariance.json`. No Gaia period was fixed when fitting photometric midpoints.

## Pixel attribution and alternate reduction

Representative S64 TESSCut difference flux lies near the target WCS position: descriptive positive-deficit centroid offset 0.062 pixel. The median exterior-pixel difference offset 1.486 flux units was removed before centroiding; this matters especially for Y009's uniform negative background change. The 3×3 target aperture with cadence-specific median outer-border background subtraction reproduces a 229.57 ppt median event deficit from 69 core and 173 baseline cadences. This independently written extraction reuses the same photons and is not another observing occasion.

Nearby Gaia sources in the 180 arcsec query are mapped through the cutout WCS in `../lead-source-localization.json`; `gaia-neighbors.csv` retains all retrieved rows. Closest neighbors:

| Gaia DR3 | Separation (arcsec) | G | G flux relative to target |
|---|---:|---:|---:|
| 6131510601859448704 | 16.27 | 19.97 | 0.00061 |
| 6131510395701039616 | 17.00 | 19.32 | 0.00112 |
| 6131510606152395776 | 21.38 | 16.62 | 0.01347 |
| 6131510567495378560 | 22.45 | 19.47 | 0.00097 |

G flux ratios are approximate feasibility screens, not TESS-band flux budgets. The deficit location is judged against capable neighbors and resolved background structures, not merely the brightest pixel. TESS cannot exclude all close unresolved companions.

## Completed scope, limits and next check

Repeated target-region eclipses are secure. Gaia orbital association has persistent 2.2-2.8 local linear-sigma offsets, and a 94.245 d timing family remains. Close unresolved companions and changing dilution remain possible.

Next check: Obtain a new resolved same-kind eclipse and radial velocities; test the 47/94 d orbital alternatives and Gaia epoch geometry.

All selected raw QLP FITS, population/download records, bulk and appointment metadata identities were checked and hashed in `../identity-audit.json`; raw event and sector coverage are in `lead-context.json`. Source identifiers were matched exactly and FITS TIC/sector headers verified. Representative images were visually inspected by the lead; helper scope is stated in `../helper-audit.md`.

Shared scoped catalogue receipts cover VSX and ASAS-SN 60 arcsec queries, Gaia EB and NSS/SIMBAD, Prša/IJspeert exact tables, full vetted Kostov tables, and the enabled Kepler EB/TOI tables. No matched prior EB is assigned to these eight in the current receipts. The bounded 244-paper identifier scan found no hits. Those successful scoped nonmatches do not establish exhaustive novelty or settle ownership of a nearby contaminant. Shared receipts live in `../../shared-catalogues/`; supervisor adjudicates novelty independently.

## Provenance

Reproducible code and numerical receipts: `../lead_context.py`, `../lead_timing.py`, `../lead_clocks.py`, `../lead_aliases.py`, `../lead_two_kinds.py`, `../lead_gaia_covariance.py`, `../lead_cuts.py`, `../lead_pixels.py`, `../lead_independent.py`, `../lead_neighbors.py`, `../lead_localization.py`, `../identity_audit.py`; corresponding JSON receipts and source file hashes. `../SHA256SUMS.json` seals this batch. No catalogue ledger or publication files were edited.
