from pathlib import Path
from PIL import Image,ImageDraw
b=Path(__file__).parent
for kind,pat,h in [('raw','*/raw-events.png',650),('phase','*/phase-review.png',650),('pixels','*/fresh-pixels/diff_fresh.png',400)]:
 can=Image.new('RGB',(1800,5*h),'white')
 for i,p in enumerate(b.glob(pat)):
  im=Image.open(p);im.thumbnail((900,h-15));can.paste(im,(i%2*900,i//2*h));ImageDraw.Draw(can).text((i%2*900,i//2*h),p.parent.parent.name if kind=='pixels' else p.parent.name,fill='black')
 can.save(b/(kind+'-contact.png'))
