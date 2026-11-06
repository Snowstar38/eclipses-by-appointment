# Y008 — TIC 140777703

**Physical verdict: CONFIRMED. Bounded review: COMPLETE.** Catalogue status: NO_EXACT_MATCH_IN_CHECKED_SCOPE. Physical classification and bounded catalogue nonmatch do not themselves authorize a new-system claim; supervisor owns novelty and acceptance.

Gaia DR3 552205598812022400; actual Gaia G=11.923841; frozen stratum repeated_discrete. Exact eight-row membership is in `../queue.csv`. The initial visual label is selection provenance, not an outcome.

## Raw event morphology

Eight sectors contain compact matching dips, including densely sampled S53/S59/S60/S73/S79/S86 occurrences. The S19/S25 samples are sparse and carry a cadence floor rather than precision weight. Modern event depths are approximately 1.2%.

| Sector | Kind | Measured BTJD | Model depth (ppt) | Contact duration (d) | Usable midpoint |
|---|---|---:|---:|---:|---|
| 19 | candidate | 1839.79748 | 6.91 | 0.282 | True |
| 25 | candidate | 1990.14396 | 15.40 | 0.166 | True |
| 53 | candidate | 2767.24898 | 11.67 | 0.163 | True |
| 59 | candidate | 2917.66023 | 11.40 | 0.160 | True |
| 60 | candidate | 2942.72336 | 12.61 | 0.168 | True |
| 73 | candidate | 3293.67111 | 12.12 | 0.160 | True |
| 79 | candidate | 3469.14192 | 12.78 | 0.173 | True |
| 86 | candidate | 3644.61834 | 12.01 | 0.163 | True |

Timing models are local trapezoids with a linear baseline, seeded by detector windows, fitted to finite positive quality-zero raw SAP. Reported contact durations and depths describe this approximate model, not binary-model parameters. Timing covariance is local; half-cadence floors were used in the clock. See `lead-timing.json`. Unusable fits are displayed for transparency and excluded from the clock. No opposite conjunction is used as a same-kind repeat.

## Clock and actual coverage

A 25.0675 d same-kind clock fits eight representative occurrences across 72 cycles. Residual RMS 0.016 d reflects the older sparse sampling and is not converted into an unwarranted uniform period error. Covered P/2 through P/6 windows exclude comparable short-alias eclipses.

The measured adopted recurrence is 25.06751514 d, epoch BTJD 1839.75531; integer cycles [0, 6, 37, 43, 44, 58, 65, 72]. Formal covariance and scatter inflation are retained in `../lead-clocks.json`, but no uniform total period error is claimed in RESULTS.csv. These are bounded representative checks, not an exhaustive all-period posterior.

| Alternative | Representative actual sector | Predicted BTJD | Core samples | Coverage fraction | Median deficit (ppt) | Baseline scatter (ppt) |
|---|---:|---:|---:|---:|---:|---:|
| P/2 | 53 | 2754.71962 | 36 | 1.000 | 0.282 | 1.155 |
| P/3 | 19 | 1823.04364 | 12 | 1.000 | -0.018 | 0.504 |
| P/4 | 53 | 2748.45274 | 36 | 1.000 | -0.012 | 1.661 |
| P/5 | 73 | 3308.71170 | 108 | 1.000 | -0.049 | 1.984 |
| P/6 | 60 | 2946.90390 | 108 | 1.000 | 0.014 | 1.762 |

The full actual-cadence table is `../lead-alias-covered-windows.json`; each row records quality-zero core coverage, maximum core gap, two populated local sidebands and source hash. A missing window is not a null. Event-matched test durations are 0.55 d for Y001 and 0.25 d otherwise. Y001 uses closer uncontaminated sidebands to avoid its opposite eclipse about one day from the half-period prediction. These tests address short same-kind recurrence aliases; they do not prove every long superperiod is impossible.

## Source-specific Gaia orbit

Gaia SB1 P=25.05892690 ± 0.01896635 d; e=0.4745, omega=265.917°, T_periastron=BTJD 387.17523. Mass function f(M)=0.0521 solar masses, consistent with a stellar binary interpretation. The edge-on conjunction estimate uses this source's orbital parameters and full SB1 correlation submatrix (P,e,omega,Tp), with the epoch conversion +389 d.

| Sector | Observed BTJD | Closest conjunction kind | Offset (d) | Local covariance sigma (d) |
|---|---:|---|---:|---:|
| 19 | 1839.79748 | 1 | -0.885 | 1.444 |
| 25 | 1990.14396 | 1 | -0.892 | 1.535 |
| 53 | 2767.24898 | 1 | -0.614 | 2.043 |
| 59 | 2917.66023 | 1 | -0.556 | 2.145 |
| 60 | 2942.72336 | 1 | -0.552 | 2.163 |
| 73 | 3293.67111 | 1 | -0.429 | 2.407 |
| 79 | 3469.14192 | 1 | -0.371 | 2.531 |
| 86 | 3644.61834 | 1 | -0.307 | 2.656 |

This is fixed-cycle local linear propagation with the source-specific correlation vector, not a full nonlinear ephemeris posterior or a calibrated sigma veto. Individual coincidence does not establish orbital association for a train with a different recurrence. The complete two-conjunction numbers and source CSV hash are in `../lead-gaia-covariance.json`. No Gaia period was fixed when fitting photometric midpoints.

## Pixel attribution and alternate reduction

Representative S59 TESSCut difference flux lies near the target WCS position: descriptive positive-deficit centroid offset 0.129 pixel. The median exterior-pixel difference offset 0.071 flux units was removed before centroiding; this matters especially for Y009's uniform negative background change. The 3×3 target aperture with cadence-specific median outer-border background subtraction reproduces a 10.99 ppt median event deficit from 30 core and 173 baseline cadences. This independently written extraction reuses the same photons and is not another observing occasion.

Nearby Gaia sources in the 180 arcsec query are mapped through the cutout WCS in `../lead-source-localization.json`; `gaia-neighbors.csv` retains all retrieved rows. Closest neighbors:

| Gaia DR3 | Separation (arcsec) | G | G flux relative to target |
|---|---:|---:|---:|
| 552205594514694400 | 8.45 | 19.14 | 0.00130 |
| 552205598809166848 | 9.87 | 18.35 | 0.00269 |
| 552205594514539904 | 25.74 | 19.41 | 0.00102 |
| 552205800672972032 | 32.69 | 19.56 | 0.00088 |

G flux ratios are approximate feasibility screens, not TESS-band flux budgets. The deficit location is judged against capable neighbors and resolved background structures, not merely the brightest pixel. TESS cannot exclude all close unresolved companions.

## Completed scope, limits and next check

Two unresolved close Gaia neighbors are faint in G-band, but color-dependent dilution is not measured. TESSCut aperture background artifacts away from the eclipse remain; they do not replace the raw-SAP event evidence.

Next check: Obtain a complete high-resolution eclipse and improve the ephemeris using the dense modern events.

All selected raw QLP FITS, population/download records, bulk and appointment metadata identities were checked and hashed in `../identity-audit.json`; raw event and sector coverage are in `lead-context.json`. Source identifiers were matched exactly and FITS TIC/sector headers verified. Representative images were visually inspected by the lead; helper scope is stated in `../helper-audit.md`.

Shared scoped catalogue receipts cover VSX and ASAS-SN 60 arcsec queries, Gaia EB and NSS/SIMBAD, Prša/IJspeert exact tables, full vetted Kostov tables, and the enabled Kepler EB/TOI tables. No matched prior EB is assigned to these eight in the current receipts. The bounded 244-paper identifier scan found no hits. Those successful scoped nonmatches do not establish exhaustive novelty or settle ownership of a nearby contaminant. Shared receipts live in `../../shared-catalogues/`; supervisor adjudicates novelty independently.

## Provenance

Reproducible code and numerical receipts: `../lead_context.py`, `../lead_timing.py`, `../lead_clocks.py`, `../lead_aliases.py`, `../lead_two_kinds.py`, `../lead_gaia_covariance.py`, `../lead_cuts.py`, `../lead_pixels.py`, `../lead_independent.py`, `../lead_neighbors.py`, `../lead_localization.py`, `../identity_audit.py`; corresponding JSON receipts and source file hashes. `../SHA256SUMS.json` seals this batch. No catalogue ledger or publication files were edited.
