"""Build the canonical publication PDF (REVIEW.pdf); run no scientific checker."""
from pathlib import Path
import argparse, hashlib, json, re, shutil, subprocess, sys
ROOT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--tectonic',default='C:/TORMENT/TRIOCTAGON_new/reconstruction/publication/paper_C/build/tools/tectonic/tectonic.exe')
parser.add_argument('--poppler-dir',default='C:/Users/Notandi/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin')
args=parser.parse_args()
build=ROOT/'tmp'/'build';build.mkdir(parents=True,exist_ok=True)
renders=ROOT/'tmp'/'pdfs';renders.mkdir(parents=True,exist_ok=True)
subprocess.run([sys.executable,'-B',str(ROOT/'make_figures.py')],cwd=ROOT,check=True)
cmd=[args.tectonic,'--keep-logs','--keep-intermediates','--outdir',str(build),'main.tex']
proc=subprocess.run(cmd,cwd=ROOT,capture_output=True)
(build/'compiler_output.txt').write_bytes(proc.stdout+b'\n'+proc.stderr)
if proc.returncode:
 print((proc.stdout+proc.stderr).decode('utf-8',errors='replace')[-16000:])
 raise SystemExit(proc.returncode)
shutil.copyfile(build/'main.pdf',ROOT/'REVIEW.pdf')
log=(build/'main.log').read_text(encoding='utf-8',errors='replace')
warnings=[x for x in log.splitlines() if any(s in x for s in ['Overfull','Underfull','undefined','Missing character','LaTeX Warning','Package hyperref Warning'])]
record={'compiler':args.tectonic,'command':cmd,'returncode':proc.returncode,'warnings':warnings,
 'pdf_sha256':hashlib.sha256((ROOT/'REVIEW.pdf').read_bytes()).hexdigest(),
 'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'main.tex',ROOT/'references.tex']},
 'scientific_checkers_executed':False,'state_updates':0}
(ROOT/'verification'/'publication_build_record.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
subprocess.run([str(Path(args.poppler_dir)/'pdftoppm.exe'),'-r','100','-png',str(ROOT/'REVIEW.pdf'),str(renders/'page')],cwd=ROOT,check=True,capture_output=True)
from PIL import Image,ImageOps,ImageDraw
pages=sorted(renders.glob('page-*.png'))
for j in range(0,len(pages),4):
 canvas=Image.new('RGB',(1240,1810),'#d0d5dc');draw=ImageDraw.Draw(canvas)
 for k,p in enumerate(pages[j:j+4]):
  im=Image.open(p).convert('RGB');im.thumbnail((600,855))
  x=10+(k%2)*620;y=30+(k//2)*900
  canvas.paste(im,(x,y));draw.text((x,y-20),p.stem,fill='black')
 canvas.save(renders/f'contact-{j//4+1:02}.png')
print(json.dumps({'pdf':str(ROOT/'REVIEW.pdf'),'rendered_pages':len(pages),'warnings':warnings},indent=2))
