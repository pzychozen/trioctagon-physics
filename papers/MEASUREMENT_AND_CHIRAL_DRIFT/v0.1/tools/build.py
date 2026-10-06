"""Portable project build: python tools/build.py --tectonic tectonic."""
from pathlib import Path
import subprocess,sys,os,argparse,json,hashlib,shutil,platform
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('--tectonic',default='tectonic')
p.add_argument('--fontconfig',help='Optional existing platform Fontconfig file')
p.add_argument('--lane',choices=['measurement','drift','both'],default='both')
a=p.parse_args()
exe=shutil.which(a.tectonic) or a.tectonic
env=os.environ.copy();env['SOURCE_DATE_EPOCH']='1791244800'
if a.fontconfig:env['FONTCONFIG_FILE']=str(Path(a.fontconfig).resolve())
records={}
for lane in (['measurement','drift'] if a.lane=='both' else [a.lane]):
    dest=ROOT/lane;build=ROOT/'results/build'/lane;build.mkdir(parents=True,exist_ok=True)
    cmd=[exe,'manuscript.tex','--outdir',str(build),'--keep-logs']
    run=subprocess.run(cmd,cwd=dest,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace')
    log=run.stdout+'\n'+run.stderr
    # Public logs carry no local production-workspace prefix.
    (build/'console.txt').write_text(log.replace(str(ROOT),'<package>'),encoding='utf-8')
    if run.returncode:print(log);raise SystemExit(run.returncode)
    filename='Measurement_Geometry_v0.1.pdf' if lane=='measurement' else 'Cubic_Common_Phase_Drift_v0.1.pdf'
    shutil.copyfile(build/'manuscript.pdf',dest/filename)
    b=(dest/filename).read_bytes()
    records[lane]={'file':f'{lane}/{filename}','bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'compiler':subprocess.check_output([exe,'--version'],text=True).strip(),'source_date_epoch':env['SOURCE_DATE_EPOCH'],'python':platform.python_version(),'returncode':run.returncode}
    print(lane,records[lane],flush=True)
record=ROOT/'results/build/build.json'
prior=json.loads(record.read_text()) if record.exists() else {}
prior.update(records);record.write_text(json.dumps(prior,indent=2)+'\n')
