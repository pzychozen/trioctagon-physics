"""Document-only offline build. No scientific evidence modules are imported."""
from pathlib import Path
import argparse, os, sys, json, hashlib, subprocess, datetime, shutil
O=Path(__file__).resolve().parents[1];M=O/'manuscript'
NAME='NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_COMPANION_v0.1.pdf'
ap=argparse.ArgumentParser();ap.add_argument('--build-dir',required=True);ap.add_argument('--tectonic',default=r'C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe');args=ap.parse_args()
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
B=Path(args.build_dir).resolve();assert not B.is_relative_to(O)
B.mkdir(parents=True,exist_ok=True)
for d in ['tmp','fontcache']:(B/d).mkdir(exist_ok=True)
epoch=str(int(datetime.datetime(2026,11,15,tzinfo=datetime.timezone.utc).timestamp()))
env={**os.environ,'SOURCE_DATE_EPOCH':epoch,'TMP':str(B/'tmp'),'TEMP':str(B/'tmp')}
fonts=Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts'
(B/'fonts.conf').write_text('<?xml version="1.0"?><fontconfig><dir>'+fonts.as_posix()+'</dir><cachedir>'+(B/'fontcache').as_posix()+'</cachedir></fontconfig>')
env.update(FONTCONFIG_FILE=str(B/'fonts.conf'),FONTCONFIG_PATH=str(B))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
cmd=[args.tectonic,'--only-cached','--untrusted','--keep-logs','--keep-intermediates','--outdir',str(B),'main.tex']
start=datetime.datetime.now(datetime.timezone.utc).isoformat();version=subprocess.run([args.tectonic,'--version'],capture_output=True,check=True).stdout.decode().strip()
q=subprocess.run(cmd,cwd=M,env=env,capture_output=True,timeout=240)
(B/'compiler.stdout').write_bytes(q.stdout);(B/'compiler.stderr').write_bytes(q.stderr)
rec={'start_utc':start,'finish_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,'cwd':str(M),'compiler':version,'exit_status':q.returncode,'client_date':'2026-11-15','source_date_epoch':epoch,'python':sys.executable,'python_version':sys.version,'conda_environment':os.environ.get('CONDA_DEFAULT_ENV'),'source_hashes':{p.relative_to(O).as_posix():sha(p) for p in M.glob('*.tex')},'build_helper_sha256':sha(Path(__file__)),'scientific_runs':0,'status':'Project-internal manuscript review complete; author-authorized repository research edition v0.1.'}
if q.returncode==0:
    shutil.copyfile(B/'main.pdf',O/NAME);rec.update(pdf_sha256=sha(O/NAME),pdf_bytes=(O/NAME).stat().st_size)
(B/'BUILD_RECEIPT.json').write_text(json.dumps(rec,indent=2)+'\n')
print((q.stdout+q.stderr).decode(errors='replace'));sys.exit(q.returncode)
