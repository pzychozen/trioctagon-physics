"""Atlas 02: independent exact algebra, no project imports or source writes.

Run after `conda activate torment`:
  python -B TRIOCTAGON_ATLAS_02_EXACT_CHECKS.py

Optional --integrity-dir attaches independently collected before/after file
inventories. Without it, mathematics still runs, but tree integrity is explicitly
NOT_CHECKED. Only the selected external JSON output is written. SymPy is required.
The analytic argument in the companion source packet gives the universal scope;
finite examples and falsifiers here are labelled separately.
"""
from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
import sympy as s

BASELINE = "0fa3b582c086e51371e8a784bc3dd145f88cfb2b"
ROOTS = {
    "current": Path(r"C:\TORMENT\TRIOCTAGON_new\trioctagon-physics"),
    "old": Path(r"C:\TORMENT\TRIOCTAGON_new\kernel_TO"),
    "torment_kernel": Path(r"C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric\torment_service\kernel"),
    "torment_checkout": Path(r"C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric"),
}
SOURCE_PATHS = {
    "A01": ROOTS["current"] / "kernel_physics/covering.py",
    "A02": ROOTS["current"] / "kernel_physics/dynamics.py",
    "A03": ROOTS["current"] / "papers/PAPER_A/publication/paper_A_publication.md",
    "A04": ROOTS["current"] / "papers/PAPER_A/PAPER_A_PROOF_AUDIT_v0.3.md",
    "A05": ROOTS["current"] / "kernel_physics/tests/test_covering.py",
    "A06": ROOTS["current"] / "papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md",
    "A07": ROOTS["current"] / "research_files/reconstruction/EXACT_3_12_24_STRUCTURE_v0.1.md",
    "A08": ROOTS["current"] / "research_files/reconstruction/CODEX_PHASE3V_PORTAL_AND_12RING_VERIFICATION_v0.1.md",
    "A09": ROOTS["current"] / "research_files/verification/paperA/paperA_proof_audit_v0_2.py",
    "A10": ROOTS["current"] / "kernel_physics/tests/parity_oracles/paper_a_oracle.py",
    "H01": ROOTS["old"] / "model_core.py",
    "H02": Path(r"C:\TORMENT\TRIOCTAGON_new\pdfs_old\TriOctagon_D24-CP-Octant-Ridge.pdf"),
    "H03": Path(r"C:\TORMENT\TRIOCTAGON_new\pdfs_old\TriOcta_violations.pdf"),
}


def clean(x):
    return s.simplify(s.expand_complex(x))


def matrix_equal(a, b):
    return a.shape == b.shape and all(clean(v) == 0 for v in a-b)


def shift(n, step=1):
    """Forward action on functions: (Tf)[a]=f[a+step mod n]."""
    return s.Matrix(n, n, lambda a, b: int(b == (a+step) % n))


def incidence_laplacian(n):
    """Independent graph definition: negative oriented incidence Gram matrix."""
    b = s.zeros(n)
    for edge in range(n):
        b[edge, edge] -= 1
        b[(edge+1) % n, edge] += 1
    return -b*b.T


def fourier(n, j):
    return s.Matrix([s.expand_complex(s.exp(2*s.pi*s.I*s.Rational(j*k, n)))
                     for k in range(n)])


def serial(value):
    if isinstance(value, s.MatrixBase):
        return [[str(clean(value[i,j])) for j in range(value.cols)]
                for i in range(value.rows)]
    if isinstance(value, s.Basic):
        return str(value)
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k):serial(v) for k,v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(v) for v in value]
    return value


def git_read(root, *args):
    return subprocess.check_output(
        ["git", "--no-optional-locks", "-C", str(root), *args],
        text=True, encoding="utf-8").strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name(
        "TRIOCTAGON_ATLAS_02_EXACT_RESULTS.json"))
    parser.add_argument("--integrity-dir", type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    for root in ROOTS.values():
        if output.is_relative_to(root.resolve()):
            raise ValueError("Output must be outside every protected source tree")

    checks = []
    def check(name, predicate, evidence, kind="EXACT_IDENTITY"):
        ok = bool(predicate)
        checks.append({"name":name, "passed":ok, "kind":kind,
                       "evidence":serial(evidence)})
        if not ok:
            raise AssertionError(name)

    head = git_read(ROOTS["current"], "rev-parse", "HEAD")
    check("frozen_current_baseline", head == BASELINE, head, "SOURCE_ATTESTATION")
    p = s.kronecker_product(s.ones(4,1), s.eye(3))
    q = p/2
    d3, d12 = incidence_laplacian(3), incidence_laplacian(12)
    l3 = s.ones(3)-3*s.eye(3)
    r, reflection, t = shift(12), s.Matrix(12,12,lambda a,b:int(b == (-a)%12)), shift(12,3)
    fibers = [[n for n in range(12) if n % 3 == a] for a in range(3)]
    check("fibers_four_preimages", fibers == [[0,3,6,9],[1,4,7,10],[2,5,8,11]], fibers)
    neighbor_residues = {n: sorted([((n-1)%12)%3, ((n+1)%12)%3]) for n in range(12)}
    check("covering_local_bijection_including_wrap", all(
        neighbor_residues[n] == sorted(set(range(3))-{n%3}) for n in range(12)), neighbor_residues)
    check("delta3_is_L3", d3 == l3, d3)
    check("incidence_matches_neighbor_laplacian", d12 == r+r.T-2*s.eye(12), d12)
    check("laplacian_intertwining", d12*p == p*d3, d12*p-p*d3)
    check("P_gram_and_rank", p.T*p == 4*s.eye(3) and p.rank() == 3,
          {"PstarP":p.T*p,"rank_complex":p.rank()})
    check("Q_isometry", q.T*q == s.eye(3), q.T*q)
    check("Q_compression", q.T*d12*q == d3, q.T*d12*q)
    check("unscaled_compression", p.T*d12*p == 4*d3, p.T*d12*p)
    projection = q*q.T
    check("sector_projector", projection*projection == projection and projection.T == projection,
          projection)
    check("sector_equals_deck_fixed_space", t*p == p and (t-s.eye(12)).nullspace().__len__() == 3,
          {"fixed_dimension_complex":3})
    check("deck_generator_order_four", t**4 == s.eye(12) and all(t**j != s.eye(12) for j in [1,2,3]),
          {"powers_on_vertex_zero":[0,3,6,9,0]})
    automorphisms = [(sign,a) for sign in (1,-1) for a in range(12)]
    deck = [(sign,a) for sign,a in automorphisms if all((sign*n+a)%3 == n%3 for n in range(12))]
    check("deck_is_exact_kernel_of_24_automorphisms", deck == [(1,0),(1,3),(1,6),(1,9)], deck)
    base_actions = {tuple((sign*n+a)%3 for n in range(3)) for sign,a in automorphisms}
    check("quotient_image_all_S3", len(base_actions) == 6, sorted(base_actions))
    check("dihedral_relations", reflection**2 == s.eye(12) and r**12 == s.eye(12)
          and reflection*r*reflection == r.T, "K^2=I, R^12=I, KRK=R^-1")
    check("base_actions_lift", r*p == p*shift(3) and reflection*p == p*s.Matrix(
        3,3,lambda a,b:int(b == (-a)%3)), "R P=P R3, K P=P K3")
    check("order_three_lift_not_deck", (r**4)**3 == s.eye(12) and r**4*p == p*shift(3)
          and r**4*p != p, "R^4 lifts the base +1 rotation; it is not fiber-preserving")
    a12=d12+2*s.eye(12)
    check("no_triangle_subgraph", s.trace(a12**3) == 0, "trace(A12^3)=0")

    modes=[fourier(12,j) for j in range(12)]
    f=s.Matrix.hstack(*modes)
    spectrum=[clean(2*s.cos(s.pi*j/6)-2) for j in range(12)]
    check("Fourier_complete_orthogonal_basis", matrix_equal(f.H*f,12*s.eye(12)), "F*F=12 I12")
    check("Fourier_Laplacian_spectrum", all(matrix_equal(d12*modes[j],spectrum[j]*modes[j])
          for j in range(12)), spectrum)
    check("Fourier_deck_characters", all(matrix_equal(t*modes[j],s.I**j*modes[j])
          for j in range(12)), {j:str(s.I**j) for j in range(12)})
    selected=[j for j in range(12) if s.I**j == 1]
    check("selected_modes_exactly_0_4_8", selected == [0,4,8], selected)
    check("base_Fourier_lift", all(matrix_equal(p*fourier(3,j),modes[4*j]) for j in range(3)),
          "P h_j = e_(4j) for unnormalized Fourier modes")
    check("normalized_Fourier_isometry", all(matrix_equal(q*fourier(3,j)/s.sqrt(3),
          modes[4*j]/s.sqrt(12)) for j in range(3)), "Q(h_j/sqrt3)=e_(4j)/sqrt12")
    u=s.Matrix([1,-1,0])/s.sqrt(2); v=s.Matrix([1,1,-2])/s.sqrt(6); common=s.ones(3,1)/s.sqrt(3)
    uv=s.Matrix.hstack(common,u,v)
    check("Paper_F_real_basis", matrix_equal(uv.T*uv,s.eye(3)) and matrix_equal(u.cross(v),common),
          {"u":u,"v":v,"ehat":common})
    coeff=(s.sqrt(3)-s.I)/(2*s.sqrt(2))
    check("Paper_F_to_complex_Fourier", matrix_equal(fourier(3,1)/s.sqrt(3),coeff*(u+s.I*v))
          and matrix_equal(fourier(3,2)/s.sqrt(3),s.conjugate(coeff)*(u-s.I*v)),
          {"h1_coefficient":coeff,"relation":"h1=coefficient*(u+i v); h2=conjugate(h1)"})
    check("lifted_Paper_F_vectors_are_tangent_to_sector", (s.eye(12)-projection)*q*u == s.zeros(12,1)
          and (s.eye(12)-projection)*q*v == s.zeros(12,1), "Q u and Q v lie in V3, not its normal complement")

    # A coordinate basis for the entire nine-complex-dimensional complement.
    b2=s.Matrix([1,-1,1,-1])/2
    bc=s.Matrix([1,0,-1,0])/s.sqrt(2)
    bs=s.Matrix([0,1,0,-1])/s.sqrt(2)
    normal=s.kronecker_product(s.Matrix.hstack(b2,bc,bs),s.eye(3))
    check("normal_coordinate_basis", matrix_equal(normal.H*normal,s.eye(9))
          and matrix_equal(normal*normal.H,s.eye(12)-projection) and p.T*normal == s.zeros(3,9),
          {"sheet_vectors":[b2,bc,bs],"complex_dimension":9,"real_dimension":18})
    e0=(s.eye(12)+t+t**2+t**3)/4
    e2=(s.eye(12)-t+t**2-t**3)/4
    e13=s.eye(12)-e0-e2
    projectors=[e0,e2,e13]
    check("deck_projectors_orthogonal_complete", all(e*e == e and e.T == e for e in projectors)
          and all(projectors[i]*projectors[j] == s.zeros(12) for i in range(3) for j in range(i))
          and sum(projectors,s.zeros(12)) == s.eye(12), "E0+E2+E13=I; pairwise orthogonal")
    check("deck_fixed_projector_equals_fiber_average", e0 == projection, e0)
    real_projectors=[s.diag(e,e) for e in projectors]
    check("real_deck_ranks_6_6_12", [e.rank() for e in real_projectors] == [6,6,12],
          {"real_ranks":[e.rank() for e in real_projectors],"realification_order":"all x, then all y"})
    check("deck_sector_mode_membership", all(matrix_equal(
        projectors[0 if j%4==0 else 1 if j%4==2 else 2]*modes[j],modes[j]) for j in range(12)),
        {"U0":[0,4,8],"U2":[2,6,10],"U13":[1,3,5,7,9,11]})

    # Exact universal polynomial-stage and phase-stage identities, separate from
    # phase-chart differentiability. No float comparisons and no model imports.
    x=s.symbols('x0:3',real=True); y=s.symbols('y0:3',real=True)
    k=s.symbols('k0:3',real=True); eps,g,lam=s.symbols('eps g lam',real=True)
    omega=s.Matrix([x[j]+s.I*y[j] for j in range(3)])
    def onsite(state,coeffs):
        return s.Matrix([z+eps*z*(coeffs[j]-z*s.conjugate(z)) for j,z in enumerate(state)])
    pre3=(onsite(omega,k)+g*d3*omega).applyfunc(s.expand)
    pre12=(onsite(p*omega,list(p*s.Matrix(k)))+g*d12*p*omega).applyfunc(s.expand)
    check("nonlinear_presync_polynomial_identity", matrix_equal(pre12,p*pre3),
          "Symbolic in six real state coordinates, eps, g and k0,k1,k2")
    arg0=s.Function('Arg0')
    check("formal_phase_extraction_commutes_with_repetition", pre12.applyfunc(arg0) == p*pre3.applyfunc(arg0),
          "Identical input expressions receive the same deterministic scalar Arg0, including zero by convention")
    phase=s.symbols('p0:3',real=True); radii=s.symbols('r0:3',nonnegative=True)
    def phase_field(phases):
        n=len(phases)
        return s.Matrix([s.sin(3*(phases[(j-1)%n]-phases[j]))+
                         s.sin(3*(phases[(j+1)%n]-phases[j])) for j in range(n)])
    h3=phase_field(phase); h12=phase_field(list(p*s.Matrix(phase)))
    check("nonlinear_phase_field_identity", matrix_equal(h12,p*h3), h3)
    phase_out3=s.Matrix([radii[j]*s.exp(s.I*(phase[j]+lam*h3[j])) for j in range(3)])
    phase_out12=s.Matrix([radii[j%3]*s.exp(s.I*(phase[j%3]+lam*h12[j])) for j in range(12)])
    check("nonlinear_phase_reconstruction_identity", phase_out12 == p*phase_out3,
          "Exact expression identity for arbitrary nonnegative radii and shared phase representatives")
    zero_checks=[]
    for mask in range(8):
        subs={z:0 for j in range(3) if mask & (1<<j) for z in (radii[j],phase[j])}
        zero_checks.append(phase_out12.subs(subs) == p*phase_out3.subs(subs))
    check("all_eight_zero_support_patterns", all(zero_checks),
          {"patterns":8,"passed":zero_checks,"zero_rule":"r_j=0 and Arg0=0 at identical residue copies"})
    check("lambda_zero_identity", all(s.simplify(h)==0 for h in (
        phase_out3.subs(lam,0)-s.Matrix([radii[j]*s.exp(s.I*phase[j]) for j in range(3)]))),
          "Implementation directly returns the pre-sync vector for lambda=0; expression agrees exactly")

    offx=s.symbols('X0:12',real=True); offy=s.symbols('Y0:12',real=True)
    off=s.Matrix([offx[j]+s.I*offy[j] for j in range(12)])
    periodic_k=list(p*s.Matrix(k))
    off_pre=onsite(off,periodic_k)+g*d12*off
    shifted_pre=onsite(t*off,periodic_k)+g*d12*t*off
    check("global_deck_equivariance_presync", (shifted_pre-t*off_pre).applyfunc(s.expand)==s.zeros(12,1),
          "Exact polynomial identity at arbitrary off-sector states with three-periodic k")
    offp=s.Matrix(s.symbols('theta0:12',real=True))
    offr=s.Matrix(s.symbols('rho0:12',nonnegative=True))
    def polar_update(radius,ph):
        field=phase_field(ph)
        return s.Matrix([radius[j]*s.exp(s.I*(ph[j]+lam*field[j])) for j in range(12)])
    check("global_deck_equivariance_phase", polar_update(t*offr,t*offp)==t*polar_update(offr,offp),
          "Exact phase-expression identity under the site permutation; common Arg0 preserves it at zeros")
    unequal_k_output=p*s.Matrix([1,s.Rational(3,2),2])
    check("full_rotation_symmetry_not_implied_for_unequal_k", r*unequal_k_output != unequal_k_output,
          {"input":"all ones (rotation-fixed)","eps":"1/2","g":0,"lambda":0,"k":[1,2,3],
           "output":unequal_k_output},"EXACT_COUNTEREXAMPLE")

    # Falsifiers delimit the theorem rather than asserting that every violating
    # parameter/state must fail (degenerate cases can agree accidentally).
    kbad=s.ones(12,1); kbad[0]=2
    bad=s.ones(12,1)+s.Rational(1,2)*(kbad-s.ones(12,1))
    check("nonperiodic_k_can_break_sector", (s.eye(12)-projection)*bad != s.zeros(12,1),
          {"input":"all ones","eps":"1/2","g":0,"lambda":0,"k":"all ones except k[0]=2","output":bad},
          "EXACT_COUNTEREXAMPLE")
    # Q is the right linear isometry but not the same nonlinear intertwiner.
    unit=s.Matrix([1,0,0]); qunit=q*unit
    nonlinear_q=s.Matrix([z-z**3 for z in qunit])
    check("Q_does_not_replace_P_in_cubic_map", nonlinear_q != s.zeros(12,1)
          and nonlinear_q == p*s.Matrix([s.Rational(3,8),0,0]),
          {"eps":1,"g":0,"lambda":0,"k":[0,0,0],"F3_input":[1,0,0],
           "Q_F3":s.zeros(12,1),"F12_Q_input":nonlinear_q},"EXACT_COUNTEREXAMPLE")
    allpairs=s.Matrix([sum(s.sin(3*(phase[j%3]-phase[n%3])) for j in range(12)) for n in range(12)])
    check("all_pairs_on_12_has_wrong_multiplicity", matrix_equal(allpairs,4*p*h3),
          "Unweighted all-pairs ring drift would be 4 times the adopted base drift on lifted states",
          "EXACT_COUNTEREXAMPLE")
    def sequential(phases):
        phases=list(phases)
        for j in range(len(phases)):
            inc=s.sin(3*(phases[(j-1)%len(phases)]-phases[j]))+s.sin(3*(phases[(j+1)%len(phases)]-phases[j]))
            phases[j]=s.simplify(phases[j]+s.pi*inc/6)
        return s.Matrix(phases)
    seqbase=sequential([0,s.pi/6,0]); seqring=sequential([0,s.pi/6,0]*4)
    seqout=seqring.applyfunc(lambda z:s.expand_complex(s.exp(s.I*z)))
    check("in_place_sweep_can_break_intertwining", seqout != p*seqbase.applyfunc(lambda z:s.expand_complex(s.exp(s.I*z)))
          and (s.eye(12)-projection)*seqout != s.zeros(12,1),
          {"initial_phases":[0,s.pi/6,0],"lambda":s.pi/6,"base_final_phases":seqbase,
           "ring_final_phases":seqring},"EXACT_COUNTEREXAMPLE")
    mixed=[0]*12; mixed[0]=s.pi/6
    mixed_h=phase_field(mixed)
    mixed_out=s.Matrix([0 if j%3==0 else s.expand_complex(s.exp(s.I*s.pi*mixed_h[j]/2)) for j in range(12)])
    check("inconsistent_zero_phase_can_break_sector", (s.eye(12)-projection)*mixed_out != s.zeros(12,1),
          {"pre_sync":"P(0,1,1)","bad_rule":"assign pi/6 at zero site 0, zero at its other copies",
           "lambda":s.pi/2,"output":mixed_out},"EXACT_COUNTEREXAMPLE")

    # An exact derivative at the homogeneous unit fixed point (k=(1,1,1)).
    # This is not the paper's heterogeneous canonical-k numerical atlas.
    jrad=(1-2*eps)*s.eye(12)+g*d12
    jphase=(s.eye(12)+3*lam*d12)*(s.eye(12)+g*d12)
    jac=s.diag(jrad,jphase); tr=s.diag(t,t)
    check("homogeneous_jacobian_deck_commutation", jac*tr == tr*jac,
          {"state":"all ones, k=(1,1,1)","radial":"(1-2 eps)I+g Delta12",
           "phase":"(I+3 lambda Delta12)(I+g Delta12)"},"EXACT_SPECIAL_CASE")
    check("homogeneous_jacobian_no_cross_block_leakage", all(
        (real_projectors[i]*jac*real_projectors[j]).applyfunc(s.expand) == s.zeros(24)
        for i in range(3) for j in range(3) if i!=j), "All E_i J E_j vanish for i != j", "EXACT_SPECIAL_CASE")
    eta=modes[1]/s.sqrt(12)
    d_eta=s.Rational(19,20)*eta-s.Rational(1,20)*s.conjugate(eta)
    char3=sum([s.I**(-3*j)*t**j for j in range(4)],s.zeros(12))/4
    leaked=char3*d_eta
    check("real_linear_derivative_can_mix_i_and_minus_i", matrix_equal(leaked,-s.conjugate(eta)/20)
          and clean((leaked.H*leaked)[0]) == s.Rational(1,400),
          {"eps":"1/20","g":0,"lambda":0,"state":"all ones, k=(1,1,1)",
           "physical_complex_character3_component_norm":"1/20"},"EXACT_SPECIAL_CASE")
    check("invariance_is_not_global_attraction", matrix_equal((s.eye(12)+d12)*modes[6],-3*modes[6]),
          {"eps":0,"g":1,"lambda":0,"normal_mode":6,"gain":-3},"EXACT_COUNTEREXAMPLE")

    # Current algebra permits a 24->12->3 tower. This check confers no historical
    # identification on an old D24 angular/perimeter construction.
    p24_12=s.kronecker_product(s.ones(2,1),s.eye(12))
    p24_3=s.kronecker_product(s.ones(8,1),s.eye(3))
    check("explicit_current_covering_tower", p24_12*p == p24_3 and
          incidence_laplacian(24)*p24_12 == p24_12*d12,
          "Current abstract maps n mod 12 then n mod 3; historical D24 identification not asserted")

    parsed=ast.parse(SOURCE_PATHS['A02'].read_text(encoding='utf-8'))
    source_l3=next(ast.literal_eval(node.value) for node in parsed.body if isinstance(node,ast.Assign)
                   and any(isinstance(target,ast.Name) and target.id=='L3' for target in node.targets))
    check("source_L3_literal_matches_independent_matrix", s.Matrix(source_l3) == l3,
          source_l3,"SOURCE_ATTESTATION")

    integrity={"status":"NOT_CHECKED", "note":"Run with --integrity-dir to attach full before/after inventories."}
    if args.integrity_dir:
        before=json.loads((args.integrity_dir/'before.json').read_text(encoding='utf-8'))
        after=json.loads((args.integrity_dir/'after.json').read_text(encoding='utf-8'))
        assert set(before)==set(after)==set(ROOTS)
        scopes={}
        for name in ROOTS:
            old,new=before[name],after[name]
            assert Path(old['root']).resolve()==ROOTS[name].resolve()==Path(new['root']).resolve()
            before_digest=hashlib.sha256(json.dumps(old['files'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
            after_digest=hashlib.sha256(json.dumps(new['files'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
            check('integrity_'+name, old['files']==new['files'] and before_digest==old['tree_sha256']
                  and after_digest==new['tree_sha256'], {"before":before_digest,"after":after_digest},"INTEGRITY_ATTESTATION")
            scopes[name]={"root":str(ROOTS[name]),"before_count":old['count'],"after_count":new['count'],
                          "before_sha256":before_digest,"after_sha256":after_digest,
                          "before_start_utc":old['start_utc'],"before_end_utc":old['end_utc'],
                          "after_start_utc":new['start_utc'],"after_end_utc":new['end_utc'],
                          "added":0,"removed":0,"modified":0}
        integrity={"status":"PASS","method":"All regular-file bytes, root-relative POSIX paths, excluding .git; sorted compact JSON path-to-file-SHA256 dictionary then SHA256",
                   "scopes":scopes,"full_inventories":str(args.integrity_dir),
                   "CURRENT_REPO_CHANGED":"NO","OLD_KERNEL_CHANGED":"NO","TORMENT_CHANGED":"NO",
                   "COMMITS":0,"PUSHES":0}
    git_state={name:{"head":git_read(ROOTS[name],'rev-parse','HEAD'),
                     "tracked_status":git_read(ROOTS[name],'status','--porcelain','--untracked-files=no')}
               for name in ['current','torment_checkout']}
    check("current_HEAD_still_frozen", git_state['current']['head']==BASELINE,git_state,'SOURCE_ATTESTATION')
    registry={sid:{"path":str(path),"sha256":hashlib.sha256(path.read_bytes()).hexdigest()}
              for sid,path in SOURCE_PATHS.items()}
    result={"task":"TRIOCTAGON_MATHEMATICAL_ATLAS_ENTRY_02","version":"0.1",
            "generated_utc":datetime.now(timezone.utc).isoformat(),"status":"PASS",
            "baseline":BASELINE,"python":sys.version,"interpreter":sys.executable,"sympy":s.__version__,
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "method":"Independent incidence matrices, exact radicals, symbolic polynomial/trigonometric identities; no project imports, no tolerance-based tests",
            "check_count":len(checks),"checks":checks,
            "artifacts":{"P":serial(p),"Q":serial(q),"Delta3":serial(d3),"Delta12":serial(d12),
                         "fibers":fibers,"fourier_modes_kept":selected,
                         "complement_modes":[j for j in range(12) if j not in selected],
                         "spectrum_by_mode":serial(spectrum),"normal_basis":serial(normal)},
            "source_register":registry,"git_state":git_state,"integrity":integrity,
            "limits":["No new numerical Floquet atlas or global attraction proof.",
                      "Symbolic phase identities are supplemented by the source packet's deterministic-zero proof; smoothness at zero is not asserted.",
                      "Finite graph/falsifier checks do not replace the analytic proofs for general M.",
                      "Historical comparisons confer no provenance or old/new model identity."]}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({"status":"PASS","check_count":len(checks),"output":str(output),
                      "integrity":integrity['status']},ensure_ascii=False))


if __name__ == '__main__':
    main()
