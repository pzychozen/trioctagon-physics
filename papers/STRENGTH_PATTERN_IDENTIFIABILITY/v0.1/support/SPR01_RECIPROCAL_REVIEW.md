# SPR-01 reciprocal review of the additional algebra

**7 October 2026 | DRAFT FOR SCIENTIFIC REVIEW | Disposition: agreement with explicit scope qualifications.**

This note independently checks the four deductions in section 4 of *SPR-01 scientific review* (GPT, 7 October 2026). Reviewer acceptance was not used as a proof. The derivation begins with the recovered native defining equation, with eps=1/20, g=1/5, phase_strength=1/30, k=(1,1,1), ordered channels (A,B,C), and precisely one update of z(a)=a(1,2,1), a>0. No additional native run or robustness experiment was performed.

## 1. Reconstruct the state before checking inverses

The triad Laplacian satisfies L3(1,2,1)=(1,-2,1). Substitution into the amplitude prestage gives

\[
u=z+\frac1{20}z\odot(1-|z|^2)+\frac15L_3z
=\frac a{20}(25-a^2,34-8a^2,25-a^2).
\]

Every prestage component is real. Nonzero phases are 0 or pi, and the native convention assigns zero phase to a zero component. Thus every harmonic-3 sine increment vanishes exactly. The mathematical synchronized output w is u, including at individual cancellations. This argument is about the declared real family; it does not remove the ambient complex map's zero-stratum qualification.

Write x=a^2, s=25-x, r=17-4x and D=s^2+2r^2. Then

\[
w=\frac a{20}(s,2r,s),\quad I_{out}=\frac{a^2D}{200},\quad
\rho^{out}=\frac1{2D}
\begin{pmatrix}s^2&2sr&s^2\\2sr&4r^2&2sr\\s^2&2sr&s^2\end{pmatrix}.
\]

Since D=33(x-161/33)^2+13778/33>0, the normalized output exists for every positive a.

## 2. Signed raw-output inverse: AGREEMENT

Direct cancellation of the cubic terms gives

\[
8w_A-w_B=\frac a{20}[8(25-a^2)-(34-8a^2)]=\frac{83}{10}a,
\qquad a=\frac{10}{83}(8w_A-w_B).
\]

This is a left inverse on the specified family and works also at both individual cancellations. It uses the signed raw amplitudes in the specified real representation and labelled channels. It is not an inverse on generic complex states, nor an operational claim about obtaining signed amplitudes from an intensity detector.

## 3. Normalized-coherence inverse and injectivity: AGREEMENT

For a!=5, the side amplitude is nonzero and

\[
t=\frac{\rho_{BA}^{out}}{2\rho_{AA}^{out}}=\frac{r}{s}
=\frac{17-4x}{25-x},\qquad x=\frac{17-25t}{4-t}.
\]

The equality t=4 would require 17=100 and cannot occur at finite a in this chart. Take the positive square root to recover a. The image of the signed chart is (-infinity,17/25) for 0<a<5 and (4,infinity) for a>5. This range restriction matters: an arbitrary noisy matrix or arbitrary t is not necessarily an output from the family.

For a global argument, let x=a^2 and y=b^2. The reduced vectors (25-x,2(17-4x),25-x) and the corresponding y-vector are never zero. Equality of their normalized rank-one outer products implies that the vectors span the same complex line. Their real nonzero entries make the proportionality factor real, although its sign may be negative. Proportionality requires

\[
(25-x)(17-4y)-(17-4x)(25-y)=83(x-y)=0.
\]

Consequently x=y and, because a,b>0, a=b. The proof includes zero side components; it does not divide by them. Equal full normalized output coherences therefore identify the input amplitude on this family.

This is exact identifiability, not finite-noise reconstruction. The ratio chart divides by a vanishing side population near a=5 and has no value at that point. The original report's bounded floating-point comparisons do not constitute a uniform error bound for this inverse. Relative-phase/coherence acquisition, preparation errors, and coefficient uncertainty remain operational questions without a new error contract.

## 4. Exceptional a=5 point: AGREEMENT

At a=5,

\[
w=(0,-83/2,0),\quad I_{out}=6889/4,\quad
\rho^{out}=\operatorname{diag}(0,1,0).
\]

For positive a, p_B=1 iff s=0, hence iff a=5. It is the unique point outside the side-channel ratio chart and is identified separately. At a=sqrt(17)/2 the middle component vanishes, but rho_AA=1/2, t=0 and the inverse remains valid. At a=0, w=0 and the normalized readout is undefined; no limiting value is substituted.

These cancellations remain outside the nonzero-prestage domain of the accepted general closure statement. Family identifiability at a=5 does not extend that closure statement to other zero-stratum inputs.

## 5. Population ambiguity and opposite coherence: AGREEMENT

At a=2, (s,r)=(21,1). At b=sqrt(382/85),

\[
(s,r)=(1743/85,-83/85)=\frac{83}{85}(21,-1).
\]

After normalization the common scalar cancels. The two coherences are exactly

\[
\rho_{\pm}=\frac1{886}
\begin{pmatrix}441&\pm42&441\\\pm42&4&\pm42\\441&\pm42&441\end{pmatrix},
\]

where + corresponds to a=2 and - to b. Thus all three populations agree, including p_B=2/443, while rho_AB is respectively +21/443 and -21/443. The same sign change occurs in the B-C cross terms. More diagonal measurements cannot distinguish the pair; the stated off-diagonal coherence can distinguish it in exact arithmetic.

This confirms a collision of the population readout, not of the raw state or full normalized output coherence. No finite-error guarantee for resolving the sign is inferred from its nonzero exact difference.

## 6. Relationship to the accepted SPR-01 and RFO-02 results

The four deductions are sound and may be incorporated as proved, family-restricted statements in the v0.1 draft. There is no substantive discrepancy requiring return before incorporation. The new exact identities do not change the accepted SPR-01 data, protocol, population-noise certificate, or entrance/direct-formula comparators.

Input rho is constant along the ray, while output rho distinguishes amplitudes. This is consistent with, and exemplifies, failure of autonomous input-rho closure: the intensity discarded at the entrance affects the update. No general normalized-coherence dynamics or kernel inverse follows. The separate negative RFO-02 fixed-pattern classification result remains intact, and computational advantage is UNESTABLISHED.

The independent exact checker reconstructs the prestage from the defining equation and checks the identities and quoted class endpoints with SymPy rational/algebraic arithmetic. It imports neither predecessor scientific helper functions nor native callables. Its 23 predicates are supporting checks; the proofs above carry the mathematical claims. Private source bindings and preservation records are intentionally outside the manuscript and publication-facing crosswalk.

## Source basis

- Paper A, *Cycle-Covering Dynamics of a Three-State Nonlinear Kernel*, section 1 and section 6.1, equations (6.0), (6.1a,b): defining recurrence and zero convention.
- RFO-02, *Native processing and readout*, sections 1 and 3: fixed coefficients and original same-rho witness; sections 5 and 8: the retained negative classification result.
- *SPR01_REPORT.md*, sections 2-5, and its frozen protocol/results: accepted response and bounded evidence.
- GPT, *SPR-01 scientific review*, section 4: the claims independently checked here; sections 2 and 5 distinguish reviewer execution from original execution evidence.

**Stop for scientific review.** This note authorizes no implementation, new error experiment, generic inversion claim, publication or next research lane.
