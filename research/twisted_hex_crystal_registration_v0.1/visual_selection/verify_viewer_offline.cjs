// Offline unit tests only. No browser, navigation, networking or user profile.
// Minimal DOM doubles test the actual generated JavaScript; they do not certify
// CSS layout, browser rendering, focus behavior, or native touch input.
const fs=require("fs"),path=require("path"),vm=require("vm"),assert=require("assert"),crypto=require("crypto");
const root=__dirname;
const html=fs.readFileSync(path.join(root,"crystal_selection_viewer.html"),"utf8");
const expected=JSON.parse(fs.readFileSync(path.join(root,"candidate_values.json"),"utf8"));
const reference=JSON.parse(fs.readFileSync(path.join(root,"PROJECTION_REFERENCE.json"),"utf8"));
const all=[],ids=new Map();
function datasetKey(key){return key.slice(5).replace(/-([a-z])/g,(_,x)=>x.toUpperCase());}
class Element{
 constructor(tag){this.tagName=tag;this.attrs={};this.dataset={};this.children=[];this.handlers={};this.hidden=false;this.checked=false;this.clientWidth=580;this.value="";this._text="";
   const classes=new Set();this.classList={toggle:(n,v)=>v?classes.add(n):classes.delete(n)};all.push(this);}
 setAttribute(k,v){this.attrs[k]=String(v);if(k==="id")ids.set(String(v),this);if(k.startsWith("data-"))this.dataset[datasetKey(k)]=String(v);if(k==="value")this.value=String(v);if(k==="checked")this.checked=true;}
 getAttribute(k){return this.attrs[k]??null;}
 append(...children){for(const c of children){if(c.tagName==="#fragment")this.children.push(...c.children);else this.children.push(c);}}
 replaceChildren(...children){this.children=[];this.append(...children);}
 set textContent(v){this._text=String(v);this.children=[];}
 get textContent(){return this._text+this.children.map(c=>c.textContent).join("");}
 addEventListener(name,f){(this.handlers[name]??=[]).push(f);}
 fire(name){for(const f of this.handlers[name]??[])f({target:this});}
}
const markup=html.split('<script id="crystal-model"')[0];
for(const tag of markup.matchAll(/<([a-z][a-z0-9-]*)(\s[^>]*?)?>/gi)){
 const e=new Element(tag[1]);
 for(const a of (tag[2]??"").matchAll(/([:\w-]+)(?:="([^"]*)")?/g))e.setAttribute(a[1],a[2]??"");
}
const payload=html.match(/<script id="crystal-model" type="application\/json">([\s\S]*?)<\/script>/)[1];
const payloadNode=new Element("script");payloadNode.setAttribute("id","crystal-model");payloadNode.textContent=payload;
const document={
 getElementById:id=>{assert(ids.has(id),"Missing element "+id);return ids.get(id);},
 createElement:tag=>new Element(tag),
 createElementNS:(_,tag)=>new Element(tag),
 createDocumentFragment:()=>new Element("#fragment"),
 querySelectorAll:sel=>{
  const match=sel.match(/^\[([a-z-]+)\]$/);assert(match,"Unexpected selector "+sel);
  return all.filter(e=>match[1].startsWith("data-")?datasetKey(match[1]) in e.dataset:match[1] in e.attrs);
 }
};
const js=html.match(/<script>\s*([\s\S]*?)<\/script>/)[1];
const networkAttempt=()=>{throw Error("Networking forbidden in offline QA");};
const sandbox={document,window:{},ResizeObserver:class{observe(){}},fetch:networkAttempt,XMLHttpRequest:networkAttempt,WebSocket:networkAttempt,console};
vm.createContext(sandbox);
vm.runInContext(js,sandbox,{timeout:10000,filename:"generated-viewer-inline.js"});
const api=sandbox.window.crystalAtlas,results=[];
function check(name,test){assert(test,name);results.push({name,pass:true});}
function button(key,value){return document.querySelectorAll(`[data-${key}]`).find(b=>b.dataset[key]===value);}
function walk(e){return [e,...e.children.flatMap(walk)];}
function countLayer(svg,layer){return walk(svg).filter(e=>e.attrs["data-layer"]===layer).length;}
check("offline_file_has_no_remote_scripts_or_styles",!/<(?:script|link)[^>]+(?:src|href)="https?:/i.test(html));
check("no_network_APIs_in_viewer_script",!/\b(?:fetch|XMLHttpRequest|WebSocket)\s*\(/.test(js));
check("initial_display_is_zero_reference_and_both_hands",api.state.t===0&&api.state.hand==="both");
check("nine_equal_status_preset_buttons",document.querySelectorAll("[data-sample]").length===9);
let maxVertexError=0,maxProjectionError=0,maxAlphaError=0,maxDeltaError=0;
for(let i=0;i<9;i++){
 const s=expected.samples[i];button("sample",String(i)).fire("click");
 check("preset_"+s.id+"_sets_exact_exported_t",api.state.t===s.t);
 check("preset_"+s.id+"_updates_t_readout",ids.get("t-value").textContent===s.t.toFixed(9));
 maxAlphaError=Math.max(maxAlphaError,Math.abs(api.alpha(s.t)-s.alpha));
 maxDeltaError=Math.max(maxDeltaError,Math.abs(api.delta(s.t)*180/Math.PI-s.delta_magnitude_degrees));
 for(const [hand,name] of [["plus","TWIST_PLUS"],["minus","TWIST_MINUS"]]){
  const actual=api.vertices(s.t,hand);
  actual.forEach((p,k)=>p.forEach((x,j)=>maxVertexError=Math.max(maxVertexError,Math.abs(x-s.hands[name].vertices[k][j]))));
  for(const view of ["perspective","top","side"]){
   actual.forEach((p,k)=>api.project(p,view).slice(0,2).forEach((x,j)=>maxProjectionError=Math.max(maxProjectionError,Math.abs(x-reference[s.id][name][view][k][j]))));
  }
 }
}
check("all_18_sample_vertex_arrays_match_python",maxVertexError<1e-13);
check("all_54_sample_view_projections_match_python",maxProjectionError<1e-13);
check("all_live_alpha_values_match_symbolic_samples",maxAlphaError<1e-13);
check("all_live_delta_values_match_symbolic_samples",maxDeltaError<1e-12);
button("hand","plus").fire("click");
check("plus_toggle_hides_minus_only",!ids.get("plus-pane").hidden&&ids.get("minus-pane").hidden);
button("hand","minus").fire("click");
check("minus_toggle_hides_plus_only",ids.get("plus-pane").hidden&&!ids.get("minus-pane").hidden);
check("minus_readout_signed_negative",ids.get("delta-value").textContent.startsWith("−"));
button("hand","both").fire("click");
check("both_toggle_displays_both",!ids.get("plus-pane").hidden&&!ids.get("minus-pane").hidden);
for(const camera of ["top","side","perspective"]){
 button("camera",camera).fire("click");
 check("camera_button_"+camera,api.state.camera===camera&&button("camera",camera).attrs["aria-pressed"]==="true");
}
for(const [id,layers] of [["host-toggle",["host-surface","host-wire"]],["surface-toggle",["crystal-surface"]],["wire-toggle",["crystal-wire"]]]){
 const e=ids.get(id);e.checked=false;e.fire("change");
 check(id+"_hides_requested_layers",["plus-svg","minus-svg"].every(id=>layers.every(layer=>countLayer(ids.get(id),layer)===0)));
 check(id+"_retains_contact_markers",["plus-svg","minus-svg"].every(id=>countLayer(ids.get(id),"upper-contact")===3&&countLayer(ids.get(id),"lower-contact")===3));
 e.checked=true;e.fire("change");
 check(id+"_restores_requested_layers",["plus-svg","minus-svg"].every(id=>layers.every(layer=>countLayer(ids.get(id),layer)>0)));
}
const slider=ids.get("t-slider");
slider.value=String(api.model.max_t/2);slider.fire("input");
check("slider_updates_live_state",api.state.t===api.model.max_t/2);
check("slider_updates_live_alpha",ids.get("alpha-value").textContent===api.alpha(api.state.t).toFixed(9));
check("slider_max_is_family_endpoint",Number(slider.max)===api.model.max_t);
let boundsCases=0;
for(const width of [320,580,720]){
 ids.get("plus-svg").clientWidth=width;ids.get("minus-svg").clientWidth=width;
 for(let sample=0;sample<9;sample++){
  button("sample",String(sample)).fire("click");
  for(const camera of ["perspective","top","side"]){
   button("camera",camera).fire("click");
   for(const id of ["plus-svg","minus-svg"]){
    const svg=ids.get(id),height=width/1.06;
    for(const e of walk(svg)){
     let pts=[];
     if(e.tagName==="polygon")pts=e.attrs.points.split(" ").map(p=>p.split(",").map(Number));
     if(e.tagName==="line")pts=[[+e.attrs.x1,+e.attrs.y1],[+e.attrs.x2,+e.attrs.y2]];
     if(e.tagName==="circle")pts=[[+e.attrs.cx-(+e.attrs.r),+e.attrs.cy-(+e.attrs.r)],[+e.attrs.cx+(+e.attrs.r),+e.attrs.cy+(+e.attrs.r)]];
     if(e.tagName==="rect")pts=[[+e.attrs.x,+e.attrs.y],[+e.attrs.x+(+e.attrs.width),+e.attrs.y+(+e.attrs.height)]];
     assert(pts.every(p=>p.every(Number.isFinite)&&p[0]>=0&&p[0]<=width&&p[1]>=0&&p[1]<=height),"SVG geometric mark bounds");
    }
    boundsCases++;
   }
  }
 }
}
check("all_SVG_mark_bounds_valid_at_supplied_widths",boundsCases===162);
button("sample","0").fire("click");button("camera","top").fire("click");
const svg=ids.get("plus-svg"),dots=walk(svg).filter(e=>e.attrs["data-layer"]==="upper-contact");
const diamonds=walk(svg).filter(e=>e.attrs["data-layer"]==="lower-contact");
check("zero_reference_top_markers_nested",dots.every((e,i)=>{
 const cx=+e.attrs.cx,cy=+e.attrs.cy,r=+e.attrs.r;
 const pts=diamonds[i].attrs.points.split(" ").map(p=>p.split(",").map(Number));
 return pts.every(p=>Math.hypot(p[0]-cx,p[1]-cy)<r);
}));
check("zero_reference_does_not_claim_band_rewiring",ids.get("status").textContent.includes("inherited band connections remain"));
const receipt={method:"OFFLINE_JAVASCRIPT_VM_WITH_MINIMAL_DOM_DOUBLES_NOT_A_BROWSER",
 browser_preview:"BLOCKED_BY_BROWSER_LOCAL_FILE_URL_POLICY",
 limitation:"No browser navigation or alternate-browser workaround. CSS layout, native keyboard/touch behavior and mobile browser rendering are not certified. Static PNG figures were inspected separately.",
 runtime:{node:process.version},generated_html_sha256:crypto.createHash("sha256").update(html).digest("hex"),
 results,pass:results.every(r=>r.pass),passed:results.length,total:results.length,
 coordinate_parity:{max_vertex_error:maxVertexError,max_projection_error:maxProjectionError,max_alpha_error:maxAlphaError,max_delta_degrees_error:maxDeltaError},
 SVG_geometry_bounds_cases:boundsCases,widths:[320,580,720],network_requests:0,
 no_value_or_hand_designated_canonical:true};
fs.writeFileSync(path.join(root,"VIEWER_QA.json"),JSON.stringify(receipt,null,2)+"\n");
console.log(JSON.stringify({passed:results.length,pass:receipt.pass,parity:receipt.coordinate_parity,SVG_geometry_bounds_cases:boundsCases,browser_preview:receipt.browser_preview},null,2));
