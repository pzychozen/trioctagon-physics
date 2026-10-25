"""Narrow E01/E02 document and byte checks, followed by review packaging.

Does not import or execute historical/scientific code, load numerical arrays,
evaluate scientific equations, generate figures, or call Git.
Run in CMD under conda environment torment after the final PDF visual review.
Local preservation checks require the original v0.1 directory and attachments.
"""
from pathlib import Path
import json, hashlib, zipfile, difflib, re, shutil, sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
ZIP_NAME = "SRG_VOLUME_III_SIM06_SIM07_v0.1_R1_REVIEW.zip"
assert not (ROOT / ZIP_NAME).exists(), "Refusing to overwrite sealed review ZIP"
sys.path.insert(0, "C:/Users/Notandi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/Lib/site-packages")
from pypdf import PdfReader

def digest(data):
    return hashlib.sha256(data).hexdigest()

def identity(path):
    data = path.read_bytes()
    return {"bytes": len(data), "sha256": digest(data)}

def read(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))

def write(name, value):
    target = ROOT / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def same(path, expected):
    actual = identity(path)
    assert actual == {k: expected[k] for k in ("bytes", "sha256")}, str(path)
    return actual

base = read("R1_INPUT_BASELINE.json")
old = Path(base["prior_directory"])
same(Path(base["prior_zip"]["path"]), base["prior_zip"])
old_files = {x["path"]: x for x in base["prior_review_files"]}
assert len(old_files) == 206
for name, record in old_files.items():
    same(old / name, record)
for record in base["external_inputs"]:
    same(Path(record["path"]), record)
same(ROOT / "r1_input/SOURCE_READBACK_E01_E02.md", base["external_inputs"][1])
preserved_copies = []
for path in sorted((ROOT / "baseline").rglob("*")):
    if path.is_file():
        name = path.relative_to(ROOT / "baseline").as_posix()
        same(path, old_files[name])
        preserved_copies.append({"path": "baseline/" + name, "original_path": name, **identity(path)})
copied_support = []
for name in old_files:
    if name.startswith(("evidence/", "handoff/")):
        same(ROOT / name, old_files[name])
        copied_support.append(name)
assert len([x for x in copied_support if x.startswith("evidence/")]) == 158
assert len([x for x in copied_support if x.startswith("handoff/")]) == 11
for name in ("CLAIM_EVIDENCE_MATRIX.md", "EVIDENCE_INDEX.md", "EVIDENCE_COPY_MANIFEST.json",
             "RECONSTRUCTION_SCOPE_AND_REMAINING_GAPS.md", "methods/build_pdf.py", "methods/render_pdf.py"):
    same(ROOT / name, old_files[name])

# Archive and member readback is byte preservation, not a scientific checker.
archives = read("handoff/INPUT_MANIFEST.json")["inputs"]
copies = read("EVIDENCE_COPY_MANIFEST.json")["copies"]
archive_results = []
for entry in archives:
    path = ROOT / "handoff" / entry["path"]
    same(path, entry)
    selected = [c for c in copies if c["parent_key"] == entry["key"]]
    with zipfile.ZipFile(path) as z:
        assert len(z.namelist()) == entry["member_count"]
        assert z.testzip() is None
        for c in selected:
            data = z.read(c["member"])
            assert digest(data) == c["sha256"], c["path"]
            assert (ROOT / c["path"]).read_bytes() == data, c["path"]
    archive_results.append({"key": entry["key"], "path": path.relative_to(ROOT).as_posix(),
                            **identity(path), "members": entry["member_count"],
                            "crc": "PASS", "selected_copies_verified": len(selected)})
assert sum(x["selected_copies_verified"] for x in archive_results) == 158

# Verify the entire manuscript-source change boundary.
source_names = ("manuscript.tex", "universe_sections.tex", "closing_sections.tex", "references.bib")
changed = [name for name in source_names if (ROOT / name).read_bytes() != (old / name).read_bytes()]
assert changed == ["closing_sections.tex", "references.bib"]
record = read("R1_SOURCE_CHANGE_RECORD.json")
for c in record["changed_manuscript_sources"]:
    same(old / c["path"], c["before"])
    same(ROOT / c["path"], c["after"])
before = (old / "closing_sections.tex").read_bytes()
after = (ROOT / "closing_sections.tex").read_bytes()
old_start = before.index(b"Both sources' GRF observer is")
new_start = after.index(b"Both sources use the pointwise diagnostic")
tail = b" This relation to displacement defines no force law."
assert before[:old_start] == after[:new_start]
assert before[before.index(tail, old_start):] == after[after.index(tail, new_start):]
old_bib = (old / "references.bib").read_bytes()
new_bib = (ROOT / "references.bib").read_bytes()
lines = old_bib.splitlines(keepends=True)
target = next(i for i, line in enumerate(lines) if line.startswith(b"@misc{s7creview,"))
assert target == 5
lines[target] = lines[target].replace(b"note={24 October.", b"note={25 October.")
assert b"".join(lines) == new_bib
diff = []
for name in source_names:
    a = (old / name).read_bytes().decode("utf-8").splitlines(keepends=True)
    b = (ROOT / name).read_bytes().decode("utf-8").splitlines(keepends=True)
    diff.extend(difflib.unified_diff(a, b, fromfile="v0.1/" + name, tofile="v0.1-R1/" + name))
assert (ROOT / "R1_EXACT_DIFF.patch").read_bytes() == "".join(diff).encode("utf-8")

pdf_id = identity(ROOT / "manuscript.pdf")
build_receipt = read("BUILD_RECEIPT.json")
same(ROOT / "manuscript.pdf", {"bytes": build_receipt["pdf_bytes"], "sha256": build_receipt["pdf_sha256"]})
reader = PdfReader(ROOT / "manuscript.pdf")
old_reader = PdfReader(old / "manuscript.pdf")
assert len(reader.pages) == len(old_reader.pages) == 33
texts = [page.extract_text() or "" for page in reader.pages]
old_texts = [page.extract_text() or "" for page in old_reader.pages]
changed_text_pages = [i + 1 for i, (a, b) in enumerate(zip(old_texts, texts)) if a != b]
assert changed_text_pages == [28, 33], changed_text_pages
compact = re.sub(r"\s+", "", texts[27])
assert "Bothsourcesusethepointwisediagnostic" in compact
assert "TowerIIdoesnotrecordawhole-fieldGRFinitsglobalmetrics." in compact
bibliography = re.sub(r"\s+", " ", texts[32])
entry11 = bibliography.split("[11]", 1)[1].split("[12]", 1)[0]
assert "25 October" in entry11 and "24 October" not in entry11
entry10 = bibliography.split("[10]", 1)[1].split("[11]", 1)[0]
assert "24 October" in entry10
(ROOT / "qa").mkdir(exist_ok=True)
pdf_text_diff = []
for number in changed_text_pages:
    pdf_text_diff.extend(difflib.unified_diff(
        old_texts[number-1].splitlines(keepends=True), texts[number-1].splitlines(keepends=True),
        fromfile=f"v0.1/PDF_physical_page_{number}", tofile=f"v0.1-R1/PDF_physical_page_{number}"))
(ROOT / "qa/PDF_TEXT_DIFF.txt").write_text("".join(pdf_text_diff), encoding="utf-8")

figure_register = read("baseline/FIGURE_REGISTER.json")
assert len(figure_register["figures"]) == 11
for figure in figure_register["figures"]:
    same(ROOT / figure["file"], figure)
    caption_pages = [i + 1 for i, text in enumerate(texts) if re.search(r"Figure\s*" + str(figure["figure"]) + r"\s*:", text)]
    assert caption_pages == [figure["physical_pdf_page"]], (figure["figure"], caption_pages)
shutil.copyfile(ROOT / "baseline/FIGURE_REGISTER.json", ROOT / "FIGURE_REGISTER.json")

# Compiled labels, bibliography, warning and navigation checks.
for name in ("manuscript.aux", "manuscript.bbl", "manuscript.log", "manuscript.toc"):
    shutil.copyfile(ROOT / "build" / name, ROOT / "qa" / name)
shutil.copyfile(ROOT / "build/typeset_01.txt", ROOT / "qa/FINAL_COMPILER_OUTPUT.txt")
aux = (ROOT / "qa/manuscript.aux").read_text(encoding="utf-8")
old_aux = (ROOT / "baseline/qa/manuscript.aux").read_text(encoding="utf-8")
label_lines = [s for s in aux.splitlines() if s.startswith("\\newlabel")]
assert label_lines == [s for s in old_aux.splitlines() if s.startswith("\\newlabel")]
assert r"\newlabel{eq:grf}{{32}{27}" in aux
assert (ROOT / "qa/manuscript.toc").read_bytes() == (ROOT / "baseline/qa/manuscript.toc").read_bytes()
tex = "\n".join((ROOT / n).read_text(encoding="utf-8") for n in source_names[:3])
labels = set(re.findall(r"\\newlabel\{([^}]+)\}", aux))
refs = set(re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", tex))
assert not refs - labels
cites = {c.strip() for group in re.findall(r"\\cite(?:[a-zA-Z]*)\{([^}]+)\}", tex) for c in group.split(",")}
bibkeys = set(re.findall(r"@\w+\{([^,]+),", new_bib.decode("utf-8")))
assert not cites - bibkeys
assert len(cites) == 12
log = (ROOT / "qa/manuscript.log").read_text(encoding="utf-8", errors="replace")
bad_log = [line for line in log.splitlines() if
           re.search(r"undefined|Missing character|undefined control sequence|Citation .* undefined|Reference .* undefined", line, re.I)]
assert not bad_log, bad_log
warnings = [s for s in log.splitlines() if "Underfull \\hbox" in s or "Overfull \\hbox" in s]
old_warnings = read("baseline/DOCUMENT_QA.json")["spacing_warnings"]
assert warnings == old_warnings, warnings
destinations = reader.named_destinations
old_destinations = old_reader.named_destinations
assert set(destinations) == set(old_destinations)
for key, destination in destinations.items():
    assert reader.get_destination_page_number(destination) == old_reader.get_destination_page_number(old_destinations[key]), key
page_ids = {page.indirect_reference.idnum for page in reader.pages}
checked_links = 0
bad_nav = []
for number, page in enumerate(reader.pages, 1):
    for ref in page.get("/Annots", []):
        annotation = ref.get_object()
        destination = annotation.get("/Dest")
        action = annotation.get("/A")
        if action:
            action = action.get_object()
            if action.get("/S") == "/GoTo":
                destination = action.get("/D")
        if destination is None:
            continue
        checked_links += 1
        if isinstance(destination, str):
            if destination not in destinations:
                bad_nav.append({"page": number, "target": destination})
        elif isinstance(destination, list):
            target_page = destination[0]
            if hasattr(target_page, "idnum") and target_page.idnum not in page_ids:
                bad_nav.append({"page": number, "target": str(target_page)})
        else:
            bad_nav.append({"page": number, "target_type": str(type(destination))})
assert not bad_nav, bad_nav
rotated = [i + 1 for i, page in enumerate(reader.pages) if page.get("/Rotate", 0) % 180]
assert rotated == [5, 11, 22, 24, 26]

manual = read("qa/MANUAL_PAGE_INSPECTION.json")
assert manual["pdf"] == pdf_id
assert len(manual["pages"]) == 33
old_page_qa = {x["physical_page"]: x for x in read("baseline/PAGE_QA.json")["pages"]}
page_records = []
changed_render_pages = []
for entry in manual["pages"]:
    n = entry["physical_page"]
    render_name = f"build/pages/page-{n:02d}.png"
    render_id = identity(ROOT / render_name)
    old_render = old / render_name
    same(old_render, old_page_qa[n])
    if render_id["sha256"] != old_page_qa[n]["sha256"]:
        changed_render_pages.append(n)
    page_records.append({**entry, "printed_page": n - 1 if n > 1 else None,
                         "render": render_name, **render_id, "rotated_landscape": n in rotated})
assert changed_render_pages == [28, 33], changed_render_pages
write("PAGE_QA.json", {"pdf": pdf_id, "renderer": "Poppler pdftoppm, 120 dpi",
      "inspected_pages": 33, "pages": page_records, "status": "PASS",
      "changed_render_pages_vs_v0_1": changed_render_pages,
      "render_retention": "Local build/pages; excluded from review ZIP; hashes retained here",
      "scope": "R1 manual page layout/legibility review, not scientific validation"})

preservation = {
    "status": "PASS", "scope": base["scope"], "prior_candidate": {
        "path": str(old), "verified_members": 206, "all_unchanged": True,
        "zip": base["prior_zip"]},
    "external_inputs_unchanged": base["external_inputs"],
    "baseline_snapshots_unchanged": preserved_copies,
    "copied_evidence_files_unchanged": 158, "copied_handoff_files_unchanged": 11,
    "accepted_archives_unchanged": archive_results, "figures_unchanged": 11,
    "manuscript_source_changes": changed, "exact_diff": identity(ROOT / "R1_EXACT_DIFF.patch"),
    "boundary": "All writes confined to new v0.1-R1; no original, accepted edition, kernel or canonical-ledger writes",
    "cmd_from_first_read": True, "python_environment": "torment",
    "new_simulations": 0, "scientific_checker_reruns": 0, "new_figures": 0,
    "merger_investigation": False, "git_or_publication_actions": False
}
write("PRESERVATION_RECEIPT.json", preservation)

# Only authored root navigation is checked; inherited evidence/baseline links
# retain their original package context and the full accepted archives.
link_count = 0
bad_links = []
for path in ROOT.glob("*.md"):
    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        target = target.strip("<>")
        if target.startswith(("https:", "http:", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        link_count += 1
        # DOCUMENT_QA is the final record emitted immediately after this check.
        if target == "DOCUMENT_QA.json":
            continue
        if not (ROOT / target).exists():
            bad_links.append({"document": path.name, "target": target})
assert not bad_links, bad_links
write("DOCUMENT_QA.json", {
    "status": "PASS", "scope": "E01/E02 editorial, document and byte checks only",
    "pdf": pdf_id, "pages": 33, "figures": 11, "references_used": len(cites),
    "resolved_tex_references": len(refs), "compiled_labels_unchanged": True,
    "table_of_contents_unchanged": True, "named_destination_pages_unchanged": True,
    "pdf_named_destinations": len(destinations), "checked_internal_link_annotations": checked_links,
    "bad_navigation": bad_nav, "undefined_references_citations_or_missing_glyphs": bad_log,
    "rotated_physical_pages": rotated, "authored_markdown_links_checked": link_count,
    "broken_authored_links": bad_links, "spacing_warnings": warnings,
    "new_spacing_warnings": [], "changed_text_pages": changed_text_pages,
    "changed_render_pages": changed_render_pages, "unchanged_render_pages": 31,
    "E01": {"status": "PASS", "physical_page": 28, "printed_page": 27, "equation": 32,
            "scope": "Common pointwise diagnostic; Universe whole-field and Tower per-band aggregates"},
    "E02": {"status": "PASS", "physical_page": 33, "printed_page": 32,
            "bibliography_entry": 11, "date": "25 October 2026"},
    "manual_review": "PAGE_QA.json and qa/MANUAL_PAGE_INSPECTION.json",
    "new_scientific_executions": 0
})

# Record the review files separately from manuscript-source changes.
excluded = {"MANIFEST.json", "REVIEW_ZIP_IDENTITY.json", ZIP_NAME}
def payload_paths():
    return sorted(p for p in ROOT.rglob("*") if p.is_file()
                  and p.relative_to(ROOT).parts[0] != "build"
                  and p.relative_to(ROOT).as_posix() not in excluded
                  and "__pycache__" not in p.parts)
inventory = []
for path in payload_paths():
    name = path.relative_to(ROOT).as_posix()
    if name.startswith("baseline/"):
        category = "unchanged v0.1 snapshot"
    elif name.startswith(("evidence/", "handoff/")):
        category = "unchanged accepted support"
    elif name in changed:
        category = "E01/E02 manuscript correction"
    elif name in old_files and identity(path)["sha256"] == old_files[name]["sha256"]:
        category = "unchanged v0.1 support"
    else:
        category = "new R1 document/build/review artifact"
    inventory.append({"path": name, "category": category})
write("PACKAGE_CHANGE_INVENTORY.json", {
    "manuscript_source_changes_only": changed, "files": inventory,
    "self_manifest_and_zip_note": "This inventory, MANIFEST and external ZIP identity are administrative records.",
    "no_additional_manuscript_corrections": True
})
files = [{"path": p.relative_to(ROOT).as_posix(), **identity(p)} for p in payload_paths()]
write("MANIFEST.json", {
    "edition": "Volume III v0.1-R1, editorial candidate for GPT/Hilmir review",
    "scope": "Every review ZIP member except this self-excluded manifest",
    "files": files, "exclusions": ["build/", "REVIEW_ZIP_IDENTITY.json", ZIP_NAME],
    "scientific_execution": 0
})
files.append({"path": "MANIFEST.json", **identity(ROOT / "MANIFEST.json")})
with zipfile.ZipFile(ROOT / ZIP_NAME, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for entry in files:
        z.write(ROOT / entry["path"], entry["path"])
with zipfile.ZipFile(ROOT / ZIP_NAME) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(set(z.namelist())) == len(files)
    assert set(z.namelist()) == {x["path"] for x in files}
    for entry in files:
        data = z.read(entry["path"])
        assert len(data) == entry["bytes"] and digest(data) == entry["sha256"], entry["path"]
    # The complete accepted archives are also freshly read from the final ZIP.
    for entry in archive_results:
        assert digest(z.read(entry["path"])) == entry["sha256"]
write("REVIEW_ZIP_IDENTITY.json", {
    "review_zip": ZIP_NAME, **identity(ROOT / ZIP_NAME),
    "verified_members": len(files), "all_members_sha256_verified_after_creation": True,
    "crc": "PASS", "fresh_archive_member_readback": True,
    "accepted_archives_verified_in_final_zip": 3,
    "manifest": identity(ROOT / "MANIFEST.json"), "pdf": pdf_id,
    "preservation_receipt": identity(ROOT / "PRESERVATION_RECEIPT.json"),
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "identity_location": "External sidecar, intentionally not inside ZIP",
    "status": "EDITORIAL_R1_READY_FOR_GPT_HILMIR_REVIEW"
})
print(json.dumps({"pdf": pdf_id, "pages": 33, "changed_pages": changed_render_pages,
                  "prior_payload_files_preserved": 206, "evidence_copies_preserved": 158,
                  "review_zip": read("REVIEW_ZIP_IDENTITY.json")}, indent=2))

