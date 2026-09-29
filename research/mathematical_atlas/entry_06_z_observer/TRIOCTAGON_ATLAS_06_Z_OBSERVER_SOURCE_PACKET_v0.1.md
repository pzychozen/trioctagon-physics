# Tri-Octagon mathematical atlas — Entry 06

## Z observer, clock, staged law, and EMA memory

Version 0.1 · 29 September 2026 · External source packet; **not published**.

The accepted observer consists of a shared norm/harmonic/vector construction and two explicit scalar laws. Staged observation multiplies the harmonic by an exponential envelope. EMA observation adds the supplied current memory; a separate operation updates that memory. Neither observation advances Ω or the clock.

Authority: current repository [trioctagon-physics](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics), HEAD **34c21830e7e7c4b5f4a5a940d084c37feaf1f82c**. Atlas 01–05 remain closed. Harmonic-three provenance remains the Atlas-01 OPEN item; no correction queue, historical geometry reconstruction, or source repair is undertaken here.

This packet derives the ideal mathematics, then records the current binary64 contract and bounded historical evidence separately. It adds no force, physical field, shell position, recurrence coefficient, or feedback law.

Companions: [independent checks](C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_06_EXACT_CHECKS.py) and [machine-readable results](C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_06_EXACT_RESULTS.json).

## 0. Source authority and reading boundary

Source IDs below refer to these exact local files. The results JSON records all 19 source SHA-256 values.

| ID | Source and scope |
|---|---|
| Z | [z_manifold.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_manifold.py): current observer contract, immutable values, clock, scalar/vector evaluation, explicit EMA and constructor-zero operations. |
| E | [Paper E v0.1.1](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md): §§2–5, 7, 8.1, 9.3, 16.1, 19 establish the present mathematical and historical boundary. |
| ZT | [test_z_manifold.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_z_manifold.py): existing exact, precision, ownership, initialization, and passivity witnesses. |
| NUM | [_response_numeric.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_response_numeric.py): conversion, checked arithmetic, and ResponsePrecisionError. |
| C | [readouts.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py): raw cyclic cross-product components. |
| A04 | [closed Atlas 04](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/research/mathematical_atlas/entry_04_face_state_chirality/TRIOCTAGON_ATLAS_04_FACE_STATE_CHIRALITY_SOURCE_PACKET_v0.1.md): established channel-area meaning and raw scale; its face/transport derivation is not repeated. |
| D | [dynamics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py): independent deterministic Ω map, no observer clock or dt. |
| RUN | [_runner.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_runner.py) and [runner tests](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_runner_records.py): actual public-runner schedule, distinguished from historical stored-row count. |
| K | [staged historical model snapshot](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/source_snapshots/staged/model_core.py): historical staged update and storage semantics. |
| H | [committed EMA snapshot](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/source_snapshots/committed_ema/model_core.py): historical memory update and subsequent observation. |
| PROV | [Paper-E snapshot provenance](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/source_provenance.json): preserved snapshot identity. |
| P9 | [K2 P9/P10 tests](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_parity_p09_p10.py) and [independent Paper-E oracle](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/parity_oracles/paper_e_oracle.py): P9 observer fixtures, literal EMA and passive-trajectory boundary. P10 diagnostics are not reconstructed here. |
| ES | [Paper-E symbolic checks](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/check_symbolic.py), [retained symbolic results](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/symbolic_results.json), [accepted reconstruction checker](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/evidence/accepted_reconstruction/verify_historical_z.py), and [edition checker](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/PAPER_E/v0.1.1/check_revision.py): supporting evidence inspected, not rerun as broad historical/diagnostic workflows. |
| NEXT | [z_diagnostics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_diagnostics.py): interface inventory only for Atlas 07. |

Principal fingerprints:

| Source | SHA-256 |
|---|---|
| Z | 97ebdbb37103e736d2ae86c272541c458a5b585e1889e6d14ff056b316494f4f |
| E | a79bc29d991c3af8bba546f0bc5e1ff7a6bbe5501d8adf2ef6d19c66b362978d |
| K | ce635fd3de1813ef0cdced1d310c1486815672a0a2b93a9f85ebc706c6ee99c6 |
| H | cd173dd818bd20983e23a72c2195b513eb3d72ae0446db8239c65657fd7d17b2 |

The historical comparison executes only the hash-bound K/H update_z method bodies, extracted into a minimal NumPy namespace. It does not import their modules or execute their integrated classes, recurrence, runner, identity logic, noise, GUI, or production consumers. Constructor and scheduling evidence is also inspected statically.

## 1. Clock: residue, stored time, and explicit advancement

Write the clock as $(q,N,t,d)$, where $d=q_{\rm step}$. Its exact domain is $q,d\in\mathbb Z$, $N\in\mathbb Z_{>0}$, with a real stored time label $t$. The current value object requires finite real t and rejects booleans/nonintegers for its three integer fields. Negative q, negative step, zero step, and negative t are allowed.

Euclidean integer remainder gives $r=q\bmod N\in\{0,\ldots,N-1\}$. Define

$$
\theta(q)=2\pi\frac{q\bmod N}{N}.
$$

Exactly, $0\leq\theta<2\pi$ and $\theta(q+kN)=\theta(q)$ for every integer k. Thus the angle retains a residue class, not the integer lift. Clock construction retains the supplied raw q: q=−1 and q=11 are different stored integers at N=12 but give the same angle. Construction does not normalize q or count turns.

An explicit advance returns

$$
q'=(q+d)\bmod N,\qquad t'=t+dt.
$$

The old object is unchanged. After n advances with a fixed step, the residue is $(q_0+nd)\bmod N$. Its orbit has $N/\gcd(N,d)$ sectors, with $\gcd(N,0)=N$, so zero step has orbit length one. For variable supplied increments, $t_n=t_0+\sum_{j=1}^n dt_j$ in ideal arithmetic. A zero dt can still advance q; a zero q_step can still change t. Negative dt is accepted.

After an advance q is a residue representative, so even the previous raw integer lift is no longer present in the new clock. The caller would need a separate winding/update count to retain it.

**CLOCK_ADVANCE != OMEGA_UPDATE. dt IS NOT A PAPER-A RECURRENCE TIME STEP.** The current step3 signature is (omega, config), and its algebra contains no clock or dt. Historical dt enters the stored t and hence K's envelope, not the Paper-A amplitude/phase increment. These statements supply no continuous physical-time interpretation. [Z: Clock, clock_angle, advance_clock; D; E §§3,16.1]

## 2. Six-real norm and scalar saturation

For $\Omega=x+iy\in\mathbb C^3$,

$$
\kappa=\|\Omega\|=\sqrt{\sum_{i=1}^3(x_i^2+y_i^2)},\qquad
\rho=\frac{\kappa}{1+\kappa}.
$$

The six summands are nonnegative, so $\kappa\geq0$, with equality exactly when Ω=0. For any finite exact state, κ is finite and

$$
\rho(0)=0,\qquad 1-\rho=\frac1{1+\kappa}>0,\qquad
\frac{d\rho}{d\kappa}=\frac1{(1+\kappa)^2}>0.
$$

Hence $0\leq\rho<1$, and ρ is strictly increasing in κ. Solving $\rho(1+\kappa)=\kappa$ gives

$$
\kappa=\frac{\rho}{1-\rho},\qquad 0\leq\rho<1.
$$

Near zero, $\rho=\kappa-\kappa^2+O(\kappa^3)$. As κ grows, $\rho\to1$ from below and $1-\rho=1/\kappa+O(\kappa^{-2})$. A real scaling r sends κ to $|r|\kappa$ and ρ to $|r|\kappa/(1+|r|\kappa)$.

The code uses a stable six-component math.hypot, avoiding naive squaring overflow/underflow in many cases. It may still reject an unrepresentable norm or a nonzero subnormal norm. At large κ, binary64 ρ can equal 1; for example Ω=(10²⁰⁰,0,0). The strict theorem and inverse above describe exact arithmetic; they do not license division by $1-\rho$ after floating saturation to one.

**Saturation affects the observer scalar. It does not rescale, normalize, overwrite, or bound Ω.** [Z: state_norm, saturated_norm; NUM]

## 3. Shared threefold harmonic and the twelve-sector sample

Set $\ell=\theta_{\rm lock}$ and $\lambda=\lambda_{vp}$. At a fixed Ω,

$$
h(\Omega,\theta)=A_0\cos(3(\theta-\ell)),\qquad A_0=\lambda\rho(\Omega).
$$

If $A_0\ne0$, the fundamental continuous angular period is $2\pi/3$. If $A_0=0$, h is identically zero and has every period. The vanishing set consists of Ω=0, λ=0, or

$$
\theta=\ell+\frac{\pi}{6}+k\frac{\pi}{3},\quad k\in\mathbb Z.
$$

Differentiation gives $h'=-3A_0\sin(3(\theta-\ell))$ and $h''=-9h$. Nondegenerate stationary angles are $\ell+k\pi/3$, with value $(-1)^kA_0$. Their largest and smallest values are $|A_0|$ and $-|A_0|$. Signed λ swaps which alternating stationary angles are maxima and minima.

For λ>0 and Ω≠0, h is positive on

$$
\ell-\frac{\pi}{6}+\frac{2k\pi}{3}<\theta<
\ell+\frac{\pi}{6}+\frac{2k\pi}{3},
$$

and negative on the intervening open intervals. For λ<0 the signs reverse. In all cases

$$
|h|\leq|\lambda|\rho.
$$

For N=12, $\theta_q=q\pi/6$ on the residue grid. With $c=\cos(3\ell)$ and $s=\sin(3\ell)$, the exact normalized harmonic pattern is

| q | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $h/A_0$ when $A_0\ne0$ | c | s | −c | −s | c | s | −c | −s | c | s | −c | −s |

The identity follows from $\cos(q\pi/2-3\ell)$. At $\ell=0.244$, $c\approx0.74383917$ and $s\approx0.66835865$: the frozen positive-amplitude sign sequence is ++−− repeated three times. This grid misses the continuous zero angles and extrema at that default lock. An extremum or zero occurs on this twelve-sector grid precisely when $\ell\in(\pi/6)\mathbb Z$.

The complex harmonic sampled on an N-sector grid has residue period $N/\gcd(N,3)$. For N=12 its period is four sectors; a step d gives harmonic period $4/\gcd(4,d)$ for a generic lock, possibly shortened by accidental cosine degeneracies. The full clock need not have that period. None of these frozen-pattern statements asserts periodicity of an evolving recorded path whose Ω, t, or memory also changes. [Z: _harmonic; E §4]

The factor 3 is the adopted harmonic in this observer. Its historical derivation is not reopened.

## 4. Staged scalar: hypotheses for an envelope to decay

The staged law is

$$
z_K=h\,e^{-\gamma t}.
$$

StagedConfig accepts finite signed real λ, γ, ℓ, α and β. No positivity constraint is silently added. With finite exact real γ,t, the exponential is strictly positive. Consequently the exact zeros of $z_K$ are precisely the zeros of h.

| Hypothesis | Exponential behavior |
|---|---|
| γ>0, t increasing | The envelope decreases; it tends to zero as t→+∞. |
| γ=0 | The envelope is one. |
| γ<0, t increasing | The envelope increases; it tends to +∞ as t→+∞. |
| t=0 | The envelope is one for every finite γ. |

Negative t is permitted. At fixed nonzero h, the corresponding magnitude follows the envelope. If Ω or θ varies, z itself need not be monotone. Nevertheless, for fixed finite λ and γ>0, the ideal bound

$$
|z_K|\leq|\lambda|\rho e^{-\gamma t}\leq|\lambda|e^{-\gamma t}
$$

forces the scalar and macro vector to zero as t→+∞, even with varying finite Ω. No such theorem follows for raw C or the full blend T.

Finite floating underflow is not an exact zero or a successful asymptotic proof. The current staged evaluator rejects exponential overflow, a nonzero subnormal envelope, and an envelope rounded to zero. It evaluates the envelope even when λ=0 or Ω=0. [Z: staged_scalar; NUM; E §§3,19]

## 5. Macro vector: a double cone in observer coordinates

For either scalar law, define

$$
v(\theta)=(\cos\theta,\sin\theta,1),\qquad
M=zv(\theta).
$$

Directly,

$$
M_z=z,\qquad M_x^2+M_y^2=z^2=M_z^2,\qquad
\|M\|^2=2z^2,\qquad\|M\|=\sqrt2\,|z|.
$$

This is the double circular cone $X^2+Y^2=Z^2$, with apex at zero; a particular observer law visits only its associated subset. Positive z lies on the upper nappe and negative z on the lower. For negative z the horizontal azimuth of M is θ+π, not θ, when the horizontal part is nonzero.

At fixed θ, $M(-z,\theta)=-M(z,\theta)$: scalar reversal is central inversion. At fixed scalar z, an angular shift δ gives $M(z,\theta+\delta)=R_\delta M(z,\theta)$, where $R_\delta$ rotates the first two observer coordinates and fixes the third.

For the actual harmonic laws, a shift δ normally also changes z. At δ=$2\pi/3$, however, h is unchanged. Holding Ω,t and parameters fixed for K, or Ω,m and parameters fixed for H, gives

$$
M(\theta+2\pi/3)=R_{2\pi/3}M(\theta).
$$

Thus the vector rotates; it does not generally stay equal to itself. A clock-grid interpretation of this shift requires $3\mid N$ and q→q+N/3; N=12 gives q→q+4. This is a comparison at held observer inputs, not four time advances along a changing trajectory.

Because $M_z=z$, M=0 iff z=0. Its cone coordinates alone imply neither a physical spatial field nor a point on the folded shell. [Z: macro_vector; E §§5,7]

## 6. Raw chiral component

Using established Atlas-04 authority,

$$
C=x\times y=
(x_2y_3-x_3y_2,\ x_3y_1-x_1y_3,\ x_1y_2-x_2y_1).
$$

It is an ordered channel-area triple. The observer evaluates it directly from the supplied Ω. In particular:

~~~text
C IS RAW
C HAS NO STAGED EXPONENTIAL ENVELOPE
C IS NOT NORMALIZED BY rho
~~~

Under Ω→rΩ for real r, C→r²C. Common complex phase preserves C; conjugation reverses it. Its tangent-frame interpretation remains the closed Atlas-04 construction, not a new spatial-frame inference here. [C; A04 §§11–12; E §8.1]

## 7. Blended observer and evaluation of zero-weight terms

The total is

$$
T=\alpha M+\beta C.
$$

For fixed real α,β this is a linear map from the pair $(M,C)\in\mathbb R^3\oplus\mathbb R^3$ to $\mathbb R^3$. For example

$$
L(a(M_1,C_1)+b(M_2,C_2))=aL(M_1,C_1)+bL(M_2,C_2).
$$

It is not generally linear in Ω: ρ saturates, C is quadratic, and H's supplied memory has its own history. At α=0, T=βC; at β=0, T=αM; at both zero, the mathematical blend is zero.

The full implementation still computes the scalar and M, still computes C even at β=0, and validates both input vectors in blend_vectors even at zero weights. Thus a zero coefficient does not suppress a shape error, nonfinite input, or precision failure in the promised full decomposition. A successful staged_scalar call need not imply successful observe_staged.

For rΩ, the macro part uses $\rho(|r|\kappa)$ while C scales by r². With fixed time and parameters, the staged macro is bounded as $|r|\to\infty$; raw C need not be. H adds current m and also retains raw C. No orthogonality of M and C is assumed. Their detailed accounting is deferred to Atlas 07.

Z_total is T. Z_vec is a property returning the very same Z_total array, with no separate storage or separate update. [Z: blend_vectors, _observe, ZReadout; E §9]

## 8. ZReadout ownership and limits

| Field | Meaning and ownership |
|---|---|
| z | Supplied finite checked real scalar. |
| Z_macro | Fresh detached read-only real array, shape (3,). |
| Z_chiral | Independently copied read-only real array, shape (3,). |
| Z_total | Independently copied read-only real array, shape (3,). |
| variant | Exactly staged or ema. |
| initialization | Exactly recomputed or historical_constructor_zero. |

ZReadout is a frozen, slotted value object. Changing a supplied array afterward does not change the stored array. Ordinary field assignment and ordinary array element writes are rejected. The arrays are copied independently, and readout arrays do not alias Ω.

These are ordinary API protections, not a security boundary: an owner can deliberately circumvent NumPy write flags or Python's frozen-dataclass machinery. No claim of adversarial immutability is made.

The record owns observer values, not Ω, a clock, or EMAState. It does not advance anything. Manual construction validates types/shapes/finite checked values and markers; it does **not** certify that its vectors satisfy the macro equation or α/β blend for some Ω. Observer functions construct consistent records; diagnostic verification of independently supplied records belongs to Atlas 07. [Z: ZReadout]

## 9. Independent cubic J algebra

Set

$$
P=\Omega_1\overline{\Omega_2}\Omega_3=K+iJ.
$$

Expansion in real coordinates gives

$$
\begin{aligned}
K&=x_1x_2x_3+y_1y_2x_3-y_1x_2y_3+x_1y_2y_3,\\
J&=x_1x_2y_3+y_1y_2y_3+y_1x_2x_3-x_1y_2x_3.
\end{aligned}
$$

Every monomial has degree three. For real r,

$$
J(r\Omega)=r^3J(\Omega),\qquad
J(\overline\Omega)=-J(\Omega),\qquad
J(-\Omega)=-J(\Omega).
$$

This distinguishes J from quadratic C, which has degree two and is unchanged by global sign reversal.

For common phase χ, the two unconjugated factors contribute $e^{2i\chi}$ and the conjugated factor contributes $e^{-i\chi}$. Therefore

$$
P(e^{i\chi}\Omega)=e^{i\chi}P(\Omega),\qquad
\begin{pmatrix}K'\\J'\end{pmatrix}
=
\begin{pmatrix}\cos\chi&-\sin\chi\\ \sin\chi&\cos\chi\end{pmatrix}
\begin{pmatrix}K\\J\end{pmatrix}.
$$

In particular $J'=K\sin\chi+J\cos\chi$, which is generally not J. Ω=(1,1,1) has J=0; Ω=(i,i,i) has J=1. Both have C=0. Conversely Ω=(1,i,0) has J=0 and C=(0,0,1). Neither quantity determines the other.

If any channel is zero, J=0. Otherwise write $\Omega_j=a_je^{i\phi_j}$ with $a_j>0$. Then

$$
J=a_1a_2a_3\sin(\phi_1-\phi_2+\phi_3),
$$

so J=0 exactly when $\phi_1-\phi_2+\phi_3\in\pi\mathbb Z$. The real-coordinate polynomial remains valid without defining phases at zero.

The outer-channel swap 1↔3 leaves P unchanged by commutativity. Other permutations can move the conjugated channel and change J. If all channels are nonzero and $U=\Omega_1\Omega_2\Omega_3$, choosing channel j as the conjugated one gives $P_j=Ue^{-2i\phi_j}$. Each choice has two outer orderings, so at most three values occur under the six permutations.

For Ω=(1+4i,2+5i,3+6i), direct exact multiplication gives:

| Channel ordering | 123 | 132 | 213 | 231 | 312 | 321 |
|---|---|---|---|---|---|---|
| J | 141 | 147 | 123 | 147 | 123 | 141 |

J is neither permutation invariant nor an alternating permutation pseudoscalar.

It is also **not generally conserved** by the accepted recurrence. With ε=1, g=0, phase_strength=0 and k=(1,1,1), Ω=(2i,2i,2i) maps to (−4i,−4i,−4i). J changes from 8 to −64. This is an exact finite-step witness, not a statement about all trajectories. [Z: cubic_j; E §§8.1,19; D: step3]

## 10. Normalized cubic

Define the odd scalar function

$$
f(J)=\widehat j=\frac{J}{1+|J|}.
$$

Its denominator is positive and strictly larger than $|J|$ for every finite exact J. Therefore

$$
|\widehat j|<1,\qquad
\operatorname{sign}\widehat j=\operatorname{sign}J,\qquad
\widehat j=0\iff J=0.
$$

Solving separately on the positive and negative branches gives the single inverse

$$
J=\frac{\widehat j}{1-|\widehat j|},\qquad -1<\widehat j<1.
$$

The derivative is $1/(1+|J|)^2$ away from zero and equals one at zero, so f is strictly increasing. It tends to ±1 without attaining either endpoint in ideal arithmetic.

Conjugation and global sign reversal negate $\widehat j$. A common phase produces $f(K\sin\chi+J\cos\chi)$, not a rotation of $\widehat j$ alone. The saturation destroys cubic homogeneity.

Binary64 may return ±1 for large finite representable J. The checked witnesses use Ω=(±i·10¹⁰⁰,1,10¹⁰⁰). The inverse is not defined at those rounded endpoints. [Z: normalized_cubic; NUM]

## 11. Explicit EMA memory update

The adopted ideal coefficient is $\tau=0.01=1/100$, with $a=1-\tau=99/100$. One explicit update is

$$
m'=am+\tau\widehat j=m+\tau(\widehat j-m).
$$

For $|m|\leq1$ and $|\widehat j|\leq1$, this is a convex combination in [−1,1]. A direct proof exposes both nonnegative distances:

$$
1-m'=a(1-m)+\tau(1-\widehat j)\geq0,\qquad
1+m'=a(1+m)+\tau(1+\widehat j)\geq0.
$$

Thus the interval is forward invariant. If J is finite in ideal arithmetic, $|\widehat j|<1$, making both inequalities strict after one update, even from m=±1. At m=1, $1-m'=\tau(1-\widehat j)>0$; at m=−1, $m'+1=\tau(1+\widehat j)>0$.

For a prescribed innovation sequence $b_j=\widehat j_j$,

$$
m_n=a^nm_0+\tau\sum_{j=1}^n a^{n-j}b_j.
$$

Induction proves this expression, and the weights sum to $a^n+\tau(1-a^n)/(1-a)=1$. For a constant innovation b,

$$
m_n=b+a^n(m_0-b).
$$

The unique fixed point is b; differences in initial memory decay by $a^n=0.99^n$. Zero innovation makes memory approach zero, but a nonzero constant innovation makes it approach b. A changing innovation need not produce monotone memory or convergence to a constant.

This is a discrete averaging/forgetting law per call, not physical damping or thermodynamic relaxation. Neither dt nor q enters advance_ema.

The implementation uses the literal binary64 0.01 and retention computed as 1.0−0.01. Replacing its innovation coefficient by 1.0−float(0.99) changes binary arithmetic and is not the accepted operation. The witness with m=0,J=1 yields 0.005 under the adopted literal and a different float under that replacement. Rounded $\widehat j=1$ and rounded m=1 can keep m'=1, so strict ideal entry into the interval interior is not a universal binary64 theorem. [Z: EMAState, advance_ema; H: update_z; E §19; P9]

## 12. EMA observation uses current memory

EMAConfig contains λ, ℓ, α and β. **It has no gamma field.** Given an explicit EMAState(m),

$$
z_H=h+m.
$$

The value m here is the current supplied memory, not a local request to calculate J or advance m. observe_ema evaluates this scalar, then M, raw C and the blend. It does not call advance_ema, advance_clock or step3. advance_ema separately computes J and one new memory value; it does not advance the clock or Ω.

For frozen Ω,m, the height extrema are $m\pm|\lambda|\rho$. When $A_0\ne0$, both signs occur iff $|m|<|A_0|$; equality gives contact with zero, and $|m|>|A_0|$ puts the whole frozen curve on one side. If $A_0=0$, height is the constant m. The bound $|z_H|\leq|\lambda|\rho+|m|\leq|\lambda|+1$ holds in ideal arithmetic under the accepted memory interval.

The cone relation persists because it uses the actual z as a common factor. The additive offset generally destroys K's frozen half-turn height reversal: $h(\theta+\pi)=-h(\theta)$ but $z_H(\theta+\pi)=-h(\theta)+m$, not $-z_H(\theta)$ unless m=0.

At fixed Ω,q,m, changing stored t alone leaves H's observation unchanged. This does not mean histories with different input states must have the same memory. [Z: EMAConfig, ema_scalar, observe_ema; E §19]

## 13. Ordering: historical rows and the actual current runner

These are distinct operations with distinct ownership:

~~~mermaid
flowchart LR
  O["Current Ω"] --> D["step3: new Ω"]
  C["Current clock"] --> A["advance_clock: new clock"]
  D --> E["advance_ema: new m"]
  M["Current m"] --> E
  D --> Z["observe: new readout"]
  A --> Z
  E --> Z
~~~

The diagram shows the data needed for one caller-chosen EMA cycle. It does not add automatic transitions to any individual observer function. For staged observation the EMA branch is absent.

**Historical K/H runner.** The inspected run loop first stores the current Ω, norm, clock indices/time and already stored z/vector values. It does not recompute the observer merely to record a row. Then step performs:

1. The amplitude/phase routine computes and commits the new state with state.Omega = Omega_next.
2. advance_phi advances the sector index.
3. Stored t increases by dt and the historical step counter increments.
4. update_z evaluates the observer. K evaluates its envelope law. H computes J from the now-committed state.Omega, advances state.z_mem, and then computes z from the new memory.
5. The historical cycle and identity updates follow.

The static source order proves which state is available to H's cubic. A bounded changed-state witness makes the distinction concrete: replacing real Ω=(1,1,1) by newly committed Ω=(i,i,i) changes the first innovation from 0 to 1/2 and produces m'=0.005, rather than a stale-state zero.

With n_steps=n, historical run stores rows 0 through n−1, but its internal state has undergone n steps on return. The last updated state is not an additional stored row. A constructor-zero first row therefore differs from recomputing the observer at the initial Ω.

**Current core functions.** They expose operations independently. A caller may observe repeatedly without advancing anything, advance a clock independently, or deliberately choose a schedule. The observer module itself is not a runner.

**Existing public RUN implementation.** The actual _runner.py is also inspected, so its schedule need not be guessed: run first samples the initial state, applying constructor-zero only when requested. Each subsequent iteration calls the recurrence, then advances each observer's clock, then its EMA memory if present, then observes and appends the new sample. The EMA call receives the new State. With updates=n it records n+1 samples, including the final updated state. This differs from the historical n-row recording convention while preserving the relevant new-Ω→clock→memory→observation order.

The focused runner tests instrument exactly that schedule and check independent observer clocks/memories. No claim is made that every historical caller or future caller uses it. Historical optional forcing/noise and signed-zero phase details are not introduced into a new replay engine here. [K/H: phase_lock_step, step, run; RUN; E §§2–3,19]

## 14. Historical constructor-zero is storage semantics

ConstructorZeroRecord stores:

- a validated, detached read-only copy of the raw complex triple;
- the supplied immutable Clock and explicitly selected StagedConfig or EMAConfig;
- EMAState(0);
- a zero ZReadout with the selected variant and initialization marker historical_constructor_zero.

It checks raw Ω components and the record types but does not evaluate κ, ρ, J, C, the harmonic, or even the clock angle. The supplied clock/config have already validated their own fields. It can therefore preserve a finite raw Ω whose later norm or cubic evaluation would fail the precision contract.

K/H ModelState fields initialize z, z_mem and all three stored vectors to zero without invoking update_z. The initial stored history row reflects those values. Current historical_constructor_zero preserves that distinction explicitly.

For Ω=(1+4i,2+5i,3+6i), recomputation gives κ=√91, C=(−3,6,−3), J=141 and a nonzero default staged scalar. Constructor-zero instead stores zero C and zero z without asserting those are the mathematical readouts of Ω. The marker is essential.

Classification: **HISTORICAL_STORAGE_SEMANTIC**, not an alternative scientific observer law. [Z: ConstructorZeroRecord, historical_constructor_zero; K/H: ModelState and run; E §2.3; P9]

## 15. Exact staged/EMA comparison

| Feature | Staged K | EMA H |
|---|---|---|
| Configuration | StagedConfig(λ,γ,ℓ,α,β) | EMAConfig(λ,ℓ,α,β) |
| Scalar | $h e^{-\gamma t}$ | $h+m$ |
| Persistent observer memory | None needed | Explicit EMAState(m) |
| Separate memory update | None | $m'=0.99m+0.01f(J(\Omega))$ |
| Clock use in observation | q,N determine θ; t enters envelope | q,N determine θ; t does not enter scalar |
| γ | Finite signed field | Absent |
| Pointwise norm/harmonic core | κ,ρ,h | Same |
| Vector decomposition | $M=zv(\theta), C=x\times y, T=\alpha M+\beta C$ | Same, using z_H |
| Constructor-zero compatibility | Explicit marked zero record | Explicit marked zero record, memory zero |
| Observation updates Ω/clock/m | No | No |

The explicit API variants are preserved; this packet does not replace them with one mode-dependent equation or an implicit state machine. [Z; E §19]

## 16. Purity, copy boundaries, and scope of the claim

Z directly imports dataclasses, math, numbers, NumPy, raw readouts, and the numeric helpers. It does not import dynamics, z_diagnostics, face geometry, the historical model or production TORMENT. A fresh-process import check confirms the observer import does not load dynamics or diagnostics.

The scientific calls read converted/copied Ω values. Clock and EMA advances return new frozen values. Observations return detached readout arrays. Runtime checks compare Ω bytes before/after successful calls, patch forbidden advancement calls to fail if reached, exercise ordinary write rejection, and retain the original values across failure cases.

Eight matched recurrence updates with different observer dt values and staged/EMA schedules produce bit-identical Ω arrays to the bare recurrence in the bounded witness. This supports the code-level dependency finding; it is not an appeal to trajectory resemblance.

The source and checks support:

~~~text
OBSERVE_STAGED DOES NOT MODIFY OMEGA
OBSERVE_EMA DOES NOT MODIFY OMEGA
ADVANCE_CLOCK DOES NOT MODIFY OMEGA
ADVANCE_EMA DOES NOT MODIFY OMEGA
~~~

No observer function writes caller clock/memory fields. Failure raises without returning a partially committed new core state. These claims concern ordinary use of the accepted input types, not adversarial objects with arbitrary conversion side effects.

They do not imply that no historical subsystem ever consumed Z. The inspected old model itself passes z into identity mapping after observation. Nor does current observer symmetry imply recurrence symmetry. [Z; NUM; C; D; RUN; K/H]

## 17. Defaults and their evidence classification

The classification distinguishes a preserved default value from permission to vary a parameter. It does not promote historical names into physical derivations.

| Value | Classification of the literal | Current freedom and evidence |
|---|---|---|
| N=12 | HISTORICAL_DEFAULT | FREE_PARAMETER: any positive integer in Clock. K/H use d24_steps=12. This does not derive a D24 physical lattice. |
| λ=0.618 | HISTORICAL_DEFAULT | FREE_PARAMETER: signed finite real. K/H label it a toy choice; the decimal is not exactly $(\sqrt5-1)/2$. |
| γ=0.577 | HISTORICAL_DEFAULT | FREE_PARAMETER in K: signed finite real. H's historical parameter object retains it but H's update does not use it; current EMAConfig omits it. |
| ℓ=0.244 radians | HISTORICAL_DEFAULT | FREE_PARAMETER: signed finite real lock. No derivation of this literal is supplied here. |
| α=1 | HISTORICAL_DEFAULT | FREE_PARAMETER: signed finite blend weight. |
| β=0.5 | HISTORICAL_DEFAULT | FREE_PARAMETER: signed finite blend weight. |
| τ_meta=0.01 | HISTORICAL_DEFAULT | Adopted fixed coefficient of advance_ema, not a configurable field. Its ideal value is 1/100; retention 99/100 follows by subtraction. |

None of those seven historical literals is established here as a DERIVED_CONSTANT. Examples of genuinely derived constants in the present calculation are the factor √2 in $\|M\|=\sqrt2|z|$, the period $2\pi/3$ for the adopted third harmonic, and 0.99 obtained from the adopted ideal τ. Historical comments such as “vesica compression constant,” “damping/drift” or “D24 sector” do not supply a missing derivation or physical calibration. [K/H: ModelParams; Z configs; E §§2,16.1]

## 18. Transformation summary with held-input qualifications

Use χ for common complex phase so it is not confused with blend weight α. Unless stated otherwise, clock time, parameters and **current memory m are held fixed**. Π denotes a real channel-permutation matrix; δ=2π/3.

| Input comparison | ρ | h | M | C | T |
|---|---|---|---|---|---|
| $\Omega\mapsto\overline\Omega$ | unchanged | unchanged | unchanged | −C | $\alpha M-\beta C$ |
| $\Omega\mapsto e^{i\chi}\Omega$ | unchanged | unchanged | unchanged | unchanged | unchanged |
| $q\mapsto q+N$ | unchanged | unchanged | unchanged | unchanged | unchanged |
| $\theta\mapsto\theta+\delta$ at held Ω,t,m | unchanged | unchanged | $R_\delta M$ | unchanged | $\alpha R_\delta M+\beta C$ |
| $\Omega\mapsto\Pi\Omega$ | unchanged | unchanged | unchanged | $(\det\Pi)\Pi C$ | $\alpha M+\beta(\det\Pi)\Pi C$ |

The last row is a relabelling of the ordered channel inputs while the clock-defined macro coordinates are held fixed. It is not an assertion that a permutation physically rotates the macro plotting frame. Likewise the θ-shift of T is generally **not** $R_\delta T$, because its chiral term was held fixed.

| Input comparison | J and normalized cubic | Current m | Relation after explicit memory advance |
|---|---|---|---|
| Conjugation | $J\mapsto-J$, $f(J)\mapsto-f(J)$ | Held fixed for the first table | Same m does not generally give m'→−m'. Transforming m→−m as well gives exact sign covariance. |
| Common phase χ | $J\mapsto K\sin\chi+J\cos\chi$, then apply f | Held fixed for the first table | No universal transformation using m and J alone; K and the input history matter. |
| q→q+N | J and f unchanged | unchanged | Update unchanged; advance_ema has no clock input. |
| θ→θ+2π/3 | J and f unchanged | unchanged | Same as above; grid shift requires 3 dividing N. |
| Outer swap 1↔3 | J and f unchanged | unchanged | Update unchanged for identical current memory. |
| Other channel permutations | Conjugated-channel choice changes J as in §9; f follows that value | Held fixed for observation | Innovation generally changes; no general invariant memory history. |

For conjugated **entire EMA histories**, m_n→−m_n follows only if initial memory is also negated and every input state is conjugated, because the update is odd jointly in (m,f(J)). Under that joint transformation, $z_H=h-m$ instead of $h+m$, so $M_H$ generally changes. The staged or fixed-current-memory reflection formula $T(\overline\Omega)=2\alpha M-T(\Omega)$ must not be transferred unchanged to such evolved EMA histories.

The q→q+N comparison leaves readouts equal while raw Clock.q is different. After one modular advance those q representatives agree. Exact angular identities in these tables can have small binary64 trigonometric residuals; they are not promises of bit equality for independently rounded transformed inputs. No recurrence symmetry is inferred. [E §§7–9.3,19; Z; A04]

## 19. Precision and failure domain: recorded, not changed

| Issue | Exact statement | Current finite-precision behavior / checked witness |
|---|---|---|
| Input domain | Finite complex triple; finite real config/time | Shape (3,), numeric type and finite checks. Booleans are not real/integer coefficients under the relevant Z validators. Invalid input typically raises TypeError/ValueError. |
| Raw norm | Finite mathematical norm for finite components | hypot is scale-stable but cannot represent every possible norm. Multiple maximum finite components overflow and raise ResponsePrecisionError; a nonzero subnormal norm is rejected. |
| Saturations | ρ<1 and $\vert f(J)\vert<1$ | 1+κ or 1+|J| can round to the numerator's scale; endpoints 1 or ±1 can result. The policy allows these rounded outputs. |
| Huge q | Reduce q modulo N in integers | q=12·10⁴⁰⁰+3 gives π/2 without float-converting q. Very large N with q=1 may underflow the sector fraction and fail. With q=N−1,N=10⁴⁰, the fraction can round to one, giving float 2π despite the ideal half-open angular range. |
| Clock increment | t'=t+dt | Nonzero dt lost to rounding raises; overflowing or nonzero-subnormal totals also fail. dt=0 can still advance q. |
| Exponential | Positive for finite real exponent | γ=1,t=−1000 overflows; t=710 yields a forbidden subnormal; t=1000 underflows to zero and is rejected. Zero harmonic does not bypass the envelope. |
| Products | Algebraic zero factors give zero | Checked nonzero products that underflow, overflow or become subnormal fail. Exact zero factors have an explicit zero branch after relevant input validation. |
| Cubic association | Multiplication is associative over exact complex numbers | The implementation evaluates $(\Omega_1\overline\Omega_2)\Omega_3$ via checked real products/sums. A bad left pair can fail even if the third factor is zero. |
| Full observation | Formula decomposes into scalar/M/C/T | β=0 does not skip C; α=0 does not skip scalar/M. Subnormal/overflow products in C can fail after scalar success. |
| Blend cancellation | Opposite finite exact terms may sum to zero | Intermediate weighted products are checked before summing. Overflowing terms are rejected even if their exact sum would cancel. |
| Sum cancellation | A sum can be exactly zero | math.fsum plus checks does not provide arbitrary-precision cancellation certification. Zero sums are accepted without a tolerance clamp. |
| Trigonometric zero | $\cos(\pi/2)=0$ | q=1,N=12,ℓ=0 is an exact harmonic zero, but the float evaluation yields a tiny nonzero residual. No “near zero” reclassification is inserted. |
| Memory/scalar domains | Exact formulas exist for all finite Ω and valid m | Ω=(10¹¹⁰,10¹¹⁰,10¹¹⁰) permits an EMA observation with supplied m but cubic evaluation for advance_ema overflows. Observation does not secretly need that cubic calculation. |
| Constructor zero | Stored initial values need no observer evaluation | Large finite components can be stored even where later computed readouts fail; no norm/cubic/chiral exception is triggered merely to construct the zero record. |

NUM checks nonfinite results, nonzero subnormals, and specified lost-nonzero products. Conversion validators do not universally reject every raw subnormal before use; later arithmetic may reject it. This is a conservative intermediate-arithmetic policy, not a proof of small relative error, correct trigonometric argument reduction at every extreme value, or exact cancellation recognition.

For the hand-scale check with binary inputs 3e200 and 4e200, the rounded norm is 4.9999999999999995e200, not the separately rounded decimal literal 5e200. The independent reference evaluates the exact binary input values at 80 digits and bounds the norm error by one ulp. Two retained P9 scalar fixtures also use 80-digit references with the existing bound max(2e−14·|reference|,2e−15); neither tolerance is presented as a universal error bound. [NUM; Z; ZT; P9]

## 20. Clean handoff to Atlas 07

Atlas 06 supplies Ω; Clock and θ; scalar z; decomposed vectors M,C,T; config α,β; current/updated memory; initialization markers; and explicit history ordering. These are the inputs whose later diagnostics can be audited.

The following NEXT interfaces are inventoried only:

| Deferred area | Current interface names |
|---|---|
| Norm and Q accounting | quadratic_form, ReadoutAccounting, readout_accounting |
| Gram/slack area identities | ChiralAreaAccounting, chiral_area_accounting |
| Alignment and unresolved directions | HistoricalAlignment, historical_alignment |
| Intensity budget | IntensityBudget, intensity_budget |
| Potential | potential |
| Direct history coordinates | Coordinates, direct_history_coordinates |
| Cylinder coordinates | cylinder_point, cylinder_history_coordinates |
| History torus | HistoryTorus, history_torus_coordinates |
| Information loss / inverse questions | To be analyzed using the relevant maps and their retained/discarded inputs in Atlas 07 |

No diagnostic derivation, display reconstruction, potential analysis, intensity budget, or inverse-map study is performed here. In particular the cone relation for the **macro** vector is not a claim that the total, a cylinder display, a torus display, and the material shell are the same space.

## 21. Bounded historical comparison ledger

| Finding | Classification | Evidence and limit |
|---|---|---|
| κ,ρ,h, staged z_K, macro factorization, raw C and blend match the explicit current equations | EXACT_CURRENT_MATH | Z and E, independently expanded/proved above. |
| K update_z agrees with current staged observation on six prescribed post-commit inputs | HISTORICAL_REPLAY | Exact snapshot hash, isolated method-body replay, componentwise retained tolerance. Not a full old simulation. |
| H update_z's memory followed by scalar/vector evaluation agrees with advance_ema then observe_ema on six prescribed inputs | HISTORICAL_REPLAY | Same bounded source-body protocol; current memory is explicit. |
| Historical H consumes newly committed Ω before updating z | HISTORICAL_REPLAY | Static phase_lock_step→step order, internal H memory-before-z order, and changed-innovation witness. |
| K/H constructors and first stored row contain zero readouts before recomputation | HISTORICAL_STORAGE_SEMANTIC | Field initializers, pre-step storage loop, current marked compatibility record. |
| Historical n stored rows versus current n+1 run samples | HISTORICAL_STORAGE_SEMANTIC | Distinct inspected recording contracts; no off-by-one repair applied. |
| Clock names containing D24 and historical comments about geometry | STRUCTURAL_ANALOGY | A finite periodic angular scaffold is present. That naming does not supply a physical shell/field map or derive its parameters. |
| Historical words “bounded Z” or “triad chirality” applied to H | EXACT_CURRENT_MATH, with explicit scope | Scalar/memory are bounded under the stated profile; cubic J is distinct from raw quadratic C. No uniform bound on raw T follows just from scalar saturation. |
| A derivation or physical calibration for literal 0.244 and the other toy defaults | OPEN | Not supplied by the inspected accepted observer authority; no archaeology extension undertaken. |
| Historical origin of harmonic three | OPEN | Existing Atlas-01 status retained without investigation. |

The snapshot identities are verified against PROV before their selected methods execute. The preserved scientific labels K/H denote the two already documented sources, not newly inferred chronological stages of a broader project.

## 22. Check results, reproducibility, and integrity

The companion checker constructs independent SymPy expressions and slack factorizations before importing current kernel functions. Runtime and historical tests are separate groups. A finite witness confirms or falsifies a bounded claim; universal statements rest on the displayed mathematical arguments and inspected call graph.

| Group | Passed |
|---|---:|
| EXACT_ALGEBRA | 35 |
| EXACT_BOUNDS | 14 |
| EXACT_SYMMETRY | 22 |
| RUNTIME/API | 37 |
| PRECISION/FALSIFIER | 40 |
| HISTORICAL_REPLAY | 35 |
| INTEGRITY | 16 |

**All 199 predicates passed: 183 scientific/API/replay checks and 16 integrity checks.** The companion JSON is the authoritative count/status receipt. The separate focused repository run passed **65 tests and 155 subtests**, with two diagnostic-named tests deselected. It covered test_z_manifold.py and test_runner_records.py using the torment environment, bytecode disabled, pytest plugin autoload disabled and the cache provider disabled.

Reproduce the scientific audit without writing source files:

~~~powershell
conda activate torment
python -B -X utf8 C:\Users\Notandi\.codex\reports\TRIOCTAGON_ATLAS_06_EXACT_CHECKS.py
~~~

The script defaults to the external evidence directory used in this execution. To make a fresh integrity comparison, use an external directory with --evidence-dir and --capture before, run the audit/tests, then --capture after and --finalize-integrity. The finalizer rejects a checker/source hash mismatch instead of relabelling earlier checks. Initial development or a run without both inventories is explicitly INCOMPLETE until integrity is supplied.

Fingerprint method: enumerate every regular file, including ignored/untracked content, except paths containing a .git component. Hash each file with SHA-256. Hash the sorted-key, compact JSON mapping relative POSIX file paths to those file hashes. Compare full before/after mappings, counts, and aggregate hashes; capture Git HEAD and tracked status separately.

This checks net file-content/path equality across the captured intervals. Enumeration is sequential, not an atomic snapshot. It does not certify timestamps, ACLs, empty directories, separate symlink metadata or .git administrative bytes. Existing untracked material is included in file inventories and was preserved; “tracked status empty” is not a claim that the repository contains no untracked files. Commits/pushes are recorded as actions of this execution, not deduced solely from a working-tree hash.

| Protected scope | Files before = after | Identical before/after tree SHA-256 |
|---|---:|---|
| Current repo | 7,803 | eb913f8b685be59b18ed9cbf1656b06e3d7dcb617b6579e3ec60fc27753dc1df |
| Old kernel_TO | 401 | cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd |
| TORMENT production kernel | 64 | 8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41 |
| Entire production torment_fabric checkout | 173,908 | 3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4 |

The production kernel is also fingerprinted as a dedicated nested scope; it is included in the whole production checkout count. Every before/after file mapping is identical: no added, removed, or content-changed files in any protected scope. Current HEAD remains 34c21830e7e7c4b5f4a5a940d084c37feaf1f82c; production HEAD remains a06edcc5c9df5d3b56405085d9f2942b768dc203. Tracked Git status is unchanged in both. Full inventory locations, their own file hashes, scan intervals and Git receipts are retained in the results JSON.

~~~text
CURRENT_REPO_CHANGED = NO
OLD_KERNEL_CHANGED = NO
TORMENT_CHANGED = NO
COMMITS = 0
PUSHES = 0
~~~

No repository placement or publication is performed. Atlas 07 remains a separate task.
