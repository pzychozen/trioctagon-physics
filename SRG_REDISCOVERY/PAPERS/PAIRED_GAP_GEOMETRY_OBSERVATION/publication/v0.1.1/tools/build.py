"""Portable offline typesetting. Set PAPER_I_TECTONIC and PAPER_I_TEX_CACHE."""
from pathlib import Path
import hashlib,json,os,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
os.chdir(ROOT)
build=ROOT/'build'; build.mkdir(exist_ok=True)
cache=ROOT/'cache';cache.mkdir(exist_ok=True)
exe=os.environ.get('PAPER_I_TECTONIC') or shutil.which('tectonic')
if not exe: raise SystemExit('Set PAPER_I_TECTONIC to an existing Tectonic executable.')
source=os.environ.get('PAPER_I_TEX_CACHE')
local=cache/'tectonic'
if source:
    source=Path(source).resolve()
    if source!=local.resolve():shutil.copytree(source,local,dirs_exist_ok=True)
if not local.is_dir():raise SystemExit('Set PAPER_I_TEX_CACHE to a populated existing cache. No downloads allowed.')
env=os.environ.copy()
env.update(TECTONIC_CACHE_DIR=str(local),SOURCE_DATE_EPOCH='1792281600',TEMP=str(cache),TMP=str(cache),XDG_CACHE_HOME=str(cache))
# Fontconfig's cache is local as well. This is not a system configuration change.
fc=cache/'fonts.conf'
fontdir=Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts'
if os.name=='nt':
    fc.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>'+fontdir.as_posix()+'</dir><cachedir>'+(cache/'fonts').as_posix()+'</cachedir></fontconfig>',encoding='utf8')
    env['FONTCONFIG_FILE']=str(fc)
args=[str(exe),'--only-cached','--untrusted','--keep-logs','--keep-intermediates','--synctex','--outdir',str(build),'manuscript.tex']
if (build/'console.log').exists():
    n=len(list(build.glob('console_pass_*.log')))+1
    shutil.copyfile(build/'console.log',build/f'console_pass_{n:03d}.log')
    for name in ['manuscript.log','build_record.json']:
        if (build/name).exists():shutil.copyfile(build/name,build/f'pass_{n:03d}_{name}')
r=subprocess.run(args,cwd=ROOT,env=env,capture_output=True)
(build/'console.log').write_bytes(r.stdout+r.stderr)
record={'command':args,'returncode':r.returncode,'python':sys.version,'tectonic':subprocess.check_output([str(exe),'--version']).decode().strip(),'executable_sha256':hashlib.sha256(Path(exe).read_bytes()).hexdigest(),'only_cached':True,'source_date_epoch':env['SOURCE_DATE_EPOCH']}
(build/'build_record.json').write_text(json.dumps(record,indent=2),encoding='utf8')
print('\n'.join((r.stdout+r.stderr).decode('utf8',errors='replace').splitlines()[-35:]))
if r.returncode:raise SystemExit(r.returncode)
shutil.copyfile(build/'manuscript.pdf',ROOT/'PAPER_I_PAIRED_GAP_GEOMETRY_OBSERVATION_v0.1.1.pdf')
