# TIC 6946549: CONFIRMED

Repeated primary/secondary eclipses survive independent SPOC photometry, background regression and on-target difference imaging; no capable 60 arcsec neighbour. Small Gaia-period tension and scatter are characterization caveats.

Full-review completion: COMPLETE (adjudicated). Novelty: no prior target EB classification found in successful queried catalogues; limited prior-art coverage, not a guaranteed discovery claim. Current SIMBAD identifies HD 176388 as SB*; known spectroscopic binarity is distinct from prior eclipse classification.

## Raw SAP, individual events and ephemerides

8 accepted primary fits across 3 sectors; median depth 55.972 ppt. Shared exposure-integrated trapezoid T14=5.2436 h, profile range [5.11324138 5.37393103] h; fractional ingress=0.350. T12 and T23 below are trapezoid coordinates; a grazing flat segment is not physical totality.

P=8.0519229126 ± 9.94e-06 d; Tref=3849.0884984 ± 0.00053 BTJD, reference cycle 89; χ²/dof=31.36/6, O−C RMS=1.869 min. Errors include grid/red-noise and ephemeris scatter scaling, conditional on shape/baseline.

Secondary: 6 usable windows, 6 individual >3σ; combined depth 25.0713 ± 0.8874 ppt (event-scatter error). Fitted phase=0.4875889, Gaia nominal=0.4865036. Phase was optimized; repeatability and controls matter more than its single-trial S/N.

P=8.0519333073 ± 1.23e-05 d; Tref=3732.2376496 ± 0.000675 BTJD, reference cycle 74; χ²/dof=25.46/4, O−C RMS=1.944 min. Errors include grid/red-noise and ephemeris scatter scaling, conditional on shape/baseline.

| kind | sector | mid BTJD ± d | depth ± ppt | T14/T12/T23 h | β | O−C min |
| --- | --- | --- | --- | --- | --- | --- |
| P | 67 | 3132.4660327 ± 0.000655 | 66.100 ± 0.457 | 5.244/1.835/1.573 | 2.21905 | -1.91011 |
| P | 67 | 3148.5712635 ± 0.000655 | 65.822 ± 0.621 | 5.244/1.835/1.573 | 2.99759 | 0.0842835 |
| P | 94 | 3865.1943893 ± 0.000655 | 55.815 ± 0.412 | 5.244/1.835/1.573 | 2.3215 | 2.94491 |
| P | 94 | 3873.2463492 ± 0.000655 | 54.038 ± 0.405 | 5.244/1.835/1.573 | 2.09984 | 2.99826 |
| P | 104 | 4179.2168951 ± 0.000655 | 56.165 ± 0.567 | 5.244/1.835/1.573 | 2.8705 | -0.637441 |
| P | 104 | 4187.2688551 ± 0.000655 | 56.017 ± 0.492 | 5.244/1.835/1.573 | 2.71761 | -0.584089 |
| P | 104 | 4195.3208151 ± 0.000655 | 55.927 ± 0.430 | 5.244/1.835/1.573 | 2.35325 | -0.530737 |
| P | 104 | 4203.3714641 ± 0.000655 | 55.803 ± 0.423 | 5.244/1.835/1.573 | 2.37893 | -2.36508 |
| S | 67 | 3128.3414648 ± 0.000655 | 28.463 ± 0.236 | 5.244/1.835/1.573 | 1.59084 | -1.70891 |
| S | 67 | 3144.4466215 ± 0.000655 | 28.285 ± 0.221 | 5.244/1.835/1.573 | 1.52571 | 0.148846 |
| S | 94 | 3861.0703825 ± 0.000655 | 23.603 ± 0.223 | 5.244/1.835/1.573 | 1.67309 | 2.59204 |
| S | 94 | 3877.1742284 ± 0.000655 | 23.237 ± 0.195 | 5.244/1.835/1.573 | 1.52335 | 2.56211 |
| S | 104 | 4183.1446773 ± 0.000655 | 24.186 ± 0.214 | 5.244/1.835/1.573 | 1.71009 | -1.78207 |
| S | 104 | 4199.2485231 ± 0.000655 | 24.267 ± 0.164 | 5.244/1.835/1.573 | 1.45878 | -1.81201 |

All primary timing scans interior: True. QUALITY=0 fits retain all untrimmed cadences; 11 flagged core cadences inspected separately in event records. Minimum background-regressed/ordinary primary depth ratio=0.9995; background is standardized in native units, never divided by normalized SAP. Centroid template shifts/errors are retained per event in fit-results.json and are not by themselves source localization.

Blind rolling-median census: 30 triggers; 13 outside the two eclipse phase windows. Largest off-phase dip=8.657 ppt, versus primary median 55.972 ppt. No off-phase event of comparable primary depth. Off-phase s094 triggers cluster near the known 3875 BTJD sector systematic where applicable; shallow isolated census triggers are not additional classified eclipses. Full trigger/threshold/duration list and every rejected/insufficient event window remain in fit-results.json; coverage failures are not nulls.

## Own Gaia covariance and physical interpretation

Source 6657873519885638144; covariance bit_index=127; source and SB1/SB2 layout asserted before reconstruction. Photometric period minus Gaia period=-2.164σ. Primary matches conjunction A. Per-event Gaia predictions, correlated timing errors and residuals are in orbit-gates.json; no correlation copied from another source.

```json
{
  "gaia_primary_epoch_comparison": [
    {
      "kind": "A",
      "epoch389_offset": 0.00874866586434564,
      "epoch389_gaia_error": 0.0426999455321721
    },
    {
      "kind": "B",
      "epoch389_offset": -3.9175385711929493,
      "epoch389_gaia_error": 0.01897283970891443
    }
  ],
  "eccentricity_comparison": {
    "bit_index": 127,
    "gaia_primary": "A",
    "gaia_relative_phase_nominal": 0.4865035711117025,
    "gaia_relative_phase_quantiles_16_50_84": [
      0.4810694076491121,
      0.48750646816807414,
      0.49439481584739775
    ],
    "gaia_relative_phase_sigma": 0.0067444774266091365,
    "gaia_e_cos_omega_quantiles": [
      -0.029736052483049096,
      -0.01962106588925358,
      -0.008800758145478952
    ],
    "gaia_e_sin_omega_quantiles": [
      0.010963023803343356,
      0.02161645960729645,
      0.03170726388345989
    ],
    "photometric_phase": 0.48758894046256385,
    "photometric_e_cos_omega_first_order": -0.01949524673303748,
    "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
    "geometry_status": "conditional shape feasibility",
    "geometry_e_sin_omega_conditional_range": [
      0.1499999999999999,
      0.1499999999999999
    ],
    "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
  },
  "physics": [
    {
      "m1": 1.65,
      "m2_min": 0.9907179702334377,
      "f_mass": 0.13944600606556237,
      "a_rsun": 23.36851181084498,
      "r1_rsun": 2.40266,
      "r2_approx_rsun": 0.992567457978695,
      "central_T14_hours": {
        "A": 8.73067717476338,
        "B": 9.14561808925202
      },
      "observed_T14_hours": 5.243586206896551
    }
  ],
  "shape_feasibility": {
    "status": "conditional shape feasibility",
    "best": {
      "chi2": 98.42753795213136,
      "dof": 121,
      "k": 0.27499999999999997,
      "b_A": 0.76,
      "e_sin_omega": 0.1499999999999999,
      "primary_scale": 0.834241799100291,
      "secondary_scale": 0.06758187226133039
    },
    "profile_interval_approx_95": {
      "k": [
        0.27499999999999997,
        0.27499999999999997
      ],
      "b_A": [
        0.76,
        0.76
      ],
      "e_sin_omega": [
        0.1499999999999999,
        0.1499999999999999
      ]
    },
    "error_inflation": 1,
    "assumptions": "Circular projected chord with eccentric speed factors; fixed TIC R1/M1, u1=.4 u2=.6, free depth scales per kind, event-scatter bin errors and 0.15ppt floor. Contact shape and dilution degeneracies persist. No claim of precise e sin omega.",
    "primary_profile_n": 64,
    "secondary_profile_n": 64
  }
}
```

Physical quantities using TIC primary properties and approximate companion radii are conditional feasibility checks. The mass function and minimum mass establish stellar-scale companions; main-sequence radii are not measured constraints. A/B conjunction uses Gaia primary ω without a 180° change. Two-disk models use limb darkening and partial overlap; no e sinω is inferred by treating a grazing trapezoid T23 as totality. Free depth scales, grid boundaries, χ² and dilution prevent precise radii/mass-ratio claims.

## Independence and attribution

SPOC, sector 104: FITS target+sector identity validated against the exact MAST row. Same TESS pixels, independent pipeline; not a second observatory. Linear/quadratic baseline sensitivity and background regressions tested. Aperture and PDCSAP dilution corrections explain depth scale differences; eclipse recurrence survives.

| BTJD | column | quadratic ppt | β error ppt | linear ppt | core n | background ppt |
| --- | --- | --- | --- | --- | --- | --- |
| 4187.26886 | SAP_FLUX | 62.9947 | 0.868542 | 63.0532 | 157 | 63.1334 |
| 4187.26886 | PDCSAP_FLUX | 64.1356 | 0.867554 | 64.0838 | 157 | 64.2649 |
| 4195.32082 | SAP_FLUX | 63.009 | 0.850754 | 63.0117 | 157 | 63.2245 |
| 4195.32082 | PDCSAP_FLUX | 63.8489 | 0.877183 | 63.919 | 157 | 64.0534 |
| 4203.37146 | SAP_FLUX | 62.7654 | 1.03422 | 62.8591 | 157 | 62.8934 |
| 4203.37146 | PDCSAP_FLUX | 63.9878 | 1.06392 | 64.1162 | 157 | 64.1165 |

Exact URI/URL, header, SHA256 and retrieval UTC are in independent-manifest.json. Neighbour required fractional dips use G as an approximate passband, not a calibrated TESS dilution correction.

| Gaia source | sep arcsec | G | required fractional dip | capable |
| --- | --- | --- | --- | --- |

Original batch difference-image evidence (old/new schemas represent the same events, not independent repeats):

```json
[
  {
    "tic": "6946549",
    "sector": 104,
    "n_events": 4,
    "deficit_minus_light_arcsec": 0.43,
    "peak_on_target": true,
    "depth_ap3": 0.06137,
    "psf_frac_resid": 0.02,
    "n_neighbours_60": 41,
    "n_possible": 0,
    "brightest_nb": {
      "G": 15.628898,
      "sep": 48.3
    }
  },
  {
    "tic": "6946549",
    "sector": 104,
    "n_events": 4,
    "deficit_minus_target_arcsec": 2.14,
    "deficit_minus_light_arcsec": 0.43,
    "peak_on_target": true,
    "depth_ap3": 0.06137,
    "psf_frac_resid": 0.02,
    "n_neighbours_60": 41,
    "n_possible": 0,
    "brightest_nb": {
      "G": 15.628898,
      "sep": 48.3
    }
  }
]
```

## Archives and novelty

Fresh 60 arcsec IDIA cones returned all nine requested table sections. Counts: {'B_vsx_vsx': 0, 'II_366_catv2021': 0, 'B_sb9_main': 0, 'B_wds_wds': 0, 'J_ApJS_279_50_table2': 0, 'J_ApJS_279_50_table3': 0, 'J_ApJS_279_50_table4': 0, 'J_A_A_691_A242_obaf-eb1': 0, 'J_ApJS_258_16_tess-ebs': 0}. Gaia EB matches=0; vari_summary rows=0; ExoFOP TOI/CTOI={'toi_count': 0, 'ctoi_count': 0}. SIMBAD exact Gaia identifier response is retained in shared cache. WDS records at 290592570/362082706 are visual companions, not an eclipse classification. Kostov table2 rows are unvetted flags and cone neighbours; they do not establish prior published EB classification. There are no target matches in VSX, ASAS-SN, SB9, vetted Kostov3/4, IJspeert or Prša in this fresh pass.

Exact catalogue rows including positions/identifiers are in catalogue-rows.json. General web search on all ten SIMBAD names plus eclipsing returned no relevant exact-target publication (an unrelated aggregated exoplanet-catalogue result was discarded); this is weaker than a complete bibliography search. Novelty remains limited to the successful named checks. Shared/fresh archive query receipts, response hashes and timestamps are indexed in archive-provenance.json and idia-receipts.json.

## Predictions and next check

After evaluation epoch BTJD 4344.32544: next primary approximately 4348.30772; next other-kind approximately 4352.23494 BTJD. These are extrapolations using photometric primary P and the observed secondary epoch (or Gaia phase for a null); formal small timing errors do not include future orbital changes or model systematics. For the three-event secondary at257800191 use these only as scheduling estimates.

Refine diluted two-star dimensions and small-e orbital solution with joint light-curve/RV modelling.

Adjudication: **CONFIRMED**. Repeated primary/secondary eclipses survive independent SPOC photometry, background regression and on-target difference imaging; no capable 60 arcsec neighbour. Small Gaia-period tension and scatter are characterization caveats.

Reproducibility: source-audit.json verifies original candidate status and absent original vet folder before claim. fit_batch.py → orbit_gates.py → secondary_fit.py → shape_secondary.py → secondary_fit.py → geometry.py; null_secondary.py and covariance_geometry.py adapt SB2 covariance as needed. Independent and pixel scripts preserve separate provenance. No original catalogue/paper edits or commits.