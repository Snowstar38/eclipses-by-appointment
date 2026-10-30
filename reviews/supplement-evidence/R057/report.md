# TIC 345050437: CONFIRMED

Thirty-three primaries and repeated secondaries establish a coherent EB. The old high PSF residual is not accepted uncritically: fresh template regression favors the target in every usable sector24 event and its free centroid is only2.97 arcsec away. A known E-type variable44.25 arcsec away has period2.5355d, inconsistent with the target4.48083d clock. Elevated geometry chi-square precludes precise radii/orbit claims.

Full review: COMPLETED_WITH_ARCHIVE_LIMITATION. Physical verdict is separate from novelty. Novelty: LIMITED_PRIOR_ART_COVERAGE; no prior target EB was established by the available current sources. New nine-catalog passes to both IDIA and Harvard timed out and are not negative matches.

## Raw SAP and event measurements

Primary P=4.480834621 +/- 0.000001500 d; Tref=2910.6551981 +/- 0.0001744 BTJD at cycle255; T0=1768.0423698. 33 fitted primary events, O-C RMS=1.518 min; chi2/dof=47.90/31. Shape T14=3.670h, profile range=[0.14927586206896548, 0.15651724137931033], ingress fraction=0.35; T12=fr*T14 and nominal T23=T14-2*T12. Trapezoid flat time is not totality for grazing systems.

|sector|mid BTJD|error d|depth ppt|error ppt|O-C min|flagged core|
|---|---:|---:|---:|---:|---:|---:|
|17|1768.0405000|0.002690|63.258|0.862|-2.693|2|
|17|1781.4830276|0.002126|64.164|1.133|-2.658|0|
|17|1785.9638701|0.002126|61.973|0.785|-2.647|0|
|24|1956.2368033|0.002273|66.176|0.811|-0.894|0|
|24|1960.7158110|0.002273|69.063|0.854|-3.524|0|
|24|1965.1984883|0.002455|67.042|1.182|-0.871|1|
|24|1969.6774961|0.002273|64.284|2.107|-3.502|0|
|24|1974.1601733|0.002273|67.753|1.005|-0.848|0|
|24|1978.6410159|0.002126|66.248|0.847|-0.837|0|
|57|2856.8879848|0.000917|65.935|1.804|4.035|0|
|57|2861.3660751|0.000459|64.653|0.540|0.083|0|
|57|2870.3277602|0.000459|64.925|0.531|0.106|0|
|57|2879.2894452|0.000459|65.006|0.658|0.129|0|
|58|2883.7702878|0.000459|62.257|1.001|0.140|0|
|58|2888.2502129|0.000459|64.256|0.789|-1.169|1|
|58|2892.7328902|0.000917|60.170|1.978|1.484|0|
|58|2901.6936578|0.000459|61.906|0.973|0.186|0|
|58|2906.1745004|0.000459|62.911|0.832|0.197|0|
|77|3399.0662603|0.000459|65.241|0.836|0.128|0|
|77|3403.5471028|0.000459|65.296|0.869|0.139|1|
|77|3421.4713903|0.000459|64.815|0.757|1.505|1|
|78|3439.3929256|0.000459|66.309|0.572|-1.091|0|
|78|3443.8756029|0.000459|64.791|0.797|1.562|0|
|78|3448.3555280|0.000459|65.014|0.651|0.253|0|
|84|3587.2607288|0.000459|73.145|1.467|-0.716|0|
|84|3591.7424887|0.000459|64.233|0.583|0.617|0|
|84|3600.7041737|0.000459|65.542|0.639|0.639|0|
|84|3605.1840989|0.000917|60.120|2.160|-0.670|0|
|84|3609.6649414|0.000459|64.949|1.022|-0.659|0|
|85|3614.1467013|0.000459|63.183|0.608|0.674|0|
|85|3618.6266265|0.000459|63.938|0.714|-0.636|0|
|85|3623.1074690|0.000459|62.384|1.369|-0.625|5|
|85|3632.0682366|0.000459|62.772|0.552|-1.923|0|

Primary median depth=64.791ppt; maximum absolute background-regression fake depth=1.579ppt. Background native units were not treated as normalized flux. 0 event timing fits hit a scan edge. Quality-zero fits use exposure integration, local quadratic baselines, red-noise beta and grid floors; flagged-core counts and centroid/background regressions are retained in fit-results.json. Source variability and shape errors may exceed these conditional errors.

Blind rolling-median census covers all available sectors without the old post-gap trim. No off-eclipse census dip exceeds30%of the primary depth outside0.08phase of either fitted eclipse kind. Smaller candidates, gaps, sector edges and all threshold details remain in fit-results.json; this is a diagnostic census, not a calibrated false-positive probability.

## Gaia and physical feasibility

Own-source SB1 covariance verified: bit_index=127,15 correlations in P,gamma,K1,e,omega,Tp order; omega-Tp correlation=0.9999283. Primary assigned conjunctionA; period discrepancy=-1.904sigma.
ConjunctionA at Gaia epoch: offset=-0.003781d, Gaia-only sigma=0.022320d; including photometric extrapolation sigma=0.022336d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.
ConjunctionB at Gaia epoch: offset=2.220511d, Gaia-only sigma=0.020657d; including photometric extrapolation sigma=0.020675d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.

Mass-function/assumed-stellar-radius checks (not measured binary parameters):

```json
[
  {
    "m1": 0.9,
    "m2_min": 0.4565141915123945,
    "f_mass": 0.05170281215759653,
    "a_rsun": 12.662074986282596,
    "r1_rsun": 1.08915,
    "r2_approx_rsun": 0.5340272595790694,
    "central_T14_hours": {
      "A": 4.352033694299332,
      "B": 4.424834246325007
    },
    "observed_T14_hours": 3.66951724137931
  },
  {
    "m1": 1.2,
    "m2_min": 0.5386596407959161,
    "f_mass": 0.05170281215759653,
    "a_rsun": 13.754188064991082,
    "r1_rsun": 1.08915,
    "r2_approx_rsun": 0.6096092521064337,
    "central_T14_hours": {
      "A": 4.193030846537644,
      "B": 4.263171608703266
    },
    "observed_T14_hours": 3.66951724137931
  },
  {
    "m1": 1.6,
    "m2_min": 0.6372582512480045,
    "f_mass": 0.05170281215759653,
    "a_rsun": 14.960133650254367,
    "r1_rsun": 1.08915,
    "r2_approx_rsun": 0.6973525189018747,
    "central_T14_hours": {
      "A": 4.0541455829552095,
      "B": 4.121963080971872
    },
    "observed_T14_hours": 3.66951724137931
  }
]
```

Limb-darkened two-sphere feasibility permits free primary/secondary flux scales and fixed TIC stellar dimensions. It does not identify the foreground component from eclipse depth alone. Using Gaia primary spectroscopic omega and positive RV away from the observer, at A (nu+omega=90deg) the RV primary is behind and the companion is foreground; at B (270deg) the primary is foreground. The deeper eclipse is assigned A here; luminosity and component labeling remain conditional. Minimum RV companion mass and eclipse luminosity/shape jointly allow a stellar companion.

```json
{
  "status": "conditional shape feasibility",
  "best": {
    "chi2": 350.28861292667847,
    "dof": 121,
    "k": 0.44999999999999996,
    "b_A": 0.5150000000000001,
    "e_sin_omega": -0.10000000000000003,
    "primary_scale": 0.3141153485690935,
    "secondary_scale": 0.008500752548683271
  },
  "profile_interval_approx_95": {
    "k": [
      0.44999999999999996,
      0.44999999999999996
    ],
    "b_A": [
      0.5150000000000001,
      0.585
    ],
    "e_sin_omega": [
      -0.12500000000000003,
      -0.10000000000000003
    ]
  },
  "error_inflation": 2.89494721427007,
  "assumptions": "Circular projected chord with eccentric speed factors; fixed TIC R1/M1, u1=.4 u2=.6, free depth scales per kind, event-scatter bin errors and 0.15ppt floor. Contact shape and dilution degeneracies persist. No claim of precise e sin omega.",
  "primary_profile_n": 64,
  "secondary_profile_n": 64
}
```

## Secondary evidence

Optimized secondary phase=0.500743; pooled depth=8.053ppt, empirical error=0.310ppt; 34/37 individually>3sigma. This scan optimizes phase and does not provide a calibrated phase error or global significance. Repeat events, independent reduction, and off-phase controls are more informative than its raw peak S/N.

```json
{
  "bit_index": 127,
  "gaia_primary": "A",
  "gaia_relative_phase_nominal": 0.5055202121952085,
  "gaia_relative_phase_quantiles_16_50_84": [
    0.49673731135095534,
    0.503280255570373,
    0.511822094639491
  ],
  "gaia_relative_phase_sigma": 0.00864590819504258,
  "gaia_e_cos_omega_quantiles": [
    -0.005123750498972375,
    0.005151058698107992,
    0.018568974484470233
  ],
  "gaia_e_sin_omega_quantiles": [
    -0.003993631637848673,
    0.005677233822333128,
    0.019493104206848237
  ],
  "photometric_phase": 0.5007430849291679,
  "photometric_e_cos_omega_first_order": 0.0011672350772335184,
  "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
  "geometry_status": "conditional shape feasibility",
  "geometry_e_sin_omega_conditional_range": [
    -0.12500000000000003,
    -0.10000000000000003
  ],
  "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
}
```

|sector|secondary mid BTJD|error d|depth ppt|error ppt|
|---|---:|---:|---:|---:|
|17|1770.2907036|0.005046|6.153|0.798|
|17|1779.2661336|0.009632|10.538|1.871|
|17|1783.7249511|0.003670|6.752|0.594|
|24|1958.4784187|0.005504|7.445|0.936|
|24|1962.9620054|0.004128|7.363|0.781|
|24|1967.4382532|0.007339|8.291|1.333|
|24|1971.9502787|0.013761|9.407|2.354|
|24|1976.3999224|0.003211|8.136|0.645|
|24|1980.8853439|0.002752|9.720|0.625|
|57|2854.6380038|0.016972|4.268|2.182|
|57|2859.1215906|0.003670|9.650|0.992|
|57|2868.0878467|0.002752|7.532|0.710|
|57|2872.5714334|0.005046|8.591|1.044|
|57|2877.0513507|0.024311|3.271|2.366|
|57|2881.5285158|0.001376|8.604|0.464|
|58|2886.0157721|0.004587|8.398|0.962|
|58|2890.4938546|0.003211|9.052|0.752|
|58|2894.9856977|0.006880|13.571|1.824|
|58|2899.4536890|0.002293|6.826|0.567|
|58|2903.9354410|0.003211|8.270|0.750|
|58|2908.4116888|0.002752|9.000|0.588|
|77|3396.8235798|0.018806|3.773|2.249|
|77|3401.3044144|0.002752|7.833|0.532|
|77|3405.7916707|0.003670|7.165|0.747|
|77|3419.2341746|0.002752|8.263|0.607|
|78|3437.1520088|0.002752|8.748|0.782|
|78|3441.6310086|0.005046|6.482|0.841|
|78|3446.1145954|0.002293|8.642|0.489|
|84|3585.0259729|0.005046|7.311|1.105|
|84|3589.4967164|0.011467|5.665|1.712|
|84|3593.9839726|0.001835|8.085|0.453|
|84|3598.4693941|0.005504|6.148|0.996|
|84|3602.9456419|0.004128|9.436|1.087|
|84|3607.4558326|0.010091|10.111|2.060|
|85|3616.3927326|0.002752|9.401|0.658|
|85|3620.8662282|0.001835|7.851|0.391|
|85|3634.3023104|0.004587|7.351|0.768|

Secondary ephemeris: {"P": 4.4808319786037885, "P_error": 5.409492670163906e-06, "Tref": 2912.896438265481, "Tref_error": 0.0006805155783497134, "reference_cycle": 255, "T0": 1770.2842837215148, "chi2": 47.73252386567204, "dof": 32, "n": 34, "oc_rms_minutes": 12.164741998817926}. Two-event periods and optimized shapes are not precise independent orbit constraints. Covered/uncovered/flagged secondary windows are enumerated individually in orbit-gates.json secondary_windows, and null-secondary.json when applicable.

## Independence and source attribution

TARS sector24, exact FITS identity validated=True. Same TESS pixels through a different reduction, not another observatory. Exact product/time coverage/URLs/SHA256 are in independent manifests; every measured event and degree1/2 background/baseline comparison is in independent-summary.json (alternate summary for345589621).

```json
{
  "tc": 1956.236803265395,
  "qlp": {
    "1": {
      "depth": 0.06645511892419378,
      "error": 0.000755561014613154,
      "red_noise_beta": 1.1136289997349256,
      "n_core": 7,
      "baseline_degree": 1,
      "background_regressed_depth": 0.06618119316628734,
      "background_template_native_sigma": -0.8281131610642404
    },
    "2": {
      "depth": 0.06628522694414007,
      "error": 0.0008369618879326378,
      "red_noise_beta": 1.0970671419745532,
      "n_core": 7,
      "baseline_degree": 2,
      "background_regressed_depth": 0.06616293083817126,
      "background_template_native_sigma": -0.1728613681302516
    }
  },
  "independent": {
    "FLUX": {
      "1": {
        "depth": 0.061070363448494584,
        "error": 0.0017553930763530643,
        "red_noise_beta": 1.2571522617855257,
        "n_core": 7,
        "baseline_degree": 1,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      },
      "2": {
        "depth": 0.06363394266684382,
        "error": 0.0016147786880699835,
        "red_noise_beta": 1.2797488779993245,
        "n_core": 7,
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
  "tc": 1960.7158110278717,
  "qlp": {
    "1": {
      "depth": 0.06900039186511787,
      "error": 0.0008746875033901591,
      "red_noise_beta": 1.2104800142767422,
      "n_core": 7,
      "baseline_degree": 1,
      "background_regressed_depth": 0.06946905757910311,
      "background_template_native_sigma": 0.8038477578531368
    },
    "2": {
      "depth": 0.06926760681753494,
      "error": 0.0009814149536555125,
      "red_noise_beta": 1.2209212300146388,
      "n_core": 7,
      "baseline_degree": 2,
      "background_regressed_depth": 0.06942456198162125,
      "background_template_native_sigma": 0.26466868079975486
    }
  },
  "independent": {
    "FLUX": {
      "1": {
        "depth": 0.06049487917754053,
        "error": 0.0009592494724983237,
        "red_noise_beta": 1.043133779087984,
        "n_core": 7,
        "baseline_degree": 1,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      },
      "2": {
        "depth": 0.06084796925770194,
        "error": 0.0010703109094375098,
        "red_noise_beta": 1.046870845821653,
        "n_core": 7,
        "baseline_degree": 2,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      }
    }
  }
}
```

Batch difference image: sector24, deficit-minus-light=2.7arcsec; deficit-minus-WCS=2.81arcsec; PSF fractional residual=0.848. Duplicate legacy/new-schema rows are a single observation. Relative light/deficit offsets receive more weight than uncalibrated WCS offsets.

Neighbor dilution within60arcsec, G<15 (Gaia G approximates TESS; not a color-corrected flux ratio):

```json
[
  {
    "source_id": "2011135380006552832",
    "ra": "355.3461946027936",
    "dec": "59.525463809467325",
    "phot_g_mean_mag": "14.965737",
    "bp_rp": "2.291256",
    "sep": "23.196200041677034",
    "required_fraction_G_approx": 1.6076962265747736,
    "capable": false
  }
]
```

pixel-localization.json:
```json
{
  "calibration": {
    "sigma_pixels": 0.45,
    "dx_pixels": -0.10000000000000009,
    "dy_pixels": -0.10000000000000009
  },
  "free_best": {
    "chi2": 1770.9734435675846,
    "pixel_x": 7.739989671941279,
    "pixel_y": 7.834463584517652,
    "distance_from_target_arcsec": 2.969848480983278,
    "fractional_residual": 0.22305336449585392
  },
  "fixed_fits": [
    {
      "source_id": "2011135311287080704",
      "sep_arcsec": 0.0,
      "G": 11.479009,
      "chi2": 1981.1935672920263,
      "amplitude": 231.18128046755353,
      "fractional_residual": 0.24112415322488306
    },
    {
      "source_id": "2011135380006552832",
      "sep_arcsec": 23.196200041677034,
      "G": 14.965737,
      "chi2": 12840.70754461235,
      "amplitude": 95.78201985484202,
      "fractional_residual": 0.8014067555286477
    }
  ],
  "caution": "Same TESS pixels as QLP, independent aperture reduction. Approximate circular Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity."
}
```
Individual event source comparisons are in pixel-localization.json; approximate PSF chi-square excludes model/correlated-noise errors and is not formal localization significance.

## Current archives and novelty

SIMBAD exact Gaia-ID: [{"id": "Gaia DR3 2011135311287080704", "main_id": "TYC 4012-825-1", "otype": "SB*", "ra": "355.34922032052", "dec": "59.51927035952001"}]. This SB* classification establishes spectroscopy, not a prior eclipse discovery. Gaia vari_eclipsing_binary rows=0; vari_summary=[]; current ExoFOP={"toi_count": 0, "ctoi_count": 0}.
Fresh shared VSX60arcsec result: {"B_vsx_vsx": [{"_r": "44.25", "Name": "Gaia DR3 2011136788755832704", "Type": "E", "Period": "2.535500000000", "RAJ2000": "355.37332", "DEJ2000": "59.52063"}]}. ROT is not prior eclipse classification. A cone neighbor must not be assigned to target.

Nine-catalog IDIA and Harvard cone requests each timed out (idia-receipts.json and idia-mirror-receipts.json). Consequently ASAS-SN, SB9, WDS, Kostov2/3/4, IJspeert and Prsa current per-object coverage is unavailable, not empty. Batched exact-name web queries on2026-10-30 returned no relevant source and do not prove novelty. Shared source receipts preserve current Gaia/VSX/SIMBAD/ExoFOP query provenance. The original paper/source records were checked live and remain unchanged.

## Follow-up and predictions

Refine stellar radii, light ratio and RV/eclipsing joint orbit with resolved photometry or spectroscopy; retry unavailable catalogs before any novelty claim.
Next fitted primary after2026-10-30: BTJD4344.52228, conditional linear-ephemeris1sigma=0.00051d. Next secondary template phase: BTJD4346.76602; phase/systematic uncertainty is uncalibrated, so do not use it as a precise scheduling window. For undetected secondary kinds use the Gaia covariance windows, not this optimized scan prediction.

Reviewed by fresh Sol lead G with fresh GPT-6.1 Terra numerical helper; measurements and script assumptions were independently inspected.