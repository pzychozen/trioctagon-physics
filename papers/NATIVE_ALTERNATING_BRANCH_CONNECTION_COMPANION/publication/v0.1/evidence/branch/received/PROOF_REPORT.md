# Native alternating-branch connection: proof and verification report

11 November 2026. Codex investigation return for GPT and author review. This is a new computer-assisted mathematical result at the exact frozen parameters, not a manuscript or publication authorization.

## Result and scope

The checked certificate joins the local supercritical M2 branch to the repaired M3 orbit over the entire requested interval

\[
0<\mu\leq 1/200,\qquad \lambda=\lambda_c+\mu.
\]

There is a continuous nontrivial H-exchanged family, smooth in mu away from zero, which tends to the accepted M2 host in its critical direction. Its positively oriented endpoint is strictly inside the exact accepted U_plus. Consequently it is the M3 two-step fixed point by inherited uniqueness. This is a graph over mu; no fold or change of physical parameters is introduced. Uniqueness is asserted in the certified regions, not throughout state space.

Attraction is a separate, narrower conclusion. The new direct two-step derivative certificate proves local quotient attraction on **4999/1000000 <= mu <= 1/200**, with a transformed norm bound below **0.9601**. M2's sufficiently-small-mu attraction and M3's endpoint capture remain inherited. Attraction along the entire connection is unresolved by this investigation. Failed sufficient interval bounds are not stability losses or dynamical obstructions.

The prior-work gate is DISTINCT_GAP within the inspected corpus; see [the completed comparison](PRIOR_WORK_COMPARISON.md). The result is conditional on the accepted M2/M3 premises and the inspected arithmetic implementation. It awaits the commissioned GPT/author review, and is not a proof-assistant or external peer-review claim.

## 1. Exact input chain and inherited premises

The parameters are epsilon=1/20, g=1/5 and k=(1,1.2208964704604097,6.35310346037241), with terminating decimals interpreted as exact rationals. The exact positive host u is the root singled out by M2, enclosed here using the accepted Krawczyk image, not a rounded center. The source's fixed orthonormal V, the larger eigenvalue m1 of V^T M_u V, and lambda_c=(1+1/m1)/9 are recomputed as interval expressions of that same host enclosure. The formulas are those in Paper G Section 4 and [the exact case](packet/EXACT_CASE.json).

The following inputs were located in the existing Paper G v0.1.1 supplement, copied unchanged, and checked against both supplied identities and the recorded commit's actual blobs:

| Input | SHA-256 | Role |
|---|---|---|
| [M2 certificate](sources/m2_accepted_certificate.json) | 6fe4f3f314db1332712b31fed8f7a64cfcee892b9c07782018ea38d3749444a8 | Accepted host box/image, spectrum, normalized critical vector and cubic coefficient |
| [M3 support](sources/m3_accepted_support.json) | 10c4f505f11f1c85c87e3a91e76f61c36e2119a023b13d6dc26af77f9289ddb3 | Exact rational U_plus and positive weights |
| [M2 joint acceptance](sources/M2_JOINT_ACCEPTANCE.md) | 17087119faf01256aea8c8673dacdfaf9c842eeaddedd2440ef958ad1c4537ce | Final local theorem and corrected normalization |

The correction and assent records are also copied and authenticated. Full paths, byte counts, Git blobs and source checkpoint are in [INPUT_IDENTITIES](logs/INPUT_IDENTITIES.json). The source checkpoint is a locator, not a reset target. No original host, jet, entrance or historical theorem checker was rerun. The positive M3 norm weights were read as exact rational strings; the new endpoint proof uses the stored Up endpoints directly. Um remains only the historical outer image enclosure and is unused in the new connection proof.

Inherited M2 facts are: the host and its unique local box; the exact compression B(lambda)=(1-9 lambda)B0; 0<m2<m1<1; the real-block spectrum in (0,0.7); sigma=9m1>0; the corrected positive coefficient 0.0865248497217<c_nf<0.0865248497219; and the unique local H-exchanged cycle at sufficiently small positive mu, attracting modulo common phase. Inherited M3 supplies the unique two-step fixed point in Up and the repaired index-301 entrance theorem at mu=1/200. Neither premise by itself supplies a branch connection.

## 2. The unchanged equation and the removable formulation

On the source slice s(z)=u+xi+i V eta and its positive gauge, use

\[
G(z,\mu)=\widehat F_\mu(z)-Hz,
\qquad H(\xi,\eta)=(\xi,-\eta).
\]

All three amplitude prestages use the same old state; all phase kicks use the same complete prestage. The branch remains in a certified regular domain. Thus the source Arg0(0)=0 convention and separate lambda=0 convention are preserved but never invoked by a singular prestage in this computation. Common-phase and conjugation equivariance are used only on this regular domain.

Let e be the exact unit m1 eigenvector in quotient coordinates, using the accepted sign

\[
e=\frac{(B_{0,12},m_1-B_{0,11})}
 {\|(B_{0,12},m_1-B_{0,11})\|},\qquad e_\perp=(-e_2,e_1).
\]

For unknown x=(X_A,X_B,X_C,y,nu), define

\[
t=\mu/\nu,\quad a=\sqrt t,\quad
\xi=tX,\quad\eta=a(e+t y e_\perp),\qquad \nu>0.
\]

The exact normalization is e^T eta=a. In particular every solution with mu>0 is nontrivial. The opposite sign of a gives its H partner, not a separately identified branch. Fixing mu>0, the coordinate transformation has determinant t^5/(2 nu) in the oriented (e,e_perp) imaginary basis. It is therefore nonsingular. This is a mathematical chart change, not a new native state or a time-dependent parameter schedule.

The regularized equations are

\[
R_R=\frac{\widehat F_R(tX,a(e+t y e_\perp);t\nu)-tX}{t},
\qquad
R_I=\frac{\widehat F_I(tX,a(e+t y e_\perp);t\nu)+a(e+t y e_\perp)}{a^3}.
\]

Here Fhat_R is the real displacement from u, and the displayed map parameter is mu. These expressions are implemented by removable formulas, never by evaluating 0/0 or by dropping a remainder.

### Exact regular evaluation

Write the input as u+tX+i a b, where b=V(e+t y e_perp). Its prestage is p+i a q, with

\[
\begin{aligned}
p_i&=u_i+t\{(J_RX)_i-\epsilon[3u_i tX_i^2+u_i b_i^2+t^2X_i^3+tX_i b_i^2]\},\\
q_i&=(M_u b)_i-\epsilon(2u_i tX_i b_i+t^2X_i^2b_i+t b_i^3).
\end{aligned}
\]

The only use of the exact host equation here is the constant prestage p(0)=u. For each pair set

\[
P_{ji}=p_jp_i+tq_jq_i,\quad Q_{ji}=q_jp_i-p_jq_i,
\quad r_i=(p_i^2+tq_i^2)^{1/2}.
\]

The original harmonic phase sine equals a(3P_ji^2 Q_ji-t Q_ji^3)/(r_j^3 r_i^3). Therefore delta_i=a d_i, where

\[
d_i=(\lambda_c+t\nu)\sum_{j\ne i}
\frac{3P_{ji}^2Q_{ji}-tQ_{ji}^3}{r_j^3r_i^3}.
\]

This is exactly Im((v_j conjugate(v_i))^3)/(|v_j|^3|v_i|^3), so it is independent of principal-argument branch jumps. All denominators are strictly positive in the recorded boxes.

Use the entire functions C(w)=cos(sqrt(w)) and S(w)=sin(sqrt(w))/sqrt(w), defined by their power series. The post-sync real and scaled imaginary components are

\[
o_i=p_i C(td_i^2)-tq_i d_i S(td_i^2),\qquad
j_i=p_i d_i S(td_i^2)+q_i C(td_i^2).
\]

Let h_R=u^T o, h_I=u^T j and D=(h_R^2+t h_I^2)^(1/2). Multiplication by conjugate(u^T F)/|u^T F| gives

\[
\widetilde o_i=(o_i h_R+t j_i h_I)/D,\qquad
\widetilde j_i=(j_i h_R-o_i h_I)/D.
\]

This is the source's positive gauge: its u-projection is the positive real number |u^T F|. It changes coordinates, not the map.

The code propagates exact divided differences f(t)=f0+t f1(t). For example,

\[
(fg)_1=f_1g_0+f_0g_1+t f_1g_1,\qquad
(f/g)_1=(f_1g_0-f_0g_1)/(g_0 g(t)),
\]

and (sqrt(f))_1=f1/(sqrt(f0)+sqrt(f(t))). These are exact identities, not truncated Taylor jets. The critical compression implies exactly tilde(o)(0)=u and V^T tilde(j)(0)=-e. Accordingly R_R=tilde(o)_1-X and R_I=V^T tilde(j)_1+y e_perp. Rounded residual constants are never substituted for either cancellation.

For C and S the implementation uses C(w)=1+w C1(w), S(w)=1+w S1(w). C1 and S1 have coefficients (-1)^(n+1)/(2n+2)! and (-1)^(n+1)/(2n+3)!, respectively. Eighteen terms are retained. For |w|<=1 the omitted value tails are bounded by 2/38! and 2/39!, and their derivative tails by 36/38! and 36/39!. Successive absolute-term ratios, including derivative ratios, are below 1/2. These explicit tails are added outward to both values and automatic derivatives. The certificate actually gives delta_i^2<0.0823 throughout; no short-kick estimate from the unrelated turning-capture family is reused.

The positive denominators at zero and these entire expressions give a real-analytic extension of R in (mu,X,y,nu) near mu=0, nu>0. For negative auxiliary t near zero this is merely the analytic extension of the regularized equations; no negative-mu native trajectory or additional physical family is computed.

## 3. Anchor to M2, including the limiting Jacobian

Let q_c=(0,e) denote the source's unit critical vector. At zero the equations are

\[
R_R=(J_R-I)X+\tfrac12\mathcal B_R(q_c,q_c),
\]

\[
R_I=(B(\lambda_c)+I)y e_\perp-\sigma\nu e
       +\mathcal B_I(q_c,(X,0))+\tfrac16\mathcal C_I(q_c,q_c,q_c).
\]

Thus X0=w_R/2 in the accepted convention. With
T= B_I(q_c,(X0,0))+C_I(q_c,q_c,q_c)/6 and gamma=1-m2/m1>0,

\[
\nu_0=e^TT/\sigma=c_{\rm nf}/\sigma>0,\qquad
y_0=-e_\perp^TT/\gamma.
\]

The full limiting Jacobian is block lower triangular: upper left J_R-I, upper right zero, and lower right columns gamma e_perp and -sigma e. The lower-left coupling through X is retained. Both diagonal blocks are invertible, so the complete five-dimensional limiting Jacobian is nonsingular. No inference from isolated diagonal entries is used.

The onset certificate proves a root at mu=0, strictly inside a small refinement box that lies inside the first uniform patch. The independent source checks place the accepted w/2 and c_nf/sigma enclosures inside the corresponding refined root enclosures. Approximate values are X0=(-0.2974355705,-0.3116473022,-0.3808921093), y0=-0.001495808834 and nu0=0.022181967628; the rational intervals, not these displays, are authoritative.

The first patch is the explicit interval **0 <= mu <= 1/25600**. It proves a unique normalized solution throughout that interval, with nu>0. Reconstructing gives z(mu)->0, eta/a->e and xi/a^2->X0 as mu decreases to zero. The resulting nontrivial H-cycle has exactly the M2 critical direction and positive unfolding. The accepted local cycle is unique near the host up to its H parity. Equivalently, its odd/even expansion, reparameterized by the exact projection a=e^T eta, has these same limiting X0,y0,nu0; local uniqueness of the regularized equations identifies the germs. Hence this is the actual M2 branch.

The uniform first patch, not an unspecified O(mu^2) remainder or a chosen small offset, supplies the quantitative bridge from that germ to finite continuation. No numerical gap to zero is left.

## 4. Uniform patches and actual root identification at joins

For a closed unknown box B=c+[-r,r], a fixed exact-rational matrix A and closed parameter interval I, define T_mu(x)=x-A R(x,mu). All finite decimal centers and A entries in the certificate are selected exact rational numbers; none is claimed to be an exact root or inverse.

The enclosed state derivative J and E=I-AJ yield

\[
q=\max_i\sum_j\sup|E_{ij}|r_j/r_i<1.
\]

For parameter midpoint m and delta=I-m, the center defect is enclosed using

\[
-A R(c,m)-[A\partial_\mu R(c,I)]\,\delta.
\]

Preconditioning occurs before multiplication by the parameter interval. This follows by integrating the derivative of A R(c,mu), with A fixed. Adding E[-r,r] gives the recorded Krawczyk offset. Strict coordinate inequalities |offset_i|<r_i prove a self-map and contraction, uniformly in mu. Banach gives a unique root for each parameter. Because ||I-AJ||<1, AJ is nonsingular; the square matrices A and J are both nonsingular. This explicitly verifies the required inverse condition without treating a floating inverse as exact.

Interval evaluations use dyadic outward supersets of the exact c+[-r,r] boxes. This does not weaken the conclusion: the derivative and regularity bounds hold on those larger convex sets, while the strict self-map is checked against the stated exact rational radii. The same derivative bound also gives uniqueness throughout the evaluated outer box. Analyticity and nonsingularity give locally smooth parameter dependence, and the uniqueness identifications below join these local graphs.

The 128 parameter intervals are exactly

\[
I_i=[i/25600,(i+1)/25600],\qquad i=0,\ldots,127.
\]

They cover [0,1/200] without gaps. The chosen unknown radii are (0.0005,0.0005,0.0006,0.001,0.0001). Every patch passes strict inclusion and has q<0.614. Recorded positive margins throughout the patch family include u^T(u+xi)>8.884, all prestage real parts >1.504, |u^T F|>8.882 and nu>0.02209. These are coarsened displays of checked rational bounds.

At each of the 127 shared parameter endpoints, a separate convex connector box contains both adjacent evaluated unknown boxes. Its derivative defect has weighted norm <0.583. The two already-existing endpoint roots therefore lie in a common uniqueness region and are identical. Mere overlap is not used. Parameter coverage and root matching are separately checked.

For mu>0 the coordinate determinant t^5/(2 nu)>0 and the invertible equation scalings (t I3,a^3 I2) transfer regularity back to G. The selected physical branch is consequently a graph in mu, not merely an unparameterized connected curve. This does not exclude other remote solutions.

## 5. Exact endpoint identity and the inherited full-state consequence

A fresh endpoint refinement at exact mu=1/200 has its entire unknown box inside the last patch's uniqueness region. It therefore selects the same endpoint root. Reconstructing its interval image in the original five quotient coordinates gives strict containment in **values.exact_receipts.Up**, not an intersection or a rounded center comparison. The positive e^T eta parity already lies in Up; no H swap is needed.

Approximate endpoint coordinates are

\[
(-0.06084823646,-0.06367959909,-0.07761457213,
 -0.01014967245,0.43725288805).
\]

The exact containment margins are in EVIDENCE_SUMMARY.json; the smallest is greater than 0.00001098. Since G=0 and H commutes with Fhat, this endpoint is a two-step fixed point in Up. Inherited M3 uniqueness identifies it with the accepted p. No 301-update propagation or withdrawn auxiliary run was repeated.

For every positive mu, eta is nonzero, so Hz differs from z and the quotient period is exactly two. The already-established equivariance algebra also applies to every regular branch point: if A=s(z) and F(A)=exp(i theta) conjugate(A), then

\[
F^2(A)=e^{i\theta}\overline{F(A)}=A.
\]

Thus the branch lifts to genuine full-state two-cycles and their neutral common-phase families. This is an application of inherited symmetry, not a newly invented lift. C, W and Gamma reverse under the H exchange by their inherited oddness and phase invariance. No all-interval nonvanishing of W or Gamma, additional amplitude law, or physical magnetic interpretation is asserted. The M3 entrance theorem now has its endpoint identified with the M2 branch, but no entrance theorem is created at any other mu.

## 6. Separate stability assessment

Root-solver contraction was not treated as a dynamical estimate. A separate implementation differentiates the original cubic prestage, harmonic phase formula and gauge in physical quotient coordinates. At an exact H-cycle, equivariance gives

\[
P=D\widehat F(Hz)D\widehat F(z)=(H D\widehat F(z))^2.
\]

For a chosen fixed rational Q and approximate inverse R_Q, the exact-rational check verifies epsilon_Q=||I-R_Q Q||_infinity<1. Therefore Q is nonsingular and

\[
\|Q^{-1}P Q\|_\infty
\leq\frac{\|R_Q P Q\|_\infty}{1-\epsilon_Q}.
\]

On the full-width continuation boxes these sufficient bounds are inconclusive: all 128 records are retained, with no instability inference. One bounded narrow check on [4999/1000000,1/200] validates a root box inside the last branch patch and obtains a strict dynamical bound <0.9601. The actual bound is approximately 0.9600371643; its rational value is recorded. This proves local attraction of the two-cycle in the quotient throughout that interval. In the full map the common-phase direction remains neutral, so the conclusion is orbital attraction modulo phase.

M2 supplies attraction on some sufficiently small positive interval but no numerical endpoint; M3 supplies its original trapping statement at mu=1/200. This investigation neither joins those stability intervals nor proves a stability loss. The branch connection itself is complete irrespective of that remaining stability question.

## 7. Arithmetic, challenge checks and reproducibility

All new Python runs used Windows Command Prompt with conda activate torment, Python 3.11.15, existing NumPy 2.4.4, mpmath 1.3.0 and SymPy 1.14.0. No dependency was installed. The new integer interval engine uses scale 2^-240: exact rational conversion, outward product/reciprocal, integer-square-root bounds, exact elementary divided identities, and the explicit entire-function tails above. Forward-mode derivatives use product, quotient and chain rules; no finite-difference derivative is a proof bound.

The basic dyadic rounding design was taken from the inspected accepted M2 engine, and the M3 forward-AD design was consulted. Both reference scripts are retained unchanged under sources/reference_implementations and were never imported or executed. The generator and checker share the **new** arithmetic/model implementation. The checker additionally recomputes the decisive contraction, self-inclusion, source, coverage, join, inverse and endpoint inequalities with independently organized exact Fraction arithmetic. Shared analytic replay is corroboration, not a second independent interval engine. The written regularization and identification arguments remain part of the proof.

The checker passed all 128 patches, 127 common-uniqueness joins, onset and endpoint refinements, and the separate stability records. Four controls were rejected: a false coverage endpoint, a connector that did not contain the two roots, substitution of the trivial host as endpoint, and replacement of the accepted trap. A further 31 exact symbolic/normalization/rounding checks passed. These are verification counts, not counts of new theorems.

The frozen nominal budget was 600 root solves and 30 Newton iterations per solve. Actual planning used 130 solves, 389 Newton iterations, and at most three iterations at any node. It used no trajectories or parameter scan outside this family. Six preliminary patch designs are retained; two failed sufficient bounds in the initial design. One full generation and one full checker replay were performed. The 128 broad stability attempts were inconclusive and preserved; the single narrow stability check was not a threshold optimization.

To verify the delivered certificate after extraction, from Command Prompt in the extracted directory:

```bat
conda activate torment
python -B scripts\check_certificate.py
python -B scripts\algebra_checks.py
```

These use only local packet/source/certificate files and existing dependencies; no repository or network access is needed. They write their current check records under data. To retain the supplied records unchanged, verify in a fresh extracted copy. The supplied run_python.cmd records the original machine's activation path. `scripts/execute.py` is the logging wrapper used for the final calculation/check commands. The scripts that initially retrieve local inputs are provenance helpers, not prerequisites for certificate replay.

See [the claim ledger](CLAIM_LEDGER.json), [certificate](data/CONNECTION_CERTIFICATE.json), [checker result](data/CERTIFICATE_CHECK.json), [exact algebra checks](data/ALGEBRA_AND_SOURCE_CHECKS.json), [stability record](data/ENDPOINT_STABILITY_STRIP.json), and [execution log](logs/EXECUTIONS.jsonl). The review ZIP includes the received packet and all copied sources unchanged, the unsuccessful attempts, executable checker, exact manifests and final member-by-member archive audit. No repository, application, kernel or publication files were changed.
