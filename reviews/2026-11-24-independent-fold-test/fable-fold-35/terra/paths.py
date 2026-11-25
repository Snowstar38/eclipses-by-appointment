from pathlib import Path
import argparse
import os

def cadence_cache():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cadence-cache", default=os.environ.get("TESS_FOLD_CACHE"),
                        help="directory of cached TIC-sector NPZ files (or set TESS_FOLD_CACHE)")
    args = parser.parse_args()
    default = Path(__file__).resolve().parents[3] / "data" / "fable52-ffi-tce-2026-11-24" / "cadences"
    path = Path(args.cadence_cache).expanduser().resolve() if args.cadence_cache else default
    if not path.is_dir():
        parser.error(f"cadence cache not found: {path}; use --cadence-cache or TESS_FOLD_CACHE")
    return path
