"""Build this document with existing cached Tectonic; no scientific imports."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, os, shutil, subprocess, sys, tempfile
ROOT=Path(__file__).resolve().parent
NAME='NATIVE_ALTERNATING_BRANCH_CONNECTION_COMPANION_v0.1.pdf'
p=argparse.ArgumentParser();p.add_argument('--tectonic',default=shutil.which('tectonic'));p.add_argument('--build-dir')
a=p.parse_args()
if not a.tectonic:p.error('Supply an existing cached Tectonic executable with --tectonic.')
if os.environ.get('CONDA_DEFAULT_ENV')!='torment':p.error('Use Command Prompt with conda activate torment.')
B=Path(a.build_dir).resolve() if a.build_dir else Path(tempfile.mkdtemp(prefix='alternating-branch-note-'))
if B.is_relative_to(ROOT):p.error('Build intermediates must be outside this edition.')
B.mkdir(parents=True,exist_ok=True)
for n in ['tmp','fontcache']:(B/n).mkdir(exist_ok=True)
env=os.environ.copy();env.update(SOURCE_DATE_EPOCH=str(int(datetime(2026,11,12,tzinfo=timezone.utc).timestamp())),TMP=str(B/'tmp'),TEMP=str(B/'tmp'))
if os.name=='nt':
    fonts=Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts'
    (B/'fonts.conf').write_text('<?xml version="1.0"?>\n<fontconfig><dir>'+fonts.as_posix()+'</dir><cachedir>'+(B/'fontcache').as_posix()+'</cachedir></fontconfig>\n',encoding='utf-8')
    env.update(FONTCONFIG_FILE=str(B/'fonts.conf'),FONTCONFIG_PATH=str(B))
cmd=[a.tectonic,'--only-cached','--untrusted','--keep-logs','--keep-intermediates','--outdir',str(B),'main.tex']
version=subprocess.run([a.tectonic,'--version'],capture_output=True,text=True,check=True).stdout.strip()
start=datetime.now(timezone.utc).isoformat();result=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True)
(B/'compiler.stdout').write_bytes(result.stdout);(B/'compiler.stderr').write_bytes(result.stderr)
record={'title':'Certified Connection from Local Period-Doubling to the Captured Alternating Cycle in the Native Triad','author':'Hilmir Frímann Halldórsson (pzychozen)','edition':'Research edition v0.1','status':'Project-internal manuscript review complete; author-authorized for repository publication. No external peer review or proof-assistant verification is claimed.','preparation_date':'2026-11-12','author_authorization_date':'2026-11-13','publication_finalization_date':'2026-11-13','timezone':'Atlantic/Reykjavik','started_utc':start,'finished_utc':datetime.now(timezone.utc).isoformat(),'command':cmd,'cwd':str(ROOT),'compiler_version':version,'exit_status':result.returncode,'python':sys.executable,'python_version':sys.version,'conda_environment':os.environ['CONDA_DEFAULT_ENV'],'source_date_epoch':env['SOURCE_DATE_EPOCH'],'sources':{x.relative_to(ROOT).as_posix():hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(ROOT.rglob('*.tex')) if not x.is_relative_to(ROOT/'evidence')},'build_helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scientific_runs':0,'protection':'--only-cached --untrusted; no shell escape, package downloads or persistent configuration changes'}
if result.returncode==0:
    shutil.copyfile(B/'main.pdf',ROOT/NAME)
    record.update(pdf_filename=NAME,pdf_sha256=hashlib.sha256((ROOT/NAME).read_bytes()).hexdigest(),pdf_bytes=(ROOT/NAME).stat().st_size)
(B/'BUILD_RECEIPT.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print((result.stdout+result.stderr).decode('utf-8',errors='replace'));print('BUILD_DIR',B);raise SystemExit(result.returncode)
