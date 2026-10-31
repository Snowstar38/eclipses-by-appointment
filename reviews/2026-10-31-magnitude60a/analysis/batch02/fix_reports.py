from pathlib import Path
b=Path(__file__).parent
p=b/'prepare_reports.py';s=p.read_text().replace('6/33/98','6/32/98');p.write_text(s)
