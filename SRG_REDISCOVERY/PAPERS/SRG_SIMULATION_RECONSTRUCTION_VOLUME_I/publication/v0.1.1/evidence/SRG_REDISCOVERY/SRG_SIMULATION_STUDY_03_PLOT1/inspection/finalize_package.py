"""Verify preservation and package an existing analysis; no dynamics execution."""
from pathlib import Path
import ast, datetime, hashlib, importlib.metadata, json, re, shutil, subprocess, zipfile
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
LEDGER=ROOT.parent/"SIMULATION_RECONSTRUCTION_RESEARCH"
ARCHIVE="SRG_SIMULATION_STUDY_03_PLOT1_GPT_REVIEW.zip"
assert REPO.name=="trioctagon-physics"
assert ROOT.name=="SRG_SIMULATION_STUDY_03_PLOT1"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write_json(p,obj): p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding="utf-8")
def git(*args):
    return subprocess.run(["git",*args],cwd=REPO,check=True,capture_output=True,
                          text=True,encoding="utf-8").stdout.rstrip("\r\n")
baseline=json.loads((ROOT/"inspection/preservation_before.json").read_text(encoding="utf-8-sig"))
protected=[]
for rec in baseline["protected_files"]:
    p=Path(rec["path"])
    current={"path":str(p),"bytes":p.stat().st_size,"sha256":sha(p)}
    current["unchanged"]=current["bytes"]==rec["bytes"] and current["sha256"]==rec["sha256"]
    assert current["unchanged"],str(p)
    protected.append(current)
assert len(protected)==119

original_specs=[
 ("plot_1.py","Simulations_Trash/Simulations_part_1/plot_1.py","ORIGINAL source"),
 ("tetrahedral_attractors_logic.mp4","Simulations_Trash/Simulations_part_1/tetrahedral_attractors_logic.mp4","ORIGINAL movie; ATTRIBUTED source; exact run join UNLINKED"),
 ("PLOT_1_tetrahedral_states_20250712_015421.csv","Simulations_Trash/Simulations_part_1/PLOT_1_tetrahedral_states_20250712_015421.csv","ORIGINAL log A; ATTRIBUTED by schema/equation checks"),
 ("tetrahedral_states_20250712_015647.csv","Simulations/CSV/tetrahedral_states_20250712_015647.csv","ORIGINAL log B; ATTRIBUTED by schema/equation checks"),
 ("Tetrahedron_7_position_trace_with_teleport_events.png","Simulations_Trash/Simulations_part_1/Tetrahedron_7_position_trace_with_teleport_events.png","ORIGINAL postprocessing chart; ATTRIBUTED to B; generator missing"),
 ("Tetrahedron_7_GRF_over_time.png","Simulations_Trash/Simulations_part_1/Tetrahedron_7_GRF_over_time.png","ORIGINAL postprocessing chart; ATTRIBUTED to B; generator missing"),
 ("3Dtriangles.py","Simulations_Trash/Simulations_part_2/3Dtriangles.py","ORIGINAL comparison source"),
]
copies=[]
for name,rel,kind in original_specs:
    original=REPO/"SRG_REDISCOVERY/OLD_MATERIAL"/rel
    copied=ROOT/"originals"/name
    assert original.read_bytes()==copied.read_bytes()
    copies.append({"original_path":original.as_posix(),"copy_path":copied.relative_to(ROOT).as_posix(),
                   "bytes":copied.stat().st_size,"sha256":sha(copied),"byte_identical":True,
                   "evidence_class_and_attribution":kind})
instructions=[]
for p in sorted((ROOT/"instructions").glob("*.md")):
    original=Path("C:/Users/Notandi/Downloads")/p.name
    assert original.read_bytes()==p.read_bytes()
    instructions.append({"original_path":original.as_posix(),"copy_path":p.relative_to(ROOT).as_posix(),
                         "sha256":sha(p),"byte_identical":True})
(ROOT/"ledger").mkdir(exist_ok=True)
for name in ("SIMULATION_STUDY_LEDGER.md","RESEARCH_CHARTER_v0.1.md"):
    shutil.copyfile(LEDGER/name,ROOT/"ledger"/name)
ledger_text=(ROOT/"ledger/SIMULATION_STUDY_LEDGER.md").read_text(encoding="utf-8")
assert "**IN REVIEW" in ledger_text and "ACCEPTED BASELINE" in ledger_text

required=["START_HERE.md","CONSTRUCTION.md","ORIGINAL_MOVIE_REVIEW.md","ORIGINAL_LOG_ANALYSIS.md",
          "TIME_SWITCH_AND_MOVEMENT.md","SIMULATION_02_COMPARISON.md","VERIFICATION_AND_PRESERVATION.md"]
checked_links=0
for p in [*(ROOT/n for n in required),ROOT/"inspection/README.md",ROOT/"ledger/SIMULATION_STUDY_LEDGER.md"]:
    assert p.is_file() and p.stat().st_size>100
    content=p.read_text(encoding="utf-8")
    assert "\ufffd" not in content
    for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)",content):
        target=unquote(match.group(1).strip("<>"))
        if target.startswith(("https://","http://","#")):continue
        target=re.sub(r":\d+$","",target.split("#")[0])
        candidate=Path(target) if re.match(r"^[A-Za-z]:/",target) else p.parent/target
        # This one report is produced below after all preservation checks pass.
        assert candidate.exists() or candidate==ROOT/"analysis/preservation_after.json",f"Missing link: {p.name}: {target}"
        checked_links+=1
for p in (ROOT/"inspection").glob("*.py"):
    ast.parse(p.read_text(encoding="utf-8"),filename=str(p))

movie=json.loads((ROOT/"analysis/movie_inspection.json").read_text())
assert movie["decoded_frames"]==200
for rec in movie["frame_records"]:
    assert sha(ROOT/rec["path"])==rec["sha256"]
summary=json.loads((ROOT/"analysis/log_summary.json").read_text())
assert summary["A"]["data_rows"]==8736 and summary["A"]["callbacks"]==1092
assert summary["B"]["data_rows"]==3520 and summary["B"]["callbacks"]==440
assert all(summary[k]["partial_or_corrupt_blocks"]==0 for k in ("A","B"))
independent=json.loads((ROOT/"analysis/independent_checks.json").read_text())
for k in ("A","B"):
    assert all(value<1e-12 for key,value in independent[k].items() if key.endswith("_residual"))

head=git("rev-parse","HEAD")
index_path=Path(git("rev-parse","--git-path","index"))
if not index_path.is_absolute():index_path=REPO/index_path
index_sha=sha(index_path)
status=git("status","--porcelain=v1","--untracked-files=normal").splitlines()
old=baseline["status"]
removed=sorted(set(old)-set(status))
added=sorted(set(status)-set(old))
expected=["?? SRG_REDISCOVERY/SIMULATION_RECONSTRUCTION_RESEARCH/",
          "?? SRG_REDISCOVERY/SRG_SIMULATION_STUDY_03_PLOT1/"]
assert head==baseline["head"] and index_sha==baseline["index_sha256"]
assert not removed and added==expected,(removed,added)
preservation={
 "verified_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "head":head,"head_unchanged":True,"index_sha256":index_sha,"index_unchanged":True,
 "before_status_entries":len(old),"after_status_entries":len(status),
 "removed_or_changed_prior_entries":removed,"added_entries":added,
 "protected_file_count":len(protected),"all_protected_files_unchanged":True,"protected_files":protected,
 "all_original_copies_byte_identical":True,"original_copies":copies,
 "decoded_frame_hashes_verified":200,"document_links_checked":checked_links,
 "scope":"Hash coverage is selected originals, aliases, attachments and prior packages; not every unrelated untracked file.",
 "writes_confined_to":[ROOT.as_posix(),LEDGER.as_posix()],
 "no_simulation_run":True,"no_source_or_kernel_changes":True,"no_staging_commits_pushes_publication":True
}
write_json(ROOT/"analysis/preservation_after.json",preservation)
assert (ROOT/"analysis/preservation_after.json").is_file()
files=sorted(p for p in ROOT.rglob("*") if p.is_file() and p.name not in ("MANIFEST.json",ARCHIVE))
payload=[{"path":p.relative_to(ROOT).as_posix(),"bytes":p.stat().st_size,"sha256":sha(p)} for p in files]
versions={}
for name in ("numpy","matplotlib","opencv-python","pillow","imageio-ffmpeg"):
    try: versions[name]=importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError: versions[name]="not registered under this package name"
manifest={
 "task":"SRG_SIMULATION_STUDY_03_PLOT1","date":"2026-10-22","scientific_lead":"GPT",
 "author_research_direction":"Hilmir Frímann Halldórsson","research_engineer":"Codex","review_status":"IN REVIEW",
 "scope":"One historical simulation; source/evidence analysis only. No new simulation, old-program import, RNG draw or calculated-state propagation.",
 "review_directory":ROOT.as_posix(),"archive_name":ARCHIVE,
 "original_copies":copies,"supplied_instruction_copies":instructions,
 "confirmed_log_A_aliases":[
  (REPO/"SRG_REDISCOVERY/OLD_MATERIAL/Simulations/CSV/PLOT_1_tetrahedral_states_20250712_015421.csv").as_posix(),
  (REPO/"SRG_REDISCOVERY/OLD_MATERIAL/Simulations_Trash/Simulations_part_3/PLOT_1_tetrahedral_states_20250712_015421.csv").as_posix()],
 "movie_to_log_join":{"formal_original_run_provenance":"UNLINKED",
  "candidate":"B callback q = movie frame f + 1",
  "tested_movie_frames":[0,1,6,34,82,120,184,199],
  "limitation":"Strong sampled content correspondence; no historical export receipt, initial state/RNG, or full 200-frame numeric join."},
 "visual_review":{"decoded_all_frames":200,"consecutive_sheets_reviewed":[[0,19],[20,39],[80,99],[120,139],[180,199]],
  "full_resolution_stills_reviewed":[0,1,6,199],"overview_reviewed":True,
  "comparison_panel_reviewed":True,"all_six_numerical_figures_reviewed":True,
  "historical_charts_reviewed":2,"excluded_neighbor_images_reviewed":2,
  "not_claimed":"All frames manually inspected or uninterrupted video playback"},
 "ledger":{"canonical_path":(LEDGER/"SIMULATION_STUDY_LEDGER.md").as_posix(),
  "snapshot_path":"ledger/SIMULATION_STUDY_LEDGER.md","sha256":sha(LEDGER/"SIMULATION_STUDY_LEDGER.md"),
  "prior_status":"Simulations01/02 accepted baseline per supplied charter;03 IN REVIEW"},
 "environment":{"python":independent["static"]["python"],"packages":versions,
  "matplotlib_callback_source":independent["static"]["library_source"],
  "matplotlib_callback_source_sha256":independent["static"]["library_source_sha256"],
  "execution":"Command Prompt; conda activate torment","historical_environment":"MISSING"},
 "preservation":{"record":"analysis/preservation_after.json","all119_protected_files_unchanged":True,
  "head_unchanged":True,"index_unchanged":True,"only_new_status_entries":expected},
 "package_files":payload,"payload_bytes_excluding_manifest":sum(p["bytes"] for p in payload),
 "largest_payload_file":max(payload,key=lambda r:r["bytes"]),
 "archive_member_count":len(payload)+1,
 "manifest_self_hash":"Excluded to avoid self-reference; manifest bytes checked in ZIP against current file.",
 "archive_policy":"ZIP excluded from payload and itself. All archived members checked against live bytes and CRCs.",
 "stop":"Return for GPT/Hilmir review. No next simulation or publication."
}
write_json(ROOT/"MANIFEST.json",manifest)
files.append(ROOT/"MANIFEST.json")
with zipfile.ZipFile(ROOT/ARCHIVE,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(files):z.write(p,p.relative_to(ROOT).as_posix())
with zipfile.ZipFile(ROOT/ARCHIVE) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(files) and len(set(z.namelist()))==len(files)
    for p in files:
        assert hashlib.sha256(z.read(p.relative_to(ROOT).as_posix())).hexdigest()==sha(p)
assert git("rev-parse","HEAD")==head and sha(index_path)==index_sha
print(json.dumps({"preservation":"PASS","protected_files":len(protected),
 "prior_status_entries":len(old),"new_status_entries":added,
 "package_members":len(files),"payload_bytes":sum(p.stat().st_size for p in files),
 "archive":str(ROOT/ARCHIVE),"archive_bytes":(ROOT/ARCHIVE).stat().st_size,
 "archive_sha256":sha(ROOT/ARCHIVE),"all_members_readback_verified":True},indent=2))
