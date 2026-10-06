"""Explicit claim-to-predicate curation; no keyword-based evidence attribution."""
from pathlib import Path
import json
L=Path(__file__).resolve().parents[1]
p=L/'provenance/theorem_ledger.json';d=json.loads(p.read_text(encoding='utf8'))
pred=json.loads((L/'verification/retained_predicates.json').read_text(encoding='utf8'))['predicates']
sets={
1:[33,34,35],2:[1,3,5,7,8,12,13,17,18],3:[9,10,11,14,15,16,19,20,21,22],4:[23,24,25,26,27,28,29,31,32],5:[],6:[33,34,35,45],7:list(range(36,42)),8:list(range(36,42)),9:[42,43,44],
10:[1,5,6],11:[1,2,3,4],12:list(range(7,13)),13:[13],14:list(range(14,28)),15:[13,15],16:list(range(28,39)),17:[],18:[1,2,3,4,5],19:[17,18],20:[12],21:[19,21,23,24,26,28,30,32],22:[6,7,8,9,10,11],23:[20,22,25,27,29,31],24:[9,27,31],25:[13,14,15,16],26:[33,34,36,41,42],27:[35,37,38],
28:list(range(1,40)),29:list(range(4,45)),30:[45],31:[46,47],32:[48,49,50],33:list(range(53,79)),34:list(range(176,212)),35:list(range(212,217)),36:list(range(154,174)),37:[223,224,225,226],38:[],39:[219,220,221,222],40:[],41:[],42:[],43:[],44:[],45:[]}
for i,r in enumerate(d['records'],1):
 r['supporting_verification_predicates']=[pred[r['checkpoint']][j-1] for j in sets[i]]
 r.pop('predicate_search',None)
 if i==5:r['statement']='For epsilon nonzero, fixed states on the nonzero common-channel line form sqrt(k) exp(i chi) 1 exactly when k>0.'
 if i==28:r['qualifications']='Not ordinary S3 action on both channel triples. This is kinematic covariance; F carries k under permutations and has a regular-domain qualification for mirrors involving common phase.'
 if i in (40,41,42):r['verification_note']='Written proof and exact source statement; bounded quotient comparisons are in SA0 numerical_checks, not in the 226 exact/source predicate list.'
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print('Explicitly curated supporting predicates for all 45 records.')
