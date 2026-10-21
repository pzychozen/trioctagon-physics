# CA04 — Finite-coupling certificate for the complete RETURN map

**21 October 2026. Disposition: CERTIFIED_LOCAL_ATTRACTION_AT_1_OVER_32.**

The complete exact-real 800-update map at alpha=1/32 has a unique attracting fixed point in each of two explicit nested chart rectangles. All five indexed exact dyadic saved starts have certified entry into the larger rectangle after one block. This proves their convergence to the same periodically driven response under the declared indefinite RETURN future.

The initial proof argument below was sealed before any fresh full-block evaluation. It is reproduced from PRE_RUN_ANALYSIS.md; the results and limitations following it were added after construction and fixed-input replay. The source recurrence, full state and advancing within-block clock remain unchanged.

# Initial sealed mathematical analysis

## Exact dynamics and domain

Let A(s)=(y^2-xz,z^2-xy,x^2-yz), H(t)=2exp(-t/2)cos(t)+exp(-3t/10)sin(t)+(3/2)exp(-7t/10)+exp(-2t/5). The full map is T=F_799 o ... o F_0, each F=P(s+qhat/10), q=(1/32)H(f/10)A(s), qhat=q min(1,(4/5)/(norm(q)+1/100000)). These rational coefficients and times are exact. The accepted binary64 evaluator remains a separate unchanged consistency reference.

For t>=0, |2e^(-t/2)cos(t)+e^(-3t/10)sin(t)|<=2e^(-t/2)+t e^(-3t/10). The derivative of this upper envelope is nonpositive because 1-3t/10<=exp(-t/5). Its value at zero is 2; adding the last two terms gives |H|<=9/2. On K, norm(s)<=3/2, rho>=1/2, norm(A)<=norm(s)^2. Thus norm(q)<=81/256, strictly below 4/5-1/100000. The horizontal straight-segment radius is at least 1/2-81/2560=1199/2560. These proofs justify the smooth inactive-clip branch on K, not an alteration of clipping. Off-K entry requires its own interval check.

## Exact two-coordinate map

Let c in (-1,1), v finite, r=1+c/2, z=sqrt(1-c^2)/2, C=(1-v^2)/(1+v^2), S=2v/(1+v^2). Then chi=(rC,rS,z), C^2+S^2=1, and chi lies on K. Conversely, on this open chart, c=2(rho-1), v=y/(rho+x), z>0.

Put k=H(f/10)/320. Resolve the torque in the horizontal basis (C,S),(-S,C):

R=C A_x+S A_y=z^2 S-rz C^2,
W=C A_y-S A_x=z^2 C-r^2 S+rz SC,
Z=A_z=r^2 C^2-rz S.

Write a=r+kR, b=kW, d=z+kZ, h=sqrt(a^2+b^2), L=sqrt(h^2+d^2). Then u=(aC-bS,aS+bC,d). With a>0, the short angular increment delta has tan(delta/2)=w=b/(h+a). Hence the exact chart update is

c_next=d/L,
v_next=(v+w)/(1-vw).

Require h+a>0, 1-vw>0 and the original horizontal half-angle denominator h+u_x>0. The explicit interval tests also require -1<c<1, h>0, L>0. There is no chart transition or phase wrap in the accepted tube. Since P(u) has radius 1+d/(2L) and height h/(2L)>0, its chi parameters are exactly (d/L,u_y/(h+u_x)); the half-angle addition identity gives the expression above. The simplification preserves the complete update and does not fix c at c*. In particular late k values remain present.

## Derivatives

For any independent coordinates x_j, use d(ab)=b da+a db, d(a/b)=(da-(a/b)db)/b, d sqrt(a)=da/(2sqrt(a)), d(a^2)=2a da. Begin Dc=(1,0), Dv=(0,1). The explicit scalar ingredients have

dr=dc/2, dz=-c dc/(2sqrt(1-c^2)),
dC=-4v dv/(1+v^2)^2, dS=2(1-v^2)dv/(1+v^2)^2.

Differentiate R,W,Z and the subsequent expressions by these rules. This produces the two-by-two local Jacobian J_f throughout the full interval state box. Propagate signed matrices D_{f+1}=J_f D_f, D_0=I, before taking absolute bounds at f=800. Natural state interval images contain every orbit of the starting rectangle; J_f therefore bounds every needed local derivative. Matrix interval induction encloses the full derivative on the entire initial domain, including correlations that are discarded conservatively. Subdivision unions can reduce overestimation and must cover the original rectangle exactly. No approximate central derivative is substituted for a set derivative.

## Directed arithmetic proof

Fix Q=2^p. An interval is [l/Q,h/Q] with arbitrary-size signed integer l<=h. Rational n/d is enclosed by floor(nQ/d),ceil(nQ/d), with d>0. Addition and subtraction are exact at the grid. Multiplication takes the min and max of four endpoint integer products, then divides outward by Q. Division first bounds the reciprocal with floor(Q^2/h),ceil(Q^2/l) when zero is excluded; negative intervals follow the same decreasing reciprocal rule. Squaring uses 0 as the minimum when the interval crosses zero. Square root for l>=0 is [isqrt(lQ),ceil_sqrt(hQ)]/Q. Integer-square comparisons establish both inequalities exactly. These operations enclose their real functions; induction encloses every arithmetic expression. No binary floating arithmetic enters a certified endpoint.

For each exact rational t=f/10, the exponents and trig arguments are divided by 128. Their absolute values are <1. Evaluate the degree-64 Taylor polynomial of exp(y), sin(y), cos(y) with interval arithmetic. The exponential remainder is at most 3/65!, since exp(|y|)<3 for |y|<=1 (the series for e is less than 3). Each sine/cosine remainder is at most 1/65! by Taylor's theorem. Add these symmetric rational error intervals, then use exp(2y)=exp(y)^2, sin(2y)=2sin(y)cos(y), cos(2y)=cos(y)^2-sin(y)^2 seven times. These identities propagate the enclosing errors to the requested arguments. Round every operation outward. This constructs 800 exact-real forcing enclosures, including constants and all late values.

For phase display, if |v|<=1/2, use 2atan(v)=2 sum_{j=0}^{127} (-1)^j v^(2j+1)/(2j+1), with symmetric error at most 2/(257*2^257); the alternating-series bound applies separately at every point in the interval. Cartesian display uses chi with the same outward arithmetic. Display bounds are not substituted back into dynamics.

## Existence and attraction theorem to verify

For an exact dyadic center xhat and positive rational radius vector r, define the closed convex rectangle X=xhat+[-r,r]. Suppose all 800 compositions are smooth on X, |T(xhat)-xhat|<=e, and |DT(x)|<=M for every x in X. For any x in X, integrate the derivative along the segment from xhat to x to get |T(x)-xhat|<=e+Mr. If e+Mr<r componentwise then T maps X into its interior. The same segment argument for any two points gives ||T(x)-T(y)||_r<=q||x-y||_r, where q=max_i (Mr)_i/r_i<1. The closed rectangle in this weighted norm is complete, so the contraction argument gives a unique fixed point in X and convergence of all its iterates. This is a statement about the physical update T, not Newton's iteration.

For a larger certified concentric B containing X, the unique root is the same because the root in X is in B. Its invariance and contraction may have different certified bounds. For each exact stored dyadic Cartesian start, carry out the actual F_0 with a rigorous off-K clipping/axis bound, extract c=u_z/norm(u), v=u_y/(rho(u)+u_x) for P(u), then evaluate f=1,...,799. If that entire endpoint enclosure is inside B (or X), induction supplies the indefinite future without extra pulses. This changes neither initial state nor dynamics. It certifies a newly declared dyadic initial-value problem, not the old floating calculation's accumulated history.

Convergence of T at the boundaries implies convergence at each corresponding within-block phase by continuity of each finite prefix F_{j-1} o ... o F_0. The result is a periodically driven response; its minimal period and within-pulse stationarity are not assumed. The theorem is intrinsic to K and the specifically validated off-K starts, not an unproved ambient neighborhood claim. A derivative interval containing zero does not prove a zero multiplier, invertibility failure or exact finite-time erasure. The geometry is a passive coordinate reference.

## Possible conclusions

Only strict verified inequalities warrant CERTIFIED_LOCAL_ATTRACTION_AT_1_OVER_32. A root existence proof without dynamics stability is CERTIFIED_FIXED_POINT_ONLY. An ordinary solver alone gives NUMERICAL_CANDIDATE_ONLY. Failure to close these obligations within scope is NO_CERTIFICATE_WITHIN_DECLARED_SCOPE, not nonexistence. Entry conclusions are separate for the five indexed initial data.

## Completed certificate at exactly 1/32

The exact dyadic center is

    c_hat = 3296863744182679 / 9007199254740992
    v_hat = 4382175857337591 / 36028797018963968

Its ordinary values are approximately (0.3660254037843512, 0.1216298133693170). The two-coordinate Newton solve took four complete-block evaluations and stopped with a binary64 residual of 5.55e-17. This was only candidate evidence. The subsequently validated exact-real residual bound is approximately e=(2.90090378513e-18, 1.58224025513e-16); its difference from the ordinary residual illustrates why the latter is not a certificate.

Define X=xhat+[-10^-6,10^-6]×[-10^-5,10^-5]. The following entries are deliberately rounded **upward** bounds on the exact nonnegative derivative-bound matrix in CERTIFICATE.json:

    M_X <= [[3.304e-16, 1.464e-13],
            [0.001919, 0.850415]]

All 800 signed derivative updates were enclosed before taking absolute values. No late update was removed, no matrix entry was declared exactly zero, and the meridional variable was not held fixed. The exact serialized certificate gives:

| Quantity | X result (display values) |
|---|---:|
| First inward margin r_c-e_c-(Mr)_c | 9.99999999995635e-7 |
| Second inward margin r_v-e_v-(Mr)_v | 1.49393583195194e-6 |
| Weighted contraction bound q_X | 0.850606416788984 < 0.851 |

The margins are strictly positive as exact rational inequalities. Thus T(X) is inside the interior of X and T contracts in the norm max(|dc|/10^-6, |dv|/10^-5). Existence and uniqueness concern the actual T; Newton plays no role in these conclusions.

The first declared enclosure succeeded at p=160. No subdivision, alternate radius or precision refinement was used. All interval-domain tests passed. For X, the smallest certified bounds over the complete tube exceed 1.176 for the radial and horizontal pre-remap components, 1.271 for the full norm, 2.318 for the original half-angle denominator, and 0.999997 for the addition denominator. The exact values are in the certificate.

The fixed point is further localized by the exact scalar implication

    |x_star-xhat| <= (I-M_X)^(-1) e.

Indeed, the nonnegative M_X has weighted norm below one, so its Neumann inverse exists and is nonnegative. Applying it to d<=e+M_X d gives the bound. This uses saved certificate inequalities and no new state evaluations. The resulting coordinate-error bounds are less than 2.901e-18 in c and 1.058e-15 in v. The rigorous phase enclosure is contained in

    0.2420705842886754 < phi_star < 0.2420705842886798 radians.

Cartesian coordinates are approximately (1.148520440083195, 0.283583940922842, 0.465302429551067); full exact interval endpoints are in CERTIFICATE_SCALAR_CONSEQUENCES.json. Display rounding can make two endpoints look equal. This does not make the mathematical interval degenerate. The old leading root near 0.245117619178 is only the seed, and no continuation proof linking branches was attempted.

## Larger attracting region and the five entry problems

Only after X passed, the declared larger concentric B with radii (1/1000,1/10) was evaluated. It also passed on its first full-domain attempt, without subdivision:

    M_B <= [[2.691e-15, 4.244e-13],
            [0.005490, 0.924524]]

| Quantity | B result (display values) |
|---|---:|
| First inward margin | 0.000999999999957557 |
| Second inward margin | 0.00754211953063461 |
| Weighted contraction bound q_B | 0.924578804693652 < 0.925 |

B uses max(|dc|/0.001, |dv|/0.1). These norm bounds cannot be read as observed phase-retention fractions or compared as if the norms were the same. Because X is a subset of B, the unique fixed point in B equals the one in X. Every point in B converges to it under T.

The certified B tube has radial/horizontal lower bounds above 1.174, norm above 1.268, original half-angle denominator above 2.206, and addition denominator above 0.999465. Thus there is no chart switch or hidden branch discontinuity.

For each saved state, the serialized exact dyadic components were first verified against the NPZ member and row hashes, float hex and exact ratios. They were then used directly. The actual Cartesian f=0 update checked norm(q)+1/100000<4/5 and a positive horizontal-segment bound. Its post-remap chart state was obtained from u_z/norm(u) and u_y/(rho(u)+u_x). The intrinsic continuation began at f=1 and finished at f=799. There was no initial projection onto K, and no clock restart after the first update.

| Exact stored IVP | Full blocks used | Final v (display only) | Final phase (display only) | Result |
|---|---:|---:|---:|---|
| A0p_RETURN | 1 | 0.065973712572206 | 0.131756488456476 | certified entry into B |
| Bhalf_RETURN | 1 | 0.065671414263580 | 0.131154500024741 | certified entry into B |
| Bthreehalf_RETURN | 1 | 0.066277935162302 | 0.132362284712477 | certified entry into B |
| Czero_RETURN | 1 | 0.065535723538212 | 0.130884281548326 | certified entry into B |
| Cquarter_RETURN | 1 | 0.068144045826960 | 0.136077721177767 | certified entry into B |

Every full two-coordinate endpoint enclosure is contained in B. Their v widths are below 2e-45; no display decimal is substituted for an endpoint. Stop-on-inclusion was obeyed, so no second entry block was run. The first-step and complete-block enclosures, all exact input components and the destination are saved in CERTIFICATE.json.

This is a theorem about the five stored numbers treated as exact new initial values under a new f=0 RETURN future. It does not certify the ideal exact-real versions of the preceding 3,200-update histories. Their later angular differences tend to zero because both full states converge to the same block fixed point and the chart phase is continuous. No exact finite-time identification is inferred.

## Independent verification and arithmetic scope

verify_certificate.py reconstructed every H interval and exactly reproduced the residual and both AD certificates from the fixed inputs. It then propagated a separately hand-derived Jacobian on each of those same full rectangles; those independent bounds also satisfied both strict contraction/inclusion tests. It independently checked all five entry IVPs. No root search, new domain, original runner or reference-evaluator call was part of replay.

The independently hand-derived bounds were approximately q_X=0.850607383690 and q_B=0.943681887849. The second is wider than the AD certificate's 0.924578804694 because the algebraic differential uses different interval groupings. Both enclose the same exact derivative and both prove contraction. The reported q<0.925 for B is the exactly reproduced AD bound.

The arithmetic audit checks exact Fraction endpoint inequalities, integer-square-root enclosure inequalities, primitive differentiation identities, torque decomposition, and the rational half-angle addition identity. The complete written derivative proof is induction through those operations. The separately hand-derived implementation expands the local differential without using the forward AD class, and composes signed interval matrices.

This is a computer-assisted proof based on the stated arithmetic and code assumptions, not a proof-assistant formalization or a theorem obtained by precision agreement. The trusted arithmetic core is limited to exact integers, rational conversion, directed operations and integer square root. The exponential and trigonometric functions are built with the explicit remainder bounds above. METHOD_AND_SOURCE_NOTES.md separates the official Python contracts from private model evidence.

The binary64 preflight covered exactly twelve saved predecessor/successor cases. All compared fields agreed exactly in this environment (maximum difference zero). That check establishes consistency only; the proof uses exact-real rational times, not the saved binary64 t values.

## Execution, preservation and limitations

The numerical plan and initial mathematical analysis were sealed before the first complete-block evaluation. The four scientific sessions were preflight/audit, candidate, construction/entry, and fixed replay. Every session's code hashes and runtime appear in EXECUTION_LEDGER.json. All completed successfully; there were no failed scientific traversals, refinements, hidden retries or finite-difference evaluations.

| Category | Actual steps | Authorized ceiling |
|---|---:|---:|
| Candidate point traversals: 4 blocks | 3,200 | 19,200 |
| Construction center, X, B: 3 blocks | 2,400 | shared below |
| Optional five entry blocks | 4,000 | shared below |
| Total construction/entry | 6,400 | 76,800 |
| Fixed replay including independent hand derivatives | 8,000 | 76,800 |
| Passive saved-transition preflight | 12 | 12 |
| Inherited prefixes / unstructured rollouts / native kernel updates | 0 / 0 / 0 | 0 / 0 / 0 |

Simultaneous derivative work is separately recorded: point 3,200, construction 1,600, replay 3,200 derivative steps. The two scalar H preparations each constructed 800 intervals and are recorded separately. Supplemental readouts, scalar root bounds, figure rendering and packaging advance no states.

The durable ledger reserves each complete traversal before execution and charges actual attempted steps on normal completion or handled failure; an unhandled process crash leaves the reservation charged. Scientific runtime totals, including conservative process-launch timing, are far below the 1,800/900-second limits. The 250 MB new-result ceiling is checked during packaging. EXECUTION_ACCOUNTING.json records non-scientific preparation and rendering activity as well.

Consumed originals are hashed before and after. HEAD, staged diff and tracked diff are recorded; outside-workspace status is compared without resetting unrelated files. Git reports pre-existing overlong untracked paths in another research lane; those warning paths are recorded, not interpreted as complete coverage of those untracked trees. Consumed hashes and tracked/index checks remain independently available.

All equations, clipping, kernels and accepted research are preserved. The geometry is a passive coordinate instrument. The explanatory figure uses only saved enclosures; its markers are visualization readouts and its rectangle is a certified chart domain, not a physical wall.

The certificate settles one local finite-parameter question and the five specified new futures. It does not classify all initial states, other fixed points, a global basin, branch connection as alpha changes, minimal period, an ambient open neighborhood, or finite-time invertibility. A tiny derivative component or an interval containing zero proves no exact erasure. Within-block convergence follows by the finite-prefix continuity argument; no continuous-time path between discrete states is assumed.
