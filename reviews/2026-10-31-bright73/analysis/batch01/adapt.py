from pathlib import Path
B=Path('[local path omitted]')
p=B/'review_measure.py';s=p.read_text().replace("('123220126','374589618','355885228','409935170')","('48752905','351335839')").replace("parity=1 if tic=='374589618' else 0","parity=0").replace("tic in ('123220126','355885228','409935170')","tic in ('48752905','351335839')");p.write_text(s)
p=B/'contact.py';p.write_text(Path('[local path omitted]').read_text().replace('magnitude60b-2026-10-31/batch03','bright73-2026-10-31/batch01'))
