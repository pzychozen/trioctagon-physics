# GM05 — Native moment to loop circulation

20 November 2026. Local assessment returned for author and GPT review. GM04 remains the accepted baseline; the conclusions below about the new jump are conditional results, not adoption of a physical source law.

**Verdict.** The specified uniform jump can launch the required signed circulation from the empty Fourier preparation. On Paper G's moment plane, the three-loop target has a unique minimum-storage solution for equal lengths and equal storage weights. The increment rule preserves that solution if it was already matched. It preserves initial errors as well, and does not correct changes of W during intervening exchange. Its work is explicit and signed. No inherited equation inspected here supplies that extra jump work from an identified internal donor.

## 1. Premises and source boundary

[SOURCE_MAP.md](SOURCE_MAP.md) gives exact labels, line locators, saved primary files and their commit-pinned identities. [SOURCE_VERIFICATION.json](SOURCE_VERIFICATION.json) records all 24 primary sources. The complete accepted [GM04 derivation](inputs/GM04_accepted/GM04_DERIVATIONS.md) and its original archive are preserved unchanged. The [GM04 acceptance review](inputs/order/GM04_GPT_REVIEW.md) accepts that derivation, not the new GM05 source hypothesis.

The installed atlas was consulted through the geometry/chirality, carrier/exchange, physical-interpretation and energy routes. The audit includes C1/C6, paired driving, RX exchange and native jumps, WT loaded transport, cadence accounts, capacity and the kernel's passive source accounts. The atlas predates GM01–GM04, so those local accepted records were read directly. The absence finding below is about this inspected chain of equations; it is not a claim that every possible extension has been excluded.

Paper G defines

\[
C=\Re\Omega\times\Im\Omega,\qquad W=TC,\qquad
T=\begin{pmatrix}
-1/2&1&-1/2\\
-\sqrt3/2&0&\sqrt3/2\\
0&0&0
\end{pmatrix}. \tag{1}
\]

Thus W lies in the horizontal plane. C is a channel-space area and W its specified ambient axial attachment. Neither is yet a calibrated physical magnetic moment. Native step number is not a physical time.

For the retained periodic C1 carrier, and also for RX during exchange,

\[
p_t+c(r_c)_s=g_c,\qquad (r_c)_t+cp_s=0,\qquad
j=L^{-1}\int_0^Lr_c\,ds,\qquad \dot j=0. \tag{2}
\]

The native-first RX jump changes only the native state, leaving the carrier and receiver unchanged. Hence this mean is also preserved across every inherited native jump. This is valid for periodic H1 solutions by integration and for L2 mild solutions by the bounded mean functional. It does not say that the whole carrier or its exterior observation vanishes.

For a circle of radius a and oriented normal nu, GM04 (16) gives the centered moment of any profile:

\[
m_c=\frac12\int(\gamma-Y)\times(r_c\widehat t)\,ds
=\pi a^2j\,\nu. \tag{3}
\]

The existing port law is \(f=KC\), with

\[
K=\kappa_{\rm in}\lambda_g
\begin{pmatrix}n_+^T\\n_-^T\end{pmatrix}R_z(\delta_g),
\qquad n_\pm=(2e_y\pm\sqrt3e_z)/\sqrt7.
\]

It loses \(v=(\cos\delta_g,-\sin\delta_g,0)^T\), whereas

\[
Kv=0,\qquad
Tv=(-\tfrac12\cos\delta_g-\sin\delta_g,
-\tfrac{\sqrt3}{2}\cos\delta_g,0)^T,\qquad
|Tv|^2=1+\tfrac12\sin(2\delta_g)\ge\tfrac12. \tag{4}
\]

Therefore no instantaneous function of the two old port values can reproduce W for all native states. Even a prescribed native history cannot fix the freely preparable mean in C1/RX: adding a constant to r leaves the old native/receiver dynamics unchanged.

WT has a different, loaded mean equation. With M the total length of its receiving arcs and b_r the actual incoming backward wave component, GM04 (24) gives

\[
L\dot j=-\kappa^2Lj+
\frac{\sqrt2\kappa}{\sqrt M}
\int_{S_L\times G} b_r(s,X,t)\,ds\,d\ell_X. \tag{5}
\]

This allows a mean change driven by returning waves; it is not a universal assignment from W. For entirely empty transport and receiving preparation, the incoming return is zero before \(2\theta_-\), and the initially zero mean remains zero there, including native jumps. Nonempty backward histories or receivers give different returns. At \(\kappa=0\), (5) reduces to (2). The WT native jump still leaves all carrier and transport stocks unchanged. Thus neither the invariant C1/RX law nor the history-dependent WT law supplies the proposed instantaneous W-to-mean source.

The retained circle in the published orientation has normal \(e_x\). A single signed mean can represent \(Tj=\alpha W\) only for W parallel to \(e_x\), when \(\alpha\ne0\). A transported version has the corresponding transported normal. Its fixed direction cannot span Paper G's entire moment plane.

## 2. Three equal circles and the minimum-storage lift

The hypothesis instantiates three simultaneous carrier states on the three allowed geometric circles. Existing geometry supplies their centers, radius and oriented normals, but does not itself instantiate those three dynamical carriers or select their actuation.

In the published frame, put

\[
u_k=R_z(2\pi k/3)e_y,\quad
\nu_k=u_k\times e_z,\quad
Y_k=O+wK_cu_k,\quad
K_c=\frac{\sqrt3}{12}+\frac{\sqrt6}{4},\quad
a=\frac{w\sqrt7K_c}{2(1+\sqrt3/2)},\quad L=2\pi a. \tag{6}
\]

Here w is the common host width and a the circle radius. The centers are distinct and are not O. The order of the means is A on circle 2, B on circle 0, C on circle 1. Consequently

\[
T=[\,\nu_2\ \nu_0\ \nu_1\,].
\]

Let \(e=(1,1,1)^T\), \(P=I-ee^T/3\) and \(\Pi=\operatorname{diag}(1,1,0)\). Direct multiplication gives

\[
D=\tfrac23T^T,\qquad TD=\Pi,\qquad DT=P,\qquad
D^TD=\tfrac23\Pi,\qquad \ker T=\mathbb Re. \tag{7}
\]

In particular, \(TDW=W\) on the moment plane, not on all of three-space.

The full family satisfying \(Tj=\alpha W\) is

\[
j=\alpha DW+\beta e=\alpha PC+\beta e,\qquad \beta\in\mathbb R. \tag{8}
\]

Existence follows from (7); exhaustiveness follows by subtracting a solution and using the kernel. The scale \(\alpha\) is real and symbolic, with units of loop mean per unit W: \(\mathrm U/\mathrm A^2\) if the native amplitude has unit A. It is distinct from RX's positive native-storage scale \(\alpha_N\). Positive alpha aligns the aggregate moment with W; negative alpha reverses it; alpha zero gives no moment response.

For independent equal carrier storage weights, the mean part of the energy is

\[
E_{\rm means}=\frac L2|j|^2
=\frac{L\alpha^2}{3}|W|^2+\frac{3L}{2}\beta^2. \tag{9}
\]

The two components are orthogonal because \(e^TD=0\). Since \(L>0\), there is a unique minimum at beta zero:

\[
\boxed{
j_*=\alpha DW=\frac{\alpha}{3}
(-W_x-\sqrt3W_y,\ 2W_x,\ -W_x+\sqrt3W_y)^T.} \tag{10}
\]

If \(r_i(s)=j_i+\widetilde r_i(s)\), with zero-mean tilde profiles, the carrier energy splits into (9) and \(\frac12\sum_i\int(p_i^2+\widetilde r_i^2)\,ds\). Thus (10) is the minimum over means for fixed other profiles. With all profiles free as well, p and tilde r must also vanish for the total carrier minimum. Unequal lengths or storage weights change the minimization problem.

The aggregate of the centered circular moments is \(\pi a^2Tj\). This equals the ordinary leading dipole moment of the steady constant profiles used below. For arbitrary nonuniform profiles it is not by itself a complete field description. In particular,

\[
m_O=\pi a^2Tj+\frac12\sum_i(Y_i-O)\times J_{0i},
\qquad J_{0i}=\int r_i\widehat t_i\,ds. \tag{11}
\]

For constant profiles \(J_{0i}=0\). For a circle with
\(\rho=a(\cos\chi\,e_y+\sin\chi\,e_z)\), center \(be_y\) and profile \(\cos\chi\), the centered moment is zero but \(J_0=\pi ae_z\) and \(m_O=\pi ab e_x/2\). Nonuniform profiles may also have the \(1/r\) vector-observation term of GM04 (19). No general dipole-only claim follows from their means.

## 3. The jump, initialization and tracking limits

Alongside the ordinary native update, impose the new actuation

\[
\Delta j=\alpha D(W^+-W^-),\qquad
r_i^+(s)=r_i^-(s)+\Delta j_i,\qquad p_i^+=p_i^- . \tag{12}
\]

This is a finite jump in the carrier, absent from both the old C1 equation and the old hybrid prescription. It uses native W before and after the update, including information lost by the old KC ports. It is spatially uniform, simultaneous on the three loops, and requires a registered native jump event. No causal mechanism implementing that synchronization or physical clock is derived here.

For every square-integrable preprofile, (12) changes its mean by exactly delta j and preserves its zero-mean part. The affine map is well-defined in the carrier energy space. A finite prescribed sequence of finite native states gives finite jumps; this is not a global theorem for a newly chosen three-loop reciprocal-feedback system, which has not been specified.

Define the vector mismatch \(q=j-\alpha DW\) and the visible mismatch \(\varepsilon=Tj-\alpha W\). Then exactly at each jump,

\[
q^+=q^-,\qquad \varepsilon^+=\varepsilon^-,\qquad
e^Tj^+=e^Tj^-. \tag{13}
\]

Consequently:

* Correct minimum initialization \(j^-=\alpha DW^-\) propagates to the correct minimum endpoint.
* A matched common offset \(j^-=\alpha DW^-+\beta e\) remains matched but retains the extra \(3L\beta^2/2\) storage.
* Any nonzero visible mismatch persists. Empty carriers are correctly initialized only if \(\alpha W^-=0\).
* The rule minimizes the norm of the increment among increments with the required visible change. It does not minimize the final storage for arbitrary initial data.

A reset to the minimum target would require

\[
\Delta j_{\rm reset}=\alpha D(W^+-W^-)-q^- . \tag{14}
\]

That is a different source law. Removing a common offset would additionally extract \(3L\beta^2/2\) of stored mean energy. The proposed increment does neither.

For a pure discrete native evolution, held constant between updates, and independent source-off C1 carriers, the means and W remain fixed on each plateau; matched initialization therefore gives tracking on all plateaus and at their jump endpoints. Active RX exchange instead changes the native state continuously while preserving the loop mean. WT can change both by its independent history-dependent law (5). Neither evolution is constrained to preserve \(Tj=\alpha W\).

There is an exact RX witness. Take unit geometric/input gains, yaw zero, native real and imaginary vectors \(a_N=e_3,b_N=e_1\), and old port output \(y=(1,1)^T\). The actual RX equation gives, for \(\mu=\eta_N/(2\alpha_N)>0\),

\[
K^Ty=\frac4{\sqrt7}e_2,\quad
\dot a_N=\mu(K^Ty)\times b_N=-\frac{4\mu}{\sqrt7}e_3,\quad
\dot b_N=-\mu(K^Ty)\times a_N=-\frac{4\mu}{\sqrt7}e_1.
\]

Thus \(C=e_2,\ W=e_x\), and

\[
\dot W=-\frac{8\mu}{\sqrt7}e_x\ne0. \tag{15}
\]

The required y is attainable with the retained disjoint equal tents:
\(p=(b_++b_-)/\|b_+\|_2^2\), an H1 periodic profile. Meanwhile \(\dot j=0\). This exhibits actual between-jump evolution allowed by RX; it is not a claim to have defined three new reciprocal ports. A subsequent application of (12) preserves the accumulated error in (13), rather than repairing it. The candidate tracks the jump contribution to W, not unobserved intervening evolution.

## 4. Exact launch and other controls

### Fourier launch from empty carriers

Use the same unnormalized native preparation and parameter tuple as accepted GM04 (18):

\[
\Omega^-=(1,\omega,\omega^2),\quad\omega=e^{-2\pi i/3},\quad
\epsilon=\frac1{10},\quad g=\frac1{60},\quad\lambda=\frac1{300},
\quad k=(999/1000,1,1001/1000).
\]

The exact ordinary native step, not an interpolating surrogate, gives

\[
\Omega_i^+=\frac{(9499,9500,9501)_i}{10000}\Omega_i^-,
\quad W^-=0,\quad
W^+=\left(\frac{\sqrt3}{200000000},\frac{57}{400000},0\right)^T. \tag{16}
\]

All three prestage factors are positive, so phases are unchanged at that stage, and the triple-angle phase kicks vanish exactly. Empty pre-carriers \(p_i^-=r_i^-=0\) are matched to \(W^-=0\). Equation (12) therefore launches

\[
\boxed{
j^+=\frac{\alpha\sqrt3}{600000000}
(-28501,\ 2,\ 28499)^T,\qquad
m_{\rm tot}=\pi a^2\alpha
\left(\frac{\sqrt3}{200000000},\frac{57}{400000},0\right)^T.} \tag{17}
\]

For positive alpha, circulation on A/circle 2 is negative, on B/circle 0 is positive and very small, and on C/circle 1 is positive. These are signed oriented means, not negative energies. The aggregate direction is almost positive y with a small positive x component, in the published frame (6). In particular, it cannot be represented by the retained x-normal circle alone.

At the immediate endpoint each profile is constant and p is zero. This is a steady source-off C1 preparation if the old drives and loading are then off and the native state is held. The ordinary RX source need not be off for this Fourier state, so the steady endpoint is a specified comparison, not a theorem about subsequent active exchange.

### Zero change, reversal and common offset

If \(\Delta W=0\), (12) gives zero increment and zero jump work; an initial mismatch remains. Reversing two matched target endpoints, \(W^+=-W^-\), gives \(j^+=-j^-\) and \(\Delta j=-2j^-\). Their mean energies agree, so the net storage work is zero. These arbitrary reversed endpoints are an algebraic control and are not asserted to be adjacent under native F. Zero net storage change also does not prove an actuator has zero physical cost. Removing a matched mean to W zero extracts its stored mean energy.

There is a native realization of the sign control: the conjugate Fourier preparation follows the conjugate native update. It produces \(-W^+\) and \(-j^+\) with the same positive launch work.

Adding \(\beta e\) to any matched means leaves \(Tj\) unchanged, costs \(3L\beta^2/2\), and survives every increment. It can change the spatial field of the three separated circles, despite leaving the leading aggregate moment unchanged. For example its constant-loop field has a nonzero singular contribution near an arc unique to one circle; the other two fields are smooth there and cannot cancel that contribution. Aggregate cancellation is not equality of all near fields.

### Equal old ports and opposite native moments

Let \(v\) be as in (4), and choose real channel vectors \(x=e_3,\ y=v\times e_3\). The two physical inputs for this algebraic test are

\[
\Omega_\pm=x\pm iy,\quad I_\pm=2,\quad C_\pm=\pm v,\quad
KC_\pm=0,\quad W_\pm=\pm Tv\ne0. \tag{18}
\]

Their minimum target initializations are opposite:

\[
j_{\pm,*}=\pm\alpha Pv,\qquad
E_{\pm,*}=\frac{L\alpha^2}{3}
\left(1+\frac12\sin2\delta_g\right). \tag{19}
\]

At yaw zero these are
\(j_{\pm,*}=\pm\alpha(2/3,-1/3,-1/3)^T\),
with \(W_\pm=\pm(-1/2,-\sqrt3/2,0)^T\) and energy \(L\alpha^2/3\).
This tests information access: the new W channel distinguishes what the old ports do not.

It does not create a free initialization. If an empty carrier is paired with either fixed nonzero W and no change of W occurs, the increment is zero and the target remains unmatched. The absolute initialization in (19) needs its own supplied actuation and work. If a genuine transition has specified \(\Delta W\), (12) uses that change. The two states in (18) are not asserted to be adjacent native iterates, and equal ports at one instant do not imply equal port histories under subsequent native updates.

## 5. Field at the prepared endpoint and required history

For the steady constant endpoint, linear superposition of the three retained C6 comparison kernels gives

\[
V(X)=\frac{g_o}{4\pi}\sum_i j_i\oint_{\Gamma_i}
\frac{d\gamma_i}{|X-\gamma_i|},\qquad H=\nabla_X\times V.
\]

By accepted GM04 (14)–(15), each loop contributes the finite-radius curl with leading moment \(\pi a^2j_i\nu_i\). About the common origin, as \(X=O+rn\) with \(r\to\infty\),

\[
H(O+rn)=\frac{g_o}{4\pi r^3}
\{3n(n\cdot m_{\rm tot})-m_{\rm tot}\}+O(r^{-4}),\quad
m_{\rm tot}=\pi a^2Tj. \tag{20}
\]

The error is uniform in n for the fixed geometry and finite means. To see the order, put \(b=wK_c\) and
\(G(R)=\operatorname{Hess}(|R|^{-1})=(3nn^T-I)/|R|^3\).
Its derivative is bounded by a constant times \(|R|^{-4}\), so translating a dipole center by \(Y_i-O\) changes G by \(O(b/(r-b)^4)\). The centered finite-radius remainder is \(O(a^4/(r-b-a)^5)\) for \(r>b+a\). The finite sum proves (20). The individual centered \(O(r^{-5})\) error in GM04 must not be transferred unchanged to O: these circles have distinct centers, so a common-origin \(r^{-4}\) correction can remain.

For the Fourier launch, substituting (17) gives the signed dipole angular pattern and inverse-cube leading falloff in the expected frame. No SI normalization, Lorentz force or second-triad sensing rule is inferred. H is the curl of the existing vector observation; it is not itself the published receiver variable. The sensing link is outside this work order.

The delay history matters. Suppose the carriers are zero before the prescribed jump at \(t_0\) and held at their constant post-jump profiles thereafter. This piecewise history requires the new source at the jump; it is not a free C1 solution across \(t_0\). At a fixed off-wire observation point define

\[
\tau_{\max}(X)=\max_{i,s}\frac{|X-\gamma_i(s)|}{c_e},
\qquad \tau_{\min}(X)=\min_{i,s}\frac{|X-\gamma_i(s)|}{c_e}.
\]

For \(t<t_0+\tau_{\min}(X)\) the retarded output is still zero. For
\(t>t_0+\tau_{\max}(X)\), all contributing delays, and those in a sufficiently small neighborhood of X, see the constant endpoint; its observed vector field and its spatial curl equal the static expressions above. The strict inequality permits differentiation in that neighborhood without crossing a wavefront. In the intervening window the actual retarded step history must be used, with possible front singularities in differentiated quantities. There is no instantaneous all-space static field. Active later drives or loading require their actual histories instead.

## 6. Symmetry and physically distinct choices

For an orthogonal change of spatial frame Q, oriented normals and W are axial:
\(T'=(\det Q)QT\) and \(W'=(\det Q)QW\).
With \(D'=\frac23T'^T\), one has \(D'W'=DW\). Thus the signed scalar means are invariant under the properly transported frame; treating mirror normals or W as polar vectors would give a spurious sign. This includes the GM04 mirror control. Cyclic relabeling permutes the means consistently with its rotation of the normals.

The minimum-energy criterion selects beta zero from (8), independently of symmetry. If a W-only assignment is additionally required to be real-linear and equivariant under the specified threefold rotation, its only extra kernel term would be \(e\ell(W)\), with a linear functional satisfying \(\ell(R_{2\pi/3}W)=\ell(W)\). There is no nonzero invariant linear functional on this plane, so that extra term vanishes.

Symmetry alone, without linearity or minimization, is weaker. For example
\(\beta(W)=b_3(W_x^3-3W_xW_y^2)\), with an appropriate dimensionful coefficient \(b_3\), is invariant under the threefold rotation, odd under W reversal and the horizontal-plane mirror's axial action, and even under the axial action \(W_y\mapsto-W_y\) of the x-reflection. It gives a nonzero common mode at some W while obeying those discrete symmetries. Its extra positive storage excludes it from the minimum member.

There is also a simple linear C-based alternative,

\[
j_{\rm raw}=\alpha C,\qquad j_*=\alpha PC,\qquad
j_{\rm raw}-j_*=\frac{\alpha\Gamma}{3}e,\quad
\Gamma=e^TC,\qquad
E_{\rm raw}-E_*=\frac{L\alpha^2\Gamma^2}{6}. \tag{21}
\]

Both give \(Tj=\alpha W\), but the raw assignment uses channel information erased by W. For the Fourier entrance, \(C=-(\sqrt3/2)e\) and W is zero. The minimum assignment is empty; the raw assignment has three equal nonzero oriented circulations and mean storage \(9L\alpha^2/8\). Its leading aggregate dipole cancels, but its near field and stored energy do not equal those of the empty preparation. Following that raw assignment over changes of Gamma would need an additional common increment \(\alpha\Delta\Gamma\,e/3\), absent from (12).

Thus the stated equal-storage minimum selects a definite mathematical construction. The simultaneous three carriers, their geometric registration, the equal weights, the source scale/sign, initialization and physical actuation remain modeling choices. The comparison above makes the alternatives concrete without silently adopting one as a new physical law or asking for an additional research task.

## 7. Exact work and the missing payer

The inherited carrier normalization is
\(E_C=\frac12\sum_i\int(p_i^2+r_i^2)\,ds\).
For arbitrary L2 preprofiles and the uniform jump (12), direct expansion gives

\[
\boxed{
\Delta E_C=L\left(j^-\cdot\Delta j+\frac12|\Delta j|^2\right)
=L\left(\frac{j^-+j^+}{2}\right)\cdot\Delta j.} \tag{22}
\]

This is a Hilbert-space quadratic identity; no smoothness in s or time integration convention is needed. The factor one-half in the squared jump is essential. Since p is unchanged and the tilde profiles are unchanged, they contribute no jump energy.

For matched minimum endpoints it reduces to

\[
E_{\rm means}=\frac{L\alpha^2}{3}|W|^2,\qquad
\Delta E_C=\frac{L\alpha^2}{3}
\left(|W^+|^2-|W^-|^2\right). \tag{23}
\]

The same work difference holds with a fixed matched common offset. For a general vector mismatch \(q^-=j^--\alpha DW^-\), the exact correction is

\[
\Delta E_C=\frac{L\alpha^2}{3}
\left(|W^+|^2-|W^-|^2\right)
+L\alpha q^-\cdot D(W^+-W^-). \tag{24}
\]

Therefore W endpoints alone do not determine the work for arbitrary carrier preparation.

For the empty Fourier launch (16)–(17),

\[
|W^+|^2=\frac{812250003}{40000000000000000},\qquad
\boxed{\Delta E_C=
\frac{270750001}{40000000000000000}L\alpha^2
=6.768750025\times10^{-9}L\alpha^2.} \tag{25}
\]

This is strictly positive when \(\alpha\ne0\). It must be supplied to the carrier by the added source actuation. General (22) can be negative, in which case the actuation receives energy from the carrier. The units are the inherited mathematical \(\mathrm U^2\mathrm L\); no conversion to joules is established.

**No inherited payer is identified.** C1/RX drives the p equation, not a uniform r impulse. RX's collocated exchange has its own continuous cancellation between native, carrier and receiver stocks. Its hybrid jump changes only x, with the explicitly recorded native source \(\alpha_N\Delta I/2\). WT adds loaded transport storage and a continuous exchange balance but likewise leaves those stocks unchanged at the ordinary native jump. The kernel's signed source entries and cadence's source/receiver budgets record changes; they do not actuate this new mean increment. Capacity bounds are not donor dynamics.

If (12) is appended while all other non-native stocks remain unchanged, the old hybrid account instead changes by

\[
\Delta H_{\rm total}=\frac{\alpha_N}{2}\Delta I+\Delta E_C. \tag{26}
\]

There is no identity making this zero. In the Fourier control,
\(\Delta I=-14624999/50000000\), hence the native trial-storage change is
\(-14624999\alpha_N/100000000\). It is not identically the negative of (25). Choosing a scale to match one preparation would not define a universal transfer law.

The same native tuple at the aligned real state \(\Omega=(1,1,1)\) is a sharper check. It gives
\(F(\Omega)=(9999/10000,1,10001/10000)\), with W zero at both endpoints and
\(\Delta I=1/50000000\). The candidate carrier work is zero, while the native trial storage increases by \(\alpha_N/100000000>0\). Thus automatic cancellation by that old native source is false even within this fixed parameter tuple.

The native quartic potential is different from the trial intensity storage and has no equation assigning this jump debit to it. GM02's proposed stores balance the specified pair-interaction change; they do not contain this new loop energy term. In the zero-load neutral-store case, their existing feedback leaves their stores unchanged while the present Fourier loop launch still costs (25). Extending such a store balance would be an additional choice, not an inherited result.

Writing an auxiliary ledger entry \(-\Delta E_C\) would make the book balance, but would not identify a carrier, its state, an admissible nonnegative reserve or a feedback law. No physical donor or electromagnetic field self-energy is established here. The successful source hypothesis is therefore a prescribed, externally worked circulation actuation, conditional on the stated preparation and comparison equations.

## 8. Verification and scope of completion

[checks.py](checks.py), run through [run_python.cmd](run_python.cmd), checks the exact matrix lift, full kernel, energy minimum, jump errors, profile work, native Fourier and conjugate controls, port-null initialization, symmetry, actual RX between-jump witness, geometry and all 24 source byte identities. [CHECK_RESULTS.json](CHECK_RESULTS.json) records 62 passing checks and the Python, SymPy, Windows and conda environment. Of these, 61 are symbolic/algebraic checks and one is a grouped source-identity check. The written mean, field, minimization and source-account arguments supply the continuum reasoning; the finite checks are corroboration rather than a replacement for those arguments.

The first check-script invocation stopped at a syntax error before executing any checks. That log is retained; the corrected script then passed and the final added nonuniform-origin control also passed. No prior scientific suite, production module or historical orbit was rerun.

The source-side assessment is complete: a new uniform three-loop jump launches the desired minimum means; the orientation follows the registered normals and the chosen alpha sign; exact work is (22), with the positive benchmark (25). Correct initialization and control of between-jump evolution are required for tracking. The physical donor and the second triad's sensing law remain unidentified. No manuscript, commit, push, production change or revision of the accepted GM04 evidence is part of this return.

