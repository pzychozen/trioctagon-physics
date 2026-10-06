"""Build this multi-file paper in an external workspace; preserve source inputs.
Defaults match the existing repository's cached Tectonic workflow. Override
THREEWAY_TECTONIC / THREEWAY_TEX_CACHE / THREEWAY_BUILD for other installations.
"""
from pathlib import Path
import os, subprocess, shutil, hashlib, json, datetime, sys, argparse
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1]
WORK=Path(os.environ.get('THREEWAY_BUILD','C:/TORMENT/TRIOCTAGON_new/publication_workspaces/three_way_reconstruction_20261005/build'))
TEX=Path(os.environ.get('THREEWAY_TECTONIC','C:/TORMENT/TRIOCTAGON_new/reconstruction/publication/paper_C/build/tools/tectonic/tectonic.exe'))
CACHE=Path(os.environ.get('THREEWAY_TEX_CACHE',str(WORK.parent/'tectonic-cache')))
parser=argparse.ArgumentParser();parser.add_argument('--fetch-tex-dependencies',action='store_true');options=parser.parse_args()
if not CACHE.exists():
    seed=Path('C:/TORMENT/TRIOCTAGON_new/publication_workspaces/paper_F_20260925/tectonic-cache')
    shutil.copytree(seed,CACHE)
WORK.mkdir(parents=True,exist_ok=True)
fc=WORK/'fontconfig.xml';fc.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>C:/Windows/Fonts</dir><cachedir>'+str(WORK/'fontconfig-cache').replace('\\','/')+'</cachedir></fontconfig>',encoding='utf-8')
env=os.environ.copy();env['TECTONIC_CACHE_DIR']=str(CACHE);env['FONTCONFIG_FILE']=str(fc)
env['SOURCE_DATE_EPOCH']=str(int(datetime.datetime(2026,10,5,tzinfo=datetime.timezone.utc).timestamp()))
args=[str(TEX),'-X','compile']+([] if options.fetch_tex_dependencies else ['--only-cached'])+['--keep-logs','--keep-intermediates','--outdir',str(WORK),str(ROOT/'source/main.tex')]
r=subprocess.run(args,cwd=ROOT/'source',env=env,capture_output=True)
(ROOT/'records/build_console.log').write_bytes(r.stdout+r.stderr)
print((r.stdout+r.stderr).decode(errors='replace')[-14000:])
if r.returncode:raise SystemExit(r.returncode)
out=ROOT/'output/pdf/three_way_reconstruction_v0.1.pdf';shutil.copyfile(WORK/'main.pdf',out)
shutil.copyfile(WORK/'main.log',ROOT/'records/latex_build.log')
shutil.copyfile(WORK/'main.aux',ROOT/'records/main.aux')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
record=dict(exit_code=r.returncode,workspace=str(WORK),command=args,tectonic_sha256=sha(TEX),tectonic_version=subprocess.check_output([str(TEX),'--version'],text=True).strip(),cache=str(CACHE),network_in_tex_build=options.fetch_tex_dependencies,source_date_epoch=env['SOURCE_DATE_EPOCH'],python=sys.version,pdf_sha256=sha(out),inputs={str(p.relative_to(ROOT)):sha(p) for folder in ['source','figures'] for p in sorted((ROOT/folder).glob('*')) if p.is_file() and p.suffix in ['.tex','.pdf']})
(ROOT/'records/build_record.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print('Wrote '+str(out))
