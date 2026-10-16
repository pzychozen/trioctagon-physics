"""Local, network-blocked Chromium check of the submitted standalone viewer."""
from pathlib import Path
import csv, json, math, time
from playwright.sync_api import sync_playwright
B=Path('/mnt/data/boundary11_submission');O=Path('/mnt/data/BOUNDARY11_GPT_REVIEW_v0.1')
errors=[];requests=[];checks=[]
def check(n,c):
 assert c,n
 checks.append(n)
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
 page=browser.new_page(viewport={'width':1400,'height':1020},accept_downloads=True)
 page.route('http://**/*',lambda route:route.abort());page.route('https://**/*',lambda route:route.abort())
 page.on('request',lambda r:requests.append(r.url))
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto((B/'BOUNDARY11_VIEWER.html').as_uri(),wait_until='load')
 page.wait_for_function("document.documentElement.dataset.viewerReady === 'true' && !rendering",timeout=15000)
 def settle():page.wait_for_function('!rendering && !pending',timeout=15000)
 def snapshot():return page.evaluate("({r:state.radius,count:state.groups.length,branches:state.branches,radial:state.radial,angle:state.sameLineAngleDegrees,traces:document.getElementById('plot').data.map(t=>({type:t.type,name:t.name,len:t.x.length})),error:document.getElementById('error').textContent})")
 initial=snapshot();check('initial 42 dots and 42 branches',initial['count']==len(initial['branches'])==42)
 check('three genuine mesh panels',sum(x['type']=='mesh3d' for x in initial['traces'])==3)
 page.screenshot(path=str(O/'VIEWER_INITIAL.png'),full_page=True)
 results=[]
 for bid in ['at-rho','at-cross-a','at-cross-b']:
  page.locator('#'+bid).click();settle();s=snapshot();check(bid+':18 dots',s['count']==18 and len(s['branches'])==42);results.append({'button':bid,'r':s['r'],'unique_dots':s['count']})
  if bid=='at-cross-b':page.screenshot(path=str(O/'VIEWER_OUTER_EVENT.png'),full_page=True)
 page.locator('#radius').fill('1');page.locator('#radius').dispatch_event('change');settle()
 page.locator('#edge').select_option('E02');settle();check('edge selection', 'E02' in page.locator('#edge-info').inner_text())
 page.locator('#radial').check();settle();s=snapshot();check('18 independent radial crosses',any(t['name']=='Radial vertices' and t['len']==18 for t in s['traces']))
 page.locator('#midpoints').check();settle();s=snapshot();check('21 midpoint markers',any(t['name']=='Tangency midpoints' and t['len']==21 for t in s['traces']))
 page.locator('[data-view=axial]').click();settle();check('axial view',page.evaluate("document.getElementById('plot').layout.scene.camera.eye.z")>1.8)
 page.locator('[data-view=oblique]').click();settle()
 with page.expect_download() as dl:page.locator('#export').click()
 download=dl.value;target=O/'VIEWER_REVIEW_EXPORT_R1.csv';download.save_as(str(target))
 rows=list(csv.DictReader(target.read_text().splitlines()));check('export preserves 42 labels',len(rows)==42 and len({r['branch'] for r in rows})==42)
 s=snapshot();expected={r['id']:r['xyz'] for r in s['branches']}
 check('export matches rendered coordinates',all([float(r['x_over_w']),float(r['y_centered_over_w']),float(r['z_over_w'])]==expected[r['branch']] for r in rows))
 page.locator('#radius').fill('0.5');page.locator('#radius').dispatch_event('change');settle();check('invalid small radius rejected',bool(page.locator('#error').inner_text()))
 page.locator('#radius').fill('10');page.locator('#radius').dispatch_event('change');settle();s=snapshot();check('typed radius above slider',s['r']==10 and s['count']==42)
 page.locator('#radius').fill('1');page.locator('#radius').dispatch_event('change');settle()
 # Independent numeric values from the Python geometry inventory in supplied examples
 # are separately validated by verify_boundary11.py, not trusted as a proof here.
 examples=json.loads((B/'data/numerical_display_examples.json').read_text());maxerr=0
 for ex in examples:
  ss=page.evaluate('(R)=>boundary11Geometry(boundaryData,R)',ex['R_over_w'])
  target=[pt for pair in ex['points'] for pt in pair]
  maxerr=max(maxerr,max(abs(a-b) for row,pt in zip(ss['branches'],target) for a,b in zip(row['xyz'],pt)))
 check('JS coordinates match independently checked fixed examples',maxerr<2e-15)
 check('no browser JS errors',not errors)
 check('no HTTP(S) requests',not any(x.startswith(('http://','https://')) for x in requests))
 browser.close()
result={'status':'PASS','method':'Chromium/Playwright; file://; network URLs blocked; software WebGL','checks':checks,'events':results,'max_coordinate_error':maxerr,'javascript_errors':errors,'request_urls':requests,'finite_scope':'Default radius, three events, layer toggles, selected edge, two camera presets, 42-row CSV, invalid radius 0.5, custom R/w=10, six fixed math test radii. Not a universal hardware or extreme-input certification.'}
(O/'INDEPENDENT_VIEWER_REVIEW.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
