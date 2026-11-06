# Z115 TIC 321797629

Lead verdict: P. Gaia DR3 5863872845916469376; actual G=11.94211. Association: HOST_UNCERTAIN; known-neighbor novelty hold. Catalogue status: KNOWN_NEIGHBOR_OWNERSHIP_HOLD.

Repeated discrete dips are established in six QLP sectors and recover81ppt in a custom aperture. Difference Gaussian is0.437pixel from target, in a severely crowded field. Prior-known EB TIC321797613/Gaia5863872807181960064 lies11.35arcsec away and has not been source-discriminated from the intended target. Short repeated dip spacings differ from Gaia47.020d and agree qualitatively with nearby VSX/ASASSN EB period2.095d (opposite conjunction spacing about1.0475d). No new-system count is authorized while known-neighbor ownership remains unresolved.

Limitations: KNOWN_NEIGHBOR_OWNERSHIP_HOLD; true eclipse source and unique clock unresolved; Gaia association not established.

Next check: Resolve target versus known EB with calibrated PRF source attribution or higher spatial resolution.

Bounded review follows paper Section2.7: representative quality0 raw SAP events, fitted same-kind timings, covered integer alternatives, alternate extraction, deciding pixels, Gaia neighbors and source-specific covariance. Independent reductions reuse the same TESS photons. Missing coverage is never a null. G flux is an approximate capability screen, not a TESS aperture-throughput model. Central sealed shared-catalogues supply dated catalogue scope; nonmatch is not exhaustive novelty proof. No queue replacement, ledger or public edits.

Numeric evidence: lead-context.json, lead-series.json, lead-timing.json, helper-localization.json/png, lead-neighbors.json, lead-capability-audit.json; batch-level clocks/aliases/Gaia-covariance/identity-audit and source hashes. See helper-independent-audit.md for independent source adjudication.

```json
{
  "clock": null,
  "gaia_geometry": {
    "source_id": "5863872845916469376",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 47.020431138769524,
    "gaia_period_error_d": 0.090351105,
    "eccentricity": 0.4195699630076004,
    "omega_deg": 152.66516216879228,
    "tp_btjd": 382.28045037524817,
    "mass_function_solar": 0.0759181818260976,
    "events": [
      {
        "sector": 11,
        "event_kind": "candidate",
        "observed_btjd": 1609.3793382125914,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 25,
            "predicted_btjd": 1601.378288466039,
            "offset_d": 8.001049746552326,
            "phase_offset": 0.1701611310823405,
            "linear_covariance_sigma_d": 1.9552342231164281
          },
          {
            "kind": 1,
            "cycle": 26,
            "predicted_btjd": 1613.798084222199,
            "offset_d": -4.418746009607503,
            "phase_offset": -0.09397502112574498,
            "linear_covariance_sigma_d": 3.166966739214188
          }
        ]
      },
      {
        "sector": 11,
        "event_kind": "candidate",
        "observed_btjd": 1615.6588325467392,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 25,
            "predicted_btjd": 1601.378288466039,
            "offset_d": 14.28054408070011,
            "phase_offset": 0.30370933942639766,
            "linear_covariance_sigma_d": 1.9552342231164281
          },
          {
            "kind": 1,
            "cycle": 26,
            "predicted_btjd": 1613.798084222199,
            "offset_d": 1.8607483245402818,
            "phase_offset": 0.03957318721831217,
            "linear_covariance_sigma_d": 3.166966739214188
          }
        ]
      },
      {
        "sector": 11,
        "event_kind": "candidate",
        "observed_btjd": 1622.9928370348425,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 25,
            "predicted_btjd": 1601.378288466039,
            "offset_d": 21.614548568803457,
            "phase_offset": 0.4596841850516704,
            "linear_covariance_sigma_d": 1.9552342231164281
          },
          {
            "kind": 1,
            "cycle": 26,
            "predicted_btjd": 1613.798084222199,
            "offset_d": 9.194752812643628,
            "phase_offset": 0.19554803284358496,
            "linear_covariance_sigma_d": 3.166966739214188
          }
        ]
      },
      {
        "sector": 11,
        "event_kind": "candidate",
        "observed_btjd": 1619.848996673383,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 25,
            "predicted_btjd": 1601.378288466039,
            "offset_d": 18.470708207343932,
            "phase_offset": 0.39282302947908043,
            "linear_covariance_sigma_d": 1.9552342231164281
          },
          {
            "kind": 1,
            "cycle": 26,
            "predicted_btjd": 1613.798084222199,
            "offset_d": 6.050912451184104,
            "phase_offset": 0.12868687727099495,
            "linear_covariance_sigma_d": 3.166966739214188
          }
        ]
      },
      {
        "sector": 38,
        "event_kind": "candidate",
        "observed_btjd": 2338.4038720490703,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 41,
            "predicted_btjd": 2353.7051866863517,
            "offset_d": -15.301314637281394,
            "phase_offset": -0.3254184248571272,
            "linear_covariance_sigma_d": 3.3069987531145606
          },
          {
            "kind": 1,
            "cycle": 41,
            "predicted_btjd": 2319.1045513037416,
            "offset_d": 19.299320745328714,
            "phase_offset": 0.41044542293479613,
            "linear_covariance_sigma_d": 4.418973473879491
          }
        ]
      },
      {
        "sector": 38,
        "event_kind": "candidate",
        "observed_btjd": 2352.018833773148,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 41,
            "predicted_btjd": 2353.7051866863517,
            "offset_d": -1.686352913203791,
            "phase_offset": -0.0358642588415858,
            "linear_covariance_sigma_d": 3.3069987531145606
          },
          {
            "kind": 1,
            "cycle": 42,
            "predicted_btjd": 2366.1249824425113,
            "offset_d": -14.106148669363392,
            "phase_offset": -0.30000041104966646,
            "linear_covariance_sigma_d": 4.504566158258341
          }
        ]
      },
      {
        "sector": 38,
        "event_kind": "candidate",
        "observed_btjd": 2342.5923990987467,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 41,
            "predicted_btjd": 2353.7051866863517,
            "offset_d": -11.112787587604998,
            "phase_offset": -0.2363395510944651,
            "linear_covariance_sigma_d": 3.3069987531145606
          },
          {
            "kind": 1,
            "cycle": 41,
            "predicted_btjd": 2319.1045513037416,
            "offset_d": 23.48784779500511,
            "phase_offset": 0.4995242966974582,
            "linear_covariance_sigma_d": 4.418973473879491
          }
        ]
      },
      {
        "sector": 38,
        "event_kind": "candidate",
        "observed_btjd": 2336.306631421545,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 41,
            "predicted_btjd": 2353.7051866863517,
            "offset_d": -17.398555264806873,
            "phase_offset": -0.37002117682543595,
            "linear_covariance_sigma_d": 3.3069987531145606
          },
          {
            "kind": 1,
            "cycle": 41,
            "predicted_btjd": 2319.1045513037416,
            "offset_d": 17.202080117803234,
            "phase_offset": 0.3658426709664873,
            "linear_covariance_sigma_d": 4.418973473879491
          }
        ]
      },
      {
        "sector": 65,
        "event_kind": "candidate",
        "observed_btjd": 3076.8562595074736,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 56,
            "predicted_btjd": 3059.011653767894,
            "offset_d": 17.844605739579492,
            "phase_offset": 0.37950748871092693,
            "linear_covariance_sigma_d": 4.626111130400744
          },
          {
            "kind": 1,
            "cycle": 57,
            "predicted_btjd": 3071.431449524054,
            "offset_d": 5.424809983419436,
            "phase_offset": 0.11537133650283662,
            "linear_covariance_sigma_d": 5.805786692658352
          }
        ]
      },
      {
        "sector": 65,
        "event_kind": "candidate",
        "observed_btjd": 3090.45046069551,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 57,
            "predicted_btjd": 3106.032084906664,
            "offset_d": -15.581624211153667,
            "phase_offset": -0.33137986687464094,
            "linear_covariance_sigma_d": 4.71478117952307
          },
          {
            "kind": 1,
            "cycle": 57,
            "predicted_btjd": 3071.431449524054,
            "offset_d": 19.019011171455986,
            "phase_offset": 0.40448398091727267,
            "linear_covariance_sigma_d": 5.805786692658352
          }
        ]
      },
      {
        "sector": 65,
        "event_kind": "candidate",
        "observed_btjd": 3086.2836825257664,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 57,
            "predicted_btjd": 3106.032084906664,
            "offset_d": -19.74840238089746,
            "phase_offset": -0.4199961995800248,
            "linear_covariance_sigma_d": 4.71478117952307
          },
          {
            "kind": 1,
            "cycle": 57,
            "predicted_btjd": 3071.431449524054,
            "offset_d": 14.852233001712193,
            "phase_offset": 0.3158676482118888,
            "linear_covariance_sigma_d": 5.805786692658352
          }
        ]
      },
      {
        "sector": 65,
        "event_kind": "candidate",
        "observed_btjd": 3071.6184764470313,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 56,
            "predicted_btjd": 3059.011653767894,
            "offset_d": 12.606822679137167,
            "phase_offset": 0.26811371937299244,
            "linear_covariance_sigma_d": 4.626111130400744
          },
          {
            "kind": 1,
            "cycle": 57,
            "predicted_btjd": 3071.431449524054,
            "offset_d": 0.1870269229771111,
            "phase_offset": 0.003977567164902125,
            "linear_covariance_sigma_d": 5.805786692658352
          }
        ]
      },
      {
        "sector": 100,
        "event_kind": "candidate",
        "observed_btjd": 4098.121065634713,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 78,
            "predicted_btjd": 4093.4611388208236,
            "offset_d": 4.659926813889342,
            "phase_offset": 0.09910429787716506,
            "linear_covariance_sigma_d": 6.587413870630139
          },
          {
            "kind": 1,
            "cycle": 79,
            "predicted_btjd": 4105.880934576984,
            "offset_d": -7.759868942271169,
            "phase_offset": -0.16503185433093492,
            "linear_covariance_sigma_d": 7.747836236123772
          }
        ]
      },
      {
        "sector": 100,
        "event_kind": "candidate",
        "observed_btjd": 4094.9783266169607,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 78,
            "predicted_btjd": 4093.4611388208236,
            "offset_d": 1.5171877961370228,
            "phase_offset": 0.03226656496745865,
            "linear_covariance_sigma_d": 6.587413870630139
          },
          {
            "kind": 1,
            "cycle": 79,
            "predicted_btjd": 4105.880934576984,
            "offset_d": -10.902607960023488,
            "phase_offset": -0.23186958724064133,
            "linear_covariance_sigma_d": 7.747836236123772
          }
        ]
      },
      {
        "sector": 100,
        "event_kind": "candidate",
        "observed_btjd": 4088.694276700031,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 78,
            "predicted_btjd": 4093.4611388208236,
            "offset_d": -4.766862120792666,
            "phase_offset": -0.10137852855335197,
            "linear_covariance_sigma_d": 6.587413870630139
          },
          {
            "kind": 1,
            "cycle": 79,
            "predicted_btjd": 4105.880934576984,
            "offset_d": -17.186657876953177,
            "phase_offset": -0.36551468076145194,
            "linear_covariance_sigma_d": 7.747836236123772
          }
        ]
      },
      {
        "sector": 100,
        "event_kind": "candidate",
        "observed_btjd": 4080.3148237647906,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 78,
            "predicted_btjd": 4093.4611388208236,
            "offset_d": -13.146315056033018,
            "phase_offset": -0.27958729296281487,
            "linear_covariance_sigma_d": 6.587413870630139
          },
          {
            "kind": 1,
            "cycle": 78,
            "predicted_btjd": 4058.860503438214,
            "offset_d": 21.454320326576635,
            "phase_offset": 0.45627655482909873,
            "linear_covariance_sigma_d": 7.65905285926998
          }
        ]
      },
      {
        "sector": 101,
        "event_kind": "candidate",
        "observed_btjd": 4124.306245840977,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 79,
            "predicted_btjd": 4140.481569959594,
            "offset_d": -16.175324118617027,
            "phase_offset": -0.34400629102866875,
            "linear_covariance_sigma_d": 6.676935307966834
          },
          {
            "kind": 1,
            "cycle": 79,
            "predicted_btjd": 4105.880934576984,
            "offset_d": 18.425311263992626,
            "phase_offset": 0.39185755676324485,
            "linear_covariance_sigma_d": 7.747836236123772
          }
        ]
      },
      {
        "sector": 101,
        "event_kind": "candidate",
        "observed_btjd": 4107.546772097614,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 78,
            "predicted_btjd": 4093.4611388208236,
            "offset_d": 14.085633276790304,
            "phase_offset": 0.2995641030006708,
            "linear_covariance_sigma_d": 6.587413870630139
          },
          {
            "kind": 1,
            "cycle": 79,
            "predicted_btjd": 4105.880934576984,
            "offset_d": 1.6658375206297933,
            "phase_offset": 0.03542795079257086,
            "linear_covariance_sigma_d": 7.747836236123772
          }
        ]
      },
      {
        "sector": 101,
        "event_kind": "candidate",
        "observed_btjd": 4102.309978715567,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 78,
            "predicted_btjd": 4093.4611388208236,
            "offset_d": 8.848839894743378,
            "phase_offset": 0.1881913815002706,
            "linear_covariance_sigma_d": 6.587413870630139
          },
          {
            "kind": 1,
            "cycle": 79,
            "predicted_btjd": 4105.880934576984,
            "offset_d": -3.570955861417133,
            "phase_offset": -0.07594477070782939,
            "linear_covariance_sigma_d": 7.747836236123772
          }
        ]
      },
      {
        "sector": 101,
        "event_kind": "candidate",
        "observed_btjd": 4110.690688550232,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 78,
            "predicted_btjd": 4093.4611388208236,
            "offset_d": 17.229549729408518,
            "phase_offset": 0.3664268768306193,
            "linear_covariance_sigma_d": 6.587413870630139
          },
          {
            "kind": 1,
            "cycle": 79,
            "predicted_btjd": 4105.880934576984,
            "offset_d": 4.809753973248007,
            "phase_offset": 0.10229072462251936,
            "linear_covariance_sigma_d": 7.747836236123772
          }
        ]
      },
      {
        "sector": 102,
        "event_kind": "candidate",
        "observed_btjd": 4132.684711614529,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 79,
            "predicted_btjd": 4140.481569959594,
            "offset_d": -7.79685834506472,
            "phase_offset": -0.16581852093304214,
            "linear_covariance_sigma_d": 6.676935307966834
          },
          {
            "kind": 1,
            "cycle": 80,
            "predicted_btjd": 4152.901365715754,
            "offset_d": -20.216654101224776,
            "phase_offset": -0.42995467314113245,
            "linear_covariance_sigma_d": 7.836655438000044
          }
        ]
      },
      {
        "sector": 102,
        "event_kind": "candidate",
        "observed_btjd": 4150.49369962783,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 79,
            "predicted_btjd": 4140.481569959594,
            "offset_d": 10.012129668236412,
            "phase_offset": 0.21293147310129956,
            "linear_covariance_sigma_d": 6.676935307966834
          },
          {
            "kind": 1,
            "cycle": 80,
            "predicted_btjd": 4152.901365715754,
            "offset_d": -2.4076660879236442,
            "phase_offset": -0.05120467910679073,
            "linear_covariance_sigma_d": 7.836655438000044
          }
        ]
      },
      {
        "sector": 102,
        "event_kind": "candidate",
        "observed_btjd": 4144.209120535205,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 79,
            "predicted_btjd": 4140.481569959594,
            "offset_d": 3.727550575611531,
            "phase_offset": 0.07927512541538718,
            "linear_covariance_sigma_d": 6.676935307966834
          },
          {
            "kind": 1,
            "cycle": 80,
            "predicted_btjd": 4152.901365715754,
            "offset_d": -8.692245180548525,
            "phase_offset": -0.18486102679270314,
            "linear_covariance_sigma_d": 7.836655438000044
          }
        ]
      },
      {
        "sector": 102,
        "event_kind": "candidate",
        "observed_btjd": 4128.495516350584,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 79,
            "predicted_btjd": 4140.481569959594,
            "offset_d": -11.986053609010014,
            "phase_offset": -0.2549116058429165,
            "linear_covariance_sigma_d": 6.676935307966834
          },
          {
            "kind": 1,
            "cycle": 79,
            "predicted_btjd": 4105.880934576984,
            "offset_d": 22.61458177359964,
            "phase_offset": 0.4809522419489971,
            "linear_covariance_sigma_d": 7.747836236123772
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
