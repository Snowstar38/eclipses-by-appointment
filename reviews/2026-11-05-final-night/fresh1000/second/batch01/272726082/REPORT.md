# Z106 TIC 272726082

Final lead verdict: C. Independent helper audit complete; see ../helper-independent-audit.md. Gaia DR3 2017370499986557056; G=11.626051; queue frozen without substitution. Association: consistent with Gaia-selected orbit.

Three deep same-kind raw events1805.31423,2885.69551,3605.94892 yield45.01584602d cycles0,24,40. Shallow opposite conjunction repeats2869.13291,3589.39022,3634.40397 with its own same-kind clock45.01600502d and cycles0,16,17. Consecutive S84/S85 shallow events reject otherwise viable90.0317/72.0254/60.0212/36.0127d primary integer aliases (9..45d residuals), without mixing conjunction kinds. Tested divisors2..6 show covered nulls. Custom aperture recovers98.45ppt; target positive centroid0.283pixel and Gaussian0.156pixel. Source-specific conjunction residuals0.527..1.163d fit covariance0.948..2.370d.

Limitations: Cadence-floor local formal timing errors; representative-event review, not all-event precision modeling.

Next check: Additional well-sampled eclipses can refine period and stellar geometry.

## Numeric evidence and provenance

Identity-audit.json verifies exact TIC FITS headers, sectors, Gaia identity and actual phot_g_mean_mag against the frozen fresh-band-next1000 population and all source SHA256 values. lead-context.json lists representative raw SAP events and quality0 coverage; lead-timing.json stores local trapezoid fits and failure flags. Independent TESScut aperture reduction and difference images share the same TESS photons. These are reduction checks, not independent observing occasions. Gaia neighbor response is a126arcsec cone queried via Heidelberg TAP; lead-neighbors.json records source pixel positions and relative G flux. G flux is an approximate contaminant capability screen, not a calibrated TESS passband or pixel-loss comparison.

```json
{
  "clock": {
    "period_d": 45.01584602398308,
    "epoch_btjd": 1805.3151271198656,
    "formal_period_error_d": 0.00015566827897662574,
    "cycles": [
      0,
      24,
      40
    ],
    "times": [
      1805.314225301031,
      2885.6955148099664,
      3605.9489182104935
    ],
    "residuals": [
      -0.0009018188345635281,
      8.31145071060746e-05,
      -4.986869544154615e-05
    ],
    "duration_d": 0.4852371004813879,
    "depth_ppt": 92.0600666650448,
    "max_residual_d": 0.0009018188345635281,
    "gaia_period_d": 45.03174722684649,
    "note": "Trials inferred from eclipse intervals; integer-cycle selection requires covered-window audit. Timing error includes cadence/2 and .002d floors."
  },
  "localization": {
    "tic": "272726082",
    "event": {
      "sector": 84,
      "screen_btjd": 3605.949176019427,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.002314835528295589,
      "first_btjd": 3605.0510195366746,
      "last_btjd": 3606.84733186555,
      "scale_sap": 1.0005208253860474,
      "noise_ppt": 2.069780984744835,
      "source_sha256": "fa6170a5d39d4e1cde0003e1d095a1aab944b967c20cf39e5333d29320a2723f",
      "center_btjd": 3605.9489182104935,
      "center_formal_error_d": 0.00025486946209761117,
      "depth_ppt": 92.64871067083178,
      "duration_d": 0.48391961331144656,
      "ingress_d": 0.11088456655027594,
      "baseline_slope_d": 5.85803460018721e-05,
      "residual_rms_ppt": 2.335323682755648,
      "fit_usable": true
    },
    "ra": 356.610059105,
    "dec": 64.8142600176,
    "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/n_-EiP-9qeAlEcXV/astrocut_356.610059105_64.8142600176_11.0x11.0px.zip",
    "zip_sha256": "4ea5f1edf5fd26e347aa0f939a4d6bc5dcd9629d88406c4feea890161be78b40",
    "fits_sha256": "bdaed43ae6899347d9f4d0eb691e4f395cb900780f8a8ba2091346f93d4b03ec",
    "target_xy": [
      5.273039613752976,
      5.3253221287833945
    ],
    "core_n": 105,
    "side_n": 524,
    "aperture_loss": 0.09845006986881233,
    "diff_peak_xy": [
      5,
      5
    ],
    "positive_diff_centroid_xy": [
      5.068817012375864,
      5.521622778720539
    ],
    "centroid_offset_pixels": 0.283268099296374,
    "status": "measured"
  },
  "timing": [
    {
      "sector": 18,
      "screen_btjd": 1805.3471332118274,
      "kind": "candidate",
      "n": 86,
      "cadence_d": 0.020832972607649936,
      "first_btjd": 1804.4513148477033,
      "last_btjd": 1806.2429505038388,
      "scale_sap": 0.9993073046207428,
      "noise_ppt": 0.6688486411860131,
      "source_sha256": "97aa37c172fab9a42460204363c5f056410a672bffbb88ea30a43c270ac3d9d2",
      "center_btjd": 1805.314225301031,
      "center_formal_error_d": 0.0002469128013037351,
      "depth_ppt": 91.75613548044049,
      "duration_d": 0.489028753566099,
      "ingress_d": 0.1161673333465668,
      "baseline_slope_d": 0.0002508115296738843,
      "residual_rms_ppt": 1.2570318262876075,
      "fit_usable": true
    },
    {
      "sector": 57,
      "screen_btjd": 2869.129074621442,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.002314845039109059,
      "first_btjd": 2868.2309145439317,
      "last_btjd": 2870.0272342404332,
      "scale_sap": 1.000876009464264,
      "noise_ppt": 2.0911637465010524,
      "source_sha256": "85a0f1b28e5e4f63d829e432cc9664ef7751e4b56457e3a7f5900e641b7a3f7d",
      "center_btjd": 2869.1329143011494,
      "center_formal_error_d": 0.001862705360442272,
      "depth_ppt": 11.695840103517291,
      "duration_d": 0.513898629980883,
      "ingress_d": 0.09180530651627289,
      "baseline_slope_d": -0.0006003633580681312,
      "residual_rms_ppt": 2.083720278850013,
      "fit_usable": true
    },
    {
      "sector": 58,
      "screen_btjd": 2885.689351156649,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.002314810225925612,
      "first_btjd": 2884.791204444835,
      "last_btjd": 2886.587497167993,
      "scale_sap": 0.9997981190681458,
      "noise_ppt": 1.9857178465334742,
      "source_sha256": "a6113c05bf94d9377aa8f3dc8a91481060283136a531f592cd4f64b116726236",
      "center_btjd": 2885.6955148099664,
      "center_formal_error_d": 0.00024645213811260824,
      "depth_ppt": 92.0600666650448,
      "duration_d": 0.4852371004813879,
      "ingress_d": 0.11160885155183926,
      "baseline_slope_d": 8.827567874514778e-05,
      "residual_rms_ppt": 2.3406991904323626,
      "fit_usable": true
    },
    {
      "sector": 84,
      "screen_btjd": 3605.949176019427,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.002314835528295589,
      "first_btjd": 3605.0510195366746,
      "last_btjd": 3606.84733186555,
      "scale_sap": 1.0005208253860474,
      "noise_ppt": 2.069780984744835,
      "source_sha256": "fa6170a5d39d4e1cde0003e1d095a1aab944b967c20cf39e5333d29320a2723f",
      "center_btjd": 3605.9489182104935,
      "center_formal_error_d": 0.00025486946209761117,
      "depth_ppt": 92.64871067083178,
      "duration_d": 0.48391961331144656,
      "ingress_d": 0.11088456655027594,
      "baseline_slope_d": 5.85803460018721e-05,
      "residual_rms_ppt": 2.335323682755648,
      "fit_usable": true
    },
    {
      "sector": 84,
      "screen_btjd": 3589.4280944173056,
      "kind": "candidate",
      "n": 757,
      "cadence_d": 0.0023148669638430874,
      "first_btjd": 3588.5299259247204,
      "last_btjd": 3590.3262626067767,
      "scale_sap": 0.9999145865440369,
      "noise_ppt": 2.110540569105019,
      "source_sha256": "fa6170a5d39d4e1cde0003e1d095a1aab944b967c20cf39e5333d29320a2723f",
      "center_btjd": 3589.3902246557254,
      "center_formal_error_d": 0.0019409104276780229,
      "depth_ppt": 11.674729847885557,
      "duration_d": 0.5170818123571214,
      "ingress_d": 0.09862570387582272,
      "baseline_slope_d": -0.00032328418359964766,
      "residual_rms_ppt": 2.042275631543155,
      "fit_usable": true
    },
    {
      "sector": 85,
      "screen_btjd": 3634.3980859807875,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.002314773366379086,
      "first_btjd": 3633.4999532990473,
      "last_btjd": 3635.296217176816,
      "scale_sap": 1.0000062882900238,
      "noise_ppt": 2.0951033274292636,
      "source_sha256": "ec0bbf633c048cb8f21e8d480ec3d1feecbe7e6e26b997c2b426e57dc98b7910",
      "center_btjd": 3634.403974531128,
      "center_formal_error_d": 0.0020308784591888582,
      "depth_ppt": 11.189608522646285,
      "duration_d": 0.5265870535501659,
      "ingress_d": 0.1007754129127907,
      "baseline_slope_d": -0.0001516915444976394,
      "residual_rms_ppt": 2.0220965669279014,
      "fit_usable": true
    }
  ],
  "gaia_geometry": {
    "source_id": "2017370499986557056",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 45.03174722684649,
    "gaia_period_error_d": 0.03132961,
    "eccentricity": 0.21422047006298106,
    "omega_deg": 17.39129612708464,
    "tp_btjd": 403.55101153310284,
    "mass_function_solar": 0.04537242835624868,
    "events": [
      {
        "sector": 18,
        "event_kind": "candidate",
        "observed_btjd": 1805.314225301031,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 31,
            "predicted_btjd": 1805.8416002237811,
            "offset_d": -0.5273749227501412,
            "phase_offset": -0.011711180560982921,
            "linear_covariance_sigma_d": 0.9477884648543182
          },
          {
            "kind": 1,
            "cycle": 30,
            "predicted_btjd": 1789.156992383979,
            "offset_d": 16.157232917051942,
            "phase_offset": 0.35879649163200833,
            "linear_covariance_sigma_d": 1.1347649795635686
          }
        ]
      },
      {
        "sector": 57,
        "event_kind": "candidate",
        "observed_btjd": 2869.1329143011494,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 55,
            "predicted_btjd": 2886.603533668097,
            "offset_d": -17.47061936694763,
            "phase_offset": -0.38796228089795737,
            "linear_covariance_sigma_d": 1.6595617282951507
          },
          {
            "kind": 1,
            "cycle": 54,
            "predicted_btjd": 2869.918925828295,
            "offset_d": -0.786011527145547,
            "phase_offset": -0.017454608704966082,
            "linear_covariance_sigma_d": 1.849818445265023
          }
        ]
      },
      {
        "sector": 58,
        "event_kind": "candidate",
        "observed_btjd": 2885.6955148099664,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 55,
            "predicted_btjd": 2886.603533668097,
            "offset_d": -0.9080188581306174,
            "phase_offset": -0.020163971288000248,
            "linear_covariance_sigma_d": 1.6595617282951507
          },
          {
            "kind": 1,
            "cycle": 54,
            "predicted_btjd": 2869.918925828295,
            "offset_d": 15.776588981671466,
            "phase_offset": 0.350343700904991,
            "linear_covariance_sigma_d": 1.849818445265023
          }
        ]
      },
      {
        "sector": 84,
        "event_kind": "candidate",
        "observed_btjd": 3605.9489182104935,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 71,
            "predicted_btjd": 3607.1114892976407,
            "offset_d": -1.162571087147171,
            "phase_offset": -0.025816699522910876,
            "linear_covariance_sigma_d": 2.1493165604402367
          },
          {
            "kind": 1,
            "cycle": 70,
            "predicted_btjd": 3590.4268814578386,
            "offset_d": 15.522036752654913,
            "phase_offset": 0.3446909726700804,
            "linear_covariance_sigma_d": 2.339396193843178
          }
        ]
      },
      {
        "sector": 84,
        "event_kind": "candidate",
        "observed_btjd": 3589.3902246557254,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 71,
            "predicted_btjd": 3607.1114892976407,
            "offset_d": -17.72126464191524,
            "phase_offset": -0.3935282491404284,
            "linear_covariance_sigma_d": 2.1493165604402367
          },
          {
            "kind": 1,
            "cycle": 70,
            "predicted_btjd": 3590.4268814578386,
            "offset_d": -1.036656802113157,
            "phase_offset": -0.023020576947437102,
            "linear_covariance_sigma_d": 2.339396193843178
          }
        ]
      },
      {
        "sector": 85,
        "event_kind": "candidate",
        "observed_btjd": 3634.403974531128,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 72,
            "predicted_btjd": 3652.1432365244873,
            "offset_d": -17.739261993359378,
            "phase_offset": -0.3939279083265016,
            "linear_covariance_sigma_d": 2.1801001045011295
          },
          {
            "kind": 1,
            "cycle": 71,
            "predicted_btjd": 3635.458628684685,
            "offset_d": -1.0546541535572942,
            "phase_offset": -0.02342023613351034,
            "linear_covariance_sigma_d": 2.3701571589609176
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
