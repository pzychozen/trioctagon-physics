"""Read-only predecessor checks, packet receipt and subfolder-only hash manifest."""
from pathlib import Path
import datetime, hashlib, json, re, subprocess

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]

def sha(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as f:
        for block in iter(lambda:f.read(1048576),b""):h.update(block)
    return h.hexdigest()

def git(*args):
    return subprocess.check_output(["git","--no-optional-locks","-C",str(REPO),*args]).decode("utf8")

def main():
    before=json.loads((HERE/"PRESERVATION_BEFORE.json").read_text(encoding="utf8"))
    changed={k:[] for k in ("tracked","untracked")}
    missing={k:[] for k in changed}
    for category in changed:
        for rel,expected in before[category].items():
            p=REPO/rel
            if not p.is_file():missing[category].append(rel)
            elif sha(p)!=expected:changed[category].append(rel)
    current=set(git("ls-files","--others","--exclude-standard","-z").rstrip("\0").split("\0"))
    prefix=HERE.relative_to(REPO).as_posix()+"/"
    outside=[p for p in current-set(before["untracked"]) if not p.startswith(prefix)]
    head=git("rev-parse","HEAD").strip()
    index=sha(REPO/".git/index")
    qa=json.loads((HERE/"VIEWER_QA.json").read_text(encoding="utf8"))
    values=json.loads((HERE/"candidate_values.json").read_text(encoding="utf8"))
    render=json.loads((HERE/"RENDER_EVIDENCE.json").read_text(encoding="utf8"))
    report=(HERE/"CRYSTAL_SELECTION_ATLAS.md").read_text(encoding="utf8")
    missing_links=[p for p in re.findall(r"\]\(([^)]+)\)",report) if p!="FINAL_PRESERVATION.json" and not (HERE/p).exists()]
    png=list((HERE/"candidates").glob("*.png"))
    conditions={
      "all_existing_tracked_bytes_unchanged":not changed["tracked"] and not missing["tracked"],
      "all_existing_untracked_bytes_unchanged":not changed["untracked"] and not missing["untracked"],
      "all_new_files_beneath_visual_selection":not outside,
      "HEAD_unchanged":head==before["head"],
      "branch_unchanged":git("branch","--show-current").strip()==before["branch"],
      "index_bytes_unchanged":index==before["index_sha256"],
      "no_staged_paths":not git("diff","--cached","--name-only"),
      "tracked_worktree_clean":not git("status","--porcelain","--untracked-files=no"),
      "original_packet_manifest_unchanged":sha(HERE.parent/"SHA256SUMS.txt")==before["verified_packet_manifest_sha256"],
      "nine_mandatory_samples":values["sample_count"]==9 and [s["label"] for s in values["samples"]]==["0","s/16","s/8","s/6","3s/16","s/4","s/3","3s/8","s/2"],
      "all_upper_contacts_exact":values["all_upper_contacts_exact"],
      "all_nonzero_lower_edge_contacts_exact":values["all_nonzero_lower_edge_contacts_exact"],
      "18_individual_three_view_images":len(png)==18,
      "all_23_rendered_image_identities_current":len(render["files"])==23 and all(sha(HERE/p)==h for p,h in render["files"].items()),
      "offline_viewer_checks_pass":qa["pass"] and qa["passed"]==qa["total"],
      "offline_viewer_qa_matches_html":qa["generated_html_sha256"]==sha(HERE/"crystal_selection_viewer.html"),
      "all_atlas_links_resolve":not missing_links,
      "no_value_or_hand_designated_canonical":not values["any_value_designated_canonical"] and not values["any_handedness_designated_canonical"]
    }
    result={"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
      "starting_head":before["head"],"final_head":head,"tracked_original_count":len(before["tracked"]),
      "untracked_original_count":len(before["untracked"]),
      "changed":changed,"missing":missing,"new_files_outside_output_folder":outside,
      "index_sha256":index,"checks":conditions,"pass":all(conditions.values()),
      "browser_preview":qa["browser_preview"],
      "browser_limit":"Offline JavaScript controls and geometry checked; live browser/CSS/mobile rendering not verified because local-file navigation was blocked.",
      "staged":False,"committed":False,"pushed":False,
      "ATLAS_CREATED":"YES","INTERACTIVE_VIEWER_CREATED":"YES","SAMPLE_COUNT":9,
      "T_VALUES":[s["label"] for s in values["samples"]],
      "ALL_UPPER_CONTACTS_EXACT":"YES","ALL_NONZERO_T_LOWER_EDGE_CONTACTS_EXACT":"YES",
      "ANY_VALUE_DESIGNATED_CANONICAL":"NO","ANY_HANDEDNESS_DESIGNATED_CANONICAL":"NO",
      "HEAD_CHANGED":"NO","STAGED":"NO","COMMITTED":"NO","PUSHED":"NO"}
    (HERE/"FINAL_PRESERVATION.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
    assert result["pass"],json.dumps({k:v for k,v in conditions.items() if not v})
    files=sorted(p for p in HERE.rglob("*") if p.is_file() and p.name!="SHA256SUMS.txt")
    (HERE/"SHA256SUMS.txt").write_text("".join(sha(p)+"  "+p.relative_to(HERE).as_posix()+"\n" for p in files),encoding="utf8")
    assert all(sha(HERE/line.split("  ",1)[1])==line.split("  ",1)[0] for line in (HERE/"SHA256SUMS.txt").read_text().splitlines())
    print(json.dumps({"preservation_pass":result["pass"],"tracked_preserved":len(before["tracked"]),
      "untracked_preserved":len(before["untracked"]),"packet_file_count":len(files)+1,"HEAD":head,
      "offline_viewer_checks":qa["passed"],"manifest_verified":True},indent=2))

if __name__=="__main__":main()
