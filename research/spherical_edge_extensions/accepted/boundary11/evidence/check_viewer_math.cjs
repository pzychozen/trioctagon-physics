const fs=require('fs'),path=require('path'),assert=require('assert');
const root=path.resolve(__dirname,'..');
const data=JSON.parse(fs.readFileSync(path.join(root,'data/geometry_inventory.json')));
const examples=JSON.parse(fs.readFileSync(path.join(root,'data/numerical_display_examples.json')));
const {boundary11Geometry}=require(path.join(root,'viewer_math.js'));
const results=[];
for(const example of examples){
 const state=boundary11Geometry(data,example.R_over_w);
 const expected=data.coincidence_events.some(e=>Math.abs(e.R_over_w-example.R_over_w)<1e-13)?18:42;
 assert.strictEqual(state.groups.length,expected);assert.strictEqual(state.branches.length,42);
 let error=0;state.branches.forEach((b,k)=>b.xyz.forEach((x,c)=>{error=Math.max(error,Math.abs(x-example.points[Math.floor(k/2)][k%2][c]));}));
 assert(error<2e-15);
 results.push({R_over_w:example.R_over_w,unique_points:state.groups.length,coordinate_error_versus_python:error,pass:true});
}
assert.throws(()=>boundary11Geometry(data,0.5));assert.throws(()=>boundary11Geometry(data,NaN));
fs.writeFileSync(path.join(__dirname,'VIEWER_MATH_CHECKS.json'),JSON.stringify({checks:results,invalid_radius_rejected:true,pass:true},null,2)+'\n');
console.log(JSON.stringify({sample_radii:results.length,all_pass:true}));
