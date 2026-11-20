"""Exact algebra for the new correspondence note, not an experimental test."""
from pathlib import Path
import hashlib
import json
import platform
import sys
import time
import sympy as s

ROOT = Path(__file__).resolve().parent
checks = []

def check(name, residual, scope):
    entries = list(residual) if isinstance(residual, s.MatrixBase) else [residual]
    reduced = [s.simplify(s.expand(v)) for v in entries]
    passed = all(v == 0 for v in reduced)
    checks.append({"id": name, "passed": passed, "scope": scope,
                   "residuals": [str(v) for v in reduced]})
    if not passed:
        raise AssertionError((name, reduced))

def grad(f, variables):
    return s.Matrix([s.diff(f, v) for v in variables])

def divergence(v, variables):
    return sum(s.diff(v[i], variables[i]) for i in range(3))

def curl(v, variables):
    return s.Matrix([s.diff(v[2], variables[1])-s.diff(v[1], variables[2]),
                     s.diff(v[0], variables[2])-s.diff(v[2], variables[0]),
                     s.diff(v[1], variables[0])-s.diff(v[0], variables[1])])

def main():
    started = time.monotonic()
    x = s.Matrix(s.symbols("x0:3", real=True))
    y = s.Matrix(s.symbols("y0:3", real=True))
    e = s.ones(3, 1)
    T = s.Matrix([[-s.Rational(1,2),1,-s.Rational(1,2)],
                  [-s.sqrt(3)/2,0,s.sqrt(3)/2],[0,0,0]])
    C = x.cross(y)
    W = T*C
    Gamma = (e.T*C)[0]
    intensity = x.dot(x)+y.dot(y)
    abs_bilinear_square = (x.dot(x)-y.dot(y))**2+4*x.dot(y)**2
    check("A01_attachment_gram", T.T*T-s.Rational(3,2)*(s.eye(3)-e*e.T/3),
          "Inherited Paper G attachment identity, transcribed independently.")
    check("A02_C_reconstruction", C-(s.Rational(2,3)*T.T*W+Gamma*e/3),
          "All complex triad states.")
    check("A03_gram_identity", intensity**2-abs_bilinear_square-4*C.dot(C),
          "All complex triad states.")
    check("A04_exact_W_identity", W.dot(W)-s.Rational(3,8)*(intensity**2-abs_bilinear_square)+Gamma**2/2,
          "Algebra behind the sharp W/intensity bound; inequality also needs nonnegativity.")
    xv, yv = s.Matrix([1,1,0]), s.Matrix([0,0,s.sqrt(2)])
    Wv = T*xv.cross(yv)
    check("A05_bound_attainment", Wv.dot(Wv)-s.Rational(3,8)*(xv.dot(xv)+yv.dot(yv))**2,
          "Witness Omega=(1,1,i sqrt(2)); a state-space identity, not an invariant orbit.")
    fx = s.Matrix([1,-s.Rational(1,2),-s.Rational(1,2)])/s.sqrt(3)
    fy = s.Matrix([0,-s.sqrt(3)/2,s.sqrt(3)/2])/s.sqrt(3)
    Cf = fx.cross(fy)
    check("A06_fourier_W_zero", T*Cf, "Normalized f1 mode; f2 follows by conjugation.")
    check("A07_fourier_C_nonzero", Cf+s.sqrt(3)*e/6, "The zero W does not imply zero chirality.")
    check("A08_conjugation_W_odd", T*x.cross(-y)+W, "Complex conjugation, not a physical time reversal assertion.")
    theta = s.symbols("theta", real=True)
    xr = s.cos(theta)*x-s.sin(theta)*y
    yr = s.sin(theta)*x+s.cos(theta)*y
    check("A09_common_phase_invariants", xr.cross(yr)-C,
          "All common phases, as an algebraic identity for C.")

    eps, g = s.symbols("epsilon g", real=True)
    kval = s.Matrix(s.symbols("k0:3", real=True))
    Isite = [x[i]**2+y[i]**2 for i in range(3)]
    potential = eps*sum(Isite[i]**2/4-kval[i]*Isite[i]/2 for i in range(3))
    potential += g*sum((x[i]-x[j])**2+(y[i]-y[j])**2 for i in range(3) for j in range(i+1,3))/2
    L = e*e.T-3*s.eye(3)
    bx = eps*s.Matrix([(kval[i]-Isite[i])*x[i] for i in range(3)])+g*L*x
    by = eps*s.Matrix([(kval[i]-Isite[i])*y[i] for i in range(3)])+g*L*y
    check("A10_native_gradient", grad(potential,list(x)+list(y))+bx.col_join(by),
          "Real coordinate normalization; does not prove full-map descent.")
    edge_sum = sum((x[i]-x[j])**2+(y[i]-y[j])**2 for i in range(3) for j in range(i+1,3))
    delta_intensity = (x+bx).dot(x+bx)+(y+by).dot(y+by)-intensity
    expected = 2*eps*sum((kval[i]-Isite[i])*Isite[i] for i in range(3))-2*g*edge_sum+bx.dot(bx)+by.dot(by)
    check("A11_native_intensity_balance", delta_intensity-expected,
          "Phase kicks preserve component moduli, so this is the full native intensity change.")
    witness_k = s.Matrix([s.Rational(999,1000),1,s.Rational(1001,1000)])
    witness_v = e+s.Rational(1,10)*(witness_k-e)+s.Rational(1,60)*L*e
    assert all(value>0 for value in witness_v)
    check("A12_NPC_charge_counterexample", witness_v.dot(witness_v)-3-s.Rational(1,50000000),
          "Exact NPC finite-domain tuple and Omega=(1,1,1); all phase kicks vanish.")
    u = s.symbols("u0:3")
    D = s.diag(*u)
    expected_commutator = s.Matrix(3,3,lambda i,j: 0 if i==j else u[j]-u[i])
    check("A13_local_phase_commutator", L*D-D*L-expected_commutator,
          "Fixed nonzero graph coupling is not covariant under arbitrary independent node phases.")

    X,Y,Z = s.symbols("X Y Z", real=True)
    coord = [X,Y,Z]
    rvec = s.Matrix(coord)
    radius = s.sqrt(rvec.dot(rvec))
    mu = s.Matrix(s.symbols("mu_x mu_y mu_z", real=True))
    nu = s.Matrix(s.symbols("nu_x nu_y nu_z", real=True))
    f = s.exp(-rvec.dot(rvec))
    check("A14_naive_field_divergence", divergence(mu*f,coord)+2*mu.dot(rvec)*f,
          "A localized axial readout generally violates div B=0.")
    current = curl(mu*f,coord)
    check("A15_bound_current_continuity", divergence(current,coord),
          "Smooth Gaussian witness; general compact-source statement follows from div curl=0.")
    A = mu.cross(rvec)/radius**3
    B = 3*mu.dot(rvec)*rvec/radius**5-mu/radius**3
    check("A16_dipole_curl_A", curl(A,coord)-B, "r>0; common mu0/(4pi) suppressed.")
    check("A17_dipole_divergence", divergence(B,coord), "r>0 only, not a distributional assertion at a point source.")
    check("A18_dipole_vacuum_curl", curl(B,coord), "r>0 only.")
    U = mu.dot(nu)/radius**3-3*mu.dot(rvec)*nu.dot(rvec)/radius**5
    force = 3*((mu.dot(rvec))*nu+(nu.dot(rvec))*mu+mu.dot(nu)*rvec)/radius**5
    force -= 15*mu.dot(rvec)*nu.dot(rvec)*rvec/radius**7
    check("A19_dipole_force", -grad(U,coord)-force, "Fixed dipoles; far-field/point-dipole effective potential.")
    check("A20_dipole_energy", U+nu.dot(B), "Pair energy has one interaction term, not double counting.")
    grav = s.symbols("G", positive=True)
    ma,mb = s.symbols("m_a m_b", positive=True)
    Ug = -grav*ma*mb/radius
    check("A21_gravity_force", -grad(Ug,coord)+grav*ma*mb*rvec/radius**3, "Positive masses; separated bodies/point limit.")
    check("A22_Newton_vacuum_Poisson", divergence(grad(-grav*mb/radius,coord),coord), "r>0; source coefficient fixed separately by Gauss flux.")
    rr, screening = s.symbols("r sigma", positive=True)
    phiY = -grav*mb*s.exp(-screening*rr)/rr
    check("A23_Yukawa_alternative", s.diff(rr**2*s.diff(phiY,rr),rr)/rr**2-screening**2*phiY,
          "A different extra spatial law leaves the same projected native map; not a native prediction.")
    kvec = s.Matrix(s.symbols("k_x k_y k_z", real=True))
    PT = s.eye(3)-kvec*kvec.T/kvec.dot(kvec)
    check("A24_transverse_projection", PT*PT-PT, "Nonzero Fourier wavevector.")
    check("A25_magnetic_Gauss_law", (kvec.T*PT).T, "Nonzero Fourier wavevector.")
    check("A26_magnetic_Ampere_law", kvec.cross(PT*mu-mu),
          "B_hat=mu0 P_T M_hat, no free current; decay fixes the real-space solution.")
    angle = s.Matrix(s.symbols("theta_x theta_y theta_z", real=True))
    ext = s.Matrix(s.symbols("B_x B_y B_z", real=True))
    check("A27_dipole_torque_virtual_work", -angle.cross(mu).dot(ext)+angle.dot(mu.cross(ext)),
          "delta U=-delta theta dot(mu cross B).")
    rho,alpha,kappa,m0 = s.symbols("rho alpha kappa m0", real=True)
    # Rigid-pose norm preservation and alpha>0 are written hypotheses.
    bound_residual = kappa**2*W.dot(W)-3*kappa**2*intensity**2/8
    check("A28_candidate_moment_bound_remainder", bound_residual+kappa**2*(3*abs_bilinear_square/8+Gamma**2/2),
          "Nonpositive remainder; m-m0=alpha I translates it to a conditional moment/mass bound.")
    mass, change, K = s.symbols("mass change K", real=True)
    delta_energy = K-grav*((mass+change)**2-mass**2)/rr
    check("A29_split_step_energy_obstruction",
          s.diff(delta_energy,rr)-grav*(2*mass*change+change**2)/rr**2,
          "Positive mass, change, G and r make the derivative positive; no state-only K cancels it for every separation.")
    versions = {"python": sys.version, "executable": sys.executable,
                "sympy": s.__version__, "platform": platform.platform()}
    assert "envs\\torment\\" in sys.executable.lower(), sys.executable
    report = {"status": "PASS", "checks": checks, "passed": len(checks),
              "meaning": "Exact algebraic checks; not independent peer review or physical validation.",
              "elapsed_seconds": time.monotonic()-started, "environment": versions,
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/"VERIFICATION_RESULTS.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status": "PASS", "checks": len(checks), **versions},indent=2))

if __name__ == "__main__":
    main()
