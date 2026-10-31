from pathlib import Path
b=Path(__file__).parent;p=b/'write_reports.py';s=p.read_text(encoding='utf-8').replace('Six successive raw events in sector91 establish recurrence.','Six measured raw events in sector91 include four successive cycles5-8 and the cycle0/1 pair, establishing recurrence.');p.write_text(s,encoding='utf-8')
