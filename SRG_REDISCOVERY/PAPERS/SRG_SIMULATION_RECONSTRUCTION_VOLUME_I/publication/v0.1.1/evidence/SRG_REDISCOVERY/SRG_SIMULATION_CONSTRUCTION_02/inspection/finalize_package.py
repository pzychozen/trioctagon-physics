"""Verify and package this construction review. No simulation operations."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
ZIP = ROOT / "SRG_SIMULATION_CONSTRUCTION_02_GPT_REVIEW.zip"
MANIFEST = ROOT / "MANIFEST.json"

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git(*args):
    return subprocess.check_output(["git", "--no-optional-locks", *args],
                                   cwd=REPO, text=True).strip()

before = json.loads((ROOT / "inspection/preservation_before.json").read_text(encoding="utf-8"))
protected = []
for item in before["hashes"]:
    actual = digest(Path(item["Path"]))
    assert actual == item["Hash"].lower(), item["Path"]
    protected.append({"path":item["Path"],"before_sha256":item["Hash"].lower(),
                      "after_sha256":actual,"unchanged":True})
head = git("rev-parse","HEAD")
index_path = Path(git("rev-parse","--git-path","index"))
if not index_path.is_absolute():
    index_path = REPO / index_path
index_hash = digest(index_path)
status = git("status","--porcelain=v1","--untracked-files=normal").splitlines()
before_set = set(before["status"])
after_set = set(status)
added = sorted(after_set-before_set)
removed = sorted(before_set-after_set)
expected = "?? SRG_REDISCOVERY/SRG_SIMULATION_CONSTRUCTION_02/"
assert head == before["head"]
assert index_hash == before["index"].lower()
assert added == [expected] and not removed, (added,removed)
original_movie = Path(protected[-1]["path"])
assert digest(ROOT / "evidence/tetrahedral_attractors_animation.mp4") == digest(original_movie)
for name in ("3Dtriangles.py","recursive_attractor.py"):
    original = REPO / "SRG_REDISCOVERY/OLD_MATERIAL/Simulations_Trash/Simulations_part_2" / name
    assert digest(original) == digest(ROOT / "source" / name)

for filename, key in [
    ("video_inspection.json","selected_frames"),
    ("early_movie_inspection.json","samples"),
    ("jump_window_inspection.json","samples"),
]:
    ledger = json.loads((ROOT / "inspection" / filename).read_text(encoding="utf-8"))
    for entry in ledger[key]:
        assert digest(ROOT / entry["path"]) == entry["sha256"], entry["path"]

required = ["START_HERE.md","CONSTRUCTION_WALKTHROUGH.md","TIME_AND_MOVEMENT.md",
            "VISUAL_EVIDENCE.md","SIMULATION_01_COMPARISON.md"]
link_count = 0
for name in required:
    path = ROOT / name
    assert path.is_file()
    for target in re.findall(r"\]\(([^)]+)\)",path.read_text(encoding="utf-8")):
        if target.startswith(("https://","http://","#")):
            continue
        target = re.sub(r":\d+$","",target)
        link_path = Path(target)
        if not link_path.is_absolute():
            link_path = ROOT / link_path
        # Manifest is created below; every other link must exist now.
        if link_path == MANIFEST:
            continue
        if link_path == ROOT / "inspection/preservation_after.json":
            continue
        assert link_path.exists(), (name,target)
        link_count += 1

preservation = {
    "checked_at_utc":datetime.now(timezone.utc).isoformat(),
    "protected_files":protected,
    "head_before":before["head"],"head_after":head,"head_unchanged":True,
    "index_before_sha256":before["index"].lower(),
    "index_after_sha256":index_hash,"index_unchanged":True,
    "existing_git_status_entries_unchanged":True,
    "baseline_status_entry_count":len(before["status"]),
    "added_status_entries":added,"removed_status_entries":removed,
    "source_and_movie_copies_byte_identical":True,
    "all_extracted_frame_ledger_hashes_verified":True,
    "markdown_file_links_checked":link_count,
    "scope":"Hashes cover the six explicitly listed protected inputs. Git HEAD, index and pre-existing status entries are unchanged. Existing untracked research was not recursively rehashed. All task writes were confined to this new package directory.",
    "historical_simulations_executed":0,
}
(ROOT / "inspection/preservation_after.json").write_text(
    json.dumps(preservation,indent=2),encoding="utf-8")

payload = sorted(p for p in ROOT.rglob("*")
                 if p.is_file() and p not in (ZIP,MANIFEST))
def role(path):
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith("source/"):
        return "unchanged historical source copy"
    if rel.endswith(".mp4"):
        return "unchanged strongly source-associated historical movie"
    if rel.startswith("evidence/frames/"):
        return "new full-resolution PNG decoded from historical movie"
    if rel.startswith("evidence/"):
        return "new labeled contact sheet of historical movie frames"
    if rel.startswith("inspection/"):
        return "new inspection helper, derived record, excerpt or preservation record"
    return "new construction review document"

manifest = {
    "task":"SRG_SIMULATION_CONSTRUCTION_02",
    "scientific_lead":"GPT","investigator":"Codex",
    "created_at_utc":datetime.now(timezone.utc).isoformat(),
    "source_origin":protected[0]["path"],
    "historical_movie_origin":str(original_movie),
    "movie_attribution":"Strong association by unique declared filename in inspected OLD_MATERIAL Python sources, title, scene, frame count and fps. Exact generating source snapshot/RNG/callback chronology not certified.",
    "scope":"Read-only historical source and media analysis; new output only in this package. Zero historical simulation runs.",
    "preservation_record":"inspection/preservation_after.json",
    "manifest_exclusions":["MANIFEST.json", ZIP.name],
    "payload_count_excluding_manifest":len(payload),
    "files":[{"path":p.relative_to(ROOT).as_posix(),"bytes":p.stat().st_size,
              "sha256":digest(p),"role":role(p)} for p in payload],
}
MANIFEST.write_text(json.dumps(manifest,indent=2),encoding="utf-8")
members = sorted(payload + [MANIFEST])
with zipfile.ZipFile(ZIP,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for path in members:
        z.write(path,path.relative_to(ROOT).as_posix())
with zipfile.ZipFile(ZIP) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(members)
    for path in members:
        assert hashlib.sha256(z.read(path.relative_to(ROOT).as_posix())).hexdigest() == digest(path)
assert git("rev-parse","HEAD") == head
assert digest(index_path) == index_hash
assert git("status","--porcelain=v1","--untracked-files=normal").splitlines() == status
print(json.dumps({"zip":str(ZIP),"bytes":ZIP.stat().st_size,"sha256":digest(ZIP),
                  "verified_zip_members":len(members),
                  "protected_files_unchanged":len(protected),
                  "existing_git_status_entries_unchanged":len(before["status"]),
                  "only_new_status_entry":expected,
                  "simulation_runs":0},indent=2))
