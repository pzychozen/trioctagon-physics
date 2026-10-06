"""Capture immutable inputs and the existing repository state. Run once per edition."""
from pathlib import Path
import hashlib, json, shutil, subprocess

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
EXT = Path('C:/Users/Notandi/.codex/visualizations/2026/10/05/01a10bcb-e66a-7063-b16a-f4486a5c6150')
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
manifest = []
def capture(code, src, dest):
    src, dst = Path(src), ROOT / dest
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    assert digest(src) == digest(dst)
    manifest.append(dict(id=code, original=str(src), snapshot=str(dst.relative_to(ROOT)), sha256=digest(src), bytes=src.stat().st_size))

baseline = ROOT/'records/baseline.json'
if baseline.exists():
    raise SystemExit('Baseline already exists; do not replace it.')
protected = {}
for folder in ['kernel_physics', 'apps/scientific_ui', '.github', 'research_files/sources']:
    for p in (REPO/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts:
            protected[str(p.relative_to(REPO))] = digest(p)
baseline.write_text(json.dumps(dict(head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip(), status=subprocess.check_output(['git','status','--porcelain=v1'],cwd=REPO,text=True), protected=protected),indent=2),encoding='utf-8')
capture('WO', 'C:/Users/Notandi/.codex/attachments/8d298bff-f983-40f0-9855-100b11f7b463/Pasted text.txt', 'provenance/work_order.txt')
reports = [
('R1','three_way_large_L_scaling_v0.1','THREE_WAY_LARGE_L_SCALING_ANALYSIS_v0.1.md'),
('R2','three_way_known_structure_review_v0.1','THREE_WAY_KNOWN_STRUCTURE_AND_PHYSICAL_ANALOGUE_REVIEW_v0.1.md'),
('R3','three_way_two_parameter_normal_form_v0.1','THREE_WAY_TWO_PARAMETER_NORMAL_FORM_v0.1.md'),
('R4','three_way_x_cover_moduli_v0.1','THREE_WAY_X_COVER_MODULI_v0.1.md'),
('R5','three_way_genus_one_galois_closure_v0.1','THREE_WAY_GENUS_ONE_GALOIS_CLOSURE_v0.1.md')]
for code, folder, name in reports:
    capture(code, EXT/folder/name, f'provenance/reconstruction/{code}/{name}')
    for p in (EXT/folder).iterdir():
        if p.suffix in ['.py','.json','.csv']:
            capture(code+'-support', p, f'provenance/reconstruction/{code}/{p.name}')
hist = [
('H1', REPO/'research_files/sources/TRIOCTAGON_new/pdfs_old/three_way_final_draft.pdf'),
('H2', REPO/'research_files/sources/Zenodo_research/17365334/Bounded_Infinity.pdf'),
('H3', Path('C:/Users/Notandi/Downloads/Three_way_test_model.pdf')),
('H4', REPO/'research_files/sources/Claude_research/portal_geometry/Reciprocal_Rational_Maps__Self_Dual_Hinges__and_Toroidal_Phase_Lifts.pdf')]
for code, p in hist:
    capture(code,p,f'provenance/historical/{code}/{p.name}')
for name in ['rrm_tool.py','rrm_asymptotes.csv','rrm_stats.csv','rrm_arclengths.csv','rtm_key_pairs.csv','rtm_curvature_landscape.csv','PHASE8_README.md']:
    capture('H2-code', REPO/'research_files/sources/Zenodo_research/17365334'/name, f'provenance/historical/H2/{name}')
for name in ['THREE_WAY_ITEM2A_CONSTANT_GEOMETRY.md','THREE_WAY_ITEM2B_CONSTANT_SURVEY.md','THREE_WAY_ITEM2C_M2_FIBONACCI_STRUCTURE.md']:
    capture('M1',Path('C:/TORMENT/playground')/name,f'provenance/modern_prior/{name}')
(ROOT/'provenance/source_manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')
print(f'Captured {len(manifest)} source files; hashed {len(protected)} protected files.')
