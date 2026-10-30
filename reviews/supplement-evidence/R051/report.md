# TIC 93213423: CONFIRMED

Repeated primary and secondary eclipses, a coherent multi-sector ephemeris, independent TESS-SPOC recovery and target-centred batch deficits establish the target EB. The small secondary phase displacement from the Gaia median is a soft-orbit characterization caveat.

Full review: COMPLETED_WITH_ARCHIVE_LIMITATION. Physical verdict is separate from novelty. Novelty: LIMITED_PRIOR_ART_COVERAGE; no prior target EB was established by the available current sources. New nine-catalog passes to both IDIA and Harvard timed out and are not negative matches.

## Raw SAP and event measurements

Primary P=3.340044799 +/- 0.000000539 d; Tref=2606.2852128 +/- 0.0001484 BTJD at cycle340; T0=1470.6699813. 27 fitted primary events, O-C RMS=0.460 min; chi2/dof=3.71/25. Shape T14=5.504h, profile range=[0.22391379310344828, 0.2347758620689655], ingress fraction=0.25; T12=fr*T14 and nominal T23=T14-2*T12. Trapezoid flat time is not totality for grazing systems.

|sector|mid BTJD|error d|depth ppt|error ppt|O-C min|flagged core|
|---|---:|---:|---:|---:|---:|---:|
|6|1470.6705479|0.001813|56.048|0.814|0.816|0|
|6|1474.0105773|0.001813|56.131|0.663|0.794|0|
|6|1480.6906362|0.001813|54.522|0.485|0.750|0|
|6|1484.0306656|0.001813|54.309|0.469|0.727|0|
|6|1487.3706950|0.001813|54.645|0.445|0.705|0|
|32|2175.4195113|0.000688|57.696|0.467|0.112|0|
|32|2178.7595407|0.000688|57.371|0.444|0.089|1|
|32|2182.0995701|0.000688|57.505|0.396|0.067|1|
|32|2188.7796290|0.000688|57.791|0.433|0.023|0|
|32|2192.1196585|0.000688|57.561|0.532|0.001|0|
|32|2195.4596879|0.000688|57.538|0.407|-0.021|0|
|32|2198.7997173|0.000688|57.402|0.473|-0.043|0|
|33|2202.1397468|0.000688|59.572|0.592|-0.065|0|
|33|2205.4797762|0.000688|59.704|0.506|-0.088|0|
|33|2208.8198056|0.000688|59.961|0.522|-0.110|0|
|33|2212.1598351|0.000688|59.952|0.527|-0.132|0|
|33|2218.8398939|0.000688|59.522|0.529|-0.176|0|
|33|2222.1799234|0.000688|59.672|0.527|-0.198|0|
|33|2225.5199528|0.000688|59.956|0.502|-0.220|0|
|98|3999.0838404|0.000688|48.482|0.405|-0.077|0|
|98|4002.4238699|0.000688|48.876|0.413|-0.099|0|
|98|4012.4439582|0.000688|48.430|0.426|-0.166|0|
|98|4015.7839876|0.000688|48.601|0.424|-0.188|0|
|98|4025.8040759|0.000688|48.946|0.403|-0.254|0|
|98|4029.1441054|0.000688|48.607|0.435|-0.276|0|
|98|4039.1655697|0.000688|48.691|0.468|1.639|0|
|98|4042.5042231|0.000688|48.621|0.395|-0.365|0|

Primary median depth=57.371ppt; maximum absolute background-regression fake depth=0.327ppt. Background native units were not treated as normalized flux. 0 event timing fits hit a scan edge. Quality-zero fits use exposure integration, local quadratic baselines, red-noise beta and grid floors; flagged-core counts and centroid/background regressions are retained in fit-results.json. Source variability and shape errors may exceed these conditional errors.

Blind rolling-median census covers all available sectors without the old post-gap trim. No off-eclipse census dip exceeds30%of the primary depth outside0.08phase of either fitted eclipse kind. Smaller candidates, gaps, sector edges and all threshold details remain in fit-results.json; this is a diagnostic census, not a calibrated false-positive probability.

## Gaia and physical feasibility

Own-source SB1 covariance verified: bit_index=127,15 correlations in P,gamma,K1,e,omega,Tp order; omega-Tp correlation=0.9999462. Primary assigned conjunctionA; period discrepancy=-0.142sigma.
ConjunctionA at Gaia epoch: offset=0.011636d, Gaia-only sigma=0.009232d; including photometric extrapolation sigma=0.009240d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.
ConjunctionB at Gaia epoch: offset=1.660093d, Gaia-only sigma=0.009006d; including photometric extrapolation sigma=0.009015d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.

Mass-function/assumed-stellar-radius checks (not measured binary parameters):

```json
[
  {
    "m1": 1.32,
    "m2_min": 0.44235364823060586,
    "f_mass": 0.027869085399606808,
    "a_rsun": 11.358066803045336,
    "r1_rsun": 2.04811,
    "r2_approx_rsun": 0.5207337073826673,
    "central_T14_hours": {
      "A": 5.770122758161012,
      "B": 5.771039096345279
    },
    "observed_T14_hours": 5.504275862068965
  }
]
```

Limb-darkened two-sphere feasibility permits free primary/secondary flux scales and fixed TIC stellar dimensions. It does not identify the foreground component from eclipse depth alone. Using Gaia primary spectroscopic omega and positive RV away from the observer, at A (nu+omega=90deg) the RV primary is behind and the companion is foreground; at B (270deg) the primary is foreground. The deeper eclipse is assigned A here; luminosity and component labeling remain conditional. Minimum RV companion mass and eclipse luminosity/shape jointly allow a stellar companion.

```json
{
  "status": "conditional shape feasibility",
  "best": {
    "chi2": 80.61193521929933,
    "dof": 121,
    "k": 0.22499999999999998,
    "b_A": 0.34,
    "e_sin_omega": -5.551115123125783e-17,
    "primary_scale": 0.9861342005182465,
    "secondary_scale": 0.004594321661181541
  },
  "profile_interval_approx_95": {
    "k": [
      0.22499999999999998,
      0.22499999999999998
    ],
    "b_A": [
      0.27,
      0.34
    ],
    "e_sin_omega": [
      -5.551115123125783e-17,
      0.02499999999999994
    ]
  },
  "error_inflation": 1,
  "assumptions": "Circular projected chord with eccentric speed factors; fixed TIC R1/M1, u1=.4 u2=.6, free depth scales per kind, event-scatter bin errors and 0.15ppt floor. Contact shape and dilution degeneracies persist. No claim of precise e sin omega.",
  "primary_profile_n": 64,
  "secondary_profile_n": 64
}
```

## Secondary evidence

Optimized secondary phase=0.498901; pooled depth=4.680ppt, empirical error=0.081ppt; 27/27 individually>3sigma. This scan optimizes phase and does not provide a calibrated phase error or global significance. Repeat events, independent reduction, and off-phase controls are more informative than its raw peak S/N.

```json
{
  "bit_index": 127,
  "gaia_primary": "A",
  "gaia_relative_phase_nominal": 0.5073008654398913,
  "gaia_relative_phase_quantiles_16_50_84": [
    0.5020331733019257,
    0.5063513152865134,
    0.5119820789147937
  ],
  "gaia_relative_phase_sigma": 0.004909515560665673,
  "gaia_e_cos_omega_quantiles": [
    0.0031936989053881286,
    0.009976516022701644,
    0.018821554711331803
  ],
  "gaia_e_sin_omega_quantiles": [
    -0.009466876184681375,
    -0.0002099496349373057,
    0.006244346914788412
  ],
  "photometric_phase": 0.49890086543989126,
  "photometric_e_cos_omega_first_order": -0.0017265165296721312,
  "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
  "geometry_status": "conditional shape feasibility",
  "geometry_e_sin_omega_conditional_range": [
    -5.551115123125783e-17,
    0.02499999999999994
  ],
  "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
}
```

|sector|secondary mid BTJD|error d|depth ppt|error ppt|
|---|---:|---:|---:|---:|
|6|1469.0133294|0.007865|5.941|1.041|
|6|1475.6711337|0.001966|5.018|0.270|
|6|1479.0124894|0.001902|4.784|0.128|
|6|1482.3551560|0.001902|4.541|0.147|
|6|1485.6938899|0.001902|4.690|0.142|
|6|1489.0365565|0.001813|4.500|0.132|
|32|2177.0831633|0.000655|4.991|0.123|
|32|2180.4245189|0.000655|5.037|0.138|
|32|2183.7671855|0.000655|4.894|0.123|
|32|2190.4472751|0.000655|4.777|0.130|
|32|2193.7873199|0.000655|5.171|0.139|
|32|2197.1234320|0.000655|5.078|0.132|
|33|2203.8035216|0.001311|5.038|0.163|
|33|2207.1448773|0.000655|5.194|0.153|
|33|2210.4862330|0.000655|5.088|0.144|
|33|2217.1650117|0.001311|4.999|0.208|
|33|2220.5050565|0.000655|5.300|0.127|
|33|2223.8451013|0.000655|5.264|0.127|
|98|3997.4102004|0.000655|4.219|0.114|
|98|4000.7502452|0.000655|4.449|0.098|
|98|4010.7716904|0.000655|4.175|0.101|
|98|4014.1091135|0.000655|4.403|0.092|
|98|4017.4504691|0.000655|4.077|0.181|
|98|4027.4719144|0.000655|4.337|0.130|
|98|4030.8106483|0.001311|4.638|0.170|
|98|4040.8294718|0.000655|4.278|0.097|
|98|4044.1695166|0.000655|4.436|0.122|

Secondary ephemeris: {"P": 3.340046052276308, "P_error": 9.909578681513317e-07, "Tref": 2648.031457938721, "Tref_error": 0.0002897530745744818, "reference_cycle": 352, "T0": 1472.3352475374606, "chi2": 85.3655446193316, "dof": 25, "n": 27, "oc_rms_minutes": 5.458855997680531}. Two-event periods and optimized shapes are not precise independent orbit constraints. Covered/uncovered/flagged secondary windows are enumerated individually in orbit-gates.json secondary_windows, and null-secondary.json when applicable.

## Independence and source attribution

TESS-SPOC sector33, exact FITS identity validated=True. Same TESS pixels through a different reduction, not another observatory. Exact product/time coverage/URLs/SHA256 are in independent manifests; every measured event and degree1/2 background/baseline comparison is in independent-summary.json (alternate summary for345589621).

```json
{
  "tc": 2202.139746762542,
  "qlp": {
    "1": {
      "depth": 0.0600649047073018,
      "error": 0.0005902903378002644,
      "red_noise_beta": 1.5811983523825757,
      "n_core": 33,
      "baseline_degree": 1,
      "background_regressed_depth": 0.060151204618899966,
      "background_template_native_sigma": 0.5000839610876912
    },
    "2": {
      "depth": 0.05962707018516755,
      "error": 0.0006012767025867044,
      "red_noise_beta": 1.559193837824628,
      "n_core": 33,
      "baseline_degree": 2,
      "background_regressed_depth": 0.05964945955946948,
      "background_template_native_sigma": 0.6620531657047218
    }
  },
  "independent": {
    "SAP_FLUX": {
      "1": {
        "depth": 0.05740428175535831,
        "error": 0.00043156696433219557,
        "red_noise_beta": 1.284745677565976,
        "n_core": 33,
        "baseline_degree": 1,
        "background_regressed_depth": 0.057213331642321764,
        "background_template_native_sigma": 1.1231207066052524
      },
      "2": {
        "depth": 0.056855633306232604,
        "error": 0.00044838305617960346,
        "red_noise_beta": 1.2757936995653905,
        "n_core": 33,
        "baseline_degree": 2,
        "background_regressed_depth": 0.05667849634483026,
        "background_template_native_sigma": 1.109443988241273
      }
    },
    "PDCSAP_FLUX": {
      "1": {
        "depth": 0.058212223050603945,
        "error": 0.0004355133693376432,
        "red_noise_beta": 1.2840275303078628,
        "n_core": 33,
        "baseline_degree": 1,
        "background_regressed_depth": 0.05801671202053907,
        "background_template_native_sigma": 1.1231207066052524
      },
      "2": {
        "depth": 0.057703867463138006,
        "error": 0.0004565326123140108,
        "red_noise_beta": 1.276652213318582,
        "n_core": 33,
        "baseline_degree": 2,
        "background_regressed_depth": 0.05752137669444432,
        "background_template_native_sigma": 1.109443988241273
      }
    }
  }
}
```

```json
{
  "tc": 2205.479776199814,
  "qlp": {
    "1": {
      "depth": 0.061172558795048446,
      "error": 0.0006109750857147577,
      "red_noise_beta": 1.6973857650165645,
      "n_core": 33,
      "baseline_degree": 1,
      "background_regressed_depth": 0.06125148818183048,
      "background_template_native_sigma": 1.1309348083095763
    },
    "2": {
      "depth": 0.05974662708111812,
      "error": 0.0005119434854652825,
      "red_noise_beta": 1.5494500953389037,
      "n_core": 33,
      "baseline_degree": 2,
      "background_regressed_depth": 0.05975227212915644,
      "background_template_native_sigma": 1.2171791958528626
    }
  },
  "independent": {
    "SAP_FLUX": {
      "1": {
        "depth": 0.05821271710872041,
        "error": 0.0005703117033196052,
        "red_noise_beta": 1.6870399422866855,
        "n_core": 33,
        "baseline_degree": 1,
        "background_regressed_depth": 0.05811556961266888,
        "background_template_native_sigma": 1.6328257877445025
      },
      "2": {
        "depth": 0.05691064534929745,
        "error": 0.00048651460593924,
        "red_noise_beta": 1.5474727254184741,
        "n_core": 33,
        "baseline_degree": 2,
        "background_regressed_depth": 0.0567831369692732,
        "background_template_native_sigma": 1.6546444740377138
      }
    },
    "PDCSAP_FLUX": {
      "1": {
        "depth": 0.05912179813603917,
        "error": 0.000581607436835985,
        "red_noise_beta": 1.6949468012764894,
        "n_core": 33,
        "baseline_degree": 1,
        "background_regressed_depth": 0.05901393162486257,
        "background_template_native_sigma": 1.6328257877445025
      },
      "2": {
        "depth": 0.057795444401436406,
        "error": 0.0004967494620723318,
        "red_noise_beta": 1.5590792940173666,
        "n_core": 33,
        "baseline_degree": 2,
        "background_regressed_depth": 0.0576565291359601,
        "background_template_native_sigma": 1.6546444740377138
      }
    }
  }
}
```

Batch difference image: sector98, deficit-minus-light=1.92arcsec; deficit-minus-WCS=3.97arcsec; PSF fractional residual=0.256. Duplicate legacy/new-schema rows are a single observation. Relative light/deficit offsets receive more weight than uncalibrated WCS offsets.

Neighbor dilution within60arcsec, G<15 (Gaia G approximates TESS; not a color-corrected flux ratio):

```json
[]
```

## Current archives and novelty

SIMBAD exact Gaia-ID: [{"id": "Gaia DR3 2966750897393787264", "main_id": "TYC 5925-1148-1", "otype": "SB*", "ra": "85.72547642917", "dec": "-20.61338249434"}]. This SB* classification establishes spectroscopy, not a prior eclipse discovery. Gaia vari_eclipsing_binary rows=0; vari_summary=[]; current ExoFOP={"toi_count": 0, "ctoi_count": 0}.
Fresh shared VSX60arcsec result: {"B_vsx_vsx": []}. ROT is not prior eclipse classification. A cone neighbor must not be assigned to target.

Nine-catalog IDIA and Harvard cone requests each timed out (idia-receipts.json and idia-mirror-receipts.json). Consequently ASAS-SN, SB9, WDS, Kostov2/3/4, IJspeert and Prsa current per-object coverage is unavailable, not empty. Batched exact-name web queries on2026-10-30 returned no relevant source and do not prove novelty. Shared source receipts preserve current Gaia/VSX/SIMBAD/ExoFOP query provenance. The original paper/source records were checked live and remain unchanged.

## Follow-up and predictions

Refine stellar radii, light ratio and RV/eclipsing joint orbit with resolved photometry or spectroscopy; retry unavailable catalogs before any novelty claim.
Next fitted primary after2026-10-30: BTJD4346.44855, conditional linear-ephemeris1sigma=0.00032d. Next secondary template phase: BTJD4344.77486; phase/systematic uncertainty is uncalibrated, so do not use it as a precise scheduling window. For undetected secondary kinds use the Gaia covariance windows, not this optimized scan prediction.

Reviewed by fresh Sol lead G with fresh GPT-6.1 Terra numerical helper; measurements and script assumptions were independently inspected.