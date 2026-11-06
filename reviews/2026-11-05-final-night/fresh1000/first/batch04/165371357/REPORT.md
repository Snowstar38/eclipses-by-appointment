# Z027: TIC 165371357

Full review completion: COMPLETE_BOUNDED. Physical verdict: REFUTED. Association: SELECTED_RAMP.

S23 selected lows near1946.6BTJD are at the start of the second orbit and form part of a multi-day recovery ramp. Earlier S16 has weak smooth lows; S49 displays obvious large settling ramps. The partial local fit is unusable.

## Selection, completion and provenance

Exact frozen queue row; Gaia DR3 1549762537000068608, nestedG=11.9990835, selectionP=41.15090366358019d. Parent fresh-band-next1000, operational first/batch04. No substitutions. This visually selected single_discrete stratum is not an unbiased occurrence or completeness denominator. Queue descriptions are historical triage and may be contradicted by raw review.

Canonical bounded criteria were read from [workspace]/Fable 5.1/made/paper/short/sec_methods.html Section2.7 and2.9, with candidate-review-delegation.txt. Completion and physical outcome are separate; completed noise-limited uncertainty is retained. Identity-audit.json checks exact Gaia identity, actual nestedG, every raw FITS TIC/sector header and SHA256. Parent bulk and appointment results preserve every saved score, trial duration, mask, nonflag and exclusion for revisiting near-threshold leads. No new selection threshold is imposed.

## Representative raw measurements

Quality-zero finite TIME, finite positive rawSAP flux. Full-sector, raw-window and selected-event panels were visually inspected by the lead. A local linear-baseline trapezoid uses ±2.5d, baseline outside±1.5d, duration bounds0.05–3d. Formal fit errors assume local point scatter and are conditional; boundary/partial/low-depth fits are excluded. Fits marked usable describe morphology and do not alone prove an eclipse.

|Sector|Kind|Center proxy BTJD|Depth ppt|Duration d|Usable fit|
|---|---|---:|---:|---:|---|
|23|partial_single|1946.877166|1.44|1.085|False|
|16|broad_support|1747.028026|1.26|0.758|False|

## Recurrence and coverage

No same-kind period is measured. Unlike features are not assigned integer cycles. lead-single-conditional-coverage.json evaluates only a conditional Gaia-period guide anchored to the representative proxy; it is not a measured clock or proof that every prediction is absent.

Successful current TESScut availability check2026-11-06T04:58:28.991096+00:00: sectors[16, 22, 23, 49, 76]. Original QLP available inventory[16, 22, 23, 49, 76]. Reviewed cached sectors[16, 22, 23, 49, 76]. Availability does not prove usable event coverage; this is bounded representative review, not exhaustive all-sector fitting.

## Reduction and source attribution

lead-reduction-comparison.json preserves SAP and KSPSAP core/side depths where available. KSPSAP can remove a day-long event; for TIC232631356 S15 it retains only0.038ppt versus5.13ppt rawSAP, a material reduction difference resolved through helper custom aperture evidence rather than treated as independent confirmation. Independent extractions reuse the same photons; different sectors are separate observing occasions. HELPER-AUDIT.md and per-target helper artifacts retain actual custom-aperture, deficit, neighbor and newer-sector results and failures. No unavailable check is treated as a success.

## Source-specific Gaia geometry

P=41.150903664 +/-0.029458381d, e=0.419946, omega=118.88009deg, Tp=406.872827BTJD; mass function=0.0122506solar masses. lead-gaia-covariance.json propagates the source SB1 P,e,omega,Tp submatrix (Gaia lower-triangle parametersP,gamma,K,e,omega,Tp). lead-nonlinear-gaia.json adds100000 nonlinear draws, seed50701, with conjunction phase unwrapped about the nominal epoch before fixed-cycle propagation. Unusable shape proxies are excluded from nonlinear inference. Edge-on conjunctions are assumptions, not measured inclination. Broad consistency does not establish ownership.

## Catalogue status

Root-owned sealed first/shared-catalogues covers VSX/ASAS-SN successful cones, source-specific SIMBAD/Gaia EB/variability/NSS, vetted Prsa/IJspeert/Kostov tables, bounded Kepler/K2/TOI and identity/literature checks. Target-specific rows and any neighbors remain in those receipts. A scoped no-target-prior-EB result is distinct from physical classification and does not establish exhaustive priority. Failed queries remain unknown. SOURCE-MANIFEST.json snapshots the catalogue seal and sources.

## Limitations and next check

This refutes the selected bounded-eclipse interpretation, not the existence of every possible eclipse in this spectroscopic binary. No valid recurrence timing.

Follow up only a new complete bounded event.

## Evidence and contributors

Target lead-context.json, lead-series.json, lead-timing.json, raw/context/full-sector panels and helper artifacts; batch identity audit, source hashes, reduction comparison, covariance/nonlinear covariance, conditional coverage, clocks/aliases, LEAD-AUDIT.md, HELPER-AUDIT.md and SOURCE-MANIFEST.json. Lead reviewed every frozen row; helper independently audited deciding morphology, sources and availability. No ledger or public file edits.
