# kernel_physics v0.1

**Paper C exact local geometry + Paper A exact abstract dynamics.**

**NO PHYSICAL COUPLING BETWEEN THEM IS CLAIMED YET.**

This is a separate, minimal Python package. Geometry and dynamics do not import
each other. There is no framework, server, plugin system, memory architecture or
historical-kernel dependency.

## Frozen definitions

- Paper C: PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.3.1.md,
  §§2–7,9 and Appendix B.
- Paper A: PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.5.1.md,
  §§1–3 and §6.

The source paths and original SHA-256 hashes are in baseline_manifest.json.
Neither paper was modified. No historical PDF or kernel source was opened.

## Modules

- **geometry.py**: SymPy exact coordinates, w=1, s=sqrt(2)-1, general-angle
  panel maps and the canonical beta=pi/3 weld. folded_module() returns an
  immutable mesh with 18 vertices, 21 edges, three octagonal faces, three seams
  and two nine-edge boundary loops, preserving Paper C's vertex/face ordering.
  Normals are computed from the oriented faces. central_section(height) returns
  three unit segments for abs(height)<=s/2: a curve, not a filled cap.
  rotate_c3, reflect_vertical and reflect_horizontal are the exact D3h
  generators about the centroid axis and the planes x=0, z=0.
- **dynamics.py**: immutable DynamicsConfig(eps, g, phase_strength, k),
  step3 and step_ring. phase_strength is Paper A's lambda;
  k is a real amplitude-coefficient triple. All parameters are explicit.
- **covering.py**: exact immutable cycle Laplacians, residue pullback P for all
  positive M,d, and Q=P/sqrt(M/d) for divisor cases. Sizes 1 and 2 retain
  incidence multiplicity. No isometry or intertwining is claimed for non-divisors.

The implemented dynamics are

~~~text
L3 = [[-2,1,1], [1,-2,1], [1,1,-2]]
Omega_tilde = Omega + eps*Omega*(k-abs(Omega)^2) + g*L3@Omega
theta_n = Arg0(Omega_tilde_n), with Arg0(0)=0
F(Omega)_n = abs(Omega_tilde_n) * exp(i * (
    theta_n + lambda * sum_{m~n} sin(3*(theta_m-theta_n))))
~~~

All phase increments use the same pre-synchronization vector. At three nodes the
two neighbors are the other two nodes; on the ring they are the periodic
neighbors, including wrap-around. step_ring requires M=3q and repeats k
by residue class. It evolves unrestricted ring states, not just lifted states.
When lambda is zero, synchronization returns a copy directly, without invoking
phase extraction or reconstructing polar coordinates.

Geometry and linear covering identities use exact symbolic arithmetic.
Dynamics use NumPy complex128; nonlinear lift identities are checked to stated
roundoff tolerances, not asserted as bitwise equal. Nonfinite input is rejected;
numerical overflow is not a physical prediction. There is no timestep parameter,
automatic state normalization, random noise, or hidden state.

Paper A's nonzero-lambda extension is generally discontinuous when pre-sync
components vanish. Global-phase equivariance tests cover nonzero pre-sync
components, and the lambda-zero case including zeros. No unrestricted
equivariance claim is made for the zero-component extension.

## Run the focused tests

Use Python compatible with the pinned dependencies (tested here on Python
3.12.14). From the parent directory containing kernel_physics, a fresh Windows
environment can be set up and tested with:

~~~powershell
python -m venv kernel_physics/.venv
.\kernel_physics\.venv\Scripts\python.exe -m pip install -r kernel_physics/requirements.txt
.\kernel_physics\.venv\Scripts\python.exe -B -m unittest discover -s kernel_physics/tests -v
~~~

The completed local environment reuses the bundled NumPy installation and keeps
the added SymPy dependency inside kernel_physics/.venv. Tests use only fixed
inputs: printed coordinates, hand-calculated steps, exact matrix identities and
selected nonlinear lifts at M=3,6,12,24. There is no atlas, scan or parameter tuning.
See VALIDATION.md, validation.json and test_run.txt for the recorded result.

## Scope boundary

The shell is one local module. No global host, caps, interior field, assigned
physical boundary conditions or privileged physical M=12 geometry is introduced.
The geometric coordinate z is not a historical kernel readout.

No J_eff interpretation, Z-family readouts, central-energy law, six-gap mapping,
SRG, RSB, meta-shell, recursive thermodynamics, magnetic coupling, gravity,
wormholes, physical color/quark interpretation or TORMENT behavior is implemented.
These subjects are not rejected; they are outside v0.1.
