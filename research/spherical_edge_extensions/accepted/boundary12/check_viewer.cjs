const fs=require('fs'),assert=require('assert'),vm=require('vm'),path=require('path');
const root=__dirname,data=JSON.parse(fs.readFileSync(path.join(root,'data/viewer_data.json'))),fixtures=JSON.parse(fs.readFileSync(path.join(root,'data/fixed_presets.json')));
const {boundary12Geometry:calc,boundary12Export:exp}=require('./viewer_math.js');
const checks=[],rows=[];let maxError=0;
function check(name,condition){assert(condition,name);checks.push(name);}
for(const p of fixtures){
 const s=calc(data,{preset:p.id,w:1,unit:'width'});check(p.id+' labels/count',s.branches.length===42&&s.groups.length===p.unique_point_count&&s.exact_event===p.exact_event);
 let err=0;for(let i=0;i<42;i++)for(let j=0;j<3;j++)err=Math.max(err,Math.abs(s.branches[i].xyz_over_w[j]-p.points[i].xyz[j]));
 maxError=Math.max(maxError,err);check(p.id+' independent Python coordinates',err<2e-14);
 for(const key of ['R_over_w','t_over_w','C_over_w','ell_over_w'])check(p.id+' '+key,Math.abs(s[key]-p.numeric[key])<2e-14);
 const payload=exp(s,data);check(p.id+' export labels retained',new Set(payload.branches.map(b=>b.branch)).size===42&&payload.exact_event===p.exact_event);
 if(p.exact_event)check(p.id+' graph/hull overlay',!!s.graph&&!!s.hull&&s.hull.V===18);else check(p.id+' no invented graph/hull',s.graph===null&&s.hull===null);
 for(const unit of ['width','edge','chord','extension']){
  if(unit==='extension'&&p.id==='original'){assert.throws(()=>calc(data,{preset:p.id,w:1,unit}));continue;}
  const u=calc(data,{preset:p.id,w:3,unit});check(p.id+' similarity/unit '+unit,u.branches.every((b,i)=>b.xyz_over_w.every((x,j)=>x===s.branches[i].xyz_over_w[j])&&b.xyz.every((x,j)=>x===3*s.branches[i].xyz_over_w[j])));
 }
 rows.push({preset:p.id,event:s.exact_event,count:s.groups.length,maximum_coordinate_error:err});
}
for(const w of [0,-1,Infinity,NaN]){assert.throws(()=>calc(data,{preset:'A',w}));checks.push('reject width '+String(w));}
for(const value of [0.5,-1,Infinity,NaN]){assert.throws(()=>calc(data,{mode:'R',value,w:1}));checks.push('reject R '+String(value));}
for(const [mode,value] of [['C',0],['ell',-1],['C',Infinity],['ell',NaN]]){assert.throws(()=>calc(data,{mode,value}));checks.push('reject '+mode+' '+String(value));}
for(const p of fixtures.filter(p=>p.exact_event))for(const delta of [-1e-10,1e-10,-1e-13,1e-13]){
 const r=p.numeric.R_over_w+delta;
 if(p.id==='original'&&delta<0){assert.throws(()=>calc(data,{mode:'R',value:r}));checks.push('below original sphere rejected '+delta);continue;}
 const s=calc(data,{mode:'R',value:r});check(p.id+' nearby '+delta+' never tagged as exact',s.exact_event===null&&s.groups.length===42&&s.unique_count_certified===null);
}
for(const [mode,value,event] of [['C',1,'A'],['ell',1,'B'],['ell',0,'original']])check('input length identity '+mode+'='+value,calc(data,{mode,value}).exact_event===event);
// Read embedded new code, not the accepted upstream evaluator, and test the actual packaged program body.
const html=fs.readFileSync(path.join(root,'BOUNDARY12_VIEWER.html'),'utf8').replace(/\r\n/g,'\n');
const math=fs.readFileSync(path.join(root,'viewer_math.js'),'utf8').replace(/\r\n/g,'\n');check('same math embedded',html.includes(math));
const embedded=html.slice(html.lastIndexOf('<script>const data=')+8,html.lastIndexOf('</script>'));
const start=embedded.indexOf('const data=')+'const data='.length,end=embedded.indexOf(';\n\'use strict\';');
check('embedded data exact',JSON.stringify(JSON.parse(embedded.slice(start,end)))===JSON.stringify(data));
const sandbox={module:{exports:{}}};vm.runInNewContext(math,sandbox);check('embedded evaluator executable',sandbox.module.exports.boundary12Geometry(data,{preset:'B'}).groups.length===18);
check('no external script dependency',!/<script[^>]+src=/.test(html));
const result={pass:true,checks_passed:checks.length,checks,presets:rows,max_coordinate_error:maxError,scope:'Seven fixed presets, deterministic validation and near-event cases; no trajectories, RNG or old checker execution'};
fs.writeFileSync(path.join(root,'evidence/VIEWER_CHECKS.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({pass:true,checks:checks.length,max_coordinate_error:maxError}));
