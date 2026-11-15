# Native response asymmetry and common-phase drift: independent comparison

**NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01 — 15 November 2026**  
**Disposition:** RD01–RD05 verified within the local hypotheses below; returned for GPT and author review. No publication approval or external peer review is implied.  
**Bounded prior-work disposition:** `DISTINCT_GAP` for the matched comparison, with the individual response and drift constructions explicitly inherited.

## 1. Objects, sources and conclusion

Use only the exact three-channel native map, in its unchanged order:

\[
v_i=z_i+h z_i(1+\xi_i-|z_i|^2)+\frac h6(L_3z)_i,
\quad \delta_i=\frac h{30}\sum_{j\ne i}\sin3(\arg v_j-\arg v_i),
\quad F_h(z)_i=v_i e^{i\delta_i},
\tag{1}
\]

where \(L_3=\mathbf1\mathbf1^T-3I\), \(0<h\le1/4\), and \(\xi_0+\xi_1+\xi_2=0\). All prestages are simultaneous and all kicks use the completed prestage. Here h means **h_step**, the mathematical step parameter; it is not an outer-geometry length or calibrated time. The unchanged implementation uses Arg0(0)=0 and returns the prestage directly at lambda=0. Derivatives and equivariance below are used only where the relevant state and prestage entries are nonzero.

Sources are preserved byte-for-byte under `sources/inherited/` and in the unchanged incoming ZIP. The source guide and original identities remain inside that ZIP. The main inherited premises are:

* NRG `response.tex`: `thm:branch`, `eq:fixed`, `eq:screen`, `eq:P`, `eq:SP`, `eq:cycle`, the corrected `eq:K`, and `eq:cycleweak`.
* D1 `drift.tex`: D1–D7, D20, D23–D30, D36–D40; `D0.md` §§6–8 and `D1_CLOSEOUT.md` §§2–7. In particular the D1 cubic coefficient is **reused, not recalculated** here.
* `dynamics.py`: `arg0`, `phase_sync`, `_advance`, `step3`, read as source only.

The conclusion is an exact local comparison of functions evaluated on different backgrounds. There is a permutation-invariant ball \(U\) about zero in the zero-sum coefficient plane, with one positive but unspecified radius for the entire closed interval \(I=[0,1/4]\), such that

\[
\overline{\mathcal C}=\mathcal A S_C,
\qquad \nu_+=\mathcal A S_D,
\qquad \nu_-=-\mathcal A S_D,
\qquad S_C,S_D>0 \quad\hbox{on } I\times U.
\tag{2}
\]

The factors are jointly real analytic on an open neighborhood of this set and symmetric in the coefficient labels. The functions at h=0 mean the specific analytic/generator extensions, not discrete motion of the identity map. The actual branch selection is essential to predict signed advance.

## 2. RD01: existence at the same parameters and a common domain

### Positive in-phase branch

At a positive real fixed state all phases and kicks vanish, and division of the prestage fixed equation by h gives

\[
E_i(r,\xi)=r_i(1+\xi_i-r_i^2)+\frac16(L_3r)_i=0.
\tag{3}
\]

This equation is independent of h. At \((r,\xi)=(\mathbf1,0)\),

\[
D_rE=-2I+L_3/6,
\quad\operatorname{spec}(D_rE)=\{-2,-5/2,-5/2\}.
\tag{4}
\]

The analytic implicit-function theorem gives one positive analytic root r(xi) near one. Uniqueness makes it permutation equivariant. Differentiating (3) gives \(D_rE\,dr+d\xi=0\); hence on the zero-sum plane

\[
r_i(\xi)=1+\frac25\xi_i+O(\|\xi\|^2).
\tag{5}
\]

This specializes the inherited branch derivative, not a new global existence theorem. For h>0 the reference also satisfies NRG's strict normal stability hypothesis: the amplitude multipliers are \(1-2h,1-5h/2,1-5h/2\), and both noncommon phase multipliers are \((1-3h/10)(1-h/2)\), all strictly between zero and one. No uniform attraction or basin at h=0 is inferred. At h=0, (3) selects a limiting root; \(F_0=\mathrm{id}\) alone does not select it.

### D1 chiral branches and the compact-parameter argument

The inherited positive-label reference is \(z^*_{+,j}=2^{-1/2}e^{2\pi ij/3}\); its conjugate is the negative-label reference. On this family its prestage equals itself for every h. Use D1's reference-specific gauge

\[
\gamma_+(z)=\frac{\Im\langle z^*_+,z\rangle}{\|z^*_+\|^2}=0,
\qquad \Re\langle z^*_+,z\rangle>0.
\tag{6}
\]

The equation is \(\mathcal H=(F_h(z;k)-e^{ih\nu}z)/h=0\), with the gauge as seventh real row. D1's full seven-dimensional reference border has determinant \(-(3h-1)^2/1600\), whose absolute value on I is at least \(1/25600\) (D25). This border includes all five transverse state directions, including the unstable directions. No stability claim is substituted for its invertibility.

Here is the uniform-neighborhood justification, rather than an unqualified minimum of pointwise radii. Near the compact reference set the state and prestage components have a common nonzero margin. Harmonic sines written with unit complex factors make the residual jointly real analytic without argument cuts. Its numerator vanishes identically at h=0 for every nearby z, xi and nu, so its convergent analytic series divides by h. At h=0 it is exactly \(X_k(z)-i\nu z\) (D26–D27).

Write the seven unknown displacements as y and the extended seven-row residual as R(h,y,xi), with R(h,0,0)=0. Let A(h)=D_yR(h,0,0). The continuous invertible matrix A(h) has a bounded inverse on I; the determinant lower bound alone is not a numerical inverse-norm bound. On a fixed small regular box, uniform continuity of the derivative allows a radius rho and coefficient radius delta such that

\[
\|I-A(h)^{-1}D_yR(h,y,\xi)\|\le1/2,
\quad \|A(h)^{-1}R(h,0,\xi)\|\le\rho/2
\tag{7}
\]

for every h in I, \(\|y\|\le\rho\), and \(\|\xi\|<\delta\). The map \(y\mapsto y-A(h)^{-1}R(h,y,\xi)\) is a contraction of that closed ball into itself. Its unique roots agree with each local analytic implicit branch; uniqueness glues them. Invertibility and regularity also persist on a slightly open h-neighborhood at the endpoints. This proves a jointly analytic branch on a common qualitative coefficient neighborhood, without computing a radius. The conjugate gauge gives \(z_- =\overline{z_+}\) and \(\nu_-=-\nu_+\) at the **same ordered k**. All phases are the small unwrapped branches, chosen continuously from zero rate.

Intersect these coefficient neighborhoods with the one for (3), and shrink to an invariant ball. The positive aligned and twisted reference orbits are distinct; small neighborhoods keep them distinct, even modulo common phase. This supplies the overlapping domains in parameter space, not a trajectory between backgrounds. The D1 reference is a saddle; neither continued branch is asserted to attract.

## 3. RD02: reconstruct the ordered response and its exact factor

For an imaginary perturbation \(iz_i'=i r_i\phi_i\) at the positive aligned state, the Cartesian prestage derivative is

\[
H_r=I+h\operatorname{diag}(1+\xi_i-r_i^2)+hL_3/6.
\]

Equation (3) gives \(H_rr=r\). With \(R=\operatorname{diag}(r_i)\), transformation to inherited phase coordinates yields

\[
P_h=R^{-1}H_rR=I+h\mathsf B_r,
\quad (\mathsf B_r)_{ij}=\frac{r_j}{6r_i}\ (i\ne j),
\quad (\mathsf B_r)_{ii}=-\frac16\sum_{j\ne i}\frac{r_j}{r_i}.
\tag{8}
\]

The synchronizer derivative is \(I+3\lambda L_3=I+hL_3/10\). It acts **after** (8):

\[
J_h=(I+hL_3/10)(I+h\mathsf B_r)
=I+h\mathsf G_r+\frac{h^2}{10}L_3\mathsf B_r,
\qquad \mathsf G_r=\mathsf B_r+L_3/10.
\tag{9}
\]

Let \(D_h=\mathsf G_r+hL_3\mathsf B_r/10\). Every off-diagonal entry of J is h times the corresponding entry of D. Thus

\[
\mathcal C=J_{01}J_{12}J_{20}-J_{02}J_{21}J_{10}
=h^3\operatorname{cyc}(D_h),
\qquad \overline{\mathcal C}:=\operatorname{cyc}(D_h).
\tag{10}
\]

This constructs an analytic extension directly, without dividing an evaluated zero by h³.

For r=(a,b,c), set \(s_1=a+b+c\), \(s_2=ab+ac+bc\), \(s_3=abc\), \(V_r=(a-b)(a-c)(b-c)\), and \(d=1-3h/10\). Direct entry expansion gives

\[
\boxed{\overline{\mathcal C}
=\frac{d V_r}{60s_3^2}\mathcal K_h(r)},
\quad
\mathcal K_h=\frac{h^2s_1^3}{360}
+\left(\frac h{90}-\frac{h^2}{180}\right)s_1s_2
+\left(\frac h{20}-\frac1{15}\right)s_3.
\tag{11}
\]

For a reproducible algebraic derivation, write the off-diagonal entries as

\[
(D_h)_{ij}=\frac{d r_j}{6r_i}
+\frac1{10}\left[1+\frac h6\left(r_j\sum_k\frac1{r_k}-\frac{s_1}{r_j}\right)\right].
\tag{12}
\]

Expand the two three-products, clear their common denominator, and divide their alternating numerator by V_r. The remaining expression, multiplied by \(60s_3^2/d\), is a symmetric homogeneous cubic. Coefficient matching in the basis \(s_1^3,s_1s_2,s_3\) gives respectively \(h^2/360,h/90-h^2/180,h/20-1/15\). `checks/exact_check.py` performs this polynomial division starting with the Cartesian derivative, and compares all coefficients exactly. A separate substitution into the published corrected GR1 expression gives \(\mathcal K=h\mathcal K_h\) and the same prefactor. All formulas concern positive r; divisions by s3 are legitimate. The factor d is nonzero throughout I.

### Exact coefficient-to-radius differences

There is a particularly direct analytic quotient. Rearranging (3) gives

\[
1+\xi_i=r_i^2+\frac12-\frac{s_1}{6r_i},
\quad
\xi_i-\xi_j=(r_i-r_j)D_{ij},
\quad D_{ij}=r_i+r_j+\frac{s_1}{6r_ir_j}>0.
\tag{13}
\]

Consequently two coefficients are equal exactly when the corresponding radii are equal on this positive branch. Put \(Q_r=D_{01}D_{02}D_{12}\). Each radius difference has an exact analytic coefficient-difference factor; at xi=0 each \(D_{ij}=5/2\). With the required orientation

\[
\mathcal A=(\xi_0-\xi_1)(\xi_1-\xi_2)(\xi_2-\xi_0),
\qquad V_r=-\mathcal A/Q_r,
\tag{14}
\]

equation (11) gives the **exact** analytic symmetric factor

\[
\boxed{S_C(h,\xi)=-\frac{d\,\mathcal K_h(r(\xi))}{60s_3(r(\xi))^2Q_{r(\xi)}}.
\tag{15}
\]

This holds on equal-coefficient sets as well. Its constant term is

\[
\mathcal K_h(\mathbf1)=\frac{3h^2+18h-8}{120},
\qquad
\boxed{a_C(h)=S_C(h,0)=
\frac{(1-3h/10)(8-18h-3h^2)}{112500}}.
\tag{16}
\]

Permutation symmetry forces the first derivative of S_C at zero to be a multiple of \(\sum\xi_i\); on the mean-zero plane it vanishes. Thus \(S_C=a_C+O(\|\xi\|^2)\), uniformly on the compact h interval after shrinking U. This is an estimate of the **analytic quotient**, not division of a bare fifth-order remainder.

### Matching the inherited D1 normalization

D1 D28–D30 and D36–D37 give

\[
\nu_+=\mathcal A S_D,
\quad S_D(h,0)=c_+(h)=
\frac{\sqrt3(33h^2-240h+688)}{6(1-3h)^3},
\quad S_D=c_++O(\|\xi\|^2).
\tag{17}
\]

Along xi=(-eta,0,eta), \(\mathcal A=2\eta^3\), whereas the increasing-pair product is \(-2\eta^3\). Therefore

\[
\overline{\mathcal C}=2a_C(h)\eta^3+O(\eta^5),
\quad \mathcal C=2h^3a_C(h)\eta^3+O(h^3\eta^5),
\quad \nu_+=2c_+(h)\eta^3+O(\eta^5),
\quad \omega_+=h\nu_+.
\tag{18}
\]

No truncated state is treated as an exact finite-eta root. The general quotient has no linear term; only the special reflected direction guarantees exact oddness in eta. A general sixth-degree term is not excluded. D1's full cubic state calculation and interval tubes were not rerun.

## 4. RD03: divisibility, positivity, complete local zero sets

For completeness, the analytic divisibility used for the drift must precede any ratio. D1's label-preserving combination of conjugation and reflection negates the rate when two coefficients are exchanged, while cyclic permutations preserve it. Local uniqueness and gauge restoration give these symmetries on the common regular neighborhood. Hence \(\nu_+\) vanishes on each equal-coefficient hyperplane. In coordinates with one such linear form as a coordinate, its convergent analytic series factors by that form. After the first division, the quotient still vanishes on the second hyperplane away from its intersection with the first; continuity gives vanishing at the intersection too. Divide again and repeat for the third. The argument works jointly with h as a parameter and on the two-dimensional mean-zero plane, where the three hyperplanes restrict to distinct lines. The quotient is symmetric because both the rate and A change sign under odd permutations. Uniqueness of analytic extensions glues local divisions. This proves the analytic S_D independently of trying to divide an O-estimate.

S_C is already analytic and symmetric by (13)–(15). On I,

\[
d\ge37/40,\qquad 8-18h-3h^2\ge53/16,
\qquad a_C(h)\ge\frac{1961}{72000000}>0.
\tag{19}
\]

For example the second inequality follows from the exact identity
\(8-18h-3h^2-53/16=(1/4-h)(75/4+3h)\).
The inherited numerator of c+ is at least 628, and \(0<(1-3h)^3\le1\), so
\(c_+(h)\ge314\sqrt3/3>0\). This conservative bound is enough; no minimization is needed.

Joint continuity on a neighborhood of the compact set I×{0} now supplies a single smaller ball U on which S_C and S_D differ from their respective positive constant terms by less than half their positive lower bounds. This uses a uniform regular implicit setting from §2, not disconnected pointwise radii. Intersecting finitely many coefficient domains and taking an invariant ball preserves all stated symmetries. The radius is **existential only**. The finite historical eta fixtures do not certify that radius.

Therefore the complete zeros of \(\overline{\mathcal C}\), \(\nu_+\), and \(\nu_-\) in U are exactly

\[
\{\xi_0=\xi_1\}\cup\{\xi_1=\xi_2\}\cup\{\xi_2=\xi_0\}.
\tag{20}
\]

For h>0 the same is true of raw C and both per-update advances. At h=0 raw C and omega vanish for **all** xi, so (20) applies there only to the normalized/extended quantities. Off (20),
\(\operatorname{sgn}\overline{\mathcal C}=\operatorname{sgn}\nu_+=\operatorname{sgn}\mathcal A\), and the negative-label rate has the opposite sign.

The exact symmetric analytic positive function

\[
\Theta(h,\xi)=S_D(h,\xi)/S_C(h,\xi)
\tag{21}
\]

is defined across all the zero planes. It gives \(\nu_\pm=\pm\Theta\overline{\mathcal C}\). Only its leading value is explicit here:

\[
\boxed{\Theta(h,0)=\frac{c_+(h)}{a_C(h)}=
\frac{18750\sqrt3(33h^2-240h+688)}
{(1-3h)^3(1-3h/10)(8-18h-3h^2)}}.
\tag{22}
\]

It varies with h. The exact Theta generally also depends on xi; no all-orders expression for S_D or a constant universal proportionality is claimed. Additional cancellations away from U, other branches and larger rings are outside the theorem.

## 5. RD04: generator, additive step, native product and the h=0 limit

Equation (9) distinguishes three matrices:

| Object | Exact definition | Off-diagonal cycle |
|---|---|---|
| In-phase generator | \(\mathsf G_r=\mathsf B_r+L_3/10\) | \(\operatorname{cyc}(\mathsf G_r)\) |
| Additive first-order step | \(I+h\mathsf G_r\) | \(h^3\operatorname{cyc}(\mathsf G_r)\) |
| Native ordered response | \(I+h\mathsf G_r+h^2L_3\mathsf B_r/10\) | \(h^3\overline{\mathcal C}(h,\xi)\) |

The radius r does not depend on h. Setting h=0 in (11), or multiplying the off-diagonal entries \(r_j/(6r_i)+1/10\) of the generator, gives

\[
\boxed{\overline{\mathcal C}(0,\xi)
=\operatorname{cyc}(\mathsf G_r)
=-\frac{(r_0-r_1)(r_0-r_2)(r_1-r_2)}{900r_0r_1r_2}}.
\tag{23}
\]

The generator/additive separation is already established in D1 D15–D18 and D0's determinant/middle-coefficient correction. Equation (23) is its specialization in the present orientation and its identification with the normalized native limit, not a new larger-ring spectral theorem. In particular the diagonal cycle product is not the GR2 Bloch coefficient and not a spectral phase.

At xi=0, the cubic coefficient values are

\[
a_C(0)=2/28125,
\qquad c_+(0)=344\sqrt3/3,
\qquad \Theta(0,0)=1612500\sqrt3.
\tag{24}
\]

For each **fixed**, sufficiently small pairwise-distinct xi, (2) makes both extended leading quantities nonzero. Analyticity in h then gives

\[
\mathcal C(h,\xi)=h^3\overline{\mathcal C}(0,\xi)+O(h^4),
\quad \nu_\pm(h,\xi)=\nu_\pm(0,\xi)+O(h),
\quad \omega_\pm=h\nu_\pm(0,\xi)+O(h^2).
\tag{25}
\]

Thus these are genuine nonzero leading orders at such a tuple, not just upper bounds. A vanishing raw response product and a vanishing per-update angle are compatible with a nonzero limiting generator rate. At h=0, F0 remains the identity and makes no update advance. The extension selects a generator relative equilibrium \(X_k(z_\pm)=i\nu_\pm z_\pm\); it does not make the identity move. At equal-coefficient points the nonzero-leading assertion is intentionally inapplicable. There is no inferred physical clock, calibrated continuum limit or physical constant in (24).

## 6. RD05: what the diagnostic does and does not select

Fix h>0 and a pairwise-distinct xi in U. Let \(D_r=\mathcal C(h,\xi)\) denote the one **assigned in-phase response diagnostic** (not the pair denominators D_ij above). The following table compares the same ordered tuple and the same assigned diagnostic while explicitly changing the full current state:

| Selected native state, up to common phase | Native update | Assigned diagnostic, always evaluated at r | Small unwrapped advance |
|---|---|---|---|
| Positive in-phase r(xi) | \(F_h(r)=r\) | \(D_r\ne0\) | 0 |
| D1 positive-label z+(h,xi) | \(F_h(z_+)=e^{ih\nu_+}z_+\) | the same \(D_r\) | \(\omega_+=h\mathcal A S_D\ne0\) |
| Conjugate D1 z−(h,xi) | \(F_h(z_-)=e^{-ih\nu_+}z_-\) | the same \(D_r\) | \(-\omega_+\) |

Here “positive label” refers to the fixed reference chirality, not an unconditional positive rate: its rate has the sign of A. Conjugation leaves k and the positive real r fixed and reverses the chiral rate. A pure site reflection also carries the coefficients and changes the branch label; it is not this same-ordered-tuple comparison.

The coefficient tuple plus the in-phase diagnostic therefore cannot select the realized signed common-phase advance **without the state/branch choice**. This statement uses inherited stationary-state and conjugation facts in the newly matched quantitative comparison. It does not claim identical full current states can evolve differently, does not invalidate deterministic reconstruction, and does not imply all state-dependent response data are insufficient. Nor does it identify the chiral state's own response matrix with J at r.

Once a D1 branch is specified, (21) is compatible with this limitation. For h>0 one can also write \(\omega_\pm=\pm\Theta\mathcal C/h^2\), keeping the distinct powers visible. This equality relates functions on different selected backgrounds. It is not a force law, causal transfer, path between branches or state-independent rule for arbitrary native states. Full-state reconstruction on the accepted coherent domain retains its established scope; that domain does not contain these twisted references.

## 7. Logical controls, execution and assessment of the proposal

The six requested challenges are resolved as follows:

| Challenge | Evidence and outcome |
|---|---|
| Wrong orientation / missing two | (14), (18); exact tests verify A(-eta,0,eta)=2eta³ and increasing-pair product=-A. Wrong-sign and half-coefficient substitutions give nonzero residuals. |
| Reverse native stages | (8)–(12); symbolic tests show both an entry of SP−PS and their normalized cycle difference are nonzero rational functions. Equality at a symmetric special point cannot validate stage reversal. |
| Raw C vs C/h³; omega vs nu | (10), (18), (25); their generic differences are explicitly nonzero, and their h orders differ. |
| Two equal coefficients | (13), analytic divisibility and (20); this is exactly a zero case locally, not a positive-sign fixture. |
| Conjugation | D1 D28–D30, gauge uniqueness and §6; same ordered coefficients/diagnostic, opposite rate. Symbolic advance sums vanish. |
| Universal signed predictor | Actual three-branch table in §6 gives 0, omega and −omega at one assigned diagnostic. These are different states. |

All 60 recorded exact identities and negative-control predicates passed. After making the checker output paths portable, a second bounded execution of the delivered checker reproduced the same 60 results; the initial successful source/output and both run records are retained. These are 60 distinct algebra/control predicates, **not a theorem count**, and are not counted twice. SymPy is the same arithmetic backend used by the packet's preparation helper. The new organization starts from the Cartesian derivative, performs alternating polynomial division and derives (13)–(15); it does not import or run that helper. The uniform-neighborhood and divisibility arguments are written proofs, not claims established by the finite count. D1's coefficient, border and branch theorem are inherited premises, not newly certified numerical results. There were zero numerical branch fixtures, trajectories, continuation tubes, old certificate replays, ring scans or scientific suite runs.

The worker was bounded by 300 seconds and a 768 MiB monitored Windows working-set ceiling; actual timing, peak observed memory, environment, stdout and stderr are supplied. An initial monitor attempted an unavailable psutil import before any symbolic worker launched; it was replaced with the Windows process-memory API, with no installation. An initial source lookup found that the current local research index is not a blob at the chosen checkpoint; its existing local file was recovered and labelled accordingly. Both administrative failures are retained in the execution record; neither is a failed mathematical identity.

**Assessment of GPT's proposed P1–P9:** the formulas and the proposed local zero/sign/ratio conclusion are supported. No sign, coefficient, parameter or theorem-domain correction is required. The review adds the explicit pair-difference identity (13), exact quotient (15), the uniform implicit-function argument, and the detailed divisibility justification needed to make the proposal complete. The distinction between an explicit leading ratio and an exact analytic existence statement is retained. All accepted predecessors and repository files remain unchanged. This closes only the commissioned correspondence review and returns it for assessment.
