"""Document-only extraction/rounding/copying. No scientific module or formula evaluation."""
from pathlib import Path
import json,hashlib,shutil
from decimal import Decimal,localcontext
R=Path(__file__).resolve().parent;T=R/'manuscript/tables';T.mkdir(parents=True,exist_ok=True)
cache={};cells=[]
def load(f):
 if f not in cache:cache[f]=json.loads((R/f).read_text(encoding='utf-8'),parse_float=Decimal)
 return cache[f]
def get(f,p):
 x=load(f)
 for k in p.strip('/').split('/'):
  k=k.replace('~1','/').replace('~0','~');x=x[int(k)] if isinstance(x,list) else x[k]
 return x
def value(table,row,col,f,p,digits=9,signed=False):
 x=get(f,p)
 if isinstance(x,list):text=', '.join(map(str,x));original=x;rule='exact categorical list'
 elif isinstance(x,str) and not x.replace('.','',1).replace('-','',1).replace('+','',1).replace('e','',1).isdigit():text=x;original=x;rule='exact category'
 else:
  original=str(x)
  with localcontext() as c:
   c.prec=140;text=format(Decimal(str(x)),('+' if signed else '')+f'.{digits}f')
  rule=f'Decimal ROUND_HALF_EVEN, {digits} places; '+('explicit sign' if signed else 'ordinary sign')
 cells.append({'table':table,'row':row,'column':col,'source_file':f,'json_pointer':p,'original_token':original,'display':text,'rule':rule})
 return text
def table(name,head,rows):
 (T/(name+'.md')).write_text('| '+' | '.join(head)+' |\n| '+' | '.join(['---']*len(head))+' |\n'+'\n'.join('| '+' | '.join(map(str,r))+' |' for r in rows)+'\n',encoding='utf-8')
o1='evidence/Z01/OBSERVATIONS.json';g1='evidence/Z01/GAP_COMPARISON.json';o2='evidence/Z02/OBSERVATIONS.json';g2='evidence/Z02/GAP_COMPARISON.json';tr='evidence/Z02/TRANSITIONS.json'
rows=[]
for label,n,mode in [('F0=S0',0,'frozen'),('F1',1,'frozen'),('S1',1,'scheduled')]:
 target='S0' if n==0 else label;pi=next(i for i,p in enumerate(get(g1,'/references/0/points')) if p['point']==target)
 rows.append([label,value('z01_points',label,'radius',o1,f'/samples/{n}/derived/{mode}/spatial/radius'),value('z01_points',label,'nearest',g1,f'/references/0/points/{pi}/nearest_arc_labels'),value('z01_points',label,'distance',g1,f'/references/0/points/{pi}/nearest_arc_distance')])
table('z01_points',['Point','Radius','Nearest arc','Boundary distance'],rows)
rows=[]
for i in range(5):
 rows.append([str(i),value('z02_points',i,'frozen_radius',o2,f'/samples/{i}/frozen/spatial/radius'),value('z02_points',i,'frozen_label',g2,f'/evaluations/F{i}/gap/unique_winner'),value('z02_points',i,'scheduled_radius',o2,f'/samples/{i}/scheduled/spatial/radius'),value('z02_points',i,'scheduled_label',g2,f'/evaluations/S{i}/gap/unique_winner')])
table('z02_points',['n','Frozen radius','Frozen label','Scheduled radius','Scheduled label'],rows)
table('chords',['Middle n','Frozen chord angle (°)','Scheduled chord angle (°)'],[[str(i),value('chords',i,'F',tr,f'/intervals/{i}/turn_at_middle_stored_index/F/angle_degrees',6),value('chords',i,'S',tr,f'/intervals/{i}/turn_at_middle_stored_index/S/angle_degrees',6)] for i in [1,2,3]])
ib='evidence/Z03/NATIVE_INTENSITY_BUDGET.json';rb='evidence/Z03/RADIAL_TRANSVERSE_ACCOUNTING.json';fb='evidence/Z03/FROZEN_Z_SOURCE_BUDGET.json'
table('intensity',['Span','Onsite','Graph','Finite square','ΔI (saved)'],[[f'{i}→{i+1}',*[value('intensity',i,k,ib,f'/runs/120/{i}/intensity/parent/{k}',6,True) for k in ['onsite','coupling','finite_increment_square']],value('intensity',i,'total',ib,f'/runs/120/{i}/intensity/actual_delta_I',6,True)] for i in range(4)])
table('radial',['Span','Macro size','Chiral size','Cross term','Total Δradius²'],[[f'{i}→{i+1}',*[value('radial',i,k,rb,f'/runs/120/{i}/radial_transverse/coarse_endpoint_difference/{k}',9,True) for k in ['macro_magnitude','chiral_magnitude','cross_alignment']],value('radial',i,'total',rb,f'/runs/120/{i}/radial_transverse/actual_delta_radius_squared',9,True)] for i in range(4)])
for name,indices in [('displacements_early',[0,1]),('displacements_late',[2,3])]:
 table(name,['Span','Δx','Δy','Δz','Δradius'],[[f'{i}→{i+1}',*[value(name,i,k,fb,f'/runs/120/{i}/frozen/actual_displacement/{j}',9,True) for j,k in enumerate(['x','y','z'])],value(name,i,'radius',rb,f'/runs/120/{i}/radial_transverse/actual_delta_radius',9,True)] for i in indices])
qa=[]
for name,keys,digits in [('intensity',['onsite','coupling','finite_increment_square'],6),('radial',['macro_magnitude','chiral_magnitude','cross_alignment'],9)]:
 for i in range(4):
  row={c['column']:Decimal(c['display']) for c in cells if c['table']==name and c['row']==i}
  residual=sum(row[k] for k in keys)-row['total'];bound=Decimal(2)*Decimal(10)**(-digits)
  assert abs(residual)<=bound
  qa.append({'table':name,'row':i,'rounded_parent_sum_minus_rounded_total':str(residual),'rounding_allowance':str(bound),'passed':True,'not_a_scientific_budget_recalculation':True})
figs=[]
for src,dest in [('evidence/Z02/figures/01_top.png','z02_top.png'),('evidence/Z02/figures/02_opposite_sides.png','z02_sides.png'),('evidence/Z03/figures/03_radial_balance.png','z03_radial.png')]:
 out=R/'manuscript/figures'/dest;out.parent.mkdir(exist_ok=True);shutil.copyfile(R/src,out)
 b=(R/src).read_bytes();assert b==out.read_bytes();figs.append({'source_extracted_file':src,'manuscript_file':'manuscript/figures/'+dest,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'modification':'none; uncropped original'})
(T/'TABLE_PROVENANCE.json').write_text(json.dumps({'policy':'Stored tokens parsed directly; only deterministic decimal rounding and table sums; no endpoint or budget computation','cells':cells},indent=2,ensure_ascii=False,default=str)+'\n',encoding='utf-8')
(R/'TABLE_QA.json').write_text(json.dumps(qa,indent=2)+'\n',encoding='utf-8')
(R/'FIGURE_PROVENANCE.json').write_text(json.dumps(figs,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'extracted_table_cells':len(cells),'tables':7,'rounded_table_sum_checks':len(qa),'original_figures_copied':len(figs),'scientific_evaluations':0}))
parent=load('evidence/Z01/inputs/parent_run_record.json');print('PARENT_KEYS',list(parent));print('PARAMETER_FIELDS',[(k,v) for k,v in parent.items() if 'param' in k or 'config' in k])
