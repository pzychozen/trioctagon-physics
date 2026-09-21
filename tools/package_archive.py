"""One-shot packaging recipe for the original Windows source tree.

This is archival tooling, not physics code. It refuses an already packaged tree.
Copied scientific files are never decoded, normalized, or rewritten.
"""

from pathlib import Path
import hashlib
import json
import shutil

REPO = Path(__file__).resolve().parents[1]
SOURCE = Path(r"C:\TORMENT\TRIOCTAGON_new")
BRIDGE = SOURCE / "research/top_to_recursive_bridge"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, text):
    target = REPO / path
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(target)
    target.write_bytes(text.encode("utf-8"))


if (REPO / "SOURCE_MANIFEST.md").exists():
    raise SystemExit("Archive already packaged; refusing to overwrite it.")

plan = []


def add(original, destination, role, status):
    original = Path(original)
    if not original.is_file() or original.is_symlink():
        raise ValueError(f"Missing or non-regular source: {original}")
    if (REPO / destination).exists():
        raise FileExistsError(REPO / destination)
    plan.append({"repository_path": destination, "original_authoritative_path": str(original),
                 "sha256": digest(original), "bytes": original.stat().st_size,
                 "mtime_ns_before": original.stat().st_mtime_ns,
                 "role": role, "status": status})


companions = {
    "A": ["PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md",
          "PAPER_A_REFERENCES_v0.2.md", "PAPER_A_SYMBOLS_AND_THEOREMS_v0.3.md",
          "PAPER_A_PROOF_AUDIT_v0.3.md", "PAPER_A_LITERATURE_CONTEXT_v0.1.md",
          "PAPER_A_REFERENCE_LEDGER_v0.1.md", "PAPER_A_POSITIONING_NOTE_v0.1.md"],
    "C": ["PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.3.1.md",
          "PAPER_C_REFERENCES_v0.2.md", "PAPER_C_SYMBOLS_AND_IDENTITIES_v0.2.md",
          "PAPER_C_PROOF_AUDIT_v0.2.2.md", "PAPER_C_LITERATURE_CONTEXT_v0.2.md",
          "PAPER_C_REFERENCE_LEDGER_v0.2.md", "PAPER_C_POSITIONING_NOTE_v0.2.md"],
}
pdfs = {"A": "PAPER_A_CYCLE_COVERING_DYNAMICS_v1.0.pdf",
        "C": "PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_v1.0.pdf"}
for letter, names in companions.items():
    for name in names:
        add(SOURCE / "reconstruction/papers" / name, f"papers/PAPER_{letter}/{name}",
            "Frozen manuscript" if "DRAFT" in name else "Current frozen-paper companion",
            "FROZEN_PRIMARY")
    pub = SOURCE / "reconstruction/publication" / f"paper_{letter}"
    publication_files = [pdfs[letter], f"paper_{letter}_publication.md",
                         f"paper_{letter}_final.tex", "publication_metadata.json",
                         f"paper_{letter}_pdf_manifest.sha256", f"paper_{letter}_build_report.md"]
    if letter == "C":
        publication_files.append("paper_C_publication_freeze_record.md")
    # Validate the already-existing PDF digest; no PDF regeneration or rendering.
    recorded_pdf_hash = (pub / f"paper_{letter}_pdf_manifest.sha256").read_text().split()[0]
    if digest(pub / pdfs[letter]) != recorded_pdf_hash:
        raise ValueError(f"Paper {letter} final PDF differs from publication manifest")
    for name in publication_files:
        is_primary = name.endswith((".pdf", ".tex")) or name.endswith("_publication.md")
        add(pub / name, f"papers/PAPER_{letter}/publication/{name}",
            "Existing publication artifact" if is_primary else "Publication provenance record",
            "FROZEN_PRIMARY" if is_primary else "SUPPORTING_PROVENANCE")

kernel_root = SOURCE / "kernel_physics"
for path in sorted(kernel_root.rglob("*")):
    relative = path.relative_to(kernel_root)
    if any(part in {".venv", "__pycache__", ".git", ".pytest_cache"} for part in relative.parts):
        continue
    if path.is_file() and path.suffix not in {".pyc", ".pyo"}:
        add(path, "kernel_physics/" + relative.as_posix(),
            "Clean kernel source, tests, requirements, or recorded validation", "EXECUTABLE_PRIMARY")

bridge_names = ["TOP_TO_RECURSIVE_BRIDGE_DERIVATION.md", "UNRESOLVED_INTERFACE_ASSUMPTIONS.md",
                "verify_bridge_identities.py", "bridge_symbolic_results.txt",
                "bridge_symbolic_results.json", "source_manifest.json"]
for name in bridge_names:
    add(BRIDGE / name, "research/top_to_recursive_bridge/" + name,
        "Completed first-bridge research or its recorded verification/provenance", "CURRENT_RESEARCH")

# Check that the recorded first-bridge sources still match, without running research.
old_manifest = json.loads((BRIDGE / "source_manifest.json").read_text(encoding="utf-8"))
for record in old_manifest["sources"]:
    if record["role"].startswith(("frozen_baseline", "kernel_physics")):
        if digest(Path(record["path"])) != record["sha256"]:
            raise ValueError(f"Authoritative baseline changed: {record['path']}")

# Hash historical supporting materials for an index only; do not copy their bytes.
historical = {}
for record in old_manifest["sources"]:
    if not record["role"].startswith(("frozen_baseline", "kernel_physics")):
        historical.setdefault(record["path"], {}).update(record)
extra_sources = [
    "pdfs_old/Recursive_Engines_Across_Scales__From_Vesica_Thermodynamics_to_QGS.pdf",
    "pdfs_old/recursive_thermodynamics.pdf",
    "pdfs_old/Recursive_SRG_Evolution_qutrip_opperator_dual_core_geometry_computational_interpretation.pdf",
    "pdfs_old/Structural_Interpretation_of_SRG_Tri_model.pdf",
    "pdfs_quantum/symmetry_normalization_geometric_origin.pdf",
    "pdfs_quantum/quantum_postulates.pdf",
    "pdfs_quantum/Modal Structure and Stability in an SRG-Inspired.pdf",
]
for rel in extra_sources:
    path = SOURCE / rel
    historical[str(path)] = {"path": str(path), "role": "historical_context_index_only",
                            "sha256": digest(path), "bytes": path.stat().st_size}
for record in historical.values():
    if digest(Path(record["path"])) != record["sha256"]:
        raise ValueError(f"Historical source changed from recorded hash: {record['path']}")

for record in plan:
    src = Path(record["original_authoritative_path"])
    dst = REPO / record["repository_path"]
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    record["sha256_after"] = digest(src)
    record["copy_sha256"] = digest(dst)
    record["mtime_ns_after"] = src.stat().st_mtime_ns
    record["byte_for_byte_match"] = src.read_bytes() == dst.read_bytes()
    if not (record["sha256"] == record["sha256_after"] == record["copy_sha256"]
            and record["byte_for_byte_match"]
            and record["mtime_ns_before"] == record["mtime_ns_after"]):
        raise ValueError(f"Integrity failure: {record['repository_path']}")

write(".gitattributes", "# Preserve scientific artifact bytes; do not normalize line endings.\n* -text\n*.pdf binary\n")
write(".gitignore", ".venv/\n__pycache__/\n*.py[cod]\n.pytest_cache/\n.DS_Store\nThumbs.db\n")
write("README.md", """# Tri-Octagon physics

Mathematical-physics reconstruction of the Tri-Octagon, by Hilmir Frímann Halldórsson.

The aim is a rigorous mathematical toy model with explicit proofs, connections
to established mathematics/physics, an executable physics kernel, and eventually
an interactive visual physics laboratory. This is not the production TORMENT
memory system.

Start with **[CURRENT_STATE.md](CURRENT_STATE.md)**, the primary human/machine handoff.

The three authoritative layers are:

1. [Paper C](papers/PAPER_C/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.3.1.md): exact folded geometry ([publication PDF](papers/PAPER_C/publication/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_v1.0.pdf)).
2. [Paper A](papers/PAPER_A/PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md): three-state nonlinear dynamics ([publication PDF](papers/PAPER_A/publication/PAPER_A_CYCLE_COVERING_DYNAMICS_v1.0.pdf)).
3. [kernel_physics](kernel_physics/README.md): the clean executable mathematical implementation, with its recorded 41-test baseline.

The current frontier is the **geometry-to-dynamical-state interface**.
The [completed first-bridge study](research/top_to_recursive_bridge/TOP_TO_RECURSIVE_BRIDGE_DERIVATION.md)
establishes exact structural results and a conditional kinematic complex-space
construction. Three complex dynamical amplitudes have not yet been derived.
No physical coupling between geometry and dynamics is claimed yet.

This repository is a byte-preserved archive/transfer of the current state.
See [SOURCE_MANIFEST.md](SOURCE_MANIFEST.md) for origins and hashes, and
[supporting_research/INDEX.md](supporting_research/INDEX.md) for historical sources
kept outside the frozen baseline. Large historical archives are not included.

Verify package bytes without executing research:

```sh
python -B tools/verify_archive.py
```

For kernel tests, follow its README and pinned requirements. Historical test
results are archived as recorded; packaging did not rerun them. The original
bridge script and scientific documents retain their original absolute paths;
see CURRENT_STATE.md before attempting research-script execution on another host.
""")
write("CURRENT_STATE.md", r"""# Current scientific state and handoff

Snapshot date: 2026-09-21. Packaging is archival/transfer only.

## Authoritative reading order

1. [Paper C v0.3.1](papers/PAPER_C/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.3.1.md) supplies the exact local folded shell.
2. [Paper A v0.5.1](papers/PAPER_A/PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md) supplies the abstract three-state nonlinear dynamics.
3. [kernel_physics](kernel_physics/README.md) implements those separate mathematical baselines.
4. [First-bridge derivation](research/top_to_recursive_bridge/TOP_TO_RECURSIVE_BRIDGE_DERIVATION.md) and [unresolved interface assumptions](research/top_to_recursive_bridge/UNRESOLVED_INTERFACE_ASSUMPTIONS.md) identify the frontier.

The publication subfolders also preserve both v1.0 PDFs and their existing
publication Markdown/TeX sources. The frozen research manuscripts retain the
detailed provenance and companion references. Packaging made no scientific edits
and does not supersede any source.

## Frozen status

```ini
PAPER_A = FROZEN
PAPER_C = FROZEN
KERNEL_PHYSICS = CLEAN
KERNEL_TEST_BASELINE = 41 PASSED
FIRST_GEOMETRY_TO_STATE_BRIDGE = COMPLETE
FIRST_BRIDGE_VERIFICATION = 51 / 51 PASSED
KERNEL_MODIFIED_BY_BRIDGE_WORK = NO
```

“Complete” means the scoped first-bridge investigation and its conditional results
are complete. It does not mean the physical/dynamical encoding has been derived.
The 41 tests and 51 predicates are the existing recorded executions, not new
packaging runs; the latter comprise 40 symbolic/combinatorial, 9 numerical
(including 2 expected counterexamples), and 2 preservation predicates.

## Exact results and remaining interface

```ini
GEOMETRY_TO_REAL_THREE_CHANNELS = EXACT
C3_BALANCED_DECOMPOSITION = EXACT
L3_PROJECTOR_IDENTITY = EXACT
THREE_ORIENTED_TANGENT_PLANES = EXACT
TANGENT_SPACE_COMPLEX_STRUCTURE = EXACT_GIVEN_ORIENTATION
GEOMETRY_TO_C3 = CONDITIONAL_KINEMATIC_CONSTRUCTION
THREE_COMPLEX_DYNAMICAL_AMPLITUDES_DERIVED = NO
SCALAR_PERIMETER_SINGLE_HARMONIC_ROUTE = OBSTRUCTED_UNDER_TESTED_ASSUMPTIONS
PHYSICAL_OBSERVABLE = UNRESOLVED
DYNAMICAL_PHASE_GENERATOR = UNRESOLVED
C3_TO_C3xC2_LIFT = DEFERRED
TOP_TO_RECURSION_HANDOFF = DEFERRED
PHYSICAL_ENCODING_READY_FOR_IMPLEMENTATION = NO
```

The exact balanced/transverse identity is

$$ u=rac{(1,1,1)^T}{sqrt3}, qquad P_perp=I-uu^T, qquad L_3=-3P_perp. $$

On each oriented face tangent plane, with outward unit normal $n_i$,

$$ J_i v=n_i	imes v, qquad J_i^2=-I. $$

Here $v$ is tangent, so $n_icdot v=0$. The square identity applies to that
two-dimensional plane, not all of ambient three-space. The direct sum of the
three planes admits a geometric identification with $mathbb C^3$. A physical
observable and dynamical phase generator have not been selected or derived.

The scalar-perimeter obstruction concerns one common Fourier harmonic per
octagon perimeter with scalar continuity imposed along all welded seam edges.
That ansatz leaves one real coefficient. It does not exclude other field types,
interface laws, or mode constructions. The report states the assumptions and
separates analytic proofs from finite checks.

The shell is one local module. No global host, physical rim boundary conditions,
upper/lower complex doubling, or recursive dynamics are defined by this package.
Historical Vesica, quantum, and SRG material is indexed as secondary provenance,
not admitted into the modern kernel.

## Archival integrity and execution scope

- Every copied scientific artifact is byte-identical to its original. Paths,
  line endings, scientific text, PDFs, and recorded outputs were not transformed.
- SOURCE_MANIFEST.md and archive_manifest.json map repository copies to originals
  and their hashes. SHA256SUMS.txt covers repository files except itself and Git
  internals; the Git commit identifies the checksum file.
- `python -B tools/verify_archive.py` checks this package using only the Python
  standard library. It executes no scientific source or historical code.
- The complete kernel includes its source, tests, pinned requirements, and
  validation records. Local `.venv` packages and bytecode are excluded.
- The copied bridge script still checks absolute original paths from its copied
  source manifest. Its original Windows execution command and imports are
  preserved. It is an archival script, not promised portable on a fresh clone.
  Do not rewrite it or rerun it merely to validate packaging.
- Original scientific documents contain local paths and references to earlier
  work outside this selected archive. Use this handoff's repository-relative
  links and SOURCE_MANIFEST.md to locate included artifacts; excluded historical
  material is identified in supporting_research/INDEX.md.
- Publication build reports and manifests describe their original build trees;
  compiler caches, temporary renders, intermediate AST files, and historical
  execution packages are intentionally not copied. PDFs were not regenerated.

No new license, physical interpretation, second bridge, or production-system
change is introduced by this archival snapshot.
""")

index = ["# Supporting historical research index", "",
         "Status: SUPPORTING_PROVENANCE. Index only; the listed PDFs, archives, and",
         "archive members are not copied into this repository and are not part of",
         "the frozen modern kernel. No scientific validity, lineage, or admission",
         "decision is inferred from filenames. No historical code was executed.", "",
         "The first bridge used TriOctagon_E8-SU3-Geometry.pdf §§9,12 and the",
         "structural quantum reconstruction §13 as secondary mathematical clues.",
         "DMQPF, the Vesica/thermodynamics material, the SRG archives, and the other",
         "quantum documents remain historical context; later bridges are deferred.", "",
         "Original absolute locations and SHA-256 values are preserved below. For",
         "extracted members, the original ZIP and member name are also recorded.",
         "All listed hashes were checked during packaging without rewriting sources.", ""]
for i, record in enumerate(historical.values(), 1):
    index += [f"## H{i:02d} — {Path(record['path']).name}", "",
              f"- Original location: `{record['path']}`",
              f"- SHA-256: `{record['sha256']}`",
              f"- Inventory role: `{record['role']}`",
              "- Repository inclusion: INDEX_ONLY; status: SUPPORTING_PROVENANCE."]
    if "archive" in record:
        index += [f"- Original archive: `{record['archive']}`",
                  f"- Member: `{record['member']}`"]
    index += [""]
write("supporting_research/INDEX.md", "\n".join(index)+"\n")

manifest_lines = ["# Source manifest", "", "Snapshot: 2026-09-21.", "",
                  "Every row is a copied scientific artifact. SHA-256 is identical",
                  "before copying, after copying at the original, and in this repository.",
                  "Direct byte comparisons and unchanged original modification times",
                  "were also verified. No line ending normalization or scientific",
                  "transformation was performed. Original absolute paths are provenance,",
                  "not required locations for reading the repository.", "",
                  "| Repository path | Original authoritative path | SHA-256 | Role | Status |",
                  "|---|---|---|---|---|"]
for record in plan:
    manifest_lines.append("| " + " | ".join(
        f"`{record[k]}`" if k in {"repository_path", "original_authoritative_path", "sha256"}
        else record[k] for k in ("repository_path", "original_authoritative_path", "sha256", "role", "status")) + " |")
manifest_lines += ["", "## New packaging records", "",
                  "README.md, CURRENT_STATE.md, this manifest, archive_manifest.json,",
                  "SHA256SUMS.txt, supporting_research/INDEX.md, .gitattributes,",
                  ".gitignore, and tools/*.py are newly authored archival documentation",
                  "or integrity tooling (SUPPORTING_PROVENANCE), not transformed",
                  "scientific artifacts. Their hashes are in SHA256SUMS.txt, except",
                  "that checksum file itself, whose bytes are identified by Git.", "",
                  "## Exclusions and portability", "",
                  "No historical archives/PDF collection, production TORMENT, kernel_TO,",
                  "kernel_new, kernel_torment, temporary render, compiler cache, local",
                  "virtual environment, or bytecode tree is packaged. The only PDFs",
                  "copied are the two existing final Paper A/C publication PDFs.", "",
                  "Scientific links and original execution paths inside copied files",
                  "are intentionally unchanged. CURRENT_STATE.md provides the portable",
                  "navigation and explains the bridge script's original-path dependency.", "",
                  f"COPIED_SCIENTIFIC_ARTIFACTS = {len(plan)}",
                  "FILES_TRANSFORMED = 0", "AUTHORITATIVE_SOURCE_MODIFIED = NO", ""]
write("SOURCE_MANIFEST.md", "\n".join(manifest_lines))
write("archive_manifest.json", json.dumps({
    "snapshot_date": "2026-09-21", "operation": "BYTE_PRESERVED_COPY",
    "source_root": str(SOURCE), "copied_scientific_artifact_count": len(plan),
    "files_transformed": 0, "authoritative_source_modified": False,
    "original_kernel_test_baseline": "41 PASSED; not rerun during packaging",
    "original_bridge_verification": "51/51 PASSED; not rerun during packaging",
    "files": plan, "supporting_sources_indexed_not_copied": list(historical.values()),
}, indent=2, ensure_ascii=False)+"\n")

# Final source pass covers all selected originals, not just the initial bridge manifest.
for record in plan:
    original = Path(record["original_authoritative_path"])
    if digest(original) != record["sha256"] or original.stat().st_mtime_ns != record["mtime_ns_before"]:
        raise ValueError(f"Original changed during packaging: {original}")

files = sorted(p for p in REPO.rglob("*") if p.is_file() and ".git" not in p.relative_to(REPO).parts)
write("SHA256SUMS.txt", "".join(f"{digest(p)}  {p.relative_to(REPO).as_posix()}\n" for p in files))
print(json.dumps({"copied_scientific_artifacts": len(plan), "files_packaged": len(files)+1,
                  "files_transformed": 0, "supporting_sources_indexed": len(historical)}, indent=2))
