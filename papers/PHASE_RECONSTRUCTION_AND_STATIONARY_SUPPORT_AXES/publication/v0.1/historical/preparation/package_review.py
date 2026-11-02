"""Record completed visual review and package the final document; no scientific execution."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import zipfile

ROOT = Path(__file__).resolve().parent
sha = lambda data:hashlib.sha256(data).hexdigest()
pdf = ROOT/'NATIVE_PHASE_SPATIAL_v0.1_REVIEW.pdf'
checks = json.loads((ROOT/'inspection/DOCUMENT_CHECKS.json').read_text(encoding='utf-8'))
external = json.loads((ROOT/'inspection/EXTERNAL_LINK_CHECKS.json').read_text(encoding='utf-8'))
build = json.loads((ROOT/'build/build_receipt.json').read_text(encoding='utf-8'))
sources = json.loads((ROOT/'provenance/source_manifest.json').read_text(encoding='utf-8'))
assert checks['status']=='PASS' and all(checks['checks'].values())
assert external['all_accessible']
assert sha(pdf.read_bytes())==checks['pdf_sha256']==build['pdf_sha256']
assert all(sha((ROOT/path).read_bytes())==value for path,value in build['source_sha256'].items())

# These notes describe pages already displayed and inspected by Codex, not an automatic visual classifier.
notes = [
 'Cover title, accented author, draft status, abstract and attribution clear; no clipping.',
 'Introduction, native map, fixed tuple and inherited bounds legible; page transition preserves the list.',
 'Notation table, positive-root representative, exact joint-span image and coherence update legible.',
 'Reconstruction theorem, inverse, multiplier and real-lift theorem statements fit; equation boxes clear.',
 'Canonical half-plane proof, aligned relaxation and overlap theorem statements clear.',
 'Overlap proof, correction sum and section-change product signs legible; no clipped formulas.',
 'Normalized changed-section unit factor, pointwise/finite-sum clarification, frame table and positioned-axis statement inspected again after final wording refinement.',
 'Positioned-axis proof, decoder inverse/projector, phase-action theorem and matched face update clear.',
 'Commuting update, full vector history, prominent complete-step box and universal theorem/Gram witness clear.',
 'Full-rank orientation witness, observation formulas and EMA innovation inspected again after wording adjustment; literal 0.01 stays with its sentence.',
 'Current-memory observation explanation, distinct EMA table rows and energy formula inspected again; table readable and fully within margins.',
 'Energy scope, interpretation boundary, attribution and analytic appendix opening legible; page break retains the argument.',
 'Analytic derivative sign and all eight references inspected; hyperlinks, long task names and final page numbering fit.',
]
assert len(notes)==checks['page_count']==13
first = json.loads((ROOT/'build/first_visual_render_hashes.json').read_text(encoding='utf-8-sig'))
initial = {Path(item['Path']).name:item['Hash'].lower() for item in first}
pages = []
changed = []
for i,note in enumerate(notes,1):
    path = ROOT/f'renders/page-{i:02d}.png'
    digest = sha(path.read_bytes())
    if digest!=initial[path.name]:
        changed.append(i)
    pages.append({'page':i,'render':path.relative_to(ROOT).as_posix(),'sha256':digest,
                  'visually_inspected':True,'status':'PASS','notes':note})
assert changed==[7,10,11]
visual = {'status':'PASS','recorded_utc':datetime.now(timezone.utc).isoformat(),
          'pdf_sha256':checks['pdf_sha256'],'page_count':13,'complete_final_page_pass':True,
          'method':'All pages rendered by Poppler at 120 dpi and directly displayed through view_image. Pages 7, 10 and 11 were re-inspected after final wording changes; the other final page images match the initially inspected images byte-for-byte.',
          'renderer':'pdftoppm 26.07.0','pages':pages,
          'render_location':'Workspace renders/; PNGs intentionally not duplicated in the review ZIP.'}
(ROOT/'inspection/VISUAL_INSPECTION.json').write_text(json.dumps(visual,indent=2)+'\n',encoding='utf-8')
for name in ['build_receipt.json','compiler_final.txt','main.log']:
    shutil.copyfile(ROOT/'build'/name,ROOT/'inspection'/name)

ledger_path = ROOT/'CLAIM_SOURCE_LEDGER.md'
ledger = ledger_path.read_text(encoding='utf-8')
assert ledger.count('<!-- SOURCE_IDENTITIES -->')==1
blocks = []
for item in sources['sources']:
    original = item['original_path']
    blocks.append(f"**{item['id']}**  \nOriginal: [{original}](<{original}>)  \n"
                  f"Packaged: `{item['package_path']}`  \nVersion/copy: {item['version']}  \n"
                  f"Locator: {item['locator']}  \nSHA-256: `{item['sha256']}`; {item['bytes']} bytes.")
ledger_path.write_text(ledger.replace('<!-- SOURCE_IDENTITIES -->','\n\n'.join(blocks)),encoding='utf-8')
prep_path = ROOT/'PREPARATION_REPORT.md'
prep = prep_path.read_text(encoding='utf-8')
assert prep.count('<!-- FINAL_DOCUMENT -->')==1
summary = (f"Final PDF: **{checks['page_count']} pages**, A4, **{checks['pdf_bytes']} bytes**.  \n"
           f"File: `NATIVE_PHASE_SPATIAL_v0.1_REVIEW.pdf`  \nSHA-256: `{checks['pdf_sha256']}`.\n\n"
           'Build, document checks, all-page visual inspection and source preservation: **PASS**. '
           'The portable ZIP carries this same inspected PDF; no concrete unresolved preparation issue remains.')
prep_path.write_text(prep.replace('<!-- FINAL_DOCUMENT -->',summary),encoding='utf-8')

members = [pdf.name,'README.md','CLAIM_SOURCE_LEDGER.md','PREPARATION_REPORT.md','prepare_sources.py','package_review.py']
for folder in ['manuscript','evidence','provenance','inspection']:
    members.extend(p.relative_to(ROOT).as_posix() for p in sorted((ROOT/folder).rglob('*')) if p.is_file())
assert len(members)==len(set(members))
files = []
for name in members:
    path = PurePosixPath(name)
    assert not path.is_absolute() and '..' not in path.parts and ':' not in name
    data = (ROOT/name).read_bytes()
    if name in ['CLAIM_SOURCE_LEDGER.md','PREPARATION_REPORT.md']:
        assert '<!-- ' not in data.decode('utf-8')
    files.append({'path':name,'bytes':len(data),'sha256':sha(data)})
manifest = {'task':'NATIVE_PHASE_SPATIAL_PAPER_01','status':'Review draft v0.1 - awaiting GPT/author manuscript review',
            'files':files,'manifest_self_hash':'Excluded by design; final archive checksum outside ZIP covers this manifest.',
            'omitted':'Workspace build caches/intermediates and rendered inspection PNGs; final inspection receipts are included.'}
manifest_name = 'PACKAGE_MANIFEST.json'
(ROOT/manifest_name).write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
archive = ROOT/'NATIVE_PHASE_SPATIAL_PAPER_01_REVIEW_PACKAGE.zip'
with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED) as bundle:
    for name in members+[manifest_name]:
        bundle.write(ROOT/name,arcname=name)

# One final archive integrity pass. Nothing from the archive is executed or extracted.
with zipfile.ZipFile(archive) as bundle:
    names = bundle.namelist()
    assert len(names)==len(set(names))
    assert set(names)==set(members)|{manifest_name}
    assert bundle.testzip() is None
    saved = json.loads(bundle.read(manifest_name))
    for item in saved['files']:
        data = bundle.read(item['path'])
        assert len(data)==item['bytes'] and sha(data)==item['sha256'],item['path']
    assert sha(bundle.read(pdf.name))==visual['pdf_sha256']==checks['pdf_sha256']
digest = sha(archive.read_bytes())
checksum = archive.with_name(archive.name+'.sha256')
checksum.write_text(f'{digest}  {archive.name}\n',encoding='ascii')
receipt = {'status':'PASS','archive':archive.name,'archive_bytes':archive.stat().st_size,
           'archive_sha256':digest,'zip_members':len(names),'hashed_payload_files':len(files),
           'crc':'PASS','all_member_sizes_and_hashes':'PASS','required_pdf_and_inspection_identity':'PASS',
           'pdf_sha256':checks['pdf_sha256'],'page_count':13,
           'scope':'Final review-package byte check only; no scientific execution.'}
(ROOT/'PACKAGE_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
