"""Editorial-only repair of inline math delimiters; no mathematical evaluation."""
from pathlib import Path
import json, re
W=Path(__file__).resolve().parent
p=W/'NATIVE_SAME_TRAJECTORY_RETURN_01_PROOF.md'
text=p.read_text(encoding='utf-8')
result=[];changed=[];display=False
for line in text.splitlines(keepends=True):
    if line.strip()==r'\[':display=True
    if display:
        result.append(line)
        if line.strip()==r'\]':display=False
        continue
    spans=[];i=0
    while i<len(line):
        if line[i]!='(':
            i+=1;continue
        start=i;depth=1;i+=1
        while i<len(line) and depth:
            if line[i]=='(':depth+=1
            elif line[i]==')':depth-=1
            i+=1
        if depth:break
        content=line[start+1:i-1]
        is_link=start>0 and line[start-1]==']'
        is_reference=bool(re.fullmatch(r'R\d+',content))
        is_math='\\' in content or bool(re.search(r'[=<>_^]',content)) or bool(re.fullmatch(r'[A-Za-z0-9]',content))
        if is_math and not is_link and not is_reference:
            spans.append((start,i,content))
    for start,end,content in reversed(spans):
        line=line[:start]+'$'+content+'$'+line[end:]
        changed.append(content)
    result.append(line)
assert not display
p.write_text(''.join(result),encoding='utf-8')
(W/'EDITORIAL_FORMATTING.json').write_text(json.dumps({'scope':'Inline Markdown math delimiters only; equations and mathematical content unchanged.',
    'repaired_spans':len(changed),'spans':list(reversed(changed))},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'inline_math_spans_repaired':len(changed)}))
