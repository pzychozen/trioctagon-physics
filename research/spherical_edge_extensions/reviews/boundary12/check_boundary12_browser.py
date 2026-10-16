"""Independent local viewer QA using a bounded loopback-only preview; no remote calls.
Uses the installed browser as-is. On navigation or launch restrictions, records the limit
and stops rather than trying an alternate navigation mode or bypass.
"""
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
import threading,json,time,traceback
from playwright.sync_api import sync_playwright
ROOT=Path('/mnt/data/boundary12_submission'); OUT=Path('/mnt/data/BOUNDARY12_GPT_SCIENTIFIC_REVIEW_v0.1')
checks=[];errors=[];blocked=[];started=time.monotonic();server=None
result={'PASS':False,'checks':checks,'page_errors':errors,'blocked_external_requests':blocked}
def ck(name,value):
    if not value:raise AssertionError(name)
    checks.append(name)
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
try:
    server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)))
    threading.Thread(target=server.serve_forever,daemon=True).start()
    url=f'http://127.0.0.1:{server.server_port}/BOUNDARY12_VIEWER.html'
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,timeout=10000)
        result['browser_version']=browser.version
        page=browser.new_page(viewport={'width':1440,'height':1050},device_scale_factor=1)
        page.on('pageerror',lambda e:errors.append(str(e)))
        def route(r):
            if r.request.url.startswith(f'http://127.0.0.1:{server.server_port}/'):r.continue_()
            else:blocked.append(r.request.url);r.abort()
        page.route('**/*',route)
        page.goto(url,wait_until='load',timeout=20000)
        def ready():page.wait_for_function("typeof running!=='undefined' && !running && !pending",timeout=15000)
        ready();page.wait_for_timeout(300)
        ck('default A and opt-in hull',page.locator('#status').inner_text().startswith('Exact event A') and not page.locator('#hull').is_checked())
        ck('actual Plotly scene and WebGL canvas',page.locator('#plot canvas').count()>0 and page.evaluate('document.getElementById("plot").data.length')>0)
        snapshots=[]
        for preset in ['original','A','B','R_equals_w','t_equals_w','assigned_R10','assigned_RT']:
            page.select_option('#preset',preset);ready()
            st=page.locator('#status').inner_text();nt=page.locator('#network-note').inner_text()
            event=preset in ['original','A','B'];ck('preset '+preset,('18 unique dots' in st)==event and ('42 separate branch markers' in st)==(not event) and page.locator('#error').inner_text()=='')
            snapshots.append({'preset':preset,'status':st,'network':nt})
        page.click('#first');ready();page.check('#hull');ready();page.screenshot(path=str(OUT/'VIEWER_A_INDEPENDENT.png'))
        page.click('#last');ready();page.click('[data-view=side]');page.wait_for_timeout(400)
        ck('B graph and hull counts','V=54, E=105' in page.locator('#network-note').inner_text() and '18/36/20' in page.locator('#network-note').inner_text())
        page.screenshot(path=str(OUT/'VIEWER_B_INDEPENDENT.png'))
        page.select_option('#edge','E01');ready();ck('edge selection preserves rays','E01-' in page.locator('#edge-info').inner_text() and 'E01+' in page.locator('#edge-info').inner_text())
        def enter(id,value):
            page.locator('#'+id).fill(str(value));page.locator('#'+id).press('Tab');ready()
        enter('chord',1);ck('C=1 selects A','Exact event A' in page.locator('#status').inner_text())
        enter('extension',1);ck('ell=1 selects B','Exact event B' in page.locator('#status').inner_text())
        # Actual UI-created export (not just function invocation).
        page.click('#export');page.locator('#export-details summary').click()
        actualB=json.loads(page.locator('#export-text').input_value());
        ck('prepared B export',actualB['exact_event']=='B' and len(actualB['branches'])==42 and len(actualB['unique_dots_if_exact_event'])==18)
        (OUT/'INDEPENDENT_BROWSER_EXPORT_B.json').write_text(json.dumps(actualB,indent=2)+'\n')
        page.click('#first');ready();enter('width',3);page.select_option('#unit','edge');ready();page.click('#export')
        exportA=json.loads(page.locator('#export-text').input_value());ck('scaled A export',exportA['w']==3 and exportA['selected_unit']=='edge' and exportA['exact_event']=='A' and len(exportA['branches'])==42)
        (OUT/'INDEPENDENT_BROWSER_EXPORT_A.json').write_text(json.dumps(exportA,indent=2)+'\n')
        enter('width',0);ck('invalid width disables export',bool(page.locator('#error').inner_text()) and page.locator('#export').is_disabled())
        enter('width',1);enter('radius',.5);ck('invalid radius disables export',bool(page.locator('#error').inner_text()) and page.locator('#export').is_disabled())
        page.click('#first');ready()
        for v in [.7637626157259734,.7637626159259734]:
            enter('radius',v);ck('near event is not exact '+str(v),'no exact event tag' in page.locator('#status').inner_text())
        page.click('#first');ready();page.select_option('#unit','extension');ready();page.click('#original');ready()
        ck('zero extension unit disabled and reverted',page.locator('#unit option[value=extension]').is_disabled() and page.locator('#unit').input_value()=='width')
        ck('no page errors',not errors)
        result.update(PASS=True,snapshots=snapshots,controls_exercised='seven presets, lengths, width/unit, graph/hull layer, edge selection, side camera, invalid/near-event input, prepared exports',limits='Mouse drag, mobile layout, save/download workflow, arbitrary ranges, and production integration not certified.')
        browser.close()
except Exception as e:
    result['failure']=str(e);result['traceback']=traceback.format_exc()
finally:
    if server:server.shutdown();server.server_close()
    result['elapsed_seconds']=time.monotonic()-started
    (OUT/'INDEPENDENT_BROWSER_QA.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
