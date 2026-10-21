# CA03 — Returning drive and retained angular differences

21 October 2026. The initial mathematical analysis was written before fresh continuations and preserved in evidence/PRE_RUN_ANALYSIS.md. Section 8 was added from the single declared numerical stage. Accepted CA01/CA02 results and source limitations are inherited; new statements below are identified by their scope.

## 1. State, clock and what is being compared

The unchanged update is C(x,y,z)=(z,x,y), a=1/32, dt=.1,
\[
H(t)=2e^{-.5t}\cos t+e^{-.3t}\sin t+1.5e^{-.7t}+e^{-.4t},\quad
q=\alpha H(t)(s\times Cs),\quad \widehat q=q\min(1,.8/(\|q\|+10^{-5})),
\]
\[
u=s+.1\widehat q,\qquad s^+=P(u).
\]
The primary P computes theta=atan2(sqrt(x*x+y*y),z), phi=atan2(y,x), then ((1+.5cos theta)cos phi,(1+.5cos theta)sin phi,.5sin theta). Its off-axis closed form uses rho=sqrt(x²+y²), L=||s||:
\[
P(s)=((1+z/(2L))x/\rho,(1+z/(2L))y/\rho,\rho/(2L)).
\]
It is not substituted into the primary evaluator. The roll convention and coefficients remain CA01's accepted printed-map completion; this is no historical replay.

The eight starts are the exact saved CA02 binary64 rows states[800], with their original lifted phases. Let j count fresh updates, n=800+j the absolute update, N=800. CONTINUE uses forcing index f=800+j; RETURN uses f=j mod N. Both retain the evolving state at every block boundary. For disturbances only j=0..799 is run with RETURN. A forcing reset is an intentional experimental input here, not a state reset or a modification to the evaluator.

For a history h and its same-arm A0p reference r, define the lift difference d=phi_h-phi_r and circular difference delta=atan2(sin d,cos d). Compare delta, |delta|, and |delta|/|delta_initial| when the denominator is nonzero. A common phase displacement is not a loss of a distinction. Wrap changes and sign reversals require separate reporting. Accompany phase with the meridional coordinate, (rho,z) separation and Cartesian distance. A zero angular readout need not mean identical full states.

CA01 gives the torus K: (rho-1)²+z²=1/4, z>=0 and rho>=1/2 after each remap. Its fixed-circle constants are
\[
r=\rho_*=(3+\sqrt3)/4,\quad z_*=\tfrac12\sqrt{\sqrt3/2},\quad
b=z_*^2/r=(\sqrt3-1)/4,\quad c_*=(\sqrt3-1)/2.
\]
Write torus states s(theta,phi)=((1+.5cos theta)cos phi,(1+.5cos theta)sin phi,.5sin theta). The fixed meridional coordinate theta_* has cos(theta_*)=c_*. On K, meridional theta=atan2(z,rho-1); this is different from the incoming polar angle atan2(rho,z), except at fixed points. Off-K initial disturbance readouts do not impose torus membership.

## 2. Smooth branch and the finite block expansion

At alpha=0, the torus update is (theta,phi) -> (g(theta),phi),
\[
g(\theta)=\operatorname{atan2}(1+.5\cos\theta,.5\sin\theta),\quad
g'(\theta)=-{.25+.5\cos\theta\over1.25+\cos\theta},\quad
g'(\theta_*)=\sqrt3-2=:m.
\]
Near the fixed circle all operations are smooth and clipping is uniformly inactive for sufficiently small alpha. A finite composition of N such maps is smooth; compactness of the phase circle permits uniform Taylor remainders, including one derivative in phase. No derivative/infinite-limit interchange is needed for the finite block.

Define T_{alpha,N}=F_{alpha,N-1} o ... o F_{alpha,0}, using local forcing indices. RETURN iterates this full two-coordinate map; CONTINUE composes different later-clock maps. No block output is replaced by a fitted point on C.

With A(s)=s cross Cs=(y²-xz,z²-xy,x²-yz), e=.1 qhat, the exact horizontal increment is
\[
\Delta\phi=\operatorname{atan2}(xe_y-ye_x,\rho^2+xe_x+ye_y).
\]
When rho-||e_xy||>0, its denominator is positive and it is the unique short-segment increment in (-pi/2,pi/2). P preserves that increment. At alpha=0 its state derivative vanishes, because the increment is zero for every state. Its alpha derivative is .1 H_f W(s), where
\[
W(s)=xz(z+y)/\rho^2-y.
\]
For a start s_*(phi) on C the unforced state is constant. Summing the N first derivatives gives the new finite-block result
\[
A_\alpha(\theta_*,\phi):=\arg T_{\alpha,N}(s_*(\phi))
=\phi+\alpha K_NG(\phi)+\alpha^2R(\alpha,\phi),
\]
\[
G(\phi)=b\cos\phi+z_*\sin\phi\cos\phi-r\sin\phi,\quad
K_N=.1\sum_{f=0}^{N-1}H(.1f).
\]
R and partial_phi R are bounded on a sufficiently small compact alpha/phase neighborhood. Consequently partial_phi A=1+alpha K_N G'(phi)+O(alpha²), with
\[
G'(\phi)=-b\sin\phi+z_*\cos(2\phi)-r\cos\phi.
\]
For nearby initial phases on C the difference is delta + alpha K_N[G(phi+delta)-G(phi)] + O(alpha² |delta|). For small delta its leading gain is 1+alpha K_N G'(phi). Starting meridional differences add their own O(alpha delta_theta) angular contribution; the actual block is not a closed scalar phase recurrence.

Put Z_N(w)=(1-w^N)/(1-w). Then the exact finite geometric sum is
\[
K_N=.1\{2\Re Z_N(e^{-.05+.1i})+\Im Z_N(e^{-.03+.1i})
+1.5Z_N(e^{-.07})+Z_N(e^{-.04})\}.
\]
For N=800 it is positive. One elementary proof uses the infinite sum: its cosine contribution has numerator 1-r_1 cos(.1)>0 and its sine contribution has numerator r_2 sin(.1)>0, with positive denominators. Its two nonoscillatory contributions exceed 2.5. The absolute omitted tail is less than 2^-24[2(1.05)/.05+1.03/.03+1.5(1.07)/.07+1.04/.04]<1, using e>2 and 1/(1-e^-x)<=(1+x)/x. Thus K_800>.15. The much sharper ordinary scalar value is recorded separately.

Since G'(0)=z_*-r<0 and G'(pi)=z_*+r>0, small positive coupling contracts phase distinctions near zero and expands them near pi, on this fixed-circle input comparison. Negative coupling reverses the leading signs. This is not an error-certified finite-a stability test; the O(alpha²) constant has not been evaluated.

## 3. Leading preferred phases and genuine full-block fixed points

At a zero of G, (r-z_* cos phi) sin phi=b cos phi. Because r>z_*>0 and b>0, sin and cos have the same sign and neither vanishes: roots lie in quadrants I and III. Use v=tan(phi/2). The root equation is exactly
\[
p(v)=b v^4+2(r+z_*)v^3+2(r-z_*)v-b=0.
\]
There is exactly one positive real root by Descartes' rule and the signs p(0)<0, p(1)>0. The polynomial p(-v) has exactly one sign change, so exactly one negative real root; p(-1)=-4r<0 and p(v) tends positive as v tends to minus infinity. Its angle lies in quadrant III by the preceding sign condition. There are exactly two zeros of G on the phase circle.

At either root the derivative simplifies to
\[
G'(\phi)=z_*\cos^2\phi-r/\cos\phi.
\]
It is strictly negative at the quadrant-I root and strictly positive at the quadrant-III root, since z_* cos³ phi-r<0. Both roots are simple. Rational interval evaluation of p, using rigorous square-root enclosures for its coefficients, can isolate v without asserting that floating trig evaluations are certified. Report displayed phi and slopes as numerical estimates; the analytic signs do not depend on those estimates.

The full fixed-point argument is stronger than identifying roots of a leading angular term. Write T_alpha=(M_alpha,A_alpha) in local torus/phase charts. At zero coupling,
\[
T_0(\theta,\phi)=(g^N(\theta),\phi),\quad
\mu=m^N=(\sqrt3-2)^{800},\quad 0<\mu<1.
\]
The meridional equation M_alpha(theta,phi)-theta=0 has theta derivative mu-1 !=0 at theta_*. The implicit function theorem therefore gives a smooth theta=h(alpha,phi)=theta_*+O(alpha). This solves the meridional fixed-point equation at each phase; it is **not** assumed to be an invariant curve under arbitrary block motion.

Define R_alpha(phi)=A_alpha(h(alpha,phi),phi)-phi. R_0 is identically zero, so R_alpha/alpha extends smoothly to alpha=0 by integrating partial_alpha R along the parameter interval. Its limiting value is K_N G(phi): A_0 has no theta dependence, so the first-order meridional correction contributes nothing. The two simple roots therefore continue, by a second implicit-function argument, to actual full-block fixed points for all sufficiently small nonzero alpha, with phi(alpha)=phi_root+O(alpha) and theta(alpha)=theta_*+O(alpha). These are local branches; exact finite-a roots were neither assumed nor numerically sought.

The two eigenvalues of the full block derivative have expansions
\[
\lambda_{\rm mer}=\mu+O(\alpha),\qquad
\lambda_{\rm ang}=1+\alpha K_NG'(\phi_{root})+O(\alpha^2).
\]
The zero-coupling matrix is diagonal with distinct eigenvalues mu and 1, so ordinary simple-eigenvalue perturbation applies; off-diagonal products first enter the angular eigenvalue at second order. For sufficiently small positive alpha the quadrant-I branch is a local attracting block fixed point, and the quadrant-III branch is a saddle with one expanding angular direction. For sufficiently small negative alpha these roles reverse. Meridional stability persists. No explicit valid alpha threshold, global basin coverage or classification at a=1/32 follows.

A block fixed point corresponds to an N-step periodically driven state history when the forcing clock is included. Motion inside a block can be nonconstant; a block boundary is not necessarily a continuously resting state or an exact point of C. No minimal period is classified. The extremely small nonzero mu must not be replaced by an exact zero because binary64 underflows when evaluating it.

### Bounded scalar evaluation before the rollout

The finite-sum estimate is K_800 = 6.58649686916413. Exact rational interval bisection (64 steps per root) gives the v brackets and slope-sign certificates in SCALAR_ANALYSIS.json. Ordinary phase estimates are 0.245117619178 and 3.252359982752 radians; the corresponding G-prime estimates are -0.781562692490 and 1.649924176265. These are leading roots, not numerically located fixed points of T at a=1/32.

## 4. Finite contraction, erasure and indefinite restarting

Under the indefinitely restarted protocol the forcing does not have a summable infinite envelope. The fading-drive endpoint theorem is therefore inapplicable. The preceding local block theorem does support asymptotic coalescence: two starts in the same sufficiently small attracting neighborhood of a continued attracting block fixed point approach that same block state under indefinite iteration. Their angular difference then tends to zero. It does not follow that the eight diagnostic histories lie in such a neighborhood at the chosen a, or that every initial state shares a basin.

A finite composition of injective local angular maps cannot identify distinct phase inputs while they remain in the relevant injective domains. Likewise near alpha=0 the full torus block has nonzero determinant at alpha=0 (mu), and local full-state invertibility persists in a sufficiently small neighborhood. Finite contraction there does not imply exact full-state coalescence. These facts do not turn the actual two-coordinate block into a phase-only map: two different meridional states can have the same angular readout, and the original three-dimensional P already removes a radial degree of freedom. The exact erasure examples from CA02 remain possible. No blanket finite-time injectivity claim is made at a=1/32.

The declared numerical outcome is consequently a finite comparison: growth, contraction, unchanged within resolution, or an unresolved distinction. Identical floating values would not prove exact equality. A small nonzero phase difference does not prove indefinite protection.

## 5. Later disturbances and a passive tangent calculation

The six disturbances are applied once to the original A0p checkpoint s_b, not to a rounded circle state. With eta=1e-4 they change fractional size, tilt beta, or phase phi separately as specified in the plan. They receive exactly the same first RETURN block as their reference. Original B/C differences describe earlier histories; these new disturbances are different experiments.

On the inactive-clip branch let d=.1 alpha H_f and
\[
DA(s)=\begin{pmatrix}-z&2y&-x\\-y&-x&2z\\2x&-z&-y\end{pmatrix},\qquad
DF(s)=DP(u)[I+dDA(s)],\quad u=s+dA(s).
\]
For v=u, define rho=||(v_x,v_y)||, L=||v||, w=(v_x/rho,v_y/rho,0), D=diag(1,1,0), h=1+v_z/(2L). Then
\[
\nabla h=e_z/(2L)-v_zv/(2L^3),\qquad Dw=(D-ww^T)/\rho,
\]
\[
DP(v)_{i,:}=h\,Dw_{i,:}+w_i\nabla h^T\ (i=x,y),\qquad
DP(v)_{z,:}=w^T/(2L)-\rho v^T/(2L^3).
\]
These derivatives are of the accepted map, with its clip fixed to one only after the regime is verified. The primary evaluator retains its clipping expression. A separate differential calculation through theta=atan2(rho,z), phi=atan2(y,x) supplies an independent Jacobian check at saved inputs.

Initial tangent directions, per unit perturbation parameter, are v_size=s_b, v_tilt=L_b(-sin beta_b cos phi_b,-sin beta_b sin phi_b,cos beta_b), v_phase=(-y_b,x_b,0). Propagate these columns along the saved reference steps by J_{j+1}=DF(s_j)J_j. The phase sensitivity is (-y delta_x+x delta_y)/rho². This passive operation produces no new state trajectory and supplies no global roundoff enclosure.

For the smooth finite block, each signed perturbation has phase change ±eta D_parameter + O(eta²), and its central difference has truncation O(eta²). Coefficients are compared with the six already authorized runs; no additional finite-difference probe is needed. Constants in these error terms are not certified numerically. Construction rounding from spherical/cylindrical reconstruction at eta=0 is recorded, and the initial lift is checked against the actual vector. Testing one eta is not a general noise-robustness result.

There is also a structural distinction between active dynamics and display: if torque is zero, the accepted step still advances s to P(s), which may differ from s. Repeatedly displaying P(s) for a state that is held fixed merely repeats one observation. It does not generate the iterates P^n(s). No replacement no-remap engine is simulated.

## 6. Clipping, nonsingularity and clock-qualified tails

The inherited bound |H(t)|<=4.5 for t>=0 follows from |sin t|<=t: the first two terms are bounded by f(t)=2e^(-.5t)+t e^(-.3t), and f'<=0 because 1-.3t<=e^(-.2t). Thus f<=2 and the other terms add at most 2.5.

Checkpoints are post-remap states, so their exact-arithmetic norms are <=1.5. The defined SIZE+ norm is at most 1.50015; tilt and phase changes preserve norm in their exact definitions. Therefore ||q0||<=4.5*(1.50015)²/32<.317<.8-1e-5. The conservative binary64 initial gate 1.501 preserves the same strict .317 margin. All later norms are <=1.5 and ||q||<=81/256. Clipping is inactive but retained in code. Perturbed horizontal radius is at least .49985; the first displacement is <.0317. Later segments have radius at least .5-.08=.42. Numerical checks verify that construction/rounding has not threatened these large margins.

After a block, if forcing index f continues to advance without further restarts, inherited angular summability gives
\[
B_f(a)={.225|a|\over.42}\left[
{2e^{-.05f}\over1-e^{-.05}}+{e^{-.03f}\over1-e^{-.03}}
+{1.5e^{-.07f}\over1-e^{-.07}}+{e^{-.04f}\over1-e^{-.04}}\right].
\]
The derivation is ||e||<=.225|a||H_f|, horizontal segment radius>=.42, and summation of the four exponential envelopes. At the final CA03 stop CONTINUE has next f=3200 and RETURN has next f=800 under the specified finite-pulse future. Disturbances have next f=800. Those hypothetical uninterrupted futures converge to C and have the corresponding exact-trajectory angular tails. At an earlier RETURN boundary B_800 applies only to the counterfactual of no further restart; it cannot bound the next actual pulse. Two-state differences use the sum of the two tail bounds.

These exact bounds concern the remaining evolution of an exact recurrence. They do not bound inherited checkpoint errors, construction rounding, accumulated binary64 errors or differentiated remainder constants. Near-zero drift at large f may fall below floating resolution. Residuals and source hashes check consistency, not a certified global enclosure.

## 7. Passive geometric instrument

The native (theta,phi) view separates contracting meridional motion from retained angular differences and makes block response intelligible. This is a coordinate analysis of the recurrence. The actual saved crystal/host reference is an additional observation, placed by y=O+s with O=(0,sqrt(3)/6,0), unit scale and fixed axes. Both face hands and their open boundaries are retained. No projection into a central ball, new toroidal guide or force is introduced.

For Q=Rz(pi/3), rotate the whole saved view about O: y'=O+Q(y-O), with reference vertices and circle transformed the same way and measuring axes Qe_i. Components measured in those co-rotated axes are (Qe_i) dot Qs=e_i dot s. Phase differences and all Euclidean distances therefore agree exactly in mathematics, up to rounding in the saved-observation check. A rotation of the start relative to untransformed dynamics would be a different experiment; equation coordinates would instead require C'=QCQ^-1 and P'=Q P Q^-1. No such new trajectory is run.

Distances to the actual reference vertices are optional relational readouts of placement, not recurrence invariants in time or a chirality detector. Both hands share the vertex set while their face surfaces differ; a vertex-distance metric alone cannot distinguish those surfaces. No predictive geometric correspondence is assumed. The numerical assessment below will state whether anything beyond context was found.

## 8. Finite evidence from the one authorized numerical stage

**Observed answer:** the earlier size and tilt traces remain distinct through all three returning pulses, but their angular separations contract to about 63.2% of their inherited values. CONTINUE preserves those distinctions to the available floating precision. This is finite contraction, not exact erasure or proof of indefinite protection.

The single launch completed all 22 branches and exactly 43,200 fresh updates in 6.093 seconds including interpreter startup. No inherited prefix was rerun, no fresh isolated call was made, and no branch failed. The 36 passive preflight evaluations matched every inherited primary value exactly. The numerical-stage workspace size was 8,797,108 bytes, below 250 MB. Source/model identity and checkpoint row-byte checks passed. See RUN_RESULTS.json and evidence/NUMERICAL_LAUNCH.json; the pre-run analysis and its hash remain in evidence/.

### 8.1 Earlier history under CONTINUE and RETURN

All values below are circular phase differences from the same-arm A0p reference, in radians. The unrounded data are in HISTORY_COMPARISONS.csv.

| Earlier history | Inherited difference at n=800 | CONTINUE at n=3200 | RETURN at n=3200 | RETURN magnitude / inherited magnitude |
|---|---:|---:|---:|---:|
| Bhalf: half starting size | -.001112179547 | -.001112179547 | -.000702991202 | .632084274 |
| Bthreehalf: 1.5 times starting size | +.001119388660 | +.001119388660 | +.000707461627 | .632007141 |
| Czero: earlier zero tilt | -.001611354867 | -.001611354867 | -.001018539820 | .632101495 |
| Cquarter: earlier pi/4 tilt | +.007988608873 | +.007988608873 | +.005046949205 | .631768220 |

After one RETURN pulse the retained fractions range .859081–.859245; after two, .737122–.737392; after three, .631768–.632101. Thus each pulse contracts these particular nearby traces in net. There are small within-pulse increases, so the saved sample sequence is not claimed to be monotonically contracting at every update. All 2401 samples per branch were checked for the four history comparisons: none reverses sign or changes its circular wrap integer. READOUT_DETAILS.json records the full-window extrema rather than only selected boundaries.

In CONTINUE, the largest change of any of these four pairwise differences anywhere in the window is 6.68e-15 rad. That does not resolve a meaningful growth or contraction from floating effects. The largest absolute phase displacement among the four cardinal controls is 5.40e-13 rad, consistent with the already-faded drive. A displayed ratio just above one in the final decimal places is not evidence of trace amplification.

The RETURN cardinal controls move by different amounts:

| Original cardinal control | Checkpoint phase | Phase at n=3200 | Total new phase displacement |
|---|---:|---:|---:|
| A0p | .034913238851 | .112815502557 | +.077902263706 |
| A1p | 1.344662016278 | .870488918024 | -.474173098254 |
| A2p | 3.097340356924 | 2.830627643033 | -.266712713891 |
| A3p | 4.947896097775 | 5.509202248956 | +.561306151182 |

This is phase-dependent motion, not a uniform rotation of the whole pattern. A3p's difference from A0p is represented by subtracting one 2pi from the lift difference throughout; that inherited wrap convention is recorded, not interpreted as a sign reversal. The cardinal starts are orientation controls, not a local neighboring pair proving finite-alpha angular expansion near every phase. The expansion statement in section 2 remains a leading small-coupling result.

The full state was carried. Across RETURN branches, the distance to C reaches .00819863125 within a pulse and falls to at most 5.23e-14 at the final boundary. Earlier-history meridional separations from A0p reach up to 6.25e-5 radians within the pulses before contracting again. Final history-pair Cartesian distances remain approximately .000832, .000837, .001205 and .005971. Some final (rho,z) differences round to zero; the full states and phases remain different. Near-circle block boundaries do not authorize setting theta=theta_*.

### 8.2 Six later disturbances

These use one first RETURN block from the original A0p checkpoint, with eta=1e-4. They are separate from the inherited B/C histories. The nominal size and tilt perturbations have zero initial angular difference; phase perturbations start at ±1e-4 rad. Rounded final phase differences from the common saved reference are:

| One-time disturbance | After 800 new updates, radians | Microradians |
|---|---:|---:|
| SIZE+ | +1.914097461e-7 | +.191409746 |
| SIZE- | -1.914095021e-7 | -.191409502 |
| TILT+ | +1.075795349e-6 | +1.075795349 |
| TILT- | -1.075435709e-6 | -1.075435709 |
| PHASE+ | +8.592158802e-5 | +85.921588017 |
| PHASE- | -8.592192633e-5 | -85.921926325 |

Size and tilt disturbances therefore acquire nonzero angular traces during the returning drive. A direct phase disturbance retains about 85.92% of its initial angular difference after one block. The perturbation parameters have different units (fractional size versus radians), so their numerical sensitivity coefficients are not a calibrated capacity or universal ranking of physical robustness.

The analytic tangent propagation on the 800 already saved A0p RETURN steps gives:

| Parameter | Phase derivative after one update | After one block | Central difference from the authorized ±eta runs |
|---|---:|---:|---:|
| Fractional size | .002248488588 | .001914096242 | .001914096241 |
| Tilt angle | .015031878091 | .010756155222 | .010756155291 |
| Phase angle | .989738702906 | .859217571868 | .859217571715 |

The first-step effects and full-block consequences are distinct. For example, the positive size impulse produces about .22485 microradians after one update and .19141 after the block; the initial angular change does not determine the whole outcome. The largest discrepancy between the block tangent and these central differences is 1.54e-10 in derivative units. No extra perturbed input or state advance was used to obtain the tangent. Closed-form and trigonometric Jacobians agree within 4.44e-16 on the saved inputs; the phase chain rule, radial-null property of DP and quadratic-torque homogeneity also pass below 1e-12. These are consistency checks, not a global numerical-error certificate.

The small asymmetry between plus/minus tilt effects is consistent with higher-order response. It was not removed by symmetrizing the states or changing eta. INPUT_DEFINITIONS.json retains the actual vectors and zero-perturbation reconstruction residuals. Only this perturbation size, time and reference orientation were tested.

### 8.3 Endpoint and error statements remain schedule-specific

For the defined finite-pulse future, the final RETURN and disturbance phases have an exact-trajectory remaining-tail bound B_800(a), whose ordinary estimate is 2.13895878976e-11 rad per state. Pairwise exact tails add. These tails are much smaller than the observed history and disturbance separations, but do not certify them against inherited or accumulated floating error. The evidence supports nonzero finite-protocol endpoint distinctions numerically, not as interval enclosures.

For CONTINUE the final uninterrupted tail is B_3200(a), estimated as 1.15050858390e-42 rad. This does **not** give 42-digit numerical accuracy to a binary64 state. The earlier checkpoint and all intermediate arithmetic still lack a certified accumulated-error enclosure. At intermediate boundaries B_1600 and B_2400 estimate to 8.07281558255e-22 and 3.04759623911e-32. For RETURN, an earlier B_800 would describe only stopping the restarts at that boundary; the next actual pulse can move the state much more.

All saved successor relations were independently checked without chaining computed outputs. Maximum closed-form successor discrepancy is 6.66e-16; scaled Euler and perpendicularity residuals are 4.60e-16 and 2.24e-17; remap surface residual is 1.67e-16. The maximum lifted-phase/azimuth residual is 1.40e-14 rad, and comparison with compensated summation of the same increments differs by at most 1.07e-14. Maximum raw torque is .211708407753; every clip factor is exactly one. The minimum horizontal segment lower bound is 1.16426885021. These checks support consistent implementation and passive measurement, not exact arithmetic equality.

### 8.4 What the actual geometric reference contributed

The passive test uses 64 indexed boundary observations: all eight unperturbed histories, both schedules, and n=800,1600,2400,3200. Both actual hands, the original face/boundary indices, the host and the circle were transformed together under Q about the stored O; scale remained one. Co-rotated phase differences agree within 3.33e-16 rad. Pair distances, point-to-circle distances and distances to reference vertices agree within 4.44e-16. The transformed measuring axes recover native coordinates within 2.22e-16. The original geometry file hash remains unchanged.

Nearest-vertex distances to either crystal hand range .90356–1.00927 in the declared chart units across these observations; the host-vertex range is .68430–.86943. These are relational placement measurements. They neither show containment nor identify an alignment selected by the dynamics. Identical nearest-vertex ranges for both hands cannot classify chirality because the vertex sets coincide while the face surfaces differ. No additional dynamical invariant or predictive correspondence was established. An overlay would add context only, so the three figure slots are used for the actual trace, response and disturbance comparisons. The meridional/phase analysis is useful without attributing physical action to the reference mesh.

## 9. Claim boundaries

**Inherited CA01/CA02:** the completed printed recurrence, remap geometry, fading-drive convergence, endpoint-retention mechanism and historical-source gaps. **New CA03 mathematics:** finite-block response with differentiated remainder; two simple leading angular roots; meridional elimination and local full-block fixed-point branches; their sufficiently-small-coupling stability; proper separation of finite and indefinite protocols. **Finite evidence at a=1/32:** approximately 36.8% net contraction of four earlier traces over three returned pulses, the six disturbance effects, derivative consistency and passive frame agreement. **Unresolved:** a certified small-coupling threshold, exact fixed points or global basins at a=1/32, indefinite behavior of these particular eight histories, rigorous accumulated floating-error enclosures, other disturbance scales or schedules, and missing historical producer inputs.

The run does not establish exact erasure. The local theorem does establish that indefinitely recurring drive can select an attracting block state for sufficiently small positive coupling, allowing asymptotic local coalescence rather than indefinite preservation of every trace. These are compatible statements about different protocols and scopes. No production code, unrelated research or physical containment rule is changed.
