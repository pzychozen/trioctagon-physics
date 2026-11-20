"""Windows Tectonic build; retain every attempt and source hashes."""
from pathlib import Path
import subprocess, shutil, json, hashlib, datetime, sys, platform, os
ROOT=Path(__file__).resolve().parent
build=ROOT/"build"
build.mkdir(exist_ok=True)
(ROOT/"output").mkdir(exist_ok=True)
previous=list(build.glob("attempt_*.json"))
attempt=f"attempt_{len(previous)+1:02d}"
out=build/"tex"; out.mkdir(exist_ok=True)
assert os.environ.get("CONDA_DEFAULT_ENV") == "torment", "Use run_python.cmd."
exe=shutil.which("tectonic")
(build/"fontcache").mkdir(exist_ok=True)
fontconfig=build/"fonts.conf"
fontconfig.write_text('<?xml version="1.0"?>\n<fontconfig><dir>C:/Windows/Fonts</dir><cachedir>'+
                      (build/"fontcache").as_posix()+'</cachedir></fontconfig>\n',"utf-8")
env=os.environ.copy()
env.update(FONTCONFIG_FILE=str(fontconfig),FONTCONFIG_PATH=str(build),
           SOURCE_DATE_EPOCH=str(int(datetime.datetime(2026,11,20,tzinfo=datetime.timezone.utc).timestamp())))
command=[exe,"--only-cached","--untrusted","--keep-logs","--keep-intermediates","--outdir",str(out),str(ROOT/"manuscript/main.tex")]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.run(command,cwd=ROOT,env=env,capture_output=True,text=True,encoding="utf-8",errors="replace")
(build/(attempt+".stdout.txt")).write_text(p.stdout,"utf-8")
(build/(attempt+".stderr.txt")).write_text(p.stderr,"utf-8")
record=dict(command=command,start_utc=start,returncode=p.returncode,platform=platform.platform(),python=sys.version,
    conda_environment=os.environ.get("CONDA_DEFAULT_ENV"),source_date_epoch=env["SOURCE_DATE_EPOCH"],
    engine_version=subprocess.run([exe,"--version"],capture_output=True,text=True).stdout.strip(),
    sources={f.relative_to(ROOT).as_posix():hashlib.sha256(f.read_bytes()).hexdigest() for f in (ROOT/"manuscript").glob("*.tex")})
if (out/"main.log").exists(): shutil.copyfile(out/"main.log",build/(attempt+".tex.log"))
if p.returncode==0:
    final=ROOT/"output/GM01_GM03_COMBINED_PAPER_v0.1.pdf"
    shutil.copyfile(out/"main.pdf",final)
    record["pdf_sha256"]=hashlib.sha256(final.read_bytes()).hexdigest()
    record["pdf"]=str(final)
    record["visual_inspection"]="pending; see separate final inspection record"
(build/(attempt+".json")).write_text(json.dumps(record,indent=2)+"\n","utf-8")
(ROOT/"BUILD_RECORD.json").write_text(json.dumps(record,indent=2)+"\n","utf-8")
print(p.stdout[-3500:]); print(p.stderr[-3500:])
print(json.dumps({"attempt":attempt,"returncode":p.returncode,"pdf_sha256":record.get("pdf_sha256")}))
sys.exit(p.returncode)
