# TIC 250742811: PLAUSIBLE

The two-kind EB signal is secure, but target versus nearly equally bright3.70arcsec companion remains ambiguous. Circular PSF favors target; expanded calibration reverses preference and event rankings. RV agreement supports target but cannot resolve the contradictory localization.

Full review: COMPLETE (adjudicated). Novelty: LIMITED; successful checks found no target EB classification, but several catalogues were unavailable.

Raw untrimmed QUALITY=0 SAP: 7 accepted primary fits; median depth64.993ppt; T14=6.5470h. Primary and secondary individual timing/depth errors, duration/ingress/flat coordinates, O-C and rejected windows are tabulated below. Errors are conditional on shape/local baseline with grid and red-noise inflation. Trapezoid flat time is not measured totality.

```json
{
  "primary_shape": {
    "T14": 0.27279310344827584,
    "fr": 0.25,
    "shift": 0,
    "T14_range": [
      0.26736206896551723,
      0.27822413793103445
    ],
    "fr_range": [
      0.21,
      0.29
    ],
    "n_local_windows": 7,
    "error_note": "profile likelihood plus half-grid resolution; conditional shape model"
  },
  "primary_ephemeris": {
    "P": 8.250042373895647,
    "P_error": 5.579828360696208e-06,
    "Tref": 2788.1877537589776,
    "Tref_error": 0.0003958331927237726,
    "reference_cycle": 120,
    "T0": 1798.1826688914998,
    "chi2": 3.805082125142994,
    "dof": 5,
    "n": 7,
    "oc_rms_minutes": 1.078264646287826
  },
  "primary_events": [
    {
      "status": "fit",
      "sec": 18,
      "tc_nom": 1798.1764,
      "tc": 1798.1813102758622,
      "tc_error": 0.001667995299098756,
      "depth": 0.06484423694331864,
      "depth_error": 0.000565041426200636,
      "T14": 0.27279310344827584,
      "T12": 0.06819827586206896,
      "T23": 0.13639655172413792,
      "beta": 1.0,
      "n_in": 13,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -0.0003152054859450466,
      "depth_with_background": 0.06502053114254382,
      "scan_edge": false,
      "x_template_shift_pix": 0.011766425097358485,
      "x_err_pix": 0.0003586022652207079,
      "y_template_shift_pix": -0.007989795703439476,
      "y_err_pix": 0.00039726368746983184,
      "cycle": 0,
      "oc_days": -0.0013586156376277359
    },
    {
      "status": "fit",
      "sec": 18,
      "tc_nom": 1806.4264624559094,
      "tc": 1806.4330094903921,
      "tc_error": 0.001667995299098756,
      "depth": 0.06499829368331307,
      "depth_error": 0.0006913557784017399,
      "T14": 0.27279310344827584,
      "T12": 0.06819827586206896,
      "T23": 0.13639655172413792,
      "beta": 1.026213487078266,
      "n_in": 13,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -0.0001951383376145231,
      "depth_with_background": 0.06520571987925058,
      "scan_edge": false,
      "x_template_shift_pix": 0.011132160932919292,
      "x_err_pix": 0.0004414276182844221,
      "y_template_shift_pix": -0.008028685000395256,
      "y_err_pix": 0.000352510090550045,
      "cycle": 1,
      "oc_days": 0.0002982249966407835
    },
    {
      "status": "insufficient",
      "tc_nom": 1814.676524911819,
      "sec": 18,
      "n_in": 12,
      "cycle": 2
    },
    {
      "status": "fit",
      "sec": 58,
      "tc_nom": 2887.1846441800367,
      "tc": 2887.187917697278,
      "tc_error": 0.0008183793103448276,
      "depth": 0.06470636508371255,
      "depth_error": 0.0006426087694457062,
      "T14": 0.27279310344827584,
      "T12": 0.06819827586206896,
      "T23": 0.13639655172413792,
      "beta": 1.848984268162736,
      "n_in": 117,
      "flagged_core": 1,
      "flag_bits_core": 1073741824,
      "background_fake_depth": -2.774946869117115e-05,
      "depth_with_background": 0.06473193735661048,
      "scan_edge": false,
      "x_template_shift_pix": 0.008920549342915647,
      "x_err_pix": 0.0005686364178682756,
      "y_template_shift_pix": -0.005935528331239723,
      "y_err_pix": 0.0007961210478660969,
      "cycle": 132,
      "oc_days": -0.0003445484471740201
    },
    {
      "status": "fit",
      "sec": 58,
      "tc_nom": 2895.434706635946,
      "tc": 2895.4379801531873,
      "tc_error": 0.0008183793103448276,
      "depth": 0.0655540490999937,
      "depth_error": 0.0005984044044424826,
      "T14": 0.27279310344827584,
      "T12": 0.06819827586206896,
      "T23": 0.13639655172413792,
      "beta": 1.7860780211843543,
      "n_in": 118,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": 2.4198141828856887e-05,
      "depth_with_background": 0.06554113668225182,
      "scan_edge": false,
      "x_template_shift_pix": 0.008455786582048402,
      "x_err_pix": 0.0005329113160735296,
      "y_template_shift_pix": -0.005303374584572711,
      "y_err_pix": 0.0006712915819085907,
      "cycle": 133,
      "oc_days": -0.0003244664335397829
    },
    {
      "status": "fit",
      "sec": 58,
      "tc_nom": 2903.6847690918557,
      "tc": 2903.689679367718,
      "tc_error": 0.0008183793103448276,
      "depth": 0.0641071908020685,
      "depth_error": 0.0005179796359521179,
      "T14": 0.27279310344827584,
      "T12": 0.06819827586206896,
      "T23": 0.13639655172413792,
      "beta": 1.56379209092289,
      "n_in": 95,
      "flagged_core": 1,
      "flag_bits_core": 1073741824,
      "background_fake_depth": -1.64057003502551e-05,
      "depth_with_background": 0.06412370926797309,
      "scan_edge": false,
      "x_template_shift_pix": 0.009767358929187146,
      "x_err_pix": 0.0003315278283742282,
      "y_template_shift_pix": -0.009260478389947785,
      "y_err_pix": 0.0003984649415396329,
      "cycle": 134,
      "oc_days": 0.0013323742014108575
    },
    {
      "status": "fit",
      "sec": 85,
      "tc_nom": 3613.190140300061,
      "tc": 3613.191777058682,
      "tc_error": 0.0008183793103448276,
      "depth": 0.06544827032454806,
      "depth_error": 0.0006338143665439024,
      "T14": 0.27279310344827584,
      "T12": 0.06819827586206896,
      "T23": 0.13639655172413792,
      "beta": 1.7683446469979394,
      "n_in": 118,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -8.513175891552684e-05,
      "depth_with_background": 0.06551497403103827,
      "scan_edge": false,
      "x_template_shift_pix": 0.009493360275919767,
      "x_err_pix": 0.00040153179966421495,
      "y_template_shift_pix": -0.005735187697881884,
      "y_err_pix": 0.00045292323698481094,
      "cycle": 220,
      "oc_days": -0.00021408986049209489
    },
    {
      "status": "fit",
      "sec": 85,
      "tc_nom": 3621.440202755971,
      "tc": 3621.4418395145917,
      "tc_error": 0.0008183793103448276,
      "depth": 0.06499268676413543,
      "depth_error": 0.0005108555987482614,
      "T14": 0.27279310344827584,
      "T12": 0.06819827586206896,
      "T23": 0.13639655172413792,
      "beta": 1.6466569223690477,
      "n_in": 117,
      "flagged_core": 1,
      "flag_bits_core": 1073741824,
      "background_fake_depth": -4.193491407717626e-05,
      "depth_with_background": 0.06502758634360307,
      "scan_edge": false,
      "x_template_shift_pix": 0.009353336508415425,
      "x_err_pix": 0.0004698640156207676,
      "y_template_shift_pix": -0.005124105929248788,
      "y_err_pix": 0.0004991856690988542,
      "cycle": 221,
      "oc_days": -0.0001940078464031103
    },
    {
      "status": "insufficient",
      "tc_nom": 3629.6902652118797,
      "sec": 85,
      "n_in": 0,
      "cycle": 222
    }
  ],
  "secondary": {
    "predicted_gaia_phase": 0.5294820156192207,
    "profile_phase": 0.4997229208198667,
    "statistic": {
      "n": 8,
      "depth": 0.0061856880236249015,
      "error": 0.00012454310236492862,
      "snr": 49.66704623673156,
      "scatter": 0.0007070672396709246,
      "chi2": 20.640159907926943,
      "dof": 7,
      "empirical_error": 0.0002499860199630823,
      "n_individual_gt3sigma": 8
    },
    "events": [
      {
        "status": "fit",
        "sec": 18,
        "tc_nom": 1794.0553617895748,
        "tc": 1794.0504515137127,
        "tc_error": 0.004091896551724136,
        "depth": 0.006235766004423604,
        "depth_error": 0.0003835722173552852,
        "T14": 0.27279310344827584,
        "T12": 0.06819827586206896,
        "T23": 0.13639655172413792,
        "beta": 1.0,
        "n_in": 13,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": -0.00012962111802702157,
        "depth_with_background": 0.006369459609736923,
        "scan_edge": false,
        "x_template_shift_pix": 0.0021370784701941004,
        "x_err_pix": 0.00046161860631349904,
        "y_template_shift_pix": 0.0005377867287622714,
        "y_err_pix": 0.0004601092497965933,
        "cycle": -1,
        "oc_days": -0.002302665481238364
      },
      {
        "status": "insufficient",
        "tc_nom": 1802.3054041634705,
        "sec": 18,
        "n_in": 0,
        "cycle": 0
      },
      {
        "status": "fit",
        "sec": 18,
        "tc_nom": 1810.5554465373662,
        "tc": 1810.5439892270213,
        "tc_error": 0.007365413793103445,
        "depth": 0.004668231014573021,
        "depth_error": 0.0005513816861231483,
        "T14": 0.27279310344827584,
        "T12": 0.06819827586206896,
        "T23": 0.13639655172413792,
        "beta": 1.1880129139763567,
        "n_in": 13,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": -5.054754037551146e-05,
        "depth_with_background": 0.004719551818400532,
        "scan_edge": false,
        "x_template_shift_pix": 0.002134440337367059,
        "x_err_pix": 0.0003979759367509644,
        "y_template_shift_pix": -0.00012834742369227135,
        "y_err_pix": 0.0004198840803033999,
        "cycle": 1,
        "oc_days": -0.008886490161557958
      },
      {
        "status": "fit",
        "sec": 58,
        "tc_nom": 2883.0609551438006,
        "tc": 2883.069138936904,
        "tc_error": 0.0024551379310344817,
        "depth": 0.0070610162162665175,
        "depth_error": 0.00033397495599649996,
        "T14": 0.27279310344827584,
        "T12": 0.06819827586206896,
        "T23": 0.13639655172413792,
        "beta": 1.1177250336300957,
        "n_in": 118,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": 1.570535205040689e-05,
        "depth_with_background": 0.0070471498483994045,
        "scan_edge": false,
        "x_template_shift_pix": 0.0010507893769104994,
        "x_err_pix": 0.0002613440845157504,
        "y_template_shift_pix": -0.006037375853397182,
        "y_err_pix": 0.0005950600723089663,
        "cycle": 131,
        "oc_days": 0.008363250441107084
      },
      {
        "status": "fit",
        "sec": 58,
        "tc_nom": 2891.3109975176963,
        "tc": 2891.3142710349375,
        "tc_error": 0.0016367586206896545,
        "depth": 0.00628605032407579,
        "depth_error": 0.00028603350107928195,
        "T14": 0.27279310344827584,
        "T12": 0.06819827586206896,
        "T23": 0.13639655172413792,
        "beta": 1.1122897086674854,
        "n_in": 118,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": -3.99831607574846e-05,
        "depth_with_background": 0.006323301936464825,
        "scan_edge": false,
        "x_template_shift_pix": 0.0008742851499615171,
        "x_err_pix": 0.0002067170318080233,
        "y_template_shift_pix": 0.00021269327881457903,
        "y_err_pix": 0.00031354639513794216,
        "cycle": 132,
        "oc_days": 0.003434579480199318
      },
      {
        "status": "fit",
        "sec": 58,
        "tc_nom": 2899.561039891592,
        "tc": 2899.5495825812473,
        "tc_error": 0.0024551379310344817,
        "depth": 0.0064133644852624756,
        "depth_error": 0.00029420539821289367,
        "T14": 0.27279310344827584,
        "T12": 0.06819827586206896,
        "T23": 0.13639655172413792,
        "beta": 1.0643652178955478,
        "n_in": 118,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": -0.0001790628540152048,
        "depth_with_background": 0.006593239995709656,
        "scan_edge": false,
        "x_template_shift_pix": 0.0011806564778787546,
        "x_err_pix": 0.000204465032800145,
        "y_template_shift_pix": 2.3086437988060068e-05,
        "y_err_pix": 0.000275682212246738,
        "cycle": 133,
        "oc_days": -0.011314643204514141
      },
      {
        "status": "fit",
        "sec": 58,
        "tc_nom": 2907.8110822654876,
        "tc": 2907.8094455068667,
        "tc_error": 0.004091896551724136,
        "depth": 0.00591918847329002,
        "depth_error": 0.0003702223859743491,
        "T14": 0.27279310344827584,
        "T12": 0.06819827586206896,
        "T23": 0.13639655172413792,
        "beta": 1.3676572531198716,
        "n_in": 117,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": -6.560196852804803e-07,
        "depth_with_background": 0.005919895964413319,
        "scan_edge": false,
        "x_template_shift_pix": 0.0016862883805665086,
        "x_err_pix": 0.00023850884584868386,
        "y_template_shift_pix": -0.0005030670600216045,
        "y_err_pix": 0.0002413365022724668,
        "cycle": 134,
        "oc_days": -0.0015124865794859943
      },
      {
        "status": "fit",
        "sec": 85,
        "tc_nom": 3617.314726420513,
        "tc": 3617.3212734549957,
        "tc_error": 0.006547034482758625,
        "depth": 0.0051227248949377155,
        "depth_error": 0.0004794111693785438,
        "T14": 0.27279310344827584,
        "T12": 0.06819827586206896,
        "T23": 0.13639655172413792,
        "beta": 1.4924368007829443,
        "n_in": 106,
        "flagged_core": 4,
        "flag_bits_core": 1073741856,
        "background_fake_depth": -0.00014167744658160673,
        "depth_with_background": 0.005249337809095555,
        "scan_edge": false,
        "x_template_shift_pix": -0.0014119611793245487,
        "x_err_pix": 0.00038395904362103155,
        "y_template_shift_pix": 0.004595212461296784,
        "y_err_pix": 0.0006338797058164146,
        "cycle": 220,
        "oc_days": 0.005089328025405848
      },
      {
        "status": "insufficient",
        "tc_nom": 3625.564768794409,
        "sec": 85,
        "n_in": 0,
        "cycle": 221
      },
      {
        "status": "fit",
        "sec": 85,
        "tc_nom": 3633.8148111683045,
        "tc": 3633.8131744096836,
        "tc_error": 0.0024551379310344817,
        "depth": 0.006137206294827567,
        "depth_error": 0.00031628504982715165,
        "T14": 0.27279310344827584,
        "T12": 0.06819827586206896,
        "T23": 0.13639655172413792,
        "beta": 1.1640860839811675,
        "n_in": 118,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": -1.138341765570234e-05,
        "depth_with_background": 0.006148741908439165,
        "scan_edge": false,
        "x_template_shift_pix": 0.0010598755617953076,
        "x_err_pix": 0.00020996109455733708,
        "y_template_shift_pix": 0.00017151611689759314,
        "y_err_pix": 0.00017579699292566252,
        "cycle": 222,
        "oc_days": -0.0031312552755480283
      }
    ],
    "ephemeris": {
      "P": 8.250060768994462,
      "P_error": 4.916338284452402e-05,
      "Tref": 2808.810228765513,
      "Tref_error": 0.0027098607203328777,
      "reference_cycle": 122,
      "T0": 1802.3028149481884,
      "chi2": 41.385713641345426,
      "dof": 6,
      "n": 8,
      "oc_rms_minutes": 9.091231386335563
    },
    "shape": {
      "T14": 0.27279310344827584,
      "fr": 0.25,
      "shift": 0,
      "T14_range": [
        0.26736206896551723,
        0.27822413793103445
      ],
      "fr_range": [
        0.21,
        0.29
      ],
      "n_local_windows": 7,
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
      "sec": 18,
      "tc": 1794.0515816387117,
      "depth": 0.008052314862445509,
      "n": 11,
      "phase": 0.49926472306863656,
      "threshold": 0.0036427856420066787,
      "duration": 0.22916794818308972
    },
    {
      "sec": 18,
      "tc": 1798.180441169915,
      "depth": 0.06500279141828735,
      "n": 13,
      "phase": 0.999729974528142,
      "threshold": 0.0036427856420066787,
      "duration": 0.2708331681611753
    },
    {
      "sec": 18,
      "tc": 1806.432498180764,
      "depth": 0.06604353801866403,
      "n": 13,
      "phase": 0.9999741716924845,
      "threshold": 0.0036427856420066787,
      "duration": 0.2708305345985309
    },
    {
      "sec": 18,
      "tc": 1810.5214842135895,
      "depth": 0.007593575696552168,
      "n": 8,
      "phase": 0.49560629665751676,
      "threshold": 0.0036427856420066787,
      "duration": 0.18749693455004035
    },
    {
      "sec": 18,
      "tc": 1814.684212856866,
      "depth": 0.0639919677728582,
      "n": 12,
      "phase": 0.00017687394909682297,
      "threshold": 0.0036427856420066787,
      "duration": 0.2499949608808265
    },
    {
      "sec": 58,
      "tc": 2883.0726150035725,
      "depth": 0.012378715918477168,
      "n": 17,
      "phase": 0.5011362298967867,
      "threshold": 0.008044253492709904,
      "duration": 0.16666968741537858
    },
    {
      "sec": 58,
      "tc": 2887.1878610053122,
      "depth": 0.06744627547169857,
      "n": 107,
      "phase": 0.9999513650482186,
      "threshold": 0.008044253492709904,
      "duration": 0.2546326264873642
    },
    {
      "sec": 58,
      "tc": 2891.2758864928023,
      "depth": 0.010818397617835429,
      "n": 12,
      "phase": 0.49546706087363646,
      "threshold": 0.008044253492709904,
      "duration": 0.16435258504589
    },
    {
      "sec": 58,
      "tc": 2895.4383929753435,
      "depth": 0.06861979242724081,
      "n": 109,
      "phase": 1.0709729536984014e-05,
      "threshold": 0.008044253492709904,
      "duration": 0.25231403539737585
    },
    {
      "sec": 58,
      "tc": 2899.5565863387815,
      "depth": 0.011865881528580258,
      "n": 9,
      "phase": 0.499183099009457,
      "threshold": 0.008044253492709904,
      "duration": 0.16435101730485258
    },
    {
      "sec": 58,
      "tc": 2903.69848128535,
      "depth": 0.06781591081211535,
      "n": 91,
      "phase": 0.001228392700824088,
      "threshold": 0.008044253492709904,
      "duration": 0.210645535616095
    },
    {
      "sec": 58,
      "tc": 2907.7782175806924,
      "depth": 0.009099830211524607,
      "n": 3,
      "phase": 0.4957393431234607,
      "threshold": 0.008044253492709904,
      "duration": 0.07870216234823602
    },
    {
      "sec": 58,
      "tc": 2907.889512041249,
      "depth": 0.010065000745648311,
      "n": 2,
      "phase": 0.5092295114780825,
      "threshold": 0.008044253492709904,
      "duration": 0.016203415870677418
    },
    {
      "sec": 85,
      "tc": 3613.192161104823,
      "depth": 0.06834020434602739,
      "n": 107,
      "phase": 2.060065546061196e-05,
      "threshold": 0.0080548676054631,
      "duration": 0.24768951692476548
    },
    {
      "sec": 85,
      "tc": 3616.65595603884,
      "depth": 0.009583241999939651,
      "n": 2,
      "phase": 0.41987237559629875,
      "threshold": 0.0080548676054631,
      "duration": 0.027778143235991593
    },
    {
      "sec": 85,
      "tc": 3616.7821389395062,
      "depth": 0.009971371674406648,
      "n": 3,
      "phase": 0.4351671940890469,
      "threshold": 0.0080548676054631,
      "duration": 0.03703753059335213
    },
    {
      "sec": 85,
      "tc": 3617.3573990309187,
      "depth": 0.010813277831236867,
      "n": 6,
      "phase": 0.5048953318781173,
      "threshold": 0.0080548676054631,
      "duration": 0.10185319231459289
    },
    {
      "sec": 85,
      "tc": 3621.441179857558,
      "depth": 0.07013117322854634,
      "n": 107,
      "phase": 0.9998965260005548,
      "threshold": 0.0080548676054631,
      "duration": 0.25000137073584483
    },
    {
      "sec": 85,
      "tc": 3633.803159711998,
      "depth": 0.011946884670090752,
      "n": 9,
      "phase": 0.49831063033960277,
      "threshold": 0.0080548676054631,
      "duration": 0.1620329047350424
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
    "w_tp_corr": 0.99955976,
    "gaia_comparison": [
      {
        "kind": "A",
        "epoch389_offset": 0.07444559838040732,
        "epoch389_gaia_error": 0.08457809144657302,
        "events": [
          {
            "sec": 18,
            "tc": 1798.1813102758622,
            "gaia_conjunction": 1798.3791394584994,
            "gaia_error": 0.28014713460734625,
            "offset_days": -0.19782918263717875,
            "z": -0.7061492043352672
          },
          {
            "sec": 18,
            "tc": 1806.4330094903921,
            "gaia_conjunction": 1806.6308806662564,
            "gaia_error": 0.28156846323833357,
            "offset_days": -0.19787117586429304,
            "z": -0.702733898975709
          },
          {
            "sec": 58,
            "tc": 2887.187917697278,
            "gaia_conjunction": 2887.608441338428,
            "gaia_error": 0.47137907311623095,
            "offset_days": -0.4205236411498845,
            "z": -0.8921121690978795
          },
          {
            "sec": 58,
            "tc": 2895.4379801531873,
            "gaia_conjunction": 2895.860384809691,
            "gaia_error": 0.4728443651170224,
            "offset_days": -0.42240465650365877,
            "z": -0.8933257008124328
          },
          {
            "sec": 58,
            "tc": 2903.689679367718,
            "gaia_conjunction": 2904.112207797224,
            "gaia_error": 0.4743098036728816,
            "offset_days": -0.42252842950620106,
            "z": -0.8908266227960984
          },
          {
            "sec": 85,
            "tc": 3613.191777058682,
            "gaia_conjunction": 3613.7607591129263,
            "gaia_error": 0.6007678554570071,
            "offset_days": -0.5689820542443158,
            "z": -0.9470904962061278
          },
          {
            "sec": 85,
            "tc": 3621.4418395145917,
            "gaia_conjunction": 3622.012560920723,
            "gaia_error": 0.6022422266781804,
            "offset_days": -0.5707214061312698,
            "z": -0.9476600176977062
          }
        ]
      },
      {
        "kind": "B",
        "epoch389_offset": 4.002440111437295,
        "epoch389_gaia_error": 0.10497095656359376,
        "events": [
          {
            "sec": 18,
            "tc": 1798.1813102758622,
            "gaia_conjunction": 1794.4760146257877,
            "gaia_error": 0.32740541905895065,
            "offset_days": 3.705295650074504,
            "z": 11.31700133898516
          },
          {
            "sec": 18,
            "tc": 1806.4330094903921,
            "gaia_conjunction": 1802.7277689881564,
            "gaia_error": 0.3288434152122665,
            "offset_days": 3.7052405022357107,
            "z": 11.267346910280418
          },
          {
            "sec": 58,
            "tc": 2887.187917697278,
            "gaia_conjunction": 2883.7026503988395,
            "gaia_error": 0.5197016764807625,
            "offset_days": 3.48526729843843,
            "z": 6.706276186792065
          },
          {
            "sec": 58,
            "tc": 2895.4379801531873,
            "gaia_conjunction": 2891.954301979682,
            "gaia_error": 0.5211705060971212,
            "offset_days": 3.483678173505268,
            "z": 6.684326602930508
          },
          {
            "sec": 58,
            "tc": 2903.689679367718,
            "gaia_conjunction": 2900.2060634155723,
            "gaia_error": 0.5226394488559245,
            "offset_days": 3.4836159521455556,
            "z": 6.665420471070426
          },
          {
            "sec": 85,
            "tc": 3613.191777058682,
            "gaia_conjunction": 3609.8541951442694,
            "gaia_error": 0.6493073939399605,
            "offset_days": 3.337581914412567,
            "z": 5.14021447246831
          },
          {
            "sec": 85,
            "tc": 3621.4418395145917,
            "gaia_conjunction": 3618.1058450123246,
            "gaia_error": 0.6507834325692312,
            "offset_days": 3.3359945022671127,
            "z": 5.126116765699119
          }
        ]
      }
    ],
    "primary_conjunction": "A",
    "predicted_secondary_phase": 0.5294820156192207,
    "secondary": {
      "n": 8,
      "depth": -0.002358024932909564,
      "error": 0.000341361705063656,
      "snr": -6.907702000345491,
      "scatter": 0.0002574930940321734,
      "chi2": 0.5769329343639855,
      "dof": 7,
      "phase": 0.5294820156192207,
      "control_scatter": 0.004933638944449242,
      "upper_3sigma": 0.014800916833347725
    },
    "secondary_windows": {
      "gaia_other_windows": [
        {
          "status": "fit",
          "sec": 18,
          "tc_nom": 1794.3008755826784,
          "tc": 1794.3008755826784,
          "tc_error": 0.001667995299098756,
          "depth": -0.002703080729458618,
          "depth_error": 0.0010267251567122508,
          "T14": 0.27279310344827584,
          "T12": 0.06819827586206896,
          "T23": 0.13639655172413792,
          "beta": 1.3043312896564276,
          "n_in": 13,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": -2.075128972617295e-05,
          "depth_with_background": -0.002667491141725176,
          "scan_edge": false,
          "x_template_shift_pix": 0.00016728494438936957,
          "x_err_pix": 0.0005518997431999415,
          "y_template_shift_pix": 0.0012534953949367067,
          "y_err_pix": 0.0005897511838318306,
          "cycle": -1
        },
        {
          "status": "insufficient",
          "tc_nom": 1802.550917956574,
          "sec": 18,
          "n_in": 0,
          "cycle": 0
        },
        {
          "status": "fit",
          "sec": 18,
          "tc_nom": 1810.8009603304697,
          "tc": 1810.8009603304697,
          "tc_error": 0.001667995299098756,
          "depth": -0.0025905574055509377,
          "depth_error": 0.0008009094105458308,
          "T14": 0.27279310344827584,
          "T12": 0.06819827586206896,
          "T23": 0.13639655172413792,
          "beta": 1.2825120830082115,
          "n_in": 13,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": -3.019923366874881e-06,
          "depth_with_background": -0.0025925331982940307,
          "scan_edge": false,
          "x_template_shift_pix": 0.00017543138363482384,
          "x_err_pix": 0.0004988713723852324,
          "y_template_shift_pix": 0.00019234267450339405,
          "y_err_pix": 0.0004263075360494071,
          "cycle": 1
        },
        {
          "status": "fit",
          "sec": 58,
          "tc_nom": 2883.306468936904,
          "tc": 2883.306468936904,
          "tc_error": 0.0008183793103448276,
          "depth": -0.0020591041861379522,
          "depth_error": 0.0011684462938263377,
          "T14": 0.27279310344827584,
          "T12": 0.06819827586206896,
          "T23": 0.13639655172413792,
          "beta": 2.9713312481490193,
          "n_in": 117,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": -0.0003320600615450444,
          "depth_with_background": -0.0017109115994405374,
          "scan_edge": false,
          "x_template_shift_pix": 0.00048715507154625516,
          "x_err_pix": 0.0006362584496034367,
          "y_template_shift_pix": -0.003868730023661568,
          "y_err_pix": 0.0013390413979296495,
          "cycle": 131
        },
        {
          "status": "fit",
          "sec": 58,
          "tc_nom": 2891.5565113107996,
          "tc": 2891.5565113107996,
          "tc_error": 0.0008183793103448276,
          "depth": -0.002242596408226797,
          "depth_error": 0.0009977295103980569,
          "T14": 0.27279310344827584,
          "T12": 0.06819827586206896,
          "T23": 0.13639655172413792,
          "beta": 2.85476514242627,
          "n_in": 118,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": 5.0202607260759545e-05,
          "depth_with_background": -0.0022899784996311475,
          "scan_edge": false,
          "x_template_shift_pix": 0.00021690044248659772,
          "x_err_pix": 0.0005545070227901655,
          "y_template_shift_pix": 0.00043341389619720033,
          "y_err_pix": 0.000811921577256935,
          "cycle": 132
        },
        {
          "status": "fit",
          "sec": 58,
          "tc_nom": 2899.8065536846952,
          "tc": 2899.8065536846952,
          "tc_error": 0.0008183793103448276,
          "depth": -0.002438630899183078,
          "depth_error": 0.0009664905862927101,
          "T14": 0.27279310344827584,
          "T12": 0.06819827586206896,
          "T23": 0.13639655172413792,
          "beta": 2.7201377168054295,
          "n_in": 117,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": -2.4363704512331676e-05,
          "depth_with_background": -0.002394345609935422,
          "scan_edge": false,
          "x_template_shift_pix": -9.394236093450714e-05,
          "x_err_pix": 0.0005452300090167446,
          "y_template_shift_pix": 7.970402849024048e-05,
          "y_err_pix": 0.000725106281265921,
          "cycle": 133
        },
        {
          "status": "fit",
          "sec": 58,
          "tc_nom": 2908.056596058591,
          "tc": 2908.056596058591,
          "tc_error": 0.0008183793103448276,
          "depth": -0.00256730027930319,
          "depth_error": 0.0009667780124470698,
          "T14": 0.27279310344827584,
          "T12": 0.06819827586206896,
          "T23": 0.13639655172413792,
          "beta": 2.8239848949936737,
          "n_in": 117,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": -0.00010214352352331923,
          "depth_with_background": -0.002468599175331026,
          "scan_edge": false,
          "x_template_shift_pix": 0.00046037113631807825,
          "x_err_pix": 0.0005243880316636901,
          "y_template_shift_pix": 5.786638838235136e-05,
          "y_err_pix": 0.0004982988255781436,
          "cycle": 134
        },
        {
          "status": "fit",
          "sec": 85,
          "tc_nom": 3617.5602402136165,
          "tc": 3617.5602402136165,
          "tc_error": 0.0008183793103448276,
          "depth": -0.0019265783443855181,
          "depth_error": 0.0009043374715670892,
          "T14": 0.27279310344827584,
          "T12": 0.06819827586206896,
          "T23": 0.13639655172413792,
          "beta": 2.606906914802729,
          "n_in": 117,
          "flagged_core": 1,
          "flag_bits_core": 1073741824,
          "background_fake_depth": 0.00016829476513128847,
          "depth_with_background": -0.002088408244454671,
          "scan_edge": false,
          "x_template_shift_pix": -0.0005750501150551021,
          "x_err_pix": 0.0005886410908041156,
          "y_template_shift_pix": 0.0024957753849400876,
          "y_err_pix": 0.0009266620178747775,
          "cycle": 220
        },
        {
          "status": "insufficient",
          "tc_nom": 3625.810282587512,
          "sec": 85,
          "n_in": 0,
          "cycle": 221
        },
        {
          "status": "fit",
          "sec": 85,
          "tc_nom": 3634.060324961408,
          "tc": 3634.060324961408,
          "tc_error": 0.0008183793103448276,
          "depth": -0.0022167534219596466,
          "depth_error": 0.0010133373176758715,
          "T14": 0.27279310344827584,
          "T12": 0.06819827586206896,
          "T23": 0.13639655172413792,
          "beta": 2.847844396489732,
          "n_in": 118,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": -8.135023258738135e-05,
          "depth_with_background": -0.0021380394228576083,
          "scan_edge": false,
          "x_template_shift_pix": 0.00017777823534556377,
          "x_err_pix": 0.0005315766357754547,
          "y_template_shift_pix": 0.0005829800494472949,
          "y_err_pix": 0.00045607300708735195,
          "cycle": 222
        }
      ]
    },
    "controls": [
      {
        "n": 7,
        "depth": 0.0002339689036860697,
        "error": 0.00030822506255121786,
        "snr": 0.7590846174203988,
        "scatter": 0.0023735791773205404,
        "chi2": 6.958482937029631,
        "dof": 6,
        "phase": 0.1
      },
      {
        "n": 8,
        "depth": -0.00015279714702447913,
        "error": 0.0001294793545211321,
        "snr": -1.180088884359872,
        "scatter": 0.0004963791069067155,
        "chi2": 12.12894488324898,
        "dof": 7,
        "phase": 0.15000000000000002
      },
      {
        "n": 8,
        "depth": -0.00014858320610833828,
        "error": 0.00013442037348102096,
        "snr": -1.1053622472587237,
        "scatter": 0.0007949392245613908,
        "chi2": 22.41467787869742,
        "dof": 7,
        "phase": 0.20000000000000004
      },
      {
        "n": 7,
        "depth": 1.8636758329279843e-05,
        "error": 0.0001497644485429417,
        "snr": 0.12444046975498432,
        "scatter": 0.00048144686582165283,
        "chi2": 11.220212732750067,
        "dof": 6,
        "phase": 0.25000000000000006
      },
      {
        "n": 8,
        "depth": -0.00039430724080093214,
        "error": 0.00012474389249670373,
        "snr": -3.160934238214119,
        "scatter": 0.0007801501742784664,
        "chi2": 35.810574236321024,
        "dof": 7,
        "phase": 0.30000000000000004
      },
      {
        "n": 9,
        "depth": -2.7661258640610666e-05,
        "error": 0.00012564111623851814,
        "snr": -0.22016087940589688,
        "scatter": 0.0006966210179468858,
        "chi2": 26.22998492619093,
        "dof": 8,
        "phase": 0.3500000000000001
      },
      {
        "n": 7,
        "depth": 0.0002327215207937395,
        "error": 0.0002418928565762377,
        "snr": 0.9620851317715219,
        "scatter": 0.000869253131090006,
        "chi2": 16.287849095241615,
        "dof": 6,
        "phase": 0.40000000000000013
      },
      {
        "n": 7,
        "depth": -0.0013976927062484582,
        "error": 0.00039952868770884133,
        "snr": -3.4983538084930568,
        "scatter": 0.0006732073940602478,
        "chi2": 2.977501992620912,
        "dof": 6,
        "phase": 0.45000000000000007
      },
      {
        "n": 8,
        "depth": 0.00613435645805471,
        "error": 0.00012803803870010497,
        "snr": 47.91042193658408,
        "scatter": 0.000720357826590714,
        "chi2": 19.2297008668373,
        "dof": 7,
        "phase": 0.5000000000000001
      },
      {
        "n": 8,
        "depth": -0.001764302705134385,
        "error": 0.00034878472743480975,
        "snr": -5.058428785314705,
        "scatter": 0.00028221431546230995,
        "chi2": 0.5442692423745971,
        "dof": 7,
        "phase": 0.5500000000000002
      },
      {
        "n": 8,
        "depth": 0.0006429306515913894,
        "error": 0.0002323431613892706,
        "snr": 2.7671597810198314,
        "scatter": 0.00031061438995043345,
        "chi2": 1.8465171031444485,
        "dof": 7,
        "phase": 0.6000000000000002
      },
      {
        "n": 8,
        "depth": 5.785032471555151e-06,
        "error": 0.00011337393057022949,
        "snr": 0.051026126045542824,
        "scatter": 0.0005044380588260065,
        "chi2": 18.97403570446348,
        "dof": 7,
        "phase": 0.6500000000000001
      },
      {
        "n": 8,
        "depth": -8.071511966848996e-05,
        "error": 0.00011323597047745577,
        "snr": -0.7128045914046331,
        "scatter": 0.0004048445109257225,
        "chi2": 11.700166512808531,
        "dof": 7,
        "phase": 0.7000000000000002
      },
      {
        "n": 7,
        "depth": 0.0002674360343747465,
        "error": 0.00012146044693534055,
        "snr": 2.2018364094865883,
        "scatter": 0.0005143733418194443,
        "chi2": 16.616644620877242,
        "dof": 6,
        "phase": 0.7500000000000002
      },
      {
        "n": 7,
        "depth": -0.0001709456526507476,
        "error": 0.0001240501309915792,
        "snr": -1.3780368572311448,
        "scatter": 0.00038923017941239283,
        "chi2": 12.87156569426556,
        "dof": 6,
        "phase": 0.8000000000000002
      },
      {
        "n": 7,
        "depth": -0.00012655156312237466,
        "error": 0.00013081638289565603,
        "snr": -0.9673984276366734,
        "scatter": 0.0007447567431196181,
        "chi2": 22.055000938598376,
        "dof": 6,
        "phase": 0.8500000000000002
      },
      {
        "n": 7,
        "depth": 0.006333375308947323,
        "error": 0.002147385021677275,
        "snr": 2.9493431522589573,
        "scatter": 0.0002569583578865338,
        "chi2": 0.013537820254490155,
        "dof": 6,
        "phase": 0.9000000000000002
      },
      {
        "n": 7,
        "depth": -0.017602761894101367,
        "error": 0.003943089897249886,
        "snr": -4.464205065773022,
        "scatter": 0.0028207658380997587,
        "chi2": 0.5011078602462928,
        "dof": 6,
        "phase": 0.9500000000000003
      },
      {
        "n": 8,
        "depth": -0.002358024932909564,
        "error": 0.000341361705063656,
        "snr": -6.907702000345491,
        "scatter": 0.0002574930940321734,
        "chi2": 0.5769329343639855,
        "dof": 7,
        "phase": 0.5294820156192207,
        "control_scatter": 0.004933638944449242,
        "upper_3sigma": 0.014800916833347725
      }
    ],
    "physics": [
      {
        "m1": 1.143,
        "m2_min": 0.439822033764002,
        "f_mass": 0.03395992893370562,
        "a_rsun": 20.026564735443678,
        "r1_rsun": 1.62427,
        "r2_approx_rsun": 0.518348189472433,
        "central_T14_hours": {
          "A": 6.814542918987544,
          "B": 6.66045065500742
        },
        "observed_T14_hours": 6.547034482758621
      }
    ],
    "period_delta_sigma": -0.9681573165677472
  },
  "covariance_geometry": {
    "bit_index": 127,
    "gaia_primary": "A",
    "gaia_relative_phase_nominal": 0.5294820156192207,
    "gaia_relative_phase_quantiles_16_50_84": [
      0.5045807407280509,
      0.5227497477010337,
      0.5430004729965459
    ],
    "gaia_relative_phase_sigma": 0.01930071332106795,
    "gaia_e_cos_omega_quantiles": [
      0.007192574702986523,
      0.0357145014669595,
      0.06755179659262689
    ],
    "gaia_e_sin_omega_quantiles": [
      -0.029692215359061126,
      -0.0038588714692126586,
      0.043879804795864744
    ],
    "photometric_phase": 0.4997229208198667,
    "photometric_e_cos_omega_first_order": -0.0004352349583847457,
    "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
    "geometry_status": "conditional shape feasibility",
    "geometry_e_sin_omega_conditional_range": [
      -0.07500000000000004,
      -0.050000000000000044
    ],
    "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
  },
  "conditional_two_disk_geometry": {
    "status": "conditional shape feasibility",
    "best": {
      "chi2": 452.1610892404347,
      "dof": 121,
      "k": 0.24999999999999997,
      "b_A": 0.23500000000000001,
      "e_sin_omega": -0.07500000000000004,
      "primary_scale": 0.928889435127105,
      "secondary_scale": 0.00591748003109156
    },
    "profile_interval_approx_95": {
      "k": [
        0.24999999999999997,
        0.24999999999999997
      ],
      "b_A": [
        0.2,
        0.23500000000000001
      ],
      "e_sin_omega": [
        -0.07500000000000004,
        -0.050000000000000044
      ]
    },
    "error_inflation": 3.736868506119295,
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
  "sector": 58,
  "provenance": "TARS",
  "fits_identity_validated": true,
  "quality_column_present": false,
  "events": [
    {
      "tc": 2887.187917697278,
      "qlp": {
        "1": {
          "depth": 0.06512902314016335,
          "error": 0.00060369056916105,
          "red_noise_beta": 1.9370194233890679,
          "n_core": 117,
          "baseline_degree": 1,
          "background_regressed_depth": 0.06517617445542219,
          "background_template_native_sigma": 0.15028751801579593
        },
        "2": {
          "depth": 0.06487414443067517,
          "error": 0.0006691565822854387,
          "red_noise_beta": 1.9257403248127594,
          "n_core": 117,
          "baseline_degree": 2,
          "background_regressed_depth": 0.06490112644744016,
          "background_template_native_sigma": 0.08406070936066994
        }
      },
      "independent": {
        "FLUX": {
          "1": {
            "depth": 0.0341978244070854,
            "error": 0.000339027519089657,
            "red_noise_beta": 1.6784321043470738,
            "n_core": 118,
            "baseline_degree": 1,
            "background_regressed_depth": null,
            "background_template_native_sigma": null
          },
          "2": {
            "depth": 0.03408763446189231,
            "error": 0.00037707368603088077,
            "red_noise_beta": 1.6725118693110865,
            "n_core": 118,
            "baseline_degree": 2,
            "background_regressed_depth": null,
            "background_template_native_sigma": null
          }
        }
      }
    },
    {
      "tc": 2895.4379801531873,
      "qlp": {
        "1": {
          "depth": 0.06543887878565166,
          "error": 0.0005412210935256819,
          "red_noise_beta": 1.7992288980328592,
          "n_core": 118,
          "baseline_degree": 1,
          "background_regressed_depth": 0.06551652470571234,
          "background_template_native_sigma": 0.3379849119088528
        },
        "2": {
          "depth": 0.06552575477963204,
          "error": 0.0006034679783615166,
          "red_noise_beta": 1.797483878532499,
          "n_core": 118,
          "baseline_degree": 2,
          "background_regressed_depth": 0.06551240060627835,
          "background_template_native_sigma": -0.05782152976832072
        }
      },
      "independent": {
        "FLUX": {
          "1": {
            "depth": 0.036454008560811095,
            "error": 0.00036683580259939583,
            "red_noise_beta": 1.8395826565902857,
            "n_core": 118,
            "baseline_degree": 1,
            "background_regressed_depth": null,
            "background_template_native_sigma": null
          },
          "2": {
            "depth": 0.03644040379043338,
            "error": 0.0004115471402197393,
            "red_noise_beta": 1.8393749936492814,
            "n_core": 118,
            "baseline_degree": 2,
            "background_regressed_depth": null,
            "background_template_native_sigma": null
          }
        }
      }
    },
    {
      "tc": 2903.689679367718,
      "qlp": {
        "1": {
          "depth": 0.06413342076541811,
          "error": 0.00044538776236467654,
          "red_noise_beta": 1.558316043164275,
          "n_core": 97,
          "baseline_degree": 1,
          "background_regressed_depth": 0.06419608675825966,
          "background_template_native_sigma": 0.17369136380779254
        },
        "2": {
          "depth": 0.06412341276515901,
          "error": 0.000516053395163022,
          "red_noise_beta": 1.5585620849841204,
          "n_core": 97,
          "baseline_degree": 2,
          "background_regressed_depth": 0.06414170785504436,
          "background_template_native_sigma": 0.050417370416782875
        }
      },
      "independent": {
        "FLUX": {
          "1": {
            "depth": 0.03607560264954888,
            "error": 0.00027862334429782227,
            "red_noise_beta": 1.4533082496128218,
            "n_core": 98,
            "baseline_degree": 1,
            "background_regressed_depth": null,
            "background_template_native_sigma": null
          },
          "2": {
            "depth": 0.03582666743288522,
            "error": 0.000314776476109704,
            "red_noise_beta": 1.421300675704658,
            "n_core": 98,
            "baseline_degree": 2,
            "background_regressed_depth": null,
            "background_template_native_sigma": null
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
    "source_id": "358654370790026496",
    "ra": "33.42414429486065",
    "dec": "50.42428787660143",
    "phot_g_mean_mag": "11.393224",
    "bp_rp": "0.82036114",
    "sep": "3.698370894837177",
    "required_fraction_G_approx": 0.0740187404938573,
    "capable": true
  },
  {
    "source_id": "358654198991334784",
    "ra": "33.44908630009805",
    "dec": "50.42142424462216",
    "phot_g_mean_mag": "11.251107",
    "bp_rp": "1.3166361",
    "sep": "54.51572619155012",
    "required_fraction_G_approx": 0.06493739921285417,
    "capable": true
  }
]
```

Original batch difference-image receipts; old/new schema duplicates are the same events:

```json
[
  {
    "tic": "250742811",
    "sector": 18,
    "n_events": 3,
    "deficit_minus_target_arcsec": 3.52,
    "deficit_minus_light_arcsec": 13.96,
    "peak_on_target": true,
    "depth_ap3": 0.03181,
    "psf_frac_resid": 0.556,
    "n_neighbours_60": 25,
    "n_possible": 2,
    "brightest_nb": {
      "G": 11.251107,
      "sep": 54.5
    }
  }
]
```

pixel-localization.json: approximate Gaussian PRF/WCS sensitivity test; formal chi-square excludes PSF mismatch and correlated pixels. Ranking reversals explicitly prevent unique attribution.

```json
{
  "source_path": "C:\\Home\\sky\\data\\sb1-scale-c3\\vet250742811\\tesscut_s018.fits",
  "sha256": "b48016a61a7d96f609a2f1c816fb951c766ba970fb752057aca03da3f4fddea0",
  "sector": 18,
  "gaia_target": {
    "source_id": "358654375087124736",
    "ra": "33.4256379929076",
    "dec": "50.423900851805286",
    "phot_g_mean_mag": "11.252031",
    "bp_rp": "0.83483505",
    "sep": "0.0"
  },
  "target_wcs_pixel": [
    7.631437718112814,
    7.817740656132482
  ],
  "gaia_positions": [
    [
      7.631437718112814,
      7.817740656132482
    ],
    [
      7.5118560822548694,
      7.949263068207227
    ],
    [
      9.774876495431474,
      6.324901063093867
    ]
  ],
  "events": [
    1798.1826688914998,
    1806.4327112653955,
    1814.6827536392911
  ],
  "calibration": {
    "sigma_pixels": 0.6500000000000001,
    "dx_pixels": 0.09999999999999987,
    "dy_pixels": -1.1102230246251565e-16
  },
  "fixed_fits": [
    {
      "source_id": "358654375087124736",
      "sep_arcsec": 0.0,
      "G": 11.252031,
      "chi2": 5293.437326913664,
      "amplitude": 158.49686592844367,
      "fractional_residual": 0.1305572638268291
    },
    {
      "source_id": "358654370790026496",
      "sep_arcsec": 3.698370894837177,
      "G": 11.393224,
      "chi2": 6051.574692789729,
      "amplitude": 156.50541294529074,
      "fractional_residual": 0.1672171987270522
    },
    {
      "source_id": "358654198991334784",
      "sep_arcsec": 54.51572619155012,
      "G": 11.251107,
      "chi2": 27405.803916701938,
      "amplitude": 14.312459551596596,
      "fractional_residual": 0.9946102136778769
    }
  ],
  "free_best": {
    "chi2": 5150.379826875676,
    "pixel_x": 7.631437718112807,
    "pixel_y": 7.917740656132475,
    "distance_from_target_arcsec": 2.0999999999998433,
    "fractional_residual": 0.11639921101960805
  },
  "event_source_comparisons": [
    {
      "tc": 1798.1826688914998,
      "best_source": "358654375087124736",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        277.26219040538535,
        12184.910579902104
      ]
    },
    {
      "tc": 1806.4327112653955,
      "best_source": "358654375087124736",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        489.8789962118558,
        9844.462921741471
      ]
    },
    {
      "tc": 1814.6827536392911,
      "best_source": "358654375087124736",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        0.5348760946162945,
        28.56791076825778
      ]
    }
  ],
  "aperture_photometry": [
    {
      "tc": 1798.1826688914998,
      "fits": [
        {
          "degree": 1,
          "depth": 0.03429884005978926,
          "formal_error": 0.0002768379327809019
        },
        {
          "degree": 2,
          "depth": 0.034401864545287,
          "formal_error": 0.00030998891425196366
        }
      ],
      "n_core": 13
    },
    {
      "tc": 1806.4327112653955,
      "fits": [
        {
          "degree": 1,
          "depth": 0.03393540629793565,
          "formal_error": 0.0003227497087879623
        },
        {
          "degree": 2,
          "depth": 0.03431930440797193,
          "formal_error": 0.00034877739629569996
        }
      ],
      "n_core": 13
    },
    {
      "tc": 1814.6827536392911,
      "fits": [
        {
          "degree": 1,
          "depth": 0.03417577787449405,
          "formal_error": 0.00046076265862423493
        },
        {
          "degree": 2,
          "depth": 0.03463212220339091,
          "formal_error": 0.00042318223713580587
        }
      ],
      "n_core": 13
    }
  ],
  "calibration_note": "Approximate Gaussian PSFs at own Gaia cone positions; no extra empirical source.",
  "caution": "Same TESS pixels as QLP, independent aperture reduction. Approximate circular Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity."
}
```

pixel-localization-elliptical.json: approximate Gaussian PRF/WCS sensitivity test; formal chi-square excludes PSF mismatch and correlated pixels. Ranking reversals explicitly prevent unique attribution.

```json
{
  "source_path": "C:\\Home\\sky\\data\\sb1-scale-c3\\vet250742811\\tesscut_s018.fits",
  "sha256": "b48016a61a7d96f609a2f1c816fb951c766ba970fb752057aca03da3f4fddea0",
  "sector": 18,
  "gaia_target": {
    "source_id": "358654375087124736",
    "ra": "33.4256379929076",
    "dec": "50.423900851805286",
    "phot_g_mean_mag": "11.252031",
    "bp_rp": "0.83483505",
    "sep": "0.0"
  },
  "target_wcs_pixel": [
    7.631437718112814,
    7.817740656132482
  ],
  "gaia_positions": [
    [
      7.631437718112814,
      7.817740656132482
    ],
    [
      7.5118560822548694,
      7.949263068207227
    ],
    [
      9.774876495431474,
      6.324901063093867
    ]
  ],
  "events": [
    1798.1826688914998,
    1806.4327112653955,
    1814.6827536392911
  ],
  "calibration": {
    "sigma_pixels": [
      0.7,
      0.7
    ],
    "dx_pixels": 0.19999999999999973,
    "dy_pixels": -2.220446049250313e-16
  },
  "fixed_fits": [
    {
      "source_id": "358654375087124736",
      "sep_arcsec": 0.0,
      "G": 11.252031,
      "chi2": 4977.796648432669,
      "amplitude": 132.25250732931812,
      "fractional_residual": 0.19514422571392834
    },
    {
      "source_id": "358654370790026496",
      "sep_arcsec": 3.698370894837177,
      "G": 11.393224,
      "chi2": 4654.031306347369,
      "amplitude": 136.3621722883437,
      "fractional_residual": 0.1549730011118878
    },
    {
      "source_id": "358654198991334784",
      "sep_arcsec": 54.51572619155012,
      "G": 11.251107,
      "chi2": 27460.674845258647,
      "amplitude": 10.398709309465941,
      "fractional_residual": 0.9944001138394531
    }
  ],
  "free_best": {
    "chi2": 4490.013597146476,
    "pixel_x": 7.531437718112807,
    "pixel_y": 7.917740656132475,
    "distance_from_target_arcsec": 2.9698484809834893,
    "fractional_residual": 0.14454088761339412
  },
  "event_source_comparisons": [
    {
      "tc": 1798.1826688914998,
      "best_source": "358654370790026496",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        -353.23524398569907,
        12211.945006508538
      ]
    },
    {
      "tc": 1806.4327112653955,
      "best_source": "358654375087124736",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        74.44808459519982,
        10245.067528853406
      ]
    },
    {
      "tc": 1814.6827536392911,
      "best_source": "358654370790026496",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        -0.10263971268621075,
        28.083344247038973
      ]
    }
  ],
  "aperture_photometry": [
    {
      "tc": 1798.1826688914998,
      "fits": [
        {
          "degree": 1,
          "depth": 0.03429884005978926,
          "formal_error": 0.0002768379327809019
        },
        {
          "degree": 2,
          "depth": 0.034401864545287,
          "formal_error": 0.00030998891425196366
        }
      ],
      "n_core": 13
    },
    {
      "tc": 1806.4327112653955,
      "fits": [
        {
          "degree": 1,
          "depth": 0.03393540629793565,
          "formal_error": 0.0003227497087879623
        },
        {
          "degree": 2,
          "depth": 0.03431930440797193,
          "formal_error": 0.00034877739629569996
        }
      ],
      "n_core": 13
    },
    {
      "tc": 1814.6827536392911,
      "fits": [
        {
          "degree": 1,
          "depth": 0.03417577787449405,
          "formal_error": 0.00046076265862423493
        },
        {
          "degree": 2,
          "depth": 0.03463212220339091,
          "formal_error": 0.00042318223713580587
        }
      ],
      "n_core": 13
    }
  ],
  "calibration_note": "Approximate Gaussian PSFs at own Gaia cone positions; no extra empirical source.",
  "caution": "Same TESS pixels as QLP, independent aperture reduction. Approximate axis-aligned elliptical Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity."
}
```

## Archives and novelty

Successful current shared60arcsec VSX, Gaia vari_summary/vari_eclipsing_binary, SIMBAD exact Gaia-ID and ExoFOP TOI/CTOI responses were rechecked. Exact paths/hashes below and shared receipts preserve timestamps. No Gaia EB/vari_summary entries and no TOI/CTOI entries for these targets. SIMBAD lists known spectroscopic binaries, not prior eclipse classifications.

```json
{
  "simbad": [
    {
      "id": "Gaia DR3 358654375087124736",
      "main_id": "BD+49   589A",
      "otype": "SB*",
      "ra": "33.42547742392",
      "dec": "50.423916165079994"
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
      "path": "C:\\Home\\Astra\\made\\binary-handoff-2026-10-30\\shared-full-review\\vsx\\250742811.tsv",
      "sha256": "d8e07b8f2ee95adf57cfc3632e20bdf6b6367b77111db502ab6792b4988b58e5"
    },
    {
      "path": "C:\\Home\\Astra\\made\\binary-handoff-2026-10-30\\shared-full-review\\exofop\\250742811.json",
      "sha256": "f9ffa3988b02a9a268210ff1e080e88d719bb2bf9eee141e7079f50052145ed7"
    }
  ]
}
```

One bounded Harvard multi-catalogue mirror probe timed out after batchG reported all IDIA9 requests timing out. ASAS-SN, SB9, WDS, Prsa, IJspeert and Kostov tables therefore remain unchecked in this fresh pass; failed service is not a negative match. VSX raw table sections were inspected; no target EB rows found. General web searches on the ten exact SIMBAD names plus eclipsing/binary found only unrelated results, not exact-target prior publications. This does not establish novelty or a complete bibliography.

## Predictions and deciding next check

AtBTJD4344.32880: next primary~4347.44576; other conjunction~4351.57159. Photometric extrapolations are scheduling estimates, conditional on stationary orbit. For null secondary use Gaia phase uncertainty, not the single date.

Resolve the3.70arcsec pair through an eclipse using ground-based photometry, or fit empirical PRFs with externally calibrated WCS across multiple sectors; establish which member loses flux.

Final adjudication: **PLAUSIBLE**. The two-kind EB signal is secure, but target versus nearly equally bright3.70arcsec companion remains ambiguous. Circular PSF favors target; expanded calibration reverses preference and event rankings. RV agreement supports target but cannot resolve the contradictory localization.

Reproducibility: scripts and manifests retained in this batch. Original source audit completed before work; no source/paper edits or commits.

Lead control audit: {"median_primary_ppt": 64.99268676413543, "offphase_census_triggers": 2, "max_offphase_census_ppt": 9.971371674406647, "minimum_bg_regressed_depth_ratio": 0.9998030263893818}. Census trigger centers/durations can merge broad eclipse wings, especially253923749; they are not a calibrated blind-search catalog.
