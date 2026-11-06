# Z101 TIC 238407344

Final lead verdict: PLAUSIBLE. Independent helper audit complete; see ../helper-independent-audit.md. Gaia DR3 2860943278543099648; G=11.942615; queue frozen without substitution. Association: single target event; orbital association unresolved.

S17 has a broad source-localized depression at BTJD1782.59. A custom TESScut aperture recovers about5ppt loss and difference centroid0.151pixel from target. The two conspicuous S84 QLP depressions do not recur in the source aperture; the first produces negative apparent loss (-1.009ppt) and no positive source difference flux. They cannot establish recurrence. Current TESScut sector inventory17/57/84 matches available QLP sectors.

Limitations: Only one credible target-localized event; S17 shallow morphology has baseline sensitivity; no eclipse-derived orbital period.

Next check: Observe a same-kind repeat; test Gaia-predicted windows using a source aperture.

## Numeric evidence and provenance

Identity-audit.json verifies exact TIC FITS headers, sectors, Gaia identity and actual phot_g_mean_mag against the frozen fresh-band-next1000 population and all source SHA256 values. lead-context.json lists representative raw SAP events and quality0 coverage; lead-timing.json stores local trapezoid fits and failure flags. Independent TESScut aperture reduction and difference images share the same TESS photons. These are reduction checks, not independent observing occasions. Gaia neighbor response is a126arcsec cone queried via Heidelberg TAP; lead-neighbors.json records source pixel positions and relative G flux. G flux is an approximate contaminant capability screen, not a calibrated TESS passband or pixel-loss comparison.

```json
{
  "clock": null,
  "localization": {
    "tic": "238407344",
    "event": {
      "sector": 84,
      "screen_btjd": 3585.92349197767,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.0023148267478063644,
      "first_btjd": 3585.025339286678,
      "last_btjd": 3586.82164473423,
      "scale_sap": 0.9996464252471924,
      "noise_ppt": 2.870914212650656,
      "source_sha256": "bf42867473567fa3656f0d996c1fb65c266bd72c6316f10a5a034d0f514c3df9",
      "center_btjd": 3585.814687264219,
      "center_formal_error_d": 0.004134030147247396,
      "depth_ppt": 14.665532124277135,
      "duration_d": 0.8999954075079308,
      "ingress_d": 0.34119306718690184,
      "baseline_slope_d": -0.0008090771652436169,
      "residual_rms_ppt": 4.329823255728428,
      "fit_usable": false
    },
    "ra": 1.33885656635,
    "dec": 29.127130743,
    "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/jc2cWobdtRino_6A/astrocut_1.33885656635_29.127130743_11.0x11.0px.zip",
    "zip_sha256": "49f915a1711fc0cbce674a5ec6992388631e34e5e8e4df2cef797e39b8e56129",
    "fits_sha256": "4506d6708cb48055172e9683552ac2baa4ec80adfdb16b097b65663633258240",
    "target_xy": [
      5.030319979982478,
      5.361052438030952
    ],
    "core_n": 195,
    "side_n": 721,
    "aperture_loss": -0.0010094282662795884,
    "diff_peak_xy": [
      4,
      6
    ],
    "positive_diff_centroid_xy": [
      NaN,
      NaN
    ],
    "centroid_offset_pixels": NaN,
    "status": "measured"
  },
  "timing": [
    {
      "sector": 84,
      "screen_btjd": 3585.92349197767,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.0023148267478063644,
      "first_btjd": 3585.025339286678,
      "last_btjd": 3586.82164473423,
      "scale_sap": 0.9996464252471924,
      "noise_ppt": 2.870914212650656,
      "source_sha256": "bf42867473567fa3656f0d996c1fb65c266bd72c6316f10a5a034d0f514c3df9",
      "center_btjd": 3585.814687264219,
      "center_formal_error_d": 0.004134030147247396,
      "depth_ppt": 14.665532124277135,
      "duration_d": 0.8999954075079308,
      "ingress_d": 0.34119306718690184,
      "baseline_slope_d": -0.0008090771652436169,
      "residual_rms_ppt": 4.329823255728428,
      "fit_usable": false
    },
    {
      "sector": 17,
      "screen_btjd": 1782.55,
      "kind": "candidate",
      "n": 67,
      "cadence_d": 0.020832669225796963,
      "first_btjd": 1781.6615787125234,
      "last_btjd": 1783.4323553153276,
      "scale_sap": 0.999470591545105,
      "noise_ppt": 0.8941134223590199,
      "source_sha256": "8f54d4c94f08a5ce015b57b6b74458ea9bf8115775ba5931db780e2d35ab2c8d",
      "center_btjd": 1782.5928310197373,
      "center_formal_error_d": 0.026125141436041933,
      "depth_ppt": 2.019007184523217,
      "duration_d": 0.7993650966622537,
      "ingress_d": 0.2392394710045896,
      "baseline_slope_d": -0.00040273678022961323,
      "residual_rms_ppt": 0.8353421879302861,
      "fit_usable": true
    },
    {
      "sector": 84,
      "screen_btjd": 3598.49,
      "kind": "candidate",
      "n": 396,
      "cadence_d": 0.0023147791603150836,
      "first_btjd": 3597.5901107161867,
      "last_btjd": 3598.504448476832,
      "scale_sap": 1.0000776052474976,
      "noise_ppt": 2.2536096692209466,
      "source_sha256": "bf42867473567fa3656f0d996c1fb65c266bd72c6316f10a5a034d0f514c3df9",
      "center_btjd": 3598.5106883717363,
      "center_formal_error_d": 36366.8967432034,
      "depth_ppt": 13.567446045266648,
      "duration_d": 0.5309913849864071,
      "ingress_d": 0.22774741025652465,
      "baseline_slope_d": -0.00032591654190873234,
      "residual_rms_ppt": 2.9432040205562955,
      "fit_usable": false
    }
  ],
  "gaia_geometry": {
    "source_id": "2860943278543099648",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 44.988923547295855,
    "gaia_period_error_d": 0.17249955,
    "eccentricity": 0.43316775038693284,
    "omega_deg": 262.2627553726658,
    "tp_btjd": 394.4394885800722,
    "mass_function_solar": 0.000812676792538526,
    "events": [
      {
        "sector": 17,
        "event_kind": "candidate",
        "observed_btjd": 1782.5928310197373,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 30,
            "predicted_btjd": 1768.7949668807046,
            "offset_d": 13.797864139032754,
            "phase_offset": 0.30669469396233423,
            "linear_covariance_sigma_d": 7.771737232796738
          },
          {
            "kind": 1,
            "cycle": 31,
            "predicted_btjd": 1789.4414380935389,
            "offset_d": -6.848607073801531,
            "phase_offset": -0.15222873840494858,
            "linear_covariance_sigma_d": 5.108631681739409
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
