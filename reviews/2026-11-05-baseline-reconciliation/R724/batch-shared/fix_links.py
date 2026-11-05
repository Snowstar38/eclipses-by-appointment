from pathlib import Path
B=Path(__file__).resolve().parent
p=B/'write_reports.py';p.write_text(p.read_text(encoding='utf-8').replace('`timing-sensitivity.json`','`../timing-sensitivity.json`'),encoding='utf-8')
