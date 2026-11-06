# Z129: TIC 235650919

Full review completion: COMPLETE_BOUNDED. Physical verdict: PLAUSIBLE. Association: UNESTABLISHED_SINGLE.

S53 contains a localized approximately8-11ppt depression near2746.400BTJD, superposed on substantial slower variability. Earlier S26/S40 and noisy S80 do not demonstrate a same-kind repeat in full-sector inspection.

## Frozen selection and identity

Exact queue row: Gaia DR3 4529160253364608000, actual nested Gaia G=11.704402, selection P=34.86943347761092d, stratum=single_discrete. Parent fresh-band-next1000; second/batch04 is operational provenance only. No substitutions and no added selection threshold. Historical triage is not a physical verdict. This selected review is not an unbiased discovery-yield denominator.

identity-audit.json verifies TIC/Gaia identity, nested magnitudes, FITS TIC/sector headers and source SHA256. Parent bulk-results and appointment-results preserve per-target window scores, trial durations, coverage, masks and nonflags for near-threshold revisiting. Historical lead-context flag_events includes recorded dip windows whether or not screening threshold passed.

## Raw flux and measured events

Lead personally inspected representative local and all supplied full-sector plots. Finite TIME, finite positive SAP_FLUX and QUALITY=0 are used. Same-kind events are distinguished from opposite conjunctions before timing. Local linear-baseline symmetric trapezoid fits retain formal conditional timing errors; partial, boundary or unbracketed fits are unusable for precision ephemerides. KSPSAP comparison tests QLP processing with the same photons, not an independent observing occasion.

| Sector | Kind | Trial center BTJD | Depth ppt | Timing usable |
|---|---|---:|---:|---|
| 53 | single | 2746.400065 | 8.24 | True |

## Recurrence, aliases and coverage

No free same-kind eclipse period is measured. Single-event conditional Gaia-period coverage is explicitly an assumption, never a measured timing clock. Missing, flagged, drifted or noise-limited windows are not clean nulls.

Current TESScut availability checked 2026-11-06T05:02:04.775456+00:00: [26, 40, 53, 80]. Original QLP sectors: [26, 40, 53, 80]. Actual inventory status, request and response hashes are saved. Availability does not guarantee useful photometry.

## Source attribution and independent reduction

See HELPER-AUDIT.md and per-target helper receipts for the completed bounded audit. A missing or inconclusive pixel result remains a limitation.

Custom TESScut aperture extractions reuse TESS photons; independent sectors are separate observing occasions. Pixel offsets must be assessed against capable Gaia neighbors and background/window sensitivity. No calibrated PRF astrometric uncertainty or dilution correction is implied.

## Source-specific Gaia geometry

Gaia P=34.869433478 +/- 0.024792032d; e=0.532056; omega=309.857279deg; Tp=374.500232BTJD; spectroscopic mass function=0.01248052solar masses. Fixed-cycle local propagation uses this source's full P,e,omega,Tp correlation submatrix from the SB1 lower triangle P,gamma,K,e,omega,Tp. Edge-on conjunctions are search predictions; consistency neither proves source ownership nor supplies an eclipse timing. Unusable trial-fit geometry remains a proxy, not independent evidence.

S53: nearest nominal conjunction offset=1.8357d, local covariance sigma=1.8884d, trial timing usable=True.

Nonlinear covariance sensitivity is also saved in lead-nonlinear-gaia.json (100000 draws, seed50701, physically valid0<=e<1 and P>0). It aligns conjunction branches before fixed-cycle propagation and reports quantiles and empirical tail fractions. These are Gaia-model consistency diagnostics, not eclipse significance or a full astrophysical posterior. Broad or phase-spanning predictions remain weak compatibility tests.

## Catalogue status

Root-owned ../shared-catalogues/ROOT-CATALOGUE-SEAL.json and target receipts retain the successful scoped VSX/ASAS-SN cones, SIMBAD identities/classifications, Gaia EB/variability tables, Prsa/IJspeert/Kostov vetted tables and additional Kepler/K2/TOI/literature checks. No exact prior EB identity is assigned to these six within the sealed scope. Failed/unavailable queries remain unknown. Scoped nonmatches do not prove exhaustive priority. Physical verdict and catalogue novelty are separate; plausible outcomes are excluded from claims.

## Limitations and next check

One credible local event; variable baseline and sparse cadence. Exact Gaia-period predictions fall in insufficiently covered windows; no measured free clock is available. Gaia geometry is compatible within broad covariance but does not establish recurrence or host.

Obtain a second source-resolved event on a measured clock.

## Evidence and provenance

Target lead-context.json, lead-series.json, lead-timing.json, lead-raw-context.png, lead-fullsectors.png and helper artifacts. Batch identity-audit.json, lead-source-hashes.json, lead-current-sector-inventory.json, lead-clocks.json, lead-alias-covered-windows.json, lead-single-conditional-coverage.json, lead-reduction-comparison.json, lead-gaia-covariance.json, LEAD-AUDIT.md, HELPER-AUDIT.md, SOURCE-MANIFEST.json and SHA256SUMS.json. No ledger or public file was edited.
