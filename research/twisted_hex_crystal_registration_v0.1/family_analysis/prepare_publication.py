"""Census and freeze this research lane. Does not stage, commit, or push.

Preserves every pre-existing file; writes only new publication-control files
in family_analysis. Reproduction is best performed in a separate checkout.
"""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
LANE = HERE.parent
REPO = LANE.parent.parent
EXPECTED_HEAD = "1dca474e09b180664a17f85a0bb2f92967dd18f1"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=REPO)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name, obj):
    (HERE / name).write_text(json.dumps(obj, indent=2) + "\n", encoding="utf8")


def main():
    before = json.loads((HERE / "PRESERVATION_BEFORE.json").read_text())
    assert git("rev-parse", "HEAD").decode().strip() == EXPECTED_HEAD
    assert git("branch", "--show-current").decode().strip() == "main"
    assert git("rev-parse", "origin/main").decode().strip() == EXPECTED_HEAD
    remote = git("ls-remote", "origin", "refs/heads/main").decode().split()[0]
    assert remote == EXPECTED_HEAD
    assert not git("diff", "--name-only")
    assert not git("diff", "--cached", "--name-only")
    changes = {
        group: [p for p, digest in before[group].items()
                if not (REPO / p).is_file() or sha(REPO / p) != digest]
        for group in ("tracked", "untracked")
    }
    assert not any(changes.values()), changes
    lane_prefix = LANE.relative_to(REPO).as_posix() + "/"
    original_lane = [p for p in before["untracked"] if p.startswith(lane_prefix)]
    current_untracked = set(git("ls-files", "--others", "--exclude-standard", "-z")
                            .decode().rstrip("\0").split("\0"))
    new_outside = [p for p in current_untracked - set(before["untracked"])
                   if not p.startswith(lane_prefix)]
    assert not new_outside, new_outside
    manifest_results = []
    for manifest in (LANE / "SHA256SUMS.txt", LANE / "visual_selection/SHA256SUMS.txt"):
        entries = manifest.read_text().splitlines()
        for line in entries:
            digest, path = line.split("  ", 1)
            assert sha(manifest.parent / path) == digest, path
        manifest_results.append({"path": manifest.relative_to(REPO).as_posix(),
                                 "entry_count": len(entries), "pass": True})
    validation = json.loads((HERE / "family_validation.json").read_text())
    assert validation["pass"] and validation["passed"] == validation["total"]
    save("PRESERVATION_CHECK.json", {
        "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "starting_head": EXPECTED_HEAD, "origin_main": EXPECTED_HEAD,
        "actual_github_main": remote, "branch": "main",
        "tracked_checked": len(before["tracked"]),
        "preexisting_untracked_checked": len(before["untracked"]),
        "preexisting_lane_files": len(original_lane),
        "preexisting_unrelated_untracked": len(before["untracked"]) - len(original_lane),
        "changed": changes, "new_outside_lane": new_outside,
        "index_bytes_unchanged_before_staging": sha(REPO / ".git/index") == before["index_sha256"],
        "original_hash_manifests": manifest_results,
        "family_predicates_passed": validation["passed"],
        "family_predicates_total": validation["total"],
        "status": "PRESTAGE_PRESERVATION_PASS_NOT_A_PUBLICATION_RECEIPT",
    })
    controlled_names = ("PUBLICATION_CENSUS.json", "PUBLICATION_ALLOWLIST.txt",
                        "PUBLICATION_SHA256SUMS.txt")
    paths = {p.relative_to(REPO).as_posix() for p in LANE.rglob("*") if p.is_file()}
    paths.update((HERE / name).relative_to(REPO).as_posix() for name in controlled_names)
    paths = sorted(paths)
    assert len(paths) == len(set(paths))
    classes = collections.Counter()
    census = []
    for path in paths:
        relative = path[len(lane_prefix):]
        if relative.startswith("family_analysis/"):
            kind = "new_family_analysis_and_publication_controls"
        elif relative.startswith("visual_selection/"):
            kind = "preserved_visual_selection"
        else:
            kind = "preserved_original_registration_and_evidence"
        classes[kind] += 1
        census.append({"path": path, "class": kind,
                       "preexisting": path in before["untracked"],
                       "identity_scope": "PUBLICATION_SHA256SUMS.txt except that manifest itself"})
    save("PUBLICATION_CENSUS.json", {
        "path_count": len(paths), "class_counts": dict(classes), "paths": census,
        "inclusions": ["All 60 original lane files, without byte changes",
                       "Existing small render font-cache JSON retained because the preserved atlas manifest covers it",
                       "No environments, external corpora, or unrelated repository files added"],
        "exclusions": [],
        "receipt_location": "Execution-stage receipt is outside the repository so it cannot mutate the frozen staged package",
    })
    (HERE / "PUBLICATION_ALLOWLIST.txt").write_text("\n".join(paths) + "\n", encoding="utf8")
    manifest_path = (HERE / "PUBLICATION_SHA256SUMS.txt").relative_to(REPO).as_posix()
    (HERE / "PUBLICATION_SHA256SUMS.txt").write_text(
        "".join(sha(REPO / path) + "  " + path + "\n" for path in paths if path != manifest_path),
        encoding="utf8")
    actual = {p.relative_to(REPO).as_posix() for p in LANE.rglob("*") if p.is_file()}
    assert set(paths) == actual
    print(json.dumps({"path_count": len(paths), "class_counts": dict(classes),
                      "all_preexisting_bytes_preserved": True,
                      "publication_manifest_entries": len(paths) - 1}, indent=2))


if __name__ == "__main__":
    main()
