# Z104 TIC 258216510

Final lead verdict: REFUTED. Independent helper audit complete; see ../helper-independent-audit.md. Gaia DR3 1757749833003161472; G=11.759831; queue frozen without substitution. Association: off-target repeated eclipse; no target by-catch claim.

Same-kind narrow raw events yield4.12434657d. One event at2823.51459 belongs to the other conjunction and was excluded from this same-kind fit. Dominant difference source is the bright object at cutout edge; Gaussian center(2.897,10.000) is4.994pixels from intended target(5.50,5.74). Difference light resides far from target, so this is positive contamination.

Limitations: Edge source centroid is truncated by11pixel cutout; true contaminant not assigned.

Next check: Larger cutout and separate source identification if contaminant science is desired.

## Numeric evidence and provenance

Identity-audit.json verifies exact TIC FITS headers, sectors, Gaia identity and actual phot_g_mean_mag against the frozen fresh-band-next1000 population and all source SHA256 values. lead-context.json lists representative raw SAP events and quality0 coverage; lead-timing.json stores local trapezoid fits and failure flags. Independent TESScut aperture reduction and difference images share the same TESS photons. These are reduction checks, not independent observing occasions. Gaia neighbor response is a126arcsec cone queried via Heidelberg TAP; lead-neighbors.json records source pixel positions and relative G flux. G flux is an approximate contaminant capability screen, not a calibrated TESS passband or pixel-loss comparison.

```json
{
  "clock": {
    "period_d": 4.124346572846539,
    "epoch_btjd": 2813.7045186694704,
    "formal_period_error_d": 1.258195797320604e-05,
    "cycles": [
      0,
      1,
      -1,
      175,
      180,
      178,
      179
    ],
    "times": [
      2813.7044969597173,
      2817.8278579308803,
      2809.5812168021916,
      3535.4649916552285,
      3556.087798767335,
      3547.838204572096,
      3551.9618343584934
    ],
    "residuals": [
      -2.170975312765222e-05,
      -0.001007311436751479,
      0.001044705567892379,
      -0.00017726238638715586,
      0.0008969854875431338,
      -4.0640584302309435e-06,
      -0.0007208505076050642
    ],
    "duration_d": 0.17258239920618298,
    "depth_ppt": 21.680842610173954,
    "max_residual_d": 0.001044705567892379,
    "gaia_period_d": 43.25892740123845,
    "note": "Trials inferred from eclipse intervals; integer-cycle selection requires covered-window audit. Timing error includes cadence/2 and .002d floors."
  },
  "localization": {
    "tic": "258216510",
    "event": {
      "sector": 55,
      "screen_btjd": 2809.591866042023,
      "kind": "candidate",
      "n": 83,
      "cadence_d": 0.006944424229686774,
      "first_btjd": 2809.1682561674565,
      "last_btjd": 2809.9251983827944,
      "scale_sap": 1.000868797302246,
      "noise_ppt": 2.0,
      "source_sha256": "57755ae17ef28319869d669c43fac07ba4b033ec61501bd470c88994c55c54c1",
      "center_btjd": 2809.5812168021916,
      "center_formal_error_d": 0.0016252673558537758,
      "depth_ppt": 26.65151116788146,
      "duration_d": 0.18171943274500355,
      "ingress_d": 0.08856469968250778,
      "baseline_slope_d": 0.00023487977006221754,
      "residual_rms_ppt": 1.0567100375776923,
      "fit_usable": true
    },
    "ra": 314.152300161,
    "dec": 11.9040009588,
    "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/_L1iWg5fE0OWJWhX/astrocut_314.152300161_11.9040009588_11.0x11.0px.zip",
    "zip_sha256": "239ff6524ec097530758e670f0c1c3b07e34f6f4f3cc650218f656dcdb4ed6a2",
    "fits_sha256": "e7ab8de84e249662b1971a0eb6d7cb1806e6f688a84bf91bc88de7fae0569fe1",
    "target_xy": [
      5.499811483135698,
      5.738001652737662
    ],
    "core_n": 13,
    "side_n": 64,
    "aperture_loss": 0.0035297310465758347,
    "diff_peak_xy": [
      3,
      10
    ],
    "positive_diff_centroid_xy": [
      4.68187559086064,
      6.77301525730075
    ],
    "centroid_offset_pixels": 1.3191938013432563,
    "status": "measured"
  },
  "timing": [
    {
      "sector": 55,
      "screen_btjd": 2813.689045305623,
      "kind": "candidate",
      "n": 198,
      "cadence_d": 0.00694433247372217,
      "first_btjd": 2812.7932262268337,
      "last_btjd": 2814.5848631942476,
      "scale_sap": 0.9991189241409302,
      "noise_ppt": 0.911808118081333,
      "source_sha256": "57755ae17ef28319869d669c43fac07ba4b033ec61501bd470c88994c55c54c1",
      "center_btjd": 2813.7044969597173,
      "center_formal_error_d": 0.0006363787672102916,
      "depth_ppt": 25.746841118714855,
      "duration_d": 0.17258239920618298,
      "ingress_d": 0.07811362241735613,
      "baseline_slope_d": 0.00027622496164543363,
      "residual_rms_ppt": 1.0940868679725795,
      "fit_usable": true
    },
    {
      "sector": 55,
      "screen_btjd": 2817.827855144713,
      "kind": "candidate",
      "n": 193,
      "cadence_d": 0.0069442988406080985,
      "first_btjd": 2816.9320404606283,
      "last_btjd": 2818.7236691063717,
      "scale_sap": 1.0000406503677368,
      "noise_ppt": 1.549060436533962,
      "source_sha256": "57755ae17ef28319869d669c43fac07ba4b033ec61501bd470c88994c55c54c1",
      "center_btjd": 2817.8278579308803,
      "center_formal_error_d": 0.0012238953423585306,
      "depth_ppt": 25.384903673702503,
      "duration_d": 0.1768382985861569,
      "ingress_d": 0.07645158319400988,
      "baseline_slope_d": 0.0010125848159813753,
      "residual_rms_ppt": 1.1309384498196782,
      "fit_usable": true
    },
    {
      "sector": 55,
      "screen_btjd": 2809.591866042023,
      "kind": "candidate",
      "n": 83,
      "cadence_d": 0.006944424229686774,
      "first_btjd": 2809.1682561674565,
      "last_btjd": 2809.9251983827944,
      "scale_sap": 1.000868797302246,
      "noise_ppt": 2.0,
      "source_sha256": "57755ae17ef28319869d669c43fac07ba4b033ec61501bd470c88994c55c54c1",
      "center_btjd": 2809.5812168021916,
      "center_formal_error_d": 0.0016252673558537758,
      "depth_ppt": 26.65151116788146,
      "duration_d": 0.18171943274500355,
      "ingress_d": 0.08856469968250778,
      "baseline_slope_d": 0.00023487977006221754,
      "residual_rms_ppt": 1.0567100375776923,
      "fit_usable": true
    },
    {
      "sector": 55,
      "screen_btjd": 2823.529113608421,
      "kind": "candidate",
      "n": 125,
      "cadence_d": 0.006944283560642361,
      "first_btjd": 2823.1055123092215,
      "last_btjd": 2824.2235417768193,
      "scale_sap": 1.0018020868301392,
      "noise_ppt": 1.1705584130847042,
      "source_sha256": "57755ae17ef28319869d669c43fac07ba4b033ec61501bd470c88994c55c54c1",
      "center_btjd": 2823.51458783494,
      "center_formal_error_d": 0.0014111749938265127,
      "depth_ppt": 22.712485263653875,
      "duration_d": 0.32915322961499255,
      "ingress_d": 0.14307703222917437,
      "baseline_slope_d": 0.0009642070730479553,
      "residual_rms_ppt": 1.3001161650881539,
      "fit_usable": true
    },
    {
      "sector": 82,
      "screen_btjd": 3535.4628891727903,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.002314813437351404,
      "first_btjd": 3534.5647404985825,
      "last_btjd": 3536.3610358304704,
      "scale_sap": 1.0008360147476196,
      "noise_ppt": 2.169786630435105,
      "source_sha256": "5c99ad218c48b36580f69c61ead3759164c9b87d946801c6c9df7cd312a8f842",
      "center_btjd": 3535.4649916552285,
      "center_formal_error_d": 0.0009433076503990607,
      "depth_ppt": 21.680842610173954,
      "duration_d": 0.16624142995044702,
      "ingress_d": 0.07654766086760689,
      "baseline_slope_d": 6.943576531272782e-05,
      "residual_rms_ppt": 1.922152088210175,
      "fit_usable": true
    },
    {
      "sector": 82,
      "screen_btjd": 3556.0898629799462,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.002314740348765554,
      "first_btjd": 3555.191743259253,
      "last_btjd": 3556.9879818909967,
      "scale_sap": 1.0003482699394226,
      "noise_ppt": 2.123759834247109,
      "source_sha256": "5c99ad218c48b36580f69c61ead3759164c9b87d946801c6c9df7cd312a8f842",
      "center_btjd": 3556.087798767335,
      "center_formal_error_d": 0.0009746506211913757,
      "depth_ppt": 20.942169821436135,
      "duration_d": 0.17296557128234585,
      "ingress_d": 0.07978898014980973,
      "baseline_slope_d": 9.385146949646114e-05,
      "residual_rms_ppt": 1.9823475826034491,
      "fit_usable": true
    },
    {
      "sector": 82,
      "screen_btjd": 3547.833132783302,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.0023147733486439392,
      "first_btjd": 3546.934999575192,
      "last_btjd": 3548.731263769808,
      "scale_sap": 1.0004016160964966,
      "noise_ppt": 2.0142886354431493,
      "source_sha256": "5c99ad218c48b36580f69c61ead3759164c9b87d946801c6c9df7cd312a8f842",
      "center_btjd": 3547.838204572096,
      "center_formal_error_d": 0.0009433959332339601,
      "depth_ppt": 19.58234687975285,
      "duration_d": 0.1640620041372901,
      "ingress_d": 0.07217654395748768,
      "baseline_slope_d": -0.000140930598213437,
      "residual_rms_ppt": 1.9067097403621354,
      "fit_usable": true
    },
    {
      "sector": 82,
      "screen_btjd": 3551.9580401190865,
      "kind": "candidate",
      "n": 682,
      "cadence_d": 0.0023147543356571987,
      "first_btjd": 3551.0599149050577,
      "last_btjd": 3552.856163979683,
      "scale_sap": 1.0001506209373474,
      "noise_ppt": 1.8181566606831738,
      "source_sha256": "5c99ad218c48b36580f69c61ead3759164c9b87d946801c6c9df7cd312a8f842",
      "center_btjd": 3551.9618343584934,
      "center_formal_error_d": 0.0008368388643788568,
      "depth_ppt": 19.86643669911565,
      "duration_d": 0.16584171006237838,
      "ingress_d": 0.07311740008673134,
      "baseline_slope_d": 0.0003299409678343831,
      "residual_rms_ppt": 1.9445430368195342,
      "fit_usable": true
    }
  ],
  "gaia_geometry": {
    "source_id": "1757749833003161472",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 43.25892740123845,
    "gaia_period_error_d": 0.015386137,
    "eccentricity": 0.4156451754723433,
    "omega_deg": 0.6775672182946119,
    "tp_btjd": 377.17460885083364,
    "mass_function_solar": 0.14196262879193647,
    "events": [
      {
        "sector": 55,
        "event_kind": "candidate",
        "observed_btjd": 2813.7044969597173,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 56,
            "predicted_btjd": 2804.8743408558585,
            "offset_d": 8.830156103858826,
            "phase_offset": 0.20412332515683293,
            "linear_covariance_sigma_d": 0.9271826484421949
          },
          {
            "kind": 1,
            "cycle": 55,
            "predicted_btjd": 2794.352224175576,
            "offset_d": 19.352272784141405,
            "phase_offset": 0.44735905272555077,
            "linear_covariance_sigma_d": 0.8192586561675957
          }
        ]
      },
      {
        "sector": 55,
        "event_kind": "candidate",
        "observed_btjd": 2817.8278579308803,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 56,
            "predicted_btjd": 2804.8743408558585,
            "offset_d": 12.953517075021864,
            "phase_offset": 0.2994414760882633,
            "linear_covariance_sigma_d": 0.9271826484421949
          },
          {
            "kind": 1,
            "cycle": 56,
            "predicted_btjd": 2837.6111515768143,
            "offset_d": -19.78329364593401,
            "phase_offset": -0.4573227963430188,
            "linear_covariance_sigma_d": 0.8333348243252868
          }
        ]
      },
      {
        "sector": 55,
        "event_kind": "candidate",
        "observed_btjd": 2809.5812168021916,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 56,
            "predicted_btjd": 2804.8743408558585,
            "offset_d": 4.706875946333184,
            "phase_offset": 0.10880704236320089,
            "linear_covariance_sigma_d": 0.9271826484421949
          },
          {
            "kind": 1,
            "cycle": 55,
            "predicted_btjd": 2794.352224175576,
            "offset_d": 15.228992626615764,
            "phase_offset": 0.35204276993191874,
            "linear_covariance_sigma_d": 0.8192586561675957
          }
        ]
      },
      {
        "sector": 55,
        "event_kind": "candidate",
        "observed_btjd": 2823.51458783494,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 56,
            "predicted_btjd": 2804.8743408558585,
            "offset_d": 18.64024697908144,
            "phase_offset": 0.43089942582690555,
            "linear_covariance_sigma_d": 0.9271826484421949
          },
          {
            "kind": 1,
            "cycle": 56,
            "predicted_btjd": 2837.6111515768143,
            "offset_d": -14.096563741874434,
            "phase_offset": -0.32586484660437665,
            "linear_covariance_sigma_d": 0.8333348243252868
          }
        ]
      },
      {
        "sector": 82,
        "event_kind": "candidate",
        "observed_btjd": 3535.4649916552285,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 73,
            "predicted_btjd": 3540.276106676912,
            "offset_d": -4.81111502168369,
            "phase_offset": -0.11121669700821,
            "linear_covariance_sigma_d": 1.1803072313344782
          },
          {
            "kind": 1,
            "cycle": 72,
            "predicted_btjd": 3529.7539899966296,
            "offset_d": 5.711001658598889,
            "phase_offset": 0.13201903056050782,
            "linear_covariance_sigma_d": 1.0635004554888754
          }
        ]
      },
      {
        "sector": 82,
        "event_kind": "candidate",
        "observed_btjd": 3556.087798767335,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 73,
            "predicted_btjd": 3540.276106676912,
            "offset_d": 15.811692090422639,
            "phase_offset": 0.3655128095009117,
            "linear_covariance_sigma_d": 1.1803072313344782
          },
          {
            "kind": 1,
            "cycle": 73,
            "predicted_btjd": 3573.012917397868,
            "offset_d": -16.925118630533234,
            "phase_offset": -0.3912514629303705,
            "linear_covariance_sigma_d": 1.078120741553754
          }
        ]
      },
      {
        "sector": 82,
        "event_kind": "candidate",
        "observed_btjd": 3547.838204572096,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 73,
            "predicted_btjd": 3540.276106676912,
            "offset_d": 7.562097895183797,
            "phase_offset": 0.17481011087129505,
            "linear_covariance_sigma_d": 1.1803072313344782
          },
          {
            "kind": 1,
            "cycle": 72,
            "predicted_btjd": 3529.7539899966296,
            "offset_d": 18.084214575466376,
            "phase_offset": 0.41804583844001286,
            "linear_covariance_sigma_d": 1.0635004554888754
          }
        ]
      },
      {
        "sector": 82,
        "event_kind": "candidate",
        "observed_btjd": 3551.9618343584934,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 73,
            "predicted_btjd": 3540.276106676912,
            "offset_d": 11.685727681581284,
            "phase_offset": 0.2701344759011925,
            "linear_covariance_sigma_d": 1.1803072313344782
          },
          {
            "kind": 1,
            "cycle": 73,
            "predicted_btjd": 3573.012917397868,
            "offset_d": -21.05108303937459,
            "phase_offset": -0.4866297965300897,
            "linear_covariance_sigma_d": 1.078120741553754
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
