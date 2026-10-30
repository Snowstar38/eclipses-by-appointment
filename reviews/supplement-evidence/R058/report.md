# TIC 236531158: PLAUSIBLE

The eclipsing signal is secure, with27 primaries and28 individually detected secondary events, but the host remains materially ambiguous. Free-amplitude calibrated circular/elliptical models favor the12arcsec G13.84 neighbor in13/13 events; enforcing Gaia-G flux ratios flips the result to target in13/13 events. PSF/color/dilution calibration is not controlled sufficiently to resolve this model dependence. PLAUSIBLE refers to the assigned target EB; it is not a claim that the eclipse signal itself is doubtful.

Full review: COMPLETED_WITH_ARCHIVE_LIMITATION. Physical verdict is separate from novelty. Novelty: LIMITED_PRIOR_ART_COVERAGE; no prior target EB was established by the available current sources. New nine-catalog passes to both IDIA and Harvard timed out and are not negative matches.

## Raw SAP and event measurements

Primary P=2.020569926 +/- 0.000000533 d; Tref=2853.3540841 +/- 0.0001656 BTJD at cycle564; T0=1713.7526460. 27 fitted primary events, O-C RMS=2.545 min; chi2/dof=27.03/25. Shape T14=2.477h, profile range=[0.10076120689655173, 0.10564913793103449], ingress fraction=0.35; T12=fr*T14 and nominal T23=T14-2*T12. Trapezoid flat time is not totality for grazing systems.

|sector|mid BTJD|error d|depth ppt|error ppt|O-C min|flagged core|
|---|---:|---:|---:|---:|---:|---:|
|15|1711.7274469|0.002690|66.887|0.730|-6.666|0|
|15|1713.7486308|0.002690|67.981|0.512|-5.782|0|
|15|1715.7691954|0.002690|67.163|0.576|-5.790|0|
|15|1717.7897600|0.002690|67.274|0.681|-5.797|0|
|15|1727.8932024|0.002690|65.241|0.641|-4.944|0|
|15|1729.9137670|0.002690|66.162|0.604|-4.951|0|
|15|1731.9343317|0.002690|66.778|0.627|-4.959|0|
|55|2798.7992675|0.000518|64.193|0.572|0.823|0|
|55|2800.8192129|0.000518|64.166|0.513|-0.077|0|
|55|2802.8403968|0.000536|64.836|0.947|0.808|1|
|55|2804.8603422|0.000556|64.057|0.666|-0.092|2|
|55|2812.9432199|0.000518|64.862|0.650|0.769|0|
|55|2814.9637846|0.000518|64.734|0.508|0.762|0|
|55|2816.9843492|0.000518|64.410|0.543|0.754|0|
|55|2819.0042946|0.000518|65.454|0.630|-0.145|0|
|82|3534.2860311|0.000310|64.909|0.505|-0.170|0|
|82|3536.3065957|0.000310|64.952|0.596|-0.178|0|
|82|3538.3277796|0.000310|65.241|0.611|0.707|6|
|82|3540.3477250|0.000310|64.945|0.665|-0.193|0|
|82|3542.3682896|0.000310|64.824|0.611|-0.200|0|
|82|3544.3888543|0.000310|64.184|0.614|-0.208|0|
|82|3546.4094189|0.000310|64.609|0.602|-0.216|0|
|82|3548.4299835|0.000310|64.464|0.497|-0.223|0|
|82|3550.4505481|0.000310|65.080|0.615|-0.231|0|
|82|3552.4717320|0.000310|64.418|0.616|0.653|0|
|82|3554.4916774|0.000310|64.810|0.588|-0.246|0|
|82|3556.5122420|0.000310|64.634|0.653|-0.254|0|

Primary median depth=64.862ppt; maximum absolute background-regression fake depth=0.728ppt. Background native units were not treated as normalized flux. 0 event timing fits hit a scan edge. Quality-zero fits use exposure integration, local quadratic baselines, red-noise beta and grid floors; flagged-core counts and centroid/background regressions are retained in fit-results.json. Source variability and shape errors may exceed these conditional errors.

Blind rolling-median census covers all available sectors without the old post-gap trim. No off-eclipse census dip exceeds30%of the primary depth outside0.08phase of either fitted eclipse kind. Smaller candidates, gaps, sector edges and all threshold details remain in fit-results.json; this is a diagnostic census, not a calibrated false-positive probability.

## Gaia and physical feasibility

Own-source SB1 covariance verified: bit_index=127,15 correlations in P,gamma,K1,e,omega,Tp order; omega-Tp correlation=0.99966836. Primary assigned conjunctionA; period discrepancy=-0.532sigma.
ConjunctionA at Gaia epoch: offset=0.012333d, Gaia-only sigma=0.015010d; including photometric extrapolation sigma=0.015025d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.
ConjunctionB at Gaia epoch: offset=0.996579d, Gaia-only sigma=0.008721d; including photometric extrapolation sigma=0.008747d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.

Mass-function/assumed-stellar-radius checks (not measured binary parameters):

```json
[
  {
    "m1": 1.225,
    "m2_min": 0.38348180443751545,
    "f_mass": 0.021797263881794683,
    "a_rsun": 7.880635700035171,
    "r1_rsun": 1.46735,
    "r2_approx_rsun": 0.46451079345321333,
    "central_T14_hours": {
      "A": 3.724241547042809,
      "B": 3.8426873934471626
    },
    "observed_T14_hours": 2.4769241379310345
  }
]
```

Limb-darkened two-sphere feasibility permits free primary/secondary flux scales and fixed TIC stellar dimensions. It does not identify the foreground component from eclipse depth alone. Using Gaia primary spectroscopic omega and positive RV away from the observer, at A (nu+omega=90deg) the RV primary is behind and the companion is foreground; at B (270deg) the primary is foreground. The deeper eclipse is assigned A here; luminosity and component labeling remain conditional. Minimum RV companion mass and eclipse luminosity/shape jointly allow a stellar companion.

```json
{
  "status": "conditional shape feasibility",
  "best": {
    "chi2": 406.6147734396419,
    "dof": 121,
    "k": 0.35,
    "b_A": 0.76,
    "e_sin_omega": 0.17499999999999988,
    "primary_scale": 0.6531649686670947,
    "secondary_scale": 0.018009764761063012
  },
  "profile_interval_approx_95": {
    "k": [
      0.29999999999999993,
      0.3999999999999999
    ],
    "b_A": [
      0.7250000000000001,
      0.865
    ],
    "e_sin_omega": [
      0.04999999999999993,
      0.1999999999999999
    ]
  },
  "error_inflation": 3.360452673054892,
  "assumptions": "Circular projected chord with eccentric speed factors; fixed TIC R1/M1, u1=.4 u2=.6, free depth scales per kind, event-scatter bin errors and 0.15ppt floor. Contact shape and dilution degeneracies persist. No claim of precise e sin omega.",
  "primary_profile_n": 64,
  "secondary_profile_n": 64
}
```

## Secondary evidence

Optimized secondary phase=0.500215; pooled depth=5.555ppt, empirical error=0.101ppt; 28/28 individually>3sigma. This scan optimizes phase and does not provide a calibrated phase error or global significance. Repeat events, independent reduction, and off-phase controls are more informative than its raw peak S/N.

```json
{
  "bit_index": 127,
  "gaia_primary": "A",
  "gaia_relative_phase_nominal": 0.514752958945282,
  "gaia_relative_phase_quantiles_16_50_84": [
    0.5028053286584397,
    0.5126002222947604,
    0.5232478994997485
  ],
  "gaia_relative_phase_sigma": 0.009847679506689013,
  "gaia_e_cos_omega_quantiles": [
    0.004405492321579887,
    0.01978956972136035,
    0.03651711001651194
  ],
  "gaia_e_sin_omega_quantiles": [
    -0.0028630625834132183,
    0.011006944769087767,
    0.025523306015155546
  ],
  "photometric_phase": 0.5002149473714801,
  "photometric_e_cos_omega_first_order": 0.00033763854157514315,
  "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
  "geometry_status": "conditional shape feasibility",
  "geometry_e_sin_omega_conditional_range": [
    0.04999999999999993,
    0.1999999999999999
  ],
  "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
}
```

|sector|secondary mid BTJD|error d|depth ppt|error ppt|
|---|---:|---:|---:|---:|
|15|1712.7407617|0.002712|6.334|0.578|
|15|1716.7724112|0.002690|6.725|0.554|
|15|1718.8072167|0.003728|4.746|0.620|
|15|1726.8847512|0.003728|5.914|0.679|
|15|1728.8985423|0.002712|5.699|0.574|
|15|1730.9177564|0.003050|5.338|0.572|
|15|1732.9457831|0.003728|5.488|0.635|
|55|2797.7915570|0.002373|6.054|0.473|
|55|2799.8073818|0.002373|5.698|0.492|
|55|2801.8313411|0.002712|5.446|0.524|
|55|2803.8525889|0.003050|4.946|0.509|
|55|2805.8745146|0.003050|4.932|0.598|
|55|2811.9335129|0.002373|4.739|0.452|
|55|2813.9547607|0.002373|6.407|0.523|
|55|2815.9705854|0.002373|5.149|0.532|
|55|2817.9945448|0.002034|5.922|0.470|
|55|2820.0185041|0.003050|4.335|0.522|
|55|2824.0535430|0.002373|5.459|0.521|
|82|3535.2968684|0.002034|6.232|0.457|
|82|3537.3221835|0.002034|5.192|0.467|
|82|3541.3599339|0.001695|5.544|0.452|
|82|3543.3791481|0.002712|5.376|0.626|
|82|3547.4189322|0.002034|6.003|0.457|
|82|3549.4374684|0.002373|5.687|0.463|
|82|3551.4573605|0.002712|5.370|0.464|
|82|3553.4799641|0.001695|5.643|0.464|
|82|3555.5018897|0.001695|5.459|0.477|
|82|3557.5211039|0.003389|5.416|0.695|

Secondary ephemeris: {"P": 2.020574908592863, "P_error": 1.9481989092571177e-06, "Tref": 2801.8285105165855, "Tref_error": 0.000642512030683303, "reference_cycle": 538, "T0": 1714.7592096936253, "chi2": 47.113966495630685, "dof": 26, "n": 28, "oc_rms_minutes": 5.0529832295951245}. Two-event periods and optimized shapes are not precise independent orbit constraints. Covered/uncovered/flagged secondary windows are enumerated individually in orbit-gates.json secondary_windows, and null-secondary.json when applicable.

## Independence and source attribution

TARS sector82, exact FITS identity validated=True. Same TESS pixels through a different reduction, not another observatory. Exact product/time coverage/URLs/SHA256 are in independent manifests; every measured event and degree1/2 background/baseline comparison is in independent-summary.json (alternate summary for345589621).

```json
{
  "tc": 3534.286031114435,
  "qlp": {
    "1": {
      "depth": 0.06632714692680686,
      "error": 0.0007571202785204066,
      "red_noise_beta": 1.6894819126436342,
      "n_core": 45,
      "baseline_degree": 1,
      "background_regressed_depth": 0.06606653037798706,
      "background_template_native_sigma": -0.6750000621966564
    },
    "2": {
      "depth": 0.06508582233867669,
      "error": 0.0005167555412750362,
      "red_noise_beta": 1.1187856010307209,
      "n_core": 45,
      "baseline_degree": 2,
      "background_regressed_depth": 0.06479885502601164,
      "background_template_native_sigma": -0.7118204707611383
    }
  },
  "independent": {
    "FLUX": {
      "1": {
        "depth": 0.06070331304734206,
        "error": 0.0008661550419790073,
        "red_noise_beta": 1.695868593231188,
        "n_core": 45,
        "baseline_degree": 1,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      },
      "2": {
        "depth": 0.059587036892043595,
        "error": 0.0007103550833787949,
        "red_noise_beta": 1.312385491712957,
        "n_core": 45,
        "baseline_degree": 2,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      }
    }
  }
}
```

```json
{
  "tc": 3536.306595743863,
  "qlp": {
    "1": {
      "depth": 0.06574393277427075,
      "error": 0.0007212640191589774,
      "red_noise_beta": 1.6424688802003156,
      "n_core": 45,
      "baseline_degree": 1,
      "background_regressed_depth": 0.06562384288193808,
      "background_template_native_sigma": -0.33686693829468967
    },
    "2": {
      "depth": 0.06490440449452724,
      "error": 0.0006155739692819678,
      "red_noise_beta": 1.3099347620520052,
      "n_core": 45,
      "baseline_degree": 2,
      "background_regressed_depth": 0.0647660719648585,
      "background_template_native_sigma": -0.37573087353344803
    }
  },
  "independent": {
    "FLUX": {
      "1": {
        "depth": 0.06181594136039163,
        "error": 0.000670178974250891,
        "red_noise_beta": 1.2978879222773796,
        "n_core": 45,
        "baseline_degree": 1,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      },
      "2": {
        "depth": 0.06103010705403677,
        "error": 0.000595145186187066,
        "red_noise_beta": 1.0643042051224818,
        "n_core": 45,
        "baseline_degree": 2,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      }
    }
  }
}
```

Batch difference image: sector82, deficit-minus-light=6.95arcsec; deficit-minus-WCS=2.58arcsec; PSF fractional residual=0.348. Duplicate legacy/new-schema rows are a single observation. Relative light/deficit offsets receive more weight than uncalibrated WCS offsets.

Neighbor dilution within60arcsec, G<15 (Gaia G approximates TESS; not a color-corrected flux ratio):

```json
[
  {
    "source_id": "1866269770941896704",
    "ra": "314.55606991437077",
    "dec": "33.49908260749376",
    "phot_g_mean_mag": "13.844145",
    "bp_rp": "1.5537663",
    "sep": "11.982427639472563",
    "required_fraction_G_approx": 0.7205101623427412,
    "capable": true
  },
  {
    "source_id": "1866269740889217792",
    "ra": "314.5529659749947",
    "dec": "33.48117007892408",
    "phot_g_mean_mag": "13.662389",
    "bp_rp": "0.76188564",
    "sep": "58.220486692174504",
    "required_fraction_G_approx": 0.6094494797392379,
    "capable": true
  }
]
```

pixel-localization.json:
```json
{
  "calibration": {
    "sigma_pixels": 0.55,
    "dx_pixels": 0.4999999999999998,
    "dy_pixels": -1.1102230246251565e-16
  },
  "free_best": {
    "chi2": 47315.681498489655,
    "pixel_x": 7.174194900952417,
    "pixel_y": 7.3476791902740874,
    "distance_from_target_arcsec": 10.707940978544986,
    "fractional_residual": 0.1715812765169125
  },
  "fixed_fits": [
    {
      "source_id": "1866269775241800320",
      "sep_arcsec": 0.0,
      "G": 11.230027,
      "chi2": 165759.92220863828,
      "amplitude": 102.62168405392656,
      "fractional_residual": 0.5725200452773824
    },
    {
      "source_id": "1866269770941896704",
      "sep_arcsec": 11.982427639472563,
      "G": 13.844145,
      "chi2": 46144.81675599125,
      "amplitude": 193.11354889769873,
      "fractional_residual": 0.17752679146606454
    },
    {
      "source_id": "1866269740889217792",
      "sep_arcsec": 58.220486692174504,
      "G": 13.662389,
      "chi2": 304064.04866461636,
      "amplitude": 1.3928228462623233,
      "fractional_residual": 0.9842874784762555
    }
  ],
  "caution": "Same TESS pixels as QLP, independent aperture reduction. Approximate circular Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity."
}
```
Individual event source comparisons are in pixel-localization.json; approximate PSF chi-square excludes model/correlated-noise errors and is not formal localization significance.

pixel-localization-elliptical.json:
```json
{
  "calibration": {
    "sigma_pixels": [
      0.7,
      0.7
    ],
    "dx_pixels": 0.5999999999999996,
    "dy_pixels": -2.220446049250313e-16
  },
  "free_best": {
    "chi2": 26273.92467241758,
    "pixel_x": 6.974194900952417,
    "pixel_y": 7.447679190274087,
    "distance_from_target_arcsec": 14.700000000000097,
    "fractional_residual": 0.19155541550787739
  },
  "fixed_fits": [
    {
      "source_id": "1866269775241800320",
      "sep_arcsec": 0.0,
      "G": 11.230027,
      "chi2": 186693.57804486455,
      "amplitude": 56.19139872628159,
      "fractional_residual": 0.6853134991794976
    },
    {
      "source_id": "1866269770941896704",
      "sep_arcsec": 11.982427639472563,
      "G": 13.844145,
      "chi2": 36479.33196592168,
      "amplitude": 123.29976294843169,
      "fractional_residual": 0.16788037749808551
    },
    {
      "source_id": "1866269740889217792",
      "sep_arcsec": 58.220486692174504,
      "G": 13.662389,
      "chi2": 304002.94721909065,
      "amplitude": 1.3085051972427295,
      "fractional_residual": 0.984317723110925
    }
  ],
  "caution": "Same TESS pixels as QLP, independent aperture reduction. Approximate axis-aligned elliptical Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity."
}
```
Individual event source comparisons are in pixel-localization-elliptical.json; approximate PSF chi-square excludes model/correlated-noise errors and is not formal localization significance.

pixel-localization-positive.json:
```json
{
  "calibration": {
    "sigma_pixels": [
      0.7,
      0.7
    ],
    "dx_pixels": 0.3999999999999997,
    "dy_pixels": -2.220446049250313e-16
  },
  "free_best": {
    "chi2": 26273.924672417565,
    "pixel_x": 7.174194900952417,
    "pixel_y": 7.447679190274087,
    "distance_from_target_arcsec": 10.500000000000112,
    "fractional_residual": 0.19155541550787775
  },
  "fixed_fits": [
    {
      "source_id": "1866269775241800320",
      "sep_arcsec": 0.0,
      "G": 11.230027,
      "chi2": 133137.82774795697,
      "amplitude": 80.14175383076574,
      "fractional_residual": 0.5085662599239503
    },
    {
      "source_id": "1866269770941896704",
      "sep_arcsec": 11.982427639472563,
      "G": 13.844145,
      "chi2": 26903.62283595638,
      "amplitude": 128.05529719714332,
      "fractional_residual": 0.22544469831837582
    },
    {
      "source_id": "1866269740889217792",
      "sep_arcsec": 58.220486692174504,
      "G": 13.662389,
      "chi2": 303719.1677772248,
      "amplitude": 2.1538533515932112,
      "fractional_residual": 0.9843339355969052
    }
  ],
  "caution": "Same TESS pixels as QLP, independent aperture reduction. Approximate axis-aligned elliptical Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity."
}
```
Individual event source comparisons are in pixel-localization-positive.json; approximate PSF chi-square excludes model/correlated-noise errors and is not formal localization significance.

pixel-localization-fluxratio.json:
```json
{
  "calibration": {
    "sigma_pixels": [
      0.7,
      0.7
    ],
    "dx_pixels": -2.220446049250313e-16,
    "dy_pixels": -0.20000000000000018
  },
  "free_best": {
    "chi2": 26273.924672417525,
    "pixel_x": 7.574194900952415,
    "pixel_y": 7.647679190274086,
    "distance_from_target_arcsec": 4.695742752749475,
    "fractional_residual": 0.1915554155078779
  },
  "fixed_fits": [
    {
      "source_id": "1866269775241800320",
      "sep_arcsec": 0.0,
      "G": 11.230027,
      "chi2": 42437.805542130925,
      "amplitude": 119.57535410526069,
      "fractional_residual": 0.21969839118602286
    },
    {
      "source_id": "1866269770941896704",
      "sep_arcsec": 11.982427639472563,
      "G": 13.844145,
      "chi2": 112342.19144314181,
      "amplitude": 89.33836039100534,
      "fractional_residual": 0.5790939719413017
    },
    {
      "source_id": "1866269740889217792",
      "sep_arcsec": 58.220486692174504,
      "G": 13.662389,
      "chi2": 301198.37961262884,
      "amplitude": 5.549090714620524,
      "fractional_residual": 0.9837094551282867
    }
  ],
  "caution": "Same TESS pixels as QLP, independent aperture reduction. Approximate axis-aligned elliptical Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity."
}
```
Individual event source comparisons are in pixel-localization-fluxratio.json; approximate PSF chi-square excludes model/correlated-noise errors and is not formal localization significance.

## Current archives and novelty

SIMBAD exact Gaia-ID: [{"id": "Gaia DR3 1866269775241800320", "main_id": "TYC 2692-150-1", "otype": "SB*", "ra": "314.55257938221996", "dec": "33.4973524698"}]. This SB* classification establishes spectroscopy, not a prior eclipse discovery. Gaia vari_eclipsing_binary rows=0; vari_summary=[]; current ExoFOP={"toi_count": 0, "ctoi_count": 0}.
Fresh shared VSX60arcsec result: {"B_vsx_vsx": []}. ROT is not prior eclipse classification. A cone neighbor must not be assigned to target.

Nine-catalog IDIA and Harvard cone requests each timed out (idia-receipts.json and idia-mirror-receipts.json). Consequently ASAS-SN, SB9, WDS, Kostov2/3/4, IJspeert and Prsa current per-object coverage is unavailable, not empty. Batched exact-name web queries on2026-10-30 returned no relevant source and do not prove novelty. Shared source receipts preserve current Gaia/VSX/SIMBAD/ExoFOP query provenance. The original paper/source records were checked live and remain unchanged.

## Follow-up and predictions

Obtain a calibrated empirical TESS PRF with color-dependent neighbor fluxes or ground-based resolved eclipse photometry of the target and12arcsec neighbor.
Next fitted primary after2026-10-30: BTJD4344.53469, conditional linear-ephemeris1sigma=0.00043d. Next secondary template phase: BTJD4343.52484; phase/systematic uncertainty is uncalibrated, so do not use it as a precise scheduling window. For undetected secondary kinds use the Gaia covariance windows, not this optimized scan prediction.

Reviewed by fresh Sol lead G with fresh GPT-6.1 Terra numerical helper; measurements and script assumptions were independently inspected.