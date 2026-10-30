# TIC 415751695: CONFIRMED

Twenty-one primaries and twenty secondary events plus independent TARS recovery establish a repeated EB. The old PSF residual0.931 is addressed by fresh regression: free deficit centroid2.97arcsec from target with fractional residual0.177 and no G<15 capable neighbor. No precise parameter inference follows from this approximate PSF model.

Full review: COMPLETED_WITH_ARCHIVE_LIMITATION. Physical verdict is separate from novelty. Novelty: LIMITED_PRIOR_ART_COVERAGE; no prior target EB was established by the available current sources. New nine-catalog passes to both IDIA and Harvard timed out and are not negative matches.

## Raw SAP and event measurements

Primary P=4.995996617 +/- 0.000000890 d; Tref=3038.5788104 +/- 0.0001250 BTJD at cycle298; T0=1549.7718185. 21 fitted primary events, O-C RMS=0.662 min; chi2/dof=17.58/19. Shape T14=4.017h, profile range=[0.16375862068965513, 0.17099999999999999], ingress fraction=0.25; T12=fr*T14 and nominal T23=T14-2*T12. Trapezoid flat time is not totality for grazing systems.

|sector|mid BTJD|error d|depth ppt|error ppt|O-C min|flagged core|
|---|---:|---:|---:|---:|---:|---:|
|9|1549.7717914|0.002273|59.973|0.402|-0.039|1|
|9|1554.7677764|0.002690|59.475|0.451|-0.056|3|
|9|1564.7597464|0.002126|60.189|0.432|-0.089|0|
|36|2284.1835911|0.000502|64.402|0.415|0.389|0|
|36|2289.1785718|0.000502|63.866|0.381|-1.074|1|
|36|2299.1715460|0.000502|64.795|0.417|0.338|3|
|36|2304.1675310|0.000502|63.828|0.445|0.322|2|
|63|3018.5953908|0.000502|62.993|0.395|0.816|0|
|63|3023.5903715|0.000502|63.181|0.357|-0.647|0|
|63|3028.5863565|0.000502|63.239|0.326|-0.663|0|
|63|3033.5833457|0.000502|62.276|0.478|0.766|2|
|63|3038.5783264|0.000502|62.947|0.387|-0.697|1|
|90|3748.0102012|0.000502|61.679|0.375|-0.186|0|
|90|3753.0061862|0.000502|61.590|0.362|-0.202|0|
|90|3758.0031754|0.000502|61.390|0.341|1.227|0|
|90|3762.9991604|0.000502|61.640|0.384|1.210|0|
|90|3767.9941411|0.000502|60.656|0.593|-0.253|2|
|90|3772.9901261|0.000502|61.139|0.486|-0.269|2|
|100|4077.7462138|0.000502|55.706|0.320|0.154|0|
|100|4082.7421987|0.000502|56.014|0.346|0.137|0|
|100|4097.7291494|0.000502|55.940|0.296|-1.359|0|

Primary median depth=61.640ppt; maximum absolute background-regression fake depth=0.744ppt. Background native units were not treated as normalized flux. 0 event timing fits hit a scan edge. Quality-zero fits use exposure integration, local quadratic baselines, red-noise beta and grid floors; flagged-core counts and centroid/background regressions are retained in fit-results.json. Source variability and shape errors may exceed these conditional errors.

Blind rolling-median census covers all available sectors without the old post-gap trim. No off-eclipse census dip exceeds30%of the primary depth outside0.08phase of either fitted eclipse kind. Smaller candidates, gaps, sector edges and all threshold details remain in fit-results.json; this is a diagnostic census, not a calibrated false-positive probability.

## Gaia and physical feasibility

Own-source SB1 covariance verified: bit_index=127,15 correlations in P,gamma,K1,e,omega,Tp order; omega-Tp correlation=0.9995584. Primary assigned conjunctionA; period discrepancy=0.544sigma.
ConjunctionA at Gaia epoch: offset=-0.050309d, Gaia-only sigma=0.050469d; including photometric extrapolation sigma=0.050471d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.
ConjunctionB at Gaia epoch: offset=-2.485075d, Gaia-only sigma=0.043945d; including photometric extrapolation sigma=0.043948d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.

Mass-function/assumed-stellar-radius checks (not measured binary parameters):

```json
[
  {
    "m1": 1.24,
    "m2_min": 0.3253200269770704,
    "f_mass": 0.014051610905027786,
    "a_rsun": 14.279420960348848,
    "r1_rsun": 1.28734,
    "r2_approx_rsun": 0.4072383223929631,
    "central_T14_hours": {
      "A": 4.534153546644391,
      "B": 4.5223599294225565
    },
    "observed_T14_hours": 4.017103448275861
  }
]
```

Limb-darkened two-sphere feasibility permits free primary/secondary flux scales and fixed TIC stellar dimensions. It does not identify the foreground component from eclipse depth alone. Using Gaia primary spectroscopic omega and positive RV away from the observer, at A (nu+omega=90deg) the RV primary is behind and the companion is foreground; at B (270deg) the primary is foreground. The deeper eclipse is assigned A here; luminosity and component labeling remain conditional. Minimum RV companion mass and eclipse luminosity/shape jointly allow a stellar companion.

```json
{
  "status": "conditional shape feasibility",
  "best": {
    "chi2": 112.7818313174603,
    "dof": 121,
    "k": 0.27499999999999997,
    "b_A": 0.375,
    "e_sin_omega": -5.551115123125783e-17,
    "primary_scale": 0.7495084330789565,
    "secondary_scale": 0.003393019985787365
  },
  "profile_interval_approx_95": {
    "k": [
      0.27499999999999997,
      0.27499999999999997
    ],
    "b_A": [
      0.375,
      0.375
    ],
    "e_sin_omega": [
      -5.551115123125783e-17,
      -5.551115123125783e-17
    ]
  },
  "error_inflation": 1,
  "assumptions": "Circular projected chord with eccentric speed factors; fixed TIC R1/M1, u1=.4 u2=.6, free depth scales per kind, event-scatter bin errors and 0.15ppt floor. Contact shape and dilution degeneracies persist. No claim of precise e sin omega.",
  "primary_profile_n": 64,
  "secondary_profile_n": 64
}
```

## Secondary evidence

Optimized secondary phase=0.500364; pooled depth=3.447ppt, empirical error=0.063ppt; 20/20 individually>3sigma. This scan optimizes phase and does not provide a calibrated phase error or global significance. Repeat events, independent reduction, and off-phase controls are more informative than its raw peak S/N.

```json
{
  "bit_index": 127,
  "gaia_primary": "A",
  "gaia_relative_phase_nominal": 0.48708226485372597,
  "gaia_relative_phase_quantiles_16_50_84": [
    0.4716521118126703,
    0.48872067074725734,
    0.4992057440662677
  ],
  "gaia_relative_phase_sigma": 0.015905871809338275,
  "gaia_e_cos_omega_quantiles": [
    -0.04452333067583703,
    -0.01771165573260186,
    -0.0012476113066753707
  ],
  "gaia_e_sin_omega_quantiles": [
    -0.01826477622258167,
    0.0016564655976043854,
    0.034809391413405985
  ],
  "photometric_phase": 0.5003640716992194,
  "photometric_e_cos_omega_first_order": 0.0005718824878237635,
  "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
  "geometry_status": "conditional shape feasibility",
  "geometry_e_sin_omega_conditional_range": [
    -5.551115123125783e-17,
    -5.551115123125783e-17
  ],
  "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
}
```

|sector|secondary mid BTJD|error d|depth ppt|error ppt|
|---|---:|---:|---:|---:|
|9|1552.2674449|0.004191|3.171|0.317|
|9|1562.2646767|0.003143|3.410|0.255|
|9|1567.2606733|0.003667|2.799|0.295|
|36|2286.6820907|0.003143|3.400|0.251|
|36|2291.6833260|0.003667|3.933|0.339|
|36|2296.6782749|0.002619|3.924|0.261|
|36|2301.6679851|0.003667|3.407|0.305|
|63|3016.0934059|0.003667|3.583|0.334|
|63|3021.0946412|0.002619|3.899|0.312|
|63|3026.0822560|0.002095|3.444|0.270|
|63|3031.0866344|0.002095|3.370|0.274|
|63|3036.0847265|0.003143|3.535|0.301|
|90|3750.5101473|0.003667|3.214|0.292|
|90|3755.5103348|0.002619|3.066|0.285|
|90|3765.5002326|0.003667|3.178|0.291|
|90|3770.4878474|0.002619|3.644|0.263|
|100|4075.2499274|0.002095|3.476|0.216|
|100|4080.2480194|0.002095|3.337|0.232|
|100|4090.2326786|0.001572|3.733|0.225|
|100|4095.2307707|0.002095|3.378|0.202|

Secondary ephemeris: {"P": 4.995992343898419, "P_error": 5.284286784174196e-06, "Tref": 3021.093453886058, "Tref_error": 0.0009118139755815085, "reference_cycle": 294, "T0": 1552.2717047799226, "chi2": 38.79656292702458, "dof": 18, "n": 20, "oc_rms_minutes": 5.09305636646804}. Two-event periods and optimized shapes are not precise independent orbit constraints. Covered/uncovered/flagged secondary windows are enumerated individually in orbit-gates.json secondary_windows, and null-secondary.json when applicable.

## Independence and source attribution

TARS sector90, exact FITS identity validated=True. Same TESS pixels through a different reduction, not another observatory. Exact product/time coverage/URLs/SHA256 are in independent manifests; every measured event and degree1/2 background/baseline comparison is in independent-summary.json (alternate summary for345589621).

```json
{
  "tc": 3748.0102012187626,
  "qlp": {
    "1": {
      "depth": 0.06172720560114846,
      "error": 0.0003529641837227917,
      "red_noise_beta": 1.2464413978554645,
      "n_core": 72,
      "baseline_degree": 1,
      "background_regressed_depth": 0.06220986786933617,
      "background_template_native_sigma": 0.5815925001153252
    },
    "2": {
      "depth": 0.06180258851366541,
      "error": 0.00039380018016685846,
      "red_noise_beta": 1.2447585271714376,
      "n_core": 72,
      "baseline_degree": 2,
      "background_regressed_depth": 0.06207641879125174,
      "background_template_native_sigma": 0.3187601725086757
    }
  },
  "independent": {
    "FLUX": {
      "1": {
        "depth": 0.0635751270335014,
        "error": 0.0006117803328877753,
        "red_noise_beta": 1.4043809507897536,
        "n_core": 72,
        "baseline_degree": 1,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      },
      "2": {
        "depth": 0.06385354232253854,
        "error": 0.0006685582578828625,
        "red_noise_beta": 1.375909782910015,
        "n_core": 72,
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
  "tc": 3753.006186192379,
  "qlp": {
    "1": {
      "depth": 0.061444738267793585,
      "error": 0.00034333138225790095,
      "red_noise_beta": 1.2469308018122431,
      "n_core": 72,
      "baseline_degree": 1,
      "background_regressed_depth": 0.061669624999183166,
      "background_template_native_sigma": 0.4121679953241458
    },
    "2": {
      "depth": 0.06159852707260317,
      "error": 0.000378557209084772,
      "red_noise_beta": 1.2320311726047433,
      "n_core": 72,
      "baseline_degree": 2,
      "background_regressed_depth": 0.06180240659779209,
      "background_template_native_sigma": 0.3750345034275165
    }
  },
  "independent": {
    "FLUX": {
      "1": {
        "depth": 0.05993002954599291,
        "error": 0.0007463446653183674,
        "red_noise_beta": 1.4695507929668603,
        "n_core": 72,
        "baseline_degree": 1,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      },
      "2": {
        "depth": 0.06078209752046338,
        "error": 0.0007718792333783774,
        "red_noise_beta": 1.378342899171527,
        "n_core": 72,
        "baseline_degree": 2,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      }
    }
  }
}
```

Batch difference image: sector90, deficit-minus-light=3.54arcsec; deficit-minus-WCS=1.47arcsec; PSF fractional residual=0.931. Duplicate legacy/new-schema rows are a single observation. Relative light/deficit offsets receive more weight than uncalibrated WCS offsets.

Neighbor dilution within60arcsec, G<15 (Gaia G approximates TESS; not a color-corrected flux ratio):

```json
[]
```

pixel-localization.json:
```json
{
  "calibration": {
    "sigma_pixels": 0.6500000000000001,
    "dx_pixels": -0.10000000000000009,
    "dy_pixels": 0.09999999999999987
  },
  "free_best": {
    "chi2": 25838.78000245633,
    "pixel_x": 7.241803277952407,
    "pixel_y": 7.167631316672429,
    "distance_from_target_arcsec": 2.9698484809834893,
    "fractional_residual": 0.17674795147329955
  },
  "fixed_fits": [
    {
      "source_id": "3549629597848975872",
      "sep_arcsec": 0.0,
      "G": 11.403031,
      "chi2": 28800.380434301325,
      "amplitude": 115.46216951474243,
      "fractional_residual": 0.19390534966841602
    }
  ],
  "caution": "Same TESS pixels as QLP, independent aperture reduction. Approximate circular Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity."
}
```
Individual event source comparisons are in pixel-localization.json; approximate PSF chi-square excludes model/correlated-noise errors and is not formal localization significance.

## Current archives and novelty

SIMBAD exact Gaia-ID: [{"id": "Gaia DR3 3549629597848975872", "main_id": "TYC 6082-305-1", "otype": "SB*", "ra": "164.63570637693", "dec": "-22.10958257191"}]. This SB* classification establishes spectroscopy, not a prior eclipse discovery. Gaia vari_eclipsing_binary rows=0; vari_summary=[]; current ExoFOP={"toi_count": 0, "ctoi_count": 0}.
Fresh shared VSX60arcsec result: {"B_vsx_vsx": []}. ROT is not prior eclipse classification. A cone neighbor must not be assigned to target.

Nine-catalog IDIA and Harvard cone requests each timed out (idia-receipts.json and idia-mirror-receipts.json). Consequently ASAS-SN, SB9, WDS, Kostov2/3/4, IJspeert and Prsa current per-object coverage is unavailable, not empty. Batched exact-name web queries on2026-10-30 returned no relevant source and do not prove novelty. Shared source receipts preserve current Gaia/VSX/SIMBAD/ExoFOP query provenance. The original paper/source records were checked live and remain unchanged.

## Follow-up and predictions

Refine stellar radii, light ratio and RV/eclipsing joint orbit with resolved photometry or spectroscopy; retry unavailable catalogs before any novelty claim.
Next fitted primary after2026-10-30: BTJD4347.52992, conditional linear-ephemeris1sigma=0.00026d. Next secondary template phase: BTJD4345.03374; phase/systematic uncertainty is uncalibrated, so do not use it as a precise scheduling window. For undetected secondary kinds use the Gaia covariance windows, not this optimized scan prediction.

Reviewed by fresh Sol lead G with fresh GPT-6.1 Terra numerical helper; measurements and script assumptions were independently inspected.