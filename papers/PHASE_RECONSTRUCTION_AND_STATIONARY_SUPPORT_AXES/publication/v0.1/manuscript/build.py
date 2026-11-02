"""Document-only cached Tectonic build; no scientific helper or project import."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
parser = argparse.ArgumentParser()
parser.add_argument('--tectonic', default=os.environ.get('TECTONIC_EXE') or shutil.which('tectonic'))
args = parser.parse_args()
if not args.tectonic:
    parser.error('Pass --tectonic pointing to an already installed Tectonic executable.')
compiler = str(Path(args.tectonic).resolve())
build = ROOT/'build'
build.mkdir(exist_ok=True)
(build/'fontcache').mkdir(exist_ok=True)
(build/'tmp').mkdir(exist_ok=True)
config = build/'fonts.conf'
fonts = Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts'
config.write_text('<?xml version="1.0"?>\n<!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n<fontconfig><dir>'+fonts.as_posix()+'</dir><cachedir>'+(build/'fontcache').as_posix()+'</cachedir></fontconfig>\n',encoding='utf-8')
env = os.environ.copy()
env.update({'FONTCONFIG_FILE':str(config),'FONTCONFIG_PATH':str(build),
            'SOURCE_DATE_EPOCH':'1793577600','TMP':str(build/'tmp'),'TEMP':str(build/'tmp')})
command = [compiler,'--only-cached','--untrusted','--keep-logs','--keep-intermediates','--outdir','build','manuscript/main.tex']
version = subprocess.run([compiler,'--version'],capture_output=True,text=True,check=True).stdout.strip()
run = subprocess.run(command,cwd=ROOT,env=env,capture_output=True)
(build/'compiler_final.txt').write_bytes(run.stdout+run.stderr)
if run.returncode:
    print((run.stdout+run.stderr).decode('utf-8',errors='replace')[-10000:])
    raise SystemExit(run.returncode)
pdf = ROOT/'NATIVE_PHASE_SPATIAL_v0.1.pdf'
shutil.copyfile(build/'main.pdf',pdf)
sha = lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
receipt = {'compiler':compiler,'compiler_version':version,'command':command,'return_code':0,
           'working_directory':str(ROOT),'python_executable':sys.executable,'python_version':sys.version,
           'pdf':pdf.name,'pdf_sha256':sha(pdf),
           'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in sorted((ROOT/'manuscript').glob('*.tex'))},
           'process_only_environment':{key:env[key] for key in ['FONTCONFIG_FILE','FONTCONFIG_PATH','SOURCE_DATE_EPOCH','TMP','TEMP']},
           'scope':'Document compilation only; cached packages, no installations, scientific execution or persistent environment changes.'}
(build/'build_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(version)
print((run.stdout+run.stderr).decode('utf-8',errors='replace'))
print(pdf)
