# SRG Final Mathematical Bridge

## From lens geometry to recurrence and known equations

**Publication edition v0.1 - accepted scientific and editorial synthesis**  
Prepared for Hilmir Frímann Halldórsson · 27 October 2026 · Publication edition v0.1

This manuscript explains the mathematical bridges recovered in the accepted FB01 investigation. It follows the research from geometric constructions into explicitly defined states and operators, then into established spectral and dynamical equations. Its purpose is to make the working mathematics understandable while showing where the model supplies an additional choice.

Two routes organize the explanation. The first starts with an overlapping-circle lens, prepares a complex state, transfers it through the fixed SRG operator, and uses the result to initialize a separate nonlinear recurrence. The second starts with a periodic spatial operator, takes an inverse spectral trace, and relates it to a standard quantum ring and the historical coupling formula. Both routes contain exact results. Their inputs and assumptions differ, and no recovered equation makes them one parameter-selection mechanism.

<!-- diagram:two_routes -->

The historical programme associated circle geometry, growth, packing and discrete sums with π, e, φ and ζ(3). That explanation survives in the fusion manuscript's Appendix A. Some further reasons for individual choices remain undocumented. Missing reasons are unknown reasons; they do not invalidate a well-defined equation. At the same time, an intended association does not by itself select a unique physical law. Keeping those distinctions allows us to preserve the exploration and explain its actual mathematical content. [P01, pp.19–20; ORIGINS1, §6.1a]

## 1. What the lens determines

Place two disks of equal radius R at centers (−d/2,0) and (d/2,0), with R>0 and 0≤d≤2R. Their intersection is the lens. The principal half-angle θ measures half of the arc cut out on either parent circle. A right triangle from a center to an intersection point gives

<!-- equation:G1 -->
$$
\theta=\arccos\!\left(\frac{d}{2R}\right),\qquad 0\leq\theta\leq\frac{\pi}{2}.
$$

Two circular sectors, less their two triangles, give the area. Dividing by the area of one parent disk removes the arbitrary overall size:

<!-- equation:G2 -->
$$
A_{\mathrm{lens}}=R^2(2\theta-\sin2\theta),\qquad I(\theta)=\frac{A_{\mathrm{lens}}}{\pi R^2}=\frac{2\theta-\sin2\theta}{\pi}.
$$

The lens therefore supplies a dimensionless fraction between zero and one. At tangency, d=2R and I=0. At coincident centers, d=0 and I=1. The overlap arcs have total length 4Rθ, whereas the width along the center line is 2R−d. Area, arc length, width and chord are different observables; choosing one as a response variable is a further step. [IVA, §A1; BOUNDARY, §§2–3]

In the classical vesica, d=R. The centers are then at ±R/2, and the centers together with either intersection point form an equilateral triangle of side R. Thus θ=π/3 and the normalized area is 2/3−√3/(2π). The appearance of √3 has a specific geometric source. For an equilateral triangle with side a and inradius r_in,

<!-- equation:G3 -->
$$
r_{\mathrm{in}}=\frac{\sqrt3}{6}a,\qquad \left(\frac{r_{\mathrm{in}}}{a}\right)^2=\frac1{12}.
$$

The denominator matters: the squared ratio to the triangle's circumradius is 1/4 instead. The positive 1/12 is an ordinary geometric ratio, not a regularized spectral remainder. [ORIGINS1, §3.1]

The older sources use more than one convention. *Vesica Delay* explicitly chooses R=1/2. Its half-angle θ=π/4 gives overlap arc length π/2 and separation d=√2R, rather than the classical d=R vesica. VPQW uses a full intersection angle, twice the half-angle used here. It also states circumference C=π on p.2 but prints r=1/(2π) in Eq.(4) on p.3. Since C=2πr, those two printed normalizations conflict: retaining C=π would give r=1/2; retaining the printed radius would give C=1. We preserve the distinction without deciding silently which statement the author intended. [VESICA, p.1; VPQW, pp.2–3; GPT_REVIEW, §5]

### Constants from specified constructions

The circle and equilateral triangle explain π and √3 in this route. There are independent supported constructions for φ and e. A regular pentagon's diagonal-to-side ratio, using Ptolemy's relation, satisfies φ²=φ+1 and selects the positive root (1+√5)/2. A Fibonacci recurrence supplies a second route: its explicit solution yields the limiting ratio φ. Neither construction is already contained in the equal-circle area formula merely because φ later appears in a parameter. [ORIGINS1, §3.2]

The exponential base e enters through growth, decay and continuous compounding. A chosen law ẋ=ax has solution x(t)=e^(at)x(0); it explains why exponential functions recur throughout the source equations. The coefficient a and its time units remain inputs to that law. In particular, the use of e as an exponential base does not independently select a factor 1/e in a later coupling. [ORIGINS1, §3.3]

There are also exact classical links between the golden split, π and Apéry's constant ζ(3). Set q=φ⁻¹ and ℓ=logφ, so q+q²=1. The accepted Origins account reproduces the classical trilogarithm relation and its finite-interval consequences:

<!-- equation:G4 -->
$$
\operatorname{Li}_3(q^2)=\frac45\zeta(3)-\frac{2\pi^2}{15}\ell+\frac23\ell^3.
$$

<!-- equation:G5 -->
$$
\int_0^\ell t^2\coth t\,dt=\frac{\zeta(3)}{10},\qquad \int_0^\ell t\coth t\,dt=\frac{\pi^2}{20}.
$$

These identities are inherited classical mathematics, not new SRG discoveries. Origins §4.4 supplies the derivation and references; GPT's FB01 review checked the comparison against the DLMF and Markov's treatment of the Hjortnaes integrals. They show that the constants are connected by exact relations, while leaving the historical product πeφ a separately specified expression.

Another useful construction starts from x/(1−x)=Σₙ≥1xⁿ on 0≤x<1. Applying the integration operator f↦∫₀ˣf(t)/t dt three times divides each coefficient by n³. The result is Li₃(x), tending to ζ(3) as x approaches one. At a different endpoint a, the result is Li₃(a). A change of variable x=au must also transform the measure: dx/(1−x)=a du/(1−au). Omitting that numerator changes the integral. The exact integration result survives without assuming that every geometric rescaling leaves it unchanged. [ORIGINS1, §§4.1–4.4]

## 2. Turning the area into an initial state

Geometry has supplied I(θ), a real scalar. To use it in the six-state recurrence, the boundary closure adds an incident amplitude ξ in ℂ² and a response rule. The incident amplitude carries magnitude and two complex coordinates; it is not determined by the lens, automatically normalized, or identified as a physical spin state by its notation.

The four assumptions below are reproduced from the boundary note. They were proposed as a minimal mathematical response and subsequently adopted in its §11 under the name `lens_area_norm_v1`.

> **A1 — Uniform area budget for squared norm.** With xi held fixed, the squared output norm is the incident squared norm times the fraction of one parent disk occupied by the lens. This is a modelled geometric norm budget; it is not an electromagnetic-energy derivation or Born-rule claim. The chosen reference area is pi R_L^2.

> **A2 — Equal coherent channel response.** All three existing channels receive the same complex amplitude in the already declared channel convention. This is stronger than equal intensities. It is an explicit coupling assumption, not a claim that two-circle geometry has a threefold spatial symmetry.

> **A3 — No helicity mixing or boundary phase imprint.** The boundary multiplies both incident helicity coordinates by the same scalar and adds no common or relative phase. All relative channel phases subsequently generated by SRG come from its existing phase operator. The boundary gain is selected nonnegative in this reference convention.

> **A4 — Raw zero is permitted.** At tangency or zero incident field the prepared vector is zero. No epsilon, arbitrary normalized ray, or hidden random seed is substituted. The accepted raw handoff is defined at zero; normalized displays are not.

[BOUNDARY, §2, A1–A4; later adoption in §11]

Let f₀=(1,1,1)ᵀ/√3. Equal coherent channels and the absence of mixing or boundary phase make the output a(θ)(ξ⊗f₀), with nonnegative gain a. Since f₀ has unit norm, A1 says a²=I. The response is therefore

<!-- equation:P1 -->
$$
\mathcal P(\theta,\xi)=\sqrt{I(\theta)}\,(\xi\otimes f_0),\qquad f_0=\frac1{\sqrt3}(1,1,1)^T.
$$

This short derivation establishes uniqueness within A1–A4. It also explains exactly where the square root enters: the area budget was assigned to squared norm. If amplitude itself were additive in area, a different rule would result. That possibility does not weaken the adopted model; it clarifies which response was chosen.

At tangency or ξ=0, P1 gives a valid raw zero vector. No normalized ray exists at that point. For a nonzero input, the overall scale remains meaningful because the later nonlinear recurrence contains a cubic amplitude term. Removing that scale would change the initial condition supplied to it. The mathematical preparation is complete; a physical incident-field or detector model would need to justify its response assumptions separately. [BOUNDARY, §§3,11; BCODE, `prepare_area_response`]

## 3. The fixed SRG transfer and what it preserves

The November source orders its six coordinates as (0+,1+,2+,0−,1−,2−). In this convention the state space is ℂ²⊗ℂ³: the first factor labels the two helicity coordinates and the second the three channels. Its evolution has four ordered factors:

<!-- equation:F1 -->
$$
U=U_{\mathrm{REFU}}\,U_{\mathrm{TGMO}}\,U_{\mathrm{flip}}\,U_{\mathrm{RPCO}}.
$$

The rightmost operator acts first. RPCO partially projects onto the balanced channel core. The flip mixes the two helicity coordinates. TGMO supplies channel and helicity phase. REFU finally applies core gain and complementary loss. Here those names denote matrices, not the grid stencil or scalar compressors encountered later. [FIXED, pp.4–6; IVA, §A6]

Write p=f₀f₀†, Π_core=I₂⊗p, q=e^(−η), r=e^γ and c=1−λ_c. The factors are `U_RPCO=(1−λ_c)I₆+λ_cΠ_core`, `U_REFU=exp(γΠ_core−η(I₆−Π_core))`, `U_flip=exp(−iβσ_x)⊗I₃`, and `U_TGMO=exp(−iασ_z)⊗Z`. With ω=e^(2πi/3), the useful reduced definitions are

<!-- equation:F2 -->
$$
R=qI_3+(r-q)p,\quad C=cI_3+(1-c)p,\quad Z=\operatorname{diag}(1,\omega^{-1},\omega^{-2}).
$$

<!-- equation:F3 -->
$$
A=RZC,\qquad B=e^{-i\alpha\sigma_z}e^{-i\beta\sigma_x},\qquad U=B\otimes A.
$$

The literal source values are λ_c=.618, γ=.577, η=.423, α=2π·.244 and β=π·.244. They are retained exactly as assigned decimals. The first is close to φ−1 but not equal to it. The gain exponent .577 is distinct from Euler–Mascheroni's constant γ_EM=.5772156649…, from Euler's number e, and from the later coupling γ*≈.0869947. Their different call sites, rather than a shared letter, determine their roles. [SRGCODE, lines21–25,57–72; ORIGINS1, §6]

### A weighted three-cycle

Define f_j=Zʲf₀ for j=0,1,2. These are an orthonormal Fourier basis for the channel space. The full channel operator moves through them with different gains:

<!-- equation:F4 -->
$$
Af_0=qf_1,\qquad Af_1=qcf_2,\qquad Af_2=rcf_0,\qquad A^3=DI_3,\quad D=rq^2c^2.
$$

This makes the transfer transparent. One step changes both the channel phase pattern and its scale. Three steps return to the original Fourier direction with common multiplier D. Although REFU alone amplifies the balanced core, the product A does not preserve that line: it sends f₀ to qf₁. The shared graph identity L₃=−3(I₃−p) is an exact algebraic link to the later triad, not a claim that the entire product acts like L₃. [IVA, §A6; TARGET, §8]

Because B is unitary, choose a normalized eigenvector χ with Bχ=λ_χχ. Normality gives χ†B=λ_χχ†. The extraction map Φ_χ=χ†⊗I₃ then obeys

<!-- equation:F5 -->
$$
\Phi_\chi U=(\lambda_\chi A)\Phi_\chi,\qquad T_\chi v=\chi\otimes v,\qquad \Phi_\chi T_\chi=I_3.
$$

Moreover UT_χ=T_χ(λ_χA). Thus extraction really preserves the reduced linear evolution v⁺=λ_χAv, and T_χ is its explicit injection. This is stronger than a resemblance between formulas. It is an exact relation between two state spaces at the same integer transfer step. [TARGET, §§2,8.2]

Combining the preparation with n≥0 transfer steps gives the closed result

<!-- equation:F6 -->
$$
\Omega_{\mathrm{initial}}=\Phi_\chi U^n\mathcal P=\sqrt I\,(\chi^\dagger\xi)\lambda_\chi^n b_n f_{n\bmod3}.
$$

<!-- equation:F7 -->
$$
b_{3m}=D^m,\qquad b_{3m+1}=D^m q,\qquad b_{3m+2}=D^m q^2c.
$$

Its squared norm is I times |χ†ξ|² times |b_n|². Aperture information is carried by this raw magnitude. Recovering I requires the known count n and known nonzero incident overlap. At χ†ξ=0 the output is zero even for an open lens. Normalizing a nonzero output removes the aperture factor. [BOUNDARY, §§3–4; TARGET, §8.4]

The full extraction Φ_χ is onto ℂ³, as its right inverse shows. The map Φ_χUⁿ from an unrestricted six-state input is also onto at the frozen invertible A. The lens-prepared family is much smaller: at a fixed n it occupies one complex Fourier line. These statements answer different questions and are compatible. The branch selects a B eigenvalue; the implemented gauge fixes an eigenvector phase convention. ξ, branch/gauge and n are explicit preparation data, and n is not automatically the clock of the subsequent nonlinear model.

The same phase cycle also explains a channel orientation readout. For Z_chiral=ReΩ×ImΩ, the unit Fourier directions f₀,f₁,f₂ give 0, −f₀/2, +f₀/2, respectively; a complex scalar multiplies this readout by its squared modulus. A complex-linear transfer can therefore produce nonzero channel chirality from the initially real balanced direction. The meaning here is channel-state orientation. [BOUNDARY, §4, C4; TARGET, §8.4]

### The next recurrence is a separate dynamical choice

The extracted Ω_initial can initialize the nonlinear triad described below. Target B also proves a precise limit: for the fixed U, there is no global complex-linear surjection Φ:ℂ⁶→ℂ³ satisfying ΦU=F_TOΦ on all raw states at the same step. When the cubic coefficient is nonzero, scaling is incompatible with an induced linear target. When it is zero, the downstream map fixes the balanced direction while powers of the frozen U decay. Neither argument denies P1, F5 or F6. They exclude that stronger full-evolution identification in its stated map class. [TARGET, §3.3 and §8.3]

At the frozen parameters, U has singular values below one and raw states contract toward zero. A useful conditional quantum comparison is nevertheless available: on density matrices, ρ↦UρU† is completely positive and trace-nonincreasing. Dividing by the resulting positive trace gives a conditional state. Identifying this as a physical measurement would add an outcome model and complementary operations. It is not a closed-system unitary evolution, and normalization changes the raw dynamical description. [IVA, §§A7,B4]

## 4. Following the changing operator definitions

The recurrence is identified by its carried state, formula and update order. The acronyms alone do not supply those details. The following compact comparison explains the principal transitions without reopening the completed simulation reconstruction. [LINEAGE, §§7–8; SRGI, §§2–5]

| Source family | State and actual operation | Meaning of the operator names |
|---|---|---|
| Early trajectory sources | Positions/velocities; scheduled H, regularized fields, componentwise damping and coordinate wrapping | Architectural grouping, with source-specific full steps |
| July 2025 sources | Separate sampled curves/fields; a position recurrence; also a distinct implicit temporal relation | A plotted TGMO minor circle is not a field Laplacian; a plotted RPCO phase field is not a compressor |
| November fixed SRG | Raw ℂ²⊗ℂ³ state; the four matrices in F1 | Exact ordered factorization, including the flip |
| January 2026 grid | Real array on periodic indices; spatial stencil, nonlinear injection, scheduled gain and scalar clipping | REFU is the composite that contains TGMO and RPCO |
| March particle adaptations | Cartesian positions and real resonance fields, rebuilt neighbors, gains, fusion and compression | Documented adaptations with extra stages and changed carriers |
| Modern nonlinear triad | Three raw complex amplitudes; cubic/graph increment followed by simultaneous phase synchronization | A specified two-stage map, with optional initialization and coordinate adapters |

Early `recursive_attractor.py`, for example, damps each velocity component by dividing it by 1+log(1+its absolute value); it also wraps coordinates into [−1,1). Other early sources retain regularized vortex denominators or a norm limiter with an added 10⁻⁵. Their mathematical behavior changes if those details are replaced by an ideal vortex or exact radial projection. [IVA, §A4]

A distinct July trail equation uses the temporal difference Θ(t+1)−2Θ(t)+Θ(t−1). Substitution into its printed update yields an implicit scalar relation y=C_λ(y+b), with b containing earlier state and frozen feedback. Its threshold map is identity below λ and division by φ at or above λ. The accepted SRG-I branch classification includes empty and nonunique solution sets. It is therefore not an everywhere-defined single-valued next-state law without further rules. Selecting a separate explicit July formula, or replacing the temporal difference by a spatial one, would be a new interpretation. [SRGI, §§2–3]

January supplies a definite spatial array operator instead. On its two periodic index axes,

<!-- equation:J1 -->
$$
(\mathcal L\Theta)_{ij}=a^{-2}(\Theta_{i+1,j}+\Theta_{i-1,j}-2\Theta_{ij})+b^{-2}(\Theta_{i,j+1}+\Theta_{i,j-1}-2\Theta_{ij}).
$$

The optional third axis has a separate second difference, reflecting by default. This is a constant-coefficient periodic-index stencil. Its flat product reference expression differs from the Laplace–Beltrami operator induced on an embedded torus of revolution, whose metric introduces position-dependent coefficients. A separate torus-embedding drawing does not change the stencil. VPQW and January share a reference expression, but the surviving cover dates do not establish the direction of copying or derive that operator from lens area. [JTGMO, lines4–46,62–76; IVA, §A1]

For the app callbacks D(Θ,t)=Θ and f(D)=κtanh(D/s), January's full REFU update is

<!-- equation:J2 -->
$$
\Theta^+=C_{\mathrm{mode}}\!\left[\left(1+\lambda\frac{H(t)}{H_{\max}}\right)\left(\Theta+dt\,\mathcal L\Theta+\kappa\tanh(\Theta/s)\right)\right].
$$

Both increments read incoming Θ; only the spatial term has the dt factor. The scheduled multiplier acts before the final compressor. Calling TGMO, RPCO and REFU three successive peers would obscure this actual order. [JREFU, lines109–138; APP, lines234–238]

The paper and signed compressors differ by the placement of the sign:

<!-- equation:J3 -->
$$
C_p(x)=\exp\!\left(\operatorname{clip}\!\left(\operatorname{sgn}(x)\log(|x|+\epsilon),-L,L\right)\right).
$$

<!-- equation:J4 -->
$$
C_s(x)=\operatorname{sgn}(x)\exp\!\left(\operatorname{clip}\!\left(\log(|x|+\epsilon),-L,L\right)\right).
$$

For a>0 on inactive clipping branches, paper mode sends −a to 1/(a+ε), while signed mode sends it to −(a+ε). At zero they return 1 and 0, respectively. The app initially selects paper mode, with L=10 and ε=10⁻⁶; generic library defaults are L=9 and ε=10⁻⁹. These are different maps with different zero behavior, not alternative spellings of the same operator. [JREFU, lines37–69; APP, lines54–57]

The shared default schedule is

<!-- equation:J5 -->
$$
H(t)=2e^{-t/2}\cos t+e^{-3t/10}\sin t+\frac32e^{-7t/10}+e^{-2t/5}.
$$

It reads time, not the evolving field's history. January uses t=n·dt starting at zero and a sampled Hmax normalization. The array still recurs because its updated value becomes the next input. Other documented models have genuine carried memory, including an exponentially weighted memory variable or a field-driven memory ODE; those should not be conflated with this schedule. [IVA, §A5; SRGI, §7]

March Seed Explorer explicitly describes an adaptation from January's refu.py and tgmo.py to particles. Subsequent stages include neighbor mixing, H gain, resonance-weighted position fusion, prescribed sinusoids and signed compression. Infinity carries two real amplitude fields and actively uses the assigned .08699 in cross-coupling. Seed Explorer stores .0870 unused, while Tower II's zeta-based `gamma_predicted` is a post-run diagnostic rather than a feedback term. The completed source reconstruction established those distinctions; rerunning its simulations would not turn an assigned parameter into an independent measurement. [LINEAGE, §8; INFINITY, lines114–195; ORIGINS1, §6.3]

## 5. The nonlinear triad and familiar dynamical structures

The modern deterministic map accepts Ω∈ℂ³ with finite real ε, g, phase strength λ and three coefficients k_i. First it computes

<!-- equation:N1 -->
$$
v_i=\Omega_i+\varepsilon\Omega_i(k_i-|\Omega_i|^2)+g(L_3\Omega)_i,\qquad L_3=-3(I_3-p).
$$

Then, using the phases of v simultaneously, it applies

<!-- equation:N2 -->
$$
F_{\mathrm{TO}}(\Omega)_i=|v_i|\exp\!\left[i\left(\arg_0v_i+\lambda\sum_{j\ne i}\sin3(\arg_0v_j-\arg_0v_i)\right)\right].
$$

Here Arg₀(0)=0 and a zero component stays zero. At λ=0 the code directly returns v. There is no lens, noise, extra memory, normalization or physical clock inside this step. The k_i are amplitude coefficients, not automatically spatial wave numbers. [DYNAMICS, lines57–104]

The adopted lens/transfer initializer can supply Ω to this map. For the bounded profile ε=1/20, g=1/5 and k_i∈[0,8], the component domain max_i|Ω_i|≤3 is invariant in exact arithmetic: the pre-sync bound is 6/5+4√15/9<3 and synchronization preserves component moduli. The sharp uniform sufficient incident budget is ||ξ||≤3√3 over all openings, branches and transfer counts, although larger individual inputs may still prepare an admissible state. This is a domain theorem, not convergence or unlimited floating-point safety. [BOUNDARY, §§5,11; REGION]

### The same state in face coordinates

Use the existing three vertical faces in their fixed order and orientation. Their unit normals n_i satisfy n_i·e_z=0, where e_z=(0,0,1). Set t_i=e_z×n_i; then (t_i,e_z) is an orthonormal tangent frame on each face. The existing optional representation is

<!-- equation:N3 -->
$$
D(\Omega)_i=\Re\Omega_i\,t_i+\Im\Omega_i\,e_z,\qquad E(v)_i=v_i\!\cdot t_i+i\,v_i\!\cdot e_z.
$$

On the selected tangent-state space these are inverse real isometries, and D∘F_TO∘E is the same recurrence in those coordinates. On arbitrary ambient vectors, DE is only the tangent projector. The implementation stores the canonical Ω and derives vectors, avoiding an automatic rounding round trip. This gives a concrete geometric meaning to the two real components of each complex channel. It does not define a field over whole faces or impose seam boundary conditions. [PHASE1, §§3–7; KSM, §10.3.3.2; FACE]

### A gradient increment and a controlled continuous parent

Write z for the complex state viewed as six real coordinates. The increment in N1 is the negative real gradient of

<!-- equation:N4 -->
$$
V(z)=\varepsilon\sum_i\left(\frac{|z_i|^4}{4}-\frac{k_i|z_i|^2}{2}\right)+\frac g2\sum_{i<j}|z_i-z_j|^2.
$$

The local quartic term controls amplitude, and the graph term couples differences between channels. Thus the increment has a familiar gradient-flow structure. A finite unit Euler step need not decrease V, so the identity concerns the increment rather than an unconditional discrete energy law. [PHASE1, §7; PHASE2_REVIEW, §3]

Let A(z)=−∇_RV and, away from zero components, define the phase vector field B_i(z)=iλz_iΣ_{j≠i}sin3(φ_j−φ_i), with φ_i=arg z_i. The explicit approximation family scales both stages by h:

<!-- equation:N5 -->
$$
A_h(z)=z+hA(z),\qquad S_h(z)_i=z_i\exp\!\left(ih\lambda\sum_{j\ne i}\sin3(\phi_j-\phi_i)\right),\qquad F_h=S_h\circ A_h.
$$

The accepted proof gives local defect O(h²) relative to ż=A+B, and global error O(h) on a fixed time interval while the compared trajectories remain in a compact smooth region bounded away from zero components. This is an Euler-type approximation, not an exact composition of subflows and not an automatic accuracy statement at h=1. Linking t=nh to physical seconds is another input. The native map also contains no independently selected free rotation −iνz. [PHASE2_REVIEW, §3, lines109–151]

### Hamiltonian phase and the cubic oscillator case

In the fixed encoding z=q+ip, use the symplectic form dq∧dp and convention i_Xω=dH. The chosen isotropic Hamiltonian H=ν(q²+p²)/2 gives q̇=νp, ṗ=−νq and hence ż=−iνz. The sign follows from the stated convention. Isotropy matters: positivity alone does not make an arbitrary quadratic generate uniform rotation in that encoding. [PHASE2_REVIEW, §1]

Away from z=0, write z=√(2I)e^(iφ), I>0. Then dq∧dp=dI∧dφ, so

<!-- equation:N6 -->
$$
\dot I=\partial_\phi H,\qquad \dot\phi=-\partial_I H,\qquad H(I)=-\int^I\varpi(s)\,ds.
$$

A supplied local clock varpi(I) is thereby realized as φ̇=varpi(I). For a multi-action rate law, the mixed-derivative integrability conditions and, globally, exactness must also hold. The construction explains how a chosen clock becomes Hamiltonian; it does not select that clock or identify the action scale with ℏ. [PHASE3_ACCEPT, §1, lines9–36]

For the accepted continuous parent, identical channel coefficients, no additional third-harmonic term (K=0), and affine clock varpi(I)=ω₀+αI give exactly

<!-- equation:N7 -->
$$
\dot z_i=(\varepsilon k+i\omega_0)z_i-(\varepsilon-i\alpha/2)|z_i|^2z_i+g(L_3z)_i.
$$

Under these restrictions, this is the coupled nonisochronous Stuart–Landau / discrete cubic complex Ginzburg–Landau form with real diffusive coupling. This is a coupled nonisochronous cubic oscillator network: the oscillation rate depends on amplitude. The factor α/2 follows from I=|z|²/2. The full K≠0 parent has an additional phase term and is not exactly this cubic network. Neither case silently replaces the discrete kernel; it is a conditional established-equation comparison with a declared continuous clock. [PHASE3_ACCEPT, §7, lines207–218; PHASE3_REVIEW, §9]

## 6. A second route: periodic spectra and the quantum ring

The spectral route begins with a different object: a positive Laplacian on a periodic loop. It does not require a lens-prepared amplitude. Let the circumference be L>0, use N sites with spacing h=L/N, and let Δ_N be the periodic second difference. Define A_N=−h⁻²Δ_N. The quadrature inner product is hΣ_j ū_jv_j. Fourier modes diagonalize A_N, with

<!-- equation:S1 -->
$$
\lambda_{N,k}(L)=4(N/L)^2\sin^2(\pi k/N),\qquad k=0,\ldots,N-1.
$$

There is one zero mode. The finite modes k and N−k have the same eigenvalue; when N is even, k=N/2 is a single Nyquist mode. The positive inverse trace excludes the zero mode and retains every nonzero multiplicity:

<!-- equation:S2 -->
$$
Z_N(p;L)=\sum_{k=1}^{N-1}\lambda_{N,k}(L)^{-p}\ \longrightarrow\ 2\left(\frac{L}{2\pi}\right)^{2p}\zeta(2p),\qquad p>\frac12.
$$

The paired low-frequency ends of the finite spectrum approach the continuum modes ±k; the condition p>1/2 makes the inverse-power tail summable. The accepted proof controls the tail as well as individual modes. Keeping only a repeated three-channel sector would be a different observable. Refining N is spatial refinement, not recurrence time. [RING, §§2–3; ORIGINS1, §5]

### What the quantum comparison adds

Adopt a free, spinless, zero-flux ring Hamiltonian with m>0 and ℏ>0:

<!-- equation:S3 -->
$$
H_N=\frac{\hbar^2}{2m}A_N,\qquad H=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}.
$$

The continuum operator acts on L²([0,L]); its self-adjoint domain consists of H² functions satisfying both ψ(0)=ψ(L) and ψ′(0)=ψ′(L). A value boundary condition alone is not the full second-derivative domain. The normalized Fourier functions L⁻¹/²exp(2πikx/L), k∈ℤ, give

<!-- equation:S4 -->
$$
E_k=\frac{\hbar^2}{2m}\left(\frac{2\pi k}{L}\right)^2,\qquad E_{N,k}=\frac{\hbar^2}{2m}\lambda_{N,k}(L).
$$

The ground mode has zero energy, and each nonzero continuum energy has the two directions ±k. Finite sine dispersion is not identical to the continuum parabola; the correspondence is exact for the stated finite dictionary and controlled in the limit. The inverse-energy trace inherits S2, multiplied by (2m/ℏ²)^p. It is a spectral property, not a prepared wavefunction's detection probability. [RING, §4]

Adopting the conventional time law U_N(t)=exp(−itH_N/ℏ) gives unitary evolution. The paper proves more than a static spectral analogy. Fix a band B_K spanned by continuum Fourier modes |k|≤K. For N>2K, sampling defines an isometry J_N,K into the lattice space. Its time-evolution comparison obeys

<!-- equation:S5 -->
$$
\|U_N(t)J_{N,K}\psi-J_{N,K}U(t)\psi\|_h\leq\frac{2\hbar\pi^4K^4|t|}{3mL^2N^2}\|\psi\|_{L^2}.
$$

The bound holds for a fixed frequency band and a bounded time interval. It does not assert uniform convergence of moving Nyquist modes. The comparison's length, mass, ℏ and Schrödinger time law have been supplied explicitly; the result does not identify the historical nonlinear SRG recurrence with this unitary evolution. [RING, §4.3, finite-band proposition, lines578–614]

### Why ζ(3) appears, and what the calibration does

Choosing p=3/2 makes the inverse spectral sum an inverse-cube frequency sum. Equation S2 becomes

<!-- equation:S6 -->
$$
\lim_{N\to\infty}\frac{Z_N(3/2;L)}{L^3}=\frac{\zeta(3)}{4\pi^3}.
$$

For unit dimensionless circumference the division by L³ is invisible. For dimensionful L it is essential: the Laplacian eigenvalues have units length⁻², so this trace has units length³. The historical relation is recovered by the declared calibration

<!-- equation:S7 -->
$$
\gamma_* =\frac{4\pi^2}{e\varphi}\lim_{N\to\infty}\frac{Z_N(3/2;L)}{L^3}=\frac{\zeta(3)}{\pi e\varphi}.
$$

The equality is exact, and the prefactor is chosen to match the earlier formula. The July source predates the October spectral construction; the latter is a mathematical reconstruction, not the original cause of the printed relation. Origins and the ring paper explicitly preserve this distinction. [ORIGINS1, §§5–6; RING, §5]

One can express the same calibration using the positive inverse-energy trace ζ_H(3/2). Multiplying that trace by (ℏ²/(2m))^(3/2) undoes the adopted kinetic scale. The remaining expression is again S7. Every m>0 satisfies it with its corresponding free-ring Hamiltonian, so the calibration does not select a particle mass.

The historical rationale is more informative than an unexplained list of famous constants. P01 associates π with geometry, e with growth, φ with packing or growth patterns, ζ(3) with discrete sums, and γ with the scale joining them. It describes a calibration near .087 and leaves a deeper derivation open. P06, meanwhile, prints the lock equation but identifies its γ with Euler–Mascheroni's constant in its glossary. That conflict is retained as a source discrepancy. The unambiguous γ* in S7 is the solved coupling, not γ_EM or the fixed gain .577. [P01, pp.19–20; P06, pp.4,6; ORIGINS1, §6]

Other nearby identities ask different questions. The positive equilateral ratio 1/12 does not conflict with a negative finite remainder obtained after a specified spectral bulk subtraction. Nor does a spatial half-turn turn an unsigned positive length ratio negative. The later author-approved Origins discussion makes a conditional two-profile torus sweep precise, while leaving its map to the original overlapping lens and analytic reflection undefined. Those exploratory ideas can remain visible without becoming prerequisites for the two routes explained here. [ORIGINS1, §5.5; ORIGINS_STATUS]

## 7. What the bridge now explains

The lens route is constructive. Geometry supplies an area fraction. The adopted response assumptions supply a unique amplitude map. The four-factor SRG operator supplies an exactly solvable transfer and an evolution-preserving reduction to λ_χA. The extracted raw state then initializes a separately specified nonlinear recurrence. Its tangent coordinates, gradient increment, controlled continuous parent and conditional Hamiltonian specializations explain several familiar structures without erasing their assumptions.

The spectral route is equally precise. A declared periodic operator and circumference supply a complete finite spectrum and a continuum inverse trace. A conventional kinetic scale and time law give the accepted quantum-ring comparison, including a finite-band dynamical bound. Choosing the inverse power 3/2 and multiplying by the stated calibration reproduces the historical coupling identity.

The remaining independent-selection question is narrow: **what native observable or principle, specified independently of the desired coupling, selects p=3/2 and the normalization 4π²/(eφ), or an equivalent independently normalized relation?** No such law was recovered in the bounded source chain. This is neither an impossibility theorem nor evidence that an undocumented historical choice had no reason. It is also not a barrier to completing this explanation: the exact identities, adopted model and recovered historical rationale already have clear mathematical content.

There is no recovered arrow identifying the lens response, the fixed gain exponent .577 and the spectral coupling .086994… as one selection mechanism. Keeping them distinct makes the established connections checkable. This publication closes with those connections and their precise boundary; it does not begin a new selector investigation or change any completed model.

<!-- appendix:equation_sources -->

## Appendix A. Equation and source guide

The main text states assumptions next to their consequences. This guide gives the short route back to the accepted evidence. “Exact” describes a mathematical result under its stated definitions; it does not independently validate a physical identification. Code references identify equations and call order only: no source module was imported or executed for FB02.

| Equations | Subject and exact locator | Status and scope |
|---|---|---|
| G1, G2 | Equal-disk geometry and parent-area fraction. IVA §A1; BOUNDARY §§2–3. | Exact geometry; response observable is a choice. |
| G3 | Equilateral inradius ratio. ORIGINS1 §3.1. | Exact for the specified denominator. |
| G4, G5 | Golden split, trilogarithm and coth integrals. ORIGINS1 §4.4; classical references below. | Classical identities; not an SRG discovery or selector. |
| P1 | Area-to-amplitude preparation. BOUNDARY §2 A1–A4, §3 C1, §11; BCODE prepare_area_response. | Unique under the adopted assumptions; raw zero allowed. |
| F1, F2, F3, F4 | Four factors and weighted Fourier cycle. FIXED pp.4–6; IVA §A6; IVA_ACCEPT §3; TARGET §§2.1,8.2. | Exact for the declared tensor order and literal constants. |
| F5 | Helicity-sector intertwining and injection. TARGET §§2.2,8.2. | Exact reduced linear dynamics; normalized eigenbra required. |
| F6, F7 | Prepared raw initializer and cycle weights. BOUNDARY §4 C2–C4, §11; TARGET §8.4. | Exact composition of adopted preparation with fixed transfer. |
| J1 | Periodic-index spatial stencil. JTGMO lines4–46,62–76; IVA §A1. | Source equation; not the embedded-torus metric Laplacian. |
| J2 | January composite REFU step. JREFU lines109–138; APP lines234–238; ORIGINS1 §7.2. | Source order with stated app callbacks. |
| J3, J4 | Paper and signed compressors. JREFU lines37–69; APP lines54–57; ORIGINS1 §7.3. | Distinct historical maps and zero branches. |
| J5 | Prescribed H schedule. IVA §A5; SRGI §7.1. | Exogenous schedule; not state-driven memory. |
| N1, N2 | Modern two-stage deterministic recurrence. DYNAMICS lines57–104. | Declared raw map, including Arg₀ and λ=0 branches. |
| N3 | Tangent-face representation. PHASE1 §§3,6–7; KSM §10.3.3.2; FACE. | Inverse real isometries on the fixed vertical-face tangent spaces, with n_i·e_z=0. |
| N4 | Negative real-gradient increment. PHASE2_REVIEW §3 lines109–120; PHASE1 §7. | Exact increment identity; no unconditional discrete energy decay. |
| N5 | Explicit h-family and first-order approximation. PHASE2_REVIEW §3 lines109–151. | Conditional smooth-domain convergence as h tends to zero. |
| N6 | Action-angle sign and local-clock realization. PHASE3_ACCEPT §1 lines9–36; PHASE2_REVIEW §1. | Exact with the declared symplectic convention and chosen clock. |
| N7 | Cubic oscillator specialization. PHASE3_ACCEPT §7 lines207–218; PHASE3_REVIEW §9. | Exact continuous comparison only for K=0 and affine local clock. |
| S1, S2 | Finite spectrum and continuum inverse trace. RING §§2–3; ORIGINS1 §§5.1–5.2. | Exact spectrum and proven limit; all positive multiplicities, p>1/2. |
| S3, S4 | Free-ring Hamiltonians and energies. RING §§4.1–4.2. | Standard quantum interpretation adopts m, ℏ and energy scale. |
| S5 | Finite-band dynamical bound. RING §4.3 lines578–614. | Proven estimate under the adopted Schrödinger law. |
| S6, S7 | Inverse-cube trace and calibrated coupling. RING §5 lines616–683; ORIGINS1 §§5.2,6. | Exact calibrated equality; exponent and prefactor specified. |

Three important unnumbered results sit beside these equations: the same-step global complex-linear surjection obstruction is TARGET §§3.3,8.3; the orientation cycle is BOUNDARY §4 C4 and, separately, TARGET §8.4; the radius-three invariant polydisk and sharp uniform incident budget are BOUNDARY §§5,11. These are inherited proofs, not new FB02 computations.

The five locator corrections requested by GPT are used here and in the main text: PHASE2_REVIEW §3; PHASE3_ACCEPT §1; PHASE3_ACCEPT §7 with PHASE3_REVIEW §9; BOUNDARY §4 C4 plus TARGET §8.4; and BOUNDARY §§5,11. FB01 has not been amended.

## Appendix B. Referenced sources and versions

Source IDs retain their FB01 meanings. Each linked ID opens the exact cited source: fifteen byte-identical files are linked at a fixed GitHub commit, and fourteen snapshots are included with this edition. SOURCE_LOCATORS.json records their titles, versions, original filenames, publication locations and SHA-256 identities. In the PDF, narrative IDs link to the entries below, whose source links open GitHub. Page references to historical PDFs are physical file pages; line references are to the frozen source text. Source snapshots retain historical local paths and instructions as evidence; use this publication source guide for current access.

**[IVA](sources/IVA.md)** — Bridge IV-A — independent adversarial review and fundamental-physics connection map. v0.1; 22 September 2026. Corrected review, scoped results.

**[IVA_ACCEPT](sources/IVA_ACCEPT.md)** — Bridge IV-A — corrected accepted-results digest. v0.2; 22 September 2026. Scoped accepted digest.

**[BOUNDARY](sources/BOUNDARY.md)** — Boundary-response toy closure: explicit proposal, proofs and implementation path. v0.1; 22 September 2026; §11 added 23 September. §11 adopts lens_area_norm_v1 and supersedes the initial pending header within scope.

**[TARGET](sources/TARGET.md)** — Bridge IV-B Target B — corrected proof reconstruction and GPT review. 22 September 2026. §8 contains the later independent acceptance; original pending header is historical.

**[ORIGINS1](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/SRG_REDISCOVERY/PAPERS/SRG_ORIGINS_FROM_GEOMETRY_TO_RECURSION/publication/v0.1.1/manuscript/SRG_ORIGINS_v0.1.1.md)** — SRG Origins — From Geometry to Recursive Operators. v0.1.1 publication edition; 21 October 2026. Author-approved edition; used without reopening its publication audit.

**[ORIGINS_STATUS](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/SRG_REDISCOVERY/PAPERS/SRG_ORIGINS_FROM_GEOMETRY_TO_RECURSION/publication/v0.1.1/PUBLICATION_DISPOSITION.md)** — PUBLICATION_DISPOSITION.md for SRG Origins. v0.1.1. Later publication disposition governs edition status.

**[RING](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/SRG_REDISCOVERY/PAPERS/SRG_QUANTUM_RING_SPECTRAL_CORRESPONDENCE/publication/v0.1/SRG_QUANTUM_RING_v0.1.tex)** — Symbolic Resonance Geometry and Quantum Ring Spectra: An Exact Discrete-to-Continuum Spectral Correspondence. v0.1; 13 October 2026. Accepted publication source; §4 is quantum theory and §5 is coupling.

**[RING_STATUS](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/SRG_REDISCOVERY/PAPERS/SRG_QUANTUM_RING_SPECTRAL_CORRESPONDENCE/publication/v0.1/PUBLICATION_DISPOSITION.md)** — PUBLICATION_DISPOSITION.md for the quantum-ring paper. v0.1. Publication disposition reused, not re-audited.

**[SRGI](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/SRG_REDISCOVERY/PAPERS/SRG_I_FOUNDATIONAL_RECONSTRUCTION/publication/v0.1.1/manuscript/SRG_I_v0.1.1.tex)** — SRG-I: Foundational Reconstruction. v0.1.1; 10 October 2026. Completed accepted volume; inherited source distinctions.

**[LINEAGE](sources/LINEAGE.md)** — SRG mathematical and operator lineage. 11 October 2026. Completed documentary reconstruction.

**[PHASE1](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/research/top_to_recursive_bridge/TOP_TO_RECURSIVE_BRIDGE_DERIVATION.md)** — First bridge: folded geometry to three complex state components. 21 September 2026. Exact kinematics and conditional state interface.

**[PHASE2_REVIEW](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/research/phase_bridge_II/PHASE_BRIDGE_II_CODEX_REVIEW.md)** — Phase Bridge II — independent Codex verification. 21 September 2026. Corrected sign and conditional first-order family.

**[PHASE3_ACCEPT](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/research/phase_bridge_III/PHASE_BRIDGE_III_ACCEPTED_RESULTS.md)** — Phase Bridge III — accepted results. 22 September 2026. Operative corrected synthesis with stated assumptions.

**[PHASE3_REVIEW](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/research/phase_bridge_III/PHASE_BRIDGE_III_CODEX_FINAL_REVIEW.md)** — Phase Bridge III — Codex final independent review. 22 September 2026. Independent review; §9 scopes the oscillator equivalence.

**[KSM](sources/KSM.md)** — KERNEL_SOURCE_TO_MODEL.md. FB01 frozen snapshot. Admitted model/state correspondence at §10.3.3.2.

**[FIXED](sources/FIXED.pdf)** — Recursive SRG Evolution: A Qutrit–Qubit Operator, Dual-Core Geometry, and Computational Interpretation. 24 November 2025; file U_REFU.pdf. Historical fixed-matrix source, interpreted through corrected Bridge IV-A/IV-B.

**[P01](sources/P01.pdf)** — Symbolic Recursion and SRG Fusion: Emergent Lattice Fields from Glyph Memory Dynamics. 15 July 2025. Historical lock equation and Appendix A design rationale.

**[P06](sources/P06.pdf)** — Recursive Dark Energy and Vacuum Feedback: A Vesica-Phase Cosmological Framework. 13 July 2025. Historical equation; glossary identification conflicts with its solved γ*.

**[VPQW](sources/VPQW.pdf)** — Vesica Piscis Quantum Wavefunction (VPQW): A Novel Geometric Approach to Quantum Systems. printed cover: 28 February 2025. Historical conventions; circumference/radius discrepancy retained.

**[VESICA](sources/VESICA.pdf)** — The Vesica Delay Method: A Geometric-Perceptual Bridge to Coherence. 2025. Historical chosen radius and half-angle example.

**[APP](sources/APP.py)** — app.py. January archive 18285147; FB01 snapshot. Historical defaults, callbacks and time convention.

**[JREFU](sources/JREFU.py)** — refu.py. January archive 18285147; FB01 snapshot. Historical composition and compressor definitions.

**[JTGMO](sources/JTGMO.py)** — tgmo.py. January archive 18285147; FB01 snapshot. Historical periodic-index stencil.

**[INFINITY](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/SRG_REDISCOVERY/PAPERS/SRG_LOCAL_GEOMETRY_AND_RESONANCE_SIM04_SIM05/publication/v0.1.1/evidence/originals/SIM05/srg_infinity.py)** — srg_infinity.py. March archive 19023429; FB01 snapshot. Historical assigned coupling call sites.

**[BCODE](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/kernel_physics/boundary_response.py)** — kernel_physics/boundary_response.py. FB01 snapshot. Adopted preparation implementation, read only.

**[SRGCODE](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/kernel_physics/srg.py)** — kernel_physics/srg.py. FB01 snapshot. Frozen decimals, branch/gauge and fixed transfer implementation.

**[DYNAMICS](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/kernel_physics/dynamics.py)** — kernel_physics/dynamics.py. FB01 snapshot. Unchanged modern raw recurrence, read only.

**[REGION](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/kernel_physics/operating_region.py)** — kernel_physics/operating_region.py. FB01 snapshot. Opt-in radius-three domain and incident budget, read only.

**[FACE](https://github.com/pzychozen/trioctagon-physics/blob/9e813022b14158a3be710fdd71717c167de8d94b/kernel_physics/face_state.py)** — kernel_physics/face_state.py. FB01 snapshot. Optional state representation, read only.

**[GPT_REVIEW](provenance/reviews/FB01_GPT_SCIENTIFIC_REVIEW.md)** — FB01_GPT_SCIENTIFIC_REVIEW.md, 27 October 2026, supplied by the operator in the FB02 order packet. Decision: FB01 accepted within its source-and-equation scope. The cited review is preserved unchanged in this edition. Its historical instructions are task guidance only as adopted by the operator, not new mathematical evidence. Subsequent final manuscript acceptance and publication authorization are recorded in PUBLICATION_DISPOSITION.md.

**Classical references already in the accepted source chain.** NIST, [DLMF §25.12, Polylogarithms](https://dlmf.nist.gov/25.12). Lubomir Markov, [Hjortnaes Integrals Involving the Di- and Trilogarithms](https://www.diogenes.bg/ijam/contents/2024-37-3/2/2.pdf), International Journal of Applied Mathematics 37(3), 305–310 (2024), DOI 10.12732/ijam.v37i3.2, especially p.308, Eqs.(8),(11). These are the classical references carried by ORIGINS1 §4.4 and §11 and checked in the supplied GPT review; FB02 makes no new literature or priority claim.
