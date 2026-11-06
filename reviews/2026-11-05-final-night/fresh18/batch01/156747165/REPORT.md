# Y009 — TIC 156747165

**Physical verdict: CONFIRMED. Bounded review: COMPLETE.** Catalogue status: NO_EXACT_MATCH_IN_CHECKED_SCOPE. Physical classification and bounded catalogue nonmatch do not themselves authorize a new-system claim; supervisor owns novelty and acceptance.

Gaia DR3 4497613271900639360; actual Gaia G=11.688592; frozen stratum repeated_discrete. Exact eight-row membership is in `../queue.csv`. The initial visual label is selection provenance, not an outcome.

## Raw event morphology

S40 and S80 contain matching deep roughly 5.5% eclipses. Separate shallow roughly 1% eclipses recur in S53 and S80. Each kind therefore repeats on distinct observing occasions; the two S80 conjunctions alone are not treated as recurrence.

| Sector | Kind | Measured BTJD | Model depth (ppt) | Contact duration (d) | Usable midpoint |
|---|---|---:|---:|---:|---|
| 40 | deep | 2392.04869 | 54.36 | 0.268 | True |
| 53 | shallow | 2763.39813 | 9.66 | 0.197 | True |
| 80 | deep | 3490.77588 | 57.18 | 0.265 | True |
| 80 | shallow | 3483.24425 | 9.63 | 0.205 | True |

Timing models are local trapezoids with a linear baseline, seeded by detector windows, fitted to finite positive quality-zero raw SAP. Reported contact durations and depths describe this approximate model, not binary-model parameters. Timing covariance is local; half-cadence floors were used in the clock. See `lead-timing.json`. Unusable fits are displayed for transparency and excluded from the clock. No opposite conjunction is used as a same-kind repeat.

## Clock and actual coverage

The deep span 1098.727193 d over 29 cycles gives 37.88714 d. The shallow span 719.846121 d over 19 cycles agrees within 0.00963 d. Neighboring integer counts fail the shallow span. A real S26 covered P/2 window at BTJD 2032.1208 has 12 quality-zero samples and -0.143 ppt deficit against 0.757 ppt scatter, excluding an extra deep event. Covered P/3 through P/6 windows similarly lack deep eclipses.

The measured adopted recurrence is 37.88714458 d, epoch BTJD 2392.04869; integer cycles [0, 29]. Formal covariance and scatter inflation are retained in `../lead-clocks.json`, but no uniform total period error is claimed in RESULTS.csv. These are bounded representative checks, not an exhaustive all-period posterior.

| Alternative | Representative actual sector | Predicted BTJD | Core samples | Coverage fraction | Median deficit (ppt) | Baseline scatter (ppt) |
|---|---:|---:|---:|---:|---:|---:|
| P/2 | 26 | 2032.12081 | 12 | 1.000 | -0.143 | 0.757 |
| P/3 | 80 | 3503.40493 | 108 | 1.000 | 0.617 | 2.750 |
| P/4 | 26 | 2032.12081 | 12 | 1.000 | -0.143 | 0.757 |
| P/5 | 80 | 3498.35331 | 108 | 1.000 | 0.250 | 2.237 |
| P/6 | 26 | 2032.12081 | 12 | 1.000 | -0.143 | 0.757 |

The full actual-cadence table is `../lead-alias-covered-windows.json`; each row records quality-zero core coverage, maximum core gap, two populated local sidebands and source hash. A missing window is not a null. Event-matched test durations are 0.55 d for Y001 and 0.25 d otherwise. Y001 uses closer uncontaminated sidebands to avoid its opposite eclipse about one day from the half-period prediction. These tests address short same-kind recurrence aliases; they do not prove every long superperiod is impossible.

## Source-specific Gaia orbit

Gaia SB1 P=37.88952707 ± 0.01155946 d; e=0.5498, omega=202.198°, T_periastron=BTJD 381.86502. Mass function f(M)=0.1129 solar masses, consistent with a stellar binary interpretation. The edge-on conjunction estimate uses this source's orbital parameters and full SB1 correlation submatrix (P,e,omega,Tp), with the epoch conversion +389 d.

| Sector | Observed BTJD | Closest conjunction kind | Offset (d) | Local covariance sigma (d) |
|---|---:|---|---:|---:|
| 40 | 2392.04869 | 1 | -0.029 | 0.619 |
| 53 | 2763.39813 | 0 | -0.590 | 0.831 |
| 80 | 3490.77588 | 1 | -0.098 | 0.953 |
| 80 | 3483.24425 | 0 | -0.645 | 1.041 |

This is fixed-cycle local linear propagation with the source-specific correlation vector, not a full nonlinear ephemeris posterior or a calibrated sigma veto. Individual coincidence does not establish orbital association for a train with a different recurrence. The complete two-conjunction numbers and source CSV hash are in `../lead-gaia-covariance.json`. No Gaia period was fixed when fitting photometric midpoints.

## Pixel attribution and alternate reduction

Representative S80 TESSCut difference flux lies near the target WCS position: descriptive positive-deficit centroid offset 0.054 pixel. The median exterior-pixel difference offset -106.331 flux units was removed before centroiding; this matters especially for Y009's uniform negative background change. The 3×3 target aperture with cadence-specific median outer-border background subtraction reproduces a 57.12 ppt median event deficit from 30 core and 173 baseline cadences. This independently written extraction reuses the same photons and is not another observing occasion.

Nearby Gaia sources in the 180 arcsec query are mapped through the cutout WCS in `../lead-source-localization.json`; `gaia-neighbors.csv` retains all retrieved rows. Closest neighbors:

| Gaia DR3 | Separation (arcsec) | G | G flux relative to target |
|---|---:|---:|---:|
| 4497613271900636928 | 8.95 | 17.46 | 0.00492 |
| 4497613271893809280 | 10.29 | 21.00 | 0.00019 |
| 4497613271892699904 | 15.48 | 20.17 | 0.00041 |
| 4497613306253252352 | 16.71 | 20.80 | 0.00023 |

G flux ratios are approximate feasibility screens, not TESS-band flux budgets. The deficit location is judged against capable neighbors and resolved background structures, not merely the brightest pixel. TESS cannot exclude all close unresolved companions.

## Completed scope, limits and next check

Deep-pair formal fit covariance has no residual degrees of freedom; no precision total period error is reported. Difference imaging needs removal of a nearly uniform background change, and close faint companions remain unresolved.

Next check: Obtain another complete deep eclipse to improve the period and resolve small QLP timing systematics.

All selected raw QLP FITS, population/download records, bulk and appointment metadata identities were checked and hashed in `../identity-audit.json`; raw event and sector coverage are in `lead-context.json`. Source identifiers were matched exactly and FITS TIC/sector headers verified. Representative images were visually inspected by the lead; helper scope is stated in `../helper-audit.md`.

Shared scoped catalogue receipts cover VSX and ASAS-SN 60 arcsec queries, Gaia EB and NSS/SIMBAD, Prša/IJspeert exact tables, full vetted Kostov tables, and the enabled Kepler EB/TOI tables. No matched prior EB is assigned to these eight in the current receipts. The bounded 244-paper identifier scan found no hits. Those successful scoped nonmatches do not establish exhaustive novelty or settle ownership of a nearby contaminant. Shared receipts live in `../../shared-catalogues/`; supervisor adjudicates novelty independently.

## Provenance

Reproducible code and numerical receipts: `../lead_context.py`, `../lead_timing.py`, `../lead_clocks.py`, `../lead_aliases.py`, `../lead_two_kinds.py`, `../lead_gaia_covariance.py`, `../lead_cuts.py`, `../lead_pixels.py`, `../lead_independent.py`, `../lead_neighbors.py`, `../lead_localization.py`, `../identity_audit.py`; corresponding JSON receipts and source file hashes. `../SHA256SUMS.json` seals this batch. No catalogue ledger or publication files were edited.
