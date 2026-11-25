# Asteroid crossings in the 154-target TESS review

Five brightening alerts track known asteroids crossing TESS stellar apertures. Two different asteroids account for the two TIC 186817099 events. All exposures used for the five orbit identifications have QLP-independent TESScut quality 0. [Five-crossing montage](pulse-sequences.jpg) · [Side-by-side TIC 186817099 movie](motion-186817099-pair.gif)

| TIC | Sector | Asteroid | First to last measured exposure (UTC) | Positions checked / measured | Residual range (arcsec) |
| --- | ---: | --- | --- | ---: | ---: |
| 153687101 | 87 | [(914) Palisana](motion-153687101-s87-track-914.csv) | 2024-12-24 08:57:51.082 to 2024-12-24 15:01:11.072 | 35 / 110 | 3.27–4.20 |
| 52300257 | 6 | [(740) Cantabia](motion-52300257-s6-track-740.csv) | 2019-01-04 12:14:35.131 to 2019-01-04 18:14:35.122 | 13 / 13 | 1.47–2.04 |
| 186817099 | 45 | [(4613) Mamoru](motion-186817099-s45-track-4613.csv) | 2021-11-17 12:33:56.841 to 2021-11-17 18:53:56.831 | 35 / 39 | 0.02–1.37 |
| 186817099 | 46 | [(16431) 1988 VH1](motion-186817099-s46-track-16431.csv) | 2021-12-29 09:43:53.713 to 2021-12-29 16:03:53.703 | 35 / 39 | 0.42–5.91 |
| 171556893 | 48 | [(2850) Mozhaiskij](motion-171556893-s48-track-2850.csv) | 2022-02-20 20:23:51.728 to 2022-02-21 02:13:51.718 | 35 / 36 | 0.48–1.62 |

At TIC 153687101, the finder also returns (273055) 2006 DJ173 close to one measured position. Full-track residuals distinguish it from Palisana. Its minimum residual is 3.89 arcsec, but the median is 33.61 arcsec and the maximum 75.09 arcsec. Predicted V is 20.6 compared with 13.2 for Palisana, equivalent to roughly 0.11% of Palisana's V-band flux. The orbit comparison alone excludes it as the dominant observed crossing. The farther candidate 2006 OW32 has a 357.88 arcsec median residual. [Candidate comparisons](motion-candidate-comparisons.csv)

The S45 TIC 171556893 pulse persists in TESS-SPOC, but the 21 native-image position fits all use quality-2048 exposures. They scatter by 4.05 pixels around the fitted path, versus 0.011–0.103 pixels for the five coherent tracks. The point pattern supplies no asteroid identification. Its origin remains unresolved. [S45 image fits](motion-171556893-s45.csv) · [Independent flux curves](spoc-171556893.png)

## Measurements

The script subtracts the median off-event image and fits the positive moving point in native 15 by 15 pixel frames. It records the fitted location, time and exposure quality for every retained position. A motion fit must span at least 2 pixels and have position-fit scatter below 0.35 pixels. Sky coordinates use the native WCS and undo each frame's barycentric timestamp correction before obtaining its UTC time. JPL SB_IDENT proposes candidates from the TESS state vector. JPL Horizons then returns apparent tracks for observer 500@-95 (TESS), evaluated at up to 35 measured timestamps uniformly spanning the measured track. The accepted match has the smallest median angular residual and no sampled residual over 10 arcsec. Minima, medians and maxima are measured residuals and include the absolute TESS WCS error. [Orbit summary](motion-orbits.csv) · [Response bytes, checksums and request URLs](motion-receipts.csv)

Run python -B moving.py ../../../tmp/mixed154-work/pixels from this directory. Cached API response bodies are reused. Every response JSON is preserved byte-for-byte beside its request URL. The per-event motion CSV preserves every fitted position, and the individual candidate tracks give the sampled Horizons predictions and angular residuals.
