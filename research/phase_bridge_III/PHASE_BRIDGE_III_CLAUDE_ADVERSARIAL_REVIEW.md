# Phase Bridge III — independent Claude adversarial review

Date: 2026-09-21. Reviewer: Claude (independent adversarial mathematical-physics review).
Frozen baseline: `899d0fa900dc0d0ab8406e889908e47468d343db` (repository `HEAD` at review time).
Report under review: `research/phase_bridge_III/PHASE_BRIDGE_III_RECURSIVE_TIME_ACTION_ANGLE.md`,
SHA-256 `d19178a45b44f422a0f9f5c38494c79778914be846f3e2eddb118e29baa68f95` (67,226 bytes, untracked).

**Headline.** The report survives. Every load-bearing theorem was re-derived from scratch — in
several cases by two or three independent routes — and **none was contradicted**. The exact
local-clock threshold $|\alpha| = 4\sqrt{14}$ is confirmed by symbolic computation in
$(I,\phi)$, by the report's own $(x,y)$ reduction, and by a numerical linearisation of the real
six-dimensional Cartesian field that uses no polar coordinates at all. The two-unit-multiplier
obstruction (8.7) is confirmed by two analytic methods and by direct numerical monodromy
including a randomized counterexample search that found nothing.

What the review adds is not refutation but **sharpening**, in four places where the report is
weaker than the mathematics permits, and **one scope correction** that matters for how the
historical programme should be read:

1. The threshold $4\sqrt{14}$ is a witness value; a **closed-form general threshold** exists
   (§15 below, `N1`).
2. Theorem (8.7) is **largely vacuous in exactly the regime H1 needs**. In the strictly
   advancing clock regime, interior periodic orbits exist only on the codimension-one set
   $\sin E_0\,J_0(A)=0$; otherwise there are none at all and the fate is decided by
   $\operatorname{sign}(\nu\!\int_0^{2\pi}\!S)$ alone — **independently of $\kappa$, $W$ and the
   warp steepness**. This is a strictly stronger refutation of H1's threshold than the report
   gives (`N2`).
3. The logarithmic chart is **one of an infinite family** of exact canonical embeddings, not a
   one-parameter family (`N3`); $I_\ast$ is pure gauge in a precise sense.
4. Above the local-clock threshold the witness model does **not** go anywhere new: it transfers
   to the in-phase synchronous branch, which §7.2 proved is linearly stable for *every* slope.
   The local clock selects between two pre-existing branches (`N5`).

And one caution that bears directly on H1's historical numerics: a unit-multiplier monodromy
with a nontrivial Jordan block is **numerically defective**. Naive eigenvalue extraction returns
a spurious spread of order $\sqrt{\epsilon_{\rm mach}}$ around $1$ — in this review's own
witness, $1 \pm 2.4\times10^{-6}i$ from an exactly unit-multiplier orbit. Any historical
measurement of "a Floquet multiplier slightly above one" in H1's interior is consistent with
this artefact and does not by itself contradict (8.7) (`N6`).

**Novelty verdict.** No novel mathematical class was found. The recursive loop is real (not a
coordinate artefact) in the coupled regime, and the $4\sqrt{14}$ effect is a genuine,
coordinate-invariant distinction from any constant-detuning replacement of the same orbit. But
the invariant that carries the distinction is $c = r^2\varpi'(I_\ast)$, which is exactly the
shear (nonisochronicity) coefficient of amplitude-phase oscillator theory; with affine
$\varpi$ the entire system is a discrete cubic complex Ginzburg–Landau network on $K_3$,
verified as an algebraic identity. `NOVELTY_STATUS = NOVELTY ONLY IN GEOMETRIC REALIZATION`.

---

## 0. Execution provenance

The report under review states that **no** script was run (its §15). This review is the
complementary object: every verdict below is backed by an executed, independently written
symbolic or numerical check.

```
Environment : Python 3.11.15 (cloud container), SymPy 1.14.0, NumPy 2.4.4, SciPy 1.17.1
              (same SymPy/NumPy versions as the Bridge II Codex run; SciPy added for ODE work)
Working dir : /home/claude/pb3_review   (outside the repository; nothing written to the repo)

  python3 -B v1_action_angle.py           17 predicates   symplectic form, Hamilton sign, 4.1-4.3, 5
  python3 -B v2_paperA_polar.py           20 predicates   Paper-A polar parent from scratch, 6, 7.2
  python3 -B v3_threshold.py              25 predicates   7.3 threshold by three independent routes
  python3 -B v4_h1.py                     29 predicates   8.2-8.3 embedding, integral, multipliers
  python3 -B v5_commutator_floquet.py     26 predicates   9.2-9.3, 10 Magnus and witnesses
  python3 -B v6_chirality_symmetry.py     33 predicates   7.1, 11, 12, 13 transformation
  python3 -B v7a_new_results.py           17 predicates   13 reductions, loop tests, new corollaries
  python3 -B v7b_criticality.py           11 predicates   quotient dynamics past the threshold
  python3 -B v8_misc.py                   10 predicates   remaining point checks
  ----------------------------------------------------------------------------------------------
  TOTAL                                  188 predicates   188 PASSED, 0 FAILED
```

Three of the 188 (`H3`) are informational records of a dynamical outcome rather than pass/fail
assertions; they are marked as such in the script. Predicate counts include grouped subcases and
are not counts of independent theorems.

**Preservation, verified on the device, read-only:**

```
git rev-parse HEAD            = 899d0fa900dc0d0ab8406e889908e47468d343db
git status --porcelain        = "?? research/phase_bridge_III/"   (nothing else)
SHA256SUMS.txt verification   = 62 tracked files checked, 0 mismatches, 0 missing
                                (62 + SHA256SUMS.txt itself = the report's 63)
Historical PDFs H1..H5        = all five SHA-256 values match the report's §15 table exactly
```

`FROZEN_FILES_MODIFIED = NO`. `KERNEL_PHYSICS_MODIFIED = NO`. `REPOSITORY_MODIFIED = NO`.
Nothing was committed or pushed. `kernel_physics/dynamics.py` was **read** (to fix $L_3$ and the
$\operatorname{Arg}_0$ convention from source) but not imported or executed.

---

## 1. Claim ledger

Dispositions: `CONFIRMED_EXACT`, `CONFIRMED_WITH_ASSUMPTION`, `WORDING_CORRECTION`,
`PROOF_INCOMPLETE`, `CONTRADICTED`, `UNRESOLVED`, `NEW_DERIVED_COROLLARY`.

| ID | Report location and claim | Disposition | Independent finding / smallest correction |
|---|---|---|---|
| R01 | §3: $\sigma=\sum dq_i\wedge dp_i=\sum dI_i\wedge d\phi_i$ | CONFIRMED_EXACT | Jacobian determinant of $(I,\phi)\mapsto(q,p)$ is identically $1$; the quoted one-forms for $dq,dp$ are exact. `A1,A1b,A1c` |
| R02 | §3: $\dot I_i=\partial_{\phi_i}H$, $\dot\phi_i=-\partial_{I_i}H$ under $\iota_X\sigma=dH$ | CONFIRMED_EXACT | Solved the contraction symbolically; the pair $(I,\phi)$ plays the roles of $(q,p)$, so the *apparent* sign inversion relative to textbook action–angle is forced, not chosen. `A2` |
| R03 | §3: consistency with Bridge II's $\dot\Omega=-i\nu\Omega$, $\nu=-\varpi$ | CONFIRMED_EXACT | Re-derived in Cartesian coordinates from $H=\tfrac\nu2(q^2+p^2)$. This renaming also **repairs** the Bridge II §3-vs-§7 sign conflict that the Codex review flagged as C05. `A2b,A2c,K6` |
| R04 | §3: $d\phi$ well defined on the punctured plane; no global real $\operatorname{Arg}$ | CONFIRMED_EXACT | $d\phi$ is closed, with period exactly $2\pi$ around the circle, hence closed but not exact. `A3,A3b` |
| R05 | §3: zero stratum has real codimension $2m$; polar chart singular there | CONFIRMED_EXACT | Elementary and correct. |
| R06 | §3: smooth radial rate extends smoothly at $\Omega=0$, phase-only neighbour term need not | CONFIRMED_EXACT | $i\varpi(\lvert z\rvert^2/2)z$ is smooth; $\sin 3(\phi_j-\phi_i)$ has ray-dependent limits at $z_i=0$. Explicit witness. `K5,K5b` |
| R07 | §4.1: the family $H(I)=-\sum[\omega^{(0)}_iI_i+\kappa\!\int^{I_i}\!W_i(r_i)]+C$ | CONFIRMED_EXACT | Differentiation reproduces $\varpi_i$ exactly; "entire family" is correct **once restricted to angle-independent $H$**, which the report does state. `A4` |
| R08 | §4.2: Hamiltonian $\iff\ \partial_{I_j}\varpi_i=\partial_{I_i}\varpi_j$ | CONFIRMED_WITH_ASSUMPTION | Necessity needs $\varpi\in C^1$ (then $H\in C^2$ and Schwarz applies) — satisfied by the report's smoothness premise but not stated. The statement is also **relative to the frozen $\sigma$**; §4.2 does not say so, §4.3 does. `A5e,A6` |
| R09 | §4.2: counterexamples $w=\sum I_i^2$ and $\varpi_i=I_i/N$ | CONFIRMED_EXACT | Cross-derivatives computed: $2I_2-2I_1$ and $-I_1/N^2$ vs $-I_2/N^2$. Both fail off the equal-action locus. `A5a,A5b` |
| R10 | §4.2: common rate $\Rightarrow w=f(N)$ globally on the positive orthant | CONFIRMED_EXACT | $\nabla w\parallel(1,1,1)$ kills every direction with $\sum dI_i=0$; the level sets $\{N=c\}$ meet the orthant in a connected open simplex. `A5c,A5d` |
| R11 | §4.3: exactness of $\beta=\sum(F_i\,d\phi_i-\varpi_i\,dI_i)$ and its three condition families | CONFIRMED_EXACT | All fifteen closedness conditions computed; they split **exactly** into the three families the report names, including $\partial_{I_j}F_i=-\partial_{\phi_i}\varpi_j$. `A6` |
| R12 | §4.4: canonical flattening $J=f(I)$, $\psi=\phi/f'$; degree-one requires $f'=\pm1$ | CONFIRMED_EXACT | $dJ\wedge d\psi=dI\wedge d\phi$; well-definedness on the circle needs $1/f'\in\mathbb Z$, and degree one then forces $f'=\pm1$. `K1a,K1b` |
| R13 | §5: rotating frame gives $\dot\Psi=A_0(\Psi)+i[w+\dot\Theta]\Psi$ | CONFIRMED_EXACT | Re-derived symbolically from $\Omega=e^{-i\Theta}\Psi$ with common-phase equivariance. `A7` |
| R14 | §5: shared clock removable on a closed equivariant phase-invariant quotient | CONFIRMED_EXACT | The clock term is purely vertical (tangent to the group orbit), so the induced quotient field is unchanged and invariant observables agree at the same $t$. |
| R15 | §5: fails for $\rho_{\rm shared}$ depending on absolute phase, auxiliary absolute-phase laws, forcing, external references; H1 is such a case | CONFIRMED_EXACT | Enumerated in §4 below. H1's $\dot\rho=\nu(1-\rho)S(\phi)$ is exactly an absolute-phase feedback, so the invisibility theorem genuinely does not apply to it. |
| R16 | §5: separate rotating frames relocate unequal rates into the coupling | CONFIRMED_EXACT | The transported amplitude acquires $e^{i(\Theta_i-\Theta_j)}$. `K3` |
| R17 | §6 (6.1): $\dot I_i=2\varepsilon I_i(k_i-2I_i)-4gI_i+2g\sum\sqrt{I_iI_j}\cos\delta_{ji}$ | CONFIRMED_EXACT | Derived independently from $\dot\Omega_i=\varepsilon\Omega_i(k_i-\lvert\Omega_i\rvert^2)+g(L_3\Omega)_i$ with $L_3$ read from `kernel_physics/dynamics.py`. Every coefficient matches; perturbing the factor 2 breaks the identity. `B1,B3` |
| R18 | §6 (6.2): $\dot\phi_i=g\sum\sqrt{I_j/I_i}\sin\delta_{ji}$ | CONFIRMED_EXACT | Same derivation. The diagonal $-2\Omega_i$ contributes to amplitude only. `B2` |
| R19 | §6: total-action identity $\frac{d}{dt}\sum I_i=2\varepsilon\sum I_i(k_i-2I_i)-g\sum_{i<j}\lvert\Omega_i-\Omega_j\rvert^2$ | CONFIRMED_EXACT | Verified symbolically; no phase term survives the regrouping. `B4` |
| R20 | §6: the eight quoted Jacobian entries | CONFIRMED_EXACT | All eight verified, including the $\delta_{ij}\varpi_i'$ placement and the zero-row-sum property of the phase block. `B5a–B5h` |
| R21 | §7.1: three phase-only classes with transverse eigenvalues $-9K,-9K$ / $-3K,9K$ / $9K/2,9K/2$ | CONFIRMED_EXACT | Eigenvalues recomputed symbolically for each class; each has the neutral common-phase direction. `F1` |
| R22 | §7.1: 9 / 27 / 18 labelled relative branches in $\phi$ | CONFIRMED_EXACT | Enumerated on a $\pi n/9$ grid using the correct relative-equilibrium criterion ($r\sin(\psi-\theta_i)=0$, so all $\theta_i\in\{\psi,\psi+\pi\}$ when $r\ne0$). Counts $(9,27,18)$ reproduced. A naive $\lvert\sum e^{i\theta}\rvert=1$ test over-counts to 135 — the report's classification is the right one. `F1d` |
| R23 | §7.1: familiar $\phi$-differences $0,\pm2\pi/3$ belong to the **synchronized $\theta$** class | CONFIRMED_EXACT | $3\delta\equiv0 \Rightarrow \delta\in\{0,2\pi/3,4\pi/3\}$. This is the Codex C18/C20 correction propagated correctly. |
| R24 | §7.2: in-phase blocks $-2\varepsilon k\mathbf1+gL_3$, zero, $(g+3K)L_3$, slope only in the lower-left block | CONFIRMED_EXACT | Full $6\times6$ symbolic Jacobian at $I_i=k/2$ reproduces all four blocks. `B7a–B7d` |
| R25 | §7.2: spectrum $\{-2\varepsilon k,\,-2\varepsilon k-3g\,(\times2),\,0,\,-3g-9K\,(\times2)\}$, independent of $\varpi'$ | CONFIRMED_EXACT | Block-triangularity makes the slope invisible. Falsifies any universal "steep clock destroys synchrony" claim. `B8` |
| R26 | §7.3: $r^2=k-3g/\varepsilon$ gives an exact $120^\circ$ relative equilibrium at common rate $\varpi(I_\ast)$ | CONFIRMED_EXACT | Both the action and the phase conditions verified symbolically. `C0a,C0b` |
| R27 | §7.3: $S_{ij}=\sin(\theta_j-\theta_i)$ skew, $Su=0$, eigenvalues $\pm3i/2$, $S^2=-(9/4)P_\perp$ | CONFIRMED_EXACT | `C2a` |
| R28 | §7.3 (7.1): the block matrix | CONFIRMED_EXACT | The report's $(x,y)$ matrix equals the full $(I,\phi)$ Jacobian conjugated by $\operatorname{diag}(r^2,r^2,r^2,1,1,1)$, symbolically, for general $\varepsilon,g,K,k,\alpha$. `C2b` |
| R29 | §7.3 (7.2): $(\lambda-a)(\lambda-d)-9g^2/4+gcs=0$ | CONFIRMED_EXACT | `C2c` |
| R30 | §7.3: $\lambda^2+12\lambda+\tfrac{63}{2}\pm\tfrac{9i}{2}\alpha=0$ at the witness parameters | CONFIRMED_EXACT | The **full** $6\times6$ characteristic polynomial factors exactly as $\lambda(\lambda+6)\big[(\lambda^2+12\lambda+\tfrac{63}{2})^2+\tfrac{81}{4}\alpha^2\big]$. `C1b,C1c` |
| R31 | §7.3: threshold $\lvert\alpha\rvert=4\sqrt{14}$, critical frequency $3\sqrt{14}/2$ | CONFIRMED_EXACT | Exact algebra: $\operatorname{Re}\sqrt{(9/2)(1\mp i\alpha)}=6 \iff \sqrt{1+\alpha^2}=15 \iff \alpha=\sqrt{224}=4\sqrt{14}$. Confirmed numerically in Cartesian coordinates and by nonlinear integration of the group-invariant deviation. `C4,C5,C8` |
| R32 | §7.3: both chiral orderings have the same spectrum | CONFIRMED_EXACT | Spectra agree to $6.5\times10^{-10}$. `C9` |
| R33 | §7.3: a fixed-detuning replacement matching the orbit misses the effect | CONFIRMED_EXACT | Solved the locking equations: a constant-detuning model retaining the exact $120^\circ$ state forces **equal** detunings, hence $c=0$ and a spectrum independent of the common rate. `C7,C7b` |
| R34 | §7.3: "the example proves neither hysteresis, new attractors, nor a nondegenerate Hopf" | CONFIRMED_WITH_ASSUMPTION | Correct restraint, and the review can now say more: the crossing **is** transversal ($d\operatorname{Re}\lambda/d\alpha\approx0.187>0$) with a simple conjugate pair, so it is a Hopf-type crossing in the quotient; the criticality remains unproved and the numerics point away from supercritical. `C6,C6b`, `N5` |
| R35 | §8.1: $\rho=1$ invariant, $\rho=0$ not; $\nu S\ge0$ sufficient for forward invariance | CONFIRMED_EXACT | Explicit violating parameters exhibited ($E_0=0.2$, $A=2.0$). `K2,K2b` |
| R36 | §8.2: $y=-\log(1-\rho)$, $I=I_\ast y$, $\rho=1-e^{-I/I_\ast}$, $dI\wedge d\phi=I_\ast d\rho\wedge d\phi/(1-\rho)$ | CONFIRMED_EXACT | `D1a–D1c` |
| R37 | §8.2 (8.4): $H_{\rm hist}$ reproduces (8.1) exactly | CONFIRMED_EXACT | Both Hamilton equations checked and pushed back to $\rho$. `D2a–D2c` |
| R38 | §8.2: $I_\ast$ is an arbitrary positive scale | CONFIRMED_EXACT, sharpened | $H_{I_\ast}(I_\ast y)=I_\ast H_1(y)$ while $\sigma$ scales by the same $I_\ast$: the **pair** scales, so the vector field is $I_\ast$-independent. $I_\ast$ is pure gauge for the dynamics and a genuine choice only for the physical identification. `D2d` |
| R39 | §8.2: single-valued on the cylinder iff $\nu\int_0^{2\pi}S=0$; $\iota_X\sigma$ has nonzero circle period otherwise | CONFIRMED_EXACT | The non-periodic part of $U$ is $\langle S\rangle\phi$. |
| R40 | §8.2: "does not exclude other integrating factors" | WORDING_CORRECTION → NEW_DERIVED_COROLLARY | True but under-stated. The **complete** family is $M=G(F(\rho)-\nu U(\phi))/(1-\rho)$ for arbitrary $G$; each gives an exact canonical embedding. Verified symbolically. `D11` / `N3` |
| R41 | §8.3 (8.5): $F(\rho)-\nu U(\phi)$ conserved | CONFIRMED_EXACT | And it equals $-H_{\rm hist}/I_\ast$ — the same object, so its multivaluedness on the cylinder is governed by the same condition as R39. `D3a,D3b` |
| R42 | §8.3 (8.6): $F(\mathcal P(\rho_0))=F(\rho_0)+\nu\int_0^{2\pi}S$ | CONFIRMED_EXACT | Verified numerically: with $E_0=0$ (so $\langle S\rangle=\sin E_0 J_0(A)=0$) the return map is the identity to $10^{-11}$ over 40 turns. `D5b,D10c` |
| R43 | §8.3: no interior fixed point when the integral is nonzero | CONFIRMED_EXACT, scope widened | Monotonicity of $F$ is **not needed** for this conclusion — only $\nu\hat S\ne0$. (Where the full turn exists, $v>0$ makes $F'>0$ anyway.) |
| R44 | §8.3 (8.7): $\mu_1=\mu_2=1$ on every regular interior periodic orbit | CONFIRMED_EXACT | Method A: the $(y,\phi)$ field is exactly divergence free. Method B: $\operatorname{div}X=-\nu S=\frac{d}{dt}\log(1-\rho)$ integrates to zero over any closed orbit, so $\det\Phi(T)=1$; the autonomous tangent direction supplies $\mu_1=1$. Confirmed numerically on rotating **and** librating orbits, plus a 60-draw randomized counterexample search (worst $\max(\lvert\det-1\rvert,\lvert\operatorname{tr}-2\rvert)=9\times10^{-12}$). `D4,D5c,D6c,D7` |
| R45 | §8.3: theorem stated for "$0<\rho<1$" | WORDING_CORRECTION | The proof is valid on the **whole chart $\rho<1$**, including $\rho<0$. Verified on an orbit through $\rho_0=-0.7$. The headline is narrower than the theorem. `D8` |
| R46 | §8.3: a Jordan block can still produce shear; finite-time amplification allowed | CONFIRMED_EXACT | The witness monodromy is $\begin{pmatrix}1&0\\2.82&1\end{pmatrix}$ — defective, with linear-in-$n$ growth of $\lVert M^n\rVert$. Period varies across the family, which is the source of the shear. `D5d,D5e,E3d` |
| R47 | §8.3: boundary orbit multipliers $\{1,\exp[-\nu T\langle S\rangle]\}$ | CONFIRMED_EXACT | Numerical monodromy matches to $10^{-8}$; $\langle S\rangle=\sin E_0\,J_0(A)$ confirmed to 9 digits. `D9` |
| R48 | §8.3: interior equilibria have $\pm\sqrt{\kappa\nu(1-\rho_\ast)W'S'}$ | CONFIRMED_EXACT | Trace-free (Hamiltonian) Jacobian; a centre when the product is negative — which is where the librating interior periodic orbits live. `D6a` |
| R49 | §8.2: no nonconstant radial identification makes the isolated Paper-A parent equal H1 | CONFIRMED_EXACT | The Paper-A action law is angle-independent; H1's is not. |
| R50 | §9.1 (9.1): exact second-order variational equation and the $W''\dot\rho/W'$ term | CONFIRMED_EXACT | Re-derived by eliminating $\delta\rho$ where $c\ne0$. |
| R51 | §9.2 (9.2): the commutator | CONFIRMED_EXACT | Direct multiplication. It is traceless, so H1's printed zero-diagonal form cannot be repaired by reversing the commutator order — reversal flips all four entries. `E1a–E1d` |
| R52 | §9.2: commuting family $\iff$ $(a,b,c)$ span dimension $\le1$ | CONFIRMED_EXACT | The three independent entries are exactly the three $2\times2$ minors of the two vectors. Confirmed by an exhaustive $5^6=15{,}625$ integer sweep with zero mismatches, plus every degenerate case in the work order. This is a clean standalone lemma. `E2a–E2g` |
| R53 | §9.3: the two triangular fundamental matrices | CONFIRMED_EXACT | Both satisfy $\dot\Phi=\mathcal J\Phi$ symbolically. `E3a,E3b` |
| R54 | §9.3: multipliers $\{e^{A(T)},1\}$, time ordering changes shear but not multipliers | CONFIRMED_EXACT | Numerically: reversing the time ordering changes the shear entry from $7.14$ to $12.92$ with identical multipliers. `E3c` |
| R55 | §10: $\mathcal M_2=-T^3[\mathcal J_0,\mathcal J_1]/12$ for $\mathcal J=\mathcal J_0+t\mathcal J_1$; convergence $\int\lVert\mathcal J\rVert_2<\pi$ | CONFIRMED_EXACT | Double integral evaluated; the $\pi$ bound is the standard sharp 2-norm criterion. `E4a` |
| R56 | §10: $M=\operatorname{diag}(-2,-1/2)$ time-ordering witness | CONFIRMED_EXACT | All of it: $e^{T_1B_1}$, $e^{T_2B_2}$, the product, purely imaginary segment spectra, purely imaginary **averaged** generator, exponent $\log2/(T_1+T_2)$. The witness also lies outside the sufficient Magnus ball ($\int\lVert\mathcal J\rVert_2\,dt=4.712>\pi$), which is consistent with a truncated Magnus series failing to predict it. `E4b–E4g` |
| R57 | §10: constant-Jacobian feedback instability $(-a\pm\sqrt{a^2+4b\kappa})/2$ | CONFIRMED_EXACT | And $b=0$ removes it for every $\kappa$. `E5a–E5c` |
| R58 | §10.1: H1's published threshold is not a proved sufficient criterion | CONFIRMED_EXACT | All five of the report's grounds hold. See `N2` for a strictly stronger refutation. |
| R59 | §10.1: H1's numerical claims are UNRESOLVED, not disproved | CONFIRMED_WITH_ASSUMPTION | Correct. This review adds a specific candidate artefact (`N6`) without asserting it is the explanation. |
| R60 | §10.2: $\widetilde{\mathcal J}=\dot PP^{-1}+P\mathcal JP^{-1}$; periodic $P$ preserves multipliers | CONFIRMED_EXACT | |
| R61 | §11 (11.1): $\dot Z_i$ identity | CONFIRMED_EXACT | Verified identically for all three cyclic indices. `F2a,F2b` |
| R62 | §11: $\dot Z\vert_{\rm clock}=\alpha(15,-12,3)$ for $\Omega=(1,2,3)$, $\varpi_i=\alpha I_i$ | CONFIRMED_EXACT | `F2c` |
| R63 | §11: shared clock has exactly zero direct chirality contribution | CONFIRMED_EXACT | `F2d` |
| R64 | §11: a nonzero local clock is not conjugation-equivariant, so a selected rate law breaks that mirror **explicitly** | CONFIRMED_EXACT | $\overline{i\varpi(I)\Omega}=-i\varpi(I)\bar\Omega$. This is the single most important guard against mislabelling the effect "spontaneous". `F2g` |
| R65 | §11: $u\cdot Z$ is odd under an odd channel permutation, so chiral pairs are genuine symmetry images | CONFIRMED_EXACT | `F2f` |
| R66 | §11/§17: $\dot M\vert_{\rm clock}=i(\varpi_1-\varpi_2+\varpi_3)M$, $\dot J_{\rm eff}\vert_{\rm clock}=(\varpi_1-\varpi_2+\varpi_3)\Re M$ | CONFIRMED_EXACT | The stated sign is consistent **only** with $J_{\rm eff}=\Im M$, which is exactly Bridge II §11.2's definition. Consistent, but the report never restates the definition; a reader who assumes $J_{\rm eff}=\Re M$ will read a sign error that is not there. `F3a,F3b` — flagged as WORDING_CORRECTION. |
| R67 | §11: a shared rate changes $J_{\rm eff}$ while leaving $Z$ fixed | CONFIRMED_EXACT | Numerical witness. $J_{\rm eff}$ is therefore a phase-reference-sensitive diagnostic: useful **only** if an external reference is derived, gauge-dependent otherwise. `F3c` |
| R68 | §12.1: $C_{U(3)}(L_3)=U(1)\times U(2)$ and the three-row joint-centralizer table | CONFIRMED_EXACT | Commutant dimensions computed exactly as null spaces of $I\otimes M-M^{\!\top}\!\otimes I$: $5,2,1$, i.e. $U(1)\times U(2)$, $U(1)\times U(1)$, $U(1)$. The $(e_+,e_-,e_3)$ structure $\operatorname{diag}(a,b,a)$ is confirmed and $\operatorname{diag}(a,b,b)$ is confirmed to fail. `F4a–F4d` |
| R69 | §12.1: the adjoint argument (commuting with $gL_3-iD$ forces commuting with both parts) | CONFIRMED_EXACT | Valid because $U$ is unitary, so $UXU^*=X\Rightarrow UX^*U^*=X^*$. |
| R70 | §12.2 (12.1): equation symmetry condition $D(U\Omega)U\Omega=UD(\Omega)\Omega$ | CONFIRMED_EXACT | |
| R71 | §12.2: identical strictly monotone $\nu(I_i)$ gives exactly $U(1)^3\rtimes S_3$ | CONFIRMED_WITH_ASSUMPTION | Monomial matrices verified to be symmetries; generic unitaries verified not to be; the one-channel witness is the right forcing argument. The assumption the report notes in passing — that $\nu$ extends continuously to $I=0$ so the witness state is admissible — is load-bearing and deserves to be stated as a hypothesis, not a parenthesis. `F5a–F5c` |
| R72 | §12.2: intersection with $C(L_3)$ is $U(1)\times S_3$; in $SU(3)$ a group of 18 elements | CONFIRMED_EXACT | Monomials commuting with $L_3$ are exactly scalar$\times$permutation; the $SU(3)$ count is 18. `F5d,F5e` |
| R73 | §12.2: "shared" alone does not give the clock a $U(3)$ symmetry | CONFIRMED_EXACT | A labelled face action is not even $S_3$-invariant. `K4,K4b` |
| R74 | §13: nonisochronous Stuart–Landau identification $\dot z=(\varepsilon k+i\omega_0)z-(\varepsilon-i\alpha/2)\lvert z\rvert^2z$ | CONFIRMED_EXACT | Algebraic identity. `G1a,G1b` |
| R75 | §13: with $K=0$ the system is a discrete cubic CGLE on $K_3$ | CONFIRMED_EXACT | $L_3=-3P_\perp$ is minus the $K_3$ graph Laplacian and $g$ is real, so this is the real-diffusion special case of the cubic complex-oscillator network. `G1c` |
| R76 | §13: $\vartheta=\phi-\tfrac cb\log r$ removes the amplitude dependence from the **isolated** phase rate, and is canonical | CONFIRMED_EXACT | $\dot\vartheta=\omega-ca/b$. The shift depends only on $I$, so $dI\wedge d\vartheta=dI\wedge d\phi$. `F6a,F6b` |
| R77 | §13: general condition $h'=(\varpi_\ast-\varpi)/F$; coupling reintroduces the radial information | CONFIRMED_EXACT | After the shift every $\delta_{ji}$ acquires $h(I_j)-h(I_i)$. `F6c,F6d` |
| R78 | §13/§14: novelty tables and falsification ledger | CONFIRMED_WITH_ASSUMPTION | Every entry that this review tested held. §20 below states the strongest scoped novelty statement the mathematics supports. |
| R79 | §15: 63 tracked files and five PDF hashes preserved | CONFIRMED_EXACT | Independently re-verified on the device: 62 files in `SHA256SUMS.txt` (which excludes itself) all match; all five PDF hashes match. |
| N1 | §7.3 gives only a witness value | NEW_DERIVED_COROLLARY | Closed-form general threshold (§15 below). |
| N2 | §8.3 / §10.1 | NEW_DERIVED_COROLLARY | Trichotomy for H1 in the advancing regime; (8.7) is vacuous exactly where H1 needs it (§9 below). |
| N3 | §8.2 | NEW_DERIVED_COROLLARY | The full integrating-factor family $G(F-\nu U)/(1-\rho)$. |
| N4 | §6 | NEW_DERIVED_COROLLARY | Exact invariant manifolds and an action-transfer constraint (§22 below). |
| N5 | §7.3 | NEW_DERIVED_COROLLARY | The nonlinear outcome past the threshold: transfer to the in-phase branch. |
| N6 | §10.1 | NEW_DERIVED_COROLLARY | Defective-monodromy conditioning as a candidate source of the historical numerical instability reading. |

---

## 2. First attack: action–angle coordinates and sign conventions

Independently re-derived. The map $(I,\phi)\mapsto(q,p)=(\sqrt{2I}\cos\phi,\sqrt{2I}\sin\phi)$
has Jacobian determinant identically $1$, so $dq\wedge dp=dI\wedge d\phi$ with **no** orientation
or wedge-sign freedom left over once the frozen $\sigma=\sum dq_i\wedge dp_i$ is fixed. The
Bridge-I/II complex structure $J_i=n_i\times\cdot$ fixes $\sigma_i=g(J_i\cdot,\cdot)=dq\wedge dp$
exactly (Codex C02), so the orientation input is the ambient right-handed orientation plus the
outward normals — geometry, not preference.

Contracting $\iota_X\sigma=\sum(\dot I_i\,d\phi_i-\dot\phi_i\,dI_i)$ against
$dH=\sum(\partial_{I_i}H\,dI_i+\partial_{\phi_i}H\,d\phi_i)$ gives
$\dot I_i=\partial_{\phi_i}H$, $\dot\phi_i=-\partial_{I_i}H$. **I try and fail to construct a
sign counterexample**: the assignment is forced because in this convention $(I,\phi)$ occupy the
$(q,p)$ slots, not the textbook $(\text{momentum},\text{angle})$ slots. Flipping either the
orientation of $\sigma$ or the Hamilton convention flips both equations together, leaving
$H=\sum\nu_iI_i\Rightarrow\dot\phi_i=-\nu_i$ consistent with Bridge II's $\dot\Omega=-i\nu\Omega$
in either case.

The renaming $\varpi_i=\dot\phi_i=-\nu_i$ is not cosmetic: it **repairs** the Bridge-II
internal conflict recorded as Codex C05 (its §3 derives $-i\nu\Omega$, its §7 writes $+i\nu\Omega$).
Bridge III is self-consistent throughout under $\varpi$.

$d\phi=(q\,dp-p\,dq)/(q^2+p^2)$ is closed with period exactly $2\pi$ — closed, not exact. The
coordinates are therefore global on $\mathcal D=(\mathbb C\setminus\{0\})^3$ with circle-valued
angles; $\sigma$ descends to the cylinder because $dI\wedge d\phi$ is well defined there even
though no global $\phi$ function exists. The report states this correctly. The topological
qualification the report does *not* make explicit is the general one: a symplectic vector field
on $((0,\infty)\times S^1)^3$ need only be **locally** Hamiltonian, the obstruction living in
$H^1$; for the angle-independent rates of §4.2 that obstruction vanishes because $\alpha=\sum
\varpi_i\,dI_i$ has no $d\phi$ component. Where it does not vanish — H1 with
$\int_0^{2\pi}S\ne0$ — the report handles it correctly in §8.2.

At $I_i=0$ the chart is singular but the Cartesian field need not be. The report's distinction
is exact and I verified both halves: $i\varpi(\lvert z\rvert^2/2)z$ extends smoothly, while
$K\sin 3(\phi_j-\phi_i)$ has three different limits along three different rays into $z_i=0$.

```
ACTION_ANGLE_FORM = CONFIRMED_EXACT  sigma = sum dI_i ^ dphi_i, Jacobian determinant identically 1
HAMILTON_SIGN     = CONFIRMED_EXACT  Idot = +dH/dphi, phidot = -dH/dI; forced by the frozen
                                     convention, not chosen; no sign counterexample exists
GLOBAL_DOMAIN     = CONFIRMED_EXACT  globally symplectic diffeomorphism on the punctured plane
                                     ((0,inf) x S^1)^3 -> (C\{0})^3; circle-valued angles, no
                                     global real Arg; local-vs-global Hamiltonian obstruction is
                                     H^1 and vanishes for angle-independent rates
ZERO_STRATUM      = CONFIRMED_EXACT  codimension 2m, polar chart singular, Cartesian field smooth
                                     for radial rates but NOT for the harmonic-3 phase term
```

---

## 3. The recursive-phase Hamiltonian theorem

The single-channel result is exact and the minus sign is right. The multi-action criterion
$\partial_{I_j}\varpi_i=\partial_{I_i}\varpi_j$ is necessary and sufficient, with two hypotheses
the report leans on without naming:

* **Regularity.** Necessity uses equality of mixed partials of $H$. With $\varpi\in C^1$ this is
  automatic ($H\in C^2$); for merely continuous $\varpi$ the criterion is not even defined. The
  report says "smooth", so the theorem is safe, but "exactly when" is a $C^1$ statement.
* **Convention relativity.** The theorem is about Hamiltonians for the **frozen** $\sigma$. §4.3
  says "in this fixed form"; §4.2 does not. A rate field that is not closed can still be
  symplectic for some other structure. This is a `WORDING_CORRECTION`, not a defect.

I attacked the counterexamples and they hold. $w=\sum I_i^2$ has $\partial_{I_2}w-\partial_{I_1}w
=2(I_2-I_1)$, nonzero off the equal-action locus. Normalized weights $\varpi_i=I_i/N$ give
$\partial_{I_2}\varpi_1=-I_1/N^2$ against $\partial_{I_1}\varpi_2=-I_2/N^2$. Both are genuine.

The common-rate theorem survives a determined attack on its **global** step. Closedness forces
$\nabla w\parallel(1,1,1)$, so $dw$ annihilates every direction with $\sum dI_i=0$; hence $w$ is
constant on connected components of $\{N=\text{const}\}$. On the positive orthant those
components are open simplices — connected — so $w=f(N)$ globally, not merely locally. On a
non-simply-connected or disconnected action domain the conclusion can fail, and the report
correctly says "on other domains exactness must be checked separately".

Zero-action boundaries: the theorem lives on the open orthant. Nothing here extends it to the
stratum, and the report does not claim it does.

```
LOCAL_RECURSIVE_HAMILTONIAN = CONFIRMED_EXACT
                              H(I) = -sum[ omega_i^(0) I_i + kappa int^{I_i} W_i(r_i(s)) ds ] + C
                              is the entire angle-independent family; minus sign confirmed
MULTI_ACTION_INTEGRABILITY  = CONFIRMED_WITH_ASSUMPTION
                              closedness d_Ij varpi_i = d_Ii varpi_j is necessary and sufficient,
                              for C^1 rates, relative to the frozen sigma, on a simply connected
                              action domain; globally sufficient on the positive orthant
COMMON_RATE_THEOREM         = CONFIRMED_EXACT
                              every varpi_i = w(I) Hamiltonian  <=>  w = f(N), N = sum I_i,
                              globally on the positive orthant; both counterexamples verified
```

---

## 4. The shared-clock removability theorem

Re-derived from scratch. With $\Omega=e^{-i\Theta}\Psi$ and common-phase equivariance,
$\dot\Psi=A_0(\Psi)+i[w+\dot\Theta]\Psi$; $\dot\Theta=-w$ removes the term. The essential
observation — which the report makes and which I confirm — is that the clock term is **vertical**,
tangent to the common-phase group orbit, so the induced field on the quotient is literally
unchanged, not merely conjugate. Invariant observables therefore evolve identically at the same
$t$: this is equation equivalence *and* observable equivalence for the invariant algebra.

The three notions must stay separate:

| Level | Status |
|---|---|
| **Equation equivalence** | Exact, on the quotient, under equivariance of $A_0$ and phase-invariance of $\rho_{\rm shared}$. |
| **Observable equivalence** | Exact **for phase-invariant observables only** ($I_i$, $\bar\Omega_i\Omega_j$, relative phases, $Z_{\rm chiral}$). Not for $\Re\Omega_i$, a phase against a supplied reference, or the literal $J_{\rm eff}$. |
| **Physical-clock equivalence** | Not established, and not establishable from these sources: it would require a derived phase reference. The report is right to refuse it. |

Failure conditions, each checked:

1. **$\rho_{\rm shared}$ depends on the global phase** — the quotient field is still unchanged
   (the term remains vertical), so *quotient* invisibility survives; what fails is closure of the
   lifted system. The report's phrasing is correct and this is a subtle point worth preserving.
2. **An auxiliary $\rho$ with its own absolute-phase equation** — fails. This is exactly H1:
   $\dot\rho=\nu(1-\rho)S(\phi)$ makes $\rho$ a non-invariant observable, so rotating the phase
   away reintroduces it inside $f$. The invisibility theorem genuinely does not cover H1.
3. **Explicit forcing / a fixed complex drive** — fails; equivariance of $A_0$ is broken.
4. **Non-equivariant observables** — fails at the observable level, not the equation level.
5. **Zero components** — the quotient is not a manifold on the zero stratum; the argument holds
   on $\mathcal D$ only.
6. **Time-dependent external references** — fails; the reference is extra non-equivariant state.
7. **State-dependent but global common rate** — succeeds, provided the state dependence is through
   a phase-invariant function. "Shared" alone is not enough: a labelled face action is not even
   permutation-invariant (verified).
8. **Rate depending on history** — fails; a history functional is extra state and is not covered.

```
SHARED_CLOCK_REMOVABLE_AS_EQUATION      = CONFIRMED_EXACT on the common-phase quotient, given
                                          common-phase equivariance of A_0
SHARED_CLOCK_OBSERVATIONALLY_INVISIBLE  = CONFIRMED_WITH_ASSUMPTION — for phase-invariant
                                          observables only; NOT physical-clock equivalence
FAILURE_CONDITIONS = auxiliary absolute-phase feedback (H1 itself); explicit forcing or a fixed
                     complex drive; any supplied external phase reference; non-invariant
                     readouts including the literal J_eff; the zero stratum; history-dependent
                     rates. A global phase dependence in rho_shared alone does NOT break quotient
                     invisibility — it breaks closure of the lift.
```

---

## 5. Independent derivation of the Paper-A action–angle equations

Derived from $\dot\Omega_i=\varepsilon\Omega_i(k_i-\lvert\Omega_i\rvert^2)+g(L_3\Omega)_i$ with
$L_3$ read directly from the frozen `kernel_physics/dynamics.py`, using
$\dot I_i=\Re(\bar\Omega_i\dot\Omega_i)$ and $\dot\phi_i=\Im(\bar\Omega_i\dot\Omega_i)/(2I_i)$,
**before** comparing to the report. Both equations match term for term.

The factors are forced, not chosen:

* the $2$ in $2\varepsilon I_i(k_i-2I_i)$ comes from $\lvert\Omega_i\rvert^2=2I_i$ in two places;
  replacing it with $3$ breaks the identity (checked);
* the $-4gI_i$ is exactly the diagonal $-2\Omega_i$ of $L_3$, which contributes to the amplitude
  only (its imaginary part against $\bar\Omega_i$ vanishes);
* the $2g\sqrt{I_iI_j}$ is $g\,r_ir_j$ with $r=\sqrt{2I}$;
* the phase sign is $\delta_{ji}=\phi_j-\phi_i$ throughout, consistently.

Zero-action limits: (6.1) extends continuously to $I_i=0$; (6.2) does not — $\sqrt{I_j/I_i}$
blows up — but the underlying Cartesian field $g(L_3\Omega)_i$ is perfectly smooth there. This is
a chart artefact for the $L_3$ term, in contrast to the genuine non-smoothness of the harmonic-3
term. The report draws this distinction correctly.

The total-action identity is exact, and the derivation shows *why* no phase term survives
separately: the $-4gI_i$ and the $\cos\delta$ terms regroup precisely into
$\sum_{i<j}\lvert\Omega_i-\Omega_j\rvert^2$.

```
PAPER_A_POLAR_PARENT   = CONFIRMED_EXACT on the nonzero domain; every coefficient, every factor
                         of 2, the diagonal L_3 contribution and the phase sign reproduced
                         independently
TOTAL_ACTION_IDENTITY  = CONFIRMED_EXACT
                         d/dt sum I_i = 2 eps sum I_i(k_i - 2 I_i) - g sum_{i<j} |Om_i - Om_j|^2
                         no phase term contributes directly; no normalization is imposed
```

---

## 6. The claimed recursive loop

Answered with equations, not terminology.

1. **$\varpi'(I)=0$.** Then $c=r^2\varpi'(I_\ast)=0$ and the lower-left block of (7.1) dies. The
   transverse characteristic equation loses its $gcs$ term entirely and the spectrum becomes
   $\alpha$-independent. The forward arrow $I\to\varpi$ is dead and the clock reduces to a common
   constant rate, removable by a rotating frame.
2. **$g=0$.** Then $\partial F_i/\partial\phi_j\equiv0$ **and** $\partial F_i/\partial I_j\equiv0$
   for $j\ne i$ (verified symbolically): the action equations decouple completely and no longer
   see the phases. The return arrow $\delta\phi\to I$ is dead. Crucially, $K$ **cannot** restore
   it: the third-harmonic term is amplitude-preserving by construction. **The entire loop is
   carried by the first-harmonic $L_3$ coupling.**
3. **All $I_i$ equal.** Then all $\varpi_i$ coincide, the clock is common on that set, and §5
   removes it. On the $120^\circ$ orbit the actions *are* equal (verified: $I=(1.5,1.5,1.5)$), so
   every $\alpha$-dependence in §7.3 is strictly off-orbit. The equal-action set is not invariant
   in general, which is why the effect is transverse rather than absent.
4. **Can a phase coordinate remove $\varpi(I)$?** For an isolated oscillator, yes:
   $\vartheta=\phi+h(I)$ with $h'=(\varpi_\ast-\varpi)/F$, which for the cubic case is exactly
   $-\tfrac cb\log r$ — the asymptotic-phase (isochron) coordinate. It is canonical.
5. **Where does the state dependence reappear?** In every coupling term: $\delta_{ji}\mapsto
   \delta_{ji}+h(I_j)-h(I_i)$, so both $g\sqrt{I_j/I_i}\sin\delta_{ji}$ and $K\sin3\delta_{ji}$
   and the $\cos\delta_{ji}$ in (6.1) become amplitude-dependent.
6. **Does coupling prevent global removal?** Yes, and there is an invariant witness. Eigenvalues
   of a linearisation at a relative equilibrium are invariant under every smooth change of
   coordinates and under the group reduction. The family parameterised by $\alpha$ shares the
   same orbit, the same actions, the same geometry and the same on-orbit rate, yet its transverse
   eigenvalues move with $\alpha$ and cross the imaginary axis at $\lvert\alpha\rvert=4\sqrt{14}$.
   No coordinate change can carry one member of that family to another near that orbit.
7. **Structurally distinct from standard nonisochronous coupling?** No. The invariant that carries
   the distinction is $c=r^2\varpi'(I_\ast)$, i.e. the shear/nonisochronicity coefficient; with
   affine $\varpi$ the whole system is *exactly* a discrete cubic CGLE on $K_3$.

```
CLASSIFICATION (regime dependent; more than one applies):

  COORDINATE_ARTIFACT              : isolated channel, or g = 0, or varpi' = 0.
                                     The loop is removable by a canonical phase shift and the
                                     spectrum is independent of the clock.
  KNOWN_NONISOCHRONOUS_FEEDBACK    : g != 0 and varpi' != 0.  The loop is mathematically real
                                     and NOT removable (invariant witness: the transverse
                                     eigenvalues at the 120-degree relative equilibrium), but it
                                     IS the standard amplitude-phase shear mechanism.
  STRUCTURALLY_DISTINCT_COUPLED_EFFECT : NOT ESTABLISHED.  No invariant was found that separates
                                     the construction from nonisochronous coupled-oscillator
                                     theory.
  UNRESOLVED                       : the cases with genuinely extra state (an independent rho
                                     with its own law, H4-type filtered memory, a history
                                     functional).  These are not specified, so nothing is decided.
```

---

## 7. H1's logarithmic canonical embedding

Every step verified. $y=-\log(1-\rho)$ gives $\dot y=\nu S(\phi)$ exactly; $I=I_\ast y$ maps
$0<\rho<1$ onto $I>0$; $dI\wedge d\phi=I_\ast\,d\rho\wedge d\phi/(1-\rho)$; and (8.4) reproduces
both of (8.1) under the frozen convention, including the push-forward
$\dot\rho=e^{-I/I_\ast}\dot I/I_\ast$.

**Attack on the scale $I_\ast$.** The report calls it "arbitrary". It is arbitrary in a precise
and slightly stronger sense than stated: $H_{I_\ast}(I_\ast y)=I_\ast\,H_1(y)$ while
$\sigma=dI\wedge d\phi=I_\ast\,dy\wedge d\phi$. The **pair** $(\sigma,H)$ scales by the same
factor, so the vector field is exactly $I_\ast$-independent. $I_\ast$ is pure gauge for the
dynamics; it is a genuine choice only for the physical identification $\Omega=\sqrt{2I}e^{i\phi}$.

**Attack on uniqueness of the chart.** This is where the report is weakest, and I can make its own
caveat precise. Every two-dimensional field is locally Hamiltonian after multiplication by a
Jacobi last multiplier, and the multiplier is far from unique. The **complete** family here is

$$M(\rho,\phi)=\frac{G\big(F(\rho)-\nu U(\phi)\big)}{1-\rho},\qquad G \text{ arbitrary},$$

verified to satisfy $\operatorname{div}(MX)=0$ identically. Each $G$ gives a different exact
canonical embedding. So the logarithmic chart is not merely "one choice with a free positive
scale"; it is one member of an infinite-dimensional family, and geometry selects none of them.
This strengthens rather than weakens the report's honesty, but it should be said.

**Domain and boundary.** $\rho=1$: $I$ diverges, the chart does not cover it, and the boundary
orbit must be treated separately (the report does). $\rho=0$: $I\to0$ and the historical boundary
circle collapses to the origin — not an invertible extension. $\rho<0$: the chart is perfectly
fine, which is why the multiplier theorem is stronger than the report claims (§9 below).
$\rho=1$ is forward invariant; $\rho=0$ is not, and I exhibited parameters ($E_0=0.2$, $A=2$)
where $\nu S<0$ somewhere and trajectories leave $[0,1]$.

**Single-valuedness.** $U(\phi)=\int^\phi S$ is $2\pi$-periodic iff $\int_0^{2\pi}S=0$; otherwise
$H$ carries a term $\nu I_\ast\langle S\rangle\phi$ and is multivalued on the cylinder while the
field itself still descends and is still symplectic. Equivalently $\iota_X\sigma$ has circle
period $\nu I_\ast\int_0^{2\pi}S\ne0$. All correct.

```
H1_LOGARITHMIC_CANONICAL_EMBEDDING = CONFIRMED_EXACT on 0 < rho < 1 (and in fact on rho < 1),
                                     conditional on choosing this chart
GLOBAL_HAMILTONIAN_CONDITION       = CONFIRMED_EXACT — single valued on the phase cylinder
                                     exactly when nu * int_0^{2pi} S(phi) dphi = 0; otherwise the
                                     field is symplectic but H is only local/multivalued
BOUNDARY_EXTENSION                 = CONFIRMED_EXACT — no invertible extension to rho = 0
                                     (circle collapses to I = 0) and none to rho = 1 (I diverges);
                                     [0,1] forward invariant only under nu S >= 0
SCALE_FREEDOM                      = CONFIRMED_EXACT and sharpened: (sigma, H) scale together so
                                     I* is pure gauge; and the chart is one of the infinite family
                                     M = G(F - nu U)/(1-rho)   [NEW_DERIVED_COROLLARY N3]
```

---

## 8. H1's first integral

$\frac{d}{dt}[F(\rho)-\nu U(\phi)]=\frac{v}{1-\rho}\nu(1-\rho)S-\nu S v=0$ identically. Verified.

Three refinements the report does not state:

* **It is the Hamiltonian.** $H_{\rm hist}=-I_\ast[F(\rho)-\nu U(\phi)]$, because
  $\int^I v(1-e^{-s/I_\ast})ds = I_\ast\!\int^\rho v(s)\,ds/(1-s)$. So the first integral and the
  Hamiltonian are one object, and the multivaluedness of §7 applies to **both**. The integral is
  a genuine global first integral on the cylinder exactly when $\int_0^{2\pi}S=0$; otherwise it
  is single-valued only on the phase cover.
* **$F$ exists wherever $v$ is continuous and $\rho<1$**; monotonicity ($F'>0$) requires $v>0$
  and is *not* needed for the no-fixed-point conclusion of the return map — only $\nu\hat S\ne0$
  is. Where $v$ changes sign, $F$ has a critical point at $v(\rho)=0$, which is precisely where
  the interior equilibria (centres or saddles) live.
* **Integrability.** With one first integral in two dimensions the system is integrable, so no
  chaos and no positive Lyapunov exponent are possible in the interior. Level sets of
  $F-\nu U$ are the orbits. This — not only (8.7) — is the deep reason H1's interior cannot host
  a recursive exponential instability.

```
H1_FIRST_INTEGRAL     = CONFIRMED_EXACT; and it equals -H_hist/I*, the same object as (8.4)
DOMAIN                = rho < 1 with v continuous; globally single valued on the cylinder iff
                        int_0^{2pi} S = 0, otherwise only on the phase cover.  Monotonicity of F
                        requires v > 0 and is NOT needed for the return-map conclusion
DYNAMICAL_CONSEQUENCE = the interior system is integrable: orbits are level sets, no chaos and no
                        positive Lyapunov exponent in the interior; a critical point of F occurs
                        exactly where v = 0, which is where the interior centres/saddles are
```

---

## 9. Critical theorem: two unit Floquet multipliers

This is the report's strongest correction and it survives the hardest attack in this review.

**Method A (transformed divergence).** In $(y,\phi)$ the field is $(\nu S(\phi),\,v(1-e^{-y}))$,
whose divergence is $0+0=0$ identically. By Liouville the variational determinant is $1$.

**Method B (autonomous periodic orbit, original coordinates).** $\operatorname{div}X=-\nu S(\phi)$,
and along trajectories $-\nu S(\phi)=\frac{d}{dt}\log(1-\rho)$, so
$\oint\operatorname{div}X\,dt=\log(1-\rho(T))-\log(1-\rho(0))=0$ for any closed orbit, giving
$\det\Phi(T)=\mu_1\mu_2=1$. A nonstationary solution of an autonomous system has its velocity as
a $T$-periodic variational solution, so $\mu_1=1$; hence $\mu_2=1$. Note Method B needs no chart
at all, so the coordinate change is a convenience, not a hypothesis.

**Counterexample search.** I integrated the variational system directly for
(i) rotating interior orbits with $E_0=0$ (so $\langle S\rangle=\sin E_0 J_0(A)=0$ exactly),
(ii) librating orbits around an interior centre ($v$ changing sign, eigenvalues $\pm i/2$),
(iii) an orbit with $\rho_0=-0.7$, and
(iv) 60 randomized parameter draws including $\nu<0$, $\kappa<0$, warp steepness $\alpha_W\in[1,6]$
and negative $\rho$.
No counterexample. Worst deviation $\max(\lvert\det-1\rvert,\lvert\operatorname{tr}-2\rvert)
=9\times10^{-12}$.

**Hypotheses that actually matter**, each tested: nonstationarity (an equilibrium is excluded, and
equilibria genuinely can be saddles); the orbit staying in a compact subset of $\rho<1$; phase
periodicity mod $2\pi$; winding number is **not** an obstruction (the velocity field is a function
of $(\rho,\phi \bmod 2\pi)$, so it is $T$-periodic whatever the winding); and the coordinate
derivative $1/(1-\rho)$ is periodic, bounded and boundedly invertible on a compact interior orbit.

**Jordan block.** $\mu_1=\mu_2=1$ leaves two possibilities. In the witness the monodromy is
$\left(\begin{smallmatrix}1&0\\2.82&1\end{smallmatrix}\right)$ — a nontrivial shear — and the
period does vary across the family ($T=6.077$ at $\rho_0=0.3$ versus $5.124$ at $\rho_0=0.6$),
which is exactly the source of the shear.

### NEW_DERIVED_COROLLARY N2 — the theorem is vacuous where H1 needs it

Suppose $v>0$ on the visited range (H1's strictly advancing "rapid clock" regime) and let
$\hat S=\int_0^{2\pi}S(\phi)\,d\phi=2\pi\sin E_0\,J_0(A)$. A periodic orbit must wind, so
$F(\rho)$ returns while changing by $\nu\hat S$ per turn. Therefore:

| | |
|---|---|
| $\hat S=0$ | **Every** interior orbit is periodic; the interior is foliated by closed orbits; the return map is the identity; $\mu_1=\mu_2=1$ with a generically nontrivial Jordan block. |
| $\nu\hat S>0$ | **No interior periodic orbit exists at all.** $F$ increases monotonically per turn and every interior trajectory converges to the boundary orbit $\rho=1$, which is linearly attracting with multipliers $\{1,\exp(-\nu\hat S/v(1))\}$. |
| $\nu\hat S<0$ | **No interior periodic orbit exists at all.** $F$ decreases per turn; $\rho$ leaves $[0,1]$ through the non-invariant boundary $\rho=0$. |

Verified numerically over 40 return-map iterations in each case (monotone increase to
$\rho=1.0000000$; monotone decrease past $\rho=0$; identity return to $6\times10^{-11}$).

Two consequences that strengthen §10.1 considerably:

* In the advancing regime the asymptotic fate is decided by $\operatorname{sign}(\nu\hat S)$
  **alone** — it does not depend on $\kappa$, on $W$, or on the warp steepness. Increasing
  $\kappa$ by a factor of 19 changes the rate of approach and nothing else (verified). Any
  proposed instability threshold of the form "$\kappa$ exceeding some multiple of $\omega$" is
  therefore refuted structurally, not merely because its proof is incomplete.
* Under H1's **own** forward-invariance requirement $\nu S\ge0$, $\hat S>0$ strictly unless
  $S\equiv0$ — so the interior contains no periodic orbits whatsoever and (8.7) has an empty
  hypothesis set in exactly the regime H1 assumes. Interior periodic orbits survive only on the
  codimension-one set $\sin E_0 J_0(A)=0$, or in the librating regime where $v$ changes sign,
  which lies outside a strictly advancing clock.

### NEW_DERIVED_COROLLARY N6 — a numerical caution

A monodromy with $\mu_1=\mu_2=1$ and a nontrivial Jordan block is **defective**: eigenvalue
extraction is ill-conditioned with a $\sqrt{\epsilon}$ law. In this review's own witness, an
orbit whose multipliers are exactly $1$ returned numerical eigenvalues $1\pm2.4\times10^{-6}i$
from a monodromy accurate to $6\times10^{-12}$ in trace and determinant. The well-conditioned
test is $\det=1$ and $\operatorname{tr}=2$.

This is a concrete, checkable candidate explanation for a historical numerical reading of "a
Floquet multiplier slightly above one" in H1's interior. It is offered as a hypothesis, not a
finding: H1's data, parameters and code were not recovered, and nothing here determines what was
actually computed.

```
H1_INTERIOR_PERIODIC_MULTIPLIERS   = CONFIRMED_EXACT, mu_1 = mu_2 = 1, by two independent
                                     derivations plus direct numerical monodromy and a 60-draw
                                     counterexample search; scope WIDENED to the whole chart
                                     rho < 1 (the report states 0 < rho < 1)
POSITIVE_FLOQUET_EXPONENT_ALLOWED  = NO for regular interior periodic orbits (exponents are
                                     exactly zero).  Not excluded at the boundary rho = 1, at
                                     interior saddles, in a discrete model, or with extra state.
FINITE_TIME_AMPLIFICATION_ALLOWED  = YES — Jordan shear gives unbounded polynomial (linear-in-n)
                                     growth and arbitrary transient gain; (8.7) rules out
                                     exponential asymptotic growth ONLY.  It does not rule out
                                     nonlinear instability, boundary instability, discrete-model
                                     instability, or instability from additional state.
```

---

## 10. The exact return-map theorem

$F(\mathcal P(\rho_0))=F(\rho_0)+\nu\int_0^{2\pi}S$ verified analytically and numerically. With
$\hat S=0$ the return map is the identity wherever the full turn exists (drift $6\times10^{-11}$
over 40 turns). With $\hat S\ne0$ there is no interior fixed point — and, by N2, no interior
periodic orbit at all, which is the stronger statement.

Monotonicity of $F$ is not required for the no-fixed-point conclusion; it is automatic in the
regime where the return map is defined. $\langle S\rangle=\sin E_0\,J_0(A)$ was confirmed to nine
digits, and the report is right that only the integral, not the Bessel representation, is needed.

Global definedness: the return map exists only while the trajectory completes a turn inside the
domain, which by N2 fails eventually whenever $\nu\hat S\ne0$. Approach to the boundary is
geometric in the turn index, $1-\rho\sim e^{-\text{const}\cdot n}$, so the boundary is reached
only asymptotically.

```
RETURN_MAP_IDENTITY            = CONFIRMED_EXACT
INTERIOR_FIXED_POINT_CONDITION = CONFIRMED_EXACT and sharpened: an interior fixed point requires
                                 nu * int_0^{2pi} S = 0, and in that case EVERY interior point is
                                 fixed (the return map is the identity).  There is no intermediate
                                 case with isolated interior fixed points.
```

---

## 11. The repaired commutator theorem

Direct multiplication confirms (9.2) entry by entry. The commutator is **traceless**, which is
the decisive structural point: H1's printed form has zero diagonal and both off-diagonals
sign-flipped, and reversing the commutator order flips **all four** entries, so no choice of
convention can produce a zero diagonal. The report's diagnosis is exactly right.

The rank criterion is correct and, in my view, the cleanest new lemma in the report. The proof is
the right one: the three independent entries of (9.2) are, up to sign, precisely the three
$2\times2$ minors of $\begin{pmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\end{pmatrix}$, and simultaneous
vanishing of all $2\times2$ minors is linear dependence. Pairwise dependence across a family with
one nonzero member forces a one-dimensional span.

Tested exhaustively on $5^6=15{,}625$ integer pairs: commuting $\iff$ rank $\le1$, zero
mismatches. Every degenerate case in the work order behaves as predicted: the zero matrix
commutes with everything; $c=0$ with non-proportional $(a,b)$ does not commute; fixed nonzero $c$
with $a_1\ne a_2$ does not commute; $b=c=0$ commutes for arbitrary $a(t)$; $\mathcal J(t)=h(t)
\mathcal J_0$ commutes. Isolated zero times are harmless, because the zero vector is dependent on
every vector — the criterion is about the span of the whole set. Piecewise definitions likewise
reduce to the span condition. Both printed counterexamples reproduce exactly.

```
COMMUTATOR_FORMULA               = CONFIRMED_EXACT (traceless; H1 Eq.(76)/(80) form is not a
                                   commutator of this family under either ordering)
PAIRWISE_COMMUTING_RANK_CRITERION = CONFIRMED_EXACT, necessary and sufficient; recommended as a
                                   standalone lemma.  Verified by exhaustive integer sweep and on
                                   every degenerate case.
```

---

## 12. The triangular propagator claims

Both fundamental matrices satisfy $\dot\Phi=\mathcal J\Phi$ identically (checked symbolically,
with $A'=a$ substituted). Because each is triangular, its eigenvalues are the diagonal entries
$e^{A(T)}$ and $1$ — **always**, with no commutation hypothesis.

Noncommuting triangular generators therefore give the same multipliers: verified numerically by
integrating a genuinely time-dependent triangular system forward and with time reversed. The
multipliers agree to $10^{-9}$ while the shear entry changes from $7.14$ to $12.92$. Time ordering
moves eigenvectors and transient gain, not the Floquet spectrum.

Shear and polynomial growth: with $A(T)=0$ both multipliers are $1$ and $\lVert\Phi(T)^n\rVert$
grows linearly in $n$ (measured ratio $9.999$ over a decade). Transient amplification within one
period is unbounded in the coefficient size.

The report's framing — "the rank criterion characterises commutation; triangularity fixes the
Floquet spectrum without requiring commutation" — is the correct separation, and its observation
that $S'\equiv0$ in H1 makes $a$ constant (a stronger special case than $b=0$) is right and does
not rescue the general lemma.

```
TRIANGULAR_PROPAGATOR      = CONFIRMED_EXACT (both c = 0 and b = 0 forms)
TRIANGULAR_FLOQUET_SPECTRUM = CONFIRMED_EXACT, {exp A(T), 1}, with NO commutation hypothesis;
                              noncommuting triangular generators share the spectrum
TIME_ORDERING_EFFECT       = CONFIRMED_EXACT: changes shear, transient gain and eigenvectors;
                              does not change the multipliers.  A(T) = 0 gives unit multipliers
                              with genuine linear (polynomial) growth.
```

---

## 13. Magnus terms and the time-ordering witness

$\mathcal M_1$, $\mathcal M_2$ and the convergence qualification are standard and correctly
stated; $\int_0^T\lVert\mathcal J\rVert_2\,dt<\pi$ is the sharp sufficient bound. The
$\mathcal J_0+t\mathcal J_1$ example gives $-T^3[\mathcal J_0,\mathcal J_1]/12$, verified by
evaluating the double integral.

The piecewise witness is exact in every particular: $B_j^2=-b_j\mathbf 1$ so
$e^{T_1B_1}=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ and
$e^{T_2B_2}=\left(\begin{smallmatrix}0&2\\-1/2&0\end{smallmatrix}\right)$; the product is exactly
$\operatorname{diag}(-2,-1/2)$; each segment has purely imaginary spectrum ($\pm i$, $\pm2i$);
and — the point that makes it a genuine time-ordering witness rather than an averaging artefact —
the **averaged** generator also has purely imaginary spectrum ($\pm1.414i$). Growth rate
$\log2/(T_1+T_2)=0.29418$.

One addition worth recording: this witness has $\int_0^T\lVert\mathcal J\rVert_2\,dt=4.712>\pi$,
so it lies outside the sufficient Magnus convergence ball. That is consistent with — and explains
— why a truncated Magnus series cannot be used to predict it, reinforcing the report's warning
that "a finite truncation outside an established error regime is not an exact stability theorem".

Also confirmed: noncommutation is not biconditional with growth in either direction. Noncommuting
generators can integrate to a zero second Magnus term, and a constant Jacobian with no time
ordering at all can be unstable — the smooth feedback example has eigenvalues
$(-a\pm\sqrt{a^2+4b\kappa})/2$ with a positive root whenever $b\kappa>0$, and setting $b=0$
removes it for every $\kappa$.

```
MAGNUS_DISCUSSION                = CONFIRMED_EXACT including the convergence qualification;
                                   the witness lies outside the sufficient convergence ball
TIME_ORDERING_INSTABILITY_WITNESS = CONFIRMED_EXACT, M = diag(-2, -1/2), each segment purely
                                   imaginary, averaged generator purely imaginary, exponent
                                   log 2 / (T1+T2) > 0.  Establishes possibility only; it is an
                                   externally specified system, not a Tri-Octagon trajectory.
```

---

## 14. The historical Floquet-threshold rejection

The report's conclusion is justified, and N2 makes it stronger. Keeping the categories strictly
separate, as the work order requires:

| Category | Verdict |
|---|---|
| Historical analytic proof invalid | **YES, CONFIRMED.** Five independent grounds: magnitude/RMS comparisons do not control signed correlations or a monodromy eigenvalue; the frozen-$\rho$, $\phi=\omega t$ proxy is a different periodic system from the actual orbit; the neglected $W''\dot\rho/W'$ term is not bounded by the proposed scaling; the printed second-order commutator is wrong and the resulting effective matrix also drops a mean lower-left term; and any approximation claiming to describe (8.1) must satisfy (8.7). Independently, N2 shows the asymptotic fate in the advancing regime is $\kappa$- and $W$-independent altogether, so no threshold of that form can exist. |
| Historical numerical observations false | **NOT ESTABLISHED.** Nothing here shows they are false. |
| Historical numerical observations unresolved | **YES.** The data, parameters, boundary handling and code were not recovered and were not rerun. N6 supplies one concrete candidate artefact (defective-monodromy conditioning) without asserting it is the explanation. Clipping at $\rho=0$, a different discrete model, or a boundary effect are equally live. |
| Effect may exist in a discrete model | **OPEN.** (8.7) is a continuous-time statement. A map is not constrained by it. |
| Effect may exist with extra state | **OPEN**, and this is the most promising direction: an independent $\rho$, or H4-type filtered memory, leaves the two-dimensional integrable setting entirely and (8.7) does not apply. |
| Effect may exist at the boundary | **OPEN and partly settled.** The $\rho=1$ orbit has multiplier $\exp(-\nu T\langle S\rangle)$, which exceeds $1$ when $\nu\langle S\rangle<0$. That is a genuine instability — but it is a boundary effect governed by the signed mean of $S$, not by a recursive commutator. |
| Effect may exist in a multi-channel extension | **OPEN, and demonstrated in a different form.** §7.3's $4\sqrt{14}$ is exactly such a multi-channel instability. It is real, it is conditional on the supplied model, and it is not H1's mechanism. |

```
H1_FLOQUET_THRESHOLD_AS_PROOF     = CONTRADICTED as a proved sufficient criterion; and refuted
                                    structurally by N2 (the advancing-regime fate is independent
                                    of kappa and W)
H1_NUMERICAL_CLAIMS               = UNRESOLVED — not disproved, not reproduced, not rerun.
                                    N6 supplies a checkable candidate artefact, not a finding.
RECURSIVE_INSTABILITY_IN_EXTENSIONS = OPEN in discrete models, with extra state, at the boundary,
                                    and in multi-channel extensions (where §7.3 exhibits one).
```

---

## 15. The local-clock stability threshold

Re-derived three independent ways, deliberately **not** starting from the reported quadratic.

**Route 1 — full symbolic $6\times6$ in $(I,\phi)$.** Differentiating (6.3) at
$I_i=r^2/2$, $\phi_i=\theta_i$ with $\varepsilon=g=K=1$, $k=6$, $\varpi(I)=1+\alpha(I-3/2)$ gives
a characteristic polynomial that factors exactly as

$$\lambda(\lambda+6)\Big[\big(\lambda^2+12\lambda+\tfrac{63}{2}\big)^2+\tfrac{81}{4}\alpha^2\Big],$$

i.e. the balanced pair $\{0,-6\}$ and the two conjugate quadratics
$\lambda^2+12\lambda+\tfrac{63}{2}\pm\tfrac{9i}{2}\alpha$ the report states.

**Route 2 — the report's $(x,y)$ reduction.** Its block matrix (7.1) is, symbolically and for
general $\varepsilon,g,K,k,\alpha$, exactly the $(I,\phi)$ Jacobian conjugated by
$\operatorname{diag}(r^2,r^2,r^2,1,1,1)$. The $S$-matrix facts ($S^\top=-S$, $Su=0$,
$S^2=-\tfrac94P_\perp$, eigenvalues $\pm\tfrac32i$) all hold, and $a,d$ are as stated.

**Route 3 — purely Cartesian numerics.** A real six-coordinate rotating-frame field on
$(\Re Z,\Im Z)$, using no polar coordinates, no $S$ matrix and no $L_3$ decomposition. Its
numerical Jacobian reproduces the analytic spectrum to $10^{-9}$ at every $\alpha$ tested,
including exactly at threshold.

**The threshold.** $\lambda=-6\pm\sqrt{(9/2)(1\mp i\alpha)}$ and
$\operatorname{Re}\sqrt z=\tfrac32\sqrt{\sqrt{1+\alpha^2}+1}$, so a root has positive real part
iff $\sqrt{1+\alpha^2}>15$, i.e. $\alpha^2>224$, i.e. $\lvert\alpha\rvert>4\sqrt{14}$. SymPy
returns $4\sqrt{14}$ as the unique positive solution. At equality the pair is exactly imaginary
with $\lvert\omega\rvert=\tfrac32\sqrt{14}=5.612486080$, matching to nine digits.

**Nature of the crossing.** Transversal: $d\operatorname{Re}\lambda/d\alpha=0.187>0$ at
threshold. The crossing pair is simple, separated from every other eigenvalue by $5.61$. Both
chiral orderings have identical spectra (agreement $6.5\times10^{-10}$), as the reflection
$\theta\mapsto-\theta$ sends $S\mapsto-S$ and merely swaps the two conjugate quadratics.

There is always one exact zero eigenvalue — the common-phase group direction. Working in the
group-reduced quotient $(I_1,I_2,I_3,\delta_{21},\delta_{31})$ removes it and leaves exactly
$\{-6\}\cup\{\text{four transverse roots}\}$ (verified at four values of $\alpha$). So the
crossing is a **Hopf bifurcation of a relative equilibrium** — a modulated-wave bifurcation — not
a steady bifurcation. The $\mathbb Z_3$ isotropy acts on the critical eigenspace as a nontrivial
one-dimensional complex irrep, so no forced degeneracy arises.

**Constant-detuning distinction.** I solved the locking equations for general constant detunings
$(w_1,w_2,w_3)$: the exact $120^\circ$ state survives **only** if $w_1=w_2=w_3$. Uniform detuning
gives $c=0$, hence transverse eigenvalues $-6\pm\sqrt{9/2}$, independent of its value. So no
constant-detuning model sharing this orbit, these actions and this on-orbit rate can reproduce
the threshold. The distinction is genuine and coordinate-invariant.

Direct nonlinear confirmation: integrating the group-invariant deviation (actions and relative
phases) from a random perturbation for $T=80$ gives $5.9\times10^{-9}$ below threshold and
$3.1\times10^{4}$ above.

### NEW_DERIVED_COROLLARY N1 — closed-form general threshold

Requiring a purely imaginary root $i\omega$ of $\lambda^2-(a+d)\lambda+\big(ad-\tfrac94g^2+
\tfrac32igc\big)=0$ gives $\omega^2=ad-\tfrac94g^2$ and $(a+d)\omega=\tfrac32gc$. Eliminating
$\omega$:

$$\boxed{\;c^2=(a+d)^2\left[\frac{4ad}{9g^2}-1\right],\qquad
a=-2\varepsilon r^2+\tfrac32 g,\quad d=\tfrac32 g-9K,\quad r^2=k-\frac{3g}{\varepsilon},\quad
c=r^2\varpi'(I_\ast),\;}$$

with critical frequency $\omega=3gc/\big(2(a+d)\big)$. The threshold exists precisely when
$a+d<0$ and $ad>\tfrac94g^2$ (which is also the condition for transverse stability at $c=0$).
At the report's witness parameters this gives $c^2=144\cdot14=2016$, hence
$\alpha=\sqrt{2016}/3=4\sqrt{14}$ and $\lvert\omega\rvert=\tfrac32\sqrt{14}$ — the report's
numbers exactly. Confirmed numerically at three further parameter sets
$(\varepsilon,g,K,k)=(1,0.8,0.5,5)$, $(0.7,1.3,2,9)$ and $(2,0.5,0.25,4)$, where the predicted
$\alpha_{\rm thr}$ is $8.0236$, $18.3075$ and $23.8079$ and the numerical crossing brackets each
to within $1\%$.

### NEW_DERIVED_COROLLARY N5 — what actually happens above the threshold

The report stops at "above threshold: linear instability". Integrating the group-reduced quotient
system past the threshold gives a definite and important answer: at $\alpha=\text{thr}+0.05$,
$+0.25$ and $+1.0$ the trajectory leaves the $120^\circ$ branch and converges to the **in-phase
synchronous branch** $I_i=k/2=3$, $\delta=0$ — which §7.2 proved is linearly stable for *every*
finite slope (re-verified here at $\alpha=25$: quotient eigenvalues $-15,-15,-12,-12,-12$).

Two consequences:

* The local clock does not open a route to anything new in this model. It **selects between two
  pre-existing branches**, both of which are present at $\alpha=0$. There is no new attractor and
  no observed chirality selection.
* No small-amplitude saturated modulated wave was found even at $0.3\%$ past threshold, which is
  evidence **against** a supercritical Hopf. Below threshold the two branches are bistable: a
  perturbation of size $0.01$ decays back to the $120^\circ$ state while one of size $0.2$ escapes
  to the in-phase branch. I was not able to complete the basin-radius-versus-$\alpha$ scaling test
  that would distinguish a subcritical Hopf from a pre-existing global basin boundary, so the
  criticality is reported as **numerically indicated subcritical, not proved**.

```
LOCAL_CLOCK_THRESHOLD        = CONFIRMED_EXACT by three independent derivations
THRESHOLD_VALUE              = |alpha| = 4 sqrt(14) = sqrt(224) ~ 14.96663; critical frequency
                               3 sqrt(14) / 2 ~ 5.61249
                               GENERAL FORM [N1]: c^2 = (a+d)^2 [ 4 a d / (9 g^2) - 1 ]
CONSTANT_DETUNING_DISTINCTION = CONFIRMED_EXACT — a constant-detuning model retaining this exact
                               relative equilibrium must have EQUAL detunings, hence c = 0 and a
                               spectrum independent of the common rate.  The distinction is
                               invariant (eigenvalues at a relative equilibrium are).
BIFURCATION_TYPE             = Hopf-type crossing of a relative equilibrium (modulated wave):
                               transversal (dRe/dalpha = 0.187), simple conjugate pair, no forced
                               Z_3 degeneracy.  CRITICALITY NOT PROVED; numerics indicate
                               subcritical with a global transition to the in-phase branch [N5].
```

---

## 16. Chirality

(11.1) verified identically for all three cyclic indices, and the clock contribution
$\dot Z_i\vert_{\rm clock}=2\sqrt{I_jI_k}\cos(\phi_k-\phi_j)(\varpi_k-\varpi_j)$ follows. The
explicit example reproduces $\alpha(15,-12,3)$ exactly.

The four requested categories, kept strictly apart:

* **`GENERATES_NONZERO_Z`** — YES for local clocks from a $Z=0$ state with **unequal** actions.
  This is phase shearing of an already asymmetric state, not generation from symmetry.
* **`BIASES_ONE_SIGN`** — NOT SHOWN. §7.3 proves the two chiral orderings have *identical*
  spectra. Nothing in the report or in this review biases either.
* **`SPONTANEOUS_SELECTION`** — NOT SHOWN, and not observed. With identical channel laws and
  exactly equal amplitudes and phases, equivariance plus uniqueness preserve $Z=0$. Past the
  $4\sqrt{14}$ threshold the witness model goes to the in-phase branch, where $Z=0$.
* **`BREAKS_SYMMETRY_EXPLICITLY`** — YES, and this is the crucial guard. A nonzero local clock is
  **not** conjugation-equivariant: $\overline{i\varpi(I)\Omega}=-i\varpi(I)\bar\Omega$ (verified
  numerically to $10^{-12}$). A Hamiltonian radial clock alone is time-reversible under
  conjugation; adding gradient damping destroys that. So a selected temporal orientation breaks
  the mirror **explicitly**, and must not be described as spontaneous breaking.

Channel-permutation covariance is intact: $u\cdot Z$ is odd under an odd permutation (verified),
so paired chiral solutions are genuine symmetry images of each other for identical parameters.

No CP language is used anywhere, and none is warranted: there is no charge and no combined
transformation here.

```
Z_CHIRAL_EVOLUTION         = CONFIRMED_EXACT (11.1) and the clock contribution
SHARED_CLOCK_CHIRALITY     = CONFIRMED_EXACT — exactly zero direct contribution; also no indirect
                             effect under §5's equivariance premises
LOCAL_CLOCK_CHIRALITY      = CONFIRMED_EXACT — GENERATES_NONZERO_Z from unequal actions;
                             BREAKS_SYMMETRY_EXPLICITLY (conjugation is not a symmetry of a
                             nonzero clock).  BIASES_ONE_SIGN not shown.
SPONTANEOUS_SELECTION_PROVED = NO.  Not proved, not observed; the symmetric state is preserved and
                             the two chiral branches have identical spectra.
```

---

## 17. $J_{\rm eff}$ clock evolution

$\dot M\vert_{\rm clock}=i(\varpi_1-\varpi_2+\varpi_3)M$ verified symbolically. The report's
$\dot J_{\rm eff}\vert_{\rm clock}=(\varpi_1-\varpi_2+\varpi_3)\Re M$ is **correct**, and is
consistent **only** with $J_{\rm eff}=\Im M$ — which is precisely Bridge II §11.2's definition
$J_{\rm eff}=\Im(\Omega_1\overline{\Omega_2}\Omega_3)$. Since §17 of the work order asks for the
sign to be checked against the Phase Bridge II convention: it checks out. The one improvement is
presentational — the report never restates the definition, so a reader who assumes
$J_{\rm eff}=\Re M$ will see a sign error that does not exist. `WORDING_CORRECTION`.

The distinction the work order asks about is real and I verified it numerically: a common phase
$\Omega\mapsto e^{i\alpha}\Omega$ leaves $Z$ invariant to $10^{-12}$ while moving $J_{\rm eff}$
from $0.0809$ to $-0.0769$. Bridge II's Codex review (C27) already established that $J_{\rm eff}$
alone is not a weight-one complex covariant — its real and imaginary parts mix.

**Verdict on usefulness.** $J_{\rm eff}$ is a **gauge-dependent diagnostic** as things stand, not
a physical observable. It becomes a potentially useful *phase-reference-sensitive* observable only
if a phase reference is independently derived — and no such reference exists in any of the five
historical sources or in Bridge I/II. Until then, a nonzero $\dot J_{\rm eff}$ reports the choice
of frame as much as the state. The report is right not to use it as feedback and right to refuse
a physical decision here.

---

## 18. Unitary carrier symmetry

**Fixed-frequency joint centralizers.** I computed the commutant dimensions exactly, as null
spaces of $\mathbb 1\otimes M-M^{\!\top}\otimes\mathbb 1$ rather than by sampling: $5$, $2$, $1$
for all-equal, exactly-two-equal, and all-distinct $D$. These are $U(1)\times U(2)$,
$U(1)\times U(1)$, $U(1)$ — the report's table, confirmed. The two-equal structure is confirmed
explicitly in the $(e_+,e_-,e_3)$ basis: $\operatorname{diag}(a,b,a)$ commutes with both $L_3$ and
$D$, while $\operatorname{diag}(a,b,b)$ does not. The $SU(3)$ restrictions follow
($a^2b=1\cong U(1)$; scalar cube roots $\mathbb Z_3$). The adjoint argument justifying the
reduction to $C(L_3)\cap C(D)$ is valid because $U$ is unitary.

**Nonlinear local-rate theorem.** The one-channel witness $z\,e_j$ forces
$\nu(\lvert U_{ij}\rvert^2\lvert z\rvert^2/2)=\nu(\lvert z\rvert^2/2)$ for every nonzero
$U_{ij}$, so strict monotonicity gives $\lvert U_{ij}\rvert=1$ and column normalisation leaves
one nonzero entry: $U$ is monomial. Verified from both sides — every monomial $P\Lambda$ is a
symmetry, a random unitary is not, and a $2\times2$ mixing block is not. So the pure local-clock
symmetry is exactly $U(1)^3\rtimes S_3$.

Two hypotheses deserve to be promoted from parentheses to stated conditions:

* **Strict monotonicity is essential.** A constant $\nu$ restores all of $U(3)$; a nonmonotone
  $\nu$ admits extra unitaries wherever it takes the same value twice.
* **The witness state has zero components**, i.e. it is off the domain where the polar
  construction lives. The report says "the argument can use limits from the nonzero domain if
  necessary"; that step needs $\nu$ to extend continuously to $I=0$, which is a hypothesis on the
  rate law, not a triviality.

**Intersection.** Monomial unitaries commuting with $L_3$ are exactly scalar $\times$ permutation,
giving $U(1)\times S_3$; the $SU(3)$ restriction has exactly 18 elements (enumerated). The report's
presentation $\{\zeta^m(\det P)P\}$ is closed under multiplication and gives all 18.

The report's distinctions — pointwise operator centralizer versus nonlinear equivariance; equal
instantaneous rates at a state versus a symmetry of the field; coefficient-space symmetry versus
physical spatial symmetry — are all correct and all load-bearing. "Shared" is confirmed
insufficient: a labelled face action is not even $S_3$-invariant.

```
FIXED_FREQUENCY_CENTRALIZERS = CONFIRMED_EXACT, all three rows, in U(3) and SU(3)
LOCAL_CLOCK_NONLINEAR_SYMMETRY = CONFIRMED_WITH_ASSUMPTION — exactly U(1)^3 x| S_3 for identical
                               strictly monotone nu, assuming nu extends continuously to I = 0 so
                               the one-channel witness is admissible; intersect with C(L_3) to get
                               U(1) x S_3
SU3_FINITE_SUBGROUP          = CONFIRMED_EXACT, 18 elements, enumerated
```

---

## 19. Known-model equivalences

Each classification was tested by performing the substitution, not by matching terminology.

| Baseline | Classification | Basis |
|---|---|---|
| Action–angle mechanics | `EXACT_EQUIVALENCE` | §§3–4 are canonical polar mechanics with the frozen sign. Verified. Identifies no physical action. |
| Hamiltonian state-dependent frequency | `SPECIAL_CASE_OF` | Angle-independent $H(I)$; the closedness criterion restricts which multi-channel rates qualify. Verified. |
| One-degree-of-freedom separable Hamiltonian | `EXACT_EQUIVALENCE` | H1 on the unwrapped interior has Hamiltonian (8.4); globally on the cylinder iff $\hat S=0$. Verified. |
| Isochronous Stuart–Landau | `EXACT_EQUIVALENCE` | $\dot z=(\varepsilon k+i\varpi)z-\varepsilon\lvert z\rvert^2z$. Verified as an algebraic identity. |
| Nonisochronous Stuart–Landau | `EXACT_EQUIVALENCE` | $\dot z=(\varepsilon k+i\omega_0)z-(\varepsilon-i\alpha/2)\lvert z\rvert^2z$ for affine $\varpi$. Verified. General $W$ need not be cubic — then `SPECIAL_CASE_OF` the wider class. |
| General amplitude-dependent nonlinear oscillators | `SPECIAL_CASE_OF` | Radial growth plus a smooth radial phase rate is exactly this class. |
| Phase–amplitude (phase) reduction | `SHARES_STRUCTURE_WITH` | The polar equations keep all six real coordinates; a phase-only reduction needs a stable cycle, weak coupling and asymptotic-phase coordinates. |
| Kuramoto-type synchronization | `SPECIAL_CASE_OF` (isolated constant-rate phase subsystem) / `EXTENSION_OF` (with evolving actions) | The $\theta=3\phi$ subsystem is identical-frequency zero-lag third-harmonic Kuramoto on $K_3$; its three classes and 9/27/18 branch counts verified. |
| Complex Ginzburg–Landau networks | `SPECIAL_CASE_OF` | With $K=0$, real $g$ and affine $\varpi$ the system is exactly a discrete cubic CGLE on $K_3$, since $L_3=-3P_\perp$ is minus the $K_3$ graph Laplacian. Verified. |
| Floquet theory | `EXACT_EQUIVALENCE` | For an actual periodic variational system. A frozen proxy is not the orbit's monodromy. |
| Parametric instability | `SHARES_STRUCTURE_WITH` | The §10 witness is an exact instance; H1's regular interior orbits instead obey (8.7). |
| H3 fixed-ratio dual-time flow | `NOT_EQUIVALENT` unless an extra equivalence is proved | No common coherence functional or fixed gradient/skew ratio is derived for (6.3). |
| H4 filtered-history recursion | `NOT_EQUIVALENT` | $M_t$ is independent stored state; equations on $(I,\phi)$ alone do not reproduce it. |

**The central falsification test.** $\vartheta=\phi-\tfrac cb\log r$ gives
$\dot\vartheta=\omega-ca/b$: the amplitude dependence *is* removed from the isolated phase rate,
and the shift is canonical because it depends only on $I$. This transformation is precisely the
isochron/asymptotic-phase coordinate, so the "removal" is a known construction, not a special
feature.

Coupling reintroduces the radial information for a concrete reason: substituting
$\phi_i=\vartheta_i+h(I_i)$ sends every phase difference to $\delta_{ji}+h(I_j)-h(I_i)$, so the
first-harmonic term, the third-harmonic term and the $\cos\delta$ in (6.1) all become
amplitude-dependent. The shift is a *per-channel* function of that channel's action, while the
coupling sees *differences* — and no single per-channel shift can flatten all three differences
simultaneously unless $h$ is affine in a way that the nonlinear $F$ does not permit. The invariant
witness is the one in §6 item 6: the transverse eigenvalues move with $\alpha$ while the orbit
data does not.

**Strongest scoped statement.** *For the coupled system with $g\ne0$ and $\varpi'(I_\ast)\ne0$,
the amplitude dependence of the phase rate is not removable by any canonical phase redefinition,
rotating frame, or fixed detuning that preserves the relative equilibrium and its on-orbit data,
and the obstruction is measured by the transverse spectrum at that equilibrium, whose stability
boundary is $c^2=(a+d)^2[4ad/9g^2-1]$. For the isolated channel, or $g=0$, or $\varpi'=0$, it is
removable exactly.*

---

## 20. Novelty attack

Structural, not priority. I tried to remove the Phase III mechanism by each listed route.

| Removal route | Result |
|---|---|
| Canonical phase redefinition | Removes it for an isolated channel; **fails** for the coupled system (relocates it into $\delta_{ji}$). |
| Rotating frame | Removes a **shared** clock exactly, on the quotient; **fails** for local clocks (relocates them into the coupling coefficients). |
| Fixed detuning | **Fails** to reproduce the neighbourhood-level stability dependence at a fixed relative equilibrium (proved: uniform detuning is forced, so $c=0$). |
| Ordinary nonlinear frequency | **Does not fail** — this *is* an ordinary nonlinear frequency. $\varpi_i=\varpi(I_i)$ is channel-local nonisochronicity, and for affine $\varpi$ the system is exactly a discrete cubic CGLE. |
| Standard coupled-oscillator theory | **Does not fail** — shear-induced destabilisation of a splay/rotating-wave state in a nonisochronous coupled-oscillator network is the standard mechanism, and the closed-form threshold N1 is a model-specific instance of it. |
| A conventional auxiliary state | Not applicable to the specified model (which has no extra state); the cases that would need it are unspecified. |

So there **is** an irreducible structure in the coupled regime, and it does have an invariant
witness — but the invariant is $c=r^2\varpi'(I_\ast)$, the shear coefficient, and the class it
belongs to is a known one. The honest reading of the requested combination

$$\text{geometric tangent state}\to\text{local state-dependent rate}\to\text{relative-phase shear}
\to\text{amplitude exchange}\to\text{new local rate}$$

is that each arrow is exact, the composite loop is real and not a coordinate artefact, and the
composite is nevertheless an instance of amplitude-phase coupling in a coupled nonlinear
oscillator network. The $4\sqrt{14}$ result is evidence that the loop *does something* — it is a
real, sharp, invariant threshold — and it is not evidence that the loop is a new mathematical
object.

What would change this verdict, stated so it is testable: an invariant of the composite that is
**not** a function of the shear data $(F,\varpi,\varpi',\text{coupling})$ at the relative
equilibrium; or a model with genuinely extra state (an independent $\rho$ with its own law, or
H4-type filtered memory) whose reduction to $(I,\phi)$ is provably impossible. Neither exists in
the present material.

```
NOVELTY_STATUS = NOVELTY ONLY IN GEOMETRIC REALIZATION
                 (no novel mathematical class found; the coupled loop is real and irreducible to
                  fixed detuning, but is an instance of nonisochronous coupled-oscillator shear.
                  POSSIBLY_NOVEL survives only for the unspecified extra-state extensions, which
                  remain UNRESOLVED because no such law has been supplied.)
```

---

## 21. Does Bridge III destroy the historical intent?

No, and the report is careful about this. Checking each historically intended concept:

| Historical concept | Status after Bridge III + this review |
|---|---|
| **Recursive time** | **Preserved.** Exactly realized as a state-dependent phase rate; proved non-removable in the coupled regime. What is refuted is a *specific* instability threshold, not the concept. |
| **State-dependent temporal phase** | **Preserved and made exact.** §4.1 gives the full Hamiltonian family; §4.2 says precisely which multi-channel rates qualify. |
| **Symmetry breaking** | **Preserved but re-labelled.** A nonzero clock breaks conjugation *explicitly*. This is a correction of vocabulary, not a removal of the mechanism. Permutation-paired chiral branches survive intact. |
| **Phase–amplitude feedback** | **Preserved and sharpened.** The loop is real whenever $g\ne0$ and $\varpi'\ne0$; it is carried entirely by the first-harmonic $L_3$ coupling. |
| **Persistent / recursive state** | **Untouched and still open.** H1's minimal two-dimensional realization is too integrable to support recursive instability — but N2 shows that is a property of *that realization*, which has one first integral in two dimensions. Genuinely extra state (H4's $M_t$) leaves that setting entirely. |
| **Chirality generation** | **Partly preserved.** Local clocks provably generate $Z$ from unequal actions. Selection from symmetry is unproved and, in the witness model past threshold, not observed. |
| **SU(3)-related carrier geometry** | **Preserved and refined.** $C_{U(3)}(L_3)=U(1)\times U(2)$ is untouched; the new content is that a state-dependent local rate collapses the *nonlinear* equation symmetry to a finite group. That is a genuine structural result about the carrier, not a demotion of it. |

The invalid inference is explicitly not drawn here: **minimal realization fails $\not\Rightarrow$
historical mechanism is false.** N2 makes the minimal realization's failure sharper — the fate is
$\kappa$- and $W$-independent — and therefore makes the case *stronger*, not weaker, that a
richer model (extra state, a discrete map, or a multi-channel extension) is where the historical
mechanism would have to live. §7.3 is an existence proof that a multi-channel extension *can*
carry a sharp, exact, clock-dependent stability transition.

---

## 22. Overlooked stronger results

Six candidates, each verified, reported for later study and **not** developed into a theory.

```
NEW_DERIVED_COROLLARY N1 — closed-form general local-clock threshold
    c^2 = (a+d)^2 [ 4 a d / (9 g^2) - 1 ],
      a = -2 eps r^2 + 3g/2,  d = 3g/2 - 9K,  r^2 = k - 3g/eps,  c = r^2 varpi'(I*),
    critical frequency  omega = 3 g c / (2 (a+d));  exists iff a+d < 0 and 4 a d > 9 g^2.
    Reproduces 4 sqrt(14) exactly; confirmed numerically at three further parameter sets.

NEW_DERIVED_COROLLARY N2 — H1 trichotomy in the strictly advancing regime (v > 0)
    Let Shat = int_0^{2pi} S(phi) dphi = 2 pi sin(E_0) J_0(A).
      Shat = 0    : every interior orbit is periodic; return map is the identity.
      nu Shat > 0 : NO interior periodic orbit; every interior orbit converges to rho = 1, whose
                    multipliers are { 1, exp(-nu Shat / v(1)) }.
      nu Shat < 0 : NO interior periodic orbit; rho leaves [0,1] through rho = 0.
    The FATE is independent of kappa, of W and of the warp steepness; only the RATE depends on
    them.  Under H1's own invariance condition nu S >= 0 the second case is forced, so (8.7) has
    an empty hypothesis set exactly where H1 needs it.

NEW_DERIVED_COROLLARY N3 — the full integrating-factor family for H1
    M(rho,phi) = G( F(rho) - nu U(phi) ) / (1 - rho)   for ARBITRARY G
    is an exact Jacobi multiplier.  Each G gives a different exact canonical embedding, so the
    logarithmic chart is one of an infinite family, not merely a one-parameter one.  Separately,
    (sigma, H) scale together under I*, so I* is pure gauge for the dynamics.

NEW_DERIVED_COROLLARY N4 — exact invariant manifolds and an action-transfer constraint for (6.3)
    (a) { Omega_1 = Omega_2 = Omega_3 } is exactly invariant for every alpha.
    (b) { Omega_j = Omega_1 exp(2 pi i j / 3) } is a 2-real-dimensional invariant manifold for
        every alpha, as is its conjugate-chirality copy; an odd permutation exchanges them.
    (c) At ANY relative equilibrium with equal k,
            2 eps sum_i I_i (k - 2 I_i)  =  g sum_{i<j} |Omega_i - Omega_j|^2 ,
        an exact algebraic balance between the growth budget and the phase spread, containing
        NEITHER K NOR the clock varpi.  It constrains every branch, whatever the clock.

NEW_DERIVED_COROLLARY N5 — the nonlinear outcome past the local-clock threshold
    In the witness model the instability transfers the system to the IN-PHASE synchronous branch
    (I_i = k/2, delta = 0), which is linearly stable for every slope.  The local clock selects
    between two pre-existing branches; no new attractor and no chirality selection was observed.
    No small saturated modulated wave at 0.3% past threshold; below threshold the branches are
    bistable.  Criticality numerically indicated subcritical, NOT PROVED.

NEW_DERIVED_COROLLARY N6 — defective-monodromy conditioning (numerical caution)
    A unit-multiplier monodromy with a nontrivial Jordan block is defective: naive eigenvalue
    extraction returns a spurious sqrt(eps) spread about 1.  Witness in this review: exact
    multipliers 1, computed as 1 +/- 2.4e-6 i, from a monodromy accurate to 6e-12 in trace and
    determinant.  The well-conditioned test is det = 1 and trace = 2.  This is a checkable
    candidate explanation for a historical numerical reading of "multiplier slightly above one";
    it is NOT asserted to be the explanation.
```

---

## 23. Corrections requested

None of these is a refutation. All are small and all should be applied before the report is
treated as an accepted source.

1. **§8.3 headline scope.** "every regular periodic orbit entirely inside the interior
   $0<\rho<1$" understates the theorem: the proof is valid on the whole chart $\rho<1$, verified
   on an orbit through $\rho_0=-0.7$. `WORDING_CORRECTION`.
2. **§8.3 / §10.1 completeness.** Add the trichotomy N2. Without it, (8.7) reads as the binding
   constraint on H1 when in fact, in H1's own regime, the binding constraint is that no interior
   periodic orbit exists at all. `PROOF_INCOMPLETE` in the sense of "true but not the strongest
   available statement".
3. **§8.2 integrating factors.** Replace "does not ... exclude other integrating factors" with the
   explicit family N3. `WORDING_CORRECTION`.
4. **§4.2 convention relativity.** State that the closedness criterion is relative to the frozen
   $\sigma$, as §4.3 already does, and that necessity is a $C^1$ statement. `WORDING_CORRECTION`.
5. **§11/§17 $J_{\rm eff}$.** Restate Bridge II's definition $J_{\rm eff}=\Im(\Omega_1
   \overline{\Omega_2}\Omega_3)$ where the clock law is given; the sign is right but unreadable
   without it. `WORDING_CORRECTION`.
6. **§12.2 hypothesis.** Promote "the argument can use limits from the nonzero domain if
   necessary" to a stated hypothesis that $\nu$ extends continuously to $I=0$.
   `WORDING_CORRECTION`.
7. **§7.3 completeness.** Add the general threshold N1 and the nonlinear outcome N5. As written,
   "above threshold: instability" leaves the impression of an open route to new behaviour, when in
   the witness model the system simply locks in phase. `WORDING_CORRECTION`.
8. **§2, third applicability qualification.** "$J\nabla C=(0,1)$, whose norm is not constant along
   a general trajectory" — the *field* has constant norm; it is the *state* norm that is not
   conserved along the flow. The mathematical point is correct; the sentence is not.
   `WORDING_CORRECTION`.

---

## 24. Mandatory final block

```ini
ACTION_ANGLE_FORM                     = CONFIRMED_EXACT_SIGMA_EQUALS_SUM_DI_WEDGE_DPHI
RECURSIVE_PHASE_HAMILTONIAN           = CONFIRMED_EXACT_FOR_LOCAL_RATES_SIGN_AND_FAMILY_VERIFIED
MULTI_ACTION_INTEGRABILITY            = CONFIRMED_WITH_ASSUMPTION_CLOSEDNESS_NECESSARY_AND_SUFFICIENT_C1_RATES_FROZEN_SIGMA
SHARED_CLOCK_REMOVABILITY             = CONFIRMED_EXACT_ON_EQUIVARIANT_PHASE_INVARIANT_QUOTIENT_NOT_PHYSICAL_CLOCK_EQUIVALENCE
PAPER_A_POLAR_PARENT                  = CONFIRMED_EXACT_ALL_COEFFICIENTS_INDEPENDENTLY_REDERIVED
STATE_PHASE_FEEDBACK_LOOP             = CONFIRMED_REAL_FOR_G_NONZERO_AND_VARPI_PRIME_NONZERO_CARRIED_ENTIRELY_BY_L3

H1_LOGARITHMIC_EMBEDDING              = CONFIRMED_EXACT_ON_RHO_LT_1_ONE_OF_AN_INFINITE_MULTIPLIER_FAMILY
H1_FIRST_INTEGRAL                     = CONFIRMED_EXACT_EQUALS_MINUS_H_HIST_OVER_I_STAR_SYSTEM_IS_INTEGRABLE
H1_RETURN_MAP                         = CONFIRMED_EXACT_IDENTITY_IFF_INTEGRAL_OF_S_VANISHES_NO_INTERMEDIATE_CASE
H1_INTERIOR_PERIODIC_FLOQUET_MULTIPLIERS = CONFIRMED_EXACT_BOTH_EQUAL_ONE_TWO_METHODS_PLUS_NUMERICAL_COUNTEREXAMPLE_SEARCH
H1_POSITIVE_INTERIOR_FLOQUET_EXPONENT = NO_EXCLUDED_EXACTLY_SHEAR_AND_FINITE_TIME_GAIN_STILL_ALLOWED

COMMUTATOR_FORMULA                    = CONFIRMED_EXACT_TRACELESS_H1_PRINTED_FORM_IRREPARABLE_BY_ORDERING
COMMUTING_FAMILY_RANK_CRITERION       = CONFIRMED_EXACT_NECESSARY_AND_SUFFICIENT_EXHAUSTIVE_SWEEP_CLEAN
TRIANGULAR_PROPAGATOR                 = CONFIRMED_EXACT_BOTH_FORMS
MAGNUS_TIME_ORDERING_RESULT           = CONFIRMED_EXACT_MONODROMY_DIAG_MINUS2_MINUS_HALF_WITNESS_OUTSIDE_CONVERGENCE_BALL

LOCAL_CLOCK_120_DEGREE_BRANCH         = CONFIRMED_EXACT_RELATIVE_EQUILIBRIUM_R2_EQUALS_K_MINUS_3G_OVER_EPS
LOCAL_CLOCK_THRESHOLD_VALUE           = CONFIRMED_EXACT_4_SQRT_14_THREE_INDEPENDENT_ROUTES_GENERAL_FORM_DERIVED
LOCAL_CLOCK_STABILITY_EFFECT          = CONFIRMED_EXACT_TRANSVERSE_ONLY_NONLINEAR_OUTCOME_IS_TRANSFER_TO_THE_IN_PHASE_BRANCH
FIXED_DETUNING_CAN_REPRODUCE_THRESHOLD = NO_UNIFORM_DETUNING_IS_FORCED_HENCE_C_EQUALS_ZERO

Z_CHIRAL_EVOLUTION                    = CONFIRMED_EXACT
SHARED_CLOCK_GENERATES_Z              = NO_EXACTLY_ZERO_DIRECT_CONTRIBUTION
LOCAL_CLOCK_CAN_GENERATE_Z            = YES_FROM_UNEQUAL_ACTIONS_BY_PHASE_SHEAR_EXPLICIT_NOT_SPONTANEOUS
SPONTANEOUS_CHIRAL_SELECTION          = NOT_PROVED_AND_NOT_OBSERVED

J_EFF_CLOCK_LAW                       = CONFIRMED_EXACT_GIVEN_BRIDGE_II_DEFINITION_J_EFF_EQUALS_IM_M_GAUGE_DEPENDENT_DIAGNOSTIC

L3_FIXED_FREQUENCY_CENTRALIZERS       = CONFIRMED_EXACT_ALL_THREE_ROWS_U3_AND_SU3
LOCAL_CLOCK_NONLINEAR_SYMMETRY        = CONFIRMED_WITH_ASSUMPTION_U1_CUBED_SEMIDIRECT_S3_REQUIRES_STRICT_MONOTONICITY_AND_CONTINUOUS_EXTENSION_AT_ZERO
SU3_REDUCTION_RESULT                  = CONFIRMED_EXACT_18_ELEMENT_FINITE_GROUP

KNOWN_MODEL_REDUCTIONS                = EXACT_IN_EVERY_SUBCASE_TESTED_NONISOCHRONOUS_STUART_LANDAU_AND_DISCRETE_CUBIC_CGLE_ON_K3
IRREDUCIBLE_RECURSIVE_STRUCTURE       = YES_IN_THE_COUPLED_REGIME_INVARIANT_WITNESS_IS_THE_TRANSVERSE_SPECTRUM
SUPPORTED_NOVEL_STRUCTURE             = NONE_FOUND_THE_IRREDUCIBLE_INVARIANT_IS_THE_STANDARD_SHEAR_COEFFICIENT
NOVELTY_STATUS                        = NOVELTY_ONLY_IN_GEOMETRIC_REALIZATION

PHYSICAL_FACE_OBSERVABLE              = UNRESOLVED
PHYSICAL_TIME_SCALE                   = UNRESOLVED
PHYSICAL_INTERPRETATION_READY         = NO

PHASE_BRIDGE_III_SURVIVES_REVIEW      = YES
READY_FOR_CODEX_VERIFICATION          = YES

FROZEN_FILES_MODIFIED                 = NO
KERNEL_PHYSICS_MODIFIED               = NO
REPOSITORY_MODIFIED                   = NO
COMMITTED_OR_PUSHED                   = NO
REVIEW_PREDICATES_EXECUTED            = 188 / 188 PASSED
```

`PHASE_BRIDGE_III_SURVIVES_REVIEW = YES` rather than `PARTIAL`, because the question asked is
whether the report's *mathematics* survives adversarial re-derivation, and no claim was
contradicted. The report's own `PHASE_BRIDGE_III_READY_FOR_CODEX = PARTIAL` refers to a different
question — whether the physical interpretation is settled — and on that question this review
agrees with it completely: `PHYSICAL_INTERPRETATION_READY = NO`.

`READY_FOR_CODEX_VERIFICATION = YES` is conditional on applying the eight corrections in §23 and
on Codex independently checking the six new corollaries in §22, which are this review's own work
and have had no second pair of eyes.

---

## 25. Stop boundary

No Phase Bridge IV was written. Recursive time was not implemented. `kernel_physics` was not
modified. No publication paper was written. Historical SRG was not restored. No CP violation was
claimed. No Standard Model physics was claimed. No novelty priority was claimed — the novelty
assessment above is structural and explicitly not a literature search.

The review stops here.
