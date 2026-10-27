# SRG mathematical and operator lineage

11 October 2026 · Bounded mathematical reconstruction · For GPT review

## 1. A worked route a reader can follow

Draw two circles of radius one whose centres are one unit apart. A point where they intersect is one unit from either centre. Those three points therefore form an equilateral triangle. Its height is $\sqrt3/2$; its inscribed circle has radius $\sqrt3/6$. Squaring that radius gives **$1/12$**. No infinite series or physical model is needed.

Now consider the quite different question of what patterns fit around a loop. A smooth wave can fit once, twice, three times, and so on. The squared frequencies grow like $1^2,2^2,3^2,\ldots$. Taking inverse powers $3/2$ turns those squared frequencies into $1,1/8,1/27,\ldots$. Their convergent sum is **$\zeta(3)$**. A finite cycle makes this calculation precise, including its scale and the pair of wave directions.

A third calculation adds positive frequencies and subtracts their continuous bulk approximation. The finite remainder tends to **$-1/12$**. Its sign comes from the subtraction: the sampled sine arch lies below the continuous arch. It is not a negative ordinary sum of positive numbers.

These results fit within one mathematical account, but they are different measurements. The historical SRG lock,

$$\pi e\varphi=\frac{\zeta(3)}{\gamma},\qquad
\gamma_*=\frac{\zeta(3)}{\pi e\varphi}
=0.08699474751703500249752365748\ldots, \tag{1}$$

introduces another choice. The loop calculation supplies $\zeta(3)/(4\pi^3)$. To obtain (1), the October analysis multiplies by $4\pi^2/(e\varphi)$. That multiplier carries the historical target into the new diagnostic. The recovered sources do not determine it from the equilateral triangle or from a measured field statistic.

Finally, a numerical operator answers a different question: “given the current field, what is its next value?” In the January composition, neighbouring values first contribute a discrete Laplacian; a nonlinear contribution reads the same incoming field; a prescribed function $H(t)$ multiplies the result; compression is last. Section 7 works through an actual $3\times3$ mathematical example without executing a source step.

**Main finding.** The exact mathematical connections are substantial and provable. The historical record does not establish one unchanged recursion running from circle geometry to the lock to all later SRG implementations. It records several definitions, some incompatible descriptions, and explicit later adaptations. This report preserves those distinctions.

## 2. Evidence conventions and chronology

**H** means recovered historical definition or claim, **D** a deduction with assumptions stated here, **A** a choice introduced in later analysis, and **U** an unresolved specification or provenance gap. “Historical claim” does not certify its truth.

Page references below are physical PDF pages, counted from one. P01–P19 retain the accepted R0 source identifiers. The full original paths and SHA-256 identities are in SOURCE_CATALOG.md and evidence/CONSUMED_INPUTS.json. Code citations count the first line as one, including a possible BOM. Byte-identical code copies are stored with a .txt suffix and were never imported.

| Date or evidence of date | Source | Mathematical development |
|---|---|---|
| 29 June 2025, internal date | P08/P09 | Golden-scaled nonlinear damping, phase/tensor feedback modules |
| Undated cover; June 2025 metadata is only a locator | P13, p.5 | A distinct “Master Recursive Dual-Phase Collapse Operator” |
| 11 July 2025 | P07, pp.3–6 | Logarithmic RPCO, spatial TGMO formula, REFU and prescribed $H$ |
| 13 July 2025 | P06, pp.4,6 | Earliest internally dated lock equation located in this bounded primary set; inconsistent identification of its $\gamma$ |
| 14 July 2025 | P03, pp.2,5,7–8 | Explicit resonance rule, consistency relation and implicit temporal trail rule |
| 15 July 2025 | P01, pp.3–4; P05 | Lock claimed empirical; patch supplies a different position engine and standalone operators |
| 22 July 2025, cover | Rainman | Geometric analogies and a proposed cycle/period construction |
| 6 September 2025 | P19 | Run-dependent coupling claim, lock penalty, unspecified GammaEstimate |
| 25 January 2026, cover | JANUARY, pp.2–3 and accompanying code | Fully specified fixed-grid composition with two RPCO modes |
| 14 March 2026, internal headers | P18 and March programs | Particle adaptation, R/D coupling, assigned frequency tower and static zeta predictions |
| 9 October 2026 | Received Geometry–Zeta Investigation 01 | Auxiliary normalized loop and three distinct spectral observables |
| October 2026 | Accepted F01, SRG-I, OC01–02 | Source recovery and mathematical analysis; no retroactive alteration of historical equations |

P06 cites earlier work that was not recovered as a target manuscript by the named-reference follow-up. Therefore “earliest located” is not a claim of absolute authorship priority. Dates are not inferred from the current copy time.

## 3. Elementary geometry, $\varphi$, and $e$

### 3.1 Circles and angle projections [D; H comparison: Rainman pp.3–4]

A circle is $(x,y)=R(\cos\theta,\sin\theta)$. Its angle gives separate horizontal and vertical projections. For example,

$$\cos45^\circ=\sin135^\circ=\frac{\sqrt2}{2},
\quad \cos45^\circ\sin135^\circ=\frac12. \tag{2}$$

For equal circles centred at $(0,0)$ and $(d,0)$, subtract
$x^2+y^2=R^2$ and $(x-d)^2+y^2=R^2$. For $0<d\leq2R$ their intersection has

$$x=d/2,\qquad y=\pm\sqrt{R^2-d^2/4}. \tag{3}$$

Thus the midpoint is forced by symmetry. The choice $d=R$ gives the canonical vesica and a $60^\circ$ equilateral triangle; $d=\sqrt2R$ gives a different, $45^\circ$ intersection geometry. They should not be substituted for one another.

Let $a$ be the equilateral triangle's side. Its altitude is $h=\sqrt3a/2$. Area equals both $ah/2$ and inradius times semiperimeter $3ar/2$, so $r=h/3$. Consequently

$$\left(\frac r a\right)^2=\frac1{12}.
\quad\text{For the canonical two-circle triangle, }a=R. \tag{4}$$

Here $R$ denotes the original circles' radius, **not** the triangle's circumradius. The latter is $a/\sqrt3$, and the inradius-to-circumradius squared is $1/4$. This notation distinction is essential.

Uniform resizing does not change (4). In particular $\gamma_*-1/12=0.00366141418\ldots\ne0$. The accepted October geometry note distinguishes its side-one triangle from the octagon edge and full shell height; none are silently identified here.

Rainman's comparison $x=1/2\leftrightarrow\Re s=1/2$ (p.3) assigns the same coordinate to two settings. It provides no map relating circle intersections to zeros of the analytic zeta function. An equal coordinate is not a proof about zeros.

### 3.2 Golden ratio: a particular proportion and a genuine recurrence [D]

For four consecutive vertices of a regular pentagon, Ptolemy's cyclic-quadrilateral identity gives $d^2=s^2+sd$, with side $s$ and diagonal $d$. Dividing by $s^2$ gives $q^2=q+1$, whose positive root is $\varphi=(1+\sqrt5)/2$. The identity also follows by drawing the intersecting diagonals and using the resulting similar triangles. This is additional pentagonal geometry; (3) alone does not force it.

For completeness, the algebraic recursion $F_{n+1}=F_n+F_{n-1}$, $F_0=0,F_1=1$, has characteristic roots $\varphi$ and $\psi=-\varphi^{-1}$. Direct substitution and the two initial conditions prove

$$F_n=\frac{\varphi^n-\psi^n}{\sqrt5},\qquad
\frac{F_{n+1}}{F_n}=
\varphi\frac{1-(\psi/\varphi)^{n+1}}{1-(\psi/\varphi)^n}
\longrightarrow\varphi. \tag{5}$$

The convergence follows from $|\psi/\varphi|<1$, not merely from assuming a limit and solving its equation.

### 3.3 Exponential growth and decay [D; H use: P07 p.6]

Compounding a unit growth rate in $n$ equal pieces gives $(1+1/n)^n$. The integral definition of logarithm yields
$x/(1+x)\leq\log(1+x)\leq x$ for $x>0$. Hence
$n/(n+1)\leq n\log(1+1/n)\leq1$, proving the limit $e$.
The series $\exp t=\sum_{k\geq0}t^k/k!$ differentiates to itself; $\exp(-bt)$ solves $u'=-bu$. This explains the mathematical role of exponentials in prescribed decay curves. It does not select the product $\pi e\varphi$ as a physical coupling.

The base $e$, Euler–Mascheroni constant $\gamma_{\rm EM}$, and the lock value $\gamma_*$ are three different numbers.

## 4. From repeated integration to $\zeta(3)$

### 4.1 A convergent construction [D; H: Rainman p.23]

For $0\leq x<1$, the geometric series gives $f_0(x)=x/(1-x)=\sum_{n\geq1}x^n$. Define
$(If)(x)=\int_0^x f(t)\,dt/t$. Termwise integration is justified by uniform convergence on compact subintervals, or by positivity. Each integration divides the $n$th coefficient by $n$:

$$I^kf_0(x)=\sum_{n\geq1}\frac{x^n}{n^k}
=\operatorname{Li}_k(x),\qquad
\lim_{x\uparrow1}I^3f_0(x)=\sum_{n\geq1}\frac1{n^3}=\zeta(3). \tag{6}$$

The endpoint follows by monotone convergence; $\sum n^{-3}$ is finite by the integral comparison test. This is repeated application of an integration operator. It is not an evolving SRG state, and the choice of three integrations does not derive three spatial dimensions.

Writing all integrations gives

$$I(a)=\int_0^a\frac{dx_1}{x_1}
\int_0^{x_1}\frac{dx_2}{x_2}
\int_0^{x_2}\frac{dx_3}{1-x_3}
=\operatorname{Li}_3(a),\quad0<a\leq1. \tag{7}$$

This validates the scalar iterated integral on Rainman p.23 at $a=1$, with the orientation chosen to agree with positive iterated integration. A differential-form presentation must choose the matching chain orientation.

### 4.2 What changes on the scaled domain [D correction to H: Rainman p.24]

Page 24 sets $a=m_{\max}\gamma$ and $x_i=a u_i$. Both the domain **and the differential form** must transform:

$$\frac{dx_3}{1-x_3}\frac{dx_2}{x_2}\frac{dx_1}{x_1}
=\frac{a\,du_3}{1-a u_3}\frac{du_2}{u_2}\frac{du_1}{u_1}. \tag{8}$$

The factor $a$ in the numerator is required. The result is $\operatorname{Li}_3(a)$, not generally $\zeta(3)$. At $a=1/2$, (7) is $0.5372131936080402\ldots$, versus $\zeta(3)=1.202056903159594\ldots$. For $0<a<1$ strict inequality follows term by term from (6). For $a>1$ the pole at $x_3=1$ obstructs the ordinary integral. A principal value or analytic continuation would require a newly specified prescription.

Using $dx_3/(a-x_3)$ instead would make the pulled-back form standard. That is a **new scale-dependent measure**, not a consequence of the historical formula. This report does not adopt that completion.

### 4.3 The proposed geometric bridge [H/U]

Rainman p.18 and p.20 define their construction using $\gamma=\gamma_*$ at the outset. They cannot then serve as an independent derivation selecting that same constant.

Page 20 chooses an affine translation by $\gamma$ inside projective space. Its $m$th power is a translation by $m\gamma$. In the concrete p.21 map
$T_\gamma([x:y:z])=[x+\gamma z:y:z]$, the forward image of $x=0$ satisfies $x-\gamma z=0$. The printed $x+\gamma z=0$ is its preimage instead. Substituting $(0,y,z)$ into the displayed transformation proves the sign distinction directly.

Nor is the asserted three-dimensional integration chain on p.24 derived from the intersections described there. A curve intersected with a hyperplane in the p.21 example gives points; the text has not supplied a map and dimension/orientation argument producing the real ordered simplex in $X^3$ used on p.23. Non-singularity of a matrix of selected classes alone does not prove they span the intended ambient space: the single vector $(1,0)$ has non-singular Gram matrix $[1]$ but does not span $\mathbb R^2$. These are specific gaps in the proposed bridge, not a rejection of the valid integral (7).

### 4.4 An exact golden-ratio relation [D; classical, reused by October analysis]

Let $q=\varphi^{-1}$ and $\ell=\log\varphi$, so $q+q^2=1$. The following identity genuinely connects the golden split with the trilogarithm:

$$\operatorname{Li}_3(q^2)=
\frac45\zeta(3)-\frac{2\pi^2}{15}\ell+\frac23\ell^3. \tag{9}$$

Here is a full derivation, independent of the proposed vesica chain. For $0<x<1/2$, differentiating the defining series proves
$\operatorname{Li}'_s(x)=\operatorname{Li}_{s-1}(x)/x$ and $\operatorname{Li}_1(x)=-\log(1-x)$. Differentiating and taking the limit at zero then prove the two dilogarithm identities

$$\begin{aligned}
\operatorname{Li}_2(x)+\operatorname{Li}_2(1-x)&=\zeta(2)-\log x\log(1-x),\\
\operatorname{Li}_2(x)+\operatorname{Li}_2(-x/(1-x))&=-\tfrac12\log^2(1-x).
\end{aligned} \tag{10}$$

Put $L=\log(1-x)$. The derivative of
$\operatorname{Li}_3(x)+\operatorname{Li}_3(1-x)+\operatorname{Li}_3(-x/(1-x))$
reduces by (10) to
$[-\zeta(2)+(\log x)L]/(1-x)-L^2/[2x(1-x)]$.
That is exactly the derivative of
$\zeta(3)+\zeta(2)L-\tfrac12\log x\,L^2+\tfrac16L^3$.
Both have limit $\zeta(3)$ at zero, fixing the constant.
Set $x=q^2$. The series also gives
$\operatorname{Li}_3(q)+\operatorname{Li}_3(-q)=\tfrac14\operatorname{Li}_3(q^2)$
by cancelling odd powers. Substitution, $L=-\ell$ and $\log x=-2\ell$, proves (9).

These are standard polylogarithm identities; definitions and the dilogarithm identities can be checked against [NIST DLMF §25.12](https://dlmf.nist.gov/25.12). The derivation above specifies the real domain and integration constant.

The companion identity is $\operatorname{Li}_2(q^2)=\pi^2/15-\ell^2$: apply (10) at $q^2$, and use $\operatorname{Li}_2(q)+\operatorname{Li}_2(-q)=\tfrac12\operatorname{Li}_2(q^2)$. Thus the exact finite-interval forms are

$$\int_0^\ell t^2\coth t\,dt=\frac{\zeta(3)}{10},
\qquad \int_0^\ell t\coth t\,dt=\frac{\pi^2}{20}. \tag{11}$$

To verify, expand $\coth t=1+2\sum_{n\geq1}e^{-2nt}$ and use positivity to integrate termwise. The first integral becomes
$\ell^3/3+\zeta(3)/2-\operatorname{Li}_3(q^2)/2
-\ell\operatorname{Li}_2(q^2)-\ell^2\operatorname{Li}_1(q^2)$.
Since $\operatorname{Li}_1(q^2)=\ell$, (9) cancels the logarithmic terms and leaves $\zeta(3)/10$.
The second is $\ell^2/2+\zeta(2)/2-\operatorname{Li}_2(q^2)/2-\ell\operatorname{Li}_1(q^2)=\pi^2/20$.
These classical Hjortnaes identities are also treated by [Markov (2024)](https://www.diogenes.bg/ijam/contents/2024-37-3/2/2.pdf).

Equation (9) rearranges exactly to

$$\gamma_*=\frac{\tfrac54\operatorname{Li}_3(\varphi^{-2})
+\tfrac{\pi^2}{6}\ell-\tfrac56\ell^3}{\pi e\varphi}. \tag{12}$$

This is an exact evaluation route, not an independent selection of the denominator. For $z=\varphi^{-2}$, truncating the trilogarithm after $K$ terms gives a positive error bounded by
$5z^{K+1}/[4\pi e\varphi(K+1)^3(1-z)]$, by bounding every omitted denominator below by $(K+1)^3$ and summing the geometric tail.

## 5. The three loop observables and the two signs of $1/12$

These calculations independently rederive the accepted October investigation. Their operator scale, zero-mode removal, exponent and bulk subtraction are **A**, not recovered July choices.

### 5.1 Spectrum and exact finite inverse trace

For $N\geq3$ define $(\Delta_Nu)_j=u_{j+1}+u_{j-1}-2u_j$ with periodic indices and $A_N=N^2(-\Delta_N)$. Substituting $u_j=e^{2\pi ikj/N}$ gives

$$\lambda_{N,k}=4N^2\sin^2(\pi k/N),\quad k=0,\ldots,N-1.
\quad Z_N(p)=\sum_{k=1}^{N-1}\lambda_{N,k}^{-p}. \tag{13}$$

The constant mode $k=0$ is deliberately excluded. The factor $N^2$ chooses spacing $1/N$, i.e. unit circumference. For circumference $\mathcal L$, eigenvalues are divided by $\mathcal L^2$ and $Z_N(p)$ is multiplied by $\mathcal L^{2p}$.

Factorization of $z^N-1$ into its $N$ roots, with $z=e^{2ix}$, gives a nonzero constant times
$\prod_{k=0}^{N-1}\sin(x+k\pi/N)=c_N\sin Nx$.
The constant is immaterial to the logarithmic derivative. Differentiating once and then once more gives

$$\sum_{k=0}^{N-1}\cot(x+k\pi/N)=N\cot Nx,\qquad
\sum_{k=0}^{N-1}\csc^2(x+k\pi/N)=N^2\csc^2 Nx. \tag{14}$$

Remove the $k=0$ term and let $x\to0$. The Taylor expansion
$\csc^2x=x^{-2}+1/3+O(x^2)$ cancels the divergent terms, leaving
$\sum_{k=1}^{N-1}\csc^2(\pi k/N)=(N^2-1)/3$. Therefore

$$Z_N(1)=\frac{1-N^{-2}}{12},\qquad
\lim Z_N(1)=\frac1{12}. \tag{15}$$

For example $Z_3(1)=2/27$, not $1/12$. Equality of the limiting number with (4) does not identify a three-node graph with a filled triangle.

### 5.2 The inverse-cube frequency sum

For $1\leq k\leq N/2$, concavity gives $\sin(\pi k/N)\geq2k/N$, so $\lambda_{N,k}\geq16k^2$. Pair $k$ and $N-k$. For fixed $k$, $\lambda_{N,k}\to(2\pi k)^2$, while the paired inverse powers are bounded by $2(16k^2)^{-p}$. This is summable for $p>1/2$. Dominated convergence, extending absent terms by zero, proves

$$\lim_{N\to\infty}Z_N(p)=\frac{2\zeta(2p)}{(2\pi)^{2p}},
\qquad
\lim Z_N(3/2)=\frac{\zeta(3)}{4\pi^3}. \tag{16}$$

The possible unpaired midpoint for even $N$ tends to zero and does not alter the limit. Taking $N$ through multiples of three gives the same full-spectrum result.

By contrast, restricting to states repeated every three nodes keeps only $k=0,N/3,2N/3$. The two nonzero eigenvalues are $3N^2$, hence the restricted sum is $2(3N^2)^{-p}\to0$. With the unscaled operator $-\Delta_N$ they instead stay equal to $3$. Neither case equals the full refinement in (16).

The historically normalized October diagnostic is

$$\gamma_N=\frac{4\pi^2}{e\varphi}Z_N(3/2)
\longrightarrow\gamma_*. \tag{17}$$

The spectral exponent and prefactor are explicit analytical choices. No preceding geometric identity uniquely selects them. For example choosing $p=1$ produces (15) instead, and changing circumference changes the uncorrected trace.

### 5.3 A different observable produces a negative finite part

Define the half-total normalized frequency sum

$$S_N=\frac1{4\pi}\sum_{k=1}^{N-1}\sqrt{\lambda_{N,k}}
=\frac N{2\pi}\sum_{k=1}^{N-1}\sin(\pi k/N). \tag{18}$$

The finite geometric sum of $e^{ik\theta}$ has imaginary part
$\sum_{k=1}^{N-1}\sin(k\theta)
=\sin((N-1)\theta/2)\sin(N\theta/2)/\sin(\theta/2)$.
At $\theta=\pi/N$ this is $\cot(\pi/(2N))$. Replacing the same finite dispersion by its continuous integral gives

$$S_N=\frac N{2\pi}\cot\frac{\pi}{2N},\quad
S_N^{\rm bulk}=\frac N{2\pi}\int_0^N\sin(\pi x/N)\,dx
=\frac{N^2}{\pi^2}. \tag{19}$$

Divide the Taylor series for cosine by that for sine to obtain
$\cot x=x^{-1}-x/3-x^3/45-2x^5/945+O(x^7)$.
Then

$$S_N-S_N^{\rm bulk}
=-\frac1{12}-\frac{\pi^2}{720N^2}
-\frac{\pi^4}{30240N^4}+O(N^{-6}). \tag{20}$$

The sign has a finite geometric explanation: the trapezoidal sum for the strictly concave sine arch lies below its integral; both endpoints are zero. All terms in $S_N$ remain positive. The negative quantity is the **difference** in (20).

This equals the usual analytically continued value $\zeta(-1)$, but the ordinary series $\sum n$ diverges. [DLMF §25.6](https://dlmf.nist.gov/25.6) records the continued integer values. As another direct comparison,

$$\sum_{n\geq1}ne^{-tn}
=\frac{e^{-t}}{(1-e^{-t})^2}
=t^{-2}-\frac1{12}+O(t^2). \tag{21}$$

Changing to half-integer modes gives
$-\frac d{dt}[1/(2\sinh(t/2))]=t^{-2}+1/24+O(t^2)$.
Thus the mode family and subtraction matter. A further oscillator factor $1/2$ halves a coefficient; it does not change the inverse moment in (16) into an energy sum.

Equations (4), (15), (16) and (20) are compatible identities. None says that $\gamma_*$ replaces $-1/12$ or establishes a physical string model.

## 6. The lock equation: what was printed, assigned, or measured

### 6.1 July sources contain a real discrepancy

P06 physical p.4 Eq.(2) prints (1). Its p.6 glossary identifies $\gamma$ as **Euler–Mascheroni's constant**, approximately $0.577$. Those two statements cannot both be exact: substituting $\gamma_{\rm EM}=0.5772156649\ldots$ does not satisfy (1). This report uses the new disambiguating notation $\gamma_*$ for the solved target and $\gamma_{\rm EM}$ for the classical constant; it does not repair the manuscript.

P01 pp.3–4 Eq.(1) repeats the equation, calls $\gamma$ a scaling constant of order $10^{-1}$, describes calibration, and explicitly says the relation was not derived from first principles. Its claim of observation is historical evidence **of the claim**, not a surviving estimator or measurement receipt. P05 p.2 and the position reconstruction instead assign GAMMA $=0.577$; it is unused in that engine.

### 6.2 September's proposed estimator is not an implementation

P19 p.8 describes $\gamma$ as inferred from spectra and adjusted to satisfy the lock. Page 13 calls
$\widehat\gamma^{(t)}\leftarrow\mathrm{GammaEstimate}(\{\Phi_a\},\mathrm{spectra},\zeta(3))$,
without defining the function. The p.12 value $0.10$ occurs in a table explicitly labelled **“Run Stamp (example)”**, with a placeholder commit and incomplete parameter arrays. It is not an independently verified run measurement.

An independently testable estimator would need an explicit map from state/spectral data to a number, its units/normalization and the raw inputs. A lock penalty or tuning procedure that drives a residual toward zero is not, by itself, an independent measurement of the target. Those missing specifications remain **U**.

### 6.3 March saved outputs distinguish predictions from observations

The inert source srg_resonance_lock_analysis.py, line 42, computes gamma_derived as zeta3/lock_product. Lines 443–448 label the odd-zeta extension as a hypothesis. Its saved resonance_lock_results.json contains $\gamma_{\rm SRG}=0.08699474751703501$, the formula itself, and six non-finite eigenmode lock times. This is evidence of a saved formula evaluation and unsuccessful listed searches, not six coupling measurements.

Tower II lines 289–318 explicitly compute the zeta argument from the **assigned** frequency, put the result in **gamma_predicted**, and separately collect lock_time, final_R and final_coherence. The received CSV has 90 rows: 45 formula predictions and 45 blanks. All finite predictions agree with the indicated formula to the precision of the saved numbers; every blank is at a negative tower index. This is a static audit of existing records. No trajectory was regenerated.

Infinity is different: its assigned $0.08699$ actually multiplies the R/D cross term (section 8). Conversely Seed Explorer's $0.0870$ is stored but unused. One cannot infer use merely from a parameter name.

### 6.4 The other “constant one” candidates

The informal phrase does not uniquely name a recovered equation. The bounded phrase search found no literal occurrence in 278 top-level supplied Markdown/text files. It would be unjustified to identify it with the July equation merely because both contain constants. Several distinguishable candidates survive:

| Candidate | Exact source and meaning | Finding |
|---|---|---|
| July lock | P06 p.4 Eq.(2), P01 p.3 Eq.(1) | $\pi e\varphi\gamma=\zeta(3)$; explicit historical target, conflicting $\gamma$ definitions |
| Dual-phase master operator | P13 p.5 | A tensor/phase/floor/compression expression, not the scalar lock |
| A literal equation equal to one | srg_resonance_lock_analysis.py, lines 293–327 | $1=(1+\lambda H/H_{\max})(1+h\mu+\kappa/s)$, an approximate single-mode multiplier condition |
| Frequency master equation | P18 p.7 Eq.(12) | $\pi e\varphi\,\gamma(\omega)=\zeta(2\log_\varphi(\omega/\omega_0)+3)$ |
| DieGlocke lock ratio | DieGlocke_Sim_Core.py, lines 6–14 | $\pi e\varphi\,\gamma_{\rm EM}\zeta(3)$, different algebra from the July lock |

The multiplier equation follows formally by linearizing $\kappa\tanh(\Theta/s)\approx(\kappa/s)\Theta$ on an eigenmode $\mathcal L\Theta=\mu\Theta$, **and** treating compression as identity on the chosen branch. For the actual $\varepsilon>0$ RPCO, the inactive nonzero branch is not exactly identity. The approximation is not a proof of (1), contains no $\zeta(3)$, and does not supply an estimator. The source's $(1,1)$ “fundamental” omits lower nonconstant modes $(1,0)$ and $(0,1)$ of the two-dimensional periodic grid. Its assigned polyhedral names are not spectral identifications proved there.

DieGlocke uses rhs $=1/(\mathrm{GAMMA}\,\mathrm{ZETA3})$, then returns lhs/rhs. Setting that ratio to one would require $\gamma=1/(\pi e\varphi\zeta(3))$, not (1). Moreover GAMMA is actually assigned $0.5772156649$, and the provided Run file neither imports nor calls the ratio. Its time loop freshly samples a product of prescribed fields; earlier composite states are stored for diagnostics, not fed into the next composite (Run lines 37–46). The radial phases, $0.244$, $0.122$, and modulation gamma $0.3$ are explicit inputs, not recovered lock measurements.

P13's master operator includes $\nabla\nabla\cdot\Phi-\Delta\Phi$, floor quantization and feedback, with complex phase $\Phi=e^{i\theta}T$. Its floor/domain and tensor-feedback typing are unresolved, as already recorded in SRG-I §9. It is a distinct historical proposal, not a substitute solver selected here.

**Bounded provenance conclusion.** No implemented independent GammaEstimate or saved independent gamma measurement was recovered in the searched sets. No native rule selecting the inverse exponent $3/2$ and normalization $4\pi^2/(e\varphi)$ was found there. The latter first appears in this inspected chain as an explicitly declared October diagnostic choice. The exact referent of the informal phrase remains unidentified; the competing equations above are now documented without asking the owner to reconstruct them from memory.

## 7. TGMO, REFU and RPCO: precise operator lineage

### 7.1 Earlier names did not denote one unchanged function

P08 p.1 gives the golden stability map $(\varphi/\sqrt3)\tanh x$. Its derivative has absolute value at most $\varphi/\sqrt3<1$, and its output is bounded by that same constant. This is a valid scalar damping statement. It is not the later threshold compressor or either logarithmic RPCO.

P07 pp.3–6 uses “Toroidal Gradient Memory Operator” and “Recursive Entangled Field Update.” It prints a weighted spatial Laplacian and the positive-output logarithmic compressor. Its claim that that compressor retains negative signs contradicts its exponential formula.

P05 p.1 and the surviving standalone scripts instead implement:

* TGMO.py lines 5–14: $(x,y,z)=((2+r\cos\theta)\cos(\pi/4),(2+r\cos\theta)\sin(\pi/4),r\sin\theta)$. This is a sampled minor circle at fixed major angle, repeated through the chosen number of rotations; it is not a field Laplacian.
* REFU.py lines 5–13: the prescribed scalar curve $H(t)$ below, not a full next-state update.
* RPCO.py lines 5–13: $\sin(5\operatorname{atan2}(Y,X))e^{-0.05(X^2+Y^2)}$, a sampled spatial phase field, not a compressor applied to evolving amplitudes.

P11 pp.1–2 correctly distinguishes a constant radius from a field. $\Delta r=0$ for constant $r$, whereas $\Delta\sqrt{x^2+y^2}=1/\sqrt{x^2+y^2}$ away from the origin in two dimensions. The latter is singular at the origin. Promoting a constant radius to a spatial field changes the mathematical object; the alternatives are not interchangeable repairs.

P03 pp.7–8 is also not January's spatial stencil: its trail definition is
$\nabla_T^2\Theta(t)=\Theta(t+1)-2\Theta(t)+\Theta(t-1)$.
Substitution in the printed update gives
$y=C_\lambda(y+b)$, $b=\Theta(t-1)-\Theta(t)+F(t)$, for a finite scalar state and frozen feedback. Its compressor is $C_\lambda(x)=x$ below $\lambda$ and $x/\varphi$ at or above $\lambda$.

The complete branches, reusing accepted SRG-I §4, are

$$\{y:y=C_\lambda(y+b)\}
=\begin{cases}(-\infty,\lambda),&b=0\\\varnothing,&b\ne0\end{cases}
\ \cup\
\begin{cases}\{\varphi b\},&\varphi^2b\geq\lambda\\\varnothing,&\varphi^2b<\lambda.\end{cases} \tag{22}$$

Proof: on the first branch $y=y+b$, requiring $b=0$; on the second $(1-\varphi^{-1})y=\varphi^{-1}b$, giving $y=\varphi b$ and input $\varphi^2b$. This exhibits both no-solution and nonunique cases. No intended root-selection solver is supplied by these sources. Replacing the temporal term by a spatial difference would be a new model choice.

The July position reconstruction, P05 p.2 / recursive_field_evolve.py, uses a fixed directed five-neighbour graph from the starting positions:
$Y=X+0.05\Delta_{\rm graph}X+0.15\tanh(\Delta_{\rm graph}X)$,
then $Z=0.95Y+0.05\overline Y+\xi$ and a small prescribed sinusoidal scaling of $Z$'s third coordinate. It is a concrete alternative evolution, with stochastic position noise, not an implementation of (22).

### 7.2 January's complete fixed-grid composition [H]

For a finite real two-dimensional field, JANUARY pp.2–3 and tgmo.py lines 4–46 define

$$\mathcal L\Theta_{ij}=
a^{-2}(\Theta_{i+1,j}+\Theta_{i-1,j}-2\Theta_{ij})
+b^{-2}(\Theta_{i,j+1}+\Theta_{i,j-1}-2\Theta_{ij}). \tag{23}$$

Indices wrap on both axes. The optional third axis has a separate second difference, reflecting by default. The normalized loop (13) shares the one-axis stencil but adds a positive sign reversal, $N^2$ scaling, zero-mode removal and a spectral observable. January does not compute (17).

For a geometric embedded torus with major radius $a$ and minor radius $b$, the induced Laplace–Beltrami operator would instead contain
$b^{-2}\partial_\theta^2-\sin\theta/[b(a+b\cos\theta)]\,\partial_\theta
+(a+b\cos\theta)^{-2}\partial_\phi^2$.
This follows from the diagonal metric $(b^2,(a+b\cos\theta)^2)$ and the divergence formula. The embedding helper does not make (23) that metric operator. January uses “Toroidal Grid Modulation Operator” for its explicit periodic stencil.

In the app's reference callbacks $D(\Theta,t)=\Theta$ and $f(D)=\kappa\tanh(D/s)$. With a fixed finite positive $H_{\max}$,

$$\begin{aligned}
P(\Theta)&=\Theta+h\mathcal L\Theta+\kappa\tanh(\Theta/s),\\
Q_t(\Theta)&=m_tP(\Theta),\quad m_t=1+\lambda H(t)/H_{\max},\\
\Theta^+&=C_{\rm mode}(Q_t(\Theta)),\\
H(t)&=2e^{-0.5t}\cos t+e^{-0.3t}\sin t+1.5e^{-0.7t}+e^{-0.4t}.
\end{aligned} \tag{24}$$

This order is explicit in refu.py lines 109–138. Both spatial and nonlinear terms read the same incoming $\Theta$; $H$ multiplies before RPCO. Only the spatial term is multiplied by $h$. Calling the scheme “Euler style” does not establish a continuous-time limit with every other per-step operation held fixed.

The library samples $\max|H|$ and adds a guard (lines 25–31). The rollout starts at $t=0$. A custom H requires both its matching Hmax and compute_global_Hmax=False; automatic normalization otherwise evaluates the original H and overwrites the supplied value. Accepted OC01's correction is retained.

### 7.3 The two compressors and their symmetry [D from H]

Let $u=e^{-L}$, $v=e^L$, $L>0,\varepsilon>0$. Moving the exponential through the monotone clamp gives exactly

$$C_p(x)=
\begin{cases}
\operatorname{clip}(x+\varepsilon,u,v),&x>0,\\
1,&x=0,\\
\operatorname{clip}((|x|+\varepsilon)^{-1},u,v),&x<0,
\end{cases}
\quad
C_s(x)=
\begin{cases}\operatorname{sgn}(x)\operatorname{clip}(|x|+\varepsilon,u,v),&x\ne0,\\0,&x=0.\end{cases} \tag{25}$$

These are refu.py lines 37–69 / JANUARY p.3. They imply the exact reciprocal pairing $C_p(a)C_p(-a)=1$ for $a>0$, since clipping in logarithmic space commutes with sign reversal. Signed mode instead has $C_s(-a)=-C_s(a)$. Neither identity is time reversal or an inverse next-state map; a plateau loses magnitude information.

An inactive signed magnitude grows by $\varepsilon$. P18 p.4 Eq.(2) prints an outside-sign formula, but its prose claims $-a\mapsto1/a$. Without epsilon or clipping, that displayed formula returns **$-a$**. January's paper mode has the reciprocal negative branch; the March engines implement signed mode. Substituting one for the other would alter the historical recurrence.

The OC01 corrections remain: signed mode is discontinuous at zero for every $L>0,\varepsilon>0$; paper mode is continuous there exactly when $\varepsilon=1$, and then is $C^1$ but not $C^2$ locally. Indeed it is $1+x$ on the positive side and $(1-x)^{-1}$ on the negative side. Multiplication by a zero gain makes the complete map constant, so discontinuity claims about the compressor do not automatically transfer to that case. Diagnostic samples and update counts remain distinct.

### 7.4 A concrete $3\times3$ mathematical step

Choose a periodic grid, $a=b=1,h=0.1,\kappa=0.1,s=1$, H off, $L=9,\varepsilon=10^{-9}$. These are declared example parameters, not all app defaults. With

$$\Theta=\begin{pmatrix}0&0&0\\0&1&0\\0&0&0\end{pmatrix},
\quad
\mathcal L\Theta=\begin{pmatrix}0&1&0\\1&-4&1\\0&1&0\end{pmatrix},$$

the nonlinear term is nonzero only at the centre, because it reads $\Theta$, not an already diffused state. Thus

$$P(\Theta)=
\begin{pmatrix}0&0.1&0\\0.1&c&0.1\\0&0.1&0\end{pmatrix},
\quad c=0.6+0.1\tanh1=0.6761594155955765\ldots. \tag{26}$$

The centre and four edge entries lie on inactive positive branches. Paper RPCO returns
$\begin{pmatrix}1&0.1+\varepsilon&1\\0.1+\varepsilon&c+\varepsilon&0.1+\varepsilon\\1&0.1+\varepsilon&1\end{pmatrix}$;
signed RPCO returns the same positive entries but keeps all four corners **zero**. This is a full algebraic evaluation of the stated example; no field-step function, field rollout or random initializer was executed.

Accepted OC01's paper-cap result and OC02's signed floor patterns/capture sets are later deductions from (24)–(25), with their stated parameter assumptions. They are not claims found in July manuscripts and do not transfer automatically to March's particle state.

## 8. The March adaptations

### 8.1 Documentary connection and substantive changes

Seed Explorer line 29 explicitly describes the operators as “from your refu.py and tgmo.py, adapted for glyph particles.” Lines 53–57 distinguish its position/resonance particle state from a fixed grid. This is direct documentary lineage; it does not assert identical operators.

For a directed neighbour set $N_i$, the position difference is
$\Delta_iX=|N_i|^{-1}\sum_{j\in N_i}(X_j-X_i)$.
The normalized resonance weights are proportional to $(d_{ij}+10^{-8})^{-1}$.
Seed Explorer lines 91–169 rebuild the Euclidean graph, update
$X_i\leftarrow X_i+0.05\Delta_iX+0.15\tanh(\Delta_iX)$,
mix $R_i$ toward its weighted neighbour mean, multiply by H, move positions toward a resonance-weighted centre, apply a prescribed $0.244$ sinusoid, then apply signed RPCO. Position noise follows. Its pass count increments before the first update, so its first H argument is one, unlike January's zero. There is no toroidal wrapping of these Cartesian positions.

| Version | Precisely supported change | Primary locator |
|---|---|---|
| July reconstructed engine | Position-only state, graph fixed before loop, unweighted centre, third-coordinate sinusoid; assigned GAMMA unused | P05 p.2; early/recursive_field_evolve.py |
| Seed Explorer | Rebuilt kNN graph, separate $R$, weighted resonance mixing and fusion, H and signed amplitude RPCO | lines 29,53–79,91–169 |
| Infinity | Adds real $D$ field, unequal R/D diffusion strengths, actual assigned-gamma cross coupling, shifted H for D | lines 91,114–137,162–195 |
| Condensate Breaking | Separate branch with optional horizon, multifrequency and breathing compression; gamma stored | lines 61–99,155–196 |
| Golden Tower | Fixed assigned golden-spaced bands; log-frequency matching, sinusoid per band, additive golden-ratio resonance mixing, band-local fusion | lines 72–94,122–179 |
| Tower II | Adds configurable stronger mixing over $\varphi^{\pm1},\varphi^{\pm2}$ and sum/difference match tests; optional amplitude-dependent cap; same stage ordering | lines 135–213 |

These are selected source variants, not a claim that every archived program belongs to one linear sequence.

### 8.2 R/D cross coupling uses the assigned gamma

For a row with neighbours, Infinity's default coefficients give

$$\begin{aligned}
R_i'&=R_i+0.15(\overline R_i-R_i)+0.01c_pD_i,\\
D_i'&=D_i+0.075(\overline D_i-D_i)+0.01c_pR_i,\\
c_p&=0.08699\sin(0.244p+\pi/2).
\end{aligned} \tag{27}$$

Both right sides read incoming R/D, and rows without neighbours skip this coupling. Subsequent gains use $H(p)$ and $H(p+\pi/2)$ separately. A time shift of a decaying curve changes its envelope as well as its trigonometric phase. These real fields are not defined as complex conjugates. Equal cross entries alone do not establish sector-exchange symmetry: the diffusion coefficients and later gains differ.

### 8.3 Tower II's actual composition and static master equation

Tower II lines 140–213 fix the graph and distances for that pass, move positions, then construct

$$R_i^{\rm mix}
=a_i\big[(1-\beta)R_i+\beta\sum_jw_{ij}R_j\big]
+\sum_j\eta_{ij}R_j,\quad
a_i=1+0.01\sin(2\pi\omega_i p). \tag{28}$$

Here $\eta_{ij}$ is the sum of the nonnegative golden-ratio and sum/difference match additions in lines 169–188. Those additions occur **after** the per-site sine multiplication; they are not multiplied by $a_i$ there. H then multiplies $R^{\rm mix}$, that precompression resonance controls band-local position fusion, and signed RPCO is last for R. Position noise is separate. This recovers the stage distinction used by accepted R0–R3 without rerunning them.

P18 p.5 Eq.(6) defines $\gamma_m=\zeta(2m+1)/(\pi e\varphi)$ for $m\geq1$. Page 7 assigns $\omega_n=\omega_0\varphi^n$, $\omega_0=0.244$, then states

$$\pi e\varphi\,\gamma(\omega)
=\zeta\!\left(2\log_\varphi(\omega/\omega_0)+3\right). \tag{29}$$

At $\omega_n$ this samples $\zeta(2n+3)$, so matching the older odd-zeta indexing requires **$m=n+1$**, with $n\geq0$. This is an index substitution, not a temporal recursion. The positive Dirichlet-series domain requires $\omega>\omega_0/\varphi$. At $\omega=\omega_0/\varphi$ the zeta argument is one and has a pole. At lower frequencies analytic continuation is a further prescription; it is not a positive coupling at every band. For instance $n=-2$ gives $-\!1/(12\pi e\varphi)$ if analytically continued.

The source's diagnostic explicitly requires zeta_arg > 1.01 and otherwise writes NaN (Tower II lines 293–298). No zeta evaluation occurs in the recovered update (28). The constant-frequency labels are assigned and are not generated by the mix. P18 itself calls the master equation static on p.7. Its limit $\gamma_m\to1/(\pi e\varphi)$ follows from $\zeta(s)\to1$ as $s\to+\infty$; neither that limit nor the CSV proves measured equilibrium couplings equal predictions.

## 9. Claim disposition and remaining definition

The source-grounded chain is:

1. **Recoverable mathematics:** circle projections; exact equilateral ratio; Fibonacci limit; exponential definition; iterated-integral identity; golden polylogarithm identity; cycle spectrum and all three observables.
2. **Recovered historical choices:** July lock formula, competing gamma meanings, threshold compression, prescribed H, January stencil/order/modes, March assigned frequencies and coupling coefficients.
3. **Later analytical choices:** scalar branch analysis with frozen feedback; normalized full-loop refinement and spectral powers; the prefactor importing the lock target; cap/floor and capture theorems.
4. **Incompatible descriptions:** P06's Euler-gamma glossary versus lock; P07's sign-retention claim versus positive exponential; P18's outside-sign equation versus reciprocal prose; Rainman's unchanged scaled integral and forward-image sign.
5. **Underdetermined:** original selector for $\pi e\varphi$; the missing GammaEstimate; an independently measured coupling record; the vesica-cycle-to-integration-chain map; temporal root selection; the exact informal “constant one” referent.

The first three categories support a careful mathematical reconstruction manuscript when attributed and qualified as above. Historical empirical/physical conclusions require evidence beyond these identities. The report proposes no replacement recursion or source repair. The most precise remaining mathematical question is whether an existing native state statistic and an independently specified selection rule choose (17)'s observable and scale. The bounded search found no such specification.

## 10. Review and preservation record

Twenty-two rendered source pages were visually inspected, including the disputed signs, gamma glossary, scaled integral, RPCO formula and master equation. Other selected PDFs were extracted completely and read or searched at the recorded extent; rendering a page is not counted as inspecting an entire manuscript.

There are 24 fresh passing check records in evidence/STATIC_MATH_CHECKS.json. They comprise exact symbolic identities, three small static cycle matrices, scalar evaluations at 80 decimal digits, and a read-only audit of saved CSV/JSON. General proofs are in this report; passing numerical checks are corroboration, not proof by sampling. Received 44-check and OC01–02 records were not replayed.

PROVENANCE_AND_REVIEW_NOTES.md specifies the full bounded search, new qualifications to the supplied note, page observations and tool limitations. SOURCE_CATALOG.md maps aliases to immutable source bytes; CLAIM_SOURCE_LEDGER.md maps substantive claims one-to-one. The package receipt verifies ZIP paths, CRC, member hashes and exact payload coverage. The preservation receipt compares every consumed original with its intake hash; its scope is consumed originals, not an unperformed whole-drive audit.

No source field-step calls, simulations, historical test-suite reruns, random draws, model changes, source repairs, application launches, kernel/UI changes, publication or Git commands were performed.
