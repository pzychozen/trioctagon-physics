# Gravity and magnetism: native deductions and a conditional physical extension

20 November 2026 · Research note GM01 · Prepared for author and scientific review

**Status:** proposed analysis, with exact algebra checked; not an accepted physical theory, an adopted model revision, or a publication. The accepted Research Manual R1 remains unchanged. This note responds to the instruction to work from the existing equations first and develop an explicit candidate extension where necessary.

## 1. Result and scope

The existing native equations determine internal dynamics and several quantities suitable for a physical correspondence. They do not yet select a gravitational or electromagnetic source–field–force–motion law. This is a specific nonselection result for the current dictionary, not a theorem excluding emergent gravity or magnetism.

A concrete conditional construction is available. Use native total intensity as a *candidate* mass contribution and Paper G's ambient axial observable as a *candidate* magnetic dipole moment. Add physical positions, a dimensional dictionary, Newtonian gravity and magnetostatics. The resulting equations produce attractive inverse-square gravity and magnetic dipole interactions. Those spatial laws enter as explicit extra premises; reproducing them is a consistency result, not their derivation from the Tri-Octagon recurrence.

The native algebra contributes a sharp constraint on this candidate:

\[
 \boxed{\ |\boldsymbol\mu|
 \le \frac{|\kappa|}{\alpha}\sqrt{\frac38}\,(m-m_0)\ },
 \qquad m=m_0+\alpha I_\Omega,\quad
 \boldsymbol\mu=\kappa R W,\quad \alpha>0.
 \tag{GM1}
\]

The bound is sharp over the full complex triad state space. Attainment by an evolving state on a particular accepted trajectory is a separate question. No gravitational constant, magnetic coupling, physical clock, or mass scale has been predicted.

This note treats one native triad as the internal state of each proposed body. It does not identify an individual face with an elementary particle, replace the SRG mass-shell dictionary, or give the accepted transport channels an unproved spatial route.

## 2. What is inherited

All primary project sources below were recovered from commit
ca22652dc000ca2b16419c1af4167918eab1ae94 and checked against the accepted atlas's byte counts, SHA-256 hashes and Git blob identities. The source guide at the end identifies exact equations. Historical recovery notes were consulted to avoid reviving withdrawn exclusions.

For \(\Omega=x+iy\in\mathbb C^3\), with \(e=(1,1,1)^T\) and \(L=ee^T-3I_3\), the native update is

\[
\begin{split}
v&=\Omega+\epsilon\Omega\odot(k-|\Omega|^2)+gL\Omega,\\
\delta_i&=\lambda\sum_{j\ne i}\sin 3(\operatorname{Arg}_0 v_j-\operatorname{Arg}_0 v_i),\\
F_i(\Omega)&=v_i e^{i\delta_i}.
\end{split}\tag{N1}
\]

The three kicks use the same prestage. The zero convention is \(\operatorname{Arg}_0(0)=0\). Common-phase equivariance of the complete map is asserted on the regular domain where every prestage is nonzero; conjugation symmetry holds globally. [NPC setting]

The specified native scalar is

\[
 V(\Omega)=\epsilon\sum_i\left(\frac{|\Omega_i|^4}{4}
 -\frac{k_i|\Omega_i|^2}{2}\right)
 +\frac g2\sum_{i<j}|\Omega_i-\Omega_j|^2,
 \qquad v-\Omega=-\nabla_{\mathbb R^6}V.
 \tag{N2}
\]

The second equality is an internal-state increment identity. Full-map descent has already been proved under the local and finite-domain hypotheses in NPC. Neither the gradient identity nor that descent theorem makes \(V\) a gravitational potential per unit mass. Their variables and units differ.

Paper G defines

\[
 I_\Omega=\|\Omega\|^2,\quad C=x\times y,\quad
 \Gamma=e^TC,\quad W=TC,\qquad
 T=\begin{pmatrix}
 -1/2&1&-1/2\\
 -\sqrt3/2&0&\sqrt3/2\\
 0&0&0
 \end{pmatrix}.
 \tag{N3}
\]

The channel vector \(C\) and ambient vector \(W\) live in different spaces. Under the declared \(D_{3h}\) geometry action, \(W\) is axial. Up to a real scalar, \(T\) is the only real-linear equivariant map from that representation of \(C\) to an ambient axial vector. This uniqueness does not cover nonlinear observables. In particular, \(\Gamma e_z\) is polar-z-like under the declared action and cannot replace \(W\) as an axial magnetic observable. [G, Proposition attachment]

Three inherited distinctions remain essential:

- The fixed face metric and matched tangent transport are not an evolved spacetime metric. NRG's response inner products and screened graph response do not establish gravitational curvature.
- The spatial-work/causal-transport extension already has traveling fields, receiving storage and an exact work account. It is substantial prior work. Its age coordinate and product measure are declared mathematical structures, with physical location, clock and route correspondence still open. Saying that the project has “no propagation” would be false.
- The SRG product has a precise conditional collinear mass-shell correspondence after choosing \(K,c>0\). It does not specify how native intensity supplies its mass coordinate, or determine gravitational sources. Setting \(m=\alpha I_\Omega\) below is an additional ansatz, not a consequence of SRG.

## 3. Deductions from the existing equations

### D1. The current native map does not select a spatial force law

Suppose additional body coordinates \(X,P\) are appended to the native state. For any proposed mechanical update \(H\), the map

\[
 \widetilde F_H(\Omega,X,P)=\bigl(F(\Omega),H(\Omega,X,P)\bigr)
 \tag{D1}
\]

projects to exactly the same native recurrence. Free motion, Newtonian attraction and a screened interaction can therefore have identical projected native dynamics. The recurrence alone cannot distinguish these completions.

This is a proof of underdetermination **when the new mechanical variables have not yet been constrained by an additional correspondence**. It does not rule out a future construction in which position and force are derived observables of a larger native system, or an effective law proved in a controlled limit.

A narrower diagnostic makes the missing coupling visible. If independently positioned triads are assigned only the additive energy
\(E_{\rm int}=\sum_a V(\Omega_a)\), with the internal state held fixed when differentiating their centers, then
\[
 -\nabla_{X_a}E_{\rm int}=0.
 \tag{D2}
\]
One must add or derive position dependence before this energy yields a force between centers. Translating the labels of a fixed face attachment is not that derivation.

### D2. A sharp native intensity–axial relation

Paper G gives
\[
 I_\Omega^2=|\Omega\cdot\Omega|^2+4|C|^2,\qquad
 |C|^2=\frac23|W|^2+\frac{\Gamma^2}{3}.
\]
The dot in \(\Omega\cdot\Omega\) is bilinear, without conjugation. Eliminating \(C\) yields
\[
 \boxed{\ |W|^2=
 \frac38\left(I_\Omega^2-|\Omega\cdot\Omega|^2\right)
 -\frac12\Gamma^2
 \le\frac38 I_\Omega^2.\ }\tag{D3}
\]

Both subtracted terms are nonnegative. Equality requires
\(\Omega\cdot\Omega=0\) and \(\Gamma=0\), and is attained, for example, at
\(\Omega=(1,1,i\sqrt2)\): \(I_\Omega=4\), \(|W|^2=6\).
This proves sharpness without numerical optimization. It is a direct consequence of inherited identities, not an independent discovery of a physical mass–moment law.

Conversely, the Fourier states
\[
 (f_j)_n=3^{-1/2}e^{-2\pi ijn/3},\quad j=1,2,
\]
have \(W(cf_j)=0\), while
\(C(cf_1)=-\sqrt3|c|^2e/6\) and
\(C(cf_2)=+\sqrt3|c|^2e/6\).
Thus nonzero chirality need not produce a moment in the proposed linear dictionary. [G, hidden-area equation]

### D3. Intensity is not an automatically conserved electric charge

Let \(b=v-\Omega\) and \(s_i=|\Omega_i|^2\). Because the phase step preserves all moduli,
\[
 I_{F\Omega}-I_\Omega
 =2\epsilon\sum_i(k_i s_i-s_i^2)
 -2g\sum_{i<j}|\Omega_i-\Omega_j|^2+\|b\|^2.
 \tag{D4}
\]

An exact witness occurs **inside the accepted NPC finite domain at its actual parameter tuple**:
\[
 \epsilon=\frac1{10},\quad g=\frac1{60},\quad
 \lambda=\frac1{300},\quad
 k=\left(\frac{999}{1000},1,\frac{1001}{1000}\right),\quad
 \Omega=(1,1,1).
\]
Here \(L\Omega=0\), every prestage is positive and every phase kick vanishes. Consequently
\[
 F\Omega=\left(\frac{9999}{10000},1,\frac{10001}{10000}\right),
 \qquad I_{F\Omega}-I_\Omega=\frac1{50\,000\,000}\ne0.
 \tag{D5}
\]

If the total electric charge of an isolated body were defined as a nonzero constant times \(I_\Omega\), this witness would contradict charge conservation unless additional charge carriers or fluxes were supplied. It does not exclude other charge dictionaries. It also means that a mass assignment proportional to intensity needs an energy/matter exchange account if it is updated in physical time.

### D4. An axial readout and a common phase are not yet electromagnetic fields

For constant \(W\), the naive localization \(B(r)=b_0 W f(r)\) satisfies
\[
 \nabla\cdot B=b_0 W\cdot\nabla f.
 \tag{D6}
\]
For \(f(r)=e^{-|r|^2}\), this is
\(-2b_0(W\cdot r)e^{-|r|^2}\), generically nonzero. Axial symmetry alone therefore does not enforce the magnetic Gauss law.

Likewise, independent node phases \(D_\chi=\operatorname{diag}(e^{i\chi_i})\) do not commute with the fixed graph coupling:
\[
 (LD_\chi-D_\chi L)_{ij}
 =e^{i\chi_j}-e^{i\chi_i}\quad(i\ne j).
 \tag{D7}
\]
For \(g\ne0\), the prestage is not covariant under arbitrary local phases with the same fixed coupling. A common-phase symmetry is not already a local electromagnetic gauge connection. New link variables could transform as
\(U_{ij}'=e^{i\chi_i}U_{ij}e^{-i\chi_j}\); their dynamics and physical meaning would still have to be supplied. This observation does not exclude gauge structure emerging at another level.

## 4. Candidate extension E1: frozen-source Newtonian gravity and magnetostatics

This section supplies a complete static field problem and its mechanical interaction law. It is a deliberately explicit **candidate extension**, not an amendment to the accepted recurrence.

### Added premises

**E1a — Physical space and preparation.** Introduce centers \(X_a\in\mathbb R^3\), rigid orientations \(R_a\in SO(3)\), and physical lengths and times. Choose a smooth, nonnegative, radially symmetric, compactly supported profile \(\chi_\ell\) of integral one. Its support scale \(\ell\) is a new physical length. For this calculation the internal preparations \(\Omega_a\) and hence \(I_a,W_a\) are held fixed. No claim is made that every preparation is a native fixed point. Rigid pose is also a new degree of freedom; the finite native symmetry theorem alone does not supply an \(SO(3)\) dynamics.

**E1b — Source dictionary.** Choose \(m_{0a}\ge0\), \(\alpha>0\), real \(\kappa\), and states with positive
\[
 m_a=m_{0a}+\alpha I_a,\qquad
 \boldsymbol\mu_a=\kappa R_aW_a.
 \tag{E1}
\]
Mass has units kg and moment has units A m\(^2\). Thus \(\alpha\) and \(\kappa\) convert squared native amplitude to these units. They are undetermined. The scalar \(I_a\) is a simple symmetry-compatible choice, not a uniqueness theorem for mass.

Set
\[
 \rho(r)=\sum_a m_a\chi_\ell(r-X_a),\qquad
 M(r)=\sum_a\boldsymbol\mu_a\chi_\ell(r-X_a).
 \tag{E2}
\]
Here \(\rho\) is mass per volume and \(M\) is moment per volume, with SI units A/m. This smooth profile is a new spatial source representation; it is neither a filled central opening nor the accepted abstract channel measure.

**E1c — Field laws and boundary conditions.** Adopt
\[
\begin{split}
 \Delta\Phi&=4\pi G_N\rho,\qquad \Phi\to0\text{ at infinity},\\
 \nabla\cdot B&=0,\qquad
 \nabla\times(B/\mu_0-M)=0,\qquad B\to0\text{ at infinity}.
\end{split}\tag{E3}
\]
These are the Newtonian and no-free-current magnetostatic equations, imposed on all of \(\mathbb R^3\). They are additional physical laws. The role of the Poisson equation and its Newtonian limit is described in [Tong's gravity introduction](https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S0.html). The magnetization-current construction is standard [electromagnetism in matter, §7.2](https://www.damtp.cam.ac.uk/user/tong/em/el6.pdf).

**E1d — Response and motion.** Identify gravitational source mass, passive gravitational mass and inertial mass at this approximation. Adopt Newtonian mechanical response to the effective interaction potential. A freely rotating body additionally needs a positive inertia tensor; that tensor is not inferred from native phase rotation.

These premises do not follow from counting facets, the occurrence of geometric constants, internal gradient descent, axial parity, or a mass-shell identity.

### Solutions and consistency

The gravitational solution is
\[
 \Phi(r)=-G_N\int\frac{\rho(r')}{|r-r'|}\,d^3r'.
 \tag{E4}
\]
For a concentrated mass, the outward flux of \(\nabla(-G_Nm/r)\) through any centered sphere is \(4\pi G_Nm\); this fixes the source coefficient. Its force on another positive mass is attractive.

For the magnetic source define
\[
 J_b=\nabla\times M,\qquad
 A(r)=\frac{\mu_0}{4\pi}\int
 \frac{J_b(r')}{|r-r'|}\,d^3r',\qquad B=\nabla\times A .
 \tag{E5}
\]
Compact smooth support removes surface ambiguities. The identity
\(\nabla\cdot J_b=0\) supplies static current continuity. In Coulomb gauge,
\(-\Delta A=\mu_0J_b\) and \(\nabla\cdot A=0\), proving E3. Integration by parts also gives
\[
 \frac12\int r\times J_b\,d^3r=\int M\,d^3r
 =\sum_a\boldsymbol\mu_a.
 \tag{E6}
\]
In components, the integral on the left is
\(\frac12\int(r_j\partial_iM_j-r_j\partial_jM_i)\);
the two integrals are \(-\int M_i\) and \(-3\int M_i\), respectively. Thus the assigned vector is actually the dipole moment of the declared current distribution.

An equivalent Fourier expression, for nonzero wavevector \(k\), is
\[
 \widehat B(k)=\mu_0
 \left(I_3-\frac{kk^T}{|k|^2}\right)\widehat M(k).
 \tag{E7}
\]
The transverse projection enforces \(k\cdot\widehat B=0\) and
\(k\times(\widehat B/\mu_0-\widehat M)=0\).
The decay condition selects the real-space solution; no arbitrary uniform background is added. In general \(B\ne\mu_0M\).

For localized sources the leading far fields are
\[
 \Phi_b=-\frac{G_Nm_b}{r},\qquad
 B_b=\frac{\mu_0}{4\pi r^3}
 \left[3(\boldsymbol\mu_b\cdot\widehat r)\widehat r-\boldsymbol\mu_b\right].
 \tag{E8}
\]
The dipole expression is used away from its point idealization; it is not asserted as a complete distribution at \(r=0\). Smooth E2–E5, rather than a singular point formula, define the full spatial problem.

### Forces, torques and the work account

For two separated bodies in the point/far-field approximation, let \(r=X_a-X_b\). Their single-counted interaction is
\[
 U_{ab}=-\frac{G_Nm_am_b}{|r|}
 +\frac{\mu_0}{4\pi|r|^3}
 \left[\boldsymbol\mu_a\cdot\boldsymbol\mu_b
 -3(\boldsymbol\mu_a\cdot\widehat r)(\boldsymbol\mu_b\cdot\widehat r)\right].
 \tag{E9}
\]
With the source values fixed in the position derivative,
\[
 F_a^{\rm grav}=-\frac{G_Nm_am_b}{|r|^2}\widehat r,\qquad
 F_a^{\rm mag}=\nabla_{X_a}(\boldsymbol\mu_a\cdot B_b),\qquad
 \tau_a=\boldsymbol\mu_a\times B_b.
 \tag{E10}
\]
These are standard permanent-dipole forces and torques, not a force inferred from the native update. The dipole field, energy and force formulas can be compared with [Tong, magnetostatics, §§3.3–3.4](https://www.damtp.cam.ac.uk/user/tong/em/em2.pdf).

The static variational functionals make the signs checkable:
\[
\begin{split}
 {\cal E}_g[\Phi]&=\int
 \left(\frac{|\nabla\Phi|^2}{8\pi G_N}+\rho\Phi\right)d^3r,\\
 {\cal E}_m[A]&=\int
 \left(\frac{|\nabla\times A|^2}{2\mu_0}
 -M\cdot(\nabla\times A)\right)d^3r .
\end{split}\tag{E11}
\]
Their first variations are respectively
\(-\Delta\Phi/(4\pi G_N)+\rho\) and
\(\nabla\times(B/\mu_0-M)\). At the field solutions they reduce to
\(\frac12\int\rho\Phi\) and \(-\frac12\int M\cdot B\).
Removing rigid self terms gives E9 in the dipole approximation. The magnetic functional is an effective fixed-moment potential with source coupling; it is not a claim that the total field-plus-matter energy is negative.

For constant masses, frozen internal preparations and fixed orientations, the mechanical equations
\[
 \dot X_a=P_a/m_a,\qquad
 \dot P_a=-\nabla_{X_a}\sum_{a<b}U_{ab}
 \tag{E12}
\]
conserve \(\sum_a |P_a|^2/(2m_a)+\sum_{a<b}U_{ab}\) wherever the point approximation is used and no collision occurs. This follows by cancellation of the two chain-rule terms. Fixed orientation requires constraints if a torque is present. Alternatively, a chosen rigid-body inertia and the torque in E10 supply rotational dynamics and the corresponding rotational kinetic energy. Neither option identifies common native phase with bodily rotation.

## 5. Consequences specific to the proposed correspondence

These statements are falsifiable *conditional predictions of E1*, not claims about measured matter.

1. **A sharp moment–mass envelope.** Orthogonality of \(R\), E1 and D3 prove GM1. Its exact refinement is
   \[
   |\boldsymbol\mu|^2=\kappa^2
   \left[\frac38(I_\Omega^2-|\Omega\cdot\Omega|^2)-\frac12\Gamma^2\right].
   \tag{P1}
   \]
   An observed violation after independently calibrating the dictionary would reject this ansatz. It would not refute every possible native-to-physical correspondence.

2. **Conjugation reverses the candidate moment while preserving candidate mass.** For \(\Omega\mapsto\overline\Omega\), \(I_\Omega\) is unchanged and \(C,W,\Gamma\) reverse. At the same pose, the gravitational source is unchanged and the magnetic source reverses. Conjugating one of two interacting preparations reverses their dipole interaction; conjugating both leaves it unchanged. This is an algebraic preparation operation, not an identification with physical time reversal.

3. **Some chiral states are magnetically silent in this ansatz.** The pure \(f_1,f_2\) preparations have nonzero \(\Gamma\) but zero \(\boldsymbol\mu\). For E2 they contribute no magnetization field at that instant. Native evolution with unequal coefficients may change the observable later; “silent” is not an invariant-orbit claim.

4. **The linear candidate has a body-plane restriction.** Since the third row of \(T\) is zero, the moment is perpendicular to \(R e_z\). A reproducible component along that body normal would reject this restricted linear dictionary. Paper G already admits nonlinear axial covariants, so the restriction must not be generalized to all candidates.

The field equations in E3 are experimentally familiar input laws. The distinctive content available for testing here is the *source dictionary*, its bound, transformation properties and blind states. No native numerical trajectory or physical experiment has been manufactured to support it.

## 6. What remains before these are physical laws of the model

### Coupling the evolving native state

E1 freezes source preparation during the mechanical calculation. Running N1 and repeatedly overwriting \(m,\boldsymbol\mu\) does not automatically yield a closed physical system. Even at fixed positions and poses,
\[
 \Delta U_{\rm source}=
 U(X,m(F\Omega),\boldsymbol\mu(F\Omega))
 -U(X,m(\Omega),\boldsymbol\mu(\Omega))
 \tag{O1}
\]
is generally nonzero. For differentiable externally prescribed sources, the corresponding term is
\[
 \left.\frac{dU}{dt}\right|_{\rm source}
 =\sum_a\left(
 \frac{\partial U}{\partial m_a}\dot m_a+
 \frac{\partial U}{\partial\boldsymbol\mu_a}\cdot
 \dot{\boldsymbol\mu}_a\right).
 \tag{O2}
\]
Changing inertial masses also changes kinetic and possible rest-energy accounts. These terms require an internal energy, source work, reservoir or feedback law. Adding an arbitrary “balancing reservoir” can make a formal ledger but would not derive its physical mechanism.

There is a sharper obstruction to one tempting shortcut. Consider two identical preparations from D5, with centers and momenta held fixed during a native split step. Their moments are zero before and after that step. Let their initial candidate mass be \(m>0\), let
\(d=\alpha/(50\,000\,000)>0\), and allow *any* state-only internal energy, including any rescaling of \(V\) and any state-only self-energy. Denote its total change by \(K\), independent of body separation \(r\). In the separated point approximation the combined change is
\[
 \Delta E(r)=K-\frac{G_N[(m+d)^2-m^2]}{r},\qquad
 \frac{d}{dr}\Delta E(r)=\frac{G_N(2md+d^2)}{r^2}>0.
 \tag{O3}
\]
It cannot vanish for every separation. Thus a state-only energy correction cannot make this specific uncoupled split step closed and energy conserving. Position-dependent feedback, another work channel, or a different source/update dictionary is necessary. This is a conditional obstruction to that construction, not an exclusion of all couplings or emergent theories.

The accepted spatial-work/transport paper provides a useful discipline: added storage and feedback were explicitly defined and their cancellation proved. Its particular Hilbert-space ports are not automatically electromagnetic work or gravitational stress-energy. A new coupling must state its own variables and recheck any native results whose hypotheses it changes.

### Causality and relativistic gravity

E3 is static; applying instantaneous Poisson solves to rapidly changing sources is not a causal relativistic theory. Magnetism in time requires its electric partner, Faraday induction, displacement current, charge continuity and an energy-momentum account. These are explicit parts of [electrodynamics](https://www.damtp.cam.ac.uk/user/tong/em/em3.pdf), not consequences of axial parity.

For relativistic gravity, an actual Lorentzian metric and a conserved stress-energy source, together with a dynamical field law and matter motion, must be supplied or derived. The fixed panel metric is not that object. The standard comparator is [Einstein gravity with matter](https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S4.html); importing it would define a further extension, not solve its emergence from this model.

### Selection, calibration and evidence

The next substantive issue is source-and-backreaction selection, not another unstructured geometry scan. A physical completion would need:

- An operational meaning of the body, its position and orientation, and measurements of the proposed internal state.
- A justified mass/energy dictionary. If the SRG mass is to be used, an explicit link to the native state is needed; the two masses cannot silently be identified.
- A clock and spatial calibration, fixed couplings, and a regime in which a static or continuum approximation has a controlled error.
- A source-work or matter action consistent with the evolving state, together with conservation and causality checks.
- Predictions tested against observations after calibration, including tests capable of rejecting the dictionary.

This is not a decision to abandon the author's geometric research direction. The earlier fresh-eyes reconciliation explicitly withdrew “nothing propagates” and dimensional impossibility as blanket exclusions. Nor is E1 uniquely recommended for adoption: screened kernels and alternative scalar sources demonstrate how much physical selection remains. E1 is one fully stated candidate against which those choices can now be compared.

**Outcome:** exact native restrictions and a checked conditional static source–field–force construction are available. Gravity and magnetism as experimentally established, dynamically closed physical laws of the native model remain unresolved.

## 7. Verification and source navigation

[VERIFICATION_RESULTS.json](VERIFICATION_RESULTS.json) records 29 passing exact symbolic checks under Windows Command Prompt after conda activation of torment. They cover native identities and the intensity witness, the local-phase commutator, the localization counterexample, field projections, exterior dipole identities, force signs, torque, the sharp bound and the split-step energy obstruction. They are algebra checks, not 29 experiments or independent proofs of physical validity. Written assumptions and arguments above remain necessary.

An initial checker used the positive-exponent Fourier vector while labeling it with Paper G's negative-exponent convention. The check caught the sign mismatch; the fixture was corrected from the unchanged source. The initial failure log is preserved. No accepted source or result was changed to make the check pass.

[SOURCE_VERIFICATION.json](SOURCE_VERIFICATION.json) records ten byte-verified primary inputs and three historical navigation copies. [CLAIM_LEDGER.json](CLAIM_LEDGER.json) separates inheritance, deductions, added assumptions and open requirements. [REVIEW_RECEIPT.json](REVIEW_RECEIPT.json) records delivery checks. The accepted reference, production code and earlier research were not edited. No commit or push was made.

| Key | Exact source and premise |
|---|---|
| G | [Paper G v0.1.1](sources/pinned/papers/PAPER_G/v0.1.1/source/paper_g.tex): eq:SA, eq:T, prop:attach, eq:reconstruct, eq:gram, eq:hidden; distinguishes linear attachment from nonlinear covariants. |
| NPC setting | [Native potential, setting](sources/pinned/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/setting.tex): eq:pre, eq:full, eq:potential, eq:gradient and regular-domain qualification. |
| NPC finite | [Finite-domain descent](sources/pinned/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/finite.tex): eq:parameters, eq:domain, thm:finite; supplies the exact admitted tuple used in D5. |
| NRG | [Interpretation boundaries](sources/pinned/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/discussion.tex), sec:limits; [response chapter](sources/pinned/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/response.tex). The response-metric and physical-spacetime distinction is inherited. |
| WT | [Declared transport](sources/pinned/papers/SPATIAL_WORK_CAUSAL_TRANSPORT/publication/v0.1/sections/05_transport.tex): eq:transportPDE, eq:closedmodel, eq:componentpowers; [physical correspondence limits](sources/pinned/papers/SPATIAL_WORK_CAUSAL_TRANSPORT/publication/v0.1/sections/09_discussion.tex). |
| SRG | [Multiplication and mass shell](sources/pinned/SRG_REDISCOVERY/PAPERS/SRG_MULTIPLICATION_MASS_SHELL/publication/v0.1/manuscript/SRG_MULTIPLICATION_MASS_SHELL_v0.1.tex): eq:dictionary and accompanying physical qualifications. |
| Author history | [Geometric origins retrospective](sources/pinned/papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/history.tex): preserves the intended questions without identifying recollection with a field equation. |
| Reconciliation | [Historical reconciliation, §2](sources/local_history/FRESH_EYES_RECONCILIATION_NOTE_v0.1.md): narrows response-operator conclusions and withdraws blanket propagation/dimension exclusions. Its older open items are not presumed current. |

The external lecture references supply standard comparison laws only. No claim of priority is made for Newtonian gravity, magnetostatics, dipole interactions, transverse projection or the associated variational calculations.
