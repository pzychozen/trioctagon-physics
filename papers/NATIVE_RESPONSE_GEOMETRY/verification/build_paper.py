"""Build the multi-file LaTeX project using an existing Tectonic executable."""
from pathlib import Path
import argparse,subprocess,json,hashlib,platform,shutil,sys,os
sys.stdout.reconfigure(encoding='utf8')
from datetime import datetime,timezone
L=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--tectonic',default='tectonic');p.add_argument('--fontconfig',help='Optional existing Fontconfig configuration for Windows');a=p.parse_args()
exe=shutil.which(a.tectonic) or a.tectonic
version=subprocess.check_output([exe,'--version'],text=True).strip()
cmd=[exe,'main.tex','--outdir','../publication','--keep-logs']
env=os.environ.copy()
if a.fontconfig:env['FONTCONFIG_FILE']=str(Path(a.fontconfig).resolve())
r=subprocess.run(cmd,cwd=L/'manuscript',env=env,capture_output=True,text=True,encoding='utf8',errors='replace')
log=r.stdout+'\n'+r.stderr
(L/'publication/build_console.txt').write_text(log,encoding='utf8')
if r.returncode:print(log);raise SystemExit(r.returncode)
pdf=L/'publication/Native_Response_Geometry_v0.1.pdf'
(L/'publication/main.pdf').replace(pdf)
inputs=[*sorted((L/'manuscript').glob('*.tex')),*sorted((L/'figures').glob('*.pdf'))]
result={'built_utc':datetime.now(timezone.utc).isoformat(),'compiler':version,'compiler_executable':str(exe),'compiler_sha256':sha(Path(exe)),'command':cmd,'fontconfig_file':env.get('FONTCONFIG_FILE'),'cwd':'manuscript','python':platform.python_version(),'returncode':r.returncode,'inputs':{q.relative_to(L).as_posix():sha(q) for q in inputs},'pdf':pdf.relative_to(L).as_posix(),'pdf_sha256':sha(pdf),'bytes':pdf.stat().st_size}
(L/'publication/build_record.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(log);print('PDF:',pdf,'bytes:',pdf.stat().st_size)
