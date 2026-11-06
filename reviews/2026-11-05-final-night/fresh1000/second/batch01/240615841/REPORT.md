# Z102 TIC 240615841

Final lead verdict: REFUTED. Independent helper audit complete; see ../helper-independent-audit.md. Gaia DR3 1973900899772254464; G=11.867113; queue frozen without substitution. Association: off-target repeated eclipse; no target by-catch claim.

Repeated deep discrete eclipses give14.92577962d, whereas target Gaia period57.28576066d. Difference Gaussian center(5.503,4.028) lies1.190pixels from target and0.09pixel from Gaia1973900968491727872 position(5.52,3.94). IJspeert TIC240615813/Gaia1973900895467234176 is at(4.70,4.14); its QLP aperture shares the clock but is not independent source attribution. Positive off-target signal refutes this intended target claim.

Limitations: Crowded field; true contaminating EB identity is not uniquely assigned here; neighbor QLP shares photons.

Next check: Characterize contaminating source separately with PRF modeling or higher resolution; no substitution into target result.

## Numeric evidence and provenance

Identity-audit.json verifies exact TIC FITS headers, sectors, Gaia identity and actual phot_g_mean_mag against the frozen fresh-band-next1000 population and all source SHA256 values. lead-context.json lists representative raw SAP events and quality0 coverage; lead-timing.json stores local trapezoid fits and failure flags. Independent TESScut aperture reduction and difference images share the same TESS photons. These are reduction checks, not independent observing occasions. Gaia neighbor response is a126arcsec cone queried via Heidelberg TAP; lead-neighbors.json records source pixel positions and relative G flux. G flux is an approximate contaminant capability screen, not a calibrated TESS passband or pixel-loss comparison.

```json
{
  "clock": {
    "period_d": 14.925779621252332,
    "epoch_btjd": 1718.835074485306,
    "formal_period_error_d": 8.221143503064434e-05,
    "cycles": [
      0,
      111,
      112,
      124
    ],
    "times": [
      1718.8340804476447,
      3375.596626952755,
      3390.5227549678257,
      3569.631406750521
    ],
    "residuals": [
      -0.0009940376612576074,
      1.4508440017380053e-05,
      0.0003629022585300845,
      -0.0003407700742172892
    ],
    "duration_d": 0.15549750340280521,
    "depth_ppt": 274.9191776201012,
    "max_residual_d": 0.0009940376612576074,
    "gaia_period_d": 57.28576066283012,
    "note": "Trials inferred from eclipse intervals; integer-cycle selection requires covered-window audit. Timing error includes cadence/2 and .002d floors."
  },
  "localization": {
    "tic": "240615841",
    "event": {
      "sector": 83,
      "screen_btjd": 3569.6255098465213,
      "kind": "candidate",
      "n": 775,
      "cadence_d": 0.002314810544703505,
      "first_btjd": 3568.727363003505,
      "last_btjd": 3570.5236559355785,
      "scale_sap": 1.0005109310150146,
      "noise_ppt": 3.6551418259303525,
      "source_sha256": "63e80af9f5007afc7b8e873141a55a67e2d309e51be6aea991646ee591335575",
      "center_btjd": 3569.631406750521,
      "center_formal_error_d": 0.00011726552517153568,
      "depth_ppt": 277.6447180210609,
      "duration_d": 0.1555922718376704,
      "ingress_d": 0.07011760125613734,
      "baseline_slope_d": -0.001505533764420183,
      "residual_rms_ppt": 3.407044822799263,
      "fit_usable": true
    },
    "ra": 326.3455184,
    "dec": 44.9665228623,
    "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/artDs8NVSX43LUCr/astrocut_326.3455184_44.9665228623_11.0x11.0px.zip",
    "zip_sha256": "674683da4dbb15d70379266714d8824d2cff3b39e2cee4c696123559e407b870",
    "fits_sha256": "8ea434acbda556aa81ce4e726e535ec5fae105a6b12c8909efbca1843ac50b98",
    "target_xy": [
      5.543513037036479,
      5.2177604854222945
    ],
    "core_n": 34,
    "side_n": 169,
    "aperture_loss": 0.08194989692129828,
    "diff_peak_xy": [
      6,
      4
    ],
    "positive_diff_centroid_xy": [
      5.369360388603444,
      4.31229014811156
    ],
    "centroid_offset_pixels": 0.9220659828373754,
    "status": "measured"
  },
  "timing": [
    {
      "sector": 15,
      "screen_btjd": 1718.842509063042,
      "kind": "candidate",
      "n": 77,
      "cadence_d": 0.020834352343172213,
      "first_btjd": 1717.9466319113958,
      "last_btjd": 1719.5300426870012,
      "scale_sap": 1.0013992190361023,
      "noise_ppt": 3.0595016597829496,
      "source_sha256": "51efdf22e9f0713e736df7a028b9173a5d56aa0e9ea7d083ea0eac45eb8bfe99",
      "center_btjd": 1718.8340804476447,
      "center_formal_error_d": 0.00029467370869229584,
      "depth_ppt": 276.5036407993692,
      "duration_d": 0.1577757981305983,
      "ingress_d": 0.06890238957124895,
      "baseline_slope_d": -0.0036470972670978206,
      "residual_rms_ppt": 1.8371402793721432,
      "fit_usable": true
    },
    {
      "sector": 16,
      "screen_btjd": 1753.9100308821337,
      "kind": "candidate",
      "n": 87,
      "cadence_d": 0.020833015076959782,
      "first_btjd": 1753.0142107936015,
      "last_btjd": 1754.805850158541,
      "scale_sap": 1.0024638175964355,
      "noise_ppt": 2.8279371494050065,
      "source_sha256": "8b2d8b9e9f8eb3c111bb96b336e2753eb035e4b18b5747ed23b3951bdfc147a2",
      "center_btjd": 1753.9061467523243,
      "center_formal_error_d": 0.0006710847203049352,
      "depth_ppt": 159.12081427328576,
      "duration_d": 0.3200591256821033,
      "ingress_d": 0.12974782538369958,
      "baseline_slope_d": 0.003202935437810743,
      "residual_rms_ppt": 1.522306835624611,
      "fit_usable": true
    },
    {
      "sector": 56,
      "screen_btjd": 2843.485991108149,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.002314796584641954,
      "first_btjd": 2842.587849679337,
      "last_btjd": 2844.3841318373693,
      "scale_sap": 1.0018205046653748,
      "noise_ppt": 3.107568159443461,
      "source_sha256": "2a152abaee1b93f2672664111d3783d3e52183905780e4ee6e9436d9d3253ca1",
      "center_btjd": 2843.485556312381,
      "center_formal_error_d": 0.000248002931744553,
      "depth_ppt": 157.1198022184808,
      "duration_d": 0.32367044652441584,
      "ingress_d": 0.13528805553268536,
      "baseline_slope_d": -0.00049889059699102,
      "residual_rms_ppt": 3.124902554233079,
      "fit_usable": true
    },
    {
      "sector": 56,
      "screen_btjd": 2828.5623701328764,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.0023148308600866585,
      "first_btjd": 2827.664215410297,
      "last_btjd": 2829.460524177279,
      "scale_sap": 0.9958752989768982,
      "noise_ppt": 5.415194300459961,
      "source_sha256": "2a152abaee1b93f2672664111d3783d3e52183905780e4ee6e9436d9d3253ca1",
      "center_btjd": 2828.559934466192,
      "center_formal_error_d": 0.00043235305698688766,
      "depth_ppt": 156.53615227941893,
      "duration_d": 0.323138782231185,
      "ingress_d": 0.1342785167385114,
      "baseline_slope_d": -0.005305880943025157,
      "residual_rms_ppt": 3.255791147521378,
      "fit_usable": true
    },
    {
      "sector": 76,
      "screen_btjd": 3375.5946765430594,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.002314795566007888,
      "first_btjd": 3374.6965363348904,
      "last_btjd": 3376.492817685537,
      "scale_sap": 0.998031884431839,
      "noise_ppt": 3.9542471984247394,
      "source_sha256": "d3216f33048ee94b10211203aee561e12016fe5b41d50261cda9134ece2cf260",
      "center_btjd": 3375.596626952755,
      "center_formal_error_d": 0.00012903168291273124,
      "depth_ppt": 273.33471444083324,
      "duration_d": 0.15481331625359188,
      "ingress_d": 0.06905849166865229,
      "baseline_slope_d": -1.6373929909163114e-05,
      "residual_rms_ppt": 4.0787289283365595,
      "fit_usable": true
    },
    {
      "sector": 76,
      "screen_btjd": 3390.525222912753,
      "kind": "candidate",
      "n": 777,
      "cadence_d": 0.002314831271633011,
      "first_btjd": 3389.627068833192,
      "last_btjd": 3391.4233779181063,
      "scale_sap": 0.9961713254451752,
      "noise_ppt": 5.190835578918109,
      "source_sha256": "d3216f33048ee94b10211203aee561e12016fe5b41d50261cda9134ece2cf260",
      "center_btjd": 3390.5227549678257,
      "center_formal_error_d": 0.0001707149916130934,
      "depth_ppt": 273.09388847652286,
      "duration_d": 0.15540273496794002,
      "ingress_d": 0.06954969358083095,
      "baseline_slope_d": -0.004308665773541798,
      "residual_rms_ppt": 4.004841728062758,
      "fit_usable": true
    },
    {
      "sector": 76,
      "screen_btjd": 3380.8168713720424,
      "kind": "candidate",
      "n": 628,
      "cadence_d": 0.002314809112704097,
      "first_btjd": 3379.918725678367,
      "last_btjd": 3381.7150176915115,
      "scale_sap": 0.9986352324485779,
      "noise_ppt": 4.32688137906416,
      "source_sha256": "d3216f33048ee94b10211203aee561e12016fe5b41d50261cda9134ece2cf260",
      "center_btjd": 3380.8122940751796,
      "center_formal_error_d": 0.0003382200174411626,
      "depth_ppt": 160.26009181325838,
      "duration_d": 0.3203333977615648,
      "ingress_d": 0.133758782232467,
      "baseline_slope_d": -0.001783483530214198,
      "residual_rms_ppt": 4.110867389307646,
      "fit_usable": true
    },
    {
      "sector": 83,
      "screen_btjd": 3569.6255098465213,
      "kind": "candidate",
      "n": 775,
      "cadence_d": 0.002314810544703505,
      "first_btjd": 3568.727363003505,
      "last_btjd": 3570.5236559355785,
      "scale_sap": 1.0005109310150146,
      "noise_ppt": 3.6551418259303525,
      "source_sha256": "63e80af9f5007afc7b8e873141a55a67e2d309e51be6aea991646ee591335575",
      "center_btjd": 3569.631406750521,
      "center_formal_error_d": 0.00011726552517153568,
      "depth_ppt": 277.6447180210609,
      "duration_d": 0.1555922718376704,
      "ingress_d": 0.07011760125613734,
      "baseline_slope_d": -0.001505533764420183,
      "residual_rms_ppt": 3.407044822799263,
      "fit_usable": true
    },
    {
      "sector": 83,
      "screen_btjd": 3559.917153244811,
      "kind": "candidate",
      "n": 571,
      "cadence_d": 0.002314829580427613,
      "first_btjd": 3559.442612931243,
      "last_btjd": 3560.81530694574,
      "scale_sap": 1.003277063369751,
      "noise_ppt": 3.2227148970937627,
      "source_sha256": "63e80af9f5007afc7b8e873141a55a67e2d309e51be6aea991646ee591335575",
      "center_btjd": 3559.9202821797344,
      "center_formal_error_d": 0.0002478420190509512,
      "depth_ppt": 163.18802262492437,
      "duration_d": 0.3241549351893974,
      "ingress_d": 0.13424854948984072,
      "baseline_slope_d": 0.002344126621026167,
      "residual_rms_ppt": 3.174862113199389,
      "fit_usable": true
    },
    {
      "sector": 83,
      "screen_btjd": 3574.847763568296,
      "kind": "candidate",
      "n": 768,
      "cadence_d": 0.0023147243787207117,
      "first_btjd": 3573.949649993923,
      "last_btjd": 3575.745876093343,
      "scale_sap": 0.998218297958374,
      "noise_ppt": 2.830049552991209,
      "source_sha256": "63e80af9f5007afc7b8e873141a55a67e2d309e51be6aea991646ee591335575",
      "center_btjd": 3574.846531440827,
      "center_formal_error_d": 0.0002213612302972663,
      "depth_ppt": 160.8534894210392,
      "duration_d": 0.32310057065876613,
      "ingress_d": 0.1322181088621491,
      "baseline_slope_d": 0.0001757245618760399,
      "residual_rms_ppt": 3.1856061543063032,
      "fit_usable": true
    }
  ],
  "gaia_geometry": {
    "source_id": "1973900899772254464",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 57.28576066283012,
    "gaia_period_error_d": 0.09367996,
    "eccentricity": 0.369853402692169,
    "omega_deg": 151.31669218826787,
    "tp_btjd": 363.92181709301246,
    "mass_function_solar": 0.001565030915664596,
    "events": [
      {
        "sector": 15,
        "event_kind": "candidate",
        "observed_btjd": 1718.8340804476447,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 23,
            "predicted_btjd": 1734.1437337710097,
            "offset_d": -15.309653323364955,
            "phase_offset": -0.2672505897839745,
            "linear_covariance_sigma_d": 2.384233307819304
          },
          {
            "kind": 1,
            "cycle": 23,
            "predicted_btjd": 1693.6983495482236,
            "offset_d": 25.135730899421105,
            "phase_offset": 0.4387779896537261,
            "linear_covariance_sigma_d": 2.251290664558351
          }
        ]
      },
      {
        "sector": 16,
        "event_kind": "candidate",
        "observed_btjd": 1753.9061467523243,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 23,
            "predicted_btjd": 1734.1437337710097,
            "offset_d": 19.762412981314583,
            "phase_offset": 0.3449794984417031,
            "linear_covariance_sigma_d": 2.384233307819304
          },
          {
            "kind": 1,
            "cycle": 24,
            "predicted_btjd": 1750.984110211054,
            "offset_d": 2.922036541270245,
            "phase_offset": 0.0510080778793989,
            "linear_covariance_sigma_d": 2.3221577462361296
          }
        ]
      },
      {
        "sector": 56,
        "event_kind": "candidate",
        "observed_btjd": 2843.485556312381,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 42,
            "predicted_btjd": 2822.5731863647816,
            "offset_d": 20.912369947599473,
            "phase_offset": 0.36505354394584255,
            "linear_covariance_sigma_d": 4.070270957917592
          },
          {
            "kind": 1,
            "cycle": 43,
            "predicted_btjd": 2839.413562804826,
            "offset_d": 4.071993507554907,
            "phase_offset": 0.07108212338353431,
            "linear_covariance_sigma_d": 3.8581477156830424
          }
        ]
      },
      {
        "sector": 56,
        "event_kind": "candidate",
        "observed_btjd": 2828.559934466192,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 42,
            "predicted_btjd": 2822.5731863647816,
            "offset_d": 5.986748101410285,
            "phase_offset": 0.10450674010679216,
            "linear_covariance_sigma_d": 4.070270957917592
          },
          {
            "kind": 1,
            "cycle": 43,
            "predicted_btjd": 2839.413562804826,
            "offset_d": -10.85362833863428,
            "phase_offset": -0.18946468045551604,
            "linear_covariance_sigma_d": 3.8581477156830424
          }
        ]
      },
      {
        "sector": 76,
        "event_kind": "candidate",
        "observed_btjd": 3375.596626952755,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 52,
            "predicted_btjd": 3395.430792993083,
            "offset_d": -19.834166040328,
            "phase_offset": -0.3462320445924951,
            "linear_covariance_sigma_d": 4.983952043857848
          },
          {
            "kind": 1,
            "cycle": 52,
            "predicted_btjd": 3354.985408770297,
            "offset_d": 20.611218182457833,
            "phase_offset": 0.3597965348452015,
            "linear_covariance_sigma_d": 4.646877466394185
          }
        ]
      },
      {
        "sector": 76,
        "event_kind": "candidate",
        "observed_btjd": 3390.5227549678257,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 52,
            "predicted_btjd": 3395.430792993083,
            "offset_d": -4.908038025257156,
            "phase_offset": -0.08567640489483344,
            "linear_covariance_sigma_d": 4.983952043857848
          },
          {
            "kind": 1,
            "cycle": 53,
            "predicted_btjd": 3412.2711694331274,
            "offset_d": -21.74841446530172,
            "phase_offset": -0.37964782545714165,
            "linear_covariance_sigma_d": 4.735671161927421
          }
        ]
      },
      {
        "sector": 76,
        "event_kind": "candidate",
        "observed_btjd": 3380.8122940751796,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 52,
            "predicted_btjd": 3395.430792993083,
            "offset_d": -14.618498917903253,
            "phase_offset": -0.25518556005469034,
            "linear_covariance_sigma_d": 4.983952043857848
          },
          {
            "kind": 1,
            "cycle": 52,
            "predicted_btjd": 3354.985408770297,
            "offset_d": 25.82688530488258,
            "phase_offset": 0.4508430193830063,
            "linear_covariance_sigma_d": 4.646877466394185
          }
        ]
      },
      {
        "sector": 83,
        "event_kind": "candidate",
        "observed_btjd": 3569.631406750521,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 55,
            "predicted_btjd": 3567.288074981573,
            "offset_d": 2.3433317689477917,
            "phase_offset": 0.040906007737944956,
            "linear_covariance_sigma_d": 5.259642679436386
          },
          {
            "kind": 1,
            "cycle": 56,
            "predicted_btjd": 3584.1284514216177,
            "offset_d": -14.497044671096774,
            "phase_offset": -0.25306541282436323,
            "linear_covariance_sigma_d": 5.003121632624182
          }
        ]
      },
      {
        "sector": 83,
        "event_kind": "candidate",
        "observed_btjd": 3559.9202821797344,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 55,
            "predicted_btjd": 3567.288074981573,
            "offset_d": -7.367792801838732,
            "phase_offset": -0.12861473281648028,
            "linear_covariance_sigma_d": 5.259642679436386
          },
          {
            "kind": 1,
            "cycle": 56,
            "predicted_btjd": 3584.1284514216177,
            "offset_d": -24.208169241883297,
            "phase_offset": -0.42258615337878846,
            "linear_covariance_sigma_d": 5.003121632624182
          }
        ]
      },
      {
        "sector": 83,
        "event_kind": "candidate",
        "observed_btjd": 3574.846531440827,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 55,
            "predicted_btjd": 3567.288074981573,
            "offset_d": 7.558456459254103,
            "phase_offset": 0.13194302339356748,
            "linear_covariance_sigma_d": 5.259642679436386
          },
          {
            "kind": 1,
            "cycle": 56,
            "predicted_btjd": 3584.1284514216177,
            "offset_d": -9.281919980790462,
            "phase_offset": -0.1620283971687407,
            "linear_covariance_sigma_d": 5.003121632624182
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
