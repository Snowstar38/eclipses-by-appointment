# TIC 351541670: PLAUSIBLE

The two-kind EB is secure but host unresolved: circular calibration favors target while expanded calibration moves to21.77arcsec neighbor and a large WCS shift. A capable1.23arcsec companion also remains unresolved. Ranking depends on calibration; no unique host is claimed.

Full review: COMPLETE (adjudicated). Novelty: LIMITED; successful checks found no target EB classification, but several catalogues were unavailable.

Raw untrimmed QUALITY=0 SAP: 8 accepted primary fits; median depth65.265ppt; T14=4.1909h. Primary and secondary individual timing/depth errors, duration/ingress/flat coordinates, O-C and rejected windows are tabulated below. Errors are conditional on shape/local baseline with grid and red-noise inflation. Trapezoid flat time is not measured totality.

```json
{
  "primary_shape": {
    "T14": 0.1746206896551724,
    "fr": 0.25,
    "shift": 0,
    "T14_range": [
      0.17099999999999999,
      0.17824137931034484
    ],
    "fr_range": [
      0.21,
      0.29
    ],
    "n_local_windows": 7,
    "error_note": "profile likelihood plus half-grid resolution; conditional shape model"
  },
  "primary_ephemeris": {
    "P": 4.155085803937364,
    "P_error": 2.5697387743335798e-06,
    "Tref": 2917.937589709707,
    "Tref_error": 0.00031057544929777623,
    "reference_cycle": 223,
    "T0": 1991.3534554316748,
    "chi2": 0.9489704973566231,
    "dof": 6,
    "n": 8,
    "oc_rms_minutes": 0.45539126045736944
  },
  "primary_events": [
    {
      "status": "insufficient",
      "tc_nom": 1987.1988183548604,
      "sec": 25,
      "n_in": 0,
      "cycle": -1
    },
    {
      "status": "insufficient",
      "tc_nom": 1991.3539,
      "sec": 25,
      "n_in": 8,
      "cycle": 0
    },
    {
      "status": "insufficient",
      "tc_nom": 1995.5089816451398,
      "sec": 25,
      "n_in": 0,
      "cycle": 1
    },
    {
      "status": "insufficient",
      "tc_nom": 1999.6640632902797,
      "sec": 25,
      "n_in": 0,
      "cycle": 2
    },
    {
      "status": "fit",
      "sec": 25,
      "tc_nom": 2003.8191449354194,
      "tc": 2003.8191449354194,
      "tc_error": 0.0021262915091884403,
      "depth": 0.06553625644179153,
      "depth_error": 0.0005365316250521009,
      "T14": 0.1746206896551724,
      "T12": 0.0436551724137931,
      "T23": 0.0873103448275862,
      "beta": 1.0,
      "n_in": 8,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -0.0004143823658111267,
      "depth_with_background": 0.06639795245569577,
      "scan_edge": false,
      "x_template_shift_pix": 0.0022556511802813203,
      "x_err_pix": 0.00027518480563798985,
      "y_template_shift_pix": -0.0054032787573631115,
      "y_err_pix": 0.00035567084166608664,
      "cycle": 3,
      "oc_days": 0.00043209193245274946
    },
    {
      "status": "fit",
      "sec": 25,
      "tc_nom": 2007.9742265805592,
      "tc": 2007.9742265805592,
      "tc_error": 0.0020046868599020323,
      "depth": 0.06526041345392888,
      "depth_error": 0.0006633722974878111,
      "T14": 0.1746206896551724,
      "T12": 0.0436551724137931,
      "T23": 0.0873103448275862,
      "beta": 1.0,
      "n_in": 9,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": 0.00023872249334178745,
      "depth_with_background": 0.06448768692850353,
      "scan_edge": false,
      "x_template_shift_pix": 0.0006903822878530932,
      "x_err_pix": 0.0007470644165424519,
      "y_template_shift_pix": -0.00526921442633099,
      "y_err_pix": 0.0007915974309989143,
      "cycle": 4,
      "oc_days": 0.0004279331349152926
    },
    {
      "status": "insufficient",
      "tc_nom": 2722.648269544603,
      "sec": 52,
      "n_in": 0,
      "cycle": 176
    },
    {
      "status": "fit",
      "sec": 52,
      "tc_nom": 2726.803351189743,
      "tc": 2726.804398913881,
      "tc_error": 0.0010477241379310345,
      "depth": 0.06252487403001666,
      "depth_error": 0.0019809161190403653,
      "T14": 0.1746206896551724,
      "T12": 0.0436551724137931,
      "T23": 0.0873103448275862,
      "beta": 1.238872841321713,
      "n_in": 14,
      "flagged_core": 11,
      "flag_bits_core": 18432,
      "background_fake_depth": 0.0017207655277552243,
      "depth_with_background": 0.060632085511515686,
      "scan_edge": false,
      "x_template_shift_pix": 0.0030247493602217237,
      "x_err_pix": 0.000482824516560661,
      "y_template_shift_pix": -0.0025342783101535756,
      "y_err_pix": 0.00037726969731402175,
      "cycle": 177,
      "oc_days": 0.0007561852926301071
    },
    {
      "status": "insufficient",
      "tc_nom": 2730.958432834883,
      "sec": 52,
      "n_in": 0,
      "cycle": 178
    },
    {
      "status": "insufficient",
      "tc_nom": 2735.113514480023,
      "sec": 52,
      "n_in": 0,
      "cycle": 179
    },
    {
      "status": "fit",
      "sec": 52,
      "tc_nom": 2739.2685961251623,
      "tc": 2739.2685961251623,
      "tc_error": 0.0005238620689655173,
      "depth": 0.06541377473514827,
      "depth_error": 0.0007372591756462628,
      "T14": 0.1746206896551724,
      "T12": 0.0436551724137931,
      "T23": 0.0873103448275862,
      "beta": 1.127335611358717,
      "n_in": 16,
      "flagged_core": 10,
      "flag_bits_core": 18432,
      "background_fake_depth": 0.0005072830608295139,
      "depth_with_background": 0.0648865200229344,
      "scan_edge": false,
      "x_template_shift_pix": 0.0024184244674874578,
      "x_err_pix": 0.0004610321768551652,
      "y_template_shift_pix": -0.004112864309842549,
      "y_err_pix": 0.0003548201276356338,
      "cycle": 180,
      "oc_days": -0.00030401523827094934
    },
    {
      "status": "fit",
      "sec": 79,
      "tc_nom": 3453.9426390892063,
      "tc": 3453.9436868133444,
      "tc_error": 0.0005238620689655173,
      "depth": 0.06526871170997502,
      "depth_error": 0.0006364812324561924,
      "T14": 0.1746206896551724,
      "T12": 0.0436551724137931,
      "T23": 0.0873103448275862,
      "beta": 2.2245820317495753,
      "n_in": 76,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -0.00011360378260267563,
      "depth_with_background": 0.06537460396579026,
      "scan_edge": false,
      "x_template_shift_pix": 0.0016065494724570662,
      "x_err_pix": 0.0005522605613535528,
      "y_template_shift_pix": -0.005608418700488267,
      "y_err_pix": 0.0005615127611853277,
      "cycle": 352,
      "oc_days": 2.839571743606939e-05
    },
    {
      "status": "insufficient",
      "tc_nom": 3458.097720734346,
      "sec": 79,
      "n_in": 0,
      "cycle": 353
    },
    {
      "status": "insufficient",
      "tc_nom": 3462.2528023794857,
      "sec": 79,
      "n_in": 0,
      "cycle": 354
    },
    {
      "status": "fit",
      "sec": 79,
      "tc_nom": 3466.4078840246257,
      "tc": 3466.4089317487637,
      "tc_error": 0.0005238620689655173,
      "depth": 0.0650907929050026,
      "depth_error": 0.000641394455964037,
      "T14": 0.1746206896551724,
      "T12": 0.0436551724137931,
      "T23": 0.0873103448275862,
      "beta": 2.2532637596812104,
      "n_in": 76,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -0.000167180087645724,
      "depth_with_background": 0.06525160746688503,
      "scan_edge": false,
      "x_template_shift_pix": 0.0029186492363629363,
      "x_err_pix": 0.0006723981402587517,
      "y_template_shift_pix": -0.005594532243784236,
      "y_err_pix": 0.0006074731043874339,
      "cycle": 355,
      "oc_days": 1.591932459632517e-05
    },
    {
      "status": "fit",
      "sec": 79,
      "tc_nom": 3470.5629656697656,
      "tc": 3470.5640133939037,
      "tc_error": 0.0005238620689655173,
      "depth": 0.06520513943824069,
      "depth_error": 0.0005839734482351178,
      "T14": 0.1746206896551724,
      "T12": 0.0436551724137931,
      "T23": 0.0873103448275862,
      "beta": 2.0777952269666664,
      "n_in": 76,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": 0.00027657751621228767,
      "depth_with_background": 0.06480619124021128,
      "scan_edge": false,
      "x_template_shift_pix": 0.0008265041408624677,
      "x_err_pix": 0.0006118315099645794,
      "y_template_shift_pix": -0.004546712738136954,
      "y_err_pix": 0.0007039467642670293,
      "cycle": 356,
      "oc_days": 1.1760527286241995e-05
    },
    {
      "status": "insufficient",
      "tc_nom": 3474.7180473149056,
      "sec": 79,
      "n_in": 0,
      "cycle": 357
    },
    {
      "status": "fit",
      "sec": 79,
      "tc_nom": 3478.873128960045,
      "tc": 3478.874176684183,
      "tc_error": 0.0005238620689655173,
      "depth": 0.06527646528922651,
      "depth_error": 0.000538581685561948,
      "T14": 0.1746206896551724,
      "T12": 0.0436551724137931,
      "T23": 0.0873103448275862,
      "beta": 1.9416230395240148,
      "n_in": 76,
      "flagged_core": 0,
      "flag_bits_core": 0,
      "background_fake_depth": -7.342548263858576e-05,
      "depth_with_background": 0.06534838888000456,
      "scan_edge": false,
      "x_template_shift_pix": 0.0002160418319132647,
      "x_err_pix": 0.0005661387508245235,
      "y_template_shift_pix": -0.0027898046943129738,
      "y_err_pix": 0.0007041362573853294,
      "cycle": 358,
      "oc_days": 3.442931756580947e-06
    }
  ],
  "secondary": {
    "predicted_gaia_phase": 0.48654805905118204,
    "profile_phase": 0.4999963061696181,
    "statistic": {
      "n": 9,
      "depth": 0.004528759442487044,
      "error": 0.00011024746631336535,
      "snr": 41.078127179944275,
      "scatter": 0.0008809108104260513,
      "chi2": 13.061774878126435,
      "dof": 8,
      "empirical_error": 0.00029363693680868375,
      "n_individual_gt3sigma": 8
    },
    "events": [
      {
        "status": "insufficient",
        "tc_nom": 1985.1208113775865,
        "sec": 25,
        "n_in": 3,
        "cycle": -2
      },
      {
        "status": "insufficient",
        "tc_nom": 1989.2758971815238,
        "sec": 25,
        "n_in": 0,
        "cycle": -1
      },
      {
        "status": "fit",
        "sec": 25,
        "tc_nom": 1993.4309829854612,
        "tc": 1993.4246966406336,
        "tc_error": 0.0026193103448275863,
        "depth": 0.004186320657812239,
        "depth_error": 0.0002935494499707658,
        "T14": 0.1746206896551724,
        "T12": 0.0436551724137931,
        "T23": 0.0873103448275862,
        "beta": 1.0286456665009784,
        "n_in": 9,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": -3.122770555049244e-05,
        "depth_with_background": 0.004211621382546754,
        "scan_edge": false,
        "x_template_shift_pix": -0.00016618761012718238,
        "x_err_pix": 0.0005988297888404351,
        "y_template_shift_pix": -4.1679647255247655e-05,
        "y_err_pix": 0.0006982031661557218,
        "cycle": 0,
        "oc_days": -0.0021494641741810483
      },
      {
        "status": "insufficient",
        "tc_nom": 1997.5860687893985,
        "sec": 25,
        "n_in": 3,
        "cycle": 1
      },
      {
        "status": "insufficient",
        "tc_nom": 2001.741154593336,
        "sec": 25,
        "n_in": 0,
        "cycle": 2
      },
      {
        "status": "fit",
        "sec": 25,
        "tc_nom": 2005.8962403972732,
        "tc": 2005.8930972248595,
        "tc_error": 0.0021262915091884403,
        "depth": 0.0047497173172470954,
        "depth_error": 0.0002443236402833591,
        "T14": 0.1746206896551724,
        "T12": 0.0436551724137931,
        "T23": 0.0873103448275862,
        "beta": 1.042688442019034,
        "n_in": 8,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": 4.342198660203923e-05,
        "depth_with_background": 0.004732251849109565,
        "scan_edge": false,
        "x_template_shift_pix": -0.00011968073514312635,
        "x_err_pix": 0.0002729961680923185,
        "y_template_shift_pix": -7.060731085430022e-05,
        "y_err_pix": 0.00045376799962087343,
        "cycle": 3,
        "oc_days": 0.0009928829115324334
      },
      {
        "status": "insufficient",
        "tc_nom": 2720.5709986745,
        "sec": 52,
        "n_in": 0,
        "cycle": 175
      },
      {
        "status": "fit",
        "sec": 52,
        "tc_nom": 2724.7260844784373,
        "tc": 2724.713511788782,
        "tc_error": 0.008381793103448276,
        "depth": 0.006285753117006433,
        "depth_error": 0.0011537847588332254,
        "T14": 0.1746206896551724,
        "T12": 0.0436551724137931,
        "T23": 0.0873103448275862,
        "beta": 1.3640841260134036,
        "n_in": 11,
        "flagged_core": 15,
        "flag_bits_core": 18432,
        "background_fake_depth": 0.0015609060415923547,
        "depth_with_background": 0.004317121955327114,
        "scan_edge": false,
        "x_template_shift_pix": 0.0017712846286137938,
        "x_err_pix": 0.0009400048053315913,
        "y_template_shift_pix": 0.0015408462810928838,
        "y_err_pix": 0.0008526857320575091,
        "cycle": 176,
        "oc_days": -0.008484228256293136
      },
      {
        "status": "fit",
        "sec": 52,
        "tc_nom": 2728.881170282375,
        "tc": 2728.890599799616,
        "tc_error": 0.006286344827586204,
        "depth": 0.003736305397472082,
        "depth_error": 0.0006926751000992894,
        "T14": 0.1746206896551724,
        "T12": 0.0436551724137931,
        "T23": 0.0873103448275862,
        "beta": 1.0,
        "n_in": 15,
        "flagged_core": 10,
        "flag_bits_core": 18432,
        "background_fake_depth": -0.0011739107897104915,
        "depth_with_background": 0.004793710296887095,
        "scan_edge": false,
        "x_template_shift_pix": -0.0008745764979608711,
        "x_err_pix": 0.0005175425060667167,
        "y_template_shift_pix": -0.0006666310050375558,
        "y_err_pix": 0.00037233486432599927,
        "cycle": 177,
        "oc_days": 0.013517703531306324
      },
      {
        "status": "fit",
        "sec": 52,
        "tc_nom": 2733.0362560863123,
        "tc": 2733.088642293209,
        "tc_error": 0.006286344827586207,
        "depth": 0.006438331186121868,
        "depth_error": 0.0017776063084177641,
        "T14": 0.1746206896551724,
        "T12": 0.0436551724137931,
        "T23": 0.0873103448275862,
        "beta": 1.4176743832939358,
        "n_in": 10,
        "flagged_core": 15,
        "flag_bits_core": 18432,
        "background_fake_depth": 0.0028805468929944135,
        "depth_with_background": 0.0036460958223583774,
        "scan_edge": true,
        "x_template_shift_pix": 0.003389445117667747,
        "x_err_pix": 0.0012931744331453284,
        "y_template_shift_pix": 0.003499596623327978,
        "y_err_pix": 0.0010962538821414818,
        "cycle": 178
      },
      {
        "status": "insufficient",
        "tc_nom": 2737.1913418902495,
        "sec": 52,
        "n_in": 0,
        "cycle": 179
      },
      {
        "status": "fit",
        "sec": 52,
        "tc_nom": 2741.3464276941872,
        "tc": 2741.3411890734974,
        "tc_error": 0.008381793103448273,
        "depth": 0.004933549329993939,
        "depth_error": 0.0009900416180497506,
        "T14": 0.1746206896551724,
        "T12": 0.0436551724137931,
        "T23": 0.0873103448275862,
        "beta": 1.0,
        "n_in": 14,
        "flagged_core": 11,
        "flag_bits_core": 18432,
        "background_fake_depth": 0.0009937994050778756,
        "depth_with_background": 0.003850638738352039,
        "scan_edge": false,
        "x_template_shift_pix": -0.0005227956782112565,
        "x_err_pix": 0.00034334177728644614,
        "y_template_shift_pix": 0.0003954572126720677,
        "y_err_pix": 0.00030667620652811685,
        "cycle": 180,
        "oc_days": -0.0011512597279761394
      },
      {
        "status": "insufficient",
        "tc_nom": 3456.0211859714136,
        "sec": 79,
        "n_in": 0,
        "cycle": 352
      },
      {
        "status": "insufficient",
        "tc_nom": 3460.1762717753513,
        "sec": 79,
        "n_in": 0,
        "cycle": 353
      },
      {
        "status": "fit",
        "sec": 79,
        "tc_nom": 3464.3313575792886,
        "tc": 3464.322975786185,
        "tc_error": 0.0015715862068965518,
        "depth": 0.0041909944782730305,
        "depth_error": 0.00023176607485504865,
        "T14": 0.1746206896551724,
        "T12": 0.0436551724137931,
        "T23": 0.0873103448275862,
        "beta": 1.0,
        "n_in": 73,
        "flagged_core": 3,
        "flag_bits_core": 1073741824,
        "background_fake_depth": 4.3822014865912824e-05,
        "depth_with_background": 0.004150622521093067,
        "scan_edge": false,
        "x_template_shift_pix": -0.0006775718803546933,
        "x_err_pix": 0.0004496284471172494,
        "y_template_shift_pix": 0.0015793234130491909,
        "y_err_pix": 0.00048117597518324907,
        "cycle": 354,
        "oc_days": -0.004342301177075569
      },
      {
        "status": "fit",
        "sec": 79,
        "tc_nom": 3468.486443383226,
        "tc": 3468.486443383226,
        "tc_error": 0.002095448275862069,
        "depth": 0.004946790853283157,
        "depth_error": 0.00022712943925534706,
        "T14": 0.1746206896551724,
        "T12": 0.0436551724137931,
        "T23": 0.0873103448275862,
        "beta": 1.0245553203487208,
        "n_in": 76,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": -0.0003389781024740452,
        "depth_with_background": 0.005289363858622982,
        "scan_edge": false,
        "x_template_shift_pix": 0.00036793944485940546,
        "x_err_pix": 0.0002478712694822958,
        "y_template_shift_pix": -8.503019585194828e-06,
        "y_err_pix": 0.0003063371005886849,
        "cycle": 355,
        "oc_days": 0.004039216816636326
      },
      {
        "status": "fit",
        "sec": 79,
        "tc_nom": 3472.641529187163,
        "tc": 3472.644672359577,
        "tc_error": 0.0031431724137931036,
        "depth": 0.004339017566941941,
        "depth_error": 0.00029180413088341955,
        "T14": 0.1746206896551724,
        "T12": 0.0436551724137931,
        "T23": 0.0873103448275862,
        "beta": 1.2065517951031612,
        "n_in": 76,
        "flagged_core": 0,
        "flag_bits_core": 0,
        "background_fake_depth": 3.965740367017721e-05,
        "depth_with_background": 0.004279926074727482,
        "scan_edge": false,
        "x_template_shift_pix": -4.1403782654203094e-05,
        "x_err_pix": 0.00047157997469956224,
        "y_template_shift_pix": 0.0007652573530392639,
        "y_err_pix": 0.00043376746875604526,
        "cycle": 356,
        "oc_days": 0.007182114120951155
      },
      {
        "status": "insufficient",
        "tc_nom": 3476.7966149911003,
        "sec": 79,
        "n_in": 0,
        "cycle": 357
      }
    ],
    "ephemeris": {
      "P": 4.1550860790467645,
      "P_error": 1.1219246150398072e-05,
      "Tref": 2824.4440619141606,
      "Tref_error": 0.001867173407529362,
      "reference_cycle": 200,
      "T0": 1993.4268461048077,
      "chi2": 23.129907417426352,
      "dof": 6,
      "n": 8,
      "oc_rms_minutes": 9.344261252741365
    },
    "shape": {
      "T14": 0.1746206896551724,
      "fr": 0.25,
      "shift": 0,
      "T14_range": [
        0.17099999999999999,
        0.17824137931034484
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
      "sec": 25,
      "tc": 1991.3545809543314,
      "depth": 0.06817186660915797,
      "n": 8,
      "phase": 0.00027087831869249395,
      "threshold": 0.003,
      "duration": 0.1666685608180387
    },
    {
      "sec": 25,
      "tc": 1993.4222282637368,
      "depth": 0.004866193095847238,
      "n": 6,
      "phase": 0.4978893167745474,
      "threshold": 0.003,
      "duration": 0.12500122107360312
    },
    {
      "sec": 25,
      "tc": 1997.5703777987615,
      "depth": 0.005820996998787686,
      "n": 3,
      "phase": 0.49621997244810645,
      "threshold": 0.003,
      "duration": 0.08333323951217153
    },
    {
      "sec": 25,
      "tc": 2003.8192576645408,
      "depth": 0.06828358313446303,
      "n": 9,
      "phase": 0.00013112149295313458,
      "threshold": 0.003,
      "duration": 0.18749944249486816
    },
    {
      "sec": 25,
      "tc": 2005.8908714487056,
      "depth": 0.005259911922095628,
      "n": 7,
      "phase": 0.4987041671330088,
      "threshold": 0.003,
      "duration": 0.14583274997164608
    },
    {
      "sec": 25,
      "tc": 2007.9738392802076,
      "depth": 0.06739002967846319,
      "n": 9,
      "phase": 9.779047959845855e-06,
      "threshold": 0.003,
      "duration": 0.1874990554432543
    },
    {
      "sec": 52,
      "tc": 2724.5462623560106,
      "depth": 0.008910525870879926,
      "n": 2,
      "phase": 0.45671871073309944,
      "threshold": 0.007921310577198672,
      "duration": 0.013888984721461384
    },
    {
      "sec": 52,
      "tc": 2724.6817416361055,
      "depth": 0.014464390113563597,
      "n": 5,
      "phase": 0.48932436233397425,
      "threshold": 0.007921310577198672,
      "duration": 0.06250050317680689
    },
    {
      "sec": 52,
      "tc": 2724.7985687263413,
      "depth": 0.010666295825793815,
      "n": 2,
      "phase": 0.5174410116038928,
      "threshold": 0.007921310577198672,
      "duration": 0.020833486149285818
    },
    {
      "sec": 52,
      "tc": 2726.8097085266186,
      "depth": 0.0725688099968611,
      "n": 14,
      "phase": 0.0014598490419928112,
      "threshold": 0.007921310577198672,
      "duration": 0.1736123726607275
    },
    {
      "sec": 52,
      "tc": 2727.047188817212,
      "depth": 0.013033125626976338,
      "n": 2,
      "phase": 0.058613973360763794,
      "threshold": 0.007921310577198672,
      "duration": 0.03472246015394376
    },
    {
      "sec": 52,
      "tc": 2730.2118546374954,
      "depth": 0.01888450986639667,
      "n": 2,
      "phase": 0.8202506686330082,
      "threshold": 0.007921310577198672,
      "duration": 0.0277779200380337
    },
    {
      "sec": 52,
      "tc": 2733.1053735854216,
      "depth": 0.009968575078429298,
      "n": 2,
      "phase": 0.5166307398181402,
      "threshold": 0.007921310577198672,
      "duration": 0.02083327283912695
    },
    {
      "sec": 52,
      "tc": 2733.78624562881,
      "depth": 0.011729783507354652,
      "n": 12,
      "phase": 0.680495477038022,
      "threshold": 0.007921310577198672,
      "duration": 0.12499922913298178
    },
    {
      "sec": 52,
      "tc": 2737.701912736305,
      "depth": 0.009492797273196407,
      "n": 2,
      "phase": 0.6228748386831455,
      "threshold": 0.007921310577198672,
      "duration": 0.020833260259905728
    },
    {
      "sec": 52,
      "tc": 2737.8522275595556,
      "depth": 0.011171807896546038,
      "n": 2,
      "phase": 0.6590509443866779,
      "threshold": 0.007921310577198672,
      "duration": 0.02777764794950599
    },
    {
      "sec": 52,
      "tc": 2739.2631290627364,
      "depth": 0.06764876443190704,
      "n": 16,
      "phase": 0.9986110809893489,
      "threshold": 0.007921310577198672,
      "duration": 0.15972093200093695
    },
    {
      "sec": 79,
      "tc": 3453.9439091350832,
      "depth": 0.07144190841313858,
      "n": 78,
      "phase": 6.033989865272815e-05,
      "threshold": 0.005457160928542694,
      "duration": 0.18055673808521533
    },
    {
      "sec": 79,
      "tc": 3466.409355605094,
      "depth": 0.07056632600805846,
      "n": 78,
      "phase": 0.00010584033049099162,
      "threshold": 0.005457160928542694,
      "duration": 0.18055468258353358
    },
    {
      "sec": 79,
      "tc": 3468.488761755343,
      "depth": 0.006806137458866379,
      "n": 12,
      "phase": 0.5005542662760831,
      "threshold": 0.005457160928542694,
      "duration": 0.09722105433456818
    },
    {
      "sec": 79,
      "tc": 3470.563798915389,
      "depth": 0.07041907411587156,
      "n": 76,
      "phase": 0.9999512120814984,
      "threshold": 0.005457160928542694,
      "duration": 0.17592336994221114
    },
    {
      "sec": 79,
      "tc": 3472.6343604270855,
      "depth": 0.007716177999041229,
      "n": 10,
      "phase": 0.49827100844635197,
      "threshold": 0.005457160928542694,
      "duration": 0.09259113484540649
    },
    {
      "sec": 79,
      "tc": 3478.8740466700765,
      "depth": 0.06953830510568215,
      "n": 75,
      "phase": 0.9999695382524578,
      "threshold": 0.005457160928542694,
      "duration": 0.17360827888887798
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
    "w_tp_corr": 0.99954325,
    "gaia_comparison": [
      {
        "kind": "A",
        "epoch389_offset": -0.050723818866629244,
        "epoch389_gaia_error": 0.029651292315453718,
        "events": [
          {
            "sec": 25,
            "tc": 2003.8191449354194,
            "gaia_conjunction": 2003.8524090359804,
            "gaia_error": 0.0924896503788466,
            "offset_days": -0.033264100560927545,
            "z": -0.35955713508145565
          },
          {
            "sec": 25,
            "tc": 2007.9742265805592,
            "gaia_conjunction": 2008.0074268309302,
            "gaia_error": 0.09268099177931984,
            "offset_days": -0.03320025037101004,
            "z": -0.35813693830816684
          },
          {
            "sec": 52,
            "tc": 2726.804398913881,
            "gaia_conjunction": 2726.8301827454884,
            "gaia_error": 0.12621855787627057,
            "offset_days": -0.025783831607441243,
            "z": -0.20427220668961132
          },
          {
            "sec": 52,
            "tc": 2739.2685961251623,
            "gaia_conjunction": 2739.2952456801468,
            "gaia_error": 0.12680570587701617,
            "offset_days": -0.026649554984487622,
            "z": -0.2101587415926234
          },
          {
            "sec": 79,
            "tc": 3453.9436868133444,
            "gaia_conjunction": 3453.9628292092634,
            "gaia_error": 0.1606518869330144,
            "offset_days": -0.019142395919061528,
            "z": -0.1191538706034594
          },
          {
            "sec": 79,
            "tc": 3466.4089317487637,
            "gaia_conjunction": 3466.4279470338324,
            "gaia_error": 0.16124472619702576,
            "offset_days": -0.01901528506868999,
            "z": -0.11792748304842203
          },
          {
            "sec": 79,
            "tc": 3470.5640133939037,
            "gaia_conjunction": 3470.582984153223,
            "gaia_error": 0.16144235423102704,
            "offset_days": -0.018970759319472563,
            "z": -0.11750732660175245
          },
          {
            "sec": 79,
            "tc": 3478.874176684183,
            "gaia_conjunction": 3478.8930758495226,
            "gaia_error": 0.16183763255377026,
            "offset_days": -0.018899165339462343,
            "z": -0.11677794608146223
          }
        ]
      },
      {
        "kind": "B",
        "epoch389_offset": -2.0681860034732154,
        "epoch389_gaia_error": 0.023232828583494358,
        "events": [
          {
            "sec": 25,
            "tc": 2003.8191449354194,
            "gaia_conjunction": 2005.8674291611055,
            "gaia_error": 0.0655214022743287,
            "offset_days": -2.048284225686075,
            "z": -31.24485218244073
          },
          {
            "sec": 25,
            "tc": 2007.9742265805592,
            "gaia_conjunction": 2010.0224407615738,
            "gaia_error": 0.06571455773637068,
            "offset_days": -2.0482141810146004,
            "z": -31.15385490061456
          },
          {
            "sec": 52,
            "tc": 2726.804398913881,
            "gaia_conjunction": 2728.8448418564467,
            "gaia_error": 0.0995770964398364,
            "offset_days": -2.0404429425657327,
            "z": -20.489952802984046
          },
          {
            "sec": 52,
            "tc": 2739.2685961251623,
            "gaia_conjunction": 2741.3099513901025,
            "gaia_error": 0.10016943258039669,
            "offset_days": -2.0413552649401936,
            "z": -20.378745261893084
          },
          {
            "sec": 79,
            "tc": 3453.9436868133444,
            "gaia_conjunction": 3455.977480983518,
            "gaia_error": 0.1342727662070274,
            "offset_days": -2.033794170173678,
            "z": -15.146620934991695
          },
          {
            "sec": 79,
            "tc": 3466.4089317487637,
            "gaia_conjunction": 3468.4425773640555,
            "gaia_error": 0.1348694297963385,
            "offset_days": -2.033645615291789,
            "z": -15.078511695275889
          },
          {
            "sec": 79,
            "tc": 3470.5640133939037,
            "gaia_conjunction": 3472.5976112744706,
            "gaia_error": 0.13506832803951005,
            "offset_days": -2.0335978805669583,
            "z": -15.055954381146375
          },
          {
            "sec": 79,
            "tc": 3478.874176684183,
            "gaia_conjunction": 3480.9077008746035,
            "gaia_error": 0.13546613995878146,
            "offset_days": -2.033524190420394,
            "z": -15.011197528943105
          }
        ]
      }
    ],
    "primary_conjunction": "A",
    "predicted_secondary_phase": 0.48654805905118204,
    "secondary": {
      "n": 8,
      "depth": 0.0023126896530751635,
      "error": 0.0003176360990139147,
      "snr": 7.28094086363229,
      "scatter": 0.0008483749127974492,
      "chi2": 3.565054216423738,
      "dof": 7,
      "phase": 0.48654805905118204,
      "control_scatter": 0.006227718491983203,
      "upper_3sigma": 0.02099584512902477
    },
    "secondary_windows": {
      "gaia_other_windows": [
        {
          "status": "insufficient",
          "tc_nom": 1985.064932756897,
          "sec": 25,
          "n_in": 5,
          "cycle": -2
        },
        {
          "status": "insufficient",
          "tc_nom": 1989.2200185608342,
          "sec": 25,
          "n_in": 0,
          "cycle": -1
        },
        {
          "status": "fit",
          "sec": 25,
          "tc_nom": 1993.3751043647717,
          "tc": 1993.3751043647717,
          "tc_error": 0.002273101237654183,
          "depth": 0.0027224611858918508,
          "depth_error": 0.0008161135913535405,
          "T14": 0.1746206896551724,
          "T12": 0.0436551724137931,
          "T23": 0.0873103448275862,
          "beta": 1.2568194871377973,
          "n_in": 7,
          "flagged_core": 1,
          "flag_bits_core": 4096,
          "background_fake_depth": -3.91571445830732e-06,
          "depth_with_background": 0.0027284462152482856,
          "scan_edge": false,
          "x_template_shift_pix": -0.0008718440097274837,
          "x_err_pix": 0.0007528610926212081,
          "y_template_shift_pix": 0.0003113064862456564,
          "y_err_pix": 0.0008743862891746732,
          "cycle": 0
        },
        {
          "status": "insufficient",
          "tc_nom": 1997.530190168709,
          "sec": 25,
          "n_in": 5,
          "cycle": 1
        },
        {
          "status": "insufficient",
          "tc_nom": 2001.6852759726464,
          "sec": 25,
          "n_in": 0,
          "cycle": 2
        },
        {
          "status": "fit",
          "sec": 25,
          "tc_nom": 2005.8403617765837,
          "tc": 2005.8403617765837,
          "tc_error": 0.0021262915091884403,
          "depth": 0.0025949297836418647,
          "depth_error": 0.0008718410420660375,
          "T14": 0.1746206896551724,
          "T12": 0.0436551724137931,
          "T23": 0.0873103448275862,
          "beta": 1.276079284545038,
          "n_in": 8,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": 0.00013753321590873055,
          "depth_with_background": 0.002490103971154569,
          "scan_edge": false,
          "x_template_shift_pix": -5.194479735040915e-05,
          "x_err_pix": 0.00031587194366042407,
          "y_template_shift_pix": 1.1902773022133383e-05,
          "y_err_pix": 0.0004388593603608397,
          "cycle": 3
        },
        {
          "status": "insufficient",
          "tc_nom": 2720.5151200538103,
          "sec": 52,
          "n_in": 0,
          "cycle": 175
        },
        {
          "status": "insufficient",
          "tc_nom": 2724.6702058577475,
          "sec": 52,
          "n_in": 9,
          "cycle": 176
        },
        {
          "status": "fit",
          "sec": 52,
          "tc_nom": 2728.8252916616852,
          "tc": 2728.8252916616852,
          "tc_error": 0.0005560035082643823,
          "depth": 0.0006643123089530666,
          "depth_error": 0.0010578382780920255,
          "T14": 0.1746206896551724,
          "T12": 0.0436551724137931,
          "T23": 0.0873103448275862,
          "beta": 1.334013782628816,
          "n_in": 13,
          "flagged_core": 12,
          "flag_bits_core": 18432,
          "background_fake_depth": -0.002438109334802984,
          "depth_with_background": 0.003034467903619231,
          "scan_edge": false,
          "x_template_shift_pix": -0.0013744528527864376,
          "x_err_pix": 0.0006706524735165795,
          "y_template_shift_pix": -0.00023550379359685647,
          "y_err_pix": 0.0005101308548445859,
          "cycle": 177
        },
        {
          "status": "fit",
          "sec": 52,
          "tc_nom": 2732.9803774656225,
          "tc": 2732.9803774656225,
          "tc_error": 0.0005357783867307928,
          "depth": 0.00047815477454444616,
          "depth_error": 0.0022992452454227118,
          "T14": 0.1746206896551724,
          "T12": 0.0436551724137931,
          "T23": 0.0873103448275862,
          "beta": 1.6401641203657333,
          "n_in": 14,
          "flagged_core": 11,
          "flag_bits_core": 18432,
          "background_fake_depth": -0.0018325572073835884,
          "depth_with_background": 0.002457814243441288,
          "scan_edge": false,
          "x_template_shift_pix": 0.0012098830238278068,
          "x_err_pix": 0.0014366118079929008,
          "y_template_shift_pix": 0.001811343366696417,
          "y_err_pix": 0.0012818364211958251,
          "cycle": 178
        },
        {
          "status": "insufficient",
          "tc_nom": 2737.1354632695598,
          "sec": 52,
          "n_in": 0,
          "cycle": 179
        },
        {
          "status": "fit",
          "sec": 52,
          "tc_nom": 2741.2905490734975,
          "tc": 2741.2905490734975,
          "tc_error": 0.0005238620689655173,
          "depth": 0.0023749770310954603,
          "depth_error": 0.0013559902635811626,
          "T14": 0.1746206896551724,
          "T12": 0.0436551724137931,
          "T23": 0.0873103448275862,
          "beta": 1.2199795060254155,
          "n_in": 16,
          "flagged_core": 9,
          "flag_bits_core": 18432,
          "background_fake_depth": 0.002774809010883084,
          "depth_with_background": -0.00044139695577962335,
          "scan_edge": false,
          "x_template_shift_pix": -0.00038101413296744906,
          "x_err_pix": 0.00041626936878689326,
          "y_template_shift_pix": 0.00032904673090844905,
          "y_err_pix": 0.000368819824143079,
          "cycle": 180
        },
        {
          "status": "insufficient",
          "tc_nom": 3455.965307350724,
          "sec": 79,
          "n_in": 19,
          "cycle": 352
        },
        {
          "status": "insufficient",
          "tc_nom": 3460.1203931546615,
          "sec": 79,
          "n_in": 0,
          "cycle": 353
        },
        {
          "status": "fit",
          "sec": 79,
          "tc_nom": 3464.275478958599,
          "tc": 3464.275478958599,
          "tc_error": 0.0005238620689655173,
          "depth": 0.002491402804875252,
          "depth_error": 0.0006628061594766573,
          "T14": 0.1746206896551724,
          "T12": 0.0436551724137931,
          "T23": 0.0873103448275862,
          "beta": 2.3339289168167356,
          "n_in": 74,
          "flagged_core": 2,
          "flag_bits_core": 1073741824,
          "background_fake_depth": 0.00012027116447121783,
          "depth_with_background": 0.002386010631137162,
          "scan_edge": false,
          "x_template_shift_pix": -0.0006200548789224728,
          "x_err_pix": 0.0010341324265294013,
          "y_template_shift_pix": 0.001493211004639794,
          "y_err_pix": 0.0011165647853830936,
          "cycle": 354
        },
        {
          "status": "fit",
          "sec": 79,
          "tc_nom": 3468.430564762536,
          "tc": 3468.430564762536,
          "tc_error": 0.0005238620689655173,
          "depth": 0.0025230618452259015,
          "depth_error": 0.0008307738119576203,
          "T14": 0.1746206896551724,
          "T12": 0.0436551724137931,
          "T23": 0.0873103448275862,
          "beta": 2.8115825543702853,
          "n_in": 76,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": -0.0001681984899326476,
          "depth_with_background": 0.0024648622493831864,
          "scan_edge": false,
          "x_template_shift_pix": 0.0003145008885131958,
          "x_err_pix": 0.000689212052544097,
          "y_template_shift_pix": -3.0116659117492405e-05,
          "y_err_pix": 0.0008271671159244372,
          "cycle": 355
        },
        {
          "status": "fit",
          "sec": 79,
          "tc_nom": 3472.5856505664733,
          "tc": 3472.5856505664733,
          "tc_error": 0.0005238620689655173,
          "depth": 0.0023632087974677055,
          "depth_error": 0.0007575154521246125,
          "T14": 0.1746206896551724,
          "T12": 0.0436551724137931,
          "T23": 0.0873103448275862,
          "beta": 2.5735584230054735,
          "n_in": 76,
          "flagged_core": 0,
          "flag_bits_core": 0,
          "background_fake_depth": 0.00012389210237314096,
          "depth_with_background": 0.002110217830440336,
          "scan_edge": false,
          "x_template_shift_pix": -0.00010771640658538709,
          "x_err_pix": 0.0009937140027917847,
          "y_template_shift_pix": 0.0004946864269438694,
          "y_err_pix": 0.0009185035712629134,
          "cycle": 356
        },
        {
          "status": "insufficient",
          "tc_nom": 3476.7407363704106,
          "sec": 79,
          "n_in": 0,
          "cycle": 357
        }
      ]
    },
    "controls": [
      {
        "n": 8,
        "depth": 0.002477253609312714,
        "error": 0.003653406179499132,
        "snr": 0.6780668471011171,
        "scatter": 0.001576225025215626,
        "chi2": 0.19135775046625042,
        "dof": 7,
        "phase": 0.1
      },
      {
        "n": 9,
        "depth": -4.104173633717512e-06,
        "error": 0.00010304393613376845,
        "snr": -0.0398293561727844,
        "scatter": 0.00040258506123538087,
        "chi2": 10.098763220984974,
        "dof": 8,
        "phase": 0.15000000000000002
      },
      {
        "n": 10,
        "depth": -0.0001076447818468853,
        "error": 9.402764649294162e-05,
        "snr": -1.1448205486560368,
        "scatter": 0.0006308646907837382,
        "chi2": 14.262274028498492,
        "dof": 9,
        "phase": 0.20000000000000004
      },
      {
        "n": 9,
        "depth": -6.553189839435205e-05,
        "error": 0.00010470971835324526,
        "snr": -0.6258435169625401,
        "scatter": 0.0009756741507893345,
        "chi2": 22.569850934325537,
        "dof": 8,
        "phase": 0.25000000000000006
      },
      {
        "n": 9,
        "depth": 9.398282632759838e-05,
        "error": 0.00011084820966221819,
        "snr": 0.8478515495558044,
        "scatter": 0.0009743782028686848,
        "chi2": 11.689645567562057,
        "dof": 8,
        "phase": 0.30000000000000004
      },
      {
        "n": 8,
        "depth": -6.077518011388786e-05,
        "error": 0.00010538506229065589,
        "snr": -0.5766963437974508,
        "scatter": 0.0006560216876940536,
        "chi2": 9.195669616667741,
        "dof": 7,
        "phase": 0.3500000000000001
      },
      {
        "n": 9,
        "depth": -9.519329632408068e-05,
        "error": 0.00017361920095223423,
        "snr": -0.5482878379924699,
        "scatter": 0.0004246138292621671,
        "chi2": 2.355730455963733,
        "dof": 8,
        "phase": 0.40000000000000013
      },
      {
        "n": 8,
        "depth": -0.0015093846080010374,
        "error": 0.0003724610009069574,
        "snr": -4.052463491011477,
        "scatter": 0.0006374987053734854,
        "chi2": 2.609240500333832,
        "dof": 7,
        "phase": 0.45000000000000007
      },
      {
        "n": 9,
        "depth": 0.004500515908106974,
        "error": 0.0001136210548577903,
        "snr": 39.609876124983025,
        "scatter": 0.0006203441382529795,
        "chi2": 11.822901929922319,
        "dof": 8,
        "phase": 0.5000000000000001
      },
      {
        "n": 10,
        "depth": -0.0017979371485593524,
        "error": 0.0003423552659518343,
        "snr": -5.251670785786315,
        "scatter": 0.0009293388485321415,
        "chi2": 3.305001289255413,
        "dof": 9,
        "phase": 0.5500000000000002
      },
      {
        "n": 11,
        "depth": 0.000169189229682758,
        "error": 0.00015344559102010318,
        "snr": 1.1026007887094795,
        "scatter": 0.0013551339128769593,
        "chi2": 8.160156770153964,
        "dof": 10,
        "phase": 0.6000000000000002
      },
      {
        "n": 11,
        "depth": -0.00014758976677270422,
        "error": 0.00011539541552388142,
        "snr": -1.2789915968729286,
        "scatter": 0.0012777583348115155,
        "chi2": 28.06027263053889,
        "dof": 10,
        "phase": 0.6500000000000001
      },
      {
        "n": 12,
        "depth": 2.086703868528975e-05,
        "error": 0.00010130352218218348,
        "snr": 0.20598532248229853,
        "scatter": 0.0009437261894513522,
        "chi2": 16.914857862821965,
        "dof": 11,
        "phase": 0.7000000000000002
      },
      {
        "n": 10,
        "depth": 1.4985360174567247e-05,
        "error": 0.00011608515189726649,
        "snr": 0.12908937904331685,
        "scatter": 0.0008484932036541399,
        "chi2": 8.001202831975611,
        "dof": 9,
        "phase": 0.7500000000000002
      },
      {
        "n": 7,
        "depth": -0.00027586227629016564,
        "error": 0.00012653306483926307,
        "snr": -2.1801596020818574,
        "scatter": 0.0012412283966793316,
        "chi2": 14.003855817386057,
        "dof": 6,
        "phase": 0.8000000000000002
      },
      {
        "n": 7,
        "depth": 0.00010658733237263565,
        "error": 0.00012981724518043204,
        "snr": 0.8210568035432481,
        "scatter": 0.0006719777032895517,
        "chi2": 8.833007030067108,
        "dof": 6,
        "phase": 0.8500000000000002
      },
      {
        "n": 8,
        "depth": 0.0018760104840373625,
        "error": 0.003692964016307432,
        "snr": 0.5079958742498585,
        "scatter": 0.0022709108755789055,
        "chi2": 0.3151118884493703,
        "dof": 7,
        "phase": 0.9000000000000002
      },
      {
        "n": 7,
        "depth": -0.023675702814051243,
        "error": 0.005118383938429994,
        "snr": -4.625620723034992,
        "scatter": 0.003847766106912582,
        "chi2": 0.47502268406299086,
        "dof": 6,
        "phase": 0.9500000000000003
      },
      {
        "n": 8,
        "depth": 0.0023126896530751635,
        "error": 0.0003176360990139147,
        "snr": 7.28094086363229,
        "scatter": 0.0008483749127974492,
        "chi2": 3.565054216423738,
        "dof": 7,
        "phase": 0.48654805905118204,
        "control_scatter": 0.006227718491983203,
        "upper_3sigma": 0.02099584512902477
      }
    ],
    "physics": [
      {
        "m1": 1.158,
        "m2_min": 0.4203614553771211,
        "f_mass": 0.02981643581605501,
        "a_rsun": 12.663500430295366,
        "r1_rsun": 1.93733,
        "r2_approx_rsun": 0.4999174651828277,
        "central_T14_hours": {
          "A": 6.135964583420574,
          "B": 6.079658803383868
        },
        "observed_T14_hours": 4.190896551724138
      }
    ],
    "period_delta_sigma": 0.4076921375785401
  },
  "covariance_geometry": {
    "bit_index": 127,
    "gaia_primary": "A",
    "gaia_relative_phase_nominal": 0.48654805905118204,
    "gaia_relative_phase_quantiles_16_50_84": [
      0.47222534736181654,
      0.48582134235220953,
      0.49557544316627955
    ],
    "gaia_relative_phase_sigma": 0.011524151094510871,
    "gaia_e_cos_omega_quantiles": [
      -0.043633909117574525,
      -0.022267420832003212,
      -0.006950033058095588
    ],
    "gaia_e_sin_omega_quantiles": [
      -0.01905995057060602,
      -0.0028022506776418693,
      0.010150533444872292
    ],
    "photometric_phase": 0.4999963061696181,
    "photometric_e_cos_omega_first_order": -5.802255195693774e-06,
    "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
    "geometry_status": "conditional shape feasibility",
    "geometry_e_sin_omega_conditional_range": [
      0.1499999999999999,
      0.1499999999999999
    ],
    "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
  },
  "conditional_two_disk_geometry": {
    "status": "conditional shape feasibility",
    "best": {
      "chi2": 260.8752367177566,
      "dof": 121,
      "k": 0.27499999999999997,
      "b_A": 0.585,
      "e_sin_omega": 0.1499999999999999,
      "primary_scale": 0.8540639237871189,
      "secondary_scale": 0.004860567786284531
    },
    "profile_interval_approx_95": {
      "k": [
        0.27499999999999997,
        0.27499999999999997
      ],
      "b_A": [
        0.585,
        0.585
      ],
      "e_sin_omega": [
        0.1499999999999999,
        0.1499999999999999
      ]
    },
    "error_inflation": 2.1559936918822857,
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
  "sector": 79,
  "provenance": "TESS-SPOC",
  "fits_identity_validated": true,
  "quality_column_present": true,
  "events": [
    {
      "tc": 3453.9436868133444,
      "qlp": {
        "1": {
          "depth": 0.06625014285552046,
          "error": 0.0006871555761947051,
          "red_noise_beta": 2.5246235767824454,
          "n_core": 75,
          "baseline_degree": 1,
          "background_regressed_depth": 0.06586723725018256,
          "background_template_native_sigma": 0.5691497654383136
        },
        "2": {
          "depth": 0.06527816750133317,
          "error": 0.0006497046900345639,
          "red_noise_beta": 2.2710040580474646,
          "n_core": 75,
          "baseline_degree": 2,
          "background_regressed_depth": 0.06539414073350912,
          "background_template_native_sigma": 0.196029427259226
        }
      },
      "independent": {
        "SAP_FLUX": {
          "1": {
            "depth": 0.05237334405244819,
            "error": 0.0005751063688461142,
            "red_noise_beta": 2.705047539175303,
            "n_core": 75,
            "baseline_degree": 1,
            "background_regressed_depth": 0.051834378171313956,
            "background_template_native_sigma": 0.7182202040708827
          },
          "2": {
            "depth": 0.051506158771041366,
            "error": 0.000520766436438326,
            "red_noise_beta": 2.378051514604589,
            "n_core": 75,
            "baseline_degree": 2,
            "background_regressed_depth": 0.051478596624995064,
            "background_template_native_sigma": 0.5196255903719781
          }
        },
        "PDCSAP_FLUX": {
          "1": {
            "depth": 0.06402692334682908,
            "error": 0.0006890143929908181,
            "red_noise_beta": 2.6787088530643084,
            "n_core": 75,
            "baseline_degree": 1,
            "background_regressed_depth": 0.06381716316807365,
            "background_template_native_sigma": 0.7182202040708827
          },
          "2": {
            "depth": 0.06316046199153794,
            "error": 0.0006747938521980842,
            "red_noise_beta": 2.478188934961999,
            "n_core": 75,
            "baseline_degree": 2,
            "background_regressed_depth": 0.06341664387769931,
            "background_template_native_sigma": 0.5196255903719781
          }
        }
      }
    },
    {
      "tc": 3466.4089317487637,
      "qlp": {
        "1": {
          "depth": 0.06613379418158673,
          "error": 0.0006980839147789801,
          "red_noise_beta": 2.580722781903427,
          "n_core": 75,
          "baseline_degree": 1,
          "background_regressed_depth": 0.06629357406241825,
          "background_template_native_sigma": 0.4642373644166992
        },
        "2": {
          "depth": 0.06518774477984164,
          "error": 0.0006551619595103751,
          "red_noise_beta": 2.2976591334295424,
          "n_core": 75,
          "baseline_degree": 2,
          "background_regressed_depth": 0.06534858870394679,
          "background_template_native_sigma": 0.4706878322628785
        }
      },
      "independent": {
        "SAP_FLUX": {
          "1": {
            "depth": 0.05250985954998039,
            "error": 0.0005569592105522673,
            "red_noise_beta": 2.6371562672220095,
            "n_core": 75,
            "baseline_degree": 1,
            "background_regressed_depth": 0.052726660656831154,
            "background_template_native_sigma": 0.6771391475211138
          },
          "2": {
            "depth": 0.05167256476162197,
            "error": 0.0005004789878873599,
            "red_noise_beta": 2.2894706111721064,
            "n_core": 75,
            "baseline_degree": 2,
            "background_regressed_depth": 0.05189299642131428,
            "background_template_native_sigma": 0.7494894283336846
          }
        },
        "PDCSAP_FLUX": {
          "1": {
            "depth": 0.06287224972411876,
            "error": 0.0005744920324821767,
            "red_noise_beta": 2.4014909357092424,
            "n_core": 75,
            "baseline_degree": 1,
            "background_regressed_depth": 0.06309654472305253,
            "background_template_native_sigma": 0.6771391475211138
          },
          "2": {
            "depth": 0.06302560387800552,
            "error": 0.0006366981161436254,
            "red_noise_beta": 2.3862226398483015,
            "n_core": 75,
            "baseline_degree": 2,
            "background_regressed_depth": 0.06327811867050735,
            "background_template_native_sigma": 0.7494894283336846
          }
        }
      }
    },
    {
      "tc": 3470.5640133939037,
      "qlp": {
        "1": {
          "depth": 0.06603977509981945,
          "error": 0.0006156498992470969,
          "red_noise_beta": 2.3471414135186293,
          "n_core": 75,
          "baseline_degree": 1,
          "background_regressed_depth": 0.06599036939778437,
          "background_template_native_sigma": -0.22242883699494698
        },
        "2": {
          "depth": 0.0652593313487301,
          "error": 0.0005961181832722528,
          "red_noise_beta": 2.1217359283020683,
          "n_core": 75,
          "baseline_degree": 2,
          "background_regressed_depth": 0.06485700053269254,
          "background_template_native_sigma": -0.604221975334949
        }
      },
      "independent": {
        "SAP_FLUX": {
          "1": {
            "depth": 0.05222613340532687,
            "error": 0.00043270219413852793,
            "red_noise_beta": 2.142318300935997,
            "n_core": 75,
            "baseline_degree": 1,
            "background_regressed_depth": 0.05231764902219431,
            "background_template_native_sigma": -0.40875224639443813
          },
          "2": {
            "depth": 0.05163965421925723,
            "error": 0.0004077547674710882,
            "red_noise_beta": 1.88013762594925,
            "n_core": 75,
            "baseline_degree": 2,
            "background_regressed_depth": 0.051449746129657754,
            "background_template_native_sigma": -0.7753118907202149
          }
        },
        "PDCSAP_FLUX": {
          "1": {
            "depth": 0.0639865076934869,
            "error": 0.00052796645530098,
            "red_noise_beta": 2.1523720970012667,
            "n_core": 75,
            "baseline_degree": 1,
            "background_regressed_depth": 0.06398882241334039,
            "background_template_native_sigma": -0.40875224639443813
          },
          "2": {
            "depth": 0.06335461548571698,
            "error": 0.0005196110650956193,
            "red_noise_beta": 1.9556483127911959,
            "n_core": 75,
            "baseline_degree": 2,
            "background_regressed_depth": 0.06290514166279042,
            "background_template_native_sigma": -0.7753118907202149
          }
        }
      }
    },
    {
      "tc": 3478.874176684183,
      "qlp": {
        "1": {
          "depth": 0.06566107694930695,
          "error": 0.0005105206007748112,
          "red_noise_beta": 2.0386844991439537,
          "n_core": 75,
          "baseline_degree": 1,
          "background_regressed_depth": 0.06578083779501948,
          "background_template_native_sigma": 0.36009748733607994
        },
        "2": {
          "depth": 0.06528690661955272,
          "error": 0.0005495107942106925,
          "red_noise_beta": 1.9838583139929218,
          "n_core": 75,
          "baseline_degree": 2,
          "background_regressed_depth": 0.06535998397085267,
          "background_template_native_sigma": 0.2034200412486516
        }
      },
      "independent": {
        "SAP_FLUX": {
          "1": {
            "depth": 0.051800752535990036,
            "error": 0.00040334453286243926,
            "red_noise_beta": 2.1814885435187064,
            "n_core": 75,
            "baseline_degree": 1,
            "background_regressed_depth": 0.05191906315460262,
            "background_template_native_sigma": 0.7300655824981404
          },
          "2": {
            "depth": 0.05156509021453393,
            "error": 0.00044046368624991165,
            "red_noise_beta": 2.147683758945782,
            "n_core": 75,
            "baseline_degree": 2,
            "background_regressed_depth": 0.0516732014468369,
            "background_template_native_sigma": 0.6103135439725611
          }
        },
        "PDCSAP_FLUX": {
          "1": {
            "depth": 0.06347267530703135,
            "error": 0.0005239423543232579,
            "red_noise_beta": 2.3352990115705503,
            "n_core": 75,
            "baseline_degree": 1,
            "background_regressed_depth": 0.06360072951855512,
            "background_template_native_sigma": 0.7300655824981404
          },
          "2": {
            "depth": 0.06326622019886498,
            "error": 0.0005792545354158661,
            "red_noise_beta": 2.3193616758072775,
            "n_core": 75,
            "baseline_degree": 2,
            "background_regressed_depth": 0.06338148021229771,
            "background_template_native_sigma": 0.6103135439725611
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
    "source_id": "4559553159927952384",
    "ra": "253.5961350234577",
    "dec": "18.154378972658453",
    "phot_g_mean_mag": "13.602669",
    "bp_rp": "",
    "sep": "1.2303465376990557",
    "required_fraction_G_approx": 0.6810318632699872,
    "capable": true
  },
  {
    "source_id": "4559553159931324288",
    "ra": "253.59831598437444",
    "dec": "18.148779591793883",
    "phot_g_mean_mag": "13.260843",
    "bp_rp": "0.8950949",
    "sep": "21.774090665368163",
    "required_fraction_G_approx": 0.497092295058387,
    "capable": true
  }
]
```

Original batch difference-image receipts; old/new schema duplicates are the same events:

```json
[
  {
    "tic": "351541670",
    "sector": 79,
    "n_events": 4,
    "deficit_minus_target_arcsec": 2.88,
    "deficit_minus_light_arcsec": 2.3,
    "peak_on_target": true,
    "depth_ap3": 0.05211,
    "psf_frac_resid": 0.109,
    "n_neighbours_60": 8,
    "n_possible": 2,
    "brightest_nb": {
      "G": 13.260843,
      "sep": 21.8
    }
  }
]
```

pixel-localization.json: approximate Gaussian PRF/WCS sensitivity test; formal chi-square excludes PSF mismatch and correlated pixels. Ranking reversals explicitly prevent unique attribution.

```json
{
  "source_path": "C:\\Home\\sky\\data\\sb1-scale-c3\\vet351541670\\tesscut_s079.fits",
  "sha256": "bf7b9bef3c8a06680e86c23449742a77fdd5a5ccdac17aece0672f6541f4d534",
  "sector": 79,
  "gaia_target": {
    "source_id": "4559553159927952128",
    "ra": "253.59644046794253",
    "dec": "18.154559424767395",
    "phot_g_mean_mag": "11.056444",
    "bp_rp": "0.8017998",
    "sep": "0.0"
  },
  "target_wcs_pixel": [
    7.547478913270142,
    7.23482884650746
  ],
  "gaia_positions": [
    [
      7.547478913270142,
      7.23482884650746
    ],
    [
      7.499994630148441,
      7.19859511744191
    ],
    [
      7.935085685422372,
      6.259026669377654
    ]
  ],
  "events": [
    3453.943658417627,
    3466.408915829439,
    3470.5640016333764,
    3478.874173241251
  ],
  "calibration": {
    "sigma_pixels": 0.6500000000000001,
    "dx_pixels": -1.1102230246251565e-16,
    "dy_pixels": -1.1102230246251565e-16
  },
  "fixed_fits": [
    {
      "source_id": "4559553159927952128",
      "sep_arcsec": 0.0,
      "G": 11.056444,
      "chi2": 20466.85527099688,
      "amplitude": 191.371713823601,
      "fractional_residual": 0.12891405057101532
    },
    {
      "source_id": "4559553159927952384",
      "sep_arcsec": 1.2303465376990557,
      "G": 13.602669,
      "chi2": 23580.714889162657,
      "amplitude": 188.5390435952295,
      "fractional_residual": 0.1608051811146963
    },
    {
      "source_id": "4559553159931324288",
      "sep_arcsec": 21.774090665368163,
      "G": 13.260843,
      "chi2": 149959.11373730362,
      "amplitude": 51.45900973050062,
      "fractional_residual": 0.8739822954614346
    }
  ],
  "free_best": {
    "chi2": 18458.27730901701,
    "pixel_x": 7.547478913270135,
    "pixel_y": 7.3348288465074525,
    "distance_from_target_arcsec": 2.0999999999998433,
    "fractional_residual": 0.13512458883359657
  },
  "event_source_comparisons": [
    {
      "tc": 3453.943658417627,
      "best_source": "4559553159927952128",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        460.8970114891083,
        19746.774257409463
      ]
    },
    {
      "tc": 3466.408915829439,
      "best_source": "4559553159927952128",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        1345.3848726677134,
        45288.23410274604
      ]
    },
    {
      "tc": 3470.5640016333764,
      "best_source": "4559553159927952128",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        538.768852574688,
        27171.65621253786
      ]
    },
    {
      "tc": 3478.874173241251,
      "best_source": "4559553159927952128",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        740.6690844023706,
        34103.39599111528
      ]
    }
  ],
  "aperture_photometry": [
    {
      "tc": 3453.943658417627,
      "fits": [
        {
          "degree": 1,
          "depth": 0.05270723188585327,
          "formal_error": 0.00021796925253930632
        },
        {
          "degree": 2,
          "depth": 0.051893995831708846,
          "formal_error": 0.00022773517429588606
        }
      ],
      "n_core": 75
    },
    {
      "tc": 3466.408915829439,
      "fits": [
        {
          "degree": 1,
          "depth": 0.05268547989403746,
          "formal_error": 0.00022173776462194604
        },
        {
          "degree": 2,
          "depth": 0.05211857203253105,
          "formal_error": 0.00024035149561566968
        }
      ],
      "n_core": 75
    },
    {
      "tc": 3470.5640016333764,
      "fits": [
        {
          "degree": 1,
          "depth": 0.05245315693026103,
          "formal_error": 0.00022133674389085957
        },
        {
          "degree": 2,
          "depth": 0.05185403705549034,
          "formal_error": 0.00023894609797694744
        }
      ],
      "n_core": 75
    },
    {
      "tc": 3478.874173241251,
      "fits": [
        {
          "degree": 1,
          "depth": 0.05233318283415838,
          "formal_error": 0.00020783163770001683
        },
        {
          "degree": 2,
          "depth": 0.051852282498526636,
          "formal_error": 0.00022655366001525208
        }
      ],
      "n_core": 75
    }
  ],
  "calibration_note": "Approximate Gaussian PSFs at own Gaia cone positions; no extra empirical source.",
  "caution": "Same TESS pixels as QLP, independent aperture reduction. Approximate circular Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity."
}
```

pixel-localization-elliptical.json: approximate Gaussian PRF/WCS sensitivity test; formal chi-square excludes PSF mismatch and correlated pixels. Ranking reversals explicitly prevent unique attribution.

```json
{
  "source_path": "C:\\Home\\sky\\data\\sb1-scale-c3\\vet351541670\\tesscut_s079.fits",
  "sha256": "bf7b9bef3c8a06680e86c23449742a77fdd5a5ccdac17aece0672f6541f4d534",
  "sector": 79,
  "gaia_target": {
    "source_id": "4559553159927952128",
    "ra": "253.59644046794253",
    "dec": "18.154559424767395",
    "phot_g_mean_mag": "11.056444",
    "bp_rp": "0.8017998",
    "sep": "0.0"
  },
  "target_wcs_pixel": [
    7.547478913270142,
    7.23482884650746
  ],
  "gaia_positions": [
    [
      7.547478913270142,
      7.23482884650746
    ],
    [
      7.499994630148441,
      7.19859511744191
    ],
    [
      7.935085685422372,
      6.259026669377654
    ]
  ],
  "events": [
    3453.943658417627,
    3466.408915829439,
    3470.5640016333764,
    3478.874173241251
  ],
  "calibration": {
    "sigma_pixels": [
      0.7,
      0.7
    ],
    "dx_pixels": -0.40000000000000013,
    "dy_pixels": 0.9999999999999996
  },
  "fixed_fits": [
    {
      "source_id": "4559553159927952128",
      "sep_arcsec": 0.0,
      "G": 11.056444,
      "chi2": 136655.85044887097,
      "amplitude": 48.32902835387414,
      "fractional_residual": 0.8575905876833079
    },
    {
      "source_id": "4559553159927952384",
      "sep_arcsec": 1.2303465376990557,
      "G": 13.602669,
      "chi2": 136363.99839498865,
      "amplitude": 49.02947339655958,
      "fractional_residual": 0.8548080898385563
    },
    {
      "source_id": "4559553159931324288",
      "sep_arcsec": 21.774090665368163,
      "G": 13.260843,
      "chi2": 16864.633511947035,
      "amplitude": 167.88213266259302,
      "fractional_residual": 0.12646967485750124
    }
  ],
  "free_best": {
    "chi2": 15299.941469666783,
    "pixel_x": 7.947478913270134,
    "pixel_y": 6.334828846507456,
    "distance_from_target_arcsec": 20.68260138377182,
    "fractional_residual": 0.13469249121713409
  },
  "event_source_comparisons": [
    {
      "tc": 3453.943658417627,
      "best_source": "4559553159931324288",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        -67.25552859452364,
        -16307.41212349039
      ]
    },
    {
      "tc": 3466.408915829439,
      "best_source": "4559553159931324288",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        -53.1677275777256,
        -42936.1109721824
      ]
    },
    {
      "tc": 3470.5640016333764,
      "best_source": "4559553159931324288",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        -75.73654366018309,
        -25689.438582003204
      ]
    },
    {
      "tc": 3478.874173241251,
      "best_source": "4559553159931324288",
      "delta_chi2_neighbor_minus_target": [
        0.0,
        -49.387016793007206,
        -29966.286230769758
      ]
    }
  ],
  "aperture_photometry": [
    {
      "tc": 3453.943658417627,
      "fits": [
        {
          "degree": 1,
          "depth": 0.05270723188585327,
          "formal_error": 0.00021796925253930632
        },
        {
          "degree": 2,
          "depth": 0.051893995831708846,
          "formal_error": 0.00022773517429588606
        }
      ],
      "n_core": 75
    },
    {
      "tc": 3466.408915829439,
      "fits": [
        {
          "degree": 1,
          "depth": 0.05268547989403746,
          "formal_error": 0.00022173776462194604
        },
        {
          "degree": 2,
          "depth": 0.05211857203253105,
          "formal_error": 0.00024035149561566968
        }
      ],
      "n_core": 75
    },
    {
      "tc": 3470.5640016333764,
      "fits": [
        {
          "degree": 1,
          "depth": 0.05245315693026103,
          "formal_error": 0.00022133674389085957
        },
        {
          "degree": 2,
          "depth": 0.05185403705549034,
          "formal_error": 0.00023894609797694744
        }
      ],
      "n_core": 75
    },
    {
      "tc": 3478.874173241251,
      "fits": [
        {
          "degree": 1,
          "depth": 0.05233318283415838,
          "formal_error": 0.00020783163770001683
        },
        {
          "degree": 2,
          "depth": 0.051852282498526636,
          "formal_error": 0.00022655366001525208
        }
      ],
      "n_core": 75
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
      "id": "Gaia DR3 4559553159927952128",
      "main_id": "Gaia DR2 4559553159927952128",
      "otype": "SB*",
      "ra": "253.59644221341",
      "dec": "18.15454619226"
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
      "path": "C:\\Home\\Astra\\made\\binary-handoff-2026-10-30\\shared-full-review\\vsx\\351541670.tsv",
      "sha256": "09d47c2c55a89ce8d562cdb86910d725fa2ed2cf0138d4ca3fa715ea676dea81"
    },
    {
      "path": "C:\\Home\\Astra\\made\\binary-handoff-2026-10-30\\shared-full-review\\exofop\\351541670.json",
      "sha256": "e967ccec9f3e0089689676983919d580dd28dd762b381161fa1335f562f90f3f"
    }
  ]
}
```

One bounded Harvard multi-catalogue mirror probe timed out after batchG reported all IDIA9 requests timing out. ASAS-SN, SB9, WDS, Prsa, IJspeert and Kostov tables therefore remain unchecked in this fresh pass; failed service is not a negative match. VSX raw table sections were inspected; no target EB rows found. General web searches on the ten exact SIMBAD names plus eclipsing/binary found only unrelated results, not exact-target prior publications. This does not establish novelty or a complete bibliography.

## Predictions and deciding next check

AtBTJD4344.32880: next primary~4347.28711; other conjunction~4345.20557. Photometric extrapolations are scheduling estimates, conditional on stationary orbit. For null secondary use Gaia phase uncertainty, not the single date.

Spatially resolved eclipse photometry must distinguish the21.77arcsec neighbor and the target/1.23arcsec pair; empirical PRF/WCS calibration in a second sector is the immediate archival deciding test.

Final adjudication: **PLAUSIBLE**. The two-kind EB is secure but host unresolved: circular calibration favors target while expanded calibration moves to21.77arcsec neighbor and a large WCS shift. A capable1.23arcsec companion also remains unresolved. Ranking depends on calibration; no unique host is claimed.

Reproducibility: scripts and manifests retained in this batch. Original source audit completed before work; no source/paper edits or commits.

Lead control audit: {"median_primary_ppt": 65.26456258195196, "offphase_census_triggers": 6, "max_offphase_census_ppt": 18.88450986639667, "minimum_bg_regressed_depth_ratio": 0.969727431716339}. Census trigger centers/durations can merge broad eclipse wings, especially253923749; they are not a calibrated blind-search catalog.
