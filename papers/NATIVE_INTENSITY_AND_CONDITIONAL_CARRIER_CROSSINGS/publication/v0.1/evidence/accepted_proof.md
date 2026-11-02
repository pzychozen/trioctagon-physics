# Native central energy transport — proof review

2 November 2026 · NATIVE_CENTRAL_ENERGY_TRANSPORT_01 · For GPT/author discussion

This is the bounded balance-and-correspondence investigation requested by Hilmir Frímann Halldórsson / pzychozen. It is not a manuscript or a model amendment. Bracketed source IDs resolve to exact paths, SHA-256 identities, and line/equation locators in `CLAIM_SOURCE_LEDGER.md`; numbered source excerpts accompany this report.

## Executive answer

**The existing model already accounts exactly for changes in the three channel strengths. It also has a separately adopted carrier that propagates a mathematically defined energy, with exact signed source work and local flux. That carrier is registered to two finite host-notch measurement regions. These are substantive positive results. The inspected equations do not yet say that native energy leaves the central region through any of its six broken opening boundaries.**

The native intensity balance separates an antisymmetric channel exchange, onsite change, pair mismatch, and the full finite-step square. The accepted potential decreases on its specified coherent domain. Neither statement supplies an exterior recipient. In the conditional carrier, a named native readout really does determine two source strengths after the specified projection and gain. However, carrier work is not debited from the native recurrence; it depends on the carrier's response as well as its drive. Thus the missing native link is a reciprocal balance equation, not merely a numerical calibration.

The strongest existing direction statement can also be made explicit. On the adopted circle, the carrier has signed power through its two host-notch crossings: minus the oriented carrier flux at the upper contact and plus that flux at the lower contact. An exact storage balance holds for the intervening arc. The signs are determined by the carrier state, not by the words “upper,” “lower,” or “outward.” This does not identify either contact with a central broken boundary, nor extend one paired carrier to six outlets.

To say **which central opening receives an amount leaving the core**, the model needs an explicit transfer observable attached to those six geometric objects and a balance coupling that observable to a named native amount. For a surface-flux interpretation this additionally requires declared oriented apertures/control surfaces; the currently defined broken arcs have no filled interiors or aperture normals. For the existing carrier route it requires a native debit and a registration from the selected two host-notch crossings to the central openings. The present sources supply neither interface. Supplying the initial common phase recovers phase-sensitive decoded vectors; that recovery alone does not supply the transfer law.

The author's controlling question is “I thought we were talking about energy leaving from the center.” The flower analogy is a qualitative lead. The earlier assistant's inward-arrival, redirection, and “next available” outlet sequence is an unverified proposal, not an author-defined mechanism. No such sequence, petal mechanism, golden-ratio controller, or new flow law is adopted here. [WORK_ORDER]

## A. Native balance and the separate transport account

### A.1 Typed inventory

| Quantity | Mathematical type and dependence | Existing placement and accounting |
| --- | --- | --- |
| `s_i=|Ω_i|²`, `I=Σs_i` | Nonnegative channel scalars; native state only | `s_i` is also the squared norm of the decoded vector based on face `i`. No spatial volume density is specified. Exact finite balance below. |
| `V` | Real quartic native potential, with fixed real coefficients | A function on six real state coordinates; no exterior location. Exact prestage and phase-stage changes; accepted domain-specific descent. |
| `D_ij=|Ω_i−Ω_j|²` | Nonnegative matched edge quadratic | Equals `||v_i−T_ij v_j||²` under the face decoder. This compares vectors after matched tangent transport; it is not a material conduit. |
| `A_ij=Im(conj(Ω_i)Ω_j)` | Antisymmetric signed area in channel coordinates | Raw `C=(A_23,−A_13,A_12)` has a separate ambient attachment `W=T_f C`. Neither is a flux merely because it is oriented. Exact prestage and phase-source budgets exist. |
| `J^I_(i→j)=g(s_i−s_j)` | Antisymmetric scalar exchange per native step in the decomposition below | Defined on the three channel edges, not on the six openings. Its divergence is fixed by this split; a divergence-free cycle can be added. |
| C1 `e=(p²+r_c²)/2`, `E=∫e ds` | Nonnegative carrier density and storage on a periodic one-dimensional circle | Under C1, `∂_t e+∂_s j=p g_c`, `dE/dt=Σf_σ y_σ`; physical identification with native energy is not supplied. |
| C1 `j=c p r_c` | Signed local flux along the oriented circle | Power through a carrier cut; the two contact signs are derived in B.4. `∫j ds` has an extra length factor and is not power through a section. |
| C6 `(U,V_ext)` | Retarded scalar/vector observation of a carrier history | Values at off-circle receivers; no ambient energy storage, radiative-power balance, or receiving load is defined by this readout. |

Here `r_c` denotes the carrier variable called `r` in its source, to distinguish it from geometric radii. Likewise `g_c` is carrier forcing, not native graph coefficient `g`. [NATIVE; DIAGNOSTICS; FACE; AXIAL; NRG_RESPONSE; NRG_ATTACHMENT; C1_FOUNDATIONS; C1_CARRIER; C6_EXTERIOR]

### A.2 Exact component and total intensity accounting — independently derived

For general real native coefficients define

\[
s_i=|\Omega_i|^2,\quad S_{ij}=\Re(\overline\Omega_i\Omega_j),\quad
A_{ij}=\Im(\overline\Omega_i\Omega_j),\quad D_{ij}=s_i+s_j-2S_{ij}.
\]

The source map uses the **prestage** increment

\[
b_i=\epsilon(k_i-s_i)\Omega_i+g\sum_{j\ne i}(\Omega_j-\Omega_i),\qquad
\widetilde\Omega=\Omega+b,\qquad F_i=e^{i\delta_i}\widetilde\Omega_i.
\tag{A1}
\]

All phase kicks are evaluated from the same prestage:
`δ_i=λΣ_(j≠i) sin(3(Arg₀ Ω̃_j−Arg₀ Ω̃_i))`, with `Arg₀(0)=0` and the native `λ=0` bypass. No quotient by a zero modulus is used here. [NATIVE; POT_SETTING]

Since multiplication by `e^{iδ_i}` preserves each modulus, direct expansion gives

\[
\Delta s_i=2\Re(\overline\Omega_i b_i)+|b_i|^2
=2\epsilon s_i(k_i-s_i)+2g\sum_{j\ne i}(S_{ij}-s_i)+|b_i|^2.
\tag{A2}
\]

For each neighbor,

\[
2g(S_{ij}-s_i)=g(s_j-s_i)-gD_{ij}.
\]

Consequently the candidate split is correct, including its orientation:

\[
\boxed{\Delta s_i=-\sum_{j\ne i}J^I_{i\to j}
 +2\epsilon s_i(k_i-s_i)-g\sum_{j\ne i}D_{ij}+|b_i|^2,\quad
 J^I_{i\to j}=g(s_i-s_j)=-J^I_{j\to i}.}
\tag{A3}
\]

Summing the three node equations cancels the exchanges. Each undirected mismatch appears at two nodes, so, counting each edge once,

\[
\boxed{\Delta I=2\epsilon\sum_i s_i(k_i-s_i)-2g\sum_{i<j}D_{ij}+\|b\|_2^2.}
\tag{A4}
\]

This agrees with `intensity_budget` and the inherited Z03 identity. The proof is a polynomial norm expansion, valid even at zero components; it needs neither the coherent-domain theorem nor a computed native successor. New symbolic groups 1–3 verify the expansion, sign, cancellation, and finite square. [DIAGNOSTICS; Z03]

The whole square matters. With `h_i=(k_i−s_i)Ω_i` and `L_N=11ᵀ−3Id`,

\[
\|b\|^2=\epsilon^2\|h\|^2+2\epsilon g\Re(h^\dagger L_N\Omega)
 +g^2\|L_N\Omega\|^2,\qquad
\|L_N\Omega\|^2=3\sum_{i<j}D_{ij}.
\tag{A5}
\]

The mixed term has no fixed sign. For `g≥0`, the displayed mismatch term is nonpositive and the algebraic exchange points from larger to smaller intensity; the complete component or total change need not have that sign. The onsite term also changes sign with `k_i−s_i` when `ε>0`. No sign rule is asserted for arbitrary negative coefficients.

**Exchange is not uniquely selected current.** Add the same real `a` to oriented edges `1→2`, `2→3`, `3→1`, and its negative to their reverses. Every node divergence is unchanged. This suffices to show cycle-current freedom when only divergence is prescribed; no classification of currents is required. Moreover, signed area is a different object: for symbolic positive unequal aligned amplitudes, `A_ij=0` while `g(s_i−s_j)` can be nonzero; for equal amplitudes with a nonzero relative sine, the exchange is zero while `A_ij` is nonzero. These are formula comparisons, not new states evolved through F.

The split therefore establishes exact **channel bookkeeping**. It supplies no spatial opening label, boundary normal, transfer duration, or external receiving state.

The earlier weighted response result does not supply a missing boundary current either. At a positive fixed branch with amplitudes `r_i`, its phase-prestage matrix satisfies `P_ij=g r_j/r_i` off diagonal and `R²P=PᵀR²`, with quadratic form `gΣ_(i<j)r_i r_j(f_i−f_j)²`. These are exact response weights, positive conductances when `g>0`; row sums alone do not make P a Markov matrix, and the complete linearized phase stage has the ordered product `S_φ P`. None of these response statements assigns a six-opening flux. [NRG_RESPONSE eq:P, eq:weighted, eq:SP]

### A.3 Synchronization and potential loss

Let `d_ij=δ_j−δ_i`. The same modulus-preserving phase stage changes pair coherence by

\[
S_{ij}^+=\widetilde S_{ij}\cos d_{ij}-\widetilde A_{ij}\sin d_{ij},\qquad
A_{ij}^+=\widetilde A_{ij}\cos d_{ij}+\widetilde S_{ij}\sin d_{ij}.
\tag{A6}
\]

For example, the inherited area budget uses `M=Id+ε diag(k−s)+gL_N`, so `Ã=MAMᵀ`; its expansion contains onsite-first, graph-first, onsite-square, mixed, and graph-square terms. The phase contribution is `Ã_ij(cos d_ij−1)+S̃_ij sin d_ij`. The ambient attachment of these areas does not alter their status into a flow law. [AXIAL; NRG_ATTACHMENT; Z03]

Use the accepted normalization

\[
\mathcal V=\epsilon\sum_i(s_i^2/4-k_i s_i/2)+\frac g2\sum_{i<j}D_{ij},
\qquad b=-\nabla_{\mathbb R^6}\mathcal V.
\tag{A7}
\]

The inherited exact prestage account is

\[
\mathcal V(\Omega+b)-\mathcal V(\Omega)
=-\|b\|^2+\int_0^1(1-t)b^T\nabla^2\mathcal V(\Omega+tb)b\,dt.
\tag{A8}
\]

For an explicit finite polynomial version, put `q_i=2Re(conj(Ω_i)b_i)+|b_i|²`. Expanding the quartic onsite term and each edge norm gives

\[
\begin{split}
\Delta\mathcal V_{\rm pre}={}&\epsilon\sum_i\left[\frac{(s_i-k_i)q_i}{2}+\frac{q_i^2}{4}\right]\\
&+g\sum_{i<j}\Re\{\overline{(\Omega_i-\Omega_j)}(b_i-b_j)\}
 +\frac g2\sum_{i<j}|b_i-b_j|^2,\\
\Delta\mathcal V_{\rm sync}={}&g\sum_{i<j}
 [\widetilde S_{ij}(1-\cos d_{ij})+\widetilde A_{ij}\sin d_{ij}].
\end{split}
\tag{A9}
\]

The second line follows because synchronization changes only the `−gΣS_ij` part of V. Thus zero synchronization intensity change does **not** mean zero potential change or no influence on later steps. New symbolic groups 4–5 support these algebraic signs and expansions. [POT_SETTING; POT_FINITE; NRG_RESPONSE]

The accepted theorem, reused without re-proving it, states

\[
\mathcal V(F\Omega)-\mathcal V(\Omega)
\le-\frac{16869}{20000}\|b\|^2
\tag{A10}
\]

at exactly `ε=1/10, g=1/60, λ=1/300`, `k=(999/1000,1,1001/1000)`, on `0.9≤|Ω_i|≤1.1` and ordinary phase width at most `π/12`, with arbitrary common phase. Forward invariance and nonzero prestages persist there. Equality in monotonicity occurs exactly on the inherited aligned fixed circle. No profile was solved here. [POT_FINITE]

**Native verdict.** In the inspected native definitions, neither V nor I has an accompanying exterior reservoir, opening term, or reciprocal source-work debit. Potential decrease, intensity change, and a source-defined emitted amount remain different quantities. Equation (A10) is not an equation identifying where a loss goes. This is a scoped inventory of these definitions, not a no-go theorem for an eventual extension.

Even if one hypothetically imposed `Σ_(k,σ) Q_k^σ=Q≥0`, that would not determine six nonnegative outlet amounts. For `Q>0`, `(Q,0,0,0,0,0)` and `(0,Q,0,0,0,0)` have the same total; an interior allocation has five free scalar directions. For `Q=0` nonnegative amounts are all zero. No equality between Q and a native loss is adopted here. This conditional nonuniqueness is much narrower than a claim that geometry can never constrain transport.

### A.4 Existing C1 transport and its actual native input map

The paired-driving paper **does supply a conditional native-to-source map**. Choose its named input family `v_in=M_macro` or raw `C`, with the specified clock/configuration as applicable, and its fixed dictionary `A_reg=λ_g R_z(δ_g)`:

\[
W_{\rm reg}=A_{\rm reg}v_{\rm in},\qquad
q_\pm=n_\pm^T W_{\rm reg},\qquad f_\pm=\kappa_{\rm in}q_\pm.
\tag{A11}
\]

The positive conversion `κ_in` is source-strength gain, not energy efficiency. In the basis `(u,v,e_z)`,
`f_s=2κ_in W_r/√7`, `f_a=√3κ_in W_z/√7`; the azimuthal component `W_a` is lost. A common sample-and-hold bridge `f_σ(t)=Σ_j f_(σ,j) 1_[jΔt,(j+1)Δt)(t)` with symbolic `Δt>0` is an explicit conditional adoption, not a native physical clock. It and its gating belong to the existing comparison model; no forcing history is instantiated here. [C1_FOUNDATIONS eq:sourcechain, eq:sectors; C1_NATIVE]

On the selected periodic circle of length `L_c`, use the source's tent width `0<ε_c<η`, translated unit-integral profiles `b_±`, and forcing `g_c=b_+f_++b_-f_-`. With independently specified real preparation and independent speed `c>0`, C1 is

\[
p_t+c(r_c)_s=g_c,\qquad (r_c)_t+c p_s=0.
\tag{A12}
\]

Multiplication by `p,r_c` and addition proves

\[
\boxed{e_t+j_s=p g_c,\quad e=(p^2+r_c^2)/2,\quad j=cpr_c,\quad
\dot E=f_+y_++f_-y_-,\quad y_\pm=\int b_\pm p\,ds.}
\tag{A13}
\]

The spatial derivative integrates to zero on the periodic circle. The source proves well-posedness for periodic `H¹` preparation and continuous drives, the local distributional identity, and the integrated global balance for the weaker time-integrable forcing/mild-solution setting. The bound
`√E(t)≤√E(0)+(1/√(3ε_c))∫₀ᵗ ||f(u)||du` is also inherited. Source-off storage is conserved. None of these results depends on selecting an SI calibration. [C1_CARRIER thm:wellposed, thm:work]

In characteristic variables `w_±=(p±r_c)/√2`,

\[
e=\tfrac12(w_+^2+w_-^2),\qquad j=\tfrac c2(w_+^2-w_-^2),\qquad |j|\le ce.
\tag{A14}
\]

The signed source work depends on the response `y_±`, not just the magnitudes or squares of the inputs. It can remove as well as add storage. Linearity of the field does not make its quadratic storage additive: superposed responses have cross terms. Equations (A12)–(A14) genuinely express model-internal transport and work, with no new wave solution required.

The paper's native comparisons further distinguish fixed-clock macro drives from chiral drives and clock-generated input changes. From zero preparation, fixed-clock macro inputs give proportional real port histories and zero **spatially integrated** directional flux throughout the stated comparison; that is not a claim of zero local j. A clock-only change can produce a directional input determinant with a fixed native core. Its separate native chiral example establishes compatibility at its stated one-step scope, not a general history, a six-outlet law, or a native time scale. None of those examples was rerun. [C1_NATIVE]

**Conditional-carrier verdict.** C1 has an exact storage/work/flux law and an explicit one-way readout-to-drive interface. It has no reciprocal debit in F. As its paper expressly states, this is an open driven comparison system. One cannot identify `−ΔV`, `−ΔI`, or `||v_in||²` with `∫Σf_σ y_σ dt` without an additional relation and matching units/time intervals. Even with the same f, different allowed carrier preparations can produce different initial source work; the drive map alone therefore does not supply that relation. [C1_CARRIER lines 77–84; C1_LIMITS line 14]

### A.5 C6 reaches exterior observations, not an ambient energy debit

For an off-circle observer X, frame B, distance `d_X(s)=||X−Γ(s)||`, independent propagation speed `c_e>0`, and gain `g_o>0`, C6 defines

\[
U(X,t)=\frac{g_o}{4\pi}\int\frac{p(s,t-d_X(s)/c_e)}{d_X(s)}\,ds,\quad
V_{\rm ext}(X,t)=\frac{g_o}{4\pi}\int\frac{r_c(s,t-d_X(s)/c_e)\hat t(s)}{d_X(s)}\,ds,
\quad Y_X=(U,B^TV_{\rm ext}).
\tag{A15}
\]

This is a bounded causal history map with adopted straight-line delay, `1/d` weight, tangent encoding, and no screening or loading. The vector `r_c t̂` is not `j`, raw C, or an assigned material current. There is no feed-back to C1 or change to (A13). The source explicitly distinguishes three missing interfaces: reciprocal core exchange, ambient energy/source accounting, and receiver loading. Its formal outgoing line-source interpretation does not supply global near-source energy or self-force. Exterior records are a positive observation result; neither `E` nor `|U|²+||V_ext||²` is declared native physical energy. [C6_EXTERIOR eq:C6, thm:history; C1_LIMITS]

## B. Center, direction, and the six openings

### B.1 The geometric objects and labels

Use width-one geometry with spatial center `O=(0,r_g,0)`, `r_g=√3/6`. All coordinates below are centered at O until O is explicitly added. Set

\[
d_g=1-\sqrt2/2,\quad a_g=d_g/2,\quad h_g=(\sqrt2-1)/2,\quad H_0=1/2,
\]
\[
e_i=(\cos(-\pi/2+i\pi/3),\sin(-\pi/2+i\pi/3)),\quad
n_k^{\rm geom}=e_{2k},\quad g_k=e_{2k+1},\quad j_k=Jg_k,
\]

where J is the planar positive quarter-turn. For the static PLUS family,
`A_τ=Id−(τ/r_g)J=√(1+(τ/r_g)²)R_(−δ)`, `δ=atan(τ/r_g)`, `0≤τ≤h_g`.
The relevant vertices are

\[
T_i=(a_ge_i,h_g),\ B_i=(a_gA_\tau e_i,-h_g),\quad
U_k=(r_g n_k^{\rm geom},H_0),\ L_k=(r_gA_\tau n_k^{\rm geom},-H_0).
\]

The six actual central objects are the two-segment broken arcs

\[
\boxed{G_k^+=U_k\!\!\longrightarrow T_{2k+1}\!\!\longrightarrow U_{k+1},\qquad
G_k^-=L_k\!\!\longrightarrow B_{2k+1}\!\!\longrightarrow L_{k+1},\quad k=0,1,2.}
\tag{B1}
\]

Arrows in (B1) only list successive vertices; they do not orient an energy flow. Indices wrap cyclically. The upper label directions are `−30°,90°,210°`; lower directions are shifted by `−δ` in PLUS. MINUS reflects the complete geometry by `diag(−1,1,1)` without relabeling. No top chord, filled aperture, normal, centroid, or hinge is added to G. The refined central construction is an additional declared research geometry, not a consequence forced by the folded host. Its triangulated annulus has 18 vertices, 42 edges, 24 faces, and two boundary cycles, not a closed six-port control surface. [CENTRAL; FIXED_GAP]

The original close enclosing sphere has radius `sqrt(13/12−√2/2)` about O. It is a geometric reference, not a flux wall. It is not the extended-line sphere; the intended tight toroid remains separate. In the central slab the section complement is a connected annular region, not three isolated fluid channels. Constriction geometry alone supplies no density, pressure, velocity, or boundary condition. The support lines `O+R g_k` remain stationary. Static τ, native step index, common phase, observer clock, and carrier time remain distinct. Two co-present arrangements are not silently replaced by one rapidly alternating arrangement. [CENTRAL; PHASE_SPATIAL; WORK_ORDER]

### B.2 Mean, face vectors, and staged placement

The channel mean `m=(Ω_1+Ω_2+Ω_3)/3` is complex, not the spatial point O. Indeed `(L_NΩ)_i=3(m−Ω_i)` is a correction in the common channel plane. Summing the exact full step gives

\[
\Delta m=\frac\epsilon3\sum_i\Omega_i(k_i-s_i)
 +\frac13\sum_i\widetilde\Omega_i(e^{i\delta_i}-1).
\tag{B2}
\]

Only the direct graph sum cancels. With synchronization disabled, the first mean step has no explicit g term at fixed input, but subsequent nonlinear terms depend on the changed states. With synchronization enabled, the second term can depend on g through the prestage already in the first full step. Neither case justifies an inward path toward O. [MEAN]

The face decoder is `v_i=D_iΩ_i=Re(Ω_i)t_i+Im(Ω_i)e_z`, based at fixed panel center c_i, with endpoint `c_i+v_i`. Its raw length is `sqrt(s_i)`, not a travel distance. The source frames are

| i | c_i | t_i | face normal n_i |
| --- | --- | --- | --- |
| 1 | `(−1/4,√3/4,0)` | `(−1/2,−√3/2,0)` | `(−√3/2,1/2,0)` |
| 2 | `(0,0,0)` | `(1,0,0)` | `(0,−1,0)` |
| 3 | `(1/4,√3/4,0)` | `(−1/2,√3/2,0)` | `(√3/2,1/2,0)` |

Matched transport `T_ij=t_i t_jᵀ+e_z e_zᵀ` is an isometry between the two face tangent planes (rank two as an ambient map), giving `D_ij=||v_i−T_ijv_j||²`. The accepted spatial correspondence is `n_i=−g_(i−1)` and `c_i−O=r_g n_i`; hence the line `c_i+R n_i` equals `O+R g_(i−1)`. A pure phase rotation of Ω_i rotates v_i about this stationary line, with the directed-axis sign accounted for. The complete F also changes amplitudes and relative phases; it is not prescribed rigid material rotation or continuous travel along a rim. [FACE; PHASE_SPATIAL]

For staged Z write

\[
K=\lambda_{vp}\frac{\sqrt I}{1+\sqrt I},\quad E_o=e^{-\gamma t_o},\quad
H_\vartheta=\cos[3(\vartheta-\ell)](\cos\vartheta,\sin\vartheta,1),
\]
\[
Z=\alpha K E_o H_\vartheta+\beta C,\qquad X=O+\mu R_z(\psi)Z,
\quad\vartheta=2\pi(q\bmod N)/N.
\tag{B3}
\]

This placement explicitly assigns the base O, scale μ, yaw ψ, observer clock `(q,t_o)`, and configuration `λ_vp,γ,ℓ,α,β,N`. They are external to native F. The raw channel C used here is not replaced by its independently defined ambient attachment W. At fixed settings, Z varies with I and C but is invariant under native common phase. The ray `O+t(X−O), t≥0`, where used in the retained Z protocol, is a defined geometric test; no such ray is silently created from a face-based vector. [Z_METHODS; Z_OBSERVER; NRG_ATTACHMENT]

On the precise domain of (A10), the retained coordinates `y=(s_1,s_2,s_3,A_12,A_13)` determine full coherence and a representative z(y). The accepted reconstruction gives

\[
\Omega=u z(y),\quad (y,u)^+=(G(y),u\kappa(y)),\qquad
\Omega_n=u_0\prod_{j=0}^{n-1}\kappa(G^j y_0)\;z(G^ny_0).
\tag{B4}
\]

No history was evaluated here. The initial `u_0` is necessary to recover the actual common phase; it is not encoded by y. A common-phase change leaves the retained history and fixed-setting staged Z history identical, while rotating the nonzero decoded vectors in their own fixed planes. **Therefore, any proposed outlet rule that genuinely distinguishes those common phases cannot be a function of that staged Z history alone.** This is an exact conditional identifiability obstruction. It does not say every possible outlet rule must be phase-sensitive, and it does not imply absence of native evolution. V and its loss are also common-phase invariant. Adding u_0 restores the decoded mathematical vectors, not an unprovided flux relation. [POT_COORDINATES; POT_RETENTION; PHASE_RECON; PHASE_OBS]

The EMA case must stay separate: its innovation uses `J_cubic=Im(Ω_1 conj(Ω_2)Ω_3)=Im[u z_1 conj(z_2)z_3]`. Memory advancement combines prior memory with the normalized innovation `J_cubic/(1+|J_cubic|)` using the source's literal `0.01`. An observation from **current** memory uses current I, C, that memory, and the external settings; it neither evaluates the cubic nor advances memory. No EMA or observer was advanced here. [Z_OBSERVER lines 226–265; PHASE_OBS]

The published universal proper-rotation obstruction concerns one rotation acting on every admitted vector triple. It neither prohibits transport nor proves emission; the positive stationary-axis correspondence also proves no emission claim. [PHASE_ROTATION]

### B.3 Retained Z evidence: movement, incidence, and labels

The following are prior results, not new measurements or a rerun. Z01 uses two saved binary64 states with `(ε,g,λ)=(0.05,0.2,0.001)`, `k=(1,1,1)`. Z02 and Z03 use the same five selected states from the 120-digit producer with `(0.1,0.2,0.17)`, `k=(2,3,4)`. These are constructed examples, not representative native sampling; the theorem (A10) is not transferred to them. [Z_METHODS; Z01; Z02; Z03]

* Z01's frozen points have nearest label `G_0^+`; its second scheduled observation instead has nearest label `G_1^+`. In Z02 all five frozen labels are `G_0^+`; scheduled labels are `G_0^+,G_0^+,G_2^−,G_0^−,G_1^+`. In the documented replacement accounting, all three scheduled switches occur at the clock replacement. That is evidence about the saved window and chosen replacement order, not a theorem that all label changes are observer-made.
* All primary placed points in those reports lie inside the original sphere and off both the broken boundaries G and finite host-notch patches N. Z01 has no forward-ray finite-patch hit; Z02 has one admitted hit of `N_0^+` by the defined ray for frozen F1. The point F1 itself does not belong to N. No carrier flux or path segment was inferred from that ray.
* A nearest label is not approach: in Z02, F1→F2 retains `G_0^+` while radius decreases approximately `0.247125→0.229832` and distance to that boundary increases `0.036974→0.060604`.
* Z03 closes the four frozen displacement budgets using native intensity and area terms with its stated numerical residual qualifications. On 2→3, retained `ΔI≈+0.00754918` accompanies `Δradius≈−0.000590475`. The finite square is essential to the positive intensity sign. On 3→4, radius increases approximately `0.00780087` while height still decreases approximately `0.00120391`; its positive macro-size contribution to squared radius exceeds negative chiral-size and cross contributions.

These observations establish actual changes of the specified readout, including an outward radial endpoint change in the saved window. They do not establish energy leaving a region. Signed displacement contributions can cancel; coordinate increase is not signed power. The native/envelope/clock telescope uses comparison replacements, not intermediate native times, continuous paths, passage events, or speeds. [Z01 lines 147–186; Z02 lines 99–221; Z03 lines 21–90]

### B.4 The host-notch correspondence and a conditional outward balance

The fixed host-notch patches are, in centered coordinates,

\[
N_k^\sigma(\lambda,\zeta)=
 (2r_g-\tfrac{\sqrt3}2d_g\lambda)g_k+\zeta j_k
 +\sigma(h_g+d_g\lambda)e_z,\quad
0\le\lambda\le1,\quad |\zeta|\le d_g\lambda/2.
\tag{B5}
\]

This λ is a triangle coordinate, not native synchronization strength. In Paper I the corresponding triangles are `Δ_j^σ=O+(r_0−c_gd_gt)u_j+ξv_j+σ(h_g+d_gt)e_z`, with `r_0=1/√3`, `c_g=√3/2`, `u_j=R_z(2πj/3)(0,1,0)`, `v_j=e_z×u_j`. Direct substitution gives the exact dictionary

\[
u_0=g_1,\quad u_1=g_2,\quad u_2=g_0,\qquad
\boxed{\Delta_j^\sigma-O=N_{(j+1)\bmod3}^\sigma.}
\tag{B6}
\]

Thus the host-notch objects in the two source routes are recognizably the same patches, with a cyclic label shift. Their normals are `n_j^σ=(2u_j+σ√3e_z)/√7`. Paper I's tip-first vertex IDs are P0 upper `(7,6,16)`, lower `(0,15,1)`; P1 upper `(4,13,5)`, lower `(3,2,8)`; P2 upper `(11,17,12)`, lower `(10,9,14)`. Two sides are material rim edges; the third is a measurement-only closure. These are not material caps or six boundary components. Equation (B6), checked in symbolic group 8, does **not** identify N with G. [CENTRAL; FIXED_GAP; PAIRED_GEOMETRY eq:triangles, eq:planes]

The retained fixed-gap result already distinguishes central fans/opening arcs from these host patches. Every broken arc contains its ring elbow, whose squared radius is at most `15/2−21√2/4`, while every host-notch plane has squared distance from O at least `19/84+√2/14`, a strictly larger value. A rotation about O preserves that elbow's radius, so it cannot put the entire broken arc in a host patch. The upper bound is on the ring elbow, not on every point of the arc; possible fan-tip contacts do not remove the obstruction. This specific obstruction is inherited, not recomputed, and is not a universal obstruction to any future transport registration. [FIXED_GAP; FIXED_GAP_REVIEW]

Paper II selects `u=u_0`, hence the **N_1 pair**, not central G_1. Put

\[
K_c=\frac{\sqrt3}{12}+\frac{\sqrt6}{4},\quad
a_c=\frac{K_c}{1+\sqrt3/2},\quad R_c=\frac{\sqrt7a_c}{2},\quad L_c=2\pi R_c,
\]
\[
\Gamma(s)=O+K_cu+R_c(\cos\chi\,u+\sin\chi\,e_z),\quad
\hat t=-\sin\chi\,u+\cos\chi\,e_z,\quad\chi=s/R_c.
\tag{B7}
\]

The contact points are `P_±=O+a_cu±a_ce_z`, in the relative interiors of the finite patches. With `θ=atan(2/√3)` and `η=R_cθ`, their arclengths are `s_+=L_c/2−η`, `s_−=L_c/2+η`. They are not antipodal. The circle is offset from O and is an additional centerline, not a material edge or an identification with the intended tight toroid. The inherited finite-crossing theorem gives

\[
\hat t(s_+)=-n_+,\qquad\hat t(s_-)=+n_-.
\tag{B8}
\]

The normal signs are outward from the O-side half-spaces: `n_±·(P_±−O)=a_c(2+√3)/√7>0`. Each candidate circle crosses only its own pair of finite patches and avoids the other four; the three geometric candidate circles are disjoint, and no planar circle contains all six selected contacts. Those geometric candidates do not instantiate three carriers or their coupling. [PAIRED_GEOMETRY thm:circle, thm:clearance; C1_FOUNDATIONS eq:circle, eq:contacts, eq:arcs]

**New conditional consequence of existing definitions.** At the stated `H¹` carrier regularity, point traces exist. Define signed carrier cut powers at those already registered crossings by projecting oriented j onto their already specified normals:

\[
\boxed{P_{\rm out,+}=j(s_+,t)\hat t(s_+)\cdot n_+=-j(s_+,t),\qquad
P_{\rm out,-}=j(s_-,t)\hat t(s_-)\cdot n_-=+j(s_-,t).}
\tag{B9}
\]

These are one-dimensional cut powers; they are not a two-dimensional density integrated over a filled central aperture. Integrating the local balance (A13) on the short arc `[s_+,s_−]` gives

\[
\boxed{\frac{d}{dt}\int_{s_+}^{s_-}e\,ds
=\int_{s_+}^{s_-}p g_c\,ds+j(s_+,t)-j(s_-,t)
=\int_{s_+}^{s_-}p g_c\,ds-P_{\rm out,+}-P_{\rm out,-}.}
\tag{B10}
\]

The identity is justified by the source's regularity and weak product rule (or its integrated-in-time form); no point-flux assertion is extended here to arbitrary spatial `L²` data. The finite-width source tents straddle the contacts, so the work restricted to this arc is generally not the whole `f_+y_++f_-y_-`. Symbolic group 7 checks the normal and balance signs.

Equations (B9)–(B10) are the strongest supported balance-and-direction statement at the inspected interface. Positive j means incoming crossing at the upper contact and outgoing crossing at the lower; negative j reverses that direction locally. The fluxes at the two contacts need not have the same sign or value at a given time. Stored fields and distributed work determine them. Geometric labels do not select either sign, and the periodic carrier does not escape or reflect at its source ports: its characteristics continue around the circle.

The source labels an inner and an outer arc midpoint, but these are locations, not proof of a globally inward then outward trajectory from O. Even the source's frozen macro reference that touches an upper contact has tangent `a_c v_j`, tangent to the patch plane, whereas Γ crosses normally. Shared contact does not establish a shared path. Nothing here chooses a “next available” central opening. [C1_CARRIER eq:characteristics and support discussion; PAIRED_GEOMETRY sec:grazing]

### B.5 Dependency table and remaining interfaces

| Link needed for the question | Status | Established content / smallest missing relationship |
| --- | --- | --- |
| Native Ω → changes of s_i and I | **Established, general algebra** | (A2)–(A5), with full finite square and cycle freedom. No exterior destination follows. |
| Native Ω → V loss | **Established on specified domain** | (A7)–(A10); no recipient or equality to emitted work is defined. |
| Coherence history → actual phase-sensitive face vectors | **Established with initial phase** | (B4) and decoder; `u_0` is needed if only y is supplied. A face-vector-to-transfer relation is still absent. |
| Native state + external settings → placed Z and source-defined ray | **Established readout/geometry** | (B3), retained incidence predicates; nearest label and ray incidence are not passage or flux. |
| Fixed staged Z history → common-phase-dependent outlet | **Underdetermined if outlet truly depends on common phase** | Distinct `u_0` give identical Z histories. Phase-sensitive data must be retained; a flux rule is still required. |
| Named native readout → two C1 source strengths | **Existing conditional connection** | (A11), adopted gain/dictionary and time bridge; loses one projected component. No need to invent this map. |
| C1 sources/preparation → storage and signed flux | **Existing conditional connection** | (A12)–(A14), genuine work and propagation; not part of unchanged native F. |
| C1 j → signed crossing of its finite host-notch pair | **Conditional exact composition** | (B6)–(B10), with traces and normal signs; selected pair is N_1 under central notch labels. |
| Host-notch crossing → passage through a central G_k^σ | **Absent from inspected definitions** | N and G differ; (B6) resolves only the host-patch dictionary. Need a declared transfer registration to G, not renamed patches or an invented closure. |
| Native loss → C1 work → six central outlet amounts | **Absent from inspected definitions** | Need a reciprocal native debit and six named transfer functionals with outward conventions and a matching balance. One total alone cannot select six amounts. |
| Carrier history → exterior records | **Existing conditional connection** | C6 (A15) is causal and bounded; ambient energy debit and receiving load remain unassigned. |

**Geometry verdict and closure.** The six central boundaries, stationary support axes, phase reconstruction, and retained point/ray observations are well-defined at their respective scopes. The C1 host-patch crossings add real conditional transport mathematics. Their combination presently stops at two distinct interfaces: native amount to reciprocal carrier work, and host-patch carrier cuts to the six central broken boundaries. A direct native-to-six-outlet model would instead need a declared six-component transfer observable tied to a named native balance. These are precise missing equations/assignments, not requests to invent a full new physics programme.

This completes the requested assessment without a further author interview: the remaining definitions can be discussed with this concrete distinction in hand. No aperture, outlet selection, density, forcing schedule, boundary condition, physical time scale, material attachment, or successor investigation has been adopted.

## Evidence and verification boundary

New results are the independent accounting derivation, the elementary cycle and six-total nonuniqueness arguments, the host-notch label dictionary, the conditional cut-power/arc balance, and the phase-sensitive outlet identifiability consequence. Inherited theorems and retained numerical measurements are identified above. The new standalone helper checked **29 exact residuals in nine groups** using generic symbols only; these checks do not re-prove the inherited continuous-domain theorems or establish physical interpretations. All defining sources were locally available. The ledger and preparation report record the actual focused input hashes and after-reading preservation check; no whole-repository verification is claimed.
