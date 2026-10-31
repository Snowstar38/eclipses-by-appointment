from pathlib import Path
p=Path(__file__).parent/'write_reports.py';s=p.read_text(encoding='utf-8');s=s.replace('\u00c2\u00b1','+/-');p.write_text(s,encoding='utf-8')
