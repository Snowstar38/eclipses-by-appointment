# Z128: TIC 469894984

Full review completion: COMPLETE_BOUNDED. Physical verdict: C. Association: GAIA_CONSISTENT_TARGET_ATTRIBUTED.

Four representative same-kind raw events occur in S17,S56,S83,S84 at1767.089131,2846.468807,3566.052785,3606.029197BTJD, with about50-52ppt trapezoid depths and0.288d duration. Free timing gives39.976960789d using cycles0,27,45,46; residuals are at most0.00123d. Divisors2-6 predict clean covered nulls. In the bounded integer scan from5d through the1838.94d event separation only the39.97696d family fits all timings and avoids clean nulls.

## Frozen selection and identity

Exact queue row: Gaia DR3 2197843346449008512, actual nested Gaia G=11.905343, selection P=40.02095612710342d, stratum=repeated_discrete. Parent fresh-band-next1000; second/batch04 is operational provenance only. No substitutions and no added selection threshold. Historical triage is not a physical verdict. This selected review is not an unbiased discovery-yield denominator.

identity-audit.json verifies TIC/Gaia identity, nested magnitudes, FITS TIC/sector headers and source SHA256. Parent bulk-results and appointment-results preserve per-target window scores, trial durations, coverage, masks and nonflags for near-threshold revisiting. Historical lead-context flag_events includes recorded dip windows whether or not screening threshold passed.

## Raw flux and measured events

Lead personally inspected representative local and all supplied full-sector plots. Finite TIME, finite positive SAP_FLUX and QUALITY=0 are used. Same-kind events are distinguished from opposite conjunctions before timing. Local linear-baseline symmetric trapezoid fits retain formal conditional timing errors; partial, boundary or unbracketed fits are unusable for precision ephemerides. KSPSAP comparison tests QLP processing with the same photons, not an independent observing occasion.

| Sector | Kind | Trial center BTJD | Depth ppt | Timing usable |
|---|---|---:|---:|---|
| 17 | same | 1767.089131 | 49.56 | True |
| 56 | same | 2846.468807 | 50.36 | True |
| 83 | same | 3566.052785 | 51.66 | True |
| 84 | same | 3606.029197 | 51.78 | True |

## Recurrence, aliases and coverage

{
  "times": [
    1767.0891309952654,
    2846.468806865469,
    3566.0527847072594,
    3606.029197203346
  ],
  "cycles": [
    0,
    27,
    45,
    46
  ],
  "epoch_btjd": 1767.0896366806573,
  "period_d": 39.97696078854838,
  "duration_d": 0.2876170665686469,
  "depth_ppt": 51.01272900549317,
  "gaia_period_d": 40.02095612710342,
  "residuals_d": [
    -0.0005056853919995774,
    0.0012288940056350839,
    -8.74580750860332e-05,
    -0.0006357505367304839
  ],
  "period_note": "Unweighted representative trapezoid midpoint clock; cycle choice tested separately",
  "weighted_epoch_btjd": 1767.0896366806578,
  "weighted_period_d": 39.976960788548396,
  "weighted_period_formal_error_d": 5.366348496352549e-05,
  "fit_chi2": 0.5444314631841884,
  "dof": 2,
  "per_event_floor_d": 0.002,
  "heuristic_period_allowance_d": 0.0001,
  "note": "Primary reported clock remains unweighted representative fit; weighted formal sensitivity fit and 0.0001d conservative allowance are separate; allowance is heuristic, not calibrated coverage."
}

Clock metadata above preserves provisional aliases and approximate periods explicitly; a number is not automatically an adopted ephemeris. lead-alias-covered-windows.json tests divisors2-6, doubling, Gaia and where relevant integer counts across the representative baseline down to5d. All observed same-kind midpoints must agree within0.04d. Both sidebands, >=75% core coverage and no large core gap are required. Local side medians define a sloped baseline. Bin width=min(0.1d,duration/5); >=2 points/bin and >=4 sideband bins give a robust scatter. Clean null criterion is depth+4*binned sideband scatter < half characteristic depth. Native and binned scatter, masks, hashes and ambiguous windows remain saved. This bounded alias comparison is not a blind search or calibrated completeness.

| Trial | Period d | Timing compatible | Covered | Clean nulls |
|---|---:|---|---:|---:|
| measured | 39.976960789 | True | 4 | 0 |
| divisor2 | 19.988480394 | True | 8 | 4 |
| divisor3 | 13.325653596 | True | 14 | 10 |
| divisor4 | 9.994240197 | True | 13 | 9 |
| divisor5 | 7.995392158 | True | 19 | 15 |
| divisor6 | 6.662826798 | True | 25 | 21 |
| double | 79.953921577 | False | 2 | 0 |
| Gaia | 40.020956127 | False | 4 | 3 |

Current TESScut availability checked 2026-11-06T05:02:03.558438+00:00: [16, 17, 56, 57, 76, 83, 84]. Original QLP sectors: [16, 17, 56, 57, 76, 83, 84]. Actual inventory status, request and response hashes are saved. Availability does not guarantee useful photometry.

## Source attribution and independent reduction

Independent7x7 TESScut S83 custom3x3 background-subtracted reduction reproduces39.6ppt loss. Background-aware difference Gaussian centroid is0.167-0.175pixel from target over five core/side variants, versus1.191-1.208pixel from capable Gaia2197843380808747904 (4.57% G flux,1.06pixel target separation). These empirical localization tests favor target ownership and distinguish the capable neighbor. Other closer Gaia neighbors individually contribute <=1.24% G flux under equal-throughput approximation. TESS/G colors, unknown blends and uncalibrated centroid errors remain limits.

Custom TESScut aperture extractions reuse TESS photons; independent sectors are separate observing occasions. Pixel offsets must be assessed against capable Gaia neighbors and background/window sensitivity. No calibrated PRF astrometric uncertainty or dilution correction is implied.

## Source-specific Gaia geometry

Gaia P=40.020956127 +/- 0.032090105d; e=0.501816; omega=111.085606deg; Tp=408.206259BTJD; spectroscopic mass function=0.1581484solar masses. Fixed-cycle local propagation uses this source's full P,e,omega,Tp correlation submatrix from the SB1 lower triangle P,gamma,K,e,omega,Tp. Edge-on conjunctions are search predictions; consistency neither proves source ownership nor supplies an eclipse timing. Unusable trial-fit geometry remains a proxy, not independent evidence.

S17: nearest nominal conjunction offset=-1.1468d, local covariance sigma=1.1604d, trial timing usable=True.

S56: nearest nominal conjunction offset=-2.3329d, local covariance sigma=2.0088d, trial timing usable=True.

S83: nearest nominal conjunction offset=-3.1261d, local covariance sigma=2.5811d, trial timing usable=True.

S84: nearest nominal conjunction offset=-3.1707d, local covariance sigma=2.6130d, trial timing usable=True.

Nonlinear covariance sensitivity is also saved in lead-nonlinear-gaia.json (100000 draws, seed50701, physically valid0<=e<1 and P>0). It aligns conjunction branches before fixed-cycle propagation and reports quantiles and empirical tail fractions. These are Gaia-model consistency diagnostics, not eclipse significance or a full astrophysical posterior. Broad or phase-spanning predictions remain weak compatibility tests.

## Catalogue status

Root-owned ../shared-catalogues/ROOT-CATALOGUE-SEAL.json and target receipts retain the successful scoped VSX/ASAS-SN cones, SIMBAD identities/classifications, Gaia EB/variability tables, Prsa/IJspeert/Kostov vetted tables and additional Kepler/K2/TOI/literature checks. No exact prior EB identity is assigned to these six within the sealed scope. Failed/unavailable queries remain unknown. Scoped nonmatches do not prove exhaustive priority. Physical verdict and catalogue novelty are separate; plausible outcomes are excluded from claims.

## Limitations and next check

Representative four-event timing, no exhaustive all-sector eclipse fit. The formal clock uncertainty and heuristic0.0001d allowance retain separate meanings. Gaia conjunction offsets1.15-3.17d have local covariance errors1.16-2.61d, broadly compatible. Custom TESScut reduction and stable background-aware localization support target attribution. Empirical centroid stability is not a calibrated PRF astrometric uncertainty, and G-based flux capability is approximate.

Retain another source-resolved same-kind timing and refine the ephemeris.

## Evidence and provenance

Target lead-context.json, lead-series.json, lead-timing.json, lead-raw-context.png, lead-fullsectors.png and helper artifacts. Batch identity-audit.json, lead-source-hashes.json, lead-current-sector-inventory.json, lead-clocks.json, lead-alias-covered-windows.json, lead-single-conditional-coverage.json, lead-reduction-comparison.json, lead-gaia-covariance.json, LEAD-AUDIT.md, HELPER-AUDIT.md, SOURCE-MANIFEST.json and SHA256SUMS.json. No ledger or public file was edited.
