"""Final-publication source/transcription/export/link/build checks; no historical writers."""
from pathlib import Path
import re,json,hashlib,argparse,ast
ROOT=Path(__file__).resolve().parents[1]
def canon(s):
    s=re.sub(r'\\label\{[^}]+\}','',s)
    s=re.sub(r'\\(?:begin|end)\{(?:gathered|aligned)\}','',s)
    return re.sub(r'\s+','',s.replace('\\\\',''))
def main():
    checks=[];info={}
    def ck(name,passed,details=None):
        checks.append({'name':name,'passed':bool(passed),'details':details})
    inventory=json.loads((ROOT/'provenance/source_inventory.json').read_text())
    bad=[e['path'] for e in inventory if hashlib.sha256((ROOT/e['path']).read_bytes()).hexdigest()!=e['sha256']]
    ck('Public source identities: unchanged copies and labeled derivatives',not bad,{'files':len(inventory),'mismatches':bad})
    for lane,name,count in [('measurement','MEASUREMENT_GEOMETRY_SYNTHESIS.md',47),('drift','CHIRAL_DRIFT_SYNTHESIS.md',53)]:
        master=(ROOT/lane/'supplement/historical'/name).read_text(encoding='utf-8')
        tex=(ROOT/lane/'manuscript.tex').read_text(encoding='utf-8')
        originals=re.findall(r'(?<!\\)\\\[(.*?)\\\]',master,re.S)
        new=re.findall(r'(?<!\\)\\\[(.*?)\\\]',tex,re.S)
        missing=[m for m in originals if canon(m) not in set(map(canon,new))]
        ck(lane+' all displayed equations, including unnumbered',not missing,{'original_display_count':len(originals),'missing':missing})
        tags=re.findall(r'\\tag\{([^}]+)\}',tex)
        ck(lane+' label crosswalk',len(tags)==count and len(set(tags))==count,{'count':len(tags)})
        refs=re.findall(r'\\eqref\{eq:([^}]+)\}',tex)
        ck(lane+' equation references',set(refs)<=set(tags),sorted(set(refs)-set(tags)))
        links=re.findall(r'\\href\{\\detokenize\{([^}]+)\}\}',tex)
        badlinks=[s for s in links if not s.startswith(('http://','https://')) and not (ROOT/lane/s).resolve().exists()]
        ck(lane+' portable local links',not badlinks,badlinks)
        nonmath=re.sub(r'(?<!\\)\\\[.*?\\\]|\\\(.*?\\\)','',tex,flags=re.S)
        ck(lane+' no private production path or placeholders',not re.search(r'(?<![A-Za-z])[A-Za-z]:[/\\]|/(?:home|mnt|tmp)/',nonmath) and not any(s in tex for s in ['ZZZTOKEN','@@TEX@@','EDITORIAL_CHECK']))
        log=(ROOT/'results/build'/lane/'manuscript.log').read_text(encoding='utf-8',errors='replace')
        failures=[s for s in log.splitlines() if 'Overfull' in s or 'Missing character' in s or 'undefined' in s.lower()]
        ck(lane+' build diagnostics',not failures,failures)
        ck(lane+' final status and public evidence destination',
           all(s in tex for s in ['Research publication v0.1','https://github.com/pzychozen/trioctagon-physics','papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/','repository publication is pending'])
           and 'Review candidate v0.1' not in tex and 'Manuscript review candidate v0.1' not in tex)
        seq=re.findall(r'(?<!\\)\\\[.*?\\\]|\\\(.*?\\\)',tex,re.S)
        digest=hashlib.sha256(json.dumps(seq,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
        reviewed=json.loads((ROOT/'provenance/review_mathematics.json').read_text())[lane]
        ck(lane+' entire reviewed inline/display mathematics sequence',digest==reviewed['math_sequence_sha256'],{'expressions':len(seq)})
    ck('Final smoke independent of retained counts',json.loads((ROOT/'results/portable_smoke.json').read_text())['status']=='PASS',{'retained_suites_replayed':False})
    exports=json.loads((ROOT/'provenance/public_export_map.json').read_text(encoding='utf-8'))['files']
    errors=[];subtrees=0;functions=0
    def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
    for e in exports:
        if e['disposition']=='omitted_container':
            if (ROOT/e['path']).exists():errors.append(e['path']+' omitted container present')
            continue
        path=ROOT/e['path'];raw=path.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=e['public_sha256']:errors.append(e['path']+' public identity')
        if 'projection_sha256' in e:
            obj=json.loads(raw);obj.pop('_public_export')
            if digest(obj)!=e['projection_sha256']:errors.append(e['path']+' documented public projection')
            for key,value in e['scientific_subtree_sha256'].items():
                subtrees+=1
                if digest(obj[key])!=value:errors.append(e['path']+' scientific subtree '+key)
        if 'unchanged_math_sequence_sha256' in e:
            text=raw.decode('utf-8-sig').replace('\r\n','\n')
            seq=re.findall(r'\\\[.*?\\\]|\\\(.*?\\\)',text,re.S)
            if hashlib.sha256(json.dumps(seq,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()!=e['unchanged_math_sequence_sha256']:errors.append(e['path']+' math strings')
        if 'unchanged_function_body_sha256' in e:
            text=raw.decode('utf-8-sig');tree=ast.parse(text)
            for n in tree.body:
                if isinstance(n,(ast.FunctionDef,ast.ClassDef)):
                    functions+=1
                    if hashlib.sha256(ast.get_source_segment(text,n).encode()).hexdigest()!=e['unchanged_function_body_sha256'][n.name]:errors.append(e['path']+' function '+n.name)
    ck('Public export fingerprints and retained scientific content',not errors,{'scientific_subtrees':subtrees,'unchanged_function_bodies':functions,'errors':errors,'raw_to_public_equality_audit':'retained production record; raw originals intentionally not distributed'})
    template=(ROOT/'tools/typeset.py').read_text(encoding='utf-8')
    ck('Source-generation template retains final publication metadata',
       'Research publication v0.1' in template and 'Review candidate v0.1' not in template and 'Manuscript review candidate v0.1' not in template)
    out={'status':'PASS' if all(c['passed'] for c in checks) else 'FAIL','checks':checks,'passed':sum(c['passed'] for c in checks),'total':len(checks)}
    (ROOT/'results/publication_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
    return 0 if out['status']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
