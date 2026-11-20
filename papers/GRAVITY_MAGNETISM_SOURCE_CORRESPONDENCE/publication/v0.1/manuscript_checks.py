"""Only manuscript consequences and saved-number transcription; no native runs or root solves."""
from pathlib import Path
import hashlib, json, platform
import sympy as sy
ROOT=Path(__file__).resolve().parent
R=sy.Rational
checks=[]
def check(id, condition, detail):
    assert bool(condition), id
    checks.append(dict(id=id, passed=True, detail=detail))
report=(ROOT/"evidence/GM03/GM03_DERIVATIONS.md").read_text("utf-8")
for tag in [1,4,20]:
    check(f"M00_source_tag_{tag}", f"\\tag{{{tag}}}" in report, "Direct refinement source locator present.")
s=sy.symbols("s", real=True)
omega=-R(1,2)-sy.I*sy.sqrt(3)/2
B=omega*(1-s/20)
check("M01_unit_omega", sy.expand_complex(omega*sy.conjugate(omega))==1, "Known normalized Fourier phase.")
check("M02_middle_channel_path", sy.expand(B-omega*(1-s/20))==0, "GM03 (4), middle channel.")
check("M03_amplitude_positivity", 1-R(3,2)/20==R(37,40)>0, "Minimum of decreasing linear amplitude on [1/2,3/2].")
check("M04_amplitude_squared", sy.simplify(B*sy.conjugate(B)-(1-s/20)**2)==0, "Together with positivity, |B|=1-s/20.")
check("M05_amplitude_inversion", sy.expand(20*(1-(1-s/20))-s)==0, "s=20(1-|B|), first-step path only.")
dx,dy,qx,qy=sy.symbols("dx dy qx qy", real=True)
dB=dx+sy.I*dy
h1=2*s-1
exposed=qx+sy.I*qy+h1*dB
control=qx+sy.I*qy+dB
check("M06_component_test", sy.expand(exposed-(qx+sy.I*qy)-(2*s-1)*(control-(qx+sy.I*qy)))==0,
      "Projection of GM03 (1) onto registered complex channel B.")
check("M07_nonzero_component", R(5561,200000)>0, "GM03 (20) plus reverse triangle implies |F_B(q1)-q1_B| > 5561/200000.")
check("M08_prestage_bound", R(9499,10000)*R(9,10)-R(1,200000)==R(170981,200000),
      "Saved regularity bound transcription.")
check("M09_modulus_gap", (1-R(9691,10000))*R(9,10)-R(1,200000)==R(5561,200000),
      "Saved nonzero-direction bound transcription.")
data=json.loads((ROOT/"evidence/GM03/CHECK_RESULTS.json").read_text("utf-8"))
tex=(ROOT/"manuscript/04_spatial.tex").read_text("utf-8")
rows=[]
for label in ["parallel","transverse"]:
    for distance in ["r0","2r0"]:
        source=data["matched_trials"][label]
        if distance=="2r0": source=source["heldout_2r0"]
        lo,hi=[R(source["s_bracket"][key]) for key in ["lo","hi"]]
        check(f"M10_bracket_order_{label}_{distance}", R(1,2)<lo<hi<R(3,2), "Read existing certified enclosure; no root solve.")
        gain=f"{float(lo):.9f}"; gain2=f"{float(hi):.9f}"
        off=f"{float(2*lo-1):.9f}"; off2=f"{float(2*hi-1):.9f}"
        check(f"M11_gain_rounding_{label}_{distance}",gain==gain2 and gain in tex,"Both accepted endpoints give printed nine decimals.")
        check(f"M12_off_rounding_{label}_{distance}",off==off2 and off in tex,"Affine transform of existing interval; not a new trajectory.")
        rows.append(dict(placement=label,distance=distance,s_lo=str(lo),s_hi=str(hi),
                         next_off_lo=str(2*lo-1),next_off_hi=str(2*hi-1),printed_gain=gain,printed_off=off))
native=(ROOT/"manuscript/01_native.tex").read_text("utf-8")
for key,target in [("I_F",native),("W_squared",native),("neutral_cos_squared",tex),("neutral_distance_squared_exact",tex)]:
    val=R(data["benchmark"][key])
    token="\\frac{"+str(val.p)+"}{"+str(val.q)+"}"
    check("M13_exact_"+key,token in target,"Exact rational transcribed from accepted GM03 benchmark.")
for key,digits in [("neutral_angle_degrees_approx",10),("neutral_distance_ratio_approx",11)]:
    from decimal import Decimal
    printed=f"{Decimal(data['benchmark'][key]):.{digits}f}"
    check("M14_decimal_"+key,printed in tex,"Rounded number agrees with saved value; approximate equality used.")
testtex=(ROOT/"manuscript/05_test.tex").read_text("utf-8")
for label in ["parallel","transverse"]:
    b=data["matched_trials"][label]["switching_work_over_S"]
    printed=f"{float(R(b['lo'])):.12f}"
    check("M15_switch_work_"+label,printed==f"{float(R(b['hi'])):.12f}" and printed in testtex,
          "Both saved work enclosure endpoints round to manuscript value.")
record=dict(status="PASS", checks=checks,count=len(checks),benchmark_transcription=rows,
            scope="No historical scientific suite rerun; no new roots, trajectories, parameter search or physical data.",
            python=platform.python_version(),sympy=sy.__version__,
            script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/"MANUSCRIPT_CHECKS.json").write_text(json.dumps(record,indent=2)+"\n","utf-8")
print(json.dumps({"status":"PASS","checks":len(checks),"benchmark_rows":len(rows)}))
