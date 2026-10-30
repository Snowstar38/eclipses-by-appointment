# TIC 67651413: CONFIRMED

Both eclipse kinds repeat, independent TESS-SPOC and on-target difference imaging agree, and no capable neighbour is present. The Gaia-period discrepancy and poor simplified two-disk shape fit preclude precise orbital/stellar claims but do not invalidate the target EB.

Full-review completion: COMPLETE (adjudicated). Novelty: no prior target EB classification found in successful queried catalogues; limited prior-art coverage, not a guaranteed discovery claim. Current SIMBAD identifies TYC 2996-1253-1 as SB*; known spectroscopic binarity is distinct from prior eclipse classification.

## Raw SAP, individual events and ephemerides

7 accepted primary fits across 2 sectors; median depth 65.013 ppt. Shared exposure-integrated trapezoid T14=3.6695 h, profile range [3.58262069 3.75641379] h; fractional ingress=0.350. T12 and T23 below are trapezoid coordinates; a grazing flat segment is not physical totality.

P=6.8329952426 ± 1.23e-05 d; Tref=2305.9547009 ± 0.000581 BTJD, reference cycle 63; χ²/dof=2.27/5, O−C RMS=0.403 min. Errors include grid/red-noise and ephemeris scatter scaling, conditional on shape/baseline.

Secondary: 6 usable windows, 6 individual >3σ; combined depth 25.7249 ± 0.5592 ppt (event-scatter error). Fitted phase=0.5002217, Gaia nominal=0.5042494. Phase was optimized; repeatability and controls matter more than its single-trial S/N.

P=6.8329911329 ± 1.3e-05 d; Tref=2247.8747538 ± 0.000705 BTJD, reference cycle 54; χ²/dof=3.10/4, O−C RMS=0.995 min. Errors include grid/red-noise and ephemeris scatter scaling, conditional on shape/baseline.

| kind | sector | mid BTJD ± d | depth ± ppt | T14/T12/T23 h | β | O−C min |
| --- | --- | --- | --- | --- | --- | --- |
| P | 21 | 1875.4758521 ± 0.00227 | 66.160 ± 0.524 | 3.670/1.284/1.101 | 1 | -0.213773 |
| P | 21 | 1889.1419252 ± 0.00227 | 66.500 ± 0.593 | 3.670/1.284/1.101 | 1 | -0.0948858 |
| P | 21 | 1895.9749617 ± 0.00227 | 66.869 ± 0.577 | 3.670/1.284/1.101 | 1.00068 | -0.0354423 |
| P | 48 | 2613.4401271 ± 0.000486 | 65.013 ± 0.482 | 3.670/1.284/1.101 | 1.20366 | 0.922018 |
| P | 48 | 2620.2722462 ± 0.000473 | 63.634 ± 0.451 | 3.670/1.284/1.101 | 1.03414 | -0.339565 |
| P | 48 | 2627.1052827 ± 0.00046 | 63.436 ± 0.481 | 3.670/1.284/1.101 | 1.19358 | -0.280121 |
| P | 48 | 2633.9383193 ± 0.000473 | 63.751 ± 0.463 | 3.670/1.284/1.101 | 1.14724 | -0.220678 |
| S | 21 | 1872.0610179 ± 0.00227 | 23.628 ± 0.343 | 3.670/1.284/1.101 | 1 | 1.11804 |
| S | 21 | 1878.8921784 ± 0.00227 | 25.426 ± 0.284 | 3.670/1.284/1.101 | 1.05253 | -1.51809 |
| S | 21 | 1892.5600036 ± 0.00269 | 25.783 ± 0.325 | 3.670/1.284/1.101 | 1 | 1.1358 |
| S | 48 | 2610.0226693 ± 0.000459 | 28.137 ± 0.324 | 3.670/1.284/1.101 | 1.07217 | -0.88487 |
| S | 48 | 2616.8565820 ± 0.000473 | 26.216 ± 0.311 | 3.670/1.284/1.101 | 1.23265 | 0.442074 |
| S | 48 | 2630.5225724 ± 0.00046 | 24.873 ± 0.345 | 3.670/1.284/1.101 | 1.26416 | 0.45391 |

All primary timing scans interior: True. QUALITY=0 fits retain all untrimmed cadences; 15 flagged core cadences inspected separately in event records. Minimum background-regressed/ordinary primary depth ratio=0.9967; background is standardized in native units, never divided by normalized SAP. Centroid template shifts/errors are retained per event in fit-results.json and are not by themselves source localization.

Blind rolling-median census: 15 triggers; 2 outside the two eclipse phase windows. Largest off-phase dip=4.541 ppt, versus primary median 65.013 ppt. No off-phase event of comparable primary depth. Off-phase s094 triggers cluster near the known 3875 BTJD sector systematic where applicable; shallow isolated census triggers are not additional classified eclipses. Full trigger/threshold/duration list and every rejected/insufficient event window remain in fit-results.json; coverage failures are not nulls.

## Own Gaia covariance and physical interpretation

Source 806524493741663232; covariance bit_index=127; source and SB1/SB2 layout asserted before reconstruction. Photometric period minus Gaia period=-3.531σ. Primary matches conjunction A. Per-event Gaia predictions, correlated timing errors and residuals are in orbit-gates.json; no correlation copied from another source.

```json
{
  "gaia_primary_epoch_comparison": [
    {
      "kind": "A",
      "epoch389_offset": 0.00544786216897819,
      "epoch389_gaia_error": 0.015698303660971
    },
    {
      "kind": "B",
      "epoch389_offset": 3.397196715908194,
      "epoch389_gaia_error": 0.010279629624072086
    }
  ],
  "eccentricity_comparison": {
    "bit_index": 127,
    "gaia_primary": "A",
    "gaia_relative_phase_nominal": 0.5042494264253734,
    "gaia_relative_phase_quantiles_16_50_84": [
      0.5008141581445732,
      0.5034658602629234,
      0.5070693921197647
    ],
    "gaia_relative_phase_sigma": 0.0031395388254875423,
    "gaia_e_cos_omega_quantiles": [
      0.0012788499486578225,
      0.005443977775436568,
      0.011104741264862305
    ],
    "gaia_e_sin_omega_quantiles": [
      -0.003999136286808038,
      0.0009789453178621137,
      0.006187132831248789
    ],
    "photometric_phase": 0.5002217082237235,
    "photometric_e_cos_omega_first_order": 0.0003482584634450499,
    "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
    "geometry_status": "conditional shape feasibility",
    "geometry_e_sin_omega_conditional_range": [
      0.09999999999999992,
      0.1499999999999999
    ],
    "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
  },
  "physics": [
    {
      "m1": 0.96,
      "m2_min": 0.7294188010569504,
      "f_mass": 0.13597410649170086,
      "a_rsun": 18.048945139917684,
      "r1_rsun": 1.61617,
      "r2_approx_rsun": 0.7769294117537343,
      "central_T14_hours": {
        "A": 6.90911196099168,
        "B": 6.934319908175338
      },
      "observed_T14_hours": 3.66951724137931
    }
  ],
  "shape_feasibility": {
    "status": "conditional shape feasibility",
    "best": {
      "chi2": 1316.6690679652888,
      "dof": 121,
      "k": 0.29999999999999993,
      "b_A": 0.8300000000000001,
      "e_sin_omega": 0.1499999999999999,
      "primary_scale": 0.9497979712015495,
      "secondary_scale": 0.14998433377066753
    },
    "profile_interval_approx_95": {
      "k": [
        0.27499999999999997,
        0.35
      ],
      "b_A": [
        0.7950000000000002,
        0.935
      ],
      "e_sin_omega": [
        0.09999999999999992,
        0.1499999999999999
      ]
    },
    "error_inflation": 10.881562545167677,
    "assumptions": "Circular projected chord with eccentric speed factors; fixed TIC R1/M1, u1=.4 u2=.6, free depth scales per kind, event-scatter bin errors and 0.15ppt floor. Contact shape and dilution degeneracies persist. No claim of precise e sin omega.",
    "primary_profile_n": 64,
    "secondary_profile_n": 64
  }
}
```

Physical quantities using TIC primary properties and approximate companion radii are conditional feasibility checks. The mass function and minimum mass establish stellar-scale companions; main-sequence radii are not measured constraints. A/B conjunction uses Gaia primary ω without a 180° change. Two-disk models use limb darkening and partial overlap; no e sinω is inferred by treating a grazing trapezoid T23 as totality. Free depth scales, grid boundaries, χ² and dilution prevent precise radii/mass-ratio claims.

## Independence and attribution

TESS-SPOC, sector 48: FITS target+sector identity validated against the exact MAST row. Same TESS pixels, independent pipeline; not a second observatory. Linear/quadratic baseline sensitivity and background regressions tested. Aperture and PDCSAP dilution corrections explain depth scale differences; eclipse recurrence survives.

| BTJD | column | quadratic ppt | β error ppt | linear ppt | core n | background ppt |
| --- | --- | --- | --- | --- | --- | --- |
| 2613.44013 | SAP_FLUX | 62.854 | 0.688027 | 62.1941 | 22 | 63.0521 |
| 2613.44013 | PDCSAP_FLUX | 63.1019 | 0.639768 | 62.306 | 22 | 63.3559 |
| 2620.27225 | SAP_FLUX | 61.8112 | 0.562852 | 61.3112 | 22 | 61.9741 |
| 2620.27225 | PDCSAP_FLUX | 62.3953 | 0.573241 | 61.8308 | 22 | 62.5857 |
| 2627.10528 | SAP_FLUX | 61.4131 | 0.526416 | 60.7633 | 22 | 61.4082 |
| 2627.10528 | PDCSAP_FLUX | 61.9325 | 0.529296 | 61.2836 | 22 | 61.9282 |
| 2633.93832 | SAP_FLUX | 61.1641 | 0.531187 | 60.7391 | 21 | 61.3927 |
| 2633.93832 | PDCSAP_FLUX | 61.69 | 0.551966 | 61.2047 | 21 | 61.9085 |

Exact URI/URL, header, SHA256 and retrieval UTC are in independent-manifest.json. Neighbour required fractional dips use G as an approximate passband, not a calibrated TESS dilution correction.

| Gaia source | sep arcsec | G | required fractional dip | capable |
| --- | --- | --- | --- | --- |

Original batch difference-image evidence (old/new schemas represent the same events, not independent repeats):

```json
[
  {
    "tic": "67651413",
    "sector": 48,
    "n_events": 7,
    "deficit_minus_light_arcsec": 0.14,
    "peak_on_target": true,
    "depth_ap3": 0.04483,
    "psf_frac_resid": 0.013,
    "n_neighbours_60": 4,
    "n_possible": 0,
    "brightest_nb": {
      "G": 16.661469,
      "sep": 36.3
    }
  },
  {
    "tic": "67651413",
    "sector": 48,
    "n_events": 7,
    "deficit_minus_target_arcsec": 0.52,
    "deficit_minus_light_arcsec": 0.14,
    "peak_on_target": true,
    "depth_ap3": 0.04483,
    "psf_frac_resid": 0.013,
    "n_neighbours_60": 4,
    "n_possible": 0,
    "brightest_nb": {
      "G": 16.661469,
      "sep": 36.3
    }
  }
]
```

## Archives and novelty

Fresh 60 arcsec IDIA cones returned all nine requested table sections. Counts: {'B_vsx_vsx': 0, 'II_366_catv2021': 0, 'B_sb9_main': 0, 'B_wds_wds': 0, 'J_ApJS_279_50_table2': 0, 'J_ApJS_279_50_table3': 0, 'J_ApJS_279_50_table4': 0, 'J_A_A_691_A242_obaf-eb1': 0, 'J_ApJS_258_16_tess-ebs': 0}. Gaia EB matches=0; vari_summary rows=0; ExoFOP TOI/CTOI={'toi_count': 0, 'ctoi_count': 0}. SIMBAD exact Gaia identifier response is retained in shared cache. WDS records at 290592570/362082706 are visual companions, not an eclipse classification. Kostov table2 rows are unvetted flags and cone neighbours; they do not establish prior published EB classification. There are no target matches in VSX, ASAS-SN, SB9, vetted Kostov3/4, IJspeert or Prša in this fresh pass.

Exact catalogue rows including positions/identifiers are in catalogue-rows.json. General web search on all ten SIMBAD names plus eclipsing returned no relevant exact-target publication (an unrelated aggregated exoplanet-catalogue result was discarded); this is weaker than a complete bibliography search. Novelty remains limited to the successful named checks. Shared/fresh archive query receipts, response hashes and timestamps are indexed in archive-provenance.json and idia-receipts.json.

## Predictions and next check

After evaluation epoch BTJD 4344.32544: next primary approximately 4349.02028; next other-kind approximately 4345.60452 BTJD. These are extrapolations using photometric primary P and the observed secondary epoch (or Gaia phase for a null); formal small timing errors do not include future orbital changes or model systematics. For the three-event secondary at257800191 use these only as scheduling estimates.

Refine diluted two-star dimensions and small-e orbital solution with joint light-curve/RV modelling.

Adjudication: **CONFIRMED**. Both eclipse kinds repeat, independent TESS-SPOC and on-target difference imaging agree, and no capable neighbour is present. The Gaia-period discrepancy and poor simplified two-disk shape fit preclude precise orbital/stellar claims but do not invalidate the target EB.

Reproducibility: source-audit.json verifies original candidate status and absent original vet folder before claim. fit_batch.py → orbit_gates.py → secondary_fit.py → shape_secondary.py → secondary_fit.py → geometry.py; null_secondary.py and covariance_geometry.py adapt SB2 covariance as needed. Independent and pixel scripts preserve separate provenance. No original catalogue/paper edits or commits.