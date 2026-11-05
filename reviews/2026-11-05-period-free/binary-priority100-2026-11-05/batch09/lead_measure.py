"""Run bounded raw-SAP measurements with the validated batch08 primitive.

The copied implementation remains in this batch for reproducibility; source
FITS hashes are checked before every measurement.
"""
from pathlib import Path

src = Path(__file__).resolve().parent.parent / 'batch08' / 'lead_measure.py'
code = src.read_text(encoding='utf-8')
code = code.replace("    packet=json.loads((ROOT/'source-packets'/tic/'sources.json').read_text())\n", "")
code = code.replace("B=Path(__file__).resolve().parent", "B=Path(__file__).resolve().parent")
exec(compile(code, str(src), 'exec'), {'__file__': __file__, '__name__': '__main__'})
