"""LOCAL ONLY: original-preservation checks and release inventory refresh."""
from pathlib import Path
import base64,gzip,hashlib,json,subprocess
from publication_runtime import ROOT,EVIDENCE
REPO=ROOT.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(p,*a):return subprocess.check_output(["git","-C",str(p),*a],text=True).splitlines()
old=json.loads(gzip.decompress(base64.b64decode((ROOT/"evidence/preservation_baseline.json.gz.b64").read_text())))
checks=[]
for e in old["paths"]:
    p=Path(e["path"]);s=p.stat()
    okay=sha(p)==e["sha256"] and s.st_size==e["bytes"] and s.st_mtime_ns==e["mtimeNs"]
    assert okay,str(p)
    checks.append({"path":str(p),"sha256":e["sha256"],"hash_size_mtime_unchanged":okay})
base=json.loads((EVIDENCE/"finalization_baseline.json").read_text())
for e in base["reviewedFiles"]:
    assert sha(ROOT/"reviewed_v0.1"/e["path"])==e["sha256"],e["path"]
review=ROOT/"CODEX_PAPER_B_PUBLICATION_VALIDATION_v0.1.md"
assert review.read_bytes().startswith((ROOT/"reviewed_v0.1"/review.name).read_bytes())
support=json.loads((EVIDENCE/"supporting_release_inputs.json").read_text())
for e in support:assert sha(REPO/e["repository_path"])==e["sha256"],e["repository_path"]
copy_path="research/folded_face_state/FOLDED_FACE_STATE_ATTACHMENT_v0.1.md"
current=git(REPO,"status","--porcelain=v1","--untracked-files=all")
outside=[x for x in current if not x[3:].startswith("papers/PAPER_B/") and x[3:]!=copy_path]
assert outside==old["modern"]["status"],"Unrelated modern Git state changed."
head=git(REPO,"rev-parse","HEAD");staged=git(REPO,"diff","--cached","--name-status")
assert head==old["modern"]["head"] and staged==old["modern"]["staged"]
hist=Path("C:/TORMENT/quantum_kernel")
assert {"head":git(hist,"rev-parse","HEAD"),"status":git(hist,"status","--porcelain=v1","--untracked-files=all")}==old["historical"]
result={"attribution":"Codex publication finalization, 2026-09-23","protected_paths":len(checks),
 "protected_hash_size_mtime_unchanged":True,"checks":checks,"archived_reviewed_files":44,
 "archived_reviewed_files_hashes_match":True,"original_validation_report_prefix_unchanged":True,
 "supporting_release_paths":len(support),"supporting_implementation_bytes_unchanged":True,
 "new_provenance_copy":copy_path,"modern_head":head[0],"index_unchanged":True,
 "unrelated_modern_status_unchanged":True,"historical_head":old["historical"]["head"][0],
 "historical_status_unchanged":True,"git_actions":"no staging, commit or push"}
(EVIDENCE/"preservation_status.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf8")
(ROOT/"PAPER_B_PRESERVATION_AND_STATUS_v0.1.1.md").write_text(
 "# Paper B preservation and Git receipt v0.1.1\n\n"
 f"All {len(checks)} originally protected files retain SHA-256, size and modification time. "
 "All 44 reviewed package files are preserved byte for byte in reviewed_v0.1. "
 "The original validation report is an unchanged prefix of the appended report.\n\n"
 "The ten supporting paths retain the recorded implementation, test, README and report bytes. "
 "One exact provenance copy was added under research/folded_face_state; the original was not changed. "
 "No model law, architecture, kernel file, Paper A/C, historical source or original scientific report was edited.\n\n"
 f"Modern HEAD remains {head[0]}. The index and all unrelated working-tree status entries are unchanged. "
 f"Historical HEAD remains {old['historical']['head'][0]} and its status is unchanged.\n\n"
 "No staging, commit or push. Revision v0.1.1 is prepared locally for approval. "
 "The relayed GPT acceptance applies to the identified v0.1 PDF's mathematical scope, not to an assertion that the later PDF bytes were already inspected.\n\n"
 "See evidence/v0.1.1/preservation_status.json and scientific_content_preservation.json for the checks. "
 "PROPOSED_GIT_ALLOWLIST.txt and PROPOSED_SUPPORTING_ALLOWLIST_v0.1.1.txt are separate exact release lists. "
 "SHA256SUMS.txt and SUPPORTING_SHA256SUMS_v0.1.1.txt record their contents.\n",encoding="utf8")
support_names=sorted(e["repository_path"] for e in support)
(ROOT/"PROPOSED_SUPPORTING_ALLOWLIST_v0.1.1.txt").write_text("\n".join(support_names)+"\n",encoding="utf8")
(ROOT/"SUPPORTING_SHA256SUMS_v0.1.1.txt").write_text(
 "\n".join(sha(REPO/name)+"  "+name for name in support_names)+"\n",encoding="utf8")
files=sorted(p for p in ROOT.rglob("*") if p.is_file()
 and ".build" not in p.relative_to(ROOT).parts and "__pycache__" not in p.relative_to(ROOT).parts
 and p.suffix!=".pyc" and p not in [ROOT/"SHA256SUMS.txt",ROOT/"PROPOSED_GIT_ALLOWLIST.txt"])
allow=ROOT/"PROPOSED_GIT_ALLOWLIST.txt";manifest=ROOT/"SHA256SUMS.txt"
all_files=sorted(files+[allow,manifest])
allow.write_text("\n".join(p.relative_to(REPO).as_posix() for p in all_files)+"\n",encoding="utf8")
manifest.write_text("\n".join(sha(p)+"  "+p.relative_to(ROOT).as_posix()
 for p in sorted(files+[allow]))+"\n",encoding="utf8")
print(json.dumps({"protected_unchanged":len(checks),"reviewed_files_preserved":44,
 "paper_paths":len(all_files),"support_paths":len(support_names),"head":head[0],"git_actions":"none"}))
