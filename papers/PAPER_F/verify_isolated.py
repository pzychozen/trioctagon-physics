"""Run the unchanged verifier in a fresh repository-layout copy; no trajectories."""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys,time
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument("workspace",type=Path);args=p.parse_args()
dst=args.workspace.resolve()
assert not dst.exists(),"Use a fresh isolated directory"
repo=ROOT/"support/repository"
names=["research/paper_F_transverse_normal_form/paper_f_exact_checks_v0_2.py",
 "research/GATE_TORUS_INVESTIGATION_v0.1/TRANSVERSE_AXIS_FALSIFICATION.csv",
 "kernel_physics/dynamics.py","kernel_physics/readouts.py"]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before={}
for name in names:
 a=repo/name;b=dst/name;b.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a,b);before[name]=sha(a)
start=time.monotonic()
run=subprocess.run([sys.executable,"-B","-X","utf8",str(dst/names[0])],cwd=dst,capture_output=True)
ev=ROOT/"records"
(ev/"isolated_exact_checks.stdout.json").write_bytes(run.stdout)
(ev/"isolated_exact_checks.stderr.log").write_bytes(run.stderr)
assert run.returncode==0,run.stderr[-2000:]
data=json.loads(run.stdout)
accepted=json.loads((repo/"research/paper_F_transverse_normal_form/PAPER_F_v0.2_VALIDATION.json").read_text())["verification"]
def canonical(v):
 if isinstance(v,dict):return {k:canonical(x) for k,x in v.items() if k not in ("path","source","runtime")}
 if isinstance(v,list):return [canonical(x) for x in v]
 return v
assert canonical(data)==canonical(accepted),"Stop: validation differs beyond runtime/input paths"
assert data["passed"]==data["total"]==131 and data["new_model_runs"]==0
after={name:sha(dst/name) for name in names}
assert before==after
record={"attribution":"Codex fresh publication-build re-execution of the unchanged accepted verifier",
 "stdout_class":"New isolated execution output; distinct from preserved original validation",
 "command":[sys.executable,"-B","-X","utf8",str(dst/names[0])],"exit_code":run.returncode,"seconds":time.monotonic()-start,
 "input_identities":before,"inputs_unchanged":before==after,"131_predicates_match_accepted":True,
 "all_output_data_match_accepted_except_runtime_and_paths":True,
 "comparison_exclusions":["runtime","absolute path/source locator fields"],"new_model_runs":0,
 "checks_by_class":{"exact_zero_residual":89,"structural_or_discrete":36,"saved_binary64_data":6},
 "stdout_sha256":sha(ev/"isolated_exact_checks.stdout.json"),"stderr_sha256":sha(ev/"isolated_exact_checks.stderr.log"),
 "runtime":data["runtime"],"result":"PASS"}
(ev/"isolated_verification.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({"result":"PASS","passed":131,"input_files":4,"new_model_runs":0,"seconds":record["seconds"]}))
