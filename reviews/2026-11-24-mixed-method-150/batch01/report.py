"""Write a reproducibility guide and verify one completed batch."""
import argparse
import csv
from pathlib import Path

HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser()
p.add_argument("batch",type=Path)
a=p.parse_args()


def read(name):
    with (a.batch/f"{name}.csv").open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))


def select(rows,**attrs):
    return [r for r in rows if all(r[k]==v for k,v in attrs.items())]


batch=read("batch")
outcomes=read("outcomes")
files=read("files")
summary=read("coverage-summary")
assert [r["tic"] for r in batch]==[r["tic"] for r in outcomes]
assert len(list((a.batch/"plots").glob("*prior.png")))==len(batch)
assert (a.batch/"plots/independent-morphology.png").is_file()
counts=[sum(int(r[k]) for r in summary if r["min_window_coverage"]==".55" or r["min_window_coverage"]=="0.55")
        for k in ("all_cycles","measured","insufficient_in_sector","outside_sector_spans")]
mask=sum(int(f["masked"]) for f in files)
script_dir="." if a.batch.resolve()==HERE else "../batch01"
lines=[
    f'# {a.batch.name.upper()} TESS aperture review',
    '',
    f'Reviewed {len(batch)} targets using {len(files)} original target-sector QLP light curves. '
    f'The sector/camera/flux-column guard removed {mask} otherwise usable cadences.',
    '',
    f'The {counts[0]:,} trial predictions comprise {counts[1]:,} measurable windows, '
    f'{counts[2]:,} insufficiently sampled windows within a sector range and '
    f'{counts[3]:,} predictions outside the loaded sector ranges. Different clocks can '
    'predict the same elapsed time. All counts use the minimum 55% sampling rule.',
    '',
    '| TIC | Finding | Pilot windows measured | Weak in either product |',
    '| --- | --- | ---: | ---: |',
]
for row in outcomes:
    tic=row["tic"]
    c=select(summary,tic=tic,clock="Pilot",min_window_coverage="0.55")[0]
    lines.append(f'| {tic} | {row["reason"]} | {c["measured"]} | {c["weak_in_either"]} |')

lines.extend([
    '',
    '## Diagnostics',
    '',
    '- [Outcomes](outcomes.csv), [input FITS inventory](files.csv), [archive windows](events.csv) and [auxiliary window measurements](aux-windows.csv). The auxiliary table lists original cadence ID, quality counts, and SAP position and sky-background shifts relative to local shoulders.',
    '- [Clock fits](clocks.csv), [per-cycle measurements](predictions.csv) and [coverage sensitivity](coverage-summary.csv). The sensitivity table repeats counts at 55%, 80%, and 95% minimum sampling in the core and shoulders. Weak means at or below 0.75 ppt in raw or corrected flux.',
    '- [Original-cadence contact sheets](plots/contact-1.png) and [second set](plots/contact-2.png). See the individual prior, Pilot, Gaia, coarse alternate and refined plots in [plots](plots/).',
    '- [Independent split-sample clocks](independent-clocks.csv) and [phase-binned sector overlays](plots/independent-morphology.png). The plot compares raw and corrected aperture data and helps separate smooth modulation from a localized recurring loss.',
    '',
    '## Reproduction',
    '',
    f'From this batch directory, run `python {script_dir}/review.py --batch-dir .`, '
    f'`python {script_dir}/diagnostics.py .`, then `python {script_dir}/crosscheck.py .`. '
    'Python dependencies are NumPy, Astropy, Matplotlib, and Pillow. '
    'Use `--fits-dir`, `--prior-dir`, `--mask` or `--clock-dir` with the applicable scripts to override workspace defaults.',
    '',
    'The direct measurements use finite original aperture flux and pipeline-corrected flux at QUALITY=0. '
    'A local line through shoulder medians defines the baseline. The trial periods include Gaia, '
    'the pilot, their harmonics or subdivisions, a coarse blind box search, short-period searches '
    'on early and late segments, and fine searches around selected periods. The pilot is tested both '
    'with a free phase and anchored to the strongest flagged time. The coarse frequency grid can '
    'miss narrow peaks over multi-year baselines. Periods recorded for smooth modulation describe '
    'the photometric timescale. The aperture data do not assign the signal to a source.',
    '',
])
(a.batch/"README.md").write_text("\n".join(lines),encoding="utf-8")
