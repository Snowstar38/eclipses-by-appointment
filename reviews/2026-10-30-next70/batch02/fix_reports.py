from pathlib import Path
p=Path('[local working path omitted; see provenance receipts]')
s=p.read_text(encoding='utf-8-sig');a=s.index(' if ip:text+=');b=s.index('\n else:text+=',a)
s=s[:a]+''' if ip:
  text+=f"Independent {i['provenance']} sector {i['sector']} confirms event depths {', '.join(f'{x:.2f}' for x in ind)} ppt. "
  if 'TESScut' in i['provenance']:
   text+="Independent 3x3 target aperture with per-cadence faint-pixel background; core medians versus local pre/post baseline, without formal errors or dilution correction. This uses the same TESS images through an independent extraction pipeline, not an independent observation. Gaia coordinates projected through the cutout WCS verify the target position and header sector. "
  else:
   text+="Fixed QLP event shape with independently extracted SAP flux; uninflated formal depth errors (ppt): "+', '.join(str(round(1000*x['formal_error'],3)) for x in ip)+". FITS TIC/sector headers and padded TIC URI identity pass. "
  text+="Input paths/URIs and SHA256 are preserved in raw-evidence/independent-results.json.\\n\\n"
''' .rstrip()+s[b:]
s=s.replace('SIMBAD SB* alone','SIMBAD SB* alone')
p.write_text(s,encoding='utf-8')
