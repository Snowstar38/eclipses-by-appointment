# Z116 TIC 322438528

Lead verdict: C. Gaia DR3 2224597625432992000; actual G=11.884822. Association: consistent with Gaia-selected orbit. Catalogue status: NO_EXACT_EB_IDENTIFICATION_IN_FINAL_CENTRAL_SCOPE.

Six shallow same-kind events across S17/59/77/78/84/86 give47.77993585d; distinct deeper opposite-conjunction S78/85 events are not mixed into that clock. Covered divisors2..6 show nulls. Deep alternative-aperture event27ppt and difference Gaussian0.070pixel from target favor target; nearest appreciable neighbor at0.79pixel has0.009 relative G flux. Gaia conjunction residuals0.084..0.649d fit covariance0.317..0.745d.

Limitations: G-band contaminant capability is approximate; local formal timing errors include cadence floors in clock.

Next check: More precise PRF photometry can refine depths.

Bounded review follows paper Section2.7: representative quality0 raw SAP events, fitted same-kind timings, covered integer alternatives, alternate extraction, deciding pixels, Gaia neighbors and source-specific covariance. Independent reductions reuse the same TESS photons. Missing coverage is never a null. G flux is an approximate capability screen, not a TESS aperture-throughput model. Central sealed shared-catalogues supply dated catalogue scope; nonmatch is not exhaustive novelty proof. No queue replacement, ledger or public edits.

Numeric evidence: lead-context.json, lead-series.json, lead-timing.json, helper-localization.json/png, lead-neighbors.json, lead-capability-audit.json; batch-level clocks/aliases/Gaia-covariance/identity-audit and source hashes. See helper-independent-audit.md for independent source adjudication.

```json
{
  "clock": {
    "period_d": 47.77993585032699,
    "epoch_btjd": 1775.110231230048,
    "formal_period_error_d": 0.00015284016341056316,
    "cycles": [
      0,
      24,
      34,
      35,
      38,
      39
    ],
    "times": [
      1775.1265122780421,
      2921.826363702187,
      3399.6263021019745,
      3447.4144810219163,
      3590.747989707154,
      3638.5247794333804
    ],
    "residuals": [
      0.01628104799419816,
      -0.002327935708763107,
      -0.0017480391911703919,
      0.006495030423593562,
      0.00019616468034655554,
      -0.0029499594202206936
    ],
    "duration_d": 0.803279181785471,
    "depth_ppt": 11.579283829497758,
    "max_residual_d": 0.01628104799419816,
    "gaia_period_d": 47.77104313807935,
    "note": "Trials inferred from eclipse intervals; integer-cycle selection requires covered-window audit. Timing error includes cadence/2 and .002d floors."
  },
  "gaia_geometry": {
    "source_id": "2224597625432992000",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 47.77104313807935,
    "gaia_period_error_d": 0.011290248,
    "eccentricity": 0.43418631825295645,
    "omega_deg": 170.2883225730139,
    "tp_btjd": 383.1115114656132,
    "mass_function_solar": 0.07747494182831025,
    "events": [
      {
        "sector": 17,
        "event_kind": "candidate",
        "observed_btjd": 1775.1265122780421,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 28,
            "predicted_btjd": 1763.7951099974698,
            "offset_d": 11.33140228057232,
            "phase_offset": 0.23720232040609995,
            "linear_covariance_sigma_d": 0.29766478430731763
          },
          {
            "kind": 1,
            "cycle": 29,
            "predicted_btjd": 1775.0427205354476,
            "offset_d": 0.08379174259448519,
            "phase_offset": 0.0017540279024741024,
            "linear_covariance_sigma_d": 0.3168484410339352
          }
        ]
      },
      {
        "sector": 59,
        "event_kind": "candidate",
        "observed_btjd": 2921.826363702187,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 52,
            "predicted_btjd": 2910.3001453113743,
            "offset_d": 11.526218390812573,
            "phase_offset": 0.24128044174159494,
            "linear_covariance_sigma_d": 0.5594052481307304
          },
          {
            "kind": 1,
            "cycle": 53,
            "predicted_btjd": 2921.547755849352,
            "offset_d": 0.2786078528347389,
            "phase_offset": 0.005832149237969108,
            "linear_covariance_sigma_d": 0.5779414715571998
          }
        ]
      },
      {
        "sector": 77,
        "event_kind": "candidate",
        "observed_btjd": 3399.6263021019745,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 62,
            "predicted_btjd": 3388.0105766921674,
            "offset_d": 11.615725409807055,
            "phase_offset": 0.24315410857226824,
            "linear_covariance_sigma_d": 0.6706300956327226
          },
          {
            "kind": 1,
            "cycle": 63,
            "predicted_btjd": 3399.2581872301457,
            "offset_d": 0.3681148718287659,
            "phase_offset": 0.007705816068632871,
            "linear_covariance_sigma_d": 0.6889841304409332
          }
        ]
      },
      {
        "sector": 78,
        "event_kind": "candidate",
        "observed_btjd": 3436.400815937951,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 63,
            "predicted_btjd": 3435.781619830247,
            "offset_d": 0.6191961077038286,
            "phase_offset": 0.0129617455895631,
            "linear_covariance_sigma_d": 0.6817829133198282
          },
          {
            "kind": 1,
            "cycle": 64,
            "predicted_btjd": 3447.029230368225,
            "offset_d": -10.628414430274006,
            "phase_offset": -0.22248654691406275,
            "linear_covariance_sigma_d": 0.7001211171288577
          }
        ]
      },
      {
        "sector": 78,
        "event_kind": "candidate",
        "observed_btjd": 3447.4144810219163,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 63,
            "predicted_btjd": 3435.781619830247,
            "offset_d": 11.632861191669235,
            "phase_offset": 0.24351281503410224,
            "linear_covariance_sigma_d": 0.6817829133198282
          },
          {
            "kind": 1,
            "cycle": 64,
            "predicted_btjd": 3447.029230368225,
            "offset_d": 0.38525065369140066,
            "phase_offset": 0.008064522530476395,
            "linear_covariance_sigma_d": 0.7001211171288577
          }
        ]
      },
      {
        "sector": 84,
        "event_kind": "candidate",
        "observed_btjd": 3590.747989707154,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 66,
            "predicted_btjd": 3579.0947492444852,
            "offset_d": 11.653240462668691,
            "phase_offset": 0.24393941804841263,
            "linear_covariance_sigma_d": 0.7152672399452087
          },
          {
            "kind": 1,
            "cycle": 67,
            "predicted_btjd": 3590.342359782463,
            "offset_d": 0.40562992469085657,
            "phase_offset": 0.008491125544786775,
            "linear_covariance_sigma_d": 0.7335601892077919
          }
        ]
      },
      {
        "sector": 85,
        "event_kind": "candidate",
        "observed_btjd": 3627.514925246005,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 67,
            "predicted_btjd": 3626.8657923825645,
            "offset_d": 0.6491328634406273,
            "phase_offset": 0.013588417183278738,
            "linear_covariance_sigma_d": 0.7264366452032022
          },
          {
            "kind": 1,
            "cycle": 68,
            "predicted_btjd": 3638.1134029205423,
            "offset_d": -10.598477674537207,
            "phase_offset": -0.2218598753203471,
            "linear_covariance_sigma_d": 0.7447152155029445
          }
        ]
      },
      {
        "sector": 86,
        "event_kind": "candidate",
        "observed_btjd": 3638.5247794333804,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 67,
            "predicted_btjd": 3626.8657923825645,
            "offset_d": 11.658987050815995,
            "phase_offset": 0.244059712431156,
            "linear_covariance_sigma_d": 0.7264366452032022
          },
          {
            "kind": 1,
            "cycle": 68,
            "predicted_btjd": 3638.1134029205423,
            "offset_d": 0.4113765128381601,
            "phase_offset": 0.008611419927530175,
            "linear_covariance_sigma_d": 0.7447152155029445
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
