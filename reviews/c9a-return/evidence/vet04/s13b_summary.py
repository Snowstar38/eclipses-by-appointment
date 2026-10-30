# summary of s13 per kind: minimum per-sector dchi2 over neighbours, summed dchi2 for the least-rejected neighbour, offsets (|off|, 1-sigma), PSF depths
import json
for tic in ('283532878','407877153'):
    d=json.load(open(f's13_pixnoise_{tic}.json'))
    for k in 'PS':
        r=[x for x in d if x['kind']==k]
        mind=min(min(dc for dc,s in zip(x['dchi'],x['seps']) if 1<s<=90) for x in r)
        sums=[(sum(x['dchi'][i] for x in r),r[0]['seps'][i],r[0]['G'][i]) for i in range(1,len(r[0]['dchi']))]
        s0=min(sums)
        offs=[(x['sector'],round((x['offE']**2+x['offN']**2)**.5,1),round(((x['offE']*x['eoff'][0])**2+(x['offN']*x['eoff'][1])**2)**.5/max((x['offE']**2+x['offN']**2)**.5,1e-6),1),round(x['snr'],1)) for x in r]
        print(f'{tic} {k}: {len(r)} sectors; min per-sector dchi2 (any neighbour) {mind:.1f}; least-rejected neighbour summed over sectors: {s0[1]:.1f}" G{s0[2]:.2f} dchi2 {s0[0]:.1f}')
        print('   (sector, |offset| arcsec, 1-sigma, diff-image S/N):',offs)
        print('   depth on target from PSF amplitude (ppt):',[round(1e3*x['dep_t'],1) for x in r])
