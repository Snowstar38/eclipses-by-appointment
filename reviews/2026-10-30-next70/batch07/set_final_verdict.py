from pathlib import Path
import json,csv,hashlib,datetime
B=Path('[local working path omitted; see provenance receipts]');p=B/'make_reports.py';s=p.read_text().replace("t not in ['101779765','311918550']","t not in ['101779765']");p.write_text(s)
