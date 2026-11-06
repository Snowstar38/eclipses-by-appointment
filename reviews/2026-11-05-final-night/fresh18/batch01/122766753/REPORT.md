# Y006 — TIC 122766753

**Physical verdict: REFUTED. Bounded review: COMPLETE.** Catalogue status: NO_EXACT_MATCH_IN_CHECKED_SCOPE. Physical classification and bounded catalogue nonmatch do not themselves authorize a new-system claim; supervisor owns novelty and acceptance.

Gaia DR3 201206229839110784; actual Gaia G=11.96915; frozen stratum repeated_discrete. Exact eight-row membership is in `../queue.csv`. The initial visual label is selection provenance, not an outcome.

## Raw event morphology

Many compact resolved dips recur in S19, S59, S73 and S86. Sparse S19 sampling alone would be weak, but the dense later sectors establish repeated narrow morphology. The train's event spacing is about 2.2093 d. The selected target is not retained as the eclipsing source: four event-local difference images locate the positive deficit on the 19.74 arcsec neighbor rather than the target.

| Sector | Kind | Measured BTJD | Model depth (ppt) | Contact duration (d) | Usable midpoint |
|---|---|---:|---:|---:|---|
| 19 | candidate | 1821.30368 | 13.47 | 0.313 | True |
| 19 | candidate | 1819.08781 | 14.97 | 0.330 | True |
| 19 | candidate | 1823.50697 | 13.11 | 0.303 | True |
| 19 | candidate | 1832.34991 | 13.75 | 0.294 | True |
| 59 | candidate | 2921.52398 | 14.03 | 0.299 | True |
| 59 | candidate | 2925.94262 | 14.91 | 0.291 | True |
| 59 | candidate | 2919.30512 | 14.53 | 0.310 | True |
| 59 | candidate | 2932.56834 | 13.83 | 0.297 | True |
| 73 | candidate | 3286.05137 | 11.41 | 0.221 | True |

Timing models are local trapezoids with a linear baseline, seeded by detector windows, fitted to finite positive quality-zero raw SAP. Reported contact durations and depths describe this approximate model, not binary-model parameters. Timing covariance is local; half-cadence floors were used in the clock. See `lead-timing.json`. Unusable fits are displayed for transparency and excluded from the clock. No opposite conjunction is used as a same-kind repeat.

## Clock and actual coverage

Nine representative events fit a 2.20928 d recurrence with 0.0034 d residual RMS. Several consecutive same-looking events within one sector constrain the short clock. A twice-longer orbital period with nearly similar opposite eclipses remains possible. Neither recurrence is the selected 27.6256 d Gaia orbit; isolated conjunction coincidences are not orbital association.

The measured adopted recurrence is 2.20927657 d, epoch BTJD 1821.30138; integer cycles [0, -1, 1, 5, 498, 500, 497, 503, 663]. Formal covariance and scatter inflation are retained in `../lead-clocks.json`, but no uniform total period error is claimed in RESULTS.csv. These are bounded representative checks, not an exhaustive all-period posterior.

| Alternative | Representative actual sector | Predicted BTJD | Core samples | Coverage fraction | Median deficit (ppt) | Baseline scatter (ppt) |
|---|---:|---:|---:|---:|---:|---:|
| P/2 | 19 | 1824.61530 | 12 | 1.000 | 1.637 | 1.058 |
| P/3 | 86 | 3643.21813 | 108 | 1.000 | 0.023 | 2.599 |
| P/4 | 59 | 2930.91054 | 108 | 1.000 | -0.098 | 2.991 |
| P/5 | 73 | 3291.35401 | 108 | 1.000 | 0.022 | 3.355 |
| P/6 | 86 | 3643.21813 | 108 | 1.000 | 0.023 | 2.599 |

The full actual-cadence table is `../lead-alias-covered-windows.json`; each row records quality-zero core coverage, maximum core gap, two populated local sidebands and source hash. A missing window is not a null. Event-matched test durations are 0.55 d for Y001 and 0.25 d otherwise. Y001 uses closer uncontaminated sidebands to avoid its opposite eclipse about one day from the half-period prediction. These tests address short same-kind recurrence aliases; they do not prove every long superperiod is impossible.

## Source-specific Gaia orbit

Gaia SB1 P=27.62559118 ± 0.01731827 d; e=0.0724, omega=187.257°, T_periastron=BTJD 379.81369. Mass function f(M)=0.0067 solar masses, consistent with a stellar binary interpretation. The edge-on conjunction estimate uses this source's orbital parameters and full SB1 correlation submatrix (P,e,omega,Tp), with the epoch conversion +389 d.

| Sector | Observed BTJD | Closest conjunction kind | Offset (d) | Local covariance sigma (d) |
|---|---:|---|---:|---:|
| 19 | 1821.30368 | 1 | -0.764 | 0.965 |
| 19 | 1819.08781 | 1 | -2.980 | 0.965 |
| 19 | 1823.50697 | 1 | 1.439 | 0.965 |
| 19 | 1832.34991 | 0 | -4.792 | 0.860 |
| 59 | 2921.52398 | 1 | -5.567 | 1.612 |
| 59 | 2925.94262 | 1 | -1.149 | 1.612 |
| 59 | 2919.30512 | 0 | 4.765 | 1.513 |
| 59 | 2932.56834 | 1 | 5.477 | 1.612 |
| 73 | 3286.05137 | 1 | -0.172 | 1.830 |

This is fixed-cycle local linear propagation with the source-specific correlation vector, not a full nonlinear ephemeris posterior or a calibrated sigma veto. Individual coincidence does not establish orbital association for a train with a different recurrence. The complete two-conjunction numbers and source CSV hash are in `../lead-gaia-covariance.json`. No Gaia period was fixed when fitting photometric midpoints.

## Pixel attribution and alternate reduction

The helper's short-clock target/neighbor difference-image audit is recorded in `../helper-audit.md` and its numerical artifacts. For Y002 the source remains unresolved. For Y006 the four consistent event-local deficits favor the neighbor and refute selected-target attribution; the structured phase stack is not a reliable localization. See the adjudication below. G-band flux ratios are approximate: a required intrinsic depth assumes equal throughput, bandpass and an appropriate aperture dilution model, so it is not a direct comparison with a blended pixel fractional loss.

## Completed scope, limits and next check

REFUTED_SOURCE for the selected Gaia/TIC target. Four separate S59 event-local differences all peak at pixel (4,5); their centroids are approximately 0.04-0.20 pixel from Gaia DR3 201206302856438528 and about one pixel from the target. This repeated local PSF displacement is stronger evidence than an unresolved-blend possibility. The phase-stack image is structured and gives a conflicting centroid; because stacking spans variable backgrounds and broad baseline states, it is not accepted as a reliable localization and does not override four consistent clean local event differences. A calibrated PRF fit or second orientation could test this adjudication, but target attribution is refuted within the bounded representative evidence. The neighbor remains a separate characterization lead, with no independent source/novelty review or claim substituted into this queue.

Next check: Perform a separate identity, catalogue and PRF/resolved-photometry review of neighbor Gaia DR3 201206302856438528; establish its true orbital period without silently relabeling the selected target.

All selected raw QLP FITS, population/download records, bulk and appointment metadata identities were checked and hashed in `../identity-audit.json`; raw event and sector coverage are in `lead-context.json`. Source identifiers were matched exactly and FITS TIC/sector headers verified. Representative images were visually inspected by the lead; helper scope is stated in `../helper-audit.md`.

Shared scoped catalogue receipts cover VSX and ASAS-SN 60 arcsec queries, Gaia EB and NSS/SIMBAD, Prša/IJspeert exact tables, full vetted Kostov tables, and the enabled Kepler EB/TOI tables. No matched prior EB is assigned to these eight in the current receipts. The bounded 244-paper identifier scan found no hits. Those successful scoped nonmatches do not establish exhaustive novelty or settle ownership of a nearby contaminant. Shared receipts live in `../../shared-catalogues/`; supervisor adjudicates novelty independently.

## Provenance

Reproducible code and numerical receipts: `../lead_context.py`, `../lead_timing.py`, `../lead_clocks.py`, `../lead_aliases.py`, `../lead_two_kinds.py`, `../lead_gaia_covariance.py`, `../lead_cuts.py`, `../lead_pixels.py`, `../lead_independent.py`, `../lead_neighbors.py`, `../lead_localization.py`, `../identity_audit.py`; corresponding JSON receipts and source file hashes. `../SHA256SUMS.json` seals this batch. No catalogue ledger or publication files were edited.
