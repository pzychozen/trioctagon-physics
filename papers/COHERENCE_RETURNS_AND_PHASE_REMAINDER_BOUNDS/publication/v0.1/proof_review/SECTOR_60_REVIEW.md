# Independent review of the proposed 60-degree phase sector

**Disposition: ACCEPTED.** Reviewed by Codex for NCM-PAPER-01, 31 October 2026. This is an internal mathematical review, not external peer review or publication approval.

Proposal: `../packet/NCM_PAPER_01_Codex_Packet_v0.1/reviews/NCM_DUAL_03_GPT_REVIEW.md`, Section 5. Baseline: final DUAL-03 report Section 2. The proposal was checked against the ordered map in `kernel_physics/dynamics.py`, lines 57–104, read as text only. The proof below, rather than sampled phases or a software check count, establishes the extension.

## Exact theorem accepted

Fix epsilon=1/10, g=1/60, lambda=1/300 and k=(999/1000,1,1001/1000). Let z≠0 belong to B3={max_i |z_i|≤3}. Suppose its p-update block is regular, p≥1, and F^p(z)=mu z with |mu|=1. If any state in that block has its three component phases in a closed ordinary arc of width at most pi/3, then z is a fixed state and mu=1. Ordinary phases are modulo 2pi, not phases identified modulo 2pi/3. No conclusion is made for wider sectors or outside B3.

## 1. Reduction and positive mixing

The independently checked returning-block amplitude argument gives every component modulus at most sqrt(K), K=1001/1000. This bound does not require regularity. Regularity implies every output component is nonzero. The last output is mu z, so the initial components are nonzero too. All phases used below therefore exist. Regular equivariance extends the known block and permits a cyclic start at the narrow-sector stage; it does not assume that all regular points form a globally invariant domain.

Write V_i=b_i z_i+g sum_{j≠i} z_j, with b_i=1+epsilon k_i−2g−epsilon |z_i|². On this block b_i≥14497/15000>0 and g>0. Choose lifts theta_i in the shortest closed interval [a,b], width D=b−a≤pi/3. If D>0, each V_i is a positive combination of all three nonzero rays. After rotation by −a, its imaginary part is strictly positive: at least one input angle is above a, all differences lie below pi, and its coefficient and amplitude are positive. Rotation by −b gives a strictly negative imaginary part. The same combination lies in the convex pointed cone spanned by the boundary rays and cannot vanish. Thus every prestage argument lies strictly in (a,b). With three components, their enclosing width D' is strictly smaller than D. No uniform contraction factor or positive lower amplitude bound is needed.

## 2. Exact simultaneous update, endpoints and phase branches

Take the consistent prestage lifts phi_i in that interval and d_ij=phi_j−phi_i. For d≠0 set a(d)=lambda sin(3d)/d; at d=0 use a(0)=3lambda. The weight is even. On the full closed difference interval [−pi/3,pi/3], 3d lies in [−pi,pi]. The ratio sin(3d)/d is nonnegative and at most 3, using the sign of sine and |sin x|≤|x|. At d=±pi/3 the weight is zero, not strictly positive; at d=0 its continuous value is 1/100. Consequently

    0 ≤ a_ij ≤ 1/100,
    1 − sum_(j≠i) a_ij ≥ 49/50,
    phi_i^+ = (1−sum a_ij) phi_i + sum a_ij phi_j.

Expanding the last line gives exactly phi_i+lambda sum sin(3(phi_j−phi_i)), with every kick computed from the same prestage. The output lifts remain in the prestage interval because these weights sum to one and are nonnegative. This is nonexpansion; strict shrinkage is supplied by the prestage, not claimed for the synchronizer alone.

Replacing phi_i by its principal argument adds an integer multiple of 2pi. Each sine argument changes by an integer multiple of 6pi, so the kick is unchanged. Exponentiation reconstructs exactly the actual complex output. The proof neither changes Arg0(0)=0 nor invokes it at a zero: none occurs on this block. No channelwise sequential synchronization is substituted.

## 3. Finite-return contradiction

Iterate the consistent lifted intervals. While the width is positive, the full update strictly decreases its shortest circular arc width; if it reaches zero, it stays zero. Width stays at most pi/3 throughout. For points contained in an arc shorter than pi, the width of their shortest such interval is their shortest circular arc width. This quantity is invariant under a common unit multiplier. Thus a finite return up to common phase cannot begin with positive width and end with the same width. The state at the chosen cyclic start must have width zero.

## 4. Aligned case and full fixedness

At width zero write z=e^(i theta)r with r_i>0. Positive prestage coefficients preserve theta and every phase kick vanishes. A unit-multiplier return of such a state has mu=1. Its real amplitude update is r^+=r−grad W(r), where

    W(r)=epsilon sum_i(r_i^4/4−k_i r_i²/2)
         +(g/2) sum_(i<j)(r_i−r_j)².

The cube [0,sqrt(K)]³ is invariant: the self coefficient is positive, and the increasing upper envelope gives max r_i^+≤T(sqrt(K))=sqrt(K). The cube is convex, so the whole segment between consecutive amplitudes is in it. The largest Hessian eigenvalue is bounded by

    L=epsilon(3K−k_min)+3g=313/1250<2.

Taylor's upper bound along that segment yields

    W(r^+) ≤ W(r) − (1−L/2)||grad W(r)||²
             = W(r) − (2187/2500)||grad W(r)||².

Summing over the finite aligned return forces every gradient and increment to vanish. This proves fixedness at the chosen cyclic start. Its future is then the same fixed state. Since the original return is a repetition up to mu=1, every original stage, including z, is that fixed state. Equivalently, follow the fixed cyclic stage around one whole repeated regular block to the original start. No inverse map or backward uniqueness is assumed.

## 5. What was strengthened, and what was not

The retained 30-degree theorem remains true and its original evidence is unchanged. The same positive-mixing argument and aligned descent extend it to a closed 60-degree complex-phase sector because the exact simultaneous kick is a convex average there. This angle is not the 60-degree spatial cone-axis midpoint. The result does not prove global convergence, absence of all three-stage or twelve-stage cycles, a physical motion law, or a native-to-cone correspondence. It imposes no normalization and no lower amplitude assumption beyond the stated regular finite block.

No substantive correction to the proposal was required. This review explicitly spells out endpoint-zero weights, branch-lift invariance and the passage from a fixed cyclic stage to the original state; these are proof details, not changes to the map or domain. Exact supporting checks are in `check_symbolic.py`, `SYMBOLIC_RESULTS.json` and `SYMBOLIC_LOG.txt`. No native F evaluation or old scientific checker was used.
