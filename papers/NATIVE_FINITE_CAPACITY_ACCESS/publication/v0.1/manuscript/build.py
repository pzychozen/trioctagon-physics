"""Document-only cached/untrusted LaTeX build; intermediates stay outside the edition."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, os, shutil, subprocess, sys, tempfile
ROOT=Path(__file__).resolve().parent.parent
parser=argparse.ArgumentParser()
parser.add_argument('--tectonic',default=shutil.which('tectonic'))
parser.add_argument('--build-dir',help='External intermediate directory; defaults to a new system-temporary directory.')
args=parser.parse_args()
if not args.tectonic:parser.error('Supply an existing cached Tectonic executable with --tectonic.')
build=Path(args.build_dir).resolve() if args.build_dir else Path(tempfile.mkdtemp(prefix='finite-capacity-access-build-'))
if build.is_relative_to(ROOT.resolve()):parser.error('Build intermediates must be outside the candidate edition.')
build.mkdir(parents=True,exist_ok=True)
for name in ['fontcache','tmp']:(build/name).mkdir(exist_ok=True)
sources=sorted((ROOT/'manuscript').glob('*.tex'))
for p in sources:
    assert not any(ord(c)<32 and c not in '\n\r\t' for c in p.read_text(encoding='utf-8')),p.name
env=os.environ.copy()
env.update(SOURCE_DATE_EPOCH=str(int(datetime(2026,11,4,tzinfo=timezone.utc).timestamp())),
           TMP=str(build/'tmp'),TEMP=str(build/'tmp'))
if os.name=='nt':
    fonts=Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts';config=build/'fonts.conf'
    config.write_text('<?xml version="1.0"?>\n<fontconfig><dir>'+fonts.as_posix()+'</dir><cachedir>'
                      +(build/'fontcache').as_posix()+'</cachedir></fontconfig>\n',encoding='utf-8')
    env.update(FONTCONFIG_FILE=str(config),FONTCONFIG_PATH=str(build))
cmd=[args.tectonic,'--only-cached','--untrusted','--keep-logs','--keep-intermediates','--outdir',str(build),'manuscript/main.tex']
version=subprocess.run([args.tectonic,'--version'],capture_output=True,text=True,check=True).stdout.strip()
run=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True)
(build/'compiler.txt').write_bytes(run.stdout+run.stderr)
print((run.stdout+run.stderr).decode('utf-8',errors='replace'))
if run.returncode:raise SystemExit(run.returncode)
pdf=ROOT/'NATIVE_FINITE_CAPACITY_ACCESS_v0.1.pdf'
shutil.copyfile(build/'main.pdf',pdf)
record={'built_utc':datetime.now(timezone.utc).isoformat(),'compiler_version':version,'command':cmd,
    'python':sys.executable,'python_version':sys.version,'source_date_epoch':env['SOURCE_DATE_EPOCH'],
    'pdf_bytes':pdf.stat().st_size,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'sources':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
    'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'build_dir':str(build),'scope':'Document-only build; cached and untrusted; no scientific imports, shell escape, installation or network package fetching.'}
(build/'build_receipt.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
