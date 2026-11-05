"""Run the bounded TESS footprint availability check for this queue."""
from pathlib import Path
src=Path(__file__).resolve().parent.parent/'batch08'/'lead_current_sectors.py'
exec(compile(src.read_text(encoding='utf-8'),str(src),'exec'),{'__file__':__file__,'__name__':'__main__'})
