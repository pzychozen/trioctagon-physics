// Reviewer-written verifier for the submitted pure viewer evaluator; no old checker execution.
const fs=require('fs'),vm=require('vm'),path=require('path');
const root='/mnt/data/boundary12_submission', out='/mnt/data/BOUNDARY12_GPT_SCIENTIFIC_REVIEW_v0.1';
const raw=fs.readFileSync(root+'/viewer_math.js','utf8').replace(/\r\n/g,'\n');
const html=fs.readFileSync(root+'/BOUNDARY12_VIEWER.html','utf8').replace(/\r\n/g,'\n');
const data=JSON.parse(fs.readFileSync(root+'/data/viewer_data.json'));
const exp=JSON.parse(fs.readFileSync(out+'/EXPECTED_VIEWER_POINTS.json'));
const names=[],errors=[],stats={max_normalized:0,max_physical:0,max_display:0};
function check(s,b){if(!b)throw Error(s);names.push(s)}
check('exact embedded pure math',html.includes(raw));
const dataText=html.split('<script>const data=')[1].split("\n'use strict';")[0].replace(/;\s*$/,'');
check('embedded data byte-equivalent in parsed content',JSON.stringify(JSON.parse(dataText))===JSON.stringify(data));
const ctx={module:{exports:{}}};vm.createContext(ctx);vm.runInContext(raw,ctx,{timeout:1000});
const {boundary12Geometry:g,boundary12Export:x}=ctx.module.exports;
function near(a,b,tol=6e-14){return Number.isFinite(a)&&Number.isFinite(b)&&Math.abs(a-b)<=tol*Math.max(1,Math.abs(b))}
let count=0;
for(const p of exp)for(const w of [.125,1,3])for(const unit of ['width','edge','chord','extension']){
 const req={preset:p.preset_id,w,unit};
 if(unit==='extension'&&p.preset_id==='original'){let raised=false;try{g(data,req)}catch(e){raised=true}check('zero extension unit '+w,raised);continue}
 const st=g(data,req), output=x(st,data), map=Object.fromEntries(st.branches.map(b=>[b.branch,b]));count++;
 check('readouts '+JSON.stringify(req),Object.entries(p.numeric).every(([k,v])=>near(st[k],v))&&st.branches.length===42&&new Set(st.branches.map(b=>b.branch)).size===42);
 const U={width:1,edge:Math.SQRT2-1,chord:p.numeric.C_over_w,extension:p.numeric.ell_over_w}[unit];
 check('unit '+JSON.stringify(req),near(st.unit_over_w,U)&&near(st.unit_length,U*w));
 for(const b of p.points){const r=map[b.branch];for(let k=0;k<3;k++){
  const en=b.xyz_over_w[k],ep=w*en,ed=en/U;
  stats.max_normalized=Math.max(stats.max_normalized,Math.abs(r.xyz_over_w[k]-en));
  stats.max_physical=Math.max(stats.max_physical,Math.abs(r.xyz[k]-ep));
  stats.max_display=Math.max(stats.max_display,Math.abs(r.display_xyz[k]-ed));
  if(!near(r.xyz_over_w[k],en)||!near(r.xyz[k],ep)||!near(r.display_xyz[k],ed))throw Error('coordinate mismatch '+b.branch);
 }}
 check('all branch coordinates '+JSON.stringify(req),true);
 const event=['original','A','B'].includes(p.preset_id)?p.preset_id:null;
 check('event and overlays '+JSON.stringify(req),st.exact_event===event&&st.unique_count_certified===(event?18:null)&&st.groups.length===(event?18:42)&&Boolean(st.graph)===!!event&&Boolean(st.hull)===!!event);
 check('export provenance '+JSON.stringify(req),output.exact_event===event&&output.branches.length===42&&output.w===w&&output.selected_unit===unit&&Object.keys(output.source_identities).length>0);
}
for(const [mode,value,event] of [['C',1,'A'],['ell',1,'B'],['ell',0,'original']])check('exact length entry '+mode+value,g(data,{mode,value}).exact_event===event);
for(const mode of ['R','C','ell'])for(const direction of [-1,1]){
 const A=exp.find(p=>p.preset_id==='A').numeric;
 const v={R:A.R_over_w,C:1,ell:A.ell_over_w}[mode]+direction*1e-10;
 const st=g(data,{mode,value:v});check('near A '+mode+' '+direction,st.exact_event===null&&st.branch_marker_count===42&&st.unique_count_certified===null);
}
const invalid=[{preset:'A',w:0},{preset:'A',w:-1},{preset:'A',w:NaN},{preset:'A',w:Infinity},{mode:'R',value:.5},{mode:'R',value:Infinity},{mode:'R',value:NaN},{mode:'C',value:0},{mode:'C',value:-1},{mode:'ell',value:-1},{mode:'invalid',value:1},{preset:'bad'},{preset:'original',unit:'extension'}];
for(const r of invalid){let thrown=false;try{g(data,r)}catch(e){thrown=true;errors.push(e.message)}check('invalid '+String(r.mode||r.preset)+' '+String(r.value??r.w),thrown)}
for(const fn of ['BROWSER_EXPORT_A_w3_edge_unit.json','BROWSER_EXPORT_B.json']){
 const got=JSON.parse(fs.readFileSync(root+'/evidence/'+fn));
 const st=g(data,{preset:got.preset_id,w:got.w,unit:got.selected_unit});
 check('actual browser export '+fn,JSON.stringify(got)===JSON.stringify(x(st,data)));
}
// Log, but do not hide, representational boundary behavior on a typed radius.
const boundary=g(data,{mode:'R',value:data.geometry.rho});
const result={PASS:true,checks_passed:names.length,valid_preset_unit_scale_cases:count,near_event_cases:6,invalid_cases:invalid.length,stats,boundary_numeric_probe:{R_over_w:boundary.R_over_w,ell_over_w:boundary.ell_over_w,exact_event:boundary.exact_event,note:'Typed binary64 radius has no exact token; this is not an exact-radius input.'},checks:names};
fs.writeFileSync(out+'/INDEPENDENT_VIEWER_MATH.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({...result,checks:undefined},null,2));
