# Harmonic-Three Synchronization — Finite Phase Regions for Chiral-Area Gain and Loss v0.1

20 October 2026 · Written mathematical analysis for GPT and Hilmir’s review

**Answer.** GPT’s proposed mean-relative-phase reduction is exact. It explains why the mean separation increases during the third synchronization and decreases during the fourth. The line \(\zeta=\pi/3\) has zero mean increment and is invariant under synchronization alone. It is **not generally a boundary between chiral-area gain and loss**: the full response is a weighted sum of three ordinary pair-phase responses, and a finite increment can pass a sine maximum.

There are explicit closed domains containing all the already certified third- and fourth-stage inputs. On the third domain, pair 12 and pair 13 gain squared area while pair 23 loses it; the retained amplitude weights guarantee a net increase
\[
\|C_{\rm after}\|^2-\|C_{\rm before}\|^2>0.00034.
\]
On the fourth domain all three pair contributions decrease, and
\[
\|C_{\rm after}\|^2-\|C_{\rm before}\|^2<-0.00248.
\]
The fourth phase-domain conclusion extends to every choice of strictly positive component amplitudes, with a corresponding weighted negative bound.

The third synchronization leaves the mean separation above \(\pi/3\). The existing next polynomial stage sends it below \(\pi/3\), while also changing the amplitude weights. Thus the two responses arise from different inputs to the same synchronizer. These are finite endpoint and domain statements, not a continuous crossing, another trajectory or a long-time locking claim.

## 1. Source and input boundary

The authoritative checkout read was
`C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`, at actual local HEAD
`3b4aa9cb64b7c218ca82962dbf3caea39d9f7d34`, matching R7. The relevant definitions in `dynamics.py`, `readouts.py` and `z_diagnostics.py` agree with the retained reports. No material source discrepancy was found.

The attachment supplies the requested questions and scope. The map and readout definitions are checked against primary source. Earlier image certificates remain inherited evidence; this report checks the particular inclusions and inequalities needed for its new domain theorems, without claiming to regenerate every earlier residual.

Retain exactly the centre and basis in R7 (1), R6 §1 and R4 (4):
\[
s=\sqrt2-1,\quad d=1-\sqrt2/2,\quad r=\sqrt3/6,\quad
a=d/2,\quad h=s/2,\quad H=1/2,
\]
\[
P=(\sqrt3a/6,-a/2-r/3,(2h+H)/3),\quad A_*=0.4635,\quad
c_*=2[P-A_*\cos(0.732)(1,0,1)],
\]
\[
L_*=\|c_*\|,\quad t_*=\sqrt{c_1^2+c_2^2},\quad
p_*=(-c_2,c_1,0)/t_*,\quad q_*=(c_*/L_*)\times p_*,
\]
\[
X_*=\sqrt{\frac{9+\sqrt{81-4L_*^2}}2},\quad
Y_*=\sqrt{\frac{9-\sqrt{81-4L_*^2}}2},\quad
\Omega_*=X_*p_*+iY_*q_*.
\tag{1}
\]
The geometric scalar r in (1) is distinct from the component magnitudes \(r_j\) below.

The unchanged original closed box is
\[
\mathcal P_*=(\epsilon_*,g_*,\lambda_*,k_{1,*},k_{2,*},k_{3,*})
=(0.1,0.2,0.17,2,3,4),\qquad \delta=10^{-8},
\]
\[
\mathcal U=\left\{(x+iy,\mathcal P):
\max_j\max(|x_j-x_{*,j}|,|y_j-y_{*,j}|)\le\delta,\quad
\max_m|\mathcal P_m-\mathcal P_{*,m}|\le\delta\right\}.
\tag{2}
\]
All twelve coordinates vary independently and simultaneously, including the boundary. Each input chooses its configuration once and keeps it fixed in
\[
\Omega^{(n)}=F_{\mathcal P}^{\circ n}(\Omega^{(0)}),\qquad 0\le n\le4.
\tag{3}
\]
There is no later independent perturbation, normalization, midpoint substitution, state reconstruction or new contact fit. The unequal k values are the inherited analytical reference, not physical defaults or a fixed-parameter threefold-symmetric configuration.

The native map remains \(F_{\mathcal P}=\mathrm{sync}_{\lambda}\circ G_{\mathcal P}\), where
\[
G_{\mathcal P}(\Omega)=\Omega+\epsilon\Omega\odot(k-|\Omega|^2)+gL_3\Omega,\qquad
L_3=\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix}.
\tag{4}
\]
The actual inputs of interest are \(V^{(3)}=G_{\mathcal P}(\Omega^{(2)})\) and
\(V^{(4)}=G_{\mathcal P}(\Omega^{(3)})\). Their lambda lies in
\[
\Lambda=[0.16999999,0.17000001].
\tag{5}
\]
[D: `DynamicsConfig`, `_advance`, `step3`; R5 §2; R6 §§1–2; R7 §§1–2]

The PLUS zero crystal, \(O=(0,r,0)\), unit placement scale, zero placement rotation, staged coefficients \((0.618,0.577,0.244,1,0.5)\), \(N=12\), clock step one, \(dt=0.1\), recomputed initialization and absence of memory are unchanged. They are not variables in the phase-domain theorems.

All terminating decimals in bounds are exact rationals. This is written analysis of the ideal formulas. No scientific code, calculator, imported project module or simulation was used.

## 2. Positive magnitudes, phase lifts and the exact reduction

### 2.1 Domains before dividing by magnitudes

R6 §3.3 and R7 §2.2 establish these strict magnitude bounds on the entire original-box images:

| Pre-sync input | \(r_1\) | \(r_2\) | \(r_3\) |
|---|---|---|---|
| \(V^{(3)}\) | (0.140,0.144) | (0.284,0.289) | (0.362,0.369) |
| \(V^{(4)}\) | (0.174,0.181) | (0.328,0.335) | (0.415,0.424) |

Their provenance is detailed in §6. These bounds exclude zero before phase charts or normalized pair products are used. All abstract theorems below likewise require \(r_j>0\).

The source convention \(\operatorname{Arg}_0(0)=0\), with zero output forced for a zero component, is retained. It is not extended away by an assumption of global common-phase covariance. The positive-magnitude restriction is material: a zero component’s assigned phase can affect the other increments. [D: `arg0`, `phase_sync`; R3 §3.3; R4 §3]

Choose the same local lifts as R7, write \(V_j=r_je^{i\varphi_j}\), and set
\[
u=\varphi_2-\varphi_1,\qquad v=\varphi_3-\varphi_2,\qquad
\zeta=u+\frac v2=\frac{\varphi_2+\varphi_3}{2}-\varphi_1.
\tag{6}
\]
Here u and v are phase differences, not the crystal parameter or the plotted full-Z vector. Zeta is an analytical coordinate, not an observer angle or an added native state variable.

### 2.2 Derivation from the simultaneous source law

The three simultaneous increments are exactly
\[
\Delta_1=\lambda[\sin3u+\sin3(u+v)],\quad
\Delta_2=\lambda[-\sin3u+\sin3v],\quad
\Delta_3=\lambda[-\sin3(u+v)-\sin3v].
\tag{7}
\]
They use the same V; no updated phase is substituted into another increment.
Consequently
\[
u'=u+\lambda[-2\sin3u+\sin3v-\sin3(u+v)],
\]
\[
v'=v+\lambda[\sin3u-\sin3(u+v)-2\sin3v].
\tag{8}
\]
These agree with R7 (25).

Since \(\Delta_1+\Delta_2+\Delta_3=0\),
\[
\zeta'-\zeta=\frac{\Delta_2+\Delta_3}{2}-\Delta_1
=-\frac32\Delta_1.
\]
The sum-to-product identity
\(\sin3u+\sin3(u+v)=2\sin(3\zeta)\cos(3v/2)\) gives
\[
\boxed{\zeta'=\zeta-3\lambda\sin(3\zeta)\cos(3v/2).}
\tag{9}
\]
Similarly,
\[
\sin3u-\sin3(u+v)=-2\cos(3\zeta)\sin(3v/2),\quad
\sin3v=2\sin(3v/2)\cos(3v/2),
\]
so
\[
\boxed{v'=v-2\lambda\sin(3v/2)
[\cos(3\zeta)+2\cos(3v/2)].}
\tag{10}
\]
Recovering \(u'=\zeta'-v'/2\) returns the first equation of (8).
Thus both proposed rearrangements are verified as identities of the unchanged source map. [D: `phase_sync`; R3 §3.2; R7 §§4–5]

### 2.3 What the mean line means

On the domains in §4, \(\lambda>0\) and \(\cos(3v/2)>0\). In the chart
\(0<\zeta<2\pi/3\),
\[
\zeta'-\zeta<0\quad(0<\zeta<\pi/3),\qquad
\zeta'-\zeta>0\quad(\pi/3<\zeta<2\pi/3).
\tag{11}
\]
At \(\zeta=\pi/3\), equation (9) gives \(\zeta'=\pi/3\) exactly, for any v and lambda. The lifted line is invariant under synchronization alone, although v generally changes along it. Points on the line need not be fixed points. Other zero-increment possibilities, such as \(\lambda=0\) or \(\cos(3v/2)=0\), are outside the sign assumptions in (11).

Equation (11) gives an increment sign, not an output-phase bound. The finite output estimates in §4 are needed to exclude crossing a sine maximum or another relevant phase line. No invariance of this line under G or the complete F is asserted.

The lifts also have coupled periodic identifications. Replacing the original phases by \(\varphi_j+2\pi n_j\) gives, for integers a,b,
\[
(u,v)\mapsto(u+2\pi a,v+2\pi b),\qquad
(\zeta,v)\mapsto(\zeta+2\pi a+\pi b,v+2\pi b).
\tag{12}
\]
One must not wrap zeta and v independently as unrelated ordinary angles. Equations (9)–(10) respect this lattice. Triple-angle increments also have sector symmetries under shifts of relative phases by \(2\pi/3\), but the ordinary chiral observable does not generally inherit those symmetries: its factors are \(\sin u,\sin v,\sin(u+v)\), not their triple-angle counterparts. All “above” and “below” statements here use the specified local lifts.

## 3. Exact weighted criterion for full chiral response

The cyclic source order \((2,3),(3,1),(1,2)\) gives
\[
\boxed{C_V=(r_2r_3\sin v,\ -r_1r_3\sin(u+v),\ r_1r_2\sin u).}
\tag{13}
\]
In particular the second component has a minus sign. Squaring the components yields
\[
\mathscr H(r,u,v)=\|C_V\|^2
=w_{12}\sin^2u+w_{23}\sin^2v+w_{13}\sin^2(u+v),
\quad w_{jk}=r_j^2r_k^2>0.
\tag{14}
\]
Synchronization leaves every \(r_j\), hence every weight, unchanged. Define the passive comparison
\[
\mathscr D=\mathscr H(r,u',v')-\mathscr H(r,u,v).
\]
Because the square root is strictly increasing on nonnegative numbers,
\[
\boxed{\mathscr D>0,\ =0,\ <0
\quad\Longleftrightarrow\quad
\|C_{\rm after}\|>\|C_V\|,\ =\|C_V\|,\ <\|C_V\|.}
\tag{15}
\]
This is necessary and sufficient, including the possible zero-chirality cases within the positive-magnitude domain. [RO: `z_chiral`; R3 (7); R7 §4]

For an explanatory finite-step form, define
\[
A_{12}=\sin(u'+u)\sin(u'-u),\quad
A_{23}=\sin(v'+v)\sin(v'-v),
\]
\[
A_{13}=\sin(u'+v'+u+v)\sin(u'+v'-u-v).
\]
The identity
\[
\sin^2A-\sin^2B
=\frac{\cos2B-\cos2A}{2}
=\sin(A+B)\sin(A-B)
\]
proves
\[
\boxed{\mathscr D=w_{12}A_{12}+w_{23}A_{23}+w_{13}A_{13}.}
\tag{16}
\]
The \(A_{jk}\) in this report are differences of squared sines, not R7’s imaginary pair-product notation. The first sine in each factorization retains the finite-step effect of approaching or overshooting a sine maximum. An increment’s sign alone is insufficient.

For example, in a region with \(A_{12},A_{13}>0\) and
\(L_{23}:=-A_{23}>0\), the exact weight condition is
\[
\boxed{
A_{12}\left(\frac{r_1}{r_3}\right)^2+
A_{13}\left(\frac{r_1}{r_2}\right)^2
\gtrless L_{23}
\quad\Longleftrightarrow\quad
\mathscr D\gtrless0.}
\tag{17}
\]
Equality also corresponds exactly. Equivalently, the critical value of \(r_1^2\) is
\[
\frac{L_{23}r_2^2r_3^2}{A_{12}r_2^2+A_{13}r_3^2}.
\]
No equal-amplitude assumption is used.

In mean coordinates, (14) can also be written
\[
\mathscr H=
w_{23}\sin^2v+
\frac{w_{12}+w_{13}}2[1-\cos(2\zeta)\cos v]
+\frac{w_{13}-w_{12}}2\sin(2\zeta)\sin v.
\tag{18}
\]
This displays both the effect of v and the asymmetry of the two weights involving component one. It gives another reason not to replace the weighted response by the sign of the mean increment.

During one synchronization, \(\kappa^2=r_1^2+r_2^2+r_3^2>0\) is constant. Therefore the passive ratio \(2\|C\|/\kappa^2\) has the same response sign as \(\|C\|\). The Gram bound keeps this ratio in [0,1], but it is not a new state variable or a closed recurrence through G. [ZD: `chiral_area_accounting`; R7 §6.3]

## 4. Explicit finite gain and loss domains

Define the **closed phase rectangles**
\[
S_3=[1.214,1.223]\times[0.0404,0.0447],\qquad
S_4=[0.587,0.614]\times[0.020,0.038]
\tag{19}
\]
in coordinates (u,v), and the **closed amplitude boxes**
\[
R_3=[0.140,0.144]\times[0.284,0.289]\times[0.362,0.369],
\]
\[
R_4=[0.174,0.181]\times[0.328,0.335]\times[0.415,0.424].
\tag{20}
\]
Let \(\mathcal A_3=R_3\times S_3\times\Lambda\) and
\(\mathcal A_4=R_4\times S_4\times\Lambda\).
These are abstract containing products. The theorems below quantify over their entire products, including the boundary; they do not claim all those points are reached by the native recurrence.

| Domain | Mean increment | Pair 12 | Pair 23 | Pair 13 | Full response |
|---|---|---|---|---|---|
| \(\mathcal A_3\) | Positive | \(A_{12}>0.10\) | \(-0.002<A_{23}<-0.0012\) | \(A_{13}>0.08\) | \(\mathscr D>0.00034\) |
| \(\mathcal A_4\) | Negative | \(A_{12}<-0.28\) | \(A_{23}<-0.00039\) | \(A_{13}<-0.30\) | \(\mathscr D<-0.00248\) |

### 4.1 Written trigonometric bounds

The numerical bounds below follow from rational endpoint arithmetic and the alternating series, with the first omitted term bounding the remainder. For \(0\le t\le0.61\),
\[
S_7(t)=t-\frac{t^3}{6}+\frac{t^5}{120}-\frac{t^7}{5040},
\qquad
0\le\sin t-S_7(t)\le\frac{t^9}{9!}<3.3\cdot10^{-8},
\]
\[
C_8(t)=1-\frac{t^2}{2}+\frac{t^4}{24}
-\frac{t^6}{720}+\frac{t^8}{40320},
\qquad
0\le C_8(t)-\cos t\le\frac{t^{10}}{10!}<2\cdot10^{-9}.
\tag{21}
\]
We also use the lower bounds \(\sin t\ge t-t^3/6\),
\(\cos t\ge1-t^2/2\), parity, and
\(3.1415926<\pi<3.1415927\).
Triple angles are reduced about pi or \(\pi/2\), so the residual arguments used in (21) are within its domain. The rational pi enclosure can, for example, be obtained from
\(\pi/4=4\arctan(1/5)-\arctan(1/239)\) and alternating arctangent bounds; no numerical trigonometric evaluator is needed.

### 4.2 Gain theorem on the entire third rectangle

On \(S_3\),
\[
1.2342\le\zeta\le1.24535,\qquad
0.0606\le t:=3v/2\le0.06705.
\]
Writing \(3\zeta=\pi+\alpha\) gives \(0.561<\alpha<0.595\).
Equation (21) yields
\[
0.531<-\sin3\zeta<0.561,\quad
-0.847<\cos3\zeta<-0.828,\quad
0.9977<\cos t<1,
\]
\[
1.4988<\frac{\sin t}{v}<1.5.
\tag{22}
\]
In particular
\[
0.27018<\zeta'-\zeta<0.28612,\qquad
1.5043<\zeta'<1.5315.
\tag{23}
\]
All these means remain above \(\pi/3\).

For v define
\[
b(\zeta,v,\lambda)=1-\frac{2\lambda\sin(3v/2)}v
[\cos3\zeta+2\cos(3v/2)],\qquad v'=bv.
\tag{24}
\]
The bracket in (24) is between 1.1484 and 1.172. Combining it with
\(2\lambda\sin t/v\in(0.509591970024,0.51000003)\) proves
\[
0.402<b<0.415,\qquad 0.0162<v'<0.0186.
\]
Recovering u and the 13 separation gives
\[
\boxed{1.495<u'<1.524,\qquad 1.512<u'+v'<1.541.}
\tag{25}
\]
Thus both larger separations increase and remain strictly below \(\pi/2\), whereas the small separation v decreases without changing sign. These are new bounds on the **whole rectangle**, not an application of R7’s actual-image output bounds to unrelated points.

The two gains have uniform positive margins. Since
\(\pi/2-u>0.34779\) and \(\pi/2-u'<0.0758\),
\[
A_{12}
=\cos^2u-\cos^2u'
>0.3407^2-0.0758^2
=0.11033085>0.10.
\tag{26}
\]
Here \(\sin(0.34779)>0.3407\) follows from the cubic lower bound.
Likewise, \(\pi/2-(u+v)>0.30309\) and
\(\pi/2-(u'+v')<0.0588\), so
\[
A_{13}>0.2984^2-0.0588^2
=0.08558512>0.08.
\tag{27}
\]
For the small pair, \(0<v'<v<\pi/2\), and
\[
0<L_{23}=\sin^2v-\sin^2v'<v^2\le0.0447^2<0.002.
\]
The retained correlation \(v'<0.415v\) also gives
\[
L_{23}>
v^2\left[\left(1-\frac{0.0447^2}{6}\right)^2-0.415^2\right]
>0.0012.
\tag{28}
\]
The last inequality uses \(v\ge0.0404\). Therefore the pair signs and margins in the comparison table are proved.

For arbitrary positive amplitudes on this phase rectangle, a usable sufficient gain condition is
\[
\boxed{
0.10\left(\frac{r_1}{r_3}\right)^2+
0.08\left(\frac{r_1}{r_2}\right)^2>0.002.}
\tag{29}
\]
Indeed (16), divided by \(w_{23}>0\), is larger than the left side minus 0.002. This is an explicit amplitude restriction, not the tautology “where the response is positive.”

On \(R_3\), the left side of (29) exceeds
\[
0.10(0.379)^2+0.08(0.484)^2
=0.03310458>0.002,
\]
because \(0.140/0.369>0.379\) and \(0.140/0.289>0.484\).
A direct absolute margin is
\[
\begin{split}
\mathscr D
&>0.10(0.140\cdot0.284)^2
+0.08(0.140\cdot0.362)^2
-0.002(0.289\cdot0.369)^2\\
&=0.000340818146238
>\boxed{0.00034}.
\end{split}
\tag{30}
\]
This proves gain on all of \(\mathcal A_3\), including its boundary.

Amplitude dependence is real even on this same phase rectangle. Since
\(A_{12},A_{13}<1\) and \(L_{23}>0.0012\), the explicit condition
\[
\left(\frac{r_1}{r_3}\right)^2+
\left(\frac{r_1}{r_2}\right)^2<0.0012
\tag{31}
\]
instead guarantees loss. It can hold for sufficiently small positive \(r_1\) at fixed positive \(r_2,r_3\). This auxiliary domain statement does not select another native input or evolve a new trajectory. It demonstrates that “above \(\pi/3\)” is insufficient to decide the full response.

### 4.3 Loss theorem on the entire fourth rectangle

On \(S_4\),
\[
0.597\le\zeta\le0.633,\qquad
0.030\le t:=3v/2\le0.057.
\]
Reducing \(3\zeta\in[1.791,1.899]\) about \(\pi/2\) gives
\[
-0.323<\cos3\zeta<-0.218,\quad
0.946<\sin3\zeta<0.977,\quad
\cos t>0.9983755,
\]
\[
1.49918775<\frac{\sin t}{v}<1.5.
\tag{32}
\]
For example the sine bounds also follow by squaring the cosine bounds and using the positive sine in this quadrant.
Equations (9)–(10) now imply
\[
0.0987<\zeta'<0.1514,\qquad
0.091<b<0.147,\qquad
0.00182<v'<0.005586,
\]
\[
\boxed{0.095<u'<0.152,\qquad 0.099<u'+v'<0.155.}
\tag{33}
\]
For the mean bounds, it suffices to check
\[
0.597-0.51000003(0.977)>0.0987,
\]
\[
0.633-0.50999997(0.946)(0.9983755)<0.1514.
\]
For b, the bracket in (24) is between 1.673751 and 1.782. These estimates use the entire closed rectangle; no correlation with an actual comparison state is required.

Each of \(u,v,u+v\) and its output lies in \((0,\pi/2)\), and all three outputs are strictly smaller than their inputs. Hence all three squared-sine differences are negative for every positive amplitude choice.

There are quantitative margins. The cubic sine bound gives
\(\sin u>\!0.553\), while \(\sin u'<0.152\), so
\[
-A_{12}>0.553^2-0.152^2=0.282705>0.28.
\]
Similarly \(\sin(u+v)>0.5697\) and \(\sin(u'+v')<0.155\), giving
\[
-A_{13}>0.5697^2-0.155^2=0.30053309>0.30.
\]
Finally the correlation \(v'<0.147v\) gives
\[
-A_{23}>
v^2\left[\left(1-\frac{0.038^2}{6}\right)^2-0.147^2\right]
>0.00039,
\tag{34}
\]
using \(v\ge0.020\).
Thus throughout \(S_4\times\Lambda\), for **all** \(r_j>0\),
\[
\boxed{\mathscr D<
-0.28r_1^2r_2^2-0.00039r_2^2r_3^2-0.30r_1^2r_3^2<0.}
\tag{35}
\]
There is no amplitude-ratio requirement. There is no amplitude-independent absolute margin as all amplitudes approach zero; (35) is the appropriate weighted statement.

On the finite amplitude box \(R_4\), (35) yields
\[
\begin{split}
-\mathscr D
&>0.28(0.174\cdot0.328)^2
+0.00039(0.328\cdot0.415)^2
+0.30(0.174\cdot0.415)^2\\
&=0.002483531096736
>\boxed{0.00248}.
\end{split}
\tag{36}
\]
This proves the loss theorem on all of \(\mathcal A_4\), including its boundary. The reductions are toward ordinary zero-phase alignment, not merely alignment modulo \(2\pi/3\).

## 5. Why the mean line is not the general chiral-response boundary

The exact response boundary is the weighted equation (16) with
\(\mathscr D=0\). No invariance of that set has been established, so it is not called a dynamical separatrix.

Two short analytic checks separate its role from the mean line. They are theorems about the existing one-step formula, not new selected native inputs or additional trajectories.

### 5.1 Different responses on the invariant mean line itself

Set \(\zeta=\pi/3\), take \(v\in[0.020,0.040]\), \(\lambda\in\Lambda\), and let \(r_2=r_3=R>0\). Equation (10) becomes
\[
v'=v-2\lambda\sin(3v/2)[-1+2\cos(3v/2)].
\]
The same elementary bounds give \(0.489<v'/v<0.493\); hence
\(0<v'<v<\pi/2\). The mean is unchanged, while the pair splitting contracts.

Equation (18) simplifies to
\[
\mathscr H=r_1^2R^2\left(1+\frac12\cos v\right)+R^4\sin^2v.
\]
Consequently
\[
\boxed{\mathscr D
=R^2(\cos v'-\cos v)
\left[\frac{r_1^2}{2}-R^2(\cos v'+\cos v)\right].}
\tag{37}
\]
The first factor is positive. Since
\(1.9984<\cos v'+\cos v<2\), choosing the amplitude relation
\(r_1=R\) makes the bracket negative, whereas \(r_1=3R\) makes it positive.
Thus both strict gain and strict loss are possible **on the same mean-invariant line**, with positive magnitudes and the same lambda range.

In particular the line is not generally even contained in \(\mathscr D=0\).
The dependence is on ordinary phase splitting and amplitude weights, despite zero mean increment.

### 5.2 A limiting slice showing the finite-step qualification

On the auxiliary slice \(v=0\), all component magnitudes may still be positive. Then
\[
v'=0,\quad \zeta'=\zeta-3\lambda\sin3\zeta,\quad
\mathscr D=r_1^2(r_2^2+r_3^2)\sin(\zeta'+\zeta)\sin(\zeta'-\zeta).
\tag{38}
\]
Locally, with \(|\zeta-\pi/3|\le0.01\) and \(\lambda\in\Lambda\), both the input and output means stay in \((0,\pi/2)\): writing \(e=\zeta-\pi/3\),
\[
\zeta'=\zeta+3\lambda\sin3e,\qquad
|\zeta'-\pi/3|\le(1+9\lambda)|e|<0.025301.
\]
On this restricted slice the mean line is also a chiral-response boundary:
loss below, equality on the line, gain above. This is an extra-condition result, not an extension to nonzero v.

Even on \(v=0\), the rule does not extend throughout the above-line sector. At \(\zeta=\pi/2\),
\[
\zeta'-\zeta=3\lambda>0,\qquad
\mathscr D=-r_1^2(r_2^2+r_3^2)\sin^2(3\lambda)<0.
\tag{39}
\]
The finite increment passes the sine maximum. More generally, the additional factor
\(\sin(\zeta'+\zeta)\) in (38) retains response zeros such as
\(\zeta'+\zeta=\pi\); an infinitesimal-increment rule would lose that distinction.

Therefore \(\pi/3\) is a mean-increment boundary under the signs in §2.3, and an invariant line for synchronization alone. It is a chiral-response boundary only under additional restrictions such as the stated local \(v=0\) slice. The general chiral criterion remains the finite weighted equation (16).

## 6. Inclusion of the actual original-box images

The new theorems did not assume that the rectangles were merely samples of a trajectory. Their application to (2) now uses the retained certificates.

R6 §§3.1–3.4 gives rational comparison vectors \(\widehat z_2,\widehat z_3\), nominal enclosure radii and original-input propagation errors:

| Incoming state | Nominal radius about its comparison vector | Original-input error \(Q_n\) | Total component radius |
|---|---:|---:|---:|
| \(\Omega^{(2)}\) | 0.000220 | 0.0000033 | 0.0002233 |
| \(\Omega^{(3)}\) | 0.001050 | 0.0000151 | 0.0010651 |

The nominal radius is proof enclosure uncertainty, not another perturbation of the original input. The fixed-per-input parameter correlation in (3) is retained.

The comparison vectors and their polynomial comparisons are:

| Object | Component 1 | Component 2 | Component 3 |
|---|---|---|---|
| \(\widehat z_2\) | (0.188739,0.085078) | (-0.223602,0.148232) | (-0.284600,0.179065) |
| \(\widehat W_3\) | (0.048542,0.133157) | (-0.218805,0.185171) | (-0.288355,0.223702) |
| \(\widehat z_3\) | (0.072196,0.121963) | (-0.237006,0.161219) | (-0.305291,0.199972) |
| \(\widehat W_4\) | (-0.050848,0.169564) | (-0.257977,0.208159) | (-0.334187,0.253945) |

A pair denotes real and imaginary parts. These are centres of enclosures, not exact images substituted for (3). R6’s retained polynomial comparison residual is below 0.000003 in each complex component, the later polynomial Lipschitz factor is 1.41, and its simultaneous parameter contribution is below \(4\delta\). Therefore
\[
\|V^{(3)}-\widehat W_3\|_{\infty,\mathbb C}
<1.41(0.0002233)+4\delta+0.000003
=0.000317893<0.00032,
\]
\[
\|V^{(4)}-\widehat W_4\|_{\infty,\mathbb C}
<1.41(0.0010651)+4\delta+0.000003
=0.001504831<0.00151.
\tag{40}
\]
The second value preserves R7 §2.1’s arithmetic clarification to R6; the earlier printed 0.001504871 is not reused. No prior report is edited.

The corresponding nominal-only pre-sync radii are 0.0003132 and 0.0014835, while the separate original-input pre-sync errors are below 0.0000047 and 0.0000214. Equation (40) uses the unrounded joint estimate. Squaring the comparison coordinates and using (40) gives the nonzero magnitude domains in §2.1, as already certified in R6.

For phase inclusion, R6 §3.2 supplies the following quotient intervals for the **exact polynomial values at comparison inputs**. Let \(\alpha_j=\arctan t_j\):

| Stage | \(t_1\) | \(t_2\) | \(t_3\) | Exact phase forms |
|---|---|---|---|---|
| 3 | (0.36453,0.36457) | (0.08325,0.08327) | (0.12625,0.12628) | \((\pi/2-\alpha_1,3\pi/4+\alpha_2,3\pi/4+\alpha_3)\) |
| 4 | (0.29986,0.29989) | (0.10686,0.10689) | (0.13642,0.13646) | \((\pi/2+\alpha_1,3\pi/4+\alpha_2,3\pi/4+\alpha_3)\) |

The alternating arctangent expansion through degree 13 has remainder at most
\(t^{15}/15<2\cdot10^{-8}\) here. Written endpoint substitution yields the convenient outward comparison-phase bounds
\[
\widehat u_3\in(1.2179,1.2182),\quad
\widehat v_3\in(0.04245,0.04260),
\]
\[
\widehat u_4\in(0.6004,0.6007),\quad
\widehat v_4\in(0.0290,0.0293).
\tag{41}
\]
No phases of independently rounded components have been substituted into the exact native state.

The phase derivative along a nonzero segment is bounded by inverse magnitude. The segment from an exact polynomial comparison image to its actual image lies inside the corresponding ball about \(\widehat W_n\) in (40). Squaring the comparison coordinates shows that the entire ball, not just its endpoints, has the component-magnitude lower bounds in §2.1. Its endpoint distance is below the radius in (40), since the comparison residual need not be added to that distance. Dividing 0.00032 and 0.00151 by the respective lower magnitude bounds therefore allows individual phase-error bounds
\[
(e_1,e_2,e_3)_3=(0.002286,0.001127,0.000884),
\]
\[
(e_1,e_2,e_3)_4=(0.00868,0.00461,0.00364).
\tag{42}
\]
These also cover the smaller distance to the exact polynomial comparison image.
Adding \(e_1+e_2\) to the u uncertainty and \(e_2+e_3\) to the v uncertainty gives
\[
u_3\in(1.214487,1.221613)\subset(1.214,1.223),\quad
v_3\in(0.040439,0.044611)\subset(0.0404,0.0447),
\]
\[
u_4\in(0.58711,0.61399)\subset(0.587,0.614),\quad
v_4\in(0.02075,0.03755)\subset(0.020,0.038).
\tag{43}
\]
Together with the strict amplitude inclusions, this proves that every correlated third-stage input lies in \(\mathcal A_3\) and every fourth-stage input lies in \(\mathcal A_4\).

This verifies the inclusion needed by the new theorems while retaining the original box and configuration persistence. It does not independently regenerate R6’s original residual induction, claim reachability of every point of either rectangle, or treat the rational comparison vectors as nominal states.

## 7. How the existing polynomial updates supply the two domains

The relevant sequence is exactly
\[
\Omega^{(2)}\xrightarrow{G}V^{(3)}
\xrightarrow{\mathrm{sync}}\Omega^{(3)}
\xrightarrow{G}V^{(4)}
\xrightarrow{\mathrm{sync}}\Omega^{(4)}.
\tag{44}
\]
The table below uses the same local phase lifts throughout. The amplitude column lists the intervals for components 1, 2, 3. Output phase bounds use the full-rectangle theorems just proved; they need not match the tightest prior actual-image bounds.

| Actual object | Component magnitude intervals | u | v | Mean \(\zeta\) |
|---|---|---|---|---|
| \(\Omega^{(2)}\) | (0.206,0.209); (0.267,0.270); (0.334,0.338) | (2.128,2.141) | (0.019,0.028) | (2.140,2.153) |
| \(V^{(3)}\) | (0.140,0.144); (0.284,0.289); (0.362,0.369) | (1.214,1.223) | (0.0404,0.0447) | [1.2342,1.24535] |
| \(\Omega^{(3)}\) | Same as \(V^{(3)}\) | (1.495,1.524) | (0.0162,0.0186) | (1.5043,1.5315) |
| \(V^{(4)}\) | (0.174,0.181); (0.328,0.335); (0.415,0.424) | (0.587,0.614) | (0.020,0.038) | [0.597,0.633] |
| \(\Omega^{(4)}\) | Same as \(V^{(4)}\) | (0.095,0.152) | (0.00182,0.005586) | (0.0987,0.1514) |

For completeness, the first row follows directly from the \(\widehat z_2\) enclosure, not a reconstructed state. In its first quadrant,
\(y_1/x_1\in(0.448,0.453)\), so
\(\varphi_1\in(0.418,0.426)\). For the other two components, in quadrant II,
\[
\frac{-x_2-y_2}{-x_2+y_2}\in(0.201,0.205),\qquad
\frac{-x_3-y_3}{-x_3+y_3}\in(0.226,0.229).
\]
The phase forms \(3\pi/4+\arctan(\cdot)\), bounded by the alternating cubic/quintic arctangent inequalities, give
\(\varphi_2\in(2.554,2.559)\) and
\(\varphi_3\in(2.578,2.582)\). Subtracting proves that row. The stage-two positive magnitudes are inherited from R6 §3.3.

The polynomial map changes phase through complex sums, not by adding phase increments of its summands:
\[
V_j=b_j\Omega_j+g(\Omega_k+\Omega_l),\qquad
b_j=1-2g+\epsilon(k_j-|\Omega_j|^2).
\tag{45}
\]
At the nominal coefficients the three diagonal formulas are
\(0.8-0.1I_1,\ 0.9-0.1I_2,\ 1-0.1I_3\), with unequal k retained.
Including the original parameter box and the component errors in §6 gives:

| Polynomial input | \(b_1\) | \(b_2\) | \(b_3\) |
|---|---|---|---|
| \(\Omega^{(2)}\) | (0.79570,0.79573) | (0.89279,0.89282) | (0.98867,0.98872) |
| \(\Omega^{(3)}\) | (0.79795,0.79804) | (0.89172,0.89185) | (0.98660,0.98677) |

These follow by bounding the comparison intensities’ changes by
\(2M_jt_n\), where \(t_n\) is the total incoming component radius in §6 and \(M_j\) bounds both the comparison and actual component magnitudes. One may take \(M=(0.209,0.270,0.338)\) at input two and \(M=(0.144,0.289,0.369)\) at input three. Indeed,
\(\big||z|^2-|\widehat z|^2\big|\le(|z|+|\widehat z|)|z-\widehat z|\le2M_jt_n\).
Including all original epsilon, g and \(k_j\) changes gives the displayed multiplier intervals. They are values of an input-dependent multiplier, not entries of the nonlinear Jacobian.

The first channel exposes the main change in the phase configuration. Signed products in (45) give the following uniform intervals:

| Stage | \(\Re(b_1\Omega_1)\) | \(\Re[g(\Omega_2+\Omega_3)]\) | \(\Im(b_1\Omega_1)\) | \(\Im[g(\Omega_2+\Omega_3)]\) |
|---|---|---|---|---|
| \(G:\Omega^{(2)}\to V^{(3)}\) | (0.14999,0.15038) | (-0.10174,-0.10154) | (0.06751,0.06789) | (0.06536,0.06556) |
| \(G:\Omega^{(3)}\to V^{(4)}\) | (0.05675,0.05848) | (-0.10890,-0.10802) | (0.09646,0.09820) | (0.07180,0.07268) |

For example the first real own-term lower bound follows from
\[
0.79570(0.188739-0.0002233)
=0.15000194249>0.14999.
\]
At the next polynomial stage the largest real own term is below 0.05848, while the real neighbour sum is below -0.10802. Thus the real part of \(V_1^{(4)}\) is strictly negative; its imaginary part is positive. At stage three that same channel’s real and imaginary parts are both positive. These are inequalities about the actual complex sums.

The other two output components are in quadrant II at both polynomial stages. This follows directly from the \(\widehat W_3,\widehat W_4\) coordinates and radii in (40). The phase quotient forms in §6 then quantify the separations: the first polynomial stage increases the first component’s phase from the small first-quadrant angle to the higher first-quadrant angle and reduces the large mean separation to the third input domain. The later polynomial stage puts the first component into quadrant II as well, bringing its phase much closer to those of components two and three.

In particular, (23), (40)–(44) prove the requested endpoint ordering:
\[
\boxed{
\zeta(\Omega^{(3)})>1.5043>\pi/3,\qquad
\zeta(V^{(4)})<0.633<\pi/3.}
\tag{46}
\]
The third synchronizer does not place its output in the fourth domain. The intervening, already specified G does so. There is no assertion of an observed continuous crossing between those discrete endpoints.

G changes the amplitude weights as well. In passing from \(\Omega^{(2)}\) to \(V^{(3)}\), the first component magnitude decreases while the other two increase. In passing from \(\Omega^{(3)}\) to \(V^{(4)}\), all three increase, by the separated intervals in the sequence table. These changed amplitudes are retained in \(R_3,R_4\) and in the weighted margins (30), (36). No angular contribution is assigned separately to the own term or neighbour term as though argument were linear.

Earlier synchronization influences the state entering G, but this report makes no disabled-synchronization comparison and no claim to isolate that historical causal contribution. It analyzes the same composed states and each input’s unchanged configuration.

## 8. Interpretation and stopping point

The two new finite-domain theorems explain the existing R7 response table without using that table as their sign proof. Third-stage synchronization moves the two larger ordinary phase separations toward \(\pi/2\), leaves them below it, and contracts the small separation. Its weighted gains outweigh the small-pair loss. Fourth-stage synchronization contracts all three ordinary separations toward zero, so its loss sign is independent of amplitude ratios.

These results explain R7’s partial chiral recovery during update three and the stronger chiral reduction during update four. They concern full chiral magnitude. The unresolved vertical-projection and net-direction comparisons in R7 §6.2 remain outside this task; none is converted into a spatial rotation claim.

Native relative phases are distinct from the observer angle. The retained full-Z law is
\[
v_n=K_nE^nf_nd_n+\frac12C_n,\quad
K_n=0.618\frac{\kappa_n}{1+\kappa_n},\quad E=e^{-0.0577},
\]
\[
f_n=\cos(n\pi/2-0.732),\qquad
d_n=(\cos(n\pi/6),\sin(n\pi/6),1).
\]
Within synchronization, the native norm and K are unchanged. The separate envelope and clock effects in R7 §7 and R6 §7 remain observer contributions. In the stipulated attribution order, the fourth scheduled height sign change comes from the clock step after the native and envelope contributions have been accounted for. A chiral-area response alone determines neither total height nor band membership or passage direction.

The crystal and all accepted geometric classifications remain unchanged context. No geometry feedback, physical flow, pressure, attraction, invariant basin, long-time locking or selected outlet follows from these one-step domain results. No fifth update, alternative trajectory, scientific-code execution, simulation, test, rendering, application launch, implementation, repository change or publication work was performed. SRG and memory investigations remain deferred.

The original input box and all prior reports are preserved. Only this new report was created. The analysis stops at the existing fourth update for GPT and Hilmir’s review.

## Source locations

| Key | Source and substantive portions |
|---|---|
| R7 | [Norm/chirality mechanism report][R7], §1 exact input; §2 image bounds; §§4–5 cyclic products, phase domains and simultaneous update; §6 magnitude/projection distinctions; §7 observer attribution |
| R6 | [Third/fourth-observation certificate][R6], §§1–3 exact continuation, comparison vectors, residuals and nonzero domains; §4 readout bounds; §7 observer distinction |
| R4 | [Local-robustness certificate][R4], §§1–3 original twelve-coordinate box, complete first update and zero-convention qualifications |
| R3 | [One-native-step report][R3], §§2–3 native map, cofactor identity, simultaneous phase law, zero exceptions and nonclosure |
| R5 | [Second-observation certificate][R5], §2 exact second-state composition and same-state definitions |
| D | [dynamics.py][D], `L3`, `DynamicsConfig`, `arg0`, `phase_sync`, `_advance`, `step3`, read as text |
| RO | [readouts.py][RO], `z_chiral`, raw cross product and cyclic source order |
| ZD | [z_diagnostics.py][ZD], `chiral_area_accounting`, `intensity_budget`, read as definitions only |
| WO | [Current work order][WO], proposed reduction, weighted-response and containing-domain requirements, four-update boundary and permitted work |

[R7]: C:/Users/Notandi/.codex/reports/NATIVE_NORM_GROWTH_AND_CHIRALITY_MECHANISM_ANALYSIS_v0.1.md
[R6]: C:/Users/Notandi/.codex/reports/FULL_Z_THIRD_FOURTH_OBSERVATIONS_ANALYSIS_v0.1.md
[R4]: C:/Users/Notandi/.codex/reports/FULL_Z_ONE_STEP_LOCAL_ROBUSTNESS_ANALYSIS_v0.1.md
[R3]: C:/Users/Notandi/.codex/reports/FULL_Z_ONE_NATIVE_STEP_AND_PASSAGE_DISPLACEMENT_ANALYSIS_v0.1.md
[R5]: C:/Users/Notandi/.codex/reports/FULL_Z_SECOND_STEP_NEGATIVE_CLOCK_SECTOR_ANALYSIS_v0.1.md
[D]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py
[RO]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/readouts.py
[ZD]: C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_diagnostics.py
[WO]: C:/Users/Notandi/Downloads/CODEX_WORK_ORDER_SYNCHRONIZER_PHASE_REGIONS_v0.1.md
