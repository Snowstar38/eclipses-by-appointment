# RS026 — TIC 352725084

Lead physical verdict: PLAUSIBLE target single eclipse. No publication claim. Fresh Terra helper independently agrees with the deciding morphology and pixel interpretation; see `HELPER-NOTE.md` and `helper-hash-identity-audit.json`.

## Identity, raw morphology and recurrence

Exact queue identity is Gaia DR3 2023283918354633344 (G 11.9167), not neighboring TIC 352725094. FITS TIC/sector headers and SHA256 checks accompany `lead-context.json`. Quality-zero, finite positive raw QLP SAP flux was examined in every available QLP sector: 14, 40, 54, 80 and 81. Full-sector plots show broad variability and offsets in the earlier data, with one convincing discrete event in S81. The event has sharp resolved ingress and egress and a rounded, approximately flat bottom. A local sloping-baseline trapezoid gives BTJD 3521.833249, formal covariance timing error 0.000715 d, depth 38.736 ppt, total duration 0.410736 d and ingress 0.079341 d. This is a descriptive single-event fit, with residual RMS 2.620 ppt; its formal error is not a calibrated timing-systematics allowance.

The current MAST Tesscut inventory independently lists only those five sectors; no newer available sector was silently ignored. An event-anchored Gaia-period recurrence check finds the earlier S40 center at 2404.616 d in a gap and no other fully covered repeat. Earlier full-sector curves do not supply another convincing same-kind eclipse. Missing coverage is not a clean null. There is no measured orbital period, no integer-cycle solution, and no basis for treating this singleton as probable merely because it occurs near a Gaia conjunction.

## Source pixels and alternative extraction

A seven-pixel S81 TESScut cube yields a sky-subtracted central 3x3 extraction recovering 35.391 ppt median core loss. The out-minus-in difference peaks at pixel (4,4), against target WCS (3.921,3.703). Positive-deficit centroid (3.829,3.733) is 0.0966 pixel from the target; this is a descriptive centroid, not a formal localization confidence region. The image supports target attribution. The independently chosen aperture uses the same TESS photons and is not another observing occasion.

The IJspeert neighbor TIC 352725094 / Gaia DR3 2023282440885901056 lies 45.285 arcsec away and around two pixels to the right in this sector. Its position does not host the S81 deficit peak. We do not substitute that neighbor for the target or automatically assign its prior classification to this event. Nearby unresolved sources and pixel calibration limit absolute attribution precision, but the resolved known neighbor does not explain this image. `lead-localization-81.png`, `lead-pixel-diagnostics.png`, neighbor table, cube hash and numerical extraction are retained.

## Gaia association and plausibility

The exact target SB1 orbit gives P=42.969910806 d, e=0.653118, mass function 0.03629 solar masses. Its conjunction-A extrapolation is BTJD 3523.04038, 1.20713 d after the event, with fixed-cycle local covariance sigma 1.47567 d. The event is consistent within that broad orbital uncertainty; this is not an ephemeris measurement, evidence of recurrence or secure association. The covariance uses the target's own P,e,omega,Tp correlations (SB1 parameter order documented in `lead-gaia-covariance.json`). The short finite eclipse shape is physically reasonable; no stellar-radius or inclination characterization is claimed. A nonlinear posterior and exhaustive alias search were not performed because no measured repeat exists.

## Catalogue scope and disposition

The shared sealed catalogue bundle is reused with hashes in `lead-central-catalogue-receipts.json`. Target VSX and ASAS-SN cones have no match; exact target Gaia DR3 EB query has no row; SIMBAD classifies the target SB*, not as eclipsing. Prsa and IJspeert have no exact-target eclipsing identity; the IJspeert neighbor is adjudicated above. Vetted Kostov tables 3/4 have no target match. The bounded 244-eprint identifier search has no exact TIC/Gaia hit, without establishing exhaustive discovery priority. These successful scoped checks do not promote a singleton. Keep the physical verdict separate from novelty.

Limitation and next check: observe another same-kind event and determine its clock; target-localized single events alone remain plausible under current methods 2.7/2.9. No addition to a confirmed/probable register is authorized by this report.
