'use strict';
function boundary12Geometry(data, request) {
 const w=request.w===undefined?1:Number(request.w);
 if(!Number.isFinite(w)||w<=0)throw new Error('Panel width w must be positive and finite.');
 const h=data.presets.find(p=>p.id==='original').numeric.t_over_w, rho=data.geometry.rho;
 let t, R, event=null, preset=null;
 if(request.preset){
  preset=data.presets.find(p=>p.id===request.preset);
  if(!preset)throw new Error('Unknown fixed preset.');
  ({t_over_w:t,R_over_w:R}=preset.numeric);event=preset.exact_event;
 }else{
  const value=Number(request.value);
  if(!Number.isFinite(value))throw new Error('Enter a finite length ratio.');
  if(request.mode==='R'){
   if(value<rho)throw new Error('R/w must be at least the original vertex-sphere radius.');
   R=value;t=Math.sqrt((R-1/Math.sqrt(3))*(R+1/Math.sqrt(3)));
  }else if(request.mode==='C'){
   if(value<2*h)throw new Error('C/w cannot be shorter than the original edge.');
   t=value/2;R=Math.hypot(1/Math.sqrt(3),t);if(value===1)event='A';
  }else if(request.mode==='ell'){
   if(value<0)throw new Error('The added extension ell/w cannot be negative.');
   t=h+value;R=Math.hypot(1/Math.sqrt(3),t);if(value===0)event='original';if(value===1)event='B';
  }else throw new Error('Choose R, C or ell as the input quantity.');
 }
 const C=2*t,ell=t-h,unit=request.unit||'width';
 const UoverW={width:1,edge:2*h,chord:C,extension:ell}[unit];
 if(UoverW===undefined||!Number.isFinite(UoverW)||UoverW<=0)throw new Error('The per-end-extension unit is undefined when ell=0.');
 if(![t,R,C,ell,w*R,w*UoverW].every(Number.isFinite))throw new Error('This numeric scale exceeds the viewer range.');
 const exact=data.events[event]||null;
 const dotMap={};if(exact)for(let j=0;j<exact.groups.length;j++)for(const branch of exact.groups[j].branches)dotMap[branch]=`${event}:P${String(j+1).padStart(2,'0')}`;
 const branches=data.geometry.edges.flatMap(e=>[-1,1].map(sign=>{
  const id=e.id+(sign<0?'-':'+');
  const xyz_over_w=e.midpoint.map((m,k)=>m+sign*t*e.unit_direction[k]);
  return {branch:id,edge:e.id,sign,kind:e.class,original_endpoint:e.vertices[sign>0?1:0],dot_id:exact?dotMap[id]:'branch:'+id,
   xyz_over_w,xyz:xyz_over_w.map(x=>w*x),display_xyz:xyz_over_w.map(x=>x/UoverW)};
 }));
 const groups=exact?exact.groups.map((g,j)=>({dot_id:`${event}:P${String(j+1).padStart(2,'0')}`,xyz_over_w:g.coordinates,display_xyz:g.coordinates.map(x=>x/UoverW),branches:g.branches})):branches.map(b=>({dot_id:b.dot_id,xyz_over_w:b.xyz_over_w,display_xyz:b.display_xyz,branches:[b.branch]}));
 return {w,R_over_w:R,t_over_w:t,C_over_w:C,ell_over_w:ell,s_over_w:2*h,unit,unit_over_w:UoverW,unit_length:w*UoverW,
  exact_event:event,event_origin:event?(preset?'fixed exact preset':'exact input length identity'):null,preset_id:preset?preset.id:null,
  kind:preset?preset.kind:'custom length input',unique_count_certified:exact?18:null,branch_marker_count:groups.length,
  branches,groups,graph:exact?data.graphs[event]:null,hull:exact?data.hulls[event]:null};
}
function boundary12Export(state,data){return {schema:'BOUNDARY12 observation-only export v0.1',source_identities:data.source_identities,
 normalization:'Original centred coordinates divided by w; physical coordinates = w * xyz_over_w. Display units affect presentation only.',
 w:state.w,R_over_w:state.R_over_w,t_over_w:state.t_over_w,C_over_w:state.C_over_w,ell_over_w:state.ell_over_w,
 selected_unit:state.unit,unit_over_w:state.unit_over_w,preset_id:state.preset_id,exact_event:state.exact_event,event_origin:state.event_origin,
 unique_count_certified:state.unique_count_certified,display_grouping:state.exact_event?'accepted exact event IDs':'one marker per branch; no tolerance-based coincidence certification',
 branches:state.branches,unique_dots_if_exact_event:state.exact_event?state.groups:null,
 graph_file:state.exact_event?`data/graph_${state.exact_event}.json`:null,hull_file:state.exact_event?`data/hull_${state.exact_event}.json`:null};}
if(typeof module!=='undefined')module.exports={boundary12Geometry,boundary12Export};
