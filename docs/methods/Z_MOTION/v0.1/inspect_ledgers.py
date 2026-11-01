from pathlib import Path
import json
R=Path(__file__).resolve().parent
def walk(x,p=''):
 if isinstance(x,dict):
  for k,v in x.items():
   if k in ['nearest_labels','nearest_arc','angle_degrees'] and not isinstance(v,dict):print(p+'/'+k,repr(v))
   if isinstance(v,(dict,list)):walk(v,p+'/'+k)
 elif isinstance(x,list):
  for i,v in enumerate(x):
   if isinstance(v,(dict,list)):walk(v,p+'/'+str(i))
for n in ['evidence/Z01/GAP_COMPARISON.json','evidence/Z02/GAP_COMPARISON.json','evidence/Z02/TRANSITIONS.json']:
 x=json.loads((R/n).read_text());print(n,list(x))
 if 'references' in x:
  print('point keys',list(x['references'][0]['points'][0]));print('point summary',{k:v for k,v in x['references'][0]['points'][0].items() if k not in ['arcs','centered']})
 if 'evaluations' in x:print('GAP0 keys',list(x['evaluations']['F0']['gap']));print('GAP0 summary',{k:v for k,v in x['evaluations']['F0']['gap'].items() if k not in ['arcs','patches']})
 walk(x)
for n in []:
 print('\nTEXT',n);lines=(R/n).read_text(encoding='utf-8').splitlines()
 print('\n'.join(lines))
