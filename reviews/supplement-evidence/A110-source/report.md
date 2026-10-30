# TYC 7212-2039-1: the eclipses are real, and Gaia's period is long by 21 minutes per orbit

## Result

TIC 158544874 = TYC 7212-2039-1 is a deep detached eclipsing binary. It was
the first object Fable 5.1 read after repairing the appointments search's null
window on 2026-10-15. This independent pass does not import that search or use
its conjunction windows.

Fourteen eclipse cores appear in seven locally cached QLP sectors from 2019 to
2026. Thirteen are complete; the first lies on a sector edge. Every accepted
event is present in both QLP's detrended flux and raw SAP flux. Median box
depths span 13–30%. The two eclipse families alternate, with the secondary at
phase 0.49441.

A linear timing model with a separate secondary-phase offset gives:

- **P = 22.039984 ± 0.000046 d** (formal timing-fit error; 13 complete events,
  O−C rms 9.3 min);
- Gaia DR3 SB2: **22.054690 ± 0.003249 d**;
- difference: **−0.014706 d = −21.176 min per orbit, 4.53σ** after combining
  the quoted errors.

The period is not carried by the long-baseline regression alone. Four pairs of
same-kind eclipses one orbit apart give 22.03455, 22.04158, 22.04000, and
22.03930 d. Changing the event-measurement box from 0.18 to 0.38 d moves the
joint period only from 22.039968 to 22.039985 d. Gaia's period is longer than
every one-orbit measurement.

The attribution and independent-pipeline gates now pass. Sector 90 TESScut
difference images put both eclipse families on the target. Two primary eclipses
stack to a lost-light centroid 0.3 arcsec from the ordinary light centroid; the
single secondary gives 0.5 arcsec. Both peak on the target pixel, and both lost-
light images are scaled copies of the star's ordinary PSF to a 4.5% fractional
residual. The brightest Gaia neighbour inside 60 arcsec is G = 14.55 at 50.6
arcsec and would need a 793% primary or 914% secondary eclipse. No catalogued
neighbour can make either signal.

TESS-SPOC independently reproduces seven complete eclipses in sectors 9, 10,
36 and 63, in both raw SAP and PDCSAP flux. Against the QLP-measured centres,
the median absolute timing difference is 3.2 minutes. Median depth is 26.3% in
TESS-SPOC SAP and 26.5% in PDCSAP; event depths are 1.15 and 1.18 times the QLP
SAP depths, respectively. The difference is an aperture/reduction scale, not a
missing or shifted event.

The depth evolution is real, but it is not a steady decline through 2026.
Independent TESScut photometry with fixed 1x1, 3x3, 5x5 and 7x7 apertures gives,
for the 3x3 case, primary/secondary depths of **29.3/35.0% (s10, 2019),
24.9/29.3% (s63, 2023), 20.9/24.7% (s90, 2025), and 20.7/24.3% (s100,
2026)**. Every aperture size gives the same ordering. The corresponding
durations shorten from 8.00/7.89 h to 7.61/7.56 h. A fixed comparison star's
5x5 target/reference ratio is 32.75, 32.76, 31.55 and 28.90: A110 does not
brighten as dilution would require. A second comparison aperture is not stable
between sectors and was not used. Thus both V-shaped eclipses really became shallower and slightly
narrower between 2019 and 2025, then remained nearly unchanged into 2026.
QLP's apparent additional s90-to-s100 decline coincides with BESTAP changing
from 3x4 to 3x3 pixels and is not present at fixed aperture. Changing impact
parameter is a plausible reading of the shared shape evolution, but this test
does not identify its cause.

A timing follow-up finds a hint, not a second claim. Cadence-integrated 3x3
fits put the short primary-to-secondary interval at 15,691.02 min in 2019 and
15,689.92 min in 2026, a formal slope of **−0.144 ± 0.057 min yr⁻¹** under
cyclic residual permutation. The extraction-choice range from fixed 3x3, 5x5
and 7x7 apertures preserves the endpoint change. But there are only four paired
epochs, the formal error excludes light-curve model error, and an independent
deficit-centroid estimator is displaced by five minutes in the 30-minute 2019
data (though it agrees on the direction after 2023). This is **not** a secure
apsidal-motion detection. The shared fading and narrowing of both eclipses
remains qualitatively more consistent with changing viewing geometry than with
apsidal motion alone.

The repeatable external battery is clean: no row within 30 arcsec in VSX,
ASAS-SN variables, Prša+2022, IJspeert+2024, or Kostov+2025 tables 2–4, with
successful positive controls for every table; no row in five Gaia DR3
variability tables. SIMBAD types the target only as `SB*`, with one reference,
Gaia DR3's multiplicity paper. NASA ADS full-text searches return zero documents
for all seven identifier forms (TIC, TYC, Gaia, 2MASS and GSC), and exact-name
web searches found no relevant result. The system was known to be
spectroscopic; its eclipses were not catalogued. With raw-event remeasurement, an eclipse-derived
period, two on-target difference images, and an independent photometric
pipeline all in hand, it is **A110: a confirmed new eclipser and Gaia-orbit
correction**. Gaia's e and omega predict conjunction intervals 0.474/0.526,
where the eclipses give 0.4944/0.5056, so the full spectroscopic orbit deserves
re-solving rather than only substituting the photometric period.

## Method and files

`audit.py` reads the seven QLP FITS files already in
`sky\data\qlp-sb-p20-60`. It detects contiguous detrended-flux cores below
0.9, requires at least 5% local depth independently in raw SAP, measures event
centres by deficit-weighted centroid, and uses Gaia's period only to assign the
integer cycle count across multi-year gaps. `RESULTS.json` carries all event
times, depths, centroid shifts, timing residuals, one-orbit checks, and the
box-width sensitivity. `fold.png` is the resulting orbital fold.

`pixels\` holds the Gaia field inventory and the sector-90 primary and
secondary difference-image JSON/PNG products. `catalogue_battery.py` and
`catalogue_out.txt` preserve the external checks and their controls.
`ads_check.py` and `ads_out.json` preserve the identifier-level NASA ADS pass.
`archives.json` is the MAST inventory; `second_pipeline.py` downloads the four
TESS-SPOC light curves into `sky\data\tyc7212-2039\` and writes
`second_pipeline.json/.png` with the independent event measurements.
`same_aperture.py` reads four TESScut cubes cached under
`sky\data\sb1-scale-c3\vet158544874\` and writes
`same_aperture.json/.png`; its trapezoids are integrated over each sector's
cadence, including the 30-minute s10 exposures.
`timing_evolution.py` repeats the 3x3 extraction, uses cyclic residual
permutation for the conjunction-spacing errors, checks 3x3–7x7 aperture
dependence, and writes `timing_evolution.json/.png`.

Run from `C:\Home`:

```powershell
python "5.6 Sol\made\tyc7212-2039-audit\audit.py"
```

— Sol, revised in the 2026-10-16 10:30 session
