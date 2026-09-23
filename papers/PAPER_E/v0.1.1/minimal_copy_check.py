"""Bounded isolated release copy: paper build, revision check and frozen figures only."""
import runtime
from runtime import ROOT
from pathlib import Path
import hashlib,json,os,re,shutil,subprocess,sys
REPO=ROOT.parents[2];TARGET=ROOT/'.build/minimal_copy/repo'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
paths=(ROOT/'PROPOSED_PUBLICATION_ALLOWLIST.txt').read_text().splitlines()
assert not TARGET.exists(),'Refusing to overwrite an existing minimal copy'
for name in paths:
    src=REPO/name;dst=TARGET/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
EP=TARGET/'papers/PAPER_E';EV=EP/'v0.1.1'
env=os.environ.copy();env['PYTHONPATH']='';env['PYTHONNOUSERSITE']='1';env['MPLCONFIGDIR']=str(TARGET/'mplconfig')
records=[]
def run(script,cwd):
    result=subprocess.run([sys.executable,'-B','-X','utf8',str(script)],cwd=cwd,env=env,capture_output=True)
    logfile=ROOT/'.build'/('minimal_'+script.stem+'.log');logfile.write_bytes(result.stdout+result.stderr)
    records.append({'script':script.relative_to(TARGET).as_posix(),'returncode':result.returncode,'stdout_stderr_sha256':sha(logfile)})
    if result.returncode:raise RuntimeError(logfile.read_text(errors='replace'))
run(EV/'build_publication.py',EV)
canonical=ROOT/'publication/PAPER_E_Z_MANIFOLD_v0.1.1.pdf'
rebuilt=EV/'publication/PAPER_E_Z_MANIFOLD_v0.1.1.pdf'
pdf_equal=sha(canonical)==sha(rebuilt)
run(EV/'check_revision.py',EV)
run(EP/'generate_figures.py',EP)
figure_comparisons=[]
for original in sorted((ROOT.parent/'figures').glob('*')):
    copied=EP/'figures'/original.name
    equal=sha(original)==sha(copied)
    metadata_only=False
    if not equal and original.suffix=='.svg':
        strip=lambda s:re.sub(r'<dc:date>.*?</dc:date>','<dc:date>IGNORED_TIMESTAMP</dc:date>',s)
        metadata_only=strip(original.read_text())==strip(copied.read_text())
    figure_comparisons.append({'path':original.name,'byte_equal':equal,'only_svg_timestamp_differs':metadata_only,'original_sha256':sha(original),'rebuilt_sha256':sha(copied)})
assert all(x['byte_equal'] or x['only_svg_timestamp_differs'] for x in figure_comparisons)
record={'attribution':'New Codex minimal-copy build and frozen-data rendering; no scientific source replay',
 'copied_paths_at_execution':len(paths),'copied_input_sha256':{n:sha(REPO/n) for n in paths},
 'commands':records,'pdf_byte_equal':pdf_equal,'canonical_pdf_sha256':sha(canonical),'rebuilt_pdf_sha256':sha(rebuilt),
 'figure_comparisons':figure_comparisons,'declared_python_library_paths':os.environ.get('PAPER_E_PYTHON_PATH','').split(os.pathsep),
 'tools':{k:os.environ.get(k) for k in ['PAPER_E_PANDOC','PAPER_E_TECTONIC','PAPER_E_TEX_CACHE']},
 'python':sys.version,'historical_replays_run':0,'GPT_checker_run':False,'installed_or_upgraded_dependencies':False,
 'remaining_inventory_step':'Late closeout metadata will be copied and every final manifest hash checked separately'}
(ROOT/'evidence/minimal_copy_results.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'copied_paths':len(paths),'pdf_byte_equal':pdf_equal,'figure_files':len(figure_comparisons),'figure_byte_equal':sum(x['byte_equal'] for x in figure_comparisons),'svg_timestamp_only':sum(x['only_svg_timestamp_differs'] for x in figure_comparisons)},indent=2))
