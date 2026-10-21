# CA01 source and measurement analysis

21 October 2026. Primary evidence: *SGR: simulation steps*, 1 August 2025, physical pages 5-8, Figures 3 and 4. This is a local research report, not a manuscript revision or publication. See [SOURCE_AND_CLAIM_MAP.md](SOURCE_AND_CLAIM_MAP.md) for exact source locators and [RESULTS.json](RESULTS.json) for full numerical precision.

**Disposition.** F3's printed object is a prescribed field plus a detector, without a carried point-motion law. Its central marker does not establish dynamical attraction. F4 is a nonautonomous recurrence. The printed remap has a normally attracting fixed circle as its limiting structure, with neutral azimuth. With the printed decaying forcing at t_n=0.1n, the recurrence converges to that circle pointwise in state, rather than maintaining a nontrivial triangular cycle. This is a new conditional mathematical result; it is not a recovery of the missing historical F4 producer.

## 1. Sources, state and clocks

The packet PDF hash is `2d803a28c0a9f4396149cf8700c2a772b5016574517061fb8761c3c50de1c547`, 3,511,783 bytes. Its 17-page count is inherited from the matching R0 inventory; pages 5-8 were newly rendered and read in full, including images. R0's extracted text is a navigation/transcription aid. The raster shows that Figure 3 connects a small cloud near zero, without time arrows, while Figure 4 shows a large initial vertical segment, a diagonal return and a smaller bend followed by another segment. The raster alone does not establish closing, repetition, temporal order of individual samples, or nearby-start attraction. Figure 3 also visibly extends below the method's stated -0.03 bound; this is an approximate visual caption/range discrepancy, not a digitized measurement.

| Target | Retained mathematical object | External input/clock | Observation | Source availability |
|---|---|---|---|---|
| F3 printed | Fixed 100x100 grid; freshly recomputed U,V. No previous U,V in the next field equation | H(t), phase offset .05 sin(.1t), stated dt=.1 | Strict 5th-percentile mask; arithmetic coordinate centroid; connected plot | PDF definition; exact producer and path log not recovered |
| F3 related code | Same grid/field; overwritten U,V; list of detector results is storage only | t=.1*k, k=0..99; explicit H coefficients | Epsilon clip, then flattened first argmin, not centroid | Surviving source and byte-identical ZIP member |
| F4 printed | s_n in R^3, and clock if made autonomous | H(t), alpha, stated dt=.1; exact executed argument schedule unknown | Stored positions and connected plot | PDF definition; alpha, s0, producer and CSV not recovered |
| SIM01 | Many centers, velocities and, in C, stored bits | Separate historical call schedules | Separate wrapped-coordinate readouts | Accepted inherited context only; not rerun or substituted |

The related F3 code has H(t)=2e^(-.5t)cos(t)+e^(-.3t)sin(t)+1.5e^(-.7t)+e^(-.4t), exactly the coefficients printed separately for F4. That does **not** prove the unrecovered F3 percentile producer used these coefficients. Diagnostic uses are labeled. No stateful accumulated memory is present in H itself. F4 retains s; SIM01 retains different state variables. Similar REFU/TGMO/RPCO names do not identify the operators across those experiments.

## 2. F3: magnitude, mask and the apparent center

Write rho^2=X^2+Y^2, theta=atan2(Y,X)+.05 sin(.1t). The printed field is

\[
U=-H(t)\sin\theta/(1+\rho^2),\qquad V=H(t)\cos\theta/(1+\rho^2).
\]

Therefore, exactly,

\[
M=\sqrt{U^2+V^2}=|H(t)|/(1+\rho^2),\qquad M_{\rm clip}=\min(M,1).
\]

The phase offset changes direction but cancels from magnitude. When H is nonzero, unclipped magnitude decreases strictly with radius. On the centered square, its minima are the corners. The center has maximal magnitude (or is on a clipped plateau); it is not a low-magnitude core. A uniform decay of H shrinks the prescribed field amplitude, not a moving particle's distance to the origin.

Let A={grid sites: M_clip<P5(M_clip)}. On an exactly inversion-paired grid, each site and its negative have identical magnitude. A scalar threshold includes or excludes both, even with tied values. Thus every nonempty A has mean coordinates exactly zero. The centroid need not belong to A or even to the grid. On the source's even 100-grid, the origin is absent. On an odd grid, the origin's angular direction is undefined mathematically; the diagnostic uses NumPy atan2(0,0)=0 and no special zero-magnitude replacement. This convention assigns a direction there, not a special quiet center.

The strict '<' matters: H=0 produces A empty. For the domain [-5,5]^2, |H|>=51 gives M_clip=1 everywhere and A empty in exact arithmetic. An undefined mean remains undefined. Partial clipping preserves pair symmetry but can change the selected count; if P5 is on the plateau, only unsaturated points are selected. Percentile interpolation and ties affect which boundary shell is included, so "lowest 5%" need not mean exactly 500 points.

The related code instead uses

\[
m_\epsilon=m\min(1,1/(m+10^{-5})).
\]

On its upper branch, m_epsilon=m/(m+epsilon), with positive derivative epsilon/(m+epsilon)^2. It approaches one without an exact plateau. Its argmin therefore selects a corner for nonzero H, with floating ties and first-index behavior deciding which corner. At H=0 it returns the first grid point even though all points tie. The producer's initial zero arrays are overwritten before observing, and its result list supplies no feedback.

### Bounded numerical evidence

Sixteen fresh field/detector evaluations were performed, never a 100-frame replay. Every grid is 100x100 except one 101x101 case. The first is the related source's literal helper evaluation plus its argmin; the others are explicit diagnostics. The PDF detector uses NumPy's linear percentile and strict '<'. Binary64 is standard; F3_08 is binary32. Full masks, fields, coordinates, H and declared times are saved.

| Case | Definition/control | Selected count | Centroid, rounded |
|---|---|---:|---|
| F3_00 | Related source, t=0, epsilon clip + argmin | 1 | (-5,-5) |
| F3_01 | Printed clip/detector, related H(0)=4.5 | 498 | (0.0148067,0) |
| F3_02 | Printed clip/detector, related H(2.5) | 497 | (-0.00965388,0.00741825) |
| F3_03 | Printed clip/detector, related H(9.9) | 497 | (-0.00741825,0.00965388) |
| F3_04 | H=0 | 0 | Undefined; JSON null |
| F3_05 | H=100, exact printed field is completely flat | 120 numerical selections | (-0.107744,0.156566), spurious relative to exact empty mask |
| F3_06 | H=100, epsilon clip with diagnostic percentile centroid | 498 | (-0.0148067,0) |
| F3_07 | H=45, partial printed plateau | 227 | (-0.188893,0.0135718); plateau rounding contaminates selection |
| F3_08 | F3_01 settings in binary32 | 500 | (-0.0339394,0) |
| F3_09 | Odd 101-grid, no origin override | 507 | (-0.00355030,-0.00670611) |
| F3_10 | Exactly paired 100-grid, trig formula | 500 | (-2.13e-17,0) |
| F3_11 | Exactly paired grid, radial magnitude formula | 496 | (-2.15e-17,0) |
| F3_12 | Paired radial formula, H=1 | 496 | (-2.15e-17,0) |
| F3_13/14 | Printed formula, H=+1/-1 | 496 each | (-1.43e-17,0) each |
| F3_15 | Printed formula, H=1e-12 | 498 | (0.0148067,0) |

These observations show threshold sensitivity, not a new physical path. For example, F3_01's inversion mask differs at four sites, while F3_10/11 are exactly inversion-symmetric as Boolean masks. The coordinate error of one included/excluded point is divided by roughly 500; consequently a one-ulp magnitude difference can cause a centroid change around .01. A small arithmetic error in magnitude need not imply a similarly small error in this discontinuous detector.

For the exact flat H=100 case, literal vector normalization followed by recomputing sqrt(U^2+V^2) yields values from .9999999999999998 to 1.0000000000000002. Strict thresholding invents a mask from those differences. The raw result is retained and labeled, not patched to mimic the theorem. The algebraic radial control is a different diagnostic evaluation, not a repaired historical producer.

The mechanisms and offset scale are verified for these declared controls. The exact Figure 3 trajectory, coefficient history, producer version and floating runtime remain unrecovered. Similar-looking points are insufficient for provenance. [Image 01](plots/01_F3_mask_and_centroid.png) shows mask and marker together; [Image 05](plots/05_F3_passive_comparison.png) preserves those same data in the passive chart.

## 3. F4: preserve the complete printed update

For the declared positive cyclic roll C(x,y,z)=(z,x,y),

\[
q_n=\alpha H(t_n)(s_n\times Cs_n),\quad
\widehat q_n=q_n\min(1,0.8/(\|q_n\|+10^{-5})),
\quad u_n=s_n+0.1\widehat q_n,\quad s_{n+1}=P(u_n).
\]

The component cross product is (y^2-xz,z^2-xy,x^2-yz). This convention is a declared reading of the printed roll, not verification of missing code. The PDF's H is the four-term curve in section 1 above. The clip is applied to torque before the Euler step. There is no velocity variable retained in this printed recurrence.

Since s dot (s cross Cs)=0 and clipping is scalar,

\[
s_n\cdot\widehat q_n=0,\qquad
\|u_n\|^2=\|s_n\|^2+0.01\|\widehat q_n\|^2.
\]

Thus a nonzero Euler increment increases the squared norm by at most .0064. A continuous equation ds/dt perpendicular to s would have a conserved norm; that fact does not establish norm preservation for this finite step. P is analyzed afterward and is not deleted or replaced.

### The map's image and non-idempotence

The PDF uses theta=atan2(sqrt(x^2+y^2),z), phi=atan2(y,x), and

\[
P(x,y,z)=((1+\tfrac12\cos\theta)\cos\phi,
(1+\tfrac12\cos\theta)\sin\phi,\tfrac12\sin\theta).
\]

For rho=hypot(x,y)>0 and L=||s||,

\[
P(s)=\left((1+z/(2L))x/\rho,(1+z/(2L))y/\rho,\rho/(2L)\right).
\]

The image off-axis is exactly the open upper half of (rho'-1)^2+z'^2=1/4, z'>0; its closure is the closed upper half-torus K. All azimuths and all theta in (0,pi) occur. The two full equatorial circles belong to the closure, not the off-axis image. At the axis phi is undefined; the PDF does not specify a branch. Our isolated numerical probes use NumPy's unsigned-zero convention: positive axis -> (1.5,0,0), negative axis -> (.5,0,0) in exact trigonometry, and origin -> (1.5,0,0). Binary sin(pi) leaves a tiny residual. Signed zeros can change atan2 branches; no unique continuous extension at the axis/origin is asserted.

P preserves azimuth but erases positive radial scale, P(lambda*s)=P(s) for lambda>0. It is not a nearest-point projection and is not idempotent:

\[
P(1,0,0)=(1,0,1/2),\quad
P(P(1,0,0))=(1+1/(2\sqrt5),0,1/\sqrt5).
\]

Surface boundedness is imposed by this update; it does not prove a triangular attractor. After a defined first step, ||s|| is between .5 and 1.5. The new Tri-Octagon reference does not supply those bounds.

## 4. Exact attraction classification for the printed map

### Remap-only dynamics

Write a point on K as s(theta,phi)=((1+r cos theta)cos phi,(1+r cos theta)sin phi,r sin theta), r=1/2, theta in [0,pi]. Then P leaves phi unchanged and advances

\[
\theta^+=g(\theta)=\operatorname{atan2}(1+r\cos\theta,r\sin\theta).
\]

Its image is [pi/3,pi/2]. Differentiating gives

\[
g'(\theta)=-\frac{r(r+\cos\theta)}{1+2r\cos\theta+r^2}.
\]

On [0,pi/2] its absolute value is at most 1/3: with c in [0,1], (1/4+c/2)/(5/4+c)<=1/3. The interval maps into itself and is strictly contracting. Consequently there is one fixed poloidal angle. The equation is 2r c^2+c-r=0, so

\[
c_*=(\sqrt3-1)/2,\quad
\rho_*=1+c_*/2=(3+\sqrt3)/4,\quad
z_*=\tfrac12\sqrt{1-c_*^2}=\tfrac12\sqrt{\sqrt3/2}.
\]

Numerically rho_*=1.1830127018922194 and z_*=.4653024295510498. The fixed set is

\[
\mathcal C=\{(\rho_*\cos\phi,\rho_*\sin\phi,z_*):\phi\in S^1\}.
\]

Local multipliers are 0 for the erased positive-ray scale, sqrt(3)-2 approximately -.267949 for the poloidal direction, and 1 for azimuth. The negative multiplier explains an alternating meridional transient. The circle attracts as a set, but a particular point does not attract an open neighborhood containing other azimuths. Contraction excludes all other recurring poloidal cycles, so there is no nontrivial period-three orbit of P.

### Decaying drive: conditional forward-convergence theorem

**Assumptions:** ideal real arithmetic, a fixed finite real alpha, the printed constants and update order, t_n=.1n without resets, and an initial state for which the first remap is defined (or an explicitly declared axis branch lands it on K). Distances are Euclidean in the full three-coordinate state. The full driven description includes clock advance; this is forward attraction at a fixed clock origin, not a compact attractor of an unbounded clock coordinate and not a pullback-attractor claim.

For n>=1, s_n is on K. Put e_n=.1*qhat_n. Then

\[
\|e_n\|\le .08,\quad
\|e_n\|\le .225|\alpha||H(.1n)|,
\quad \sum_n\|e_n\|<\infty,
\]

because ||s cross Cs||<=||s||^2<=2.25 and every exponential envelope in the stated H is summable at this clock. For every point of the segment s_n+v e_n, 0<=v<=1, horizontal radius is at least .5-.08=.42. The polar and lifted azimuthal angular gradients have norms at most 1/.42. Hence the increment changes either input angle by at most ||e_n||/.42. The branch-cut coordinate phi is handled by a continuous lift, not by subtracting wrapped angles.

The next height obeys

\[
z_{n+1}=\tfrac12\rho(s_n+e_n)/\|s_n+e_n\|
\ge \tfrac12(.42)/(1.58)>.1329.
\]

For n>=2 this implies z_n+e_{n,z}>.0529, and so theta_n is in (0,pi/2) from n=3. The perturbed contraction now gives

\[
|\theta_{n+1}-\theta_*|\le\tfrac13|\theta_n-\theta_*|+\|e_n\|/.42.
\]

Iterating this inequality proves theta_n -> theta_* (the exponentially weighted convolution of a sequence tending to zero tends to zero). The lifted phi increments have absolutely summable bounds, so phi_n has a finite limit. Therefore s_n converges to one point of C. In particular distance(s_n,C)->0 and no nonzero-size triangle or persistent moving loop is possible under these assumptions.

C is generally **not invariant under each finite-time driven step**; it is the fixed set of the limiting map and the asymptotic endpoint set. A different nearby start need not converge to the same point. More strongly, fix any initial latitude circle in K. Every finite composition is continuous and its azimuth lift satisfies Phi(phi+2pi)=Phi(phi)+2pi, because the increments never cross the axis and each angular displacement has a continuous lift along the short increment. The tail bound above is uniform over that initial circle, so its limiting azimuth map is continuous of degree one, hence onto the full circle. The limiting family cannot collapse to a universal single point.

There is also no time-independent state for the entire nonzero-alpha schedule. A constant state would have to belong to C by H->0. P is injective on off-axis positive-ray directions; keeping P(s+e)=P(s)=s forces s+e to be a positive multiple of s. Orthogonality forces e=0. For the declared real cyclic roll, s cross Cs=0 only at zero or on the (1,1,1) line; neither intersects C. At t=0, H=4.5 is nonzero. The alpha=0 exception is exactly C.

These results do not cover clock resets or a different producer, nor do they prove that the plotted original samples used this recurrence. They classify the printed map on its stated, explicitly completed clock convention. The symmetry of C is continuous axial symmetry, not a match to the crystal's threefold face symmetry.

### Finite checks, separately from the theorem

Twelve isolated preflights were used: eight remap probes (including axis/origin conventions, a fixed-circle state and the two non-idempotence evaluations) and four torque fixtures with explicit diagnostic alphas. Their full inputs/outputs are in RESULTS.json. They check both clipping branches, zero cross product, sign reversal, orthogonality, Euler accounting and torus membership. The chosen tolerance was 1e-12 before execution.

There is exactly one rollout: alpha=0, s0=(1,0,0), 200 updates, assigned t_n=.1n. This is an admissible off-axis diagnostic start, not a recovered historical initial condition. It stores the initial state and all 200 successors. The distance to C is .5 initially, .18627284 at n=1, .04444195 at n=2, .000869405 at n=5, 1.20043e-6 at n=10, and 2.28989e-12 at n=20. The stored distance at n=200 is zero due to finite precision. Maximum saved post-remap surface residual is 5.55e-17. No driven baseline, nearby-start comparison, extension, random seed, sweep or repeated drive was executed.

The [time-resolved image](plots/02_F4_remap_only.png) marks the initial transient and time direction of this control, and shows the whole 200-step horizon. Its segments are connecting lines between discrete states, not recovered continuous trajectories. Time labels cannot be assigned to individual original Figure 4 samples without the missing record. The early segment resemblance is not a producer match.

## 5. The new measurement geometry remains passive

The existing width-one host and refined PLUS zero face complex were recovered from exact definitions, with MINUS displayed separately. The geometry source's `canonical_points` and `candidate_faces` were detached by AST; no runner or kernel was imported. The face list agrees with the existing candidate JSON, and current Paper C/kernel geometry hashes match HOST_GEOMETRY.json. The later zero-family review supplies tau=0; the earlier candidate JSON's illustrative positive-tau member was not silently substituted. Tau is a shape parameter, never time.

The crystal has 18 vertices, 24 triangles, 42 edges and two six-edge open boundaries. Its fan tips, actual fan openings, and host's finite virtual notch triangles remain different objects. Both hands have the same zero vertex scaffold and distinct chiral face surfaces. Their prior classification is inherited; CA01 only checks the identity of the rendered arrays. The [reference image](plots/04_reference_mesh_and_openings.png) contains no caps or reconstructed sketch geometry.

For F4 the explicit display map is

\[
s_{n+1}=F(s_n,t_n),\qquad y_n=O+s_n,\quad O=(0,\sqrt3/6,0).
\]

For F3, y_grid=O+(X,Y,0) and y_detector=O+(mean X[A],mean Y[A],0), when the detector is defined. Its field construction replaces F; no recurrence is invented for the centroid. The origin shift is constant, axes remain right-handed, scale is exactly one and there is no added azimuth rotation. SRG's units and the host's width-one coordinate unit have no recovered physical calibration. This is an illustrative chart identification, not a canonical coupling or an SRG-to-Z bridge. A three-component source state is not thereby a channel triple or a Z readout.

The central-ball idea serves as an inspection location: no ball surface, radius, state variable or boundary condition is defined. Exact surrounding toroidal-guide dimensions were not supplied; that proposed guide remains schematic and is not added as a measured surface. The native F4 torus and its fixed circle, when shown, are explicitly mathematical update/limit objects, not this new guide.

No frame-dependent centering, normalization, scaling or geometry feedback is used. Unit translation preserves all distances, and a separately declared rigid rotation plus translation preserved pairwise saved-state distances within 1.95e-16. Overlay on/off gives identical displayed coordinates and unchanged raw-file hashes. Cylindrical coordinates retain rho and z, with atan2 wrapping and the axis singularity stated; reconstruction residual is zero for this control. There is no observer clock or shrinking envelope, so clock-induced visual decay does not occur in this chosen view. n is update index, .1n is the declared numerical/forcing clock, and these static PNGs have no animation frame clock.

All 201 saved F4 states lie outside the illustrative central window |x|,|y|<=.3, |z|<=.5 relative to O. This is a disclosed display-window fact, not a geometric collision or containment classification. The [native comparison](plots/03_passive_native_comparison.png) shows them all. F3's outer mask also remains at full scale in [Image 05](plots/05_F3_passive_comparison.png). The geometry supplies readable axes, openings and a comparison origin; no extra dynamical invariant or selected alignment follows.

## 6. Physical identification

| Interpretation | Established mathematical behavior | Possible analogy | Missing identification |
|---|---|---|---|
| Thermodynamics | Prescribed amplitude decay and bounded numerical state | Relaxation or saturation language | Temperature/entropy/heat variables and units; thermodynamic state, energy balance and empirical mapping |
| Magnetism | A three-component cross product and imposed torus remap | Turning or magnetic-looking geometry | Identification and units of fields/moments/currents, a governing magnetic evolution law, boundary/material data and empirical correspondence |
| Light | An oscillatory clock function and spatial plots | Wave or optical display language | Electromagnetic/optical state, propagation relation and physical scale, frequency/wavelength mapping and empirical correspondence |

No one of these interpretations is selected by the supplied definitions. H's label "memory" and the words torque, energy, helicity or toroidal are not physical calibration. There is no claim that a physical connection is impossible, and no outside physical law is imported to complete the model.

## 7. Verification and completion scope

The pre-execution derivation and budgets are preserved in [ALGEBRA_AND_CHECK_PLAN.md](ALGEBRA_AND_CHECK_PLAN.md). New numerical work totals 16 F3 evaluations, 12 F4 isolated steps and one 200-step remap-only trajectory. Passive review of saved arrays is counted separately. No SIM01 replay, native kernel step, dependency installation or graphical viewer was used. Matplotlib generated offline PNGs; all Python ran under CMD with `conda activate torment`.

The exact claims use the displayed algebra; SymPy reductions check supporting identities. Floating checks corroborate implementation and are not formal proof-assistant verification. The record keeps numerical artifacts, conditional theorems, inherited geometry/SIM01 findings and unresolved historical lineage distinct. See [VERIFICATION.json](VERIFICATION.json), [OBSERVER_CHECKS.json](OBSERVER_CHECKS.json) and [EXECUTION_RECEIPT.md](EXECUTION_RECEIPT.md) for final checks and preservation.

An exact replay is blocked only by missing F3/F4 producer/data and F4 parameters. That does not block this work order's mathematical and passive-view conclusions. No additional author clarification is required for the completed scope.
