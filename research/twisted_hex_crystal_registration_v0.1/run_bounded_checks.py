"""Run only this packet's checks/render, then verify preservation and write receipt.
Never stages, commits, pushes, deletes, or changes a predecessor.
"""
from pathlib import Path
import datetime, hashlib, json, os, platform, subprocess, sys

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
PREFIX=HERE.relative_to(REPO).as_posix()+"/"

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):h.update(block)
    return h.hexdigest()

def dump(name,data):
    (HERE/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf8")

def git(*args):
    return subprocess.check_output(["git","--no-optional-locks","-C",str(REPO),*args]).decode("utf8")

def main():
    import numpy, sympy, matplotlib
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    env=os.environ.copy();env["PYTHONDONTWRITEBYTECODE"]="1"
    runs=[]
    for script in ("verify_crystal_geometry.py","verify_host_registration.py","render_figures.py"):
        cmd=[sys.executable,"-B","-X","utf8",str(HERE/script)]
        result=subprocess.run(cmd,cwd=HERE,env=env,capture_output=True,text=True,encoding="utf8")
        runs.append({"command":cmd,"cwd":str(HERE),"exit_code":result.returncode,
                     "stdout":result.stdout,"stderr":result.stderr,
                     "script_sha256":sha(HERE/script)})
        print(script+": "+("PASS" if result.returncode==0 else "FAIL"),flush=True)
        if result.returncode:break
    evidence={"attribution":"NEW_CODEX_EXECUTION_NOT_ORIGINAL_HISTORICAL_STDOUT","started_utc":started,
              "finished_checks_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "runtime":{"python":platform.python_version(),"executable":sys.executable,
                         "numpy":numpy.__version__,"sympy":sympy.__version__,"matplotlib":matplotlib.__version__,
                         "PYTHONPATH":env.get("PYTHONPATH","")},
              "runs":runs,"all_pass":len(runs)==3 and all(r["exit_code"]==0 for r in runs),
              "verification_output_hashes":{name:sha(HERE/name) for name in (
                  "HISTORICAL_CRYSTAL.json","HOST_GEOMETRY.json","CANONICAL_CRYSTAL_CANDIDATE.json","REGISTRATION_VALIDATION.json") if (HERE/name).exists()},
              "scope":"No evolution, optimization, sweep, historical script tail, publication build, or source regeneration."}
    dump("EXECUTION_EVIDENCE.json",evidence)
    if not evidence["all_pass"]:return 1
    before=json.loads((HERE/"PRESERVATION_BEFORE.json").read_text(encoding="utf8"))
    changed={};missing={}
    for category in ("tracked","untracked"):
        changed[category]=[];missing[category]=[]
        for rel,expected in before[category].items():
            p=REPO/rel
            if not p.is_file():missing[category].append(rel)
            elif sha(p)!=expected:changed[category].append(rel)
    external={p:{"expected":h,"actual":sha(p)} for p,h in before["external_sources"].items()}
    untracked=set(git("ls-files","--others","--exclude-standard","-z").rstrip("\0").split("\0"))
    new=sorted(untracked-set(before["untracked"]))
    unexpected_new=[p for p in new if not p.startswith(PREFIX)]
    head=git("rev-parse","HEAD").strip()
    tracked_status=git("status","--porcelain","--untracked-files=no")
    stage=git("diff","--cached","--name-only")
    index=sha(REPO/".git/index")
    actual_remote=git("ls-remote","origin","refs/heads/main").strip()
    conditions={
        "all_original_tracked_bytes_preserved":not changed["tracked"] and not missing["tracked"],
        "all_original_untracked_bytes_preserved":not changed["untracked"] and not missing["untracked"],
        "external_originals_preserved":all(x["actual"]==x["expected"] for x in external.values()),
        "all_new_repository_files_in_research_folder":not unexpected_new,
        "HEAD_unchanged":head==before["head"],
        "branch_main":git("branch","--show-current").strip()=="main",
        "index_bytes_unchanged":index==before["index_sha256"],
        "no_staged_paths":not stage,
        "tracked_worktree_clean":not tracked_status,
        "remote_main_still_equals_start":actual_remote.split()[0]==before["head"]}
    preservation={"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "baseline":"PRESERVATION_BEFORE.json","baseline_sha256":sha(HERE/"PRESERVATION_BEFORE.json"),
        "starting_head":before["head"],"final_head":head,"actual_remote_main":actual_remote,
        "tracked_original_count":len(before["tracked"]),"untracked_original_count":len(before["untracked"]),
        "changed":changed,"missing":missing,"external_originals":external,
        "new_paths_outside_output_folder":unexpected_new,
        "index_sha256":index,"staged_paths":stage.splitlines(),"tracked_status":tracked_status,
        "checks":conditions,"pass":all(conditions.values()),
        "actions":{"staged":False,"committed":False,"pushed":False,"cleanup":False}}
    dump("FINAL_PRESERVATION.json",preservation)
    files=sorted(p for p in HERE.rglob("*") if p.is_file() and p.name!="SHA256SUMS.txt")
    (HERE/"SHA256SUMS.txt").write_text("".join(sha(p)+"  "+p.relative_to(HERE).as_posix()+"\n" for p in files),encoding="utf8")
    print(json.dumps({"historical_predicates":len(json.loads((HERE/"HISTORICAL_CRYSTAL.json").read_text())["checks"]),
                      "registration":json.loads((HERE/"REGISTRATION_VALIDATION.json").read_text())["passed"],
                      "preservation":preservation["pass"],"packet_file_count":len(files)+1,
                      "preservation_failures":[k for k,v in conditions.items() if not v]},indent=2))
    return 0 if preservation["pass"] else 1

if __name__=="__main__":
    raise SystemExit(main())
