# TIC 211231319: CONFIRMED

Repeated primary and secondary eclipses, independent SPOC recovery, own Gaia timing and on-target deficit establish a target EB; no bright capable neighbor.

Full review: COMPLETE (adjudicated). Novelty: LIMITED; successful checks found no target EB classification, but several catalogues were unavailable.

Raw untrimmed QUALITY=0 SAP: 11 accepted primary fits; median depth62.881ppt; T14=5.0599h. Primary and secondary individual timing/depth errors, duration/ingress/flat coordinates, O-C and rejected windows are tabulated below. Errors are conditional on shape/local baseline with grid and red-noise inflation. Trapezoid flat time is not measured totality.

```json
{
  "primary_shape": {
    "T14": 0.21082758620689654,
    "fr": 0.35,
    "shift": 0,
    "T14_range": [
      0.2072068965517241,
      0.21444827586206897
    ],
    "fr_range": [
      0.31,
      0.38999999999999996
    ],
    "n_local_windows": 11,
    "error_note": "profile likelihood plus half-grid resolution; conditional shape model"
  },
  "primary_ephemeris": {
    "P": 5.825582739160461,
    "P_error": 3.5484816951184273e-06,
    "Tref": 3649.4443969332056,
    "Tref_error": 0.00019070181835443363,
    "reference_cycle": 89,
    "T0": 3130.9675331479248,
    "chi2": 0.4367806882295022,
    "dof": 9,
    "n": 11,
    "oc_rms_minutes": 0.18148743172124418
  },
  "primary_events": [
    {
      "status": "fit",
      "sec": 67,
      "tc_nom": 3130.9701,
      "tc": 3130.9675700689654,
      "tc_error": 0.0006324827586206908,
      "depth": 0.06482123988718184,
      "depth_error": 0.0005164329721558844,
      "T14": 0.21082758620689654,
      "T12": 0.07378965517241379,
      "T23": 0.06324827586206896,
      "beta": 1.442707537461658,
      "n_in": 91,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -6.805611012674033e-05,
      "depth_with_background": 0.06488522070290835,
      "scan_edge": false,
      "x_template_shift_pix": -0.0008441200313412518,
      "x_err_pix": 0.0004829884503990536,
      "y_template_shift_pix": -0.0003100405447985497,
      "y_err_pix": 0.0004951700854626245,
      "cycle": 0,
      "oc_days": 3.692104064612067e-05
    },
    {
      "status": "insufficient",
      "tc_nom": 3136.7956513779945,
      "sec": 67,
      "n_in": 0,
      "cycle": 1
    },
    {
      "status": "fit",
      "sec": 67,
      "tc_nom": 3142.621202755989,
      "tc": 3142.6186728249545,
      "tc_error": 0.0006324827586206897,
      "depth": 0.06516093173830083,
      "depth_error": 0.0004971552976467926,
      "T14": 0.21082758620689654,
      "T12": 0.07378965517241379,
      "T23": 0.06324827586206896,
      "beta": 1.423667102216404,
      "n_in": 91,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -0.00031707812183127525,
      "depth_with_background": 0.06547381258853077,
      "scan_edge": false,
      "x_template_shift_pix": -0.0009238067184290841,
      "x_err_pix": 0.0004314460887403326,
      "y_template_shift_pix": -0.0012711935687489027,
      "y_err_pix": 0.00046279426790930573,
      "cycle": 2,
      "oc_days": -2.580129103080253e-05
    },
    {
      "status": "fit",
      "sec": 67,
      "tc_nom": 3148.446754133983,
      "tc": 3148.4442242029486,
      "tc_error": 0.0006324827586206897,
      "depth": 0.0648262459297684,
      "depth_error": 0.0005259205172534642,
      "T14": 0.21082758620689654,
      "T12": 0.07378965517241379,
      "T23": 0.06324827586206896,
      "beta": 1.4602192696109995,
      "n_in": 91,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -0.0002393400611654192,
      "depth_with_background": 0.06506408357992312,
      "scan_edge": false,
      "x_template_shift_pix": 0.003995803857184631,
      "x_err_pix": 0.0007523650452571926,
      "y_template_shift_pix": -0.0026228306034628344,
      "y_err_pix": 0.000664951091835192,
      "cycle": 3,
      "oc_days": -5.7162457324011484e-05
    },
    {
      "status": "insufficient",
      "tc_nom": 3154.2723055119777,
      "sec": 67,
      "n_in": 0,
      "cycle": 4
    },
    {
      "status": "fit",
      "sec": 92,
      "tc_nom": 3806.7340598473565,
      "tc": 3806.735324812874,
      "tc_error": 0.0006324827586206897,
      "depth": 0.06271768341280667,
      "depth_error": 0.0004972809062130513,
      "T14": 0.21082758620689654,
      "T12": 0.07378965517241379,
      "T23": 0.06324827586206896,
      "beta": 1.4687138837030451,
      "n_in": 91,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -4.97328442230456e-05,
      "depth_with_background": 0.06276857351994151,
      "scan_edge": false,
      "x_template_shift_pix": -0.006200186056014031,
      "x_err_pix": 0.0005663988118111941,
      "y_template_shift_pix": -0.004414123230788973,
      "y_err_pix": 0.0004832576675746935,
      "cycle": 116,
      "oc_days": 0.00019392233571124962
    },
    {
      "status": "fit",
      "sec": 92,
      "tc_nom": 3812.5596112253506,
      "tc": 3812.560876190868,
      "tc_error": 0.0006324827586206897,
      "depth": 0.06339753843558767,
      "depth_error": 0.0004457549448178604,
      "T14": 0.21082758620689654,
      "T12": 0.07378965517241379,
      "T23": 0.06324827586206896,
      "beta": 1.3146755501419933,
      "n_in": 91,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": 1.890133164571791e-05,
      "depth_with_background": 0.06337966197705433,
      "scan_edge": false,
      "x_template_shift_pix": -0.006269946573349865,
      "x_err_pix": 0.0005298047905906974,
      "y_template_shift_pix": -0.00450170166513181,
      "y_err_pix": 0.0004935217856716613,
      "cycle": 117,
      "oc_days": 0.00016256116941804066
    },
    {
      "status": "fit",
      "sec": 92,
      "tc_nom": 3818.385162603345,
      "tc": 3818.3864275688625,
      "tc_error": 0.0006324827586206897,
      "depth": 0.06325390179169249,
      "depth_error": 0.00048645452273598285,
      "T14": 0.21082758620689654,
      "T12": 0.07378965517241379,
      "T23": 0.06324827586206896,
      "beta": 1.4309067537176017,
      "n_in": 91,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -0.00020375305751518493,
      "depth_with_background": 0.0634699018138775,
      "scan_edge": false,
      "x_template_shift_pix": -0.005824569969391162,
      "x_err_pix": 0.0004872279782871828,
      "y_template_shift_pix": -0.004028131472717987,
      "y_err_pix": 0.00042425556261571845,
      "cycle": 118,
      "oc_days": 0.00013120000357957906
    },
    {
      "status": "fit",
      "sec": 92,
      "tc_nom": 3824.2107139813397,
      "tc": 3824.211978946857,
      "tc_error": 0.0006324827586206897,
      "depth": 0.06288077035150803,
      "depth_error": 0.00043245144533664645,
      "T14": 0.21082758620689654,
      "T12": 0.07378965517241379,
      "T23": 0.06324827586206896,
      "beta": 1.3682653051114009,
      "n_in": 91,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -5.003240901759617e-06,
      "depth_with_background": 0.06288612642042292,
      "scan_edge": false,
      "x_template_shift_pix": -0.004990658566244356,
      "x_err_pix": 0.0005503566968475886,
      "y_template_shift_pix": -0.004997572874765426,
      "y_err_pix": 0.0004437038818123109,
      "cycle": 119,
      "oc_days": 9.983883774111746e-05
    },
    {
      "status": "fit",
      "sec": 94,
      "tc_nom": 3859.1640222493065,
      "tc": 3859.165287214824,
      "tc_error": 0.0006324827586206897,
      "depth": 0.05491487264758656,
      "depth_error": 0.00036038329892423534,
      "T14": 0.21082758620689654,
      "T12": 0.07378965517241379,
      "T23": 0.06324827586206896,
      "beta": 1.5626153406753827,
      "n_in": 91,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": 7.201736294427339e-06,
      "depth_with_background": 0.0549039331707617,
      "scan_edge": false,
      "x_template_shift_pix": -0.0004689844312310604,
      "x_err_pix": 0.00033322376074580625,
      "y_template_shift_pix": -0.00015776297655557204,
      "y_err_pix": 0.00028888218746859324,
      "cycle": 125,
      "oc_days": -8.832815819914686e-05
    },
    {
      "status": "fit",
      "sec": 94,
      "tc_nom": 3864.989573627301,
      "tc": 3864.9908385928184,
      "tc_error": 0.0006324827586206897,
      "depth": 0.05344718577918166,
      "depth_error": 0.0003440883156836905,
      "T14": 0.21082758620689654,
      "T12": 0.07378965517241379,
      "T23": 0.06324827586206896,
      "beta": 1.509499293519585,
      "n_in": 91,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -8.257365095074265e-06,
      "depth_with_background": 0.05343872790698427,
      "scan_edge": false,
      "x_template_shift_pix": -0.00030534606711996926,
      "x_err_pix": 0.00034174590997268955,
      "y_template_shift_pix": -0.00018138676127433363,
      "y_err_pix": 0.00026970670267426636,
      "cycle": 126,
      "oc_days": -0.00011968932403760846
    },
    {
      "status": "fit",
      "sec": 94,
      "tc_nom": 3870.815125005295,
      "tc": 3870.8163899708125,
      "tc_error": 0.0006324827586206897,
      "depth": 0.0523257888455752,
      "depth_error": 0.0003508841210944688,
      "T14": 0.21082758620689654,
      "T12": 0.07378965517241379,
      "T23": 0.06324827586206896,
      "beta": 1.6024031390939972,
      "n_in": 91,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -2.1791117862979998e-05,
      "depth_with_background": 0.05233410560542191,
      "scan_edge": false,
      "x_template_shift_pix": -0.0007604634860688921,
      "x_err_pix": 0.0003439539784556411,
      "y_template_shift_pix": 0.0021569744262091885,
      "y_err_pix": 0.00045675046231169675,
      "cycle": 127,
      "oc_days": -0.00015105049078556476
    },
    {
      "status": "fit",
      "sec": 94,
      "tc_nom": 3876.6406763832897,
      "tc": 3876.641941348807,
      "tc_error": 0.0006324827586206897,
      "depth": 0.05360793429883999,
      "depth_error": 0.0004206444732768277,
      "T14": 0.21082758620689654,
      "T12": 0.07378965517241379,
      "T23": 0.06324827586206896,
      "beta": 1.8501575983998768,
      "n_in": 91,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -6.370476652670328e-06,
      "depth_with_background": 0.05361338628601294,
      "scan_edge": false,
      "x_template_shift_pix": -0.0008716629375184221,
      "x_err_pix": 0.0003917509257402428,
      "y_template_shift_pix": -0.0002646118637564502,
      "y_err_pix": 0.0004357515522491628,
      "cycle": 128,
      "oc_days": -0.00018241165662402636
    }
  ],
  "secondary": {
    "predicted_gaia_phase": 0.526930647023727,
    "profile_phase": 0.5001500791769494,
    "statistic": {
      "n": 9,
      "depth": 0.026364749862133347,
      "error": 0.00010561304551987905,
      "snr": 249.6353526437303,
      "scatter": 0.0019387810824852358,
      "chi2": 349.2995214963789,
      "dof": 8,
      "empirical_error": 0.0006462603608284119,
      "n_individual_gt3sigma": 9
    },
    "events": [
      {
        "status": "fit",
        "sec": 67,
        "tc_nom": 3128.055616077007,
        "tc": 3128.055616077007,
        "tc_error": 0.0006324827586206897,
        "depth": 0.02773221546063867,
        "depth_error": 0.00036547767248020944,
        "T14": 0.21082758620689654,
        "T12": 0.07378965517241379,
        "T23": 0.06324827586206896,
        "beta": 1.1145797904499133,
        "n_in": 91,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": -8.26149881730296e-05,
        "depth_with_background": 0.027813733574769534,
        "scan_edge": false,
        "x_template_shift_pix": -0.0009002828341990531,
        "x_err_pix": 0.00028731709356676007,
        "y_template_shift_pix": 0.00018170943908707852,
        "y_err_pix": 0.0002793077640204064,
        "cycle": -1,
        "oc_days": 0.00039669169063927257
      },
      {
        "status": "fit",
        "sec": 67,
        "tc_nom": 3133.881198816168,
        "tc": 3133.8799338506506,
        "tc_error": 0.0006324827586206897,
        "depth": 0.028059793408125533,
        "depth_error": 0.0003684040484998446,
        "T14": 0.21082758620689654,
        "T12": 0.07378965517241379,
        "T23": 0.06324827586206896,
        "beta": 1.1389013881845396,
        "n_in": 91,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": -3.5461672251892084e-05,
        "depth_with_background": 0.028091108589611034,
        "scan_edge": false,
        "x_template_shift_pix": 0.00440210616022739,
        "x_err_pix": 0.0005547259578045657,
        "y_template_shift_pix": -0.0015895069223155409,
        "y_err_pix": 0.000551777985122607,
        "cycle": 0,
        "oc_days": -0.000866266229422763
      },
      {
        "status": "insufficient",
        "tc_nom": 3139.7067815553282,
        "sec": 67,
        "n_in": 0,
        "cycle": 1
      },
      {
        "status": "fit",
        "sec": 67,
        "tc_nom": 3145.5323642944886,
        "tc": 3145.5323642944886,
        "tc_error": 0.0006324827586206908,
        "depth": 0.02827930890485498,
        "depth_error": 0.00033520889704433815,
        "T14": 0.21082758620689654,
        "T12": 0.07378965517241379,
        "T23": 0.06324827586206896,
        "beta": 1.0,
        "n_in": 91,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": 8.949891691078958e-06,
        "depth_with_background": 0.028270334492171003,
        "scan_edge": false,
        "x_template_shift_pix": -0.0005300416917783139,
        "x_err_pix": 0.0005486886760793642,
        "y_template_shift_pix": -0.00041956044991342127,
        "y_err_pix": 0.0006538089211628589,
        "cycle": 2,
        "oc_days": 0.0004027144814244821
      },
      {
        "status": "insufficient",
        "tc_nom": 3151.357947033649,
        "sec": 67,
        "n_in": 0,
        "cycle": 3
      },
      {
        "status": "fit",
        "sec": 92,
        "tc_nom": 3803.823213819621,
        "tc": 3803.823213819621,
        "tc_error": 0.0006324827586206897,
        "depth": 0.028586245581225,
        "depth_error": 0.00035435747916254284,
        "T14": 0.21082758620689654,
        "T12": 0.07378965517241379,
        "T23": 0.06324827586206896,
        "beta": 1.0391547989882177,
        "n_in": 91,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": 8.46635538389916e-06,
        "depth_with_background": 0.028573912813707556,
        "scan_edge": false,
        "x_template_shift_pix": 0.012209798391835048,
        "x_err_pix": 0.001573314225898176,
        "y_template_shift_pix": 0.002544127078942248,
        "y_err_pix": 0.000642284493329488,
        "cycle": 115,
        "oc_days": 0.0006295729249359283
      },
      {
        "status": "insufficient",
        "tc_nom": 3809.648796558781,
        "sec": 92,
        "n_in": 9,
        "cycle": 116
      },
      {
        "status": "insufficient",
        "tc_nom": 3815.4743792979416,
        "sec": 92,
        "n_in": 0,
        "cycle": 117
      },
      {
        "status": "fit",
        "sec": 92,
        "tc_nom": 3821.299962037102,
        "tc": 3821.2986970715847,
        "tc_error": 0.0006324827586206897,
        "depth": 0.028017227469651705,
        "depth_error": 0.000361672833850778,
        "T14": 0.21082758620689654,
        "T12": 0.07378965517241379,
        "T23": 0.06324827586206896,
        "beta": 1.1597239517104962,
        "n_in": 91,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": 2.386686478530344e-05,
        "depth_with_background": 0.027993058192278035,
        "scan_edge": false,
        "x_template_shift_pix": -0.003471366745931944,
        "x_err_pix": 0.0004536792927961767,
        "y_template_shift_pix": -0.0012443181958440856,
        "y_err_pix": 0.00043446307082754967,
        "cycle": 118,
        "oc_days": -0.0006293698020272132
      },
      {
        "status": "fit",
        "sec": 92,
        "tc_nom": 3827.1255447762624,
        "tc": 3827.1255447762624,
        "tc_error": 0.0006324827586206897,
        "depth": 0.027834113504504772,
        "depth_error": 0.00030726192708575834,
        "T14": 0.21082758620689654,
        "T12": 0.07378965517241379,
        "T23": 0.06324827586206896,
        "beta": 1.0430190098600822,
        "n_in": 91,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": -0.00022592963726291755,
        "depth_with_background": 0.02806163574390672,
        "scan_edge": false,
        "x_template_shift_pix": -0.0030870503434741988,
        "x_err_pix": 0.00044468181125585784,
        "y_template_shift_pix": -0.0017943566581221735,
        "y_err_pix": 0.0003641344771450769,
        "cycle": 119,
        "oc_days": 0.0006376033120432112
      },
      {
        "status": "insufficient",
        "tc_nom": 3856.2534584720647,
        "sec": 94,
        "n_in": 0,
        "cycle": 124
      },
      {
        "status": "fit",
        "sec": 94,
        "tc_nom": 3862.0790412112256,
        "tc": 3862.0790412112256,
        "tc_error": 0.0006324827586206908,
        "depth": 0.023716177765615062,
        "depth_error": 0.00029173021035846163,
        "T14": 0.21082758620689654,
        "T12": 0.07378965517241379,
        "T23": 0.06324827586206896,
        "beta": 1.3259933860236082,
        "n_in": 86,
        "flagged_core": 5,
        "flag_bits_core": 1073741824,
        "background_fake_depth": 3.3082478998874497e-06,
        "depth_with_background": 0.023715965159519233,
        "scan_edge": false,
        "x_template_shift_pix": 0.00039962348281299574,
        "x_err_pix": 0.00032248872649143613,
        "y_template_shift_pix": 0.0008643814646924422,
        "y_err_pix": 0.00030627920766092287,
        "cycle": 125,
        "oc_days": 0.0006496488936136302
      },
      {
        "status": "insufficient",
        "tc_nom": 3867.904623950386,
        "sec": 94,
        "n_in": 0,
        "cycle": 126
      },
      {
        "status": "fit",
        "sec": 94,
        "tc_nom": 3873.7302066895463,
        "tc": 3873.728941724029,
        "tc_error": 0.0006324827586206897,
        "depth": 0.023615282531087543,
        "depth_error": 0.00031926180980187003,
        "T14": 0.21082758620689654,
        "T12": 0.07378965517241379,
        "T23": 0.06324827586206896,
        "beta": 1.3657796373429425,
        "n_in": 83,
        "flagged_core": 8,
        "flag_bits_core": 1073741824,
        "background_fake_depth": 8.254383703925496e-06,
        "depth_with_background": 0.02360238747575892,
        "scan_edge": false,
        "x_template_shift_pix": 3.926727877637243e-05,
        "x_err_pix": 0.0004954481818956764,
        "y_template_shift_pix": 0.00022550294166483214,
        "y_err_pix": 0.0004810703867830458,
        "cycle": 127,
        "oc_days": -0.000611301430126332
      },
      {
        "status": "fit",
        "sec": 94,
        "tc_nom": 3879.5557894287067,
        "tc": 3879.5545244631894,
        "tc_error": 0.0006324827586206897,
        "depth": 0.024845342549666104,
        "depth_error": 0.00023480764074926012,
        "T14": 0.21082758620689654,
        "T12": 0.07378965517241379,
        "T23": 0.06324827586206896,
        "beta": 1.2016079613124588,
        "n_in": 91,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": -6.415304987300776e-05,
        "depth_with_background": 0.02486067278567144,
        "scan_edge": false,
        "x_template_shift_pix": -0.0004580689321393249,
        "x_err_pix": 0.0003611096578078211,
        "y_template_shift_pix": 9.599726122085043e-05,
        "y_err_pix": 0.000373890595202461,
        "cycle": 128,
        "oc_days": -0.0006092938333495113
      }
    ],
    "ephemeris": {
      "P": 5.825580731563617,
      "P_error": 4.061621009459631e-06,
      "Tref": 3605.752839373533,
      "Tref_error": 0.00023354222697399146,
      "reference_cycle": 81,
      "T0": 3133.88080011688,
      "chi2": 8.589107801489197,
      "dof": 7,
      "n": 9,
      "oc_rms_minutes": 0.8897417205320814
    },
    "shape": {
      "T14": 0.21082758620689654,
      "fr": 0.35,
      "shift": 0,
      "T14_range": [
        0.2072068965517241,
        0.21444827586206897
      ],
      "fr_range": [
        0.31,
        0.38999999999999996
      ],
      "n_local_windows": 11,
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
      "sec": 67,
      "tc": 3128.05621179432,
      "depth": 0.03386598899597826,
      "n": 76,
      "phase": 0.5002523380134294,
      "threshold": 0.007719422184183442,
      "duration": 0.17824519265968775
    },
    {
      "sec": 67,
      "tc": 3130.9684151656365,
      "depth": 0.07202335453071063,
      "n": 85,
      "phase": 0.00015140420302419506,
      "threshold": 0.007719422184183442,
      "duration": 0.19676269153433168
    },
    {
      "sec": 67,
      "tc": 3133.8807439438865,
      "depth": 0.03294482436681623,
      "n": 69,
      "phase": 0.5000719973263245,
      "threshold": 0.007719422184183442,
      "duration": 0.1643540431459769
    },
    {
      "sec": 67,
      "tc": 3142.619466080835,
      "depth": 0.0718219894807327,
      "n": 83,
      "phase": 0.00013173868156268753,
      "threshold": 0.007719422184183442,
      "duration": 0.19907430050034236
    },
    {
      "sec": 67,
      "tc": 3145.5318851463253,
      "depth": 0.0326413461343007,
      "n": 73,
      "phase": 0.5000678302097947,
      "threshold": 0.007719422184183442,
      "duration": 0.17361010629247176
    },
    {
      "sec": 67,
      "tc": 3148.444422869999,
      "depth": 0.070331840422311,
      "n": 84,
      "phase": 2.4290203950450007e-05,
      "threshold": 0.007719422184183442,
      "duration": 0.1944425094784492
    },
    {
      "sec": 92,
      "tc": 3803.8235602759546,
      "depth": 0.03353932134833759,
      "n": 72,
      "phase": 0.5002095507095703,
      "threshold": 0.007246403057883452,
      "duration": 0.17362751477958227
    },
    {
      "sec": 92,
      "tc": 3806.7353734093567,
      "depth": 0.06986616938953394,
      "n": 84,
      "phase": 4.16299672281184e-05,
      "threshold": 0.007246403057883452,
      "duration": 0.19446182133469847
    },
    {
      "sec": 92,
      "tc": 3809.7324846523957,
      "depth": 0.01168017856957626,
      "n": 3,
      "phase": 0.5145156967231372,
      "threshold": 0.007246403057883452,
      "duration": 0.016205057895604114
    },
    {
      "sec": 92,
      "tc": 3812.560533716772,
      "depth": 0.07141495429591238,
      "n": 85,
      "phase": 0.9999691167502789,
      "threshold": 0.007246403057883452,
      "duration": 0.199089987858315
    },
    {
      "sec": 92,
      "tc": 3818.3864733725422,
      "depth": 0.07060327440348146,
      "n": 87,
      "phase": 3.0383858756977133e-05,
      "threshold": 0.007246403057883452,
      "duration": 0.20372046405145738
    },
    {
      "sec": 92,
      "tc": 3821.298026495025,
      "depth": 0.03486083469259116,
      "n": 74,
      "phase": 0.4998178305138339,
      "threshold": 0.007246403057883452,
      "duration": 0.17825426016861456
    },
    {
      "sec": 92,
      "tc": 3824.2119480347974,
      "depth": 0.06923809511319345,
      "n": 86,
      "phase": 1.1831739570311584e-05,
      "threshold": 0.007246403057883452,
      "duration": 0.19908804331180363
    },
    {
      "sec": 92,
      "tc": 3827.1269372275297,
      "depth": 0.034233744017765355,
      "n": 75,
      "phase": 0.5003891026926084,
      "threshold": 0.007246403057883452,
      "duration": 0.18288229514018894
    },
    {
      "sec": 94,
      "tc": 3856.7226848556306,
      "depth": 0.008896080455776945,
      "n": 31,
      "phase": 0.5806959068778497,
      "threshold": 0.004738138848206751,
      "duration": 0.2638973812856875
    },
    {
      "sec": 94,
      "tc": 3856.9053051337864,
      "depth": 0.005276206466860112,
      "n": 2,
      "phase": 0.6120438915057633,
      "threshold": 0.004738138848206751,
      "duration": 0.006944614264966731
    },
    {
      "sec": 94,
      "tc": 3859.1655515101093,
      "depth": 0.05945670865567265,
      "n": 87,
      "phase": 3.0205926989879117e-05,
      "threshold": 0.004738138848206751,
      "duration": 0.20139424078820412
    },
    {
      "sec": 94,
      "tc": 3862.078218127225,
      "depth": 0.02713086294951872,
      "n": 76,
      "phase": 0.5000087913372653,
      "threshold": 0.004738138848206751,
      "duration": 0.18518867651278015
    },
    {
      "sec": 94,
      "tc": 3864.9905560523875,
      "depth": 0.057395746330969,
      "n": 87,
      "phase": 0.9999309545888764,
      "threshold": 0.004738138848206751,
      "duration": 0.20602097752248483
    },
    {
      "sec": 94,
      "tc": 3870.816697445084,
      "depth": 0.0577074810252719,
      "n": 88,
      "phase": 2.6851181743836605e-05,
      "threshold": 0.004738138848206751,
      "duration": 0.20370573661261915
    },
    {
      "sec": 94,
      "tc": 3873.7321565158454,
      "depth": 0.02811811213707327,
      "n": 71,
      "phase": 0.5004847798217611,
      "threshold": 0.004738138848206751,
      "duration": 0.18055586021614545
    },
    {
      "sec": 94,
      "tc": 3874.7624990318923,
      "depth": 0.0058170825372239054,
      "n": 3,
      "phase": 0.677349921418795,
      "threshold": 0.004738138848206751,
      "duration": 0.02546295719162117
    },
    {
      "sec": 94,
      "tc": 3875.5295938809677,
      "depth": 0.00879955286466616,
      "n": 15,
      "phase": 0.8090268511650436,
      "threshold": 0.004738138848206751,
      "duration": 0.18518465290094355
    },
    {
      "sec": 94,
      "tc": 3875.7357579369996,
      "depth": 0.007641698156733878,
      "n": 9,
      "phase": 0.8444162817615819,
      "threshold": 0.004738138848206751,
      "duration": 0.07870345467858897
    },
    {
      "sec": 94,
      "tc": 3876.6421728815576,
      "depth": 0.05905297203153237,
      "n": 85,
      "phase": 8.431962271515658e-06,
      "threshold": 0.004738138848206751,
      "duration": 0.19675816062613194
    },
    {
      "sec": 94,
      "tc": 3879.5549699182975,
      "depth": 0.028339035865031836,
      "n": 81,
      "phase": 0.5000094047678942,
      "threshold": 0.004738138848206751,
      "duration": 0.18749768728343952
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
    "w_tp_corr": 0.9994037,
    "gaia_comparison": [
      {
        "kind": "A",
        "epoch389_offset": 0.03748307162840092,
        "epoch389_gaia_error": 0.0509664794426134,
        "events": [
          {
            "sec": 67,
            "tc": 3130.9675700689654,
            "gaia_conjunction": 3131.047589008408,
            "gaia_error": 0.2226275564666908,
            "offset_days": -0.08001893944265248,
            "z": -0.3594281758695091
          },
          {
            "sec": 67,
            "tc": 3142.6186728249545,
            "gaia_conjunction": 3142.6991814646717,
            "gaia_error": 0.22361449646441292,
            "offset_days": -0.08050863971720901,
            "z": -0.3600317463847591
          },
          {
            "sec": 67,
            "tc": 3148.4442242029486,
            "gaia_conjunction": 3148.525005207576,
            "gaia_error": 0.2241080416204541,
            "offset_days": -0.0807810046276245,
            "z": -0.3604541913691478
          },
          {
            "sec": 92,
            "tc": 3806.735324812874,
            "gaia_conjunction": 3806.8423472148506,
            "gaia_error": 0.2801352358959794,
            "offset_days": -0.10702240197679203,
            "z": -0.3820373715546941
          },
          {
            "sec": 92,
            "tc": 3812.560876190868,
            "gaia_conjunction": 3812.668202977485,
            "gaia_error": 0.28063286113329106,
            "offset_days": -0.10732678661725004,
            "z": -0.3824445704685359
          },
          {
            "sec": 92,
            "tc": 3818.3864275688625,
            "gaia_conjunction": 3818.494064503536,
            "gaia_error": 0.28113051166365166,
            "offset_days": -0.10763693467333724,
            "z": -0.38287079418690956
          },
          {
            "sec": 92,
            "tc": 3824.211978946857,
            "gaia_conjunction": 3824.3198880130876,
            "gaia_error": 0.2816281873529762,
            "offset_days": -0.10790906623060437,
            "z": -0.3831604894309825
          },
          {
            "sec": 94,
            "tc": 3859.165287214824,
            "gaia_conjunction": 3859.2749258635386,
            "gaia_error": 0.28461476243593714,
            "offset_days": -0.10963864871473561,
            "z": -0.38521676479443945
          },
          {
            "sec": 94,
            "tc": 3864.9908385928184,
            "gaia_conjunction": 3865.100796315482,
            "gaia_error": 0.2851126105616077,
            "offset_days": -0.10995772266369386,
            "z": -0.3856632363267602
          },
          {
            "sec": 94,
            "tc": 3870.8163899708125,
            "gaia_conjunction": 3870.9266814455914,
            "gaia_error": 0.2856104828067332,
            "offset_days": -0.11029147477893275,
            "z": -0.38615951089131967
          },
          {
            "sec": 94,
            "tc": 3876.641941348807,
            "gaia_conjunction": 3876.752503514046,
            "gaia_error": 0.28610837904538944,
            "offset_days": -0.11056216523911644,
            "z": -0.3864336146118839
          }
        ]
      },
      {
        "kind": "B",
        "epoch389_offset": 2.8124656821789245,
        "epoch389_gaia_error": 0.04623364715209959,
        "events": [
          {
            "sec": 67,
            "tc": 3130.9675700689654,
            "gaia_conjunction": 3128.265340549453,
            "gaia_error": 0.2617381271245756,
            "offset_days": 2.702229519512457,
            "z": 10.324142147807843
          },
          {
            "sec": 67,
            "tc": 3142.6186728249545,
            "gaia_conjunction": 3139.9169937636984,
            "gaia_error": 0.26273495311759487,
            "offset_days": 2.7016790612560726,
            "z": 10.282877100928998
          },
          {
            "sec": 67,
            "tc": 3148.4442242029486,
            "gaia_conjunction": 3145.7428297942615,
            "gaia_error": 0.26323340216201774,
            "offset_days": 2.701394408687065,
            "z": 10.262324570932877
          },
          {
            "sec": 92,
            "tc": 3806.735324812874,
            "gaia_conjunction": 3804.060529043781,
            "gaia_error": 0.3196849014977061,
            "offset_days": 2.674795769092725,
            "z": 8.366959220194865
          },
          {
            "sec": 92,
            "tc": 3812.560876190868,
            "gaia_conjunction": 3809.886306208598,
            "gaia_error": 0.32018539276038216,
            "offset_days": 2.674569982269986,
            "z": 8.353175455807367
          },
          {
            "sec": 92,
            "tc": 3818.3864275688625,
            "gaia_conjunction": 3815.7120904760386,
            "gaia_error": 0.3206858972759662,
            "offset_days": 2.674337092823862,
            "z": 8.339412222717803
          },
          {
            "sec": 92,
            "tc": 3824.211978946857,
            "gaia_conjunction": 3821.5379401940545,
            "gaia_error": 0.321186414982499,
            "offset_days": 2.6740387528025167,
            "z": 8.325487764785235
          },
          {
            "sec": 94,
            "tc": 3859.165287214824,
            "gaia_conjunction": 3856.492748450665,
            "gaia_error": 0.3241897948101118,
            "offset_days": 2.6725387641586167,
            "z": 8.243731668194151
          },
          {
            "sec": 94,
            "tc": 3864.9908385928184,
            "gaia_conjunction": 3862.318613116935,
            "gaia_error": 0.3246904031504063,
            "offset_days": 2.6722254758833515,
            "z": 8.230056632546594
          },
          {
            "sec": 94,
            "tc": 3870.8163899708125,
            "gaia_conjunction": 3868.144446905269,
            "gaia_error": 0.3251910241995831,
            "offset_days": 2.6719430655434735,
            "z": 8.216518332081941
          },
          {
            "sec": 94,
            "tc": 3876.641941348807,
            "gaia_conjunction": 3873.9702257474737,
            "gaia_error": 0.3256916578990366,
            "offset_days": 2.6717156013332897,
            "z": 8.203190037910252
          }
        ]
      }
    ],
    "primary_conjunction": "A",
    "predicted_secondary_phase": 0.526930647023727,
    "secondary": {
      "n": 10,
      "depth": -0.0009004036767013284,
      "error": 0.0005665987851005401,
      "snr": -1.5891380291991912,
      "scatter": 0.0030639781802322156,
      "chi2": 32.80262775238627,
      "dof": 9,
      "phase": 0.526930647023727,
      "control_scatter": 0.004695514773510155,
      "upper_3sigma": 0.014086544320530464
    },
    "secondary_windows": {
      "gaia_other_windows": [
        {
          "status": "fit",
          "sec": 67,
          "tc_nom": 3128.2116284908,
          "tc": 3128.2116284908,
          "tc_error": 0.0006324827586206897,
          "depth": -0.008226707908960662,
          "depth_error": 0.0047043376097262776,
          "T14": 0.21082758620689654,
          "T12": 0.07378965517241379,
          "T23": 0.06324827586206896,
          "beta": 3.9038192978987696,
          "n_in": 91,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": 4.7604835625031735e-05,
          "depth_with_background": -0.008265109328306227,
          "scan_edge": false,
          "x_template_shift_pix": -0.00024656685346596965,
          "x_err_pix": 0.000993688701279469,
          "y_template_shift_pix": -0.000925658743106763,
          "y_err_pix": 0.0009622193140286295,
          "cycle": -1
        },
        {
          "status": "fit",
          "sec": 67,
          "tc_nom": 3134.037211229961,
          "tc": 3134.037211229961,
          "tc_error": 0.0006324827586206897,
          "depth": -0.008793437906526596,
          "depth_error": 0.004748733747187592,
          "T14": 0.21082758620689654,
          "T12": 0.07378965517241379,
          "T23": 0.06324827586206896,
          "beta": 3.910049611768342,
          "n_in": 91,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": -0.00016318870069086366,
          "depth_with_background": -0.008640980353647626,
          "scan_edge": false,
          "x_template_shift_pix": 0.003233418352406504,
          "x_err_pix": 0.0018536300064680967,
          "y_template_shift_pix": -0.0009753834894857105,
          "y_err_pix": 0.0013870921506594393,
          "cycle": 0
        },
        {
          "status": "insufficient",
          "tc_nom": 3139.8627939691214,
          "sec": 67,
          "n_in": 0,
          "cycle": 1
        },
        {
          "status": "fit",
          "sec": 67,
          "tc_nom": 3145.688376708282,
          "tc": 3145.688376708282,
          "tc_error": 0.0006324827586206897,
          "depth": -0.009213732761525838,
          "depth_error": 0.004854209536081643,
          "T14": 0.21082758620689654,
          "T12": 0.07378965517241379,
          "T23": 0.06324827586206896,
          "beta": 3.9101654219562554,
          "n_in": 92,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": -7.408259174587172e-05,
          "depth_with_background": -0.009079898226273359,
          "scan_edge": false,
          "x_template_shift_pix": 0.00021814325390904704,
          "x_err_pix": 0.0022695268429152866,
          "y_template_shift_pix": -0.000464191723594046,
          "y_err_pix": 0.0027374187665828846,
          "cycle": 2
        },
        {
          "status": "insufficient",
          "tc_nom": 3151.513959447442,
          "sec": 67,
          "n_in": 0,
          "cycle": 3
        },
        {
          "status": "fit",
          "sec": 92,
          "tc_nom": 3803.979226233414,
          "tc": 3803.979226233414,
          "tc_error": 0.0006324827586206897,
          "depth": -0.008872201921360437,
          "depth_error": 0.004831519880732618,
          "T14": 0.21082758620689654,
          "T12": 0.07378965517241379,
          "T23": 0.06324827586206896,
          "beta": 3.9058902562802817,
          "n_in": 91,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": -3.1376330271506425e-05,
          "depth_with_background": -0.008843740907855098,
          "scan_edge": false,
          "x_template_shift_pix": 0.015047174327652822,
          "x_err_pix": 0.005422645862871843,
          "y_template_shift_pix": 0.006936929296571709,
          "y_err_pix": 0.0023476415440826554,
          "cycle": 115
        },
        {
          "status": "fit",
          "sec": 92,
          "tc_nom": 3809.8048089725744,
          "tc": 3809.8048089725744,
          "tc_error": 0.0006324827586206897,
          "depth": 0.0003431618247630786,
          "depth_error": 0.0006074842864495893,
          "T14": 0.21082758620689654,
          "T12": 0.07378965517241379,
          "T23": 0.06324827586206896,
          "beta": 1.671325999092107,
          "n_in": 76,
          "flagged_core": 7,
          "flag_bits_core": 1073741856,
          "background_fake_depth": -9.998039668813366e-05,
          "depth_with_background": 0.0004365556813787896,
          "scan_edge": false,
          "x_template_shift_pix": -0.0016844077419348,
          "x_err_pix": 0.000757325478724927,
          "y_template_shift_pix": 0.012807170079408028,
          "y_err_pix": 0.001261931859537495,
          "cycle": 116
        },
        {
          "status": "insufficient",
          "tc_nom": 3815.630391711735,
          "sec": 92,
          "n_in": 0,
          "cycle": 117
        },
        {
          "status": "fit",
          "sec": 92,
          "tc_nom": 3821.455974450895,
          "tc": 3821.455974450895,
          "tc_error": 0.0006324827586206897,
          "depth": -0.008715210252292467,
          "depth_error": 0.004743198697887217,
          "T14": 0.21082758620689654,
          "T12": 0.07378965517241379,
          "T23": 0.06324827586206896,
          "beta": 3.925729056838218,
          "n_in": 91,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": -4.006287979871982e-05,
          "depth_with_background": -0.008677212304889069,
          "scan_edge": false,
          "x_template_shift_pix": 0.00029654676128869145,
          "x_err_pix": 0.001661834123736206,
          "y_template_shift_pix": 0.00029019042626021507,
          "y_err_pix": 0.0015442300476526565,
          "cycle": 118
        },
        {
          "status": "fit",
          "sec": 92,
          "tc_nom": 3827.2815571900555,
          "tc": 3827.2815571900555,
          "tc_error": 0.0006324827586206897,
          "depth": -0.008075062374512113,
          "depth_error": 0.004791932661070105,
          "T14": 0.21082758620689654,
          "T12": 0.07378965517241379,
          "T23": 0.06324827586206896,
          "beta": 3.9377706442618057,
          "n_in": 91,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": 0.00013984655019337594,
          "depth_with_background": -0.008200779588357583,
          "scan_edge": false,
          "x_template_shift_pix": 0.00035798248855214233,
          "x_err_pix": 0.0017850642647744734,
          "y_template_shift_pix": 0.00032661361715902295,
          "y_err_pix": 0.0014583259140653266,
          "cycle": 119
        },
        {
          "status": "insufficient",
          "tc_nom": 3856.409470885858,
          "sec": 94,
          "n_in": 21,
          "cycle": 124
        },
        {
          "status": "fit",
          "sec": 94,
          "tc_nom": 3862.2350536250187,
          "tc": 3862.2350536250187,
          "tc_error": 0.0006324827586206897,
          "depth": -0.01190107775867706,
          "depth_error": 0.004391718087477133,
          "T14": 0.21082758620689654,
          "T12": 0.07378965517241379,
          "T23": 0.06324827586206896,
          "beta": 3.950077221983461,
          "n_in": 78,
          "flagged_core": 7,
          "flag_bits_core": 1073741824,
          "background_fake_depth": 0.000624975324879786,
          "depth_with_background": -0.012253150971007388,
          "scan_edge": false,
          "x_template_shift_pix": 0.00019279830564980597,
          "x_err_pix": 0.0009611739932692893,
          "y_template_shift_pix": 0.0010604507658351211,
          "y_err_pix": 0.0009816489268645227,
          "cycle": 125
        },
        {
          "status": "insufficient",
          "tc_nom": 3868.060636364179,
          "sec": 94,
          "n_in": 0,
          "cycle": 126
        },
        {
          "status": "fit",
          "sec": 94,
          "tc_nom": 3873.8862191033395,
          "tc": 3873.8862191033395,
          "tc_error": 0.0006324827586206897,
          "depth": -0.010440954497915156,
          "depth_error": 0.004999435260275058,
          "T14": 0.21082758620689654,
          "T12": 0.07378965517241379,
          "T23": 0.06324827586206896,
          "beta": 3.874409731125598,
          "n_in": 67,
          "flagged_core": 24,
          "flag_bits_core": 1073741824,
          "background_fake_depth": -9.430082303307278e-06,
          "depth_with_background": -0.010431871393149075,
          "scan_edge": false,
          "x_template_shift_pix": 5.7291849424817076e-05,
          "x_err_pix": 0.0016039031955308585,
          "y_template_shift_pix": 0.0007413011278427652,
          "y_err_pix": 0.0016114193663836092,
          "cycle": 127
        },
        {
          "status": "fit",
          "sec": 94,
          "tc_nom": 3879.7118018425,
          "tc": 3879.7118018425,
          "tc_error": 0.0006324827586206897,
          "depth": -0.00847245479294592,
          "depth_error": 0.004449220231653192,
          "T14": 0.21082758620689654,
          "T12": 0.07378965517241379,
          "T23": 0.06324827586206896,
          "beta": 3.9665997366630306,
          "n_in": 85,
          "flagged_core": 6,
          "flag_bits_core": 1073741824,
          "background_fake_depth": -0.00011594571868405449,
          "depth_with_background": -0.008356905682261138,
          "scan_edge": false,
          "x_template_shift_pix": -0.0006202496816592973,
          "x_err_pix": 0.0012454622176090188,
          "y_template_shift_pix": 7.173694336607884e-05,
          "y_err_pix": 0.001310882444463925,
          "cycle": 128
        }
      ]
    },
    "controls": [
      {
        "n": 11,
        "depth": 0.007501685528930469,
        "error": 0.0020729408299475062,
        "snr": 3.6188613879154654,
        "scatter": 0.0013452781679534663,
        "chi2": 0.4098761797244565,
        "dof": 10,
        "phase": 0.1
      },
      {
        "n": 11,
        "depth": 6.422429064611454e-05,
        "error": 8.011492851668591e-05,
        "snr": 0.8016519746720894,
        "scatter": 0.00023602869079540465,
        "chi2": 8.10330225588723,
        "dof": 10,
        "phase": 0.15000000000000002
      },
      {
        "n": 10,
        "depth": 4.4203288422837456e-05,
        "error": 8.099046216394852e-05,
        "snr": 0.5457838767898002,
        "scatter": 0.0003543614087062882,
        "chi2": 13.899370389910274,
        "dof": 9,
        "phase": 0.20000000000000004
      },
      {
        "n": 10,
        "depth": 5.815955528841765e-06,
        "error": 7.895153452975235e-05,
        "snr": 0.07366488268381992,
        "scatter": 0.00030762464791433096,
        "chi2": 11.470047501123219,
        "dof": 9,
        "phase": 0.25000000000000006
      },
      {
        "n": 11,
        "depth": -0.00011025521605035874,
        "error": 7.656614021004321e-05,
        "snr": -1.4399996623559264,
        "scatter": 0.00023862648538885064,
        "chi2": 6.743443339067092,
        "dof": 10,
        "phase": 0.30000000000000004
      },
      {
        "n": 11,
        "depth": 4.481129537273677e-05,
        "error": 7.876609080829739e-05,
        "snr": 0.5689160768661158,
        "scatter": 0.000314267372598804,
        "chi2": 9.757330089654232,
        "dof": 10,
        "phase": 0.3500000000000001
      },
      {
        "n": 9,
        "depth": -0.00029752534946022056,
        "error": 0.0001801113726026503,
        "snr": -1.6518965191420818,
        "scatter": 0.0016516067014541768,
        "chi2": 10.497707516453866,
        "dof": 8,
        "phase": 0.40000000000000013
      },
      {
        "n": 10,
        "depth": -0.0006047986501243181,
        "error": 0.0004768716446200848,
        "snr": -1.2682629737948679,
        "scatter": 0.0024589431527848307,
        "chi2": 18.11150841728915,
        "dof": 9,
        "phase": 0.45000000000000007
      },
      {
        "n": 9,
        "depth": 0.026411919216185117,
        "error": 0.00010573963784241166,
        "snr": 249.7825768568258,
        "scatter": 0.0019355905362816383,
        "chi2": 340.0439256150322,
        "dof": 8,
        "phase": 0.5000000000000001
      },
      {
        "n": 8,
        "depth": -0.0007659231488208406,
        "error": 0.0005254769679996444,
        "snr": -1.4575770118650737,
        "scatter": 0.002407082142862373,
        "chi2": 13.808616744057442,
        "dof": 7,
        "phase": 0.5500000000000002
      },
      {
        "n": 10,
        "depth": 0.0006975981846030983,
        "error": 0.0004183069818156837,
        "snr": 1.6676704308762345,
        "scatter": 0.0012579932802515878,
        "chi2": 7.684594800408375,
        "dof": 9,
        "phase": 0.6000000000000002
      },
      {
        "n": 10,
        "depth": 5.3105223746537507e-05,
        "error": 0.0001032249073707423,
        "snr": 0.5144613359235569,
        "scatter": 0.00048186420415024893,
        "chi2": 16.0336471778104,
        "dof": 9,
        "phase": 0.6500000000000001
      },
      {
        "n": 9,
        "depth": 4.6991916076902464e-05,
        "error": 0.00011312084199185309,
        "snr": 0.4154134220490226,
        "scatter": 0.00021626043377997707,
        "chi2": 3.5156822398278895,
        "dof": 8,
        "phase": 0.7000000000000002
      },
      {
        "n": 9,
        "depth": -6.004697291653503e-05,
        "error": 0.00010904303513693819,
        "snr": -0.550672244597071,
        "scatter": 0.0005140221096137344,
        "chi2": 14.873761805479768,
        "dof": 8,
        "phase": 0.7500000000000002
      },
      {
        "n": 8,
        "depth": 0.00010596742760916957,
        "error": 0.00010954507049192264,
        "snr": 0.9673409048286032,
        "scatter": 0.00037840829109905144,
        "chi2": 10.92324833321145,
        "dof": 7,
        "phase": 0.8000000000000002
      },
      {
        "n": 11,
        "depth": 9.672894952895935e-05,
        "error": 9.03981829938028e-05,
        "snr": 1.0700320108822383,
        "scatter": 0.0003084733461871905,
        "chi2": 10.041602205039384,
        "dof": 10,
        "phase": 0.8500000000000002
      },
      {
        "n": 10,
        "depth": 0.00030166020121725974,
        "error": 0.0003523973297906873,
        "snr": 0.8560229482908859,
        "scatter": 0.0027261266696401083,
        "chi2": 10.889480409327591,
        "dof": 9,
        "phase": 0.9000000000000002
      },
      {
        "n": 11,
        "depth": -0.016031488877599812,
        "error": 0.003207776107607119,
        "snr": -4.997695705626633,
        "scatter": 0.0017138727793283054,
        "chi2": 0.27786470610342334,
        "dof": 10,
        "phase": 0.9500000000000003
      },
      {
        "n": 10,
        "depth": -0.0009004036767013284,
        "error": 0.0005665987851005401,
        "snr": -1.5891380291991912,
        "scatter": 0.0030639781802322156,
        "chi2": 32.80262775238627,
        "dof": 9,
        "phase": 0.526930647023727,
        "control_scatter": 0.004695514773510155,
        "upper_3sigma": 0.014086544320530464
      }
    ],
    "physics": [
      {
        "m1": 1.11,
        "m2_min": 0.6788348617118547,
        "f_mass": 0.09775791098493487,
        "a_rsun": 16.539877583192265,
        "r1_rsun": 2.42488,
        "r2_approx_rsun": 0.7335189026341297,
        "central_T14_hours": {
          "A": 8.644336869337469,
          "B": 8.340564723183823
        },
        "observed_T14_hours": 5.059862068965517
      }
    ],
    "period_delta_sigma": -0.44733686420777735
  },
  "covariance_geometry": {
    "bit_index": 127,
    "gaia_primary": "A",
    "gaia_relative_phase_nominal": 0.526930647023727,
    "gaia_relative_phase_quantiles_16_50_84": [
      0.509682679004746,
      0.5221610597291002,
      0.5359022743963849
    ],
    "gaia_relative_phase_sigma": 0.013132054939758322,
    "gaia_e_cos_omega_quantiles": [
      0.015199584465658434,
      0.034804518052089964,
      0.05640515049309252
    ],
    "gaia_e_sin_omega_quantiles": [
      -0.04378457831522854,
      -0.015010402625209932,
      0.005159078303713091
    ],
    "photometric_phase": 0.5001500791769494,
    "photometric_e_cos_omega_first_order": 0.0002357438198805577,
    "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
    "geometry_status": "conditional shape feasibility",
    "geometry_e_sin_omega_conditional_range": [
      0.12499999999999994,
      0.12499999999999994
    ],
    "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
  },
  "conditional_two_disk_geometry": {
    "status": "conditional shape feasibility",
    "best": {
      "chi2": 323.73433553419284,
      "dof": 121,
      "k": 0.24999999999999997,
      "b_A": 0.7950000000000002,
      "e_sin_omega": 0.12499999999999994,
      "primary_scale": 1.0,
      "secondary_scale": 0.07001602539267648
    },
    "profile_interval_approx_95": {
      "k": [
        0.24999999999999997,
        0.24999999999999997
      ],
      "b_A": [
        0.7950000000000002,
        0.7950000000000002
      ],
      "e_sin_omega": [
        0.12499999999999994,
        0.12499999999999994
      ]
    },
    "error_inflation": 2.6754903763156435,
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
  "sector": 67,
  "provenance": "SPOC",
  "fits_identity_validated": true,
  "quality_column_present": true,
  "events": [
    {
      "tc": 3130.9675700689654,
      "qlp": {
        "1": {
          "depth": 0.06529124370427689,
          "error": 0.0005130623632699111,
          "red_noise_beta": 1.5770081320602038,
          "n_core": 91,
          "baseline_degree": 1,
          "background_regressed_depth": 0.06536193102152371,
          "background_template_native_sigma": 0.07831769224170827
        },
        "2": {
          "depth": 0.06482849224170768,
          "error": 0.0005513057902685319,
          "red_noise_beta": 1.5418354233554286,
          "n_core": 91,
          "baseline_degree": 2,
          "background_regressed_depth": 0.06488489490634364,
          "background_template_native_sigma": 0.0623093125548261
        }
      },
      "independent": {
        "SAP_FLUX": {
          "1": {
            "depth": 0.06091820043032117,
            "error": 0.0004376448171325368,
            "red_noise_beta": 1.8936761999710836,
            "n_core": 152,
            "baseline_degree": 1,
            "background_regressed_depth": 0.061539433282718714,
            "background_template_native_sigma": 0.672018695500491
          },
          "2": {
            "depth": 0.06045337002336058,
            "error": 0.00045519811590840633,
            "red_noise_beta": 1.7955976794390818,
            "n_core": 152,
            "baseline_degree": 2,
            "background_regressed_depth": 0.06102387124298941,
            "background_template_native_sigma": 0.5917996303717963
          }
        },
        "PDCSAP_FLUX": {
          "1": {
            "depth": 0.06194412581928007,
            "error": 0.00044156503347929756,
            "red_noise_beta": 1.8770295320662882,
            "n_core": 152,
            "baseline_degree": 1,
            "background_regressed_depth": 0.06257392891125148,
            "background_template_native_sigma": 0.672018695500491
          },
          "2": {
            "depth": 0.06153190999373936,
            "error": 0.00046694742964339036,
            "red_noise_beta": 1.8051761225081284,
            "n_core": 152,
            "baseline_degree": 2,
            "background_regressed_depth": 0.06210771618235774,
            "background_template_native_sigma": 0.5917996303717963
          }
        }
      }
    },
    {
      "tc": 3142.6186728249545,
      "qlp": {
        "1": {
          "depth": 0.06587098834178523,
          "error": 0.0004902110027998316,
          "red_noise_beta": 1.5301308082790508,
          "n_core": 91,
          "baseline_degree": 1,
          "background_regressed_depth": 0.06630681030062309,
          "background_template_native_sigma": 0.5805589998237558
        },
        "2": {
          "depth": 0.06531738164880299,
          "error": 0.0005172822529232551,
          "red_noise_beta": 1.4746455830994576,
          "n_core": 91,
          "baseline_degree": 2,
          "background_regressed_depth": 0.0656298636286474,
          "background_template_native_sigma": 0.3919633440621917
        }
      },
      "independent": {
        "SAP_FLUX": {
          "1": {
            "depth": 0.06129739810973945,
            "error": 0.00044373315948638886,
            "red_noise_beta": 1.829131380738969,
            "n_core": 151,
            "baseline_degree": 1,
            "background_regressed_depth": 0.061740279985341685,
            "background_template_native_sigma": 0.5783896781444573
          },
          "2": {
            "depth": 0.06080557836093089,
            "error": 0.0004584497702171423,
            "red_noise_beta": 1.723090153550826,
            "n_core": 151,
            "baseline_degree": 2,
            "background_regressed_depth": 0.06121798747447693,
            "background_template_native_sigma": 0.5326209704068721
          }
        },
        "PDCSAP_FLUX": {
          "1": {
            "depth": 0.06240005833615117,
            "error": 0.0004468352948882808,
            "red_noise_beta": 1.8132559706014484,
            "n_core": 151,
            "baseline_degree": 1,
            "background_regressed_depth": 0.06284904499112604,
            "background_template_native_sigma": 0.5783896781444573
          },
          "2": {
            "depth": 0.061931978364909,
            "error": 0.0004665915449511542,
            "red_noise_beta": 1.7242504550372273,
            "n_core": 151,
            "baseline_degree": 2,
            "background_regressed_depth": 0.06234980731744048,
            "background_template_native_sigma": 0.5326209704068721
          }
        }
      }
    },
    {
      "tc": 3148.4442242029486,
      "qlp": {
        "1": {
          "depth": 0.065479450661358,
          "error": 0.000505014337393955,
          "red_noise_beta": 1.5393505507283418,
          "n_core": 91,
          "baseline_degree": 1,
          "background_regressed_depth": 0.06572864348465926,
          "background_template_native_sigma": 0.24762579382414956
        },
        "2": {
          "depth": 0.0649189211487917,
          "error": 0.0005331147052123233,
          "red_noise_beta": 1.4765032557830784,
          "n_core": 91,
          "baseline_degree": 2,
          "background_regressed_depth": 0.06516322611890053,
          "background_template_native_sigma": 0.2425257917524243
        }
      },
      "independent": {
        "SAP_FLUX": {
          "1": {
            "depth": 0.06066326146871611,
            "error": 0.00042547007346693425,
            "red_noise_beta": 1.7921812681598963,
            "n_core": 152,
            "baseline_degree": 1,
            "background_regressed_depth": 0.06096447103969774,
            "background_template_native_sigma": 0.72950413575382
          },
          "2": {
            "depth": 0.060435471967050354,
            "error": 0.00046785314940267264,
            "red_noise_beta": 1.7728102076386651,
            "n_core": 152,
            "baseline_degree": 2,
            "background_regressed_depth": 0.06051348077830295,
            "background_template_native_sigma": 0.14845814651044298
          }
        },
        "PDCSAP_FLUX": {
          "1": {
            "depth": 0.06127540786524081,
            "error": 0.0004301665281344294,
            "red_noise_beta": 1.785692306899311,
            "n_core": 152,
            "baseline_degree": 1,
            "background_regressed_depth": 0.06163852390460498,
            "background_template_native_sigma": 0.72950413575382
          },
          "2": {
            "depth": 0.0614810945528842,
            "error": 0.00047378670494079613,
            "red_noise_beta": 1.7684056057376447,
            "n_core": 152,
            "baseline_degree": 2,
            "background_regressed_depth": 0.06155797533139017,
            "background_template_native_sigma": 0.14845814651044298
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
[]
```

Original batch difference-image receipts; old/new schema duplicates are the same events:

```json
[
  {
    "tic": "211231319",
    "sector": 92,
    "n_events": 4,
    "deficit_minus_target_arcsec": 1.61,
    "deficit_minus_light_arcsec": 0.53,
    "peak_on_target": true,
    "depth_ap3": 0.06209,
    "psf_frac_resid": 0.15,
    "n_neighbours_60": 19,
    "n_possible": 0,
    "brightest_nb": {
      "G": 15.675792,
      "sep": 43.3
    }
  }
]
```

## Archives and novelty

Successful current shared60arcsec VSX, Gaia vari_summary/vari_eclipsing_binary, SIMBAD exact Gaia-ID and ExoFOP TOI/CTOI responses were rechecked. Exact paths/hashes below and shared receipts preserve timestamps. No Gaia EB/vari_summary entries and no TOI/CTOI entries for these targets. SIMBAD lists known spectroscopic binaries, not prior eclipse classifications.

```json
{
  "simbad": [
    {
      "id": "Gaia DR3 6749770323777264128",
      "main_id": "TYC 7440-1461-1",
      "otype": "SB*",
      "ra": "299.51092397216",
      "dec": "-31.327449139220004"
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
      "path": "C:\\Home\\Astra\\made\\binary-handoff-2026-10-30\\shared-full-review\\vsx\\211231319.tsv",
      "sha256": "561d9171d5a6318a11db31808ba3c1bba347627871e28b5e0c40e8618984d349"
    },
    {
      "path": "C:\\Home\\Astra\\made\\binary-handoff-2026-10-30\\shared-full-review\\exofop\\211231319.json",
      "sha256": "55e14f91c83a41dc54554154f4152af65ccf87d950343308a49dded6f20bd21c"
    }
  ]
}
```

One bounded Harvard multi-catalogue mirror probe timed out after batchG reported all IDIA9 requests timing out. ASAS-SN, SB9, WDS, Prsa, IJspeert and Kostov tables therefore remain unchecked in this fresh pass; failed service is not a negative match. VSX raw table sections were inspected; no target EB rows found. General web searches on the ten exact SIMBAD names plus eclipsing/binary found only unrelated results, not exact-target prior publications. This does not establish novelty or a complete bibliography.

## Predictions and deciding next check

AtBTJD4344.32880: next primary~4348.51433; other conjunction~4345.60159. Photometric extrapolations are scheduling estimates, conditional on stationary orbit. For null secondary use Gaia phase uncertainty, not the single date.

Joint diluted light-curve/RV modelling to refine radii, flux ratio and small-e geometry.

Final adjudication: **CONFIRMED**. Repeated primary and secondary eclipses, independent SPOC recovery, own Gaia timing and on-target deficit establish a target EB; no bright capable neighbor.

Reproducibility: scripts and manifests retained in this batch. Original source audit completed before work; no source/paper edits or commits.

Lead control audit: {"median_primary_ppt": 62.88077035150803, "offphase_census_triggers": 5, "max_offphase_census_ppt": 8.896080455776945, "minimum_bg_regressed_depth_ratio": 0.9997180259837454}. Census trigger centers/durations can merge broad eclipse wings, especially253923749; they are not a calibrated blind-search catalog.
