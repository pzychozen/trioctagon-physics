"""Read-only HTTP availability check of bibliography URLs; no repository operation."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
tex = (ROOT/'manuscript/references.tex').read_text(encoding='utf-8')
urls = sorted(set(re.findall(r'\\href\{(https://[^}]+)\}',tex)))

def check(url):
    request = urllib.request.Request(url,method='HEAD',headers={'User-Agent':'Document-reference-check/1.0'})
    try:
        with urllib.request.urlopen(request,timeout=15) as response:
            return {'url':url,'status_code':response.status,'final_url':response.url,'accessible':200<=response.status<400}
    except urllib.error.HTTPError as error:
        return {'url':url,'status_code':error.code,'accessible':False,'error':str(error)}
    except Exception as error:
        return {'url':url,'accessible':False,'error':str(error)}

with ThreadPoolExecutor(max_workers=4) as pool:
    entries = list(pool.map(check,urls))
record = {'checked_utc':datetime.now(timezone.utc).isoformat(),'method':'HTTP HEAD; redirects followed',
          'results':entries,'all_accessible':all(item['accessible'] for item in entries),
          'scope':'Bibliography availability only; no literature search, content inference, Git or scientific execution.'}
(ROOT/'verification/EXTERNAL_LINK_CHECKS.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
