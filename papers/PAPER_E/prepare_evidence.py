"""Initial local evidence capture only. Copies preserved inputs without alteration."""
from pathlib import Path
import shutil,json
from package_tools import P,WORK,sha,write
K=WORK/'kernel_TO'; E=P/'evidence'; E.mkdir(exist_ok=True)
names=['model_core','geometry_3d','geometry_embeddings','z_spike_diagnostic','definitions','diagnostics',
       'toy_3d_triocta','analysis_tools','chirality_lab','constants_selector','su3_basis','phase_triad_sync',
       'latent_foreclosure','identity_rules','provenance']
pairs=[(K/(n+'.py'),E/'source_snapshots/staged'/(n+'.py')) for n in names]
pairs.append((WORK/'reconstruction/recursive_state_archaeology/codex_verification_I/source_snapshots/model_core.py',E/'source_snapshots/committed_ema/model_core.py'))
for kind in ['subcritical','critical']:
    for pattern in ['*_series.csv','*_summary.txt']:
        src=next((K/('vrec_ts_'+kind)).glob(pattern));pairs.append((src,E/'preserved_runs'/src.name))
accepted=WORK/'research/GPT_proof/historical_z_manifold_v0.1'
for name in ['verification_results.json','preservation_receipt.json','verify_historical_z.py']:
    pairs.append((accepted/name,E/'accepted_reconstruction'/name))
pairs.append((WORK/'research/GPT_proof/HISTORICAL_Z_MANIFOLD_AND_SIX_GAP_RECONSTRUCTION_v0.1.md',E/'accepted_reconstruction/HISTORICAL_Z_RECONSTRUCTION_v0.1.md'))
records=[]
for src,dst in pairs:
    dst.parent.mkdir(parents=True,exist_ok=True)
    if dst.exists() and sha(dst)!=sha(src):raise RuntimeError('Refusing changed evidence replacement: '+str(dst))
    shutil.copyfile(src,dst);records.append({'source':str(src),'copy':dst.relative_to(P).as_posix(),'sha256':sha(src),'byte_identical':sha(src)==sha(dst)})
write(E/'source_provenance.json',{'attribution':'Codex preservation copy, no source correction','copies':records,
      'accepted_figures_reused_as_prior_visual_evidence':[{'path':str(x),'sha256':sha(x)} for x in sorted((accepted/'figures').glob('*.png'))],
      'review':'Paper E scientific review pending GPT; preceding reconstruction accepted as input by the work order'})
print('Preserved',len(records),'small source/evidence files; no environments or archives copied')
