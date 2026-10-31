from pathlib import Path
B=Path('[local path omitted]')
s=Path('[local path omitted]').read_text()
a=s.index('special=');b=s.index('\nfor q in',a)
special={
'135362193':'Shallow repeated eclipses across sectors53/80; capable neighbors at18.9/22.9arcsec lie0.91/1.06pixel from deficit versus target0.11pixel. Target-centered core supports attribution at TESS resolution; no calibrated localization errors. Sector80 pipeline offsets remain systematic uncertainty.',
'346865542':'Four deep isolated eclipses test within-sector recurrence and long-baseline cycle count. Aperture dilution retained; fitted depths are not intrinsic.',
'131331287':'Deep repeated events have reduced depths in sector102 relative to37/64; aperture dilution or baseline changes possible, no intrinsic depth variation claimed.',
'48752905':'Unequal alternating eclipses establish doubled period relative to historical SAP half-period. Deeper even historical cycles alone define epoch and orbital timing; mixed historical cutout stack is not a same-kind depth measurement.',
'337881909':'Crowded field: eight capable neighbors, nearest17.8arcsec; deficit0.06pixel from target versus0.80pixel from nearest capable source. Target-centered core favors target, but highPSF fractional residual0.83 limits precise localization. No calibrated errors or resolved binary parameters claimed.',
'274578846':'Same-kind repeat within sector53 and84 secures long-baseline cycle count. Modest aperture/sector depth differences retained.',
'14291901':'Repeated isolated eclipses at multiple successive cycles; Gaia conjunction offset retained with propagated orbit covariance and radius/model limitations.',
'180179209':'Crowded field: eleven capable neighbors, nearest16.6arcsec; deficit0.23pixel from target versus1.00pixel from nearest capable source. PSF residual0.82 limits localization precision; target-centered core supports attribution at TESS resolution. Final partial/singular sector101 fit excluded from timing.',
'351335839':'Unequal alternating eclipse depths establish doubled orbital period; deeper even historical cycles define ephemeris. Initial duration bound broadened to capture deepV morphology. Poor PSF residual0.99 limits detailed image modeling, but target-centered deficit and no capable listed neighbors support source. Mixed historical cutout stack cannot be equated to primary depth.',
'89553209':'Sector14 cycle-1 lacks ingress coverage and is excluded from timing. Remaining five measured events include successive sector54/81 pairs and a full sector14 event. Historical prediction drift is fitted freely; partial raw event is not a precise timing. Broad eclipse duration and radius-based central estimate agree approximately.'}
s=s[:a]+'special='+repr(special)+s[b:]
s=s.replace("verdict='PROBABLE' if tic=='374589618' else 'CONFIRMED'","verdict='CONFIRMED'")
s=s.replace("('123220126','374589618','355885228','409935170')","('48752905','351335839')")
s=s.replace("else 'usable; same-kind selection applies'","else 'usable; same-kind selection applies'")
s=s.replace("'excluded singular timing fit' if not e.get('timing_usable',True)","e.get('timing_failure_reason','excluded timing fit') if not e.get('timing_usable',True)")
s=s.replace('Singular center-covariance fits flagged timing_usable=false','Partial or singular center-covariance fits flagged timing_usable=false')
s=s.replace('quality-zero raw QLP SAP_FLUX show','quality-zero raw QLP SAP_FLUX contain')
s=s.replace('Raw events: pass.** Free trapezoid fits','Raw events: pass.** Free trapezoid fits')
s=s[:s.index('for p in [SB/\'search.jsonl\'')]+"\n# Manifest is generated only after helper final audit.\n"
s=s.replace('±','+/-')
(B/'write_reports.py').write_text(s,encoding='utf-8')
