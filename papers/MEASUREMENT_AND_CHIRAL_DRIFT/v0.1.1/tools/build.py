"""Build the edited measurement v0.1.1 source only; never regenerate v0.1."""
from pathlib import Path
import argparse,subprocess,os,shutil,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
arg=argparse.ArgumentParser()
arg.add_argument('--tectonic',default='tectonic')
arg.add_argument('--fontconfig')
a=arg.parse_args()
out=ROOT/'results/build';out.mkdir(exist_ok=True,parents=True)
env=os.environ.copy();env['SOURCE_DATE_EPOCH']='1791244800'
if a.fontconfig:env['FONTCONFIG_FILE']=str(Path(a.fontconfig).resolve())
run=subprocess.run([a.tectonic,'manuscript.tex','--outdir',str(out),'--keep-logs'],cwd=ROOT/'measurement',env=env,capture_output=True,text=True,encoding='utf-8',errors='replace')
console=run.stdout+'\n'+run.stderr
(out/'console.txt').write_text(console.replace(str(ROOT),'<candidate>'),encoding='utf-8')
if run.returncode:print(console);raise SystemExit(run.returncode)
dest=ROOT/'measurement/Measurement_Geometry_v0.1.1.pdf'
shutil.copyfile(out/'manuscript.pdf',dest)
b=dest.read_bytes()
record={'returncode':0,'file':str(dest.relative_to(ROOT)).replace('\\','/'),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'compiler':subprocess.check_output([a.tectonic,'--version'],text=True).strip(),'source_date_epoch':env['SOURCE_DATE_EPOCH'],'scope':'Measurement correction only; no drift build or predecessor science replay'}
(out/'build.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
