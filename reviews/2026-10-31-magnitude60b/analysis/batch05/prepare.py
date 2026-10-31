from pathlib import Path
b=Path(__file__).parent
p=b/'review_measure.py';s=p.read_text();s=s.replace("sorted((BASE.parent/'shared-qlp').glob(tic+'_s*.fits'))", "sorted(list((BASE.parent/'shared-qlp').glob(tic+'_s*.fits'))+list((BASE/tic/'raw').glob(tic+'_s*.fits')))");p.write_text(s)
p=b/'pixel_audit.py';s=(b.parent/'batch04/pixel_audit.py').read_text().replace(" if tic=='394386248':continue\n",'');p.write_text(s)
