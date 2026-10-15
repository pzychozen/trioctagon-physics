# SIM04 — Finite-step collective-speed bounds
## Mathematical specification v0.1 · 14 October 2026

**Status:** New proposed derivations and a fixed analysis design, supplied by GPT for Codex to verify and evaluate. These are not numerical results of SIM04 or additional findings attributed to SIM03. The model, saved histories and previously accepted science remain unchanged.

**Question:** How informative is the existing bound on the difference between two collective mean-speed responses? Can preserving difference alignment and the component information relevant to damping give a materially tighter bound, and what explicit sufficient conditions on these quantities control phasewise dispersion?

The inherited starting point is `reference/SRG_NEXT_MATH_FINITE_STEP_DISPERSION_NOTE_20261014.md`. Its authorizations were deferred at issuance. The accompanying work order now authorizes this particular saved-intermediate investigation. The new component and component-profile bounds below are source-derived extensions proposed for this task, not quotations from that earlier note.

## 1. Variables and the information boundary

At a fixed repeated-driving phase j, compare cycles c and d. There are N=8 labeled centers. Use the accepted SIM03 arrays:

- v_(c,i): incoming velocity;
- a_(c,i): already reconstructed, signed source impulse;
- w_(c,i)=v_(c,i)+a_(c,i): already stored pre-damping velocity;
- y_(c,i): saved successor velocity, reserved for the outcome/diagnostic side of the analysis.

In real-valued notation the successor is D(w), where D acts componentwise and

    D(x) = x / [1 + log(1+|x|)].

Let u_c=mean_i ||v_(c,i)||, U_c=mean_i ||w_(c,i)|| and u_c^+=mean_i ||y_(c,i)||. These are incoming, pre-damping and saved post-damping mean speeds, not mean squared speeds or RMS speeds.

For interpretation of the impulse, use the stored sequential displacement d_(c,i), successor bit sign s_(c,i), and the actual saved H and G:

    alpha_j = 0.1 H_j,       h_j = |alpha_j|,
    g_(c,i) = s_(c,i) d_(c,i)/(||d_(c,i)||+0.01),
    a_(c,i) = alpha_j G_c g_(c,i),       G_c = 1/(1+u_c).

Here **g is signed normalized geometry**; do not use z for it, because SIM03's `z` is reconstructed post-damping velocity. The stored `d` already incorporates C's sequential mixed-position centroid. Do not reconstruct it again from positions. H may be negative. No RNG operation is needed: successor bits are recorded outcomes.

The factorized expression describes the real-valued source. Use the accepted stored impulse and w for the numerical bound evaluations; assess equivalence to the factorization at the declared tolerance rather than replacing their source arithmetic grouping.

All proposed analytic bound functions may read only incoming velocities, signed impulses, stored pre-damping vectors, stored d, successor bit signs, H and G. They may calculate g and derivatives of D. They must not read saved successor velocities, stored z/t/post_norm/retention/loss, or observed dispersion. The outcome arrays are joined only after these bounds are fixed. The stored w and impulses are **realized sequential intermediates**, so this is a conditional one-step analysis, not a forecast from initial positions or from mean speed alone.

## 2. Baseline and source-separated bounds

Use Delta v_i=v_(c,i)-v_(d,i), Delta a_i=a_(c,i)-a_(d,i), Delta w_i=w_(c,i)-w_(d,i), and

    S_cd = |u_c^+ - u_d^+|,
    V_cd = mean_i ||Delta v_i||,
    J_cd = mean_i ||Delta a_i||,
    Rg_cd = mean_i ||g_(c,i)-g_(d,i)||,
    qbar_c = mean_i ||g_(c,i)||.

S is an outcome, not a bound input. In the real-valued model:

    S_cd <= Q_cd := mean_i ||Delta w_i||
                    = mean_i ||Delta v_i + Delta a_i||.

Proof: absolute value of a mean is no greater than the mean absolute value; the reverse triangle inequality for norms bounds each scalar-speed difference by the successor vector distance; SIM03's damping nonexpansion bounds that by ||Delta w_i||.

The following coarser bounds separate the ingredients without asserting causal attribution:

    T_cd = V_cd + J_cd,

    Gamma_(c|d) = V_cd + h_j [|G_c-G_d| qbar_c + G_d Rg_cd],
    Gamma_(d|c) = V_cd + h_j [|G_c-G_d| qbar_d + G_c Rg_cd],
    Gamma_cd = min(Gamma_(c|d), Gamma_(d|c)),

    Omega_cd = (1+h_j) V_cd + h_j min(G_c,G_d) Rg_cd.

To prove Gamma, expand G_c g_c-G_d g_d in the two indicated orders and use triangle inequalities. To prove Omega, use qbar<=1 and

    |G_c-G_d| = |u_c-u_d|/[(1+u_c)(1+u_d)] <= V_cd.

The complete coarse hierarchy is

    S_cd <= Q_cd <= T_cd <= Gamma_cd <= Omega_cd.

The source-dependent inequalities are exact in the stated real-valued notation; numerical evaluations use tolerance, not a claim of bitwise identity of algebraic rearrangements.

### Difference alignment is distinct from SIM03's within-state alignment

Record, for every center pair,

    ||Delta w_i||^2 = ||Delta v_i||^2 + ||Delta a_i||^2
                       + 2 Delta v_i dot Delta a_i.

This new cross-history alignment can be positive or negative. It is **not** SIM03's 2 v_i dot a_i for a single history. Negative difference alignment can reduce Q relative to the separated triangle bound T. Record the signed term, the direct triangle slack, and a cosine only when both difference norms are nonzero. Do not divide by a nearly cancelling net change. Compute Q directly from stored w differences, not by taking a square root of a cancellation-prone expanded expression.

## 3. Sharpening A: component-interval damping bound

For s>=0, define b(s)=1+log(1+s) and

    k(s) = [b(s)-s/(1+s)]/b(s)^2.

Then D'(x)=k(|x|), including D'(0)=k(0)=1. SIM03 established 0<k<=1. A further source-derived fact proposed here is that k decreases with s:

    k'(s) = [2s-(s+2)b(s)] / [(1+s)^2 b(s)^3] < 0.

For a proof, put J(s)=(s+2)b(s)-2s. J(0)=2 and

    J'(s)=log(1+s)+1/(1+s)>0.

Consequently J(s)>0. This proof, rather than a derivative grid search, determines the interval maximum.

For each component of two pre-damping vectors x=w_(c,i) and y=w_(d,i), let

    ell_a = 0, if the closed interval between x_a and y_a contains zero;
            min(|x_a|,|y_a|), otherwise,
    kappa_a = k(ell_a).

Test interval containment with comparisons, not multiplication of endpoints that could overflow. The mean-value bound gives

    |D(x_a)-D(y_a)| <= kappa_a |x_a-y_a|.

Define

    K_i = sqrt(sum_a kappa_a^2 (x_a-y_a)^2),
    K_cd = mean_i K_i.

Then

    S_cd <= K_cd <= Q_cd.

When intervals include zero their coefficient is one; do not invent a uniform strict contraction constant. This is a bound on the damping of two **specified pre-damping vectors**, not a global contraction theorem for C's coupled dynamics.

## 4. Sharpening B: the scalar-relevant component profile

The output mean speed discards more information than a labeled vector distance. D is odd and applies the same scalar function to each coordinate. Therefore the scalar F(w)=||D(w)|| is unchanged by coordinate sign changes and permutations.

Define p(w) as the three absolute component magnitudes of w, sorted in **ascending** order. This is a derived diagnostic vector, never an evolving state:

    F(w) = ||D(p(w))||.

For x=p(w_(c,i)), y=p(w_(d,i)), all coordinates are nonnegative. Define

    lambda_a = k(min(x_a,y_a)),
    P_i = sqrt(sum_a lambda_a^2 (x_a-y_a)^2),
    P_cd = mean_i P_i.

The same component mean-value argument gives

    S_cd <= P_cd.

Also P_cd<=Q_cd. To prove this, first use lambda<=1. Sorting two real nonnegative triples in the same order minimizes their squared matching distance: expand the squares and apply a pairwise exchange argument to the dot product. Thus

    ||p(x)-p(y)|| <= || |x|-|y| || <= ||x-y||.

Apply this centerwise to the original pre-damping vectors. This does not assert an ordering between P_cd and K_cd; measure both separately. Their fixed, valid lower envelope is

    Bbest_cd = min(K_cd,P_cd),
    S_cd <= Bbest_cd <= Q_cd.

Sorting is **not** arbitrary rotation, center relabeling, geometric alignment, alteration of source coordinate conventions or another model. It uses only exact symmetries of the scalar damping readout. Equal Euclidean norms with different component magnitudes need not have equal output norms; the axis/equal-component example remains an essential fixture. The profile bound does not assume rotation invariance.

No exact output secant, observed loss, reconstructed D(w) endpoint, or observed speed is allowed in these analytic bounds. A calculation that uses the exact output difference to reproduce that same difference is not a sharper explanatory bound.

## 5. Population dispersion requires all pairs

For a cycle set C of size m, at fixed phase j,

    Var_C(u^+) = (1/m^2) sum_{c>d in C} (u_c^+-u_d^+)^2.

This is population variance (ddof=0). Equivalently the ordered-pair expression has denominator 2m^2. The unordered-pair denominator is **m^2, not the number of pairs**.

For any of Omega, Gamma, T, Q, K, P, Bbest, write the pair bound as B_cd and define

    W_B(C,j) = (1/m^2) sum_{c>d in C} B_cd,j^2,
    E_B(C,j) = sqrt(W_B(C,j)).

Then Var_C(u^+)<=W_B and the population standard deviation is <=E_B. Use every unordered pair: ten for C={0,1,2,3,4}, six for C={1,2,3,4}. The six new-four pairs are a subset, not six additional independently evaluated pair families. The three pairs absent from SIM03's seven-pair report are (3,1), (4,1), (4,2). Their bounds and outcomes are new saved-data comparisons here, not new trajectories.

Take min(K,P) **at each pair before** squaring and summing for Bbest. Keep both individual families for interpretation. There is no fit, learned coefficient, selected phase window or outcome-driven choice of the bound family.

### Explicit sufficient conditions to report

These are conditional mathematical implications, not assumed outcomes:

1. If B_cd<=epsilon, the corresponding output mean speeds differ by at most epsilon.
2. If W_B<=epsilon^2, the selected cycles' output population SD is at most epsilon.
3. If W_B<=Var_C(U), the bound is sufficient for scalar-dispersion nonincrease across the damping stage for the specified pre-damping ensemble.
4. If W_B<=Var_C(u), it is sufficient for output scalar-dispersion nonincrease relative to the incoming ensemble, **conditional on these realized sequential impulses and bits**.

Evaluate conditions 3 and 4 separately, using Bbest, and report their margins. Compare them with the actually measured pre/post and incoming/post variance changes. An inconclusive sufficient condition is not a counterexample to the bound and does not imply that actual dispersion increased. A passing phase does not imply future-cycle convergence, a full-state contraction, or closure of dynamics on scalar mean speed.

All five/new-four moments concern correlated histories. There are no independent-trial confidence intervals, p-values or statistical generalization. Near equality of phase-averaged incoming/outgoing spreads retains the already accepted reindexing caveat; do not rediscover it as regulation.

## 6. Locate why an upper bound is loose, without using outcomes to build it

After analytic bound arrays are frozen, separately form from saved successors:

    Zsigned = mean_i ||y_(c,i)-y_(d,i)||,
    Zprofile = mean_i ||p(y_(c,i))-p(y_(d,i))||,
    Tnorm = mean_i | ||y_(c,i)|| - ||y_(d,i)|| |,
    S = |mean_i ||y_(c,i)|| - mean_i ||y_(d,i)|| |.

Check Tnorm<=Zsigned<=K and Tnorm<=Zprofile<=P, with S<=Tnorm. For a tie K=P choose K deterministically. Select Zstar=Zsigned when Bbest=K and Zstar=Zprofile otherwise. The following decomposition is exact algebra:

    Q-S = (Q-Bbest) + (Bbest-Zstar) + (Zstar-Tnorm) + (Tnorm-S).

All four terms are nonnegative in the real-valued bound setting. Respectively they locate improvement from the fixed sharpening, remaining damping-bound slack, the norm-projection inequality, and cancellation of signed center-speed differences during averaging. These are **gaps in an inequality chain**, not fractions of physical dynamics caused by different mechanisms.

Record the signed center speed differences rather than just their magnitudes. Also record T-Q to show what was lost by separating Delta v and Delta a. Inspect fixed largest-gap and weakest-bound locations from the completed tables, not from additional reconstruction passes.

## 7. Numerical interpretation and proof standard

Codex must verify every derivation before empirical evaluation. These are real-valued inequalities evaluated on stored float64 data; numerical passes at tolerances are not outward-rounded interval certificates. Preserve signed residuals and worst-case locators.

Use absolute tolerances from the companion experiment specification. No clipping of inequality gaps, no epsilon inserted into a theorem, and no altered source parameters. Display-only masks and plotting conveniences must not overwrite raw values. Expected undefined ratio cases get a mask and null/blank, not zero or infinity.

A useful answer can be that Q is loose, that one fixed sharpening is helpful, or that the best proposed upper bound still fails to account tightly for the scalar similarity. State the numerical degree of improvement and the retained information required. Do not choose the conclusion in advance.
