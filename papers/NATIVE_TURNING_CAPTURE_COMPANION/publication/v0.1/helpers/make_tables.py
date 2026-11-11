"""Transcribe accepted saved terminal bounds; no scientific checker or trajectory."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
import hashlib, json, os
R=Path(__file__).resolve().parents[1]
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
source=R/'evidence/accepted_capture/submitted/data/CERTIFICATE_CHECK.json'
c=json.loads(source.read_text());assert c['status']=='PASS' and c['exact_seed_entry_N']==50
expected=[('0.997219','0.997220',492851),('0.997622','0.997623',492769),('0.996782','0.996783',492356)]
rows=[]
for label,item,(lo,hi,margin) in zip('ABC',c['terminal'],expected):
    assert list(map(Fraction,item['amplitude_bounds']))==[Fraction(lo),Fraction(hi)]
    assert item['cone_margin_lower_integer']==margin
    rows.append(f'{label} & {lo} & {hi} & {margin} \\\\')
text=r'''% Generated only from the accepted saved checker record; decimals are exact.
\begin{table}[htbp]\centering
\caption{Strict terminal amplitude bounds and conservative cone margins at
update 50. The last column bounds $\re w_i-8|\im w_i|$ from below.
All values concern native state coordinates; no physical units are assigned.}
\label{tab:terminal}
\begin{tabular}{@{}lrrr@{}}\toprule
Channel & Lower amplitude & Upper amplitude & Cone margin\\\midrule
'''+ '\n'.join(rows)+r'''
\bottomrule\end{tabular}
\end{table}
'''
out=R/'tables/terminal_bounds.tex';out.parent.mkdir(exist_ok=True);out.write_text(text,encoding='utf-8')
record={'kind':'Document transcription check, not scientific replay','status':'PASS','checked_utc':datetime.now(timezone.utc).isoformat(),'source':source.relative_to(R).as_posix(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'output':out.relative_to(R).as_posix(),'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'exact_fraction_comparisons':6,'cone_margin_comparisons':3,'new_native_updates':0,'scientific_checker_executions':0}
(R/'verification/TABLE_TRANSCRIPTION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
