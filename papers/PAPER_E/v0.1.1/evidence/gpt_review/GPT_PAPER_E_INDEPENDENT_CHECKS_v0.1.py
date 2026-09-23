#!/usr/bin/env python3
"""Independent, bounded supporting checks for Paper E v0.1.

This script checks mathematical transcriptions and selected already-uploaded
source bodies. It does not import or execute either historical or modern kernel,
launch the viewer, rerun Codex's suite, or certify the publication package.

Usage:
    python GPT_PAPER_E_INDEPENDENT_CHECKS_v0.1.py --output results.json
Optional:
    --source-dir DIRECTORY  # contains original geometry_*.py and viewer upload

Requires SymPy and NumPy. No network, plotting, or package installation.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
import platform
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import sympy as sp


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entries(expr: Any) -> list[Any]:
    if isinstance(expr, sp.MatrixBase):
        return list(expr)
    if isinstance(expr, (list, tuple)):
        out: list[Any] = []
        for x in expr:
            out.extend(entries(x))
        return out
    return [expr]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('GPT_PAPER_E_INDEPENDENT_RESULTS_v0.1.json'))
    parser.add_argument('--source-dir', type=Path, default=None)
    args = parser.parse_args()
    groups: list[dict[str, Any]] = []

    def exact(name: str, expressions: Any, detail: str = '') -> None:
        residuals = []
        for expr in entries(expressions):
            e = sp.expand(expr)
            r = sp.simplify(sp.trigsimp(e)) if e.has(sp.sin, sp.cos) else sp.simplify(e)
            residuals.append(r)
        groups.append({'name': name, 'kind': 'symbolic_identity',
                       'evaluated_conditions': len(residuals),
                       'pass': all(r == 0 for r in residuals),
                       'nonzero_residuals': [str(r) for r in residuals if r != 0],
                       'detail': detail})

    def predicate(name: str, tests: Iterable[bool], detail: str,
                  evidence: dict[str, Any] | None = None, kind: str = 'finite_witness') -> None:
        values = [bool(x) for x in tests]
        groups.append({'name': name, 'kind': kind,
                       'evaluated_conditions': len(values), 'pass': all(values),
                       'condition_values': values, 'detail': detail,
                       'evidence': evidence or {}})

    th, ell, A, d = sp.symbols('theta ell A delta', real=True)
    ez = sp.Matrix([0, 0, 1])
    f = A*sp.cos(3*(th-ell))
    M = f*sp.Matrix([sp.cos(th), sp.sin(th), 1])
    R = lambda a: sp.Matrix([[sp.cos(a), -sp.sin(a), 0],
                             [sp.sin(a), sp.cos(a), 0], [0, 0, 1]])
    H = sp.diag(1, 1, -1)
    S = sp.diag(1, -1, 1)
    Q = lambda v: v[0]**2 + v[1]**2 - v[2]**2

    exact('E01_harmonic_derivatives_and_extremum_values',
          [sp.diff(f, th) + 3*A*sp.sin(3*(th-ell)), sp.diff(f, th, 2)+9*f]
          + [f.subs(th, ell+j*sp.pi/3)-A*(-1)**j for j in range(6)]
          + [sp.diff(f, th, 2).subs(th, ell+j*sp.pi/3)+9*A*(-1)**j for j in range(6)],
          'Derivative/value checks support the analytic classification; A sign and zero case remain explicit.')
    pattern = [sp.cos(3*ell), sp.sin(3*ell), -sp.cos(3*ell), -sp.sin(3*ell)]
    exact('E02_twelve_clock_values',
          [sp.cos(sp.pi*q/2-3*ell)-pattern[q % 4] for q in range(12)])
    j, r = sp.symbols('j r', integer=True)
    exact('E03_exact_grid_hit_sufficiency',
          sp.cos(sp.pi*(r+2*j)/2-3*(r*sp.pi/6))-(-1)**j,
          'Necessity is the manuscript integer rearrangement, not inferred from this single identity.')
    z = sp.symbols('z', real=True)
    Mz = z*sp.Matrix([sp.cos(th), sp.sin(th), 1])
    exact('E04_cone_and_squared_norm', [Q(Mz), Mz.dot(Mz)-2*z*z])
    extrema_residuals = []
    for k in range(6):
        if k % 2 == 0:
            idx, height = k//2, 1
        else:
            idx, height = (k//2+2) % 3, -1
        aj = ell+2*sp.pi*idx/3
        target = A*sp.Matrix([sp.cos(aj), sp.sin(aj), height])
        extrema_residuals.append(M.subs(th, ell+k*sp.pi/3)-target)
    exact('E05_vertical_pairs_and_visiting_order', extrema_residuals)
    exact('E06_cartesian_harmonics_and_planar_half_period',
          [M[0]-A*(sp.cos(4*th-3*ell)+sp.cos(2*th-3*ell))/2,
           M[1]-A*(sp.sin(4*th-3*ell)-sp.sin(2*th-3*ell))/2,
           M[0].subs(th, th+sp.pi)-M[0], M[1].subs(th, th+sp.pi)-M[1]])
    exact('E07_five_frozen_transformations',
          [M.subs(th, th+2*sp.pi/3)-R(2*sp.pi/3)*M,
           M.subs(th, th+sp.pi)-H*M,
           M.subs(th, -th)-S*M.subs(ell, -ell),
           M.subs(th, 2*ell-th)-R(2*ell)*S*M,
           M.subs(ell, ell+d)-R(d)*M.subs(th, th-d)])

    x = sp.Matrix(sp.symbols('x1:4', real=True))
    y = sp.Matrix(sp.symbols('y1:4', real=True))
    omega = x+sp.I*y
    C = x.cross(y)
    pairs = [(1, 2), (2, 0), (0, 1)]
    exact('E08_channel_area_products',
          sp.Matrix([sp.im(sp.expand(sp.conjugate(omega[j])*omega[k])) for j,k in pairs])-C)
    a,b = sp.symbols('a b', real=True)
    cp = sp.symbols('common_phase', real=True)
    exact('E09_chiral_phase_conjugation_and_scaling',
          [(a*x-b*y).cross(b*x+a*y)-(a*a+b*b)*C,
           x.cross(-y)+C,
           (sp.cos(cp)*x-sp.sin(cp)*y).cross(sp.sin(cp)*x+sp.cos(cp)*y)-C])
    k2 = x.dot(x)+y.dot(y)
    exact('E10_gram_determinant_and_sharp_slack',
          [C.dot(C)-x.dot(x)*y.dot(y)+x.dot(y)**2,
           k2**2/4-C.dot(C)-(x.dot(x)-y.dot(y))**2/4-x.dot(y)**2])
    t = sp.symbols('t', real=True)
    xx, yy = sp.Matrix([t,0,0]), sp.Matrix([0,t,0])
    cc = xx.cross(yy)
    exact('E11_sharpness_witness', cc.dot(cc)-(xx.dot(xx)+yy.dot(yy))**2/4)
    alpha,beta = sp.symbols('alpha beta', real=True)
    m = sp.Matrix(sp.symbols('m1:4', real=True))
    c = sp.Matrix(sp.symbols('c1:4', real=True))
    T = alpha*m+beta*c
    exact('E12_blend_norm_and_cone_defect',
          [T.dot(T)-alpha**2*m.dot(m)-beta**2*c.dot(c)-2*alpha*beta*m.dot(c),
           Q(T)-alpha**2*Q(m)-beta**2*Q(c)-2*alpha*beta*(m[0]*c[0]+m[1]*c[1]-m[2]*c[2]),
           (alpha*m-beta*c)-(2*alpha*m-T)])
    v = sp.Matrix(sp.symbols('v1:4', real=True))
    rr = sp.sqrt(v.dot(v))
    uu = v/rr
    # Formula is checked on the nonzero domain; no evaluation at v=0.
    exact('E13_normalization_differential', uu.jacobian(v)-(sp.eye(3)-uu*uu.T)/rr)

    kap,R0,rmax,Hz = sp.symbols('kappa R rmax H_z', positive=True)
    chi = sp.symbols('chi', real=True)
    rad = rmax*kap/(1+kap)
    XX, YY, ZZ = (R0+rad*sp.cos(chi))*sp.cos(th), (R0+rad*sp.cos(chi))*sp.sin(th), rad*sp.sin(chi)
    exact('E14_torus_inverse_algebra',
          [XX**2+YY**2-(R0+rad*sp.cos(chi))**2,
           (rad*sp.cos(chi))**2+ZZ**2-rad**2,
           rad/(rmax-rad)-kap,
           2*Hz*(sp.pi*z/(2*Hz))/sp.pi-z],
          'Square-root signs and atan2 branches use the written R>rmax>0, kappa>0, |chi|<pi/2 hypotheses.')
    oa, ob = sp.Matrix([1,1,1]), sp.Matrix([1,sp.I,1])
    cof = lambda o: sp.re(o).cross(sp.im(o))
    exact('E15_scalar_information_loss_witness',
          [(sp.conjugate(oa).T*oa)[0]-(sp.conjugate(ob).T*ob)[0],
           cof(oa), cof(ob)-sp.Matrix([-1,0,1])])

    L = sp.ones(3)-3*sp.eye(3)
    eps,g = sp.symbols('eps g', real=True)
    ks = sp.symbols('k1:4', real=True)
    si = [x[i]**2+y[i]**2 for i in range(3)]
    D = sp.Matrix([eps*(ks[i]-si[i])*omega[i] for i in range(3)])+g*L*omega
    norm2 = lambda w: (sp.conjugate(w).T*w)[0].expand()
    pair_sum = sum(sp.expand(sp.conjugate(omega[i]-omega[j])*(omega[i]-omega[j])) for i in range(3) for j in range(i+1,3))
    exact('E16_graph_quadratic_form', (sp.conjugate(omega).T*L*omega)[0]+pair_sum)
    base = 2*eps*sum(ks[i]*si[i]-si[i]**2 for i in range(3))-2*g*pair_sum
    exact('E17_exact_intensity_and_remainder',
          [norm2(omega+D)-norm2(omega)-base-norm2(D),
           norm2(D)-eps**2*sum(si[i]*(ks[i]-si[i])**2 for i in range(3))-g**2*norm2(L*omega)
           -2*eps*g*sp.re(sum((ks[i]-si[i])*sp.conjugate(omega[i])*(L*omega)[i] for i in range(3)))])
    dx,dy = sp.Matrix(sp.symbols('dx1:4', real=True)),sp.Matrix(sp.symbols('dy1:4', real=True))
    delta = dx+sp.I*dy
    exact('E18_forced_intensity_identity',
          norm2(omega+D+delta)-norm2(omega)-base-norm2(D+delta)-2*sp.re((sp.conjugate(omega).T*delta)[0]))
    potential = eps*sum(si[i]**2/4-ks[i]*si[i]/2 for i in range(3))+g*pair_sum/2
    exact('E19_six_real_gradient',
          [sp.diff(potential,x[i])+sp.re(D[i]) for i in range(3)]
          + [sp.diff(potential,y[i])+sp.im(D[i]) for i in range(3)])
    vals = {**dict(zip(x,[2,2,2])),**dict(zip(y,[0,0,0])),**dict(zip(ks,[1,1,1])),eps:1}
    nxt = (omega+D).subs(vals)
    newvals = vals|dict(zip(x,[-4,-4,-4]))
    exact('E20_overshoot_intensity_and_potential_witness',
          [nxt-sp.Matrix([-4,-4,-4]), norm2(omega).subs(vals)-12,
           norm2(nxt)-48, base.subs(vals)+72, norm2(D).subs(vals)-108,
           potential.subs(vals)-6, potential.subs(newvals)-168])
    aa = sp.symbols('ema_a', positive=True)
    n = sp.symbols('n', integer=True, positive=True)
    wsum = aa**n+(1-aa)*(1-aa**n)/(1-aa)
    exact('E21_ema_weight_sum', wsum-1,
          'The analytic bound also needs 0<a<1, |m0|<=1 and |J| finite, as in the manuscript.')
    inputs = sp.symbols('j1:5', real=True)
    m0 = sp.symbols('m0', real=True)
    mnow=m0
    res=[]
    for n0 in range(1,5):
        mnow=aa*mnow+(1-aa)*inputs[n0-1]
        closed=aa**n0*m0+(1-aa)*sum(aa**(n0-j)*inputs[j-1] for j in range(1,n0+1))
        res.append(mnow-closed)
    exact('E22_ema_closed_form_finite_induction_witnesses',res,
          'Finite checks supplement, and do not replace, the written induction proof.')
    exact('E23_diagnostic_separating_values',
          [sp.sqrt((10-1)**2)-9,
           sp.acos(sp.Integer(1)),
           sp.sqrt((2*sp.Rational(1,10**8))**2)-sp.Rational(2,10**8),
           sp.acos(-sp.Integer(1))-sp.pi,
           sp.sqrt(sp.Rational(1,4))-sp.Rational(1,2)])

    # Missing definition witness: zero has no unique polar phase. These phase
    # assignments preserve the same V but affect a neighbouring nonzero entry.
    lam = sp.symbols('lambda_phase', real=True)
    phase_a = [0,sp.pi/6,0]
    phase_b = [sp.pi,sp.pi/6,0]
    inc = lambda p: lam*sum(sp.sin(3*(p[k]-p[1])) for k in range(3))
    exact('E24_zero_phase_ambiguity_algebra',
          [inc(phase_a)+2*lam,inc(phase_b)],
          'Both are valid polar descriptions of V=(0,exp(i*pi/6),1); the middle increments differ.')
    phases=np.angle(np.array([complex(0.,0.),complex(-0.,0.)],dtype=np.complex128))
    diff=abs(np.exp(1j*(np.pi/6-2*.001))-np.exp(1j*np.pi/6))
    predicate('E25_signed_zero_and_nonzero_neighbor_witness',
              [phases[0] == 0., phases[1] == np.pi, diff > .0019],
              'Standalone NumPy convention witness and transcription of equation (4), not an execution of the historical helper.',
              {'numpy_angles':phases.tolist(),'middle_output_distance_at_lambda_0001':float(diff)})

    sources={}
    if args.source_dir is not None:
        source_dir=args.source_dir
        p=source_dir/'geometry_embeddings.py'
        if not p.is_file():
            raise FileNotFoundError(p)
        tree=ast.parse(p.read_text(encoding='utf-8-sig'))
        funcs={node.name:node for node in tree.body if isinstance(node,ast.FunctionDef)}
        cylinder=ast.unparse(funcs['history_to_xyz'])
        torus=ast.unparse(funcs['history_to_torus_xyz'])
        predicate('E26_static_embedding_configuration',
                  [' / 12' in cylinder,'config' not in cylinder,'config.n_sectors' in torus],
                  'AST source check: alternate cylinder has fixed 12; alternate torus reads config.n_sectors.',
                  {'file':p.name,'sha256':sha256(p)},kind='source_static')
        sources[p.name]=sha256(p)
        core=source_dir/'model_core.py'
        if core.is_file():
            tr=ast.parse(core.read_text(encoding='utf-8-sig'))
            methods={node.name:node for node in ast.walk(tr) if isinstance(node,ast.FunctionDef)}
            core_z=ast.unparse(methods['update_z'])
            step=ast.unparse(methods['phase_lock_step'])
            predicate('E27_static_core_readout_dependency',
                      ['alpha * Z_macro + beta * Z_chiral' in core_z,
                       'state.Z_vec' not in step,'state.z' not in step,
                       'state.Omega = Omega_next' in step],
                      'Static supplied working-core check only; not verification of every possible external caller.',
                      {'file':core.name,'sha256':sha256(core)},kind='source_static')
            sources[core.name]=sha256(core)
    report={'reviewed_paper':'Paper E v0.1',
            'reviewed_pdf_sha256':'0d2a1e0b40d96f39c3929ad3c0a3c833b7eebebffc336b452ea9e1004f88880d',
            'author':'GPT independent review',
            'scope':'Supporting identities, finite witnesses, and optional static source checks. No kernel imports, historical reruns, GUI launches, package build or protected-file verification.',
            'versions':{'python':platform.python_version(),'sympy':sp.__version__,'numpy':np.__version__},
            'source_hashes':sources,'script_sha256':sha256(Path(__file__)),
            'groups':groups,
            'summary':{'groups':len(groups),'passed':sum(row['pass'] for row in groups),
                       'evaluated_conditions':sum(row['evaluated_conditions'] for row in groups),
                       'symbolic_groups':sum(row['kind']=='symbolic_identity' for row in groups),
                       'static_groups':sum(row['kind']=='source_static' for row in groups),
                       'finite_witness_groups':sum(row['kind']=='finite_witness' for row in groups),
                       'all_pass':all(row['pass'] for row in groups)},
            'count_notice':'Groups and scalar conditions are supporting checks, not counts of theorems. Nonzero-domain and inequality hypotheses are reviewed analytically.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps(report['summary'],indent=2))
    for row in groups:
        if not row['pass']:
            print('FAILED',row['name'],row.get('nonzero_residuals',row.get('condition_values')))
    return 0 if report['summary']['all_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
