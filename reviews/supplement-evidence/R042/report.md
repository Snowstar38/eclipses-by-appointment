# TIC 290592570: CONFIRMED

Two eclipse kinds repeat at the resolved orbital period and match the RV system. Own calibrated pixel fits favour the target over its 9.1 arcsec bright neighbour in both covered events. Depths depend on aperture/dilution; this does not remove the eclipses.

Full-review completion: COMPLETE (adjudicated). Novelty: no prior target EB classification found in successful queried catalogues; limited prior-art coverage, not a guaranteed discovery claim. Current SIMBAD identifies TYC 7467-193-1 as SB*; known spectroscopic binarity is distinct from prior eclipse classification.

## Raw SAP, individual events and ephemerides

8 accepted primary fits across 3 sectors; median depth 81.856 ppt. Shared exposure-integrated trapezoid T14=4.1909 h, profile range [4.104     4.2777931] h; fractional ingress=0.350. T12 and T23 below are trapezoid coordinates; a grazing flat segment is not physical totality.

P=8.8871978965 ± 2.08e-06 d; Tref=3005.4048697 ± 0.000185 BTJD, reference cycle 108; χ²/dof=3.97/6, O−C RMS=0.531 min. Errors include grid/red-noise and ephemeris scatter scaling, conditional on shape/baseline.

Secondary: 7 usable windows, 7 individual >3σ; combined depth 34.6232 ± 0.9374 ppt (event-scatter error). Fitted phase=0.4970615, Gaia nominal=0.5005982. Phase was optimized; repeatability and controls matter more than its single-trial S/N.

P=8.8872001208 ± 2.29e-06 d; Tref=2876.5145337 ± 0.000198 BTJD, reference cycle 93; χ²/dof=2.48/5, O−C RMS=0.449 min. Errors include grid/red-noise and ephemeris scatter scaling, conditional on shape/baseline.

| kind | sector | mid BTJD ± d | depth ± ppt | T14/T12/T23 h | β | O−C min |
| --- | --- | --- | --- | --- | --- | --- |
| P | 27 | 2036.7007263 ± 0.000524 | 82.945 ± 0.623 | 4.191/1.467/1.257 | 1.30221 | 0.615282 |
| P | 27 | 2045.5868954 ± 0.000524 | 82.665 ± 0.562 | 4.191/1.467/1.257 | 1.42372 | -0.866118 |
| P | 27 | 2054.4751600 ± 0.000524 | 82.428 ± 0.653 | 4.191/1.467/1.257 | 1.18092 | 0.669927 |
| P | 67 | 3129.8252582 ± 0.000524 | 82.125 ± 0.640 | 4.191/1.467/1.257 | 2.01262 | -0.550187 |
| P | 67 | 3147.5996920 ± 0.000524 | 81.588 ± 1.024 | 4.191/1.467/1.257 | 2.16595 | -0.495542 |
| P | 94 | 3858.5759939 ± 0.000524 | 69.843 ± 0.550 | 4.191/1.467/1.257 | 2.03132 | 0.181556 |
| P | 94 | 3867.4632108 ± 0.000524 | 69.440 ± 0.719 | 4.191/1.467/1.257 | 2.03712 | 0.208879 |
| P | 94 | 3876.3504276 ± 0.000524 | 69.841 ± 0.583 | 4.191/1.467/1.257 | 2.07721 | 0.236202 |
| S | 27 | 2041.1177827 ± 0.000524 | 37.003 ± 0.473 | 4.191/1.467/1.257 | 1.48798 | 0.0869243 |
| S | 27 | 2050.0049806 ± 0.000524 | 37.035 ± 0.315 | 4.191/1.467/1.257 | 1.1644 | 0.0837213 |
| S | 27 | 2058.8921785 ± 0.000524 | 36.954 ± 0.363 | 4.191/1.467/1.257 | 1.03461 | 0.0805183 |
| S | 67 | 3134.2431240 ± 0.000524 | 35.657 ± 0.333 | 4.191/1.467/1.257 | 1.37515 | -0.307047 |
| S | 67 | 3143.1303219 ± 0.000524 | 35.918 ± 0.334 | 4.191/1.467/1.257 | 1.51749 | -0.31025 |
| S | 94 | 3862.9933515 ± 0.000524 | 31.221 ± 0.337 | 4.191/1.467/1.257 | 1.55127 | -0.569694 |
| S | 94 | 3871.8815971 ± 0.000524 | 31.058 ± 0.286 | 4.191/1.467/1.257 | 1.31994 | 0.935826 |

All primary timing scans interior: True. QUALITY=0 fits retain all untrimmed cadences; 20 flagged core cadences inspected separately in event records. Minimum background-regressed/ordinary primary depth ratio=0.9993; background is standardized in native units, never divided by normalized SAP. Centroid template shifts/errors are retained per event in fit-results.json and are not by themselves source localization.

Blind rolling-median census: 19 triggers; 2 outside the two eclipse phase windows. Largest off-phase dip=6.451 ppt, versus primary median 81.856 ppt. No off-phase event of comparable primary depth. Off-phase s094 triggers cluster near the known 3875 BTJD sector systematic where applicable; shallow isolated census triggers are not additional classified eclipses. Full trigger/threshold/duration list and every rejected/insufficient event window remain in fit-results.json; coverage failures are not nulls.

## Own Gaia covariance and physical interpretation

Source 6695056769751681664; covariance bit_index=127; source and SB1/SB2 layout asserted before reconstruction. Photometric period minus Gaia period=2.098σ. Primary matches conjunction A. Per-event Gaia predictions, correlated timing errors and residuals are in orbit-gates.json; no correlation copied from another source.

```json
{
  "gaia_primary_epoch_comparison": [
    {
      "kind": "A",
      "epoch389_offset": 0.014802134114063392,
      "epoch389_gaia_error": 0.020711153170966536
    },
    {
      "kind": "B",
      "epoch389_offset": -4.432148571263724,
      "epoch389_gaia_error": 0.022799711586115157
    }
  ],
  "eccentricity_comparison": {
    "bit_index": 127,
    "gaia_primary": "A",
    "gaia_relative_phase_nominal": 0.5005982136030157,
    "gaia_relative_phase_quantiles_16_50_84": [
      0.4966178325324745,
      0.5004188405102833,
      0.5041068990386895
    ],
    "gaia_relative_phase_sigma": 0.004174853945575952,
    "gaia_e_cos_omega_quantiles": [
      -0.005311852857204527,
      0.0006578823338586681,
      0.006450399662696864
    ],
    "gaia_e_sin_omega_quantiles": [
      0.009480644197146965,
      0.017069386767230507,
      0.02496020609739401
    ],
    "photometric_phase": 0.49706147181960564,
    "photometric_e_cos_omega_first_order": -0.004615829271946755,
    "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
    "geometry_status": "conditional shape feasibility",
    "geometry_e_sin_omega_conditional_range": [
      0.0749999999999999,
      0.09999999999999992
    ],
    "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
  },
  "physics": [
    {
      "m1": 1.07,
      "m2_min": 0.7405549838443879,
      "f_mass": 0.12389349106526702,
      "a_rsun": 22.005243695569593,
      "r1_rsun": 1.53232,
      "r2_approx_rsun": 0.7864042415243565,
      "central_T14_hours": {
        "A": 7.025347153451335,
        "B": 7.283732188639722
      },
      "observed_T14_hours": 4.190896551724138
    }
  ],
  "shape_feasibility": {
    "status": "conditional shape feasibility",
    "best": {
      "chi2": 150.22054515725134,
      "dof": 121,
      "k": 0.3749999999999999,
      "b_A": 0.9000000000000001,
      "e_sin_omega": 0.0749999999999999,
      "primary_scale": 0.987098050162664,
      "secondary_scale": 0.09794134347107186
    },
    "profile_interval_approx_95": {
      "k": [
        0.35,
        0.3749999999999999
      ],
      "b_A": [
        0.865,
        0.9000000000000001
      ],
      "e_sin_omega": [
        0.0749999999999999,
        0.09999999999999992
      ]
    },
    "error_inflation": 1.2414921087376143,
    "assumptions": "Circular projected chord with eccentric speed factors; fixed TIC R1/M1, u1=.4 u2=.6, free depth scales per kind, event-scatter bin errors and 0.15ppt floor. Contact shape and dilution degeneracies persist. No claim of precise e sin omega.",
    "primary_profile_n": 64,
    "secondary_profile_n": 64
  }
}
```

Physical quantities using TIC primary properties and approximate companion radii are conditional feasibility checks. The mass function and minimum mass establish stellar-scale companions; main-sequence radii are not measured constraints. A/B conjunction uses Gaia primary ω without a 180° change. Two-disk models use limb darkening and partial overlap; no e sinω is inferred by treating a grazing trapezoid T23 as totality. Free depth scales, grid boundaries, χ² and dilution prevent precise radii/mass-ratio claims.

## Independence and attribution

TESS-SPOC, sector 27: FITS target+sector identity validated against the exact MAST row. Same TESS pixels, independent pipeline; not a second observatory. Linear/quadratic baseline sensitivity and background regressions tested. Aperture and PDCSAP dilution corrections explain depth scale differences; eclipse recurrence survives.

| BTJD | column | quadratic ppt | β error ppt | linear ppt | core n | background ppt |
| --- | --- | --- | --- | --- | --- | --- |
| 2036.70073 | SAP_FLUX | 47.4536 | 0.373625 | 47.625 | 25 | 47.5145 |
| 2036.70073 | PDCSAP_FLUX | 80.3903 | 0.621327 | 80.7928 | 25 | 80.4691 |
| 2045.5869 | SAP_FLUX | 46.9238 | 0.338916 | 46.907 | 22 | 46.93 |
| 2045.5869 | PDCSAP_FLUX | 79.4024 | 0.570665 | 79.3774 | 22 | 79.4059 |
| 2054.47516 | SAP_FLUX | 46.6413 | 0.339209 | 46.5793 | 22 | 46.7156 |
| 2054.47516 | PDCSAP_FLUX | 78.8202 | 0.616742 | 78.2573 | 22 | 78.0879 |

Exact URI/URL, header, SHA256 and retrieval UTC are in independent-manifest.json. Neighbour required fractional dips use G as an approximate passband, not a calibrated TESS dilution correction.

| Gaia source | sep arcsec | G | required fractional dip | capable |
| --- | --- | --- | --- | --- |
| 6695056838471158912 | 9.06145 | 11.102676 | 0.122916 | True |

Original batch difference-image evidence (old/new schemas represent the same events, not independent repeats):

```json
[
  {
    "tic": "290592570",
    "sector": 27,
    "n_events": 5,
    "deficit_minus_light_arcsec": 3.57,
    "peak_on_target": true,
    "depth_ap3": 0.03128,
    "psf_frac_resid": 0.178,
    "n_neighbours_60": 12,
    "n_possible": 1,
    "brightest_nb": {
      "G": 11.102676,
      "sep": 9.1
    }
  },
  {
    "tic": "290592570",
    "sector": 27,
    "n_events": 5,
    "deficit_minus_target_arcsec": 2.84,
    "deficit_minus_light_arcsec": 3.57,
    "peak_on_target": true,
    "depth_ap3": 0.03128,
    "psf_frac_resid": 0.178,
    "n_neighbours_60": 12,
    "n_possible": 1,
    "brightest_nb": {
      "G": 11.102676,
      "sep": 9.1
    }
  }
]
```

pixel-localization.json:

```json
{
  "source_path": "C:\\Home\\sky\\data\\sb1-scale-c3\\vet290592570\\tesscut_s027.fits",
  "sha256": "ff435b27c5815b8d9838fd593e3296d14c4371688601054cbda4c08da484d289",
  "sector": 27,
  "calibration": {
    "sigma_pixels": 0.55,
    "dx_pixels": -0.10000000000000009,
    "dy_pixels": -0.20000000000000007
  },
  "fixed_fits": [
    {
      "source_id": "6695056769751681664",
      "sep_arcsec": 0.0,
      "G": 10.661288,
      "chi2": 2979.049171055395,
      "amplitude": 436.41668389677454,
      "fractional_residual": 0.1317029655590075
    },
    {
      "source_id": "6695056838471158912",
      "sep_arcsec": 9.061447109205899,
      "G": 11.102676,
      "chi2": 7676.342720513076,
      "amplitude": 410.7548080270191,
      "fractional_residual": 0.33015318181326486
    }
  ],
  "free_best": {
    "chi2": 2741.3711180634955,
    "pixel_x": 8.072174859875762,
    "pixel_y": 7.504140334399938,
    "distance_from_target_arcsec": 2.969848480983278,
    "fractional_residual": 0.11570610833772482
  },
  "event_source_comparisons": [
    {
      "tc": 2045.5874969191968,
      "best_source": "6695056769751681664",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        1677.9542048550059
      ]
    },
    {
      "tc": 2054.4746948156812,
      "best_source": "6695056769751681664",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        3008.219703521313
      ]
    }
  ],
  "caution": "Same TESS pixels as QLP, independent aperture reduction. Approximate circular Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity."
}
```

## Archives and novelty

Fresh 60 arcsec IDIA cones returned all nine requested table sections. Counts: {'B_vsx_vsx': 0, 'II_366_catv2021': 0, 'B_sb9_main': 0, 'B_wds_wds': 1, 'J_ApJS_279_50_table2': 2, 'J_ApJS_279_50_table3': 0, 'J_ApJS_279_50_table4': 0, 'J_A_A_691_A242_obaf-eb1': 0, 'J_ApJS_258_16_tess-ebs': 0}. Gaia EB matches=0; vari_summary rows=0; ExoFOP TOI/CTOI={'toi_count': 0, 'ctoi_count': 0}. SIMBAD exact Gaia identifier response is retained in shared cache. WDS records at 290592570/362082706 are visual companions, not an eclipse classification. Kostov table2 rows are unvetted flags and cone neighbours; they do not establish prior published EB classification. There are no target matches in VSX, ASAS-SN, SB9, vetted Kostov3/4, IJspeert or Prša in this fresh pass.

Exact catalogue rows including positions/identifiers are in catalogue-rows.json. General web search on all ten SIMBAD names plus eclipsing returned no relevant exact-target publication (an unrelated aggregated exoplanet-catalogue result was discarded); this is weaker than a complete bibliography search. Novelty remains limited to the successful named checks. Shared/fresh archive query receipts, response hashes and timestamps are indexed in archive-provenance.json and idia-receipts.json.

## Predictions and next check

After evaluation epoch BTJD 4344.32544: next primary approximately 4347.37175; next other-kind approximately 4351.78918 BTJD. These are extrapolations using photometric primary P and the observed secondary epoch (or Gaia phase for a null); formal small timing errors do not include future orbital changes or model systematics. For the three-event secondary at257800191 use these only as scheduling estimates.

Refine diluted two-star dimensions and small-e orbital solution with joint light-curve/RV modelling.

Adjudication: **CONFIRMED**. Two eclipse kinds repeat at the resolved orbital period and match the RV system. Own calibrated pixel fits favour the target over its 9.1 arcsec bright neighbour in both covered events. Depths depend on aperture/dilution; this does not remove the eclipses.

Reproducibility: source-audit.json verifies original candidate status and absent original vet folder before claim. fit_batch.py → orbit_gates.py → secondary_fit.py → shape_secondary.py → secondary_fit.py → geometry.py; null_secondary.py and covariance_geometry.py adapt SB2 covariance as needed. Independent and pixel scripts preserve separate provenance. No original catalogue/paper edits or commits.