"""Copy focused accepted evidence and reading sources; never execute their code."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
RESEARCH = ROOT.parent
PUB = RESEARCH / 'NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree'
PRED = PUB / 'papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1'
DOWNLOADS = Path('C:/Users/Notandi/Downloads')
sources = []

def keep(source_id, original, target, version, locator, expected=None):
    original = Path(original)
    data = original.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    if expected is not None:
        assert sha == expected, f'Reviewed-source discrepancy: {original}: {sha}'
    dest = ROOT / target
    dest.parent.mkdir(parents=True, exist_ok=True)
    assert not dest.exists(), dest
    dest.write_bytes(data)
    sources.append({'id': source_id, 'original_path': original.as_posix(), 'package_path': target,
                    'version': version, 'locator': locator, 'bytes': len(data), 'sha256': sha,
                    'reviewed_hash_match': True if expected is not None else None})

keep('ORDER', DOWNLOADS / 'NATIVE_PHASE_SPATIAL_PAPER_01_CODEX_WORK_ORDER.md', 'provenance/work_order.md', '2 November 2026 manuscript order', 'Sections 1-7; acceptance and four editorial/table corrections.')
expected = {'phase':'0ce3d59e249ee7794c3386047e2bf79f9d7a83b76ec563c8541de4b66c35f2c6',
            'spatial':'9b89dfdd94be93ea50bb0e4b9f8029383801a0bae6965e8c662eb4e4d07f2ddd'}
review_status = {}
for kind, task in [('phase','NATIVE_PHASE_RECONSTRUCTION_01'), ('spatial','NATIVE_SPATIAL_CORRESPONDENCE_01')]:
    folder = RESEARCH / task
    files = [task+'_PROOF_REVIEW.md', 'exact_algebra.py', 'exact_algebra_results.json', 'SOURCE_IDENTITIES.json']
    if kind == 'spatial':
        files.append('CLAIM_SOURCE_LEDGER.md')
    for name in files:
        keep(kind.upper()+'-'+name, folder/name, f'evidence/{kind}/{name}',
             'Accepted project research evidence, 2 November 2026',
             'Proof and retained exact-algebra/source record; helper preserved, not executed.',
             expected[kind] if name.endswith('_PROOF_REVIEW.md') else None)
    review_name = task+'_GPT_REVIEW.md'
    found = next((p for p in [folder/review_name, DOWNLOADS/review_name] if p.is_file()), None)
    review_status[kind] = found.as_posix() if found else 'No separate local copy used; acceptance and operative corrections supplied by ORDER.'
    if found:
        keep(kind.upper()+'-REVIEW', found, f'evidence/{kind}/{review_name}', 'Available project acceptance review', 'Accepted disposition.')

primary = [
 ('P-main', PRED/'manuscript/main.tex','potential_main.tex','Published predecessor v0.1, 2 November 2026','Title, authorship and research-edition status; established paper style.'),
 ('P-setting', PRED/'manuscript/setting.tex','potential_setting.tex','Published predecessor v0.1','Section 2; eq:pre, eq:full, eq:potential and regular equivariance.'),
 ('P-coordinates', PRED/'manuscript/coordinates.tex','potential_coordinates.tex','Published predecessor v0.1','Section 5; thm:reconstruction, prop:image, thm:autonomy.'),
 ('P-retention', PRED/'manuscript/retention.tex','potential_retention.tex','Published predecessor v0.1','Section 6; energy retention, matched edges and retained descent.'),
 ('P-finite', PRED/'manuscript/finite.tex','potential_finite.tex','Published predecessor v0.1','Section 4; eq:prebounds, thm:finite, monotonicity equality.'),
 ('P-references', PRED/'manuscript/references.tex','potential_references.tex','Published predecessor v0.1','Verified primary titles, edition dates and immutable reference links.'),
 ('RELAX', PRED/'provenance/primary_sources/papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex','relaxation_main.tex','Accepted primary snapshot, research edition v0.1, 28 October 2026','Sections 6-7; lem:phase, thm:convergence, eq:nesting and eq:phasebound.'),
 ('NRG-main', PUB/'papers/NATIVE_RESPONSE_GEOMETRY/manuscript/main.tex','nrg_main.tex','Research publication v0.1, 6 October 2026','Verified title, edition date and attribution.'),
 ('NRG-observables', PUB/'papers/NATIVE_RESPONSE_GEOMETRY/manuscript/observables_closure.tex','nrg_observables_closure.tex','NRG retained publication-worktree reading copy','eq:decoder, eq:faceupdate, eq:chiral and interpretation limits.'),
 ('NRG-frames', PUB/'papers/NATIVE_RESPONSE_GEOMETRY/manuscript/appendices.tex','nrg_appendices.tex','NRG retained publication-worktree reading copy','app:notation, exact frame table.'),
 ('Z-methods', PUB/'docs/methods/Z_MOTION/v0.1/manuscript/NOTE.md','z_methods.md','Explanatory methods draft v0.1, 1 November 2026','Sections 2, 3 and 8: coefficients, staged/EMA definitions and limits.'),
 ('Z-code', PUB/'kernel_physics/z_manifold.py','z_manifold.py','Retained implementation reading copy; no execution','advance_ema, ema_scalar, observe_ema, _harmonic and _observe.'),
 ('GAP', RESEARCH/'NATURAL_CORE_MOTION_Z_FIXED_REFERENCE_01/packet/REFERENCES/NCM_FIXED_GAP_01_REPORT.md','fixed_gap_report.md','NCM-FIXED-GAP-01 v0.1, 31 October 2026','Sections 1 and 3; origin, reference support directions, stationary/attachment distinction.'),
 ('GAP-review', RESEARCH/'NATURAL_CORE_MOTION_Z_FIXED_REFERENCE_01/packet/REFERENCES/NCM_FIXED_GAP_01_GPT_REVIEW.md','fixed_gap_review.md','Accepted GPT review, 31 October 2026','Accepted geometry scope and material-attachment boundary.'),
]
for key, path, target, version, locator in primary:
    keep(key, path, 'provenance/primary/'+target, version, locator,
         'bc43cadd16d4235cda17fc42f082e5fa6fe579158ac3ed9ad779687fb4ec9da8' if key == 'GAP' else None)
record = {'recorded_utc':datetime.now(timezone.utc).isoformat(),
          'publication_reading_reference':'634ff13b666604d5caed11cc3731dcb5a863ff6c',
          'checkout_not_queried_or_changed':True, 'separate_acceptance_reviews':review_status,
          'sources':sources, 'scope':'Focused byte-preserved copies. No helper, module, certificate, native map or observer executed.'}
(ROOT/'provenance/source_manifest.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','sources_copied':len(sources),'both_reviewed_proof_hashes_match':True,'separate_reviews':review_status},indent=2))
