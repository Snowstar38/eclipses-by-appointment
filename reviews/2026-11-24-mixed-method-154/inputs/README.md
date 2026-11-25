# Public replay inputs

The release manifest has **8,406 distinct QLP FITS products** (3.823 GB). It records **1,408 target products** for all 154 TICs and **7,211 same-camera products** used in the comparison fields. The two sets overlap by 213 products. Each row gives the original filename, detector, byte count, SHA-256 and versioned MAST URL. Sectors 74 through 79 use v02. Other sectors use v01. The comparison sets are the available field products on the sector and camera pairs specified by the published control-event files.

| Batch | Targets | Target FITS | Additional FITS with `--controls` |
| ---: | ---: | ---: | ---: |
| 01 | 10 | 163 | 0 |
| 02 | 10 | 51 | 0 |
| 03 | 10 | 102 | 0 |
| 04 | 10 | 120 | 0 |
| 05 | 10 | 77 | 0 |
| 06 | 10 | 105 | 0 |
| 07 | 10 | 101 | 0 |
| 08 | 10 | 189 | 0 |
| 09 | 10 | 112 | 0 |
| 10 | 10 | 63 | 0 |
| 11 | 10 | 50 | 1892 |
| 12 | 10 | 92 | 1296 |
| 13 | 10 | 89 | 1828 |
| 14 | 10 | 35 | 962 |
| 15 | 10 | 45 | 1024 |
| 16 | 4 | 14 | 469 |

## Prepare a replay

From the release root, with Python 3.11 or newer and `requests` installed:

```text
python inputs/prepare.py 16
python inputs/prepare.py 16 --verify-only
python batch11/review.py --batch batch16
```

The default replay workspace is `inputs/workspace`. Choose a batch from 1 through 16. Add `--controls` for the batch's same-camera comparison files, or `--target TIC` for a target-only replay. `--root PATH` changes the workspace location. For `--controls` with `--target`, the full batch comparison field is included. Existing FITS files are byte-counted and hashed before reuse. `--verify-only` checks the prepared FITS, archived scan JSON, and guard without network access.

Run `python batch01/review.py --batch-dir batch01` after preparing a batch from 01 through 05. Run `python batch06/review_lane.py 6 --root inputs/workspace` for the batch 06 example, substituting the appropriate number for 07 through 10. For batch 11 through 16 use `python batch11/review.py --batch batchN` with the zero-padded batch directory name, as shown above. The scripts use NumPy, Astropy, and Matplotlib. The contact-sheet helper also uses Pillow. See each batch's review notes for other inputs or additional analyses.

## Archived inputs and verification

- [qlp.csv](qlp.csv) is the product manifest. The builder checks target headers, hashes every local original file, verifies the stored historical source hashes, and checks that published camera comparison rows are covered.
- [historical-scans.json.gz](historical-scans.json.gz) preserves the historical JSON records for 154 targets. Recorded absolute paths were normalized to FITS basenames. Individual scans are restored under the expected historical directory in the replay workspace.
- [exposure-guard.csv](exposure-guard.csv) is the calibrated Sector 26 QLP lookup for three camera-specific exposures. The source screen is described in the [exposure guard provenance](exposure-guard.md).
- [replay-qa.txt](replay-qa.txt) records a clean public download, offline hash recheck, and exact archive-window replay for batch 16 and one target from batch 01. `python inputs/qa_replay.py` repeats those checks in a temporary copy of the published scripts and manifests.
