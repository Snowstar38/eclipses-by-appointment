# Image-side pilot review

`inspect_stamp.py CONFIG.json OUTPUT_DIR` reads an original SPOC target-pixel FITS file, identifies the pipeline aperture, and plots five quality-zero median frames relative to a selected temporal baseline. The top row restores FLUX+BKG to expose positive moving flux; the bottom row shows FLUX differences. Yellow outlines the target aperture. Green crosses mark the largest positive pixel, but **a maximum is always present**, even in pure noise. Evidence includes positions, spacecraft UTC mid-times, quality selection, camera/CCD, file hash and aperture FLUX/BKG changes. Pixel peaks have ~21 arcsec quantization, are not precise astrometry and cannot be automatically matched to catalogues without a coherent signal. The script requires numpy, astropy and matplotlib; file path, TIC, sector, center and baseline are in JSON. `fetch_pilot.py` retrieves original files to the temporary cache, not this evidence folder. Frames are medians in +/-0.075 h windows around -1,-0.5,0,+0.5,+1 h, rather than the exact photometric detector integration widths. Baseline windows are in the per-event config.

Control tests, visually inspected: `control-moving` (TIC 356752132 S42) shows a bright positive feature traversing the right edge in successive frames, while aperture FLUX loss is approximately offset by rising background. `control-star` (TIC 187261476 S59 deep loss) shows a stable, target-aperture-centered negative image, while its green positive maxima are tiny, arbitrary noise peaks. These distinguish the characteristic patterns but do not measure completeness.

Permissive v1-only sensitivity-audit events, visually inspected in six `diagnostic.png` files: the frozen v2 screen has zero qualifying windows; these are not primary detections.

- TIC 1002308236 S50: weak noisy differences, no coherent track or unambiguous stationary loss. Unresolved.
- TIC 1002310422 S50: broad field-wide negative change in restored frames around/after event, not a resolved compact track; aperture-level loss is small against structured changes. Unresolved.
- TIC 46536693 S42: weak, changing edge excesses, insufficient continuity or S/N for a trajectory. Unresolved.
- TIC 76458127 S43: broad field-wide change in restored frames and weak aperture-level structure; no resolved coherent track. Unresolved.
- TIC 1002155701 S23: noise-dominated changing maxima with no consistent motion or stationary loss. Unresolved.
- TIC 952640462 S63: noise-dominated changing maxima; no convincing track or isolated central loss. Unresolved.

No candidate coordinates are offered for matching: selected maxima do not form defensible coherent tracks, and a catalogue non-match would not imply an astrophysical cause. Quality-zero filtering does not eliminate all artifacts, and faint stamps, frame sampling, background estimation, aperture clipping and selection of baseline can hide moving objects. Wider FFI images, physical PSF fitting and robust significance/epoch validation would be needed before claiming a source position or exclusion. These are original same-instrument pixels, not independent data from another facility.
