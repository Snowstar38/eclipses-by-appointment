# Y002 — TIC 65684549

**Physical verdict: PROBABLE. Bounded review: COMPLETE.** Catalogue status: NO_EXACT_MATCH_IN_CHECKED_SCOPE. Physical classification and bounded catalogue nonmatch do not themselves authorize a new-system claim; supervisor owns novelty and acceptance.

Gaia DR3 476202682178968832; actual Gaia G=11.981233; frozen stratum repeated_discrete. Exact eight-row membership is in `../queue.csv`. The initial visual label is selection provenance, not an outcome.

## Raw event morphology

A train of compact resolved dips repeats throughout S59, S73 and S86, separated by approximately 1.137 d. Individual depths change with sector and baseline quality. These are discrete contact-shaped deficits rather than a smooth tidal wave.

| Sector | Kind | Measured BTJD | Model depth (ppt) | Contact duration (d) | Usable midpoint |
|---|---|---:|---:|---:|---|
| 59 | candidate | 2935.35819 | 26.49 | 0.192 | True |
| 59 | candidate | 2931.95999 | 24.52 | 0.208 | True |
| 59 | candidate | 2934.23779 | 24.82 | 0.185 | True |
| 59 | candidate | 2919.43741 | 25.52 | 0.192 | True |
| 73 | candidate | 3311.77944 | 25.75 | 0.210 | True |
| 73 | candidate | 3309.51077 | 21.10 | 0.190 | True |
| 73 | candidate | 3307.22900 | 22.00 | 0.200 | True |
| 73 | candidate | 3308.35483 | 22.97 | 0.207 | True |
| 86 | candidate | 3650.67141 | 13.94 | 0.191 | True |
| 86 | candidate | 3660.88253 | 15.18 | 0.187 | True |

Timing models are local trapezoids with a linear baseline, seeded by detector windows, fitted to finite positive quality-zero raw SAP. Reported contact durations and depths describe this approximate model, not binary-model parameters. Timing covariance is local; half-cadence floors were used in the clock. See `lead-timing.json`. Unusable fits are displayed for transparency and excluded from the clock. No opposite conjunction is used as a same-kind repeat.

## Clock and actual coverage

The 1.13719 d recurrence is measured from ten representative dips spanning three sectors. Within-sector cadence and dozens of repeated events anchor this clock; the 0.008 d timing RMS is larger than formal fit errors. This is an eclipse recurrence, and a twice-longer orbital period with similar opposite eclipses is not excluded. The train cannot be the selected 20.825 d Gaia orbit: many cycles occur inside a single Gaia period.

The measured adopted recurrence is 1.13719062 d, epoch BTJD 2935.36679; integer cycles [0, -3, -1, -14, 331, 329, 327, 328, 629, 638]. Formal covariance and scatter inflation are retained in `../lead-clocks.json`, but no uniform total period error is claimed in RESULTS.csv. These are bounded representative checks, not an exhaustive all-period posterior.

| Alternative | Representative actual sector | Predicted BTJD | Core samples | Coverage fraction | Median deficit (ppt) | Baseline scatter (ppt) |
|---|---:|---:|---:|---:|---:|---:|
| P/2 | 73 | 3306.65953 | 108 | 1.000 | 0.025 | 3.772 |
| P/3 | 86 | 3659.37816 | 108 | 1.000 | -0.184 | 5.366 |
| P/4 | 73 | 3306.65953 | 108 | 1.000 | 0.025 | 3.772 |
| P/5 | 73 | 3295.17391 | 108 | 1.000 | -0.040 | 5.123 |
| P/6 | 86 | 3659.56769 | 108 | 1.000 | -0.014 | 4.126 |

The full actual-cadence table is `../lead-alias-covered-windows.json`; each row records quality-zero core coverage, maximum core gap, two populated local sidebands and source hash. A missing window is not a null. Event-matched test durations are 0.55 d for Y001 and 0.25 d otherwise. Y001 uses closer uncontaminated sidebands to avoid its opposite eclipse about one day from the half-period prediction. These tests address short same-kind recurrence aliases; they do not prove every long superperiod is impossible.

## Source-specific Gaia orbit

Gaia SB1 P=20.82527988 ± 0.04346612 d; e=0.1990, omega=330.960°, T_periastron=BTJD 398.84016. Mass function f(M)=0.0002 solar masses, consistent with a stellar binary interpretation. The edge-on conjunction estimate uses this source's orbital parameters and full SB1 correlation submatrix (P,e,omega,Tp), with the epoch conversion +389 d.

| Sector | Observed BTJD | Closest conjunction kind | Offset (d) | Local covariance sigma (d) |
|---|---:|---|---:|---:|
| 59 | 2935.35819 | 1 | -1.709 | 5.460 |
| 59 | 2931.95999 | 1 | -5.107 | 5.460 |
| 59 | 2934.23779 | 1 | -2.829 | 5.460 |
| 59 | 2919.43741 | 1 | 3.195 | 5.418 |
| 73 | 3311.77944 | 1 | -0.143 | 6.223 |
| 73 | 3309.51077 | 1 | -2.412 | 6.223 |
| 73 | 3307.22900 | 1 | -4.693 | 6.223 |
| 73 | 3308.35483 | 1 | -3.567 | 6.223 |
| 86 | 3650.67141 | 0 | -2.562 | 7.174 |
| 86 | 3660.88253 | 1 | -5.070 | 6.948 |

This is fixed-cycle local linear propagation with the source-specific correlation vector, not a full nonlinear ephemeris posterior or a calibrated sigma veto. Individual coincidence does not establish orbital association for a train with a different recurrence. The complete two-conjunction numbers and source CSV hash are in `../lead-gaia-covariance.json`. No Gaia period was fixed when fitting photometric midpoints.

## Pixel attribution and alternate reduction

The helper's short-clock target/neighbor difference-image audit is recorded in `../helper-audit.md` and its numerical artifacts. For Y002 the source remains unresolved. For Y006 the four consistent event-local deficits favor the neighbor and refute selected-target attribution; the structured phase stack is not a reliable localization. See the adjudication below. G-band flux ratios are approximate: a required intrinsic depth assumes equal throughput, bandpass and an appropriate aperture dilution model, so it is not a direct comparison with a blended pixel fractional loss.

## Completed scope, limits and next check

The 6.46 arcsec G=9.82 neighbor is 7.33 times the target G-band flux and easily capable of supplying the eclipse loss. TESS alone may not resolve which member is eclipsing. Gaia association fails. The separately extracted 3x3 aperture dilutes the train strongly in the bright blended PSF; small repeated deficits remain but do not discriminate ownership.

Next check: Resolve target and 6.46 arcsec neighbor during one short-clock eclipse; determine which star owns the train and search that source's known-variable identity.

All selected raw QLP FITS, population/download records, bulk and appointment metadata identities were checked and hashed in `../identity-audit.json`; raw event and sector coverage are in `lead-context.json`. Source identifiers were matched exactly and FITS TIC/sector headers verified. Representative images were visually inspected by the lead; helper scope is stated in `../helper-audit.md`.

Shared scoped catalogue receipts cover VSX and ASAS-SN 60 arcsec queries, Gaia EB and NSS/SIMBAD, Prša/IJspeert exact tables, full vetted Kostov tables, and the enabled Kepler EB/TOI tables. No matched prior EB is assigned to these eight in the current receipts. The bounded 244-paper identifier scan found no hits. Those successful scoped nonmatches do not establish exhaustive novelty or settle ownership of a nearby contaminant. Shared receipts live in `../../shared-catalogues/`; supervisor adjudicates novelty independently.

## Provenance

Reproducible code and numerical receipts: `../lead_context.py`, `../lead_timing.py`, `../lead_clocks.py`, `../lead_aliases.py`, `../lead_two_kinds.py`, `../lead_gaia_covariance.py`, `../lead_cuts.py`, `../lead_pixels.py`, `../lead_independent.py`, `../lead_neighbors.py`, `../lead_localization.py`, `../identity_audit.py`; corresponding JSON receipts and source file hashes. `../SHA256SUMS.json` seals this batch. No catalogue ledger or publication files were edited.
