"""Check preservation and write only Paper B receipts/explicit package allowlist."""
from pathlib import Path
import base64,gzip,hashlib,json,subprocess
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(p,*args):return subprocess.check_output(["git","-C",str(p),*args],text=True).splitlines()
baseline=json.loads(gzip.decompress(base64.b64decode((ROOT/"evidence/preservation_baseline.json.gz.b64").read_text())))
checks=[]
for before in baseline["paths"]:
    p=Path(before["path"])
    after={"sha256":sha(p),"bytes":p.stat().st_size,"mtimeNs":p.stat().st_mtime_ns}
    same=all(after[k]==before[k] for k in after)
    checks.append({"path":str(p),"unchanged":same,**after})
assert all(x["unchanged"] for x in checks),"A protected input changed; investigate before finalizing."
modern={"head":git(REPO,"rev-parse","HEAD"),
        "status":git(REPO,"status","--porcelain=v1","--untracked-files=all"),
        "staged":git(REPO,"diff","--cached","--name-status")}
outside=[x for x in modern["status"] if not x[3:].startswith("papers/PAPER_B/")]
assert outside==baseline["modern"]["status"],"Working tree outside Paper B changed."
assert modern["head"]==baseline["modern"]["head"]
assert modern["staged"]==baseline["modern"]["staged"]
# The historical root is explicitly named by the preservation boundary.
historical_root=Path("C:/TORMENT/quantum_kernel")
historical={"head":git(historical_root,"rev-parse","HEAD"),
            "status":git(historical_root,"status","--porcelain=v1","--untracked-files=all")}
assert historical==baseline["historical"],"Historical Git state changed."
out={"attribution":"Codex Paper B preservation check, 2026-09-23",
     "baseline_created_utc":baseline["createdUtc"],"protected_paths":len(checks),
     "all_hashes_sizes_mtimes_unchanged":True,"checks":checks,
     "modern_head":modern["head"],"preexisting_status_entries":len(outside),
     "status_outside_paper_b_unchanged":True,"staged_state_unchanged":True,
     "historical_head":historical["head"],"historical_status_unchanged":True,
     "staging_commit_push":"none","publication_status":"local review draft only"}
(ROOT/"evidence/preservation_status.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf8")
(ROOT/"PAPER_B_PRESERVATION_AND_STATUS_v0.1.md").write_text(
 "# Paper B preservation and status receipt v0.1\n\n"
 "Checked by Codex on 2026-09-23 against the baseline captured before authoring.\n\n"
 f"- Protected files: **{len(checks)}**, all SHA-256, byte sizes and modification times unchanged.\n"
 "- Includes the current kernel, boundary/SRG implementation, face adapter, historical protected inputs, Paper A/C and earlier proof/continuity reports.\n"
 f"- Modern repository HEAD: **{modern['head'][0]}**, unchanged.\n"
 f"- Existing modern status entries outside Paper B: **{len(outside)}**, unchanged.\n"
 "- Git index: unchanged. No staging, commit or push.\n"
 f"- Historical repository HEAD: **{historical['head'][0]}**, unchanged; its status is unchanged.\n"
 "- New project writes are confined to papers/PAPER_B; ignored .build holds isolated dependencies/cache and QA renders.\n"
 "- No existing source-to-model map, recovery record or prior proof report was changed for this publication task.\n"
 "- Saved output is a review draft, not an uploaded, published or frozen paper.\n\n"
 "The machine receipt is evidence/preservation_status.json. The compressed baseline includes the original two repository status listings. The exact proposed commit paths are in PROPOSED_GIT_ALLOWLIST.txt; checksums are in SHA256SUMS.txt. No directory-wide staging is authorized.\n",
 encoding="utf8")
# Explicit names for the two self-referential inventories; the SHA file does not hash itself.
files=sorted(p for p in ROOT.rglob("*") if p.is_file() and ".build" not in p.parts
             and "__pycache__" not in p.parts and p.suffix!=".pyc"
             and p.name not in ["SHA256SUMS.txt","PROPOSED_GIT_ALLOWLIST.txt"])
allow=ROOT/"PROPOSED_GIT_ALLOWLIST.txt"
manifest=ROOT/"SHA256SUMS.txt"
entries=sorted(files+[allow,manifest])
allow.write_text("\n".join(p.relative_to(REPO).as_posix() for p in entries)+"\n",encoding="utf8")
manifest.write_text("\n".join(sha(p)+"  "+p.relative_to(ROOT).as_posix()
                    for p in sorted(files+[allow]))+"\n",encoding="utf8")
print(json.dumps({"protected":len(checks),"unchanged":True,"allowlist_paths":len(entries),
                  "checksum_entries":len(files)+1,"head":modern["head"][0],"git_actions":"none"}))
