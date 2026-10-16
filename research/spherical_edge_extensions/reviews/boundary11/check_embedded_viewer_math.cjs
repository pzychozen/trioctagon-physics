// Reviewer-written bounded check of the exact pure evaluator embedded in the HTML.
// No DOM, network, engine, or archived Python scientific scripts are executed.
'use strict';
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const base='/mnt/data/boundary11_submission/',out='/mnt/data/BOUNDARY11_GPT_REVIEW_v0.1/';
const html=fs.readFileSync(base+'BOUNDARY11_VIEWER.html','utf8').replace(/\r\n/g,'\n');
const pure=fs.readFileSync(base+'viewer_math.js','utf8').replace(/\r\n/g,'\n');
assert(html.includes(pure));
const start=html.indexOf('const boundaryData=')+'const boundaryData='.length;
const stop=html.indexOf(';\n',start);
const data=JSON.parse(html.slice(start,stop));
const inventory=JSON.parse(fs.readFileSync(base+'data/geometry_inventory.json','utf8'));
assert.deepStrictEqual(data,inventory);
const context={module:{exports:{}},Math,Number};vm.createContext(context);
vm.runInContext(pure,context,{timeout:3000});
const fn=context.module.exports.boundary11Geometry;
const examples=JSON.parse(fs.readFileSync(base+'data/numerical_display_examples.json','utf8'));
let err=0;const rows=[];
for(const ex of examples){
 const result=fn(data,ex.R_over_w),expected=ex.points.flat();
 assert.strictEqual(result.branches.length,42);assert.strictEqual(result.radial.length,18);
 for(let i=0;i<42;i++)for(let j=0;j<3;j++)err=Math.max(err,Math.abs(result.branches[i].xyz[j]-expected[i][j]));
 const event=data.coincidence_events.some(e=>e.R_over_w===ex.R_over_w);
 assert.strictEqual(result.groups.length,event?18:42);
 rows.push({R_over_w:ex.R_over_w,labelled_points:42,unique_display_groups:result.groups.length});
}
assert(err<2e-15);
assert.throws(()=>fn(data,0.5));assert.throws(()=>fn(data,Infinity));
assert.strictEqual(fn(data,10).groups.length,42);
const result={status:'PASS',embedded_function_identical_after_CRLF_LF_normalization:true,embedded_data_equal_to_verified_inventory:true,test_radii:rows,max_coordinate_error:err,invalid_radius_rejection:true,custom_R10_count:42,scope:'Pure JS evaluator only. This does not independently exercise browser rendering or controls.'};
fs.writeFileSync(out+'INDEPENDENT_VIEWER_MATH.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));
