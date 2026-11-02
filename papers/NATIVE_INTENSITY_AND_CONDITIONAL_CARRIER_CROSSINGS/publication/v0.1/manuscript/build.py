"""Cached document compilation only. No scientific imports or evaluation."""
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parent.parent
arg=argparse.ArgumentParser();arg.add_argument('--tectonic',default=shutil.which('tectonic'))
a=arg.parse_args()
if not a.tectonic:arg.error('Supply an existing cached Tectonic executable with --tectonic.')
for p in (ROOT/'manuscript').glob('*.tex'):
    data=p.read_text(encoding='utf-8')
    assert not any(ord(c)<32 and c not in '\n\r\t' for c in data),f'Control character: {p.name}'
build=ROOT/'build';build.mkdir(exist_ok=True)
for d in ['fontcache','tmp']:(build/d).mkdir(exist_ok=True)
config=build/'fonts.conf'
config.write_text('<?xml version="1.0"?>\n<fontconfig><dir>'+str(Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts').replace('\\','/')+'</dir><cachedir>'+(build/'fontcache').as_posix()+'</cachedir></fontconfig>\n',encoding='utf-8')
env=os.environ.copy();env.update(FONTCONFIG_FILE=str(config),FONTCONFIG_PATH=str(build),SOURCE_DATE_EPOCH='1793577600',TMP=str(build/'tmp'),TEMP=str(build/'tmp'))
cmd=[a.tectonic,'--only-cached','--untrusted','--keep-logs','--keep-intermediates','--outdir',str(build),'manuscript/main.tex']
version=subprocess.run([a.tectonic,'--version'],capture_output=True,text=True,check=True).stdout.strip()
run=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True)
(build/'compiler.txt').write_bytes(run.stdout+run.stderr)
print((run.stdout+run.stderr).decode('utf-8',errors='replace'))
if run.returncode:raise SystemExit(run.returncode)
pdf=ROOT/'NATIVE_INTENSITY_CARRIER_CROSSINGS_v0.1.pdf';shutil.copyfile(build/'main.pdf',pdf)
record={'compiler_version':version,'command':cmd,'python':sys.executable,'python_version':sys.version,
        'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'sources':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'manuscript').glob('*.tex'))},
        'scope':'Document compilation only, cached TeX, untrusted mode, no installations or scientific evaluation.'}
(build/'build_receipt.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
