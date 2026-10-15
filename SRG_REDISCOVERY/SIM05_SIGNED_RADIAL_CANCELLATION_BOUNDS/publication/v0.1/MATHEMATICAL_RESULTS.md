# SIM05 — Independent pre-evaluation mathematical verification

14 October 2026. New construction proposed by GPT in received/SIM05_MATHEMATICAL_SPEC_v0.1.md; independent derivations checked by Codex before the fixture gate and primary evaluation. All theorems below are real-arithmetic statements. Float64 checks are not outward-rounded interval certificates.

## Authorities and hypotheses

The accepted SIM04 damping derivative, scalar-profile symmetry and complete-pair variance identity are inherited. The subsequent GPT review proves the stronger universal weak ordering P≤K; see review/ADDITIONAL_PROFILE_DOMINANCE_THEOREM.md. Its weighted matching cost C(a,b)=k(min(a,b))²(a−b)² has mixed derivative 4kk'(b−a)−2k²<0 for a<b, and the symmetric expression for b<a. Rectangle integration and uncrossing prove the weighted sorted matching inequality; the signed-to-absolute comparison completes P≤K. This is an inherited reviewer theorem, not a new empirical inference or modification of the original SIM04 report.

For each fixed labeled center take finite nonnegative ascending three-component profiles p,q and the existing valid P_i≥|F(p)−F(q)|. The original coordinate signs and permutations do not affect F; arbitrary rotations generally do. Center labels are never sorted. All differences have orientation c minus d. Denote b(s)=1+log(1+s), d(s)=s/b(s), F(p)=||d(p)||. D/F are proof notation only on source records; production evaluation uses the allowed formulas below, without evaluating the exact readout.

## 1. Squared-coordinate derivative and concavity

Let Φ(z)=z/b(sqrt(z))² for z≥0. For z>0, put s=sqrt(z). The chain rule gives Φ'(z)=d(s)d'(s)/s=k(s)/b(s)=θ(s), where k(s)=[b(s)−s/(1+s)]/b(s)². At zero, Φ(z)/z tends to 1, so the right derivative is 1, continuously matching θ(0).

Independently, k'(s)=[2s−(s+2)b(s)]/[(1+s)²b(s)³]. The positive numerator complement J(s)=(s+2)b(s)−2s has J(0)=2 and J'(s)=log(1+s)+1/(1+s)>0. Thus k>0 and k'<0. Differentiating θ=k/b gives θ'=k'/b−k/[(1+s)b²]<0, including its right derivative at zero. Consequently Φ has a positive decreasing derivative and is increasing and concave on the closed nonnegative half-line. This argument does not use a numerical derivative grid.

## 2. Fixed signed Darboux intervals

For each component x=p²,y=q²,h=x−y, the fundamental theorem of calculus gives Φ(x)−Φ(y)=h times the average of Φ' over [min(x,y),max(x,y)]. Numerically h is evaluated as (p−q)(p+q); the direct-square subtraction is retained as an algebra residual. Five prescribed equally spaced squared-coordinate nodes provide the monotone derivative values t_0,…,t_4. For J=1, the lower/upper averages are t_4,t_0. For J=4 they are (t_1+…+t_4)/4 and (t_0+…+t_3)/4. Signed multiplication requires the minimum and maximum of h times those two bounds; replacing h by |h| would lose the desired sign.

Summing the three signed component intervals encloses F(p)²−F(q)². The four-subinterval lower average is no smaller than the one-subinterval lower average, and its upper average is no larger. The signed intervals, and their sums, therefore nest. If h=0 the component interval is exactly zero; all five derivative slots are still evaluated as prescribed. J=1 reuses endpoints, not additional node evaluations. These are integration intervals, not physical time steps.

## 3. Norm envelopes, rationalization and intersections

With m=||p|| and M=max(p), b(p_a)≤b(M) implies F(p)²≥m²/b(M)². Jensen's inequality for concave Φ gives ΣΦ(p_a²)≤3Φ(m²/3)=m²/b(m/sqrt(3))². Taking nonnegative square roots proves L(p)=m/b(M)≤F(p)≤U(p)=m/b(m/sqrt(3)). Both vanish at zero. These are analytic envelopes even when special inputs make one exact; no componentwise exact F sum is needed.

Unless both profiles vanish, D_low=L(p)+L(q)>0 and D_high=U(p)+U(q). Rationalization yields δ=[F(p)²−F(q)²]/[F(p)+F(q)]. A continuous quotient on a numerator interval times a positive denominator interval attains its extrema among the four endpoint quotients: monotonicity in the numerator and sign-dependent monotonicity in the denominator suffice. This avoids an invalid fixed-denominator choice when the numerator changes sign.

Intersect the quotient interval with [L(p)−U(q), U(p)−L(q)] to obtain the raw radial interval. Then intersect with [−P_i,P_i]. Both intersections are valid since each interval contains the same δ. They are input-only prior intersections, not correction against observed outcomes. Retain original endpoints, the quotients, endpoint-source flags, and the separate prior activity. If p=q=0 define [0,0] without division. If p=q≠0 then every signed numerator is exactly zero and the interval is [0,0]. Refinement nesting survives each fixed intersection. In real arithmetic no intersection is empty.

Numerical inversions are not hidden: width inversion>1e−12 stops; a smaller positive inversion is recorded and replaced by its outward hull, with roundoff-unresolved flags. Endpoint activity is recorded before that hull. No fitted padding, denominator epsilon or silent point collapse is allowed. Underflow/overflow/invalid floating operations stop. These rules do not turn float64 into formal interval arithmetic.

## 4. Signed averaging, uncertainty and lower bounds

Write each effective interval [l_i,r_i] as μ_i±ε_i, with ε_i≥0. Averaging all eight centers gives [mean(l),mean(r)]=mean(μ)±mean(ε). Its absolute upper endpoint is B_signed=|mean(μ)|+mean(ε). Taking absolute values before averaging gives B_unsigned=mean(|μ|)+mean(ε), using exactly the same intervals. Their difference is mean(|μ|)−|mean(μ)|≥0, with no claim that a midpoint is the true difference. Retain the remaining radius explicitly.

The absolute lower bound is zero if the collective interval contains zero, otherwise the lesser endpoint magnitude. Thus A_J≤|Δu|≤B_signed,J≤B_unsigned,J≤mean(P_i). The last inequality follows because every effective center interval lies in [−P_i,P_i]. J=4 nesting yields A_4≥A_1, B_signed,4≤B_signed,1 and B_unsigned,4≤B_unsigned,1. Equality is possible. The same aggregation is retained for raw pre-P intervals, without asserting they are below P.

Signs are resolved positive only for l>1e−12, negative only for r<−1e−12, otherwise unresolved. Any interval affected by the prescribed inversion hull is also flagged roundoff-unresolved. An interval containing zero supplies no preferred sign. Synthetic sign/center cancellation examples test, but do not prove, these identities.

## 5. Two-sided population dispersion

For m scalars, Σ_(c>d)(u_c−u_d)²=mΣu_c²−(Σu_c)²=m²Var(u), where variance is ddof=0. Squaring the nonnegative pair lower/upper bounds and summing therefore gives W_low=ΣA²/m²≤Var(u⁺)≤W_high=ΣB_signed²/m². Use all ten unordered pairs for m=5, and the six already evaluated pairs with indices 1–4 for m=4. Denominators are 25 and 16. Joint attainability of all pair endpoints is unnecessary for validity; sharpness is not implied.

For either incoming or pre-damping reference variance, W_high<V_ref suffices for decrease and W_low>V_ref suffices for increase. Neither condition being met determines no direction. Both comparisons and the actual V_ref−V_post are kept separate. Numeric test margins must exceed 1e−14; opposite margins below −1e−14 are NOT_ESTABLISHED and the closed band is UNRESOLVED. Exact zero is separately counted. A pass against a resolved opposite actual change is a QA contradiction.

For ε≥0, B_signed≤ε implies the paired speed difference≤ε, and W_high≤ε² implies SD≤ε. No ε is chosen from outcomes. Aggregate SD is sqrt(mean phase variance), not mean phase SD.

## 6. Post-seal diagnostic ladder and scope

After joining saved signed center differences, let S=|mean δ_i|. Subtraction gives exactly P−S=(P−B_unsigned,4)+(B_unsigned,4−B_signed,4)+(B_signed,4−S). The three nonnegative real-arithmetic gaps locate within-center enclosure improvement, extra signed-averaging benefit, and remaining slack. They are not causal shares. All raw signed float residuals remain available, including differences from separately reduced accepted collective means.

All proposed formulas are valid under their stated hypotheses; no mathematical replacement is required. The new method retains more scalar information while conditioning on realized sequential profiles. It does not change the dynamics, establish contraction of a complete update or imply long-time convergence. Any certificate counts and degree of tightness remain empirical questions for the single bounded pass, after the fixed fixture gate.
