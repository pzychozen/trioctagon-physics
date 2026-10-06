# Three-Way map — Item 2B constant geometry survey

Completed in the playground only. This is a bounded substitution and lock-geometry calculation; no dynamics, network calls, or production imports.

The useful exact finding is a quadratic norm-one structure at c=phi with rational A,B. No new pi/e identity or reciprocal pairing of the six roles was found. Input inversion is an exact property of the formula, independent of the choice of constants.

## Scope, precision, and classification

F(c;A,B)=(A*c^4+B*c^2+1)/(c^4+B*c^2+A). All distinct ordered triples from pi, e, phi, sqrt2, sqrt3, 2, half=1/2, 3, sqrt5, ln2 were evaluated: **720 total = 210 primary + 510 involving optional controls**. Exactly 210 assignments contain only algebraic constants; each has an exact SymPy reduction and an independent 200-digit numerical check.

All F/G values and metrics were computed independently at 120 and 200 decimal digits; the largest absolute change across those runs was 7.46461e-121. JSON/NPZ retain 195 significant digits of the 200-digit results and 115 of the 120-digit values. Float64 arrays are conveniences only.

Every reported relation is classified as EXACT_BY_SYMBOLIC_CHECK, ALGEBRAIC_REDUCTION, RECIPROCAL_IDENTITY, HIGH_PRECISION_NEAR_EQUALITY, or NO_RELATION. A row's NO_RELATION means no extra constant-specific identity was established, not that its value has no mathematical properties. All finite positive substitutions have positive denominators and outputs; none can produce -1.

The operational near-equality threshold is absolute residual < 1e-6, after separating exact symbolic identities. This threshold is a reporting convention, not significance. Comparisons cover +/-1, c, 1/c; the ten constants and their inverses; all within-triple role pairs; and all 258,840 global F output pairs for equality and reciprocal products. G gets the same single-value metrics and all within-triple pairs, but no extra global pair search. PSLQ was not used; there are no PSLQ candidates.

The JSON includes all 3,600 within-triple comparison records per map (120 sets × 15 unordered pairs × two tests); non-near global F pairs are summarized by counts and nearest examples rather than serialized individually.

## Exact architecture

**RECIPROCAL_IDENTITY:** F(c)F(1/c)=1 wherever both sides are defined and nonzero, c!=0. Also F(c;1/A,B/A)=1/F(c;A,B), under the corresponding domain restrictions. The latter changes both coefficients; it is not a simple A/B or A/c role swap.

**EXACT_BY_SYMBOLIC_CHECK:**

```text
F(-c) = F(c)
F-1 = (A-1)(c^4-1)/(c^4+B*c^2+A)
F+1 = ((A+1)c^4+2B*c^2+A+1)/(c^4+B*c^2+A)
```

All 720 input-inversion checks passed; maximum numeric product residual 3.26605e-201. Across the finite assignment table there are exactly 56 reciprocal output pairs, all with the same A,B and c=2 versus c=1/2. None belongs to the same unordered three-constant set. There are zero equal F output pairs and zero exact hits on the target-constant list.

## Permutation matrices

All six role assignments are explicit below. P is a reciprocal partner **inside the same six-row block**; '-' means none. Every P entry has classification NO_RELATION; no pair of distinct rows in a block has equal outputs either. Each F value still obeys the external input-inversion identity. Distances below are absolute; each metric's classification is stored in JSON.

### {pi, e, phi}

| (A,B,c) | F | P | d(+1) | d(-1) | d(c) | d(1/c) |
|---|---:|:---:|---:|---:|---:|---:|
| (pi,e,phi) | 1.73263905189547 | - | 0.73263905 | 2.7326391 | 0.11460506 | 1.1146051 |
| (pi,phi,e) | 2.64695606498099 | - | 1.6469561 | 3.6469561 | 0.071325763 | 2.2790766 |
| (e,pi,phi) | 1.56520173145847 | - | 0.56520173 | 2.5652017 | 0.052832257 | 0.94716774 |
| (e,phi,pi) | 2.42689627636223 | - | 1.4268963 | 3.4268963 | 0.71469638 | 2.1085864 |
| (phi,pi,e) | 1.41704205108596 | - | 0.41704205 | 2.4170421 | 1.3012398 | 1.0491626 |
| (phi,e,pi) | 1.47343262068597 | - | 0.47343262 | 2.4734326 | 1.66816 | 1.1551227 |

Same assignments in the shuffled control:

| (A,B,c) | G | P | d(+1) | d(-1) | d(c) | d(1/c) | G(c)G(1/c)-1 |
|---|---:|:---:|---:|---:|---:|---:|---:|
| (pi,e,phi) | 1.66595777352231 | - | 0.66595777 | 2.6659578 | 0.047923785 | 1.0479238 | 0.023409774 |
| (pi,phi,e) | 2.32257140847459 | - | 1.3225714 | 3.3225714 | 0.39571042 | 1.954692 | 0.43816488 |
| (e,pi,phi) | 1.62785016950673 | - | 0.62785017 | 2.6278502 | 0.0098161808 | 1.0098162 | -0.022874292 |
| (e,phi,pi) | 2.23871612199924 | - | 1.2387161 | 3.2387161 | 0.90287653 | 1.9204062 | 0.4015757 |
| (phi,pi,e) | 1.61495488912376 | - | 0.61495489 | 2.6149549 | 1.1033269 | 1.2470754 | -0.30466944 |
| (phi,e,pi) | 1.59728520533459 | - | 0.59728521 | 2.5972852 | 1.5443074 | 1.2789753 | -0.28651731 |

### {sqrt2, sqrt3, phi}

| (A,B,c) | F | P | d(+1) | d(-1) | d(c) | d(1/c) |
|---|---:|:---:|---:|---:|---:|---:|
| (sqrt2,sqrt3,phi) | 1.18939861839703 | - | 0.18939862 | 2.1893986 | 0.42863537 | 0.57136463 |
| (sqrt2,phi,sqrt3) | 1.21703170155036 | - | 0.2170317 | 2.2170317 | 0.51501911 | 0.63968143 |
| (sqrt3,sqrt2,phi) | 1.34873752139831 | - | 0.34873752 | 2.3487375 | 0.26929647 | 0.73070353 |
| (sqrt3,phi,sqrt2) | 1.24488440389116 | - | 0.2448844 | 2.2448844 | 0.16932916 | 0.53777762 |
| (phi,sqrt2,sqrt3) | 1.33270844142949 | - | 0.33270844 | 2.3327084 | 0.39934237 | 0.75535817 |
| (phi,sqrt3,sqrt2) | 1.20414823639674 | - | 0.20414824 | 2.2041482 | 0.21006533 | 0.49704146 |

Same assignments in the shuffled control:

| (A,B,c) | G | P | d(+1) | d(-1) | d(c) | d(1/c) | G(c)G(1/c)-1 |
|---|---:|:---:|---:|---:|---:|---:|---:|
| (sqrt2,sqrt3,phi) | 1.23917427843915 | - | 0.23917428 | 2.2391743 | 0.37885971 | 0.62114029 | -0.042784084 |
| (sqrt2,phi,sqrt3) | 1.250415908625 | - | 0.25041591 | 2.2504159 | 0.4816349 | 0.67306564 | -0.036011304 |
| (sqrt3,sqrt2,phi) | 1.2945608801306 | - | 0.29456088 | 2.2945609 | 0.32347311 | 0.67652689 | 0.044696378 |
| (sqrt3,phi,sqrt2) | 1.22925616778904 | - | 0.22925617 | 2.2292562 | 0.18495739 | 0.52214939 | 0.0080354655 |
| (phi,sqrt2,sqrt3) | 1.2971271486197 | - | 0.29712715 | 2.2971271 | 0.43492366 | 0.71977688 | 0.037356562 |
| (phi,sqrt3,sqrt2) | 1.2194572610195 | - | 0.21945726 | 2.2194573 | 0.1947563 | 0.51235048 | -0.0079714115 |

### {2, half, sqrt2}

| (A,B,c) | F | P | d(+1) | d(-1) | d(c) | d(1/c) |
|---|---:|:---:|---:|---:|---:|---:|
| (2,half,sqrt2) | 1.42857142857143 | - | 0.42857143 | 2.4285714 | 0.014357866 | 0.72146465 |
| (2,sqrt2,half) | 0.611970495498946 | - | 0.3880295 | 1.6119705 | 0.1119705 | 1.3880295 |
| (half,2,sqrt2) | 0.823529411764706 | - | 0.17647059 | 1.8235294 | 0.59068415 | 0.11642263 |
| (half,sqrt2,2) | 0.661504294989356 | - | 0.33849571 | 1.6615043 | 1.3384957 | 0.16150429 |
| (sqrt2,2,half) | 0.803550083271254 | - | 0.19644992 | 1.8035501 | 0.30355008 | 1.1964499 |
| (sqrt2,half,2) | 1.3200337430942 | - | 0.32003374 | 2.3200337 | 0.67996626 | 0.82003374 |

Same assignments in the shuffled control:

| (A,B,c) | G | P | d(+1) | d(-1) | d(c) | d(1/c) | G(c)G(1/c)-1 |
|---|---:|:---:|---:|---:|---:|---:|---:|
| (2,half,sqrt2) | 1.17647058823529 | - | 0.17647059 | 2.1764706 | 0.23774297 | 0.46936381 | 0.17647059 |
| (2,sqrt2,half) | 0.747985655958283 | - | 0.25201434 | 1.7479857 | 0.24798566 | 1.2520143 | 0.1377402 |
| (half,2,sqrt2) | 1.0 | - | 0.0 | 2.0 | 0.41421356 | 0.29289322 | -0.15 |
| (half,sqrt2,2) | 0.754954827420823 | - | 0.24504517 | 1.7549548 | 1.2450452 | 0.25495483 | -0.34728404 |
| (sqrt2,2,half) | 0.657430979726107 | - | 0.34256902 | 1.657431 | 0.15743098 | 1.342569 | -0.12106472 |
| (sqrt2,half,2) | 1.15663607791059 | - | 0.15663608 | 2.1566361 | 0.84336392 | 0.65663608 | 0.53205998 |

The table metric G=1 at (A,B,c)=(half,2,sqrt2) is EXACT_BY_SYMBOLIC_CHECK. It is a new control-specific lock, not survival of reciprocal architecture. Complete control metric classifications are in JSON.

## Near equalities and negative results

**NO_RELATION:** no within-triple F permutation equality or reciprocal product lies within 1e-6 of its target. The closest comparisons across different triples are retained only as numerical controls:

| Comparison | Assignments | Absolute residual | Classification |
|---|---|---:|---|
| F equal output comparison | (sqrt2,e,3) vs (sqrt3,2,phi) | 5.32804479299752965e-7 | HIGH_PRECISION_NEAR_EQUALITY |

These are nonzero residuals stable at 120 and 200 digits, not exact-looking relations that improve with precision. With hundreds of values and hundreds of thousands of pair comparisons, small gaps are expected search outcomes. No inference about pi/e/phi follows.

For the visually tempting primary triple, F(phi;pi,e) differs from sqrt3 by 0.0005882443265901553273. Classification: NO_RELATION.

## Phi compared on the same footing

**ALGEBRAIC_REDUCTION:** phi^2=phi+1, phi^4=3phi+2, and

```text
F(phi;A,B)=((3A+B)phi+2A+B+1)/((3+B)phi+A+B+2)
H=3(A+1)+2B; K=A-1
F(phi;A,B)=(H+sqrt(5)K)/(H-sqrt(5)K)
(H^2-5K^2)(q^2+1)-2(H^2+5K^2)q=0, q=F(phi;A,B)
```

For rational A,B, the conjugate of phi is -1/phi. Evenness and input inversion therefore give conjugate(q)=1/q. For positive rational A,B with A!=1 this is a degree-two algebraic output of norm one. This explains the palindromic quadratic without a fitted relation.

For example F(phi;2,1/2)=(21+4sqrt5)/19, so **19q^2-42q+19=0**. The conjugate is its reciprocal, but that conjugate input is not another positive role permutation of {2,1/2,phi}.

| Varied constant | Role (other entries rational) | Exact expression | Minimal polynomial / status |
|---|---|---|---|
| phi | c | `4*sqrt(5)/19 + 21/19` | `19*q**2 - 42*q + 19` |
| phi | A | `367/682 + 285*sqrt(5)/682` | `341*q**2 - 367*q - 199` |
| phi | B | `60*sqrt(5)/1289 + 734/1289` | `1289*q**2 - 1468*q + 404` |
| pi | c | `(2 + pi**2 + 4*pi**4)/(4 + pi**2 + 2*pi**4)` | `nonconstant rational function of a transcendental` |
| pi | A | `(3 + 16*pi)/(pi + 18)` | `nonconstant rational function of a transcendental` |
| pi | B | `2*(9 + 4*pi)/(8*pi + 33)` | `nonconstant rational function of a transcendental` |
| e | c | `(2 + exp(2) + 4*exp(4))/(4 + exp(2) + 2*exp(4))` | `nonconstant rational function of a transcendental` |
| e | A | `(3 + 16*E)/(E + 18)` | `nonconstant rational function of a transcendental` |
| e | B | `2*(9 + 4*E)/(8*E + 33)` | `nonconstant rational function of a transcendental` |

The common role tests are (A,B,c)=(2,1/2,t), (t,1/2,2), and (1/2,t,2). Phi rows are ALGEBRAIC_REDUCTION. Pi/e rows are EXACT_BY_SYMBOLIC_CHECK for the displayed rational expressions; they do not assert an additional pi/e identity. In these single-transcendental, rational-background cases the output is itself transcendental: otherwise the nonconstant rational relation would make t algebraic. No such argument establishes algebraic independence for the mixed pi/e assignments.

Phi is not uniquely good at lowering algebraic degree. At c=sqrt(k), the even powers remove that square root entirely: F=(A*k^2+B*k+1)/(k^2+B*k+A). For rational A,B this is rational. For example F(sqrt2;2,1/2)=10/7. Both phi and these square-root controls simplify for known algebraic reasons.

The fixed-input -1 lock is B=-(A+1)(c^2+c^(-2))/2. At phi this is B=-3(A+1)/2; at sqrt2 it is B=-5(A+1)/4. For pi/e the same formula remains exact, with their unevaluated powers. These real positive c locks require negative B when A>0 and lie outside the positive survey. The +1 lock equation is equally simple for every coefficient choice; phi does not simplify c^4=1 further.

## What the shuffled denominator removes

G=(A*c^4+B*c^2+1)/(c^4+A*c^2+B). **EXACT_BY_SYMBOLIC_CHECK:**

```text
G(c)G(1/c)-1 = (A-B)(c^2-1)^2(c^4+c^2+1)
                   /[(c^4+A*c^2+B)(1+A*c^2+B*c^4)]
G-1=(c^2-1)((A-1)c^2+B-1)/(c^4+A*c^2+B)
G=-1: (A+1)c^4+(A+B)c^2+B+1=0
```

Because all assignments have A!=B, positive c!=1, and positive denominators, **0/720** retain input reciprocity. Absolute product defects range from 0.003854610359 to 2.105590999. The sign is the sign of A-B.

G retains evenness and the +1 roots c=+/-1. The original +/-i +1 roots are lost when A!=B (or can become poles); extra parameter-dependent +1 roots replace them. The -1 polynomial generally loses its palindromic coefficients and reciprocal root pairing. With distinct rational A,B, the phi conjugate still substitutes -1/phi, but its product with G(phi) is no longer one where both are defined. Low-degree algebraic reductions survive because they come from the constants, not from reciprocity. A/B/c permutation reciprocity was absent in F already, so it cannot be counted as a lost pattern.

The shuffled control also produces three exact target hits that F does not: **G(sqrt2;1/2,2)=1**, **G(2;1/2,3)=1**, and **G(phi;3,sqrt5)=phi** (all EXACT_BY_SYMBOLIC_CHECK). For the last one, its numerator reduces to 12phi+8 and denominator to 8phi+4, whose ratio is phi. Thus even a striking exact phi substitution is not, by itself, evidence for the reciprocal architecture; the conjugate-norm comparison is the discriminating test.

## Power ladder: m=1,...,5, no dynamics

All 20 sample evaluations pass input reciprocity at 200 digits; the five identities and lock factorizations also pass exact symbolic checks:

```text
F_m(c)F_m(1/c)=1
F_m-1=(A-1)(c^(2m)-1)/(c^(2m)+B*c^m+A)
F_m+1=((A+1)c^(2m)+2B*c^m+A+1)/(c^(2m)+B*c^m+A)
```

The +1 roots are the 2m-th roots of unity for A!=1, excluding poles. The -1 equation is quadratic in y=c^m. The samples are (pi,e,phi), (sqrt2,sqrt3,phi), (2,half,phi), (2,half,sqrt2). JSON/NPZ retain F_m, F_m-1, F_m+1, and reciprocal checks for every sample. The rational-background phi ladder makes the parity distinction visible:

| m | Exact F_m(phi;2,1/2) | Field norm | Minimal polynomial |
|---:|---|---|---|
| 1 | `2*sqrt(5)/15 + 1` | 41/45 | `45*q**2 - 90*q + 41` |
| 2 | `4*sqrt(5)/19 + 21/19` | 1 | `19*q**2 - 42*q + 19` |
| 3 | `16*sqrt(5)/57 + 65/57` | 155/171 | `171*q**2 - 390*q + 155` |
| 4 | `132*sqrt(5)/439 + 529/439` | 1 | `439*q**2 - 1058*q + 439` |
| 5 | `66*sqrt(5)/205 + 249/205` | 981/1025 | `1025*q**2 - 2490*q + 981` |

Classification: ALGEBRAIC_REDUCTION for the exact rows, RECIPROCAL_IDENTITY for every input-inversion check. With rational A,B, norm one survives for even m. For odd m, conjugation changes the sign of c^m, so conjugate(F_m(phi;A,B))=1/F_m(phi;A,-B); the norm need not be one. This does not break F_m(c)F_m(1/c)=1.

## +1 and -1 locks at (A,B)=(pi,e)

**EXACT_BY_SYMBOLIC_CHECK:** the +1 roots are 1,-1,i,-i, and do not move under independent perturbations of A or B, as long as the roots remain defined and A!=1. If A=1 the function is identically one where the original denominator is nonzero. This is an identity of lock locations, not parameter-independent slope or stiffness in an unspecified observable.

For -1, y=c^2 solves y^2+2r*y+1=0 with r=B/(A+1). At pi,e, 0<r<1, so all four roots lie on the unit circle. They have angles alpha, pi-alpha, pi+alpha, 2pi-alpha, where alpha=acos(-r)/2. There are no real -1 roots at this positive coefficient pair.

| Root | Baseline angle (radians) | Re(c) | Im(c) |
|---:|---:|---:|---:|
| 0 | 1.14337506012794759 | 0.414525438683143693 | 0.910037724868890959 |
| 1 | 1.99821759346184564 | -0.414525438683143693 | 0.910037724868890959 |
| 2 | 4.28496771371774083 | -0.414525438683143693 | -0.910037724868890959 |
| 3 | 5.13981024705163888 | 0.414525438683143693 | -0.910037724868890959 |

The historical reference is *Experimental Geometry of a Three-Way Reciprocal Construct: Numerical Evidence for Structural Stability*, January 19, 2026. Sections 3.1-3.5 specify the two parameter directions, scans, paired Monte Carlo design, and dual numerical backends. Section 3.2 delegates the actual Delta log S and Delta D formulas to accompanying code. No such code was found in the searched playground/Downloads code and text files, and the PDF has no accompanying-code link. :codex-file-citation{path="C:/Users/Notandi/Downloads/Three_way_test_model.pdf" purpose="source"}

**Historical protocol facts:** b_only uses (A0,B0+delta); antisym uses (A0+delta,B0-delta). Deterministic scans are described for delta=10^-k, k=1,...,1000. Monte Carlo uses typically R=4096 with paired Gaussian noise on both parameters, mean contrasts, 95% confidence intervals and a detectability score; section 4.3 gives sigma=1e-6. Section 3.5 names float64/mpmath but does not specify the precision-selection implementation.

The supplied code repeats the documented **parameter directions** for k=1,3,6,12,13,30,100,1000 and evaluates the explicitly defined root phase, complex displacement, and modulus. This is 16 bounded geometry checks, not a reconstruction of the missing historical observables, the entire original scan, or its Monte Carlo statistics. The special reference for this geometry comparison is the exact baseline (pi,e). Precision is max(200,k+120) digits, reaching 1120 at k=1000; at least 100 useful digits of displacement remain. Selected results:

| Protocol | k | +1 root motion | Minus alpha shift / delta | Minus maximum displacement |
|---|---:|---:|---:|---:|
| b_only | 1 | 0 (exact) | 0.16233636045950729 | 0.0162334577938 |
| antisym | 1 | 0 (exact) | -0.25331822114726748 | 0.0253311448093 |
| b_only | 6 | 0 (exact) | 0.16001551879798798 | 1.60015518798e-7 |
| antisym | 6 | 0 (exact) | -0.26503951378506509 | 2.65039513785e-7 |
| b_only | 13 | 0 (exact) | 0.16001549652334568 | 1.60015496523e-14 |
| antisym | 13 | 0 (exact) | -0.26503963888900785 | 2.65039638889e-14 |
| b_only | 1000 | 0 (exact) | 0.16001549652334345 | 1.60015496523e-1001 |
| antisym | 1000 | 0 (exact) | -0.26503963888902036 | 2.65039638889e-1001 |

In both paper directions the +1 roots stay exactly fixed. The -1 roots move by a nonzero amount proportional to delta to first order, all the way to the sampled delta=10^-1000. Their moduli remain exactly one in this regime; only numerical residuals depart from one. Consequently a pure unit-modulus drift diagnostic is zero on **both** lock families here, even though the -1 family moves in phase. This conclusion does not require reconstructing Delta D.

The following additional independent +/- A/B perturbations are **new diagnostics**, retained separately from the historical protocols:

| Additive perturbation | Max +1 root displacement | Shift of alpha | Max -1 root displacement |
|---|---:|---:|---:|
| A -1*1e-3 | 0 (exact) | 0.000105059109486669 | 0.000105059109438354 |
| B -1*1e-3 | 0 (exact) | -0.000159993230816729 | 0.000159993230646084 |
| A +1*1e-3 | 0 (exact) | -0.000104989201809081 | 0.000104989201760861 |
| B +1*1e-3 | 0 (exact) | 0.000160037780095666 | 0.000160037779924878 |
| A -1*1e-6 | 0 (exact) | 1.05024177319523e-7 | 1.05024177319523e-7 |
| B -1*1e-6 | 0 (exact) | -1.60015474248717e-7 | 1.60015474248717e-7 |
| A +1*1e-6 | 0 (exact) | -1.05024107411857e-7 | 1.05024107411857e-7 |
| B +1*1e-6 | 0 (exact) | 1.60015518797988e-7 | 1.60015518797988e-7 |

The angle derivatives are

```text
dalpha/dA = -B/[2(A+1)^2 sqrt(1-r^2)]
dalpha/dB =  1/[2(A+1) sqrt(1-r^2)]
```

At pi,e they are -0.105024142365676904 and 0.160015496523343452. Centered differences at steps 1e-3, 1e-6, and 1e-30 verify these derivatives; the smallest-step errors are below 1e-58. All sampled lock residuals are below 1e-190.

Even the -1 locations remain unchanged along paths with constant B/(A+1); independent A or B changes generally move them. The +1 locations remain unchanged for arbitrary allowed coefficient changes. For comparison F'(1)=4(A-1)/(A+B+1), which does vary with the coefficients. Thus zero +1 displacement alone cannot be called physical stiffness or immunity to perturbation.

**OLD_STIFFNESS_RESULT_INTERPRETATION = PLUS-BRANCH FIGURES IDENTIFIED; METRIC UNRECONSTRUCTED.** Figure 1's caption/title and Figure 4's image title explicitly identify the plotted deterministic stiffness as a plus-branch measurement. The reported roots near real +/-1 fit the +1 level; at pi,e the -1 roots listed above are complex and are not near real +/-1. The exact code's branch selection remains unverified. For the +1 level, root locations cannot explain a nonzero stiffness contrast because they do not move. A local slope or another stability proxy can change at those fixed roots. Without the metric formula, the observed nonzero Delta log S cannot be identified with a particular derivative or dismissed as root-motion error. What is established is the precise separation between fixed +1 locations, changing local geometry, and moving -1 phases. Historical detectability thresholds were not reproduced or treated as universal properties of F.

## Reproduction and data schema

```powershell
& 'C:\Users\Notandi\miniconda3\envs\torment\python.exe' -B .\three_way_item2b_constant_survey.py
```

The script regenerates only its three companion deliverables. It contains symbolic assertions, independently computed precision comparisons, exact algebraic-to-numerical checks, lock residual/sensitivity checks, and NPZ/JSON serialization checks. Input provenance and library versions are recorded in JSON, including a hash of the user-designated PDF when present. It reads no production roots and imports no existing experiment modules.

JSON `rows` use zero-based IDs in lexicographic permutation order relative to the declared constant-name list. Each row supplies A/B/c names, all six `role_permutation_ids` with their index permutations, and separate F/G values and metrics. Thus F(c;B,A) is `coefficient_swap_id`, and F(A;c,B) is `A_input_c_coefficient_id`. Input inversion is a separate evaluation even when its constant is absent from the set. `output_pairs`, `permutation_tests`, `algebraic_reductions`, `phi_comparison`, `power_ladder`, and `locks` carry their own relation labels. No pickled objects occur in NPZ.

## Required summary

```text
TOTAL_ASSIGNMENTS_TESTED = 720 (210 primary; 510 optional-control assignments), each for F and G
RECIPROCAL_IDENTITIES_CONFIRMED = F input inversion: symbolic + 720/720; 56 in-table c=2/half pairs; coefficient inversion also symbolic
EXACT_SPECIAL_RELATIONS_FOUND = phi rational-coefficient conjugate/reciprocal quadratic; 210 algebraic reductions; no target-constant equality hits for F
PHI_EXACT_SIMPLIFICATIONS = Norm-one quadratic at m=2; F(phi;2,half)=(21+4sqrt5)/19; phi^-2+phi^2=3
PI_E_EXACT_RELATIONS = Architecture identities only in the bounded search; no additional mixed pi/e identity established
PERMUTATION_NEAR_EQUALITIES = 0 within-triple; 1 cross-triple residual(s) <1e-6, explicitly nonzero
PSLQ_CANDIDATES_SURVIVING_PRECISION = 0; PSLQ not used
CONTROL_FAMILY_PATTERNS_LOST = Input reciprocity, +/-i plus locks, reciprocal minus-root pairing, phi norm one; algebraic reductions and +/-1 plus locks survive
POWER_LADDER_RECIPROCITY = YES, m=1..5 symbolic and 20/20 numerical; phi field norm one only for even m in this nonzero-B example
PLUS_LOCK_BEHAVIOR = Exactly parameter-independent c^4=1, excluding poles and A=1 degeneracy
MINUS_LOCK_BEHAVIOR = Depends only on B/(A+1); independent A/B perturbations move roots, constant-ratio paths do not
OLD_STIFFNESS_RESULT_INTERPRETATION = Paper's deterministic figures label the plus branch; exact metric/code absent. +1 locations fixed; local slopes can vary. Both documented parameter directions checked; no Delta log S/Delta D reconstruction
MOST_SURPRISING_CONSTANT_RELATION = Phi conjugation realizes input inversion (up to the harmless even-input sign), forcing norm-one outputs
MOST_USEFUL_CLAUDE_TARGET = Generalize the palindromic output polynomial for reciprocal quadratic units; separate power-ladder parity from input reciprocity
NUMEROLOGY_WARNINGS = Finite target list, many pair comparisons, arbitrary near threshold; no decimal coincidence promoted to an identity; mixed pi/e independence not assumed
```
