# TIC 192198579: CONFIRMED

Four primary and six secondary events plus independent TESS-SPOC support an EB. Own pixel fits favor target over the13.26arcsec neighbor in both events (target residual0.146 vs neighbor0.582). High geometry residual limits dimensions, not eclipse reality.

Full review: COMPLETE (adjudicated). Novelty: LIMITED; successful checks found no target EB classification, but several catalogues were unavailable.

Raw untrimmed QUALITY=0 SAP: 4 accepted primary fits; median depth63.689ppt; T14=6.0257h. Primary and secondary individual timing/depth errors, duration/ingress/flat coordinates, O-C and rejected windows are tabulated below. Errors are conditional on shape/local baseline with grid and red-noise inflation. Trapezoid flat time is not measured totality.

```json
{
  "primary_shape": {
    "T14": 0.25106896551724134,
    "fr": 0.25,
    "shift": 0,
    "T14_range": [
      0.24563793103448273,
      0.25649999999999995
    ],
    "fr_range": [
      0.21,
      0.29
    ],
    "n_local_windows": 6,
    "error_note": "profile likelihood plus half-grid resolution; conditional shape model"
  },
  "primary_ephemeris": {
    "P": 10.580574222973285,
    "P_error": 2.2458786516858076e-05,
    "Tref": 2775.456548345538,
    "Tref_error": 0.00037664530007887787,
    "reference_cycle": 87,
    "T0": 1854.9465909468622,
    "chi2": 0.035563458500850485,
    "dof": 2,
    "n": 4,
    "oc_rms_minutes": 0.10227012311710909
  },
  "primary_events": [
    {
      "status": "insufficient",
      "tc_nom": 1844.3566360417753,
      "sec": 20,
      "n_in": 6,
      "cycle": -1
    },
    {
      "status": "insufficient",
      "tc_nom": 1854.9373,
      "sec": 20,
      "n_in": 0,
      "cycle": 0
    },
    {
      "status": "insufficient",
      "tc_nom": 1865.5179639582248,
      "sec": 20,
      "n_in": 7,
      "cycle": 1
    },
    {
      "status": "fit",
      "sec": 47,
      "tc_nom": 2585.003113117512,
      "tc": 2585.006125945098,
      "tc_error": 0.000753206896551724,
      "depth": 0.06341701310087257,
      "depth_error": 0.00029332795197713104,
      "T14": 0.25106896551724134,
      "T12": 0.06276724137931033,
      "T23": 0.12553448275862067,
      "beta": 1.3816590529002772,
      "n_in": 33,
      "flagged_core": 3,
      "flag_bits_core": 2048,
      "background_fake_depth": -0.00026920216573683296,
      "depth_with_background": 0.06371411574386689,
      "scan_edge": false,
      "x_template_shift_pix": -0.0008164780153764598,
      "x_err_pix": 0.0002889959742940035,
      "y_template_shift_pix": 0.002852997086593569,
      "y_err_pix": 0.00030215898188592507,
      "cycle": 69,
      "oc_days": -8.63869208842516e-05
    },
    {
      "status": "insufficient",
      "tc_nom": 2595.5837770757366,
      "sec": 47,
      "n_in": 0,
      "cycle": 70
    },
    {
      "status": "fit",
      "sec": 47,
      "tc_nom": 2606.1644410339613,
      "tc": 2606.1674538615475,
      "tc_error": 0.000753206896551724,
      "depth": 0.06388772477545769,
      "depth_error": 0.00029072506169603986,
      "T14": 0.25106896551724134,
      "T12": 0.06276724137931033,
      "T23": 0.12553448275862067,
      "beta": 1.410045106932388,
      "n_in": 32,
      "flagged_core": 4,
      "flag_bits_core": 2080,
      "background_fake_depth": -0.00010317300452890874,
      "depth_with_background": 0.06398169242263912,
      "scan_edge": false,
      "x_template_shift_pix": -0.002620083870747004,
      "x_err_pix": 0.00044372605800854775,
      "y_template_shift_pix": 0.002054174170397343,
      "y_err_pix": 0.0002297453824391613,
      "cycle": 71,
      "oc_days": 9.308358221460367e-05
    },
    {
      "status": "fit",
      "sec": 60,
      "tc_nom": 2944.7456876971555,
      "tc": 2944.7456876971555,
      "tc_error": 0.000753206896551724,
      "depth": 0.0634902034333539,
      "depth_error": 0.00025210579489044115,
      "T14": 0.25106896551724134,
      "T12": 0.06276724137931033,
      "T23": 0.12553448275862067,
      "beta": 1.6291749843431416,
      "n_in": 108,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -9.718922305261512e-05,
      "depth_with_background": 0.06357520792236253,
      "scan_edge": false,
      "x_template_shift_pix": -0.0007566413637961844,
      "x_err_pix": 0.00028432657497706027,
      "y_template_shift_pix": 0.002182033461234889,
      "y_err_pix": 0.00028948619879333145,
      "cycle": 103,
      "oc_days": -4.8215955303021474e-05
    },
    {
      "status": "fit",
      "sec": 60,
      "tc_nom": 2955.3263516553798,
      "tc": 2955.3263516553798,
      "tc_error": 0.000753206896551724,
      "depth": 0.06420232816829236,
      "depth_error": 0.00029971162349359234,
      "T14": 0.25106896551724134,
      "T12": 0.06276724137931033,
      "T23": 0.12553448275862067,
      "beta": 1.6408705546034439,
      "n_in": 108,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -6.903520922613657e-05,
      "depth_with_background": 0.06428312651449046,
      "scan_edge": false,
      "x_template_shift_pix": -0.0018154158200145774,
      "x_err_pix": 0.0006493031630283436,
      "y_template_shift_pix": 0.004580380755601911,
      "y_err_pix": 0.001172933766124412,
      "cycle": 104,
      "oc_days": 4.1519295791658806e-05
    }
  ],
  "secondary": {
    "predicted_gaia_phase": 0.46427955413851396,
    "profile_phase": 0.4732966646361086,
    "statistic": {
      "n": 6,
      "depth": 0.005897188198823768,
      "error": 0.00013024829109504907,
      "snr": 45.276511110002026,
      "scatter": 8.894561360501162e-05,
      "chi2": 0.46682766039302603,
      "dof": 5,
      "empirical_error": 0.00013024829109504907,
      "n_individual_gt3sigma": 6
    },
    "events": [
      {
        "status": "fit",
        "sec": 20,
        "tc_nom": 1849.373767213557,
        "tc": 1849.3722607997638,
        "tc_error": 0.003766034482758626,
        "depth": 0.006008839416088083,
        "depth_error": 0.0003387538836627372,
        "T14": 0.25106896551724134,
        "T12": 0.06276724137931033,
        "T23": 0.12553448275862067,
        "beta": 1.2680367159744592,
        "n_in": 12,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": 8.971790712742341e-05,
        "depth_with_background": 0.005973307420146473,
        "scan_edge": false,
        "x_template_shift_pix": -0.00017438316700189426,
        "x_err_pix": 0.00023812261703328686,
        "y_template_shift_pix": 0.0007929968933194434,
        "y_err_pix": 0.0002685391748272106,
        "cycle": -1,
        "oc_days": 0.0009526687986181059
      },
      {
        "status": "fit",
        "sec": 20,
        "tc_nom": 1859.9543414365303,
        "tc": 1859.949822195151,
        "tc_error": 0.0037660344827586192,
        "depth": 0.005972491720468983,
        "depth_error": 0.0003668635767004372,
        "T14": 0.25106896551724134,
        "T12": 0.06276724137931033,
        "T23": 0.12553448275862067,
        "beta": 1.2088838633466488,
        "n_in": 11,
        "flagged_core": 1,
        "flag_bits_core": 4096,
        "background_fake_depth": 4.752383755673946e-06,
        "depth_with_background": 0.005968671846897969,
        "scan_edge": false,
        "x_template_shift_pix": -0.0007811429787017349,
        "x_err_pix": 0.00023808955127113367,
        "y_template_shift_pix": 0.0009232787804151288,
        "y_err_pix": 0.00033087873515944813,
        "cycle": 0,
        "oc_days": -0.002075314277817597
      },
      {
        "status": "fit",
        "sec": 47,
        "tc_nom": 2590.013962821687,
        "tc": 2590.013962821687,
        "tc_error": 0.0037660344827586192,
        "depth": 0.0057821231641915745,
        "depth_error": 0.0002899659749553518,
        "T14": 0.25106896551724134,
        "T12": 0.06276724137931033,
        "T23": 0.12553448275862067,
        "beta": 1.6968907256251309,
        "n_in": 35,
        "flagged_core": 1,
        "flag_bits_core": 2048,
        "background_fake_depth": -2.6968673181543434e-05,
        "depth_with_background": 0.005815645053521497,
        "scan_edge": false,
        "x_template_shift_pix": -0.0011300974565093059,
        "x_err_pix": 0.0002913434299160071,
        "y_template_shift_pix": 0.0005484363707586822,
        "y_err_pix": 0.000247728429014219,
        "cycle": 69,
        "oc_days": 0.0013981982751829491
      },
      {
        "status": "fit",
        "sec": 47,
        "tc_nom": 2600.5945370446607,
        "tc": 2600.5945370446607,
        "tc_error": 0.003012827586206898,
        "depth": 0.0058589267464612075,
        "depth_error": 0.000290021253472017,
        "T14": 0.25106896551724134,
        "T12": 0.06276724137931033,
        "T23": 0.12553448275862067,
        "beta": 1.6946015794763094,
        "n_in": 31,
        "flagged_core": 5,
        "flag_bits_core": 2048,
        "background_fake_depth": 2.3709855620739857e-05,
        "depth_with_background": 0.005852715099514351,
        "scan_edge": false,
        "x_template_shift_pix": -0.0011006905498863711,
        "x_err_pix": 0.0003198650098910484,
        "y_template_shift_pix": 0.0005602447919952107,
        "y_err_pix": 0.0003806508172772261,
        "cycle": 70,
        "oc_days": 0.0013830427851644345
      },
      {
        "status": "fit",
        "sec": 60,
        "tc_nom": 2939.1729121798053,
        "tc": 2939.169899352219,
        "tc_error": 0.003012827586206898,
        "depth": 0.00581146955487459,
        "depth_error": 0.0003566525209224226,
        "T14": 0.25106896551724134,
        "T12": 0.06276724137931033,
        "T23": 0.12553448275862067,
        "beta": 2.2308808339817805,
        "n_in": 109,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": 4.8501362010419864e-06,
        "depth_with_background": 0.005820453911023836,
        "scan_edge": false,
        "x_template_shift_pix": -0.0013677197755049251,
        "x_err_pix": 0.0006067989572506871,
        "y_template_shift_pix": 0.0009153292941719038,
        "y_err_pix": 0.0005697851081625864,
        "cycle": 102,
        "oc_days": -0.002114760489348555
      },
      {
        "status": "insufficient",
        "tc_nom": 2949.753486402779,
        "sec": 60,
        "n_in": 40,
        "cycle": 103
      },
      {
        "status": "fit",
        "sec": 60,
        "tc_nom": 2960.334060625752,
        "tc": 2960.334060625752,
        "tc_error": 0.0037660344827586192,
        "depth": 0.005983656115224172,
        "depth_error": 0.00029936804993118863,
        "T14": 0.25106896551724134,
        "T12": 0.06276724137931033,
        "T23": 0.12553448275862067,
        "beta": 2.210946493509683,
        "n_in": 108,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": -5.216988802168167e-05,
        "depth_with_background": 0.00604309215338422,
        "scan_edge": false,
        "x_template_shift_pix": -0.0005875090458029885,
        "x_err_pix": 0.00039285989987124855,
        "y_template_shift_pix": 0.00037167591347857096,
        "y_err_pix": 0.000353282431368981,
        "cycle": 104,
        "oc_days": 0.0008677561168042303
      }
    ],
    "ephemeris": {
      "P": 10.580589378463523,
      "P_error": 3.405999573797622e-05,
      "Tref": 2463.0454920818497,
      "Tref_error": 0.0014205616655678065,
      "reference_cycle": 57,
      "T0": 1859.9518975094288,
      "chi2": 1.2620065610236337,
      "dof": 4,
      "n": 6,
      "oc_rms_minutes": 2.221465540480615
    },
    "shape": {
      "T14": 0.25106896551724134,
      "fr": 0.25,
      "shift": 0,
      "T14_range": [
        0.24563793103448273,
        0.25649999999999995
      ],
      "fr_range": [
        0.21,
        0.29
      ],
      "n_local_windows": 6,
      "error_note": "profile likelihood plus half-grid resolution; conditional shape model"
    },
    "profile_scan_note": "Conditional fitted secondary shape when secondary-shape.json exists, otherwise primary shape; phase optimized over +/- one T14. Weak/modulated secondary shape remains model dependent."
  }
}
```

## Raw-event controls and coverage

Background regressions use standardized native background units, not normalized flux ratios. Event records retain flagged-core counts, background-regressed depth and centroid template shifts. Centroid shifts are diagnostics, not source attribution. The blind rolling-median census below is diagnostic and uncalibrated; off-phase triggers, known common-mode sector times and shallow systematics must not be promoted to extra eclipses. Missing/flagged windows are not nulls.

```json
{
  "blind_census": [
    {
      "sec": 20,
      "tc": 1844.3130795931909,
      "depth": 0.06819738413986887,
      "n": 6,
      "phase": 0.9949967620298799,
      "threshold": 0.003,
      "duration": 0.12500123812492347
    },
    {
      "sec": 20,
      "tc": 1849.3718036330479,
      "depth": 0.005792432865313835,
      "n": 11,
      "phase": 0.47311108108764344,
      "threshold": 0.003,
      "duration": 0.22916700744008267
    },
    {
      "sec": 20,
      "tc": 1859.9545543033903,
      "depth": 0.006422499932797199,
      "n": 10,
      "phase": 0.4733167832852057,
      "threshold": 0.003,
      "duration": 0.22916380256629054
    },
    {
      "sec": 20,
      "tc": 1865.5742777278458,
      "depth": 0.06482264217024403,
      "n": 6,
      "phase": 0.004452741128928128,
      "threshold": 0.003,
      "duration": 0.12499728109423813
    },
    {
      "sec": 47,
      "tc": 2585.0010355337176,
      "depth": 0.06557045178916499,
      "n": 33,
      "phase": 0.9995107261485003,
      "threshold": 0.003,
      "duration": 0.24999888442744123
    },
    {
      "sec": 47,
      "tc": 2590.0109243738757,
      "depth": 0.0067806362216713545,
      "n": 33,
      "phase": 0.473009492338349,
      "threshold": 0.003,
      "duration": 0.23610748045348373
    },
    {
      "sec": 47,
      "tc": 2600.591101851278,
      "depth": 0.006937474238491337,
      "n": 29,
      "phase": 0.47297199479211827,
      "threshold": 0.003,
      "duration": 0.23610430706776242
    },
    {
      "sec": 47,
      "tc": 2606.1623125440756,
      "depth": 0.06562016783098479,
      "n": 31,
      "phase": 0.9995228771346945,
      "threshold": 0.003,
      "duration": 0.24304538204978599
    },
    {
      "sec": 60,
      "tc": 2939.169928452312,
      "depth": 0.007086879077722763,
      "n": 90,
      "phase": 0.47301466411038007,
      "threshold": 0.003480354249109344,
      "duration": 0.2523184916349237
    },
    {
      "sec": 60,
      "tc": 2944.7462121212934,
      "depth": 0.06638142551114334,
      "n": 105,
      "phase": 4.50077824609707e-05,
      "threshold": 0.003480354249109344,
      "duration": 0.24305660852087385
    },
    {
      "sec": 60,
      "tc": 2949.67975452569,
      "depth": 0.007539782217847235,
      "n": 37,
      "phase": 0.46632805636072305,
      "threshold": 0.003480354249109344,
      "duration": 0.10879509481537752
    },
    {
      "sec": 60,
      "tc": 2955.326709855992,
      "depth": 0.06672411308057946,
      "n": 104,
      "phase": 3.7778659219611654e-05,
      "threshold": 0.003480354249109344,
      "duration": 0.24073802731709293
    },
    {
      "sec": 60,
      "tc": 2960.3339661849554,
      "depth": 0.007313807513423476,
      "n": 93,
      "phase": 0.47328773876928665,
      "threshold": 0.003480354249109344,
      "duration": 0.24073519940156984
    }
  ]
}
```

## Own Gaia covariance and physical feasibility

Source identity, solution layout and bit order were asserted before covariance sampling. No borrowed correlations. Per-event conjunction predictions and residuals, period tension, mass function, companion minimum mass, orbital scale and central duration estimates follow. TIC properties and assumed companion radii are feasibility inputs, not measured dimensions. Two-disk limb-darkened models account for partial overlap; poor fits/grid edges prevent calibrated e sin omega or component posterior claims.

```json
{
  "orbit": {
    "gaia_source": "shared-full-review/gaia-nss-ari.csv",
    "gaia_bit_index": 127,
    "w_tp_corr": 0.9866238,
    "gaia_comparison": [
      {
        "kind": "A",
        "epoch389_offset": -0.025363100818879047,
        "epoch389_gaia_error": 0.048242150895593645,
        "events": [
          {
            "sec": 47,
            "tc": 2585.006125945098,
            "gaia_conjunction": 2585.332735564696,
            "gaia_error": 0.5292567286565293,
            "offset_days": -0.3266096195980026,
            "z": -0.6171093746534692
          },
          {
            "sec": 47,
            "tc": 2606.1674538615475,
            "gaia_conjunction": 2606.496854867049,
            "gaia_error": 0.5339931143748969,
            "offset_days": -0.3294010055014951,
            "z": -0.616863156008834
          },
          {
            "sec": 60,
            "tc": 2944.7456876971555,
            "gaia_conjunction": 2945.1221200431282,
            "gaia_error": 0.6097953508378716,
            "offset_days": -0.3764323459727166,
            "z": -0.6173088369732819
          },
          {
            "sec": 60,
            "tc": 2955.3263516553798,
            "gaia_conjunction": 2955.7042430471674,
            "gaia_error": 0.6121646968915693,
            "offset_days": -0.3778913917876707,
            "z": -0.617303003040453
          }
        ]
      },
      {
        "kind": "B",
        "epoch389_offset": -4.948562392419376,
        "epoch389_gaia_error": 0.12573808773927736,
        "events": [
          {
            "sec": 47,
            "tc": 2585.006125945098,
            "gaia_conjunction": 2590.249894016585,
            "gaia_error": 0.4121336104798816,
            "offset_days": -5.243768071487011,
            "z": -12.723444972587167
          },
          {
            "sec": 47,
            "tc": 2606.1674538615475,
            "gaia_conjunction": 2611.4138299558053,
            "gaia_error": 0.41677362409838153,
            "offset_days": -5.246376094257812,
            "z": -12.588050738720963
          },
          {
            "sec": 60,
            "tc": 2944.7456876971555,
            "gaia_conjunction": 2950.038597066774,
            "gaia_error": 0.4912889671191114,
            "offset_days": 5.289110202952766,
            "z": 10.765769925658127
          },
          {
            "sec": 60,
            "tc": 2955.3263516553798,
            "gaia_conjunction": 2960.6210591111267,
            "gaia_error": 0.49362453866525813,
            "offset_days": 5.287312116824292,
            "z": 10.71118947198572
          }
        ]
      }
    ],
    "primary_conjunction": "A",
    "predicted_secondary_phase": 0.46427955413851396,
    "secondary": {
      "n": 6,
      "depth": 0.0030390904069044935,
      "error": 0.00039984205142644093,
      "snr": 7.600727327359653,
      "scatter": 0.0002973254075157309,
      "chi2": 0.5525515876619841,
      "dof": 5,
      "phase": 0.46427955413851396,
      "control_scatter": 0.00039984205142644093,
      "upper_3sigma": 0.004238616561183816
    },
    "secondary_windows": {
      "gaia_other_windows": [
        {
          "status": "fit",
          "sec": 20,
          "tc_nom": 1849.2783610066604,
          "tc": 1849.2783610066604,
          "tc_error": 0.001736098441805704,
          "depth": 0.0028506522952571555,
          "depth_error": 0.0010247055172280023,
          "T14": 0.25106896551724134,
          "T12": 0.06276724137931033,
          "T23": 0.12553448275862067,
          "beta": 1.3852983895966937,
          "n_in": 12,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": -2.9193672181014757e-05,
          "depth_with_background": 0.0029773667381130186,
          "scan_edge": false,
          "x_template_shift_pix": -7.99126933534906e-05,
          "x_err_pix": 0.00025773102930510324,
          "y_template_shift_pix": 0.0004401966713565738,
          "y_err_pix": 0.0002916203147945799,
          "cycle": -1
        },
        {
          "status": "fit",
          "sec": 20,
          "tc_nom": 1859.8589352296337,
          "tc": 1859.8589352296337,
          "tc_error": 0.0019018005572531077,
          "depth": 0.003093735029118091,
          "depth_error": 0.0010367767009132774,
          "T14": 0.25106896551724134,
          "T12": 0.06276724137931033,
          "T23": 0.12553448275862067,
          "beta": 1.3637600433343744,
          "n_in": 10,
          "flagged_core": 2,
          "flag_bits_core": 4096,
          "background_fake_depth": -0.00011166524990067522,
          "depth_with_background": 0.0031673493605655512,
          "scan_edge": false,
          "x_template_shift_pix": -0.0006248515206086818,
          "x_err_pix": 0.0003086571402572971,
          "y_template_shift_pix": 0.000907659986176765,
          "y_err_pix": 0.0003887524092326031,
          "cycle": 0
        },
        {
          "status": "fit",
          "sec": 47,
          "tc_nom": 2589.9185566147903,
          "tc": 2589.9185566147903,
          "tc_error": 0.000753206896551724,
          "depth": 0.0028576370117569436,
          "depth_error": 0.0009807944407401665,
          "T14": 0.25106896551724134,
          "T12": 0.06276724137931033,
          "T23": 0.12553448275862067,
          "beta": 2.30234224772411,
          "n_in": 34,
          "flagged_core": 3,
          "flag_bits_core": 2048,
          "background_fake_depth": 7.519635691194007e-06,
          "depth_with_background": 0.002862911027807848,
          "scan_edge": false,
          "x_template_shift_pix": -0.0007916883360157246,
          "x_err_pix": 0.00042642970033335807,
          "y_template_shift_pix": 0.0003694731761943529,
          "y_err_pix": 0.0003434888450642985,
          "cycle": 69
        },
        {
          "status": "fit",
          "sec": 47,
          "tc_nom": 2600.499130837764,
          "tc": 2600.499130837764,
          "tc_error": 0.000753206896551724,
          "depth": 0.0036813905521577363,
          "depth_error": 0.0009815019812514272,
          "T14": 0.25106896551724134,
          "T12": 0.06276724137931033,
          "T23": 0.12553448275862067,
          "beta": 2.2885504858438424,
          "n_in": 24,
          "flagged_core": 12,
          "flag_bits_core": 22528,
          "background_fake_depth": -4.32404330574545e-05,
          "depth_with_background": 0.003752083609415319,
          "scan_edge": false,
          "x_template_shift_pix": -0.000889189497257053,
          "x_err_pix": 0.0004969681897451647,
          "y_template_shift_pix": 0.00043148523269136163,
          "y_err_pix": 0.0005666599079642285,
          "cycle": 70
        },
        {
          "status": "fit",
          "sec": 60,
          "tc_nom": 2939.0775059729085,
          "tc": 2939.0775059729085,
          "tc_error": 0.000753206896551724,
          "depth": 0.0028974664047020254,
          "depth_error": 0.0009397544078893885,
          "T14": 0.25106896551724134,
          "T12": 0.06276724137931033,
          "T23": 0.12553448275862067,
          "beta": 3.5779790017809634,
          "n_in": 109,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": 0.0001587223178722407,
          "depth_with_background": 0.0028261801808711793,
          "scan_edge": false,
          "x_template_shift_pix": -0.0012906354370545233,
          "x_err_pix": 0.0009576167077793693,
          "y_template_shift_pix": 0.000380062793419255,
          "y_err_pix": 0.0009330803151989057,
          "cycle": 102
        },
        {
          "status": "insufficient",
          "tc_nom": 2949.658080195882,
          "sec": 60,
          "n_in": 81,
          "cycle": 103
        },
        {
          "status": "fit",
          "sec": 60,
          "tc_nom": 2960.2386544188553,
          "tc": 2960.2386544188553,
          "tc_error": 0.000753206896551724,
          "depth": 0.0028763841751370716,
          "depth_error": 0.0009275405522505518,
          "T14": 0.25106896551724134,
          "T12": 0.06276724137931033,
          "T23": 0.12553448275862067,
          "beta": 3.734131405151466,
          "n_in": 108,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": 1.6629118344593324e-05,
          "depth_with_background": 0.0028695350959787127,
          "scan_edge": false,
          "x_template_shift_pix": -0.0003091469270192272,
          "x_err_pix": 0.0006532953642884099,
          "y_template_shift_pix": 9.104196881323699e-05,
          "y_err_pix": 0.0005934648126845781,
          "cycle": 104
        }
      ]
    },
    "controls": [
      {
        "n": 5,
        "depth": -0.0001547373546815185,
        "error": 6.205350448165465e-05,
        "snr": -2.4936118592184378,
        "scatter": 0.00011489899950000123,
        "chi2": 3.2517973610617577,
        "dof": 4,
        "phase": 0.1
      },
      {
        "n": 6,
        "depth": 6.78668254751609e-05,
        "error": 5.622786321430252e-05,
        "snr": 1.2069963465710682,
        "scatter": 0.00016419709816918617,
        "chi2": 8.625735677011905,
        "dof": 5,
        "phase": 0.15000000000000002
      },
      {
        "n": 6,
        "depth": -5.1141657630583335e-05,
        "error": 5.6733992018538055e-05,
        "snr": -0.901428857921237,
        "scatter": 0.0002200610784318648,
        "chi2": 10.693329926405777,
        "dof": 5,
        "phase": 0.20000000000000004
      },
      {
        "n": 4,
        "depth": 0.00010034385889004247,
        "error": 6.211813391182673e-05,
        "snr": 1.6153714313516736,
        "scatter": 6.26700316619025e-05,
        "chi2": 1.0759784831155512,
        "dof": 3,
        "phase": 0.25000000000000006
      },
      {
        "n": 5,
        "depth": -3.7102827710641534e-05,
        "error": 5.970700600230259e-05,
        "snr": -0.6214149761455242,
        "scatter": 0.000292369238999993,
        "chi2": 12.88783285124272,
        "dof": 4,
        "phase": 0.30000000000000004
      },
      {
        "n": 4,
        "depth": -0.00011956551890314811,
        "error": 6.083862335084492e-05,
        "snr": -1.9652896847063124,
        "scatter": 0.00012363937805626727,
        "chi2": 4.3720053381715145,
        "dof": 3,
        "phase": 0.3500000000000001
      },
      {
        "n": 5,
        "depth": 0.0006335225842584175,
        "error": 0.0002347244642706856,
        "snr": 2.6990053475117772,
        "scatter": 0.00010005001977657233,
        "chi2": 0.1564896130201861,
        "dof": 4,
        "phase": 0.40000000000000013
      },
      {
        "n": 7,
        "depth": -0.002459948293688112,
        "error": 0.0002703945863130329,
        "snr": -9.097624058346556,
        "scatter": 0.00032877189025981693,
        "chi2": 1.7403347426009554,
        "dof": 6,
        "phase": 0.45000000000000007
      },
      {
        "n": 6,
        "depth": -0.002699964344994718,
        "error": 0.0004297536263305276,
        "snr": -6.2825865323080485,
        "scatter": 9.971029921586506e-05,
        "chi2": 0.05432866342435043,
        "dof": 5,
        "phase": 0.5000000000000001
      },
      {
        "n": 5,
        "depth": 0.0002557148710444467,
        "error": 0.00022402521915973171,
        "snr": 1.1414557343301603,
        "scatter": 0.00016654388625744412,
        "chi2": 0.5912480165648752,
        "dof": 4,
        "phase": 0.5500000000000002
      },
      {
        "n": 7,
        "depth": 0.00013131340488593146,
        "error": 5.5133277173881525e-05,
        "snr": 2.381744957256758,
        "scatter": 0.00020173314540302144,
        "chi2": 11.017787317367928,
        "dof": 6,
        "phase": 0.6000000000000002
      },
      {
        "n": 7,
        "depth": 2.1971172655669865e-05,
        "error": 5.0075106202235134e-05,
        "snr": 0.4387643745963572,
        "scatter": 6.475047034705056e-05,
        "chi2": 1.7505709951962392,
        "dof": 6,
        "phase": 0.6500000000000001
      },
      {
        "n": 6,
        "depth": -9.581910285489302e-06,
        "error": 5.405590632395006e-05,
        "snr": -0.1772592661395066,
        "scatter": 0.00022552785113726922,
        "chi2": 12.455420433241507,
        "dof": 5,
        "phase": 0.7000000000000002
      },
      {
        "n": 5,
        "depth": -4.640905240174405e-05,
        "error": 6.565352935295842e-05,
        "snr": -0.7068782571039772,
        "scatter": 6.654501029323647e-05,
        "chi2": 1.0513389136169295,
        "dof": 4,
        "phase": 0.7500000000000002
      },
      {
        "n": 5,
        "depth": -6.696265365506873e-05,
        "error": 6.279068833148258e-05,
        "snr": -1.0664424205952583,
        "scatter": 0.00020250537431044339,
        "chi2": 10.134467581319646,
        "dof": 4,
        "phase": 0.8000000000000002
      },
      {
        "n": 4,
        "depth": 6.399046214591256e-05,
        "error": 7.087515952178525e-05,
        "snr": 0.9028616313201171,
        "scatter": 0.00011630419379325656,
        "chi2": 3.651242448225091,
        "dof": 3,
        "phase": 0.8500000000000002
      },
      {
        "n": 4,
        "depth": -4.999241405110298e-05,
        "error": 6.717996990353688e-05,
        "snr": -0.7441565413453838,
        "scatter": 0.00013004102225149374,
        "chi2": 3.875954931708794,
        "dof": 3,
        "phase": 0.9000000000000002
      },
      {
        "n": 5,
        "depth": 0.0002242530320825966,
        "error": 0.00018488990661514996,
        "snr": 1.2129003480399898,
        "scatter": 0.002109726665896928,
        "chi2": 1.0680981612514473,
        "dof": 4,
        "phase": 0.9500000000000003
      },
      {
        "n": 6,
        "depth": 0.0030390904069044935,
        "error": 0.00039984205142644093,
        "snr": 7.600727327359653,
        "scatter": 0.0002973254075157309,
        "chi2": 0.5525515876619841,
        "dof": 5,
        "phase": 0.46427955413851396,
        "control_scatter": 0.00039984205142644093,
        "upper_3sigma": 0.004238616561183816
      }
    ],
    "physics": [
      {
        "m1": 1.212,
        "m2_min": 0.47499924666874516,
        "f_mass": 0.03765728326791486,
        "a_rsun": 24.146550165943616,
        "r1_rsun": 2.13847,
        "r2_approx_rsun": 0.5512572784739247,
        "central_T14_hours": {
          "A": 7.343207954041072,
          "B": 11.008026411765206
        },
        "observed_T14_hours": 6.025655172413792
      }
    ],
    "period_delta_sigma": -0.6101445656815186
  },
  "covariance_geometry": {
    "bit_index": 127,
    "gaia_primary": "A",
    "gaia_relative_phase_nominal": 0.46427955413851396,
    "gaia_relative_phase_quantiles_16_50_84": [
      0.4518117107049352,
      0.46536877869007326,
      0.4807520538793517
    ],
    "gaia_relative_phase_sigma": 0.015127757432957266,
    "gaia_e_cos_omega_quantiles": [
      -0.07442258047029468,
      -0.053375861342004546,
      -0.02952439693933903
    ],
    "gaia_e_sin_omega_quantiles": [
      0.16149660234067104,
      0.1985753678171447,
      0.23573132466891505
    ],
    "photometric_phase": 0.4732966646361086,
    "photometric_e_cos_omega_first_order": -0.04194550110277289,
    "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
    "geometry_status": "conditional shape feasibility",
    "geometry_e_sin_omega_conditional_range": [
      0.1999999999999999,
      0.1999999999999999
    ],
    "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
  },
  "conditional_two_disk_geometry": {
    "status": "conditional shape feasibility",
    "best": {
      "chi2": 1772.071742664617,
      "dof": 121,
      "k": 0.24999999999999997,
      "b_A": 0.585,
      "e_sin_omega": 0.1999999999999999,
      "primary_scale": 1.0,
      "secondary_scale": 0.008178226956015212
    },
    "profile_interval_approx_95": {
      "k": [
        0.24999999999999997,
        0.24999999999999997
      ],
      "b_A": [
        0.585,
        0.585
      ],
      "e_sin_omega": [
        0.1999999999999999,
        0.1999999999999999
      ]
    },
    "error_inflation": 14.645221013757165,
    "assumptions": "Circular projected chord with eccentric speed factors; fixed TIC R1/M1, u1=.4 u2=.6, free depth scales per kind, event-scatter bin errors and 0.15ppt floor. Contact shape and dilution degeneracies persist. No claim of precise e sin omega.",
    "primary_profile_n": 64,
    "secondary_profile_n": 64
  }
}
```

## Independent reduction and source attribution

Exact target and sector FITS identities were validated. This is a different pipeline using the same TESS pixels, not another observatory. Linear/quadratic baseline and background-sensitive depths are retained; aperture/PDCSAP depth differences reflect dilution and processing. TARS has no quality column.

```json
{
  "sector": 47,
  "provenance": "TESS-SPOC",
  "fits_identity_validated": true,
  "quality_column_present": true,
  "events": [
    {
      "tc": 2585.006125945098,
      "qlp": {
        "1": {
          "depth": 0.06349738960256184,
          "error": 0.0002741846216609471,
          "red_noise_beta": 1.4432178509937017,
          "n_core": 33,
          "baseline_degree": 1,
          "background_regressed_depth": 0.06378444183073415,
          "background_template_native_sigma": 1.5513611361334831
        },
        "2": {
          "depth": 0.06349758586956049,
          "error": 0.00030663180282010507,
          "red_noise_beta": 1.4432357037921617,
          "n_core": 33,
          "baseline_degree": 2,
          "background_regressed_depth": 0.06379255090958114,
          "background_template_native_sigma": 1.5926782471649803
        }
      },
      "independent": {
        "SAP_FLUX": {
          "1": {
            "depth": 0.05094629561202871,
            "error": 0.000181272398525721,
            "red_noise_beta": 1.2843860250944266,
            "n_core": 36,
            "baseline_degree": 1,
            "background_regressed_depth": 0.05141846926991552,
            "background_template_native_sigma": 2.300506388992049
          },
          "2": {
            "depth": 0.05096222290629743,
            "error": 0.00020277000773804402,
            "red_noise_beta": 1.284073189477434,
            "n_core": 36,
            "baseline_degree": 2,
            "background_regressed_depth": 0.051417648348290775,
            "background_template_native_sigma": 2.2181846138285026
          }
        },
        "PDCSAP_FLUX": {
          "1": {
            "depth": 0.0613548624118228,
            "error": 0.00021976463165143765,
            "red_noise_beta": 1.2855760661298758,
            "n_core": 36,
            "baseline_degree": 1,
            "background_regressed_depth": 0.06190997932360541,
            "background_template_native_sigma": 2.300506388992049
          },
          "2": {
            "depth": 0.06139190585135487,
            "error": 0.0002454933159684317,
            "red_noise_beta": 1.2839345396537525,
            "n_core": 36,
            "baseline_degree": 2,
            "background_regressed_depth": 0.061924532206522886,
            "background_template_native_sigma": 2.2181846138285026
          }
        }
      }
    },
    {
      "tc": 2606.1674538615475,
      "qlp": {
        "1": {
          "depth": 0.06399437618243897,
          "error": 0.0002654359001801269,
          "red_noise_beta": 1.439316189022659,
          "n_core": 33,
          "baseline_degree": 1,
          "background_regressed_depth": 0.06410440083272523,
          "background_template_native_sigma": 0.8437624839245095
        },
        "2": {
          "depth": 0.06393600473542972,
          "error": 0.00029575409280683916,
          "red_noise_beta": 1.4333532166516225,
          "n_core": 33,
          "baseline_degree": 2,
          "background_regressed_depth": 0.06403004339397109,
          "background_template_native_sigma": 0.6960543400595894
        }
      },
      "independent": {
        "SAP_FLUX": {
          "1": {
            "depth": 0.05113330891840641,
            "error": 0.00017633174248311747,
            "red_noise_beta": 1.2703904540663573,
            "n_core": 37,
            "baseline_degree": 1,
            "background_regressed_depth": 0.051576634774039606,
            "background_template_native_sigma": 2.4409446489817967
          },
          "2": {
            "depth": 0.051137988750544205,
            "error": 0.00019734109358651058,
            "red_noise_beta": 1.2705319082502982,
            "n_core": 37,
            "baseline_degree": 2,
            "background_regressed_depth": 0.05156621022893188,
            "background_template_native_sigma": 2.0472073048464123
          }
        },
        "PDCSAP_FLUX": {
          "1": {
            "depth": 0.06160203255398649,
            "error": 0.00020852174125548115,
            "red_noise_beta": 1.2440260596751924,
            "n_core": 37,
            "baseline_degree": 1,
            "background_regressed_depth": 0.062173318340451936,
            "background_template_native_sigma": 2.4409446489817967
          },
          "2": {
            "depth": 0.0616107029217486,
            "error": 0.00023338636538387984,
            "red_noise_beta": 1.2442890435564402,
            "n_core": 37,
            "baseline_degree": 2,
            "background_regressed_depth": 0.062160296653844226,
            "background_template_native_sigma": 2.0472073048464123
          }
        }
      }
    }
  ],
  "note": "Same TESS pixels; independent reduction only. Fixed QLP eclipse template and timing; uncertainties conditional and beta-inflated. TARS has no quality flags; its FLUX background provenance unspecified."
}
```

Gaia G<15 neighbors within60arcsec and required intrinsic fractional dips (G approximate passband; not calibrated TESS dilution):

```json
[
  {
    "source_id": "977665638971641088",
    "ra": "105.67151458471844",
    "dec": "46.82832953686493",
    "phot_g_mean_mag": "12.131536",
    "bp_rp": "0.8744564",
    "sep": "13.263741925334552",
    "required_fraction_G_approx": 0.3883618714215827,
    "capable": true
  },
  {
    "source_id": "977667086376402688",
    "ra": "105.69205506549349",
    "dec": "46.83663159994198",
    "phot_g_mean_mag": "13.530179",
    "bp_rp": "0.71845627",
    "sep": "47.00996217611928",
    "required_fraction_G_approx": 1.4082954793008624,
    "capable": false
  }
]
```

Original batch difference-image receipts; old/new schema duplicates are the same events:

```json
[
  {
    "tic": "192198579",
    "sector": 47,
    "n_events": 2,
    "deficit_minus_light_arcsec": 1.13,
    "peak_on_target": true,
    "depth_ap3": 0.05272,
    "psf_frac_resid": 0.112,
    "n_neighbours_60": 14,
    "n_possible": 1,
    "brightest_nb": {
      "G": 12.131536,
      "sep": 13.3
    }
  },
  {
    "tic": "192198579",
    "sector": 47,
    "n_events": 2,
    "deficit_minus_target_arcsec": 4.37,
    "deficit_minus_light_arcsec": 1.13,
    "peak_on_target": true,
    "depth_ap3": 0.05272,
    "psf_frac_resid": 0.112,
    "n_neighbours_60": 14,
    "n_possible": 1,
    "brightest_nb": {
      "G": 12.131536,
      "sep": 13.3
    }
  }
]
```

pixel-localization.json: approximate Gaussian PRF/WCS sensitivity test; formal chi-square excludes PSF mismatch and correlated pixels. Ranking reversals explicitly prevent unique attribution.

```json
{
  "source_path": "C:\\Home\\sky\\data\\sb1-scale-c3\\vet192198579\\tesscut_s047.fits",
  "sha256": "df27e113a13081327bb71173b19ba1c9369b997ef38b7b864db3f834c4f21fe3",
  "sector": 47,
  "gaia_target": {
    "source_id": "977665643267391744",
    "ra": "105.67459800174386",
    "dec": "46.8313501830083",
    "phot_g_mean_mag": "10.168605",
    "bp_rp": "0.7398691",
    "sep": "0.0"
  },
  "target_wcs_pixel": [
    7.3532083200413965,
    7.692111496566284
  ],
  "gaia_positions": [
    [
      7.3532083200413965,
      7.692111496566284
    ],
    [
      7.702888115061629,
      8.239048844337773
    ],
    [
      5.233815470578137,
      6.707548624290706
    ]
  ],
  "events": [
    2585.006212332019,
    2606.1673607779653
  ],
  "calibration": {
    "sigma_pixels": 0.7500000000000001,
    "dx_pixels": -1.1102230246251565e-16,
    "dy_pixels": -1.1102230246251565e-16
  },
  "fixed_fits": [
    {
      "source_id": "977665643267391744",
      "sep_arcsec": 0.0,
      "G": 10.168605,
      "chi2": 49930.464975993025,
      "amplitude": 305.1083254316861,
      "fractional_residual": 0.14589365111766353
    },
    {
      "source_id": "977665638971641088",
      "sep_arcsec": 13.263741925334552,
      "G": 12.131536,
      "chi2": 200134.27247391883,
      "amplitude": 191.08913100923834,
      "fractional_residual": 0.582432067633735
    },
    {
      "source_id": "977667086376402688",
      "sep_arcsec": 47.00996217611928,
      "G": 13.530179,
      "chi2": 347719.13879770954,
      "amplitude": 34.284338919481314,
      "fractional_residual": 0.9809266838782089
    }
  ],
  "free_best": {
    "chi2": 43508.43774699984,
    "pixel_x": 7.25320832004139,
    "pixel_y": 7.792111496566276,
    "distance_from_target_arcsec": 2.9698484809834893,
    "fractional_residual": 0.17499557542712396
  },
  "event_source_comparisons": [
    {
      "tc": 2585.006212332019,
      "best_source": "977665643267391744",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        69195.77084866399,
        124110.1529612737
      ]
    },
    {
      "tc": 2606.1673607779653,
      "best_source": "977665643267391744",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        80580.58795257425,
        173665.81519170967
      ]
    }
  ],
  "aperture_photometry": [
    {
      "tc": 2585.006212332019,
      "fits": [
        {
          "degree": 1,
          "depth": 0.05244960412891384,
          "formal_error": 0.00015611734931345045
        },
        {
          "degree": 2,
          "depth": 0.05250194422565496,
          "formal_error": 0.0001745093169361869
        }
      ],
      "n_core": 36
    },
    {
      "tc": 2606.1673607779653,
      "fits": [
        {
          "degree": 1,
          "depth": 0.05296436288580969,
          "formal_error": 0.00015224170296405896
        },
        {
          "degree": 2,
          "depth": 0.052915617967813994,
          "formal_error": 0.0001701979193123977
        }
      ],
      "n_core": 36
    }
  ],
  "calibration_note": "Approximate Gaussian PSFs at own Gaia cone positions; no extra empirical source.",
  "caution": "Same TESS pixels as QLP, independent aperture reduction. Approximate circular Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity."
}
```

## Archives and novelty

Successful current shared60arcsec VSX, Gaia vari_summary/vari_eclipsing_binary, SIMBAD exact Gaia-ID and ExoFOP TOI/CTOI responses were rechecked. Exact paths/hashes below and shared receipts preserve timestamps. No Gaia EB/vari_summary entries and no TOI/CTOI entries for these targets. SIMBAD lists known spectroscopic binaries, not prior eclipse classifications.

```json
{
  "simbad": [
    {
      "id": "Gaia DR3 977665643267391744",
      "main_id": "TYC 3391-623-1",
      "otype": "SB*",
      "ra": "105.67464026268",
      "dec": "46.83149278762"
    }
  ],
  "gaia_vari_summary": [],
  "gaia_eb": [],
  "exofop": {
    "toi_count": 0,
    "ctoi_count": 0
  },
  "shared_receipts": [
    {
      "path": "C:\\Home\\Astra\\made\\binary-handoff-2026-10-30\\shared-full-review\\vsx\\192198579.tsv",
      "sha256": "3b27bdfd3c2ffa34985ec536ad36957b97b0b7c78f7f1516e59408d1a928404e"
    },
    {
      "path": "C:\\Home\\Astra\\made\\binary-handoff-2026-10-30\\shared-full-review\\exofop\\192198579.json",
      "sha256": "6298d6fb593ac5f23f86a048c73a1e335aa59943af92a099a90bdfc627a46ef7"
    }
  ]
}
```

One bounded Harvard multi-catalogue mirror probe timed out after batchG reported all IDIA9 requests timing out. ASAS-SN, SB9, WDS, Prsa, IJspeert and Kostov tables therefore remain unchecked in this fresh pass; failed service is not a negative match. VSX raw table sections were inspected; no target EB rows found. General web searches on the ten exact SIMBAD names plus eclipsing/binary found only unrelated results, not exact-target prior publications. This does not establish novelty or a complete bibliography.

## Predictions and deciding next check

AtBTJD4344.32880: next primary~4351.96211; other conjunction~4346.39040. Photometric extrapolations are scheduling estimates, conditional on stationary orbit. For null secondary use Gaia phase uncertainty, not the single date.

Joint diluted light-curve/RV modelling to refine radii, flux ratio and small-e geometry.

Final adjudication: **CONFIRMED**. Four primary and six secondary events plus independent TESS-SPOC support an EB. Own pixel fits favor target over the13.26arcsec neighbor in both events (target residual0.146 vs neighbor0.582). High geometry residual limits dimensions, not eclipse reality.

Reproducibility: scripts and manifests retained in this batch. Original source audit completed before work; no source/paper edits or commits.

Lead control audit: {"median_primary_ppt": 63.688964104405805, "offphase_census_triggers": 0, "max_offphase_census_ppt": 0, "minimum_bg_regressed_depth_ratio": 1.0012584955795731}. Census trigger centers/durations can merge broad eclipse wings, especially253923749; they are not a calibrated blind-search catalog.
