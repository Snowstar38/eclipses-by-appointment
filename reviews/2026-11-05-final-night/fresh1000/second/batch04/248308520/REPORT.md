# Z130: TIC 248308520

Full review completion: COMPLETE_BOUNDED. Physical verdict: P. Association: GAIA_CONSISTENT_HOST_UNCERTAIN.

Full-sector inspection recovered a second approximately14ppt S55 event at2818.46073BTJD besides the selected2797.28093BTJD event. Matching shape/depth and21.179806d separation support recurrence near Gaia21.136496d. The first starts at the sector edge and lacks pre-event baseline; its symmetric fit is explicitly unusable for precision timing. The second is resolved. Divisors2-6 predict covered clean nulls; the next assumed Gaia-period window in S81 is insufficiently covered.

## Frozen selection and identity

Exact queue row: Gaia DR3 4226656498288395136, actual nested Gaia G=11.926497, selection P=21.136495945169248d, stratum=single_discrete. Parent fresh-band-next1000; second/batch04 is operational provenance only. No substitutions and no added selection threshold. Historical triage is not a physical verdict. This selected review is not an unbiased discovery-yield denominator.

identity-audit.json verifies TIC/Gaia identity, nested magnitudes, FITS TIC/sector headers and source SHA256. Parent bulk-results and appointment-results preserve per-target window scores, trial durations, coverage, masks and nonflags for near-threshold revisiting. Historical lead-context flag_events includes recorded dip windows whether or not screening threshold passed.

## Raw flux and measured events

Lead personally inspected representative local and all supplied full-sector plots. Finite TIME, finite positive SAP_FLUX and QUALITY=0 are used. Same-kind events are distinguished from opposite conjunctions before timing. Local linear-baseline symmetric trapezoid fits retain formal conditional timing errors; partial, boundary or unbracketed fits are unusable for precision ephemerides. KSPSAP comparison tests QLP processing with the same photons, not an independent observing occasion.

| Sector | Kind | Trial center BTJD | Depth ppt | Timing usable |
|---|---|---:|---:|---|
| 55 | same | 2797.280927 | 14.64 | False |
| 55 | same | 2818.460733 | 14.06 | True |

## Recurrence, aliases and coverage

{
  "times": [
    2797.2809273558773,
    2818.4607334418615
  ],
  "cycles": [
    0,
    1
  ],
  "epoch_btjd": 2797.2809273558773,
  "period_d": 21.179806085984183,
  "duration_d": 0.23,
  "depth_ppt": 14.3,
  "gaia_period_d": 21.136495945169248,
  "period_note": "One representative same-kind interval; first event lacks prebaseline so approximate shape-conditional clock, conservative .02d heuristic allowance; not calibrated."
}

Clock metadata above preserves provisional aliases and approximate periods explicitly; a number is not automatically an adopted ephemeris. lead-alias-covered-windows.json tests divisors2-6, doubling, Gaia and where relevant integer counts across the representative baseline down to5d. All observed same-kind midpoints must agree within0.04d. Both sidebands, >=75% core coverage and no large core gap are required. Local side medians define a sloped baseline. Bin width=min(0.1d,duration/5); >=2 points/bin and >=4 sideband bins give a robust scatter. Clean null criterion is depth+4*binned sideband scatter < half characteristic depth. Native and binned scatter, masks, hashes and ambiguous windows remain saved. This bounded alias comparison is not a blind search or calibrated completeness.

| Trial | Period d | Timing compatible | Covered | Clean nulls |
|---|---:|---|---:|---:|
| measured | 21.179806086 | True | 0 | 0 |
| divisor2 | 10.589903043 | True | 2 | 2 |
| divisor3 | 7.059935362 | True | 3 | 3 |
| divisor4 | 5.294951521 | True | 4 | 4 |
| divisor5 | 4.235961217 | True | 6 | 6 |
| divisor6 | 3.529967681 | True | 8 | 8 |
| double | 42.359612172 | False | 0 | 0 |
| Gaia | 21.136495945 | False | 0 | 0 |

Current TESScut availability checked 2026-11-06T05:02:06.620198+00:00: [55, 81]. Original QLP sectors: [55, 81]. Actual inventory status, request and response hashes are saved. Availability does not guarantee useful photometry.

## Source attribution and independent reduction

Independent7x7 TESScut S55 custom3x3 reduction confirms both matching troughs, with a23.4ppt full-event loss. Background-aware Gaussian difference includes11.10counts uniform sky offset; target separation0.046-0.093pixel under five window variants versus0.414-0.434pixel from the close Gaia neighbor0.47pixel from target. That neighbor has1.86% G flux versus2.34% blended custom-aperture loss; unknown TESS/G colors and relative throughput prevent a strict capability exclusion. Localization favors target but the close blend and uncalibrated centroid errors retain host uncertainty. First event starts0.126d before the trial center and lacks a clean prebaseline; independent aperture confirms an eclipse-shaped trough with comparable depth, not a precision midpoint.

Custom TESScut aperture extractions reuse TESS photons; independent sectors are separate observing occasions. Pixel offsets must be assessed against capable Gaia neighbors and background/window sensitivity. No calibrated PRF astrometric uncertainty or dilution correction is implied.

## Source-specific Gaia geometry

Gaia P=21.136495945 +/- 0.07248048d; e=0.149095; omega=12.349047deg; Tp=379.862613BTJD; spectroscopic mass function=0.001696499solar masses. Fixed-cycle local propagation uses this source's full P,e,omega,Tp correlation submatrix from the SB1 lower triangle P,gamma,K,e,omega,Tp. Edge-on conjunctions are search predictions; consistency neither proves source ownership nor supplies an eclipse timing. Unusable trial-fit geometry remains a proxy, not independent evidence.

S55: nearest nominal conjunction offset=4.2523d, local covariance sigma=7.4479d, trial timing usable=False.

S55: nearest nominal conjunction offset=4.2956d, local covariance sigma=7.5200d, trial timing usable=True.

Nonlinear covariance sensitivity is also saved in lead-nonlinear-gaia.json (100000 draws, seed50701, physically valid0<=e<1 and P>0). It aligns conjunction branches before fixed-cycle propagation and reports quantiles and empirical tail fractions. These are Gaia-model consistency diagnostics, not eclipse significance or a full astrophysical posterior. Broad or phase-spanning predictions remain weak compatibility tests.

## Catalogue status

Root-owned ../shared-catalogues/ROOT-CATALOGUE-SEAL.json and target receipts retain the successful scoped VSX/ASAS-SN cones, SIMBAD identities/classifications, Gaia EB/variability tables, Prsa/IJspeert/Kostov vetted tables and additional Kepler/K2/TOI/literature checks. No exact prior EB identity is assigned to these six within the sealed scope. Failed/unavailable queries remain unknown. Scoped nonmatches do not prove exhaustive priority. Physical verdict and catalogue novelty are separate; plausible outcomes are excluded from claims.

## Limitations and next check

Only one same-kind interval and a truncated first ingress/baseline. The21.179806d period is approximate, with a heuristic0.02d allowance rather than calibrated error; no long-baseline precision ephemeris. Broad Gaia timing covariance7.45-7.52d allows the approximately4.3d nominal offset. Independent extraction confirms recurrence; close capable/approximately capable0.47pixel neighbor prevents definitive ownership.

Observe another complete source-resolved eclipse and refine the approximate period.

## Evidence and provenance

Target lead-context.json, lead-series.json, lead-timing.json, lead-raw-context.png, lead-fullsectors.png and helper artifacts. Batch identity-audit.json, lead-source-hashes.json, lead-current-sector-inventory.json, lead-clocks.json, lead-alias-covered-windows.json, lead-single-conditional-coverage.json, lead-reduction-comparison.json, lead-gaia-covariance.json, LEAD-AUDIT.md, HELPER-AUDIT.md, SOURCE-MANIFEST.json and SHA256SUMS.json. No ledger or public file was edited.
