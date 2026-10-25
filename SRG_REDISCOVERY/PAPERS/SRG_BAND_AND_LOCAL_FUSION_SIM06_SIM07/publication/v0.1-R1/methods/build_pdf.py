"""Document-only compiler. Does not import any scientific or historical code."""
from pathlib import Path
import os, subprocess, shutil, json, hashlib
ROOT=Path(__file__).resolve().parents[1]
OLD=Path("C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/SRG_REDISCOVERY/SIMULATION_RECONSTRUCTION_RESEARCH/VOLUME_I_01_R1/build")
build=ROOT/"build"; build.mkdir(exist_ok=True)
exe=build/"toolchain/tectonic.exe"; exe.parent.mkdir(exist_ok=True)
if not exe.exists(): shutil.copyfile(OLD/"toolchain/tectonic.exe",exe)
for name in ["tectonic-cache","cache"]:
    if not (build/name).exists() and (OLD/name).exists():
        shutil.copytree(OLD/name,build/name)
env=os.environ.copy()
for k,v in {"TECTONIC_CACHE_DIR":"tectonic-cache","XDG_CONFIG_HOME":"config","XDG_CACHE_HOME":"cache","TEMP":"tmp","TMP":"tmp"}.items():
    env[k]=str(build/v); (build/v).mkdir(exist_ok=True)
(build/"font-cache").mkdir(exist_ok=True)
(build/"fonts.conf").write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><cachedir>'+(build/"font-cache").as_posix()+'</cachedir></fontconfig>',encoding="utf-8")
env["FONTCONFIG_FILE"]=str(build/"fonts.conf"); env["FONTCONFIG_PATH"]=str(build)
cmd=[str(exe),"--untrusted","--keep-logs","--keep-intermediates","--outdir",str(build),str(ROOT/"manuscript.tex")]
n=1+len(list(build.glob("typeset_*.txt")))
log=build/f"typeset_{n:02d}.txt"
with log.open("w",encoding="utf-8") as f:
    proc=subprocess.run(cmd,cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT)
print(log.read_text(encoding="utf-8")[-10000:])
assert proc.returncode==0, proc.returncode
shutil.copyfile(build/"manuscript.pdf",ROOT/"manuscript.pdf")
version=subprocess.run([str(exe),"--version"],capture_output=True,text=True,env=env).stdout.strip()
receipt={"scope":"Document compilation only; no scientific imports, calculations or runs","command":cmd,"compiler_origin":str(OLD/"toolchain/tectonic.exe"),"compiler_sha256":hashlib.sha256(exe.read_bytes()).hexdigest(),"version":version,"pdf_bytes":(ROOT/"manuscript.pdf").stat().st_size,"pdf_sha256":hashlib.sha256((ROOT/"manuscript.pdf").read_bytes()).hexdigest(),"log":str(log.relative_to(ROOT)),"returncode":proc.returncode}
(ROOT/"BUILD_RECEIPT.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8")
print(json.dumps(receipt,indent=2))

