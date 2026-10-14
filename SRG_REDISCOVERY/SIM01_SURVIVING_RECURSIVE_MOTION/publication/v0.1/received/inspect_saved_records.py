"""Read saved historical CSVs; never import or run an archived simulation.

All transition calculations restart from recorded input blocks. No new trajectory,
random-number draw, historical file write, or original GUI callback occurs.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import pandas as pd


def h_value(t: float) -> float:
    return (2.0*np.exp(-.5*t)*np.cos(t) + np.exp(-.3*t)*np.sin(t)
            + 1.5*np.exp(-.7*t) + np.exp(-.4*t))


def inspect_log(path: Path) -> dict:
    df = pd.read_csv(path, float_precision='round_trip')
    if len(df) % 8:
        raise ValueError(f'Incomplete eight-body blocks: {path}')
    a = df.to_numpy(dtype=float).reshape(-1,8,len(df.columns))
    ci = {c:i for i,c in enumerate(df.columns)}
    ids = a[:,:,ci['Tetrahedron']]
    if not np.all(ids == np.arange(8)):
        raise ValueError('Rows are not ordered eight-body blocks')
    frames = a[:,0,ci['Step']].astype(int)
    if not np.all(a[:,:,ci['Step']] == frames[:,None]):
        raise ValueError('Frame labels differ within a callback block')
    p = a[:,:,[ci[c] for c in ('X','Y','Z')]]
    v = a[:,:,[ci[c] for c in ('VX','VY','VZ')]]
    b = a[:,:,ci['Rule_State']].astype(int)
    if not np.isin(b,[0,1]).all():
        raise ValueError('Nonbinary rule states')
    g_saved = a[:,:,ci['GRF']]
    e_saved = a[:,:,ci['Energy']]
    vres=[]; pres=[]; gres=[]; eres=[]; norm_steps=[]
    for j in range(1,len(a)):
        prev=p[j-1].copy(); vhat=v[j-1].copy()
        grf=1.0/(1.0+np.mean(np.linalg.norm(v[j-1],axis=1)))
        h=h_value(.1*frames[j])
        for i in range(8):
            centroid=np.mean(prev,axis=0)
            d=np.mod(centroid-prev[i]+5,10)-5
            force=d/(np.linalg.norm(d)+1e-2)*h*(-1 if b[j,i] else 1)
            raw=vhat[i]+.1*force*grf
            vhat[i]=raw/(1+np.log1p(np.abs(raw)))
            prev[i]=np.mod(prev[i]+.1*vhat[i],10)
        vres.append(float(np.max(np.abs(vhat-v[j]))))
        pres.append(float(np.max(np.abs(prev-p[j]))))
        gres.append(float(np.max(np.abs(grf-g_saved[j]))))
        energy=.5*np.sum(np.linalg.norm(v[j],axis=1)**2)
        eres.append(float(np.max(np.abs(energy-e_saved[j]))))
        # Coordinate check uses saved output velocity and observed previous state.
        wrapped=np.mod(p[j]-p[j-1]+5,10)-5
        norm_steps.append(float(np.max(np.abs(wrapped-.1*v[j]))))
    return dict(path=path.name,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        rows=len(df),blocks=len(a),saved_input_re_evaluations=len(a)-1,
        unique_frame_labels=len(np.unique(frames)),
        frame_labels=[int(frames.min()),int(frames.max())],
        repeated_step_body_keys=int(df.duplicated(['Step','Tetrahedron']).sum()),
        same_frame_successions=int(np.sum(np.diff(frames)==0)),
        descending_frame_successions=int(np.sum(np.diff(frames)<0)),
        observed_binary_rule_flips=int(np.sum(b[1:]!=b[:-1])),
        max_velocity_residual=max(vres),max_position_prediction_residual=max(pres),
        max_saved_velocity_position_residual=max(norm_steps),
        max_grf_residual=max(gres),max_energy_residual=max(eres),
        all_saved_input_velocity_residuals_below_1e_12=bool(max(vres)<1e-12),
        interpretation='Source consistency conditional on saved binary outcomes; original RNG and callback launch history not reconstructed.')


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--archive-root',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    root=args.archive_root.resolve()
    paths=['Simulations/CSV/PLOT_1_tetrahedral_states_20250712_015421.csv',
           'Simulations/CSV/tetrahedral_states_20250712_015647.csv']
    logs=[inspect_log(root/p) for p in paths]
    raw=pd.read_csv(root/'Simulations/CSV/tetrahedral_states_curvature_20250712_062601.csv',float_precision='round_trip')
    glyph=pd.read_csv(root/'Simulations/CSV/symbolic_glyphs_resonance_pass.csv',float_precision='round_trip')
    emb=pd.read_csv(root/'Simulations/CSV/ProtoSRG_1_Recursive_Embedding.csv',float_precision='round_trip')
    joined=glyph.merge(raw,on=['Step','Tetrahedron'],suffixes=('_glyph','_raw'),how='left',validate='many_to_one')
    matched = joined[['X_raw','Y_raw','Z_raw']].notna().all(axis=1)
    if not matched.all():
        raise ValueError('Not every glyph row matched a saved curvature record')
    jres={c:float(np.max(np.abs(joined[c+'_glyph']-joined[c+'_raw']))) for c in ['X','Y','Z']}
    notes=dict(glyph_rows=len(glyph),glyph_body_ids=sorted(map(int,glyph.Tetrahedron.unique())),
        glyph_symbolic_ids=sorted(glyph.Symbolic_ID.unique().tolist()),
        glyph_steps=[int(glyph.Step.min()),int(glyph.Step.max())],
        matched_curvature_rows=int(matched.sum()),coordinate_join_residuals=jres,
        embedding_rows=len(emb),embedding_xyz_residual=float(np.max(np.abs(emb[['X','Y','Z']].to_numpy()-glyph[['X','Y','Z']].to_numpy()))),
        curvature_rows=len(raw),curvature_adjusted_dt_range=[float(raw.Adjusted_DT.min()),float(raw.Adjusted_DT.max())],
        curvature_generator_status='Not located in this ZIP; separate data family, not assigned to plot_1.py.')
    out=dict(method='Passive analysis of uploaded records; no historical source imported or executed; no new dynamics rollout.',
             numpy=np.__version__,pandas=pd.__version__,logs=logs,trail_lineage=notes)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,allow_nan=False))

if __name__=='__main__':
    main()
