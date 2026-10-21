# CA02: initial-state retention in the limiting angular position

21 October 2026. **New result:** a pre-remap drive can convert initial size and tilt differences into an angular endpoint difference. P alone erases size immediately and tilt asymptotically; applying P after a state-dependent torque does not erase every trace of those earlier differences. Retention is dependence, not independent recovery of all initial coordinates.

This report begins with the written derivation before fresh diagnostics. A finite-evidence supplement below is added only after execution. CA01's printed-map completion, convergence and source limitations are inherited; its files are not modified. Diagnostic alpha and starts do not recover the old producer. No physical substance, confinement, memory capacity or SRG-to-Z mapping is asserted.

## 1. Endpoint, domain and the clock

Use the accepted C(x,y,z)=(z,x,y), t_n=.1n, dt=.1 and complete update

\[
H(t)=2e^{-.5t}\cos t+e^{-.3t}\sin t+1.5e^{-.7t}+e^{-.4t},
\quad q_n=\alpha H(t_n)(s_n\times Cs_n),
\]
\[
\widehat q_n=q_n\min(1,.8/(\|q_n\|+10^{-5})),\quad
u_n=s_n+.1\widehat q_n,\quad s_{n+1}=P(u_n).
\]

The primary P first computes theta=atan2(sqrt(x*x+y*y),z) and phi=atan2(y,x), then returns ((1+.5 cos theta)cos phi,(1+.5 cos theta)sin phi,.5 sin theta). Its equivalent off-axis closed form is ((1+z/(2L))x/rho,(1+z/(2L))y/rho,rho/(2L)), L=||s||. The primary code keeps the trigonometric order; the closed form is an independent check only.

Denote the update at absolute index n by F_{alpha,n}. For the endpoint/lift analysis below use the sufficient domain rho(s0)>0 and rho(s0)>||(.1 qhat_0)_xy||. This ensures a nonsingular first horizontal segment; all subsequent ones satisfy the CA01 .42 lower bound. It includes all specified diagnostics and a neighborhood of every fixed off-axis start at alpha=0. This is a sufficient domain, not a claim to characterize all admissible endpoints. CA01 gives

\[
E_{\alpha,k}(s)=\lim_{j\to\infty}F_{\alpha,k+j-1}\circ\cdots\circ F_{\alpha,k}(s)
=s_*(\Phi_{\alpha,k}(s)\bmod 2\pi).
\]

The initial forcing clock k is held fixed when starts are compared. A real lift is defined on a local angular chart (or the angular covering space) by the incoming azimuth plus continuous short-segment increments. It satisfies

\[
E_{\alpha,k}(s)=E_{\alpha,k+1}(F_{\alpha,k}(s)),
\quad \Phi_{\alpha,k}(s)=\Phi_{\alpha,k+1}(F_{\alpha,k}(s))
\]

when the lift on the successor is continued from that on the predecessor. The lift identity otherwise holds modulo 2pi. In particular E_{alpha,0}(F_{alpha,0}(s)) is generally the wrong formula: it would restart the drive at time zero. The full clock is part of the nonautonomous description.

The endpoint set C has rho_*=(3+sqrt(3))/4 and z_*=sqrt(sqrt(3)/2)/2. An endpoint has only one continuous angular coordinate. It may depend on three initial coordinates without allowing all three to be recovered separately.

## 2. Exactly what P alone forgets

At alpha=0, on rho>0,

\[
E_{0,k}(x,y,z)=\left(\rho_*x/\rho,\rho_*y/\rho,z_*\right),
\qquad \Phi_{0,k}=\operatorname{atan2}(y,x).
\]

This is independent of k. Any two off-axis points with the same azimuth have the same endpoint. In a fixed azimuth chart, each fiber is the half-plane (rho cos phi,rho sin phi,z), rho>0, z arbitrary. Positive full-vector scale is erased by the first P; initial inclination affects the first torus point and is then contracted under repeated P. Azimuth is retained exactly throughout. On the angular chart,

\[
\nabla\Phi_0=(-y/\rho^2,x/\rho^2,0),
\]

so the endpoint map has rank one. The two-dimensional fibers describe many distinct states with one endpoint; they are not an independently recoverable three-coordinate record. The axis and origin do not have this smooth azimuth definition and are outside these endpoint charts. CA01's inherited alpha=0 trajectory illustrates the contraction without a new zero-drive run.

For clarity, the inherited contraction uses torus parameter theta and
\[
g(\theta)=\operatorname{atan2}(1+.5\cos\theta,.5\sin\theta),\qquad
g'(\theta)=-{.25+.5\cos\theta\over1.25+\cos\theta}.
\]
The first P puts a state on the upper torus; g maps [0,pi] into [pi/3,pi/2] and contracts [0,pi/2] with |g'|<=1/3. Its unique fixed theta has cos(theta_*)=(sqrt(3)-1)/2. This is why tilt differences vanish in the limiting coordinates without forcing. The endpoint circle is a set of possible final resting positions, not an orbit along which the state keeps circulating.

## 3. Exact angular transfer before remapping

Set A(s)=s cross Cs=(y^2-xz,z^2-xy,x^2-yz) and e=.1*qhat. Because P preserves the input azimuth, the entire update's angular increment is the argument of the horizontal vector change:

\[
\Delta\phi_n=\operatorname{atan2}
\left(xe_y-ye_x,\rho^2+xe_x+ye_y\right).
\]

Indeed, (x+iy)^*(x+e_x+i(y+e_y)) has precisely this real and imaginary part. When rho(s)-||e_xy||>0 the connecting segment avoids the axis; moreover its dot-product denominator is >=rho(rho-||e_xy||)>0. The displayed atan2 is then the unique increment in (-pi/2,pi/2) consistent with the short-segment lift. CA01 supplies rho>=.5 and ||e||<=.08 after the first remap. The prescribed CA02 starts also satisfy a strict first-step bound.

Consequently

\[
\Phi_{\alpha,0}(s_0)=\phi_0+\sum_{n=0}^\infty\Delta\phi_n,
\]

with absolute convergence from CA01's summable forcing bound. This is an angular readout of the full recurrence, with no feedback from the readout.

For a positive scale lambda, the exact first update is

\[
F_{\alpha,n}(\lambda s)=P\left(s+.1\alpha H_n\lambda A(s)
\min\left(1,{.8\over |\alpha H_n|\lambda^2\|A(s)\|+\epsilon}\right)\right).
\]

Thus the full update is not scale-independent simply because P is. On the inactive clip branch the effective pre-remap torque relative to s is proportional to lambda. Initial tilt also changes A(s), the horizontal-angle numerator and the early meridional states on which later forcing acts.

**Exact erasure exception.** For nonzero s=c(1,1,1), A(s)=0. Every positive scale of that same direction has the same first successor P(s), for any alpha and any common starting clock. All later states and endpoints then agree. This is exact first-step erasure, despite possible later driven motion. Conversely a zero first angular numerator alone need not imply endpoint erasure: a changed inclination can affect subsequent angular increments.

## 4. Derivative at zero drive, and why the infinite sum may be differentiated

For a fixed start in a compact smooth off-axis neighborhood, sufficiently small |alpha| keeps clipping inactive: the bounded initial states and all post-remap states give a uniform torque margin. The functions are then smooth in state and alpha; the norm inside the clip does not create a cusp because the selected minimum branch is identically one. Let s_n^0=P^n(s0). Direct differentiation of the increment at alpha=0 gives

\[
W(s)={xA_y-yA_x\over\rho^2}
={xz(z+y)\over\rho^2}-y,
\qquad
D(s_0):=\left.\partial_\alpha\Phi_{\alpha,0}(s_0)\right|_0
=.1\sum_{n=0}^\infty H(.1n)W(s_n^0).
\]

The first-order change of s_n itself does not add another term to this coefficient: the angular increment is identically zero for every s at alpha=0, so its state derivative there is zero. State perturbations enter higher orders.

Here is the convergence justification, not merely termwise formal differentiation. After the first remap use torus coordinates (theta,phi). At zero coupling the map is (g(theta),phi), and after a fixed finite entrance interval the theta map has contraction factor bounded strictly below one on a compact neighborhood of the unforced path. For small coupling, all differences from this map and their fixed-order derivatives are bounded by constants times |alpha H_n|; derivatives in alpha supply H_n. The forcing envelopes and their products are summable. The derivative recurrence has a contracting theta direction and a neutral phi direction perturbed only by a summable sequence. The bound product_n(1+K|alpha H_n|)<=exp(K|alpha|sum|H_n|) is finite, while variation of constants bounds the stable coordinate by a contraction convolution with the forcing. This gives uniformly bounded first sensitivities and decaying stable-coordinate sensitivities.

The same induction works through order three: the nonlinear g terms contain stable-coordinate sensitivities, whose decay is summable; all angular higher-derivative increments have an H_n factor and bounded sensitivities. On any fixed sufficiently small compact parameter/start neighborhood the increment series and its derivatives through order three therefore converge uniformly. Finite entrance steps are smooth. The endpoint lift is locally C^3 (indeed this argument extends to each fixed finite order), permitting derivative/sum interchange and Taylor remainder estimates. This is a local small-coupling argument, not a global regularity or invertibility classification at arbitrary alpha or clipping switches.

In particular the phase gradient remains nonzero locally near alpha=0. The endpoint map still has rank one there, with two-dimensional local level surfaces by the implicit function theorem. On the initial fixed circle, partial_phi Phi=1+O(alpha) uniformly, so for sufficiently small |alpha| it is strictly increasing on the lifted circle and locally/globally invertible as a degree-one circle map. No numerical threshold for this sufficient neighborhood is claimed; degree one alone does not prove monotonicity at the diagnostic couplings.

### 4.1 Starts on the fixed circle

For s0=s_*(phi), the unforced state is constant and

\[
G(\phi)=W(s_*(\phi))={z_*^2\over\rho_*}\cos\phi
+z_*\sin\phi\cos\phi-\rho_*\sin\phi,
\qquad D_C(\phi)=.1 S G(\phi),
\]

where S=sum_{n>=0}H(.1n) is exactly

\[
S=2\Re{1\over1-e^{-.05+.1i}}+
\Im{1\over1-e^{-.03+.1i}}+
{1.5\over1-e^{-.07}}+{1\over1-e^{-.04}}.
\]

Every geometric series has ratio modulus less than one. The four cardinal G values are b,-rho_*,-b,rho_*, where b=z_*^2/rho_*=(sqrt(3)-1)/4. Thus the response is not a constant phase rotation and not axial symmetry. Under a passive rigid frame change, C itself must be transformed to Q C Q^{-1}; rotating just the start relative to the unchanged C is a different dynamical experiment. The torque has cyclic-coordinate structure, whereas P singles out z, so a threefold symmetry of the crystal or of one operator is not a symmetry proof for their complete update. The nonconstant G explicitly disproves continuous axial equivariance near zero coupling.

### 4.2 Size alone: closed response on positive rays of C

W(lambda*s)=lambda W(s). Starting at lambda*s_*(phi), all zero-drive states from n=1 are s_*(phi). Hence

\[
D_{\rm ray}(\lambda,\phi)=D_C(\phi)+.1H(0)(\lambda-1)G(\phi)
=D_C(\phi)+.45(\lambda-1)G(\phi).
\]

At phi=0, G=b>0, so the derivative of endpoint phase with respect to alpha differs strictly between lambda=.5,1,1.5. Differentiability and the nonzero difference of these derivatives imply genuinely different limiting phases for these fixed starts at all sufficiently small nonzero alpha. This proves a retention mechanism at the endpoint, rather than only a first-step separation. It does not itself certify the finite alpha=1/32 measurements. At roots G(phi)=0 the first-order size trace vanishes; this does not imply exact all-order erasure. The exact c(1,1,1) exception above is stronger.

### 4.3 Tilt alone at equal starting norm

For s0=L_*(cos beta,0,sin beta), initial azimuth is zero and norm is L_* for every beta. The instantaneous angular factor is W0=L_* sin^2(beta)/cos(beta). For n>=1 let theta_1=pi/2-beta,

\[
\theta_{n+1}=g(\theta_n),\qquad
w(\theta)={\tfrac14\sin^2\theta\over1+\tfrac12\cos\theta}.
\]

For the two specified beta values theta_1 lies in [0,pi/2]. Put b=w(theta_*). Then

\[
D_{\rm tilt}(\beta)=.1\left[SG(0)+H(0)(W_0-b)
+\sum_{n=1}^\infty H_n(w(\theta_n)-b)\right].
\]

This separates the closed stationary sum from a rapidly convergent meridional correction. On [0,pi/2], |w'|<=5/8 and |theta_n-theta_*|<=(pi/2)3^{-(n-1)}. Truncating this correction before term M leaves absolute derivative error at most

\[
.1\cdot4.5\cdot{5\pi\over16}\,{3^{-(M-1)}\over1-1/3}.
\]

Use M=40 for scalar coefficient evaluation, not an additional full-state zero-drive rollout.

The saved evaluation includes the initial n=0 coefficient and correction indices n=1,...,39, with the remainder beginning at n=40. Thus there are 40 scalar indices in total and 39 meridional-correction terms. This makes precise the plan's shorthand about 40 terms; no extra full-state iteration is involved.

These two equal-norm tilt derivatives differ provably from D_C(0), without relying only on numerical sums. For beta=0, W0=0, theta_1=pi/2 and w(theta_1)=1/4. The first two difference terms are at most .45(1/4-2b)<-.0522 (H_1<=4.5 and 1/4-b>0). Since c_*<.37<sin(.4), pi/2-theta_*<.4; on [theta_*,pi/2], |g'|<.27. Thus |theta_2-theta_*|<.108, and the entire remaining difference tail has magnitude below .45*(5/8)*.108/(1-1/3)=.0455625. The total difference is strictly negative.

For beta=pi/4, W0=L_*/sqrt(2)>.89 and b<.184, so the first difference term exceeds .3177. Here 0<theta_*-pi/4<pi/6 (cos(theta_*)>cos(5pi/12)); the remaining magnitude is at most .45*(5/8)*(pi/6)/(1-1/3)<.221. The difference is strictly positive. Thus initial tilt at fixed norm can also leave a first-order angular endpoint trace. Its mechanism includes the initial impulse and the subsequent decaying memory of the unforced meridional transient.

## 5. Tail and numerical-error distinctions

For N>=1, the exact future increment has |Delta phi_n|<=.225|alpha||H_n|/.42. Summing the four exponential envelopes from n=N gives exactly the work order's bound

\[
B_N(\alpha)={.225|\alpha|\over.42}
\left({2e^{-.05N}\over1-e^{-.05}}+{e^{-.03N}\over1-e^{-.03}}
+{1.5e^{-.07N}\over1-e^{-.07}}+{e^{-.04N}\over1-e^{-.04}}\right).
\]

This bounds the uncomputed tail after state N of an exact trajectory. It does not bound accumulated binary64 error, initial constant rounding or the evaluation error in a scalar series. The report retains the exact expression; ordinary numerical evaluations are labeled estimates. Two endpoint comparisons have mathematical tail at most the sum of their two bounds. Central differences have tail contribution at most B_N(h)/h.

For a locally C^3 endpoint lift f(alpha), the central difference at h obeys |(f(h)-f(-h))/(2h)-f'(0)|<=h^2 sup_{[-h,h]}|f'''|/6 within the smooth neighborhood. This establishes the truncation order, not a numerical bound on that supremum. In the finite diagnostic table the observed difference from the derived derivative and the change under halving h are evidence about this regime. They do not independently prove differentiability, monotonicity or a certified all-error interval. No extra run is warranted to force an error ratio.

For completeness, |H(t)|<=4.5 for t>=0 is valid even though summing its four separate amplitude bounds would give 5.5 at t=0. Bound its first two terms by f(t)=2e^{-.5t}+t e^{-.3t}, using |sin t|<=t. Since 1-.3t<=e^{-.2t}, f'(t)=-e^{-.5t}+(1-.3t)e^{-.3t}<=0, and f(0)=2. The other two terms contribute at most 2.5. This proves the 4.5 bound used in the clip and scalar-correction estimates.

For the specified starts, smoothness can also be justified throughout [-a,a], as needed to apply this remainder at both selected h values. The initial norm <=9/4 and subsequent norm <=3/2, with |H|<=4.5 and |s cross Cs|<=||s||^2, give the uniform inactive-clip bounds 729/1024 and 81/256, both strictly below .8-1e-5. The smallest initial horizontal radius is rho_*/2>.59, whereas the first displacement is at most .1*(729/1024)<.072. Afterward the segment radius is at least .42. Thus the finite initial updates are uniformly smooth on a compact neighborhood of these parameter/start sets. The forcing tends uniformly to zero there. For all sufficiently late n, the torus parameter map is uniformly close, together with its derivatives, to g on [0,pi]; one step enters a small neighborhood of [pi/3,pi/2] where |g'|<r<1. That neighborhood remains invariant once the forcing is small enough. The stable/neutral derivative estimates from section 4 then apply uniformly to the tail; the finite entrance steps do not affect convergence. This proves a finite C^3 supremum on the tested interval, but does not supply its numerical value or prove monotonicity in initial azimuth there.

## 6. Execution and finite-evidence supplement

The single numerical stage completed in 2.0 seconds including interpreter startup, below 600 seconds. It made exactly 12,800 fresh rollout calls (16 runs of 800), no isolated fresh calls, no failed calls and no kernel updates. The 12 inherited fixtures and 200 inherited saved transitions matched CA01 exactly before these runs. The largest workspace size at numerical-stage completion was 2,230,981 bytes, below the 250 MB ceiling. See RUN_RESULTS.json and evidence/NUMERICAL_LAUNCH.json. The scalar coefficient and saved-data analyses do not advance trajectories.

The closed stationary sum is S approximately 65.86496869148128. Ordinary binary64 coefficient values are:

| Initial state, azimuth zero | D = partial_alpha Phi at zero |
|---|---:|
| .5 s_*(0), size only | 1.1642347301 |
| s_*(0), reference | 1.2054125880 |
| 1.5 s_*(0), size only | 1.2465904460 |
| L_*(1,0,0), tilt zero | 1.1456671347 |
| L_*(1,0,1)/sqrt(2), tilt pi/4 | 1.4963456589 |

The exact scalar-series remainder bound in section 4.3 is retained separately from its floating evaluation and from coefficient rounding. At alpha=+1/32 the saved comparisons are:

| Initial change | Phase at state 800 (rad) | Circular difference from reference (rad) | First-order difference prediction (rad) |
|---|---:|---:|---:|
| Reference s_*(0) | .034913238851 | 0 | 0 |
| Half initial size, same direction | .033801059304 | -.001112179547 | -.001286808060 |
| 1.5 times initial size, same direction | .036032627511 | +.001119388660 | +.001286808060 |
| Tilt zero, same norm and azimuth | .033301883984 | -.001611354867 | -.001867045417 |
| Tilt pi/4, same norm and azimuth | .042901847724 | +.007988608873 | +.009091658465 |

These are finite numerical endpoint estimates. The reference tilt is atan2(z_*,rho_*), about .375 radians; the zero and pi/4 cases alter only that tilt at fixed L_*. In particular the zero-tilt case has first angular increment exactly zero in the saved arithmetic but a nonzero eventual shift. This illustrates why a vanishing first angular impulse is not an erasure theorem.

At state 800, B_800(a) is approximately 2.1389587898e-11 rad, half that for a/2; a two-trajectory difference has exact-tail allowance approximately 4.2779175795e-11 rad. These allowances are tiny relative to the observed 0.0011–0.0080 rad differences. They **do not** enclose accumulated binary64 error. The endpoint separations at this finite diagnostic alpha are numerical evidence, while the nonzero derivative differences prove separation for sufficiently small nonzero alpha independently of those runs. No interval-certified separation at a=1/32 is claimed.

| Initial phase | Analytic derivative | Central difference, h=1/32 | Central difference, h=1/64 |
|---|---:|---:|---:|
| 0 | 1.2054125880 | 1.2086813559 | 1.2062300019 |
| pi/2 | -7.7919094572 | -7.7387649474 | -7.7788173778 |

The respective derivative discrepancies decrease from .00326877 to .000817414 and from .05314451 to .01309208. Their observed ratios, 3.999 and 4.059, support the O(h^2) central-difference behavior established by the smoothness argument; no particular ratio was an acceptance condition. The exact-tail contribution to either central difference is at most B_800(h)/h, approximately 6.8446681272e-10. Richardson estimates are recorded in the machine-readable table as estimates only. In particular the second Richardson discrepancy remains about -.000258731; the extrapolation is not treated as exact.

Across saved records, independently evaluating P in its closed form differed from the primary trigonometric successor by at most 4.44e-16. Scaled Euler and perpendicularity residuals were at most 4.62e-16 and 2.19e-17; maximum remap surface residual was 1.67e-16. The accumulated phase lift differed from the saved state's azimuth by at most 1.13e-14 rad modulo 2pi, and from a compensated summation of the same increments by at most 6.22e-15. These measure internal arithmetic consistency, not a rigorous global error enclosure. The minimum horizontal segment lower bound was .5894268; largest raw torque .4807432; every clip factor was exactly one. Distance to C at state 800 ranged from approximately 1.01e-14 to 5.63e-14. None of these finite residuals replaces the inherited convergence proof.

All case inputs, all 801 saved states per case and every torque/clock/intermediate record are retained. ENDPOINT_TABLE.csv lists all 16 phases, circle distances and response coefficients. DERIVATIVE_TABLE.csv and INITIAL_STATE_COMPARISONS.csv retain the comparison arithmetic; ENDPOINT_RESULTS.json also contains the scalar meridional corrections.

## 7. Scope and interpretation

**Inherited:** accepted printed update, circle, convergence, degree one and passive geometry conventions. **Newly derived:** correct clock-indexed endpoint relation, angular-increment sum, exact zero-drive fibers, small-drive response, size/tilt transfer and exact diagonal-ray erasure. **Finite evidence:** the 16 diagnostic phase estimates and residuals. **Unresolved:** global level-set classification, injectivity at arbitrary alpha, rigorous accumulated floating bounds and historical Figure 4 inputs/producer. The derivative coefficients depend on the accepted H and roll completion.

P continually removes a radial degree of freedom and contracts the meridional coordinate, but their previous influence can remain in the neutral angular direction. It is the final angular dependence that survives, not an independently readable copy of size, tilt and azimuth. Even near zero drive the rank-one map has two-dimensional local level sets. An exception may erase a difference exactly; a zero first-order response may merely defer it to higher order.

No physical geometry supplies the endpoint circle or the angular transfer: both come from the accepted printed recurrence. The optional geometric overlay is omitted because native coordinates answer the question directly. No crystal reconstruction, central-ball fit, rescaling, reference-frame experiment, native Z sample, feedback or additional dynamical operation was introduced. The two figures show estimates of possible endpoints and discrete saved samples; they imply neither circular motion nor physical confinement.
