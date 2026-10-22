"""Static source comparison only. Historical modules are never executed."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
OLD = REPO / "SRG_REDISCOVERY/OLD_MATERIAL/Simulations_Trash"
sources = {}
trees = {}
for name in ("3Dtriangles.py", "recursive_attractor.py"):
    copied = ROOT / "source" / name
    original = OLD / "Simulations_part_2" / name
    raw = copied.read_bytes()
    assert raw == original.read_bytes()
    trees[name] = ast.parse(raw.decode("utf-8-sig"), filename=name)
    sources[name] = {"bytes":len(raw), "lines":len(raw.splitlines()),
                     "sha256":hashlib.sha256(raw).hexdigest(),
                     "copy_matches_original":True}
def function_body(tree, name):
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
    body = node.body[:]
    if isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
        body = body[1:]
    return [ast.dump(n, include_attributes=False) for n in body]
same = {name: function_body(trees["3Dtriangles.py"],name) ==
              function_body(trees["recursive_attractor.py"],name)
        for name in ("H","RPCO")}
assert all(same.values())
parts = []
def excerpt(path, ranges):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    parts.append(f"\nFILE: {path}\nSHA256: {hashlib.sha256(path.read_bytes()).hexdigest()}\n")
    for a,b in ranges:
        parts.extend(f"{i}: {lines[i-1]}\n" for i in range(a,b+1))
excerpt(OLD / "Simulations_part_1/plot_1.py",
        [(10,13),(86,86),(155,161)])
excerpt(REPO / "SRG_REDISCOVERY/R0_SOURCE_RECOVERY/source_manifest.json",
        [(947,960),(1003,1017)])
excerpt(REPO / "SRG_REDISCOVERY/R0_SOURCE_RECOVERY/SRG_R0_REPORT.md",
        [(320,328),(333,335)])
(ROOT / "inspection/provenance_excerpts.txt").write_text("".join(parts),encoding="utf-8")
result = {"sources":sources,"same_H_and_RPCO_AST_ignoring_docstrings":same,
          "scope":"Parse and compare source only. No source module imported, no update called, no simulation or trajectory reconstruction."}
(ROOT / "inspection/static_source_checks.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(result,indent=2))
