# TRIOCTAGON Mathematical Atlas 08 — boundary response, fixed SRG, initialization handoff

Version 0.1 · 29 September 2026 · External source packet · **UNPUBLISHED**

Authority: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics at
**34c21830e7e7c4b5f4a5a940d084c37feaf1f82c**.
This entry reconstructs the existing optional initialization, without modifying source, papers, prior Atlas artifacts, or production. The mathematical conclusion is conditional on the definitions and fixed conventions below; it supplies no physical boundary law.

The complete raw handoff is

\[
 \boxed{\Omega_n=G(\theta)(\chi^\dagger\xi)\lambda_B^n b_n f_j,\qquad
 n=3m+j,\quad b_n=(rq^2c^2)^m(1,q,q^2c)_j.}
\]

This is the exact reduction of preparation → fixed linear transfer → named extraction. Successful binary64 evaluation is a narrower domain than existence of this exact formula. Current modules remain **unsupported v1 internals**, preserved for explicit research use; this entry does not add them to the facade or Runner. The current README states this boundary at lines 55–60 and 117–121.

## 1. Authority, source map, and evidence levels

| ID | Current source | Operative locations / role |
|---|---|---|
| BR | [boundary_response.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/boundary_response.py) | Response ID line 15; theta chart 18–37; polynomial 40–52; area 55–67; gain 70–83; preparation 86 onward |
| SR | [srg.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/srg.py) | Literals 21–28; Fourier 50; operators 57; gauge 75; projection 97; extraction 108; count 114; cycle 122; receipt 134; handoff 154 |
| NUM | [_response_numeric.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_response_numeric.py) | Strict conversion, checked real products, compensated sums; conservative precision domain |
| TBR | [test_boundary_response.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_boundary_response.py) | Geometry/area/gain/preparation, precision and validation witnesses |
| TSR | [test_srg.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_srg.py) | Operators, gauge, reduction, direct transfer, zeros, metadata |
| TBP | [test_boundary_pipeline.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_boundary_pipeline.py) | Existing integration and README replay witnesses, including separate downstream calls |
| README | [kernel README](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/README.md:337) | Explicit research option, initialization-only receipt, numerical stage limits; v1 support boundary near its beginning |
| DYN | [dynamics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py:99) | Existing nonlinear step3; separation from the present initialization |
| Z | [readouts.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py:7) | Subsequent raw chirality observer; no boundary-response feedback |
| OR | [operating_region.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/operating_region.py:15) | Interface inventory only; bounded-profile proof deferred to Atlas 09 |

Evidence levels are kept separate:

1. **Definitions/adoptions:** the area-to-squared-norm response, coherent balanced channel, fixed literals, tensor order, named gauge, and explicit selection.
2. **Exact consequences:** geometric formula, matrix identities, reduction, and inequalities proved below.
3. **Numerical policy:** binary64 conversion, normal-number checks, literal zero, guarded products and residual limits.
4. **Finite witnesses:** independent symbolic predicates and high-precision or binary64 comparisons; test passes are not a theorem count or a guarantee for all finite inputs.
5. **Interpretation:** physical incident calibration, actual boundary/material attachment and physical helicity remain open.

### Accepted review lane

These are read-only contextual records, not alternate executable authorities:

| Record | Dated role and relevant disposition |
|---|---|
| [GPT_BOUNDARY_RESPONSE_TOY_CLOSURE_v0.1.md](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/GPT_BOUNDARY_RESPONSE_TOY_CLOSURE_v0.1.md) | Candidate assumptions and formulas; later reconciliation is attributed within the same record |
| [CODEX_BOUNDARY_RESPONSE_VERIFICATION_v0.1.md](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_BOUNDARY_RESPONSE_VERIFICATION_v0.1.md) | 22 September: conditional mathematical acceptance; area-to-squared-norm and coherent scalar response are assumptions, not consequences of circle geometry |
| [CLAUDE_BOUNDARY_RESPONSE_REVIEW_v0.1.md](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CLAUDE_BOUNDARY_RESPONSE_REVIEW_v0.1.md) | Independent toy-option acceptance, including normality hypothesis for the eigenbra step; no recovered physical law |
| [CODEX_BOUNDARY_RESPONSE_IMPLEMENTATION_v0.1.md](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_BOUNDARY_RESPONSE_IMPLEMENTATION_v0.1.md) | 23 September implementation; **§7 supersedes pending-review language in §§1–6** and closes the implementation within its documented numerical domain |
| [CLAUDE_BOUNDARY_RESPONSE_IMPLEMENTATION_REVIEW_v0.1.md](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CLAUDE_BOUNDARY_RESPONSE_IMPLEMENTATION_REVIEW_v0.1.md) | Review of pre-finish bytes: accepted with nonblocking findings; its writable-array/missing-numeric-clock observations are historical, not current defects |
| [CODEX_BOUNDARY_RESPONSE_FINISH_RESULTS.json](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_BOUNDARY_RESPONSE_FINISH_RESULTS.json) | Finishing receipt identifies current BR, SR, NUM, OR, DYN and Z hashes; numeric clock_fraction and read-only operator arrays are present now |

No historical checker or production module was executed. Old test counts and environments remain attributed to their records. No 0.244 archaeology, harmonic-three provenance work, or Atlas-01 correction was reopened. Reading a record that also contains an operating-profile proof does not import that proof into this entry.

## 2. Equal-circle chart: exact geometry and binary64 input

Use \(R_L>0\) for circle radius to avoid confusing it with the SRG scalar \(r=e^\gamma\). Two equal circles have centre separation \(d\). Their intersection chord bisects the centre line; in either right triangle, adjacent side is \(d/2\), hypotenuse \(R_L\). Define the half-sector angle

\[
\theta=\arccos\frac{d}{2R_L},\quad
0\le d\le2R_L,\quad0\le\theta\le\frac{\pi}{2}.
\]

Cosine is strictly decreasing on this interval, hence this chart is bijective for a fixed positive radius, with inverse \(d=2R_L\cos\theta\). Tangency \(d=2R_L\) gives \(\theta=0\) and zero area. Coincidence \(d=0\) gives \(\theta=\pi/2\) and the full disk. The endpoint formulas are understood by continuity when the chord degenerates.

BR.theta_from_lens validates finite strict real scalars, positive radius, and nonnegative separation. It computes ratio = d/R_L, verifies 0 ≤ ratio ≤ 2, checks loss of a nonzero ratio, checks ratio × 0.5, and returns acos. Forming \((d/R_L)/2\) avoids needless overflow of \(2R_L\): radius and separation \(10^{308}\) give \(\theta\approx\pi/3\).

This does not recover information lost on input conversion. Rounded ratios can merge distinct separations; acos also rounds. The floating API's coincidence endpoint is the stored value math.pi/2, not an exact real representation of \(\pi/2\). A subnormal/lost half-ratio is rejected under the product policy. A ratio rounded outside the interval is a domain error. No exact machine inverse or uniformly accurate reconstruction near tangency is promised.

## 3. Lens area, derivative, convexity, and actual Taylor polynomial

One circular segment is a sector of angle \(2\theta\), area \(R_L^2\theta\), minus a triangle of area \(R_L^2\sin(2\theta)/2\). There are two such segments. Dividing their sum by the full disk area \(\pi R_L^2\) gives the exact definition

\[
 I(\theta)=\frac{2\theta-\sin(2\theta)}{\pi}.
\]

The denominator is one parent disk, not the union area. The endpoints are \(I(0)=0\), \(I(\pi/2)=1\). Direct differentiation gives

\[
 I'(\theta)=\frac{4\sin^2\theta}{\pi},\qquad
 I''(\theta)=\frac{4\sin2\theta}{\pi}.
\]

Thus I is nonnegative, strictly increasing on the whole closed interval, and strictly convex on its interior; the endpoint second derivatives vanish. The first derivative vanishes only at the left endpoint, and is \(4/\pi\) at the right. In particular \(0\le I\le1\).

Expanding sine, the implementation's polynomial is

\[
\begin{aligned}
I(\theta)=\frac{\theta^3}{\pi}\bigg[
&\frac43-\frac4{15}\theta^2+\frac8{315}\theta^4
-\frac4{2835}\theta^6+\frac8{155925}\theta^8
-\frac8{6081075}\theta^{10}\bigg]\\
&+\frac{16}{638512875\pi}\theta^{15}+O(\theta^{17}).
\end{aligned}
\]

The bracket divided by \(\pi\) is precisely the degree-10 polynomial represented by BR._small_factor on its Horner branch. Multiplying by \(\theta^3\) gives degree 13; the first omitted area power is 15, and the first omitted factor power is 12. This follows also from the source coefficients \((-1)^{j+1}2^{2j+1}/(2j+1)!\), \(j=1,\ldots,6\). The leading coefficient is \(4/(3\pi)\), so \(I\sim4\theta^3/(3\pi)\).

For \(0\le\theta\le0.1\), the alternating terms decrease in magnitude. The absolute area truncation error is at most \(16\theta^{15}/(638512875\pi)\), about \(7.98\times10^{-24}\) at 0.1. This bounds Taylor truncation in exact arithmetic; it is not a bound on every binary64 operation. The source uses this polynomial only below 0.1 and uses the direct formula at and above 0.1.

Below \(10^{-8}\), _small_factor returns only \(4/(3\pi)\). The first relative correction is \(-\theta^2/5\); its omitted alternating correction magnitude is below \(\theta^2/5<2\times10^{-17}\). The choice avoids forming an unnecessary tiny square. It does not mean the exact function is constant after division by \(\theta^3\).

For positive small theta, write \(\theta=M2^e\) using frexp, \(1/2\le M<1\). Area is evaluated as ldexp(factor × \(M^3\), \(3e\)). At exact floating endpoints, the functions return 0 or 1 directly. The Taylor polynomial and endpoint branches are evaluation choices for the defined area, not replacement geometric definitions.

## 4. Gain and its larger numerical domain

Define the nonnegative amplitude gain \(G=\sqrt I\). Exact consequences are

\[
G(0)=0,\quad G(\pi/2)=1,\quad0\le G\le1,\qquad
G(\theta)\sim\sqrt{\frac4{3\pi}}\theta^{3/2}.
\]

For \(0<\theta<\pi/2\), \(G'=I'/(2\sqrt I)>0\). Near zero,
\(G=\sqrt{4/(3\pi)}\,\theta^{3/2}(1-\theta^2/10+O(\theta^4))\).
The right derivative tends to zero; the second derivative is unbounded. None of this assigns a physical aperture meaning.

The stable small-angle gain evaluates the square root without first requiring the area to survive. With \(3e=2p+o\), \(o\in\{0,1\}\), the source computes

\[
 G_{\rm approx}=2^p\sqrt{\mathrm{factor}(\theta)\,M^3\,2^o}.
\]

At \(\theta=10^{-120}\), the true area is of order \(10^{-360}\), below binary64's representable nonzero range. The gain is about \(6.5147001587056\times10^{-181}\), a normal number. The area API raises ResponsePrecisionError, while gain and preparation for xi=(1,0) succeed. Each first-block preparation component is about \(3.761263890318375\times10^{-181}\); the other block is zero. The checker compares scaled nonzero values with a 500-digit reference, with zero absolute tolerance so a lost zero cannot pass.

**AREA REPRESENTABILITY != GAIN REPRESENTABILITY.** Squaring the valid tiny gain in binary64 does not restore the true area. Exact \(G^2=I\) is an identity of real functions, not a promise that both machine APIs succeed together.

## 5. Fourier convention on C3

Let \(w=-1/2+i\sqrt3/2=e^{2\pi i/3}\), so \(1+w+\bar w=0\). The exact matrix represented by SR.fourier_basis is

\[
F=(f_0,f_1,f_2)=\frac1{\sqrt3}
\begin{pmatrix}1&1&1\\1&\bar w&w\\1&w&\bar w\end{pmatrix}.
\]

Every column has norm one. Distinct-column inner products vanish by the root sum, hence \(F^\dagger F=I_3\). We have \(f_0=\bar f_0\) and \(f_2=\bar f_1\). In zero-based coordinates, \(f_j(k)=w^{-jk}/\sqrt3\).

Define the forward shift explicitly: \((Sx)_k=x_{k-1\bmod3}\), or \(Se_k=e_{k+1}\). Then \(Sf_j=w^j f_j\), in the order \(1,w,\bar w\). The opposite shift has conjugate eigenvalues. This fixes the source convention; interchanging f1 and f2 would reverse the cycle and its derived orientation signs.

The columns form a coefficient-space basis. The cyclic shift is an algebraic channel permutation. Nothing here identifies channels with three physical arms or six-state entries with spatial cells.

## 6. Raw preparation and modelling assumptions

For an arbitrary incident \(\xi=(\xi_0,\xi_1)^T\in\mathbb C^2\), define

\[
\Psi_0=G(\theta)(\xi\otimes f_0)
=\frac{G}{\sqrt3}
(\xi_0,\xi_0,\xi_0,\xi_1,\xi_1,\xi_1)^T.
\]

The storage index is \(3h+k\): two helicity-major blocks, three C3 entries per block. BR first multiplies each real and imaginary incident part by gain, then by \(1/\sqrt3\), and repeats each resulting complex value three times. The returned complex128 six-vector is fresh and writable; caller inputs are copied and unchanged.

Since \(\|f_0\|=1\), the tensor norm identity gives \(\|\Psi_0\|=G\|\xi\|\), and \(\|\Psi_0\|^2=I\|\xi\|^2\). At fixed theta the exact map is complex-linear in xi; real scaling, negative scaling, and a common complex phase are retained. There is no normalization. Either theta=0 or xi=0 gives raw zero.

The validation order is theta then both incident components, followed by componentwise exact-zero shortcuts. Thus theta=0 does not excuse a NaN incident entry, and xi=0 does not excuse an invalid theta. Tiny nonzero xi is not identified by a squared norm: xi=(\(10^{-300}\),0) survives preparation at \(\pi/2\) even though its computed squared norm underflows.

Geometry determines the overlap area once the chart is chosen. It does **not** determine that area should equal a squared coefficient norm. The accepted response additionally assumes a coherent balanced channel, the same scalar on both incident coordinates, no extra phase/mixing, nonnegative gain, and raw zero at zero input. Within that class the squared-norm rule fixes gain to \(\sqrt I\). Equal intensities alone do not select f0: f1 and f2 also have equal entry magnitudes. This conditional uniqueness is not a derivation of the selected response class from DMQPF.

## 7. Fixed November literals and operator R, C, Z, A

| Stored field | Literal | Classification in this construction |
|---|---:|---|
| eta | 0.423 | HISTORICAL_ADOPTED_LITERAL |
| gamma | 0.577 | HISTORICAL_ADOPTED_LITERAL |
| lambda_c | 0.618 | HISTORICAL_ADOPTED_LITERAL |
| clock_fraction | 0.244 | HISTORICAL_ADOPTED_LITERAL |

NovemberParameters is frozen with these defaults, and fixed_november_srg takes no parameter argument and reads the global NOVEMBER instance. Python can construct a different standalone dataclass instance; that is not a parameter-selection interface for this named pipeline. Directly instantiating its dataclasses is not equivalent to running the validated factory. The accepted operation assumes the module constants have not been monkeypatched.

For exact mathematics interpret these decimal literals as \(423/1000,577/1000,309/500,61/250\). Current execution uses their binary64 approximations. No literal is replaced by a nearby named irrational or derived from another motif. In particular, this entry does not reopen 0.244 provenance.

Let \(P_0=f_0f_0^\dagger=\mathbf1\mathbf1^T/3\), \(Q_0=I-P_0\), and
\[
 q=e^{-\eta},\quad r=e^\gamma,\quad c=1-\lambda_c=191/500.
\]
These q,r,c and \(\alpha=2\pi(0.244),\beta=\pi(0.244)\) are **DERIVED_CONSTANT** values of the fixed adopted option, not free runtime knobs. This scalar q is unrelated to Paper E's clock counter q.

\[
 R=rP_0+qQ_0,\qquad C=P_0+cQ_0,\qquad
 Z=\operatorname{diag}(1,\bar w,w),\qquad A=RZC.
\]

| Operator | On span(f0) | On f0-perpendicular | Exact properties at fixed constants |
|---|---|---|---|
| R | r | q, multiplicity 2 | Positive Hermitian, normal, invertible; not unitary |
| C | 1 | c, multiplicity 2 | Positive Hermitian, normal, invertible; not unitary |
| Z | Does not preserve the common/transverse split separately | Advances Fourier index | Unitary, determinant 1 |

R and C commute with each other, since both are polynomials in P0. Their placement around Z matters: A is RZC, with C acting first. Names such as amplification or attenuation here describe numerical eigenvalue sizes, not material laws.

Since \(Zf_j=f_{j+1\bmod3}\), C acts before the index shift and R after it:

\[
 Af_0=qf_1,\qquad Af_1=qcf_2,\qquad Af_2=rcf_0.
\]

Consequently
\[
 F^\dagger AF=W=
\begin{pmatrix}0&0&rc\\q&0&0\\0&qc&0\end{pmatrix},\qquad
 D_{\rm cycle}=rq^2c^2>0,\qquad A^3=D_{\rm cycle}I.
\]

Thus \(\det A=D_{\rm cycle}\), \(\operatorname{tr}A=0\), and its characteristic polynomial is \(z^3-D_{\rm cycle}\). Its three distinct eigenvalues are \(D_{\rm cycle}^{1/3}w^\ell\), \(\ell=0,1,2\). For any root a, an eigenvector in Fourier coordinates is \((1,q/a,q^2c/a^2)^T\). The Fourier modes themselves are cycled, not individual A eigenvectors.

In Fourier coordinates \(W^\dagger W=\operatorname{diag}(q^2,q^2c^2,r^2c^2)\), so the singular values are the positive weights q,qc,rc. The matrix is normal iff these three squared weights are equal; it is unitary iff they are all one. At the fixed constants neither condition holds. R and C being normal does not make A normal. In particular, replacing its operator norm by its spectral radius without proof would be wrong.

## 8. B, its spectrum, and distinctness

The source multiplication order is
\[
B=\begin{pmatrix}e^{-i\alpha}&0\\0&e^{i\alpha}\end{pmatrix}
\begin{pmatrix}\cos\beta&-i\sin\beta\\-i\sin\beta&\cos\beta\end{pmatrix}.
\]
Each factor is unitary for real angles and has determinant one. Their product is unitary, hence normal, and \(\det B=1\). Its trace is \(2\cos\alpha\cos\beta=2\tau\). Therefore
\[
\det(zI-B)=z^2-2\tau z+1,\qquad
\lambda_\pm=\tau\pm i\sqrt{1-\tau^2}.
\]
For real angles \(|\tau|\le1\); both eigenvalues have unit modulus. They are distinct iff \(|\tau|<1\). Degeneracy requires both cosines to have magnitude one; B then equals \(+I\) or \(-I\). With the linked angles \(\alpha=2\beta=2\pi f\), this occurs precisely at integer f. The adopted f=61/250 is nondegenerate.

An independent useful representation uses Pauli matrices:
\[
B=\tau I-iH,\quad H=\mathbf h\cdot\boldsymbol\sigma,\quad
\mathbf h=(\cos\alpha\sin\beta,\ \sin\alpha\sin\beta,\ \sin\alpha\cos\beta).
\]
One checks \(H^\dagger=H\), \(H^2=\delta^2 I\), and
\(\delta^2=\|\mathbf h\|^2=1-\tau^2\). The checker reconstructs numerical B through this expression before comparison with the source's factor product.

## 9. Full fixed SRG

\[
U=B\otimes A:\mathbb C^2\otimes\mathbb C^3\longrightarrow
\mathbb C^2\otimes\mathbb C^3.
\]

It is a 6×6 matrix with blocks \(B_{ab}A\), in the same helicity-major order as preparation. For product eigenmodes \(B\chi_s=\lambda_s\chi_s\), \(Av_\ell=a_\ell v_\ell\),
\(U(\chi_s\otimes v_\ell)=\lambda_s a_\ell(\chi_s\otimes v_\ell)\).
Both factors are diagonalizable here, so these six product vectors form an eigenbasis. The spectrum is the multiset \(\{\lambda_s D_{\rm cycle}^{1/3}w^\ell\}_{s=\pm,\ell=0,1,2}\). The Kronecker determinant identity gives
\[
\det U=(\det B)^3(\det A)^2=D_{\rm cycle}^2.
\]
Its singular values are those of A, each repeated twice. U is neither normal nor unitary at the fixed literals, since \(U^\dagger U=I_2\otimes A^\dagger A\) and \(UU^\dagger=I_2\otimes AA^\dagger\).

The factory returns fresh read-only R,Z,C,A,B,U arrays; copies are available for separate experiments. No cache is used. These binary64 arrays only approximate the exact identities. U is the fixed initialization transfer; it is not the cubic Paper-A step3/F3 map and introduces no downstream recurrence.

## 10. Named spectral-projector gauge

For either nondegenerate B eigenvalue \(\lambda\), let \(\mu=\bar\lambda\) be the other. Define
\[
 P_\lambda=\frac{B-\mu I}{\lambda-\mu}.
\]

The characteristic identity \((B-\lambda I)(B-\mu I)=0\) gives \(BP_\lambda=\lambda P_\lambda\) and \(P_\lambda^2=P_\lambda\). Equivalently in the Pauli form,
\[
P_-=\frac{I+H/\delta}{2},\qquad
P_+=\frac{I-H/\delta}{2}.
\]
They are Hermitian complementary orthogonal projectors. Trace one and idempotence give rank one; determinant zero is an independent check. The hypothesis \(\delta>0\) is essential.

The named gauge is **spectral_projector_maxdiag_positive_v1**:

1. Select the largest real diagonal entry of P, using np.argmax. Exact ties choose the first index.
2. Let that index be p and set \(\chi=P[:,p]/\sqrt{\operatorname{Re}P_{pp}}\).
3. Canonicalize the pivot's imaginary part to positive zero; preserve its positive real value.

For an exact orthogonal rank-one projector, diagonal entries are nonnegative and sum to one, hence the largest is at least 1/2. Moreover \(\|Pe_p\|^2=P_{pp}\). Thus this construction has unit norm and \(\chi_p=\sqrt{P_{pp}}>0\). It fixes the free eigenvector phase whenever the chosen pivot is nonzero. If the diagonals tie, first-index selection is deterministic; it is not a continuity assertion across every hypothetical parameter change.

Here \(h_z=\sin\alpha\cos\beta>0\), so negative_imag uses \(\lambda_-=\tau-i\delta\) and pivot 0, while positive_imag uses \(\lambda_+=\tau+i\delta\) and pivot 1. Both are verified against the independent Pauli projector. The implementation does not use eigensolver column order. It rejects if either \(\|B\chi-\lambda\chi\|>2\times10^{-14}\) or \(|\operatorname{Re}(\chi^\dagger\chi)-1|>2\times10^{-14}\). The returned chi is read-only.

The pivot is a reproducible coordinate convention, not a physically unique helicity gauge. If B had repeated eigenvalues, this projector quotient would be undefined; the current fixed constants avoid that case.

## 11. Generic bra versus named extraction

Write \(\psi=(\psi^{(0)},\psi^{(1)})\) in two three-vectors. For a supplied \(b\in\mathbb C^2\),
\[
E_b\psi=(b^\dagger\otimes I_3)\psi
=\bar b_0\psi^{(0)}+\bar b_1\psi^{(1)}.
\]
This is project_bra: complex-linear in psi, conjugate-linear in b, not jointly complex-linear. Validation requires shapes (6,) and (2,), respectively. Each component uses checked complex products and compensated real/imaginary sums.

For each channel, Cauchy–Schwarz gives
\(\left|\sum_h\bar b_h\psi_{hk}\right|^2\le\|b\|^2\sum_h|\psi_{hk}|^2\).
Summing k yields \(\|E_b\psi\|\le\|b\|\|\psi\|\), with exact operator norm \(\|E_b\|=\|b\|\). For unit b this is a contraction. An arbitrary supplied b need not have unit norm: b=(2,0) doubles a populated first block.

extract_helicity first obtains the named fixed-B chi, then calls this generic projection. The generic function has no H1/eigenbra or physical-helicity promise. It does not normalize b or threshold overlaps. Both projection functions return fresh writable three-vectors, unlike the read-only handoff result.

## 12. Full-space intertwining, with the correct eigenvalue on the bra

Because B is unitary and \(|\lambda|=1\), \(B\chi=\lambda\chi\) implies \(B^\dagger\chi=\bar\lambda\chi\); taking adjoints gives
\(\chi^\dagger B=\lambda\chi^\dagger\). **The bra identity uses \(\lambda\), not \(\bar\lambda\).** More generally, normality and orthogonal spectral decomposition justify this for a normal B. A right eigenvector of an arbitrary nonnormal matrix would not suffice.

For every integer \(n\ge0\), the Kronecker product identity yields
\[
\begin{aligned}
E_\chi U^n
&=(\chi^\dagger\otimes I)(B^n\otimes A^n)\\
&=(\chi^\dagger B^n)\otimes A^n
=\lambda^n A^n E_\chi.
\end{aligned}
\]

This is an equality of 3×6 operators, hence valid for all six-dimensional inputs, not just prepared states. At n=0 both sides are E_chi. The checker compares the full matrices for both branches and several counts. It also exhibits failure for b=(1,0), which is not a B eigenvector: the generic off-block mixing cannot be replaced by a scalar lambda.

## 13. Cycle gain and transfer count

Applying the Fourier actions in §7 gives
\[
A^0f_0=f_0,\quad Af_0=qf_1,\quad
A^2f_0=q^2cf_2,\quad A^3f_0=rq^2c^2f_0.
\]
Each further block of three contributes the same scalar D_cycle. For \(n=3m+j\), \(j=0,1,2\),
\[
A^nf_0=D_{\rm cycle}^{m}(1,q,q^2c)_j f_j=b_nf_j.
\]
There is no missing Fourier phase factor: the selected Z shifts the columns exactly. The only separate scalar phase in the final handoff is \(\lambda_B^n\) and any incident-overlap phase.

transfer_count accepts Python/NumPy integral values, converts to int, excludes Python and NumPy booleans, and rejects negative integers. A value such as 1.0 is rejected even though mathematically integer-valued. n counts U applications **before** the triad becomes the downstream initial condition. It is neither physical time, a downstream step count, nor Paper E's clock q. n=0 applies no U but still applies preparation and named extraction.

## 14. Derivation of the raw initialization formula

For the selected response, start with \(\Psi_0=G(\xi\otimes f_0)\). Either directly by product action, or by §12,
\[
\begin{aligned}
\Omega_n
&=E_\chi U^n\Psi_0\\
&=G(\chi^\dagger B^n\xi)A^nf_0\\
&=G(\chi^\dagger\xi)\lambda_B^n b_n f_j.
\end{aligned}
\]

SR.handoff_area_response evaluates this reduced formula. It computes the overlap, gain, cycle gain/index, scales the complex amplitude by G and b_n, multiplies by the eigenvalue power, then multiplies by each source Fourier-column entry. It does not iterate an old SRG engine or call step3.

This establishes exact equivalence with prepare → U^n → extract_helicity for the stated real/complex mathematical inputs and conventions. The two floating algorithms use different operation orders, so equality is within measured tolerances, not bitwise equality. Either may fail at an intermediate step even when a differently scaled algorithm could evaluate the final exact result.

The checker uses an independently reconstructed A and B, full six-state powers, both branches, counts 0,1,2,3,7,10, and three nontrivial incident vectors. It separately compares the closed form, full-space intertwining, norm identity, and component magnitudes. Existing package fixtures independently retain direct source U powers and named extraction.

## 15. Five different zero statements

| Case | Exact statement | Current behavior / limitation |
|---|---|---|
| A. theta=0 | G=0, so preparation and handoff vanish | Canonical complex zero after all required input validation |
| B. xi=0 | The tensor input and extracted triad vanish | Componentwise zero test; can bypass unusably tiny gain or very large cycle count |
| C. Computed overlap=0 | A statement about the computed complex sum | Literal comparison, no tolerance; skips gain/cycle evaluation and returns canonical zero |
| D. Exact orthogonality \(\chi^\dagger\xi=0\) | The exact triad is zero for all n,theta | Floating chi/xi need not preserve exact orthogonality; residuals may survive |
| E. Rounded cancellation | A computed zero can have a nonzero exact dot product | Allowed by the compensated-sum policy; it is not an orthogonality certificate |

The handoff validates response, theta, incident shape/components, count, and branch/mode in that order **before** any return of zero. A valid integer count of \(10^{400}\) can accompany exact zero because no transfer amplitude needs evaluation; that does not make the corresponding nonzero case numerically admissible. All zeros in the shortcut result have positive real and imaginary zero signs and the result is read-only.

For a stored chi, the constructed vector \((-\bar\chi_1,\bar\chi_0)\) gives a symmetric calculated cancellation in the tested arithmetic. A separately calculated opposite-branch chi is exactly orthogonal in the ideal model but can leave platform-dependent floating residuals. On this run both opposite-branch checked overlaps were calculated zero; the code does not guarantee that outcome everywhere.

An exact rational counterexample makes the limitation concrete. Let
\[
a=1+2^{-27},\quad b=1-2^{-27},\quad
\mathrm{bra}=(a,1),\quad\mathrm{vector}=(b,-1).
\]
Both a and b are exactly representable binary64 numbers. Their exact dot product is \(ab-1=-2^{-54}\), while the individual product ab rounds to 1; NUM.bra_dot returns calculated zero. Compensated summation cannot recover a term already lost in multiplication. This witness concerns the shared generic numerical kernel, not a claim that this arbitrary bra is a named B mode.

Conversely an explicit overlap near \(10^{-250}\) survives the named handoff at theta=\(\pi/2\), n=0 for both branches, with a scaled reference and zero absolute tolerance. Small is not treated as zero by a threshold.

## 16. Response selection and initialization receipt

handoff_area_response requires keyword arguments transfer_count, branch, and response. Only the exact string **lens_area_norm_v1** passes the response gate. An unknown string or wrong type raises ValueError; omission raises Python's missing-argument TypeError. This is an explicit option, not a default silently selected by the handoff.

HandoffResult has frozen slots omega, theta, xi, transfer_count, branch. Through the factory, omega is a fresh read-only complex128 triad, theta is the validated float, xi is a detached tuple of two complex values, and the count is a nonnegative int. The dataclass itself has no validating __post_init__; these guarantees refer to the factory result, not arbitrary manually constructed records.

metadata() returns a fresh JSON-ready dictionary:

| Key | Current meaning/value |
|---|---|
| response_id | lens_area_norm_v1 |
| source_id | november_fixed_srg |
| source_parameters | eta=.423, gamma=.577, lambda_c=.618, clock_fraction=.244; alpha="2*pi*0.244", beta="pi*0.244" |
| tensor_order | helicity_major_C2_tensor_C3 |
| branch | negative_imag or positive_imag |
| gauge | spectral_projector_maxdiag_positive_v1 |
| theta | Validated supplied aperture coordinate |
| xi | Two [real,imaginary] pairs preserving raw incident values after conversion |
| transfer_count | Initialization transfer count n |
| normalization | none |

It does not contain omega, the downstream configuration, downstream step count, profile choice, original radius/separation, physical calibration, environment or code hashes. It names the gauge and source but does not store eigenvectors or every intermediate product. Callers who need full replay must record those other inputs/identities separately; initial Omega can be an expected comparison result rather than an extra preparation input. The current README demonstrates such a combined record. This packet's results separately store module hashes and interpreter/library versions.

The current numeric clock_fraction and read-only operator arrays are the completed A-1/A-2 fixes documented in the implementation record §7. Older review statements about missing numeric clock_fraction or writable arrays apply to earlier bytes. No further fix was made here.

## 17. Exact norm and component bounds

Set overlap \(o=\chi^\dagger\xi\). With the named unit chi, Cauchy–Schwarz gives \(|o|\le\|\xi\|\). Unit Fourier columns and \(|\lambda_B|=1\) give the exact identity

\[
\|\Omega_n\|=G|o|b_n
\le G b_n\|\xi\|
\le b_n\|\xi\|.
\]

All factors b_n are positive for finite n. The sharper identity retains both G and the actual overlap; bounds do not infer overlap from unknown incident data.

Since every Fourier component has modulus \(1/\sqrt3\),
\[
\max_k|\Omega_{n,k}|=\frac{\|\Omega_n\|}{\sqrt3}
=\frac{G|o|b_n}{\sqrt3}
\le\frac{b_n\|\xi\|}{\sqrt3}.
\]
This component equality is specific to the prepared/extracted Fourier line, not a claim that arbitrary triads have equal moduli. Euclidean norm and maximum component modulus are distinct.

At the adopted constants all three cycle weights are strictly below one. q is in (0,1), and qc<q because \(0<c<1\). For rc, the elementary inequality \(e^t<1/(1-t)\) for \(0<t<1\) follows by differentiating \(-\log(1-t)-t\), whose derivative is \(t/(1-t)>0\). Hence
\[
rc=\frac{191}{500}e^{577/1000}
<\frac{382}{423}<1.
\]
Thus D_cycle<1, \(b_0=1\), and each subsequent b_n decreases by one of q,qc,rc. In particular \(b_n\le1\), so \(\|\Omega_n\|\le\|\xi\|\). Equivalently the full U has operator norm max(q,qc,rc)<1 and named extraction is a contraction.

Approximate derived numbers in the checked environment:

| Quantity | Value |
|---|---:|
| q | 0.6550786331118063 |
| r | 1.780688344599613 |
| c | 0.382 |
| qc | 0.25024003784871 |
| rc | 0.6802229476370522 |
| D_cycle | 0.11150684043720777 |
| tau | 0.027148578726827747 |
| delta | 0.9996314094070441 |

These are initialization bounds and fixed-transfer decay statements. They establish no attraction or stability theorem for the nonlinear downstream dynamics, no radius-three invariant region, and no incident calibration. They do not certify all repeated binary64 operations.

## 18. Numerical domain and failure audit

The exact map exists for finite complex incident values, theta in its exact interval and any finite nonnegative integer n. Current numerical success additionally depends on conversion, intermediate products, cancellation, powers and component checks.

| Stage | Current rule | Consequence / witness |
|---|---|---|
| Real scalar conversion | numbers.Real, excluding bool and np.bool_; convert to float; reject nonfinite or nonzero-to-zero conversion | Strings, complex scalars and 0-D arrays are not silently accepted as theta; domain checks follow |
| Vector conversion | Exact declared one-dimensional shape; entries numbers.Complex, excluding booleans; finite complex128 conversion | Wrong length/nested arrays/strings/nonfinite parts fail even on zero-theta paths |
| Input conversion limits | Real nonzero subnormal inputs are not categorically forbidden; vector conversion guards loss of an entire nonzero entry to zero | Input acceptance does not certify all later operations or conversion of every tiny part of extended-precision inputs |
| checked_real | Nonfinite fails; zero allowed unless nonzero=True; any nonzero result with magnitude below sys.float_info.min fails | This deliberately rejects nonzero subnormal checked results |
| product | If either supplied factor is exactly zero, return canonical 0; otherwise checked binary64 multiplication with nonzero=True | Lost products and nonfinite products raise ResponsePrecisionError rather than silently disappearing |
| Complex multiplication | Four separately checked real products, then real/imaginary compensated sums | A small constituent product can fail even if final complex magnitude is normal; a finite final cancellation can still be unreachable |
| total / bra_dot | math.fsum of already computed products, followed by checks; literal zero allowed | Better summation does not certify relative accuracy near cancellation; §15 counterexample remains |
| Area/gain | Small-angle factorizations; separate normal-range checks | theta=\(10^{-120}\): area fails while gain/preparation/handoff may succeed |
| Preparation | Gain then incident component, then \(1/\sqrt3\), checked separately | theta=\(10^{-20}\), xi=(\(10^{-300}\),0) fails; componentwise zero shortcut avoids squared-norm misclassification |
| Named mode | Spectral quotient at fixed nondegenerate B; eigenvector/norm residual checks | Both branch checks use \(2\times10^{-14}\); they are not an all-input physical certificate |
| Cycle | checked_real(D**m, nonzero=True), then checked partial gain | Decay can leave the normal range; a large incident amplitude does not rescue the cycle calculation |
| Eigenvalue power | Source complex lambda**n and subsequent checked complex product | Exact unit modulus and floating unit modulus are distinct; no all-n phase-error guarantee |
| Final component | Multiply amplitude by each Fourier entry with checked real products/sums | Failures can occur after a normal cycle and amplitude, at a particular real/imaginary component |

sys.float_info.min is approximately \(2.2250738585072014\times10^{-308}\). This is the threshold for checked nonzero real quantities, not a universal lower input-amplitude threshold for the entire pipeline. Exact zeros remain allowed. Some internal trigonometric/matrix operations use ordinary floating arithmetic and do not pass through every shared check.

### Large n: decay versus overflow

For the fixed constants, \(0<D_{\rm cycle}<1\). Its exact nonnegative powers cannot grow or overflow. n=10000 with nonzero incident input raises because the power is lost to zero. An enormous integral count such as \(10^{400}\) can instead cause Python power's exponent conversion to raise OverflowError; the source wraps that as “transfer count exceeds normal cycle-gain range.” The existence of that catch is not evidence that the fixed exact cycle amplifies.

The older implementation review describes a first rejected n=964 as leaving the normal cycle range. That wording must be localized to the evaluation stage and fixture. Current bounded spot checks give:

| n | _cycle_gain alone | Handoff at theta=.7, xi=(1,0), negative_imag |
|---:|---|---|
| 963 | \(1.526809211484379\times10^{-306}\) | Succeeds |
| 964 | \(1.0001800912817018\times10^{-306}\) | Fails: **initial component** subnormal result |
| 965 | \(2.502851038978593\times10^{-307}\) | Fails: **initial component** subnormal result |
| 968 | \(2.7908501144148565\times10^{-308}\) | Fails: **transferred amplitude** subnormal result |
| 969 | Fails: **SRG cycle gain** subnormal result | Same cycle-stage failure |

These are selected stage witnesses, not a universal maximum transfer count: theta, xi, overlap, branch, phase and zero bypasses also matter. The earlier document is left unchanged. No threshold sweep or numerical-policy repair was performed.

### Finite final mathematics does not ensure this evaluation succeeds

Generic projection of two opposite blocks ±\(10^{308}(1,1,1)\) with bra=(2,2) has exact result zero, but each product \(2\times10^{308}\) overflows and the function raises before cancellation. Similarly, computing overlap before a tiny gain, or requiring a cycle to be normal before multiplication by a large incident amplitude, can reject a mathematically finite rescaled result.

No algorithm was reordered, rescaled or patched. Success of initialization does not guarantee success of a later quadratic readout or cubic step; those are separate stages. The Atlas-07 runtime caveat is reported as execution evidence in §22, without diagnosis.

## 19. Interpretation ledger

| Statement / object | Classification | Permitted conclusion |
|---|---|---|
| Equal-circle chart and area formula | EXACT_CURRENT_MATH | Euclidean circle geometry under the stated radius/separation domain |
| Fourier basis, tensor ordering, matrix identities, projectors | EXACT_CURRENT_MATH | Finite-dimensional algebra under the explicit conventions |
| Reduced handoff, norm and component identities | EXACT_CURRENT_MATH | Exact consequences of the selected preparation and fixed operators |
| Choice “area fraction = squared coefficient-norm fraction,” coherent f0 preparation, nonnegative scalar gain | ADOPTED_HISTORICAL_OPTION | Adopted toy response class, not implied solely by circle area |
| Named lens_area_norm_v1 and explicit response gate | ADOPTED_HISTORICAL_OPTION | A caller deliberately selects this mathematical initialization |
| Fixed November literals and fixed option | ADOPTED_HISTORICAL_OPTION | Source-preserved constants; no new origin claim |
| Named positive-pivot gauge | EXACT_CURRENT_MATH | Deterministic coordinate representative of an eigenline, after adopting the convention |
| “Helicity” as the two-mode name | ADOPTED_HISTORICAL_OPTION | Names distinguish B branches; no electromagnetic identification follows |
| Lens/aperture, transfer, channel or shell language used as a physical picture | STRUCTURAL_ANALOGY | May describe the chosen picture; it adds no equation or measured calibration |
| Real incident field, physical lens/membrane coupling, material-shell boundary condition | OPEN_PHYSICAL_INTERFACE | No attachment/calibration supplied by this chain |
| Dark-matter/DMQPF response or electromagnetic helicity | OPEN_PHYSICAL_INTERFACE | No physical recovery or identification established |
| Physical time associated with n or downstream steps | OPEN_PHYSICAL_INTERFACE | Integers are algorithmic counts; no physical time map is derived |

The accepted chain is raw initialization. It supplies no boundary field equation, second recurrence, downstream SRG engine, membrane law, dark-matter response, or new geometry coupling. Historical names do not fill those interfaces.

## 20. Atlas-09 boundary: inventory only

OR is inventoried here, without reproducing its invariant-domain proof:

| Interface | Current identifier / handoff role |
|---|---|
| PROFILE_ID | triad_eps005_g02_k0to8_radius3_v1 |
| UNIFORM_INCIDENT_BUDGET | \(3\sqrt3\), exposed as an optional sufficient-budget constant |
| bounded_config(*, k, phase_strength) | Strict entry to the existing DynamicsConfig under the named profile |
| validate_bounded_triad(state, config, *, profile) | Admission of the actual triad/config; returns a fresh raw copy |
| validate_uniform_incident_budget(xi) | Separate optional incident-budget validator |
| initialize_bounded_area(theta, xi, *, config, profile, transfer_count, branch, response) | Calls the current handoff, then validates the actual initialized triad |
| step_bounded_triad(state, config, *, profile) | Wrapper around one existing step3, with numerical/admission checks |

Atlas 09 will analyze the exact invariant-domain proof, radius-three **component** bound, k in [0,8], eps=1/20, g=1/5, sufficient uniform incident budget, actual initialization admission, and one existing step3 call with no clipping or second recurrence. This entry neither proves nor extends those claims.

The required existing test_boundary_pipeline.py runs its pre-existing downstream integration fixtures. Reporting those tests does not substitute for or start the Atlas-09 mathematical proof. No extra operating-region test suite or new bounded-profile experiment was run.

## 21. Claim-to-check map and checker contract

[TRIOCTAGON_ATLAS_08_EXACT_CHECKS.py](C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_08_EXACT_CHECKS.py) constructs its symbolic expectations before importing the current BR/SR/NUM APIs. It uses:

- exact SymPy circle/Taylor and Fourier/projector identities;
- a Pauli derivation of B and the eigenprojectors independent of the source's factor multiplication;
- a positive delta variable with polynomial reduction modulo \(\delta^2=h_x^2+h_y^2+h_z^2\), explicitly restricted to delta>0;
- 500-digit mpmath references evaluated at the actual supplied binary64 angles;
- independently built U powers and complete 3×6 intertwining matrices;
- exact rational cancellation and concrete adverse-input witnesses.

| Work-order target | Packet proof / boundary | Checker group or existing focused evidence |
|---|---|---|
| 1–3: lens, area, gain | §§2–4 | EXACT_LENS_GEOMETRY, API/PRECISION, TBR |
| 4–5: Fourier and raw preparation | §§5–6 | EXACT_FOURIER_SRG, EXACT_HANDOFF, BOUNDS, TBR |
| 6–9: fixed constants and operators | §§7–9 | EXACT_FOURIER_SRG, API/PRECISION, TSR |
| 10: gauge | §10 | EXACT_SPECTRAL_GAUGE, TSR |
| 11–12: generic/named projection and full-space reduction | §§11–12 | EXACT_HANDOFF, BOUNDS, FALSIFIERS, TSR |
| 13–15: cycle, count, handoff | §§13–14 | EXACT_HANDOFF, API/PRECISION, direct powers and TSR/TBP |
| 16–17: zeros, explicit selection, metadata | §§15–16 | API/PRECISION, FALSIFIERS, TSR |
| 18–19: bounds and numerical failures | §§17–18 | BOUNDS, API/PRECISION, FALSIFIERS |
| 20–21: physical and next-entry boundaries | §§19–20 | Source inspection and classification; no numerical test purports to prove physical meaning |
| 22–24: independent checks, reproducibility, integrity | §§21 onward | Independent result, preserved focused-test streams, separate integrity receipt |

The counts are measured from emitted predicates. Group names containing EXACT include both symbolic checks and clearly tagged floating/API witnesses; each result's kind field distinguishes them. There is no invented target count and no claim that 386 predicates are 386 independent theorems.

The checker requires --output and --scratch. Both resolve outside the selected repo and protected trees; conservatively, the local guard excludes the whole C:/TORMENT tree for outputs. Existing outputs are rejected before imports/scratch creation and opened with exclusive-create mode at completion. --repo can be explicit or discovered from the current directory/ancestors, with the known local authoritative path as fallback. Output paths are never derived from the script location. The checker uses __file__ only to record its own hash.

No historical/production imports, source edits, test subprocesses, installs or network calls occur inside the checker. It disables bytecode writes and directs temporary/cache locations externally. Optional --integrity-directory and --test-receipt attach evidence separately from scientific predicates. Without them, the result says NOT_SUPPLIED and does not certify a new full-tree fingerprint or focused-test execution.

Seven external CLI/relocation checks cover required arguments, no overwrite, protected output, protected scratch, preservation of the existing result, absence of paths after refusal, and execution of a read-only relocated copy from repository cwd without --repo. These are operational checks separate from the 386 scientific/API predicates.

## 22. Executed results and runtime qualification

**ATLAS_08_STATUS = PASS_WITH_RUNTIME_CAVEAT.**
The mathematical/API check result is **PASS**, integrity comparison is **PASS**, and publication remains **NO**.

[TRIOCTAGON_ATLAS_08_EXACT_RESULTS.json](C:/Users/Notandi/.codex/reports/TRIOCTAGON_ATLAS_08_EXACT_RESULTS.json) records **386/386 passed**, zero failed:

| Group | Predicates passed |
|---|---:|
| EXACT_LENS_GEOMETRY | 8 |
| EXACT_FOURIER_SRG | 31 |
| EXACT_SPECTRAL_GAUGE | 27 |
| EXACT_HANDOFF | 85 |
| BOUNDS | 115 |
| API/PRECISION | 107 |
| FALSIFIERS | 13 |
| Total scientific/API predicates | 386 |
| INTEGRITY | Separate full before/after receipt, PASS; not added to mathematical count |

By evidence kind: 59 exact symbolic predicates, 3 import identities, 11 high-precision witnesses, 229 binary64 witnesses, 76 API contracts, 6 counterexamples, 1 call-boundary witness and 1 exact rational counterexample. The many handoff/norm cases exercise branch/count/input combinations; they are not additional independent mathematical theorems.

The final checker used **Python 3.11.15**, **NumPy 2.4.4**, **SymPy 1.14.0**, **mpmath 1.3.0**, from C:/Users/Notandi/miniconda3/envs/torment/python.exe, with -B and -X utf8. It exited 0 with **empty stderr**. Its own source hash is stored in the result, and the external execution receipt binds its result bytes.

The single required focused pytest run selected only TBR, TSR and TBP. It reported:

~~~text
21 passed, 76 subtests passed in 1.65s
returncode = 0
~~~

However, that same run's stderr contained **“Windows fatal exception: access violation”** diagnostics. The raw stdout (126 bytes) and stderr (7193 bytes) were captured separately without decoding/re-encoding the original files. The receipt additionally includes readable text. Therefore the focused assertions passed, but this is **not a runtime-clean test run**. No test retry, anomaly isolation, environment repair or investigation of the Atlas-07 caveat was performed.

| Execution evidence | Receipt |
|---|---|
| Focused test command, timing, exit status, exact stream hashes and readable text | [focused_test_receipt.json](C:/Users/Notandi/AppData/Local/Temp/trioctagon_atlas08_20260929_9d133ee3c2/focused_test_receipt.json), also embedded in the delivered result |
| Unmodified stdout bytes | [focused_stdout.bin](C:/Users/Notandi/AppData/Local/Temp/trioctagon_atlas08_20260929_9d133ee3c2/focused_stdout.bin), SHA-256 a4222f8eb18ff8a1313d69d612f1eb4a94f0cd45e6a24405233915ebf64d1643 |
| Unmodified stderr bytes | [focused_stderr.bin](C:/Users/Notandi/AppData/Local/Temp/trioctagon_atlas08_20260929_9d133ee3c2/focused_stderr.bin), SHA-256 0ef9ab7cbeebbae3adb765e1e10cab8e0f771cfb14465693ad8be9cb80c08f8c |
| Final checker execution | [final_checker_execution.json](C:/Users/Notandi/AppData/Local/Temp/trioctagon_atlas08_20260929_9d133ee3c2/final_checker_execution.json), exit 0, stderr 0 bytes |
| CLI refusal checks | [cli_contract_receipt.json](C:/Users/Notandi/AppData/Local/Temp/trioctagon_atlas08_20260929_9d133ee3c2/cli_contract_receipt.json) |
| Final-byte read-only relocation / cwd discovery | [relocation_final_receipt.json](C:/Users/Notandi/AppData/Local/Temp/trioctagon_atlas08_20260929_9d133ee3c2/relocation_final_receipt.json), exit 0, stderr 0 bytes |

Checker development produced an initial scratch result with ten symbolic false negatives: characteristic-polynomial generator identity and an unstated symbolic positive-delta assumption. The checker was corrected to substitute its polynomial generator explicitly and reduce gauge numerators under delta>0 and delta²=||h||². The original scratch receipt remains [preflight_results.json](C:/Users/Notandi/AppData/Local/Temp/trioctagon_atlas08_20260929_9d133ee3c2/preflight_results.json). Corrected development, final-byte relocation and final authoritative runs all passed 386/386. Those changes were confined to this new external checker, not the scientific sources.

Measured area/gain errors on the eleven 500-digit fixtures were largest at theta=0.1: area relative error about \(7.4931\times10^{-15}\), gain about \(3.7398\times10^{-15}\). Stated acceptance thresholds were \(10^{-14}\) and \(6\times10^{-15}\), respectively. These are fixture measurements, not uniform error bounds. Direct handoff/operator comparisons use explicit relative/absolute tolerances stored per predicate, normally 2e-14/2e-15; tiny witnesses use scaled references and zero absolute tolerance.

## 23. Windows CMD reproduction

No install or environment change is needed. Choose a fresh ATLAS08_REPRO directory/suffix for each execution; the checker refuses to overwrite its result. The following commands are for **Windows CMD**, not PowerShell:

~~~bat
call conda activate torment
set "ATLAS08_REPO=C:\TORMENT\TRIOCTAGON_new\trioctagon-physics"
set "ATLAS08_REPRO=%TEMP%\trioctagon_atlas08_repro_01"
mkdir "%ATLAS08_REPRO%"
set "PYTHONDONTWRITEBYTECODE=1"
cd /d "%ATLAS08_REPRO%"
python -B -X utf8 "C:\Users\Notandi\.codex\reports\TRIOCTAGON_ATLAS_08_EXACT_CHECKS.py" --repo "%ATLAS08_REPO%" --output "%ATLAS08_REPRO%\results.json" --scratch "%ATLAS08_REPRO%\scratch" 1>"%ATLAS08_REPRO%\checker_stdout.txt" 2>"%ATLAS08_REPRO%\checker_stderr.txt"
echo Checker exit code: %ERRORLEVEL%
~~~

That command runs independent mathematics/API witnesses, with historical full-tree/test receipts omitted and clearly labeled NOT_SUPPLIED. It does not run pytest or imply a new integrity certification. --repo may be omitted when the cwd is the authoritative repository or a descendant. The output/scratch parameters remain required even if the checker is eventually placed inside a repository; the read-only relocation test confirms there is no output dependence on script location.

To reproduce the same **focused test selection** once, in a fresh external directory:

~~~bat
set "PYTEST_DISABLE_PLUGIN_AUTOLOAD=1"
set "PYTHONPATH=%ATLAS08_REPO%"
set "MPLCONFIGDIR=%ATLAS08_REPRO%\mpl"
set "XDG_CACHE_HOME=%ATLAS08_REPRO%\cache"
python -B -X utf8 -m pytest -q -p no:cacheprovider --basetemp "%ATLAS08_REPRO%\pytest_temp" "%ATLAS08_REPO%\kernel_physics\tests\test_boundary_response.py" "%ATLAS08_REPO%\kernel_physics\tests\test_srg.py" "%ATLAS08_REPO%\kernel_physics\tests\test_boundary_pipeline.py" 1>"%ATLAS08_REPRO%\focused_stdout.txt" 2>"%ATLAS08_REPRO%\focused_stderr.txt"
echo Focused test exit code: %ERRORLEVEL%
~~~

Retain both streams and distinguish the exit status/test summary from stderr diagnostics. The actual run used the absolute torment executable, stored in the delivered result. [run_focused.py](C:/Users/Notandi/AppData/Local/Temp/trioctagon_atlas08_20260929_9d133ee3c2/run_focused.py) is the actual byte-preserving wrapper, preserved as evidence; its fixed filenames are not an invitation to rerun it over this receipt.

The exact final checker invocation, choosing a new result path for any replay, can attach the existing historical evidence with:

~~~bat
python -B -X utf8 "C:\Users\Notandi\.codex\reports\TRIOCTAGON_ATLAS_08_EXACT_CHECKS.py" --repo "%ATLAS08_REPO%" --output "%ATLAS08_REPRO%\results_with_recorded_receipts.json" --scratch "%ATLAS08_REPRO%\scratch_with_receipts" --test-receipt "C:\Users\Notandi\AppData\Local\Temp\trioctagon_atlas08_20260929_9d133ee3c2\focused_test_receipt.json" --integrity-directory "C:\Users\Notandi\AppData\Local\Temp\trioctagon_atlas08_20260929_9d133ee3c2"
~~~

Attaching these files validates and reports this dated evidence; it does **not** capture a new before/after inventory for a future session. A new integrity claim requires new fingerprints in a fresh external directory. The [fingerprint helper](C:/Users/Notandi/AppData/Local/Temp/trioctagon_atlas08_20260929_9d133ee3c2/fingerprint.py) preserves the established path/content algorithm described below; do not overwrite this entry's before/after receipts.

## 24. Integrity method and scope

The established helper inventories each regular file under each specified root, including ignored/untracked source-tree files, except any path containing a .git component. It hashes file contents in 1 MiB chunks using SHA-256; records relative forward-slash paths and full content hashes; and fingerprints the map by SHA-256 of sorted-key compact JSON. The delivered checker verifies equality of the complete before/after maps **and** recomputes their aggregate digests/counts.

Git HEAD and tracked status are captured separately with --no-optional-locks. Current HEAD is the expected 34c21830e7e7c4b5f4a5a940d084c37feaf1f82c before and after. Production HEAD remains a06edcc5c9df5d3b56405085d9f2942b768dc203. Tracked status is empty for both; this is not a claim that pre-existing untracked material was absent.

| Scope | Before/after file count | Identical path/content fingerprint |
|---|---:|---|
| Current repo | 7,803 | eb913f8b685be59b18ed9cbf1656b06e3d7dcb617b6579e3ec60fc27753dc1df |
| Old kernel_TO | 401 | cec5e60047e01772dde3b8053949dca69c7124378bdca9ce68a7aee96962d2bd |
| Production torment_service/kernel subtree | 64 | 8b11e5bb287212e51dfd8e80fe7a3e96f1c6757e34f3fcc02bdd5eece7f56b41 |
| Full TORMENT production checkout | 173,908 | 3a1a4b061dfbee500f065f053677013573b5f300c847e18c972accac5d512fc4 |

Exact roots:

- C:/TORMENT/TRIOCTAGON_new/trioctagon-physics
- C:/TORMENT/TRIOCTAGON_new/kernel_TO
- C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric/torment_service/kernel
- C:/TORMENT/TORMENT_repo/TORMENT-fabric_v2/torment_fabric

The paper subset under papers/PAPER_A through papers/PAPER_F contains **5,001 unchanged files**. Separately, **21 prior external Atlas artifacts** in C:/Users/Notandi/.codex/reports, including Atlas 01–07 outputs and the harmonic-three/correction ledgers, retain their individual before hashes. Published in-repo Atlas artifacts are included in the unchanged current-tree inventory. No prior artifact was executed as a checker, edited or republished.

The result's separate integrity object contains scope counts/digests/times, Git states, paper/prior comparisons, and paths plus SHA-256 identities for [before.json](C:/Users/Notandi/AppData/Local/Temp/trioctagon_atlas08_20260929_9d133ee3c2/before.json), [after.json](C:/Users/Notandi/AppData/Local/Temp/trioctagon_atlas08_20260929_9d133ee3c2/after.json), both Git receipts and the prior-Atlas manifest. Full inventories remain external. This is a regular-file path/content and Git-state claim, not an ACL, timestamp, whole-disk or .git-internals forensic claim.

Required closeout:

~~~text
CURRENT_REPO_CHANGED = NO
OLD_KERNEL_CHANGED = NO
TORMENT_CHANGED = NO
PAPERS_A_F_CHANGED = NO
PRIOR_ATLAS_CHANGED = NO
COMMITS = 0
PUSHES = 0
ATLAS_08_PUBLISHED = NO
~~~

Atlas 01–05 remain closed/published, Atlas 06 remains closed/external/unpublished, and Atlas 07 remains scientifically closed/external/unpublished with its existing runtime caveat. This entry stops at the Atlas-09 interface inventory.

## 25. Exact source identities

These SHA-256 values bind the inspected current bytes. The delivered result stores absolute paths, byte counts and the same hashes, and verifies that they remain unchanged during the checker. Primary files additionally belong to the full before/after tree inventory.

| Source | SHA-256 |
|---|---|
| [boundary_response.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/boundary_response.py) | febcd7d4dd8c51104dd0b75c7d2fbf14779895099897525aaf892e1833f8116c |
| [srg.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/srg.py) | 90a563d8ef0a18ef769c76d4884e94badbaa38771d4dd192610a4cc74d709d34 |
| [_response_numeric.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_response_numeric.py) | cc33f797e76f7dbeff6fbd58ab52003fde2acbadf35ae299d827b4b55ba29655 |
| [readouts.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py) | 3889051f08c09197224a30263195f8f0d474e5f7b93671fb56e6c240c58e91c9 |
| [dynamics.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py) | ed1af486a2de5176057d49a795bf32f83705f91507a7f108402623a095d535c4 |
| [operating_region.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/operating_region.py) | 4428dc5d1b9a8328da818550c51e1aef489d42ddd8338c19c3185fed9300f160 |
| [README.md](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/README.md) | 431f24a0e5f1ff75ac1cb3ca9b49a40ee9b1005aee6b6bd61d3cb3b54bbc1ac5 |
| [tests/test_boundary_response.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_boundary_response.py) | 6d95629e69ebc0d80c9d16f39286b4c26ce1f4a47c05346cb49b467365cfefe7 |
| [tests/test_srg.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_srg.py) | a74119c3211e7f790a99a0f3eba2574bffaa45482e8a7a3b9ff5a597f28fed59 |
| [tests/test_boundary_pipeline.py](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/tests/test_boundary_pipeline.py) | e820c5ea52c3d53f580cac1427d97935a45a8c35ea10da120b00447c437f64c9 |
| [GPT_BOUNDARY_RESPONSE_TOY_CLOSURE_v0.1.md](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/GPT_BOUNDARY_RESPONSE_TOY_CLOSURE_v0.1.md) | 84f9cb16ea4071b55869b51eff764695e3216ff7eb59cb93ae42a9c3c5b12bd6 |
| [CODEX_BOUNDARY_RESPONSE_VERIFICATION_v0.1.md](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_BOUNDARY_RESPONSE_VERIFICATION_v0.1.md) | c5db2c43b5391edb1e6747b78365d117261791342b939f72f752d6ff1fffa47c |
| [CLAUDE_BOUNDARY_RESPONSE_REVIEW_v0.1.md](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CLAUDE_BOUNDARY_RESPONSE_REVIEW_v0.1.md) | 977916394b017740660a59972a576d01e94e4e4f6b0c78174ff4c428466d7b3e |
| [CODEX_BOUNDARY_RESPONSE_IMPLEMENTATION_v0.1.md](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_BOUNDARY_RESPONSE_IMPLEMENTATION_v0.1.md) | 7d65c0c61560bc93149f307edd4a2f617e4e717cb9c11c356cf543b7444227ae |
| [CLAUDE_BOUNDARY_RESPONSE_IMPLEMENTATION_REVIEW_v0.1.md](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CLAUDE_BOUNDARY_RESPONSE_IMPLEMENTATION_REVIEW_v0.1.md) | afd98682a0156eef171392a2b0d5308b6ea31194835d9ae9f47f1ccaa6e9ce05 |
| [CODEX_BOUNDARY_RESPONSE_FINISH_RESULTS.json](C:/TORMENT/TRIOCTAGON_new/research/GPT_proof/CODEX_BOUNDARY_RESPONSE_FINISH_RESULTS.json) | a7a8627938b080c3da30c1547b4034e5f25f47883d3024eba7a26e46a2904781 |

Delivered checker SHA-256: d8f73688926d65c83e1c7583f53b29152ba588d8945451aa3ebf21bf72b2696c.

Delivered results SHA-256: 637be9be62ad80c56de4d2055f433b478c73d77af3b617154b59a23b7b4d28a5.
