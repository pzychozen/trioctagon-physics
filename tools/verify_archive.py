"""Verify archive bytes without importing or running scientific code."""

import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
expected = {}
for line in (root / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
    sha, name = line.split("  ", 1)
    path = (root / name).resolve()
    if not path.is_relative_to(root) or name in expected:
        raise SystemExit(f"Invalid checksum path: {name}")
    expected[name] = sha
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != sha:
        raise SystemExit(f"HASH MISMATCH: {name}")

manifest = json.loads((root / "archive_manifest.json").read_text(encoding="utf-8"))
allowed = {"FROZEN_PRIMARY", "EXECUTABLE_PRIMARY", "CURRENT_RESEARCH", "SUPPORTING_PROVENANCE"}
for record in manifest["files"]:
    if (record["status"] not in allowed or not record["byte_for_byte_match"]
            or expected.get(record["repository_path"]) != record["sha256"]
            or record["sha256"] != record["sha256_after"]
            or record["sha256"] != record["copy_sha256"]
            or record["mtime_ns_before"] != record["mtime_ns_after"]):
        raise SystemExit(f"INVALID PROVENANCE RECORD: {record['repository_path']}")

print(f"PASS: {len(expected)} file checksums; {len(manifest['files'])} byte-preserved scientific artifacts.")
print("SHA256SUMS.txt itself is identified by the Git commit; no scientific code executed.")
