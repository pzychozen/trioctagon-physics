# Proposed analytical start — not an accepted result

**Task:** NATIVE_ALTERNATING_BRANCH_CONNECTION_01.  
These are GPT's proposed ways to attack the connection. Codex should challenge the algebra, the normalization and all proof conditions. No new continuation calculation or certificate was executed while preparing this guide.

## 1. Why the symmetric equation is a useful reduction

Paper G supplies a smooth regular quotient with H-equivariance and a nontrivial H-exchanged local two-cycle. On that chart,

\[
G(z,\mu)=\widehat F_\mu(z)-Hz=0
\]

implies the two-step equation by equivariance. With eta nonzero, H z differs from z, so the quotient period is exactly two. The inherited full-state lift then applies. This is a smaller root problem than treating two independent five-coordinate points, and exposes the trivial host root z=0 that exists at every mu.

Do NOT confuse a fixed point of H composed with Fhat with a fixed point of Fhat. Their stability problems are different. Also, H-exchanged continuation near the M3 endpoint alone does not prove a connection to onset.

## 2. A smooth gauge without an argument branch

For Psi=F_lambda(s(z)), set h=u^T Psi. Where h is nonzero, the quotient can be expressed by multiplying Psi by conjugate(h)/|h| and taking its real displacement from u and its V-projected imaginary part. This should agree exactly with the source's positive gauge. Derive and check that agreement and its derivatives; a valid chart change cannot change the map.

Similarly, on nonzero prestages the source phase sine can be evaluated by

\[
\sin(3[\arg v_j-\arg v_i])=
\operatorname{Im}((v_j\overline{v_i})^3)/(|v_j|^3|v_i|^3).
\]

This avoids artificial principal-argument jumps, but every denominator still needs a strict lower bound.

## 3. Proposed amplitude regularization of the onset

Let e be an exact unit critical eigenvector of B0=V^T M_u V for m1, and let e_perp be an orthonormal complement. Choose its sign consistently; the H partner is the opposite parity of the same cycle. Put a real amplitude a, t=a^2, and consider

\[
\xi=tX,\qquad \eta=a(e+t y e_\perp),\qquad \mu=t\nu.
\]

The unknowns for fixed t are X in R^3, y in R and nu in R: five unknowns. The gauge condition e^T eta=a is exact. This is a coordinate ansatz near the critical direction, not an additional dynamical state or a physical clock.

Split Fhat into real and imaginary slice components. A candidate divided system is

\[
R_R=\frac{\widehat F_R(tX,a(e+t y e_\perp);t\nu)-tX}{t},
\qquad
R_I=\frac{\widehat F_I(tX,a(e+t y e_\perp);t\nu)+a(e+t y e_\perp)}{a^3}.
\]

Here the parameter argument of Fhat is mu, not lambda itself. Its real component is H-even and its imaginary component H-odd. The host is fixed for every mu. The critical relation (B(lambda_c)+I)e=0 cancels the apparent order-a term. These facts suggest removable extensions at t=0. **Derive those extensions before using the divided expressions; never evaluate 0/0 or discard a Taylor remainder.** Prove the regularity needed by the chosen implicit-function or validated local theorem.

The proposed limiting real equation is

\[
(J_R-I)X+\tfrac12\mathcal B_R(q,q)=0,\qquad q=(0,e),
\]

so X0=w_R/2 in Paper G's convention. Let

\[
T_I=\mathcal B_I(q,(X_0,0))+\tfrac16\mathcal C_I(q,q,q),
\quad \sigma=9m_1.
\]

The limiting imaginary equation should be

\[
(B(\lambda_c)+I)y_0e_\perp-\sigma\nu_0 e+T_I=0.
\]

Its e projection proposes nu0=c_nf/sigma>0; the transverse coefficient is 1-m2/m1>0 and determines y0. These are deductions to verify from the accepted jet normalization, not substitute certificate values. The simple crossing, invertible real block and noncritical imaginary eigenvalue suggest an invertible five-dimensional limiting Jacobian. Check the complete Jacobian and the allowed unknown dependence rather than inferring it from selected diagonal entries.

This construction offers a route to an explicit validated branch anchored at onset, instead of guessing that an arbitrary small numerical mu lies in M2's unspecified local range. If using t as a continuation parameter, prove how its mu(t) covers the intended interval. Monotonicity mu'(t)>0 would justify a graph in mu, but must be checked, not presumed. A fold does not automatically mean branch disconnection.

It is also legitimate to choose a different Lyapunov–Schmidt, center-manifold remainder or regularized system. What is mandatory is a rigorous anchor and no gap to the subsequent continuation interval.

## 4. A simple sufficient continuation-patch test

For a regular root problem G(x,mu)=0 away from onset, a possible patch proof uses a fixed verified nonsingular matrix A and

\[
T_\mu(x)=x-A G(x,\mu).
\]

For every mu in a specified closed parameter interval, prove that T_mu maps the complete chosen state box into itself and that its state derivative has norm bounded by a uniform q<1 there. Then the root in that box is unique and exists for each parameter; the contraction equation and continuity give continuous dependence. This elementary sufficient route may be conservative. A different interval-existence theorem is acceptable with its hypotheses explicitly verified.

Adjacent patch boxes intersecting is not enough. Validate a connector region containing both endpoint root enclosures with a uniqueness certificate, or another rigorous root-identification argument. Keep exact coverage endpoints and all overlap certificates in the new evidence.

At mu=1/200, containment in the accepted U_plus, up to a declared H parity, identifies the root with M3 by the inherited uniqueness theorem. No new 301-step entrance calculation is required.

## 5. Claims deliberately left undecided

The guide does not assert that the candidate divided system stays regular up to the endpoint, that the branch is monotone in mu, that it remains attracting, or that W and Gamma stay nonzero throughout. Those are possible outputs of the investigation. Neither this guide nor favorable nominal continuation proves them.

No new physical magnetic field, gravity mechanism, continuous time, moving support, or transport law is proposed. The purpose is to determine whether the existing native onset theorem actually explains the identity of the existing finite-amplitude alternating cycle.
