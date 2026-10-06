# THREE-WAY MAP — ITEM 2A — CONSTANT GEOMETRY / EXACT ALGEBRA

**Lane:** playground research only. No TORMENT production code touched, nothing connected to the memory kernel, Brainvision, SQLite runtime, Character Forge, Hivemind or production cognition.
**Object:** the Three-Way reciprocal map

$$F(c;A,B)=\frac{A c^4+B c^2+1}{c^4+B c^2+A}, \qquad u=c^2,\quad G(u;A,B)=\frac{Au^2+Bu+1}{u^2+Bu+A},\quad F=G(c^2).$$

(The dynamical notes Items 1–1G call the same function $f$; this note follows the Item 2A naming and does not call it RTM or SRG.)

**Labels.** Every claim carries one of `[PROVEN]` (exact, checked in `three_way_item2a_checks.py`), `[DERIVED WITH STANDARD THEOREM]` (exact, relies on a named classical theorem), `[NUMERICALLY CONSISTENT]` (high-precision numerics, no proof), `[OPEN]`. Constant-specific findings are additionally sorted into the six bins the brief asks for: `EXACT_IDENTITY`, `ALGEBRAIC_SIMPLIFICATION`, `RECIPROCAL_SYMMETRY`, `SPECIAL_CONSTANT_EFFECT`, `APPROXIMATE_COINCIDENCE`, `NO_STRUCTURE`.

**Sources actually read.** `PLAYGROUND_ORIENTATION_NOTE.md` (its §1.1–1.3 are the captured content of the original Three-Way material: reciprocity, fixed-point quintic, lock values $F=\pm1$), and the modern Items 1, 1C, 1E, 1F, 1G. **The original Three-Way papers themselves were not found** in `C:\TORMENT\playground` or in the project docs (the folder holds only the Item 1–1G files and Codex atlases). §8 therefore reconstructs the "old perturbation experiment" from the brief's description ($F=1/F\Rightarrow F=\pm1$, plus branch stiff, minus branch parameter-sensitive) and gives the exact sensitivities for *each* way the experiment could have been set up, rather than asserting which one it was. Nothing external was added.

**Notation reused from Item 1.** $P=A+1+B$, $Q=A+1-B$, $\lambda=2(A-1)/P$ (so $F'(1)=2\lambda$), $n=P/Q$. One new quantity is used throughout:

$$\beta=\frac{B}{A+1}, \qquad n=\frac{1+\beta}{1-\beta}.$$

---

## 1. BASIC CONSTANT RECIPROCITY `[PROVEN]`

### 1.1 The identity and its proof

$$F(1/c;A,B)=\frac{A c^{-4}+B c^{-2}+1}{c^{-4}+B c^{-2}+A}=\frac{A+Bc^2+c^4}{1+Bc^2+Ac^4}=\frac{1}{F(c;A,B)}$$

wherever both sides are defined (i.e. $c\ne0,\infty$ and neither $c^4+Bc^2+A$ nor $Ac^4+Bc^2+1$ vanishes). The mechanism is that multiplying numerator and denominator of $F(1/c)$ by $c^4$ *reverses the coefficient lists*: $(A,B,1)\to(1,B,A)$ and $(1,B,A)\to(A,B,1)$. Reciprocity is exactly "numerator and denominator are each other's reversal" — this is the whole content of §6.

### 1.2 Log-coordinate form

Put $c=e^{\rho}$ (so $c\mapsto1/c$ is $\rho\mapsto-\rho$) and split the two polynomials into their even and odd parts under the reversal: $N=\tfrac12(P_{\rm num}-Q_{\rm den})=\tfrac12(A-1)(c^4-1)$ and $M=\tfrac12(P_{\rm num}+Q_{\rm den})=\tfrac12[(A+1)(c^4+1)+2Bc^2]$. Dividing both by $c^2$,

$$\boxed{\;F(e^{\rho};A,B)=\frac{\mathcal M+\mathcal N}{\mathcal M-\mathcal N},\qquad \mathcal M=(A+1)\cosh2\rho+B\ \ (\text{even in }\rho),\quad \mathcal N=(A-1)\sinh2\rho\ \ (\text{odd in }\rho)\;}$$

so that

$$\tfrac12\log F=\operatorname{artanh}\frac{\mathcal N}{\mathcal M}=\operatorname{artanh}\frac{(A-1)\sinh2\rho}{(A+1)\cosh2\rho+B}.$$

Reciprocity is now literally "$\tfrac12\log F$ is an odd function of $\log c$". With $A=e^{\alpha}$ ($A>0$) this reads

$$\tanh\!\big(\tfrac12\log F\big)=\frac{\tanh(\alpha/2)\,\tanh(2\rho)}{1+B\,\operatorname{sech}(2\rho)/(A+1)} .$$

For $B=0$ the denominator is $1$ and the map is the hyperbolic Möbius map $M_A(c^4)$ of Item 1; the $B$ term is the only thing that spoils the pure product $\tanh(\alpha/2)\tanh(2\rho)$.

### 1.3 The exact symmetry group of the family (identities in $A,B,c$)

| transformation | effect on $F$ |
|---|---|
| $c\mapsto -c$ | $F\mapsto F$ (even) |
| $c\mapsto ic$ | $F(ic;A,B)=F(c;A,-B)$ |
| $c\mapsto 1/c$ | $F\mapsto 1/F$ |
| $(A,B)\mapsto(1/A,\,B/A)$, $c$ fixed | $F\mapsto 1/F$ (the "outer swap" normalised) |
| $(c;A,B)\mapsto(1/c;\,1/A,\,B/A)$ | $F\mapsto F$ |
| $(c;A,B)\mapsto\big(A^{1/4};\ c^4,\ Bc^2/\sqrt A\big)$ | $F\mapsto F$ (**variable/parameter exchange**, see 1.4) |

**No permutation of the raw slots $(c,A,B)$ is an identity** `[PROVEN]`: all five nontrivial permutations give a rational function different from $F(c;A,B)$ (the difference numerators are non-zero polynomials; §5 lists when they vanish). The structural reason: $F$ is of degree $4$ in $c$ but degree $(1,1)$ — a Möbius transformation — in each of $A$ and $B$ separately:

$$F=\frac{c^4\,A+(Bc^2+1)}{A+(c^4+Bc^2)},\ \det=(c^4-1)(c^4+Bc^2+1);\qquad F=\frac{c^2\,B+(Ac^4+1)}{c^2\,B+(c^4+A)},\ \det=(1-A)\,c^2(c^4-1).$$

Slots of different degree cannot be exchanged by any identity. The two determinants are also the exact statement of *where $F$ stops depending on a parameter*: $F$ is $A$-independent exactly on $c^4=1$ (where $F=1$) and on the palindromic core curve $c^4+Bc^2+1=0$ (where $F=c^4$, see §2); $F$ is $B$-independent exactly at $c\in\{0,\infty,\pm1,\pm i\}$.

### 1.4 The symmetric three-slot form — the cleanest statement of "three-way" `[PROVEN]`

With $X=A$, $Y=c^4$, $\mathsf m=Bc^2$:

$$\boxed{\;F=\mathcal R(X,Y,\mathsf m)=\frac{XY+\mathsf m+1}{X+Y+\mathsf m}\;}$$

which is **symmetric in $X\leftrightarrow Y$**, i.e. in $A\leftrightarrow c^4$ at fixed middle term $Bc^2$. Written back on the raw slots this is the exchange identity in the table: $F(c;A,B)=F(A^{1/4};\,c^4,\,Bc^2/\sqrt A)$ (branches of the roots chosen consistently; checked for positive $A,c$). The reciprocal involution acts as $(X,Y,\mathsf m)\mapsto(X,1/Y,\mathsf m/Y)$ or $(1/X,Y,\mathsf m/X)$ (each inverts $\mathcal R$) and $(1/X,1/Y,\mathsf m/(XY))$ (leaves $\mathcal R$ fixed). In this form the log identity is

$$\tanh\!\big(\tfrac12\log F\big)=\frac{(X-1)(Y-1)}{(X+1)(Y+1)+2\mathsf m}.$$

The "three ways" of the construct are therefore: two *outer* slots ($A$ and $c^4$) entering symmetrically through $XY+1$ and $X+Y$, and one *middle* slot ($Bc^2$) entering additively in both numerator and denominator. This is the picture every later section reduces to.

---

## 2. SPECIAL LEVEL CONDITIONS `[PROVEN]`

Numerator of $F-\text{level}$, factored over $\mathbb Q(A,B)$; second column is the same condition in $(X,Y,\mathsf m)$ when it exists.

| level | exact condition (factored) | in $(X,Y,\mathsf m)$ | collapses? |
|---|---|---|---|
| $F=1$ | $(A-1)(c^4-1)=0$ | $(X-1)(Y-1)=0$ | yes — $B$ absent; $c\in\{\pm1,\pm i\}$ for all $A\ne1$ |
| $F=-1$ | $(A+1)(c^4+1)+2Bc^2=0$, i.e. $u^2+2\beta u+1=0$, $u=c^2$ | $(X+1)(Y+1)+2\mathsf m=0$ | partly — depends on $(A,B)$ only through $\beta=B/(A+1)$; roots $u_\pm=-\beta\pm\sqrt{\beta^2-1}$, $u_+u_-=1$ |
| $F=c$ | $(c-1)\big[c^4+(1-A)c^3+(1-A+B)c^2+(1-A)c+1\big]=0$; $y=c+1/c$: $y^2+(1-A)y+(B-A-1)=0$ | — | to a quadratic in $y$ (palindromic quartic) |
| $F=1/c$ | $(c-1)\big[Ac^4+(A-1)c^3+(A-1+B)c^2+(A-1)c+A\big]=0$; $Ay^2+(A-1)y+(B-A-1)=0$ | — | same, and it is **the fixed-point equation of the swapped parameters** $(1/A,B/A)$ |
| $F=A$ | $(1-A)(Bc^2+A+1)=0$ ⇒ $c^2=-(A+1)/B$ (plus $c=\infty$ twice) | $(X-1)(X+\mathsf m+1)=0$ | yes — linear in $\mathsf m$ |
| $F=1/A$ | $(A-1)c^2\big((A+1)c^2+B\big)=0$ ⇒ $c^2=-B/(A+1)$ (plus $c=0$ twice) | $(X-1)(XY+Y+\mathsf m)=0$ | yes |
| $F=c^4$ | $(c^4-1)(c^4+Bc^2+1)=0$ | $(Y-1)(Y+\mathsf m+1)=0$ | yes — the core curve is $A$-independent |
| $F=1/c^4$ | $(c^4-1)(Ac^4+Bc^2+A)=0$ | $(Y-1)(XY+X+\mathsf m)=0$ | yes |
| $F=B$ | $(A-B)c^4+B(1-B)c^2+(1-AB)=0$ | — | **no**: irreducible over $\mathbb Q(A,B)$ |
| $F=1/B$ | $(AB-1)c^4+B(B-1)c^2+(B-A)=0$ | — | no (reciprocal of the previous) |

What the table says structurally:

* Every level that can be written in the symmetric algebra $(X,Y,\mathsf m)$ **factors**, and the factors are the six "walls" $X=\pm1$, $Y=\pm1$, $X+\mathsf m+1=0$, $Y+\mathsf m+1=0$ and their reciprocal partners. $F=X$ and $F=Y$ are the two outer-slot lines; $F=1$ is the product of the two outer walls; $F=-1$ is the only level that couples all three slots in one irreducible factor.
* Levels that need $c$ itself (not $c^4$) or $B$ itself (not $Bc^2$) do not live in the symmetric algebra and do not collapse beyond the forced factor $(c-1)$ (present in $F=c$ and $F=1/c$ because $1$ is always fixed) — $F=B$ has no forced factor at all.
* $F=c$ and $F=1/c$ are the two halves of one structure: reciprocity maps solutions of $F(c)=c$ at $(A,B)$ to solutions of $F(c)=1/c$ at $(1/A,B/A)$, and the two $y$-quadratics are exactly each other's image under $(A,B)\mapsto(1/A,B/A)$.
* The plus lock $F=1$ and the minus lock $F=-1$ are now visibly different in kind: the plus condition is a *product of one-slot conditions*, the minus condition is the *single irreducible three-slot relation* — this is the algebraic root of §8.

---

## 3. ALGEBRAIC CONSTANT REDUCTION `[PROVEN]`

### 3.1 $\varphi=(1+\sqrt5)/2$, $\varphi^2=\varphi+1$ — `ALGEBRAIC_SIMPLIFICATION` + `SPECIAL_CONSTANT_EFFECT`

$\varphi^4=3\varphi+2$, so

$$F(\varphi;A,B)=\frac{\alpha+\beta_\varphi\varphi}{\gamma+\delta\varphi},\qquad \alpha=2A+B+1,\ \ \beta_\varphi=3A+B,\ \ \gamma=A+B+2,\ \ \delta=B+3 .$$

Rationalising with $\bar\varphi=1-\varphi=-1/\varphi$ and the norm $N(x+y\varphi)=x^2+xy-y^2$:

$$F(\varphi;A,B)=r+s\varphi,\qquad r=\frac{\alpha\gamma+\alpha\delta-\beta_\varphi\delta}{N_\varphi},\quad s=\frac{\beta_\varphi\gamma-\alpha\delta}{N_\varphi},\quad N_\varphi=A^2+3AB+B^2+7A+3B+1 .$$

The special-constant effect is that **numerator and denominator have the same norm**: $N(\alpha+\beta_\varphi\varphi)=N(\gamma+\delta\varphi)=N_\varphi$. Consequently

$$\boxed{\;N\big(F(\varphi;A,B)\big)=r^2+rs-s^2=1\quad\text{for all rational }A,B\;}$$

and the Galois conjugation of $\mathbb Q(\sqrt5)$ acts on the value as **inversion**: $\sigma\big(F(\varphi)\big)=F(\bar\varphi)=F(-1/\varphi)=F(1/\varphi)=1/F(\varphi)$. The reason is not special to $\varphi$'s decimal digits but to $\varphi$ being a *unit* of its field: $\varphi\bar\varphi=-1$ turns Galois conjugation into the map $c\mapsto-1/c$, which evenness plus reciprocity send to $F\mapsto1/F$. The same holds for every quadratic unit: $1+\sqrt2$ (conjugate $-1/(1+\sqrt2)$), $2+\sqrt3$ (conjugate $1/(2+\sqrt3)$), both checked. Consequences: the minimal polynomial of $F(\varphi;A,B)$ over $\mathbb Q$ is

$$t^2-(2r+s)\,t+1 \qquad(\text{trace }F(\varphi)+F(\bar\varphi)=2r+s),$$

so $F(\varphi)$ lies on the norm-one conic $r^2+rs-s^2=1$ and is rational only when $s=0$, i.e. only at the locks $F=\pm1$. Example $(A,B)=(3,5)$: $F(\varphi)=\tfrac{26}{29}+\tfrac{11}{29}\varphi$, minimal polynomial $29t^2-63t+29$.

Reciprocity inside $\mathbb Q(\varphi)$ reads $F(\varphi-1;A,B)=1/F(\varphi;A,B)$ because $1/\varphi=\varphi-1$: the reciprocal of the constant is again a "nice" element — this is the only constant in the list for which that is true (`RECIPROCAL_SYMMETRY` expressed inside the constant's own field).

### 3.2 $\sqrt2$, $\sqrt3$ — `ALGEBRAIC_SIMPLIFICATION` (complete collapse)

The map sees only $c^2$, so

$$F(\sqrt2;A,B)=\frac{4A+2B+1}{A+2B+4},\qquad F(\sqrt3;A,B)=\frac{9A+3B+1}{A+3B+9},\qquad\text{generally } F(\sqrt k)=G(k)=\frac{k^2A+kB+1}{k^2+kB+A}.$$

These are **rational** for rational $A,B$: the square root disappears completely. Galois-theoretically the conjugate of $\sqrt k$ is $-\sqrt k$ and $F$ is even, so $F(\sqrt k)$ is Galois-fixed. Quadratic constants therefore split into exactly two classes under this map: *square-root type* ($\sigma c=-c$, value rational) and *unit type* ($\sigma c=\pm1/c$, value of norm $1$). $\varphi$ is unit type, $\sqrt2,\sqrt3$ are square-root type.

### 3.3 $2$ and $1/2$ — `RECIPROCAL_SYMMETRY` only

$F(2;A,B)=\dfrac{16A+4B+1}{A+4B+16}$, $F(\tfrac12;A,B)=\dfrac{A+4B+16}{16A+4B+1}=1/F(2;A,B)$. Nothing beyond reciprocity.

### 3.4 $\pi$, $e$ — no forced simplification, by design of the brief

$F(\pi;A,B)=G(\pi^2;A,B)$ and $F(e;A,B)=G(e^2;A,B)$; no reduction exists (§4, §9). One coordinate remark only, not a simplification: $e$ is the unit point $\rho=1$ of the log coordinate of §1.2, so

$$F(e;A,B)=\frac{(A+1)\cosh2+B+(A-1)\sinh2}{(A+1)\cosh2+B-(A-1)\sinh2}$$

(`SPECIAL_CONSTANT_EFFECT`, weak: it is a restatement, not a reduction). $\pi$: `NO_STRUCTURE`.

---

## 4. ALGEBRAIC DEGREE QUESTION

Let $c$ be algebraic of degree $d$ over $\mathbb Q$.

**$A,B$ rational** `[PROVEN]`. $F(c)\in\mathbb Q(c^2)$ and $[\mathbb Q(c^2):\mathbb Q]\in\{d,\,d/2\}$; it is $d/2$ exactly when the minimal polynomial of $c$ is a polynomial in $c^2$ (equivalently $-c$ is a conjugate of $c$, equivalently $c\notin\mathbb Q(c^2)$). So $\deg F(c)$ divides $d$, and divides $d/2$ in the even case. Generically it equals $[\mathbb Q(c^2):\mathbb Q]$; it drops further only when $G$ identifies two conjugates of $c^2$. Examples (all at $(A,B)=(3,5)$, degrees computed): $\sqrt2\to1$, $\varphi\to2$, $2^{1/3}\to3$, $2^{1/4}\to2$, $2^{1/8}\to4$. For unit-type quadratic $c$ (§3.1) the degree is $2$ unless $F=\pm1$.

**$A,B$ algebraic** `[PROVEN]`. $F(c)\in\mathbb Q(A,B,c^2)$, degree at most $[\mathbb Q(A,B,c^2):\mathbb Q]\le\deg A\cdot\deg B\cdot d$; the exact norm-one statement of §3.1 needs $\sigma(A)=A,\sigma(B)=B$ and survives when $A,B$ lie in a field on which the conjugation fixing $\sigma c=\pm1/c$ acts trivially.

**One or both parameters transcendental** `[DERIVED WITH STANDARD THEOREM]`. Since $F$ is a Möbius function of $A$ with determinant $(c^4-1)(c^4+Bc^2+1)$, if $A$ is transcendental over $\mathbb Q(B,c)$ and $c^4\ne1$, $c^4+Bc^2+1\ne0$, then $F(c;A,B)$ is transcendental over $\mathbb Q(B,c)$ (a non-degenerate Möbius image of a transcendental is transcendental). Same for $B$ with the exceptional set $c\in\{0,\infty,\pm1,\pm i\}$, $A\ne1$. If instead $c$ is transcendental and $A\ne1$, $B$ algebraic, $F(c)$ is transcendental (non-constant rational function with algebraic coefficients of a transcendental). Hence $F(\pi;A,B)$ and $F(e;A,B)$ are transcendental for all algebraic $A\ne1,B$ (Lindemann, Hermite).

**Everything transcendental** `[OPEN]` — and open for a standard reason, not a playground one. Whether $F(\pi;\varphi,e)$, $F(\varphi;\pi,e)$, … are transcendental, or even irrational, depends on the algebraic independence of $\pi$ and $e$, which is not known (it would follow from Schanuel's conjecture). The map cannot manufacture a decision here: since $F$ is Möbius in $A$, *any* target value is hit by exactly one $A$, so a constant-slot value can be rational for suitable transcendental $A$. All six permutation values in §5 are therefore of unknown arithmetic nature, and no claim is made.

---

## 5. CONSTANT PERMUTATIONS

### 5.1 Structural statement `[PROVEN]`

The only exact identities relating different fillings of the three slots are those of §1.3 — the reciprocal group and the $A\leftrightarrow c^4$ exchange. None of them is a permutation of the raw constants. Two raw permutations coincide exactly on an explicit hypersurface; for the three transpositions these factor as

$$F(c;A,B)=F(c;B,A)\iff (c^4-1)(A-B)\big(c^4+(A+B-1)c^2+1\big)=0,$$
$$F(c;A,B)=F(A;c,B)\iff (A-1)(c-1)(c-A)\,\Sigma_1(A,B,c)=0,\qquad F(c;A,B)=F(B;A,c)\iff (A-1)(c-B)\,\Sigma_2(A,B,c)=0,$$

with $\Sigma_1,\Sigma_2$ irreducible of total degree $6$ (listed by the script). The first is the useful one: swapping $A$ and $B$ is invisible not only when $A=B$ or $c^4=1$ but on the extra curve $c^4+(A+B-1)c^2+1=0$ — a "middle-outer exchange curve" that is again palindromic in $c$. The remaining twelve pairwise conditions are irreducible or carry only the trivial factors $A-1$, $B-1$, $c-1$, $A\pm1$, $B\pm1$, $c-A$, $c-B$, $A-B$.

### 5.2 The six values for $\{\pi,e,\varphi\}$ `[PROVEN unequal; arithmetic nature OPEN]`

```text
F( pi ;  e , phi) = 2.42689627636222621003539712919
F( pi ; phi,  e ) = 1.47343262068597109815441228824
F(  e ;  pi, phi) = 2.64695606498098749585893534103
F(  e ; phi,  pi) = 1.41704205108596444343193933960
F(phi ;  pi,  e ) = 1.73263905189546744885475107109
F(phi ;  e ,  pi) = 1.56520173145846962012078890737
minimum pairwise separation 0.0564   (50-digit evaluation)
```

All fifteen pairs are unequal: a nonzero difference at 50 digits is a proof of inequality, and no algebraic relation among $\pi,e,\varphi$ is needed for that. The exchange identity checks on the constants: $F(\pi;\varphi,e)=F(\varphi^{1/4};\pi^4,e\pi^2/\sqrt\varphi)$ to 50 digits. Nearest rationals with denominator $\le50$ differ by $10^{-3}$–$10^{-5}$ (the closest, $F(\varphi;e,\pi)\approx36/23$, by $1.6\cdot10^{-5}$); with 300 candidate fractions per value this is the expected size of the best miss, so every one of these is `NO_STRUCTURE`. No `APPROXIMATE_COINCIDENCE` is recorded.

Reciprocal pairs at the default point $(A,B)=(\pi,e)$ all satisfy $F(1/c)F(c)=1$ to $10^{-50}$ — `RECIPROCAL_SYMMETRY`, expected. Values for the record: $F(\pi)=2.6209$, $F(e)=2.4749$, $F(\varphi)=1.7326$, $F(\sqrt2)=1.5108$, $F(\sqrt3)=1.8441$, $F(2)=2.0703$, $F(1/2)=0.4830$.

---

## 6. OUTER-SWAP / MIDDLE-FIXED STRUCTURE (high priority) `[PROVEN]`

### 6.1 The grammar $P=Au+Bv+1$, $Q=u+Bv+A$

Require $F(1/c)=1/F(c)$ as an identity in $A$ and $B$. Writing $u'=u(1/c)$, $v'=v(1/c)$, the condition $P(1/c)P(c)=Q(1/c)Q(c)$ expanded in monomials of $(A,B)$ gives exactly four coefficient equations, of which two are independent:

$$\boxed{\;u(1/c)\,u(c)=1,\qquad v(1/c)=\frac{v(c)}{u(c)}\;}\qquad\Big(\text{equivalently } \frac{v^2}{u}\text{ is invariant under }c\mapsto1/c\Big).$$

So the most general pair is $u=$ any function with $\log u$ odd in $\log c$, and $v=\sqrt u\cdot k$ with $k$ any function even in $\log c$. The original $(c^4,c^2)$ is $u=c^4$, $k\equiv1$. Non-obvious members: $(u,v)=(c^4,\,c^3+c)$ works ($k=c+1/c$), $(c^4,\,c^4+1)$ works ($k=c^2+c^{-2}$), while $(c^4,\,c^2+1)$ fails — all three checked. $u$ itself may be any reciprocal map (e.g. $u=(c^2+a)/(ac^2+1)$), so the grammar nests.

### 6.2 The general reciprocal rational map

Let $F=P/Q$ in lowest terms (in this subsection $P,Q$ are generic polynomials, not Item 1's constants), $d=\max(\deg P,\deg Q)$, and $P^*(c)=c^dP(1/c)$ the reversal. Reciprocity is $P^*/Q^*=Q/P$, i.e. $PP^*=QQ^*$; coprimality gives $P\mid Q^*$ and (assuming $\deg P=d$) $Q^*=\kappa P$, hence $P^*=\kappa Q$, and reversing once more forces $\kappa^2=1$. Therefore

$$\boxed{\;F(1/c)=1/F(c)\iff F=\pm\frac{P(c)}{P^*(c)}\ \text{ for some polynomial }P\;}$$

— two components ($\pm$), and the Three-Way "outer swap" $(A,B,1)\leftrightarrow(1,B,A)$ is precisely $P\leftrightarrow P^*$. In group language: reciprocal maps are exactly the rational maps commuting with the involution $\iota(c)=1/c$; they are closed under composition ($F_2\circ F_1$) and under products, so $F(F(c;A,B);A',B')$ is again reciprocal (checked). Item 1's decomposition $f=g\circ(\text{square})$ is one instance of this closure. The sign component $-P/P^*$ is *not* reachable inside the Three-Way family except on the degenerate lines $B=\pm(A+1)$ (checked); its plus and minus locks are interchanged.

### 6.3 Is $(c^4,c^2,1)$ special?

Within *polynomial* grammars, $u(1/c)u(c)=1$ forces $u=c^{2m}$ (a unit of $\mathbb Q[c,c^{-1}]$), and then $v$ must satisfy $c^{2m}v(1/c)=v(c)$: $v$ is any **palindromic polynomial of degree $2m$**, $v=\sum_{j=0}^m a_j(c^{m+j}+c^{m-j})$. For $m=2$ the admissible middle terms are the span of $c^2$, $c^3+c$, $c^4+1$; absorbing $c^4+1$ into the outer coefficients, the full degree-4 reciprocal family is $P/P^*$ with $P=Ac^4+B_1c^3+B_2c^2+B_1c+1$, three parameters. The Three-Way quartic is the slice $B_1=0$, and that slice is characterised uniquely: **it is the set of degree-4 reciprocal maps with $P(0)\ne0$ that are also even**, i.e. that carry the full Klein four-group $\{\pm c,\pm1/c\}$ of Item 1. So $(c^4,c^2,1)$ is one member of a large class (all $\pm P/P^*$), but within degree 4 it is the unique two-parameter member with the extra $c\mapsto-c$ symmetry — and evenness is what makes $F=G(c^2)$, what puts the $A$-independent core curve in $c^2$, and what makes the fixed-point quartic palindromic and hence solvable in $y=c+1/c$.

---

## 7. GENERALISATION BY POWER LADDER `[PROVEN]`

$F_m(c;A,B)=\dfrac{Ac^{2m}+Bc^m+1}{c^{2m}+Bc^m+A}=G(c^m;A,B)$: the same degree-2 map $G$ pre-composed with the $m$-th power. Checked for $m=1,\dots,6$:

| identity | survives? |
|---|---|
| reciprocity $F_m(1/c)=1/F_m(c)$ | all $m$ |
| $F_m=1\iff(A-1)(c^{2m}-1)=0$ | all $m$: plus lock $=$ the $2m$-th roots of unity, parameter-free |
| $F_m=-1\iff(A+1)(c^{2m}+1)+2Bc^m=0$, i.e. $c^m=u_\pm=-\beta\pm\sqrt{\beta^2-1}$ | all $m$: minus lock depends only on $\beta$ |
| evenness $F_m(-c)=F_m(c)$ | iff $m$ even; for odd $m$, $F_m(-c)=F_m(c;A,-B)$ |
| unit circle $\lvert c\rvert=1\Rightarrow\lvert F_m(c)\rvert=1$ | all $m$ ($\lvert c^m\rvert=1$ and $G$ preserves $S^1$) |
| fixed lock $c=1$, multiplier $F_m'(1)=m\lambda$ | all $m$; the pitchfork wall of Item 1C moves from $\lambda=\tfrac12$ to $\lambda=1/m$ |
| fixed-point reduction | $(c-1)\times$ palindromic degree-$2m$ quotient, degree $m$ in $y=c+1/c$; $m=1$: $c^2+(B-A+1)c+1$; $m=2$: the Item 1 quadratic |
| critical points | $c=0,\infty$ of order $m-1$ plus the $2m$ roots of $Bc^{2m}+2(A+1)c^m+B=0$, i.e. $c^m=-1/\beta\pm\sqrt{\beta^{-2}-1}$ |
| nesting | $F_{2m}(c)=F_m(c^2)$ |

**Is $m=2$ distinguished?** Yes, in one precise sense and one softer sense. Precise: $m=1$ is $G$ itself, a degree-2 map, which Item 1 showed is Möbius-conjugate to the one-parameter family $\lambda v/(v^2+1)$ — one of the two parameters is a conjugacy and dynamically inert. For $m\ge2$ the conjugacy that normalises $G$ does not commute with $c\mapsto c^m$, so both $\lambda$ and $n$ are effective: **$m=2$ is the smallest rung with two dynamically effective parameters**, and it is the smallest even rung (Klein symmetry, $y$-reduction of the fixed points to a *quadratic*). Softer: for $m\ge3$ the fixed-point reduction is a degree-$m$ polynomial in $y$, so the closed-form region classifications of Items 1C/1E have no analogue beyond radicals. Not launched here: any dynamics of $F_m$, $m\ge3$ (see Codex targets).

---

## 8. THREE-WAY LOCKS REVISITED `[PROVEN]`

$F=1/F\iff F^2=1\iff F=\pm1$.

**Plus lock, parameter-independent.** $F=1\iff(A-1)(c^4-1)=0$: for every $(A,B)$ with $A\ne1$ the lock set is $\{\pm1,\pm i\}$ — the 4th roots of unity, the fixed points of the Klein group's reflections. $B$ does not appear at all; $A$ appears only as the overall factor $(A-1)$ that switches the lock off when the map degenerates to $F\equiv1$. All four points are non-critical ($F'(\pm1)=\pm2\lambda$, $F'(\pm i)=\mp4i(A-1)/Q$) and all four map to the fixed point $1$.

**Minus lock, parameter-dependent through one number.** $F=-1\iff u^2+2\beta u+1=0$, $u=c^2$, $\beta=B/(A+1)$: $u_\pm=-\beta\pm\sqrt{\beta^2-1}$, $u_+u_-=1$. On the unit circle for $|\beta|<1$ ($PQ>0$, the Blaschke half of Item 1), on the real/imaginary axes for $|\beta|>1$ (folded regime). The whole $(A,B)$ dependence is through $\beta$, i.e. through Item 1's $n=(1+\beta)/(1-\beta)$: the minus lock is constant along every ray through $(A,B)=(-1,0)$.

**Duality with the critical points (new).** The critical points of $F$ solve $Bc^4+2(A+1)c^2+B=0$, i.e.

$$u^2+\tfrac{2}{\beta}u+1=0\qquad\text{versus the minus lock}\qquad u^2+2\beta u+1=0 .$$

Minus locks and critical points are the *same one-parameter family with $\beta\leftrightarrow1/\beta$*: when the locks sit on the circle the critical points sit on the axes and vice versa, and they coincide exactly at $\beta=\pm1$ (the degeneracy lines $B=\pm(A+1)$, where Item 1 found the critical collision). This is the one-line reason the two dynamical regimes of Item 1 are separated by those lines.

**Why plus is stiff and minus is sensitive — exact sensitivities.** For any $c$,

$$\frac{\partial F}{\partial A}=\frac{c^4-F}{D},\qquad \frac{\partial F}{\partial B}=\frac{c^2(1-F)}{D},\qquad D(c)=c^4+Bc^2+A\ \ (\text{the denominator; not Item 1's }Q).$$

At a plus lock ($c^4=1$, $F=1$) **both vanish identically**: $F(\pm1;A,B)=F(\pm i;A,B)=1$ for all $(A,B)$, so every parameter perturbation, of any size, leaves the lock value and the lock location exactly unchanged — `EXACT_ALGEBRAIC_LOCK`. At a minus lock ($F=-1$, numerator $=-D$, hence $D=\tfrac12(1-A)(u^2-1)$), the first-order response to $(\delta A,\delta B)$ is

$$\delta F=\frac{2(u^2+1)\,\delta A+4u\,\delta B}{(1-A)(u^2-1)}=\frac{4u}{(1-A)(u^2-1)}\big(\delta B-\beta\,\delta A\big),$$

using $u^2+1=-2\beta u$ on the lock. The gradient is $\propto(-B,\,A+1)$: the minus lock is insensitive *only* along the ray $\delta B/\delta A=\beta$ and responds with gain $4u/((1-A)(u^2-1))$ transverse to it (finite-difference check at $(\pi,e)$: $\beta=0.6563$, $u=-0.6563\pm0.7545i$ on the circle). If instead the perturbation is in $c$ at fixed parameters, the plus lock is *not* special: $F(1+\epsilon)=1+2\lambda\epsilon+O(\epsilon^2)$, an ordinary linear response with slope $2\lambda=4(A-1)/P$, which at $(\pi,e)$ is $1.249$.

**Reinterpretation of the old stiffness experiment.** Three readings are possible and the algebra separates them:

1. Parameters $(A,B)$ perturbed, $F$ evaluated at the old lock points: plus branch exactly rigid, minus branch shifts by the formula above — `EXACT_ALGEBRAIC_LOCK`, nothing perturbative about it.
2. $c$ perturbed near a lock, single evaluation: both branches respond linearly (slopes $2\lambda$ at $\pm1$; $F'(c_-)$ at the minus lock); no stiffness asymmetry exists at this level.
3. $c$ perturbed and the map *iterated*: the plus lock $c=1$ is a fixed point and is attracting iff $|2\lambda|<1$ (Items 1/1C); the minus lock points are not fixed — they go $c_-\mapsto-1\mapsto1$, so after two steps every minus-lock orbit lands on the plus lock and inherits its stability. Here stiffness is `NONTRIVIAL_PERTURBATIVE_STABILITY`, quantified by $|\lambda|<\tfrac12$, and at the default point $(\pi,e)$ the fixed point $1$ is in fact *repelling* ($2\lambda=1.249$).

Which reading the old paper used cannot be settled without the paper (not in the folder); the brief's wording — plus branch "structurally stiff", minus branch "parameter-sensitive" — matches reading 1, in which case the old result is `EXACT_ALGEBRAIC_LOCK`: it is the statement $\partial_{A,B}F(\pm1)\equiv0$.

---

## 9. $\pi$ / $e$ / $\varphi$ COMPARISON

Every identity of §1, §2, §6, §7, §8 is an identity in $c$, so it holds **verbatim** for $\pi$, $e$ and $\varphi$ alike: reciprocity, evenness, the log form, the $(X,Y,\mathsf m)$ form, the lock factorisations, the level conditions, the Möbius-in-$A$/$B$ structure. The architecture does not know what number sits in the slot. What differs is only what happens *after* substitution:

| | $\varphi$ | $\sqrt2,\sqrt3$ | $\pi$, $e$ |
|---|---|---|---|
| field of $F(c;A,B)$, $A,B\in\mathbb Q$ | $\mathbb Q(\sqrt5)$, degree 2 | $\mathbb Q$ | transcendental |
| extra structure | value has norm 1; Galois conjugation $=$ inversion; minimal polynomial $t^2-(2r+s)t+1$ | square root vanishes | none ($e$: unit point of the log coordinate, cosmetic) |
| reciprocal of the constant | $\varphi-1$, inside the same field | $\sqrt k/k$ | $1/\pi$, $1/e$ |
| bin | `SPECIAL_CONSTANT_EFFECT` | `ALGEBRAIC_SIMPLIFICATION` | `NO_STRUCTURE` |

So the answer to the brief's question is yes: the Three-Way architecture produces the *same* structural identities for all three, and $\varphi$ adds exactly one thing — a Galois symmetry ($\sigma\varphi=-1/\varphi$) that happens to coincide with the map's own reciprocal-plus-even symmetry, which is why its value inherits the norm-one property. $\pi$ and $e$ add nothing, and nothing about them is close to anything (§5.2).

---

## 10. NO PHYSICS

Nothing here is interpreted. The unit-circle statements are algebraic; "lock" is a level set; $\beta$ is a ratio of coefficients.

---

## STATUS

```text
PROVEN                          : §1 (all), §2 (table), §3, §4 (rational/algebraic cases), §5.1, §5.2 inequality, §6, §7, §8
DERIVED WITH STANDARD THEOREM   : §4 transcendence for algebraic parameters (Lindemann/Hermite), Galois statements in §3
NUMERICALLY CONSISTENT          : §5.2 values, §8 finite-difference sensitivities (both are consequences of proven formulas)
OPEN                            : arithmetic nature of the six {pi,e,phi} permutation values (needs pi,e independence);
                                  dynamics of F_m for m >= 3; the general non-even degree-4 reciprocal family P/P* with B1 != 0
NOT AVAILABLE                   : the original Three-Way papers (not in the folder or project docs); §8 gives all three readings
```

Check script: `three_way_item2a_checks.py` — A1–A70 exact (sympy), B1–B8 numeric (mpmath, 50 digits), all True.

---

## REQUIRED SUMMARY

```text
RECIPROCITY_FOR_CONSTANTS = F(1/c;A,B) = 1/F(c;A,B) for every c (coefficient-list reversal (A,B,1)<->(1,B,A)); in log
                            coordinates c=e^rho: F = (M+N)/(M-N), M=(A+1)cosh2rho+B even, N=(A-1)sinh2rho odd, so
                            (1/2)log F = artanh(N/M) is odd in log c. Exact symmetry group of the family: c->-c, c->ic (B->-B),
                            c->1/c (F->1/F), (A,B)->(1/A,B/A) (F->1/F), and the exchange (c;A,B)->(A^{1/4}; c^4, Bc^2/sqrtA)
                            (F->F). No permutation of the raw slots is an identity (F is Moebius in A and in B, quartic in c).
SPECIAL_LEVEL_CONDITIONS  = F=1: (A-1)(c^4-1)=0.  F=-1: (A+1)(c^4+1)+2Bc^2=0, i.e. u^2+2 beta u+1=0, beta=B/(A+1), u=c^2.
                            F=c: (c-1)[palindromic quartic], y^2+(1-A)y+(B-A-1)=0.  F=1/c: (c-1)[...], A y^2+(A-1)y+(B-A-1)=0
                            = fixed-point equation of (1/A,B/A).  F=A: Bc^2=-(A+1).  F=1/A: c^2=-B/(A+1).  F=c^4: c^4=1 or
                            c^4+Bc^2+1=0 (A-independent core).  F=B: (A-B)c^4+B(1-B)c^2+(1-AB)=0, irreducible.
                            In X=A, Y=c^4, m=Bc^2:  F=(XY+m+1)/(X+Y+m);  F=1 <=> (X-1)(Y-1)=0;  F=-1 <=> (X+1)(Y+1)+2m=0;
                            F=X <=> X+m+1=0;  F=Y <=> Y+m+1=0.  Everything expressible in (X,Y,m) factors; F=c, F=B do not.

PHI_REDUCTION   = F(phi;A,B) = (alpha+beta phi)/(gamma+delta phi), alpha=2A+B+1, beta=3A+B, gamma=A+B+2, delta=B+3;
                  N(alpha+beta phi) = N(gamma+delta phi) = A^2+3AB+B^2+7A+3B+1 =: N_phi;  F(phi) = r + s phi with
                  r=(alpha gamma+alpha delta-beta delta)/N_phi, s=(beta gamma-alpha delta)/N_phi, and r^2+rs-s^2 = 1:
                  F(phi) is a norm-one element of Q(sqrt5); Galois conjugation acts as inversion (phibar = -1/phi);
                  minimal polynomial t^2-(2r+s)t+1.  Example (3,5): 26/29 + 11/29 phi.
SQRT2_REDUCTION = F(sqrt2;A,B) = (4A+2B+1)/(A+2B+4)   -- rational; the root vanishes (evenness).
SQRT3_REDUCTION = F(sqrt3;A,B) = (9A+3B+1)/(A+3B+9)   -- rational.   (General: F(sqrt k) = G(k).)

PI_E_TRANSCENDENTAL_DIFFERENCE = For algebraic A!=1, B: F(pi;A,B), F(e;A,B) are transcendental (Lindemann, Hermite) and admit
                                 no reduction; every structural identity is identical to the phi case; phi's extra content is
                                 exactly the Galois symmetry sigma(phi)=-1/phi coinciding with the map's even+reciprocal
                                 symmetry. e is the unit point rho=1 of the log coordinate (cosmetic). pi: no structure.

PERMUTATION_IDENTITIES_FOUND = none among raw slot permutations. Exact non-permutation identities: the reciprocal group and the
                               A <-> c^4 exchange at fixed Bc^2 (F symmetric in X,Y).  All six {pi,e,phi} values distinct
                               (min separation 0.0564 at 50 digits); no near-rational or near-simple coincidence found.
PERMUTATION_COINCIDENCES_REQUIRING_SPECIAL_CONDITIONS =
                               F(c;A,B)=F(c;B,A) <=> (c^4-1)(A-B)(c^4+(A+B-1)c^2+1)=0;
                               F(c;A,B)=F(A;c,B) <=> (A-1)(c-1)(c-A) Sigma_1=0;  F(c;A,B)=F(B;A,c) <=> (A-1)(c-B) Sigma_2=0;
                               the other 12 pairs: irreducible up to trivial factors (A-1, B-1, c-1, A+-1, B+-1, c-A, c-B, A-B).

GENERAL_RECIPROCAL_GRAMMAR = For P=Au+Bv+1, Q=u+Bv+A (identity in A,B): u(1/c)u(c)=1 and v(1/c)=v(c)/u(c), i.e. log u odd
                             in log c and v^2/u reciprocal-invariant (v = sqrt(u)*k, k even in log c). Theorem: F(1/c)=1/F(c)
                             <=> F = +-P/P*, P*(c)=c^d P(1/c) (two components); reciprocal maps = centraliser of c->1/c,
                             closed under composition and products.  Polynomial case: u=c^{2m}, v any palindromic polynomial
                             of degree 2m; degree 4: P = A c^4 + B1 c^3 + B2 c^2 + B1 c + 1 (three parameters).
POWER_LADDER_GENERALIZATION = F_m = G(c^m).  Survive for all m: reciprocity, F=1 <=> c^{2m}=1, F=-1 <=> c^m = -beta +-
                              sqrt(beta^2-1), unit-circle invariance, fixed lock c=1 with multiplier m*lambda (pitchfork wall
                              lambda=1/m), F_{2m}(c)=F_m(c^2), critical points c^m = -1/beta +- sqrt(1/beta^2-1) plus 0,inf of
                              order m-1.  Evenness iff m even.  Fixed-point reduction: degree m in y=c+1/c.

ORIGINAL_M2_DISTINGUISHED = YES: (i) m=1 is the degree-2 map G, conjugate to the one-parameter family lambda v/(v^2+1) --
                            one parameter is dynamically inert; m=2 is the smallest rung on which both (lambda,n) are
                            effective; (ii) m=2 is the smallest even rung (Klein four-group, F=G(c^2), palindromic fixed-point
                            quartic, quadratic in y); (iii) within degree 4, (c^4,c^2,1) is the unique even slice of the
                            three-parameter reciprocal family P/P*.
THREE_WAY_PLUS_LOCK_EXACT_EXPLANATION = F-1 has numerator (A-1)(c^4-1): B is absent, A only as an on/off factor, so the lock
                            set {+-1,+-i} and the lock value are exactly parameter-independent; dF/dA = (c^4-F)/D and
                            dF/dB = c^2(1-F)/D (D = denominator) both vanish identically there. In (X,Y,m): the product of the two outer walls.
THREE_WAY_MINUS_LOCK_DEPENDENCE = single irreducible three-slot relation (X+1)(Y+1)+2m=0; depends on (A,B) only through
                            beta=B/(A+1) (constant on rays through (-1,0)); roots u+-=-beta+-sqrt(beta^2-1), on S^1 iff
                            |beta|<1; dual to the critical points (u^2+2u/beta+1=0) under beta<->1/beta; first-order response
                            dF = 4u(dB - beta dA)/((1-A)(u^2-1)).

OLD_STIFFNESS_EXPERIMENT_REINTERPRETATION = If the experiment perturbed (A,B): EXACT_ALGEBRAIC_LOCK (plus branch rigid to all
                            orders, minus branch moves with the gradient above). If it perturbed c without iterating: no
                            asymmetry (linear slopes 2 lambda and F'(c_-)). If it iterated: NONTRIVIAL_PERTURBATIVE_STABILITY
                            governed by |lambda|<1/2, with minus-lock orbits landing on the plus lock in two steps; at (pi,e)
                            the plus lock is repelling (2 lambda = 1.249). The brief's wording matches the first reading.

MOST_INTERESTING_NEW_IDENTITY = F = (XY+m+1)/(X+Y+m) with X=A, Y=c^4, m=Bc^2, symmetric in A <-> c^4, with
                            tanh((1/2)log F) = (X-1)(Y-1)/((X+1)(Y+1)+2m): the plus lock is the product of the two outer walls,
                            the minus lock and the critical points are the beta <-> 1/beta pair u^2+2 beta u+1 / u^2+2u/beta+1.
                            Runner-up: N(F(phi;A,B)) = 1 for all rational A,B.
MOST_IMPORTANT_OPEN_POINT = Whether the beta <-> 1/beta duality between minus locks and critical points has a dynamical
                            consequence beyond Item 1's regime split (e.g. an exact relation between lock preimages and the
                            critical orbits of Items 1F/1G), and whether the odd middle-term family P = Ac^4+B1c^3+B2c^2+B1c+1
                            keeps any of the Item 1C/1E closed forms.
CODEX_TARGETS_AFTER_ANALYSIS = (1) high-precision scan of F(c;A,B) over a grid of algebraic c of degree <=4 checking the degree
                            table of §4 and the norm-one conic for quadratic units; (2) numerical verification of the three
                            transposition hypersurfaces of §5.1 (sample points on c^4+(A+B-1)c^2+1=0 and confirm F(c;A,B)=
                            F(c;B,A)); (3) sensitivity map |dF/d(A,B)| on the minus-lock locus over the (lambda,n) plane and
                            its zero-direction field (-B, A+1); (4) power ladder m=3,4: locate the plus/minus locks and
                            critical points on the circle and confirm the pitchfork wall lambda=1/m; (5) no dynamics study.
```
