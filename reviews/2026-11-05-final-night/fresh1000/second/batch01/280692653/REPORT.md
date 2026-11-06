# Z108 TIC 280692653

Final lead verdict: P. Independent helper audit complete; see ../helper-independent-audit.md. Gaia DR3 490489564469187072; G=11.971896; queue frozen without substitution. Association: HOST_UNCERTAIN; Gaia association marginal; half-period alias unresolved.

Four narrow same-source raw events1822.75451,2922.19616,3306.99522,3636.83455 yield54.97197625d cycles0,20,27,33. Custom aperture7.28ppt and difference centroid0.101pixel favor target. The27.485988d alias lacks clean null coverage. Gaia full-period conjunction residuals3.234..6.724d are about2.7..3.0 local covariance sigma; Gaia association is not secured. Repeated eclipses remain real.

Limitations: Capable0.011relative G-flux neighbor0.63pixel away; target attribution favored but shallow event needs tighter PRF check. Unique orbit and Gaia association unresolved.

Next check: Test half-period window; improve PRF source attribution and revisit Gaia orbit association.

## Numeric evidence and provenance

Identity-audit.json verifies exact TIC FITS headers, sectors, Gaia identity and actual phot_g_mean_mag against the frozen fresh-band-next1000 population and all source SHA256 values. lead-context.json lists representative raw SAP events and quality0 coverage; lead-timing.json stores local trapezoid fits and failure flags. Independent TESScut aperture reduction and difference images share the same TESS photons. These are reduction checks, not independent observing occasions. Gaia neighbor response is a126arcsec cone queried via Heidelberg TAP; lead-neighbors.json records source pixel positions and relative G flux. G flux is an approximate contaminant capability screen, not a calibrated TESS passband or pixel-loss comparison.

```json
{
  "clock": {
    "period_d": 54.97197625000774,
    "epoch_btjd": 1822.7548362282344,
    "formal_period_error_d": 0.00024875013091668597,
    "cycles": [
      0,
      20,
      27,
      33
    ],
    "times": [
      1822.7545070231324,
      2922.196157647331,
      3306.9952160309617,
      3636.8345511541006
    ],
    "residuals": [
      -0.00032920510193434893,
      0.0017964189414669818,
      -0.002978947481551586,
      0.004498675610648206
    ],
    "duration_d": 0.13740786873942107,
    "depth_ppt": 9.089939684190504,
    "max_residual_d": 0.004498675610648206,
    "gaia_period_d": 54.8663379786091,
    "note": "Trials inferred from eclipse intervals; integer-cycle selection requires covered-window audit. Timing error includes cadence/2 and .002d floors."
  },
  "localization": {
    "tic": "280692653",
    "event": {
      "sector": 19,
      "screen_btjd": 1822.744016570617,
      "kind": "candidate",
      "n": 85,
      "cadence_d": 0.02083338397778789,
      "first_btjd": 1821.8481804513021,
      "last_btjd": 1823.6398515340773,
      "scale_sap": 1.0000762939453125,
      "noise_ppt": 0.6121795898749827,
      "source_sha256": "c49a3f292cc67e701ec7ba3d9f78ca96730af24b65ee5f7fab06d2fe2092ef75",
      "center_btjd": 1822.7545070231324,
      "center_formal_error_d": 0.001957898095665401,
      "depth_ppt": 9.77380651949231,
      "duration_d": 0.1401273432638283,
      "ingress_d": 0.06574354732180518,
      "baseline_slope_d": -0.00016976179354291008,
      "residual_rms_ppt": 0.6863904571845207,
      "fit_usable": true
    },
    "ra": 63.8439826312,
    "dec": 67.514137587,
    "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/cBa-k3cv20HG4gbY/astrocut_63.8439826312_67.514137587_11.0x11.0px.zip",
    "zip_sha256": "90651cd49f8b30384d8334e6a1f4106048d5a9cbe61155dc651c8323032779f2",
    "fits_sha256": "a4facfd86ceaeceaedeed963c225bf09b262204bb7e96b409e8785a5cf01375e",
    "target_xy": [
      5.2093419203465645,
      5.374610567624222
    ],
    "core_n": 4,
    "side_n": 16,
    "aperture_loss": 0.007276736287246566,
    "diff_peak_xy": [
      5,
      5
    ],
    "positive_diff_centroid_xy": [
      5.119003866794404,
      5.328683395200264
    ],
    "centroid_offset_pixels": 0.10134233610122195,
    "status": "measured"
  },
  "timing": [
    {
      "sector": 19,
      "screen_btjd": 1822.744016570617,
      "kind": "candidate",
      "n": 85,
      "cadence_d": 0.02083338397778789,
      "first_btjd": 1821.8481804513021,
      "last_btjd": 1823.6398515340773,
      "scale_sap": 1.0000762939453125,
      "noise_ppt": 0.6121795898749827,
      "source_sha256": "c49a3f292cc67e701ec7ba3d9f78ca96730af24b65ee5f7fab06d2fe2092ef75",
      "center_btjd": 1822.7545070231324,
      "center_formal_error_d": 0.001957898095665401,
      "depth_ppt": 9.77380651949231,
      "duration_d": 0.1401273432638283,
      "ingress_d": 0.06574354732180518,
      "baseline_slope_d": -0.00016976179354291008,
      "residual_rms_ppt": 0.6863904571845207,
      "fit_usable": true
    },
    {
      "sector": 59,
      "screen_btjd": 2922.2,
      "kind": "candidate",
      "n": 778,
      "cadence_d": 0.002314806920821866,
      "first_btjd": 2921.301369794285,
      "last_btjd": 2923.0999745444246,
      "scale_sap": 0.9999394416809082,
      "noise_ppt": 2.81510356338158,
      "source_sha256": "5762644ebc962ce610bf07780b3280b48092a2f1733fa158f0d5f48312be3239",
      "center_btjd": 2922.196157647331,
      "center_formal_error_d": 0.002377802628636438,
      "depth_ppt": 8.752469910737448,
      "duration_d": 0.1336999506981965,
      "ingress_d": 0.047287373596746514,
      "baseline_slope_d": -0.0006414034242204193,
      "residual_rms_ppt": 2.5431316421272188,
      "fit_usable": true
    },
    {
      "sector": 73,
      "screen_btjd": 3307.01,
      "kind": "candidate",
      "n": 740,
      "cadence_d": 0.0023147612587308686,
      "first_btjd": 3306.1967827797084,
      "last_btjd": 3307.9097061054877,
      "scale_sap": 0.999628484249115,
      "noise_ppt": 2.339974985366078,
      "source_sha256": "1902c49ebc490ad3cae4a7634dd810445196929b295cad98718fce2ed7397031",
      "center_btjd": 3306.9952160309617,
      "center_formal_error_d": 0.0021058901864573405,
      "depth_ppt": 8.733902074766135,
      "duration_d": 0.13468839421501383,
      "ingress_d": 0.05329570701189945,
      "baseline_slope_d": 0.00012644499747064904,
      "residual_rms_ppt": 2.3313429271484867,
      "fit_usable": true
    },
    {
      "sector": 86,
      "screen_btjd": 3636.74,
      "kind": "candidate",
      "n": 399,
      "cadence_d": 0.0023148442073761544,
      "first_btjd": 3636.5055048386253,
      "last_btjd": 3637.449961314581,
      "scale_sap": 1.0014780759811401,
      "noise_ppt": 3.8627689275819708,
      "source_sha256": "f95f79ccf1fc05a4ecc46566e11dec45f39079463180bf34c18aae5c4a6166ac",
      "center_btjd": 3636.8345511541006,
      "center_formal_error_d": 0.0035496844366709073,
      "depth_ppt": 9.427409457643563,
      "duration_d": 0.15673265150618781,
      "ingress_d": 0.06524712833431798,
      "baseline_slope_d": 0.0027175744591887837,
      "residual_rms_ppt": 2.984290879495494,
      "fit_usable": true
    }
  ],
  "gaia_geometry": {
    "source_id": "490489564469187072",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 54.8663379786091,
    "gaia_period_error_d": 0.045257572,
    "eccentricity": 0.5342255646353845,
    "omega_deg": 221.29614951030007,
    "tp_btjd": 390.9183358965478,
    "mass_function_solar": 0.08411405085954862,
    "events": [
      {
        "sector": 19,
        "event_kind": "candidate",
        "observed_btjd": 1822.7545070231324,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 25,
            "predicted_btjd": 1806.5961717517962,
            "offset_d": 16.158335271336227,
            "phase_offset": 0.29450362219610726,
            "linear_covariance_sigma_d": 1.6023654908087692
          },
          {
            "kind": 1,
            "cycle": 26,
            "predicted_btjd": 1819.5208992627495,
            "offset_d": 3.233607760382938,
            "phase_offset": 0.05893609596550136,
            "linear_covariance_sigma_d": 1.0785563994027112
          }
        ]
      },
      {
        "sector": 59,
        "event_kind": "candidate",
        "observed_btjd": 2922.196157647331,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 45,
            "predicted_btjd": 2903.9229313239784,
            "offset_d": 18.273226323352446,
            "phase_offset": 0.33304986256740304,
            "linear_covariance_sigma_d": 2.455100446742681
          },
          {
            "kind": 1,
            "cycle": 46,
            "predicted_btjd": 2916.8476588349313,
            "offset_d": 5.348498812399612,
            "phase_offset": 0.09748233633680539,
            "linear_covariance_sigma_d": 1.9334581831794397
          }
        ]
      },
      {
        "sector": 73,
        "event_kind": "candidate",
        "observed_btjd": 3306.9952160309617,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 52,
            "predicted_btjd": 3287.987297174242,
            "offset_d": 19.007918856719698,
            "phase_offset": 0.3464404506845412,
            "linear_covariance_sigma_d": 2.761451990697092
          },
          {
            "kind": 1,
            "cycle": 53,
            "predicted_btjd": 3300.912024685195,
            "offset_d": 6.083191345766863,
            "phase_offset": 0.11087292445394359,
            "linear_covariance_sigma_d": 2.2420127617002885
          }
        ]
      },
      {
        "sector": 86,
        "event_kind": "candidate",
        "observed_btjd": 3636.8345511541006,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 58,
            "predicted_btjd": 3617.1853250458967,
            "offset_d": 19.649226108203948,
            "phase_offset": 0.3581289882307189,
            "linear_covariance_sigma_d": 3.025752713749445
          },
          {
            "kind": 1,
            "cycle": 59,
            "predicted_btjd": 3630.1100525568495,
            "offset_d": 6.724498597251113,
            "phase_offset": 0.12256146200012133,
            "linear_covariance_sigma_d": 2.508125534401213
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
