from pathlib import Path
b=Path(__file__).parent;p=b/'write_reports.py';s=p.read_text(encoding='utf-8').replace('sectors18/58/85','sectors58/85');p.write_text(s,encoding='utf-8')
