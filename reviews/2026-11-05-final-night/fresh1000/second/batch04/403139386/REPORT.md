# Z132: TIC 403139386

Full review completion: COMPLETE_BOUNDED. Physical verdict: PLAUSIBLE. Association: UNESTABLISHED_SINGLE.

S73 shows a resolved deep approximately85ppt V-shaped event centered3288.10224BTJD on a slowly variable baseline. S59/S86 have broad variability and large gaps rather than demonstrated same-kind repeats. A current inventory added S19, explicitly tested using a small TESScut.

## Frozen selection and identity

Exact queue row: Gaia DR3 256449374806957056, actual nested Gaia G=11.832154, selection P=42.87795896022648d, stratum=single_discrete. Parent fresh-band-next1000; second/batch04 is operational provenance only. No substitutions and no added selection threshold. Historical triage is not a physical verdict. This selected review is not an unbiased discovery-yield denominator.

identity-audit.json verifies TIC/Gaia identity, nested magnitudes, FITS TIC/sector headers and source SHA256. Parent bulk-results and appointment-results preserve per-target window scores, trial durations, coverage, masks and nonflags for near-threshold revisiting. Historical lead-context flag_events includes recorded dip windows whether or not screening threshold passed.

## Raw flux and measured events

Lead personally inspected representative local and all supplied full-sector plots. Finite TIME, finite positive SAP_FLUX and QUALITY=0 are used. Same-kind events are distinguished from opposite conjunctions before timing. Local linear-baseline symmetric trapezoid fits retain formal conditional timing errors; partial, boundary or unbracketed fits are unusable for precision ephemerides. KSPSAP comparison tests QLP processing with the same photons, not an independent observing occasion.

| Sector | Kind | Trial center BTJD | Depth ppt | Timing usable |
|---|---|---:|---:|---|
| 73 | single | 3288.102240 | 85.26 | True |

## Recurrence, aliases and coverage

No free same-kind eclipse period is measured. Single-event conditional Gaia-period coverage is explicitly an assumption, never a measured timing clock. Missing, flagged, drifted or noise-limited windows are not clean nulls.

Current TESScut availability checked 2026-11-06T05:02:10.109292+00:00: [19, 59, 73, 86]. Original QLP sectors: [59, 73, 86]. Actual inventory status, request and response hashes are saved. Availability does not guarantee useful photometry.

## Source attribution and independent reduction

See HELPER-AUDIT.md and per-target helper receipts for the completed bounded audit. A missing or inconclusive pixel result remains a limitation.

Custom TESScut aperture extractions reuse TESS photons; independent sectors are separate observing occasions. Pixel offsets must be assessed against capable Gaia neighbors and background/window sensitivity. No calibrated PRF astrometric uncertainty or dilution correction is implied.

## Source-specific Gaia geometry

Gaia P=42.877958960 +/- 0.030153926d; e=0.412921; omega=173.796848deg; Tp=375.639557BTJD; spectroscopic mass function=0.02412415solar masses. Fixed-cycle local propagation uses this source's full P,e,omega,Tp correlation submatrix from the SB1 lower triangle P,gamma,K,e,omega,Tp. Edge-on conjunctions are search predictions; consistency neither proves source ownership nor supplies an eclipse timing. Unusable trial-fit geometry remains a proxy, not independent evidence.

S73: nearest nominal conjunction offset=1.4754d, local covariance sigma=1.9580d, trial timing usable=True.

Nonlinear covariance sensitivity is also saved in lead-nonlinear-gaia.json (100000 draws, seed50701, physically valid0<=e<1 and P>0). It aligns conjunction branches before fixed-cycle propagation and reports quantiles and empirical tail fractions. These are Gaia-model consistency diagnostics, not eclipse significance or a full astrophysical posterior. Broad or phase-spanning predictions remain weak compatibility tests.

## Catalogue status

Root-owned ../shared-catalogues/ROOT-CATALOGUE-SEAL.json and target receipts retain the successful scoped VSX/ASAS-SN cones, SIMBAD identities/classifications, Gaia EB/variability tables, Prsa/IJspeert/Kostov vetted tables and additional Kepler/K2/TOI/literature checks. No exact prior EB identity is assigned to these six within the sealed scope. Failed/unavailable queries remain unknown. Scoped nonmatches do not prove exhaustive priority. Physical verdict and catalogue novelty are separate; plausible outcomes are excluded from claims.

## Limitations and next check

Only one eclipse. The S19 cutout has no detectable stellar PSF and near-zero negative median pixels: its normalized aperture plot is invalid and cannot provide a null or recurrence. The attempt is explicitly unavailable/noise-limited. Gaia offset1.48d versus sigma1.96d is compatible but does not measure an orbital clock.

Obtain another source-resolved deep event and discriminate free periods.

## Evidence and provenance

Target lead-context.json, lead-series.json, lead-timing.json, lead-raw-context.png, lead-fullsectors.png and helper artifacts. Batch identity-audit.json, lead-source-hashes.json, lead-current-sector-inventory.json, lead-clocks.json, lead-alias-covered-windows.json, lead-single-conditional-coverage.json, lead-reduction-comparison.json, lead-gaia-covariance.json, LEAD-AUDIT.md, HELPER-AUDIT.md, SOURCE-MANIFEST.json and SHA256SUMS.json. No ledger or public file was edited.
