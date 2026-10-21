"""Publication typesetting and TeX-to-Markdown synchronization only.
No scientific module is imported or executed. No resources are downloaded.
Build intermediates and logs belong in --work-dir, outside this publication.
"""
from pathlib import Path
import argparse, hashlib, json, os, re, shutil, subprocess, time
B=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write_json(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def braced(text, start):
    assert text[start]=='{', (start,text[start:start+30])
    n=1; i=start+1
    while n:
        if text[i]=='{' and text[i-1]!='\\': n+=1
        elif text[i]=='}' and text[i-1]!='\\': n-=1
        i+=1
    return text[start+1:i-1], i

def replace_cmd(text, name, fn):
    pattern=re.compile(r'\\'+re.escape(name)+r'\{')
    result=[]; pos=0
    for_loop_guard=0
    while True:
        m=pattern.search(text,pos)
        if not m: result.append(text[pos:]); break
        arg,end=braced(text,m.end()-1)
        result += [text[pos:m.start()],fn(arg)]
        pos=end; for_loop_guard+=1
        assert for_loop_guard<10000
    return ''.join(result)

def synchronize(work):
    tex=(B/'manuscript.tex').read_text(encoding='utf-8')
    aux=(work/'manuscript.aux').read_text(encoding='utf-8') if (work/'manuscript.aux').exists() else ''
    labels=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux))
    citations=dict(re.findall(r'\\bibcite\{([^}]+)\}\{([^}]+)\}',aux))
    body=tex.split(r'\begin{document}',1)[1].split(r'\end{document}',1)[0]
    body=re.sub(r'^%.*$', '', body, flags=re.M)
    title='SRG Attractor Dynamics: Selective Retention and Certified Convergence under Returning Drive'
    body=body.replace(r'\maketitle', '# '+title+'\n\nHilmir Frímann Halldórsson\n\n21 October 2026\n\nv0.1 — Publication edition')
    body=body.replace(r'\begin{abstract}', '\n## Abstract\n').replace(r'\end{abstract}','\n')
    body=re.sub(r'\\addcontentsline\{toc\}\{section\}\{[^}]*\}', '', body)
    body=body.replace(r'\tableofcontents','').replace(r'\clearpage','').replace(r'\FloatBarrier','').replace(r'\appendix','')
    body=body.replace(r'\begin{landscape}','').replace(r'\end{landscape}','')
    section_n=0; subsection_n=0; append=False
    def heading(m):
        nonlocal section_n,subsection_n,append
        level,star,title,label=m.group(1),m.group(2),m.group(3),m.group(4)
        if level=='section':
            subsection_n=0
            if label in labels:
                num=labels[label]
            elif not star:
                section_n+=1; num=str(section_n)
            else: num=''
        else:
            subsection_n+=1; num=''
        anchor=f'<a id="{label}"></a>\n' if label else ''
        return '\n'+anchor+('##' if level=='section' else '###')+' '+(num+' ' if num else '')+title+'\n'
    body=re.sub(r'\\(section|subsection)(\*?)\{([^}]+)\}(?:\\label\{([^}]+)\})?',heading,body)
    def figure(m):
        content=m.group(1)
        file=re.search(r'\\includegraphics\[[^]]+\]\{([^}]+)\}',content).group(1)
        cm=re.search(r'\\caption\{',content); caption,_=braced(content,cm.end()-1)
        label=re.search(r'\\label\{([^}]+)\}',content).group(1)
        number=labels.get(label,label)
        return f'\n<a id="{label}"></a>\n![Figure {number}]({file})\n\n**Figure {number}.** '+caption+'\n'
    body=re.sub(r'\\begin\{figure\}\[[^]]*\](.*?)\\end\{figure\}',figure,body,flags=re.S)
    def table(m):
        content=m.group(1)
        cm=re.search(r'\\caption\{',content); caption,_=braced(content,cm.end()-1)
        label=re.search(r'\\label\{([^}]+)\}',content).group(1)
        bm=re.search(r'\\begin\{tabular\}\{',content); _,end=braced(content,bm.end()-1)
        data=content[end:content.index(r'\end{tabular}')]
        data=re.sub(r'\\(?:toprule|midrule|bottomrule)','',data)
        rows=[x.strip() for x in data.split('\\\\') if x.strip()]
        cells=[[c.strip().replace('\n',' ') for c in row.split('&')] for row in rows]
        output=['| '+' | '.join(cells[0])+' |','| '+' | '.join(['---']*len(cells[0]))+' |']
        output += ['| '+' | '.join(row)+' |' for row in cells[1:]]
        return '\n<a id="'+label+'"></a>\n**Table '+labels.get(label,label)+'.** '+caption+'\n\n'+'\n'.join(output)+'\n'
    body=re.sub(r'\\begin\{table\}\[[^]]*\](.*?)\\end\{table\}',table,body,flags=re.S)
    def equation(m):
        s=m.group(1)
        lm=re.search(r'\\label\{([^}]+)\}',s); lab=lm.group(1)
        s=s.replace(lm.group(0),'').strip()
        return '\n<a id="'+lab+'"></a>\n$$\n'+s+'\n\\tag{'+labels.get(lab,lab)+'}\n$$\n'
    body=re.sub(r'\\begin\{equation\}(.*?)\\end\{equation\}',equation,body,flags=re.S)
    for env in ['theorem','proposition','corollary']:
        def theorem(m,env=env):
            lab=m.group(2)
            return '\n<a id="'+lab+'"></a>\n**'+env.title()+' '+labels.get(lab,lab)+' ('+m.group(1)+').** '+m.group(3).strip()+'\n'
        body=re.sub(r'\\begin\{'+env+r'\}\[([^]]+)\]\\label\{([^}]+)\}(.*?)\\end\{'+env+r'\}',theorem,body,flags=re.S)
    body=body.replace(r'\begin{proof}', '\n**Proof.** ').replace(r'\end{proof}',' $\\square$\n')
    body=body.replace(r'\begin{thebibliography}{99}','\n## References\n').replace(r'\end{thebibliography}','')
    body=re.sub(r'\\bibitem\{([^}]+)\}',lambda m:'\n<a id="ref-'+m[1]+'"></a>\n['+citations.get(m[1],m[1])+'] ',body)
    body=replace_cmd(body,'cite', lambda s:', '.join('['+citations.get(k,k)+'](#ref-'+k+')' for k in s.split(',')))
    body=replace_cmd(body,'eqref',lambda s:'(['+labels.get(s,s)+'](#'+s+'))')
    body=replace_cmd(body,'ref',lambda s:'['+labels.get(s,s)+'](#'+s+')')
    body=replace_cmd(body,'texttt',lambda s:'`'+s.replace(r'\_','_')+'`')
    body=replace_cmd(body,'emph',lambda s:'*'+s+'*')
    body=body.replace(r'\Cset',r'\mathcal C').replace(r'\atanTwo',r'\operatorname{atan2}')
    body=re.sub(r'\\R\b',lambda _:r'\mathbb R',body)
    body=body.replace('~',' ').replace('``','“').replace("''",'”').replace('---','—')
    # Preserve Markdown table delimiters after text dash normalization.
    body=re.sub(r'(?m)^\| ([— |]+)\|$',lambda m:m[0].replace('—','---'),body)
    body=re.sub(r'(?<!-)--(?!-)','–',body)
    body=body.replace(r'\_','_')
    body=re.sub(r'\n{3,}','\n\n',body).strip()+'\n'
    note='<!-- Generated editorially from manuscript.tex; do not edit independently. Equation/table/figure numbering is synchronized from the compiled AUX. -->\n\n'
    (B/'SRG_ATTRACTOR_DYNAMICS_v0.1.md').write_text(note+body,encoding='utf-8')
    write_json(work/'TEXT_SYNCHRONIZATION.json', {'canonical':'manuscript.tex','tex_sha256':sha(B/'manuscript.tex'),
        'markdown_sha256':sha(B/'SRG_ATTRACTOR_DYNAMICS_v0.1.md'),'labels':labels,'citations':citations,
        'method':'single canonical TeX body; editorial structural conversion; no scientific evaluation'})


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--tectonic',required=True)
    ap.add_argument('--cache-dir',type=Path,required=True)
    ap.add_argument('--work-dir',type=Path,required=True)
    a=ap.parse_args()
    work=a.work_dir.resolve(); work.mkdir(parents=True,exist_ok=True)
    assert work!=B and B not in work.parents, 'Keep build work outside the publication payload.'
    assert a.cache_dir.is_dir(), 'Use an existing Tectonic cache.'
    env=os.environ.copy();env['TECTONIC_CACHE_DIR']=str(a.cache_dir.resolve())
    env['SOURCE_DATE_EPOCH']='1792540800'
    fc=work/'fontconfig-cache';fc.mkdir(exist_ok=True)
    cfg=work/'fonts.conf'
    cfg.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>C:/Windows/Fonts</dir><cachedir>'+fc.as_posix()+'</cachedir></fontconfig>',encoding='utf-8')
    env['FONTCONFIG_FILE']=str(cfg)
    cmd=[a.tectonic,'-X','compile','--only-cached','--keep-logs','--keep-intermediates','--outdir',str(work),str(B/'manuscript.tex')]
    start=time.time();p=subprocess.run(cmd,cwd=B,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (work/'compile.txt').write_text(p.stdout+'\nSTDERR\n'+p.stderr,encoding='utf-8')
    write_json(work/'BUILD_RUN.json',{'argv':cmd,'exit_code':p.returncode,'seconds':time.time()-start,'science_steps':0,'network':'only-cached'})
    print(p.stdout[-2500:]);print(p.stderr[-2500:])
    if p.returncode:raise SystemExit(p.returncode)
    shutil.copyfile(work/'manuscript.pdf',B/'SRG_ATTRACTOR_DYNAMICS_v0.1.pdf')
    synchronize(work)
    print('Publication PDF built; Markdown synchronized; scientific executions: 0.')
