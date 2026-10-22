"""Independent scalar arithmetic on saved rows; no model execution."""
from pathlib import Path
import ast,csv,hashlib,inspect,json,math,platform
import matplotlib
from matplotlib import animation
ROOT=Path(__file__).resolve().parents[1]
TOL=1e-12
def norm(v):return math.sqrt(math.fsum(t*t for t in v))
def H(t):return 2*math.exp(-.5*t)*math.cos(t)+math.exp(-.3*t)*math.sin(t)+1.5*math.exp(-.7*t)+math.exp(-.4*t)
def D(t):return (t+5)%10-5
result={}
for label,filename,n_expected in [
    ("A","PLOT_1_tetrahedral_states_20250712_015421.csv",1092),
    ("B","tetrahedral_states_20250712_015647.csv",440),
]:
    with (ROOT/"originals"/filename).open(newline="") as f:rows=list(csv.DictReader(f))
    assert len(rows)==8*n_expected
    blocks=[rows[k:k+8] for k in range(0,len(rows),8)]
    Eerr=0.;Perr=0.;Gerr=0.;Verr=0.
    sample=list(range(1,6))+list(range(len(blocks)-5,len(blocks)))
    for q,block in enumerate(blocks):
        assert [int(r["Tetrahedron"]) for r in block]==list(range(8))
        V=[[float(r[k]) for k in ("VX","VY","VZ")] for r in block]
        K=.5*math.fsum(t*t for vec in V for t in vec)
        Eerr=max(Eerr,abs(K-float(block[0]["Energy"])))
        if q==0:continue
        old=blocks[q-1]
        X0=[[float(r[k]) for k in ("X","Y","Z")] for r in old]
        X1=[[float(r[k]) for k in ("X","Y","Z")] for r in block]
        V0=[[float(r[k]) for k in ("VX","VY","VZ")] for r in old]
        g=1/(1+math.fsum(norm(vec) for vec in V0)/8)
        Gerr=max(Gerr,abs(g-float(block[0]["GRF"])))
        for i in range(8):
            for k in range(3):
                Perr=max(Perr,abs(D(X1[i][k]-(X0[i][k]+.1*V[i][k])%10)))
        if q not in sample:continue
        h=H(.1*int(block[0]["Step"]))
        for i in range(8):
            center=[math.fsum(X1[j][k] if j<i else X0[j][k] for j in range(8))/8 for k in range(3)]
            d=[D(center[k]-X0[i][k]) for k in range(3)]
            sign=1-2*int(block[i]["Rule_State"])
            for k in range(3):
                u=V0[i][k]+.1*g*h*sign*d[k]/(norm(d)+.01)
                rhs=u/(1+math.log1p(abs(u)))
                Verr=max(Verr,abs(V[i][k]-rhs))
    assert max(Eerr,Perr,Gerr,Verr)<TOL
    result[label]={"callbacks":len(blocks),"R0_sample_callbacks":sample,
        "all_energy_max_residual":Eerr,"all_position_max_residual":Perr,
        "all_GRF_max_residual":Gerr,"sample_velocity_max_residual":Verr,
        "absolute_tolerance":TOL}
raw=(ROOT/"originals/plot_1.py").read_bytes()
tree=ast.parse(raw.decode("utf-8-sig"))
other_path=ROOT/"originals/3Dtriangles.py"
other=ast.parse(other_path.read_text(encoding="utf-8-sig"))
def body(t,name):
    node=next(n for n in t.body if isinstance(n,ast.FunctionDef) and n.name==name)
    lines=node.body
    if isinstance(lines[0],ast.Expr) and isinstance(lines[0].value,ast.Constant):
        lines=lines[1:]
    return [ast.dump(n,include_attributes=False) for n in lines]
same={n:body(tree,n)==body(other,n) for n in ("H","RPCO","GRF")}
assert all(same.values())
lib=Path(inspect.getsourcefile(animation))
targets=[animation.Animation._start,animation.Animation.save,
         animation.TimedAnimation.__init__,animation.TimedAnimation._step,
         animation.FuncAnimation.__init__,animation.FuncAnimation._init_draw]
chunks=[]
for obj in targets:
    lines,start=inspect.getsourcelines(obj)
    chunks.append(f"\n{obj.__qualname__} — {lib}:{start}\n")
    chunks.extend(f"{start+i}: {line}" for i,line in enumerate(lines))
(ROOT/"inspection/matplotlib_callback_excerpts.txt").write_text("".join(chunks),encoding="utf-8")
result["static"]={"same_H_RPCO_GRF_as_simulation_02":same,
    "plot1_lines":len(raw.splitlines()),"plot1_sha256":hashlib.sha256(raw).hexdigest(),
    "matplotlib":matplotlib.__version__,"library_source":str(lib),
    "library_source_sha256":hashlib.sha256(lib.read_bytes()).hexdigest(),
    "python":platform.python_version()}
result["scope"]="Independent stdlib csv/math checks of observed states, plus AST/library inspection. No historical imports, random calls or calculated-state propagation."
(ROOT/"analysis/independent_checks.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(result,indent=2))
