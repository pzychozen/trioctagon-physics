"""Package an already audited, visually reviewed edition; no source edits."""
from pathlib import Path
import json,hashlib,zipfile
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
audit=json.loads((ROOT/'records/delivery_audit.json').read_text())
visual=json.loads((ROOT/'records/visual_review.json').read_text())
pdf=ROOT/'output/pdf/three_way_reciprocal_hierarchy_v0.1.pdf'
assert visual['status']=='passed' and visual['pdf_sha256']==audit['pdf_sha256']==sha(pdf)
assert len(visual['pages_reviewed'])==audit['pages']
build=json.loads((ROOT/'records/build_record.json').read_text())
paper1=ROOT.parent/'three_way_reconstruction/output/pdf/three_way_reconstruction_v0.1.pdf'
report=f'''PAPER II BUILD AND VERIFICATION REPORT / 5 October 2026

Result: COMPLETE. THREE-WAY RECIPROCAL HIERARCHY = PARKED.
Final bridge status: FINITE S3 BRIDGE ONLY.
The exact finite action/incidence match is retained. No independently justified continuous identification with t, h or a critical-value cross-ratio follows from inspected definitions. This is a bounded source-limited finding, not a universal impossibility theorem.

PAPER
{audit['pages']} pages, {audit['figures']} figures in PDF/SVG/PNG, {audit['bibliography_entries']} bibliography entries.
PDF SHA-256: {sha(pdf)}
Editable LaTeX source: source/main.tex plus seven section/appendix files and references.tex.
Bibliography metadata: bibliography.bib.
Claim/evidence records: {audit['claim_records']}; every labeled theorem/proposition is mapped.
Bridge-source records: 8 with original absolute paths, exact locators and hashes.

MATHEMATICAL VALIDATION
Hierarchy suite: 51 exact checks passed; 4 numerical checks passed.
Cubic suite: 73 exact checks passed; 3 complex probes at t=17 passed at 100 digits.
Additional bridge source-formula checks: 10 exact checks passed.
Total exact checks: {audit['exact_checks']}.
Original hierarchy/cubic verifier copies are byte-identical to their external source scripts.
The all-degree existence/monodromy/genus proof is a prose mathematical proof, not numerical extrapolation or machine-formalized topology.
Numerical values are floating high-precision checks, not interval-certified bounds.

BUILD AND LAYOUT
Tectonic: {build['tectonic_version']}; cached-only build; no TeX installation or network dependency fetch.
Dedicated external build/cache workspace: {build['workspace']}
No overfull or underfull boxes, missing glyphs, undefined references or citations in final LaTeX log.
{audit['internal_pdf_links']} internal PDF links checked; all named destination pages resolve.
{audit['source_labels']} source labels and {audit['source_references']} explicit source references checked.
All source/figure input hashes match the final PDF build record.
All {audit['pages']} pages rendered at 110 dpi and visually inspected in two-page sheets; all five figure originals also inspected. Title, single-page contents, equations, tables, captions, appendix, references and page numbers reviewed. No clipping or overlap found in final edition.
Three primary literature URLs opened successfully during the work; project evidence is preserved locally.

PRESERVATION
{audit['protected_files_checked']} protected file identities unchanged, including all tracked repository files, Paper I, kernel/UI files in protected directories, and both external analytical-report directories.
Paper I PDF SHA-256 remains: {sha(paper1)}
Repository HEAD unchanged; status unchanged from baseline taken after creating the authorized Paper II lane.
No kernel imports for the bridge audit. No kernel/UI or historical source edits. No commits, remote publication, new model, fitting or physics interpretation.
All new project files reside in this Paper II directory; build/cache/render intermediates reside in the dedicated external publication workspace.

SCOPE
No degree-five study, exhaustive quartic census, further coupling or physical implementation was started.
Manuscript attribution/publication metadata is a draft prepared for author review; no priority claim.
'''
(ROOT/'records/BUILD_VERIFICATION_REPORT.txt').write_text(report,encoding='utf-8')
excluded={'artifact_manifest.json','package_record.json'}
files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and p.suffix!='.zip' and p.name not in excluded and '__pycache__' not in p.parts]
manifest={str(p.relative_to(ROOT)).replace('\\','/'):dict(bytes=p.stat().st_size,sha256=sha(p)) for p in files}
manifestfile=ROOT/'records/artifact_manifest.json';manifestfile.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
bundle=ROOT/'output/three_way_reciprocal_hierarchy_v0.1_bundle.zip'
with zipfile.ZipFile(bundle,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files+[manifestfile]:z.write(p,str(p.relative_to(ROOT)).replace('\\','/'))
with zipfile.ZipFile(bundle) as z:
    assert z.testzip() is None
    for rel,item in manifest.items():assert hashlib.sha256(z.read(rel)).hexdigest()==item['sha256'],rel
record=dict(bundle=str(bundle),sha256=sha(bundle),bytes=bundle.stat().st_size,entries=len(files)+1,archive_crc_check='passed',all_manifest_hashes_match_archive=True,pdf_sha256=sha(pdf),status='THREE-WAY RECIPROCAL HIERARCHY = PARKED',bridge='FINITE S3 BRIDGE ONLY')
(ROOT/'records/package_record.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(record,indent=2))
