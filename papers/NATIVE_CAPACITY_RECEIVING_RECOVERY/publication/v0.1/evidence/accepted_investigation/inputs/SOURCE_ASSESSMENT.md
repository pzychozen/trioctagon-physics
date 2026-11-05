# Source-based assessment — NATIVE_CAPACITY_RECEIVING_RECOVERY_01

**Prepared:** 5 November 2026. **Research author:** Hilmir Frímann Halldórsson (pzychozen).
**Formulation:** GPT. **Status:** new proposed argument for independent Codex investigation; not an accepted theorem.

## 1. What is established, and the precise next gap

P4, *Finite-Time Access to Native Projection Capacity*, is published at `bcfffc64ac5a62290763041b3cbe6fcac2fdbfb6`. Its Theorem 3.1 proves, at yaw pi/4 and for the coherent empty launch, that

\[
\sigma_{\rm ext}\le\nu/2\quad\Longrightarrow\quad
E_{\rm out}(t_A)>\frac{1053}{4096}C>\frac14 C,
\qquad t_A=1/\nu,\quad C=C_{\rm joint}=\alpha_N(1-\cos\phi).
\]

P4 explicitly leaves receiver allocation and later recovery of that capacity-sized stock unproved. P3's receiver and recovery fractions have a different sufficient regime. The next task is to connect capacity-scale access, reception and net native recovery along one unchanged solution. No tagged parcel or energy cohort is assumed.

The proposal below uses a narrower but nonempty subfamily of P4. It keeps the native response active in a coupled linear reference near the zero-drive aligned state, then bounds the **actual nonlinear, positive-speed solution** against that reference over a fixed finite window. This is not the earlier frozen-core comparison.

Read `CLAIM_SOURCE_MAP.md` for precise source labels. Source copies and historical execution records are byte-preserved; the calculations labelled PR below are new proposals, not claims already present in those publications.

## 2. Compatibility audit: why the old certificate cannot simply be joined

P3 defines, with its notation, \(\omega=\sqrt{m/\beta_R}\), \(S=2\pi/\omega\), \(\Lambda=\sqrt{\beta_R}|f_0|\), \(A=\nu^2F_{\max}/2\), and \(B_2=\sqrt m A S^3/3\). Its sufficient threshold includes

\[
\kappa^2\ge\frac{2B_2}{q\Lambda},\qquad 0<q\le1/5.
\]

Consequently, the proposed exact substitution gives

\[
\left(\frac{\kappa\omega}{\nu}\right)^2
\ge\frac{8\pi^3F_{\max}}{3q|f_0|}
\ge\frac{8\pi^3}{3q}>\frac14. \tag{PR01}
\]

P4's sufficient condition instead implies \((\kappa\omega/\nu)^2\le1/4\). Codex should verify this incompatibility of the **published sufficient certificates**. It is not a proof that the underlying behaviors cannot coexist, nor a necessary restriction on the dynamics. The new route must not import P3's 80/81 guarantee or P2's returning-power conclusion.

## 3. Proposed restricted finite regime and target

Retain the original equations and all P4 geometric/profile assumptions. In addition to fixed yaw \(\delta_g=\pi/4\), select the fixed finite positive coefficients so that

\[
\gamma:=c\sqrt{d/m},\qquad
\omega_R:=\kappa\sqrt{m/\beta_R}=\frac\nu3,
\qquad 0<\frac\gamma\nu\le\frac1{100}. \tag{PR02}
\]

These choices are made **before the phase**. For each

\[
0<\phi\le\frac1{100}\quad\text{(radians)},\qquad
\Omega_0=(1,e^{i\phi},1),\quad p_0=r_{c,0}=z_0=0, \tag{PR03}
\]

use the same coefficients. This phase interval is strictly narrower than P4's \((0,\pi/12)\). It is not a modification of P4 or a new allowed geometric configuration.

Define reference rates and landmarks

\[
\omega_N=\sqrt{5/6}\,\nu,\qquad
\varpi=\sqrt{\omega_N^2+\omega_R^2}=\sqrt{17/18}\,\nu,
\qquad t_A=\nu^{-1}<t_R=\pi/\varpi<t_F=2\pi/\varpi. \tag{PR04}
\]

The symbol \(\varpi\) is a frequency of a specified **comparison system**, not an asserted frequency, period or physical clock of the exact nonlinear model. The actual solution has positive c, positive kappa, and no parameter changes or resets.

The proposed primary conclusion is

\[
\boxed{
H_R(t_R)>C/4,\qquad H_C(t_R)<C/100,
\qquad E_{\rm out}(t_F)<C/100.} \tag{PR05}
\]

The condition automatically lies within P4 because

\[
\frac{\sigma_{\rm ext}^2}{\nu^2}
=\frac{\gamma^2}{\nu^2}+\frac19
\le\frac1{10000}+\frac19<\frac14. \tag{PR06}
\]

Thus P4's actual stock at \(t_A\) and the proposed receiving/recovery conclusions belong to the same fixed-parameter trajectory, rather than to unrelated preparation regimes.

## 4. New tangent calculation at the existing aligned state

Work first in the published normalized native-amplitude convention. Put

\[
v=(1,1,1),\quad e=(1,-1,0)/\sqrt2,\quad
u=a-v,\quad \Omega=v+u+ib.
\]

**Notation:** the real deviation \(u=a-v\) is distinct from the estimate rate \(\nu\). No new state is added to the actual model.

At yaw pi/4 the raw matrix and its tangent drive are

\[
K=\frac G{\sqrt7}
\begin{pmatrix}\sqrt2&\sqrt2&\sqrt3\\ \sqrt2&\sqrt2&-\sqrt3\end{pmatrix},
\qquad D=K[v]_\times,
\qquad \ell=De.
\]

The proposal is to verify directly

\[
D=\ell e^T,\quad |\ell|^2=\frac{20G^2}{7},\quad
\omega_N^2=\frac{\eta_N^2m|\ell|^2}{2\alpha_N}
=\frac56\nu^2. \tag{PR07}
\]

This rank-one statement concerns the **linearized drive at v**. The actual K remains rank two, and the full nonlinear source still contains \(K(u\times b)\). Dropping that source from the exact model would invalidate the task.

## 5. Auxiliary norm, exact decomposition and nonlinear bound

For \(Y=(u,b,p,r_c,z)\) introduce the auxiliary proof norm

\[
\|Y\|_*^2
=2\alpha_N(|u|^2+|b|^2)
+\|p\|_2^2+\|r_c\|_2^2+\beta_R|z|^2. \tag{PR08}
\]

It is **not** the published total storage, a newly added physical store, or a claim of nonlinear conservation. The factor \(2\alpha_N\) makes the tangent coupling cancel exactly in the norm calculation.

With \(y=\mathcal B^*p\), \(w=K^Ty\), \(\mu=\eta_N/(2\alpha_N)\), define the finite-c linear operator

\[
\mathscr A_cY=
\left(
0,-\mu D^Ty,
-c(r_c)_s+\eta_N\mathcal BDb-\kappa\mathcal Bz,
-cp_s,\frac\kappa{\beta_R}y
\right). \tag{PR09}
\]

Its domain has periodic H1 carrier coordinates and unrestricted finite-dimensional coordinates. Derive, rather than assume,

\[
\langle Y,\mathscr A_cY\rangle_*=0.
\]

The tangent native term contributes \(-\eta_N(Db)^Ty\), cancelling the carrier's tangent drive. Periodic propagation and receiver loading cancel as in P1. For already strong curves, norm regularization gives the forced integral inequality, including at zero norm.

The exact nonlinear equations in these coordinates are

\[
\dot Y=\mathscr A_cY+\mathscr N(Y),\qquad
\mathscr N(Y)=
\left(\mu w\times b,-\mu w\times u,
\eta_N\mathcal BK(u\times b),0,0\right). \tag{PR10}
\]

P1's global theorem supplies the actual strong solution from the empty carrier. The finite-dimensional shift and auxiliary norm do not change its regularity. No new existence assertion is inferred from a formal cancellation.

Set

\[
L=\frac{\eta_Nk\sqrt m}{2\alpha_N}.
\]

A proposed global quadratic bound is

\[
\|\mathscr N(Y)\|_*\le L\|Y\|_*^2. \tag{PR11}
\]

For verification, write \(X=\sqrt{2\alpha_N}\sqrt{|u|^2+|b|^2}\) and \(V=\|(p,r_c,z)\|_{CR}\). The weighted native remainder is at most \(LXV\), and the external remainder at most \((L/2)X^2\). Their sum is at most \(L(X^2+V^2)\), using \(2XV\le X^2+V^2\). This deliberately nonoptimal bound suffices.

The exact initial deviation, not a first-order approximation to it, is

\[
u_0=(0,\cos\phi-1,0),\quad b_0=(0,\sin\phi,0),
\qquad Y_0^{\rm norm}:=\|Y(0)\|_*=2\sqrt C. \tag{PR12}
\]

For \(LY_0^{\rm norm}t<1\), the forced estimate and a scalar comparison should give

\[
\|Y(t)\|_*\le\frac{Y_0^{\rm norm}}{1-LY_0^{\rm norm}t}. \tag{PR13}
\]

A direct proof is to set \(Q(t)=Y_0^{\rm norm}+L\int_0^t\|Y(s)\|_*^2ds\). Then \(\|Y\|_*\le Q\), \(Q'\le LQ^2\) and \(Q(0)>0\). Integrate the reciprocal inequality only while its stated positive denominator remains positive. The actual solution already exists globally.

## 6. Coupled reference: native mode, carrier and receiver all move

Only for the comparison, use \(\dot Y^{(0)}=\mathscr A_0Y^{(0)}\), removing propagation and the quadratic remainder. Use the **exact same initial deviation** as PR12. The real u and the component of b perpendicular to e remain constant in this reference.

Let \(n=\ell/|\ell|\), \(h=e^Tb\), and use normalized coordinates

\[
X=\sqrt{2\alpha_N}\,h,\quad
p=\mathcal Bn\,P/\sqrt m,\quad r_c=0,\quad z=nZ/\sqrt{\beta_R}.
\]

The active reference equations are

\[
\dot X=-\omega_NP,\qquad
\dot P=\omega_NX-\omega_RZ,\qquad
\dot Z=\omega_RP. \tag{PR14}
\]

Do not assume \(X_0>0\): here \(X_0=-\sqrt{\alpha_N}\sin\phi\). With \(P_0=Z_0=0\), the proposed exact solution is

\[
\begin{aligned}
X(t)&=X_0\frac{\omega_R^2+\omega_N^2\cos(\varpi t)}{\varpi^2},\\
P(t)&=X_0\frac{\omega_N}{\varpi}\sin(\varpi t),\\
Z(t)&=X_0\frac{\omega_N\omega_R}{\varpi^2}[1-\cos(\varpi t)].
\end{aligned} \tag{PR15}
\]

At \(t_R\), the reference carrier is zero; at \(t_F\), both reference external states vanish. The reference active stock scale satisfies

\[
\frac{X_0^2}{2}=C\cos^2(\phi/2),\qquad
\frac{|Z(t_R)|}{\sqrt{2C}}
=\frac{2\sqrt{30}}{17}\cos(\phi/2). \tag{PR16}
\]

This reference is a strong curve: its p is a fixed H1 profile multiplied by a smooth scalar. Its period is not asserted to be a period of the exact solution. In particular the comparison does not restart the exact trajectory at \(t_R\) or \(t_F\).

## 7. Proposed uniform error over the complete episode

Let \(E=Y-Y^{(0)}\). By subtraction, E is strong before any residual is estimated, and

\[
\dot E=\mathscr A_cE+\mathscr N(Y)
+(0,0,0,-c\partial_sp^{(0)},0),\qquad E(0)=0. \tag{PR17}
\]

The only propagation residual is in the second carrier coordinate. The receiver is retained inside **both** linear systems; it is not an omitted error term. No second derivative of a tent is used.

Set \(T=t_F\), \(\theta=LY_0^{\rm norm}T\). Applying the forced inequality, PR13, and the absolute sine integral over one reference period gives

\[
\sup_{0\le t\le T}\frac{\|Y(t)-Y^{(0)}(t)\|_*}{\sqrt{2C}}
\le\frac{\sqrt2\,\theta}{1-\theta}
+\frac{4\gamma\omega_N}{\varpi^2},\qquad \theta<1. \tag{PR18}
\]

The intermediate derivations to check are

\[
\int_0^TL\|Y(t)\|_*^2dt
\le\frac{Y_0^{\rm norm}\theta}{1-\theta},
\]
\[
\int_0^T c\|\partial_sp^{(0)}(t)\|_2dt
=\frac{4\gamma|X_0|\omega_N}{\varpi^2}
\le\sqrt{2C}\frac{4\gamma\omega_N}{\varpi^2}.
\]

The same upper bound controls all earlier times because both absolute integrals are nondecreasing. This is a finite-c error estimate, not an operator-norm convergence assertion about an unbounded generator.

### Exact margins proposed for PR18

Using \(1-\cos\phi\le\phi^2/2\) and the normalized \(R^2=3\),

\[
\theta=\frac{\sqrt2}{R}\sqrt{1-\cos\phi}\,\nu T
\le\frac\phi{\sqrt3}\,\nu T<4\phi\le\frac1{25}. \tag{PR19}
\]

For the strict step, \(\nu T=2\pi\sqrt{18/17}<20/3\) and \(1/\sqrt3<3/5\). An entirely elementary certificate for the pi bound used here is

\[
\frac{22}{7}-\pi=\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx>0.
\]

This ordinary inequality has no connection to, and does not rely on, the pi-exponent brainstorming material.

Also

\[
\frac{4\gamma\omega_N}{\varpi^2}
=\frac{72}{17}\sqrt{\frac56}\frac\gamma\nu
<4\frac\gamma\nu\le\frac1{25},
\qquad \sqrt2<\frac{10}{7}.
\]

Thus the proposed uniform error is

\[
\boxed{\sup_{0\le t\le t_F}
\frac{\|E(t)\|_*}{\sqrt{2C}}
<\frac5{84}+\frac1{25}
=\frac{209}{2100}<\frac1{10}.} \tag{PR20}
\]

Codex must independently verify these inequalities, signs, weights and phase-uniform quantifiers. The preparatory algebra script checks finite expressions, not PR13 or the functional-analytic justification.

## 8. From the error estimate to actual reception and recovery

The carrier and weighted receiver coordinate are contractive projections of the auxiliary norm. At \(t_R\),

\[
\frac{2\sqrt{30}}{17}>\frac58,
\qquad \cos(\phi/2)\ge1-\phi^2/8>\frac{24}{25}.
\]

Consequently the reference receiver norm exceeds \((3/5)\sqrt{2C}\). Subtracting PR20 leaves an actual receiver norm greater than \((1/2)\sqrt{2C}\). The reference carrier vanishes at that time. At \(t_F\) the whole external reference vanishes. Squaring these **positive** bounds establishes PR05 if all preceding steps pass.

The proposed direct consequences, with the original storage account and positive denominators, are

\[
\frac{H_R(t_R)}{E_{\rm out}(t_R)}>\frac{25}{26},
\qquad 0\le\frac{H_R(t_F)}{H_R(t_R)}<\frac1{25}, \tag{PR21}
\]
\[
\begin{aligned}
\mathcal R_A&:=\frac{H_N(t_F)-H_N(t_A)}{E_{\rm out}(t_A)}
=1-\frac{E_{\rm out}(t_F)}{E_{\rm out}(t_A)}>\frac{24}{25},\\
\mathcal R_R&:=\frac{H_N(t_F)-H_N(t_R)}{E_{\rm out}(t_R)}
=1-\frac{E_{\rm out}(t_F)}{E_{\rm out}(t_R)}>\frac{24}{25},\\
H_N(t_F)-H_N(t_R)&>\frac6{25}C.
\end{aligned} \tag{PR22}
\]

Both recovery fractions are at most one. For \(\mathcal R_A\) the precise lower bound before relaxing it is \(1-4096/105300=25301/26325>24/25\); for \(\mathcal R_R\), use \(E_{\rm out}(t_R)>C/4\). The receiving-share bound follows from \(H_C(t_R)/H_R(t_R)<1/25\), not by changing the denominator of P3's statistic.

Positive receiving and native-recovery increments, together with continuous powers, imply existence of appropriate sign intervals within the declared windows. They do **not** by themselves establish simultaneous native/receiver power signs, monotonic recovery throughout a window, or signs at the exact comparison landmarks. No such extra power theorem is required.

## 9. Nonempty fixed finite parameters and dimensions

Fix any admitted finite profiles/geometry, positive finite \(c,\alpha_N,\beta_R,G\). Choose a finite positive native coupling such that

\[
\nu=\eta_N kR\sqrt{\frac m{2\alpha_N}}\ge100c\sqrt{\frac dm},
\quad\text{equivalently}\quad
\eta_N\ge\frac{100c\sqrt{d/m}\sqrt{2\alpha_N}}{kR\sqrt m}.
\]

Then choose once

\[
\kappa=\frac\nu3\sqrt{\frac{\beta_R}{m}}>0. \tag{PR23}
\]

Both are finite, selected before phi and constant throughout each trajectory. This is one sufficient, intentionally nonoptimized subfamily, not a claim about every P4 parameter tuple. There is no limit solution, time-dependent control, new profile or new registration.

When restoring native amplitude units, v and u have native amplitude units; e and n are unit directions; D and ell have drive-per-native-amplitude units. The native factor R remains in nu. The auxiliary norm has units of the square root of trial storage, L has units \((\text{norm}\times\text{time})^{-1}\), theta is dimensionless, and \(\gamma,\nu,\omega_N,\omega_R,\varpi\) are inverse-time quantities. Restored launch expressions carry the same native-amplitude normalization as P4; no dimensionless replacement of R in a dimensional identity is allowed.

## 10. Meaning, limitation and stopping point

If established, this would connect the existing finite-capacity access theorem to a new **same-solution reception and net recovery certificate**. It does not require or assert overlap with P3's sufficient regime, exact ceiling saturation, a physical energy calibration, a geometric circuit, or permanence of receiver storage.

The phi interval is small. In particular \(C/H_N(0)=\tfrac23(1-\cos\phi)\) still tends to zero with phi. A substantial fraction of a small capacity is not a claim of large absolute energy. Receiving at \(t_R\) and recovery between specified times are storage accounts, not a path reconstruction or a tagged-cohort assertion.

The substantive independent task is the full finite-error bridge, especially the auxiliary native weight, exact initial conditions, nonlinear comparison, first-derivative propagation residual and strict fractions. A failed estimate must be identified and corrected or reported; failure of this proposed certificate alone is not physical impossibility. Do not widen into a parameter scan, a new receiver design, a hybrid native-cadence analysis or a manuscript. Return the bounded investigation for review.
