# Z107 TIC 278185284

Final lead verdict: P. Independent helper audit complete; see ../helper-independent-audit.md. Gaia DR3 4525746853876018304; G=11.9361515; queue frozen without substitution. Association: Gaia-consistent full-period solution; half-period alias unresolved.

Three deep raw events2417.72864,2751.19526,3501.49600 yield27.78890921d cycles0,12,39. Custom aperture126.76ppt and difference centroid0.078pixel localize on target. Geometry residuals0.710..1.499d fit covariance2.547..3.944d. The13.8944546d alias is timing-compatible and has no additional clean covered null in this bounded sample. Real repeated eclipses established; missing unique clock check supports probable.

Limitations: Full period versus half period remains unresolved; pipeline comparisons share TESS photons.

Next check: Obtain/test a clean13.894d-interleaved predicted window.

## Numeric evidence and provenance

Identity-audit.json verifies exact TIC FITS headers, sectors, Gaia identity and actual phot_g_mean_mag against the frozen fresh-band-next1000 population and all source SHA256 values. lead-context.json lists representative raw SAP events and quality0 coverage; lead-timing.json stores local trapezoid fits and failure flags. Independent TESScut aperture reduction and difference images share the same TESS photons. These are reduction checks, not independent observing occasions. Gaia neighbor response is a126arcsec cone queried via Heidelberg TAP; lead-neighbors.json records source pixel positions and relative G flux. G flux is an approximate contaminant capability screen, not a calibrated TESS passband or pixel-loss comparison.

```json
{
  "clock": {
    "period_d": 27.788909211822933,
    "epoch_btjd": 2417.728521731702,
    "formal_period_error_d": 9.342637007858393e-05,
    "cycles": [
      0,
      12,
      39
    ],
    "times": [
      2417.7286440112252,
      2751.1952556356723,
      3501.495999024236
    ],
    "residuals": [
      0.00012227952311150148,
      -0.00017663790504229837,
      1.803143959477893e-05
    ],
    "duration_d": 0.37606272838431304,
    "depth_ppt": 103.84092715304726,
    "max_residual_d": 0.00017663790504229837,
    "gaia_period_d": 27.809137053749616,
    "note": "Trials inferred from eclipse intervals; integer-cycle selection requires covered-window audit. Timing error includes cadence/2 and .002d floors."
  },
  "localization": {
    "tic": "278185284",
    "event": {
      "sector": 80,
      "screen_btjd": 3501.497924488927,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.0023147788358528487,
      "first_btjd": 3500.599789868493,
      "last_btjd": 3502.3960582788163,
      "scale_sap": 0.9980744123458862,
      "noise_ppt": 3.0483553151375475,
      "source_sha256": "9fb885b859784f59184603f4dd02255bcaf9576375353809f5c8d0bb3f2667d5",
      "center_btjd": 3501.495999024236,
      "center_formal_error_d": 0.00030977946958588053,
      "depth_ppt": 103.98323768973302,
      "duration_d": 0.3774382780275193,
      "ingress_d": 0.09530423698571315,
      "baseline_slope_d": 0.0013117298364263201,
      "residual_rms_ppt": 3.1849618427190722,
      "fit_usable": true
    },
    "ra": 279.705359711,
    "dec": 20.8173199762,
    "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/bbZDRTd-0aoD7xNy/astrocut_279.705359711_20.8173199762_11.0x11.0px.zip",
    "zip_sha256": "57d3a7d9502ac06b1da1ddb8ad7a707281063526c607b2ad529ab0e5065dfff8",
    "fits_sha256": "5b29be93be4378ec03b75064913dd0fd7b50d012db8081281d1438cdae2e715b",
    "target_xy": [
      5.607125798107246,
      5.109868778385454
    ],
    "core_n": 81,
    "side_n": 407,
    "aperture_loss": 0.12675597175963682,
    "diff_peak_xy": [
      6,
      5
    ],
    "positive_diff_centroid_xy": [
      5.564999807547904,
      5.175935098818152
    ],
    "centroid_offset_pixels": 0.0783540539865143,
    "status": "measured"
  },
  "timing": [
    {
      "sector": 40,
      "screen_btjd": 2417.729849745913,
      "kind": "candidate",
      "n": 176,
      "cadence_d": 0.006944330321857706,
      "first_btjd": 2416.8340311176703,
      "last_btjd": 2418.625667856665,
      "scale_sap": 0.9995465874671936,
      "noise_ppt": 4.750619313783635,
      "source_sha256": "6604bedef4b2b3623eb5e21bc285d5e0d3f4cfc14f7dacde40208e234ed1a262",
      "center_btjd": 2417.7286440112252,
      "center_formal_error_d": 0.0009782643663198481,
      "depth_ppt": 103.84092715304726,
      "duration_d": 0.37306033801386257,
      "ingress_d": 0.09189834578537273,
      "baseline_slope_d": -0.004362260088293511,
      "residual_rms_ppt": 2.0854143142124957,
      "fit_usable": true
    },
    {
      "sector": 53,
      "screen_btjd": 2751.1950383414905,
      "kind": "candidate",
      "n": 157,
      "cadence_d": 0.006944564700688716,
      "first_btjd": 2750.3130787351347,
      "last_btjd": 2752.090886765298,
      "scale_sap": 1.0004136562347412,
      "noise_ppt": 1.750147806061822,
      "source_sha256": "05c10ca013f4deaac70b3e2397c7978959069c0c057769f475c4d2c9d09a6c80",
      "center_btjd": 2751.1952556356723,
      "center_formal_error_d": 0.00038779571509000205,
      "depth_ppt": 101.32055341330793,
      "duration_d": 0.37606272838431304,
      "ingress_d": 0.09247763157034448,
      "baseline_slope_d": 0.0004888841392447993,
      "residual_rms_ppt": 2.164005251341614,
      "fit_usable": true
    },
    {
      "sector": 80,
      "screen_btjd": 3501.497924488927,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.0023147788358528487,
      "first_btjd": 3500.599789868493,
      "last_btjd": 3502.3960582788163,
      "scale_sap": 0.9980744123458862,
      "noise_ppt": 3.0483553151375475,
      "source_sha256": "9fb885b859784f59184603f4dd02255bcaf9576375353809f5c8d0bb3f2667d5",
      "center_btjd": 3501.495999024236,
      "center_formal_error_d": 0.00030977946958588053,
      "depth_ppt": 103.98323768973302,
      "duration_d": 0.3774382780275193,
      "ingress_d": 0.09530423698571315,
      "baseline_slope_d": 0.0013117298364263201,
      "residual_rms_ppt": 3.1849618427190722,
      "fit_usable": true
    }
  ],
  "gaia_geometry": {
    "source_id": "4525746853876018304",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 27.809137053749616,
    "gaia_period_error_d": 0.037710533,
    "eccentricity": 0.2230729892008714,
    "omega_deg": 251.57668815532807,
    "tp_btjd": 400.1135077411157,
    "mass_function_solar": 0.018614205165314635,
    "events": [
      {
        "sector": 40,
        "event_kind": "candidate",
        "observed_btjd": 2417.7286440112252,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 72,
            "predicted_btjd": 2418.4386680488265,
            "offset_d": -0.7100240376012152,
            "phase_offset": -0.02553204136571652,
            "linear_covariance_sigma_d": 2.546673536975758
          },
          {
            "kind": 1,
            "cycle": 73,
            "predicted_btjd": 2431.067315707406,
            "offset_d": -13.338671696180882,
            "phase_offset": -0.479650687124877,
            "linear_covariance_sigma_d": 3.403502016988091
          }
        ]
      },
      {
        "sector": 53,
        "event_kind": "candidate",
        "observed_btjd": 2751.1952556356723,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 84,
            "predicted_btjd": 2752.148312693822,
            "offset_d": -0.9530570581496249,
            "phase_offset": -0.034271363987582654,
            "linear_covariance_sigma_d": 2.9689280169436785
          },
          {
            "kind": 1,
            "cycle": 85,
            "predicted_btjd": 2764.7769603524016,
            "offset_d": -13.581704716729291,
            "phase_offset": -0.4883900097467432,
            "linear_covariance_sigma_d": 3.8548787753909473
          }
        ]
      },
      {
        "sector": 80,
        "event_kind": "candidate",
        "observed_btjd": 3501.495999024236,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 111,
            "predicted_btjd": 3502.9950131450614,
            "offset_d": -1.49901412082545,
            "phase_offset": -0.053903654684722836,
            "linear_covariance_sigma_d": 3.9436290633078115
          },
          {
            "kind": 1,
            "cycle": 111,
            "predicted_btjd": 3487.8145237498916,
            "offset_d": 13.681475274344393,
            "phase_offset": 0.4919776995561128,
            "linear_covariance_sigma_d": 4.83359933728808
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
