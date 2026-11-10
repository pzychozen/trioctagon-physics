"""Document-only, cached, untrusted Tectonic build with external intermediates."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, os, shutil, subprocess, sys, tempfile
ROOT=Path(__file__).resolve().parent
CANONICAL='CENTRAL_ROUTE_SIX_OPENING_CORRESPONDENCE_v0.1.pdf'
parser=argparse.ArgumentParser()
parser.add_argument('--tectonic',default=shutil.which('tectonic'))
parser.add_argument('--build-dir',help='Directory outside the edition; default: new temporary directory.')
args=parser.parse_args()
if not args.tectonic: parser.error('Supply the existing cached Tectonic executable with --tectonic.')
if os.environ.get('CONDA_DEFAULT_ENV')!='torment': parser.error('Run in Command Prompt after conda activate torment.')
build=Path(args.build_dir).resolve() if args.build_dir else Path(tempfile.mkdtemp(prefix='central-six-paper-'))
if build.is_relative_to(ROOT): parser.error('Build intermediates must stay outside the edition.')
build.mkdir(parents=True,exist_ok=True)
for name in ['fontcache','tmp']: (build/name).mkdir(exist_ok=True)
sources=sorted(ROOT.rglob('*.tex'))+sorted((ROOT/'figures').glob('*.pdf'))
for p in ROOT.rglob('*.tex'):
    assert not any(ord(c)<32 and c not in '\n\r\t' for c in p.read_text(encoding='utf-8')),p
env=os.environ.copy()
env.update(SOURCE_DATE_EPOCH=str(int(datetime(2026,11,10,tzinfo=timezone.utc).timestamp())),
           TMP=str(build/'tmp'), TEMP=str(build/'tmp'))
if os.name=='nt':
    fonts=Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts'
    (build/'fonts.conf').write_text('<?xml version="1.0"?>\n<fontconfig><dir>'+fonts.as_posix()
        +'</dir><cachedir>'+(build/'fontcache').as_posix()+'</cachedir></fontconfig>\n',encoding='utf-8')
    env.update(FONTCONFIG_FILE=str(build/'fonts.conf'),FONTCONFIG_PATH=str(build))
cmd=[args.tectonic,'--only-cached','--untrusted','--keep-logs','--keep-intermediates',
     '--outdir',str(build),'main.tex']
version=subprocess.run([args.tectonic,'--version'],capture_output=True,text=True,check=True).stdout.strip()
started=datetime.now(timezone.utc).isoformat()
run=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True)
(build/'compiler.txt').write_bytes(run.stdout+run.stderr)
print((run.stdout+run.stderr).decode('utf-8',errors='replace'))
if run.returncode: raise SystemExit(run.returncode)
pdf=ROOT/CANONICAL
shutil.copyfile(build/'main.pdf',pdf)
record={'title':'Central-Route Accounting and Six-Opening Geometry in the Reciprocal Chiral Exchange Candidate',
 'author':'Hilmir Frímann Halldórsson (pzychozen)', 'edition':'v0.1',
 'status':'Research edition v0.1 — accepted mathematics; author-authorized repository publication',
 'preparation_date':'2026-11-10','timezone':'Atlantic/Reykjavik',
 'started_utc':started,'built_utc':datetime.now(timezone.utc).isoformat(),
 'compiler_version':version,'command':cmd,'python':sys.executable,'python_version':sys.version,
 'conda_environment':os.environ.get('CONDA_DEFAULT_ENV'), 'source_date_epoch':env['SOURCE_DATE_EPOCH'],
 'pdf_filename':CANONICAL,'pdf_bytes':pdf.stat().st_size,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
 'content':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
 'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'build_dir':str(build),
 'scope':'Document-only; cached and untrusted. No scientific imports, shell escape or TeX package fetching.'}
(build/'BUILD_RECEIPT.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print('Built', pdf, record['pdf_sha256'])
