# Z117 TIC 347159772

Lead verdict: C. Gaia DR3 4531227025992849920; actual G=11.588064. Association: consistent with Gaia-selected orbit. Catalogue status: NO_EXACT_EB_IDENTIFICATION_IN_FINAL_CENTRAL_SCOPE.

Deep same-kind consecutive S53/S54 eclipses at2752.01031 and2777.98834 yield25.97802721d. Shallow opposite conjunction repeats at2795.02763 and3496.43481, independently supporting25.97804d over27cycles. Divisors2..6 have covered nulls. Gaia conjunction residuals1.12..2.02d fit local covariance about0.99..1.25d. S80 primary at predicted3505.37310 is visibly recovered with partial quality flags; lead-flagged-repeat.json/png preserves the raw check without a formal timing claim. First S53 TESScut core had zero good samples; independent S80 secondary extraction localizes within0.103pixel of target and deep S80 primary custom aperture recovers200.9ppt at0.0219pixel centroid offset.

Limitations: Initial S53 and S54 source cutouts unavailable at eclipse core; alternate S80 secondary source image succeeds. Close few-percent G-flux neighbors cannot straightforwardly supply250ppt primary loss.

Next check: Improve primary eclipse photometry and passband-specific neighbor constraints.

Bounded review follows paper Section2.7: representative quality0 raw SAP events, fitted same-kind timings, covered integer alternatives, alternate extraction, deciding pixels, Gaia neighbors and source-specific covariance. Independent reductions reuse the same TESS photons. Missing coverage is never a null. G flux is an approximate capability screen, not a TESS aperture-throughput model. Central sealed shared-catalogues supply dated catalogue scope; nonmatch is not exhaustive novelty proof. No queue replacement, ledger or public edits.

Numeric evidence: lead-context.json, lead-series.json, lead-timing.json, helper-localization.json/png, lead-neighbors.json, lead-capability-audit.json; batch-level clocks/aliases/Gaia-covariance/identity-audit and source hashes. See helper-independent-audit.md for independent source adjudication.

```json
{
  "clock": {
    "period_d": 25.978027207342524,
    "epoch_btjd": 2752.010314946358,
    "formal_period_error_d": 0.00491049661684004,
    "cycles": [
      0,
      1
    ],
    "times": [
      2752.0103149463575,
      2777.9883421537006
    ],
    "residuals": [
      -4.547473508864641e-13,
      0.0
    ],
    "duration_d": 0.20100322890920125,
    "depth_ppt": 245.5810866891788,
    "max_residual_d": 4.547473508864641e-13,
    "gaia_period_d": 25.99097013991088,
    "note": "Trials inferred from eclipse intervals; integer-cycle selection requires covered-window audit. Timing error includes cadence/2 and .002d floors."
  },
  "gaia_geometry": {
    "source_id": "4531227025992849920",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 25.99097013991088,
    "gaia_period_error_d": 0.010003125,
    "eccentricity": 0.4039125279330685,
    "omega_deg": 48.52587009674782,
    "tp_btjd": 386.7258459698279,
    "mass_function_solar": 0.1010222392089802,
    "events": [
      {
        "sector": 53,
        "event_kind": "candidate",
        "observed_btjd": 2752.0103149463575,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 91,
            "predicted_btjd": 2753.12809358372,
            "offset_d": -1.1177786373623348,
            "phase_offset": -0.04300642228224912,
            "linear_covariance_sigma_d": 1.0883494484390885
          },
          {
            "kind": 1,
            "cycle": 90,
            "predicted_btjd": 2744.714884959297,
            "offset_d": 7.295429987060743,
            "phase_offset": 0.28069094565493424,
            "linear_covariance_sigma_d": 0.9717385702487459
          }
        ]
      },
      {
        "sector": 54,
        "event_kind": "candidate",
        "observed_btjd": 2777.9883421537006,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 92,
            "predicted_btjd": 2779.119063723631,
            "offset_d": -1.1307215699303015,
            "phase_offset": -0.043504400329943925,
            "linear_covariance_sigma_d": 1.0972050230593637
          },
          {
            "kind": 1,
            "cycle": 91,
            "predicted_btjd": 2770.705855099208,
            "offset_d": 7.282487054492776,
            "phase_offset": 0.28019296760723944,
            "linear_covariance_sigma_d": 0.9810606010857896
          }
        ]
      },
      {
        "sector": 54,
        "event_kind": "candidate",
        "observed_btjd": 2795.0276268335324,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 93,
            "predicted_btjd": 2805.110033863542,
            "offset_d": -10.082407030009563,
            "phase_offset": -0.38791961114707874,
            "linear_covariance_sigma_d": 1.1060801636248163
          },
          {
            "kind": 1,
            "cycle": 92,
            "predicted_btjd": 2796.696825239119,
            "offset_d": -1.669198405586485,
            "phase_offset": -0.06422224320989538,
            "linear_covariance_sigma_d": 0.9903959198270317
          }
        ]
      },
      {
        "sector": 80,
        "event_kind": "candidate",
        "observed_btjd": 3496.434814215401,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 120,
            "predicted_btjd": 3506.8662276411355,
            "offset_d": -10.431413425734718,
            "phase_offset": -0.401347597630324,
            "linear_covariance_sigma_d": 1.3516771607866156
          },
          {
            "kind": 1,
            "cycle": 119,
            "predicted_btjd": 3498.4530190167125,
            "offset_d": -2.01820480131164,
            "phase_offset": -0.07765022969314066,
            "linear_covariance_sigma_d": 1.2463723551579682
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
