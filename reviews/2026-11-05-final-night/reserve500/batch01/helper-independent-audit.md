# Independent helper audit

Reviewed delegation instructions and bounded evidence. Independent image reductions use the same TESS photons, not independent observing occasions. Gaia G flux ratios are rough potential-contaminant screens, not TESS-band eclipse depths.

- RS001: S101 3x3 aperture oscillates about 0.13 d, with 8.1% loss; deficit centroid 1.33 px from target and 0.18 px from G=12.07 Gaia DR3 6125690306996118016, consistent with neighbor contamination. Bright neighbor identification and catalogue association are lead's responsibility.
- RS002: S32 BTJD 2187.7 pixel aperture independently recovers bounded ~0.4% depression; difference centroid 0.47 px from target, low signal and centroid imprecision caution. No Gaia source within 3 px is bright enough under the conservative unattenuated G flux screen. Two outside: flux ratios .007 at 4.14 px and .159 at 5.17 px; deficit geometry favors target. S5/S32/S98 recurrence is observationally separate.
- RS003: no secure repeated bounded eclipses in reviewed all-sector context; no source localisation claimed.
- RS004: S6/S7/S33 recurrent narrow troughs, eclipse-like bycatch cannot be dismissed as monotonic ramps. S7 at 1493.764 target 3x3 pixel aperture fails to reproduce QLP dip, with deficit toward cutout edge; spatial origin unresolved. Other S34/S61/S88 show severe instrumental ramps. Plausible or host-ambiguous outcome fits limitations; no claimed target localization.
- RS005: S67 aperture recovers ~6.5% bounded eclipse with centroid 0.18 px from target; only potentially capable bright Gaia neighbor within 3 px at 2.62 px (G flux ratio .14), disfavored by centroid.
- RS006: S40 aperture recovers ~1.8% bounded eclipse, centroid 0.15 px from target. Potentially capable Gaia neighbors are at 1.93–2.95 px; target-favored centroid disfavors these, with unresolved sources and color caveats.
- RS007: S56 aperture recovers ~12.6% flat-bottom event, target-centered centroid 0.10 px; no Gaia neighbor within 3 px has sufficient unattenuated G flux under conservative screen. ROT/ASASSN labels do not decide eclipse morphology or imply known EB.
- RS008: S102 aperture recovers ~20.9% eclipse, centroid 0.07 px from target; no capable Gaia neighbor within 3 px by conservative screen. Deep S37/S102 interval is 48 cycles, P=38.0585127727 d. Shallow S11/S37 separation /19 gives ~38.058648 d, providing independent event-kind interval compatible with selected integer family; truncated S64 does not supply precision timing.

45/45 original raw-source and initial pixel-cutout SHA-256 hashes reproduced; each raw QLP TICID/sector header matches. RS002 later cutout and RS004 wider cutout receipts remain in their respective JSON files. The five selected WLS clocks' residuals and endpoint calculations match. Formal period errors are conditional on chosen events, cycle counts, timing model and error floor, not full precision guarantees. Fixed-cycle, nominal-unwrapped nonlinear 100,000-draw Gaia covariance check uses edge-on conjunction geometry; relevant conjunction 3-sigma residual intervals include zero for all five. See helper-nonlinear-gaia.json. Evidence supports strong repeated on-target eclipses for RS002/005/006/007/008 subject to the lead's final classification and alias/coverage assessment; physical review remains separate from novelty.

Thank you, the project coordinator.

