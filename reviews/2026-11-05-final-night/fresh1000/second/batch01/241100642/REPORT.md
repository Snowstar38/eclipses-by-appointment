# Z103 TIC 241100642

Final lead verdict: P. Independent helper audit complete; see ../helper-independent-audit.md. Gaia DR3 359275560498692352; G=11.92658; queue frozen without substitution. Association: HOST_UNCERTAIN; period consistent with Gaia-selected orbit.

Three narrow raw-flux events at1798.64790,2905.00394,3613.06019 yield44.25378579d with cycles0,25,41. Covered predicted windows support the measured clock; tested divisors2..6 have clean nulls. Source difference Gaussian0.216pixel and positive centroid0.179pixel from target; custom aperture recovers6.9ppt. Source-specific SB1 conjunction offsets are0.297..0.416d with covariance sigmas0.95..2.385d.

Limitations: Shallow event has a physically capable faint neighbor with0.0081 target G flux at0.86pixel; deciding centroid favors target but no calibrated source-discriminating PRF uncertainty test excludes it. HOST_UNCERTAIN. Timing error uses cadence/2 and0.002d floors, not calibrated posterior.

Next check: Higher-SNR target PRF extraction could sharpen faint-neighbor attribution and period.

## Numeric evidence and provenance

Identity-audit.json verifies exact TIC FITS headers, sectors, Gaia identity and actual phot_g_mean_mag against the frozen fresh-band-next1000 population and all source SHA256 values. lead-context.json lists representative raw SAP events and quality0 coverage; lead-timing.json stores local trapezoid fits and failure flags. Independent TESScut aperture reduction and difference images share the same TESS photons. These are reduction checks, not independent observing occasions. Gaia neighbor response is a126arcsec cone queried via Heidelberg TAP; lead-neighbors.json records source pixel positions and relative G flux. G flux is an approximate contaminant capability screen, not a calibrated TESS passband or pixel-loss comparison.

```json
{
  "clock": {
    "period_d": 44.25378578771851,
    "epoch_btjd": 1798.6566101123524,
    "formal_period_error_d": 0.0002277376656686564,
    "cycles": [
      0,
      25,
      41
    ],
    "times": [
      1798.6478988666183,
      2905.0039408300518,
      3613.060191904386
    ],
    "residuals": [
      -0.008711245734048134,
      0.0026860247367039847,
      -0.0016355044253941742
    ],
    "duration_d": 0.20308412571836093,
    "depth_ppt": 6.8476596081324965,
    "max_residual_d": 0.008711245734048134,
    "gaia_period_d": 44.256869769433756,
    "note": "Trials inferred from eclipse intervals; integer-cycle selection requires covered-window audit. Timing error includes cadence/2 and .002d floors."
  },
  "localization": {
    "tic": "241100642",
    "event": {
      "sector": 18,
      "screen_btjd": 1798.640481337354,
      "kind": "candidate",
      "n": 86,
      "cadence_d": 0.02083323878855481,
      "first_btjd": 1797.7446515364213,
      "last_btjd": 1799.5363100231575,
      "scale_sap": 0.9991315603256226,
      "noise_ppt": 0.6830735314697702,
      "source_sha256": "b57b83b24a862a9595163eb4cc051c4a365d3c1ca76aec85892e23e90967336e",
      "center_btjd": 1798.6478988666183,
      "center_formal_error_d": 0.003055135389029355,
      "depth_ppt": 5.876486441771913,
      "duration_d": 0.20308412571836093,
      "ingress_d": 0.07368360124704898,
      "baseline_slope_d": -0.0001505888342410664,
      "residual_rms_ppt": 0.7645896362840567,
      "fit_usable": true
    },
    "ra": 29.5764378224,
    "dec": 50.7905640747,
    "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/zbrqYgEtSHx6-qDt/astrocut_29.5764378224_50.7905640747_11.0x11.0px.zip",
    "zip_sha256": "10fc225ac664b1de107f9f5d432d83400b697202ded36912b9c9ed230e7a8cc8",
    "fits_sha256": "fa0634f2835fe9415dc3f60a7a8ad3349f04f9dce4f933fb6f257015bd1ae031",
    "target_xy": [
      5.200115934420711,
      5.0216370268894375
    ],
    "core_n": 5,
    "side_n": 25,
    "aperture_loss": 0.00653493523199844,
    "diff_peak_xy": [
      5,
      5
    ],
    "positive_diff_centroid_xy": [
      5.2696027440763205,
      5.186121966868876
    ],
    "centroid_offset_pixels": 0.17856010807611616,
    "status": "measured"
  },
  "timing": [
    {
      "sector": 18,
      "screen_btjd": 1798.640481337354,
      "kind": "candidate",
      "n": 86,
      "cadence_d": 0.02083323878855481,
      "first_btjd": 1797.7446515364213,
      "last_btjd": 1799.5363100231575,
      "scale_sap": 0.9991315603256226,
      "noise_ppt": 0.6830735314697702,
      "source_sha256": "b57b83b24a862a9595163eb4cc051c4a365d3c1ca76aec85892e23e90967336e",
      "center_btjd": 1798.6478988666183,
      "center_formal_error_d": 0.003055135389029355,
      "depth_ppt": 5.876486441771913,
      "duration_d": 0.20308412571836093,
      "ingress_d": 0.07368360124704898,
      "baseline_slope_d": -0.0001505888342410664,
      "residual_rms_ppt": 0.7645896362840567,
      "fit_usable": true
    },
    {
      "sector": 58,
      "screen_btjd": 2904.99,
      "kind": "candidate",
      "n": 778,
      "cadence_d": 0.002314772854333569,
      "first_btjd": 2904.091251389943,
      "last_btjd": 2905.889829869113,
      "scale_sap": 0.9998306035995483,
      "noise_ppt": 2.2645958174057963,
      "source_sha256": "e5caa8f673d4fce087105f2fc488d739b3e87a9ca506cdea35c762ff3a7c990b",
      "center_btjd": 2905.0039408300518,
      "center_formal_error_d": 0.003613347502316764,
      "depth_ppt": 6.8476596081324965,
      "duration_d": 0.209020922666485,
      "ingress_d": 0.10241998419707066,
      "baseline_slope_d": 0.00015821575493574704,
      "residual_rms_ppt": 2.210953488603134,
      "fit_usable": true
    },
    {
      "sector": 85,
      "screen_btjd": 3613.07,
      "kind": "candidate",
      "n": 576,
      "cadence_d": 0.0023148467566898034,
      "first_btjd": 3612.6381469489606,
      "last_btjd": 3613.9691837818727,
      "scale_sap": 1.0008574724197388,
      "noise_ppt": 2.7769388888563915,
      "source_sha256": "b2cb40621103b38ade579f8bf9e8df5142d78c7d083e15288e12f783dd702ee6",
      "center_btjd": 3613.060191904386,
      "center_formal_error_d": 0.0036107923447860025,
      "depth_ppt": 6.915747487535272,
      "duration_d": 0.17770343990136556,
      "ingress_d": 0.06959015018696087,
      "baseline_slope_d": -0.0014710169242327037,
      "residual_rms_ppt": 2.7758707583852544,
      "fit_usable": true
    }
  ],
  "gaia_geometry": {
    "source_id": "359275560498692352",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 44.256869769433756,
    "gaia_period_error_d": 0.035604045,
    "eccentricity": 0.42210634445506606,
    "omega_deg": 344.4686464326797,
    "tp_btjd": 386.74696132881775,
    "mass_function_solar": 0.07654383273125569,
    "events": [
      {
        "sector": 18,
        "event_kind": "candidate",
        "observed_btjd": 1798.6478988666183,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 32,
            "predicted_btjd": 1809.871247910105,
            "offset_d": -11.223349043486678,
            "phase_offset": -0.2535956361567655,
            "linear_covariance_sigma_d": 1.4611733390213728
          },
          {
            "kind": 1,
            "cycle": 31,
            "predicted_btjd": 1798.9445557703334,
            "offset_d": -0.2966569037150748,
            "phase_offset": -0.0067030701732991175,
            "linear_covariance_sigma_d": 0.9502489819321402
          }
        ]
      },
      {
        "sector": 58,
        "event_kind": "candidate",
        "observed_btjd": 2905.0039408300518,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 57,
            "predicted_btjd": 2916.2929921459486,
            "offset_d": -11.289051315896813,
            "phase_offset": -0.25508020279585286,
            "linear_covariance_sigma_d": 2.318551114286944
          },
          {
            "kind": 1,
            "cycle": 56,
            "predicted_btjd": 2905.366300006177,
            "offset_d": -0.36235917612521007,
            "phase_offset": -0.008187636812386477,
            "linear_covariance_sigma_d": 1.8205530846593956
          }
        ]
      },
      {
        "sector": 85,
        "event_kind": "candidate",
        "observed_btjd": 3613.060191904386,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 73,
            "predicted_btjd": 3624.402908456889,
            "offset_d": -11.34271655250268,
            "phase_offset": -0.25629278825174817,
            "linear_covariance_sigma_d": 2.877720189238565
          },
          {
            "kind": 1,
            "cycle": 72,
            "predicted_btjd": 3613.476216317117,
            "offset_d": -0.41602441273107615,
            "phase_offset": -0.00940022226828174,
            "linear_covariance_sigma_d": 2.385227976964008
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
