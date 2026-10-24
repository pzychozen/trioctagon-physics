"""Document input identities/copy only. No numerical modules or study scripts imported."""
from pathlib import Path
import hashlib,json,zipfile,shutil
ROOT=Path(__file__).resolve().parent
RESEARCH=ROOT.parents[3]
S4=RESEARCH/'SRG_SIMULATION_STUDY_04_SEED_EXPLORER'
S5=RESEARCH/'SRG_SIMULATION_STUDY_05_INFINITY'
def digest(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def dump(name,o):(ROOT/name).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
rows=[]
def copy(p,rel):
    b=p.read_bytes();q=ROOT/rel;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(b)
    rows.append(dict(original_path=str(p),candidate_path=rel,**digest(b)))
    return b
def main():
    assert not (ROOT/'INPUT_BASELINE.json').exists()
    copy(Path('C:/Users/Notandi/Downloads/SRG_VOLUME_II_SIM04_SIM05_CODEX_MANUSCRIPT_WORK_ORDER.md'),'evidence/AUTHORITATIVE_WORK_ORDER.md')
    for sid,base,zname in [(4,S4,'SRG_SIMULATION_STUDY_04_SEED_EXPLORER_REVIEW.zip'),(5,S5,'SRG_SIMULATION_STUDY_05_INFINITY_REVIEW.zip')]:
        b=copy(base/zname,'evidence/inputs/'+zname)
        with zipfile.ZipFile(base/zname) as z:
            assert z.testzip() is None
            manifest=json.loads(z.read('MANIFEST.json'))
            fs=manifest['files'] if isinstance(manifest,dict) else manifest
            if isinstance(fs,dict):fs=[dict(path=k,**v) for k,v in fs.items()]
            for f in fs:
                name=f.get('path',f.get('relative_path'));bb=z.read(name)
                assert hashlib.sha256(bb).hexdigest()==f['sha256'],name
            # Compare the local scientific originals and documents used below to the sealed input.
            for name in z.namelist():
                if name.startswith('originals/') or (name.endswith('.md') and '/' not in name):
                    assert (base/name).read_bytes()==z.read(name),name
        for p in (base/'originals').glob('*'):
            if p.is_file():copy(p,'evidence/originals/SIM%02d/'%sid+p.name)
        for name in ['START_HERE.md','CONSTRUCTION.md','VERIFICATION_AND_LIMITS.md','FIGURE_REGISTER.json']:
            copy(base/name,'evidence/studies/SIM%02d/'%sid+name)
    for name in ['ORIGINAL_EVIDENCE.md']:copy(S4/name,'evidence/studies/SIM04/'+name)
    for name in ['HISTORICAL_EVIDENCE_AND_CLAIMS.md','REPLAY_AND_3D_ANALYSIS.md','SIM04_3D_ADDENDUM.md','MODEL_FAMILIES_AND_PAPER_PLAN.md']:
        copy(S5/name,'evidence/studies/SIM05/'+name)
    r4=S5/'context/SIM04_GPT_REVIEW'
    for name in ['SIM04_GPT_SCIENTIFIC_REVIEW.md','source_review.md','independent_data/independent_checks.json','independent_data/fixed_final_partition_variance.json','additional_figure/figure_data.json']:
        copy(r4/name,'evidence/reviews/SIM04/'+name)
    # Original figure bytes, deliberately no plotting or calculations.
    figures=[]
    selections=[(S4/'figures','F01_recorded_overview.png','S4_overview.png'),(S4/'figures','F02_position_views.png','S4_positions.png'),(S4/'figures','F03_identifiable_episodes.png','S4_episodes.png'),(S4/'figures','F04_terms_and_neighbors.png','S4_terms.png'),(r4/'additional_figure','SIM04_six_point_component.png','S4_six_review.png')]
    selections += [(S5/'figures',n+'.png',n+'.png') for n in ['F01_SIM05_whole_field','F02_SIM05_selected_groups','F03_SIM05_stages','F04_SIM05_second_field','F05_SIM05_geometry_and_motion','F06_SIM04_context','F07_SIM04_scale_and_shape']]
    for parent,name,target in selections:
        b=copy(parent/name,'figures/'+target);figures.append(dict(path='figures/'+target,original=str(parent/name),unchanged=True,**digest(b)))
    dump('FIGURE_INPUT_IDENTITIES.json',figures)
    for name in ['historical_checks.json','analysis_checks.json','detail_checks.json','SIM04_geometry_checks.json','component_geometry.csv','stage_windows.csv','clipping_events.csv','historical_replay_columns.csv','SIM04_six_geometry.csv','SIM04_pair_shape_changes.csv']:
        copy(S5/'analysis'/name,'evidence/tables/SIM05/'+name)
    for name in ['ENVIRONMENT.json','REFERENCE_EQUIVALENCE.json','RUN_BUDGET.json','CORE_IDENTITY.json']:
        copy(S5/name,'evidence/studies/SIM05/'+name)
    # Retained administrative context is baseline-only, not scientific main-text material.
    for p in [RESEARCH/'SIMULATION_RECONSTRUCTION_RESEARCH/SIMULATION_STUDY_LEDGER.md',RESEARCH/'PUBLICATION_WORK/V1_PUBLISH/PUBLICATION_RECEIPT.md']:
        rows.append(dict(original_path=str(p),candidate_path=None,**digest(p.read_bytes())))
    dump('INPUT_BASELINE.json',rows)
    dump('INPUT_GATE.json',dict(local_study_archives_valid=True,local_originals_documents_match=True,SIM05_new_GPT_review='PENDING LOCATION',new_simulation_calls=0,numerical_checker_reruns=0))
    print(json.dumps(dict(protected_inputs=len(rows),copied_figures=len(figures),new_science_calls=0,pending='Accepted SIM05 review archive named in work order')))
if __name__=='__main__':main()
