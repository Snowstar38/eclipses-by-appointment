# Z127: TIC 457228352

Full review completion: COMPLETE_BOUNDED. Physical verdict: PLAUSIBLE. Association: UNESTABLISHED_ALIASES_GAIA_DISFAVORED.

Raw S6 and S32 contain clean approximately9-10ppt eclipse-shaped events at1483.29086 and2194.62680BTJD. Their711.33594d separation has many unexcluded integer-cycle alternatives. The trial20-cycle35.566797d clock is only an alias, not an adopted period.

## Frozen selection and identity

Exact queue row: Gaia DR3 3237564901983551232, actual nested Gaia G=11.558939, selection P=35.9867141344699d, stratum=repeated_discrete. Parent fresh-band-next1000; second/batch04 is operational provenance only. No substitutions and no added selection threshold. Historical triage is not a physical verdict. This selected review is not an unbiased discovery-yield denominator.

identity-audit.json verifies TIC/Gaia identity, nested magnitudes, FITS TIC/sector headers and source SHA256. Parent bulk-results and appointment-results preserve per-target window scores, trial durations, coverage, masks and nonflags for near-threshold revisiting. Historical lead-context flag_events includes recorded dip windows whether or not screening threshold passed.

## Raw flux and measured events

Lead personally inspected representative local and all supplied full-sector plots. Finite TIME, finite positive SAP_FLUX and QUALITY=0 are used. Same-kind events are distinguished from opposite conjunctions before timing. Local linear-baseline symmetric trapezoid fits retain formal conditional timing errors; partial, boundary or unbracketed fits are unusable for precision ephemerides. KSPSAP comparison tests QLP processing with the same photons, not an independent observing occasion.

| Sector | Kind | Trial center BTJD | Depth ppt | Timing usable |
|---|---|---:|---:|---|
| 6 | same | 1483.290861 | 9.73 | True |
| 32 | same | 2194.626803 | 8.71 | True |

## Recurrence, aliases and coverage

{
  "times": [
    1483.290861006441,
    2194.626803060828
  ],
  "cycles": [
    0,
    20
  ],
  "epoch_btjd": 1483.2908610064408,
  "period_d": 35.56679710271932,
  "duration_d": 0.21687318815535542,
  "depth_ppt": 9.219171088316822,
  "gaia_period_d": 35.9867141344699,
  "residuals_d": [
    2.2737367544323206e-13,
    9.094947017729282e-13
  ],
  "period_note": "Two-event provisional alias"
}

Clock metadata above preserves provisional aliases and approximate periods explicitly; a number is not automatically an adopted ephemeris. lead-alias-covered-windows.json tests divisors2-6, doubling, Gaia and where relevant integer counts across the representative baseline down to5d. All observed same-kind midpoints must agree within0.04d. Both sidebands, >=75% core coverage and no large core gap are required. Local side medians define a sloped baseline. Bin width=min(0.1d,duration/5); >=2 points/bin and >=4 sideband bins give a robust scatter. Clean null criterion is depth+4*binned sideband scatter < half characteristic depth. Native and binned scatter, masks, hashes and ambiguous windows remain saved. This bounded alias comparison is not a blind search or calibrated completeness.

| Trial | Period d | Timing compatible | Covered | Clean nulls |
|---|---:|---|---:|---:|
| measured | 35.566797103 | True | 2 | 0 |
| divisor2 | 17.783398551 | True | 3 | 1 |
| divisor3 | 11.855599034 | True | 3 | 1 |
| divisor4 | 8.891699276 | True | 4 | 2 |
| divisor5 | 7.113359421 | True | 5 | 3 |
| divisor6 | 5.927799517 | True | 5 | 3 |
| double | 71.133594205 | True | 2 | 0 |
| Gaia | 35.986714134 | False | 1 | 0 |

Current TESScut availability checked 2026-11-06T05:01:59.980773+00:00: [6, 32]. Original QLP sectors: [6, 32]. Actual inventory status, request and response hashes are saved. Availability does not guarantee useful photometry.

## Source attribution and independent reduction

See HELPER-AUDIT.md and per-target helper receipts for the completed bounded audit. A missing or inconclusive pixel result remains a limitation.

Custom TESScut aperture extractions reuse TESS photons; independent sectors are separate observing occasions. Pixel offsets must be assessed against capable Gaia neighbors and background/window sensitivity. No calibrated PRF astrometric uncertainty or dilution correction is implied.

## Source-specific Gaia geometry

Gaia P=35.986714134 +/- 0.045946065d; e=0.295785; omega=344.268437deg; Tp=374.490756BTJD; spectroscopic mass function=0.008931593solar masses. Fixed-cycle local propagation uses this source's full P,e,omega,Tp correlation submatrix from the SB1 lower triangle P,gamma,K,e,omega,Tp. Edge-on conjunctions are search predictions; consistency neither proves source ownership nor supplies an eclipse timing. Unusable trial-fit geometry remains a proxy, not independent evidence.

S6: nearest nominal conjunction offset=-2.3979d, local covariance sigma=1.1875d, trial timing usable=True.

S32: nearest nominal conjunction offset=-10.7962d, local covariance sigma=2.0547d, trial timing usable=True.

Nonlinear covariance sensitivity is also saved in lead-nonlinear-gaia.json (100000 draws, seed50701, physically valid0<=e<1 and P>0). It aligns conjunction branches before fixed-cycle propagation and reports quantiles and empirical tail fractions. These are Gaia-model consistency diagnostics, not eclipse significance or a full astrophysical posterior. Broad or phase-spanning predictions remain weak compatibility tests.

## Catalogue status

Root-owned ../shared-catalogues/ROOT-CATALOGUE-SEAL.json and target receipts retain the successful scoped VSX/ASAS-SN cones, SIMBAD identities/classifications, Gaia EB/variability tables, Prsa/IJspeert/Kostov vetted tables and additional Kepler/K2/TOI/literature checks. No exact prior EB identity is assigned to these six within the sealed scope. Failed/unavailable queries remain unknown. Scoped nonmatches do not prove exhaustive priority. Physical verdict and catalogue novelty are separate; plausible outcomes are excluded from claims.

## Limitations and next check

Many integer-cycle clocks between5d and the711.34d event separation remain; narrow observing blocks do not decide them. Divisor tests refute some short aliases but do not establish uniqueness. The later event is10.80d from the nearest nominal Gaia conjunction versus local propagated sigma2.06d; source-orbit association is disfavored. Two-event resemblance alone cannot promote it.

Measure another source-resolved eclipse and discriminate integer cycle counts.

## Evidence and provenance

Target lead-context.json, lead-series.json, lead-timing.json, lead-raw-context.png, lead-fullsectors.png and helper artifacts. Batch identity-audit.json, lead-source-hashes.json, lead-current-sector-inventory.json, lead-clocks.json, lead-alias-covered-windows.json, lead-single-conditional-coverage.json, lead-reduction-comparison.json, lead-gaia-covariance.json, LEAD-AUDIT.md, HELPER-AUDIT.md, SOURCE-MANIFEST.json and SHA256SUMS.json. No ledger or public file was edited.
