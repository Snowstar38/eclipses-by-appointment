# Z019: TIC 25073050

Full review completion: COMPLETE_BOUNDED. Physical verdict: C. Association: GAIA_CONSISTENT_TARGET_ATTRIBUTED.

S80 contains two matching shallow eclipses centered3480.81500 and3505.10663BTJD, depth about62ppt and duration0.704d. A deep approximately172ppt eclipse at3493.14654BTJD is the other conjunction, not a third same-kind repeat. The measured same-kind interval24.291620859d is close to Gaia24.285909256d. Independent custom aperture reproduces the eclipse and the deficit is target-centered.

## Exact selection and provenance

Exact frozen queue row, Gaia DR3 4495351743976888192, nested Gaia G=11.718269. No substitution. Parent fresh-band-next1000; operational group first/batch03 is provenance, not a scientific rank. The single_discrete visual stratum is selected follow-up, not a blind yield denominator. Queue visual_reason is historical triage and can be contradicted by raw review.

Identity-audit.json verifies exact Gaia/TIC identity, nested magnitudes, FITS TIC/sector headers, and every parent QLP SHA256. Bulk-results and appointment-results retain per-window scores, trial durations, coverage, masks and nonflags for near-threshold revisiting. No additional threshold was imposed here. Lead-context flag_events includes every saved dip window, including nonflags, despite its historical name.

## Raw flux and timing

Finite TIME, finite positive SAP_FLUX and QUALITY=0. Raw full-sector and local plots were personally inspected by the lead. KSPSAP where present is an alternate reduction of the same photons. Same-kind versus opposite conjunction was judged before fitting. Local linear-baseline trapezoid errors are conditional formal errors, not calibrated astrophysical accuracy. Boundary, partial and extrapolated fits are unusable for precision timing.

| Sector | Kind | Trial center BTJD | Trial depth ppt | Timing usable |
|---|---|---:|---:|---|
| 80 | shallow | 3480.815004 | 61.98 | True |
| 80 | deep | 3493.146539 | 171.99 | True |
| 80 | shallow | 3505.106625 | 62.44 | True |

## Clock and aliases

Same-kind period=24.291620859d from cycles0,1; epoch3480.815004BTJD is the shallow-kind epoch, not the deeper primary. Formal difference error=0.00282843d after0.002d/event floor. A heuristic0.02d allowance describes baseline/shape limitations and is not calibrated coverage. No O-C scatter follows from two points. Deep event phase=0.507646. TESS sector80 common absolute timing offset largely cancels in this same-sector interval.

Divisors3–6 predict covered clean nulls and are rejected. The half-period combines alternating depths and the deep event is displaced from the shallow half-clock by0.186d, so it is not a same-kind period. Doubling fails to map both observed shallow events to one conjunction; a two-orbit interpretation is not established. The bounded tested alternatives, masks and per-window values are in lead-alias-covered-windows.json. Core coverage>=75%, no large core gap and both sidebands are required. Null condition depth+4*local point scatter < half characteristic depth is deliberately conservative; missing/flagged windows are not nulls.

| Trial | Period d | Timing compatible | Covered | Clean nulls |
|---|---:|---|---:|---:|
| measured | 24.29162086 | True | 2 | 0 |
| divisor2 | 12.14581043 | True | 3 | 0 |
| divisor3 | 8.09720695 | True | 3 | 1 |
| divisor4 | 6.07290521 | True | 4 | 1 |
| divisor5 | 4.85832417 | True | 4 | 2 |
| divisor6 | 4.04860348 | True | 5 | 2 |
| double | 48.58324172 | False | 1 | 0 |
| Gaia | 24.28590926 | True | 2 | 0 |

Current TESScut sector inventory checked2026-11-06T04:25:43.129510+00:00: [80]. Original QLP inventory: [80]. Response/status/hashes in lead-current-sector-inventory.json. Availability is not proof of usable eclipse coverage.

## Independent reduction and source attribution

HELPER-AUDIT.md and target helper artifacts document custom TESScut apertures, difference images and Gaia neighbors where informative, including unavailable or inconclusive checks. These reductions share the same TESS photons; separate sectors are separate occasions. A centered deficit must be distinguished from capable neighbors before confirmation; a capable unresolved blend retains host uncertainty. Unperformed work is not silently a successful check.

## Gaia geometry

Source-specific P=24.285909256 +/- 0.0075833867d, e=0.039907, omega=323.15380deg, Tp=387.720968BTJD, mass function=0.199561solar masses. The lead-gaia-covariance artifact uses each source's P,e,omega,Tp correlation submatrix with fixed-cycle local linear propagation and edge-on conjunctions. Unusable fits remain labeled; their proxy offsets are not independent timing evidence. Broad covariance consistency is not source-ownership proof or a full nonlinear orbit posterior.

## Catalogue status

Physical classification and novelty remain separate. Root-owned shared-catalogues/ROOT-CATALOGUE-SEAL.json covers successful VSX/ASAS-SN cones, SIMBAD exact IDs, Gaia EB and variability tables, Prsa/IJspeert/Kostov comparisons, Kepler/K2 and TOI checks and bounded identity/literature searches. No exact prior EB identification appears for these eight in that scope. The Z021 nearby SR|M entry is retained separately. Failed or absent queries are unknown; a scoped nonmatch does not prove exhaustive priority. No plausible row is a counted new system.

## Limitations and next check

The clock has only one same-kind interval. The capable G12.52 neighbor25.07arcsec away is spatially distinguished: all three background-corrected deficit centroids stay0.085-0.234pixel from the target versus1.25-1.36pixels from that neighbor under varied windows. This empirical localization has no calibrated PRF astrometric uncertainty; bandpass and throughput are approximate. No precision long-baseline ephemeris is claimed. The deep event has a data gap truncating egress.

Obtain another same-kind eclipse and source-resolved follow-up.

## Evidence

Target lead-context.json, lead-series.json, lead-timing.json, lead-fullsectors.png, lead-raw-context.png, selected-event plot and helper artifacts; batch lead-clocks.json, lead-alias-covered-windows.json, lead-single-conditional-coverage.json, identity-audit.json, lead-gaia-covariance.json, HELPER-AUDIT.md, LEAD-AUDIT.md and SOURCE-MANIFEST.json.
