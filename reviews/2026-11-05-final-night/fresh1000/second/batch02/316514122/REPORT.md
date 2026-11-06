# Z113 TIC 316514122

Lead verdict: REFUTED. Gaia DR3 448454547745791744; actual G=11.857313. Association: positive off-target eclipsing contamination. Catalogue status: NO_EXACT_EB_IDENTIFICATION_IN_FINAL_CENTRAL_SCOPE.

Repeated narrow raw dips are genuine, but decisive S86 difference deficit centers(1.263,5.511),4.060pixels from intended target. Target aperture retains diluted8ppt while QLP dips reach50ppt. The positive off-target deficit refutes this intended-target claim. Event spacings near2.248d are unrelated to selected Gaia26.454d; no target by-catch claim or substitute identity is made.

Limitations: True contaminant identity and exact alternating-conjunction clock not characterized; no new target claim.

Next check: Identify contaminant separately using larger field and dedicated extraction.

Bounded review follows paper Section2.7: representative quality0 raw SAP events, fitted same-kind timings, covered integer alternatives, alternate extraction, deciding pixels, Gaia neighbors and source-specific covariance. Independent reductions reuse the same TESS photons. Missing coverage is never a null. G flux is an approximate capability screen, not a TESS aperture-throughput model. Central sealed shared-catalogues supply dated catalogue scope; nonmatch is not exhaustive novelty proof. No queue replacement, ledger or public edits.

Numeric evidence: lead-context.json, lead-series.json, lead-timing.json, helper-localization.json/png, lead-neighbors.json, lead-capability-audit.json; batch-level clocks/aliases/Gaia-covariance/identity-audit and source hashes. See helper-independent-audit.md for independent source adjudication.

```json
{
  "clock": null,
  "gaia_geometry": {
    "source_id": "448454547745791744",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 26.45436456558505,
    "gaia_period_error_d": 0.014333804,
    "eccentricity": 0.3435786473915207,
    "omega_deg": 357.5938604182933,
    "tp_btjd": 391.03147395916005,
    "mass_function_solar": 0.044282808200813144,
    "events": [
      {
        "sector": 18,
        "event_kind": "candidate",
        "observed_btjd": 1807.325763481927,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 53,
            "predicted_btjd": 1797.0397855057622,
            "offset_d": 10.285977976164759,
            "phase_offset": 0.3888196955426391,
            "linear_covariance_sigma_d": 0.7050875564196682
          },
          {
            "kind": 1,
            "cycle": 53,
            "predicted_btjd": 1815.9331285017438,
            "offset_d": -8.607365019816825,
            "phase_offset": -0.32536653823143796,
            "linear_covariance_sigma_d": 0.9312268157952923
          }
        ]
      },
      {
        "sector": 18,
        "event_kind": "candidate",
        "observed_btjd": 1800.5822682727223,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 53,
            "predicted_btjd": 1797.0397855057622,
            "offset_d": 3.54248276696012,
            "phase_offset": 0.13390919892170075,
            "linear_covariance_sigma_d": 0.7050875564196682
          },
          {
            "kind": 1,
            "cycle": 52,
            "predicted_btjd": 1789.4787639361589,
            "offset_d": 11.103504336563446,
            "phase_offset": 0.4197229651476185,
            "linear_covariance_sigma_d": 0.9175736827533655
          }
        ]
      },
      {
        "sector": 18,
        "event_kind": "candidate",
        "observed_btjd": 1793.8387250659273,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 53,
            "predicted_btjd": 1797.0397855057622,
            "offset_d": -3.2010604398349187,
            "phase_offset": -0.12100311205354881,
            "linear_covariance_sigma_d": 0.7050875564196682
          },
          {
            "kind": 1,
            "cycle": 52,
            "predicted_btjd": 1789.4787639361589,
            "offset_d": 4.359961129768408,
            "phase_offset": 0.1648106541723689,
            "linear_covariance_sigma_d": 0.9175736827533655
          }
        ]
      },
      {
        "sector": 18,
        "event_kind": "candidate",
        "observed_btjd": 1798.331701064299,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 53,
            "predicted_btjd": 1797.0397855057622,
            "offset_d": 1.2919155585368571,
            "phase_offset": 0.048835629951873155,
            "linear_covariance_sigma_d": 0.7050875564196682
          },
          {
            "kind": 1,
            "cycle": 52,
            "predicted_btjd": 1789.4787639361589,
            "offset_d": 8.852937128140184,
            "phase_offset": 0.3346493961777909,
            "linear_covariance_sigma_d": 0.9175736827533655
          }
        ]
      },
      {
        "sector": 19,
        "event_kind": "candidate",
        "observed_btjd": 1832.0575188409225,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 54,
            "predicted_btjd": 1823.4941500713473,
            "offset_d": 8.563368769575163,
            "phase_offset": 0.32370343836250753,
            "linear_covariance_sigma_d": 0.7188447751798325
          },
          {
            "kind": 1,
            "cycle": 54,
            "predicted_btjd": 1842.3874930673287,
            "offset_d": -10.329974226406193,
            "phase_offset": -0.39048279541156095,
            "linear_covariance_sigma_d": 0.9449001090455086
          }
        ]
      },
      {
        "sector": 19,
        "event_kind": "candidate",
        "observed_btjd": 1836.5521024659936,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 54,
            "predicted_btjd": 1823.4941500713473,
            "offset_d": 13.057952394646236,
            "phase_offset": 0.4936029501775884,
            "linear_covariance_sigma_d": 0.7188447751798325
          },
          {
            "kind": 1,
            "cycle": 54,
            "predicted_btjd": 1842.3874930673287,
            "offset_d": -5.835390601335121,
            "phase_offset": -0.22058328359648008,
            "linear_covariance_sigma_d": 0.9449001090455086
          }
        ]
      },
      {
        "sector": 19,
        "event_kind": "candidate",
        "observed_btjd": 1823.0623680517185,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 54,
            "predicted_btjd": 1823.4941500713473,
            "offset_d": -0.4317820196288267,
            "phase_offset": -0.01632176870317042,
            "linear_covariance_sigma_d": 0.7188447751798325
          },
          {
            "kind": 1,
            "cycle": 53,
            "predicted_btjd": 1815.9331285017438,
            "offset_d": 7.129239549974727,
            "phase_offset": 0.2694919975227559,
            "linear_covariance_sigma_d": 0.9312268157952923
          }
        ]
      },
      {
        "sector": 19,
        "event_kind": "candidate",
        "observed_btjd": 1820.8164883525517,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 54,
            "predicted_btjd": 1823.4941500713473,
            "offset_d": -2.6776617187956617,
            "phase_offset": -0.10121814538985674,
            "linear_covariance_sigma_d": 0.7188447751798325
          },
          {
            "kind": 1,
            "cycle": 53,
            "predicted_btjd": 1815.9331285017438,
            "offset_d": 4.883359850807892,
            "phase_offset": 0.18459562083606956,
            "linear_covariance_sigma_d": 0.9312268157952923
          }
        ]
      },
      {
        "sector": 59,
        "event_kind": "candidate",
        "observed_btjd": 2926.9199567277465,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 96,
            "predicted_btjd": 2934.5774618259193,
            "offset_d": -7.6575050981728054,
            "phase_offset": -0.28946093485589103,
            "linear_covariance_sigma_d": 1.3078790138607785
          },
          {
            "kind": 1,
            "cycle": 95,
            "predicted_btjd": 2927.016440256316,
            "offset_d": -0.09648352856947895,
            "phase_offset": -0.0036471686299732967,
            "linear_covariance_sigma_d": 1.516047837013861
          }
        ]
      },
      {
        "sector": 59,
        "event_kind": "candidate",
        "observed_btjd": 2917.928768199091,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 95,
            "predicted_btjd": 2908.1230972603344,
            "offset_d": 9.80567093875652,
            "phase_offset": 0.37066363527449425,
            "linear_covariance_sigma_d": 1.29371545993411
          },
          {
            "kind": 1,
            "cycle": 95,
            "predicted_btjd": 2927.016440256316,
            "offset_d": -9.087672057225063,
            "phase_offset": -0.34352259849958283,
            "linear_covariance_sigma_d": 1.516047837013861
          }
        ]
      },
      {
        "sector": 59,
        "event_kind": "candidate",
        "observed_btjd": 2935.915135921151,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 96,
            "predicted_btjd": 2934.5774618259193,
            "offset_d": 1.337674095231705,
            "phase_offset": 0.05056534591543011,
            "linear_covariance_sigma_d": 1.3078790138607785
          },
          {
            "kind": 1,
            "cycle": 95,
            "predicted_btjd": 2927.016440256316,
            "offset_d": 8.898695664835031,
            "phase_offset": 0.3363791121413478,
            "linear_covariance_sigma_d": 1.516047837013861
          }
        ]
      },
      {
        "sector": 59,
        "event_kind": "candidate",
        "observed_btjd": 2915.682308973125,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 95,
            "predicted_btjd": 2908.1230972603344,
            "offset_d": 7.559211712790784,
            "phase_offset": 0.28574535192671746,
            "linear_covariance_sigma_d": 1.29371545993411
          },
          {
            "kind": 1,
            "cycle": 95,
            "predicted_btjd": 2927.016440256316,
            "offset_d": -11.3341312831908,
            "phase_offset": -0.42844088184735957,
            "linear_covariance_sigma_d": 1.516047837013861
          }
        ]
      },
      {
        "sector": 86,
        "event_kind": "candidate",
        "observed_btjd": 3659.8301669509683,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 123,
            "predicted_btjd": 3648.8453050967155,
            "offset_d": 10.984861854252813,
            "phase_offset": 0.4152381671092268,
            "linear_covariance_sigma_d": 1.6913795364456181
          },
          {
            "kind": 1,
            "cycle": 123,
            "predicted_btjd": 3667.738648092697,
            "offset_d": -7.908481141728771,
            "phase_offset": -0.29894806666485024,
            "linear_covariance_sigma_d": 1.9118691675594937
          }
        ]
      },
      {
        "sector": 86,
        "event_kind": "candidate",
        "observed_btjd": 3648.587443277839,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 123,
            "predicted_btjd": 3648.8453050967155,
            "offset_d": -0.25786181887633575,
            "phase_offset": -0.009747420628344737,
            "linear_covariance_sigma_d": 1.6913795364456181
          },
          {
            "kind": 1,
            "cycle": 122,
            "predicted_btjd": 3641.284283527112,
            "offset_d": 7.303159750726991,
            "phase_offset": 0.276066345597573,
            "linear_covariance_sigma_d": 1.8976927276451079
          }
        ]
      },
      {
        "sector": 86,
        "event_kind": "candidate",
        "observed_btjd": 3646.3400501750098,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 123,
            "predicted_btjd": 3648.8453050967155,
            "offset_d": -2.5052549217057276,
            "phase_offset": -0.09470100540478897,
            "linear_covariance_sigma_d": 1.6913795364456181
          },
          {
            "kind": 1,
            "cycle": 122,
            "predicted_btjd": 3641.284283527112,
            "offset_d": 5.055766647897599,
            "phase_offset": 0.19111276082112874,
            "linear_covariance_sigma_d": 1.8976927276451079
          }
        ]
      },
      {
        "sector": 86,
        "event_kind": "candidate",
        "observed_btjd": 3662.0772377171816,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 124,
            "predicted_btjd": 3675.299669662301,
            "offset_d": -13.222431945119297,
            "phase_offset": -0.49982043274328325,
            "linear_covariance_sigma_d": 1.7056137301827776
          },
          {
            "kind": 1,
            "cycle": 123,
            "predicted_btjd": 3667.738648092697,
            "offset_d": -5.661410375515516,
            "phase_offset": -0.21400666651734832,
            "linear_covariance_sigma_d": 1.9118691675594937
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
