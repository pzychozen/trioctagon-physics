# D0 — Reconciliation verification and an isolated chiral reference
<!-- Public locator-only derivative; original raw SHA-256 and exact edits in provenance/public_export_map.json. Historical status wording is retained. -->

6 October 2026 · External mathematical research · Read-only source audit

**D0 = PASS_WITH_QUALIFICATIONS.** One explicit rational small-step family has a nonzero chiral fixed reference, an invertible full phase-gauged relative-equilibrium system, and an analytic extension to the generator limit. It supplies a valid local setup for the proposed D1 test. It is a saddle. No unequal-background relative equilibrium, drift coefficient, trajectory, or parameter scan was computed.

The Section B correction is proved: its proposed imaginary expression belongs to the additive-step **determinant**, not to its middle characteristic coefficient. The reconciliation's reference Jacobian and cubic selection argument survive independent verification with the domain, sign, gauge, and branch qualifications below. None of this discovers physical rotation or a missing physical coupling.

## 1. Authority, preservation, and evidence

The authority is `project-source/trioctagon-physics`, at actual HEAD `82cab10cbe550f58c43163fb8b05fabdad1b05ae`, branch `main`. No earlier expected HEAD was substituted. The initial index had no staged paths. Its `git ls-files --stage -z` fingerprint was `34a5907d8b24ce98cbd18af7e671ac6b2f2398c52ad269c1f8e4430839590a06`.

The working tree was already dirty: ten tracked scientific-UI/workflow paths and the untracked material recorded verbatim in `D0_RESULTS.json`. They were neither cleaned nor edited. A fresh byte inventory covered 16,032 existing files across the scientific checkout, historical `kernel_TO`, production `kernel_torment`, the separate sibling `kernel_physics`, external research predecessors, and reconstruction records. `.git` internals and only this new D0 output directory were excluded from that file inventory; HEAD, index, branch, and status were separately compared. All six root fingerprints and all Git comparisons passed.

The output set contains exactly this report, `verify_d0.py`, and `D0_RESULTS.json`, in `project-source/research/D0_chiral_reference_20261006/`. No repository files, papers, historical implementations, review materials, fixtures, or predecessor research were modified. No staging, commit, push, cleanup, tag, release, or publication revision occurred.

Evidence labels used here:

- **SOURCE DEFINITION:** a formula or convention actually present in the inspected source.
- **DERIVED IDENTITY / EXACT THEOREM:** a written argument in this report; exact symbolic checks are corroboration.
- **EXACT SYMBOLIC CHECK:** a finite rational/symbolic predicate in the external verifier.
- **NUMERICAL EVIDENCE:** a bounded numerical comparison, with arithmetic and tolerance distinguished.
- **STRUCTURAL ANALOGY / PHYSICAL INTERPRETATION:** explicitly separated from the identities. No new physical identification is adopted.
- **OPEN QUESTION:** a matter not settled by D0.

### Source crosswalk

All paths below are relative to `project-source/` unless stated otherwise.

| Source | Locator | Use |
|---|---|---|
| `trioctagon-physics/kernel_physics/dynamics.py` | lines 28–45, 57–112 | Real parameter domain; Arg0; simultaneous synchronizer; prestage; complete triad/ring map. |
| `trioctagon-physics/kernel_physics/z_diagnostics.py` | lines 219–302, especially `potential` at 290 | Adopted potential normalization and finite intensity accounting. |
| `trioctagon-physics/kernel_physics/readouts.py` | `z_chiral`, lines 7–16 | Raw channel chirality, with no imposed decay or physical-motion attachment. |
| `trioctagon-physics/papers/PAPER_A/publication/paper_A_final.tex` | §§1, 6.1; model-class discussion §6.5 | Accepted map and zero convention; existing coupled-map context. No paper revision. |
| `research/GR0_native_gravity_20261006/GR0_NATIVE_GRAVITY_INVENTORY_AND_PERTURBATION_BASELINE.md` | §§3–5, especially §4(d), §5.1 | Existing gradient identity, non-descent witness, regularity limitations. |
| `research/FRESH_EYES_SCIENTIFIC_REVIEW_20261006/FRESH_EYES_SCIENTIFIC_REVIEW_v0.1.md` | Entire file; especially §§1, 7, 9 | Original claims and proposed test. |
| Same directory, `FRESH_EYES_RECONCILIATION_NOTE_v0.1.md` | Entire file; §§1a–c, 2, 3.1–3.7, 5 | Actual reconciliation, rather than the owner's summary. |
| Same directory, `fresh_eyes_checks.py` | Entire file; B around lines 67–121, F from 185 | Matrix definitions and printed diagnostics; no project import. |
| Same directory, `fresh_eyes_checks_output.txt` | Entire file | Retained diagnostic output, including the Section B mismatch. |

The original manifest matches the raw local bytes:

| File | SHA-256 |
|---|---|
| Original review | `65dc00967ccdecc1c513bd8b3046568f475894ae0b960db314e1c0575c75b90d` |
| Reconciliation note, newly recorded | `de945528c31fdc318e5ff6a5165757f81587b888b6a748722819dcf7262fe383` |
| Original check script | `807e79cf4bda818835d19bc072b5802d23fff312dddc96c7df0ab26e7dca6d2d` |
| Original output | `92314cd236004d47cc3216aca509414cc05b062ed33605897f01fda7792eb31e` |

The machine-readable results retain the exact computed identities and source hashes. No predecessor bytes were normalized. This audit does not undertake another literature or novelty review, and does not reopen Paper G, gravity, Three-Way, or the TL synthesis.

## 2. The native map and its regular domain

**SOURCE DEFINITION.** Write the state as \(z\in\mathbb C^N\), \(N=3q\), and let \(\Delta\) be the real symmetric cycle Laplacian with diagonal \(-2\) and the two cyclic neighbors. The triad has \(\Delta=L_3\). With real parameters,

\[
 A_k(z)_i=\widetilde z_i
 =z_i+\epsilon z_i(k_i-|z_i|^2)+g(\Delta z)_i,
\]
\[
 \delta_i(w)=\lambda\sum_{j\sim i}\sin3(\operatorname{Arg}_0w_j-\operatorname{Arg}_0w_i),
 \qquad F_k(z)_i=\widetilde z_i e^{i\delta_i(\widetilde z)}.
\]

The last form includes zero outputs; the source implements equivalent modulus/phase reconstruction and explicitly resets exact zero components to zero. The native convention is \(\operatorname{Arg}_0(0)=0\), including signed IEEE zero. For \(\lambda=0\), synchronization returns the input directly.

The open domain

\[
 \mathcal U_k=\{z:\widetilde z_i\ne0\text{ for all }i\}
\]

guarantees real analyticity of the complete map and common-phase equivariance. This uses the analytic unit factors \(w_i/|w_i|\), not differentiability of a principal-argument branch cut. For D0's relative equilibria use the stronger domain

\[
 \mathcal D_k=\{z:z_i\ne0,\ \widetilde z_i\ne0\ \forall i\}.
\]

Nonzero input alone is insufficient: \(z=(1,1,2)\), \(\epsilon=1,g=0,k=0\) gives \(\widetilde z=(0,0,-6)\). No forward-invariance theorem for \(\mathcal U_k\) or \(\mathcal D_k\) is assumed. At \(\lambda=0\), the full map is polynomial globally; at nonzero \(\lambda\), some exceptional zero states still happen to respect common rotations, but there is no all-state U(1) theorem.

## 3. Section B: the misplaced imaginary coefficient

**DERIVED IDENTITY.** Use the script's definitions, with positive \(a,b,c\), real \(g,\ell\), and Bloch coordinate \(\zeta\ne0\):

\[
 D(\zeta)=\begin{pmatrix}-2&1&\zeta^{-1}\\1&-2&1\\\zeta&1&-2\end{pmatrix},\quad R=\operatorname{diag}(a,b,c),\quad s=a+b+c,
\]
\[
 H=I+g\left[D-\operatorname{diag}\left(\frac{s-3a}{a},\frac{s-3b}{b},\frac{s-3c}{c}\right)\right],\quad P=R^{-1}HR.
\]

Keep three objects separate:

\[
 J_{\rm nat}=(I+\ell D)P,\qquad J_{\rm sum}=P+\ell D,\qquad K=\frac{J_{\rm sum}-I}{h}
 \quad(g=h\widehat g,\ \ell=h\widehat\ell).
\]

\(J_{\rm sum}\) is an additive **step** comparator. It is not itself the generator. For a 3-by-3 matrix define \(t=\operatorname{tr}J\), \(b=B_2(J)=[t^2-\operatorname{tr}(J^2)]/2\), \(d=\det J\). Its characteristic polynomial is \(\mu^3-t\mu^2+b\mu-d\).

Set

\[
 V=\frac{(a-b)(a-c)(b-c)}{abc},\quad
 \chi=g\ell(\ell-g)V,\quad
 \Gamma=g\ell[\ell(1+3g)-g]V.
\]

Then the exact Laurent identities are

\[
 t_{\rm sum}(\zeta)=t_{\rm sum}(\zeta^{-1}),\quad
 b_{\rm sum}(\zeta)=b_{\rm sum}(\zeta^{-1}),\quad
 d_{\rm sum}(\zeta)-d_{\rm sum}(\zeta^{-1})=\chi(\zeta-\zeta^{-1}),
\]
\[
 t_{\rm nat}(\zeta)=t_{\rm nat}(\zeta^{-1}),\quad
 b_{\rm nat}(\zeta)-b_{\rm nat}(\zeta^{-1})=-\Gamma(\zeta-\zeta^{-1}),\quad
 d_{\rm nat}(\zeta)=d_{\rm nat}(\zeta^{-1}).
\]

**Proof of the additive identities.** The diagonal entries are real and independent of \(\zeta\). Each off-diagonal pair product, including the wrapping pair, cancels its Bloch factors. Thus the trace and every principal 2-by-2 minor are real and independent of those factors. In the determinant, only the two oriented three-cycles carry an unmatched factor. Their coefficients differ by

\[
 (ga/c+\ell)(gb/a+\ell)(gc/b+\ell)
 -(gc/a+\ell)(ga/b+\ell)(gb/c+\ell)=g\ell(\ell-g)V.
\]

This proves the determinant formula. For the native map, multiplication followed by the same trace/minor expansion gives the displayed \(-\Gamma\) difference; this expansion is independently checked symbolically. Its determinant is inversion-even because \(\det J_{\rm nat}=\det(I+\ell D)\det H\), and \(H(\zeta^{-1})=H(\zeta)^T\), with the same relation for \(D\).

For \(\zeta=e^{i\theta}\), complex conjugation equals \(\zeta\mapsto\zeta^{-1}\). Therefore

\[
 \boxed{\Im B_2(J_{\rm sum})=0,\qquad \Im\det J_{\rm sum}=\chi\sin\theta.}
\]

By contrast \(\Im B_2(J_{\rm nat})=-\Gamma\sin\theta\) and \(\Im\det J_{\rm nat}=0\). The original Section B printed \(-\Im B_2(J_{\rm sum})=0\) beside \(\chi\), without an equality predicate. It is a mismatch, not a passing check. At its rational fixture \((a,b,c,g,\ell,\zeta)=(4/5,1,13/10,1/5,3/100,i)\), the corrected exact determinant imaginary part is \(153/5200000\), while the middle imaginary coefficient is exactly zero.

### Generator and decrement-rate polynomials

Since \(J_{\rm sum}=I+hK\), with \(K\) independent of \(h\), its characteristic coefficients satisfy

\[
 t_K=\frac{t_{\rm sum}-3}{h},\quad
 b_K=\frac{b_{\rm sum}-2t_{\rm sum}+3}{h^2},\quad
 d_K=\frac{d_{\rm sum}-b_{\rm sum}+t_{\rm sum}-1}{h^3}.
\]

These follow either from the three eigenvalue shifts or by expanding \(\det(I+hK)\); no diagonalizability assumption is needed. Put \(\widehat\chi=\widehat g\widehat\ell(\widehat\ell-\widehat g)V\). Then

\[
 \Im t_K=\Im b_K=0,\qquad \Im d_K=\widehat\chi\sin\theta.
\]

The generator polynomial is \(\xi^3-t_K\xi^2+b_K\xi-d_K\). The script's Section F reports the **decrement rates** \(\rho=(1-\mu)/h\), the negatives of generator eigenvalues; their polynomial is \(\rho^3+t_K\rho^2+b_K\rho+d_K\). If \(\widehat\chi\sin\theta\ne0\), not all three roots can be real. This explains why the Section B correction is consistent with Section F's complex rates. A vanishing obstruction is not, alone, a theorem of real spectrum.

For the exact native finite-step generator comparator \(K_h^{\rm nat}=(J_{\rm nat}-I)/h\), write \(P=I+hQ\). Then

\[
 K_h^{\rm nat}=K+h\widehat\ell DQ,
\]
\[
 \Im b_{K_h^{\rm nat}}=-h[\widehat\chi+3h\widehat g^2\widehat\ell^2V]\sin\theta,
 \qquad
 \Im d_{K_h^{\rm nat}}=[\widehat\chi+3h\widehat g^2\widehat\ell^2V]\sin\theta.
\]

Its trace remains real. The native middle-coefficient obstruction disappears in the generator limit while the determinant obstruction remains. When \(\widehat\ell=\widehat g\), the leading determinant obstruction vanishes and the displayed native correction is of higher order. This is an algebraic limit, not a physical time calibration.

The old script uses NumPy matrix arithmetic. Setting `mp.mp.dps = 60` does not change NumPy arithmetic. Its outputs remain bounded numerical diagnostics, not a symbolic or high-precision all-pass suite. They were preserved and not rerun as an expanded larger-ring experiment. Equality of chirality bilinears proves a kinematic identity; it does not prove a conserved Noether current. For example, with \(g=\lambda=0,\epsilon=1/4,k=0\), a state with all three moduli one is multiplied by \(3/4\); a nonzero chirality is multiplied by \(9/16\), not conserved.

## 4. Gradient increments, descent, and zero-stratum symmetry

### 4.1 Amplitude stage

**DERIVED IDENTITY.** In real coordinates \(z_i=x_i+iy_i\), the native potential is

\[
 V=\epsilon\sum_i\left(\frac{|z_i|^4}{4}-\frac{k_i|z_i|^2}{2}\right)
 +\frac g2\sum_{\{i,j\}\in E}|z_i-z_j|^2.
\]

Its negative real Euclidean gradient is exactly \(A_k(z)-z\). The onsite Hessian at \(v_i=(x_i,y_i)^T\) is

\[
 \epsilon\big[(|z_i|^2-k_i)I_2+2v_iv_i^T\big],
\]

and the graph Hessian is \(gL\otimes I_2\), \(L=-\Delta\), in site-interlaced coordinates. Let \(d=-\nabla V(z)\). Taylor's integral remainder proves that if \(\nabla^2V(z+td)\preceq LI\) on the whole segment, with \(L<2\), then

\[
 V(z+d)\le V(z)-(1-L/2)\|\nabla V(z)\|^2.
\]

A conservative, explicit sufficient condition is

\[
 |\epsilon|(3R^2+K)+|g|\Lambda<2,
\]

where every component on that segment has modulus at most \(R\), \(|k_i|\le K\), and \(\Lambda=\|L\|_2\le4\) (exactly 3 for the triad). Endpoint component bounds imply the same segment bound by convexity of each disk. This is a region/step hypothesis, not a globally imposed model restriction. With \(V=h\widehat V\), the equivalent sufficient small-step condition is \(h\widehat L<2\) for descent of fixed \(\widehat V\). At the established witness \(z=(2,2,2),\epsilon=1,g=0,k=1\), \(V\) instead rises from 6 to 168.

### 4.2 Phase stage and the sign of lambda

Let the fixed phase energy be

\[
 E(\theta)=-\frac13\sum_{\{i,j\}\in E}\cos3(\theta_j-\theta_i),\quad U_\lambda=\lambda E.
\]

Then \(\theta^+=\theta-\lambda\nabla E=\theta-\nabla U_\lambda\), with

\[
 \nabla^2U_\lambda=3\lambda\sum_e\cos(3\Delta_e\theta)L_e,
 \qquad \|\nabla^2U_\lambda\|_2\le3|\lambda|\Lambda.
\]

The norm bound follows by bounding the absolute value of its quadratic form by \(3|\lambda|\sum_e(v_i-v_j)^2\). Consequently:

- For descent of **fixed** \(E\), \(0<\lambda<2/(3\Lambda)\) is sufficient, with strict decrease unless its gradient vanishes. On every cycle, \(0<\lambda<1/6\) suffices; on the triad the sharper sufficient bound is \(0<\lambda<2/9\). At \(\lambda=0\) the step is the identity.
- For descent of the **lambda-scaled** \(U_\lambda\), the sufficient condition is \(3|\lambda|\Lambda<2\), allowing negative lambda. For small negative lambda, decreasing \(U_\lambda\) means increasing fixed \(E\).

Thus the note's unsigned statement “lambda < 1/6” is incomplete, and its norm bound needs an absolute value. These are phase-chart statements on nonzero components. On a zero stratum, phase reconstruction resets the assigned phase at a zero output, so one cannot silently claim the same state-level phase-energy descent theorem there. Separate stage descent does not establish a common Lyapunov function for the composition.

### 4.3 Exact zero-stratum symmetries

**EXACT THEOREM.** Conjugation commutes with both stages on all states in ideal exact arithmetic. At nonzero components, arguments negate modulo \(2\pi\); at zero, Arg0 remains zero. Sine increments change sign, and outputs conjugate. Native floating-point evaluation satisfies this only to its arithmetic accuracy.

For independent \(\omega_i=e^{2\pi in_i/3}\), synchronization satisfies \(S_\lambda(\omega\odot w)=\omega\odot S_\lambda(w)\) even at exact zeros: a nonzero argument shifts by \(2\pi n_i/3\), while a zero retains argument zero. Either change is invisible inside every triple-angle sine, and a zero output stays zero. This proves local Z3 for the **phase stage**, not the coupled full map. The onsite stage alone respects arbitrary independent rotations; the graph term generally reduces these to common rotations for \(g\ne0\). At \(g=0\), the full local Z3 identity does hold. Common Z3 is also retained globally, even on zero strata.

Arbitrary common U(1) rotation fails on zero strata in general. For \(w=(0,1,1)\), rotating by \(\alpha=\pi/6\) makes each nonzero site's kick \(-\lambda\), although the unrotated kicks are zero. The assigned zero phase does not rotate. This is an exact counterexample when \(e^{-i\lambda}\ne1\).

Only graph automorphisms may be used as site-permutation symmetries. On the triad these are all of \(S_3=D_3\); on a general cycle they are dihedral permutations. The ordered coefficient tuple must be transformed along with the state. Permuting arbitrary sites of a larger ring is not a symmetry assertion licensed by the source.

The note's distinction between polar coordinate metric, response operators, nonunique SPD inner products, interaction graph, and unidentified physical spacetime is retained. The triad calculation below concerns state-space response. No new gravity/QED assessment follows. Statements about locally contracting fixed backgrounds remain restricted to those backgrounds; a negative real multiplier can alternate sign between iterations, so “real spectrum” should not be read as excluding every alternating response.

## 5. Relative-equilibrium identity and the symmetry table

Let \(F_k(z)=e^{i\omega}z\) on \(\mathcal D_k\), with \(\omega\) modulo \(2\pi\), and evaluate \(\delta_i\) at the **actual** \(\widetilde z=A_k(z)\).

**EXACT THEOREM.** The prestage can be written \(\widetilde z=B(z)z\), where

\[
 B(z)=\operatorname{diag}[1+\epsilon(k_i-|z_i|^2)]+g\Delta
\]

is real symmetric. Therefore \(z^\dagger B(z)z\) is real. Synchronization preserves moduli, so on a relative equilibrium \(\widetilde z_i=e^{i(\omega-\delta_i)}z_i\). Taking the imaginary part gives

\[
 \boxed{\sum_i|z_i|^2\sin(\omega-\delta_i)=0.}
\]

With \(S=\sum_i|z_i|^2e^{i\delta_i}\), this is \(\Im(e^{i\omega}\overline S)=0\). It implies \(\omega=\arg S\pmod\pi\) **only if \(S\ne0\)**. If \(S=0\), the sine identity remains true but imposes no restriction on omega. This missing qualifier in the note matters generally. In D0's chosen domain, \(|\delta_i|\le2|\lambda|\le1/60<\pi/2\), so \(\Re S>0\); the issue is excluded there.

If \(\lambda=0\), \(S=\sum_i|z_i|^2>0\), giving \(\omega\in\{0,\pi\}\). On the near-zero branch, expansion of \(\arg S\), together with exact \(\sum_i\delta_i=0\), gives

\[
 \omega=\frac{\sum_i(|z_i|^2-\overline{r^2})\delta_i}{\sum_i|z_i|^2}
 +O(\max_i|\delta_i|^3),\qquad
 \overline{r^2}=N^{-1}\sum_i|z_i|^2.
\]

This is a leading small-kick statement, not an exact all-orders criterion that amplitude inhomogeneity is necessary for finite-step drift. Zero total kick alone does not force zero argument of its exponential sum. For example, kicks \((t,t,-2t)\) have zero sum but \(\Im(2e^{it}+e^{-2it})\ne0\) generically. This example illustrates the identity's limitation; it is not a claim of a new relative equilibrium.

Define winding using the principal neighbor differences, away from zero components and neighbor differences equal to pi, and define the oriented triad chirality \(\Gamma_z=\sum_j\Im(\overline z_jz_{j+1})\). Use indices \(j=0,1,2\), positive cyclic orientation, translation \(\tau z_j=z_{j-1}\), and reflection \(\rho z_j=z_{-j}\).

| Operation | State | Ordered coefficients | Winding, chirality | Omega |
|---|---|---|---|---|
| Common phase | \(e^{i\alpha}z\) | \(k\) | unchanged | unchanged |
| Conjugation C | \(\bar z\) | \(k\) | both negated | negated |
| Reflection rho | \(z_{-j}\) | \((k_0,k_2,k_1)\) | both negated | unchanged |
| C rho | \(\bar z_{-j}\) | \((k_0,k_2,k_1)\) | unchanged | negated |
| Translation tau | \(z_{j-1}\) | \((k_2,k_0,k_1)\) | unchanged | unchanged |

**Proof.** For each graph automorphism \(P\), \(F_{Pk}(Pz)=PF_k(z)\), since the Laplacian and neighbor sum commute with it and the onsite coefficients travel with their entries. Complex conjugation changes \(e^{i\omega}\) into \(e^{-i\omega}\). A reflection reverses orientation of every edge in the winding/chirality sums. A translation does not. Common-phase covariance is applied only on the regular domain. These identities prove the table. Gauge restoration, when necessary, is a common rotation and does not change omega or the labels.

If two coefficients coincide, a reflection fixes their tuple. Combining it with conjugation fixes the chirality label and reverses omega. **Symmetry alone still allows two different states with opposite drift.** To conclude zero drift requires a locally unique branch modulo phase, invariance of that branch under this combined operation, regularity, and a near-zero angle continuation that excludes pi. Then uniqueness gives \(C\rho z=e^{i\beta}z\), and equivariance gives \(e^{i\omega}=e^{-i\omega}\); continuity selects zero rather than pi.

At a moving relative equilibrium, “multiplier one” means the derivative of the **co-rotating map** \(e^{-i\omega}F_k\), not unqualified \(DF_k\). At D0's fixed reference omega is zero, so they agree. A simple group multiplier is a sufficient local isolation condition; it is not a necessary characterization of every possible isolated nonlinear solution.

**Interpretation boundary.** Omega measures a common complex phase increment. At a relative equilibrium, \(zz^\dagger\), all intensities, winding, and common-phase-invariant chirality readouts are unchanged. This does not supply a spatial core-position law or rigid rotation of the fixed measurement scaffold. Equality of a bilinear with a familiar current formula does not change that conclusion.

## 6. Twisted reference: existence and the complete derivative

### 6.1 Ordinary and sign-flipping branches

For equal \(k_j=\bar k\), write

\[
 z_j=Ae^{i\phi j},\quad \phi=2\pi m/N,\quad A>0,\quad
 h_m=2-2\cos\phi=4\sin^2(\pi m/N).
\]

Then \(\Delta z=-h_mz\) and \(\widetilde z=cz\), where

\[
 c=1+\epsilon(\bar k-A^2)-gh_m.
\]

For \(c\ne0\), all phases receive the same possible extra pi, and each synchronizer kick cancels: \(\sin3\phi+\sin(-3\phi)=0\). Thus \(F(z)=cz\) on this ansatz. A nonzero relative equilibrium requires \(|c|=1\), giving exactly two possibilities within this ansatz:

\[
 c=1:\quad A^2=\bar k-gh_m/\epsilon>0,\quad\omega=0;
\]
\[
 c=-1:\quad A^2=\bar k-(gh_m-2)/\epsilon>0,\quad\omega=\pi.
\]

These formulas assume \(\epsilon\ne0\). At \(c=0\), the entire prestage and output vanish, so no nonzero relative equilibrium results. At \(\epsilon=0\), amplitudes are unconstrained if \(gh_m=0\) for the fixed branch or \(gh_m=2\) for the pi branch; such amplitude continua fail the isolation test used here. These are classifications of the twisted ansatz, not of all native relative equilibria.

For the triad modes \(m=1,2\), \(h_m=3\). Use representatives \(\phi=2\pi/3,-2\pi/3\). The principal winding is respectively \(+1,-1\), not \(+1,+2\). For a uniform twist generally it is \(N\operatorname{Arg}(e^{i\phi})/(2\pi)\); writing \(w=m\) requires the signed representative with \(|\phi|<\pi\). The chirality is \(NA^2\sin\phi\). Conjugation exchanges these references, while C rho fixes each reference up to the allowed gauge.

### 6.2 Derive before separating

**DERIVED IDENTITY.** Perturb in the rotating local channel coordinates:

\[
 z_j=e^{i\phi j}(A+a_j+ib_j).
\]

At the ordinary fixed branch, direct differentiation of the cubic onsite term gives \(-2\epsilon A^2a_j\) relative to its phase derivative. The shifted neighbors carry factors \(e^{\pm i\phi}\). For a Fourier perturbation \((a_j,b_j)=(a,b)e^{i\vartheta j}\), put \(u=1-\cos\vartheta\). The prestage derivative is

\[
 \begin{pmatrix}D_a&-iX\\iX&D_b\end{pmatrix},\quad
 D_a=1-2\epsilon A^2-2g\cos\phi\,u,\quad
 D_b=1-2g\cos\phi\,u,\quad X=2g\sin\phi\sin\vartheta.
\]

For example the real part's coupling to \(b\) is \(-g\sin\phi(b_{j+1}-b_{j-1})=-iXb\), and the imaginary part's coupling to \(a\) has the opposite sign. These mixed terms do not disappear on a twisted reference.

At the reference, prestage modulus equals A and its kick is zero. Thus the sync derivative preserves the real radial perturbation and sends its imaginary perturbation to \((I+3\lambda\cos3\phi\,\Delta)b\). The complete Fourier block is

\[
 \boxed{M(\vartheta)=\begin{pmatrix}1&0\\0&\sigma_\vartheta\end{pmatrix}
 \begin{pmatrix}D_a&-iX\\iX&D_b\end{pmatrix},\quad
 \sigma_\vartheta=1-2\ell\cos3\phi\,u,\quad\ell=3\lambda.}
\]

This verifies the reconciliation's formula. The order of the two factors matters. At \(\vartheta=0\), the multipliers are \(1-2\epsilon A^2\) and 1. In every other mode the multiplier-one determinant is

\[
 (D_a-1)(\sigma_\vartheta D_b-1)-\sigma_\vartheta X^2.
\]

If these are nonzero and \(\epsilon A^2\ne0\), the only unit multiplier is the algebraically simple common-phase one. Conjugate Fourier modes reconstruct the full real derivative; no unstable direction has been discarded. Only the triad is used for D0's gate. No larger-ring reference experiment was performed.

## 7. One rational reference family and the full isolation certificate

Choose, without a parameter search,

\[
 (\widehat\epsilon,\widehat g,\widehat\lambda,\bar k)
 =\left(1,\frac16,\frac1{30},1\right),\quad
 (\epsilon,g,\lambda)=h\left(1,\frac16,\frac1{30}\right),\quad
 \kappa=(-1,0,1).
\]

The selected domain is \(0<h\le1/4\); \(\widehat\ell=1/10\). The perturbation direction is nontrivial, zero-sum, and three-distinct. It is specified for a future test only. At eta zero,

\[
 A^2=1-3/6=1/2,\qquad
 z_j^*=2^{-1/2}e^{\pm2\pi ij/3},\qquad \widetilde z^*=z^*.
\]

All reference components and prestage components are nonzero. Chirality is \(\Gamma_z=\pm3\sqrt3/4\). This parameter choice is checked directly rather than borrowed from Paper G.

For nonzero triad Fourier modes, \(X=\pm h/4\), and

\[
 D_a=1-3h/4,\quad D_b=1+h/4,\quad\sigma=1-3h/10,
\]
\[
 q_h(\mu)=\det(\mu I-M)
 =\mu^2-\left(2-\frac45h-\frac3{40}h^2\right)\mu
 +1-\frac45h-\frac1{10}h^2+\frac3{40}h^3,
\]
\[
 \boxed{q_h(1)=\frac{h^2(3h-1)}{40}\ne0.}
\]

The full six-real-dimensional characteristic polynomial is

\[
 (\mu-1)(\mu-(1-h))q_h(\mu)^2.
\]

The common amplitude multiplier \(1-h\) is distinct from one. Since \(q_h(1)<0\), each real-coefficient quadratic has one root below one and one above one. In fact \(q_h(0)>0\) throughout this interval, so the lower root lies in \((0,1)\). The reference has three contracting real directions, two expanding real directions, and its one phase-neutral direction. It is a valid saddle; stability was not a gate requirement. The degeneracy at \(h=1/3\) lies outside the selected interval.

### 7.1 Gauge and seven real equations

Use a reference-specific slice

\[
 \gamma(z)=\frac{\Im\langle z^*,z\rangle}{\|z^*\|^2}=0,
 \qquad \Re\langle z^*,z\rangle>0.
\]

The tangent to the group orbit is \(q=iz^*\), and \(d\gamma(q)=1\). This slice is valid even though the reference's unweighted channel sum is zero; a gauge based on that zero sum would not be valid.

For fixed positive h, the full unknowns are six real state coordinates and omega, with six real equations \(F_h(z,k)-e^{i\omega}z=0\) plus gamma. At the reference its border is

\[
 \begin{pmatrix}J_h-I&-q\\d\gamma&0\end{pmatrix}.
\]

For a uniform small-step continuation use \(\nu=\omega/h\) and the rescaled residual

\[
 \mathcal H(h,z,k,\nu)=\frac{F_h(z,k)-e^{ih\nu}z}{h},\qquad \gamma(z)=0.
\]

The corresponding reference border is

\[
 \mathcal B_h=\begin{pmatrix}(J_h-I)/h&-q\\d\gamma&0\end{pmatrix}.
\]

**EXACT SYMBOLIC CERTIFICATE, with written justification.** Direct construction of the complete 6-by-6 real derivative, followed by this 7-by-7 border, gives

\[
 \boxed{\det\mathcal B_h=-\frac{(3h-1)^2}{1600}.}
\]

Alternatively decompose into the common radial/group modes and the two transverse Fourier modes. The border pairs the sole group zero direction with \(-q\) and gamma, contributing determinant one. The common radial eigenvalue of \((J_h-I)/h\) is \(-1\), and each transverse determinant is \((3h-1)/40\). Multiplying gives the same certificate. This removes only the common phase. All five other state directions, including the unstable ones, remain in the equations. The unrescaled omega border has determinant \(-h^5(3h-1)^2/1600\).

For \(0\le h\le1/4\), \(|\det\mathcal B_h|\ge1/25600\). This is an invertibility bound, not a claim that the determinant equals a condition number.

### 7.2 Legitimate extension at h zero

Near \(z^*\), all prestage components remain away from zero for h in a neighborhood of this compact interval. The amplitude map, unit complex factors, sine kicks, and exponential are jointly real analytic in state, k, and h. Since \(F_0(z,k)=z\), the numerator defining \(\mathcal H\) vanishes identically at h zero. Its convergent local power series therefore has a factor h. The analytic extension is

\[
 \mathcal H(0,z,k,\nu)=\mathcal X_k(z)-i\nu z,
\]
\[
 \mathcal X_k(z)_i=\widehat\epsilon z_i(k_i-|z_i|^2)
 +\widehat g(\Delta z)_i
 +i\widehat\lambda z_i\sum_{j\sim i}\sin3(\arg z_j-\arg z_i).
\]

Here the phase kick is evaluated at z because the prestage tends to z. This is a derived formal small-step generator; no physical time unit is supplied. Its derivative at the reference has eigenvalues

\[
 0\ (1),\quad -1\ (1),\quad
 \frac{-8+\sqrt{74}}{20}\ (2),\quad
 \frac{-8-\sqrt{74}}{20}\ (2).
\]

The numbers in parentheses are real multiplicities. Its rescaled border has determinant \(-1/1600\), not zero. Thus the generator-level isolation claim is made only after an analytic desingularization, not by setting h to zero in an identically vanishing unrescaled residual.

**EXACT THEOREM.** The analytic implicit-function theorem yields a locally unique gauge-fixed branch \((z(h,x),\nu(h,x))\), \(k=(1,1,1)+x\), near \(x=0\), including h zero. Restricting to \(\sum x_i=0\) gives the intended fixed-mean problem. The compact reference interval and uniformly invertible analytic border also permit a common sufficiently small neighborhood of x after shrinking charts. D0 proves existence of such a neighborhood; it does not provide a certified numerical eta radius. A future finite eta choice must be validated to stay inside it.

For this positive-epsilon family the twisted pi branch has \(A_\pi^2=1/2+2/h\). It does not approach the selected finite-amplitude reference as h tends to zero, and it is excluded locally by continuity. No claim excludes other pi states elsewhere.

## 8. Cubic selection, with no coefficient calculation

Fix the positively oriented reference \(m=1\), with the above gauge, and use the small unwrapped omega. At the reference, translation acts by a common phase, and C rho fixes the branch label. Apply each transformation, then restore the slice by a common phase. Local uniqueness proves the scalar identities

\[
 \nu(h,\tau x)=\nu(h,x),\qquad
 \nu(h,\rho x)=-\nu(h,x).
\]

Every odd permutation of the triad is a reflection followed by a cyclic permutation. Therefore nu, and hence omega, is an alternating real-analytic function of x. On any plane \(x_i=x_j\), it must vanish. An analytic function vanishing on a linear hyperplane is divisible by its defining linear form: choose that form as a coordinate and factor its Taylor series, or integrate its derivative in that coordinate. Successively doing this on the three distinct lines in the zero-sum plane gives

\[
 \nu_m(h,x)=(x_0-x_1)(x_1-x_2)(x_2-x_0)\,S_m(h,x),
\]

where the quotient is analytic and symmetric. The successive factors are legitimate because, away from their intersections, a previously removed factor is nonzero; analyticity extends the remaining vanishing to the intersection. The quotient has no symmetric linear term on \(\sum x_i=0\), since every permutation-invariant linear functional is proportional to \(x_0+x_1+x_2\).

Consequently for fixed kappa,

\[
 \boxed{\nu_m(h,\eta\kappa)=c_m^{\rm rate}(h)\,\eta^3
 (\kappa_0-\kappa_1)(\kappa_1-\kappa_2)(\kappa_2-\kappa_0)+O(\eta^5),}
\]
\[
 \omega_m(h,\eta\kappa)=h\nu_m(h,\eta\kappa).
\]

The absence of a fourth-order term is therefore justified. A sixth-order term is not forbidden: the symmetric quotient can contain a cubic invariant. There is no general assertion that omega is odd under arbitrary \(x\mapsto-x\); the chosen direction \((-1,0,1)\) happens to turn its negative into a reflected tuple, so its continuation does have that additional sign test.

For the chosen direction, the oriented product is 2. Conjugation gives \(c_{m=2}^{\rm rate}=-c_{m=1}^{\rm rate}\). Reversing the adopted ring orientation reverses winding/chirality labels and the oriented Vandermonde convention consistently. Pure reflection alone preserves omega while changing the branch label; its fixed-label, sign-reversing comparison is C rho.

**Qualification:** cubic is the first symmetry-allowed order. This proves neither \(c_m^{\rm rate}(h)\ne0\) nor \(c_m^{\rm rate}(0)\ne0\). A higher-order or identically zero scalar is fully consistent with D0. The note's phrase “the drift is cubic” must be read as “drift is divisible by this cubic factor.” The verifier checks low-degree representation dimensions but never evaluates the actual native drift coefficient.

## 9. Claim disposition

| Claim | D0 disposition |
|---|---|
| Section B's additive middle-coefficient imaginary formula | **Corrected:** zero middle imaginary part; proposed chi belongs to the determinant. Native composition has a different coefficient placement. |
| Complex rates in original Section F | **Consistent with the corrected exact determinant obstruction.** NumPy values are retained diagnostics; no new larger-ring run. |
| Prestage and phase gradient increments | **Verified with native normalizations.** Distinct coordinate gradients do not prove composite descent or a common metric. |
| Phase bound “lambda < 1/6” | **Qualified:** positive lambda for descent of fixed energy; absolute-value bound for descent of lambda-scaled potential. |
| Amplitude descent | **Conditional:** a Hessian upper bound below 2 on the whole actual step segment, with explicit sufficient radius/step bound. |
| U(1), conjugation, local Z3 | **Domain-separated:** U(1) on the regular prestage domain; conjugation and phase-stage local Z3 include zeros. Full graph coupling generally breaks local Z3. |
| Permutations | **Graph automorphisms with coefficient ordering carried along.** All permutations only for the triad. |
| Exact sine drift identity | **Verified.** Its argument reformulation additionally needs a nonzero weighted exponential sum. Leading torque correlation is not an all-orders necessity theorem. |
| Reflection reverses drift | **Only in the fixed-label C rho comparison.** Pure reflection preserves omega and flips the label. |
| Two equal coefficients force zero | **True locally on the analytic isolated continuation near omega zero,** not from coefficient equality alone. |
| Twisted fixed branch and pi alternative | **Verified within the ansatz,** with epsilon, positivity, and prestage-factor conditions. Triad m=2 has principal winding minus one. |
| Complete twisted linearization | **Verified, including mixed terms and composition order.** |
| Isolation | **Verified by the full seven-real-variable border** for one rational family on an explicit h interval, including the desingularized generator endpoint. |
| Cubic selection | **Verified as divisibility and an allowed leading order; coefficient not computed.** |
| Chirality identities imply a conserved Noether current | **Not established; bilinear equality is insufficient**, and native chirality need not be conserved. |
| Coordinate metric / response / symmetrizer / graph / physical spacetime | **Keep distinct.** No physical-motion or spacetime identification is adopted. |
| No drift would prove equilibrium/variational physics | **Rejected as an inference.** A future zero result is branch- and parameter-restricted. |

The original review's model-class comparisons are useful descriptions at the level of the displayed increments and harmonic energies. A composition of explicit gradient **steps** should not be mistaken for a composition of exact gradient-flow time maps. Nor should linear Jacobians be declared self-adjoint at arbitrary states merely because a stage has a gradient-form increment. D0 establishes the equations and conditions above, rather than a new universal model-class or physics verdict.

## 10. Verification results and their limits

The external script records named exact symbolic predicates, source-byte checks, native numerical comparisons, high-precision independent comparisons, and preservation checks separately. The first complete run passed **64/64**. The results file records the final count and every predicate, with no promotion of the predecessor's printed diagnostics into retrospective pass/fail assertions.

Exact checks include the Laurent coefficient identities, characteristic-coefficient rescalings, six-real-coordinate potential gradient, Hessians, total prestage imaginary pairing, the complete reference characteristic polynomial, both Fourier intertwiners, the full bordered determinant, and alternating-polynomial dimensions through degree four. The latter dimensions are \(0,0,0,1,0\), confirming the allowed cubic and forbidden quartic terms; the all-orders divisibility rests on the analytic proof in §8.

Bounded numerical evidence:

| Comparison | Arithmetic / prescribed fixture | Result |
|---|---|---|
| Actual `step3` at the twisted reference | Native complex128, h=1/10 | Maximum fixed residual about \(2.01\times10^{-16}\). |
| Independent full native formula at the reference | mpmath 100 decimal digits; h=1/4,1/10,1/100; eta=0 only | Maximum fixed residual below \(3.76\times10^{-103}\). |
| All six real columns of the complete Jacobian | 100 digits, central difference \(10^{-30}\), h=1/10 | Maximum error about \(1.00000000004\times10^{-61}\) against the exact matrix. |
| Zero-stratum and ordered symmetry comparisons | Native complex128, a few explicitly specified states | Conjugation and local-Z3 tests pass; the arbitrary-U(1) zero-stratum counterexample has defect about 0.09996. |
| Source and preservation | Raw byte hashes and Git fingerprints | All original evidence identities and all protected-root comparisons pass. |

The high-precision formula is an independent transcription, not a claim that the native implementation runs at 100 digits. Finite differences are not interval certificates. Exact isolation follows from the symbolic determinant and written proof; its conclusion is not inferred from small residuals alone. No positive eta drift solve, nonlinear iteration, or finite-step scan was used.

## 11. Proposed D1 specification — not executed

**OPEN QUESTION:** on this isolated branch, is the allowed cubic coefficient nonzero, and if it is, does its rate survive the small-step limit?

One bounded later test can use exactly the tuple in §7 and \(\kappa=(-1,0,1)\), preserving all source equations. Solve the seven real equations \((\mathcal H,\gamma)=0\), including nu, by local continuation from the certified reference. Use the analytic h-zero residual as well as prescribed positive steps \(h=1/10,1/100,1/1000\); no retuning of hatted coefficients to elicit drift. Both chiral entrances are fixed in advance.

A prospective eta ladder is \(\pm1/100,\pm1/200,\pm1/400\), but these values are **not certified by D0**. Before using them, validate continuation and regularity, for example by interval Newton bounds on the full bordered equations. If the proposed ladder falls outside the certified local neighborhood, choose a smaller nested ladder within it; do not switch to a different root or fit parameters. Use at least 100 decimal digits for numerical diagnostics, and error bounds that resolve division by \(\eta^3\); precision alone is not certification.

For each accepted root report full residuals, gauge residual, minimum input/prestage modulus, branch winding/chirality, and bordered invertibility. Check the exact weighted sine identity with the **computed prestage** kicks. Check conjugation, cyclic ordering, C rho order reversal, and an independently validated two-equal-coefficient branch comparison. Do not infer drift from a long trajectory.

Estimate or bound \(\nu/(2\eta^3)\), with the \(O(\eta^2)\) correction controlled before calling it a cubic coefficient. Report omega, omega/h, and omega/h² separately. A nonzero coefficient for the h-zero residual would establish a generator-level rate on this branch. If it vanishes there but an h-derivative is certified nonzero, the leading per-step angle is of order h². A null result must state its parameter, branch, error, and resolved-order limits; it does not identify an equilibrium physical model. Finite fixtures alone do not prove an h-asymptotic classification.

## 12. Checkpoint conclusion

**D0 = PASS_WITH_QUALIFICATIONS:** the requested experiment setup exists and is locally isolated. The explicit saddle reference and the full analytic border make the future drift question well posed; the sign/domain/coefficient corrections prevent the predecessor diagnostics from answering it prematurely.

The remaining mathematical question is whether the permitted scalar coefficient is nonzero. The remaining physical interpretation gap is separate: a common complex phase increment is not yet a spatial motion observable, a physical clock, or a core/scaffold rotation law. D0 introduces none of those ingredients.

**STOP:** no unequal-branch drift was solved, no drift coefficient was calculated, and no new model, paper, or implementation was begun. The TL synthesis remains a separate outstanding write-up.
