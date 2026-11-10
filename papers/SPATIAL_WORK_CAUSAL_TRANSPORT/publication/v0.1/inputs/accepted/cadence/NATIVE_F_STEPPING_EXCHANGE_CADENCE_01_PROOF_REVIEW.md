# Native F-stepping and exchange cadence: independent proof review

Research author: Hilmir Frímann Halldórsson (pzychozen).  
Review: Codex, 9 November 2026, Atlantic/Reykjavik.  
Task: NATIVE_F_STEPPING_EXCHANGE_CADENCE_01.

## Disposition and verification scope

The twelve proposed items are verified at their stated, bounded scopes. No mathematical coefficient or formula in the analytical start requires correction. The proofs below supply the analytical steps that exact arithmetic alone does not establish. Some locators in the internal notes require documentary clarification; these are recorded in CORRECTIONS_AND_LIMITS.md without changing any supplied file.

The first native jump can either increase or decrease native trial storage. It leaves the exact normalized episode-launch family for every allowed positive phase, but its actual synchronized chiral source remains nonzero throughout that interval. Consequently the first subsequent exchange segment has strict initial native debit and receiver gain, at each fixed phase. The original later capacity-sized receiving and quantified return theorem has not been established for this hybrid. Neither a phase-uniform positive exchange interval nor a selected physical cadence is proved here.

The map, exchange system, global solution theorem, exchange invariants, window accounts and restricted retained-receiver ratio are inherited. The indexed organization, specialized first-jump calculation, post-synchronization bound, local capacity expansion and limit deductions are checked here from those equations. Reliance on an accepted theorem is identified explicitly; this is not a new proof of the complete prior research programme.

Eight independent symbolic/rational check groups were completed before reading or running the two supplied checker implementations. Subsequent execution used exact copies outside the input tree and agreed on the shared quantities. Those two replays are corroboration, not two more independent findings. Analytical proofs, rather than scripts, establish regularity, strict inequalities, endpoint conventions, branch selection and asymptotic remainders.

## Source aliases and immutable basis

Paths here are relative to the delivered inputs directory:

- F: sources/native_code/dynamics.py.
- RR: sources/receiving_recovery/publication/v0.1/manuscript/.
- RX: sources/receiving_recovery/publication/v0.1/evidence/accepted_investigation/inputs/sources/P1/manuscript/.
- PC: sources/receiving_recovery/publication/v0.1/evidence/accepted_investigation/inputs/sources/P3/manuscript/.

SOURCE_LOCATORS.json and the claim/source ledger give exact labels, functions, lines and identities. The pinned reading commit is 6b1ef6494a4d4c34398ba9d9e5a7afce1fb03f37; the scientific publication commit is 34bf6c6e4e18adcc177ac700359fda16cf4d772d. The 140 paper files are retained accepted bytes bound to a fresh GitHub tree during packet preparation; four native-code files were newly fetched during that preparation. This execution checks their supplied bytes and reconstructed Git blob identities. It performs no fresh remote retrieval and does not describe all 140 paper files as newly downloaded. Both actual prior acceptance reports remain unchanged.

## F01 — exact map, model, ordering and state space

Put Ω=a+ib in C³, I=|Ω|², and retain

\[
\epsilon=\frac1{10},\qquad g=\frac1{60},\qquad
\lambda=\frac1{300},\qquad
(k_1,k_2,k_3)=\left(\frac{999}{1000},1,\frac{1001}{1000}\right).
\tag{1}
\]

Every component of the prestage uses the same original state:

\[
d_{{\rm pre},i}=\epsilon(k_i-|\Omega_i|^2)\Omega_i+
g\sum_{j\ne i}(\Omega_j-\Omega_i),\qquad v=\Omega+d_{\rm pre}.
\tag{2}
\]

Every phase increment uses the same v:

\[
\delta_i=\lambda\sum_{j\ne i}\sin(3[\operatorname{Arg}_0v_j-\operatorname{Arg}_0v_i]),
\qquad F_i(\Omega)=e^{i\delta_i}v_i.
\tag{3}
\]

Here Arg₀(0)=0, and an exactly zero v_i gives exactly zero F_i. The source's λ=0 path returns the prestage without phase extraction. At the present nonzero λ it applies the simultaneous harmonic-3 synchronizer. For three nodes the two cyclic neighbours in F/phase_sync are precisely j≠i; F/_advance uses the matrix L₃=11ᵀ−3Id. Its configuration calls λ “phase_strength”; it does not supply numerical defaults for (1). The tuple comes from RX/hybrid.tex, eq:tuple. The equivalent source expression |v_i|exp(i(Arg₀v_i+δ_i)) agrees with (3) in exact mathematics, including zero output. Floating-point complex128 evaluation, rounding and overflow are separate from these exact identities. No repository module is imported.

The prestage increment is generally different from FΩ−Ω. Neither the polynomial prestage nor synchronization is replaced by a differential equation, normalization or rescaled map.

For the exchange problem write α=α_N>0, β=β_R>0, η=η_N>0, κ=η_R>0, with fixed finite coefficients. At the fixed yaw π/4,

\[
\chi=a\times b,\quad f(x)=K\chi,\quad J(x)=D_xf(x),\quad
K=\frac G{\sqrt7}\begin{pmatrix}\sqrt2&\sqrt2&\sqrt3\\
\sqrt2&\sqrt2&-\sqrt3\end{pmatrix},\quad G=\kappa_{\rm in}\lambda_g>0 .
\tag{4}
\]

The native k_i in (1) are not the operator norm of K; λ is not the registration scale λ_g. Keep the finite periodic carrier, its admitted disjoint H¹ tent profiles, and the original receiver. With Bq=b_+q_++b_-q_- and y=B*p, B*B=mId₂, m=2/(3ε_c)>0, the unchanged system is

\[
\dot x=-\frac{\eta}{2\alpha}J(x)^Ty,\quad
p_t+c(r_c)_s=B(\eta f(x)-\kappa z),\quad
(r_c)_t+cp_s=0,\quad \dot z=\frac{\kappa}{\beta}y.
\tag{5}
\]

All spatial integrations are on the admitted finite periodic circle. Its geometry, profile width and receiver placement conventions are inherited, not chosen here. Define the original stores

\[
H_N=\frac\alpha2 I,\quad H_C=\frac12(\|p\|_2^2+\|r_c\|_2^2),
\quad H_R=\frac\beta2|z|^2,\quad E=H_C+H_R,\quad H_{\rm tot}=H_N+E.
\tag{6}
\]

The state space and norm used in the limit claims are

\[
\mathcal H=\mathbb R^6\times L^2_{\rm per}\times L^2_{\rm per}\times\mathbb R^2,
\quad \|X\|_E^2=\alpha|x|^2+\|p\|_2^2+\|r_c\|_2^2+\beta|z|^2.
\tag{7}
\]

For fixed positive weights this is a Hilbert norm equivalent to the product norm. RX/wellposed.tex, thm:global, gives the unique global mild exchange flow Φ_t, strong continuity, finite-time local Lipschitz dependence on bounded energy sets and conservation. Native and receiver coordinates are C¹. H¹ carrier data give C_tH¹∩C_t¹L² regularity; only first weak profile derivatives are needed.

Define F̂X=(F_Rx,p,r_c,z), and for one fixed symbolic h>0 retain

\[
X_{n+1}=T_hX_n=\Phi_h\widehat F X_n,\qquad X_n^+=\widehat F X_n.
\tag{8}
\]

X_n is immediately before its jump, X_n^+ immediately after it, and X_{n+1} is after exchange but before the next jump. This is inherited F-first composition. The external coordinates are carried through each native jump. It is not a numerical splitting approximation to a separately specified simultaneous native ODE.

Every ideal finite native state has a finite polynomial prestage and a defined finite synchronized image. The global exchange theorem therefore gives every finite hybrid iterate, including outside the earlier coherent domain. This does not imply a uniform bound over infinitely many native steps.

## F02 — first-jump-inclusive balances and endpoints

Homogeneity gives J(x)x=2f(x). Thus (5), periodic integration and the original one-half factors give

\[
P_{NC}=\eta f^Ty,\quad P_{CR}=\kappa z^Ty,\qquad
\dot H_N=-P_{NC},\quad\dot H_C=P_{NC}-P_{CR},\quad\dot H_R=P_{CR}.
\tag{9}
\]

The calculation is legitimate for H¹ preparations. RX's approximation/dependence argument extends the integrated identities to mild energy-space solutions. In particular it is not justified by assuming an H² tent.

At jump n set

\[
b_n=H_N(F\Omega_n)-H_N(\Omega_n),\qquad
D_n=\int_0^hP_{NC}(\Phi_tX_n^+)\,dt .
\tag{10}
\]

A native jump changes only H_N, by b_n. Integrating (9) afterward proves

\[
E_{n+1}-E_n=D_n,\quad H_{N,n+1}-H_{N,n}=b_n-D_n,\quad
H_{{\rm tot},n+1}-H_{{\rm tot},n}=b_n.
\tag{11}
\]

For N completed rounds, including the initial native jump,

\[
H_{\rm tot}(X_N)=H_{\rm tot}(X_0)+\sum_{n=0}^{N-1}b_n,\quad
E_N-E_0=\sum_{n=0}^{N-1}D_n,\quad
H_{N,N}-H_{N,0}=\sum_{n=0}^{N-1}b_n-(E_N-E_0).
\tag{12}
\]

For clarity, let native jumps occur at τ_n=nh, with X_n=X(τ_n−). The initial preparation X_0 is the pre-jump 0− state. Formula (12) compares pre-jump endpoints 0− and (Nh)−, so its jump set is n=0,…,N−1. If instead both endpoints are post-jump, 0+ and (Nh)+, the included jumps are n=1,…,N. Mixing these two conventions would drop the first jump or add the wrong final jump.

For arbitrary finite windows adopt RX's post-jump endpoint convention: at a jump endpoint use X(t+), and count t_a<τ_j≤t_b. With

\[
B_N(t_a,t_b)=\sum_{t_a<\tau_j\le t_b}b_j
\tag{13}
\]

one has ΔH_tot=B_N. External stocks are continuous across jumps. There is no impulsive carrier or receiver work. Define per-port powers P_{N,σ}=ηf_σy_σ and P_{R,σ}=κz_σy_σ and take positive and negative parts before summing:

\[
Q_{N\to C}=\int\sum_\sigma[P_{N,\sigma}]_+,\quad
Q_{C\to N}=\int\sum_\sigma[-P_{N,\sigma}]_+,
\quad
Q_{C\to R}=\int\sum_\sigma[P_{R,\sigma}]_+,\quad
Q_{R\to C}=\int\sum_\sigma[-P_{R,\sigma}]_+.
\tag{14}
\]

Piecewise continuity and finitely many jumps make these integrals well defined. Values at isolated endpoints do not change them. Their differences recover the signed total powers. Consequently

\[
\begin{aligned}
\Delta H_N&=B_N-Q_{N\to C}+Q_{C\to N},\\
\Delta H_C&=Q_{N\to C}-Q_{C\to N}-Q_{C\to R}+Q_{R\to C},\\
\Delta H_R&=Q_{C\to R}-Q_{R\to C},\\
\Delta H_N-B_N&=E(t_a)-E(t_b).
\end{aligned}\tag{15}
\]

These are inherited accounts with explicit indexing, not a newly proposed reservoir.

## F03 — recovery attribution and the retained ratio

Write E_a=E(t_a), E_b=E(t_b). Only if E_a>0 define

\[
\mathcal R_{\rm ex}=\frac{\Delta H_N-B_N}{E_a}
=1-\frac{E_b}{E_a}\le1,\qquad
\mathcal R_{\rm raw}=\frac{\Delta H_N}{E_a}
=\mathcal R_{\rm ex}+\frac{B_N}{E_a}.
\tag{16}
\]

The inequality uses E_b≥0. Exchange-attributable recovery is nonnegative exactly when E_b≤E_a. No strictly positive lower recovery bound follows from accounting alone. A positive baseline can increase the raw ratio without additional exchange credit; a negative baseline can reduce it while exchange credits the native store. In general preloaded windows there is no universal nonnegative lower bound for (16). Ratios with E_a=0 are undefined, even though (15) remains valid.

The denominator in RX's retained-receiver proposition is different. If H_C(t_a)=H_R(t_a)=0 and Q_{N→C}>0, (15) yields

\[
0\le\Delta H_R=H_R(t_b)=Q_{N\to C}-Q_{C\to N}-H_C(t_b)
\le Q_{N\to C}.
\tag{17}
\]

Therefore 0≤ΔH_R/Q_{N→C}≤1 survives finite native jumps under those actual starting and counting hypotheses. If Q_{R→C}=0 as well, ΔH_R=Q_{C→R} and the same bound holds for the gross receiving ratio. Without that extra condition, gross receiving counts repeated transfer and (17) is not its bound. With external preload neither nonnegativity of ΔH_R nor the bound by supply follows by this proof. Later hybrid segments cannot be silently relabelled empty.

The ratios (16), retained stock divided by positive supplied work, gross receiving work divided by supplied work, fractions of joint capacity and fractions of initial native stock are distinct. No tagged-cohort or physical efficiency statement follows. The earlier RR >24/25 recovery bounds require its actual exchange-only endpoint estimates; they are not consequences of (15) across jumps.

## F04 — moving floor and preloaded finite-window envelopes

At yaw π/4 set e=(1,−1,0)/√2, so Ke=0. For every native state define

\[
Z_2=\Omega^T\Omega,\quad h_e=|e\cdot\Omega|^2,\quad j=I-2h_e,
\quad L(\Omega)=\frac\alpha2\max(|Z_2|,j),\quad
C(\Omega)=H_N-L=\min\{C_Z,\alpha h_e\},
\quad C_Z=\frac\alpha2(I-|Z_2|).
\tag{18}
\]

The transpose in Z₂ is bilinear. The identity I²−|Z₂|²=4|a×b|² gives I≥|Z₂|, while h_e≥0 gives I≥j; thus 0≤L≤H_N and C≥0. Negative j is allowed.

For an independent check of invariance put w=Kᵀy and μ=η/(2α). Equation (5) gives

\[
\dot a=\mu w\times b,\quad\dot b=-\mu w\times a,\quad
\dot\Omega=-i\mu w\times\Omega.
\tag{19}
\]

Since Ωᵀ(w×Ω)=0, Z₂ is constant. Also İ=−4μw·(a×b). In a right-handed orthonormal basis with e as its third axis, w₃=0, and direct differentiation gives ḣ_e=−2μw·(a×b), hence j̇=0. Native coordinates are C¹ even for mild carrier data, so these differentiations are valid. L is consequently fixed during each exchange interval. These are PC's general-preparation invariants, not invariants of F.

In interval n let L_n^+=L(FΩ_n), C_n^+=C(FΩ_n), and keep the actual external preload E_n. Conservation on that interval and H_N(t)≥L_n^+ imply

\[
0\le E(t)\le E_n+C_n^+,\qquad
-E_n\le E(t)-E_n\le C_n^+ .
\tag{20}
\]

At a jump subtract the defining capacities to obtain exactly

\[
C(F\Omega)-C(\Omega)=b(\Omega)-[L(F\Omega)-L(\Omega)].
\tag{21}
\]

During exchange C(Ω(t))+E(t)=H_tot−L is constant; across a jump it changes by b−ΔL. Calling C an “exchange-only invariant” would therefore be wrong even within an interval: it is L, Z₂ and j that remain constant, while C falls when external stock rises.

For t inside interval n, after its jump and before the next,

\[
E(t)\le H_{\rm tot}(X_0)+\sum_{j=0}^{n}b_j-L(F\Omega_n).
\tag{22}
\]

This follows from (12) with the current jump included. Endpoint changes must use the matching convention in F02. A coarser finite-index consequence is E_N≤E_0+Σ_{n=0}^{N−1}C_n^+. Neither estimate bounds arbitrary pre-existing stock by C_n^+ alone, supplies a uniform infinite-step bound, or proves attainment of a capacity. The PC theorem's algebraic sharpness on a common invariant level is distinct from dynamical accessibility on a particular trajectory.

## F05 — exact first native storage increment and both signs

Now specialize only this first-jump comparison to the empty-external coherent preparation

\[
\Omega_\phi=(1,e^{i\phi},1),\qquad 0<\phi\le1/100,\qquad p=r_c=z=0.
\tag{23}
\]

Put q=e^{iφ}, D=1−cosφ and d₀=1/10000; d₀ is not the profile derivative constant. Substitution into (2), with ε(k_i−1)=(−d₀,0,d₀), gives

\[
v_1=1-d_0+g(q-1),\quad v_2=q+2g(1-q),\quad
v_3=1+d_0+g(q-1).
\tag{24}
\]

For any input, modulus preservation in (3) and expansion of |Ω+d_pre|² give

\[
I(F\Omega)-I(\Omega)=
2\epsilon\sum_i|\Omega_i|^2(k_i-|\Omega_i|^2)
-2g\sum_{i<j}|\Omega_i-\Omega_j|^2+\|d_{\rm pre}\|^2.
\tag{25}
\]

The coupling identity follows by pairing the two endpoints of each edge. If h_i=(k_i−|Ω_i|²)Ω_i, the square is

\[
\epsilon^2\|h\|^2+2\epsilon g\operatorname{Re}(h^\dagger L_3\Omega)
+g^2\|L_3\Omega\|^2,\qquad
\|L_3\Omega\|^2=3\sum_{i<j}|\Omega_i-\Omega_j|^2.
\tag{26}
\]

This is inherited and independently reconstructed in group A01. On (23) the onsite sum in (25) vanishes, the edge sum is 4D, and the full square equals 2d₀²+12g²D. Indeed d_pre=(−d₀+g(q−1),−2g(q−1),d₀+g(q−1)); the opposite onsite terms cancel the mixed terms after summation. Thus

\[
\Delta I=2d_0^2-4g(2-3g)D
=\frac1{50000000}-\frac{13}{100}D,\qquad
b_0=\alpha\left[\frac1{100000000}-\frac{13}{200}D\right].
\tag{27}
\]

Synchronization is fully present; λ disappears from this intensity calculation because it preserves each modulus. Omitting the finite square would wrongly omit the positive constant and change the D coefficient.

On 0≤φ≤1/100 the convergent alternating cosine series has decreasing term magnitudes, giving

\[
\frac{\phi^2}{2}-\frac{\phi^4}{24}\le1-\cos\phi\le\frac{\phi^2}{2}.
\tag{28}
\]

At φ=1/10000 these inequalities give ΔI≥387/20000000000>0. At φ=1/1000 they give ΔI≤−107999987/2400000000000000<0. Both are allowed positive phases. D is continuous and strictly increasing there because sinφ>0. Hence its single crossing of 1/6500000 gives

\[
\phi_*=\arccos(1-1/6500000),\qquad 1/10000<\phi_*<1/1000.
\tag{29}
\]

The baseline is positive below, zero at and negative above that threshold within the admitted interval. The old empty-launch capacity C_φ=αD is positive for φ>0, and

\[
\frac{b_0}{C_\phi}=\frac1{100000000D}-\frac{13}{200}\longrightarrow+\infty
\quad(\phi\downarrow0).
\tag{30}
\]

Here b₀ itself tends to the small finite value α/100000000; the denominator tends to zero. This unbounded ratio is neither exchange efficiency nor an unbounded increase in accessible capacity.

## F06 — exit from the precise RR preparation

Expanding (24) and again using modulus preservation gives

\[
|F_1\Omega_\phi|^2=(1-d_0)^2-2g(1-d_0-g)D<(1-d_0)^2<1,
\tag{31}
\]

because D>0 and 1−d₀−g>0. Moreover,

\[
|F_3\Omega_\phi|^2-|F_1\Omega_\phi|^2
=4d_0(1-gD)>0.
\tag{32}
\]

For example D≤1/20000 from (28), so 1−gD>0. Thus every allowed positive phase leaves the exact unit-modulus family; unequal first and third moduli cannot be repaired by a common phase or a single common nonzero amplitude factor. In particular FΩ_φ≠Ω_φ. This is failure of a narrow launch hypothesis, not proof of departure from the larger coherent domain.

Even h≥t_F from RR would only allow sufficient exchange time before the next jump. In the fixed F-first protocol the first interval starts at FΩ_φ, not Ω_φ. The old theorem therefore cannot be reapplied merely by lengthening h. Later intervals also generally have external preload. This is an obstruction to importing that theorem, not a counterexample to actual later receiving or recovery in the hybrid.

## F07 — full-interval phase ordering and the synchronized source bound

Write v_i=ρ_i exp(iθ_i). In (24),

\[
v_1=(1-d_0-g)+gq,\quad v_2=2g+(1-2g)q,\quad
v_3=(1+d_0-g)+gq.
\tag{33}
\]

All coefficients are positive. For 0<φ≤1/100 each v_i is nonzero and strictly inside the cone spanned by 1 and q, so 0<θ_i<φ with ordinary principal arguments and no wrap. Direct multiplication gives

\[
\operatorname{Im}(\overline v_1v_2)=A_*\sin\phi,\qquad
A_*=1-3g-d_0(1-2g)=\frac{284971}{300000}>0.
\tag{34}
\]

Also Im(conj(v₃)v₁)=2d₀g sinφ>0. Since every phase difference has magnitude below φ<π/2, sine has its sign. Thus θ₃<θ₁<θ₂.

Let θ_i^+=θ_i+δ_i be the actual phases appearing in (3). On |u|≤φ define

\[
w(u)=\begin{cases}\lambda\sin(3u)/u,&u\ne0,\\3\lambda,&u=0.\end{cases}
\quad 0\le w(u)\le3\lambda .
\tag{35}
\]

Indeed |3u|≤3/100<π, so sin(3u) has the sign of u, and |sin(3u)|≤3|u|. Hence

\[
\theta_i^+=\left(1-\sum_{j\ne i}w(\theta_j-\theta_i)\right)\theta_i+
\sum_{j\ne i}w(\theta_j-\theta_i)\theta_j.
\tag{36}
\]

The sum of off-diagonal weights is at most 6λ=1/50<1. Thus every updated phase stays between the original minimum and maximum and remains in (0,φ). Equation (36) concerns the actual simultaneous update, not sequential averaging.

For any ordered pair θ_j>θ_i, put Δ=θ_j−θ_i>0 and let ℓ be the third node. Subtracting the increments gives

\[
\theta_j^+-\theta_i^+
=\Delta-2\lambda\sin(3\Delta)
+\lambda[\sin(3(\theta_\ell-\theta_j))-\sin(3(\theta_\ell-\theta_i))]
\ge(1-9\lambda)\Delta.
\tag{37}
\]

Here sin(3Δ)≤3Δ and the derivative of sin(3u) has absolute value ≤3, so the bracket is ≥−3Δ. Set s_*=1−9λ=97/100>0. All three strict phase orderings survive. In particular Δ^+=θ₂^+−θ₁^+≥s_*Δ>0 and Δ^+≤φ<π/2.

Sine is increasing on this interval and concave on [0,π/2]. Therefore sinΔ^+≥sin(s_*Δ)≥s_*sinΔ. The actual synchronized third chirality component satisfies

\[
\chi_3^+=\rho_1\rho_2\sin\Delta^+
\ge s_*\rho_1\rho_2\sin\Delta=s_*A_*\sin\phi>0.
\tag{38}
\]

The raw port convention in (4) is explicitly

\[
f_{{\rm raw},\pm}=\frac G{\sqrt7}
\{\sqrt2(\chi_1+\chi_2)\ \mathord{\pm}\ \sqrt3\chi_3\},
\quad f_{{\rm raw},+}-f_{{\rm raw},-}=\frac{2\sqrt3G}{\sqrt7}\chi_3.
\tag{39}
\]

There are no additional ambient-contact orientation signs. At the original launch χ=(−sinφ,0,sinφ), these formulas give Gsinφ(−√2±√3)/√7, with positive raw + and negative raw − entries. For the post-F proof it is the strictly positive difference in (39) that is needed; it does not assume that every individual post-F port has a particular sign. Squaring and adding the two raw entries gives exactly

\[
|K\chi|^2=\frac{G^2}{7}\{4(\chi_1+\chi_2)^2+6\chi_3^2\}.
\tag{40}
\]

Using (38) in (40) proves, throughout the entire permitted positive phase interval,

\[
|f(F\Omega_\phi)|^2\ge
\frac{6G^2}{7}s_*^2A_*^2\sin^2\phi>0.
\tag{41}
\]

The coefficient multiplying G²sin²φ is the exact rational 764090502142969/1050000000000000. “Uniform” refers to that coefficient over the phase interval, not an absolute positive lower bound independent of phase: sinφ→0 at the excluded zero endpoint. This proof uses no phase sweep.

## F08 — initial actual supply and receiving, with the quantifiers retained

Use f^{post}=f(FΩ_φ) for the full two-component source vector, to avoid confusing a post-jump superscript with the raw + port. Fix one finite positive exchange coefficient tuple before considering phase. For each fixed φ in (0,1/100], start the exact exchange flow at X_0^+=(FΩ_φ,0,0,0).

The inherited RX empty-carrier proposition applies to arbitrary native preparation with nonzero drive; it does not require the old all-unit family. Nonvanishing follows from (41). Empty carrier data are H¹, so the inherited strong theorem supplies p′(0)=ηBf^{post} and r_c′(0)=0 in L². Thus

\[
p(t)=\eta tBf^{post}+o_{L^2}(t),\quad r_c(t)=o_{L^2}(t),
\quad y(t)=\eta mtf^{post}+o(t).
\tag{42}
\]

Boundedness of J near this fixed native preparation and y(t)=O(t) imply x(t)−x(0)=O(t²). Since f is a quadratic polynomial, f(x(t))=f^{post}+O(t²). Integrating (9) and the receiver equation gives

\[
\begin{aligned}
H_N(F\Omega_\phi)-H_N(t)&=\frac{\eta^2m}{2}|f^{post}|^2t^2+o(t^2),\\
z(t)&=\frac{\eta\kappa m}{2\beta}f^{post}t^2+o(t^2),\\
H_R(t)&=\frac{\eta^2\kappa^2m^2}{8\beta}|f^{post}|^2t^4+o(t^4).
\end{aligned}\tag{43}
\]

The second line is squared only after its vector expansion, retaining the original β/2 storage factor. The leading coefficients of the native debit and receiver gain are strictly positive. More explicitly,

\[
P_{NC}(t)=\eta^2m|f^{post}|^2t+o(t),\qquad
P_{CR}(t)=\frac{\eta^2\kappa^2m^2}{2\beta}|f^{post}|^2t^3+o(t^3).
\tag{44}
\]

At this fixed preparation the definition of little-o supplies a δ(φ,tuple)>0 such that both powers and both quantities in (43) are positive for 0<t<δ. For example choose each remainder smaller than half its positive leading coefficient times the displayed power, then take the minimum of the finitely many positive neighbourhood sizes. Q_{N→C}>0 on such short windows because the sum of positive per-port powers is at least the strictly positive signed total.

These are actual conservative feedback trajectories with the receiver coupling retained, not a source-clamped comparison. No second spatial derivative of a tent was used. In the hybrid these estimates apply up to the next jump: 0<t<min(h,δ). They do not ensure that the state sampled at h remains in this small-time regime unless h is also suitably small. No uniform lower bound for δ over φ is obtained merely from (41), and no such bound is claimed or disproved here. The later quarter-capacity receiver stock and >24/25 return bounds remain unproved for this trajectory.

## F09 — local branch change and exact asymptotic capacity coefficient

For the original launch, I₀=3, Z₀=2+exp(2iφ), h_e=D and j₀=1+2cosφ. Both j₀ and |Z₀| are positive. Their squared difference is

\[
j_0^2-|Z_0|^2=4\cos\phi(1-\cos\phi)>0.
\tag{45}
\]

Hence the old positive-phase capacity is the projection branch C_φ=αD.

Keep the actual nonzero d₀ fixed. At φ=0, (24) and zero synchronization give

\[
r=F\Omega_0=(1-d_0,1,1+d_0),\quad R^2=|r|^2=3+2d_0^2,
\quad C_Z(r)=0,\quad h_e(r)=d_0^2/2>0.
\tag{46}
\]

Both competing capacity functions are continuous. The strictly positive difference αh_e−C_Z at zero therefore remains positive in some neighbourhood of zero. In that neighbourhood C(FΩ_φ)=C_Z(FΩ_φ). This is an existence-of-neighbourhood argument; it supplies no explicit numerical phase width and does not establish that this branch controls the whole (0,1/100] interval.

Let u=(g,1−2g,g). The analytic prestage (24) has derivative iu at zero. Since r_i>0, ordinary phase extraction is real analytic in a neighbourhood of this prestage, with θ_i′(0)=u_i/r_i. Differentiating the simultaneous synchronization at equal zero phases gives

\[
\delta_i'(0)=3\lambda\left(\sum_j u_j/r_j-3u_i/r_i\right),\qquad
F\Omega_\phi=r+it\phi+O(\phi^2),\quad
t=s_*u+3\lambda r\sum_j u_j/r_j .
\tag{47}
\]

This derivative can equivalently be reconstructed as diag(r)(Id+3λL₃)diag(1/r)u; independent group A05 uses that matrix derivation. The added multiple of r contributes no cross product:

\[
r\times t=s_*(r\times u)
=\frac1{30000000}(-27647813,97,27642187).
\tag{48}
\]

Locally FΩ_{−φ}=conj(FΩ_φ): the prestage coefficients are real, the phases are odd under conjugation near positive r, and sine is odd. Real analyticity and this symmetry give

\[
\operatorname{Re}F\Omega_\phi=r+v_2\phi^2+O(\phi^4),\quad
\operatorname{Im}F\Omega_\phi=t\phi+O(\phi^3),
\quad \chi^+=(r\times t)\phi+O(\phi^3).
\tag{49}
\]

The unknown real v₂ must not be silently discarded. Indeed its contributions are

\[
\begin{aligned}
I&=R^2+(2r\cdot v_2+|t|^2)\phi^2+O(\phi^4),\\
|Z_2|&=R^2+
\left(2r\cdot v_2-|t|^2+\frac{2(r\cdot t)^2}{R^2}\right)\phi^2+O(\phi^4).
\end{aligned}\tag{50}
\]

The modulus expansion is valid because Z₂(0)=R²>0. Subtracting cancels v₂, giving

\[
C_Z(F\Omega_\phi)=\alpha\left(|t|^2-\frac{(r\cdot t)^2}{R^2}\right)\phi^2
+O(\phi^4).
\tag{51}
\]

Equivalently C_Z=2α|a×b|²/(I+|Z₂|); (49) and the nonzero even denominator prove the same remainder order. The fixed α is included in the constant implicit in O(φ⁴).

The radial term in t cancels from the orthogonal squared norm in (51). Direct exact arithmetic yields

\[
|u|^2=\frac{187}{200},\quad r\cdot u=1,\quad
Q=s_*^2\left(\frac{187}{200}-\frac1{3+2d_0^2}\right)
=\frac{169832451759483}{300000002000000}>0.
\tag{52}
\]

Combining branch selection and (51), then using 1−cosφ=φ²/2+O(φ⁴), proves

\[
C(F\Omega_\phi)=\alpha Q\phi^2+O(\phi^4),\qquad
\lim_{\phi\downarrow0}\frac{C(F\Omega_\phi)}{C_\phi}
=2Q=\frac{169832451759483}{150000001000000}
\simeq1.132216337515111.
\tag{53}
\]

This is a ratio of two algebraic ceilings, not achieved transfer, an efficiency improvement, a new receiving certificate or a full-interval bound. Taking d₀=0 before taking φ→0 removes the strict gap in (46) and invalidates this branch-selection argument. Neither that different limit nor any detuning optimization is undertaken.

## F10 — strong small-h limit and the finite-N qualification

For fixed X∈H the image F̂X is a defined point even if F fails to be continuous at neighbouring inputs. Strong continuity of the inherited exchange flow at this fixed point gives

\[
T_hX=\Phi_h(\widehat FX)\longrightarrow\widehat FX
\quad\text{in }\|\cdot\|_E,\quad h\downarrow0.
\tag{54}
\]

No differentiation of the unbounded translation generator is used. If F̂X≠X, norm continuity gives

\[
\|T_hX-X\|_E\longrightarrow\|\widehat FX-X\|_E>0,\qquad
\frac{\|T_hX-X\|_E}{h}\longrightarrow+\infty.
\tag{55}
\]

For every positive phase in (23), (31) already guarantees FΩ_φ≠Ω_φ. Indeed the first component alone gives |F₁−1|≥1−|F₁|>d₀, although no uniform-in-phase exchange remainder is needed for the pointwise conclusion (55).

Suppose samples at h were to approximate, uniformly near time zero, a continuous limiting curve Y with Y(0)=X. Then Y(h)→X, but T_hX→F̂X≠X, so the error at the first sample cannot tend to zero. Thus the fixed map does not give an ordinary near-identity time refinement with that same initial value. This does not exclude useful finite h, special fixed states, singular initial layers or a differently justified limiting problem.

For fixed finite N assume F is continuous at the native parts of X,F̂X,…,F̂^{N−1}X. All encountered prestage components being nonzero is sufficient: expressions involving exp(i3Arg v) are powers of v/|v|, so a branch cut of Arg alone is not an obstruction away from zero. The zero convention by itself supplies no general neighbouring continuity at zero-prestage strata.

Joint continuity of exchange near (0,Y) follows from the inherited estimate:

\[
\|\Phi_hY_h-Y\|_E
\le e^{Lh}\|Y_h-Y\|_E+\|\Phi_hY-Y\|_E\longrightarrow0
\quad\text{if }Y_h\to Y,\ h\downarrow0,
\tag{56}
\]

where nearby preparations lie in a common bounded energy ball and L is a finite local Lipschitz constant. Assuming T_h^nX→F̂^nX, continuity of F̂ at F̂^nX and (56) give the n+1 case. Induction proves

\[
T_h^NX\longrightarrow\widehat F^NX\qquad\text{for each such fixed finite }N.
\tag{57}
\]

RX's cited native-only forward-invariant coherent-domain result supplies nonzero prestages along the native-only orbit of the coherent launches, hence is sufficient for any fixed N there. This use of an inherited native-only theorem does not assert invariance of the active hybrid domain. No constants uniform in N are proved, and nothing permits substituting N≈T/h into the finite induction. No relation tying h to ν, γ, ω_R or the carrier circumference follows from (54)–(57).

## F11 — positive baseline, changed invariants, zero capacity and dark iterates

The boundary value φ=0 is outside RR's strictly positive launch range, but is an admissible separate real preparation. Exactly

\[
F(1,1,1)=(9999/10000,1,10001/10000)=r,\qquad
b=\frac\alpha{100000000}>0.
\tag{58}
\]

Before and after this jump the state is real, so χ=f=0, Z₂=I, L=H_N and C=0. More explicitly,

\[
\begin{aligned}
I(r)=Z_2(r)&=3+2d_0^2,&
h_e(r)&=d_0^2/2,& j(r)&=3+d_0^2,\\
\Delta I=\Delta Z_2&=2d_0^2,&
\Delta j&=d_0^2,& \Delta L&=b,\quad\Delta C=0.
\end{aligned}\tag{59}
\]

Thus neither exchange invariant survives the native jump unchanged, and the entire positive baseline increment can raise the invariant floor without raising capacity.

For any real native state the polynomial prestage is real. Its nonzero component arguments are integer multiples of π, with Arg₀(0)=0. Every sine in (3) is therefore exactly zero and the image remains real, including zero-prestage cases. This statement concerns the exact mathematical map; floating evaluations of sin(3π) are not being asserted to vanish bit-for-bit.

At a real native state with empty external coordinates the constant full state solves (5), since f=0, y=0 and z=0. The inherited uniqueness theorem makes each exchange segment stationary. Induction then gives real native coordinates and identically zero external stores at every finite hybrid iterate, for every fixed positive h. Native increments need not remain positive in later rounds; the positive first increment in (58) is the witness required here.

This does not contradict the nonzero drive at every strictly positive phase. It also does not imply that zero drive plus arbitrary external preload is stationary: the native feedback Jᵀy can then be nonzero. The witness establishes that baseline gain alone guarantees neither exchange activity nor capacity replenishment.

## F12 — cadence status and the remaining gap

The exact conclusions are (11)–(22), the first-jump formulas and sign transition (27)–(30), departure from RR's precise launch family, full-phase nonzero synchronized source (41), phasewise initial activity (43), local ceiling expansion (53), the strong and qualified finite-N limits, and the separate dark witness.

For the accepted episode tuple RR defines comparison rates ν, γ and ω_R and times t_A,t_R,t_F for one exchange-only preparation. Dimensionless comparisons such as νh, γh, ω_Rh and ch/L_c may compare a chosen h with those scales. They do not choose h or identify native iteration number with a physical clock. The source-off circulation period also requires vanishing internal forcing to describe the actual carrier motion; an active autonomous feedback system is not source-off merely because it has no external forcing.

The later receiving/recovery certificate would require a new estimate for the actual post-F preparation and, for subsequent rounds, actual external preload and further native jumps. The baseline-subtracted endpoint identity remains available, but estimates forcing E_b/E_a below the required recovery threshold have not been proved for those hybrid windows. This is a remaining theorem gap, not a source conflict and not a proof that such receiving/recovery is impossible.

In particular this review proves neither H_R>C/4 nor >24/25 native exchange recovery after inserting native steps, no recurrent orbit, no optimum cadence, no exact physical period, no uniform infinite-step bound, and no automatic preservation of the earlier coherent domain by active exchange. A claim of a uniform positive exchange interval across all allowed phases would require a suitable relative remainder estimate not supplied here.

No author decision is needed to finish this bounded existing-equation assessment. A later choice to identify native updates with physical time would require an explicit additional modeling rule. Reordering to exchange-first, delaying the first jump, resetting external states, normalizing F, adding a compensating reservoir or scaling native coefficients with h would change the present problem. None is done.

The carrier circle remains distinct from the intended toroid and central spatial route; this trial-storage account does not assign a material receiver location, a six-opening route, irreversible retention or physical energy calibration. The broader geometry and native-motion programme remain outside this first-stage result.

## Evidence and completion statement

F01–F12 each have an explicit inherited/new classification and proof location in the claim ledger. INDEPENDENT_ALGEBRA_RESULTS.json records eight exact support groups; SUPPORT_COMPARISON.json records the two separate unchanged checker replays and matching quantities. The derivation of inequalities, regularity, endpoint rules and asymptotic orders is the written proof above, not a claim of formal-machine theorem verification.

All 169 input occurrences and all 144 source identities are covered by before/after checks. The prepared deliverables and source locators are checked before packaging. No Git command, remote mutation, repository-module import, evolved trajectory, broad sweep, scientific-suite rerun, dependency installation, manuscript build or successor investigation is performed. This review is returned for GPT/author assessment, not represented as already accepted by them.
