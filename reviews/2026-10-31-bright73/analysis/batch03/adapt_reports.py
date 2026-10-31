from pathlib import Path
import json,csv
b=Path(__file__).parent
s=(b.parent/'batch01/write_reports.py').read_text()
a=s.index('special=');z=s.index('\nfor q in',a)
sp={
'157850336':'Repeated isolated eclipses and successive raw cycles secure recurrence; target deficit0.066pixel versus capable neighbor2.53pixels. Aperture dilution retained.',
'233462817':'Shallow repeated raw eclipses in sectors49/77; no capable listed neighbor. Deficit centroid0.53pixel offset and noisy difference image limit precise localization. Gaia conjunction offset0.041phase is interpreted with full covariance (0.245d), short observed duration allowing noncentral geometry; no arbitrary sigma veto.',
'48870240':'Six successive raw events in sector91 establish recurrence. Capable neighbor1.39pixels from deficit versus target0.056pixel; target core favors attribution.',
'178199444':'Three raw events in sector31 include consecutive cycles110/111 and a two-cycle separation108/110. Single selected sector supplies repeated cycles; this is not a single-event case.',
'375058760':'Deep repeated V eclipses show sector-dependent morphology and fitted depths; raw baseline/shape systematics remain and fitted depths are diluted. No detailed binary characterization claimed.',
'167923097':'Deep repeated V eclipses in sectors9/62/109; aperture differences and0.44pixel deficit offset retained; no capable listed neighbor.',
'406297889':'Repeated raw events across sectors14/55/82 with stable isolated morphology; no capable listed neighbor.',
'160258534':'Repeated eclipses across sectors14/56/83; capable neighbors2.51/2.73pixels from deficit versus target0.079pixel. Pixel core supports target at TESS resolution.',
'16809274':'Persistent unequal alternating eclipses establish doubled orbital period relative to historical SAP half-period7.363d. Even historical cycles are the shallower event; only those five measured events define the ephemeris, explicitly not called deeper primary. Odd deeper events remain in raw evidence. Capable neighbor1.046pixels from deficit versus target0.160pixel; target core favors attribution. Historical cutout stack mixes eclipse kinds.',
'279065540':'Deep repeated isolated eclipses across sectors18/58/85; no capable listed neighbor. Aperture dilution retained.'}
s=s[:a]+'special='+repr(sp)+s[z:]
s=s.replace("('48752905','351335839')","('16809274',)")
s=s.replace('excluded from primary fit (secondary)','excluded from selected shallower-eclipse fit (deeper event)')
s=s.replace('deeper even historical cycles define ephemeris','selected even historical cycles define ephemeris')
(b/'write_reports.py').write_text(s,encoding='utf-8')
