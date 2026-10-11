# Start here: SRG Origins

**From Geometry to Recursive Operators**  
Hilmir Frímann Halldórsson · v0.1 · 11 October 2026  
Prepared for final GPT publication review; not yet published.

This guide is the four-page opening of [the complete paper](SRG_ORIGINS_v0.1.pdf). The [technical reading text](manuscript/SRG_ORIGINS_v0.1.md) gives every proof, domain and historical qualification. **Historical** means found in a source; **derived** means proved from stated assumptions; **later diagnostic** means a measurement chosen in the October analysis; **illustrative** means example values selected to explain an existing formula.

Guide navigation: [Circles](#1-begin-with-two-circles) · [One loop](#2-one-loop-three-questions) · [Historical lock](#3-how-the-historical-lock-enters) · [Grid update](#4-from-a-field-now-to-a-field-next).

Technical PDF sections: [Geometry, §3](SRG_ORIGINS_v0.1.pdf#page=8) · [Integrals, §4](SRG_ORIGINS_v0.1.pdf#page=10) · [Loop proofs, §5](SRG_ORIGINS_v0.1.pdf#page=12) · [Lock history, §6](SRG_ORIGINS_v0.1.pdf#page=14) · [Operators, §7](SRG_ORIGINS_v0.1.pdf#page=16) · [March adaptations, §8](SRG_ORIGINS_v0.1.pdf#page=19).

## 1. Begin with two circles

**Derived geometry.** Draw two circles, each of radius one length unit, with their centres one unit apart. The upper intersection is one unit from both centres. Join these three points: every side has length one, so the triangle is equilateral. Its height is $\sqrt3/2$. The small circle touching all three sides has radius $r=\sqrt3/6$, because the triangle's area is both half base times height and inradius times semiperimeter. Thus

$$\left(\frac{r}{R}\right)^2=\frac1{12},\qquad R=1.$$

Here $R$ is the radius of either original circle, also the triangle's side. It is **not** the triangle's circumradius. The latter would give $1/4$ instead. Resizing the whole picture preserves both ratios. The PDF labels the centres, intersection, side and inradius.

Four constants enter by four constructions. **$\pi$** is circumference divided by diameter. **$e$** is the limit of ever more finely compounded unit growth, $(1+1/n)^n$. **$\varphi$**, the golden ratio, is the diagonal-to-side ratio of a regular pentagon and the limiting ratio of successive Fibonacci numbers. **$\zeta(3)$** adds inverse cubes:

$$\zeta(3)=1+\frac1{2^3}+\frac1{3^3}+\cdots\approx1.2020569.$$

These connections are exact mathematics. A two-circle diagram alone does not select all four constants or a unique product of them. See technical §§3–4.

## 2. One loop, three questions

**Later diagnostic; derived calculation; illustrative six-site example.** Put six equally spaced sites around a loop of circumference one. A field is simply six numbers, one at each site. A neighbour-difference operator compares each number with its two neighbours; reversing its sign and multiplying by $6^2$ gives a positive operator $A_6$. Its five nonconstant wave modes have squared frequencies

$$36,\quad108,\quad144,\quad108,\quad36.$$

The constant mode has value zero and is omitted. The repeated values count the two directions around the loop. Keep **all** five entries, not only patterns repeated every three sites.

Now ask three different questions about exactly this list.

1. **Add inverses:** $2/36+2/108+1/144=35/432\approx0.081019$. With $N$ sites this is exactly $(1-N^{-2})/12$, approaching **$+1/12$**.
2. **Add inverse powers $3/2$:** $2/36^{3/2}+2/108^{3/2}+1/144^{3/2}\approx0.011620$ (rounded). With more sites this approaches **$\zeta(3)/(4\pi^3)$**. Squared frequencies grow like $k^2$, so this exponent produces inverse cubes $k^{-3}$.
3. **Add frequencies, then subtract a bulk integral:** divide the sum of square roots by $4\pi$ to obtain $S_6=3(2+\sqrt3)/\pi$. Subtract $36/\pi^2$. The difference is about **$-0.083717$**, approaching **$-1/12$** as the loop is refined.

Why is the third answer negative? The samples of a concave sine arch fall below its continuous area. Every frequency is positive; the negative result is what remains after subtracting a larger number. It does **not** say that the ordinary sum $1+2+3+\cdots$ converges to a negative value. Nor does this comparison invalidate other regularizations.

The two appearances of positive $1/12$—in a triangle and in a limiting inverse trace—are equal numbers obtained by different measurements. The negative finite part comes from a third measurement. The loop's scale, zero-mode deletion and powers are declared choices, with proofs in technical §5.

## 3. How the historical lock enters

**Historical definition and interpretation.** The July fusion paper, *Symbolic Recursion and SRG Fusion* (P01, pp.3–4 and Appendix A, pp.19–20), prints

$$\pi e\varphi=\frac{\zeta(3)}{\gamma},
\qquad\gamma_*=\frac{\zeta(3)}{\pi e\varphi}\approx0.0869947475.$$

Its appendix explains the design: circle geometry and growth, golden packing or growth patterns, discrete lattice sums, and a scaling/calibration factor. It reports approximately $0.087$ and distinguishes the relation from a first-principles physical derivation. That rationale is part of the history.

**Later diagnostic choice.** To turn the loop's inverse-power sum into that target, the October analysis explicitly multiplies by

$$\frac{4\pi^2}{e\varphi};
\qquad
\frac{4\pi^2}{e\varphi}\,\frac{\zeta(3)}{4\pi^3}
=\gamma_*.$$

The equality is exact. The multiplier imports the historical normalization; the loop did not independently select it. The source search did not recover an independently specified GammaEstimate or a saved independent measurement selecting the coupling. A later R/D engine actually uses approximately $0.08699$ as an input.

There is also an established, exact golden-interval identity:

$$\zeta(3)=10\int_0^{\log\varphi}t^2\coth t\,dt.$$

The hyperbolic cotangent is $(e^t+e^{-t})/(e^t-e^{-t})$; the integrand has a finite limit at zero. Technical §4.4 proves this classical result through convergent series and the trilogarithm. It is a real mathematical bridge, with established attribution, rather than a new project discovery or an independent selection of the lock's denominator. Technical §6 separates these roles.

## 4. From a field now to a field next

**Historical January composition; illustrative parameters.** An operator is a rule transforming an input. On a periodic grid, opposite edges are neighbours. Start with one nonzero centre:

$$\Theta=\begin{pmatrix}0&0&0\\0&1&0\\0&0&0\end{pmatrix},\qquad
\mathcal L\Theta=\begin{pmatrix}0&1&0\\1&-4&1\\0&1&0\end{pmatrix}.$$

TGMO supplies this neighbour difference. REFU composes it with a nonlinear contribution reading the **same incoming grid**:

$$P=\Theta+0.1\mathcal L\Theta+0.1\tanh\Theta
=\begin{pmatrix}0&.1&0\\.1&c&.1\\0&.1&0\end{pmatrix},
\qquad c=.6+.1\tanh1\approx.6761594.$$

The full order is **incoming state → TGMO and same-state injection → prescribed $H(t)$ gain → RPCO compression → next state**. This example turns H off and uses $L=9$, $\varepsilon=10^{-9}$. RPCO adds $\varepsilon$ to the five positive entries on their inactive branches. Its **paper mode maps each zero corner to one**; its **signed mode keeps those corners zero**. Thus the mode changes the next state even in this small example.

The January names are Toroidal Grid Modulation Operator (TGMO), Recursive Phase-Compression Operator (RPCO) and Recursive Field Update (REFU). July texts and standalone scripts used some of these names for different functions. The March engines explicitly adapted them to moving particles, neighbour graphs and resonance values. An R/D pair adds two real fields, with unequal gains; their names alone do not imply time reversal or complex conjugation.

Recursion means using a result in a subsequent update. A clock-prescribed H curve does not itself accumulate state memory. January fixed-grid theorems, July's unresolved implicit temporal equation and March particle results each retain their own assumptions. Technical §§7–8 show the formulas and distinctions; §9 identifies what remains open.

Continue with the [complete technical paper](manuscript/SRG_ORIGINS_v0.1.md), the [claim ledger](CLAIM_SOURCE_LEDGER.md) and [human-readable source index](SOURCE_INDEX.md). This companion explains existing mathematics; it introduces no replacement recursion or new simulation.
