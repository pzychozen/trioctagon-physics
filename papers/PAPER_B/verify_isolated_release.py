"""LOCAL MAINTAINER test: committed baseline + the two exact release allowlists."""
from pathlib import Path
import argparse,hashlib,io,json,os,shutil,subprocess,sys,zipfile
from publication_runtime import ROOT,EVIDENCE
REPO=ROOT.parents[1]
BASE="a0875c493b23b7d1aaa718ea2b40aa17af9adcd2"
parser=argparse.ArgumentParser()
parser.add_argument("--destination",required=True)
parser.add_argument("--python",required=True)
args=parser.parse_args()
DEST=Path(args.destination).resolve()
if DEST.exists():raise RuntimeError("Choose a new empty destination; this tool does not delete existing trees.")
DEST.mkdir(parents=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
payload=subprocess.check_output(["git","-C",str(REPO),"archive","--format=zip",BASE])
with zipfile.ZipFile(io.BytesIO(payload)) as z:
    names=[x for x in z.namelist() if not x.endswith("/")]
    for name in z.namelist():
        assert (DEST/name).resolve().is_relative_to(DEST),name
    z.extractall(DEST)
paper=(ROOT/"PROPOSED_GIT_ALLOWLIST.txt").read_text().splitlines()
support=(ROOT/"PROPOSED_SUPPORTING_ALLOWLIST_v0.1.1.txt").read_text().splitlines()
assert not set(paper)&set(support)
for name in paper+support:
    src=(REPO/name).resolve();dst=(DEST/name).resolve()
    assert src.is_relative_to(REPO) and dst.is_relative_to(DEST)
    dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
MINI=DEST/"papers/PAPER_B"
env=os.environ.copy();env.pop("PYTHONPATH",None)
env["PYTHONNOUSERSITE"]="1";env["PYTHONDONTWRITEBYTECODE"]="1"
for key in ["PAPER_B_PANDOC","PAPER_B_TECTONIC","PAPER_B_TEX_CACHE","PAPER_B_PYTHON_PATH"]:
    if not env.get(key):raise RuntimeError("Explicit existing tool prerequisite required for isolated test: "+key)
commands=[
 ("saved_package",[str(MINI/"check_package.py")],"runtime"),
 ("paper_algebra",[str(MINI/"check_manuscript_algebra.py")],"paper"),
 ("figures",[str(MINI/"generate_figures.py")],"paper"),
 ("pdf_build",[str(MINI/"build_publication.py")],"paper"),
 ("public_verification",[str(MINI/"verify_publication.py")],"paper"),
 ("runtime_smoke",[str(MINI/"runtime_smoke.py")],"runtime"),
 ("cited_tests",["-m","unittest","kernel_physics.tests.test_face_state",
   "kernel_physics.tests.test_readouts","kernel_physics.tests.test_dynamics","-v"],"runtime")]
outcomes=[]
for label,cmd,mode in commands:
    runenv=env.copy()
    if mode=="runtime":runenv.pop("PAPER_B_PYTHON_PATH",None)
    result=subprocess.run([args.python,"-B","-X","utf8",*cmd],cwd=DEST,env=runenv,
                          capture_output=True,text=True,encoding="utf8")
    (EVIDENCE/("isolated_"+label+".log")).write_text(result.stdout+result.stderr,encoding="utf8")
    outcomes.append({"command":label,"mode":mode,"exit_code":result.returncode})
    if result.returncode:
        print((result.stdout+result.stderr)[-6000:])
        raise RuntimeError("Isolated command failed: "+label)
cfg=json.loads((ROOT/"publication_config.json").read_text())
pdf_rel=Path(cfg["publication_dir"])/cfg["pdf_name"]
same=sha(ROOT/pdf_rel)==sha(MINI/pdf_rel)
assert same,"Isolated regenerated PDF differs; inspect before accepting."
figures=[p.relative_to(ROOT) for p in (ROOT/"figures").glob("figure_*.*")]
assert all(sha(ROOT/p)==sha(MINI/p) for p in figures)
for name in ["runtime_smoke.json","publication_verification.json","figure_generation.json","manuscript_algebra.json"]:
    shutil.copy2(MINI/cfg["evidence_dir"]/name,EVIDENCE/("isolated_"+name))
execution_files=[name for name in paper+support if name.endswith(".py") or
                 name.endswith(".tex") or name.endswith("publication_config.json") or
                 "_PUBLICATION_v0.1.1.md" in name or name=="kernel_physics/README.md"]
execution_files+=["kernel_physics/geometry.py","kernel_physics/dynamics.py",
 "kernel_physics/__init__.py","kernel_physics/tests/__init__.py","kernel_physics/tests/test_dynamics.py"]
receipt={"attribution":"Codex isolated publication-content verification, 2026-09-23",
 "status":"PASS","baseline_commit":BASE,"committed_files":len(names),
 "assembly":"git archive baseline plus exactly the current paper and supporting allowlists",
 "paper_paths_at_assembly":len(paper),"support_paths":len(support),"destination":str(DEST),
 "no_full_archive_copy":True,"no_environment_install_or_upgrade":True,
 "tools_external_and_explicit":{k:env[k] for k in ["PAPER_B_PANDOC","PAPER_B_TECTONIC","PAPER_B_TEX_CACHE","PAPER_B_PYTHON_PATH"]},
 "python_executable":args.python,"commands":outcomes,
 "paper_pdf_identical_to_local_build":same,"pdf_sha256":sha(MINI/pdf_rel),
 "all_ten_figure_files_identical":True,
 "execution_inputs":[{"repository_path":name,"sha256":sha(DEST/name)} for name in sorted(set(execution_files))],
 "limits":"Baseline-plus-proposed-files test with existing declared tools; not a remote clone or clean-machine dependency installation. Final non-executable receipts may be appended after this run and synchronized with a final read-only package check."}
(EVIDENCE/"isolated_release_check.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf8")
print(json.dumps({k:v for k,v in receipt.items() if k not in ["execution_inputs","tools_external_and_explicit"]},indent=2))
